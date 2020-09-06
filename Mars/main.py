#Twitter: @vzcode
#Github: https://github.com/vz-code
#Youtube: https://www.youtube.com/channel/UCYAW591GkbvnoreBeSjwojQ?view_as=subscriber
#Telegram: @vzcode
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import datetime
import json
import asyncio
from discord.utils import get
import youtube_dl
import os
import ffmpeg
from discord.voice_client import VoiceClient
from discord import FFmpegPCMAudio
from os import system
mars = commands.Bot(command_prefix = '/')
mars.remove_command('help')
@mars.event
async def on_ready():
    print('Development by vzcode')#Nada de cambiar el nombre del author =)) att vzcode
#Evento cuando usuario se une :D
@mars.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="﹙🪐﹚joins")
    await channel.send(f"{member.mention} has join.")
    embed = discord.Embed(
            colour= discord.Colour.red(),
            title="© Mars Development",
            description=f"{member.mention} has join."
        )
    await channel.send(embed=embed)
#Evento cuando un usuario se va :c
@mars.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name="﹙🪐﹚joins")
    embed = discord.Embed(
            colour= discord.Colour.red(),
            title="© Mars Development",
            description=f"{member.mention} has leave."
        )
    await channel.send(embed=embed)
#Comando de ayuda lel :D
@mars.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def help(ctx):
    embed = discord.Embed(
        colour= discord.Colour.red(),
        title="© Mars Development",
        description="Help in using the bot"
    )
    embed.set_author(name="© Mars Development", icon_url="https://cdn.discordapp.com/avatars/738976118538764408/e5c924956eacb6f0082d956fb7d0170a.png?size=128")
    embed.add_field(name="ping", value="This command shows you my latency", inline=False)
    embed.add_field(name="bugreport", value="You can report bugs to fix", inline=False)
    embed.add_field(name="suggest", value="Can you give us a suggestion", inline=False)
    embed.add_field(name="dev", value="Show my developer and my version", inline=False)
    embed.add_field(name="info", value="Show server information", inline=False)
    embed.add_field(name="send", value="He sent a message that you established", inline=False)
    embed.add_field(name="clear", value="I delete the number of messages established", inline=False)
    embed.add_field(name="marsnew", value="You open a ticket for support", inline=False)
    embed.add_field(name="marsclose", value="You close your ticket", inline=False)
    embed.set_footer(text=f"© Mars Development")

    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/738976118538764408/e5c924956eacb6f0082d956fb7d0170a.png?size=128")

    await ctx.send(embed=embed)
#Sistema de kickeos.
@mars.command()
@commands.has_any_role('Admin')
async def marskick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
#Sistema de baneos.
@mars.command()
@commands.has_any_role('Admin')
async def marsban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
#Ping mediante latencia.
@mars.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def ping(ctx):
    embed = discord.Embed(title=f"© Mars Development")
    embed.add_field(name="Latency", value=f"{round(mars.latency * 1000)}ms")
    embed.set_footer(text=f"© Mars Development")
    await ctx.send(embed=embed)
#Enviar un argumento
@mars.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def send(ctx, *, arg):
    embed = discord.Embed(
        colour= discord.Colour.red(),
        title="© Mars Development",
    )
    embed.add_field(name="Message", value= arg)
    embed.set_footer(text=f"© Mars Development")
    await ctx.send(embed=embed)
#Borrar mensajes
@mars.command()
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_any_role('Admin')
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(title=f"© Mars Development", color=discord.Color.red())
    embed.add_field(name="Clear", value=f"{amount} messages cleaned")
    embed.set_footer(text=f"© Mars Development")
    await ctx.send(embed=embed)
#Informacion del servidor
@mars.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="© Mars Development", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/738976118538764408/e5c924956eacb6f0082d956fb7d0170a.png?size=128")

    await ctx.send(embed=embed)
