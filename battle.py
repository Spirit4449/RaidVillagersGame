import time
import random
import var
import sys
from colorama import Fore, Style, init

# Initializes colorama
init(autoreset=True)

# Print slow function


def print_slow(text, speed=0.01):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)

# Starts the battle. Sets village health etc..


def battle_start(tutorial=None):
    # Changes state of the game
    var.state = 'battle'
    # If player health is 0 they cannot start a game
    if var.player_health == 0:
        print(Fore.RED + 'You cannot start a battle with 0 health! Buy meat from the shop to increase your health.')
        return

    # if the tutorial is true, it will guide them through the battle and make it easier to win
    if var.tutorial == True:
        var.village_health = random.randrange(40, 70)
    # Range of values if player attack is less than 10
    elif var.player_attack <= 10:
        minimum = int((var.player_attack * 150 / 100)) + \
            random.randrange(70, 100)
        maximum = int((var.player_attack * 220 / 100)) + \
            random.randrange(101, 140)
        var.village_health = random.randrange(minimum, maximum)
    # Range of values if player attack is between 10 and 20
    elif var.player_attack > 10 and var.player_attack <= 20:
        minimum = int((var.player_attack * 150 / 100)) + \
            random.randrange(90, 120)
        maximum = int((var.player_attack * 220 / 100)) + \
            random.randrange(121, 160)
        var.village_health = random.randrange(minimum, maximum)
    # Range of values if player atack is above 20
    else:
        minimum = int((var.player_attack * 150 / 100)) + \
            random.randrange(140, 180)
        maximum = int((var.player_attack * 220 / 100)) + \
            random.randrange(181, 250)
        var.village_health = random.randrange(minimum, maximum)

    print('The battle has started! This village has ' +
          Fore.YELLOW + Style.BRIGHT + str(var.village_health) + Style.RESET_ALL + ' health')
    time.sleep(2)

    # Prints the current stats of the player
    print(f"""
Your Stats:
🗡️  Attack: {Fore.MAGENTA}{str(var.player_attack)}{Fore.RESET}
🛡️  Defense: {Fore.GREEN}{str(var.player_defense)}{Fore.RESET}
❤️  Health: {Fore.RED}{str(var.player_health)}{Fore.RESET}
""")

    time.sleep(2)

    if tutorial == True:
        print('Now you will choose your weapon. Type the name of the weapon you would like to choose.')
        time.sleep(3)

    global player_weapon

    # Randomly picks the weapons and puts it into 3 choices
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

    print(f'''
a) {weapon1}
b) {weapon2}
c) {weapon3}
''')
    time.sleep(1)

    # Player chooses weapon
    print_slow('Your weapon: ')
    player_weapon = input(Fore.CYAN).lower()

    # The while loop is so the game continues forever if the weapon is not in the weapon list
    while True:
        if player_weapon in var.weaponlist or player_weapon == 'a' or player_weapon == 'b' or player_weapon == 'c':
            break
        else:
            print(Fore.RED + 'That is not an option')
            time.sleep(0.5)
            print_slow('Your weapon: ')
            player_weapon = input(Fore.CYAN).lower()

    print(Style.RESET_ALL)

    if player_weapon == 'a':
        player_weapon = weapon1
    if player_weapon == 'b':
        player_weapon = weapon2
    if player_weapon == 'c':
        player_weapon = weapon3

    # Special cases of weapons does special things
    if player_weapon == 'atomic bomb':
        print('You choose such an overpowered weapon that you automatically won the game!')
        var.raid_coins += 200
        var.village_health = 0
    elif player_weapon == 'machine gun':
        print('Good choice. Your weapon gave you ' + Fore.GREEN +
              '+10' + Style.RESET_ALL + ' attack bonus')
        var.raid_attack += 10
        var.player_attack += 10
    elif player_weapon == 'water gun':
        print('Why did you choose such a terrible weapon. You have no weapon attack bonus.')

    elif player_weapon == 'stick':
        print('Bro what were you thinking. Your stick broke during battle. Now you have no weapon attack bonus.')
    else:
        print('Good choice. Your weapon gave you ' + Fore.GREEN +
              '+5' + Style.RESET_ALL + ' attack bonus')
        var.raid_attack += 5
        var.player_attack += 5

    time.sleep(2)
    if var.tutorial == True:
        print('\nNow we will begin the battle. Below you will be asked to choose an option. Type the option you want to choose...\n')
        time.sleep(4)
    battle(player_weapon)


