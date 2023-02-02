import csv


state = ''

name = ''
loginDate = ''

tutorial = True

player_health = 115
player_defense = 5
player_attack = 5
player_coins = 0

max_health = 115


raid_attack = 0
raid_defense = 0
raid_coins = 0
double_damage = False
halftimesdamage = False

village_health = None

lifesaver = False
coindoubler = False

generated_Data = []


admins = ['nischay', 'george', 'logan',
          'mr. daab', 'mrdaab', 'mr daab', 'charles']

weaponlist = ['katana', 'ak47', 'sword', 'knife', 'grenade', 'stick', 'baseball bat', 'shotgun', 'atomic bomb', 'bow and arrow', 'spear', 'electric rifle', 'pistol', 'water gun', 'shuriken',
              'nunchucks', 'poison bottle', 'rocket launcher' 'machine gun', 'dynamite', 'bomb', 'dagger', 'revolver', 'targeted missiles', 'hand cannon', 'hamer', 'boomerang', 'javelin', 'plasma gun']

choicelist = [
    ' a house',
    'Attack a fort',
    'Break into mansion',
    'Disable defenses',
    'Hide in the well',
    'Infiltrate a library',
    'Loot the marketplace',
    'Raid a farm',
    'Raid a house',
    'Raid the treasury',
    'Ransom villagers',
    'Sabotoge a mine',
    'Set a house on fire',
    'Sneak into town hall',
    'Swim in the pool'
]


choicecopylist = [
    ' a house',
    'Attack a fort',
    'Break into mansion',
    'Disable defenses',
    'Hide in the well',
    'Infiltrate a library',
    'Loot the marketplace',
    'Raid a farm',
    'Raid a house',
    'Raid the treasury',
    'Ransom villagers',
    'Sabotoge a mine',
    'Set a house on fire',
    'Sneak into town hall',
    'Swim in the pool'
]


choicehouselist = [
    {"event": "You successfully dealt ** damage to the house with your weapon.",
        "weight": .5, "xdmg": 21, "ydmg": 39},
    {"event": "You completely destroyed the house and dealt ** damage.",
        "weight": .5, "xdmg": 19, "ydmg": 35}
]

houseweights = [event["weight"] for event in choicehouselist]

choiceraidlist = [
    {"event": "You succesfully raided the house and dealt ** damage to the village.",
        "weight": 0.27, "xdmg": 20, "ydmg": 35},
    {"event": "You destroyed the house dealing ** damage and gained ++ coins",
        "weight": 0.27, "xdmg": 20, "ydmg": 35, "xcoins": 30, "ycoins": 60},
    {"event": "You found ++ coins in the raid",
        "weight": 0.3, "xcoins": 50, "ycoins": 80},
    {"event": "You got shot by the home owner and took -- damage",
        "weight": 0.08, "xhlth": 20, "yhlth": 35},
    {"event": "The home owner chased you and you tried to jump out of the window and took -- damage.",
        "weight": 0.08, "xhlth": 8, "yhlth": 20}
]

raidweights = [event["weight"] for event in choiceraidlist]

choicefirelist = [
    {"event": "You set a house on fire and cause ** damage. You gained ++ coins.",
     "weight": 0.25, "xdmg": 10, "ydmg": 30, "xcoins": 15, "ycoins": 40, },
    {"event": "The house burns to the ground, causing ** damage to the village. You gained ++ coins",
        "weight": 0.25, "xdmg": 20, "ydmg": 37, "xcoins": 30, "ycoins": 60},
    {"event": "The villagers put out the fire only dealing ** damage. You gained no coins.",
        "weight": 0.15, "xdmg": 5, "ydmg": 15},
    {"event": "You actually ended up setting several houses on fire and dealt ** damage! And you gained a whopping ++ coins!",
        "weight": 0.15, "xdmg": 30, "ydmg": 45, "xcoins": 80, "ycoins": 120},
    {"event": "The wind blew out the fire and didn't deal any damage. What a waste of time.", "weight": 0.1, },
    {"event": "You messed up while lighting the fire and actually burned yoruself. You took -- damage.",
        "weight": 0.1, "xhlth": 15, "yhlth": 25},
]

fireweights = [event["weight"] for event in choicefirelist]

