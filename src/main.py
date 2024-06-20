# Imports
import os
from dotenv import load_dotenv
import asyncio
import nextcord
import random
import datetime
import os
import shutil
from datetime import time as checktime
from nextcord.utils import get
from mutagen.mp3 import MP3
# from mutagen.wave import WAVE
from datetime import timezone
import sys
import ffmpeg
import random
from stringcolor import *
from nextcord.ext import commands, tasks
from nextcord import ui
import characterdata
import itemdata
import pytz
tzpy = pytz.timezone('US/Eastern')
global tz
import sqlite3
from createdata import data
tz = timezone(datetime.timedelta(hours=-5) + datetime.datetime.now(tzpy).dst())

itemdata, cursor_obj, connection_obj = data()

# Client Setup
intents = nextcord.Intents.all()
client = commands.Bot(command_prefix="r!", intents=intents, activity=nextcord.Game(name=' Nothing'))
client.remove_command('help')

# @client.event
# async def on_command_error(ctx, error):
#     await ctx.send(f"```Error flagged: {error}```")

# @client.event
# async def on_application_command_error(ctx, error):
#     await ctx.send(f"```Error flagged: {error}```")

async def my_autocomplete(ctx, option: str):
    all_options = ['Amaranth','Amethyst','Aquamarine','Artichoke Dip',"Autumn's Bounty",'Baked Fish','Banana Pudding','Battery Pack','Bean Hotpot','Beer','Beet','Blackberry Cobbler','Blueberry','Blueberry Tart','Cactus Fruit','Carp Surprise','Catfish','Cauliflower','Cave Carrot','Chanterelle','Cheese Cauliflower','Chocolate Cake','Chowder','Clay','Cloth','Coconut','Coffee','Common Mushroom','Complete Breakfast', 'Copper Bar', 'Crab Cakes', 'Cranberry Candy', 'Crispy Bass', 'Crocus', 'Daffodil', 'Dandelion', 'Diamond', "Dish O' The Sea", 'Dragon Tooth', 'Driftwood', 'Duck Egg', 'Duck Feather', 'Eggplant Parmesan', 'Emerald', 'Escargot', 'Fairy Rose', "Farmer's Lunch", 'Fiddlehead Risotto', 'Fish Stew', 'Fish Taco', 'Flounder', 'Fried Calamari', 'Fried Eel', 'Fried Mushroom', 'Frozen Tear', 'Fruit Salad', 'Ginger', 'Ginger Ale', 'Glazed Yams', 'Goat Cheese', 'Goat Milk', 'Gold Bar', 'Grape', 'Green Tea', 'Hazelnut', 'Holly', 'Hot Pepper', 'Ice Cream', 'Iridium Bar', 'Jade', 'Jelly', 'Joja Cola', 'Large Goat Milk', 'Leek', 'Lemon Stone', 'Lingcod', 'Lobster', 'Lobster Bisque', 'Magma Cap', 'Mango', 'Mango Sticky Rice', 'Maple Bar', 'Mead', 'Melon', "Miner's Treat", 'Morel', 'Nautilus Shell', 'Oak Resin', 'Obsidian', 'Octopus', 'Omni Geode', 'Orange', 'Ostrich Egg', 'Pale Ale', 'Pancakes', 'Parsnip Soup', 'Peach', 'Pepper Poppers', 'Pickles', 'Piña Colada', 'Pine Tar', 'Pink Cake', 'Pizza', 'Plum Pudding', 'Poi', 'Pomegranate', 'Poppy', 'Poppyseed Muffin', 'Pufferfish', 'Pumpkin', 'Pumpkin Pie', 'Pumpkin Soup', 'Purple Mushroom', 'Quartz', 'Radioactive Bar', 'Radioactive Ore', 'Rainbow Shell', 'Red Plate', 'Rhubarb Pie', 'Rice Pudding', 'Roasted Hazelnuts', 'Roots Platter', 'Ruby', 'Salad', 'Salmon Dinner', 'Sandfish', 'Sashimi', 'Sea Cucumber', 'Sea Urchin', 'Seafoam Pudding', 'Snail', 'Snow Yam', 'Solar Essence', 'Spaghetti', 'Spice Berry', 'Spicy Eel', 'Squid', 'Squid Ink', 'Stir Fry', 'Strawberry', 'Stuffing', 'Sturgeon', 'Sugar', 'Summer Spangle', 'Sunflower', 'Super Cucumber', 'Super Meal', 'Survival Burger', 'Sweet Pea', 'Tea Leaves', 'Tiger Trout', 'Tigerseye', 'Tom Kha Soup', 'Topaz', 'Tropical Curry', 'Trout Soup', 'Truffle', 'Truffle Oil', 'Tulip', 'Vegetable Medley', 'Void Egg', 'Void Essence', 'Void Mayonnaise', 'Wild Horseradish', 'Wine', 'Winter Root', 'Wool', 'Yam']  # Your full list
    filtered_options = [i for i in all_options if i.lower().startswith(option.lower())]
    return filtered_options[:25]  # Slice to return only 25 options

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

