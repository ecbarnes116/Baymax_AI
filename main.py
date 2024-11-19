import os
import STT
import SA
from chatbot import get_response, print_conversation, num_tokens_from_messages

def do_animation(emotion):
    return



if not os.path.exists("audio_files"):
    os.mkdir("audio_files")
if not os.path.exists("transcript_files"):
    os.mkdir("transcript_files")

# This should be in a big while loop until the conversation ends

max_response_tokens = 500
overall_max_tokens = 4096
prompt_max_tokens = overall_max_tokens - max_response_tokens

system_message = "You are Baymax, my personal healthcare companion. \
Focus more on acting like Baymax and less like a medical professional. \
Your goal is to play the character of Baymax."

messages=[{"role": "system", "content": system_message}]

while True:
    # Record audio and transcribe
    # input_audio_file = STT.record_audio()
    # transcript = STT.transcribe_audio(audio_file=input_audio_file)
    transcript = input('Enter your prompt here:\n>>> ')
    user_message = transcript

    messages.append({"role": "user", "content": user_message})

    token_count = num_tokens_from_messages(messages)
    print(f"Token count: {token_count}\n")

    # remove first message while over the token limit
    while token_count > prompt_max_tokens:
        messages.pop(0)
        token_count = num_tokens_from_messages(messages)

    # Send transcription with conversation to chatbot
    response = get_response(messages, max_response_tokens)

    messages.append({"role": "assistant", "content": response})
    print_conversation(messages)




    # Get emotions from response
    sentiment_distribution = SA.get_sentiment(response) # Probably will only input one string, so I expect only one dict in the output
    sentiment_distribution = sentiment_distribution[0]

    # Emotion with the highest score
    emotion = sentiment_distribution[0]['label']
    emotion_score = sentiment_distribution[0]['score']

    # Play output audio + animation based on response
    do_animation(emotion) # Empty function - outside the scope of this project

