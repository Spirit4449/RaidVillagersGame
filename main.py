# DISCLAIMER
# OPEN CONSOLE FULL SCREEN FOR THE BEST EXPERIENCE

import var
import time
#import random
import csv
import sys
import threading
from datetime import date
from battle import battle_start
from colorama import Fore, Style, init
init(autoreset=True)



def add_Data(data, file_Name='database.csv'):
  #fields = ['Name', 'Attack', 'Defense', 'Health', 'Coins']
  rows = []
  for value in data:
    rows.append(value)

  with open(file_Name, 'a+', newline='') as file:
    #Mode a+ appends without rewriting
    #Create writer object
    csvfile = csv.writer(file)

    #Write Fields (puts on same row)
    #csvfile.writerow(fields)

    #writeMyData (Puts on different rows)
    csvfile.writerow(rows)

def print_slow(text, speed=0.01):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)


file = 'database.csv'
var.generated_Data = var.read_Data(file)

print_slow('Player Name: ')
var.name = input(Fore.CYAN).lower()
print(Style.RESET_ALL, end='')

global today
today = date.today()
var.loginDate = today.strftime("%d-%m-%y")

def retrievedata():
  for list in var.generated_Data:
    for value in list:
      if value == var.name:
        var.player_attack = int(list[1])
        var.player_defense = int(list[2])
        var.player_health = int(list[3])
        var.player_coins = int(list[4])
        var.loginDate = list[5]
        var.tutorial = False

  if var.tutorial == True:
    new_player = [var.name, var.player_attack, var.player_defense, var.player_health, var.player_coins, var.loginDate]
    add_Data(new_player)
    var.tutorial = True



    
retrievedata()

loginlist = var.loginDate.split("-")
# Tutorial
if var.tutorial == True:
    print(f"Welcome to Raid Villagers {var.name}! Raid Villagers is an adventure game where you play as a raider attacking villages for gold and treasure. Your goal is to become the most powerful raider by upgrading your character's stats. Are you ready to embark on this epic adventure?\n")
    time.sleep(5)
    print('Upgrade all of your players stats to level 10 to win the game!\n')
  
    print('Let\'s start by attacking your first village.\n')
    time.sleep(2)

    battle_start()

elif int(today.strftime("%y")) - int(loginlist[2]) > 0 or int(today.strftime("%m")) - int(loginlist[1]) > 0 or int(today.strftime("%d")) - int(loginlist[0]) >= 2:
     print('Welcome back ' + var.name)
     time.sleep(.5)
     print_slow('Would you like a quick tutorial? ', 0.01)
     quicktutorial = input(Fore.CYAN)
     print(Style.RESET_ALL, end="")
     if quicktutorial.lower() == 'yes':
         var.tutorial = True
         print("Ok, here is a quick tutorial. Lets start by going into a battle.")
         time.sleep(2)
         battle_start(True)
     if quicktutorial.lower() == 'no':
         print("Ok. If you need a list of commands type " + Fore.CYAN + "/help\n")
     else:
         print(
             "That is not a valid option! I guess you don't want a tutorial. If you ever need a list of commands, just type" + Fore.YELLOW + "/help")
else:
  print('Welcome back ' + var.name)
  time.sleep(.4)
  print('Type' + Fore.YELLOW + ' /help' + Fore.RESET + ' for a list of commands')

var.loginDate = today.strftime("%d-%m-%y")
var.save_data(var.name, var.player_attack, var.player_defense, var.player_coins, var.player_health, var.loginDate)

if var.tutorial == True:
    print(f'You are now ready to play the game! Type {Fore.YELLOW}/help{Fore.RESET} to view the list of commands...')
    var.tutorial = False 

valid_command = False