# Now the battle begins
def battle(player_weapon):

    # If they destroy the village
    if var.village_health <= 0:
        if var.halftimesdamage == True:
          var.player_attack /= 1.5
          var.halftimesdamage = False
          var.player_attack = round(var.player_attack)
        if var.double_damage == True:
          var.player_attack /= 2
          var.double_damage = False
          var.player_attack = round(var.player_attack)
          
        var.player_attack -= var.raid_attack
        var.player_defense -= var.raid_defense
        var.player_defense += var.raid_subdefense 
        print('\n' + Fore.GREEN + 'Congratulations, you have successfully destroyed the village! You gained a total of ' +
              Fore.LIGHTYELLOW_EX + str(var.raid_coins) + Fore.GREEN + ' coins!')
        var.player_coins += var.raid_coins
        var.raid_coins = 0
        var.raid_attack = 0
        var.raid_defense = 0
        time.sleep(1)
        return

    # If the player dies
    if var.player_health <= 0:
        # If the player dies with a lifesaver
        if var.lifesaver == True:
            print(Fore.MAGENTA + 'You were killed in the battle but your lifesaver saved you! The battle continues!')
            var.player_health = var.max_health
            var.lifesaver = False
            time.sleep(2)

        # If the player dies without a lifesaver
        else:
            print(Fore.RED +
                  'Oh no! You have been killed in the raid! You lost 20% your coins. The battle has ended.')
            var.player_coins = int(
                var.player_coins - (var.player_coins * 20 / 100))
            var.player_coins += var.raid_coins
            var.raid_coins = 0
            var.player_attack -= var.raid_attack
            var.player_defense += var.raid_defense
            if var.player_health <= 0:
                var.player_health = var.max_health
            var.raid_attack = 0
            var.raid_defense = 0
            return None

    global choice1
    global choice2
    global choice3

    # Randomly chooses 3 choices for the player to pick from
    choice1 = random.choice(var.choicelist)
    var.choicelist.remove(choice1)
    choice2 = random.choice(var.choicelist)
    var.choicelist.remove(choice2)
    choice3 = random.choice(var.choicelist)
    var.choicelist.remove(choice3)

    # If the choice is 'a house' the game will add the player weapon in front of it
    if choice1 == ' a house':
        choice1 = player_weapon + '' + choice1
    elif choice2 == ' a house':
        choice2 = player_weapon + '' + choice2
    elif choice3 == ' a house':
        choice3 = player_weapon + '' + choice3

    # Clears the list for the next line of code
    var.choicelist.clear()
    # Readds all the choices into the list
    var.choicelist.extend(var.choicecopylist)

    print('\nChoose an option from the following:\n' + 'a) ' +
          choice1 + '\n' + 'b) ' + choice2 + '\n' + 'c) ' + choice3 + '\n')
    time.sleep(.2)

    while True:
        # Saves data
        var.save_data(var.name, var.player_attack,
                      var.player_defense, var.player_health, var.max_health, var.player_coins)

        # Player chooses their choice
        print_slow('Your choice: ')
        player_choice = input(Fore.CYAN)
        print(Style.RESET_ALL, end="")
        if player_choice.lower() == choice1.lower() or player_choice.lower() == choice2.lower() or player_choice.lower() == choice3.lower() or player_choice.lower() == 'a' or player_choice.lower() == 'b' or player_choice.lower() == 'c' or player_choice.lower() == 'a)' or player_choice.lower() == 'b)' or player_choice.lower() == 'c)' or player_choice.lower() == player_weapon + ' a house' or player_choice.lower() == player_weapon + ' a house' or player_choice.lower() == player_weapon + ' a house':
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
    battle_result(player_choice, player_weapon)


