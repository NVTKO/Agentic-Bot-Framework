import sys
import os

#Force project root into sys.path BEFORE any other import
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import asyncio                         # For running async tasks
from agents.agent import Agent         # Import the agent

async def main():
    agent = Agent()                   # Create an agent
    await agent.run()                 # Start the loop

if __name__ == '__main__':
    asyncio.run(main())              # Run the program