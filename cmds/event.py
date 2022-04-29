import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
  jdata = json.load(jfile)

class Event(Cog_Extension):
  @commands.Cog.listener()
  async def on_member_join(self, member):
    channel = self.bot.get_channel(int(jdata['Welcome_channel']))
    print(f'{member} join!')
    await channel.send(f'{member} join!')


  @commands.Cog.listener()
  async def on_member_remove(self, member):
    channel = self.bot.get_channel(int(jdata['Left_channel']))
    print(f'{member} left!')
    await channel.send(f'{member} left!')

  @commands.Cog.listener()
  async def on_message(self, msg):
    # keyword = ['apple', 'pen', 'pie'] -> in keyword
    if msg.content == 'apple' and msg.author != self.bot.user: #endwith, startwith
      await msg.channel.send('hi')

def setup(bot):
  bot.add_cog(Event(bot))