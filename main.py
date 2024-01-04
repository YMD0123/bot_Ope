import discord
import os
from keep_alive import keep_alive

print("start")
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

TOKEN = os.getenv("DISCORD_TOKEN")
# Web サーバの立ち上げ
keep_alive()
client.run(TOKEN)