def round_seconds(obj: datetime.datetime) -> datetime.datetime:
    if obj.microsecond >= 500_000:
        obj += datetime.timedelta(seconds=1)
    return obj.replace(microsecond=0)

async def timers(current_song_length, timer):
    while timer < current_song_length:
        timer += 1
        await asyncio.sleep(1)

async def play_song(song_count):
    global current_song
    global timer
    song_count += 1
    current_song = track1[song_count]
    current_song_length = int(round(MP3(current_song).info.length))
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.playing, name=SONGNAMES[SONGS.index(current_song.replace("./assets/soundtrack/", ""))]))
    voice_client=[]
    for guild in client.guilds:
        if not get(client.voice_clients, guild=guild):
            continue
        voice_client.append(get(client.voice_clients, guild=guild))

    for i in voice_client:
        i.stop()
        i.play(nextcord.FFmpegPCMAudio(current_song))
    print(f'{cs(str(datetime.datetime.now(tz).replace(microsecond=0)) + ":", "green")} Playing {SONGNAMES[SONGS.index(current_song.replace("./assets/soundtrack/", ""))]} for {datetime.timedelta(seconds=current_song_length)}')
    global timer
    timer = 0
    current_song_length = int(round(MP3(current_song).info.length))
    task = asyncio.create_task(timers(current_song_length, timer))
    try:
        await task
    except asyncio.CancelledError:
        pass

    return song_count

async def loop(track_1, song_count, current_song):
    while song_count < len(track_1) - 1 and datetime.datetime.now(tz).hour < 21:
        song_count = await play_song(song_count)

async def joinup(ctx):
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    if current_song != "":
        rand = random.randint(0, 100000)
        audio_input = ffmpeg.input(current_song)
        audio_cut = audio_input.audio.filter('atrim', start=timer)
        audio_output = ffmpeg.output(audio_cut, f'./assets/trims/out{rand}.mp3', loglevel="quiet")
        ffmpeg.run(audio_output)
        vc.play(nextcord.FFmpegPCMAudio(f'./assets/trims/out{rand}.mp3'))
        return f'./assets/trims/out{rand}.mp3'
    return None

def cleartrims():
    print(f"{cs(str(datetime.datetime.now(tz).replace(microsecond=0)) + ':', 'green')} Cleared ./assets/trims contents")
    folder = './assets/trims'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"{cs(str(datetime.datetime.now(tz).replace(microsecond=0)) + ':', 'red')} Failed to delete {file_path}. Reason: {e}")

@client.event
async def on_ready():
    print(f"{cs(str(datetime.datetime.now(tz).replace(microsecond=0)) + ':', 'green')} Broadcasting as {client.user.name}")
    client.add_cog(DailyAction(client))
    global current_song
    current_song = ""

