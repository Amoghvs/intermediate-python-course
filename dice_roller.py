import random

dice_sum=0
dice_rolls=2

for i in range(0,dice_rolls):
 roll=random.randint(1,6)
 dice_sum+=roll
 print(f' You rolled a {roll}')
print(f'You rolled a {dice_sum}')
