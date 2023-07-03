if __name__ == "__main__":

    import os

    import discord
    import dotenv

    from ezreal import Ezreal


    dotenv.load_dotenv("../.env")

    token = os.getenv("DISCORD_TOKEN")
    dev_guild_id = discord.Object(int(os.getenv("DEV_GUILD_ID")))

    intents = discord.Intents(messages=True, guilds=True, members=True)
    client = Ezreal(intents=intents, guild_id=dev_guild_id)

    client.run(token)
