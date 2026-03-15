from Player import HumanPlayer, CpuPlayer
from datetime import datetime
import random
import csv

def loadgame():
    print("Welcome to the game!\nPress 'CTRL+C' at any moment to quit the game.\n")
    N = 100
    toguess = random.randint(0, N)
    oldguess = None

    name = input("Insert your name: ")
    human = HumanPlayer(name)
    cpu = CpuPlayer()
    tries = 0

    while True:
        humannumber = human.insertTry(N)
        if humannumber is None:
            continue
        tries += 1
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        row = [name, toguess, tries, humannumber, now]

        with open("registers.csv", mode='a', encoding='utf-8', newline='') as file:
            scrittore = csv.writer(file, delimiter='\t')
            scrittore.writerow(row)

        oldguess = cpu.insertTry(N, oldguess)

        if human.checkTry(humannumber, toguess) is True:
            print(f"Good job, you guessed the number. It was {toguess} :)")
            break
        oldguess = cpu.checkTry(oldguess, toguess)
        if oldguess is True:
            print(f"I'm sorry but the CPU won this time. The number to guess was {toguess} :(")
            break
        else:
            print(f"The CPU is trying the number {oldguess} next round!")

if __name__ == "__main__":
    loadgame()