import discord
from discord.ext import commands
import random
import time
import ast
import os

bot = commands.Bot(command_prefix=commands.when_mentioned_or("b."), case_insensitive=True)
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Online and no errors so far.")
    print("Version of the bot launched = 0.01")
    await bot.change_presence(activity=discord.Game(name=f"with {len(bot.guilds)} servers!"))

@bot.command()
async def ping(ctx):
    ping_ = bot.latency
    ping = round(ping_ * 1000)
    embed = discord.Embed(color=discord.Color(value=0x7DC6F))
    embed.add_field(name="Ping!", value=f"My latancey is {ping}ms.")
    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed = discord.Embed(color=discord.Color(value=0x7DC6F))
    embed.set_author(name="Help with Blueshell", icon_url=bot.user.avatar_url)
    embed.add_field(name="Prefix", value="The normal prefix on this server is [b.]. Or you can mention the bot.")
    embed.add_field(name="Genaral", value="Ping, userinfo, more comming soon")
    embed.add_field(name="Mod Comamnds", value="Ban, kick, mute and unmute.")
    embed.set_footer(text="To use the commands above you simply do b.[command] | Help for Blueshell. | b.cmdsetup for mute setup")
    embed.set_thumbnail(url=bot.user.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def cmdsetup(ctx):
    embed = discord.Embed(color=discord.Color(value=0x7DC6F))
    embed.add_field(name="Mute Command Setup", value="To use the mute and unmute command you need a role called **muted** there is a setting next to send messages what says **read channels and voice channels** uncheck that. Next uncheck **send messages** and it will be all good now you can start muting people.")
    await ctx.send(embed=embed)

@bot.command()
async def userinfo(ctx, member:discord.Member=None):
    if member == None:
        member = ctx.message.author
        pronoun = "Your"
    else:
        pronoun = "Their"
    name = f"{member.name}#{member.discriminator}"
    status = member.status
    joined = member.joined_at
    role = member.top_role
    embed = discord.Embed(color=discord.Color(value=0xadd8e6))
    embed.set_author(name="Name Cmd", icon_url=bot.user.avatar_url)
    embed.add_field(name="Joined at", value=f"They joined at {joined}", inline=False)
    embed.add_field(name="Top role", value=f"{pronoun} top role is {role}", inline=False)
    embed.add_field(name="Status", value=f"{pronoun} status is {status}", inline=False)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"{pronoun} name is {name}.")
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member = None, reason = None):
    if member == None or member == ctx.message.author:
        await ctx.send("You made an oopsie there. Please specify a member, or you cannot ban yourself.")
        return
    if reason == None:
        reason = "No Reason..."
    message = f"You have been **banned** from **{ctx.guild.name}**! You were banned for **{reason}**. You can join back if your ban is revoked, if not sorry pal."
    await member.send(message)
    await member.ban()
    await ctx.send(f"{member} has been banned. You can revoke the ban in server setings.")

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member = None, reason = None):
    if member == None or member == ctx.message.author:
        await ctx.send("You made an oopsie there. Please specify a member, or you cannot kick yourself.")
        return
    if reason == None:
        reason = "No Reason..."
    message = f"You have been **Kicked** from **{ctx.guild.name}**! You were Kicked for **{reason}**. You can join back with an invite if you have one."
    await member.send(message)
    await member.kick()
    await ctx.send(f"{member} has been Kicked. Watch out they can come back.")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member:discord.Member = None, reason = None):
    role = discord.utils.get(ctx.guild.roles, name="muted")
    if member == None or member == ctx.message.author:
        await ctx.send("You made an oopsie there. Please specify a member, or you cannot mute yourself.")
        return
    if reason == None:
        reason = "No reason..."
    message = f"You have been **muted** from **{ctx.guild.name}**! You were muted for **{reason}**."
    await member.send(message)
    await member.add_roles(role)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member:discord.Member = None, reason = None):
    role = discord.utils.get(ctx.guild.roles, name="muted")
    if member == None or member == ctx.message.author:
        await ctx.send("You made an oopsie there. Please specify a member, or you cannot mute yourself.")
        return
    if reason == None:
        reason = "No reason..."
    message = f"You have been **unmuted** from **{ctx.guild.name}** You were unmuted for **{reason}**."
    await member.send(message)
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.remove_roles(role)
    


@bot.command()
async def invite(ctx):
    embed = discord.Embed(color=discord.Color(value=0xadd8e6))
    embed.add_field(name="Invite Blueshell!", value="[Blueshell link shortener™](https://discordapp.com/api/oauth2/authorize?client_id=541252510506156062&permissions=8&scope=bot)")
    await ctx.send(embed=embed)
    
bot.run("NTQxMjUyNTEwNTA2MTU2MDYy.DzcwWw.pLVaau0hkMM0LdRoMYBpOKG5VjY")