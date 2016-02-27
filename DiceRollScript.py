from random import randint

def intro():
    print("Enter the amount of times you wish to roll the dice and how many sides the dice has")
    print("Sample input \"2 4\" Would produce : (3, 1)")
    print("Enter input : ")
    return input().split()


def generateRolls(rollsNr, sides):
    answer = tuple()
    while(rollsNr > 0):
        answer = answer + (randint(1, sides),)
        rollsNr -= 1
    return answer

if __name__ == '__main__':
    x = intro()
    print(generateRolls(int(x[0]), int(x[1])))