choicemansionlist = [
    {"event": "You caused massive damage to the items in the mansion and dealt ** damage. Unfortunately you didn't think of stealing the items and didn't obtain any coins.",
        "weight": 0.14, "xdmg": 30, "ydmg": 50},
    {"event": "The mansions guards put up a fight but you were able to overpower them and deal ** damage. You also gained ++ coins",
        "weight": 0.2, "xdmg": 20, "ydmg": 30, "xcoins": 30, "ycoins": 58},
    {"event": "You carefully infiltrated the mansion and stole valuable artwork and jewelry. Your stealthy tactics caused no damage but you gained ++ coins.",
        "weight": 0.19, "xcoins": 60, "ycoins": 76},
    {"event": "The mansion's security was no match for your skills. You successfully stole valuable antiques and gained a bonus to your defense. You caused no damage but gained ++ coins.",
        "weight": 0.12, "xcoins": 30, "ycoins": 43},
    {"event": "The mansion was empty but you caused some damage. You caused ** damage.",
        "weight": 0.14, "xdmg": 15, "ydmg": 25},
    {"event": "The mansion was heavily guarded and you were caught. You took -- damage and gained no coins.",
        "weight": 0.12, "xhlth": 30, "yhlth": 45},
    {"event": "The mansion had many security cameras and they alerted the police. You managed to escape but took -- damage. ",
        "weight": 0.09, "xhlth": 20, "yhlth": 30},
]

mansionweights = [event["weight"] for event in choicemansionlist]

choiceswimlist = [
    {"event": "You take a swim and enjoy the cool water. You gain ++ coins but cause 0 damage.",
        "weight": 0.3, "xcoins": 29, "ycoins": 40},
    {"event": "You take a dive in the water and found a fortue worth of coins at the bottom. You gained ++ coins but didn't do any damage",
        "weight": 0.15, "xcoins": 100, "ycoins": 200},
    {"event": "You splash around in the pool, enjoying the luxurious surroundings. You gain ++ coins and cause no damage.",
        "weight": 0.2, "xcoins": 15, "ycoins": 25},
    {"event": "The pool is empty and you gain no coins and cause 0 damage.", "weight": 0.2},
    {"event": "The villagers were having a pool party and chased you down. You took -- damage.",
        "weight": 0.15, "xhlth": 16, "yhlth": 28},
]

swimweights = [event["weight"] for event in choiceswimlist]

choicetreasurylist = [
    {"event": "The raid on the treasury was a complete success! You caused ** damage and gained ++ coins",
        "weight": 0.25, "xdmg": 8, "ydmg": 20, "xcoins": 50, "ycoins": 69},
    {"event": "The guards put up a fight but you were able to steal ++ coins and cause ** damage.",
        "weight": 0.25, "xdmg": 15, "ydmg": 25, "xcoins": 45, "ycoins": 60},
    {"event": "You successfully raided the treasury and gained a stash of coins. You caused ** damage and gained ++ coins.",
        "weight": 0.3, "xdmg": 20, "ydmg": 30, "xcoins": 80, "ycoins": 140},
    {"event": "The treasury was empty, causing 0 damage and gaining no coins", "weight": 0.1},
    {"event": "You couldn't pick the lock to the treasury and gained no coins. You took -- damage.",
        "weight": 0.1, "xhlth": 17, "yhlth": 30},
    {"event": "The guards swarmed you while you were in the treasury and you took -- damage. You caused ** damage but gained no coins.",
        "weight": 0.1, "xhlth": 10, "yhlth": 17}
]

treasuryweights = [event["weight"] for event in choicetreasurylist]

choicefortlist = [
    {"event": "You successfully attacked the fort and caused ** damage. You gained ++ coins.",
        "weight": 0.23, "xdmg": 22, "ydmg": 30, "xcoins": 30, "ycoins": 39},
    {"event": "You completely overrun the fort and caused ** damage. You also managed to gain a total of ++ coins!",
        "weight": 0.25, "xdmg": 30, "ydmg": 47, "xcoins": 40, "ycoins": 69},
    {"event": "The fort's defenses were strong, but you were able to cause ** damage and gain ++ coins.",
        "weight": 0.25, "xdmg": 15, "ydmg": 25, "xcoins": 15, "ycoins": 27},
    {"event": "The fort's defenses were too strong and you were only able to cause ** damage. You gained no coins.",
        "weight": 0.18, "xdmg": 5, "ydmg": 15},
    {"event": "The fort's defenders fought back fiercly causing you to take -- damage.",
        "weight": 0.1, "xhlth": 20, "yhlth": 35}
]

