import discord
from discord.ext import tasks
from datetime import datetime 

TOKEN = "" #トークン
CHANNEL_ID = 000 #チャンネルID
# 接続に必要なオブジェクトを生成
intents = discord.Intents.default()
client = discord.Client(intents=intents)

#指定した時刻に1回だけ処理を実行するためのフラグ
flag = True


@tasks.loop(seconds=30)
async def loop():
    global flag

    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    # 曜日
    day_of_week = datetime.now().strftime('%A')
    print(now, day_of_week, flag)

    if now == '01:34' and flag:
        if day_of_week == 'Sunday':
            channel = client.get_channel(CHANNEL_ID)
            await channel.send('明日は燃えるゴミの日！')
        elif day_of_week == 'Monday':
            channel = client.get_channel(CHANNEL_ID)
            #await channel.send('')
        elif day_of_week == 'Tuesday':
            channel = client.get_channel(CHANNEL_ID)
            #await channel.send('')
        elif day_of_week == 'Wednesday':
            channel = client.get_channel(CHANNEL_ID)
            await channel.send('明日は燃えるゴミの日！')
            await channel.send('今日は活動日！')
        elif day_of_week == 'Thursday':
            channel = client.get_channel(CHANNEL_ID)
            await channel.send('明日はびん･缶･ペットボトルのゴミの日！')
        elif day_of_week == 'Friday':
            channel = client.get_channel(CHANNEL_ID)
            #await channel.send('')
        elif day_of_week == 'Saturday':
            channel = client.get_channel(CHANNEL_ID)
            await channel.send('明後日は燃えるゴミの日！')
            await channel.send('今日は活動日！')
        
        flag = False
    else:
        flag = True
        

@client.event
async def on_ready():
    loop.start()


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
