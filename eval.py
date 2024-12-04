import evaluate


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
    from semscore import EmbeddingModelWrapper
    em = EmbeddingModelWrapper()

    # Maybe append the response to the references and then take the average
    # of the similarities between the response and all the references
    words = ["lemon", "orange", "car", "money"]
    embds = em.get_embeddings(words)

    similarities = em.get_similarities(embds)
    return

