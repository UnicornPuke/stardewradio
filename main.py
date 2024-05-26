# Imports
import os
from dotenv import load_dotenv
import asyncio
import sqlite3
import nextcord
import random
import nacl
import ffmpeg
import mutagen
from mutagen.mp3 import MP3
from mutagen.wave import WAVE

# Unpack Environment
load_dotenv("env/.env")
TOKEN = os.getenv("TOKEN")
SONGS = os.getenv("SONGS")

# Generate Programming
def generate_programming():
    total_time = 0
    track_1 = []
    track_2 = []
    track_3 = []

    morning = f"./assets/overlays/morning_{random.randint(1, 2)}.wav"
    morning_length = int(round(WAVE(morning).info.length, 3) * 1000)
    track_2.append(morning)
    track_1.append(morning_length)
    return ([track_1, track_2, track_3])

# Client Setup
intents = nextcord.Intents.all()
client = nextcord.Client(intents=intents, activity=nextcord.Game(name=' Stardew Valley Music'))

@client.slash_command(guild_ids=[1244302066600640613])
async def join(ctx):
    channel = ctx.user.voice.channel
    vc = await channel.connect()
    await ctx.send("Tuning in...")
    # vc.play(nextcord.FFmpegPCMAudio(executable="????", source="./assets/soundtrack/ConcernedApe - Stardew Valley OST - 01 Stardew Valley Overture.mp3"))

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
