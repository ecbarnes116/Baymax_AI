from transformers import pipeline

# Sentiment Analysis
# https://huggingface.co/SamLowe/roberta-base-go_emotions?text=I+am+not+having+a+great+day.

def get_sentiment(text):
    classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None, device=0)

    # produces a list of dicts for each of the labels
    model_outputs = classifier(text)

    print(model_outputs[0][0])
    print(model_outputs[0][1])
    print(model_outputs[0][2])
    print()

    return model_outputs

