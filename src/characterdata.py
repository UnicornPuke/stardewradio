import nextcord
from nextcord import ui
from stringcolor import *

class Universal:
    def __init__(self):
        self.Hate = '''```\n\n
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
        self.Dislike = '''```\n\n\nAll Building Materials -- Battery Packs, Clay, Fiber, Hardwood, Moss, Stone, and Wood
All Artifacts
All Bombs
All Crafted Floors and Paths
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
        self.Neutral = '''```\n\nAll Books (except Price Catalogue)
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
        self.Like = "```\n\n\nAll Artisan Goods (except Oil and Void Mayonnaise)\nAll Cooking (except Fried Egg, Bread, Strange Bun, and Seafom Pudding)\nAll Flowers (except Poppy)\nAll Foraged Materials (except Quartz)\nAll Fruit Tree Fruits (except Banana and Mango)\nAll Gems (except Prismatic Shards)\nAll Vegetables (except Hops, Tea Leaves, Wheat, and Unmilled Rice)\nFiddlehead Fern\nMaple Syrup\nPiña Colada\nRainbow Shell\nTreasure Chest```"
        self.Love = "```\n\n\nGolden Pumpkin\nPearl\nPrismatic Shard\nRabbit's Foot\nStardrop Tea```"

class Alex:
    def __init__(self):
        self.Hate = '''```\n\n
All Universal Hates
Holly
Quartz```'''
        self.Dislike = '''```\n\n
All Universal Dislikes (except Dinosaur Egg, Frog Egg, and Parrot Egg)
All Books (except Jack Be Nimble, Jack Be Thick)
Salmonberry
Wild Horseradish```'''
        self.Neutral = '''```\n
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
        self.Like = '''```\n
All Universal Likes
All Eggs (except Void Egg)
Dinosaur Egg
Field Snack
Parrot Egg```'''
        self.Love = '''```\n\n
All Universal Loves
Complete Breakfast
Jack Be Nimble, Jack Be Thick
Salmon Dinner```'''

class Harvey:
    def __init__(self):
        self.Hate = '''```\n\n
All Universal Hates
Coral
Nautilus Shell
Rainbow Shell
Salmonberry
Spice Berry```'''
        self.Dislike = '''```\n\n
All Universal Dislikes (except Spring Onion)
Blueberry Tart
Bread
Cheese
Chocolate Cake
Cookie
Cranberry Sauce
Fried Mushroom
Glazed Yams
Goat Cheese
Hashbrowns
Ice Cream
Pancakes
Pink Cake
Pizza
Rhubarb Pie
Rice Pudding```'''
        self.Neutral = '''```\n
All Universal Neutrals (except Bread, Coral, Duck Feather, and Nautilus Shell)
All Eggs (except Duck Egg and Void Egg)*
Large Milk
Milk

*Dinosaur Eggs do not count as eggs, but artifacts.```'''
        self.Like = '''```\n
All Universal Likes (except Cheese, Goat Cheese, Rainbow Shell, and the following cooked dishes: Blueberry Tart, Chocolate Cake, Cookie, Cranberry Sauce, Fried Mushroom, Glazed Yams, Hashbrowns, Ice Cream, Pancakes, Pink Cake, Pizza, Rhubarb Pie, and Rice Pudding)
All Fruit (except Salmonberry and Spice Berry)
Chanterelle
Common Mushroom
Daffodil
Dandelion
Duck Egg
Duck Feather
Ginger
Goat Milk
Hazelnut
Holly
Large Goat Milk
Leek
Magma Cap
Morel
Purple Mushroom
Quartz
Snow Yam
Spring Onion
Wild Horseradish
Winter Root```'''
        self.Love = '''```\n\n
All Universal Loves
Coffee
Pickles
Super Meal
Truffle Oil
Wine```'''

class Elliot:
    def __init__(self):
        self.Hate = '''```\n\n
All Universal Hates (except Sea Urchin)
Amaranth
Quartz
Salmonberry
Sea Cucumber*
Super Cucumber*

Elliot will return any Sea Cucumbers that are given to him.```'''
        self.Dislike = '''```\n\n
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
        self.Neutral = '''```\n
