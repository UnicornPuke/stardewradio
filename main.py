import os
from dotenv import load_dotenv
import asyncio
import sqlite3
import nextcord
import random
import nacl
import ffmpeg

# Get Token
load_dotenv("env/.env")
TOKEN = os.getenv("TOKEN")

# Client Setup
intents = nextcord.Intents.all()
client = nextcord.Client(intents=intents)

@client.slash_command(guild_ids=[1244302066600640613])
async def join(ctx):
    channel = ctx.user.voice.channel
    vc = await channel.connect()
    await ctx.send("Tuning in...")
    # vc.play(nextcord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="file.mp3"))

@client.slash_command(guild_ids=[1244302066600640613])
async def leave(ctx):   
    await ctx.guild.voice_client.disconnect()
    await ctx.send("Tuning out...")


@client.event
async def on_ready():
    print(f"Broadcasting as {client.user.name}")
    embed = nextcord.Embed(title=f"{client.user.name} is online", description="", color=0x9966CB)

@client.event
async def on_close():
    print(f"Terminating broadcast as {client.user.name}")
    embed = nextcord.Embed(title=f"{client.user.name} is offline", description="", color=0x9966CB)

# Client Run
client.run(TOKEN)
