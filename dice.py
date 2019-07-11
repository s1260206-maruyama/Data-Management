import random

dice1=random.randint(1,6)
dice2=random.randint(1,6)
total=dice1+dice2

print("Rolling the dice...")
print('Die 1: %d' % dice1)
print('Die 2: %d' % dice2)
print('Total value: %d' % total)

if total>7:
    print("You won!") 
else:
    print("You lost!")
