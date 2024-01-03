#TO DO
#下のURL見ながらトークン死守頑張って
#https://qiita.com/raiga0310/items/d5c7b0f852527b82d786
#https://qiita.com/harukikaneko/items/b004048f8d1eca44cba9

# インストールした discord.py を読み込む
import discord
import sys

# 自分のBotのアクセストークンに置き換えてください
TOKEN = sys.argv[1]

# 接続に必要なオブジェクトを生成
client = discord.Client(intents=discord.Intents.all())

# 起動時に動作する処理
@client.event
async def on_ready():
    #BOT起動時の処理
    print('ログインしました')


# メッセージ受信時に動作する処理
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
    
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
