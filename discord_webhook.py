from discord_webhooks import DiscordWebhooks
import time
import json
d = {}
with open('user_details.txt','r') as txtfl:
    for line in txtfl:
            (key,val) = line.split()
            d[int(key)] = val

# IMPORTANT : If you're hosting on pythonanywhere, use discordapp.com instead of discord.com in the URL
WEBHOOK_URL = d[3]

def send_msg(username,current_following,current_followers,old_followers,follower_change,discord_webhook_url):

	uf = []
	f = []
	a = set(old_followers).difference(set(current_followers))
	b = set(current_followers).difference(set(old_followers))
	for i in a:
		uf.append(i)
	
	for i in b:
		f.append(i)
 
	if set(current_followers) == set(old_followers):
		print("No change in followers, so not sending message to discord")
		return
	
			
	webhook = DiscordWebhooks(WEBHOOK_URL)
	webhook.set_content(title='Report for %s'%time.ctime(),description="Here's your report with :heart:")

	# Attaches a footer
	webhook.set_footer(text='-- Afzal')

	# Appends a field
	webhook.add_field(name='Username', value=username)
	webhook.add_field(name='Total follower change', value=follower_change)
	try:
		webhook.add_field(name='who unfollowed',value=json.dumps(uf))
		webhook.add_field(name='New followers',value=json.dumps(f))
	except Exception as e:
		print(e)
	webhook.send()

	print("Sent message to discord")