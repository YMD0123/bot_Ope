import discord
import os
from keep_alive import keep_alive

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.author.bot:
      return
    elif str_box[0:19] == "https://twitter.com":
      x_url = "https://vxtwitter.com/" + message.content[20:]
      await message.channel.send(x_url)
    elif str_box[0:13] == "https://x.com":
      x_url = "https://vxtwitter.com/" + message.content[14:]


TOKEN = os.getenv("DISCORD_TOKEN")
# Web サーバの立ち上げ
keep_alive()
client.run(TOKEN)
