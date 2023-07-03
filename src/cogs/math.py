from sympy import Symbol, integrate, diff

import discord
from discord.ext import commands
from discord import app_commands


async def setup(bot):
    await bot.add_cog(Math(bot))


class Math(commands.Cog):
    def __init__(self, bot) -> None:
        self._bot = bot

    @app_commands.command(description="Returns the sum of two values")
    @app_commands.describe(
        first_value="The first value you want to add something to",
        second_value="The value you want to add to the first value"
    )
    async def add(self, interaction: discord.Interaction, first_value: int, second_value: int):
        await interaction.response.send_message(f'{first_value} + {second_value} = {first_value + second_value}')
    
    @app_commands.command(description="Differentiates an expression")
    @app_commands.describe(
        variable="Variable to differentiate with respect towards",
        expression="Expression to differentiate"
    )
    async def differentiate(self, interaction: discord.Interaction, variable: str, expression: str):
        await interaction.response.send_message(f"```{diff(expression, Symbol(variable))}```")

    @app_commands.command(description="Calculates the definite or indefinite integral of an expression")
    @app_commands.describe(
        variable="Variable to integrate with respect towards",
        expression="Expression to integrate",
        lower_bound="Lower bound of the definite integral",
        upper_bound="Upper bound of the definite integral"
    )
    async def integrate(self, interaction: discord.Interaction, variable: str, expression: str, lower_bound: float=None, upper_bound: float=None):
        respect = Symbol(variable)
        if None in (lower_bound, upper_bound):
            res = f"Indefinite integral of {expression} with respect to {variable}\n=> {integrate(expression, respect)}"
        else:
            res = f"Definite integral from {lower_bound} to {upper_bound} of {expression} with respect to {variable}\n=> {integrate(expression, (respect, lower_bound, upper_bound))}"
        await interaction.response.send_message(f"```{res}```")
