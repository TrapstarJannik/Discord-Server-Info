# discord imports
import discord
from discord.ext import commands

# other imports 
from typing import Literal, Optional
import datetime
import json

# config file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# bot configs 
TOKEN = config['token'] # <-- changeable, in config.json
PREFIX = config['prefix'] # <-- changeable in config.json

# "bot" for commands/events, prefix ".", permissions "all"
bot = commands.Bot(command_prefix=PREFIX, intents = discord.Intents.all())

# start message 
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}") # <-- bot name
    print(f"Bot ID: {bot.user.id}") # <-- bot ID
    print("Bot is ready.") # <-- ready message
    
# command for syncing slash commands
@bot.command()
@commands.guild_only()
@commands.is_owner()
async def sync(ctx: commands.Context, guilds: commands.Greedy[discord.Guild], spec: Optional[Literal["guild", "global", "clear"]] = None) -> None: # <-- command usages
    embed = discord.Embed(title="Synced successfully!", color=0x99e699)  # <-- embed title and color

    if not guilds:
        if spec == "guild": # <-- sync to the current guild
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "global": # <-- sync to all guilds
            ctx.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "clear": # <-- clear and sync in the current guild
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else: # <-- sync all slash commands 
            synced = await ctx.bot.tree.sync()

        embed.description = f"Synced `{len(synced)}` slash-command/s {'globally' if spec is None else 'in the current guild.'}" # <-- message about the sync
    
    else:
        ret = 0
        for guild in guilds: # <-- for guild ID's 
            try:
                await ctx.bot.tree.sync(guild=guild)
            except discord.HTTPException: # <-- sync with discord 
                pass
            else:
                ret += 1

        embed.description = f"Synced to `{ret}/{len(guilds)}` Guild/s." # <-- Message about sync for multiple guilds

    if ctx.author.avatar:
        avatar_url = ctx.author.avatar.url # <-- getting avatar 
    else:
        avatar_url = ctx.author.default_avatar.url # <-- getting default avatar if avatar is none
    embed.set_footer(text=f"{ctx.author.name}・{datetime.datetime.now().strftime('%H:%M:%S')}", icon_url=avatar_url)  # <-- embed footer (you can change %H:%M:%S to your time format)

    await ctx.send(embed=embed) # <-- send embed

  
@bot.tree.command(description="Shows you information about the server")
async def serverinfo(interaction: commands.Context):
    guild = interaction.guild
    bot_avatar_url = bot.user.avatar.url if bot.user.avatar else bot.user.default_avatar.url

    # Values (only change if you know what you are doing)
    name = guild.name
    server_id = guild.id
    server_owner = guild.owner.mention
    all_members = guild.member_count
    non_bot_members = sum(not member.bot for member in guild.members)
    bots = sum(member.bot for member in guild.members)
    role_count = len(guild.roles)
    staff_role_count = sum(1 for role in guild.roles if role.permissions.administrator)
    text_channels = len(guild.text_channels) 
    voice_channels = len(guild.voice_channels) 
    categories = len(guild.categories) 
    total_channels = text_channels + voice_channels 

    features = '\n'.join(guild.features)  # <-- Features separated by line breaks
    features = features.lower()  # <-- Write features in lowercase letters

    creation_date = guild.created_at.strftime("%A, %B %dth %Y %I:%M %p")

    embed = discord.Embed(title=f"📌 Server Information - {name}", color=0xb3b3ff)
    embed.set_thumbnail(url=bot_avatar_url)  # <-- Set the bot's avatar as thumbnail
    embed.add_field(name="💳 Server ID", value=server_id, inline=True) # <-- Name (changeable) and values
    embed.add_field(name="👑 Server Owner", value=server_owner, inline=True) # <-- Name (changeable) and values
    embed.add_field(name=" ", value=" ", inline=False) # <-- Empty field for spacing
    embed.add_field(name="🌎 All Members", value=all_members, inline=True) # <-- Name (changeable) and values
    embed.add_field(name="🎨 Role Count", value=role_count, inline=True) # <-- Name (changeable) and valuess
    embed.add_field(name=" ", value=" ", inline=False) # <-- Empty field for spacing
    embed.add_field(name="👥 Members", value=non_bot_members, inline=True) # <-- Name (changeable) and values
    embed.add_field(name="👮 Staff Roles", value=staff_role_count, inline=True) # <-- Name (changeable) and value
    embed.add_field(name="🤖 Bots", value=bots, inline=False) # <-- Name (changeable) and values
    embed.add_field(name=" ", value=" ", inline=False) # <-- Empty field for spacing
    embed.add_field(name="📊 Total Channels", value=total_channels, inline=True)
    embed.add_field(name="📂 Categories", value=categories, inline=True) # <-- Name (changeable) and values
    embed.add_field(name=" ", value=" ", inline=False) # <-- Empty field for spacing
    embed.add_field(name="📄 Text Channels", value=text_channels, inline=True) # <-- Name (changeable) and values
    embed.add_field(name="🔊 Voice Channels", value=voice_channels, inline=True) # <-- Name (changeable) and values
    embed.add_field(name=" ", value=" ", inline=False) # <-- Empty field for spacing
    
    
    # emojis for features
    features_with_emojis = []
    
    # features listed on the top
    if "community" in features: 
        features_with_emojis.append("🌎 Community") # <-- Name (changeable)
    if "news" in features:
        features_with_emojis.append("📣 News") # <-- Name (changeable)
    if "animated icon" in features:
        features_with_emojis.append("🎞️ Animated Icon") # <-- Name (changeable)
    
    # adding other features
    for feature in features.split('\n'):
        if "community" in feature or "news" in feature:
            continue  # <-- continue after the main features (you can add more main features)
        else:
            features_with_emojis.append("🛠️ " + feature) # <-- emoji for other features (changeable)
    
    # Joining the features list with emojis into a single string separated by line brakes
    features_formatted = "\n".join(features_with_emojis)

    embed.add_field(name="📋 Features", value=features_formatted, inline=False) # <-- Name (changeable) and values
    embed.add_field(name=" ", value=" ", inline=False) # <-- Empty field for spacing
    embed.add_field(name="🕙 Server Creation Date", value=creation_date, inline=False) # <-- Name (changeable) and values
    if interaction.user.avatar:
        avatar_url = interaction.user.avatar.url
    else:
        avatar_url = interaction.user.default_avatar.url # <-- getting avatar for embed footer
    embed.set_footer(text=f"{interaction.user.name}・{datetime.datetime.now().strftime('%I:%M:%S %p')}", icon_url=avatar_url) # <-- embed footer, time (changeable)
    await interaction.response.send_message(embed=embed) # <-- Send embed

bot.run(TOKEN)