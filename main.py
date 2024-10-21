import os
import STT
import chatbot

if not os.path.exists("audio_files"):
    os.mkdir("audio_files")
if not os.path.exists("transcript_files"):
    os.mkdir("transcript_files")

# This should be in a big while loop until the conversation ends

# Record audio and transcribe
input_audio_file = STT.record_audio()
transcript = STT.transcribe_audio(audio_file=input_audio_file)

# Send transcription to chatbot
response, conversation = chatbot.get_response(transcript)

# Need to do some weird stuff to format the response into the
# from of a continuing conversation

# Get emotions from response


# Play output audio + animation based on response

