state = ''

name = ''

tutorial = True

player_health = 100
player_defense = 4
player_attack = 4
player_coins = 0

max_health = 100

raid_coins = 0

village_health = None

lifesaver = False

generated_Data = []

weaponlist = ['katana', 'ak47', 'sword', 'knife', 'grenade', 'stick', 'baseball bat', 'shotgun', 'nuclear bomb',
              'bow and arrow', 'spear', 'electric rifle', 'pistol', 'water gun', 'shuriken', 'nunchucks', 'paper airplane', 'machine gun']

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
  'Sabotoge a mine', 
  'Set a house on fire', 
  'Sneak into town hall',
  'Swim in the pool'
]

choiceraidlist = [
    {"event": "You succesfully raided the house and dealt ** damage to the village.", "weight": 0.27, "xdmg": 20, "ydmg": 35},
    {"event": "You destroyed the house dealing ** damage and gained ++ coins", "weight": 0.23, "xdmg": 20, "ydmg": 35, "xcoins": 30, "ycoins": 60},
    {"event": "You found ++ coins in the raid", "weight": 0.3, "xcoins": 50, "ycoins": 80},
    {"event": "You got shot by the home owner and took -- damage", "weight": 0.08, "xhlth": 20, "yhlth": 35},
    {"event": "The home owner chased you and you tried to jump out of the window and took -- damage.", "weight": 0.12, "xhlth": 8, "yhlth": 20}
]

raidweights = [event["weight"] for event in choiceraidlist]

choicefirelist = [
    {"event": "You set a house on fire and cause ** damage. You gained ++ coins.", 
     "weight": 0.25, "xdmg": 10, "ydmg": 30, "xcoins": 15, "ycoins": 40,},
    {"event": "The house burns to the ground, causing ** damage to the village. You gained ++ coins", "weight": 0.22, "xdmg": 20, "ydmg": 37, "xcoins": 30, "ycoins": 60},
    {"event": "The villagers put out the fire only dealing ** damage. You gained no coins.", "weight": 0.14, "xdmg": 5, "ydmg": 15},
    {"event": "You actually ended up setting several houses on fire and dealt ** damage! And you gained a whopping ++ coins!", "weight": 0.14, "xdmg": 30, "ydmg": 45, "xcoins": 80, "ycoins": 120},
    {"event": "The wind blew out the fire and didn't deal any damage. What a waste of time.", "weight": 0.1,},
    {"event": "You messed up while lighting the fire and actually burned yoruself. You took -- damage.", "weight": 0.15, "xhlth": 15, "xhlth": 25},
]

fireweights = [event["weight"] for event in choicefirelist]

choicemansionlist = [
    {"event": "You caused massive damage to the items in the mansion and dealt ** damage. Unfortunately you didn't think of stealing the items and didn't obtain any coins.", "weight": 0.14, "xdmg": 30, "ydmg": 50},
    {"event": "The mansions guards put up a fight but you were able to overpower them and deal ** damage. You also gained ++ coins", "weight": 0.2, "xdmg": 20, "ydmg": 30, "xcoins": 30, "ycoins": 58},
    {"event": "You carefully infiltrated the mansion and stole valuable artwork and jewelry. Your stealthy tactics caused no damage but you gained ++ coins.", "weight": 0.19, "xcoins": 60, "ycoins": 76},
    {"event": "The mansion's security was no match for your skills. You successfully stole valuable antiques and gained a bonus to your defense. You caused no damage but gained ++ coins.", "weight": 0.12, "xcoins": 30, "ycoins": 43},
    {"event": "The mansion was empty but you caused some damage. You caused ** damage.", "weight": 0.11, "xdmg": 15, "ydmg": 25},
    {"event": "The mansion was heavily guarded and you were caught. You took -- damage and gained no coins.", "weight": 0.12, "xhlth": 30, "yhlth": 45},
    {"event": "The mansion had many security cameras and they alerted the police. You managed to escape but took -- damage. ", "weight": 0.12, "xhlth": 20, "yhlth": 30},
]

mansionweights = [event["weight"] for event in choicemansionlist]

