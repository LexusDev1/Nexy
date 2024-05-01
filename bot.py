import discord
import pymongo
import yaml
import os
import asyncio
import motor

from lib.util.database import DB
from lib.util.msgprint import Print

textPrint = Print()
class Client(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    async def on_ready(self):
        await tree.sync(guild = discord.Object(id=1137395128806416446))
        textPrint.warning("TEST WARNING", "TEST WARNING BLUD!")
        
        

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
intents.members = True

client = Client(
    shard_count=10,
    command_prefix="?",
    intents=intents,
    case_insensitive=False,
    owner_id="965968259289612301"
)
tree = discord.app_commands.CommandTree(client)

id = 1137395128806416446

@tree.context_menu(name="Hello", guild=discord.Object(id = id))
async def translate(interaction: discord.Interaction, message: discord.Message):
    
    await interaction.response.send_message("Hi")

client.run("MTEyMDUzMDcwMTAwODI0ODg0Mw.G7jYqq.I5wGZXXP0jUx1VL7p7FMjOockISqmImQzhXOok")