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
