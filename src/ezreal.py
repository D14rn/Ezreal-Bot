import discord
from discord.ext import commands


class Ezreal(commands.Bot):
    def __init__(self, *args, intents: discord.Intents, guild_id: int=None):
        super().__init__(args, intents=intents)
        self.guild_id = guild_id
    
    async def setup_hook(self):
        await self.load_extension("cogs.general")
        await self.load_extension("cogs.math")
        await self.load_extension("cogs.ranked")

        self.tree.copy_global_to(guild=self.guild_id)
        await self.tree.sync(guild=self.guild_id)

    async def on_ready(self):
        print(f"Successfully logged in as {self.user}")        
    
    async def on_member_join(self, member):
        print(f"{member.name}")
