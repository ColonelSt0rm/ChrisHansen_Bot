#! /bin/python3
import asyncio
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import logging
from difflib import SequenceMatcher


defaultserv = 'garden_of_eden'

logging.basicConfig(level=logging.INFO)

client=discord.Client()


softbanned = []

botToken = ""

def checkDuplicates(name):
	cnt = 0
	for usr in client.get_all_members():
		if usr.nick:
			sim =similar(name, usr.nick)

			print(sim)
			if sim > 0.799:
				cnt = cnt + 1
	

	print("Count", cnt)	
	if cnt > 1:
		return True
	else:
		return False

def similar(a, b):
	return SequenceMatcher(None, a, b).ratio()

def sban(updown):
	if updown == "up":
		return
	elif updown == "down":
		return


def get_channel(channels, channel_name):
	for channel in client.get_all_channels():
		print(channel)
		if channel.name == channel_name:
			return channel

	return None

async def tell(msg, payload):
	await client.send_message(msg.channel, payload)


def getToken():
	global botToken
	Tokenfile = open('/botKey', "r")
	token = Tokenfile.read()
	botToken = token



@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	client.change_presence(game=discord.Game(name="Internet Predators"))
	print('------')


@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content == '!intro':
		await tell(message, "Hi! I'm Chris Hansen. I'm the new automated moderator! Why don't you take a seat right over there?")
		await tell(message, "As of right now, I am designed to enforce one rule:\n\nNO DUPLICATE USERNAMES OR NICKNAMES\n\nIf new rules arise, I will be updated to enforce them. If my developer finds himself with extra free time, I will be expanded to do things other than boring law enforcement!")
		await tell(message, "A few things to remember:\n1) I am a robot, there's nobody in my driver's seat!\n2) My AI is very primitive, so I may make mistakes\n3) I am not a meme\n4) I am not your enemy\n5) I am serious about my decisions!")	
		await tell(message, "Some FAQ:\nQ: 'Are you memeing me?'\n\tA: Definitely Not. My name may be a meme, but I am still a moderator with moderator powers.\n\nQ: 'What happens if I break a rule you've been taught?'\n\t A: You will be softbanned for the period I specify. It generally won't be long.\n\nQ: 'What do I do if I'm softbanned without cause?'\n\tA: If you know you didn't break any rules, type '!appeal' into the chat to notify the human admins. The senate will decide your fate.")


@client.event
async def on_member_update(before, after):
	await client.send_message(get_channel(client.get_all_channels(), defaultserv), before.nick+" changed their name to "+after.nick)
	aname = after.nick
	if aname:
		dups = checkDuplicates(aname)
		if dups:
			await client.send_message(get_channel(client.get_all_channels(), defaultserv), "Duplicate Username Detected! Have a seat right over there for me, would you?")
			await client.change_nickname(after, "A Filthy Pedophile")

getToken()
client.run(botToken.strip())




