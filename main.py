import discord, colorama, sys, os, json, pystyle
from discord.ext import commands, tasks
from discord import Option
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System


os.system("title Discord Payment Bot")

bot = discord.Bot(intents=discord.Intents.all())
config = json.load(open("settings.json", encoding="utf-8"))

# payment configs
paypaluser = "ur paypal user"
ethaddy = "ur eth address"
btcaddy = "ur btc address"
ltcaddy = "ur ltc address"
cashappaddy = "ur cashapp"
swishaddy = "ur swish number"

# color config (hex) get colors from here https://stackoverflow.com/questions/63768372/color-codes-for-discord-py
btccolor = 0xf1c40f
ltccolor = 0x979c9f
paypalcolor = 0x0084ff
ethcolor = 0x979c9f
cashappcolor = 0x2ecc71
swishcolor = 0xe67e22

# image configs
paypalimage = "https://seeklogo.com/images/P/paypal-logo-481A2E654B-seeklogo.com.png"
btcimage = "https://seeklogo.com/images/B/bitcoin-logo-DDAEEA68FA-seeklogo.com.png"
ethimage = "https://seeklogo.com/images/E/ethereum-logo-DE26DD608D-seeklogo.com.png"
ltcimage = "https://seeklogo.com/images/L/litecoin-logo-09A62FE1FB-seeklogo.com.png"
cashappimage = "https://seeklogo.com/images/C/cash-app-logo-A39DD086EB-seeklogo.com.png"
swishimage = "https://seeklogo.com/images/S/swish-logo-B5728161FC-seeklogo.com.png"

# don't change anything below

@bot.slash_command(guild_ids=[config["guildID"]], name='paypal', description='send paypal')
async def paypal(ctx,
                 amount: Option(str, 'how much money you want them to send to you',
    required=True, default=None),

):
    embed = discord.Embed(title=f"PayPal", description=f"Send **${amount}USD** to **{paypaluser}** in family and friends.",
                          color=paypalcolor)
    embed.set_thumbnail(url=f"{paypalimage}")
    await ctx.channel.send(embed=embed)
    print(colorama.Fore.RED + 'Sent')

@bot.slash_command(guild_ids=[config["guildID"]], name='btc', description='send btc addy')
async def bitcoin(ctx,
                 amount: Option(str, 'how much money you want them to send to you',
    required=True, default=None),

):
    embed = discord.Embed(title=f"Bitcoin", description=f"Send **${amount}USD** to **{btcaddy}**.",
                          color=btccolor)
    embed.set_thumbnail(url=f"{btcimage}")
    await ctx.channel.send(embed=embed)
    print(colorama.Fore.RED + 'Sent')

@bot.slash_command(guild_ids=[config["guildID"]], name='eth', description='send eth addy')
async def eth(ctx,
                 amount: Option(str, 'how much money you want them to send to you',
    required=True, default=None),

):
    embed = discord.Embed(title=f"ETH", description=f"Send **${amount}USD** to **{ethaddy}**.",
                          color=ethcolor)
    embed.set_thumbnail(url=f"{ethimage}")
    await ctx.channel.send(embed=embed)
    print(colorama.Fore.RED + 'Sent')

@bot.slash_command(guild_ids=[config["guildID"]], name='ltc', description='send ltc addy')
async def ltc(ctx,
                 amount: Option(str, 'how much money you want them to send to you',
    required=True, default=None),

):
    embed = discord.Embed(title=f"LTC", description=f"Send **${amount}USD** to **{ltcaddy}**.",
                          color=ltccolor)
    embed.set_thumbnail(url=f"{ltcimage}")
    await ctx.channel.send(embed=embed)
    print(colorama.Fore.RED + 'Sent')

@bot.slash_command(guild_ids=[config["guildID"]], name='cashapp', description='send cashapp addy')
async def ltc(ctx,
                 amount: Option(str, 'how much money you want them to send to you',
    required=True, default=None),

):
    embed = discord.Embed(title=f"cashapp", description=f"Send **${amount}USD** to **{cashappaddy}**.",
                          color=cashappcolor)
    embed.set_thumbnail(url=f"{cashappimage}")
    await ctx.channel.send(embed=embed)
    print(colorama.Fore.RED + 'Sent')

@bot.slash_command(guild_ids=[config["guildID"]], name='swish', description='send swish addy')
async def ltc(ctx,
                 amount: Option(str, 'how much money you want them to send to you',
    required=True, default=None),

):
    embed = discord.Embed(title=f"swish", description=f"Send **${amount}USD** to **{swishaddy}**.",
                          color=swishcolor)
    embed.set_thumbnail(url=f"{swishimage}")
    await ctx.channel.send(embed=embed)
    print(colorama.Fore.RED + 'Sent')

@bot.slash_command(guild_ids=[config["guildID"]], name='latency', description='sends the bots latency')
async def latency(ctx: discord.ApplicationContext):
    await ctx.send(f"`My latency is {bot.latency}ms!`")
    print({bot.latency})
    print(colorama.Fore.MAGENTA + 'Sent')

@bot.command(guild_ids=[config["guildID"]], name="activity", description="Changes the activity of the bot.")
@commands.guild_only()
async def activity(ctx, activity):
    if not str(ctx.author.id) in config["botAdminId"]:
        return await ctx.respond(embed=discord.Embed(description="You must be an owner to use this command.", color=0xFF0000))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=activity))
    return await ctx.respond(embed=discord.Embed(description=f"Changed activity to {activity}", color=0xffffff))



# you can change the part below if you want

print(colorama.Fore.BLUE + "██████╗░░█████╗░██╗░░░██╗███╗░░░███╗███████╗███╗░░██╗████████╗██████╗░░█████╗░████████╗")
print(colorama.Fore.BLUE + "██╔══██╗██╔══██╗╚██╗░██╔╝████╗░████║██╔════╝████╗░██║╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝")
print(colorama.Fore.BLUE + "██████╔╝███████║░╚████╔╝░██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░██████╦╝██║░░██║░░░██║░░░")
print(colorama.Fore.BLUE + "██╔═══╝░██╔══██║░░╚██╔╝░░██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░██╔══██╗██║░░██║░░░██║░░░")
print(colorama.Fore.BLUE + "██║░░░░░██║░░██║░░░██║░░░██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░██████╦╝╚█████╔╝░░░██║░░░")
print(colorama.Fore.BLUE + "╚═╝░░░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚═════╝░░╚════╝░░░░╚═╝░░░")
print(colorama.Fore.BLUE + "                              Bot Made By skurken♡#0002                                ")

bot.run(config["bottoken"])