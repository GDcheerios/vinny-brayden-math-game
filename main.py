import config
from player import Player
from math_question import MathQuestion

from tabulate import tabulate
import time

def clear():
    for i in range(25):
        print("\n")

for i in range(config.rounds):
    clear()
    round = i + 1

    player: Player
    for player in config.players:
        clear()
        print(f"round {round}/{config.rounds}\t{player.name}'s turn")
        question = MathQuestion.create(player.difficulty)
        start = time.time()
        is_correct = question.check(input(f'{question} = '))
        end = time.time()
        duration = end-start
        duration_score = 0
        if duration <= 1:
            duration_score += 300

        if duration <= 2:
            duration_score += 100

        if duration <= 3:
            duration_score += 50

        if is_correct:
            print("Correct!")
            player.add_combo()
            score = (100 + duration_score) * ((question.difficulty + 1) * player.combo)
            player.score += score

            print(tabulate([[
                score,
                question.difficulty + 1,
                duration_score,
                f'x{player.combo}'
            ]], headers=['total', 'difficulty', 'time buff', 'combo']))

        else:
            print(f"Incorrect!\nThe answer is: {question.answer}")
            player.combo = 0
            player.incorrect_count += 1

        input("Press enter to continue...")
        clear()

    table = []
    for player in config.players:
        table.append(player.get_scoreboard_info())

    print(tabulate(table, headers=
                   [
                   'name',
                   'score',
                   'incorrect count',
                   'combo',
                   'max combo',
                   'difficulty'
                   ]))

    input("Press enter to continue...")
