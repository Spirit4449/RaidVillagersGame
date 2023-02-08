# DISCLAIMER: OPEN CONSOLE FULL SCREEN FOR THE BEST EXPERIENCE

import var
import time
import random
import csv
import sys
import threading
from datetime import date
from battle import battle_start
from colorama import Fore, Style, Back, init

# Initialize colorama
init(autoreset=True)


# Function to add data to a csv file
def add_Data(data, file_Name='database.csv'):
  # fields = ['Name', 'Attack', 'Defense', 'Health', 'Coins']
  rows = []
  for value in data:
    rows.append(value)

  with open(file_Name, 'a+', newline='') as file:
    # Mode a+ appends without rewriting
    # Create writer object
    csvfile = csv.writer(file)

    # Write Fields (puts on same row)
    # csvfile.writerow(fields)

    # writeMyData (Puts on different rows)
    csvfile.writerow(rows)


# add_Data
def add_Name(name, file_Name='admins.csv'):
  with open(file_Name, 'a+') as file:
    csvfile = csv.writer(file)
    csvfile.writerow([name])


# Function to print text slowly
def print_slow(text, speed=0.01):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(speed)


# File to store the data
file = 'database.csv'

# Read the data from the file and store it in a variable
var.generated_Data = var.read_Data(file)

# Ask the player for their name and store it in a variable
print_slow('Player Name: ')
var.name = input(Fore.CYAN).lower()
# Reset the color output
print(Style.RESET_ALL, end='')


# Function to handle when the player wins the game
def win():
  atklevel = int((var.player_attack) / 5)
  deflevel = int((var.player_defense) / 5)
  hlthlevel = int((var.max_health - 100) / 15)

  # List of colors
  colors = [
    Fore.BLACK, Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.RED, Fore.MAGENTA,
    Fore.YELLOW
  ]

  # Check if all stats are maxed out
  if atklevel == 10 and deflevel == 10 and hlthlevel == 10:
    add_Name(var.name)
    time.sleep(.5)
    print_slow('All of your stats are now maxed!')
    var.admins.append(var.name)
    time.sleep(2)
    print(f'''
    🗡️  Attack - Level {atklevel} {Fore.BLUE}(MAX){Fore.RESET}
    🛡️  Defense - Level {deflevel} {Fore.BLUE}(MAX){Fore.RESET}
    ❤️  Health - Level {hlthlevel} {Fore.BLUE}(MAX){Fore.RESET}
    ''')
    time.sleep(4)
    colorchange = 0
    # Loop to change the color of the message repeatedly for a few seconds
    while colorchange < 15:
      for color in colors:
        print(color + 'Congratulations on beaing the game!' + Fore.RESET,
              end='\r')
        time.sleep(.8)
        colorchange += 1

    print(Fore.MAGENTA + 'You are now an admin!. You now have access to /admincommands')
    print_slow(
      'Now that you have beat the game, would you like to continue playing? You can always change your answer later. (Yes or No): '
    )
    while True:
      # Ask if the player wants to keep playing since they won they game or stop playing
      continuePlaying = input(Fore.CYAN)
      if continuePlaying.lower() == 'yes':
        print(Fore.RESET, end='')
        print_slow(
          'Ok you are welcome to continue playing. If you would like to restart from the beggining play under another name.\n\n'
        )
        break
        return
      elif continuePlaying.lower() == 'no':
        print(Fore.RESET, end='')
        print_slow(
          'Ok, I wish you a goodbye! If you would like to play again just use the same name. If you would like to restart from the beggining play under another name.'
        )
        exit()
      else:
        print(Fore.RESET, end='')
        print("I didn't catch what you said. (Yes or No): ", end='')


