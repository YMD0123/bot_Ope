import discord
import os, datetime, time
from keep_alive import keep_alive

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
    elif "/stop" in message.content:
      #ログオフ
      await message.channel.send("Goodbye")
      await self.close()
      return 
    

    elif message.content == "/hi":
      await message.channel.send("hi")  
      if(channel1 != None):
        await channel1.send("hi")

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
  #タイムゾーン調整
  tz_jst = datetime.timezone(datetime.timedelta(hours=9))
  #環境変数からtokenを取ってくる
  TOKEN = os.getenv("DISCORD_TOKEN")
  keep_alive()
  #すべての機能を使えるようにする
  intents = discord.Intents.all()
  #クラス生成、intentsは必須パラメータ
  client = MyClient(intents=intents)

  try:
    #Discord接続(エラー発生用)


    if (client.is_closed()):
      #discord.errors.HTTPException: 429 Too Many Requests対策
      SysClose()
    
  except discord.DiscordException as e:
    errorTime = str(datetime.datetime.now(tz_jst))
    errorText = "エラー発生:" + errorTime + "\n"
    errorText += str(e) + "\n"

    print("\n" + errorText)
    #エラーログを保存
    LogWrite(errorText)
    #discord.errors.HTTPException: 429 Too Many Requests対策
    SysClose()

#discord.errors.HTTPException: 429 Too Many Requests対策
def SysClose():
  print("osを切ります")
  os.system("kill 1")

#エラーログを保存する
def LogWrite(logText):
  sleepTime = 12
  textFile = open('log.txt', 'a')
  textFile.write(logText)
  textFile.close()
  print("処理が終わるまで待ちます:" + str(sleepTime) + "秒")
  #更新が終わるまで待たせる(早いと更新が正常に終わらない)
  time.sleep(sleepTime)

if __name__ == "__main__":
  main()
