# coding: utf_8
encoding="utf-8"

import discord
import asyncio
import random

discord_token = 'MTA1NzcwNzM5Mjg4MTY3NjM1OQ.G13GdP.LdROt1xl0qCp6g3HMde2U8bAs_npE-uC2OJfmQ' # Discordbotのアクセストークンを入力

vc = None

intents = discord.Intents.all()
client = discord.Client(intents=intents)

emoji00 = "👍"


@client.event
async def on_ready():
    print('Botを起動しました。')

@client.event
async def on_message(message):
    global voiceChannel
    global w1
    global kudov
    global kudog
    player = None
    msg = message.content
    print(msg)

#botは無視
    if message.author.bot:
        return

#bot以外に話しかけられた時


# （相対）重みweights
    w1 = [7, 14, 17, 25, 28, 29, 30]
    kudo = [
           ['kudo01.mp3','kudo01.jpg'],
           ['kudo02.mp3','kudo02.jpg'],
           ['kudo03.mp3','kudo03.jpg'],
           ['kudo04.mp3','kudo04.jpg'],
           ['kudo05.mp3','kudo05.jpg'],
           ['kudo06.mp3','kudo06.jpg'],
           ['kudo07.mp3','kudo07.jpg'],
           ]
                     


            
    if msg == "!seyana":
            global vc
            if message.author.voice is None:
                await message.channel.send("VC参加してるやろか")
                return
            if vc == None:
                vc = await message.author.voice.channel.connect()
            print('ボイスチャンネルに参加')

            # メッセージを書きます
            m = "せやな"

            # メッセージが送られてきたチャンネルへメッセージを送ります
            msgp = await message.channel.send(m)
            await msgp.add_reaction(emoji00)

    if  "どうなん" in msg:
        # メッセージを書きます
        m =  message.author.name + "、せやな"
        # メッセージが送られてきたチャンネルへメッセージを送ります
        await message.channel.send(m)
 

    if  "せやな" in msg:
        # メッセージを書きます
        m =  "せやな"
        # メッセージが送られてきたチャンネルへメッセージを送ります
        await message.channel.send(m)
    
    if  "ほんまか" in msg:
        # メッセージを書きます
        m =  "せやな"
        # メッセージが送られてきたチャンネルへメッセージを送ります
        await message.channel.send(m)
    
    if  "せやけど" in msg:
        # メッセージを書きます
        m =  "せやな"
        # メッセージが送られてきたチャンネルへメッセージを送ります
        await message.channel.send(m)
    
    if  "そうなん" in msg:
        # メッセージを書きます
        m =  "せやな"
        # メッセージが送られてきたチャンネルへメッセージを送ります
        await message.channel.send(m)
    
    if  "せやろ" in msg:
        # メッセージを書きます
        m =  "せやな"
        # メッセージが送られてきたチャンネルへメッセージを送ります
        await message.channel.send(m)

    if  "あかん" in msg:
        # メッセージを書きます
        m =  "せやな"
        # メッセージが送られてきたチャンネルへメッセージを送ります
        await message.channel.send(m)

    if  "せやかて" in msg:
        # メッセージを書きます
        m =  "工藤"
        # メッセージが送られてきたチャンネルへメッセージを送ります
        await asyncio.sleep(2)
        await message.channel.send(m)

        if message.author.voice is None:
            return
        if vc == None:
                vc = await message.author.voice.channel.connect()

        if message.guild.voice_client.is_playing():
            return

        kudo_rondom  = random.choices(kudo, cum_weights=w1,k=1)
        print(kudo_rondom)
        print(kudo_rondom[0][1])
        await message.channel.send(file=discord.File(kudo_rondom[0][1]))
        #再生
        vc.play(discord.FFmpegPCMAudio(kudo_rondom[0][0]))

        return

    if  "でんがな" in msg:
        # メッセージを書きます
        m =  "まんがな"
        # メッセージが送られてきたチャンネルへメッセージを送ります
        await message.channel.send(m)       

    if  "ちゃうんか" in msg:
        # メッセージを書きます
        m =  "なんでやねん！"
        # メッセージが送られてきたチャンネルへメッセージを送ります
        await message.channel.send(m)

    if  "なんでやねん" in msg:
        # メッセージを書きます
        m =  "どないやねん"
        # メッセージが送られてきたチャンネルへメッセージを送ります
        await message.channel.send(m)

    if  "せやねん" in msg:
        # メッセージを書きます
        m =  "せやねんなぁ"
        # メッセージが送られてきたチャンネルへメッセージを送ります
        await message.channel.send(m)

    if  "せやろか" in msg:
            if message.guild.voice_client is None:
                await message.channel.send("せやかて")
                return

            await message.channel.send('せやな・・・')
            await message.guild.voice_client.disconnect()
            vc = None
            return


#リアクションが付いたときにsummer
@client.event
async def on_raw_reaction_add(payload):

#せやな
        if payload.emoji.name == emoji00:
            global vc
        
            channel = client.get_channel(payload.channel_id)
            member = channel.guild.get_member(payload.user_id)

            if member.bot == True:    # botは無視
                return

            #再生
            if channel.guild.voice_client.is_playing():
                return
            vc.play(discord.FFmpegPCMAudio('seyana.mp3'))
            return


        else:
            return

async def main():
    # start the client
    async with client:
        await client.start(discord_token)
        
asyncio.run(main())
