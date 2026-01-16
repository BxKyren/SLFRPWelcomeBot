import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")
WELCOME_CHANNEL_ID = 1461675123433148508  # Your welcome channel

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.event
async def on_member_join(member: discord.Member):
    embed = discord.Embed(
        title="👋 Welcome to Serving London Frontline Roleplay!",
        description=(
            "Welcome to **Serving London Frontline Roleplay**!\n\n"
            "To get started, please open a **verification ticket** using the link below:\n"
            "🔗 https://discord.com/channels/1461674232810311792/1461701215988748469\n\n"
            "We look forward to seeing you roleplay with us!"
        ),
        color=discord.Color.blue()
    )

    embed.set_image(
        url="https://media.discordapp.net/attachments/1461788493142560952/1461791732286099520/WELCOME_3.png"
    )

    # Send message in the welcome channel
    channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        await channel.send(
            content=f"{member.mention}",
            embed=embed
        )

    # Send DM
    try:
        await member.send(embed=embed)
    except discord.Forbidden:
        pass  # User has DMs closed


bot.run(TOKEN)
