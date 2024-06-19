import nextcord
from nextcord import ui

class Like(ui.Select):
    def __init__(self):
        options = [
            nextcord.SelectOption(label="Love", description="+80 Friendship Points", emoji="❤️"),
            nextcord.SelectOption(label="Like", description="+45 Friendship Points", emoji="👍"),
            nextcord.SelectOption(label="Neutral", description="+20 Friendship Points", emoji="🤷"),
            nextcord.SelectOption(label="Dislike", description="-20 Friendship Points", emoji="👎"),
            nextcord.SelectOption(label="Hate", description="-40 Friendship Points", emoji="💔"),
        ]
        super().__init__(placeholder="Choose a character.", options=options, min_values=1, max_values=5)

    async def callback(self, interaction):
        await interaction.response.send_message(f"You've chosen {self.values}")

class Characters(ui.Select):
    def __init__(self):
        options = [
            nextcord.SelectOption(label="Alex", description="", emoji="🏈"),
            nextcord.SelectOption(label="Elliot", description="", emoji="🐟"),
            nextcord.SelectOption(label="Harvey", description="", emoji="🏥"),
            nextcord.SelectOption(label="Sam", description="", emoji="🎸"),
            nextcord.SelectOption(label="Sebastian", description="", emoji="🙄"),
            nextcord.SelectOption(label="Shane", description="", emoji="🤢"),
            nextcord.SelectOption(label="Abigail", description="", emoji="🟣"),
            nextcord.SelectOption(label="Haley", description="", emoji="📷"),
            nextcord.SelectOption(label="Leah", description="", emoji="🖌️"),
            nextcord.SelectOption(label="Maru", description="", emoji="🪛"),
            nextcord.SelectOption(label="Penny", description="", emoji="🍳"),
            nextcord.SelectOption(label="Emily", description="", emoji="👗")
        ]
        super().__init__(placeholder="Choose a character.", options=options, min_values=1, max_values=1)

    async def callback(self, interaction):
        view = ui.View()
        view.add_item(Like())

        await interaction.response.send_message("Choose any fields of gifts you want to see. Choose up to 5.", view=view)