import discord
import os
from keep_alive import keep_alive

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
  print('ログインしました')

@client.event
async def on_message(message):
  print("test")
  str_box = message.content
  if message.author.bot:
    return
  elif "test-hi" in message.content :
    await message.channel.send("hi")

TOKEN = os.getenv("DISCORD_TOKEN")
# Web サーバの立ち上げ
keep_alive()
client.run(TOKEN)