# Result of the battle
def battle_result(player_choice, player_weapon):

    if player_choice.lower() == player_weapon + ' a house':
        selected_event = random.choices(
            var.choicehouselist, weights=var.houseweights, k=1)[0]
        selected_event = selected_event["event"]
        result_creator(
            selected_event, xdmg=var.choiceraidlist[0]["xdmg"], ydmg=var.choiceraidlist[0]["ydmg"])

    if player_choice == var.choicelist[1]:
        selected_event = random.choices(
            var.choicefortlist, weights=var.fortweights, k=1)[0]
        selected_event = selected_event["event"]
        if selected_event == var.choicefortlist[0]['event']:
            result_creator(selected_event, xdmg=var.choicefortlist[0]["xdmg"], ydmg=var.choicefortlist[0]
                           ["ydmg"], xcoins=var.choicefortlist[0]["xcoins"], ycoins=var.choicefortlist[0]["ycoins"])
        elif selected_event == var.choicefortlist[1]['event']:
            result_creator(selected_event, xdmg=var.choicefortlist[1]["xdmg"], ydmg=var.choicefortlist[1]
                           ["ydmg"], xcoins=var.choicefortlist[1]["xcoins"], ycoins=var.choicefortlist[1]["ycoins"])
        elif selected_event == var.choicefortlist[2]['event']:
            result_creator(selected_event, xdmg=var.choicefortlist[2]["xdmg"], ydmg=var.choicefortlist[2]
                           ["ydmg"], xcoins=var.choicefortlist[2]["xcoins"], ycoins=var.choicefortlist[2]["ycoins"])
        elif selected_event == var.choicefortlist[3]['event']:
            result_creator(
                selected_event, xdmg=var.choicefortlist[3]["xdmg"], ydmg=var.choicefortlist[3]["ydmg"])
        elif selected_event == var.choicefortlist[4]['event']:
            result_creator(
                selected_event, xhlth=var.choicefortlist[4]["xhlth"], yhlth=var.choicefortlist[4]["yhlth"])

    if player_choice == var.choicelist[2]:
        selected_event = random.choices(
            var.choicemansionlist, weights=var.mansionweights, k=1)[0]
        selected_event = selected_event["event"]
        if selected_event == var.choicemansionlist[0]['event']:
            result_creator(
                selected_event, xdmg=var.choicemansionlist[0]["xdmg"], ydmg=var.choicemansionlist[0]["ydmg"])
        elif selected_event == var.choicemansionlist[1]['event']:
            result_creator(selected_event, xdmg=var.choicemansionlist[1]["xdmg"], ydmg=var.choicemansionlist[1]
                           ["ydmg"], xcoins=var.choicemansionlist[1]["xcoins"], ycoins=var.choicemansionlist[1]["ycoins"])
        elif selected_event == var.choicemansionlist[2]['event']:
            result_creator(
                selected_event, xcoins=var.choicemansionlist[2]["xcoins"], ycoins=var.choicemansionlist[2]["ycoins"])
        elif selected_event == var.choicemansionlist[3]['event']:
            result_creator(
                selected_event, xcoins=var.choicemansionlist[3]["xcoins"], ycoins=var.choicemansionlist[3]["ycoins"])
            var.raid_defense += 5
            var.player_defense += 5
        elif selected_event == var.choicemansionlist[4]['event']:
            result_creator(
                selected_event, xdmg=var.choicemansionlist[4]["xdmg"], ydmg=var.choicemansionlist[4]["ydmg"])
        elif selected_event == var.choicemansionlist[5]['event']:
            result_creator(
                selected_event, xhlth=var.choicemansionlist[5]["xhlth"], yhlth=var.choicemansionlist[5]["yhlth"])
        elif selected_event == var.choicemansionlist[6]['event']:
            result_creator(
                selected_event, xhlth=var.choicemansionlist[6]["xhlth"], yhlth=var.choicemansionlist[6]["yhlth"])

    if player_choice == var.choicelist[3]:
        selected_event = random.choices(
            var.choicedisablelist, weights=var.disableweights, k=1)[0]
        selected_event = selected_event["event"]
        if selected_event == var.choicedisablelist[0]['event']:
            result_creator(
                selected_event, xdmg=var.choicedisablelist[0]["xdmg"], ydmg=var.choicedisablelist[0]["ydmg"])
        elif selected_event == var.choicedisablelist[1]['event']:
            result_creator(
                selected_event, xcoins=var.choicedisablelist[1]["xcoins"], ycoins=var.choicedisablelist[1]["ycoins"])
            var.player_attack = int(var.player_attack * 2)
            var.double_damage = True
        elif selected_event == var.choicedisablelist[2]['event']:
            result_creator(
                selected_event, xdmg=var.choicedisablelist[2]["xdmg"], ydmg=var.choicedisablelist[2]["ydmg"], xcoins=var.choicedisablelist[2]['xcoins'], ycoins=var.choicedisablelist[2]['ycoins'])
        elif selected_event == var.choicedisablelist[3]['event']:
            result_creator(
                selected_event, xcoins=var.choicedisablelist[3]["xcoins"], ycoins=var.choicedisablelist[3]["ycoins"])
            var.player_attack = int(var.player_attack * 1.5)
            var.halftimesdamage = True
        elif selected_event == var.choicedisablelist[4]['event']:
            result_creator(
                selected_event, xcoins=var.choicedisablelist[4]["xcoins"], ycoins=var.choicedisablelist[4]["ycoins"])
            var.player_attack += 5
            var.raid_attack += 5
        elif selected_event == var.choicedisablelist[5]['event']:
            result_creator(
                selected_event, xcoins=var.choicedisablelist[5]["xcoins"], yhlth=var.choicedisablelist[5]["ycoins"])
        elif selected_event == var.choicedisablelist[6]['event']:
            result_creator(
                selected_event, xhlth=var.choicedisablelist[6]["xhlth"], yhlth=var.choicedisablelist[6]["yhlth"])
        elif selected_event == var.choicedisablelist[7]['event']:
            result_creator(
                selected_event, xhlth=var.choicedisablelist[7]["xhlth"], yhlth=var.choicedisablelist[7]["yhlth"])

    if player_choice == var.choicelist[4]:
        selected_event = random.choices(
            var.choicehidelist, weights=var.hideweights, k=1)[0]
        selected_event = selected_event["event"]
        if selected_event == var.choicehidelist[0]['event']:
            result_creator(
                selected_event, xcoins=var.choicehidelist[0]["xcoins"], ycoins=var.choicehidelist[0]["ycoins"])
        elif selected_event == var.choicehidelist[1]['event']:
            result_creator(
                selected_event, xhlth=var.choicehidelist[1]["xhlth"], yhlth=var.choicehidelist[1]["yhlth"])
        elif selected_event == var.choicehidelist[2]['event']:
            result_creator(
                selected_event, xdmg=var.choicehidelist[2]["xdmg"], ydmg=var.choicehidelist[2]["ydmg"])
        elif selected_event == var.choicehidelist[3]['event']:
            result_creator(
                selected_event, xdmg=var.choicehidelist[3]["xdmg"], ydmg=var.choicehidelist[3]["ydmg"], xcoins=var.choicehidelist[3]["xcoins"], ycoins=var.choicehidelist[3]["ycoins"])
        elif selected_event == var.choicehidelist[4]['event']:
            result_creator(
                selected_event, xcoins=var.choicehidelist[4]["xcoins"], ycoins=var.choicehidelist[4]["ycoins"])
        elif selected_event == var.choicehidelist[5]['event']:
            result_creator(selected_event)
            var.player_health += 20
            if var.player_health >= var.max_health:
                var.player_health = var.max_health
        elif selected_event == var.choicehidelist[6]['event']:
            result_creator(
                selected_event, xhlth=var.choicehidelist[6]["xhlth"], yhlth=var.choicehidelist[6]["yhlth"])
        elif selected_event == var.choicehidelist[7]['event']:
            result_creator(
                selected_event, xhlth=var.choicehidelist[7]["xhlth"], yhlth=var.choicehidelist[7]["yhlth"])

    if player_choice == var.choicelist[5]:
        selected_event = random.choices(
            var.choicelibrarylist, weights=var.libraryweights, k=1)[0]
        selected_event = selected_event["event"]
        if selected_event == var.choicelibrarylist[0]['event']:
            result_creator(selected_event)
            var.player_attack += 10
            var.raid_attack += 10
        elif selected_event == var.choicelibrarylist[1]['event']:
            result_creator(
                selected_event, xcoins=var.choicelibrarylist[1]["xcoins"], ycoins=var.choicelibrarylist[1]["ycoins"])
        elif selected_event == var.choicelibrarylist[2]['event']:
            result_creator(selected_event)
        elif selected_event == var.choicelibrarylist[3]['event']:
            result_creator(
                selected_event, xhlth=var.choicelibrarylist[3]["xhlth"], yhlth=var.choicelibrarylist[3]["yhlth"])
        elif selected_event == var.choicelibrarylist[4]['event']:
            result_creator(
                selected_event, xhlth=var.choicelibrarylist[4]["xhlth"], yhlth=var.choicelibrarylist[4]["yhlth"])
        elif selected_event == var.choicelibrarylist[5]['event']:
            result_creator(
                selected_event, xcoins=var.choicelibrarylist[5]["xcoins"], ycoins=var.choicelibrarylist[5]["ycoins"])
        elif selected_event == var.choicelibrarylist[6]['event']:
            result_creator(
                selected_event, xcoins=var.choicelibrarylist[6]["xcoins"], ycoins=var.choicelibrarylist[6]["ycoins"])

    if player_choice == var.choicelist[6]:
        selected_event = random.choices(
            var.choicemarketlist, weights=var.marketweights, k=1)[0]
        selected_event = selected_event["event"]
        if selected_event == var.choicemarketlist[0]['event']:
            result_creator(selected_event, xdmg=var.choicemarketlist[0]["xdmg"], ydmg=var.choicemarketlist[0]
                           ["ydmg"], xcoins=var.choicemarketlist[0]["xcoins"], ycoins=var.choicemarketlist[0]["ycoins"])
        elif selected_event == var.choicemarketlist[1]['event']:
            result_creator(
                selected_event, xdmg=var.choicemarketlist[1]["xdmg"], ydmg=var.choicemarketlist[1]["ydmg"], xcoins=var.choicemarketlist[1]["xcoins"], ycoins=var.choicemarketlist[1]["ycoins"])
        elif selected_event == var.choicemarketlist[2]['event']:
            result_creator(
                selected_event, xhlth=var.choicemarketlist[2]["xhlth"], yhlth=var.choicemarketlist[2]["yhlth"])
        elif selected_event == var.choicemarketlist[3]['event']:
            result_creator(
                selected_event, xhlth=var.choicemarketlist[3]["xhlth"], yhlth=var.choicemarketlist[3]["yhlth"])
        elif selected_event == var.choicemarketlist[4]['event']:
            result_creator(selected_event, xhlth=var.choicemarketlist[4]["xhlth"], yhlth=var.choicemarketlist[4]
                           ["yhlth"])
        elif selected_event == var.choicemarketlist[5]['event']:
            result_creator(selected_event)

    if player_choice == var.choicelist[7]:
        selected_event = random.choices(
            var.choicefarmlist, weights=var.farmweights, k=1)[0]
        selected_event = selected_event["event"]
        if selected_event == var.choicefarmlist[0]['event']:
            result_creator(selected_event, xdmg=var.choicefarmlist[0]["xdmg"], ydmg=var.choicefarmlist[0]
                           ["ydmg"], xcoins=var.choicefarmlist[0]["xcoins"], ycoins=var.choicefarmlist[0]["ycoins"])
        elif selected_event == var.choicefarmlist[1]['event']:
            result_creator(
                selected_event, xcoins=var.choicefarmlist[1]["xcoins"], ycoins=var.choicefarmlist[1]["ycoins"])
        elif selected_event == var.choicefarmlist[2]['event']:
            result_creator(
                selected_event, xdmg=var.choicefarmlist[2]["xdmg"], ydmg=var.choicefarmlist[2]["ydmg"], xcoins=var.choicefarmlist[2]["xcoins"], ycoins=var.choicefarmlist[2]["ycoins"])
        elif selected_event == var.choicefarmlist[3]['event']:
            result_creator(
                selected_event, xdmg=var.choicefarmlist[3]["xdmg"], ydmg=var.choicefarmlist[3]["ydmg"], xcoins=var.choicefarmlist[3]["xcoins"], ycoins=var.choicefarmlist[3]["ycoins"])
        elif selected_event == var.choicefarmlist[4]['event']:
            result_creator(
                selected_event, xhlth=var.choicefarmlist[4]["xhlth"], yhlth=var.choicefarmlist[4]["yhlth"])
        elif selected_event == var.choicefarmlist[5]['event']:
            result_creator(
                selected_event, xhlth=var.choicefarmlist[5]["xhlth"], yhlth=var.choicefarmlist[5]["yhlth"])
        elif selected_event == var.choicefarmlist[6]['event']:
            result_creator(selected_event)
        elif selected_event == var.choicefarmlist[7]['event']:
            result_creator(selected_event)
            var.player_coins -= random.randrange(50, 100)

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
            result_creator(
                selected_event, xhlth=var.choiceraidlist[4]["xhlth"], yhlth=var.choiceraidlist[4]["yhlth"])

    if player_choice == var.choicelist[9]:
        selected_event = random.choices(
            var.choicetreasurylist, weights=var.treasuryweights, k=1)[0]
        selected_event = selected_event["event"]
        if selected_event == var.choicetreasurylist[0]['event']:
            result_creator(selected_event, xdmg=var.choicetreasurylist[0]["xdmg"], ydmg=var.choicetreasurylist[0]
                           ["ydmg"], xcoins=var.choicetreasurylist[0]["xcoins"], ycoins=var.choicetreasurylist[0]["ycoins"])
        elif selected_event == var.choicetreasurylist[1]['event']:
            result_creator(selected_event, xdmg=var.choicetreasurylist[1]["xdmg"], ydmg=var.choicetreasurylist[1]
                           ["ydmg"], xcoins=var.choicetreasurylist[1]["xcoins"], ycoins=var.choicetreasurylist[1]["ycoins"])
        elif selected_event == var.choicetreasurylist[2]['event']:
            result_creator(selected_event, xdmg=var.choicetreasurylist[2]["xdmg"], ydmg=var.choicetreasurylist[2]
                           ["ydmg"], xcoins=var.choicetreasurylist[2]["xcoins"], ycoins=var.choicetreasurylist[2]["ycoins"])
        elif selected_event == var.choicetreasurylist[3]['event']:
            result_creator(selected_event)
        elif selected_event == var.choicetreasurylist[4]['event']:
            result_creator(
                selected_event, xhlth=var.choicetreasurylist[4]['xhlth'], yhlth=var.choicetreasurylist[4]['yhlth'])
        elif selected_event == var.choicetreasurylist[5]['event']:
            result_creator(
                selected_event, xhlth=var.choicetreasurylist[5]['xhlth'], yhlth=var.choicetreasurylist[5]['yhlth'])

    if player_choice == var.choicelist[10]:
        selected_event = random.choices(
            var.choiceransomlist, weights=var.ransomweights, k=1)[0]
        selected_event = selected_event["event"]
        if selected_event == var.choiceransomlist[0]['event']:
            result_creator(selected_event, xdmg=var.choiceransomlist[0]["xdmg"], ydmg=var.choiceransomlist[0]
                           ["ydmg"], xcoins=var.choiceransomlist[0]["xcoins"], ycoins=var.choiceransomlist[0]["ycoins"])
        elif selected_event == var.choiceransomlist[1]['event']:
            result_creator(
                selected_event, xcoins=var.choiceransomlist[1]["xcoins"], ycoins=var.choiceransomlist[1]["ycoins"])
        elif selected_event == var.choiceransomlist[2]['event']:
            result_creator(
                selected_event, xcoins=var.choiceransomlist[2]["xcoins"], ycoins=var.choiceransomlist[2]["ycoins"])
        elif selected_event == var.choiceransomlist[3]['event']:
            result_creator(
                selected_event, xcoins=var.choiceransomlist[3]["xcoins"], ycoins=var.choiceransomlist[3]["ycoins"])
            var.player_defense -= 3
            var.raid_subdefense += 3
        elif selected_event == var.choiceransomlist[4]['event']:
            result_creator(selected_event)
        elif selected_event == var.choiceransomlist[5]['event']:
            result_creator(
                selected_event, xhlth=var.choiceransomlist[5]["xhlth"], yhlth=var.choiceransomlist[5]["yhlth"])
        elif selected_event == var.choiceransomlist[6]['event']:
            result_creator(
                selected_event, xhlth=var.choiceransomlist[6]["xhlth"], yhlth=var.choiceransomlist[6]["yhlth"])

  
    if player_choice == var.choicelist[11]:
        selected_event = random.choices(
            var.choicesabotagelist, weights=var.sabotageweights, k=1)[0]
        selected_event = selected_event["event"]
        if selected_event == var.choicesabotagelist[0]['event']:
            result_creator(selected_event, xdmg=var.choicesabotagelist[0]["xdmg"], ydmg=var.choicesabotagelist[0]
                           ["ydmg"], xcoins=var.choicesabotagelist[0]["xcoins"], ycoins=var.choicesabotagelist[0]["ycoins"])
        elif selected_event == var.choicesabotagelist[1]['event']:
            result_creator(
                selected_event, xdmg=var.choicesabotagelist[1]["xdmg"], ydmg=var.choicesabotagelist[1]["ydmg"], xcoins=var.choicesabotagelist[1]["xcoins"], ycoins=var.choicesabotagelist[1]["ycoins"])
        elif selected_event == var.choicesabotagelist[2]['event']:
            result_creator(
                selected_event, xcoins=var.choicesabotagelist[2]["xcoins"], ycoins=var.choicesabotagelist[2]["ycoins"])
        elif selected_event == var.choicesabotagelist[3]['event']:
            result_creator(
                selected_event, xhlth=var.choicesabotagelist[3]["xhlth"], yhlth=var.choicesabotagelist[3]["yhlth"])
        elif selected_event == var.choicesabotagelist[4]['event']:
            result_creator(
                selected_event, xhlth=var.choicesabotagelist[4]['xhlth'], yhlth=var.choicesabotagelist[4]['yhlth'])
        elif selected_event == var.choicesabotagelist[5]['event']:
            result_creator(
                selected_event, xdmg=var.choicesabotagelist[5]["xdmg"], ydmg=var.choicesabotagelist[5]["ydmg"], xcoins=var.choicesabotagelist[5]["xcoins"], ycoins=var.choicesabotagelist[5]["ycoins"])
        elif selected_event == var.choicesabotagelist[6]['event']:
            result_creator(
                selected_event, xcoins=var.choicesabotagelist[6]["xcoins"], ycoins=var.choicesabotagelist[6]["ycoins"])
        elif selected_event == var.choicesabotagelist[7]['event']:
            result_creator(
                selected_event, xhlth=var.choicesabotagelist[7]['xhlth'], yhlth=var.choicesabotagelist[7]['yhlth'])
        elif selected_event == var.choicesabotagelist[8]['event']:
            result_creator(
                selected_event, xhlth=var.choicesabotagelist[8]['xhlth'], yhlth=var.choicesabotagelist[8]['yhlth'])

    if player_choice == var.choicelist[12]:
        selected_event = random.choices(
            var.choicefirelist, weights=var.fireweights, k=1)[0]
        selected_event = selected_event["event"]
        if selected_event == var.choicefirelist[0]['event']:
            result_creator(selected_event, xdmg=var.choicefirelist[0]["xdmg"], ydmg=var.choicefirelist[0]
                           ["ydmg"], xcoins=var.choicefirelist[0]["xcoins"], ycoins=var.choicefirelist[0]["ycoins"])
        elif selected_event == var.choicefirelist[1]['event']:
            result_creator(selected_event, xdmg=var.choicefirelist[1]["xdmg"], ydmg=var.choicefirelist[1]
                           ["ydmg"], xcoins=var.choicefirelist[1]["xcoins"], ycoins=var.choicefirelist[1]["ycoins"])
        elif selected_event == var.choicefirelist[2]['event']:
            result_creator(
                selected_event, xdmg=var.choicefirelist[2]["xdmg"], ydmg=var.choicefirelist[2]["ydmg"])
        elif selected_event == var.choicefirelist[3]['event']:
            result_creator(selected_event, xdmg=var.choicefirelist[3]["xdmg"], ydmg=var.choicefirelist[3]
                           ["ydmg"], xcoins=var.choicefirelist[3]["xcoins"], ycoins=var.choicefirelist[3]["ycoins"])
        elif selected_event == var.choicefirelist[4]['event']:
            result_creator(selected_event)
        elif selected_event == var.choicefirelist[5]['event']:
            result_creator(
                selected_event, xhlth=var.choicefirelist[5]["xhlth"], yhlth=var.choicefirelist[5]["yhlth"])

    if player_choice == var.choicelist[13]:
        selected_event = random.choices(
            var.choicesneaklist, weights=var.sneakweights, k=1)[0]
        selected_event = selected_event["event"]
        if selected_event == var.choicesneaklist[0]['event']:
            result_creator(selected_event, xdmg=var.choicesneaklist[0]["xdmg"], ydmg=var.choicesneaklist[0]
                           ["ydmg"], xcoins=var.choicesneaklist[0]["xcoins"], ycoins=var.choicesneaklist[0]["ycoins"])
        elif selected_event == var.choicesneaklist[1]['event']:
            result_creator(
                selected_event, xdmg=var.choicesneaklist[1]["xdmg"], ydmg=var.choicesneaklist[1]["ydmg"], xcoins=var.choicesneaklist[1]["xcoins"], ycoins=var.choicesneaklist[1]["ycoins"])
        elif selected_event == var.choicesneaklist[2]['event']:
            result_creator(
                selected_event, xcoins=var.choicesneaklist[2]["xcoins"], ycoins=var.choicesneaklist[2]["ycoins"])
        elif selected_event == var.choicesneaklist[3]['event']:
            result_creator(
                selected_event, xcoins=var.choicesneaklist[3]["xcoins"], ycoins=var.choicesneaklist[3]["ycoins"])
        elif selected_event == var.choicesneaklist[4]['event']:
            result_creator(
                selected_event, xhlth=var.choicesneaklist[4]["xhlth"], yhlth=var.choicesneaklist[4]["yhlth"])
        elif selected_event == var.choicesneaklist[5]['event']:
            result_creator(
                selected_event, xhlth=var.choicesneaklist[5]["xhlth"], yhlth=var.choicesneaklist[5]["yhlth"])

    if player_choice == var.choicelist[14]:
        selected_event = random.choices(
            var.choiceswimlist, weights=var.swimweights, k=1)[0]
        selected_event = selected_event["event"]
        if selected_event == var.choiceswimlist[0]['event']:
            result_creator(
                selected_event, xcoins=var.choiceswimlist[0]["xcoins"], ycoins=var.choiceswimlist[0]["ycoins"])
        elif selected_event == var.choiceswimlist[1]['event']:
            result_creator(
                selected_event, xcoins=var.choiceswimlist[1]["xcoins"], ycoins=var.choiceswimlist[1]["ycoins"])
        elif selected_event == var.choiceswimlist[2]['event']:
            result_creator(
                selected_event, xcoins=var.choiceswimlist[2]["xcoins"], ycoins=var.choiceswimlist[2]["ycoins"])
        elif selected_event == var.choiceswimlist[3]['event']:
            result_creator(selected_event)
        elif selected_event == var.choiceswimlist[4]['event']:
            result_creator(
                selected_event, xhlth=var.choiceswimlist[4]["xhlth"], yhlth=var.choiceswimlist[4]["yhlth"])

    time.sleep(2.5)
    if var.double_damage == True:
        var.round += 1
        if var.round == 2:
          var.player_attack /= 2
          var.double_damage = False
          var.player_attack = round(var.player_attack)

    if var.halftimesdamage == True:
        var.round2 += 1
        if var.round2 == 2:
          var.player_attack /= 1.5
          var.halftimesdamage = False
          var.player_attack = round(var.player_attack)


    if var.village_health <= 0:
        var.village_health = 0
    if var.player_health <= 0:
        var.player_health = 0
    print('       🛖  Village health: ' + str(var.village_health) +
          '\n' + '       ❤️  Your health: ' + str(var.player_health))
    time.sleep(1)
    battle(player_weapon)


