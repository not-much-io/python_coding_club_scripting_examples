from random import randint


def intro():
    print("Enter the amount of times you wish to roll the dice and how many sides the dice has")
    print("Sample input \"2 4\" Would produce : (3, 1)")
    print("Enter input : ")
    return input().split()


def generate_rolls(rolls_nr, sides):
    answer = tuple()
    while rolls_nr > 0:
        answer = answer + (randint(1, sides),)
        rolls_nr -= 1
    return answer


if __name__ == '__main__':
    x = intro()
    print(generate_rolls(int(x[0]), int(x[1])))
