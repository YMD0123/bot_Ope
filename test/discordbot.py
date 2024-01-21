
import discord
import sys

class MyClient(discord.Client):
  #メッセージが書き込まれた時
  async def on_message(self, message):
    str_box = message.content
    #送信者がbot自身の場合はコマンドを無効にする
    if message.author.bot:
      return
    elif "/stop" in message.content:
      #ログオフ
      await message.channel.send("Goodbye")
      await self.close()
      return 
    elif message.content == "/hi":
      await message.channel.send("hi")
    elif str_box[0:19] == "https://twitter.com":
      x_url = "https://vxtwitter.com/" + message.content[20:]
      await message.channel.send(x_url)
      await message.channel.send(message.author)
      await message.delete()
    elif str_box[0:13] == "https://x.com":
      x_url  = "https://vxtwitter.com/" + message.content[14:]
      await message.channel.send(x_url)
      await message.channel.send(message.author)
      await message.delete()




def main():
  #環境変数からtokenを取ってくる
  TOKEN = sys.argv[1]
  #すべての機能を使えるようにする
  intents = discord.Intents.all()
  #intentsは必須パラメータ
  client = MyClient(intents=intents)
  #Discord接続
  client.run(TOKEN)

if __name__ == "__main__":
  main()