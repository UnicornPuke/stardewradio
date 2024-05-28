# Imports
import os
from dotenv import load_dotenv
import asyncio
import nextcord
import random
import nacl
import ffmpeg
from mutagen.mp3 import MP3
from mutagen.wave import WAVE
import math

# Constants
load_dotenv("env/.env")
TOKEN = os.getenv("TOKEN")
SONGS = ['ConcernedApe - Stardew Valley OST - 01 Stardew Valley Overture.mp3', 'ConcernedApe - Stardew Valley OST - 02 Cloud Country.mp3', "ConcernedApe - Stardew Valley OST - 03 Grandpa's Theme.mp3", 'ConcernedApe - Stardew Valley OST - 04 Settling In.mp3', "ConcernedApe - Stardew Valley OST - 05 Spring (It's A Big World Outside).mp3", 'ConcernedApe - Stardew Valley OST - 06 Spring (The Valley Comes Alive).mp3', 'ConcernedApe - Stardew Valley OST - 07 Spring (Wild Horseradish Jam).mp3', 'ConcernedApe - Stardew Valley OST - 08 Pelican Town.mp3', 'ConcernedApe - Stardew Valley OST - 09 Flower Dance.mp3', 'ConcernedApe - Stardew Valley OST - 10 Fun Festival.mp3', 'ConcernedApe - Stardew Valley OST - 11 Distant Banjo.mp3', "ConcernedApe - Stardew Valley OST - 12 A Glimpse Of The Other World (Wizard's Theme).mp3", "ConcernedApe - Stardew Valley OST - 13 Summer (Nature's Crescendo).mp3", 'ConcernedApe - Stardew Valley OST - 14 Summer (The Sun Can Bend An Orange Sky).mp3', 'ConcernedApe - Stardew Valley OST - 15 Summer (Tropicala).mp3', 'ConcernedApe - Stardew Valley OST - 16 The Adventure Guild.mp3', 'ConcernedApe - Stardew Valley OST - 17 The Stardrop Saloon.mp3', 'ConcernedApe - Stardew Valley OST - 18 Luau Festival.mp3', 'ConcernedApe - Stardew Valley OST - 19 Dance Of The Moonlight Jellies.mp3', 'ConcernedApe - Stardew Valley OST - 20 Fall (The Smell Of Mushroom).mp3', 'ConcernedApe - Stardew Valley OST - 21 Fall (Ghost Synth).mp3', "ConcernedApe - Stardew Valley OST - 22 Fall (Raven's Descent).mp3", 'ConcernedApe - Stardew Valley OST - 23 The Library And Museum.mp3', 'ConcernedApe - Stardew Valley OST - 24 Stardew Valley Fair Theme.mp3', 'ConcernedApe - Stardew Valley OST - 25 Festival Game.mp3', "ConcernedApe - Stardew Valley OST - 26 Spirit's Eve Festival.mp3", 'ConcernedApe - Stardew Valley OST - 27 Winter (Nocturne Of Ice).mp3', 'ConcernedApe - Stardew Valley OST - 28 Winter (The Wind Can Be Still).mp3', 'ConcernedApe - Stardew Valley OST - 29 Winter (Ancient).mp3', 'ConcernedApe - Stardew Valley OST - 30 Winter Festival.mp3', 'ConcernedApe - Stardew Valley OST - 31 A Golden Star Is Born.mp3', 'ConcernedApe - Stardew Valley OST - 32 Country Shop.mp3', 'ConcernedApe - Stardew Valley OST - 33 Night Market.mp3', 'ConcernedApe - Stardew Valley OST - 34 Submarine Theme.mp3', 'ConcernedApe - Stardew Valley OST - 35 Mermaid Song.mp3', 'ConcernedApe - Stardew Valley OST - 36 Calico Desert.mp3', 'ConcernedApe - Stardew Valley OST - 37 Playful.mp3', 'ConcernedApe - Stardew Valley OST - 38 Buttercup Melody.mp3', "ConcernedApe - Stardew Valley OST - 39 Pleasant Memory (Penny's Theme).mp3", "ConcernedApe - Stardew Valley OST - 40 Piano Solo (Elliott's Theme).mp3", "ConcernedApe - Stardew Valley OST - 41 Land Of Green and Gold (Leah's Theme).mp3", "ConcernedApe - Stardew Valley OST - 42 A Stillness In The Rain (Abigail's Melody).mp3", "ConcernedApe - Stardew Valley OST - 43 Starwatcher (Maru's Theme).mp3", "ConcernedApe - Stardew Valley OST - 44 A Sad Song (Alex's Theme).mp3", "ConcernedApe - Stardew Valley OST - 45 Pickle Jar Rag (Haley's Theme).mp3", "ConcernedApe - Stardew Valley OST - 46 Echos (Sebastian's Theme).mp3", "ConcernedApe - Stardew Valley OST - 47 Grapefruit Sky (Dr. Harvey's Theme).mp3", "ConcernedApe - Stardew Valley OST - 48 Frozen Pizza And Eggs (Shane's Theme).mp3", "ConcernedApe - Stardew Valley OST - 49 Song Of Feathers (Emily's Theme).mp3", 'ConcernedApe - Stardew Valley OST - 50 Dreamscape.mp3', "ConcernedApe - Stardew Valley OST - 51 Emily's Dance.mp3", "ConcernedApe - Stardew Valley OST - 52 Alex's Keepsake.mp3", 'ConcernedApe - Stardew Valley OST - 53 Band Practice.mp3', "ConcernedApe - Stardew Valley OST - 54 Sam's Band (Electronic Version).mp3", "ConcernedApe - Stardew Valley OST - 55 Sam's Band (Pop Version).mp3", "ConcernedApe - Stardew Valley OST - 56 Sam's Band (Bluegrass Version).mp3", "ConcernedApe - Stardew Valley OST - 57 Sam's Band (Heavy Version).mp3", 'ConcernedApe - Stardew Valley OST - 58 A Dark Corner Of The Past.mp3', 'ConcernedApe - Stardew Valley OST - 59 Music Box Song.mp3', 'ConcernedApe - Stardew Valley OST - 60 Jaunty.mp3', 'ConcernedApe - Stardew Valley OST - 61 Violin Solo.mp3', 'ConcernedApe - Stardew Valley OST - 62 Wedding Celebration.mp3', 'ConcernedApe - Stardew Valley OST - 63 Mines (Crystal Bells).mp3', 'ConcernedApe - Stardew Valley OST - 64 Mines (A Flicker In The Deep).mp3', 'ConcernedApe - Stardew Valley OST - 65 Mines (Star Lumpy).mp3', 'ConcernedApe - Stardew Valley OST - 66 Mines (Icicles).mp3', 'ConcernedApe - Stardew Valley OST - 67 Mines (Marimba Of Frozen Bones).mp3', 'ConcernedApe - Stardew Valley OST - 68 Mines (Cloth).mp3', 'ConcernedApe - Stardew Valley OST - 69 Mines (Visitor To The Unknown).mp3', 'ConcernedApe - Stardew Valley OST - 70 Mines (The Lava Dwellers).mp3', 'ConcernedApe - Stardew Valley OST - 71 Mines (Magical Shoes).mp3', 'ConcernedApe - Stardew Valley OST - 72 Mines (Danger!).mp3', 'ConcernedApe - Stardew Valley OST - 73 In The Deep Woods.mp3', 'ConcernedApe - Stardew Valley OST - 74 Journey Of The Prairie King (Overworld).mp3', 'ConcernedApe - Stardew Valley OST - 75 Journey Of The Prairie King (The Outlaw).mp3', 'ConcernedApe - Stardew Valley OST - 76 Journey Of The Prairie King (Final Boss & Ending).mp3', 'ConcernedApe - Stardew Valley OST - 77 Load Game.mp3', 'ConcernedApe - Stardew Valley OST - 78 Sun Room (Alone With Relaxing Tea).mp3', 'ConcernedApe - Stardew Valley OST - 79 Grapefruit Sky (Pasta Primavera Mix).mp3', 'ConcernedApe - Stardew Valley OST - 80 The Happy Junimo Show Theme.mp3', 'ConcernedApe - Stardew Valley OST - 81 Movie Theater.mp3', 'ConcernedApe - Stardew Valley OST - 82 Crane Game.mp3', 'ConcernedApe - Stardew Valley OST - 83 Wumbus (Movie Theme).mp3', 'ConcernedApe - Stardew Valley OST - 84 Exploring Our Vibrant World (Movie Theme).mp3', 'ConcernedApe - Stardew Valley OST - 85 The Zuzu City Express (Movie Theme).mp3', 'ConcernedApe - Stardew Valley OST - 86 Movie Theater (Closing Time).mp3', 'ConcernedApe - Stardew Valley OST - 87 JunimoKart (Title Theme).mp3', 'ConcernedApe - Stardew Valley OST - 88 JunimoKart (The Gem Sea Giant).mp3', "ConcernedApe - Stardew Valley OST - 89 JunimoKart (Slomp's Stomp).mp3", 'ConcernedApe - Stardew Valley OST - 90 JunimoKart (Ghastly Galleon).mp3', 'ConcernedApe - Stardew Valley OST - 91 JunimoKart (Glowshroom Grotto).mp3', 'ConcernedApe - Stardew Valley OST - 92 Ginger Island.mp3', "ConcernedApe - Stardew Valley OST - 93 Professor Snail's Radio.mp3", 'ConcernedApe - Stardew Valley OST - 94 Volcano Mines (Molten Jelly).mp3', 'ConcernedApe - Stardew Valley OST - 95 Volcano Mines (Forgotten World).mp3', 'ConcernedApe - Stardew Valley OST - 96 Mystery Of The Caldera.mp3', "ConcernedApe - Stardew Valley OST - 97 The Gourmand's Cave.mp3", 'ConcernedApe - Stardew Valley OST - 98 Pirate Theme.mp3', "ConcernedApe - Stardew Valley OST - 99 Leo's Song.mp3", 'ConcernedApe - Stardew Valley OST - 100 Summit Celebration.mp3']
temp = []
for i in SONGS:
    curn = i
    curn = curn.replace("ConcernedApe - Stardew Valley OST - ", "")
    curn = curn.replace(".mp3", "")
    if curn == "100 Summit Celebration":
        curn = curn[4:]
    else:
        curn = curn[3:]
    temp.append(curn)