All Universal Neutrals (except Books, Duck Feather, and Squid Ink)
All Eggs (except Void Egg)*
All Fish (except Carp, Lobster, Octopus, Sea Cucumber, Snail, and Squid)
Rainbow Shell
Sea Urchin

*Dinosaur Eggs do not count as eggs, but artifacts```'''
        self.Like = '''```\n
All Universal Likes (except Amaranth, Pizza, and Rainbow Shell)
All Books
All Fruit (except Pomegranate and Salmonberry)
Octopus
Squid```'''
        self.Love = '''```\n\n
All Universal Loves
Crab Cakes
Duck Feather
Lobster
Pomegranate
Squid Ink
Tom Kha Soup```'''

class Sam:
    def __init__(self):
        self.Hate = '''```\n\n
All Universal Hates (except Joja Cola and Seaweed)
Bone Fragment
Cinder Shard
Coal
Copper Bar
Duck Mayonnaise
Gold Bar
Gold Ore
Iridium Bar
Iridium Ore
Iron Bar
Mayonnaise
Pickles
Refined Quartz```'''
        self.Dislike = '''```\n\n
All Universal Dislikes (except Bone Fragment, Cinder Shard, Coal, Copper Bar, Gold Bar, Gold Ore, Iridium Bar, Iridium Ore, Iron Bar, Refined Quartz, and Tigerseye)
All Vegetables (except Hops, Tea Leaves, and Wheat)
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
Purple Mushroom
Quartz
Salmonberry
Seaweed
Snow Yam
Wild Horseradish
Winter Root```'''
        self.Neutral = '''```\n
All Universal Neutrals
All Fruit (except Cactus Fruit, Fruit Tree Fruit, and Salmonberry)
All Milk```'''
        self.Like = '''```\n
All Universal Likes (except Duck Mayonnaise, Mayonnaise, Pickles, and Vegetables)
All Eggs (except Void Egg)*
Joja Cola

*Dinosaur Eggs do not count as eggs, but artifacts```'''
        self.Love = '''```\n\n
All Universal Loves
Cactus Fruit
Maple Bar
Pizza
Tigerseye```'''

class Sebastian:
    def __init__(self):
        self.Hate = '''```\n\n
All Universal Hates
All Artisan Goods (except Coffee, Green Tea, and Oil)
All Eggs (except Void Egg)*
Clay
Complete Breakfast
Farmer's Lunch
Omelet
Piña Colada

*Dinosaur Eggs do not count as eggs, but artifacts.```'''
        self.Dislike = '''```\n\n
All Universal Dislikes (except Clay, Fish, Frog Egg, Obsidian, and Void Egg)
All Flowers (except Poppy)
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
Purple Mushroom
Salmonberry
Snow Yam
Wild Horseradish
Winter Root```'''
        self.Neutral = '''```\n
All Universal Neutrals (except Combat Quarterly and Monster Compendium)
All Fruit (except Fruit Tree Fruit and Salmonberry)
All Fish (except Carp, Flounder, and Snail)
All Milk```'''
        self.Like = '''```\n