#Dev p.d este bot fue creado por vzcode nd de cambiar el author =))
@mars.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def dev(ctx):
    embed = discord.Embed(
        colour= discord.Colour.red(),
        title="© Mars Development",
        description="Development by vzcode"
    )
    embed.set_author(name="Author", icon_url="https://cdn.discordapp.com/avatars/738976118538764408/e5c924956eacb6f0082d956fb7d0170a.png?size=128")
    embed.set_image(url="https://cdn.discordapp.com/avatars/738976118538764408/e5c924956eacb6f0082d956fb7d0170a.png?size=128")
    embed.add_field(name="Version", value="0.1")
    embed.set_footer(text=f"© Mars Development")

    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/738976118538764408/e5c924956eacb6f0082d956fb7d0170a.png?size=128")

    await ctx.send(embed=embed)
#Anuncios
@mars.command()
@commands.has_any_role('Admin')
@commands.cooldown(1, 5, commands.BucketType.user)
async def announce(ctx, *, arg):
    channel = mars.get_channel(741942439698235403)
    embed = discord.Embed(
        colour= discord.Colour.red(),
        title="© Mars Development",
    )
    embed.add_field(name="ADS", value= arg, inline=False)
    embed.set_footer(text=f"© Mars Development")
    await channel.send(embed=embed)
#BugReport
@mars.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def bugreport(ctx, *, arg):
    channel = mars.get_channel(741942374317424642)
    embed = discord.Embed(
        colour= discord.Colour.red(),
        title="© Mars Development",
    )
    embed.add_field(name="Bug Report", value= arg)
    embed.set_footer(text=f"© Mars Development")
    await channel.send(embed=embed)
#Suguerencias
@mars.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def suggest(ctx, *, arg):
    channel = mars.get_channel(741942323331596318)
    embed = discord.Embed(
        colour= discord.Colour.red(),
        title="© Mars Development",
    )
    embed.add_field(name="Suggest", value= arg)
    embed.set_footer(text=f"© Mars Development")
    await channel.send(embed=embed)
#Abrir ticket
@mars.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def marsnew(ctx, *, args = None):

    await mars.wait_until_ready()

    if args == None:
        message_content = "Please wait"

    else:
        message_content = "".join(args)

    with open("data.json") as f:
        data = json.load(f)

    ticket_number = int(data["ticket-counter"])
    ticket_number += 1

    ticket_channel = await ctx.guild.create_text_channel("MarsTicket-{}".format(ticket_number))
    await ticket_channel.set_permissions(ctx.guild.get_role(ctx.guild.id), send_messages=False, read_messages=False)

    for role_id in data["valid-roles"]:
        role = ctx.guild.get_role(role_id)

        await ticket_channel.set_permissions(role, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)

    await ticket_channel.set_permissions(ctx.author, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)

    em = discord.Embed(title="Ticket of {}#{}".format(ctx.author.name, ctx.author.discriminator), description= "{}".format(message_content), color=0x00a8ff)

    await ticket_channel.send(embed=em)

    pinged_msg_content = ""
    non_mentionable_roles = []

    if data["pinged-roles"] != []:

        for role_id in data["pinged-roles"]:
            role = ctx.guild.get_role(role_id)

            pinged_msg_content += role.mention
            pinged_msg_content += " "

            if role.mentionable:
                pass
            else:
                await role.edit(mentionable=True)
                non_mentionable_roles.append(role)

        await ticket_channel.send(pinged_msg_content)

        for role in non_mentionable_roles:
            await role.edit(mentionable=False)

    data["ticket-channel-ids"].append(ticket_channel.id)

    data["ticket-counter"] = int(ticket_number)
    with open("data.json", 'w') as f:
        json.dump(data, f)

    created_em = discord.Embed(title="Mars Tickets", description="Ticket create at {}".format(ticket_channel.mention), color=0x00a8ff)

    await ctx.send(embed=created_em)
#Cerrar ticket
@mars.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def close(ctx):
    with open('data.json') as f:
        data = json.load(f)

    if ctx.channel.id in data["ticket-channel-ids"]:

        channel_id = ctx.channel.id

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "/marsclose"

        try:

            em = discord.Embed(title="Mars Tickets", description="If you want to close the ticket write /marsclose", color=0x00a8ff)

            await ctx.send(embed=em)
            await mars.wait_for('message', check=check, timeout=60)
            await ctx.channel.delete()

            index = data["ticket-channel-ids"].index(channel_id)
            del data["ticket-channel-ids"][index]

            with open('data.json', 'w') as f:
                json.dump(data, f)

        except asyncio.TimeoutError:
            em = discord.Embed(title="Mars Tickets", description="Fail, retry", color=0x00a8ff)
            await ctx.send(embed=em)


