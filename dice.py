import random

print("What is your name?\n> ",end = '')
name=input()
print('Hello, %s!' % name)

dice1=random.randint(1,6)
dice2=random.randint(1,6)
total=dice1+dice2

print("Rolling the dice...")
print('Die 1: %d' % dice1)
print('Die 2: %d' % dice2)
print('Total value: %d' % total)

if total>7:
    print("%s won!" % name) 
else:
    print("%s lost!" % name)

count=0
for i in range(1,7):
    for j in range(1,7):
        if total==i+j:
            count+=1
print('Probability that Total value becomes %d: %d/36' % (total,count))
