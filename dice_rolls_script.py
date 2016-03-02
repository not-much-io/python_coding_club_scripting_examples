from random import randint


def intro():
    print("Enter the amount of times you wish to roll the dice and how many sides the dice has"
          "\nSample input '2d4' Could produce : (3, 1) the sum would be 4 "
          "\nEnter input : ", end="")
    return input().split("d")


def generate_rolls(nr_dice, dice_sides):
    result = []
    while nr_dice > 0:
        result.append(randint(1, dice_sides))
        nr_dice -= 1
    return result


if __name__ == '__main__':
    user_input = intro()
    nr_dice = int(user_input[0])
    dice_sides = int(user_input[1])
    answer = generate_rolls(nr_dice, dice_sides)
    print(str(answer) + " the sum is " + str(sum(answer)))
