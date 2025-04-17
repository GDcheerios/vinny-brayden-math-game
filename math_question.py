import random
import config

operators = [
    "+",
    "-",
    "*",
    "/",
    "%",
    "**"
]

class MathQuestion:
    difficulty: float = 0
    answer: int = 0
    problem: str = "0 + 0"


    def __init__(
        self,
        problem: str = "0 + 0",
        difficulty: int = 0,
        answer: int = 0
    ) -> None:
        self.problem = problem
        self.difficulty = difficulty
        self.answer = answer

    @staticmethod
    def generate_problem() -> tuple:
        return (
            random.randint(config.number_range[0], config.number_range[1]),
            random.randint(config.number_range[0], config.number_range[1])
        )

    @staticmethod
    def create(diff: int) -> 'MathQuestion':
        problem = MathQuestion.generate_problem()

        operator = operators[random.randint(0, diff)]
        difficulty = operators.index(operator)
        if operator == "+":
            difficulty += problem[0] * 0.01
            difficulty += problem[1] * 0.01

            if problem[0] % 2 == 1:
                difficulty += 0.25
            if problem[1] % 2 == 1:
                difficulty += 0.25

        elif operator == "-":
            difficulty += 0.5 if problem[0] < problem[1] else 0

        elif operator == "*":
            difficulty += (problem[0] * problem[1]) * 0.01

        elif operator == "/":
            while (problem[0] * problem[1] == 0) or (problem[0] % problem[1] != 0) or (problem[0] < problem[1]):
                problem = MathQuestion.generate_problem()

        elif operator == "%":
            while (problem[0] * problem[1] == 0):
                problem = MathQuestion.generate_problem()

        else:
            difficulty += problem[0] * 0.05
            difficulty += problem[1]


        

        problem=f"{problem[0]} {operator} {problem[1]}"

        return MathQuestion(
            problem=problem,
            difficulty=difficulty,
            answer=eval(problem)
        )

    def check(self, result: str) -> bool:
        try:
            result = int(result)

            return result == self.answer
        except ValueError:
            return False

    def __repr__(self) -> str:
        return self.problem

