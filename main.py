# DISCLAIMER
# OPEN CONSOLE FULL SCREEN FOR THE BEST EXPERIENCE


import time
import random
import colorama
from battle import battle_start
import var

class player:
  player_health = 100
  player_defense = 1
  player_attack = 5

tutorial = False

    
#Tutorial
if tutorial == True:
  print("Welcome to Raid Villagers! Raid villagers is a trhilling text-based adventure game where you play as a ruthless raider, attacking and looting villages for gold and treasure. Your ultimate goal is to become the most powerful raider in the land by upgrading your character's stats. You will have to make strategic choices, outsmart the village defenders, and overcome dangerous obstacles to succeed. You will gain gold throughout your journey. Spend it wisely on your character stats. Now are you ready to embark on this epic journey?  Let's being!")
  time.sleep(5)

  name = input('Player Name: ')
  time.sleep(0.2)
  print('Welcome ' + name + '. Let\'s start by attacking your first village.')
  time.sleep(2)
  
  battle_start()

else:
  name = input('Player Name: ')
  battle_start(False)
  