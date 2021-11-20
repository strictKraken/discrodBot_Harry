import discord
import config
import random
import time

from discord.ext import commands
from dotenv import load_dotenv


class trash_bot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user} ({self.bot.user.id}) ready ')

    @commands.command()
    async def roll(self, ctx):
        rolling = random.randrange(100)
        if random.randrange(100) % 2 == 0:
            flag = 'Решка'
        else:
            flag = 'Орёл'
        await ctx.send(flag)

    @commands.command()
    async def rend(self, ctx, number):
        await ctx.send(random.randrange(0, int(number)))

    @commands.command()
    async def boom(self, ctx):
        if ctx.channel.id == config.CHANNEL_ID:
            print('Start move people')
            voice_channel_id = config.VOICE_CHANNEL_ID.values()
            #list of voice channels for active
            voice_channels = []
            for channel in voice_channel_id:
                voice_channels.append(self.bot.get_channel(channel))
            print(voice_channels)

            # Get all members in chat
            for channel in voice_channels:
                # Search members
                tmp_channel_mem = channel.members
                print(tmp_channel_mem)
                # Show id
                for membr in tmp_channel_mem:
                    await membr.move_to(voice_channels[random.randrange(len(voice_channels))])
#
intents = discord.Intents.default()
intents.members = True
intents.presences = True
# bot prefix
bot = commands.Bot(command_prefix=commands.when_mentioned_or(config.CONFIG_PREFIX))
# random seed
random.seed(time.time())

if __name__ == '__main__':
    # 123

    bot.add_cog(trash_bot(bot))
    bot.run(config.TOKEN, reconnect=True)
