import discord
import asyncio
import random
import pickle
import os


client = discord.Client()

@client.event
async def on_ready():
	print("Logged in as:")
	print(client.user.name)
	print("ID:")
	print(client.user,id)
	print("Ready for use!")

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	elif message.content.startswith("!ping"):
		await client.send_message(message.channel, ":ping_pong: Pong!")
	elif message.content.startswith("!hey"):
		await client.send_message(message.channel, "Hi!")
	elif message.content.startswith("!hi"):
		await client.send_message(message.channel, "Hey!")
	elif message.content.startswith("!info"):
		await client.send_message(message.channel, "My name is SkeleBot, a working functional bot made by SkeleDash#5733. do !2info for more info on me.")
	elif message.content.startswith("!2info"):
		await client.send_message(message.channel, "I was programmed in python and was made just for the purpose of using random commands and imploding my system. ;3;")
	elif message.content.startswith("!flip"):
		flip = random.choice(["Heads", "Tails"])
		await client.send_message(message.channel, flip)
	elif message.content.startswith("!addquote"):
		if not os.path.isfile("quote_file.pk1"):
			quote_list = []
		else:
			with open("quote_file.pk1", "rb") as quote_file:
				quote_list = pickle.load(quote_file)
		quote_list.append(message.content[9:])
		with open("quote_file.pk1", "wb") as quote_file:
			pickle.dump(quote_list, quote_file)
	elif message.content.startswith("!quote"):
		with open("quote_file.pk1", "rb") as quote_file:
				quote_list = pickle.load(quote_file)
		await client.send_message(message.channel, random.choice(quote_list))

	elif message.content.startswith("!help"):
		await client.send_message(message.channel, "**Heres a list of commands i can do!**")
		await client.send_message(message.channel, "!ping: makes me say pong. :/")
		await client.send_message(message.channel, "!info: some info on me...")
		await client.send_message(message.channel, "!2info: a bit more...")
		await client.send_message(message.channel, "!addquote [quote]: adds a quote to a list of quotes.")
		await client.send_message(message.channel, "!quote: will say a random quote from the list of quotes.")
		await client.send_message(message.channel, "!flip: will 'flip a coin', used in case of arguments. ")
		await client.send_message(message.channel, "**If there are any other problems you may have, feel free to contact SkeleDash#5733! :wink:**")


client.run("Mzc5MDI5OTA1NjU4MzQ3NTIw.DPoOVA.g6zMZRSnR2RijgiQxv-BD-reNXs")

