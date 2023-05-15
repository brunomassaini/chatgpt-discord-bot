import discord
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

intents = discord.Intents.default()
client = discord.Client(intents=intents)

def generate_response(message):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "assistant", "content": message}
        ]
    )

    message = completion.choices[0].message.content
    return message

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.guild is None: # Check if the message was sent in a DM
        async with message.channel.typing():
            response = generate_response(message.content)
            await message.channel.send(response)
    else: # If the message was sent in a guild, only respond if the bot is tagged
        if client.user.mentioned_in(message):
            async with message.channel.typing():
                response = generate_response(message.content)
                await message.channel.send(response)

client.run(os.getenv('DISCORD_API_KEY'))