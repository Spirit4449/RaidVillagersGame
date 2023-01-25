# DISCLAIMER
# OPEN CONSOLE FULL SCREEN FOR THE BEST EXPERIENCE


import var
import time
import random
from colorama import Fore, Style, init
from battle import battle_start
init(autoreset=True)


class player:
    player_health = 100
    player_defense = 1
    player_attack = 5


tutorial = False


# Tutorial
if tutorial == True:
    print("Welcome to Raid Villagers! Raid villagers is a trhilling text-based adventure game where you play as a ruthless raider, attacking and looting villages for gold and treasure. Your ultimate goal is to become the most powerful raider in the land by upgrading your character's stats. You will have to make strategic choices, outsmart the village defenders, and overcome dangerous obstacles to succeed. You will gain gold throughout your journey. Spend it wisely on your character stats. Now are you ready to embark on this epic journey?  Let's being!")
    time.sleep(5)

    name = input('Player Name: ')
    time.sleep(0.2)
    print('Welcome ' + name + '. Let\'s start by attacking your first village.')
    time.sleep(2)

    battle_start()

else:
    name = input('Player Name: ')
    quicktutorial = input("Would you like a quick tutorial? ")
    if quicktutorial.lower() == 'yes':
        battle_start(True)
    if quicktutorial.lower() == 'no':
        print("Ok. If you need a list of commands type /help")
    else:
        print("That is not a valid option! I guess you don't want a tutorial. If you ever need a list of commands, just type /help")

if tutorial == True:
    print('You are now ready to play the game! Type /help to view the list of commands...')

valid_command = False


while True:
    command = input('')
    if command == '/help':
        valid_command = True
        print('''
  /help - displays the help command
  /battle - starts a battle
  /upgrade - displays a list of upgrades to your character
  /stats - displays your current stats
  /shop - brings a menu with items you can buy
  /coins - displays current amount of coins
  /exit - exits the game (progress does not save)''')
    if command == '/shop':
        valid_command = True
        print('Here a a list of things you can buy:\n🍖 Meat - restores health for 50 hitpoints on purchase.\n💝 Lifesaver - gives another change if you are about to die')
    if command == '/upgrade':
        valid_command = True
        print('Which stat would you like to upgrade? Armor - 100 coins, Defense - 100 coins or Health - 100 coins')
    if command == '/battle':
        valid_command = True
        battle_start()
    if command == '/exit':
        valid_command = True
        print('Thank you for playing. See you later!')
        exit()
    if command == '/stats':
        valid_command = True
        print('Here are your stats:\nAttack: ' + str(var.player_attack) +
              '\nDefense: ' + str(var.player_defense) + '\nHealth: ' + str(var.player_health))
    if command == '/coins':
        valid_command = True
        print('You currently have ' + str(var.player_coins) + ' coins.')
    if not valid_command:
        print(Fore.RED + "That is not a valid command. Type /help for a list of commands")
    valid_command = False
