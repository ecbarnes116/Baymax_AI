from openai import OpenAI
import tiktoken
from sentence_transformers import SentenceTransformer, util
import config

# Chatbot
# https://github.com/Azure/openai-samples/blob/main/Basic_Samples/Chat/chatGPT_managing_conversation.ipynb

client = OpenAI(api_key=config.OPENAI_KEY)
chatgpt_model_name = 'gpt-4o' # maybe use a fine-tuned model instead



def get_response(messages, max_response_tokens):
    response = client.chat.completions.create(
        model=chatgpt_model_name,
        messages=messages,
        max_tokens=max_response_tokens,
    )

    return response.choices[0].message.content



# Defining a function to print out the conversation in a readable format
def print_conversation(messages):
    for message in messages:
        print(f"[{message['role'].upper()}]")
        print(message['content'])
        print()



def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0301"):
    encoding = tiktoken.encoding_for_model(model)
    num_tokens = 0

    for message in messages:
        num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
        
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))

            if key == "name":  # if there's a name, the role is omitted
                num_tokens += -1  # role is always required and always 1 token
                
    num_tokens += 2  # every reply is primed with <im_start>assistant

    return num_tokens



def check_phrase(user_input):
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    target_phrase = "I am satisfied with my care"
    embeddings = model.encode([user_input, target_phrase])
    similarity = util.cos_sim(embeddings[0], embeddings[1]).item()

    return similarity > 0.90