#Dar acceso.
@mars.command()
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_any_role('Owner')
async def addacc(ctx, role_id=None):

    with open('data.json') as f:
        data = json.load(f)

    valid_user = False

    for role_id in data["verified-roles"]:
        try:
            if ctx.guild.get_role(role_id) in ctx.author.roles:
                valid_user = True
        except:
            pass

    if valid_user or ctx.author.guild_permissions.administrator:
        role_id = int(role_id)

        if role_id not in data["valid-roles"]:

            try:
                role = ctx.guild.get_role(role_id)

                with open("data.json") as f:
                    data = json.load(f)

                data["valid-roles"].append(role_id)

                with open('data.json', 'w') as f:
                    json.dump(data, f)

                em = discord.Embed(title="Mars Tickets", description="Add `{}` to the list of roles with access to tickets.".format(role.name), color=0x00a8ff)

                await ctx.send(embed=em)

            except:
                em = discord.Embed(title="Mars Tickets", description="Invalid ID.")
                await ctx.send(embed=em)

        else:
            em = discord.Embed(title="Mars Tickets", description="That role already has access to tickets!", color=0x00a8ff)
            await ctx.send(embed=em)

    else:
        em = discord.Embed(title="Mars Tickets", description="Nope", color=0x00a8ff)
        await ctx.send(embed=em)
#Quitar acceso.
@mars.command()
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_any_role('Owner')
async def delacc(ctx, role_id=None):
    with open('data.json') as f:
        data = json.load(f)

    valid_user = False

    for role_id in data["verified-roles"]:
        try:
            if ctx.guild.get_role(role_id) in ctx.author.roles:
                valid_user = True
        except:
            pass

    if valid_user or ctx.author.guild_permissions.administrator:

        try:
            role_id = int(role_id)
            role = ctx.guild.get_role(role_id)

            with open("data.json") as f:
                data = json.load(f)

            valid_roles = data["valid-roles"]

            if role_id in valid_roles:
                index = valid_roles.index(role_id)

                del valid_roles[index]

                data["valid-roles"] = valid_roles

                with open('data.json', 'w') as f:
                    json.dump(data, f)

                em = discord.Embed(title="Mars Tickets", description="Removed `{}` from the list of roles with access to tickets.".format(role.name), color=0x00a8ff)

                await ctx.send(embed=em)

            else:

                em = discord.Embed(title="Mars Tickets", description="That role already doesn't have access to tickets!", color=0x00a8ff)
                await ctx.send(embed=em)

        except:
            em = discord.Embed(title="Mars Tickets", description="Invalid ID.")
            await ctx.send(embed=em)

    else:
        em = discord.Embed(title="Mars Tickets", description="Nope", color=0x00a8ff)
        await ctx.send(embed=em)
#Agregar un ping
@mars.command()
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_any_role('Owner')
async def addping(ctx, role_id=None):

    with open('data.json') as f:
        data = json.load(f)

    valid_user = False

    for role_id in data["verified-roles"]:
        try:
            if ctx.guild.get_role(role_id) in ctx.author.roles:
                valid_user = True
        except:
            pass

    if valid_user or ctx.author.guild_permissions.administrator:

        role_id = int(role_id)

        if role_id not in data["pinged-roles"]:

            try:
                role = ctx.guild.get_role(role_id)

                with open("data.json") as f:
                    data = json.load(f)

                data["pinged-roles"].append(role_id)

                with open('data.json', 'w') as f:
                    json.dump(data, f)

                em = discord.Embed(title="Mars Tickets", description="Added `{}` to the list of roles that get pinged when new tickets are created!".format(role.name), color=0x00a8ff)

                await ctx.send(embed=em)

            except:
                em = discord.Embed(title="Mars Tickets", description="Invalid ID.")
                await ctx.send(embed=em)

        else:
            em = discord.Embed(title="Mars Tickets", description="That role already receives pings when tickets are created.", color=0x00a8ff)
            await ctx.send(embed=em)

    else:
        em = discord.Embed(title="Mars Tickets", description="Nope", color=0x00a8ff)
        await ctx.send(embed=em)