def result_creator(selected_event, xdmg=None, ydmg=None, xcoins=None, ycoins=None, xhlth=None, yhlth=None):

    # This is where the good stuff happens. It changes the values of the player depending on what response the game picked. It also changes the responses with the updated values that it picked
    if '**' in selected_event:
        random_attack = random.randrange(xdmg, ydmg)
        attack = int((var.player_attack * 80 / 100) +
                     (random_attack * 80 / 100))
        var.village_health -= attack
        selected_event = selected_event.replace(
            "**", Fore.MAGENTA + str(attack) + Fore.RESET)
    if '++' in selected_event:
        random_coins = random.randrange(xcoins, ycoins)
        if var.coindoubler == True:
            random_coins *= 2
        var.raid_coins += random_coins
        random_coins = random_coins + int(var.player_coins * 1 / 100)
        var.player_coins += random_coins
        selected_event = selected_event.replace(
            "++", Fore.LIGHTYELLOW_EX + str(random_coins) + Fore.RESET)

    if '--' in selected_event:
        random_damage = random.randrange(xhlth, yhlth)
        health = random_damage

        health = int(health + (var.player_health * 10 / 100))
        health = int(health - (var.player_defense * 40 / 100))

        selected_event = selected_event.replace(
            "--", Fore.RED + str(health) + Fore.RESET)
        var.player_health -= health


    if '@@' in selected_event:
      coinloss = random.randrange(50, 100)
      selected_event = selected_event.replace('@@', str(coinloss))
      var.player_coins = int(var.player_coins - int(coinloss))
    print(selected_event)