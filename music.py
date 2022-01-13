import discord
from discord.ext import commands
import youtube_dl
import urllib.request
import re
from requests import get
from youtube_dl import YoutubeDL

YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}


class music(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    
    
    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("You're not in a voice channel!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
            await ctx.send(f"Joined <#{voice_channel.id}>")
        else:
            await ctx.voice_client.move_to(voice_channel)
            await ctx.send(f"Joined <#{voice_channel.id}>")

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()
        await ctx.send("Left Channel")

    @commands.command()
    async def play(self, ctx, *, content):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format':"bestaudio"}
        vc = ctx.voice_client
        
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            content2=content.replace(" ", "_", )
            search_keyword=content2
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            finalvid = ("https://www.youtube.com/watch?v=" + video_ids[1])
            info = ydl.extract_info(finalvid, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)
            await ctx.send(f"Now Playing {finalvid}")
    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.send("Succesfully Paused")
    
    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.send("Sucessfully Resumed")

def setup(client):
    client.add_cog(music(client))