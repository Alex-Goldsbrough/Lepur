# Lepur By Hanger

#Other Stuff
import discord
from discord import member
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import asyncio

bot = commands.Bot(command_prefix='-', status=discord.Status.online, activity=discord.Game(name="do -help to Help!"))
bot.remove_command('help')

#Up and running
@bot.event
async def on_ready():
    print ("I am Up and running!")

#Help Command
@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        colour = discord.Colour.red()
    )

    embed.set_author(name="Help Menu")
    embed.add_field(name="-help", value="Show you all the commands!", inline=False)
    embed.add_field(name="-ping", value="checks the bots ping!", inline=False)
    embed.add_field(name="-purge [Ammount]", value="Deletes an ammount of Messages you want!", inline=False)
    embed.add_field(name="-joke",value="See a Funny Dad joke!", inline=False)
    embed.add_field(name="-ban [Player]",value="Ban someone for their rulebreaking!", inline=False)
    embed.add_field(name="-kick [Player]",value="Kick someone for their rulebreaking!", inline=False)

    await author.send(embed=embed)
    await ctx.send("**Message Sent to your DM's!**")

#Ping Command 
@bot.command(pass_context=True)
async def ping(ctx):
    ping_ = bot.latency
    ping = round(ping_ * 1000)
    await ctx.channel.send(f"My ping is **{ping}ms**")

#Purge/Clear Command
@bot.command()
async def purge(ctx, amount: int):
    errorEmbed = discord.Embed(color=discord.Color.red())
    errorEmbed.add_field(name="Error", value="You do not have permissions to purge the message(s)!")
    succEmbed = discord.Embed(color=discord.Color.green())
    succEmbed.add_field(name="Success", value="I have purged %s message(s) for you!" % str(amount))
    try:
        await ctx.channel.purge(limit=amount)
        Success = await ctx.send(embed=succEmbed)
        await asyncio.sleep(2)
        await Success.delete()
    except:
        await ctx.send(embed=errorEmbed)

#Kick Command
@bot.command(name="kick", pass_context=True)
@has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member = None):
    if user is None:
        await ctx.send("**Please tag a user**")
        return
    else:
        await ctx.send("**I have chased {0} away. Cya!**".format(user.mention))
        await user.kick()

#Ban Command                          
@bot.command(name="ban", pass_context=True)
@has_permissions(manage_roles=True, ban_members=True)
async def ban(ctx, user: discord.Member = None):
    if user is None:
        await ctx.send("**Please tag a user**")
        return
    else:
        await ctx.send("**I have jailed {0}. Cya!**".format(user.mention))
        await user.ban()

bot.run("TOKEN")