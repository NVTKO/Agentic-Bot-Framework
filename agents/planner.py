import openai
import os
from dotenv import load_dotenv
load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # OpenAI setup

def plan_task(goal):
    plan_prompt = f"Break down the following user goal into a clear multi-step plan:\n\nGoal: {goal}\n\nSteps:"
    result = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert planner that turns goals into step-by-step instructions."},
            {"role": "user", "content": plan_prompt}
        ]
    )
    return result.choices[0].message.content       # Return step-by-step plan