def guidebook(page_number=1):
  page_number = page_number

  if int(page_number) == 1:
    chapter = 'Table of Contents'
    print(f"""
{Style.BRIGHT}📕 Guidebook               {Fore.YELLOW}Page {page_number}{Fore.RESET}
{Back.LIGHTBLUE_EX}{chapter}:{Style.RESET_ALL}
{Back.GREEN}     Battling    -    Page 2 {Style.RESET_ALL}
{Back.GREEN}     Upgrading   -    Page 3 {Style.RESET_ALL}
{Back.GREEN}     Shop        -    Page 4 {Style.RESET_ALL}
{Back.GREEN}     Winning     -    Page 5 {Style.RESET_ALL}
To exit guide type: {Fore.RED}exit
""")

  if int(page_number) == 2:
    chapter = 'Battling'
    print(f"""
{Style.BRIGHT}📕 Guidebook               {Fore.YELLOW}Page {page_number}{Fore.RESET}
{Back.LIGHTBLUE_EX}{chapter}:{Style.RESET_ALL}{Back.GREEN}
Battling is the most important part of the game and represents a 
substantial amount of coins. Prior to entering a battle, it is 
advisable to ensure that your health is at its maximum level to 
minimize the risk of defeat. The village health is determined through
a combination of your character's stats and a 
random number generation (RNG) factor.

Once the battle begins, you will be presented with a menu 
displaying your character's stats. It is imperative to 
review these stats, as if you have neglected to upgrade your 
health, it will become apparent at this stage. Next, you will be 
asked to choose a weapon from the available options, each 
possessing its own unique abilities. No weapon is better than the other,
but it depends on which weapon best suits you.

After selecting your weapon, you will be given a choice 
between three different scenarios, each with its distinct 
advantages and disadvantages in terms of coins earned,
damage dealt, and the likelihood of inflicting damage. 
The outcome of each scenario will be determined by both your 
current stats and an RNG factor.

The battle can conclude in either victory, or defeat. If victorious, 
you will keep all the coins earned during the battle. If defeated, 
you will lose 20% of your current coins. If defeated while having a 
lifesaver equipped, you will be able to continue with the battle with
full health once again. After this you can still die, but it is very 
unlikely.

In conclusion, battling is a vital aspect of the game that offers a 
substantial source of coins. It is advisable to invest time into 
upgrading your character's stats before entering a battle. 
To initiate a battle, use the command "/battle".
{Style.RESET_ALL}
""")

  if int(page_number) == 3:
    chapter = 'Upgrading'
    print(f"""
{Style.BRIGHT}📕 Guidebook               {Fore.YELLOW}Page {page_number}{Fore.RESET}
{Back.LIGHTBLUE_EX}{chapter}:{Style.RESET_ALL}{Back.GREEN}
Upgrading your stats is an essential aspect of playing the game, 
as it makes battling easier and enables you to reach the maximum stat 
levels more quickly. To upgrade a stat, simply enter the command 
"/upgrade" and specify which stat you wish to upgrade. 
The "/upgrades" command will display a menu with detailed information
about the cost of each upgrade and which stats are available for upgrading.
It should be noted that the cost of upgrades increases with each 
upgrade, and the maximum level for each stat is 10. At level 10, 
the stats are as follows: Attack: 50, Defense: 50, and Health: 250. 
Additionally, upgrading your health will also set it to its maximum 
value, which can be used as a strategic advantage to conserve coins 
rather than spending them on meat. The primary benefit of upgrading 
your stats is to more efficiently destroy villages and advance in the game.

Upon reaching the maximum levels for all of your stats, you will 
have officially won the game. Further information on winning can 
be found on Page 5 of the guidebook (Winning).{Style.RESET_ALL}
""")

  if int(page_number) == 4:
    chapter = 'Shop'
    print(f"""
{Style.BRIGHT}📕 Guidebook               {Fore.YELLOW}Page {page_number}{Fore.RESET}
{Back.LIGHTBLUE_EX}{chapter}:{Style.RESET_ALL}{Back.GREEN}
The in-game shop offers a range of items that can aid the player
in their progress through the game. The shop consists of three 
items: meat, a lifesaver, and a coin doubler. The cost of each 
item can be viewed by using the "/shop" command. To purchase an 
item, the player must use the "/buy [item]" command.

Meat is an essential item in the game, as it can restore health. 
It is almost impossible to complete the game without purchasing 
meat at least once. Meat restores 25 health points, but it will 
not exceed the player's maximum health. For example, if a 
player's maximum health is 115 and their current health is 110,
the meat will only restore 5 health points.

The lifesaver, costing 250 coins, is another useful item in the 
game. This item allows the player to continue battling even if 
their health reaches zero. If the lifesaver item is utilized,
the player's health will be restored to its maximum value and 
the lifesaver item will be consumed. The player must purchase 
the lifesaver item again in order to use it in subsequent battles. 
The effect of the lifesaver will remain in effect until the player 
logs out of the game or the lifesaver is consumed during a battle.
The player can check if they have a lifesaver active by using the "/stats" command.

Finally, the coin doubler costs 400 coins and doubles all coins
the player recieves for the next minute. It is a wise investment 
for players who can make the most of the one-minute time frame. 
The coin doubler will send a message when it's effect expires.{Style.RESET_ALL}
""")
  if int(page_number) == 5:
    chapter = 'Winning'
    print(f"""
{Style.BRIGHT}📕 Guidebook               {Fore.YELLOW}Page {page_number}{Fore.RESET}
{Back.LIGHTBLUE_EX}{chapter}:{Style.RESET_ALL}{Back.GREEN}
Winning the game is a major accomplishment and requires a combination
of strategy and determination. In order to win the game, you must 
first focus on leveling up your character's stats. The goal is to 
get all of your stats to level 10, which can be achieved by battling 
enemies and earning coins to upgrade your character's abilities.
Once you have accomplished this task, you will be rewarded with a 
special message and access to admin commands. This new level of 
access allows you to explore and experience the game on a whole new 
level, so make sure to work hard and earn those coins! I wonder what
you can do with admin commands... 👀. You will have to find out for
yourself. Good luck!{Style.RESET_ALL}
""")
  return page_number


