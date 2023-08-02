#Game is from Pull Request Practice from week 8 Assignment

import random
import time

first_name = input('What is your first name?\n')
last_name = input("What's your last name?\n")
print(f'Hi, {first_name} {last_name}.')
print()

gamePlay = True
while gamePlay:
  play_game = input(f"Do you want to play a game, {first_name}? y/n  \nPress q to quit. \n").casefold()

  if play_game == 'y':
    def displayIntro():
      print('You are in a land full of dragons. In front of you, you see two caves. In one cave, the dragon is friendly and will share his treasure with you. The other dragon is greedy and hungry, and will eat you on sight.')
    print()

    def chooseCave():
      cave = ''
      while cave != '1' and cave != '2':
            print('Which cave will you go into? (1 or 2)')
            cave = input()
      return cave

    def checkCave(chosenCave):
      print('You approach the cave...')
    #sleep for 2 seconds
      time.sleep(2)
      print('It is dark and spooky...')
    #sleep for 2 seconds
      time.sleep(3)
      print('A large dragon jumps out in front of you! He opens his jaws and...')
      print()
    #sleep for 2 seconds
      time.sleep(2)
      friendlyCave = random.randint(1, 2)

      if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
      else:
        print('Gobbles you down in one bite!')


    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print("Thanks for playing")
    break
    
  elif play_game =='n':
    print("OK, have a great day! Bye!")
    break

  elif play_game == 'q':
    break

  else:
    print("Not sure what you want to do.")
  



