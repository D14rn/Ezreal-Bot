from typing import Optional

import discord
from discord.ext import commands
from discord import app_commands

from api import RiotPlatform, SummonerV4, LeagueV4, RankedQueue, LeagueAssets


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


class ProfileEmbedGenerator:
    @staticmethod
    def from_summoner_id(platform, name, summoner_id, icon_id):
        data = LeagueV4.by_summoner_id(platform, summoner_id)
        embed = discord.Embed()
        embed.set_author(name=name, url=f"https://op.gg/summoners/{platform}/{name}".replace(" ", "%20"), icon_url=LeagueAssets.icon_url(icon_id))
        if len(data) == 0:
            embed.description = f"is currently unranked"
        for index, queue in enumerate(data):
            embed.insert_field_at(index=index*3,
                                  name=RankedQueue[queue["queueType"]],
                                  value=f"{queue['tier']} {queue['rank']} {queue['leaguePoints']}LP",
                                  inline=True)
            embed.insert_field_at(index=index*3+1,
                                  name="Winrate",
                                  value=f"{queue['wins']}W/{queue['losses']}L ({round(queue['wins'] / (queue['wins'] + queue['losses']) * 100, 2)}%)",
                                  inline=True)
            if index != len(data)-1:
                embed.insert_field_at(index*3+2, name=" ", value=" ", inline=False)

    @classmethod
    def from_name(cls, platform, name):
        data = SummonerV4.by_name(platform, name)
        return cls.from_summoner_id(platform, data["name"], data["id"], data["profileIconId"])

class Ranked(commands.Cog):
    def __init__(self, bot) -> None:
        self._bot = bot
    
    @app_commands.command(description=commands_dict["profile"]["description"]["en"], extras=commands_dict["profile"]["help"])
    @app_commands.describe(
        name="Summoner name",
        region="Region of the summoner"
    )
    async def profile(self, interaction: discord.Interaction, member: Optional[discord.Member], name: Optional[str], region: Optional[RiotPlatform]=RiotPlatform.EUW.name):
        embed = ProfileEmbedGenerator.from_name(region, name)
        await interaction.response.send_message(embed=embed)
