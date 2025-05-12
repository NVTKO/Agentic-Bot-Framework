import os
from dotenv import load_dotenv         # Load .env file
from agents.tools import get_tools     # Load tools
from memory.simple_memory import MemoryDB  # In-memory fallback memory
from memory.embeddings import get_embedding # For vector embedding
from improvement.self_eval import evaluate_response # For self-feedback
from agents.planner import plan_task   # For planning steps

load_dotenv()

class Agent:
    def __init__(self):
        self.memory = MemoryDB()       # Initialize memory
        self.tools = get_tools()       # Load toolset

    async def run(self):
        print("Agent initialized. Listening...")
        while True:
            user_input = input("You: ")         # Get user input
            context = self.memory.query(user_input)  # Look up memory
            plan = plan_task(user_input)             # Make a plan
            print(f"[Plan] {plan}")
            response = self.think(user_input, context) # Generate reply
            print(f"Agent: {response}")
            self.memory.store(user_input, response)    # Save memory
            evaluate_response(user_input, response)    # Grade itself

    def think(self, input_text, context):
        return f"Processed: {input_text} with context: {context}"  # Basic reply