import sqlite3
import discord
from discord.ext import commands
import sqlite3

class Cog_Extension(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.db = sqlite3.connect('discord.db')
    self.create_tables()

  def create_tables(self):
    cur = self.db.cursor()
    # create table
    cur.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        id integer PRIMARY KEY,
        username text NOT NULL,
        start_time text
        )
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS dailyRecord (
        id integer NOT NULL,
        totalRecordDay integer NOT NULL,
        oldDate text,
        latestDate text,
        FOREIGN KEY (id)
          REFERENCES accounts (id) 
        )
    ''')
    self.db.commit()