import time
import random
import var
import math
import sys
from colorama import Fore, Back, Style, init
init(autoreset=True)

def print_slow(text, speed=0.01):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)


def battle_start(tutorial=None):

    if var.tutorial == True:
        var.village_health = random.randrange(70, 80)
    else:
        minimum = int((var.player_attack * 150 / 100)) + \
                      random.randrange(140, 180)
        maximum = int((var.player_attack * 220 / 100)) + \
                      random.randrange(181, 250)
        var.village_health = random.randrange(minimum, maximum)

    print('The battle has started! This village has ' +
          Fore.YELLOW + Style.BRIGHT + str(var.village_health) + Style.RESET_ALL + ' health')
    time.sleep(2.5)

    if tutorial == True:
        print('Now you will choose your weapon. Type the name of the weapon you would like to choose.')
        time.sleep(3)

    weapon1 = random.choice(var.weaponlist)
    var.weaponlist.remove(weapon1)
    weapon2 = random.choice(var.weaponlist)
    var.weaponlist.remove(weapon2)
    weapon3 = random.choice(var.weaponlist)
    var.weaponlist.remove(weapon3)

    var.weaponlist.append(weapon1)
    var.weaponlist.append(weapon2)
    var.weaponlist.append(weapon3)

    print('\nChoose your weapon to begin')
    time.sleep(1)

    print('\n  ' + weapon1 + '        ' +
          weapon2 + '        ' + weapon3 + '\n')
    time.sleep(1)

    global player_weapon

    player_weapon = input('Your weapon: ' + Fore.CYAN)
    while player_weapon.lower() not in var.weaponlist:

        print(Style.RESET_ALL + 'That is not an option')
        time.sleep(0.5)
        player_weapon = input('Your weapon: ' + Fore.CYAN)
    print(Style.RESET_ALL)

    if player_weapon == 'nuclear bomb':
        print('You choose such an overpowered weapon that you automatically won the game!')
        var.village_health = 0
    elif player_weapon == 'machine gun':
        print('Good choice. Your weapon gave you ' + Fore.GREEN +
              '+10' + Style.RESET_ALL + ' attack bonous')
        var.player_attack += 10
    elif player_weapon == 'water gun':
        print('Why did you choose such a terrible weapon. You have no weapon attack bonus.')

    elif player_weapon == 'stick':
        print('Bro what were you thinking. Your stick broke during battle. Now you have no weapon attack bonous.')
    else:
        print('Good choice. Your weapon gave you ' + Fore.GREEN +
              '+5' + Style.RESET_ALL + ' attack bonous')
        var.player_attack += 5

    time.sleep(2)
    if var.tutorial == True:
        print('\nNow we will begin the battle. Below you will be asked to choose an option. Type the option you want to choose...\n')
        time.sleep(4)
    battle(player_weapon)



