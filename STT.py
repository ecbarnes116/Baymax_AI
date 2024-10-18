# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)

import assemblyai as aai

aai.settings.api_key = "0194f45e04ad4c7f8b0cde69f1e23ae0"
transcriber = aai.Transcriber()

transcript = transcriber.transcribe("https://assembly.ai/news.mp4")
# transcript = transcriber.transcribe("./my-local-audio-file.wav")

print(transcript.text)

