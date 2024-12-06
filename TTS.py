from pyht import Client
from pyht.client import TTSOptions
import wave
import config
# import simpleaudio as sa


# TODO:
def play_speech(speech_file):
     return


def save_audio_wave(audio_chunks, output_file, channels=1, sample_width=2, frame_rate=23000):
    with wave.open(output_file, 'wb') as wf:
        # Set parameters: channels, sample width (bytes), frame rate, and no. of frames
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(frame_rate)
        
        # Write each chunk to the file
        for chunk in audio_chunks:
            wf.writeframes(chunk)


def get_TTS(input_text, file_name):
	client = Client(
	user_id=config.PLAYHT_USER_ID,
	api_key=config.PLAYHT_KEY,
	)
    
	output_file = f"TTS_output/{file_name}.wav"


	baymax_voice = "s3://voice-cloning-zero-shot/070256ca-4825-499a-846a-beeab92d9dfc/original/manifest.json"
	# default_voice = "s3://voice-cloning-zero-shot/d82d246c-148b-457f-9668-37b789520891/adolfosaad/manifest.json"

	# input_text = "I will scan you now. ...... Scan complete. You have a slight epidermal abrasion on your forearm. I suggest an anti-bacterial spray."
     
	options = TTSOptions(voice=baymax_voice)
	audio_chunks = client.tts(text=input_text, options=options)
	save_audio_wave(audio_chunks, output_file=output_file)
	play_speech(output_file)


get_TTS("Hello", file_name="output_voice")

