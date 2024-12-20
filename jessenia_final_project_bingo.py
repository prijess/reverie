# -*- coding: utf-8 -*-
"""Jessenia_Final Project_Bingo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zAQ7r5-R6CjCt0PA9YWmT9SqrtKjU4jc

#**Bingo**
This is a bingo game system that you can use per what you need.<br>If you only need the callout, just run the callout.<br>If you need the card generation as well, you can run the card generation.<br>If you want to check here if you win? Run the bingo checking cell. <br><br> You can use the cell as itself, but it is *advised to run the first two system.*

**Bingo Number Callout System**<br>Please run this system.
"""

import random

def callout(called):
  while True:
    called_number = random.randint(1, 75)  # create a random number callout in the range of 1-75
    if called_number not in called:
      called.append(called_number)
      break

#limitation for formatting
  if 1 <= called_number <= 15:
      letter = "B"
  elif 16 <= called_number <= 30:
      letter = "I"
  elif 31 <= called_number <= 45:
      letter = "N"
  elif 46 <= called_number <= 60:
      letter = "G"
  else:
      letter = "O"

  formatted_callout = f"{letter} {called_number}" #the formatting
  return called_number, formatted_callout

"""**Bingo Card Generator System**<br>Please run this system."""

import random

def generate_bingo_card(card, column_ranges):
    if not column_ranges:
        return card

    column_name, (start, end) = column_ranges[0]

    numbers = random.sample(range(start, end + 1), 5)  # Get 5 unique numbers
    card[column_name] = numbers

    return generate_bingo_card(card, column_ranges[1:])

# Usage:
column_ranges = [
    ("B", (1, 15)),
    ("I", (16, 30)),
    ("N", (31, 45)),
    ("G", (46, 60)),
    ("O", (61, 75)),
]

"""**Play The Game!**<br>
1. Generate your Bingo Card!<br> By running the generate function that has already been defined on **Bingo Card Generator System**
"""

import time

random.seed(time.time())  #randomize the number in each run

card = {}
generate_bingo_card(card, column_ranges)

"""2. Let the total of 40 random Bingo Numbers Callouts generate!<br>
 By running the callout function that has already been defined on the **Bingo Number Callout System**<br> Enter your name and let the game start. Don't forget to daub the numbers.
"""

import time

input("Name: ")
time.sleep(0.5)


print('')
print("Game Start!")
time.sleep(1)


print('')
#number callout
called = []                               #empty 'called' list
for i in range(40):                       #make a total 40 callout (changable)
  called_number, formatted_callout = callout(called)
  print(formatted_callout)
  time.sleep(2)                           #to make the number callout one-by-one with a 2 seconds delay


print('')
print("Game is Over.")
time.sleep(1)


print('')
called.sort()
print("Your called numbers:", called)     #make a sorted list of the numbers in called

"""And you're done playing bingo!

**Bingo Card Check**<br> Definitely an option if you only want to play by just running the cells. But as far, it can only identifies the column bingo, meaning that if the numbers in B, I, N, G, O, is called in the callout, you will get a bingo.
"""

#retrieving the data from card
B = card.get("B", [])
I = card.get("I", [])
N = card.get("N", [])
G = card.get("G", [])
O = card.get("O", [])

def check_bingo(called):
  bingo = False
  for number in called:   #referring to the number that is in 'called' list
   if number in B:
     B.remove(number)     #removes the number in B when it is 'called' list
   if number in I:
     I.remove(number)
   if number in N:
     N.remove(number)
   if number in G:
     G.remove(number)
   if number in O:
     O.remove(number)

  # Indented the following block within the function
  if not B or not I or not N or not G or not O:
    print("\033[1mBingo!\nCongratulations!!")
    bingo = True  # Set bingo to True when there's a bingo
  else:
    print("\033[1mYou lose.\nTry Again!")
    bingo = False  # Set bingo to False when there's no bingo

  return bingo  # Return the bingo status

_=check_bingo(called)