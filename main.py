# DISCLAIMER
# OPEN CONSOLE FULL SCREEN FOR THE BEST EXPERIENCE

import var
import time
import random
import sys
from battle import battle_start
from colorama import Fore, Back, Style, init
init(autoreset=True)


def print_slow(text, speed=0.01):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)


tutorial = False

# Tutorial
if tutorial == True:
    print("Welcome to Raid Villagers! Raid villagers is a trhilling text-based adventure game where you play as a ruthless raider, attacking and looting villages for gold and treasure. Your ultimate goal is to become the most powerful raider in the land by upgrading your character's stats. You will have to make strategic choices, outsmart the village defenders, and overcome dangerous obstacles to succeed. You will gain gold throughout your journey. Spend it wisely on your character stats. Now are you ready to embark on this epic adventure?  Let's begin!\n")
    time.sleep(5)

    print_slow('Player Name: ')
    name = input(Fore.CYAN)
    time.sleep(0.2)
    print(Style.RESET_ALL + 'Welcome ' + name +
          '. Let\'s start by attacking your first village.')
    time.sleep(2)

    battle_start()

else:
    print_slow('Player Name: ')
    name = input(Fore.CYAN)
    print(Style.RESET_ALL, end="")
    print_slow('Would you like a quick tutorial? ')
    quicktutorial = input(Fore.CYAN)
    print(Style.RESET_ALL, end="")
    if quicktutorial.lower() == 'yes':
        print("Ok, here is a quick tutorial. Lets start by going into a battle.")
        time.sleep(2)
        battle_start(True)
    if quicktutorial.lower() == 'no':
        print("Ok. If you need a list of commands type " + Fore.CYAN + "/help\n")
    else:
        print(
            "That is not a valid option! I guess you don't want a tutorial. If you ever need a list of commands, just type /help"
        )

if tutorial == True:
    print(
        'You are now ready to play the game! Type /help to view the list of commands...'
    )

valid_command = False

while True:
    var.state = 'menu'
    command = input(Fore.CYAN).lower()
    print(Style.RESET_ALL, end="")
    if command == '/help':
        valid_command = True
        print('''
  /help - displays the help command
  /battle - starts a battle
  /upgrades - displays a list of upgrades to your character
  /stats - displays your current stats
  /shop - brings a menu with items you can buy
  /coins - displays current amount of coins
  /exit - exits the game (progress does not save)''')
    if command == '/shop':
        valid_command = True
        print(f"""
{Style.BRIGHT}SHOP          Your coins: {Fore.LIGHTYELLOW_EX}{var.player_coins}{Style.RESET_ALL}
🍖 Meat - {Fore.GREEN}100 coins{Style.RESET_ALL}
     Restores health for 50 hitpoints on purchase.
💝 Lifesaver - {Fore.GREEN}250 coins{Style.RESET_ALL}
     Gives another change if you are about to die. (Can only buy one at a time)
{Fore.BLACK}Type /buy [item] to purchase""")
    if command == '/buy meat':
        valid_command = True
        if var.player_health != 100:
            if var.player_coins - 100 >= 0:
                var.player_coins -= 100
                var.player_health += 50
                if var.player_health >= 100:
                    var.player_health = 100
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
            
    elif command == '/upgrades':
        valid_command = True
        atklevel = var.player_attack - 4
        deflevel = var.player_defense - 4
        hlthlevel = int((var.player_health - 95) / 5)

        atkcoins = 50 + (50*atklevel)
        defcoins = 50 + (50*deflevel)
        hlthcoins = 50 + (50*hlthlevel)

        print(f"""
{Style.BRIGHT}UPGRADES         Your coins: {Fore.YELLOW}{var.player_coins}{Style.RESET_ALL}
🗡️ Attack (Lvl {atklevel}) - {Fore.GREEN}{atkcoins} coins{Fore.RESET}
     Increases attack by 1
🛡️ Defense (Lvl {deflevel}) - {Fore.GREEN}{defcoins} coins{Fore.RESET}
     Increases defense by 1
❤️ Health (Lvl {hlthlevel}) - {Fore.GREEN}{hlthcoins} coins{Fore.RESET}
     Increases max health by 5
{Fore.BLACK}Type /upgrade [stat] to upgrade""")

    if command == '/upgrade attack':
        valid_command = True
        atklevel = var.player_attack - 4
        atkcoins = 50 + (50*atklevel)
        if atklevel <= 10:
            if var.player_coins - atkcoins >=0:
                var.player_coins -= atkcoins
                var.player_attack += 1
                atklevel += 1
                print('You successfully upgraded your attack to level '+str(atklevel)+' for '+str(atkcoins)+' coins')
            else:
                print("You don't have enough coins!")
        else:
            print("Your attack is already at the max level!")
    if command == '/upgrade defense':
        valid_command = True
        deflevel = var.player_defense - 4
        defcoins = 50 + (50*deflevel)
        if deflevel <= 10:
            if var.player_coins - defcoins >=0:
                var.player_coins -= defcoins
                var.player_defense += 1
                deflevel += 1
                print('You successfully upgraded your defense to level '+str(deflevel)+' for '+str(defcoins)+' coins')
            else:
                print("You don't have enough coins!")
        else:
            print("Your attack is already at the max level!")
    if command == '/upgrade health':
        hlthlevel = int((var.player_health - 95) / 5)
        hlthcoins = 50 + (50*hlthlevel)
        valid_command = True
        if hlthlevel <= 10:
            if var.player_coins - hlthcoins >=0:
                var.player_coins -= hlthcoins
                var.player_health += 5
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
        exit()
    elif command == '/stats':
        valid_command = True
        print(f"""
Stats for {name}:
🗡️ Attack: {str(var.player_attack)}
🛡️ Defense: {str(var.player_defense)}
❤️ Health: {str(var.player_health)}""")
        if var.lifesaver == True:
            print(Style.DIM + 'Lifesaver active')
    elif command == '/coins':
        valid_command = True
        print('You currently have ' + str(var.player_coins) + ' coins.')
    elif '/givecoins' in command:
        valid_command = True
        splitlist = command.split(" ")
        try:
            givecoins = int(splitlist[1])
            var.player_coins += givecoins
            print('Gave ' + str(givecoins) + ' coins')
        except ValueError:
            print('That is not a number!')
       
    elif '/sethealth' in command:
        valid_command = True
        splitlist = command.split(" ")
        var.player_health = int(splitlist[1])
        if ValueError == True:
            print('That is not a number!')
        print('Your health is now'+str(var.player_health))
    elif not valid_command:
        print(Fore.RED + "That is not a valid command. Type /help for a list of commands")

    valid_command = False
