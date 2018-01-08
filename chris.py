#! /bin/python3

import discord
import logging

logging.basicConfig(level=logging.INFO)

client=discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')


@client.event
async def on_message(message):
	if message.content is '!intro':
		client.send_message(message.channel, "Hi! I'm Chris Hansen. Why don't you take a seat right over there?")
