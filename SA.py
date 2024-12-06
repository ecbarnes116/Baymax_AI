from transformers import pipeline

# Sentiment Analysis
# https://huggingface.co/SamLowe/roberta-base-go_emotions?text=I+am+not+having+a+great+day.

def get_sentiment(text):
    classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None, device=0)

    # produces a list of dicts for each of the labels
    model_outputs = classifier(text)

    print(model_outputs[0][0])
    print()

    return model_outputs

# with open("baymax_quotes.txt", "r") as f:
#     scores = []
#     quotes = f.readlines()

# for quote in quotes:
#     scores.append(get_sentiment(quote))

# with open("emotion_scores.txt", "w") as f:
#     for score in scores:
#         f.write(str(score) + '\n')

# print(scores)