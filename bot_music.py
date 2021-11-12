import discord
import config
import logging
import spotify
from discord.ext import commands

logging.basicConfig(level=logging.INFO)

class Spotify(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Spotify(bot))


