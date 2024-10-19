import assemblyai as aai
import config
from pvrecorder import PvRecorder
import wave
import struct
import datetime

for index, device in enumerate(PvRecorder.get_audio_devices()):
    print(f"[{index}] {device}")

def STT(audio_file):
    aai.settings.api_key = config.assemblyai_key
    transcriber = aai.Transcriber()

    # transcript = transcriber.transcribe("https://assembly.ai/news.mp4")
    transcript = transcriber.transcribe("./my-local-audio-file.wav")

    print(transcript.text)

    return transcript.text



def record_audio():
    date_time = datetime.now().strftime("%Y-%m-%d %H;%M;%S")
    path = f"audio_files/{date_time}.wav"

    recorder = PvRecorder(device_index=-1, frame_length=512)
    audio = []

    try:
        recorder.start()

        while True:
            frame = recorder.read()
            audio.extend(frame)
    except KeyboardInterrupt:
        recorder.stop()
        with wave.open(path, 'w') as f:
            f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
            f.writeframes(struct.pack("h" * len(audio), *audio))
    finally:
        recorder.delete()


