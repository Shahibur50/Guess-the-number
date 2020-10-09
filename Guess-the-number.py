'''
Guess-the-number  Copyright (C) 2020  Shahibur Rahaman
This program comes with ABSOLUTELY NO WARRANTY.
'''

import random


def main():
    Guess().life()
    Guess().game()

class Guess():
    def __init__(self):
        self.start = start
        self.end = end
        self.r = random.randint(start, end)
    
    def life(self):
        if self.end - self.start < 30:
            self.lives = 3
        elif self.end - self.start < 125:
            self.lives = 5
        elif self.end - self.start < 250:
            self.lives = 7
        elif self.end - self.start < 500:
            self.lives = 10
        elif self.end - self.start < 1000:
            self.lives = 13
        elif self.end - self.start < 2500:
            self.lives = 15
        elif self.end - self.start < 5000:
            self.lives = 18
        elif self.end - self.start < 10000:
            self.lives = 20  
        return self.lives

    def game(self):
        for i in range(Guess().life()):
            lives = Guess().life() - i
            print(f"\nREMAINING LIVES: [{lives}]")
            while True:
                try:
                    num = int(input("\nEnter your guess: "))
                except ValueError:
                    print("Please enter only numerical values.")
                else:
                    break
            if num == self.r:
                print("\nCongratulations! You have guessed the right number!\n")
                break
            elif lives == 1:
                print("Better Luck next time! :P")
                print(f"The number was {self.r}")
            elif num < self.r:
                print("You are getting cold!\n")
            elif num > self.r:
                print("You are getting hot!\n")
            
            
            
if __name__ == "__main__":
    while True:
        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))
        main()
        NG = input("Do you want to play another match? [y/n] ")
        if NG == 'n' or NG == 'N':
            break
        else:
            continue
