from random import randint


def intro():
    print("Enter the amount of times you wish to roll the dice and how many sides the dice has")
    print("Sample input \"2d4\" Would produce : (3, 1) the sum would be 4")
    print("Enter input : ")
    return input().lower().split("d")


def generate_rolls(rollsNr, sides):
    answer = tuple()
    while (rollsNr > 0):
        answer = answer + (randint(1, sides),)
        rollsNr -= 1
    return answer


if __name__ == '__main__':
    x = intro()
    x = tuple(map(int, x))
    answer = generate_rolls(x[0], x[1])
    print(str(answer) + " the sum would be " + str(sum(answer)))