fortweights = [event["weight"] for event in choicefortlist]

choiceransomlist = [
    {"event": "You successfullly ransomed the hostages and gained a large sum of ++ coins. You also dealt ** damage to the village.",
        "weight": 0.17, "xdmg": 20, "ydmg": 30, "xcoins": 50, "ycoins": 80},
    {"event": "The villagers paid a hefty ransom for the safe return of their loved ones. You gained a lot of coins from the negotiation. + ++ coins.",
        "weight": 0.23, "xcoins": 70, "ycoins": 100},
    {"event": "The hostages were important figures in the village and their release came at a high price. You gained a significant amount of coins from the ransom. + ++ coins.",
        "weight": 0.22, "xcoins": 80, "ycoins": 120},
    {"event": "You capture some of the villagers and demand a ransom for their release. You gain ++ coins but loose some defense.",
        "weight": 0.17, "xcoins": 60, "ycoins": 80},
    {"event": "The hostages were not wealthy and the village refused to pay for the ransom. You gained no coins from the negotiation.", "weight": 0.1},
    {"event": "The hostages organized a counter-attack and made you take -- damage. You gained no coins.",
        "weight": 0.08, "xhlth": 20, "yhlth": 40},
    {"event": "The hostages turned out to be special trained forces of the army and managed to take you hostage instead. You paid @@ coins for your own release and took -- damage. Talk about being dumb.", "weight": 0.08, "xhlth": 20, "yhlth": 40}
]

ransomweights = [event["weight"] for event in choiceransomlist]

choicesneaklist = [
    {"event": "You manage to sneak into the town hall and steal valuable treasures. You caused ** damage and gained ++ coins.",
        "weight": 0.23, "xdmg": 10, "ydmg": 15, "xcoins": 50, "ycoins": 100},
    {"event": "The town hall's guards put up a fight, but you were able to steal ++ coins and deal ** damage.",
        "weight": 0.21, "xdmg": 5, "ydmg": 10, "xcoins": 75, "ycoins": 125},
    {"event": "You successfully infiltrate the town hall and retrieve important documents, gaining ++ coins.",
        "weight": 0.21, "xcoins": 50, "ycoins": 100},
    {"event": "You were able to sneak into the town hall undetected and grab valuable artifacts, earning ++ coins.",
        "weight": 0.14, "xcoins": 60, "ycoins": 90},
    {"event": "You were caught by the guards while trying to sneak into the town hall, taking -- damage.",
        "weight": 0.1, "xhlth": 10, "yhlth": 30},
    {"event": "You were caught by the guards and had to fight your way out of the town hall, taking -- damage and losing coins.",
        "weight": 0.11, "xhlth": 5, "yhlth": 20}
]

sneakweights = [event["weight"] for event in choicesneaklist]

choicefarmlist = [
    {"event": "You successfully raid the farm, stealing valuable livestock, doing ** damage, and earning ++ coins.",
        "weight": 0.15, "xdmg": 22, "ydmg": 37, "xcoins": 30, "ycoins": 45},
    {"event": "You raid the farm and find a hidden stash of coins, gaining a total of ++ coins.",
        "weight": 0.18, "xcoins": 100, "ycoins": 150},
    {"event": "You set fire to the farm as you raid, causing ** hitpoints of widespread damage and gaining ++ coins.",
        "weight": 0.12, "xdmg": 20, "ydmg": 30, "xcoins": 30, "ycoins": 60},
    {"event": "The farm owner put up a fight, but you were able to steal ++ coins and deal ** damage.",
        "weight": 0.11, "xdmg": 5, "ydmg": 10, "xcoins": 50, "ycoins": 75},
    {"event": "The farm owner was able to call for backup and you had to flee the scene, taking -- damage.",
        "weight": 0.1, "xhlth": 19, "yhlth": 30},
    {"event": "You were caught by the farmers while trying to raid the farm, taking -- damage.",
        "weight": 0.09, "xhlth": 5, "yhlth": 20},
    {"event": "You raid the farm but find nothing of value and leave empty handed", "weight": 0.12},
    {"event": "The farm owner was able to call for backup and you had to flee the scene, losing coins.", "weight": 0.1},
]

