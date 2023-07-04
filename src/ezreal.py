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

if __name__ == "__main__":

    import os

    import discord
    import dotenv


    dotenv.load_dotenv("../.env")

    token = os.getenv("DISCORD_TOKEN")
    dev_guild_id = discord.Object(int(os.getenv("DEV_GUILD_ID")))

    intents = discord.Intents(messages=True, guilds=True, members=True)
    client = Ezreal(intents=intents, guild_id=dev_guild_id)

    client.run(token)
