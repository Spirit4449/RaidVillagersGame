player_health = 100
player_defense = 5
player_attack = 5

village_health = None

win = False
loose = False


weaponlist = ['katana', 'ak47', 'sword', 'knife', 'grenade', 'stick', 'baseball bat', 'shotgun', 'nuclear bomb',
              'bow and arrow', 'spear', 'electric rifle', 'pistol', 'water gun', 'shuriken', 'nunchucks', 'paper airplane', 'machine gun']

choicelist = [
    'Raid a house',
    'Set a house on fire',
    ' a house',
    'Break into mansion',
    'Swim in the pool',
    'Raid the treasury',
    'Attack a fort',
    'Sabotoge a mine',
    'Sneak into town hall',
    'Loot the marketplace',
    'Raid a farm',
    'Hide in the well',
    'Infiltrate a library',
    'Disable defenses'
]

choiceraidlist = [
    "You succesfully raided the house and dealt __ damage to the village",
    "You destroyed the house dealing __ damage and gained +__ coins",
    "You found +__ coins in the raid",
    "You got shot by the home owner and took -__ damage",
    "The home owner chased you and you tried to jump out of the window and took -__ damage"
]

choicefirelist = [
    "You set a house on fire and cause __ damage. You gained +__ coins.",
    "The house burns to the ground, causing __ damage to the village. You gained +__ coins"
    "The villagers put out the fire only dealing __ damage. You gained no coins."
    "You actually ended up setting several houses on fire and dealt __ damage! And you gained a whopping +__ coins!"
    "The wind blew out the fire and didn't deal any damage. What a waste of time."
    "You messed up while lighting the fire and actually burned yoruself. You took -__ damage."
]

choicemansionlist = [
    "You caused massive damage to the items in the mansion and dealt __ damage. Unfortunately you didn't think of stealing the items and didn't obtain any coins."
    "The mansions guards put up a fight but you were able to overpower them and deal __ damage. You also gained +__ coins"
    "You carefully infiltrated the mansion and stole valuable artwork and jewelry. Your stealthy tactics caused no damage and you gained +__ coins."
    "The mansion's security was no match for your skills. You successfully stole valuable antiques and gained a bonus to your defense. You caused no damage and gained +__ coins."
    "The mansion was empty but you found valuable items. You caused __ damage but gained +__ coins."
    "The mansion was heavily guarded and you were caught. You took -__ damage and gained no coins."
    "The mansion had many security cameras and they alerted the police. You managed to escape but took -__ damage. "
]

choiceswimlist = [
    "You take a swim and enjoy the cool water. You gain 10 coins and cause 0 damage."
    "You take a dive in the water and found a fortue worth of coins at the bottom. You gained +__ coins but didn't do any damage"
    "You splash around in the pool, enjoying the luxurious surroundings. You gain +__ coins and cause no damage."
    "The pool is empty and you gain no coins and cause 0 damage."
    "The villagers were having a pool party and chased you down. You took -__ damage."
]

choicetreasurylist = [
    "The raid on the treasury was a complete success! You caused __ damage and gained +__ coins"
    "The guards put up a fight but you were able to steal +__ coins and cause __ damage."
    "You successfully raided the treasury and gained a stash of coins. You caused __ damage and gained +__ coins."
    "The treasury was empty, causing 0 damage and gaining no coins"
    "You could pick the lock to the treasury and gained no coins. You also took -__ damage."
    "The guards swarmed you while you were in the treasury and you took -__ damage. You caused __ damage but gained no coins."
]

choicefortlist = [
    "You successfully attacked the fort and caused __ damage. You gained +__ coins and gained an advantage in this battle"
    "You completely overrun the fort and caused __ damage. You also managed to gain a total of +__ coins!"
    "The fort's defenses were strong, but you were dable to cause __ damage and gain +__ coins."
    "The fort's defenses were too strong and you were only able to cause __ damage. You gained no coins."
    "The fort's defenders fought back fiercly causing you to take -__ damage and you gained no coins."
]

choiceransomlist = [
    "You successfullly ransomed the hostages and gained a large sum of +__ coins. You also dealt __ damage to the village."
    "The villagers paid a hefty ransom for the safe return of their loved ones. YOu gained a lot of coins from the negotiation. + +__ coins."
    "The hostages were important figures in the village and their release came at a high price. You gained a significant amount of coins from the ransom."
    "You capture some of the villagers and demand a ransom for their release. You gain +__ coins but loose some defense."
    "The hostages were not wealthy and the village refused to pay for the ransom. You gained no coins from the negotiation."
    "The hostages organized a counter-attack and made you take -__ damage. You gained no coins."
    "The hostages turned out to be special trained forces of the army and manage to take you hostage instead. You paid +__ coins for your release and took -__ damage."
]

choicesneaklist = [
    "You manage to sneak into the town hall and steal valuable treasures. You caused -__ damage and gained +__ coins."
    "The town hall's guards put up a fight, but you were able to steal +__ coins and deal __ damage."
]
