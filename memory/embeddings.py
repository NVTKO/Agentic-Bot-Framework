from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # OpenAI setup

def get_embedding(text):
    return client.embeddings.create(
        model="text-embedding-ada-002",
        input=text
    ).data[0].embedding                              # Return vector