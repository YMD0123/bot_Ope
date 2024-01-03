import discord
import sys
import os
from keep_alive import keep_alive

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    emoji ="👍"
    await message.add_reaction(emoji)

TOKEN = os.getenv(sys.argv[1])
# Web サーバの立ち上げ
keep_alive()
client.run(TOKEN)
