import random
import time


print("Do you want to compete against computer or another player?")
dec = input()
print("Enter the number of overs:\t")
overs = int(input())
print("Enter the number of wickets:\t")
wicks = int(input())

runs = 0
choice = 0


class game_info:
    chances = wicks
    run = runs
    ch = choice
    ov = overs*6

    def __init__(self, name):
        self.name = name

    def printdetails(self):
        print(
            f"********{self.name}********\n    Runs scored = {self.run}\n    Wickets remaining = {self.chances}")


p1 = game_info("player1")
if "computer" in dec:
    p2 = game_info("computer")
else:
    p2 = game_info("Player2")

target = 0


def game(t1, t2):

    if (t1.chances == 0):
        print(f"*************{t2.name}'s turn*************")
        print(F"Target run = {t1.run + 1}")

    if t1.ov == overs:
        print(f"*************{t1.name}'s turn*************")

    t1.ch = 0
    t2.ch = 0
    if (t1.chances > 0) and (t1.ov > 0):

        if (t1.name == "player1"):

            print(f"{t1.name}: Swing your bat :\t")
            t1.ch = int(input())
            t2.ch = random.randint(0, 6)

        else:

            print(f"{t2.name}: Throw the ball :\t")
            t2.ch = int(input())

            t1.ch = random.randint(0, 6)

        if (t1.ch == t2.ch):

            print(
                f"{t1.name} chose {t1.ch} and {t2.name} chose {t2.ch}\nIt is an out")
            t1.chances = t1.chances - 1
            print(t1.chances)

        elif t1.ch <= 6 and t1.ch >= 0:

            t1.run = t1.run + t1.ch
            print(f"{t1.name} chose {t1.ch} and {t2.name} chose {t2.ch}\n")
            print(f"{t1.name}'s Run = {t1.run}")
            print(f"{t2.name}'s Run = {t2.run}")

        t1.ov = t1.ov - 1

        if ((t1.chances == 0) and ((t2.chances != 0)) and (t1.ov == 0)):
            print(f"***********{t2.name}***********")
            print(f"Target score = {t1.run + 1}")

        

        game(t1, t2)

    if (t2.chances > 0) and (t2.ov > 0):
        game(t2, t1)

    


def toss():
    toss_dec = random.randint(1, 2)
    if toss_dec == 2:
        print(f"{p2.name} has won the toss")
        time.sleep(1)
        game(p2, p1)
    else:
        print(f"{p1.name} has won the toss")
        time.sleep(1)
        game(p1, p2)


if __name__ == "__main__":

    toss()
    print("\n\n\n**************Results**************")

    p1.printdetails()
    p2.printdetails()

    if (p1.run)>(p2.run):
        print(f"{p1.name} won the game")
    else:
        print(f"{p2.name} won the game")


