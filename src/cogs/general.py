from io import BytesIO

import discord
from discord.ext import commands
from discord import app_commands

from utils.images import welcome_image


async def setup(bot):
    await bot.add_cog(General(bot))


class General(commands.Cog):
    def __init__(self, bot) -> None:
        self._bot = bot
    
    @app_commands.command(description="Sends welcome image to server (test)")
    async def welcome(self, interaction: discord.Interaction):
        await interaction.response.defer()
        x = await welcome_image(interaction.user)
        with BytesIO() as img_buffer:
            x.save(img_buffer, format="PNG")
            img_buffer.seek(0)
            to_send = discord.File(img_buffer, "temp.png")
            await interaction.followup.send(file=to_send)
