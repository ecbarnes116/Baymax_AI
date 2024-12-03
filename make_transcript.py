import assemblyai as aai
import config
import os

input_dir = "baymax_new_audio"

aai.settings.api_key = config.ASSEMBLYAI_KEY

contents = []

for root, _, files in os.walk(input_dir):
            for file in files:
                if file.endswith(".wav"):
                    transcriber = aai.Transcriber()

                    audio_file_path = os.path.join(root, file)
                    transcript = transcriber.transcribe(audio_file_path)

                    print(file + '|' + transcript.text)
                    contents.append(file + '|' + transcript.text + '\n')

with open("transcript.txt", "w") as f:
    f.writelines(contents)
    # f.writelines(file + '|' + transcript.text)
    # print(transcript.text)

# with open("transcript.txt", "w") as f:
#     for line in contents:
#         f.write(contents + "\n")

