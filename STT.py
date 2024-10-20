import assemblyai as aai
import config
from pvrecorder import PvRecorder
import wave
import struct
from datetime import datetime

aai.settings.api_key = config.ASSEMBLYAI_KEY

def record_audio():
    date_time = datetime.now().strftime("%Y-%m-%d_%H;%M;%S")

    audio_file = date_time
    audio_file_path = f"audio_files/{audio_file}.wav"

    recorder = PvRecorder(device_index=-1, frame_length=512)
    audio = []

    try:
        print("Sarting recoring...")
        recorder.start()

        while True:
            frame = recorder.read()
            audio.extend(frame)

    except KeyboardInterrupt:
        recorder.stop()
        print("Recording ended")

        with wave.open(audio_file_path, 'w') as f:
            f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
            f.writeframes(struct.pack("h" * len(audio), *audio))

    finally:
        recorder.delete()
    
    return audio_file


def transcribe_audio(audio_file, save=True):
    transcriber = aai.Transcriber()

    audio_file_path = f"audio_files/{audio_file}.wav"

    transcript = transcriber.transcribe(audio_file_path)

    print(transcript.text)

    if save:
        transcript_path = f"transcript_files/{audio_file}.txt"

        with open(transcript_path, 'w') as f:
            f.write(transcript.text)

    return transcript.text

