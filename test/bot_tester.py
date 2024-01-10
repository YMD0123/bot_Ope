import discord
import os, datetime, time
from keep_alive import keep_alive

class MyClient(discord.Client):
  #botクラスの処理内容
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
    elif str_box[0:13] == "https://x.com":
      x_url = "https://vxtwitter.com/" + message.content[14:]

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
    client.run(TOKEN)

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
