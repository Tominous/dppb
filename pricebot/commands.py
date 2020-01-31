from discord.ext import commands
import json

bot = commands.Bot(command_prefix="!pricebot")
bot.run(json.loads(open("../config/config.json", "r").read())["token"])

@bot.command()
async def priceof(ctx, query):
    pass

@bot.command()
async def top(ctx):
    pass

@bot.command()
async def parts(ctx):
    await ctx.send('''Support parts are: 
                Processor(cpu)
                Graphics Processor(gpu)
                Power Supply(psu)
                Memory(ram)
                Motherboard(mobo)
                Internal Hard Drive(hdd)
                Case(case)
                
                Use the abbreviations in parentheses as the part you request
            ''')