import os
import time
import crayons
import sys
import random
from bs4 import BeautifulSoup
import colorama
from colorama import init
from colorama import Fore, Style
from instapy import InstaPy
from instapy import smart_run
from instapy.quota_supervisor import inspector

def clear():
        os.system('cls')

clear()


def logo():
    try:
        text = """                                   
                $$\                       $$\                                   
                \__|                      $$ |                                  
                $$\ $$$$$$$\   $$$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\  $$\   $$\ 
                $$ |$$  __$$\ $$  _____|\_$$  _|   \____$$\ $$  __$$\ $$ |  $$ |
                $$ |$$ |  $$ |\$$$$$$\    $$ |     $$$$$$$ |$$ /  $$ |$$ |  $$ |
                $$ |$$ |  $$ | \____$$\   $$ |$$\ $$  __$$ |$$ |  $$ |$$ |  $$ |
                $$ |$$ |  $$ |$$$$$$$  |  \$$$$  |\$$$$$$$ |$$$$$$$  |\$$$$$$$ |
                \__|\__|  \__|\_______/    \____/  \_______|$$  ____/  \____$$ |
                                                           $$ |      $$\   $$ |
                                                           $$ |      \$$$$$$  |
                                                           \__|       \______/  
                                                                            
                                                                             
                                                                             \n                    
        """
        bad_colors = ['LIGHTRED_EX', 'GREEN']
        codes = vars(colorama.Fore)
        colors = [codes[color] for color in codes if color in bad_colors]
        colored_chars = [random.choice(colors) + char for char in text]
        print(''.join(colored_chars))
        print(Fore.RESET + "\t\t\t               Coded by: xFijo#0999\n")

    except KeyboardInterrupt:
        sys.exit()

clear()
logo()

os.system('Title InstaPy Login.')
user = input(crayons.cyan('Please provide your instagram username. : '))
time.sleep(1)
print(crayons.green('Checking username'))
print('\n')
passw = input(crayons.cyan('Please provide the matching password. : '))
time.sleep(1)
print(crayons.green('Logging in....'))
time.sleep(1.5)
print('\n')

pass

session = InstaPy(username=user,
                  password=passw,
                  headless_browser=True)
print(crayons.green(f'Logged in as {user}.'))
os.system(f'Title Logged in as: {user}')
pass


with smart_run(session):

     clear()

def like_posts(like):
        os.system(f'Title Post Like Bot ~ ~ ~ User: {user}')
        tags = input(crayons.cyan('What tag do you want ? : '))
        print(crayons.green(f'Tags {tags} chosen.'))
        amount = int(input(crayons.cyan('How many posts do you want to like ? : ')))
        print(crayons.green(f'Chosen to like {amount} posts under the tag {tags}....'))
        session.like_by_tags([tags], amount=amount)
        time.sleep(2.5)
        print(crayons.green('Posts liked!'))
        os.system(f'Title Like Bot Complete. ~ ~ ~ User: {user}')

pass
clear()

def follow_bot(follow):
        os.system(f'Title Follower Bot ~ ~ ~ User: {user}')
        print(crayons.green('Follower Bot Launching....'))
        accs = ['instagram', 'jlo', 'ddlovato', 'kevinhart4real', 'kourtneykardash', 'katyperry', 'mileycyrus', 'khloekardashian', 'nickiminaj', 'kendalljenner', 'taylorswift', 'neymarjr', 'justinbieber', 'beyonce', 'leomessi', 'selenagomez', 'kyliejenner', 'therock', 'kimkardashian', 'arianagrande', 'cristiano']
        time.sleep(1.5)
        print(crayons.green('Accounts Loaded.'))
        print(crayons.cyan('Following users.'))
        session.follow_by_list(accs, times=5, sleep_delay=600, interact=False)
        time.sleep(2.5)
        print(crayons.green('Users followed.'))
        time.sleep(2.5)
        print('\n')
        print(crayons.cyan('Follow Bot Relaunching......'))
        tags = input(crayons.cyan('What tag do you want ? : '))
        session.follow_by_tags([tags], amount=30)
        session.unfollow_users(amount=30)
        print(crayons.green('Successfully Ran Both follower bots!'))
        os.system(f'Title Follower Bot Complete ~ ~ ~ User: {user}')
        print('\n')
        time.sleep(2.5)

initialChoice = input(crayons.cyan('What would you like to bot ? : [followers] [likes]'))
if initialChoice == 'followers':
        follow_bot(10000)
elif initialChoice == 'likes':
        like_posts(10000)
else:
        print(crayons.red('Invalid Choice.'))
                









        
        """
        choice = input(crayons.cyan('Would you like to run again'))
        if choice == 'yes':
                print(crayons.green('Running again..'))
                print(crayons.green('Follower Bot Launching....'))
                accs = ['instagram', 'jlo', 'ddlovato', 'kevinhart4real', 'kourtneykardash', 'katyperry', 'mileycyrus', 'khloekardashian', 'nickiminaj', 'kendalljenner', 'taylorswift', 'neymarjr', 'justinbieber', 'beyonce', 'leomessi', 'selenagomez', 'kyliejenner', 'therock', 'kimkardashian', 'arianagrande', 'cristiano']
                time.sleep(1.5)
                print(crayons.green('Accounts Loaded.'))
                print(crayons.cyan('Following users.'))
                session.follow_by_list(accs, times=5, sleep_delay=600, interact=False)
                time.sleep(2.5)
                print(crayons.green('Users followed.'))
                time.sleep(2.5)
                print('\n')
                print(crayons.cyan('Follow Bot Relaunching......'))
                session.follow_by_tags([tags], amount=30)
                session.unfollow_users(amount=30)
                print(crayons.green('Successfully Ran Both follower bots!'))

        """