# Gets the date the player logged in
global today
today = date.today()
var.loginDate = today.strftime("%d-%m-%y")

# Function to retrieve data if the player has played the game before. It checks if their name is already in the database


def retrievedata():
  for list in var.generated_Data:
    for value in list:
      if value == var.name:
        var.player_attack = int(list[1])
        var.player_defense = int(list[2])
        var.player_health = int(list[3])
        var.max_health = int(list[4])
        var.player_coins = int(list[5])
        var.loginDate = list[6]
        var.tutorial = False

  # If the player is not found in the database, it will set the tutorial to TRUE so they can learn the game
  if var.tutorial == True:
    new_player = [
      var.name, var.player_attack, var.player_defense, var.player_health,
      var.max_health, var.player_coins, var.loginDate
    ]
    add_Data(new_player)
    var.tutorial = True


# Calls the function
retrievedata()

    

# Gets the login information from the database and splits it into multiple strings for the next step
loginlist = var.loginDate.split("-")
# Tutorial
if var.tutorial == True:
  print_slow(
    f"Welcome to Raid Villagers {var.name}! Raid Villagers is an adventure game where you play as a raider attacking villages for gold and treasure. Your goal is to become the most powerful raider by upgrading your character's stats. Are you ready to embark on this epic adventure?\n",
    0.01)
  time.sleep(8)

  print('\nLet\'s start by attacking your first village.\n')
  time.sleep(2)

  battle_start()

# If it has been multiple days since the user logged on, the game will prompt the player if they want a quick tutorial
elif int(today.strftime("%y")) - int(loginlist[2]) > 0 or int(
    today.strftime("%m")) - int(loginlist[1]) > 0 or int(
      today.strftime("%d")) - int(loginlist[0]) >= 2:
  print('Welcome back ' + var.name)
  time.sleep(.5)
  print_slow('Would you like a quick tutorial? ', 0.01)
  quicktutorial = input(Fore.CYAN)
  print(Style.RESET_ALL, end="")
  while True:
    if quicktutorial.lower() == 'yes':
        var.tutorial = True
        print("Ok, here is a quick tutorial. Lets start by going into a battle.")
        time.sleep(2)
        battle_start(True)
        break
    elif quicktutorial.lower() == 'no':
        print("Ok. If you need a list of commands type " + Fore.CYAN + "/help\n")
        break
    else:
        print("That is not a valid option!")

# A quick welcome for the returning player
else:
  
  print('Welcome back ' + var.name)
  time.sleep(.4)
  print('Type' + Fore.YELLOW + ' /help' + Fore.RESET +
        ' for a list of commands')

  
# Sets the login date
var.loginDate = today.strftime("%d-%m-%y")
var.save_data(var.name, var.player_attack, var.player_defense,
              var.player_coins, var.player_health, var.max_health,
              var.loginDate)

