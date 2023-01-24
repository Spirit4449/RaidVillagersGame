import time
import random
from numpy.random import choice
import var


def battle_start(tutorial):

    var.village_health = random.randrange(70, 130)

    print('The battle has started! This village has ' +
          str(var.village_health) + ' health')
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
    time.sleep(1.5)

    print('\n  ' + weapon1 + '        ' +
          weapon2 + '        ' + weapon3 + '\n')
    time.sleep(1.2)

    global player_weapon

    player_weapon = input('Your weapon: ')
    while player_weapon.lower() not in var.weaponlist:

        print('That is not an option')
        time.sleep(0.5)
        player_weapon = input('Your weapon: ')

    if player_weapon == 'nuclear bomb':
        print('You choose such an overpowered weapon that you automatically won the game!')
        win = True
    elif player_weapon == 'machine gun':
        print('Good choice. Your attack is now +10')
        var.player_attack += 10
    elif player_weapon == 'water gun':
        print('Your weapon wasn\'t enough to take down a village. You automatically lost.')
        loose = True
    elif player_weapon == 'stick':
        print('Bro what were you thinking. Your stick broke during battle. Now you have no weapon attack bonous.')
    else:
        print('Good Choice. Your weapon gave you +5 attack bonous.')
        var.player_attack += 5

    time.sleep(2)
    battle(player_weapon)


def battle(player_weapon):
    choice1 = random.choice(var.choicelist)
    var.choicelist.remove(choice1)
    choice2 = random.choice(var.choicelist)
    var.choicelist.remove(choice2)
    choice3 = random.choice(var.choicelist)
    var.choicelist.remove(choice3)

    var.choicelist.append(choice1)
    var.choicelist.append(choice2)
    var.choicelist.append(choice3)

    if choice1 == ' a house':
        choice1 = player_weapon + choice1
    elif choice2 == ' a house':
        choice2 = player_weapon + choice2
    elif choice3 == ' a house':
        choice3 = player_weapon + choice2

    # if tutorial == True:
    #     print('\nNow we will begin the raid. Below you will be asked to choose an option. Type the option you want to choose...\n')
    #     time.sleep(6)

    print('\nChoose an option from the following:\n' + 'a) ' +
          choice1 + '\n' + 'b) ' + choice2 + '\n' + 'c) ' + choice3 + '\n')
    time.sleep(1)

    while True:
        player_choice = input('Choose an option: ')
        if player_choice.lower() == choice1.lower() or player_choice.lower() == choice2.lower() or player_choice.lower() == choice3.lower():
            player_choice.capitalize()
            break
        else:
            print('That is not an option!')
            time.sleep(0.5)

    battle_result(player_choice)


def battle_result(player_choice):
    if player_choice == var.choicelist[0]:
        result = choice(var.choiceraidlist, size=1,
                        p=[0.4, 0.3, 0.18, 0.09, 0.03])
        print(result)
        if result == var.choiceraidlist[0]:
            var.village_health -= (var.player_attack + 10)
            var.choice1list[0].replace("__", var.player_attack+10)
            print(var.choicelist[0])

    battle(player_weapon)