class DailyAction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.generate_programming.start()
        self.play.start()
        self.clear.start()
        self.stop.start()

    @tasks.loop(time=checktime(16, 39, 00, tzinfo=tz))
    async def generate_programming(self):
        total_time = 0
        track_1 = []
        track_2 = []
        track_3 = []
        times = []

        # morning = nextcord.FFmpegPCMAudio(source = f"./assets/overlays/morning_{random.randint(1, 2)}.wav")
        # morning_length = int(round(WAVE(f"./assets/overlays/morning_{random.randint(1, 2)}.wav").info.length, 3) * 1000)
        # track_2.append(morning)
        # track_1.append(morning_length)
        # total_time += morning_length
        recent_songs = []
        while total_time < 46800:
            num = random.randint(0,99)
            while num in recent_songs:
                num = random.randint(0,99)
            recent_songs.append(num)
            if len(recent_songs) > 10:
                recent_songs.pop(0)
            song = f"./assets/soundtrack/{SONGS[num]}"
            song_length = int(round(MP3(f"./assets/soundtrack/{SONGS[num]}").info.length))
            if song_length <= 60:
                song_length *= 4
                track_1.extend([song, song, song, song])
                times.extend([total_time, total_time, total_time, total_time])
            elif song_length <= 100:
                song_length *= 2
                track_1.extend([song, song])
                times.extend([total_time, total_time])
            else:
                track_1.append(song)
                times.append(total_time)
            track_2.append(song_length)
            total_time += song_length
        global track1 
        track1 = track_1
        global track2
        track2 = track_2
        global track3 
        track3 = track_3
        global programs
        programs = times
        global total_program
        total_program = total_time
        print(f"{cs(str(datetime.datetime.now(tz).replace(microsecond=0)) + ':', 'green')} Programming generated, going live in {datetime.datetime(int(datetime.datetime.now(tz).year), int(datetime.datetime.now(tz).month), int(datetime.datetime.now(tz).day), 8,00,0,tzinfo=tz) - datetime.datetime.now(tz).replace(microsecond=0)}")
        return track_1, track_2, track_3, times, total_time

    @tasks.loop(time=checktime(16, 40, 0, tzinfo=tz))
    async def play(self):
        global current_song
        song_count = -1
        current_song_length = int(round(MP3(track1[song_count]).info.length))
        print(f'{cs(str(datetime.datetime.now(tz).replace(microsecond=0)) + ":", "green")} Starting daily broadcast')
        task = asyncio.create_task(loop(track1, song_count, current_song_length))
        self.loop = task
        try:
            await task
        except asyncio.CancelledError:
            task.cancel()
        current_song = ""

    @tasks.loop(time=checktime(21, 00, 0, tzinfo=tz))
    async def stop(self):
        self.loop.cancel()
        voice_client=[]
        for guild in client.guilds:
            if not get(client.voice_clients, guild=guild):
                continue
            voice_client.append(get(client.voice_clients, guild=guild))

        for i in voice_client:
            i.stop()
        sys.stdout.write('\033[2K\033[1G')
        print(f'{cs(str(datetime.datetime.now(tz).replace(microsecond=0)) + ":", "green")} Terminating daily broadcast')
        await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.playing, name="Nothing"))
        current_song = ""
        tz = timezone(datetime.timedelta(hours=-5) + datetime.datetime.now(tzpy).dst())

    @tasks.loop(minutes=30)
    async def clear(self):
        cleartrims()

@client.command(aliases=["changevolume"], description= "Changes the volume of the radio.")
async def volume(ctx, new_volume=None):
    if new_volume == None:
        await ctx.channel.send('```Please enter a whole number.```')
        return
    try:
        int(new_volume)
    except:
        await ctx.channel.send('```Please enter a whole number.```')
        return
    if 0 <= int(new_volume) <= 100:
        new_volume = int(new_volume) / 100
        if not ctx.guild.voice_client:
            await ctx.channel.send('```There is no channel connected.```')
        elif not ctx.guild.voice_client.source:
            await ctx.channel.send('```There is no song playing.```')
        else:
            ctx.guild.voice_client.source.volume = new_volume
            await ctx.channel.send(f'```Set the volume to {new_volume}.```')
    else:
        await ctx.channel.send('```Please enter a number between 0 and 100.```')

@client.slash_command(description="Shows you an item's data",guild_ids=[1244302066600640613])
async def items(ctx: nextcord.Interaction, item: str = nextcord.SlashOption(autocomplete_callback=my_autocomplete)):
    people = ['Abigail',	'Alex',	'Caroline',	'Clint',	'Demetrius',	'Dwarf',	'Elliott',	'Emily',	'Evelyn',	'George',	'Gus',	'Haley',	'Harvey',	'Jas',	'Jodi',	'Kent',	'Krobus',	'Leah',	'Leo',	'Lewis',	'Linus',	'Marnie',	'Maru',	'Pam',	'Penny',	'Pierre',	'Robin',	'Sam',	'Sandy',	'Sebastian',	'Shane',	'Vincent',	'Willy',	'Wizard',]
    cursor_obj.execute("SELECT [%s] FROM [cooltable]" % item) 
    oliked = cursor_obj.fetchall()
    liked = []
    for i in oliked:
        liked.append(i[0])
    Lovei = []
    Likei = []
    Neutrali = []
    Dislikei = []
    Hatei = []
    count = 0
    for i in liked:
        exec(f'{i}i.append("{people[count]}")')
        count += 1
    Love = "```"
    Like = "```"
    Neutral = "```"
    Dislike = "```"
    Hate = "```"
    for i in Lovei:
        Love += f"\n{i}\t"
    for i in Likei:
        Like += f"\n{i}\t"
    for i in Neutrali:
        Neutral += f"\n{i}\t"
    for i in Dislikei:
        Dislike += f"\n{i}\t"
    for i in Hatei:
        Hate += f"\n{i}\t"
    Love += " ```"
    Like += " ```"
    Hate += " ```"

    count1 = Neutral.count("\n")
    count2 = Dislike.count("\n")

    if count1 < count2:
        if count1 == 0:
            countthing = 1
        else:
            countthing = 0
        for i in range(countthing, count2-count1):
            Neutral += "\t\n"
    else:
        if count2 == 0:
            countthing = 1
        else:
            countthing = 0
        for i in range(countthing, count1-count2):
            Dislike += "\t\n"

    Neutral += " ```"
    Dislike += " ```"


    embed = nextcord.Embed(title=item, color=0x70c725)
    embed.add_field(name="Loves", value=Love, inline= False)
    embed.add_field(name="Likes", value=Like, inline= False)
    embed.add_field(name="Neutral", value=Neutral)
    embed.add_field(name="Dislikes", value=Dislike)
    embed.add_field(name="Hates", value=Hate, inline= False)
    await ctx.send(embed=embed)