# At this point the tutorial is almost finished. The player is ready to explore on their own.
if var.tutorial == True:
  time.sleep(1)
  print('You completed your first battle!')
  time.sleep(1)
  print(
    f"""You are now ready to play the game! Here are some quick pointers:
The game is command based. You type commands to execute actions
The goal is to upgrade all your stats to level 10.
Battling gives you coins so you can upgrade stats and buy stuff from the shop{Style.RESET_ALL}
Type {Fore.YELLOW}/help{Fore.RESET} to view the list of commands..."""
  )
  var.tutorial = False

# Creates a variable: valid_command
valid_command = False


# Admin check
adminPrint = ''
adminlist = var.read_Data('admins.csv')
for name in adminlist:
  if str(var.name) == name[0]:
    time.sleep(0.5)
    print('This account also has admin commands: ' + Fore.YELLOW + '/admincommands')
    var.admin = True

# Main loop for the game. The player has the freedom to type whatever commands they want while this loop is running. The game responds depending on which command the player chose
while True:
  # Sets the state of the game
  var.state = 'menu'
  # Input for the command
  command = input(Fore.CYAN).lower()
  command = command.strip()
  # Resets the color
  print(Style.RESET_ALL, end="")

  # Help command
  if command == '/help':
    valid_command = True
    print(F"""
{Fore.LIGHTRED_EX}📃 /help - displays the help command
{Fore.BLUE}⚔️  /battle - starts a battle
{Fore.LIGHTGREEN_EX}💪 /upgrades - displays a list of upgrades to your character
{Fore.MAGENTA}📊 /stats - displays your current stats
{Fore.LIGHTCYAN_EX}🛒 /shop - brings a menu with items you can buy
{Fore.YELLOW}💰 /coins - displays current amount of coins
{Fore.GREEN}📕 /guide - displays a guide to the game
{Fore.RED}❌ /exit - exits the game (progress is saved)
""",
          end="")

    # If the player is an admin it displays an extra command
    if var.admin == True:
      print(
        Fore.LIGHTBLACK_EX +
        '💎 /admincommands - displays a list of commands only admins can use\n')
    # If they are not it will print a new line
    else:
      print('\n', end='')

  # Shop Command. This code handles the functionality of the /shop command in the game. The player can view a list of items available for purchase and then buy them using the /buy [item] command.
  if command == '/shop':
    valid_command = True
    print(f"""
{Style.BRIGHT}SHOP        Your coins: {Fore.LIGHTYELLOW_EX}{var.player_coins}{Style.RESET_ALL}
🍖 Meat - {Fore.GREEN}50 coins{Style.RESET_ALL}
     Restores health for 25 hitpoints
💝 Lifesaver - {Fore.GREEN}250 coins{Style.RESET_ALL}
     Gives another change if you are about to die. (Can only buy one at a time)
🪙  Coin Doubler - {Fore.GREEN}400 coins{Style.RESET_ALL}
     Doubles all coins you earn for the next minute
{Fore.BLACK}Type /buy [item] to purchase""")

  # Meat
  if command == '/buy meat':
    valid_command = True
    hlthlevel = int((var.max_health - 100) / 15)
    if var.player_health < var.max_health:
      if var.player_coins - 50 >= 0:
        var.player_coins -= 50
        var.player_health += 25
        if var.player_health >= var.max_health:
          var.player_health = var.max_health
        print(Fore.GREEN +
              'You just bought a meat for 50 coins! Your health is now ' +
              str(var.player_health))
      else:
        print(Fore.RED + "You don't have enough coins to buy that!")
    else:
      print(Fore.RED + 'You are already at max health!')

  # Lifesaver
  elif command == '/buy lifesaver':
    valid_command = True
    if var.lifesaver != True:
      if var.player_coins - 250 >= 0:
        var.player_coins -= 250
        var.lifesaver = True
        print(
          Fore.GREEN +
          'You just bought a lifesaver for 250 coins! Lifesaver will be active until it is used or you exit the game.'
        )
      else:
        print(Fore.RED + "You don't have enough coins to buy that!")
    else:
      print(Fore.LIGHTRED_EX + 'A lifesaver is already active!')

  # Coin doubler
  elif command == '/buy coin doubler' or command == '/buy coindoubler' or command == '/buy coin doubler' or command == '/buy doubler':

    # Function that starts a seperate thread that counts down from 1 minute
    def coin_doubler():
      x = 0
      while True:
        time.sleep(1)
        x += 1
        if x == 60:
          var.coindoubler = False
          break
        else:
          continue
      while var.state != 'menu':
        time.sleep(1)
        continue
      else:
        print(Fore.YELLOW + 'Coin doubler has expired')

    valid_command = True
    if var.coindoubler == False:
      if var.player_coins - 400 >= 0:
        var.player_coins -= 400
        var.coindoubler = True
        print(
          Fore.GREEN +
          'You just bought a coin doubler for 400 coins! You have one minute to use it!'
        )

        # Starts the countdown
        t1 = threading.Thread(target=coin_doubler)
        t1.start()

      else:
        print(Fore.RED + "You don't have enough coins to buy that!")
    else:
      print(Fore.LIGHTRED_EX + 'A coin doubler is already active!')

  # Upgrade command
  elif command == '/upgrades' or command == '/upgrade':
    valid_command = True
    atklevel = int((var.player_attack) / 5)
    deflevel = int((var.player_defense) / 5)
    hlthlevel = int((var.max_health - 100) / 15)

    atkcoins = 50 + (50 * atklevel)
    defcoins = 50 + (50 * deflevel)
    hlthcoins = 50 + (50 * hlthlevel)

    if int(atklevel) >= 10:
      atkcoins = 'MAX'
    else:
      atkcoins = str(atkcoins) + ' coins'
    if int(deflevel) >= 10:
      defcoins = 'MAX'
    else:
      defcoins = str(defcoins) + ' coins'
    if int(hlthlevel) >= 10:
      hlthcoins = 'MAX'
    else:
      hlthcoins = str(hlthcoins) + ' coins'

    print(f"""
{Style.BRIGHT}UPGRADES        Your coins: {Fore.YELLOW}{var.player_coins}{Style.RESET_ALL}
🗡️  Attack (Lvl {atklevel}) - {Fore.GREEN}{atkcoins}{Fore.RESET}
     Increases attack by 5
🛡️  Defense (Lvl {deflevel}) - {Fore.GREEN}{defcoins}{Fore.RESET}
     Increases defense by 5
❤️  Health (Lvl {hlthlevel}) - {Fore.GREEN}{hlthcoins}{Fore.RESET}
     Increases max health by 15
{Fore.BLACK}Max Level for all stats: 10
{Fore.BLACK}Type /upgrade [stat] to upgrade
""")

  # Upgrade attack
  if command == '/upgrade attack' or command == '/upgrade [attack]':
    valid_command = True
    atklevel = int((var.player_attack) / 5)
    atkcoins = 50 + (50 * atklevel)
    if atklevel < 10:
      if var.player_coins - atkcoins >= 0:
        var.player_coins -= atkcoins
        var.player_attack += 5
        atklevel += 1
        print(Fore.GREEN + 'You successfully upgraded your attack to level ' +
              str(atklevel) + ' for ' + str(atkcoins) + ' coins')
        time.sleep(0.5)
        win()
      else:
        print(Fore.RED + "You don't have enough coins!")
    else:
      print(Fore.LIGHTRED_EX + "Your attack is already at the max level!")

  # Upgrade defense
  if command == '/upgrade defense' or command == '/upgrade [defense]':
    valid_command = True
    deflevel = int((var.player_defense) / 5)
    defcoins = 50 + (50 * deflevel)
    if deflevel < 10:
      if var.player_coins - defcoins >= 0:
        var.player_coins -= defcoins
        var.player_defense += 5
        deflevel += 1
        print(Fore.GREEN + 'You successfully upgraded your defense to level ' +
              str(deflevel) + ' for ' + str(defcoins) + ' coins')
        time.sleep(0.5)
        win()
      else:
        print(Fore.RED + "You don't have enough coins!")
    else:
      print(Fore.LIGHTRED_EX + "Your attack is already at the max level!")

  # Upgrade health
  if command == '/upgrade health' or command == '/upgrade [health]':
    hlthlevel = int((var.max_health - 100) / 15)
    hlthcoins = 50 + (50 * hlthlevel)
    valid_command = True
    if hlthlevel < 10:
      if var.player_coins - hlthcoins >= 0:
        var.player_coins -= hlthcoins
        var.max_health += 15
        var.player_health = var.max_health
        hlthlevel += 1
        print(Fore.GREEN + 'You successfully upgraded your health to level ' +
              str(hlthlevel) + ' for ' + str(hlthcoins) + ' coins')
        win()
      else:
        print(Fore.RED + "You don't have enough coins!")
    else:
      print(Fore.LIGHTRED_EX + "Your attack is already at the max level!")

  # Battle command
  elif command == '/battle':
    valid_command = True
    battle_start()

  # Exit command
  elif command == '/exit':
    valid_command = True
    print(
      Fore.YELLOW +
      'Thank you for playing. Next time you play, use the same name and you can restore your progress!'
    )
    # Makes sure the code does not error out when joining the other thread
    try:
      t1.join()
    except NameError:
      pass
    exit()

  # Player stats command
  elif command == '/stats':
    valid_command = True
    # Determines the levels of the player
    atklevel = int((var.player_attack) / 5)
    deflevel = int((var.player_defense) / 5)
    hlthlevel = int((var.max_health - 100) / 15)
    # Prints the levels
    print(f"""
Stats for {var.name}:
🗡️  Attack: {Fore.MAGENTA}{str(var.player_attack)}{Fore.RESET}  (Level {atklevel})
🛡️  Defense: {Fore.GREEN}{str(var.player_defense)}{Fore.RESET} (Level {deflevel})
❤️  Health: {Fore.RED}{str(var.player_health)}{Fore.RESET} (Level {hlthlevel})
""")
    # If lifesaver is active print "Livesaver active"
    if var.lifesaver == True:
      print(Style.DIM + 'Lifesaver active')
    # If coin doubler is active print "Coin doubler active"
    if var.coindoubler == True:
      print(Style.DIM + 'Coin doubler active')

  # Simmple command to display user coins
  elif command == '/coins':
    valid_command = True
    print('You currently have ' + Fore.YELLOW + str(var.player_coins) +
          Fore.RESET + ' coins')

  elif command == '/guide' or command == '/tutorial' or command == '/guidebook':
    page_number = guidebook()
    while True:
      current_page = page_number
      page_number = input('Page Number: ')
      if page_number == current_page:
        print(Fore.RED + 'You are already on that page!')
      if page_number.isnumeric() != True and 'exit' not in page_number:
        print(Fore.RED + 'That is not a number!')
      elif page_number not in ['1', '2', '3', '4', '5'
                               ] and 'exit' not in page_number:
        print(Fore.RED + 'That page does not exist!')
      elif 'exit' in page_number.lower():
        print(Fore.BLUE + 'Exited guidebook...')
        break
      else:
        guidebook(page_number)

  # Admin command /givecoins
  elif '/givecoins' in command or '/setcoins' in command:
    valid_command = True
    if var.admin == True:
      if ' ' in command:
        splitlist = command.split(" ")
        try:
          givecoins = int(splitlist[1])
          if '/givecoins' in command:
            var.player_coins += givecoins
            print('Gave ' + Fore.YELLOW + str(givecoins) + Fore.RESET +
                  ' coins')
          if '/setcoins' in command:
            var.player_coins = givecoins
            print('Set your coin balance to ' + Fore.YELLOW + str(givecoins) +
                  Fore.RESET)
        except ValueError:
          print('That is not a number!')
      else:
        print('No value provided')
    else:
      print('Nice try but only admins can do that')

  # Admin command /sethealth
  elif '/sethealth' in command:
    valid_command = True
    if var.admin == True:
      if ' ' in command:
        splitlist = command.split(" ")
        try:
          if var.max_health >= int(splitlist[1]):
            var.player_health = int(splitlist[1])
          else:
            var.max_health = int(splitlist[1])
            var.player_health = var.max_health
          print('Your health is now ' + str(var.player_health))
        except ValueError:
          print('That is not a number!')

      else:
        print('No value provided')
    else:
      print('Nice try but only admins can do that')

  # Admin command /setattack
  elif '/setattack' in command:
    valid_command = True
    if var.admin == True:
      if ' ' in command:
        splitlist = command.split(" ")
        try:
          var.player_attack = int(splitlist[1])
          print('Your attack is now ' + str(var.player_attack))
        except ValueError:
          print('That is not a number!')
      else:
        print('No value provided')
    else:
      print('Nice try but only admins can do that')

  # Admin command /setdefense
  elif '/setdefense' in command:
    valid_command = True
    if var.admin == True:
      if ' ' in command:
        splitlist = command.split(" ")
        try:
          var.player_defense = int(splitlist[1])
          print('Your defense is now ' + str(var.player_defense))
        except ValueError:
          print('That is not a number!')
      else:
        print('No value provided')
    else:
      print('Nice try but only admins can do that')

  # Funny command. I created it for fun
  elif command == '/hack':
    if var.admin == True:
      print('I warned you not to run this command...')
      time.sleep(1)
      for i in range(0, 16):
        for j in range(0, 16):
          code = str(i * 16 + j)
          sys.stdout.write(u"\u001b[48;5;" + code + "m " + code.ljust(4))
        print(u"\u001b[0m")
      x = 0
      colors = [
        Fore.BLACK, Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.RED, Fore.MAGENTA,
        Fore.YELLOW
      ]
      while x <= 10000:
        color = random.choice(colors)
        print(color + '01', end='')
        x += 1
      print('\n')
    else:
      print('Nice try but only admins can do that')

  # Utility command to help test the game
  elif command == '/resetall':
    valid_command = True
    if var.admin == True:
      var.player_attack = 5
      var.player_defense = 5
      var.player_coins = 0
      var.player_health = 115
      var.max_health = 115
      print(Fore.YELLOW + 'Reset all your data')
    else:
      print('Nice try but only admins can do that')

  # Debugging command that displays multiple variables
  elif command == '/variables':
    if var.admin == True:
      print(f"""
Name: {var.name}\nLogin Date: {var.loginDate}\nAttack: {var.player_attack}\nDefense: {var.player_defense}\nHealth: {var.player_health}\nMax Health: {var.max_health}\nLifesaver: {var.lifesaver}\nCoin Doubler: {var.coindoubler}\n\nVillage Health: {var.village_health}\nRaid Atk: {var.raid_attack}\nRaid Def: {var.raid_defense}\nRaid Coins: {var.raid_coins}\nDouble Damage: {var.double_damage}\n1.5x Damge: {var.halftimesdamage}\n\nAdmins: {var.admins}
""")
    else:
      print('Nice try but only admins can do that')

  # Command to automatically win the game
  elif command == '/win':
    valid_command == True
    if var.admin == True:
      var.player_attack = 50
      var.player_defense = 50
      var.player_health = 250
      var.max_health = 250
      print_slow('Are you sure you want to win the game? (Yes or No): ')
      while True:
        continueWin = input(Fore.BLUE)
        if continueWin.lower() == 'yes':
          print(Fore.RESET, end='')
          win()
          break
        elif continueWin.lower() == 'no':
          print(Fore.RESET, end='')
          print('Alright then...')
          break
        else:
          print("I didn't catch what you said. (Yes or No): ")
          continue
    else:
      print('Nice try but only admins can do that')

  # Similar to help command, displays a list of commands that can only be used by admins
  elif command == '/admincommands':
    if var.admin == True:
      valid_command = True
      print(f"""
💎 /admincommands - displays a list of commands that only admins can use
🤑 /givecoins {Fore.LIGHTBLUE_EX}[amount]{Fore.RESET} - gives x amount of coins
💸 /setcoins {Fore.LIGHTBLUE_EX}[amount]{Fore.RESET} - sets your coins to specified amount
🪄  /setattack {Fore.LIGHTBLUE_EX}[amount]{Fore.RESET} - sets your attack to specified amount
🕶️  /setdefense {Fore.LIGHTBLUE_EX}[amount]{Fore.RESET} - sets your defense to specified amount
😍 /sethealth {Fore.LIGHTBLUE_EX}[amount]{Fore.RESET} - sets your health to specified amount
🏆 /win - beat the game without effort
📚 /variables - displays list of variables used for debugging
⛓️  /hack - do not try this....
♻️  /resetall - resets all your data
  """)
    else:
      print('You are not an admin!')

  # If the command is not valid, it will print this
  elif not valid_command:
    print(Fore.RED +
          "That is not a valid command. Type /help for a list of commands")

  valid_command = False

  # Saves the player data after every command. Save_data function is in var.py since it is accessed by multiple files with circular import.
  var.save_data(var.name, var.player_attack, var.player_defense,
                var.player_health, var.max_health, var.player_coins)
