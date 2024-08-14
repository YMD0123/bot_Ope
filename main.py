import discord
import os
from keep_alive import keep_alive

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('ログインしました')

@client.event
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

  #https://twitter.comがある場合
  elif str_box.find("https://twitter.com") != -1:
    #https://twitter.comの位置を取得
    x_point = str_box.find("https://twitter.com")
    #https://vxtwitter.com/の後ろのURLを取得
    x_url  = "https://vxtwitter.com/" + message.content[x_point+20:]
    #URLが3つ以下の場合は無効
    if(x_url.count('/') <= 3):
      return
    #URLを送信
    await message.channel.send(x_url)
    #送信者を送信
    await message.channel.send(message.author)
    #https://twitter.comが先頭の場合は削除
    if(x_point == 0):
      await message.delete()
    #ログチャンネルがある場合
    if(channel1 != None):
      #URLを送信
      await channel1.send(x_url)
      #送信者を送信
      await channel1.send(message.author)




  elif str_box.find("https://x.com") != -1:
    #https://x.comの位置を取得
    x_point = str_box.find("https://x.com")
    #https://vxtwitter.com/の後ろのURLを取得
    x_url  = "https://vxtwitter.com/" + message.content[x_point+14:]
    #URLが3つ以下の場合は無効
    if(x_url.count('/') <= 3):
      return
    #URLを送信
    await message.channel.send(x_url)
    #送信者を送信
    await message.channel.send(message.author)
    #https://x.comが先頭の場合は削除
    if(x_point == 0):
      await message.delete()
    #ログチャンネルがある場合
    if(channel1 != None):
      #URLを送信
      await channel1.send(x_url)
      #送信者を送信
      await channel1.send(message.author)


TOKEN = os.getenv("DISCORD_TOKEN")
# Web サーバの立ち上げ
keep_alive()
client.run(TOKEN)
