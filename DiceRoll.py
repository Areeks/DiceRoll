import random

def parse_input(input_string):
    if input_string.strip() in {'1', '2', '3', '4', '5', '6'}:
        return int(input_string)
    else:
        print('Please enter a number from 1 to 6.')
        exit()


def roll_dice(n_dice):
    roll_result = []
    for _ in range(n_dice):
        roll = random.randint(1,6)
        roll_result.append(roll)
    return roll_result

n_dice_input = input("How many dice do you want to roll? [1-6] ->")
n_dice = parse_input(n_dice_input)

roll_result = roll_dice(n_dice)
print(roll_result)