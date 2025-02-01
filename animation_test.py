import json
import time
import requests

def play_animation(emotion_name):
    port=59224
    base_url = f'http://localhost:{port}/PlaybackState/'

    # get emotion params (animation_number, wait_time)
    # params = load_emotion_params(emotion_name)
    params = emotion_params.get(emotion_name)

    animation_number = params['animation_number']
    wait_time = params['wait_time']

    try:
        request_params = {
            'selectedAnimationIndex': animation_number,
            'playbackTimeInMS': 2,
            'isPlaying': True
        }

        response = requests.put(base_url, json=request_params)
        response.raise_for_status()

        time.sleep(wait_time)
        
    except requests.exceptions.RequestException as e:
        print(f"Error triggering animation: {e}")
    
    print("done playing animation")



# def load_emotion_params(emotion_name):
#     # Extract a specific emotion by name
#     for emotion in emotion_params:
#         print(f'emotion: {emotion}')
#         print(f'type: {type(emotion)}')
#         print()

#         if emotion.lower() == emotion_name.lower():
#             return emotion.get()


# Load emotion params at beginning to be accessed later
# Need to restart main when this file is updated
with open("emotion_params.json", "r") as file:
    emotion_params = json.load(file)


play_animation('head roll')