@client.command(description= "Sets the radio volume to zero.")
async def mute(ctx):
    if not ctx.guild.voice_client:
        await ctx.channel.send('```There is no channel connected.```')
    elif not ctx.guild.voice_client.source:
        await ctx.channel.send('```There is no song playing.```')
    else:
        ctx.guild.voice_client.source.volume = 0

@client.command(aliases=["tunein", "connect"], description= "Connects the bot to a voice channel.")
async def join(ctx):
    if ctx.author.voice == None:
        await ctx.channel.send("```There is no channel to tune into.```")
    elif ctx.guild.voice_client: 
        if ctx.guild.voice_client.channel == ctx.user.voice.channel:
            await ctx.channel.send("```I am already in.```")
        else:
            await ctx.guild.voice_client.disconnect()
            out = await joinup(ctx)
            await ctx.channel.send("```Joining...```")
    else:
        out = await joinup(ctx)
        await ctx.channel.send("```Joining...```")
            
@client.command(aliases=["tuneout", "disconnect"], description= "Disconnects the bot from a voice channel.")
async def leave(ctx):
    cursor_obj.close()
    if ctx.guild.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.channel.send("```Leaving...```")
    else:
        await ctx.channel.send("```There is no channel to tune out of.```")

@client.slash_command(description="Shows you a character's gift chart.", guild_ids=[1244302066600640613])
async def gifts(ctx: nextcord.Interaction, character: str = nextcord.SlashOption(name="character", description="A character to choose from", choices=["Universal", "Alex", "Elliot", "Harvey", "Sam", "Sebastian", "Shane", "Abigail", "Haley", "Leah", "Maru", "Penny", "Emily"])):
    view = ui.View()
    view.add_item(characterdata.Like(character))

    await ctx.send(f"```Choose fields for {character}. You have 15 seconds.```", view=view, delete_after=15, ephemeral=True)

@client.slash_command(description="Shows this message.", guild_ids=[1244302066600640613])
async def help(ctx, command: str = nextcord.SlashOption(name="command", description="The bot's commands or categories", choices=["Home", "Radio Control", "Setup", "Tips", "mute", "volume", "join", "leave", "gifts", "help"])):
    if command == "Home":
        await ctx.send('''
```Radio Control:
  mute   Sets the radio volume to zero.
  volume Changes the volume of the radio.
Setup:
  join   Connects the bot to a voice channel.
  leave  Disconnects the bot from a voice channel.
Tips:
  /gifts Shows you a character's gift chart.
Other:
  /help  Shows this message.

Type /help command for more info on a command.
You can also type /help category for more info on a category
Any command marked with a / is a slash command.```
''')
    elif command == "Radio Control":
        await ctx.send('''
```Radio Control:
  mute   Sets the radio volume to zero.
  volume Changes the volume of the radio.```
''')
    elif command == "Setup":
        await ctx.send('''
```Setup:
  join   Connects the bot to a voice channel
  leave  Disconnects the bot from a voice channel.```
''')
    elif command == "Tips":
        await ctx.send('''
```Tips:
  /gifts Shows you a character's gift chart.```
''')
    elif command == "volume":
        await ctx.send('''
```Aliases: changevolume

r!volume <new_volume>

Changes the volume of the radio.```
''')
    elif command == "gifts":
        await ctx.send('''
```/gifts <character>

Shows you a character's gift chart.```
''')
    elif command == "help":
        await ctx.send('''
```/help

Shows this message.```
''')
    else:
        desc = eval(f"getattr({command}, 'description')")
        await ctx.send(f'''
```r!{command}

{desc}```
''')

        
@client.event
async def on_close():
    voice_client=[]
    for guild in client.guilds:
        if not get(client.voice_clients, guild=guild):
            continue
        voice_client.append(get(client.voice_clients, guild=guild))

    for i in voice_client:
        await i.disconnect()

    sys.stdout.write('\033[2K\033[1G')

    print(f"{cs(str(datetime.datetime.now(tz).replace(microsecond=0)) + ':', 'red')} Terminating broadcast as {client.user.name}")
    # print(tasks)
    # sys.exit()
    embed = nextcord.Embed(title=f"{client.user.name} is offline", description="", color=0x9966CB)

# Client Run
client.run(TOKEN)
