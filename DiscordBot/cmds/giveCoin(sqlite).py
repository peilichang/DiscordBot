import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import datetime

class GiveCoin(Cog_Extension):

  # 身份驗證時可以新增帳號名單
  @commands.command()
  async def vertify(self, ctx):
    cur = self.db.cursor()
    cur.execute('''
    INSERT OR IGNORE INTO accounts (id,username)
      Values(?,?)
    ''',[f'{ctx.message.author.id}',f'{ctx.message.author.name}'])
    self.db.commit()
    print(f'userId = {ctx.message.author.name}' )
    await ctx.send('Vertify successfully!')

  # Daily
  @commands.command()
  async def daily(self, ctx):
    userId = ctx.message.author.id
    date = datetime.date.today()  
    cur = self.db.cursor() #id,totalRecordDay,oldDate,latestDate
    # cur.execute('''
    # INSERT OR IGNORE INTO accounts (id,latestDate)
    #   Values(?,?)
    # ''',[f'{ctx.message.author.id}',f'{date}'])
    # self.db.commit()
    # print(f'userId = {ctx.message.author.name}' )
    # print('上次打卡時間', date+datetime.timedelta(days=1))
    # print('')

    cur.execute('''
    SELECT * FROM dailyRecord WHERE id=?
    ''',[f'{userId}'])
    result = cur.fetchone()
    if result :
      # 比較日期
      print('now', result)
      if str(result[3]) == str(date ): #- datetime.timedelta(days=1)
        sql = 'UPDATE dailyRecord SET totalRecordDay = ?, oldDate = ?, latestDate = ? WHERE id = ?'
        cur.execute('UPDATE dailyRecord SET totalRecordDay = ?, oldDate = ?, latestDate = ? WHERE id = ?',(str(result[1]+1), str(result[3]), str(date- datetime.timedelta(days=11)), userId))
        print("同一天",result[1]+1, result[3], date- datetime.timedelta(days=11), userId)

      else :
        print("不同天", result[3],"u",date - datetime.timedelta(days=1))

    else :
      cur.execute('''
      INSERT INTO dailyRecord (id, totalRecordDay, latestDate)
        Values(?,?,?)
      ''',[f'{userId}',0,f'{date}'])
      print("沒紀錄過")

    
      self.db.commit()
    await ctx.send(f'{date}')

def setup(bot):
  bot.add_cog(GiveCoin(bot))