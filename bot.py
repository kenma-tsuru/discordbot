import discord
from discord.ext import commands
import math
import dotenv
import os
dotenv.load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def gcd(ctx, x: int, y: int):
    result = math.gcd(x, y)
    await ctx.send(f"The GCD of {x} and {y} is: {result}")

@bot.command()
async def gcds(ctx, *args):
    if len(args) < 2:
        await ctx.send("Please provide at least two numbers.")
        return
    
    try:
        numbers = [int(arg) for arg in args]
    except ValueError:
        await ctx.send("All arguments must be integers.")
        return

    result = numbers[0]
    for num in numbers[1:]:
        result = math.gcd(result, num)

    numbers_str = ", ".join(str(num) for num in numbers)
    await ctx.send(f"The GCD of {numbers_str} is: {result}")


# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run(os.getenv('DISCORD_TOKEN'))