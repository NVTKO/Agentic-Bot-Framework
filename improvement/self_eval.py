import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def evaluate_response(prompt, response):
    feedback_prompt = f"""You are an AI critic. Evaluate the quality, accuracy, and helpfulness of this response:\nPrompt: {prompt}\nResponse: {response}\nGive suggestions for improvement."""

    result = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful AI trainer."},
            {"role": "user", "content": feedback_prompt}
        ]
    )
    feedback = result.choices[0].message.content
    print("[Self-Eval]", feedback)
    return feedback