import discord
import os
import asyncio
from dotenv import load_dotenv
from agents.agent import Agent

load_dotenv()

token = os.getenv("DISCORD_TOKEN")     # Get bot token
agent = Agent()                         # Create agent

intents = discord.Intents.default()     # Discord permissions
intents.messages = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')    # Log bot info

@client.event
async def on_message(message):
    if message.author == client.user:
        return                              # Ignore self messages

    user_input = message.content
    context = agent.memory.query(user_input)         # Get memory
    response = agent.think(user_input, context)      # Think + reply
    await message.channel.send(response)             # Send reply
    agent.memory.store(user_input, response)         # Save reply

if __name__ == '__main__':
    client.run(token)                               # Run bot