choiceswimlist = [
    {"event": "You take a swim and enjoy the cool water. You gain ++ coins but cause 0 damage.", "weight": 0.3, "xcoins": 29, "ycoins": 40},
    {"event": "You take a dive in the water and found a fortue worth of coins at the bottom. You gained ++ coins but didn't do any damage", "weight": 0.1, "xcoins": 100, "ycoins": 200},
    {"event": "You splash around in the pool, enjoying the luxurious surroundings. You gain ++ coins and cause no damage.", "weight": 0.2, "xcoins": 15, "ycoins": 25},
    {"event": "The pool is empty and you gain no coins and cause 0 damage.", "weight": 0.2},
    {"event": "The villagers were having a pool party and chased you down. You took -- damage.", "weight": 0.2, "xhlth": 16, "yhlth": 28},
]

swimweights = [event["weight"] for event in choiceswimlist]

choicetreasurylist = [
    {"event": "The raid on the treasury was a complete success! You caused ** damage and gained ++ coins", "weight": 0.25, "xdmg": 8, "ydmg": 20, "xcoins": 50, "ycoins": 69},
    {"event": "The guards put up a fight but you were able to steal ++ coins and cause ** damage.", "weight": 0.25, "xdmg": 15, "ydmg": 25, "xcoins": 45, "ycoins": 60},
    {"event": "You successfully raided the treasury and gained a stash of coins. You caused ** damage and gained ++ coins.", "weight": 0.3, "xdmg": 20, "ydmg": 30, "xcoins": 80, "ycoins": 140},
    {"event": "The treasury was empty, causing 0 damage and gaining no coins", "weight": 0.1},
    {"event": "You couldn't pick the lock to the treasury and gained no coins. You took -- damage.", "weight": 0.1, "xhlth": 17, "yhlth": 30},
    {"event": "The guards swarmed you while you were in the treasury and you took -- damage. You caused ** damage but gained no coins.", "weight": 0.1, "xdmg": 10, "ydmg": 17}
]

treasuryweights = [event["weight"] for event in choicetreasurylist]

choicefortlist = [
    {"event": "You successfully attacked the fort and caused ** damage. You gained ++ coins.", "weight": 0.23, "xdmg": 22, "ydmg": 30, "xcoins": 30, "ycoins": 39},
    {"event": "You completely overrun the fort and caused ** damage. You also managed to gain a total of ++ coins!", "weight": 0.2, "xdmg": 30, "ydmg": 47, "xcoins": 40, "ycoins": 69},
    {"event": "The fort's defenses were strong, but you were able to cause ** damage and gain ++ coins.", "weight": 0.2, "xdmg": 15, "ydmg": 25, "xcoins": 15, "ycoins": 27},
    {"event": "The fort's defenses were too strong and you were only able to cause ** damage. You gained no coins.", "weight": 0.18, "xdmg": 5, "ydmg": 15},
    {"event": "The fort's defenders fought back fiercly causing you to take -- damage.", "weight": 0.2, "xhlth": 20, "yhlth": 35}
]

fortweights = [event["weight"] for event in choicefortlist]

choiceransomlist = [
    "You successfullly ransomed the hostages and gained a large sum of ++ coins. You also dealt ** damage to the village."
    "The villagers paid a hefty ransom for the safe return of their loved ones. You gained a lot of coins from the negotiation. + ++ coins."
    "The hostages were important figures in the village and their release came at a high price. You gained a significant amount of coins from the ransom. + ++ coins."
    "You capture some of the villagers and demand a ransom for their release. You gain ++ coins but loose some defense."
    "The hostages were not wealthy and the village refused to pay for the ransom. You gained no coins from the negotiation."
    "The hostages organized a counter-attack and made you take -- damage. You gained no coins."
    "The hostages turned out to be special trained forces of the army and managed to take you hostage instead. You paid ++ coins for your own release and took -- damage. Talk about being dumb."
]

choicesneaklist = [
    "You manage to sneak into the town hall and steal valuable treasures. You caused ** damage and gained ++ coins."
    "The town hall's guards put up a fight, but you were able to steal ++ coins and deal ** damage."
]