SONGNAMES = temp

# Generate Programming
def generate_programming(start):
    total_time = 0
    track_1 = []
    track_2 = []
    track_3 = []
    times = []

    morning = nextcord.FFmpegPCMAudio(source = start)
    morning_length = int(round(WAVE(start).info.length, 3) * 1000)
    track_2.append(morning)
    track_1.append(morning_length)
    total_time += morning_length
    recent_songs = []
    while total_time < 3600000:
        num = random.randint(0,99)
        while num in recent_songs:
            num = random.randint(0,99)
        recent_songs.append(num)
        if len(recent_songs) > 10:
            recent_songs.pop(0)
        song = nextcord.FFmpegPCMAudio(source = f"./assets/soundtrack/{SONGS[num]}")
        song_length = int(round(MP3(f"./assets/soundtrack/{SONGS[num]}").info.length, 3) * 1000)
        if song_length <= 60000:
            song_length *= 4
            track_1.append(song)
            track_1.append(song)
            track_1.append(song)
            track_1.append(song)
            times.append(total_time)
            times.append(total_time)
            times.append(total_time)
            times.append(total_time)
        elif song_length <= 120000:
            song_length *= 2
            track_1.append(song)
            track_1.append(song)
            times.append(total_time)
            times.append(total_time)
        else:
            track_1.append(song)
            times.append(total_time)
        track_2.append(song_length)
        total_time += song_length

    return track_1, track_2, track_3, times, total_time

