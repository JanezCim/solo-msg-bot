# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL = os.getenv('DISCORD_CHANNEL')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
        print(guild)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    # do nothing if the message author is bot
    if message.author.name == "solo-msg-bot":
        return
    
    # only process message if its in the correct GUILD and CHANNEL 
    if message.guild.name == GUILD and message.channel.name == CHANNEL:
        #print(message.author.guild_permissions)
        
        # disable permission to send further messages for this user on this channel
        await message.channel.set_permissions(message.author, read_messages=True, send_messages=False)        
        #await message.channel.send(f"Successfully toggled {message.author.name}'s view of this channel!")

@client.event
async def on_message_delete(message):
    # do nothing if the message author is bot
    if message.author.name == "solo-msg-bot":
        return

    # if user deletes message, set the send permission back to true
    await message.channel.set_permissions(message.author, read_messages=True, send_messages=True)

client.run(TOKEN)