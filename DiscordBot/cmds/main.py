import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime

class Main(Cog_Extension):
  @commands.command()
  async def ping(self, ctx): #延遲秒速
    await ctx.send(f'{round(self.bot.latency*1000)}(ms)')
    # ctx = context(上下文)
    # A: hi (使用者、id、所在伺服 器、所在頻道)
    # B: hey（根據上文的屬性來得知）

  @commands.command()
  async def hi(self, ctx):
    await ctx.send('10000')

  @commands.command()
  async def em(self, ctx):
    embed=discord.Embed(title="活動名稱", url="https://tronclass.scu.edu.tw", description="web3.0課程", color=0xa8c6fe, timestamp=datetime.datetime.now())
    embed.set_author(name="Pecu", url="https://pecu.github.io/peculab/", icon_url="https://pecu.github.io/peculab/assets/peculabimgs/pecu.jpg")
    embed.set_thumbnail(url="https://pecu.github.io/peculab/assets/peculabimgs/peculab.jpg")
    embed.add_field(name="活動日期", value="2022/04/12", inline=True)
    embed.add_field(name="活動主題", value="手動作智能合約", inline=True)
    embed.set_footer(text="2022/04/01")
    await ctx.send(embed=embed)

  # @commands.command(invoke_without_command=True)
  #   async def welcome(self,ctx)
  


def setup(bot):
  bot.add_cog(Main(bot))