import time
import random
import var
import math

def battle_start(tutorial=None):

    var.village_health = random.randrange(70, 130)

    print('The battle has started! This village has ' +
          str(var.village_health) + ' health')
    #time.sleep(2.5)

    if tutorial == True:
        print('Now you will choose your weapon. Type the name of the weapon you would like to choose.')
        #time.sleep(3)

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
    #time.sleep(1.5)

    print('\n  ' + weapon1 + '        ' +
          weapon2 + '        ' + weapon3 + '\n')
    #time.sleep(1.2)

    global player_weapon

    player_weapon = input('Your weapon: ')
    while player_weapon.lower() not in var.weaponlist:

        print('That is not an option')
        time.sleep(0.5)
        player_weapon = input('Your weapon: ')

    if player_weapon == 'nuclear bomb':
        print('You choose such an overpowered weapon that you automatically won the game!')
        var.win = True
    elif player_weapon == 'machine gun':
        print('Good choice. Your weapon gave you +10 attack bonous')
        var.player_attack += 10
    elif player_weapon == 'water gun':
        print('Your weapon wasn\'t enough to take down a village. You automatically lost.')
        var.loose = True
    elif player_weapon == 'stick':
        print('Bro what were you thinking. Your stick broke during battle. Now you have no weapon attack bonous.')
    else:
        print('Good Choice. Your weapon gave you +5 attack bonous.')
        var.player_attack += 5
    print(var.player_attack)

    if var.win == True:
        time.sleep(2)
        exit()
    elif var.loose == True:
        time.sleep(2)
        exit()

    #time.sleep(2)
    battle(player_weapon)


def battle(player_weapon):

    if var.village_health <= 0:
        print('Congratulations, you have successfully destroyed the village! You gained a total of ' + str(var.raid_coins) + ' coins!')
        var.player_coins += var.raid_coins
        var.raid_coins = 0
        return None
    if var.player_health <= 0:
        print('Oh no! You have been killed in the raid! You lost the coins you gained in the raid.')
        var.raid_coins = 0
        return None


    choice1 = var.choicelist[8]
    var.choicelist.remove(choice1)
    choice2 = random.choice(var.choicelist)
    var.choicelist.remove(choice2)
    choice3 = random.choice(var.choicelist)
    var.choicelist.remove(choice3)

    var.choicelist.append(choice1)
    var.choicelist.append(choice2)
    var.choicelist.append(choice3)
    var.choicelist.sort()

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
            player_choice = player_choice.capitalize()
            break
        else:
            print('That is not an option!')
            time.sleep(0.5)

    battle_result(player_choice)


def battle_result(player_choice):
    if player_choice == var.choicelist[8]:
        selected_event = random.choices(var.choiceraidlist, weights=var.raidweights, k=1)[0]
        selected_event = selected_event["event"]

        if selected_event == var.choiceraidlist[0]['event']:
            result_creator(selected_event, xdmg=var.choiceraidlist[0]["xdmg"], ydmg=var.choiceraidlist[0]["ydmg"])
        elif selected_event == var.choiceraidlist[1]['event']:
            result_creator(selected_event, xdmg=10, ydmg=20, xcoins=25, ycoins=50)
        elif selected_event == var.choiceraidlist[2]['event']:
            result_creator(selected_event, xcoins=40, ycoins=69)
        elif selected_event == var.choiceraidlist[3]['event']:
            result_creator(selected_event, xhlth=10, yhlth=20)
        else:
            print('Unlucky bro')
    battle(player_weapon)


def result_creator(selected_event, xdmg=None, ydmg=None, xcoins=None, ycoins=None, xhlth=None, yhlth=None):

    if '**' in selected_event:
        random_attack = random.randrange(xdmg, ydmg)
        attack = var.player_attack + random_attack
        var.village_health -= attack
        selected_event = selected_event.replace("**", str(attack))
    if '++' in selected_event:
        random_coins = random.randrange(xcoins, ycoins)
        selected_event = selected_event.replace("++", str(random_coins))
        var.raid_coins += random_coins
    if '--' in selected_event:
        random_damage = random.randrange(xhlth, yhlth)
        selected_event = selected_event.replace("--", str(random_damage))
        var.player_health = var.player_health - random_damage + math.ceil(var.player_defense * 75 / 100)

    print(selected_event)
    