All Universal Likes (except Flowers, Complete Breakfast, Farmer's Lunch, Omelet, Piña Colada, and Artisan Goods other than Coffee, Green Tea, and Oil)
Combat Quarterly
Flounder
Monster Compendium
Quartz```'''
        self.Love = '''```\n\n
All Universal Loves
Frog Egg
Frozen Tear
Obsidian
Pumpkin Soup
Sashimi	Raw
Void Egg```'''

class Shane:
    def __init__(self):
        self.Hate = '''```\n\n
All Universal Hates (except Seaweed & Strange Bun)
Pickles
Quartz```'''
        self.Dislike = '''```\n\n
All Universal Dislikes
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
Purple Mushroom
Seaweed
Snow Yam
Wild Horseradish
Winter Root```'''
        self.Neutral = '''```\n
All Universal Neutrals
All Milk
Strange Bun```'''
        self.Like = '''```\n
All Universal Likes (except Pickles)
All Eggs (except Void Egg)*
All Fruit (except Hot Pepper)

*Dinosaur Eggs do not count as eggs, but artifacts.```'''
        self.Love = '''```\n\n
All Universal Loves
Beer
Hot Pepper
Pepper Poppers
Pizza```'''

class Abigail:
    def __init__(self):
        self.Hate = '''```\n\n
All Universal Hates (except Sugar)
Clay
Holly```'''
        self.Dislike = '''```\n\n
All Universal Dislikes (except Ancient Sword, Basilisk Paw, Bone Flute, Clay & Pufferfish)
All Eggs*
All Fruit (except Fruit Tree Fruit)
All Vegetables (except Hops, Pumpkin, Tea Leaves, & Wheat)
Sugar
Wild Horseradish

*Dinosaur Eggs do not count as eggs, but artifacts.```'''
        self.Neutral = '''```\n
All Universal Neutrals (except Combat Quarterly and Monster Compendium)
All Milk
Chanterelle
Common Mushroom
Daffodil
Dandelion
Ginger
Hazelnut
Leek
Magma Cap
Morel
Purple Mushroom
Snow Yam
Winter Root```'''
        self.Like = '''```\n
All Universal Likes (except Vegetables)
Ancient Sword
Basilisk Paw
Bone Flute
Combat Quarterly
Quartz```'''
        self.Love = '''```\n\n
All Universal Loves
Amethyst
Banana Pudding
Blackberry Cobbler
Chocolate Cake
Monster Compendium
Pufferfish
Pumpkin
Spicy Eel```'''

class Haley:
    def __init__(self):
        self.Hate = '''```\n\n
All Universal Hates
All Fish
Clay
Prismatic Shard
Wild Horseradish```'''
        self.Dislike = '''```\n\n
All Universal Dislikes (except Clay & Fish)
All Eggs*
All Fruit (except Coconut)
All Milk
All Vegetables (except Hops, Tea Leaves, & Wheat)
Chanterelle
Common Mushroom
Dandelion
Ginger
Hazelnut
Holly
Leek
Magma Cap
Morel
Mystic Syrup
Purple Mushroom
Quartz
Snow Yam
Winter Root

*Dinosaur Eggs do not count as eggs, but artifacts.```'''
        self.Neutral = '''```\n
All Universal Neutrals (except Mystic Syrup)```'''
        self.Like = '''```\n
All Universal Likes (except Vegetables)
Daffodil```'''
        self.Love = '''```\n\n
All Universal Loves (except Prismatic Shard)
Coconut
Fruit Salad
Pink Cake
Sunflower```'''

class Leah:
    def __init__(self):
        self.Hate = '''```\n\n
All Universal Hates (except Seaweed)
Bread
Hashbrowns
Pancakes
Pizza
Void Egg```'''
        self.Dislike = '''```\n\n
All Universal Dislikes (except Driftwood, Spring Onion, & Void Egg)
All Foraged Minerals (except Earth Crystal)
All Gems (except Diamond & Prismatic Shard)
Carp Surprise
Cookie
Fried Egg
Ice Cream
Pink Cake
Rice Pudding
Seaweed
Survival Burger```'''
        self.Neutral = '''```\n
All Universal Neutrals (except Bread, Fried Egg, & Truffle)```'''
        self.Like = '''```\n
All Universal Likes (except:
  Foraged Minerals other than Earth Crystal
  Gems other than Diamond & Prismatic Shard
  Carp Surprise, Cookie, Hashbrowns, Ice Cream, Pancakes, Pink Cake, Pizza, Rice Pudding, Survival Burger, & Tortilla)
All Eggs (except Void Egg)*
All Fruit
All Milk
Chanterelle
Common Mushroom
Daffodil
Dandelion
Driftwood
Ginger
Hazelnut
Holly
Leek
Magma Cap
Morel
Purple Mushroom
Snow Yam
Spring Onion
Wild Horseradish
Winter Root

*Dinosaur Eggs do not count as eggs, but artifacts.```'''
        self.Love = '''```\n\n
All Universal Loves
Goat Cheese
Poppyseed Muffin
Salad
Stir Fry
Truffle
Vegetable Medley
Wine```'''

class Maru:
    def __init__(self):
        self.Hate = '''```\n\n
All Universal Hates (except Radioactive Bar & Radioactive Ore)
Holly
Honey
Pickles
Snow Yam
Truffle```'''
        self.Dislike = '''```\n\n
All Universal Dislikes (except Battery Pack, Copper Bar, Dwarf Gadget, Gold Bar, Iridium Bar, Iron Bar, Oak Resin, & Pine Tar)
Blackberry
Common Mushroom
Crystal Fruit
Maple Syrup
Salmonberry```'''
        self.Neutral = '''```\n
All Universal Neutrals (except Truffle)
All Eggs (except Void Egg)*
All Fruit (except Blackberry, Crystal Fruit, Fruit Tree Fruit, Salmonberry, & Strawberry)
All Milk
Daffodil
Dandelion
Ginger
Hazelnut
Leek
Wild Horseradish
Winter Root

*Dinosaur Eggs do not count as eggs, but artifacts.```'''
        self.Like = '''```\n
All Universal Likes (except Honey, Maple Syrup, & Pickles)
Chanterelle
Copper Bar
Iron Bar
Magma Cap
Morel
Oak Resin
Pine Tar
Purple Mushroom
Quartz
Radioactive Ore```'''
        self.Love = '''```\n\n
All Universal Loves
Battery Pack
Cauliflower
Cheese Cauliflower
Diamond
Dwarf Gadget
Gold Bar
Iridium Bar
Miner's Treat
Pepper Poppers
Radioactive Bar
Rhubarb Pie
Strawberry```'''

class Penny:
    def __init__(self):
        self.Hate = '''```\n\n
All Universal Hates (except Poppy and Red Mushroom)
Beer
Grape
Holly
Hops
Mead
Pale Ale
Piña Colada
Rabbit's Foot
Wine```'''
        self.Dislike = '''```\n\n
All Universal Dislikes (except Artifacts, Price Catalogue, & Sandfish)
Algae Soup
Duck Feather
Pale Broth
Purple Mushroom
Quartz
Red Mushroom
Salmonberry
Wool```'''
        self.Neutral = '''```\n
All Universal Neutrals (except Books, Duck Feather, Hops, & Wool)
All Eggs (except Void Egg)*
All Fruit (except Fruit Tree Fruit, Grape, Melon, & Salmonberry)
Chanterelle
Common Mushroom
Daffodil
Ginger
Hazelnut
Magma Cap
Morel
Snow Yam
Wild Horseradish
Winter Root

*Dinosaur Eggs do not count as eggs, but artifacts.```'''
        self.Like = '''```\n
All Universal Likes (except Algae Soup, Beer, Mead, Pale Ale, Pale Broth, Piña Colada, & Wine)
All Milk
All Artifacts
Dandelion
Leek```'''
        self.Love = '''```\n\n
All Universal Loves (except Rabbit's Foot)
All Books
Diamond
Emerald
Melon
Poppy
Poppyseed Muffin
Red Plate
Roots Platter
Sandfish
Tom Kha Soup```'''

class Emily:
    def __init__(self):
        self.Hate = '''```\n\n
All Universal Hates
Fish Taco
Holly
Maki Roll
Salmon Dinner
Sashimi```'''
        self.Dislike = '''```\n\n
All Universal Dislikes (except Parrot Egg)
Fried Eel
Ice Cream
Rice Pudding
Salmonberry
Spicy Eel```'''
        self.Neutral = '''```\n
All Universal Neutrals (except Wool)
All Eggs (except Void Egg)*
All Fruit (except Fruit Tree Fruit & Salmonberry)
All Milk
Chanterelle
Common Mushroom
Dandelion
Ginger
Hazelnut
Leek
Magma Cap
Morel
Purple Mushroom
Snow Yam
Wild Horseradish
Winter Root

*Dinosaur Eggs do not count as eggs, but artifacts.```'''
        self.Like = '''```\n
All Universal Likes (except Fish Taco, Fried Eel, Ice Cream, Maki Roll, Rice Pudding, Salmon Dinner, Spicy Eel, & Sashimi)
Daffodil
Quartz```'''
        self.Love = '''```\n\n
All Universal Loves
Amethyst
Aquamarine
Cloth
Emerald
Jade
Parrot Egg
Ruby
Survival Burger
Topaz
Wool```'''

class Caroline:
    def __init__(self):
        self.Hate = '''```\n\n
All Universal Hates
Quartz
Salmonberry```'''
        self.Dislike = '''```\n\n
All Universal Dislikes
Amaranth
Chanterelle
Common Mushroom
Dandelion
Duck Mayonnaise
Ginger
Hazelnut
Holly
Leek
Magma Cap
Mayonnaise
Morel
Purple Mushroom
Snow Yam
Winter Root```'''
        self.Neutral = '''```\n
All Universal Neutrals (except Tea Leaves)
All Eggs (except Void Egg)*
All Fruit (except pre-1.5 Fruit Tree Fruit & Salmonberry)
All Milk

*Dinosaur Eggs do not count as eggs, but artifacts.```'''
        self.Like = '''```\n
All Universal Likes (except Amaranth, Duck Mayonnaise, & Mayonnaise)
Daffodil
Tea Leaves
Wild Horseradish```'''
        self.Love = '''```\n\n
All Universal Loves
Fish Taco
Green Tea
Summer Spangle
Tropical Curry```'''

class Clint:
    def __init__(self):
        self.Hate = '''```\n\n
All Universal Hates
Holly```'''
        self.Dislike = '''```\n\n
All Universal Dislikes (except Coal, Copper Bar, Gold Bar, Gold Ore, Iridium Bar, Iridium Ore, Iron Bar, Omni Geode, & Refined Quartz)
All Flowers (except Poppy)
Quartz
Salmonberry
Wild Horseradish```'''
        self.Neutral = '''```\n
All Universal Neutrals (except Mining Monthly)
All Eggs (except Void Egg)*
All Fruit (except Fruit Tree Fruit & Salmonberry)
All Milk
Chanterelle
Common Mushroom
Coal
Daffodil
Dandelion
Ginger
Gold Ore
Hazelnut
Iridium Ore
Leek
Magma Cap
Morel
Purple Mushroom
Refined Quartz
Snow Yam
Winter Root

*Dinosaur Eggs do not count as eggs, but artifacts.```'''
        self.Like = '''```\n
All Universal Likes (except Flowers)
Copper Bar
Iron Bar
Mining Monthly```'''
        self.Love = '''```\n\n
All Universal Loves
Amethyst
Aquamarine
Artichoke Dip
Emerald
Fiddlehead Risotto
Gold Bar
Iridium Bar
Jade
Omni Geode
Ruby
Topaz```'''

class Demetrius:
    def __init__(self):
        self.Hate = '''```\n\n
All Universal Hates
Holly```'''
        self.Dislike = '''```\n\n
All Universal Dislikes (except Dinosaur Egg & Fish)
Quartz```'''
        self.Neutral = '''```\n
All Universal Neutrals
All Fish (except Carp & Snail)
All Milk
Chanterelle
Common Mushroom
Daffodil
Dandelion
Ginger
Hazelnut
Leek
Magma Cap
Morel
Snow Yam
Wild Horseradish
Winter Root```'''
        self.Like = '''```\n
All Universal Likes
All Eggs (except Void Egg)*
All Fruit (except Strawberry)
Dinosaur Egg
Purple Mushroom

*Dinosaur Eggs do not count as eggs, but artifacts.```'''
        self.Love = '''```\n\n
All Universal Loves
Bean Hotpot
Ice Cream
Rice Pudding
Strawberry```'''

class Dwarf:
    def __init__(self):
        self.Hate = '''```\n\n
All Universal Hates```'''
        self.Dislike = '''```\n\n
All Universal Dislikes (except Artifacts, Cave Carrot, Lava Eel, Lemon Stone, Omni Geode, Solar Essence, & Void Essence)
All Eggs*
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
Purple Mushroom
Salmonberry
Snow Yam
Wild Horseradish
Winter Root

*Dinosaur Eggs do not count as eggs, but artifacts.```'''
        self.Neutral = '''```\n
All Universal Neutrals
All Fruit (except Fruit Tree fruit & Salmonberry)
All Milk
Solar Essence
Void Essence```'''
        self.Like = '''```\n
All Universal Likes
All Artifacts
Cave Carrot
Quartz```'''
        self.Love = '''```\n\n
All Universal Loves
Amethyst
Aquamarine
Emerald
Jade
Lava Eel
Lemon Stone
Omni Geode
Ruby
Topaz```'''

class Evelyn:
    def __init__(self):
        self.Hate = '''```\n\n
All Universal Hates (except Broken Glasses & Sea Urchin)
All Fish (except Clam, Cockle, Mussel, & Oyster)
Clay
Fried Eel
Garlic
Holly
Maki Roll
Salmonberry
Sashimi	Raw
Spice Berry
Spicy Eel
Trout Soup```'''
        self.Dislike = '''```\n\n
All Universal Dislikes (except Clay & Fish)
Quartz
Wild Horseradish```'''
        self.Neutral = '''```\n
All Universal Neutrals (except Coral & Nautilus Shell)
All Eggs (except Void Egg)*
All Fruit (except Fruit Tree Fruit, Salmonberry, & Spice Berry)
Chanterelle
Common Mushroom
Dandelion
Ginger
Hazelnut
Leek
Magma Cap
Morel
Purple Mushroom
Snow Yam
Winter Root

*Dinosaur Eggs do not count as eggs, but artifacts.```'''
        self.Like = '''```\n
All Universal Likes (except Fried Eel, Garlic, Maki Roll, Sashimi, Spicy Eel, & Trout Soup)
All Milk
Broken Glasses
Clam
Cockle
Coral
Daffodil
Mussel
Nautilus Shell
Oyster
Sea Urchin```'''
        self.Love = '''```\n\n
All Universal Loves
Beet
Chocolate Cake
Diamond
Fairy Rose
Raisins
Stuffing
Tulip``'''

class George:
    def __init__(self):
        self.Hate = '''```\n\n
All Universal Hates
Clay
Dandelion
Holly
Quartz```'''
        self.Dislike = '''```\n\n
All Universal Dislikes (except Clay)
All Flowers (except Poppy)
Salmonberry
Wild Horseradish```'''
        self.Neutral = '''```\n
All Universal Neutrals
All Eggs (except Void Egg)*
All Fruit (except Fruit Tree Fruit & Salmonberry)
All Milk
Chanterelle
Common Mushroom
The Cave
Ginger
Hazelnut
Magma Cap
Morel
Purple Mushroom
Snow Yam
Winter Root

*Dinosaur Eggs do not count as eggs, but artifacts.```'''
        self.Like = '''```\n
All Universal Likes (except Flowers)
Daffodil```'''
        self.Love = '''```\n\n
All Universal Loves
Fried Mushroom
Leek``'''

class Gus:
    def __init__(self):
        self.Hate = '''```\n\n
All Universal Hates
Coleslaw
Holly
Quartz```'''
        self.Dislike = '''```\n\n
All Universal Dislikes
Salmonberry
Wild Horseradish```'''
        self.Neutral = '''```\n
All Universal Neutrals (except Truffle)
All Eggs (except Void Egg)*
All Fruit (except Fruit Tree Fruit & Salmonberry)
All Milk
Chanterelle
Common Mushroom
Dandelion
Ginger
Hazelnut
Leek
Magma Cap
Morel
Purple Mushroom
Snow Yam
Winter Root

*Dinosaur Eggs do not count as eggs, but artifacts.```'''
        self.Like = '''```\n
All Universal Likes (except Coleslaw)
Daffodil
Truffle```'''
        self.Love = '''```\n\n
All Universal Loves
Diamond
Escargot
Fish Taco
Orange
Tropical Curry``'''

class Jas:
    def __init__(self):
        self.Hate = '''```\n\n
All Universal Hates
All Artisan Goods (except Honey, Jelly & Oil)
Clay
Piña Colada
Triple Shot Espresso
Wild Horseradish```'''
        self.Dislike = '''```\n\n
All Universal Dislikes (except Ancient Doll, Clay, Fairy Box, Strange Doll (green), & Strange Doll (yellow))
All Eggs*
All Fruit (except Coconut & Fruit Tree Fruit)
All Vegetables (except Hops & Wheat)
Chanterelle
Common Mushroom
Dandelion
Ginger
Hazelnut
Holly
Leek
Magma Cap
Morel
Purple Mushroom
Quartz
Snow Yam
Winter Root

*Dinosaur Eggs do not count as eggs, but artifacts.```'''
        self.Neutral = '''```\n
All Universal Neutrals```'''
        self.Like = '''```\n
All Universal Likes (except Piña Colada, Triple Shot Espresso, Vegetables and Artisan Goods other than Honey, Jelly, & Oil)
All Milk
Coconut
Daffodil```'''
        self.Love = '''```\n\n
All Universal Loves
Ancient Doll
Fairy Box
Fairy Rose
Pink Cake
Plum Pudding
Strange Doll (green)
Strange Doll (yellow)``'''

class Jodi:
    def __init__(self):
        self.Hate = '''```\n\n
All Universal Hates
Daffodil
Dandelion
Spice Berry```'''
        self.Dislike = '''```\n\n
All Universal Dislikes
Chanterelle
Common Mushroom
Garlic
Ginger
Hazelnut
Holly
Leek
Magma Cap
Morel
Purple Mushroom
Quartz
Snow Yam
Wild Horseradish
Winter Root```'''
        self.Neutral = '''```\n
All Universal Neutrals```'''
        self.Like = '''```\n
All Universal Likes (except Garlic)
All Eggs (except Void Egg)*
All Fruit (except Spice Berry)
All Milk

*Dinosaur Eggs do not count as eggs, but artifacts.```'''
        self.Love = '''```\n\n
	
All Universal Loves
Chocolate Cake
Crispy Bass
Diamond
Eggplant Parmesan
Fried Eel
Pancakes
Rhubarb Pie
Vegetable Medley``'''

class Kent:
    def __init__(self):
        self.Hate = '''```\n\n
All Universal Hates
All Milk
Algae Soup
Holly
Sashimi
Tortilla```'''
        self.Dislike = '''```\n\n
All Universal Dislikes
Piña Colada
Quartz
Snow Yam```'''
        self.Neutral = '''```\n
All Universal Neutrals (except Dwarvish Safety Manual)
Chanterelle
Common Mushroom
Dandelion
Ginger
Hazelnut
Leek
Magma Cap
Morel
Purple Mushroom
Wild Horseradish
Winter Root```'''
        self.Like = '''```\n
All Universal Likes (except Algae Soup, Piña Colada, Sashimi, & Tortilla)
All Eggs (except Void Egg)*
All Fruit
Daffodil
Dwarvish Safety Manual

*Dinosaur Eggs do not count as eggs, but artifacts.```'''
        self.Love = '''```\n\n
All Universal Loves
Fiddlehead Risotto
Roasted Hazelnuts``'''

class Krobus:
    def __init__(self):
        self.Hate = '''```\n\n
All Universal Hates (except Monster Musk, Seafoam Pudding, Strange Bun, & Void Mayonnaise)```'''
        self.Dislike = '''```\n\n
All Universal Dislikes (except Gold Bar, Iridium Bar, & Void Egg)
All Cooking (except Bread, Fried Egg, Seafoam Pudding, & Strange Bun)
Chanterelle
Common Mushroom
Daffodil
Dandelion
Ginger
Hazelnut
Holly
Leek
Life Elixir
Magma Cap
Morel
Purple Mushroom
Salmonberry
Snow Yam
Winter Root```'''
        self.Neutral = '''```\n
All Universal Neutrals (except Monster Compendium)
All Eggs (except Void Egg)*
All Fruit (except Fruit Tree Fruit & Salmonberry)
All Milk

*Dinosaur Eggs do not count as eggs, but artifacts.```'''
        self.Like = '''```\n
All Universal Likes (except Life Elixir and All Cooking excluding Seafoam Pudding & Strange Bun)
Gold Bar
Quartz
Seafoam Pudding
Strange Bun```'''
        self.Love = '''```\n\n
All Universal Loves
Diamond
Iridium Bar
Monster Compendium
Monster Musk
Pumpkin
Void Egg
Void Mayonnaise
Wild Horseradish``'''

class Leo:
    def __init__(self):
        self.Hate = '''```\n\n
All Universal Hates (except Dragon Tooth & Sea Urchin)
Beer
Holly
Hops
Mead
Morel
Oil
Pale Ale
Piña Colada
Triple Shot Espresso
Unmilled Rice
Wine```'''
        self.Dislike = '''```\n\n
All Universal Disikes (except Oil, Unmilled Rice, & Fish)
All Cooked Dishes (other than Bread, Fried Egg, Poi, Mango Sticky Rice, & Triple Shot Espresso)
Chanterelle
Common Mushroom
Daffodil
Dandelion
Ginger
Hazelnut
Leek
Magma Cap
Pickles
Purple Mushroom
Salmonberry
Snow Yam
Wild Horseradish
Winter Root```'''
        self.Neutral = '''```\n
All Universal Neutrals (except Duck Feather, Hops, Nautilus Shell, & Rainbow Shell)
All Eggs (except Ostrich Egg and Void Egg)*
All Fish (except Carp & Snail)
All Fruit (except Mango, Salmonberry, & Spice Berry)
All Milk
Coffee

*Dinosaur Eggs do not count as eggs, but artifacts.```'''
        self.Like = '''```\n
All Universal Likes (except Beer, Coffee, Mead, Pale Ale, Piña Colada, Wine, and Cooking other than Bread, Fried Egg, Poi, Mango Sticky Rice, & Triple Shot Espresso)
Dragon Tooth
Mango Sticky Rice
Nautilus Shell
Quartz
Rainbow Shell
Sea Urchin
Spice Berry```'''
        self.Love = '''```\n\n
All Universal Loves
Duck Feather
Mango
Ostrich Egg
Poi``'''

class Lewis:
    def __init__(self):
        self.Hate = '''```\n\n
All Universal Hates
Holly
Quartz```'''
        self.Dislike = '''```\n\n
All Universal Dislikes
All Milk
Salmonberry
Wild Horseradish```'''
        self.Neutral = '''```\n
All Universal Neutrals
All Eggs (except Void Egg)*
All Fruit (except Blueberry, Cactus Fruit, Coconut, Fruit Tree Fruit, Hot Pepper, & Salmonberry)
Chanterelle
Common Mushroom
Daffodil
Dandelion
Ginger
Hazelnut
Leek
Magma Cap
Morel
Purple Mushroom
Snow Yam
Winter Root

*Dinosaur Eggs do not count as eggs, but artifacts.```'''
        self.Like = '''```\n
All Universal Likes
Blueberry
Cactus Fruit
Coconut```'''
        self.Love = '''```\n\n
All Universal Loves
Autumn's Bounty
Glazed Yams
Green Tea
Hot Pepper
Vegetable Medley``'''

class Linus:
    def __init__(self):
        self.Hate = '''```\n\n
All Universal Hates```'''
        self.Dislike = '''```\n\n
All Universal Dislikes (except Fish & Spring Onion)
All Foraged Minerals
All Gems (except Diamond & Prismatic Shard)```'''
        self.Neutral = '''```\n
All Universal Neutrals
All Fish (except Carp & Snail)```'''
        self.Like = '''```\n
All Universal Likes (except Foraged Minerals & Gems other than Diamond & Prismatic Shard)
All Eggs (except Void Egg)*
All Milk
All Fruit (except Cactus Fruit & Coconut)
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
Purple Mushroom
Snow Yam
Spring Onion
Wild Horseradish
Winter Root

*Dinosaur Eggs do not count as eggs, but artifacts.```'''
        self.Love = '''```\n\n
All Universal Loves
Blueberry Tart
Cactus Fruit
Coconut
Dish o' The Sea
Yam``'''

class Marnie:
    def __init__(self):
        self.Hate = '''```\n\n
All Universal Hates (except Seaweed)
Clay
Holly```'''
        self.Dislike = '''```\n\n
All Universal Dislikes (except Clay)
Salmonberry
Seaweed
Wild Horseradish```'''
        self.Neutral = '''```\n
All Universal Neutrals
All Fruit (except Fruit Tree Fruit & Salmonberry)
Chanterelle
Common Mushroom
Daffodil
Dandelion
Ginger
Hazelnut
Leek
Magma Cap
Morel
Purple Mushroom
Snow Yam
Winter Root```'''
        self.Like = '''```\n
All Universal Likes
All Eggs (except Void Egg)*
All Milk
Quartz

*Dinosaur Eggs do not count as eggs, but artifacts.```'''
        self.Love = '''```\n\n
All Universal Loves
Diamond
Farmer's Lunch
Pink Cake
Pumpkin Pie``'''