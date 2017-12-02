import asyncio
import discord
from discord.ext.commands import Bot
from discord.ext import commands
########################################
bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print('Ready to go')
    print(bot.user.name)
    print(bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.send(':ping_pong: Pong!')

@bot.command(pass_context=True)
async def embed(ctx):
    embed = discord.Embed(description = 'Hi')
    await ctx.send(embed = embed)

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed()
    embed.add_field(name = "Username: ", value = user.name, inline=True)
    embed.add_field(name = '', value = '')
    embed.add_field(name = "Join Date: ", value = user.joined_at,inline=True)
    embed.add_field(name = "Display name: ", value = user.display_name,inline=True)
    embed.add_field(name = '', value = '')
    embed.add_field(name = "Account Created at: ",value = user.created_at,inline=True)
    await ctx.send(embed = embed)

@bot.command(pass_context=True)
async def password(ctx, *, password):
    if password=='123':
        ctx.send('Granted')
        ctx.message.delete
        ctx.message.author.add_roles(roles = discord.utils.get(ctx.guild.roles, name='x'))
    else:
        ctx.send('Try Again')
        
@bot.command(pass_context=True)
async def user(ctx):
    print('hi : {}'.format(ctx.message.author))
    
@bot.command(pass_context=True)
async def kick(ctx,user:discord.Member):
    if ctx.message.author.guild_permissions.administrator==True and user.guild_permissions.administrator==False:
        print('Kicked: {}'.format(user.name))
        await ctx.send("Bye!")
        await ctx.guild.kick(user)
        print('Users currently : {}'.format(bot.get_all_members()))
    else:
        await ctx.send('Bye! {}'.format(ctx.message.author.mention))

bot.run('MzgzMDIzMTgzNTg4MjI5MTIx.DPeRbg.W4aJe-4-JFuEqzlPkikUCciIkbo')