while True:
    var.state = 'menu'
    command = input(Fore.CYAN).lower()
    print(Style.RESET_ALL, end="")
    if command == '/help':
        valid_command = True
        print(f'''
  {Fore.GREEN}/help - displays the help command
  {Fore.BLUE}/battle - starts a battle
  {Fore.LIGHTGREEN_EX}/upgrades - displays a list of upgrades to your character
  {Fore.MAGENTA}/stats - displays your current stats
  {Fore.LIGHTCYAN_EX}/shop - brings a menu with items you can buy
  {Fore.YELLOW}/coins - displays current amount of coins
  {Fore.RED}/exit - exits the game (progress is saved)
''')
    if command == '/shop':
        valid_command = True
        print(f"""
{Style.BRIGHT}SHOP        Your coins: {Fore.LIGHTYELLOW_EX}{var.player_coins}{Style.RESET_ALL}
🍖 Meat - {Fore.GREEN}50 coins{Style.RESET_ALL}
     Restores health for 25 hitpoints
💝 Lifesaver - {Fore.GREEN}250 coins{Style.RESET_ALL}
     Gives another change if you are about to die. (Can only buy one at a time)
🪙 Coin Doubler - {Fore.GREEN}400 coins{Style.RESET_ALL}
     Doubles all coins you earn for the next minute
{Fore.BLACK}Type /buy [item] to purchase""")
    if command == '/buy meat':
        valid_command = True
        hlthlevel = int((var.max_health - 100) / 10)
        if var.player_health != 100 + (hlthlevel*10):
            if var.player_coins - 100 >= 0:
                var.player_coins -= 50
                var.player_health += 25
                if var.player_health >= 100 + (hlthlevel*10):
                    var.player_health = var.max_health
                print('You just bought a meat for 100 coins! Your health is now '+str(var.player_health))
            else:
                print(Fore.RED + "You don't have enough coins to buy that!")
        else:
            print('You are already at max health!')
        
    elif command == '/buy lifesaver':
        valid_command = True
        if var.lifesaver != True:
            if var.player_coins - 250 >= 0:
                var.player_coins -= 250
                var.lifesaver = True
                print('You just bought a lifesaver for 250 coins! You can check if you have a lifesaver in the /stats command.')
            else:
                print(Fore.RED + "You don't have enough coins to buy that!")    
        else:
            print('A lifesaver is already active!')  

    elif command == '/buy coin doubler' or command == '/buy coindoubler' or command == '/buy coin doubler' or command == '/buy doubler':
        def coin_doubler():
            x = 0
            while True:
                time.sleep(1)
                x+=1
                if x == 60:
                    var.coindoubler = False
                    break
                else: 
                    continue
            while var.state != 'menu':
                time.sleep(1)
                continue
            else:
                print(Fore.YELLOW + 'Coin doubler has expired')
                t1.join()
                    
        valid_command = True
        if var.coindoubler == False:
            if var.player_coins - 400 >= 0:
                var.player_coins -= 400
                var.coindoubler = True
                print('You just bought a coin doubler for 400 coins! You have one minute to use it!')
                t1 = threading.Thread(target=coin_doubler)
                t1.start()
            
            else:
                print(Fore.RED + "You don't have enough coins to buy that!")    
        else:
            print('A coin doubler is already active!')
            
    elif command == '/upgrades' or command == '/upgrade':
        valid_command = True
        atklevel = int((var.player_attack - 5) / 5)
        deflevel = int((var.player_defense - 5) / 5)
        hlthlevel = int((var.max_health - 100) / 10)

        atkcoins = 50 + (50*atklevel)
        defcoins = 50 + (50*deflevel)
        hlthcoins = 50 + (50*hlthlevel)

        print(f"""
{Style.BRIGHT}UPGRADES        Your coins: {Fore.YELLOW}{var.player_coins}{Style.RESET_ALL}
🗡️  Attack (Lvl {atklevel}) - {Fore.GREEN}{atkcoins} coins{Fore.RESET}
     Increases attack by 5     (Max - lvl 10)
🛡️  Defense (Lvl {deflevel}) - {Fore.GREEN}{defcoins} coins{Fore.RESET}
     Increases defense by 5     (Max - lvl 10)
❤️  Health (Lvl {hlthlevel}) - {Fore.GREEN}{hlthcoins} coins{Fore.RESET}
     Increases max health by 10   (Max - lvl 10)
{Fore.BLACK}Type /upgrade [stat] to upgrade
""")

    if command == '/upgrade attack' or command == '/upgrade [attack]':
        valid_command = True
        atklevel = int((var.player_attack - 5) / 5)
        atkcoins = 50 + (50*atklevel)
        if atklevel < 10:
            if var.player_coins - atkcoins >=0:
                var.player_coins -= atkcoins
                var.player_attack += 5
                atklevel += 1
                print('You successfully upgraded your attack to level '+str(atklevel)+' for '+str(atkcoins)+' coins')
            else:
                print("You don't have enough coins!")
        else:
            print("Your attack is already at the max level!")
    if command == '/upgrade defense' or command == '/upgrade [defense]':
        valid_command = True
        deflevel = int((var.player_defense - 5) / 5)
        defcoins = 50 + (50*deflevel)
        if deflevel < 10:
            if var.player_coins - defcoins >=0:
                var.player_coins -= defcoins
                var.player_defense += 5
                deflevel += 1
                print('You successfully upgraded your defense to level '+str(deflevel)+' for '+str(defcoins)+' coins')
            else:
                print("You don't have enough coins!")
        else:
            print("Your attack is already at the max level!")
    if command == '/upgrade health' or command == '/upgrade [health]':
        hlthlevel = int((var.max_health - 100) / 10)
        hlthcoins = 50 + (50*hlthlevel)
        valid_command = True
        if hlthlevel < 10:
            if var.player_coins - hlthcoins >=0:
                var.player_coins -= hlthcoins
                var.max_health += 10
                var.player_health = var.max_health
                hlthlevel += 1
                print('You successfully upgraded your health to level '+str(hlthlevel)+' for '+str(hlthcoins)+' coins')
            else:
                print("You don't have enough coins!")
        else:
            print("Your attack is already at the max level!")
    
    elif command == '/battle':
        valid_command = True
        battle_start()
    elif command == '/exit':
        valid_command = True
        print(Fore.YELLOW + 'Thank you for playing. See you later!')
        try:
          t1.join()
        except NameError:
          pass
          
        exit()
    elif command == '/stats':
        valid_command = True
        atklevel = int((var.player_attack - 5) / 5)
        deflevel = int((var.player_defense - 5) / 5)
        hlthlevel = int((var.max_health - 100) / 10)
        print(f"""
Stats for {var.name}:
🗡️  Attack: {Fore.MAGENTA}{str(var.player_attack)}{Fore.RESET}  (Level {atklevel})
🛡️  Defense: {Fore.GREEN}{str(var.player_defense)}{Fore.RESET} (Level {deflevel})
❤️  Health: {Fore.LIGHTRED_EX}{str(var.player_health)}{Fore.RESET} (Level {hlthlevel})
""")
        if var.lifesaver == True:
            print(Style.DIM + 'Lifesaver active')
    elif command == '/coins':
        valid_command = True
        print('You currently have ' + str(var.player_coins) + ' coins.')

    elif '/givecoins' in command:
        valid_command = True
        if var.name in var.admins:
            if ' ' in command:
              splitlist = command.split(" ")
              try:
                  givecoins = int(splitlist[1])
                  var.player_coins += givecoins
                  print('Gave ' + str(givecoins) + ' coins')
              except ValueError:
                  print('That is not a number!')
            else:
              print('No value provided')
        else:
            print('Nice try but only admins can do that')

    elif '/sethealth' in command:
        valid_command = True
        if var.name in var.admins:
            if ' ' in command: 
              splitlist = command.split(" ")
              try:
                var.player_health = int(splitlist[1])
                print('Your health is now '+str(var.player_health))
              except ValueError:
                 print('That is not a number!')

            else:
              print('No value provided')
        else:
            print('Nice try but only admins can do that')

    elif '/setattack' in command:
        valid_command = True
        if var.name in var.admins:
            if ' ' in command:
              splitlist = command.split(" ")
              try:
                var.player_attack = int(splitlist[1])
                print('Your attack is now '+str(var.player_attack))
              except ValueError:
                print('That is not a number!')
            else:
              print('No value provided')
        else:
            print('Nice try but only admins can do that')


    elif '/setdefense' in command:
        valid_command = True
        if var.name in var.admins:
            if ' ' in command:
              splitlist = command.split(" ")
              try:
                var.player_defense = int(splitlist[1])
                print('Your defense is now '+str(var.player_defense))
              except ValueError:
                print('That is not a number!')
            else:
              print('No value provided')
        else:
            print('Nice try but only admins can do that')

    elif command == '/hack':
      while True:
        print('01', end="")

    elif command == '/resetall':
        valid_command = True
        if var.name in var.admins:
            var.player_attack = 5
            var.player_defense = 5
            var.player_coins = 0
            var.player_health = 100
            print(Fore.YELLOW + 'Reset all your data')
        else:
            print('Nice try but only admins can do that')

    elif command == '/admincommands':
      if var.name in var.admins:
        print(f"""
    /givecoins {Fore.LIGHTBLUE_EX}[amount]{Fore.RESET} - gives x amount of coins
    /setattack {Fore.LIGHTBLUE_EX}[amount]{Fore.RESET} - sets x amount of attack
    /setdefense {Fore.LIGHTBLUE_EX}[amount]{Fore.RESET} - sets x amount of defense
    /sethealth {Fore.LIGHTBLUE_EX}[amount]{Fore.RESET} - sets x amount of health
    /hack - do not try this....
    /resetall - resets all your data
  """)
      else:
         print('You are not an admin!')


    elif not valid_command:
        print(Fore.RED + "That is not a valid command. Type /help for a list of commands")

    valid_command = False
    var.save_data(var.name, var.player_attack, var.player_defense, var.player_health, var.player_coins)