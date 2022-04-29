import discord
from discord.ext import commands
import json
import random
import os
import sqlite3

with open('setting.json', 'r', encoding='utf8') as jfile:
  jdata = json.load(jfile)

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='/', intents = intents)
TOKEN = jdata['TOKEN']


@bot.event
async def on_ready():
  # db = sqlite3.connect('main.squite')
  # cursor = db.cursor()
  # cursor.execute('''
  #   CREATE TABLE IF NOT EXISTS main(
  #   guid_id TEXT,
  #   msg TExT,
  #   channel_id TExt
  #   )
  # ''')
  print(">> Bot is online >>")


@bot.command()
async def load(ctx, extension):
  bot.load_extension(f'cmds.{extension}')
  await ctx.send(f'Loaded {extension} done.')

@bot.command()
async def unload(ctx, extension):
  bot.unload_extension(f'cmds.{extension}')
  await ctx.send(f'Un-Loaded {extension} done.')

@bot.command()
async def reload(ctx, extension):
  bot.reload_extension(f'cmds.{extension}')
  await ctx.send(f'Re-Loaded {extension} done.')

for filename in os.listdir('./cmds'):
  if filename.endswith('.py'):
    bot.load_extension(f'cmds.{filename[:-3]}')






if __name__ == "__main__":
  bot.run(TOKEN)