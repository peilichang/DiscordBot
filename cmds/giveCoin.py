import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import datetime
import pygsheets
import pandas as pd


gc = pygsheets.authorize(service_file='discord.json')
sht = gc.open_by_url('https://docs.google.com/spreadsheets/d/1JaEC7b58HLlDQg76PO2VkeAMS6HfFpK-Jfl_0oZcds0/')

class GiveCoin(Cog_Extension):

  # 身份驗證時可以新增帳號名單
  @commands.command()
  async def vertify(self, ctx):
    accounts = sht.worksheet_by_title("accounts")
    userInfo = [ctx.message.author.id, ctx.message.author.name]
    df = pd.DataFrame(accounts.get_all_records())
    lastRow = len(df)+1
    accounts.insert_rows(row=lastRow, number=1, values=userInfo)
    
    print(f'userId = {ctx.message.author.name}' )
    await ctx.send('Vertify successfully!')

  # Daily
  @commands.command()
  async def daily(self, ctx):
    userId = ctx.message.author.id
    date = datetime.date.today()  
    dailyRecord = sht.worksheet_by_title("dailyRecord")
    dailyRecordDf = pd.DataFrame(dailyRecord.get_all_records())
    lastRow = len(dailyRecordDf)+1
    print(dailyRecordDf)
    print(list(dailyRecordDf['totalRecordDay']),userId)
    if userId in list(dailyRecordDf['ID']):
      print("紀錄過ㄐ")
      selected = dailyRecordDf[dailyRecordDf['ID']==userId]
      previousDate = selected["previousDate"]
      latestDate = selected["latestDate"]
      print(type(latestDate))
    else:
      userDailyRecord = [str(userId), 0, "", str(date)]
      dailyRecord.insert_rows(row=lastRow, number=1, values=userDailyRecord)
      print("沒紀錄過")

    print(dailyRecordDf)



    
    await ctx.send(f'{date}')

def setup(bot):
  bot.add_cog(GiveCoin(bot))