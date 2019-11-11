import random
import datetime


class Result():
    def __init__(self, attempts, player_name, date):
        self.attempts = attempts
        self.player_name = player_name
        self.date = date


secret = random.randint(1, 25)

attempts = 0
while True:
    guess = int(input("Guess the number (between 1 and 25): "))
    attempts += 1
    if guess == secret:
        print("Congratulations, you got the right number! It's number " + str(secret))
        break
    elif guess > secret:
        print("Try something smaller")
    elif guess < secret:
        print("Try something bigger")
    else:
        print("Oh no, that's not the right number. Sorry!")


name = input("Enter your Name: ")
date_game = datetime.datetime.now().strftime("%d.%m.%y, %T")

scorelist = Result(attempts=attempts, player_name=name, date=date_game)

with open("results.txt", "a") as score_file:
    score_file.write("\n")
    score_file.write(str(scorelist.__dict__))

print("Score successfully entered.")
print("Player's data: {0}".format(scorelist.__dict__))
