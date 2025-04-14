import random
from tabulate import tabulate

mode_faster_response = False
rounds = 11
players = {}
player_combo = {}
player_incorrect = {}
min_number = 1
max_number = 10
operators = [
    "+", # addition
    "-", # subtraction
    "*", # multiplication
    # "/", # division
    "%"  # mod
]

def create_user(name: str) -> None:
    players[name] = 0
    player_combo[name] = 0
    player_incorrect[name] = 0


if not mode_faster_response:
    while True:
        response = input('Enter a name: ')
        if response == 'done':
            break
        
        create_user(response)


def give_answer(numbers: tuple, operator: str) -> dict:
    if operator == "+":
        answer = numbers[0] + numbers[1] 
        difficulty = 1
    elif operator == "-":
        answer = numbers[0] - numbers[1]
        difficulty = 1
    elif operator == "*":
        answer = numbers[0] * numbers[1]
        difficulty = 2
    elif operator == "/":
        answer = numbers[0] / numbers[1]
        difficulty = 3
    elif operator == "%":
        answer = numbers[0] % numbers[1]
        difficulty = 4

    return {
        "answer": answer,
        "difficulty": difficulty
    }

def get_numbers() -> tuple:
    return (random.randint(min_number, max_number),
            random.randint(min_number, max_number))

def clear_screen() -> None:
    for _ in range(50):
        print("\n")


def scoreboard() -> None:
    table = []
    for name, score in players.items():
        table.append([name, f'{score:,}', player_incorrect[name], player_combo[name]])

    print(tabulate(table, headers=["name", "score", "incorrect count", "current combo"]))


for i in range(rounds):
    if not mode_faster_response:
        for user in players.keys():
            clear_screen()
            numbers = get_numbers()
            operator = random.choice(operators)
            answer = give_answer(numbers, operator)
            print(
                f"""
                Round {i + 1}/{rounds}
                {user}'s turn
    
                What's the answer for
                {numbers[0]} {operator} {numbers[1]}
                """
            )
            response = input("answer: ")
            if int(response) == answer['answer']:
                print("correct!")
                player_combo[user] += 1
                players[user] += (answer['difficulty'] * player_combo[user]) * (i + 1)
            else:
                print("incorrect")
                player_combo[user] = 0
                player_incorrect[user] += 1

            input("\nPress enter to continue...")
    else:
        clear_screen()
        numbers = get_numbers()
        operator = random.choice(operators)
        answer = give_answer(numbers, operator)

        print(
            f"""
            Round {i + 1}/{rounds}
    
            What's the answer for
            {numbers[0]} {operator} {numbers[1]}
            """
        )

        response = input("answer: ")
        user = input("Who answered this?\nEnter name: ")
        if players.get(user) == None:
            create_user(user)

        if int(response) == answer['answer']:
            print("correct!")
            player_combo[user] += 1
            players[user] += (answer['difficulty'] * player_combo[user]) * (i + 1)
            players[user] += answer['difficulty'] * player_combo[user]
        else:
            print("incorrect")
            player_combo[user] = 0
            player_incorrect[user] += 1

    print(f"\nthe answer is: {answer['answer']}")

    scoreboard()
    input("press enter to continue")

clear_screen()
print("final results")
scoreboard()
