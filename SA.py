from transformers import pipeline
import pdb

# Sentiment Analysis

def get_sentiment(text):
    classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None, device=0)

    # produces a list of dicts for each of the labels
    model_outputs = classifier(text)

    # print(model_outputs[0])

    return model_outputs

