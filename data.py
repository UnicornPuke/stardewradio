import nextcord
from nextcord import ui
from stringcolor import *

class Universal:
    def __init__(self):
        self.Hate = '''```diff\n-- Hates:\n
All Bait
All Fossils
All Monster Loot (except Solar Essence and Void Essence)
All Trash (except Driftwood)
All Warp Totems
Artifact Trove
Blue Grass Starter
Bug Steak.png Bug Steak
Butterfly Powder
Carp
Cookout Kit
Copper Ore
Crab Pot
Dragon Tooth
Drum Block
Energy Tonic
Error Item
Explosive Ammo
Fairy Dust
Flute Block
Grass Starter
Green Algae
Golden Coconut
Golden Mystery Box
Golden Tag
Hay
Iron Ore
Journal Scrap
Monster Musk
Muscle Remedy
Mystery Box
Oil of Garlic
Poppy
Seasoning
Radioactive Bar
Radioactive Ore
Rain Totem
Red Mushroom
Sap
Sea Urchin
Seafoam Pudding
Seaweed
Secret Note
Slime Egg (any color)
Snail
Strange Bun
Sugar
Tent Kit
Torch
Void Mayonnaise
White Algae```'''
        self.Dislike = '''```diff\n- Dislikes:\n\nAll Building Materials -- Battery Packs, Clay, Fiber, Hardwood, Moss, Stone, and Wood
All Artifacts
All Bombs
All Crafted Floors & Paths
All Fences
All Fertilizer
All Fish (except Carp and Snails)
All Geode Minerals
All Geodes
All Seeds (including Fruit Tree Saplings, Tea Saplings, and Tree seeds)
All Sprinklers
All Tackle
All Trinkets
Fireworks
Misc. Mined/Metal Goods (Bone Fragment, Cinder Shard, Coal, Copper Bars, Gold Bars, Gold Ore, Iridium Bars, Iridium Ore, Iron Bars, and Refined Quartz)
Cave Carrot
Driftwood
Field Snack
Jack-O-Lantern
Oak Resin
Oil
Pine Tar
Price Catalogue
Qi Fruit
Rice
Solar Essence
Spring Onion
Tea Set
Unmilled Rice
Vinegar
Void Egg
Void Essence
Wheat Flour```'''
        self.Neutral = '''```Neutral:\n\nAll Books (Except Price Catalogue)
Bread
Coral
Duck Feather
Fried Egg
Hops
Mystic Syrup
Nautilus Shell
Roe
Squid Ink
Sweet Gem Berry
Tea Leaves
Truffle
Wool```'''
        self.Like = "```diff\n+ Likes:\n\nAll Artisan Goods (Except Oil and Void Mayonnaise)\nAll Cooking (Except Fried Egg, Bread, Strange Bun, and Seafom Pudding)\nAll Flowers (Except Poppy)\nAll Foraged Materials (Except Quartz)\nAll Fruit Tree Fruits (Except Banana and Mango)\nAll Gems (Except Prismatic Shards)\nAll Vegetables (Except Hops, Tea Leaves, Wheat, and Unmilled Rice)\nFiddlehead Fern\nMaple Syrup\nPiña Colada\nRainbow Shell\nTreasure Chest```"
        self.Love = "```diff\n++ Loves:\n\nGolden Pumpkin\nPearl\nPrismatic Shard\nRabbit's Foot\nStardrop Tea```"

class Alex:
    def __init__(self):
        self.Hate = '''```diff\n-- Hates:\n
All Universal Hates
Holly
Quartz```'''
        self.Dislike = '''```diff\n- Dislikes:\n
All Universal Dislikes (except Dinosaur Egg, Frog Egg, and Parrot Egg)
All Books (except Jack Be Nimble, Jack Be Thick)
Salmonberry
Wild Horseradish```'''
        self.Neutral = '''```Neutral:\n
All Universal Neutrals (except Books)
All Fruit (except Fruit Tree Fruit and Salmonberry)
All Milk
Chanterelle
Common Mushroom
Daffodil
Dandelion
Frog Egg
Ginger
Hazelnut
Leek
Magma Cap
Morel
Purple Mushroom
Snow Yam
Winter Root```'''
        self.Like = '''```diff\n+ Likes:
All Universal Likes
All Eggs (Except Void Egg)
Dinosaur Egg
Field Snack
Parrot Egg```'''
        self.Love = '''```diff\n++ Loves:\n
All Universal Loves
Complete Breakfast
Jack Be Nimble, Jack Be Thick
Salmon Dinner```'''

class Elliot:
    def __init__(self):
        self.Hate = '''```diff\n-- Hates:\n
All Universal Hates (except Sea Urchin)
Amaranth
Quartz
Salmonberry
Sea Cucumber*
Super Cucumber*

Elliot will return any Sea Cucumbers that are given to him.```'''
        self.Dislike = '''```diff\n- Dislikes:\n
All Universal Dislikes (except Fish)
All Milk
Chanterelle
Common Mushroom
Daffodil
Dandelion
Ginger
Hazelnut
Holly
Leek
Magma Cap
Morel
Pizza
Purple Mushroom
Snow Yam
Wild Horseradish
Winter Root```'''
        self.Neutral = '''```Neutral:\n
All Universal Neutrals (except Books, Duck Feather, and Squid Ink)
All Eggs (except Void Egg)*
All Fish (except Carp, Lobster, Octopus, Sea Cucumber, Snail, and Squid)
Rainbow Shell
Sea Urchin

*Dinosaur Eggs do not count as eggs, but artifacts```'''
        self.Like = '''```diff\n+ Likes:
All Universal Likes (except Amaranth, Pizza, and Rainbow Shell)
All Books
All Fruit (except Pomegranate and Salmonberry)
Octopus
Squid```'''
        self.Love = '''```diff\n++ Loves:\n
All Universal Loves
Crab Cakes
Duck Feather
Lobster
Pomegranate
Squid Ink
Tom Kha Soup```'''

class Like(ui.Select):
    def __init__(self, character):
        self.character=character
        options = [
            nextcord.SelectOption(label="Love", description="+80 Friendship Points", emoji="❤️"),
            nextcord.SelectOption(label="Like", description="+45 Friendship Points", emoji="👍"),
            nextcord.SelectOption(label="Neutral", description="+20 Friendship Points", emoji="🤷"),
            nextcord.SelectOption(label="Dislike", description="-20 Friendship Points", emoji="👎"),
            nextcord.SelectOption(label="Hate", description="-40 Friendship Points", emoji="💔"),
        ]
        super().__init__(placeholder="`Choose fields.`", options=options, min_values=1, max_values=5)

    async def callback(self, interaction):
        result = []
        results = ""
        for i in self.values:
            result.append(eval(f"{self.character}().{i}"))
        for i in self.values:
            results += eval(f"{self.character}().{i}")
        if len(results) < 2000:
            await interaction.response.send_message(results)
        else:
            await interaction.response.send_message(result[0])
            result.pop(0)
            for i in result:
                await interaction.followup.send(content=i)