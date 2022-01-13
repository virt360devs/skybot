
import os
os.system("pip install PyNaCl")
import asyncio
import discord
import music
import nacl
import random
import praw
import flask
from discord.ext import commands
from keep_alive import keep_alive
from memes import Memes
from music import music
TOKEN = os.environ['TOKEN']


intents = discord.Intents.default()

intents.members = True
client = commands.Bot(command_prefix="-", intents=intents)

reddit = praw.Reddit(
    client_id="Xb8UffWk_E_3Sw",
    client_secret="YpwNrZRvIXG9wA93V3358BEhdmpjTQ",
    user_agent="SKYbot Discord Bot",
)
client.add_cog(Memes(client))
client.add_cog(music(client))

@client.command(name='announce')
@commands.has_permissions(administrator=True)
async def announce(ctx, *, content):
  myEmbed = discord.Embed(title="Announcement",
                            description=content,
                            color=0xffe603)
  myEmbed.set_footer(text="Sent by SKYbot")

  await ctx.send(embed=myEmbed)
  pingmessage = await ctx.send("@everyone")
  await ctx.message.delete
  await asyncio.sleep(1)
  pingmessage.delete

@client.command(name="embedtitle")
@commands.has_permissions(manage_guild=True)
async def customemblink(ctx,*, content):
  global emblink
  emblink=content
  await ctx.send(f"Embed Title Is Now {content}")

@client.command(name="customembed")
@commands.has_permissions(manage_guild=True)
async def customemb(ctx, *, content):
  myEmbed = discord.Embed(title=emblink,
                            description=content,
                            color=0xffe603)
  myEmbed.set_footer(text="Sent by SKYbot")
  await ctx.send(embed=myEmbed)

@client.command(name='8ball')
async def ball(ctx):
  response = ["maybe", "I have no idea", "definitely not", "Hell yeah", "Im Busy leave me alone", "no.", "yes.", "optomisticly, yes. truthfully, no", "Absolutely!"]
  await ctx.send(random.choice(response))

@client.command(name='config')
@commands.has_permissions(administrator=True)
async def config(ctx):
    await ctx.guild.create_text_channel('reports')
    channel = discord.utils.get(ctx.guild.channels, name='reports')
    channel_id = channel.id
    await channel.set_permissions(ctx.guild.default_role, view_channel=False)
    await ctx.send('success!')


@client.command(name='report')
async def report(ctx, Member: discord.Member, *, content: str):
      channel = discord.utils.get(ctx.guild.channels, name='reports')
      channel_id = channel.id
      myEmbed = discord.Embed(title="New report",
          description=f"Reporting {Member.mention} for {content}",
          color=0xffe603)
      myEmbed.set_footer(text="Sent by SKYbot")
      await channel.send(embed=myEmbed)

@client.command(name='dm')
async def dm(ctx, Member: discord.Member, *, content: str):
      await ctx.send(f'{Member.mention} has been dmed saying: {content}')
      await Member.send(f'you were dmed by {ctx.message.author}: {content}')

@client.command(name='warn')
@commands.has_permissions(kick_members=True)
async def warn(ctx, Member: discord.Member, *, content: str):
      await ctx.send(f'{Member.mention} has been warned for {content}')
      await Member.send(f'you were warned for {content}')

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason='dieloser'):

      await member.kick(reason=reason)

      await ctx.send(f'User {member.mention} has been kicked.')


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason='die_loser'):

      await member.ban(reason=reason)

      await ctx.send(f'User @{member.mention} has been banned.')

@client.command()
async def echo(ctx, *, content: str):
    myEmbed = discord.Embed(title="echoing",
                            description=content,
                            color=0xffe603)
    myEmbed.set_footer(text="Sent by SKYbot")

    await ctx.send(embed=myEmbed)
    await ctx.message.delete()

global pigs
pigs = 3

@client.command(name='set-link')
async def link(ctx, *, message):
   global link
   link = f'{message}'
   await ctx.send('Link is set to: ' + link)
   await ctx.message.delete()

@client.command()
async def flight(ctx, *, content: str):
     myEmbed = discord.Embed(
         title="Flight Announcement!",
         description=link,
         color=0xffe603)
     myEmbed.add_field(name="Flight Info:", value=content)
     myEmbed.set_footer(text="Sent by SKYbot")
     myEmbed.add_field(name='React with ✔️ to get your ticket', value=f'in {ctx.guild.name}')
     message = await ctx.send(embed=myEmbed)
     await message.add_reaction('✔️')
     await ctx.message.delete()
     global flightmsg
     flightmsg = message

