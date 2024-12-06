import evaluate
import matplotlib.pyplot as plt
import pandas as pd
# from semscore import EmbeddingModelWrapper


# Get all Baymax lines from movie transcript
def get_baymax_lines():
    quotes = []

    with open('movie_transcript.txt', 'r') as f:
        lines = f.readlines()

        matches = ["*Baymax: ", "*'''Baymax''': "]

        for line in lines:
            for match in matches:
                if line.startswith(match):
                    quote = line.split(match,1)[1]
                    quote = quote.replace("\xc2\xa0", " ")   # delete <0xa0> (non-breaking spaces)
                    quotes.append(quote)
    
    with open('baymax_quotes.txt', 'w') as f:
        f.writelines(quotes)


# Not the best metric to be used - used for checking translation with n-gram overlap
def get_BLEU_score(prediction):
    # Load the BLEU metric
    bleu = evaluate.load("bleu")

    with open('baymax_quotes.txt', 'r') as f:
        references = [f.readlines()]
    
    # Compute BLEU score
    results = bleu.compute(predictions=[prediction], references=references) # [[ref] for ref in references]

    print(f"BLEU Score: {results['bleu']}")
    return results['bleu']


def get_cosine_similarity(response):
    em = EmbeddingModelWrapper()

    # Maybe append the response to the references and then take the average
    # of the similarities between the response and all the references
    words = ["lemon", "orange", "car", "money"]
    embds = em.get_embeddings(words)

    similarities = em.get_similarities(embds)
    return


def plot_emotions(scores):
    with open("emotion_scores.txt", "r") as f:
        emotions = f.readlines()


def plot_emotion_histogram(filename, neutral=1):
    # Read the file
    emotions = []
    
    # Read the file line by line
    with open(filename, 'r') as file:
        for line in file:
            # Parse the dictionary-like string
            try:
                # Remove whitespace and convert to dictionary
                emotion_dict = eval(line.strip())
                
                # Only add non-neutral emotions
                if neutral==0:
                    if emotion_dict['label'].lower() != 'neutral':
                        emotions.append(emotion_dict['label'])
                else:
                    emotions.append(emotion_dict['label'])
            except (SyntaxError, KeyError):
                print(f"Skipping invalid line: {line.strip()}")
    
    # Create a histogram
    plt.figure(figsize=(10, 6))
    emotion_counts = pd.Series(emotions).value_counts()
    emotion_counts.plot(kind='bar')
    
    plt.title('Emotion Distribution')
    plt.xlabel('Emotion')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the plot
    if neutral == 0:
        plt.savefig("C:\\Users\\Ethan\\Documents\\TAMU_Fall_2024\\Baymax_AI\\emotions_histogram_NO_NEUTRAL.png")
    else:
        plt.savefig("C:\\Users\\Ethan\\Documents\\TAMU_Fall_2024\\Baymax_AI\\emotions_histogram.png")




# plot_emotion_histogram("emotion_scores.txt", neutral=1)
# plot_emotion_histogram("emotion_scores.txt", neutral=0)