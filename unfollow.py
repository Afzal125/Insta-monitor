import instaloader
from time import sleep
import datetime
import sys
import os
from os import path


d= {} # user data 

if not path.exists('user_details.txt'): # storing user data as a txt file
    username = input("Enter ur username: ") # mention the username without '@'
    password = input("Enter ur password: ")
    url = input("Enter ur Discord webhook url: ")
    
    with open('user_details.txt','w') as txtfl:
        txtfl.write('1 '+username+'\n')
        txtfl.write('2 '+password+'\n')
        txtfl.write('3 '+url+'\n')
    txtfl.close()
        

with open('user_details.txt','r+') as txtfl:
    for line in txtfl:
        (key,val) = line.split()
        d[int(key)] = val
    print(d)
        
import discord_webhook            
while True:
    ig = instaloader.Instaloader()
    try:
        ig.login('@'+d[1], d[2])
    except Exception as e:
        print("\n",e)
    

    Time_interval = 10 # configured for 1 hr
    profile = instaloader.Profile.from_username(ig.context, d[1])
    print("\nSuccessfully logged in")
    
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
        
        
            
    if not path.exists('followers_details.txt'): # storing followers details
        with open('followers_details.txt','w') as txtfile: 
            
            for i in current_followers:
                txtfile.write(i+'\n')
            txtfile.close()
    
    else:
        with open('followers_details.txt','r+') as txtfile: 
            for i in txtfile:
                if i == ' ':
                    pass
                else:
                    old_followers.append(i)
                
            while("\n" in old_followers):
                old_followers.remove("\n")
            txtfile.truncate()
            txtfile.close()

        with open('followers_details.txt','r+') as txtfile: 
            for i in current_followers:
                if i == ' ':
                    pass
                else:
                    txtfile.write(i+'\n')
            txtfile.close()
            
        follower_change  = len(old_followers)-len(current_followers)
        if  len(old_followers) < len(current_followers):
            follower_change = 'no one unfollowed'
    print("\nCurrent_followers: ",len(current_followers))
    

        
            
        
                
 
                
    discord_webhook.send_msg(username,current_following,current_followers,old_followers,follower_change)

    sleep(Time_interval*60)