from pydub import AudioSegment
import os

# Convert mp3 files to wav files for voice model training

input_dir = "baymax_old_audio"
output_dir = "baymax_new_audio"

for root, _, files in os.walk(input_dir):
            for file in files:
                if file.endswith(".mp3"):
                    mp3_path = os.path.join(root, file)

                    base = os.path.splitext(file)[0]
                    wav_path = os.path.join(output_dir, base) + ".wav"

                    sound = AudioSegment.from_mp3(mp3_path)
                    sound.export(wav_path, format="wav")

