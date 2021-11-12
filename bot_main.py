import discord
import config
import random
import time
# import logging
from discord.ext import commands

#Для рандома
random.seed(time.time())
bot = commands.Bot(command_prefix='соси ', intents=discord.Intents.all())


@bot.command(pas_context=True)
async def bibu(message):
    if message.channel.id == config.CHANNEL_ID:
        print('start move people')
        voice_channel_id = config.VOICE_CHANNEL_ID.values()
        #Лист каналов для взаимодействия с ними
        voice_channel = []
        for channel in voice_channel_id:
            voice_channel.append(bot.get_channel(channel))

        #Получение всех активных участников каналов
        members = []
        for channel in voice_channel:
            #Найти просто участников
            tmp_channel_mem = channel.members
            #Dывести иx id
            for membr in tmp_channel_mem:
                await membr.move_to(voice_channel[random.randrange(len(voice_channel))])
                #members.append(membr.id)
        #print(members)



        #members = voice_channel_id.members
        #memids = []
        #for member in members:
        #    memids.append(member.id)
        #print(memids)
    #    await message.channel.send('booms')


@bot.event
async def on_ready():
    print('Im ready to work')

bot.run(config.TOKEN)
# logging.basicConfig(level=logging.INFO)1