@client.command(name='pollping')
async def pollping(ctx, content: str):
    global pollping
    pollping = content
    await ctx.send(f'Poll ping is now ```{pollping}```')

@client.command(name='poll')
@commands.has_permissions(manage_guild=True)
async def poll(ctx, *, content: str):
    myEmbed = discord.Embed(title="What do you think?", description=content)
    message = await ctx.send(f"<@&{pollping}>", embed=myEmbed)
    await message.add_reaction('👍')
    await message.add_reaction('👎')
    await ctx.message.delete()


@client.event 
async def on_reaction_add(Reaction, user): 
   if Reaction.message == flightmsg:
     await user.send(f"you haved booked your ticket for a flight in {Reaction.message.guild.name}")

@client.event
async def on_ready():
    print("online")
    for x in range(0, 9999999999999999999999999999999):
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for -help"))
      await asyncio.sleep(40)
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"over {len(client.guilds)} servers!"))
      await asyncio.sleep(40)
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="SKYBOT V2! Music And Embeds! "))
      await asyncio.sleep(40)
      
      
global GuildNum
GuildNum = client.guilds
from flask import Flask
app = Flask('/')
from threading import Thread
from flask import render_template
@app.route('/')
def home():
  return render_template("file.html", myvar=GuildNum)
    







INTENTS = discord.Intents.default()
x = 3
# Startup Information





@client.event
async def on_command_error(ctx, error):
  channel = client.get_channel(845040645118623765)
  await channel.send(f'error in {ctx.guild.name} by {ctx.author.name}:{error}')



@client.command(name='whois') #whois cmd
async def whois(ctx, member: discord.Member):

    avatar = str(member.avatar_url)

    id = str(member.id)

    name = str(member.name)

    tag = str(member.discriminator)

    joindate = member.created_at.strftime("%Y-%m-%d")
    serverdate = member.joined_at.strftime("%Y-%m-%d")
    roles = len(member.roles)

    Bembed = discord.Embed(
        title=name + "'s Information", color=0xffe603
    )
    Bembed.set_thumbnail(url=avatar)
    Bembed.add_field(name="User and Tag", value = name+"#"+tag, inline=True)
    Bembed.add_field(name="ID", value = id, inline=True)
    Bembed.add_field(name="Roles", value = roles, inline=False)
    Bembed.add_field(name="Date Registered", value = joindate, inline = True)
    Bembed.add_field(name="Date Joined", value = serverdate, inline = True)

    await ctx.send(embed=Bembed)



@client.command(name='therapy')
async def therapy(ctx):
    await ctx.send('so tell me how it all began')
    for x in range(0, 3):
        await asyncio.sleep(8)
        await ctx.send('and how did that make you feel')
    await asyncio.sleep(8)
    await ctx.send('now give me 10k in dank memer currency')


@client.command(name='ping')
async def ping(ctx):
    myEmbed = discord.Embed(title="you say ping",
                            description="i say pong!",
                            color=0xffe603)
    myEmbed.set_footer(text="Sent by SKYbot")

    await ctx.send(embed=myEmbed)


@client.command(name='invite')
async def invite(ctx):
    myEmbed = discord.Embed(
        title="hey do you like the bot?",
        description=
        "invite it here:https://discord.com/api/oauth2/authorize?client_id=798203593227501598&permissions=8&scope=bot",
        color=0xffe603)
    myEmbed.set_footer(text="Sent by SKYbot")

    await ctx.send(embed=myEmbed)


@client.command(name='hi')
async def hello(ctx):
    myEmbed = discord.Embed(title="hi!",
                            description="do you need friends too",
                            color=0xffe603)
    myEmbed.add_field(name="if you need mental help do ", value="-therapy")
    myEmbed.set_footer(text="Sent by SKYbot")

    await ctx.send(embed=myEmbed)



@client.command(name='spam')
@commands.has_permissions(kick_members=True)
async def spam(ctx):
    for y in range(0, 10):
        await ctx.send('spam')





@client.command(name='botcredits')
async def credits(ctx):
    await ctx.send('this bot was made by virt360#3086')



keep_alive()
client.run(TOKEN)