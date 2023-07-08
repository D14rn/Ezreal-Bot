from typing import Optional

import discord
from discord.ext import commands
from discord import app_commands

from api import RiotPlatform, SummonerV4, LeagueV4, RankedQueue


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
    def from_summoner_id(platform, name, summoner_id):
        data = LeagueV4.by_summoner_id(platform, summoner_id)
        unranked = True
        if len(data) > 0:
            for queue in data:
                if queue["queueType"] == RankedQueue.RANKED_SOLO_5x5.name:
                    unranked = False
                    tier = queue["tier"]
                    rank = queue["rank"]
                    league_points = queue["leaguePoints"]
                    wins = queue["wins"]
                    losses = queue["losses"]
        embed = discord.Embed(title=name)
        if unranked:
            embed.description = f"is currently unranked"
        else:
            embed.description = f"is currently {tier} {rank} {league_points} LP ({int(int(wins) / (int(losses) + int(wins)) * 100)}% WR)"
        return embed

    @classmethod
    def from_name(cls, platform, name):
        data = SummonerV4.by_name(platform, name)
        return cls.from_summoner_id(platform, data["name"], data["id"])

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
