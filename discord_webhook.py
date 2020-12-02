from discord_webhooks import DiscordWebhooks
import time


#Put your discord webhook url here.
# IMPORTANT : If you're hosting on pythonanywhere, use discordapp.com instead of discord.com in the URL
WEBHOOK_URL = 'https://discord.com/api/webhooks/775738599156482080/b_ZgT0NVNhRbjAiGh3doJGyTFTeKAujWTDdiBCNveOiSp79SYOWOFL8H1QYKopGUbAvH'


        
def send_msg(username,current_following,current_followers,old_followers,follower_change,discord_webhook_url):

	idiots = []
	a = set(old_followers).difference(set(current_followers))
	for i in a:
		idiots.append(i)
 
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
		webhook.add_field(name='who unfollowed',value=idiots[0:])
	except Exception as e:
		print(e)
	webhook.send()

	print("Sent message to discord")