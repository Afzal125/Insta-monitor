import csv
import instaloader
import discord_webhook
from time import sleep
import datetime
import sys
import ast
from os import path
from pytz import timezone
while True:
    ig = instaloader.Instaloader()
    ig.login('@', '') #enter ur username and password
    person = 'smartphone_network'  # mention the username without '@'
    discord_webhook_url = 'https://discord.com/api/webhooks/775738599156482080/b_ZgT0NVNhRbjAiGh3doJGyTFTeKAujWTDdiBCNveOiSp79SYOWOFL8H1QYKopGUbAvH'

    Time_interval = 120 
    profile = instaloader.Profile.from_username(ig.context, person)
    
    current_followers = []
    old_followers = []
    follower_change = 0

    for follower in profile.get_followers():

        username = follower.username

        current_followers.append(username+"\n")
        
        
    current_following = []

    for followee in profile.get_followees():

        username = followee.username

        current_following.append(username)
        
        
            
    if not path.exists('unfollowers.txt'):
        with open('unfollowers.txt','w') as txtfile: # unfollowers.csv file saved on system

            
            for i in current_followers:
                txtfile.write(i+'\n')
            txtfile.close()
    
    else:
        with open('unfollowers.txt','r+') as txtfile: 
            for i in txtfile:
                old_followers.append(i)
            while("\n" in old_followers):
                old_followers.remove("\n")
            txtfile.truncate()

        with open('unfollowers.txt','r+') as txtfile: 
            for i in current_followers:
                if i == ' ':
                    pass
                else:
                    txtfile.write(i+'\n')
            txtfile.close()
        print((current_followers,old_followers))
        follower_change  = len(current_followers)-len(old_followers)

        
            
        
                
 
                
    discord_webhook.send_msg(username,current_following,current_followers,old_followers,follower_change,discord_webhook_url)

    sleep(Time_interval*60)