def battle(player_weapon):
    if var.village_health <= 0:
        if player_weapon == 'machine gun':
          var.player_attack -= 10
        else:
          var.player_attack -= 5
        print('\n' + Fore.GREEN + 'Congratulations, you have successfully destroyed the village! You gained a total of ' +
              Fore.LIGHTYELLOW_EX + str(var.raid_coins) + Fore.RESET + ' coins!')
        var.player_coins += var.raid_coins
        var.raid_coins = 0
        return None
    if var.player_health <= 0:
        print(Fore.LIGHTMAGENTA_EX +
              'Oh no! You have been killed in the raid! You lost the coins you gained in the raid.')
        var.raid_coins = 0
        return None

    global choice1
    global choice2
    global choice3

    choice1 = random.choice(var.choicelist)
    var.choicelist.remove(choice1)
    choice2 = random.choice(var.choicelist)
    var.choicelist.remove(choice2)
    choice3 = random.choice(var.choicelist)
    var.choicelist.remove(choice3)

    var.choicelist.append(choice1)
    var.choicelist.append(choice2)
    var.choicelist.append(choice3)
    var.choicelist.sort()

    if choice1 == var.choicelist[0]:
        choice1 = player_weapon + choice1
    elif choice2 == var.choicelist[0]:
        choice2 = player_weapon + choice2
    elif choice3 == var.choicelist[0]:
        choice3 = player_weapon + choice2


    print('\nChoose an option from the following:\n' + 'a) ' +
          choice1 + '\n' + 'b) ' + choice2 + '\n' + 'c) ' + choice3 + '\n')
    time.sleep(1)

    while True:
        print_slow('Your choice: ')
        player_choice = input(Fore.CYAN)
        print(Style.RESET_ALL, end="")
        if player_choice.lower() == choice1.lower() or player_choice.lower() == choice2.lower() or player_choice.lower() == choice3.lower() or player_choice == 'a' or player_choice == 'b' or player_choice == 'c' or player_choice == 'a)' or player_choice == 'b)' or player_choice == 'c)':
            if player_choice == 'a' or player_choice == 'a)':
                player_choice = choice1
            if player_choice == 'b' or player_choice == 'b)':
                 player_choice = choice2
            if player_choice == 'c' or player_choice == 'c)':
                 player_choice = choice3
            player_choice = player_choice.capitalize()
            break
        else:
            Style.RESET_ALL
            print('That is not an option!')
            time.sleep(0.5)
    print(Style.RESET_ALL, end="")
    battle_result(player_choice)


