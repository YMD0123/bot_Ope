# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'MTE4OTkyMjY0NTY5NzkwNDc5MA.GBgD7A.TF0NM9d2PLQTHWNDZs5mEEDpsjHmLaS_Y1Icxc'

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
    if message.content == "/clean":
        #特定行または指定範囲のコメント消したいなぁー
        return 
    if str_box[0:19] == "https://twitter.com":
        #機能はこの2行で完了
        x_url = "https://vxtwitter.com/" + message.content[20:]
        await message.channel.send(x_url)
        #区切り場所と引数で処理変更すれば関数になるよ
    if str_box[0:13] == "https://x.com":
        x_url = "https://vxtwitter.com/" + message.content[14:]
        await message.channel.send(x_url)
    
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
