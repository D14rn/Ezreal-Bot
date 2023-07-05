from typing import Optional

import discord
from discord.ext import commands
from discord import app_commands

from api.riot import RiotPlatform
from api.summonerV4 import SummonerV4


commands_dict = {
    "profile": {
        "description": {
            "en": "Shows the profile of a summoner"
        },
        "help": {
            "en": "Use this command to display a summoner's profile",
            "fr": "Utilisez cette commande pour afficher le profile d'un invocateur"
        }
    }
}


async def setup(bot):
    await bot.add_cog(Ranked(bot))


class ProfileEmbed(discord.Embed):
    def __init__(self, summoner_name, region):
        self.summoner_data = SummonerV4.



class Ranked(commands.Cog):
    def __init__(self, bot) -> None:
        self._bot = bot
    
    @app_commands.command(description=commands_dict["profile"]["description"]["en"], extras=commands_dict["profile"]["help"])
    @app_commands.describe(
        name="Summoner name",
        region="Region of the summoner"
    )
    async def profile(self, interaction: discord.Interaction, member: Optional[discord.Member], name: Optional[str], region: Optional[RiotPlatform]=RiotPlatform.EUW.name):
        raise NotImplementedError