#Restar un ping
@mars.command()
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_any_role('Owner')
async def delping(ctx, role_id=None):

    with open('data.json') as f:
        data = json.load(f)

    valid_user = False

    for role_id in data["verified-roles"]:
        try:
            if ctx.guild.get_role(role_id) in ctx.author.roles:
                valid_user = True
        except:
            pass

    if valid_user or ctx.author.guild_permissions.administrator:

        try:
            role_id = int(role_id)
            role = ctx.guild.get_role(role_id)

            with open("data.json") as f:
                data = json.load(f)

            pinged_roles = data["pinged-roles"]

            if role_id in pinged_roles:
                index = pinged_roles.index(role_id)

                del pinged_roles[index]

                data["pinged-roles"] = pinged_roles

                with open('data.json', 'w') as f:
                    json.dump(data, f)

                em = discord.Embed(title="Mars Tickets", description="Removed `{}` from the list of roles that get pinged when new tickets are created.".format(role.name), color=0x00a8ff)
                await ctx.send(embed=em)

            else:
                em = discord.Embed(title="Mars Tickets", description="That role already isn't getting pinged when new tickets are created!", color=0x00a8ff)
                await ctx.send(embed=em)

        except:
            em = discord.Embed(title="Mars Tickets", description="Invalid ID")
            await ctx.send(embed=em)

    else:
        em = discord.Embed(title="Mars Tickets", description="Nope.", color=0x00a8ff)
        await ctx.send(embed=em)
#Agregar un admin
@mars.command()
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_any_role('Owner')
async def addadmin(ctx, role_id=None):

    try:
        role_id = int(role_id)
        role = ctx.guild.get_role(role_id)

        with open("data.json") as f:
            data = json.load(f)

        data["verified-roles"].append(role_id)

        with open('data.json', 'w') as f:
            json.dump(data, f)

        em = discord.Embed(title="Mars Tickets", description="You have successfully added `{}` to the list of roles that can run admin-level commands!".format(role.name), color=0x00a8ff)
        await ctx.send(embed=em)

    except:
        em = discord.Embed(title="Mars Tickets", description="Invalid ID.")
        await ctx.send(embed=em)
#Eliminar un admin
@mars.command()
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_any_role('Owner')
async def deladmin(ctx, role_id=None):
    try:
        role_id = int(role_id)
        role = ctx.guild.get_role(role_id)

        with open("data.json") as f:
            data = json.load(f)

        admin_roles = data["verified-roles"]

        if role_id in admin_roles:
            index = admin_roles.index(role_id)

            del admin_roles[index]

            data["verified-roles"] = admin_roles

            with open('data.json', 'w') as f:
                json.dump(data, f)

            em = discord.Embed(title="Mars Tickets", description="Removed `{}` from the list of roles that get pinged when new tickets are created.".format(role.name), color=0x00a8ff)

            await ctx.send(embed=em)

        else:
            em = discord.Embed(title="Mars Tickets", description="That role isn't getting pinged when new tickets are created!", color=0x00a8ff)
            await ctx.send(embed=em)

    except:
        em = discord.Embed(title="Mars Tickets", description="Invalid ID.")
        await ctx.send(embed=em)
#Canales de voz entrada y salida.
@mars.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@mars.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

#Musica
@mars.command(pass_context=True, aliases=['p', 'pla'])
async def play(ctx, url: str):

    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("ERROR: Music playing")
        return

    await ctx.send("Getting everything ready now")

    voice = get(mars.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now\n")
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    nname = name.rsplit("-", 2)
    await ctx.send(f"Playing: {nname[0]}")
    print("playing\n")
# Errores
youtube_dl.utils.bug_reports_message = lambda: ''


ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
@mars.command()
    async def yt(self, ctx, url):
        """Plays from a url (almost anything youtube_dl supports)"""

    async with ctx.typing():
        player = await YTDLSource.from_url(url, loop=self.bot.loop)
        ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

        await ctx.send('Now playing: {}'.format(player.title))
mars.run('token :3')
