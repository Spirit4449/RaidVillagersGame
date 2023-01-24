player_health = 100
player_defense = 5
player_attack = 5

player_coins = 0
raid_coins = 0

village_health = None

win = False
loose = False


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
    {"event": "You succesfully raided the house and dealt ** damage to the village.", "weight": 0.5, "xdmg": 20, "ydmg": 35},
    {"event": "You destroyed the house dealing ** damage and gained ++ coins", "weight": 0.35, "xdmg": 20, "ydmg": 35},
    {"event": "You found ++ coins in the raid", "weight": 0.05, "xdmg": 20, "ydmg": 35},
    {"event": "You got shot by the home owner and took -- damage", "weight": 0.05, "xdmg": 20, "ydmg": 35},
    {"event": "The home owner chased you and you tried to jump out of the window and took -- damage.", "weight": 0.05, "xdmg": 20, "ydmg": 35}
]

raidweights = [event["weight"] for event in choiceraidlist]

choicefirelist = [
    "You set a house on fire and cause ** damage. You gained ++ coins.",
    "The house burns to the ground, causing ** damage to the village. You gained ++ coins"
    "The villagers put out the fire only dealing ** damage. You gained no coins."
    "You actually ended up setting several houses on fire and dealt ** damage! And you gained a whopping ++ coins!"
    "The wind blew out the fire and didn't deal any damage. What a waste of time."
    "You messed up while lighting the fire and actually burned yoruself. You took -- damage."
]

choicemansionlist = [
    "You caused massive damage to the items in the mansion and dealt ** damage. Unfortunately you didn't think of stealing the items and didn't obtain any coins."
    "The mansions guards put up a fight but you were able to overpower them and deal ** damage. You also gained ++ coins"
    "You carefully infiltrated the mansion and stole valuable artwork and jewelry. Your stealthy tactics caused no damage and you gained ++ coins."
    "The mansion's security was no match for your skills. You successfully stole valuable antiques and gained a bonus to your defense. You caused no damage and gained ++ coins."
    "The mansion was empty but you found valuable items. You caused ** damage but gained ++ coins."
    "The mansion was heavily guarded and you were caught. You took -- damage and gained no coins."
    "The mansion had many security cameras and they alerted the police. You managed to escape but took -- damage. "
]

choiceswimlist = [
    "You take a swim and enjoy the cool water. You gain ++ coins but cause 0 damage."
    "You take a dive in the water and found a fortue worth of coins at the bottom. You gained ++ coins but didn't do any damage"
    "You splash around in the pool, enjoying the luxurious surroundings. You gain ++ coins and cause no damage."
    "The pool is empty and you gain no coins and cause 0 damage."
    "The villagers were having a pool party and chased you down. You took -- damage."
]

choicetreasurylist = [
    "The raid on the treasury was a complete success! You caused ** damage and gained ++ coins"
    "The guards put up a fight but you were able to steal ++ coins and cause ** damage."
    "You successfully raided the treasury and gained a stash of coins. You caused ** damage and gained ++ coins."
    "The treasury was empty, causing 0 damage and gaining no coins"
    "You could pick the lock to the treasury and gained no coins. You also took -- damage."
    "The guards swarmed you while you were in the treasury and you took -- damage. You caused ** damage but gained no coins."
]

choicefortlist = [
    "You successfully attacked the fort and caused ** damage. You gained ++ coins and gained an advantage in this battle"
    "You completely overrun the fort and cause ** damage. You also managed to gain a total of ++ coins!"
    "The fort's defenses were strong, but you were dable to cause ** damage and gain ++ coins."
    "The fort's defenses were too strong and you were only able to cause ** damage. You gained no coins."
    "The fort's defenders fought back fiercly causing you to take -- damage."
]

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

choicetreasurylist = [
  "The raid on the treasury was a complete success! You caused ** damage and gained ++ coins"
  "The guards put up a fight but you were able to steal ++ coins and cause ** damage."
  "You successfully raided the treasury and gained a stash of coins. You caused ** damage and gained ++ coins."
  "The treasury was empty, causing 0 damage and gaining no coins"
  "You could not figure out how to pick the lock to the treasury and gained no coins. You also took -- damage."
  "The guards swarmed you while you were in the treasury and you took -- damage. You caused ** damage but gained no coins."
]
