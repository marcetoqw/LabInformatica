from abc import ABC, abstractmethod
import random

class Player(ABC):
    @abstractmethod
    def insertTry(self, N, oldguess=None):
        pass

    @abstractmethod
    def checkTry(self, number, toguess):
        pass

class HumanPlayer(Player):
    def __init__(self, name):
        self.name = name
    def insertTry(self, N, oldguess=None):
        try:
            number = int(input(f"\nTry inserting a number between 0 and {N}: "))
            if number<0 or number>N:
                raise ValueError("Input number is less than zero or higher than N.")
        except ValueError as v:
            print(f"{v} Try again.")
            number = None
        return number
    def checkTry(self, number, toguess):
        if number>toguess:
            print("Input number is higher than the number to guess.")
            return False
        elif number<toguess:
            print("Input number is lower than the number to guess.")
            return False
        return True
        
class CpuPlayer(Player):
    def insertTry(self, N, oldguess):
        if oldguess is None:
            number = random.randint(0, N)
            return number
        return oldguess
    def checkTry(self, number, toguess):
        if number>toguess:
            return number-1
        if number<toguess:
            return number+1
        return True