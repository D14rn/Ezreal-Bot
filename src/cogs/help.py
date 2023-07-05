from typing import Literal, Optional

import discord
from discord.ext import commands
from discord import app_commands


# descriptions of implemented commands
commands_dict = {
    "help": {
        "description": {
            "en": "Lists the available commands and their description",
            #"fr": "Liste l'ensemble des commandes et leur description"
        },
        "help": {
            "en": "Use this command to list all the commands and their use",
            "fr": "Utilisez cette commande pour afficher la liste des commandes et leur utilité"
        }
    }
}


async def setup(bot):
    await bot.add_cog(Help(bot))


class HelpEmbed(discord.Embed):
    def __init__(self, commands, lang):
        super().__init__()
        for command in commands:
            self.add_field(name=f"/{command.name}", value=command.extras.get(lang, command.description), inline=False)

class Help(commands.Cog):
    def __init__(self, bot) -> None:
        self._bot = bot
    
    @app_commands.command(description=commands_dict["help"]["description"]["en"], extras=commands_dict["help"]["help"])
    async def help(self, interaction: discord.Interaction, language: Optional[Literal["en", "fr"]]="en"):
        commands = self._bot.tree.get_commands()
        await interaction.response.send_message(embed=HelpEmbed(commands, language))
