import discord
from discord.ext import commands
from discord import app_commands


async def setup(bot):
    await bot.add_cog(Ranked(bot))


class Ranked(commands.Cog):
    def __init__(self, bot) -> None:
        self._bot = bot
    
    @app_commands.command()
    @app_commands.describe(
        name="Summoner name",
        region="Region of the summoner, default = EUW"
    )
    async def rank(self, interaction: discord.Interaction, name: str=None, region: str='EUW'):
        await interaction.response.send_message(
            f"name={name if name is not None else interaction.user.name}\nregion={region}"
        )
