import operator
import random
import json
import datetime

secret = random.randint(1, 30)
player_name = input("Write your name: ")
attempts = 0
score_dict = 0
wrong = []

with open("h11_1_2_3.json", "r") as score_file:
    score_list = json.loads(score_file.read())

    for score_dict in sorted(score_list, key=lambda item: item['attempts']):
        print(f"Player name {score_dict['player']}, secret number {score_dict['secret number']}, {score_dict['attempts']} attempts, wrong attempts were {score_dict['wrong_attempts']}, date: {score_dict.get('date')}")

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        score_data = {"player": player_name, "secret number": secret, "attempts": attempts, "wrong_attempts": wrong, "date": str(datetime.datetime.now())}
        score_list.append(score_data)
        with open("h11_1_2_3.json", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

    wrong.append(guess)
