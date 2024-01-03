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
    # メッセージ送信者がBotだった場合は無視する
    str_box = message.content
    if message.author.bot:
        return 
    elif str_box[0:19] == "https://twitter.com":
        x_url = "https://vxtwitter.com/" + message.content[20:]
        await message.channel.send(x_url)
    elif str_box[0:13] == "https://x.com":
        x_url = "https://vxtwitter.com/" + message.content[14:]
        await message.channel.send(x_url)
    
TOKEN = os.getenv(sys.argv[1])
# Web サーバの立ち上げ
keep_alive()
client.run(sys.argv[1])