farmweights = [event["weight"] for event in choicefarmlist]

choicemarketlist = [
    {"event": "You successfully loot the marketplace, dealing ** damage and earning ++ coins worth of stolen goods.",
        "weight": 0.26, "xdmg": 30, "ydmg": 50, "xcoins": 50, "ycoins": 80},
    {"event": "You rob the cash register and steal ++ coins from inside and deal ** damage to the market.",
        "weight": 0.28, "xdmg": 25, "ydmg": 41, "xcoins": 100, "ycoins": 150},
    {"event": "As you loot the marketplace, a guard spots you and deals -- damage before you can escape.",
        "weight": 0.1, "xhlth": 5, "yhlth": 20},
    {"event": "You try to loot the marketplace but are unsuccessful and end up getting injured. You take -- damage.",
        "weight": 0.1, "xhlth": 5, "yhlth": 10},
    {"event": "You tried to knock out the marketeer but he blocks your punch and acutally knocks you out. You took -- damage. Talk about karma.",
        "weight": 0.1, "xhlth": 28, "yhlth": 40},
    {"event": "You attempt to loot the marketplace but find nothing of value and leave empty handed.", "weight": 0.15}
]
marketweights = [event["weight"] for event in choicemarketlist]


choicelibrarylist = [
    {"event": "You successfully infiltrate the library and find a valuable book gaining useful information. You learned the art of attack and now your attack is significantly higher for the rest of the battle.", "weight": 0.2},
    {"event": "You sneak into the library and steal important books, earning ++ coins.",
        "weight": 0.2, "xcoins": 75, "ycoins": 125},
    {"event": "As you infiltrate the library, a guard spots you and you are forced to flee empty handed.", "weight": 0.16},
    {"event": "You try to infiltrate the library but are caught and thrown in jail, taking -- damage.",
        "weight": 0.13, "xhlth": 25, "yhlth": 50},
    {"event": "You attempt to infiltrate the library but trip an alarm and have to fight off security, taking -- damage.",
        "weight": 0.1, "xhlth": 12, "yhlth": 30},
    {"event": "You successfully sneak into the library undetected and find a rare, antique book that brings in ++ coins when sold",
        "weight": 0.12, "xcoins": 50, "ycoins": 87},
    {"event": "While exploring the library, you stumble upon a secret room containing valuable artifacts and ++ coins.",
        "weight": 0.12, "xcoins": 30, "ycoins": 100}
]
libraryweights = [event["weight"] for event in choicelibrarylist]

choicehidelist = [
    {"event": "You found a hidden stash of ++ coins in the well.",
     "weight": 0.1, "xcoins": 50, "ycoins": 80},
    {"event": "You hide in the well successfully, but took -- damage from the sharp edges.",
     "weight": 0.1, "xhlth": 5, "yhlth": 15},
    {"event": "You stumbled upon a group of bandits and quickly hide in the well. You dealt ** damage to them when they got too close.",
     "weight": 0.21, "xdmg": 20, "ydmg": 35},
    {"event": "You successfully evaded a dangerous situation by hiding in the well. You dealt ** damage and gained ++ coins.",
     "weight": 0.23, "xdmg": 20, "ydmg": 35, "xcoins": 30, "ycoins": 50},
    {"event": "You found a secret passage while hiding in the well and gained ++ coins.",
     "weight": 0.1, "xcoins": 30, "ycoins": 60},
    {"event": "You were able to catch your breath and heal yourself while hiding in the well.",
     "weight": 0.12},
    {"event": "The well was filled with toxic gas and you took -- damage.",
     "weight": 0.07, "xhlth": 10, "yhlth": 30},
    {"event": "You were ambushed by enemies while hiding in the well and took -- damage.",
     "weight": 0.07, "xhlth": 8, "yhlth": 20}
]

hideweights = [event["weight"] for event in choicehidelist]

