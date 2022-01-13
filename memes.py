import discord
from discord.ext import commands
import praw
reddit = praw.Reddit(
    client_id="Xb8UffWk_E_3Sw",
    client_secret="YpwNrZRvIXG9wA93V3358BEhdmpjTQ",
    user_agent="ASY3 Discord Bot",
)
intents = discord.Intents.default()

intents.members = True
client = commands.Bot(command_prefix="-", intents=intents)


class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.post_id = 0

    @commands.command(name='meme')
    async def command(self, ctx):
         
        i = 0
        thePost = None
        for post in reddit.subreddit("dankmemes").hot(limit=20):
            if i == self.post_id: 
                thePost = post
                break
            i += 1
        self.post_id += 1
        if self.post_id > 20: self.post_id = 0
        myEmbed = discord.Embed(title=post.title)
        myEmbed.set_image(url=post.url)
        await ctx.send(embed=myEmbed)