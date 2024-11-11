from transformers import pipeline
import pdb

# Sentiment Analysis

def get_sentiment(text):
    classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

    sentences = ["I am not having a great day"]

    model_outputs = classifier(sentences)

    print(sentences)
    print(model_outputs[0])
    # produces a list of dicts for each of the labels

    pdb.set_trace()

    return model_outputs

sentiment = get_sentiment('')