choicedisablelist = [
    {"event": "You successfully disabled the defenses, dealing ** damage to the enemy.",
        "weight": 0.15, "xdmg": 30, "ydmg": 40},
    {"event": "You disabled the defenses and found ++ coins in the process. Your next attack will do 2x damage.",
     "weight": 0.13, "xcoins": 40, "ycoins": 60},
    {"event": "The defenses were weakened and you easily took them down, dealing ** damage and gaining ++ coins!",
     "weight": 0.12, "xdmg": 35, "ydmg": 50, "xcoins": 50, "ycoins": 60},
    {"event": "You took advantage of the weakened defenses and gained ++ coins. Your next attack will do 1.5x damage",
     "weight": 0.13, "xcoins": 50, "ycoins": 75},
    {"event": "The defenses were easy to take down and you made a quick getaway with ++ coins. You gain +5 attack for the rest of the battle.",
     "weight": 0.13, "xcoins": 60, "ycoins": 90},
    {"event": "You used your cunning tactics and disabled the defenses, gaining ++ coins.",
        "weight": 0.1, "xcoins": 70, "ycoins": 100},
    {"event": "You encountered resistance while disabling the defenses and took -- damage.",
        "weight": 0.08, "xhlth": 20, "yhlth": 30},
    {"event": "The defenses were too strong and you took a significant amount of -- damage.",
        "weight": 0.08, "xhlth": 10, "yhlth": 20},
    {"event": "You encountered a booby trap while you were disabling the defenses and took -- damage",
        "weight": 0.08, "xhlth": 15, "yhlth": 27}
]

disableweights = [event["weight"] for event in choicedisablelist]

choicesabotagelist = [
    {"event": "You successfully sabotaged the mine and dealt ** damage to the enemy's operations. You looted a total of ++ coins.",
        "weight": 0.15, "xdmg": 20, "ydmg": 35, "xcoins": 60, "ycoins": 140},
    {"event": "You planted a bomb and dealt ** damage to the mine and gained ++ coins",
        "weight": 0.12, "xdmg": 20, "ydmg": 35, "xcoins": 50, "ycoins": 90},
    {"event": "You snuck into the mine and completely raided the goblins of their treasure! You gained a whole ++ coins!!",
        "weight": 0.13, "xcoins": 130, "ycoins": 200},
    {"event": "The goblins heard you enter the mine and fought you. You took -- damage.",
        "weight": 0.1, "xhlth": 20, "yhlth": 31},
    {"event": "You attempted to sabotage the mine but failed and took -- damage",
        "weight": 0.1, "xhlth": 8, "yhlth": 20},
    {"event": "You caused a cave-in and dealt ** damage to the mine and gained ++ coins",
        "weight": 0.15, "xdmg": 31, "ydmg": 37, "xcoins": 60, "ycoins": 80},
    {"event": "You found DIAMONDS in the mine and traded them for ++ coins!!!",
        "weight": 0.1, "xcoins": 130, "ycoins": 220},
    {"event": "You were caught by the goblins and beat to the ground losing -- health",
        "weight": 0.07, "xhlth": 30, "yhlth": 50},
    {"event": "You were injured while planting a bomb and took -- damage",
        "weight": 0.08, "xhlth": 10, "yhlth": 20}
]

sabotageweights = [event["weight"] for event in choicesabotagelist]


def read_Data(file_Name):

    data_List = []

    # Opens the file and stores it as a variable file
    with open(file_Name, mode='r') as file:
        # Read file
        csvFile = csv.reader(file)

        # Show contents of file
        for lines in csvFile:
            data_List.append(lines)
    return data_List


def save_data(player_name=None, player_attack=None, player_defense=None, player_health=None, player_coins=None, loginDate=None):
    # Read data from csv file into a list
    data_list = read_Data('database.csv')

    # Iterate through the list and update values for the specified player
    for i in range(len(data_list)):
        if data_list[i][0] == player_name:
            if player_attack != None:
                data_list[i][1] = player_attack
            if player_defense != None:
                data_list[i][2] = player_defense
            if player_health != None:
                data_list[i][3] = player_health
            if player_coins != None:
                data_list[i][4] = player_coins
            if loginDate != None:
                data_list[i][5] = loginDate

    # Write the updated data back to the csv file
    with open('database.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data_list)


RESET = '\u001b[0m'


CLEAR_LINE = '\u001b[2K'
CLEAR_SCREEN = '\u001b[2J'

UP = '\u001b[1A'
Down = '\u001b[1B'
Right = '\u001b[1C'
Left = '\u001b[2D'

DEL = '<none>'