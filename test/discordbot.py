
import discord
import sys

class MyClient(discord.Client):
  #メッセージが書き込まれた時
  async def on_message(self, message):
    if message.author.bot:
      return
    elif "/stop" in message.content:
    #ログオフ
      await message.channel.send("Goodbye")
      await self.close()
      return 

    str_box = message.content
    channel1 = self.get_channel(1196743997465575424) #logチャンネル


    #送信者がbot自身の場合はコマンドを無効にする
    if message.author.bot:
      return
    
    #/stopコマンド＝bot停止
    elif "/stop" in message.content:
      #ログオフ
      await message.channel.send("Goodbye")
      await self.close()
      return 
    
    #/hiコマンド＝存在確認
    elif message.content == "/hi":
      await message.channel.send("hi")  
      if(channel1 != None):
        await channel1.send("hi")

    #https://twitter.comが
    elif str_box.find("https://twitter.com") != -1:
      x_point = str_box.find("https://twitter.com")
      x_url  = "https://vxtwitter.com/" + message.content[x_point+20:]
      if(x_url.count('/') <= 3):
        return
      await message.channel.send(x_url)
      await message.channel.send(message.author)
      if(x_point == 0):
        await message.delete()
      if(channel1 != None):
        await channel1.send(x_url)
        await channel1.send(message.author)




    elif str_box.find("https://x.com") != -1:
      x_point = str_box.find("https://x.com")
      x_url  = "https://vxtwitter.com/" + message.content[x_point+14:]
      if(x_url.count('/') <= 3):
        return
      await message.channel.send(x_url)
      await message.channel.send(message.author)
      if(x_point == 0):
        await message.delete()
      if(channel1 != None):
        await channel1.send(x_url)
        await channel1.send(message.author)




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