'''Guess-the-number  Copyright (C) 2020  Shahibur Rahaman
This program comes with ABSOLUTELY NO WARRANTY.
'''

import random


def main():
    Guess().life()
    Guess().game()

class Guess:

    def __init__(self):
        self.start = start
        self.end = end
        self.lives = 0
        self.r = r
    
    def life(self):
        if self.r < 30:
            self.lives = 3
        elif self.r < 125:
            self.lives = 5
        elif self.r < 250:
            self.lives = 7
        elif self.r < 500:
            self.lives = 10
        elif self.r < 1000:
            self.lives = 13
        elif self.r < 2500:
            self.lives = 15
        elif self.r < 5000:
            self.lives = 18
        elif self.r < 10000:
            self.lives = 20
  
        return self.lives

    def game(self):
        for i in range(Guess().life()):
            print(f"\nREMAINING LIVES: [{Guess().life() - i}]")
            num = int(input("\nEnter your guess: "))
            if num < self.r:
                print("You are getting cold!\n")
            elif num > self.r:
                print("You are getting hot!\n")
            elif Guess().life() == 1:
                print("Better Luck next time! :P")
                print(f"The number was {self.r}")
            else:
                print("\nCongratulations! You have guessed the right number!\n")
                break
            
if __name__ == "__main__":
    while True:
        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))
        r = random.randint(start, end)
        main()
        NG = input("Do you want to play another match? [y/n] ")
        if NG == 'n' or NG == 'N':
            break
        else:
            continue
