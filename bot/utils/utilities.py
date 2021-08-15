# -*- coding: utf-8 -*-
import io
import logging
import os
import pprint
import random
import string
import sys
import traceback
import discord
from discord.errors import InvalidArgument
from discord.ext import commands

import pymysql.cursors
from dotenv import load_dotenv

load_dotenv(".env")

__databaseConfig__ = pymysql.connect(
	host=os.getenv("mysqlServer"),
	user="root",
	password=os.getenv("mysqlPassword"),
	port=3306,
	database="tragedy",
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor,
	read_timeout=5,
	write_timeout=5,
	connect_timeout=5,
	autocommit=True
)

columnNames = ["defaultPrefix","prefix1", "prefix2", "prefix3", "prefix4", "prefix5"]

class InstagramConverter(commands.Converter):
	async def convert(self, ctx, username):
		formatted = username
		validChars = list(string.ascii_lowercase + '._1234567890')

		if str(username).startswith('@'):
			formatted = str(username)[1:]
		if len(formatted) > 29:
			raise InvalidArgument
		for char in list(username):
			if char not in validChars:
				return InvalidArgument
			else:
				pass
		else:
			pass
		
		print(validChars)
		return formatted.casefold()

def DotenvVar(var: str):
	load_dotenv('.env')
	return os.getenv(var)

def EmojiBool(bool: bool):
	switch = {
		True: ":white_check_mark:",
		False: ":x:",
	}
	return switch.get(bool, "N/A")


def HumanStatus(status):
	switch = {
		"dnd": "Do Not Disturb.",
		"online": "Online.",
		"idle": "Idle.",
		"offline": "Offline.",
	}
	return switch.get(status, "Error.")


def custom_prefix(bot, message):
	try:
		return getServerPrefixes(message.guild.id)
	except:
		try:
			__databaseConfig__.cursor().execute("INSERT INTO prefix (guild) VALUES (%s)", (str(message.guild.id)))
			__databaseConfig__.commit()
			print("[Logging] Added {} ({}) to prefix database.".format(message.guild.name, str(message.guild.id)))
			return getServerPrefixes(message.guild.id)
		except Exception as exc:
			logError(exc)
		except pymysql.err.InterfaceError as exc:
			logError(exc)

async def report(self, ctx, error):
	try:
		error = ''.join(traceback.format_exception(etype=type(error), value=error, tb=error.__traceback__))
		owner = await self.bot.fetch_user(self.bot.owner_id)
		id = __import__('nanoid').generate()
		embed = discord.Embed(title="Oops !", description="Something went wrong and we're not quite sure what. Your error has been reported to the developers. ID - `%s`" % (id),
							  color=discord.Color.red())
		await ctx.reply(embed=embed, mention_author=True)

		if len(error) < 1850:
			await owner.send('ID - **`{}`**\n**Error in the command `{}`**, Invoked in `{}` by `{}`\n```\n'.format(id, ctx.command.name, ctx.guild.name, ctx.author) + error + '\n```')
		else:
			await owner.send(content='**Error in the command `{}`**, Invoked in `{}` by `{}`'.format(ctx.command.name, ctx.guild.name, ctx.author), file=discord.File(fp=io.BytesIO(error.encode(errors='ignore')), filename='exception.txt'))
	except Exception as exc:
		print(traceback.format_exception(etype=type(exc), value=exc, tb=exc.__traceback__))

def getServerPrefixes(guild_id):
	columns = ["defaultPrefix","prefix1", "prefix2", "prefix3", "prefix4", "prefix5"]
	with __databaseConfig__.cursor() as cursor:
		cursor.execute(
			"SELECT * FROM prefix WHERE guild=%s", (str(guild_id))
			)
		try:
			response = dict(cursor.fetchone())
		except TypeError:
			return ['xv ']
		prefixes = list()
		for col in columns:
			if response.get(col) != None:
				prefixes.append(response.get(col))
		return prefixes

def logError(exception: Exception):
	pprint.pprint(traceback.format_exception(type(exception), exception, exception.__traceback__))

def logInfo(message):
	logging.log(logging.INFO, message)

def wrap(font, text,
		 line_width):  # https://github.com/DankMemer/imgen/blob/master/utils/textutils.py (useful asf so i stole it not even gonna cap w you)
	words = text.split()
	lines = []
	line = []
	for word in words:
		newline = ' '.join(line + [word])
		width, height = font.getsize(newline)
		if width > line_width:
			lines.append(' '.join(line))
			line = [word]
		else:
			line.append(word)
	if line:
		lines.append(' '.join(line))
	return ('\n'.join(lines)).strip()