def battle_result(player_choice):
    if player_choice == var.choicelist[8]:
        selected_event = random.choices(
            var.choiceraidlist, weights=var.raidweights, k=1)[0]
        selected_event = selected_event["event"]

        if selected_event == var.choiceraidlist[0]['event']:
            result_creator(
                selected_event, xdmg=var.choiceraidlist[0]["xdmg"], ydmg=var.choiceraidlist[0]["ydmg"])
        elif selected_event == var.choiceraidlist[1]['event']:
            result_creator(selected_event, xdmg=var.choiceraidlist[1]["xdmg"], ydmg=var.choiceraidlist[1]
                           ["ydmg"], xcoins=var.choiceraidlist[1]["xcoins"], ycoins=var.choiceraidlist[1]["ycoins"])
        elif selected_event == var.choiceraidlist[2]['event']:
            result_creator(
                selected_event, xcoins=var.choiceraidlist[2]["xcoins"], ycoins=var.choiceraidlist[2]["ycoins"])
        elif selected_event == var.choiceraidlist[3]['event']:
            result_creator(
                selected_event, xhlth=var.choiceraidlist[3]["xhlth"], yhlth=var.choiceraidlist[3]["yhlth"])
        elif selected_event == var.choiceraidlist[4]['event']:
            result_creator(selected_event, xhlth=var.choiceraidlist[4]["xhlth"], yhlth=var.choiceraidlist[4]["yhlth"])

    if player_choice == var.choicelist[9]:
        selected_event = random.choices(
            var.choicetreasurylist, weights=var.treasuryweights, k=1)[0]
        selected_event = selected_event["event"]
        if selected_event == var.choicetreasurylist[0]['event']:
            result_creator(selected_event, xdmg=var.choicetreasurylist[0]["xdmg"], ydmg=var.choicetreasurylist[0]["ydmg"], xcoins=var.choicetreasurylist[0]["xcoins"], ycoins=var.choicetreasurylist[0]["ycoins"])
        elif selected_event == var.choicetreasurylist[1]['event']:
            result_creator(selected_event, xdmg=var.choicetreasurylist[1]["xdmg"], ydmg=var.choicetreasurylist[1]["ydmg"], xcoins=var.choicetreasurylist[1]["xcoins"], ycoins=var.choicetreasurylist[1]["ycoins"])
        elif selected_event == var.choicetreasurylist[2]['event']:
            result_creator(selected_event, xdmg=var.choicetreasurylist[2]["xdmg"], ydmg=var.choicetreasurylist[2]["ydmg"], xcoins=var.choicetreasurylist[2]["xcoins"], ycoins=var.choicetreasurylist[2]["ycoins"])
        elif selected_event == var.choicetreasurylist[3]['event']:
            result_creator(selected_event)
        elif selected_event == var.choicetreasurylist[4]['event']:
            result_creator(selected_event, xhlth=var.choicetreasurylist[4]['xhlth'], yhlth=var.choicetreasurylist[4]['yhlth'])
        elif selected_event == var.choicetreasurylist[5]['event']:
            result_creator(selected_event, xhlth=var.choicetreasurylist[5]['xhlth'], yhlth=var.choicetreasurylist[5]['yhlth'])

    if player_choice == var.choicelist[11]:
        selected_event = random.choices(
            var.choicefirelist, weights=var.fireweights, k=1)[0]
        selected_event = selected_event["event"]
        if selected_event == var.choicefirelist[0]['event']:
            result_creator(selected_event, xdmg=var.choicefirelist[0]["xdmg"], ydmg=var.choicefirelist[0]["ydmg"], xcoins=var.choicefirelist[0]["xcoins"], ycoins=var.choicefirelist[0]["ycoins"])
        elif selected_event == var.choicefirelist[1]['event']:
            result_creator(selected_event, xdmg=var.choicefirelist[1]["xdmg"], ydmg=var.choicefirelist[1]["ydmg"], xcoins=var.choicefirelist[1]["xcoins"], ycoins=var.choicefirelist[1]["ycoins"])
        elif selected_event == var.choicefirelist[2]['event']:
            result_creator(selected_event, xdmg=var.choicefirelist[2]["xdmg"], ydmg=var.choicefirelist[2]["ydmg"])
        elif selected_event == var.choicefirelist[3]['event']:
            result_creator(selected_event, xdmg=var.choicefirelist[3]["xdmg"], ydmg=var.choicefirelist[3]["ydmg"], xcoins=var.choicefirelist[3]["xcoins"], ycoins=var.choicefirelist[3]["ycoins"])
        elif selected_event == var.choicefirelist[4]['event']:
            result_creator(selected_event)
        elif selected_event == var.choicefirelist[5]['event']:
            result_creator(selected_event, xhlth=var.choicefirelist[5]["xhlth"], yhlth=var.choicefirelist)

    if player_choice == var.choicelist[1]:
        selected_event = random.choices(
            var.choicefortlist, weights=var.fortweights, k=1)[0]
        selected_event = selected_event["event"]
        if selected_event == var.choicefortlist[0]['event']:
            result_creator(selected_event, xdmg=var.choicefortlist[0]["xdmg"], ydmg=var.choicefortlist[0]["ydmg"], xcoins=var.choicefortlist[0]["xcoins"], ycoins=var.choicefortlist[0]["ycoins"])
        elif selected_event == var.choicefortlist[1]['event']:
            result_creator(selected_event, xdmg=var.choicefortlist[1]["xdmg"], ydmg=var.choicefortlist[1]["ydmg"], xcoins=var.choicefortlist[1]["xcoins"], ycoins=var.choicefortlist[1]["ycoins"])
        elif selected_event == var.choicefortlist[2]['event']:
            result_creator(selected_event, xdmg=var.choicefortlist[2]["xdmg"], ydmg=var.choicefortlist[2]["ydmg"], xcoins=var.choicefortlist[2]["xcoins"], ycoins=var.choicefortlist[2]["ycoins"])
        elif selected_event == var.choicefortlist[3]['event']:
            result_creator(selected_event, xdmg=var.choicefortlist[3]["xdmg"], ydmg=var.choicefortlist[3]["ydmg"])
        elif selected_event == var.choicefortlist[4]['event']:
            result_creator(selected_event, xhlth=var.choicefortlist[4]["xhlth"], yhlth=var.choicefortlist[4]["yhlth"])


    if player_choice == var.choicelist[2]:
        selected_event = random.choices(
            var.choicemansionlist, weights=var.mansionweights, k=1)[0]
        selected_event = selected_event["event"]
        if selected_event == var.choicemansionlist[0]['event']:
            result_creator(selected_event, xdmg=var.choicemansionlist[0]["xdmg"], ydmg=var.choicemansionlist[0]["ydmg"])
        elif selected_event == var.choicemansionlist[1]['event']:
            result_creator(selected_event, xdmg=var.choicemansionlist[1]["xdmg"], ydmg=var.choicemansionlist[1]["ydmg"], xcoins=var.choicemansionlist[1]["xcoins"], ycoins=var.choicemansionlist[1]["ycoins"])
        elif selected_event == var.choicemansionlist[2]['event']:
            result_creator(selected_event, xcoins=var.choicemansionlist[2]["xcoins"], ycoins=var.choicemansionlist[2]["ycoins"])
        elif selected_event == var.choicemansionlist[3]['event']:
            result_creator(selected_event, xcoins=var.choicemansionlist[3]["xcoins"], ycoins=var.choicemansionlist[3]["ycoins"])
            var.player_defense += 6
        elif selected_event == var.choicemansionlist[4]['event']:
            result_creator(selected_event, xdmg=var.choicemansionlist[4]["xdmg"], ydmg=var.choicemansionlist[4]["ydmg"])
        elif selected_event == var.choicemansionlist[5]['event']:
            result_creator(selected_event, xhlth=var.choicemansionlist[5]["xhlth"], yhlth=var.choicemansionlist[5]["yhlth"])
        elif selected_event == var.choicemansionlist[6]['event']:
            result_creator(selected_event, xhlth=var.choicemansionlist[6]["xhlth"], yhlth=var.choicemansionlist[6]["yhlth"])


    if player_choice == var.choicelist[13]:
        selected_event = random.choices(
            var.choiceswimlist, weights=var.swimweights, k=1)[0]
        selected_event = selected_event["event"]
        if selected_event == var.choiceswimlist[0]['event']:
            result_creator(selected_event, xcoins=var.choiceswimlist[0]["xcoins"], ycoins=var.choiceswimlist[0]["ycoins"])
        elif selected_event == var.choiceswimlist[1]['event']:
            result_creator(selected_event, xcoins=var.choiceswimlist[1]["xcoins"], ycoins=var.choiceswimlist[1]["ycoins"])
        elif selected_event == var.choiceswimlist[2]['event']:
            result_creator(selected_event, xcoins=var.choiceswimlist[2]["xcoins"], ycoins=var.choiceswimlist[2]["ycoins"])
        elif selected_event == var.choiceswimlist[3]['event']:
            result_creator(selected_event)
        elif selected_event == var.choiceswimlist[4]['event']:
            result_creator(selected_event, xhlth=var.choiceswimlist[4]["xhlth"], yhlth=var.choiceswimlist[4]["yhlth"])


    time.sleep(2.2)
    battle(player_weapon)


def result_creator(selected_event, xdmg=None, ydmg=None, xcoins=None, ycoins=None, xhlth=None, yhlth=None):

    if '**' in selected_event:
        random_attack=random.randrange(xdmg, ydmg)
        attack = math.ceil((var.player_attack * 50 / 100) + (random_attack * 90 / 100))
        var.village_health -= attack
        selected_event=selected_event.replace(
            "**", Fore.MAGENTA + str(attack) + Fore.RESET)
    if '++' in selected_event:
        random_coins=random.randrange(xcoins, ycoins)
        selected_event=selected_event.replace(
            "++", Fore.LIGHTYELLOW_EX + str(random_coins) + Fore.RESET)
        var.raid_coins += random_coins
    if '--' in selected_event:
        random_damage = random.randrange(xhlth, yhlth)
        selected_event=selected_event.replace(
            "--", Fore.RED + str(random_damage)+Fore.RESET)
        var.player_health = int((var.player_health - random_damage + math.floor(var.player_health * 30 / 100)) + (var.player_defense * 90 / 100))

    print(selected_event)
