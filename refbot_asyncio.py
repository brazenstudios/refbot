##################################################
#
# Discord Bot
# ßrazen 5tudios
# Splurket
# Dillon_Marks
# M° frymatic
# YUP
# 2020
#
##################################################

import discord, random, sys, time
from discord_tokens import *

from listener_module import ListenerBot

sys.path.append('../Lead_Manager')
from lead_bot import *

client = discord.Client()

filepath = 'recentRefreshes.txt'

@client.event
async def on_ready():
	print('{0.user} is online and ready for your command.'.format(client))

@client.event
async def on_message(message):

	# get user name of command author
	if message.author == client.user:
		return

	# invite refbot to voice channel that permissioned user is in
	if message.content.startswith('!join'):
		print(message.content)
		# await message.channel.send(random.choice(greeting))

		# start voice stream

	# excuse refbot from the channel
	if message.content.startswith('!leave'):
		print(message.content)
		await message.channel.send(random.choice(nico))

	# toggle whistle on/off
	if message.content.startswith('!whistle'):
		print(message.content)
		await message.channel.send(random.choice(daye))

	# more for later
	if message.content.startswith(''):
		print(message.content)
		await message.channel.send(random.choice(stephen))

	# help commands 
	if message.content.startswith('!help'):
		await message.channel.send('Commands: $hello $ban $rules $scoreboard /leads /clear')

	# drop user from channel (or maybe server?)
	if message.content.startswith('$ban'):

		author = message.author.name
		authorDiscord = dialers[author]['name']
		notify = 'you\'re fired, ' + authorDiscord

		await message.channel.send(notify)





# with open(filepath,'a') as guestList:
#     guestList.write(input("Sign the guest book!:") + " " + str(datetime.date.today()) + "\n")

		original = message.content
		print(original)

		assignee = original.replace('/leads ','')
		print(assignee)

		timestamp = time.time()

		last = dialers[assignee]['last_leads']


		print("timestamp: ", timestamp, ", last_leads: ", last)

		if last:
			print("existing time stamp")
			if (timestamp - last) >= 9000:
				notify = '💯 leads for ' + assignee

				await message.channel.send(notify)

				recycle(assignee)
				notify = 'leads refreshed for ' + assignee

				await message.channel.send(notify)
				last = timestamp
				print(last, dialers[assignee]['last_leads'])
			else:
				notify = 'need to wait a little longer til ' + assignee + ' can get leads...'
				await message.channel.send(notify)
	
		else:
			print("no recent timestamp")
			last = timestamp
			print(last, dialers[assignee]['last_leads'])

			notify = '💯 leads for ' + assignee

			await message.channel.send(notify)

			recycle(assignee)
			notify = 'leads refreshed for ' + assignee

			await message.channel.send(notify)

	if message.content.startswith('$scoreboard'):
		await message.channel.send('the score is tied at fun to fun')

	if message.content.startswith('$brayden'):
		await message.channel.send('on god!')
	   

client.run(token)