generate_programming(f"./assets/overlays/morning_{random.randint(1, 2)}.wav")

# Client Setup
intents = nextcord.Intents.all()
client = nextcord.Client(intents=intents, activity=nextcord.Game(name=' Nothing'))

@client.slash_command(guild_ids=[1244302066600640613])
async def join(ctx):
    if ctx.user.voice == None:
        await ctx.send("There is no channel to tune into.")
    elif ctx.guild.voice_client: 
        if ctx.guild.voice_client.channel == ctx.user.voice.channel:
            await ctx.send("I am already tuned in.")
        else:
            await ctx.guild.voice_client.disconnect()
            channel = ctx.user.voice.channel
            vc = await channel.connect()
            await ctx.send("Tuning in...")
    else:
        channel = ctx.user.voice.channel
        vc = await channel.connect()
        # if not os.path.exists("out_merger.mp3"):
        #     audio_output = ffmpeg.concat(ffmpeg.input("./assets/overlays/morning_2.wav"), ffmpeg.input("./assets/overlays/morning_1.wav"), v=0, a=1).output('out_merger.mp3')
        #     ffmpeg.run(audio_output)
        # vc.play(nextcord.FFmpegPCMAudio(source = f"out_merger.mp3"))
        await ctx.send("Tuning in...")

@client.slash_command(guild_ids=[1244302066600640613])
async def leave(ctx):   
    if ctx.guild.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Tuning out...")
    else:
        await ctx.send("There is no channel to tune out.")


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
