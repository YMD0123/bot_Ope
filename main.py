import discord
import os
from keep_alive import keep_alive
from logging import getLogger


client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
  print('ログインしました')

@client.event
async def on_message(message):
  str_box = message.content
  if message.author.bot:
    return
  if message.content == "/hi":
    await message.channel.send("hi")

logger = getLogger(__name__)
logger.info('message')
TOKEN = os.getenv("DISCORD_TOKEN")
# Web サーバの立ち上げ
keep_alive()
client.run(TOKEN)
