import os
import discord
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
if not DISCORD_TOKEN:
    raise ValueError('DISCORD_TOKEN is not set in the environment variables')
AI_CONFIG = {
    "model": "deepseek-chat",
    "api_key": os.getenv('DEEPSEEK_API_KEY'),
    "base_url": "https://api.deepseek.com"
}

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(DISCORD_TOKEN)