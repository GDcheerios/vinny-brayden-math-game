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
    difficulty: int = 0
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
    def generate_answer() -> tuple:
        return (
            random.randint(config.number_range[0], config.number_range[1]),
            random.randint(config.number_range[0], config.number_range[1])
        )

    @staticmethod
    def create(diff: int) -> 'MathQuestion':
        problem = MathQuestion.generate_answer()

        operator = operators[random.randint(0, diff)]
        if operator == "/":
            while (problem[0] * problem[1] == 0) or (problem[0] % problem[1] != 0) or (problem[0] < problem[1]):
                problem = MathQuestion.generate_answer()

        elif operator == "%":
            while (problem[0] * problem[1] == 0):
                problem = MathQuestion.generate_answer()

        problem=f"{problem[0]} {operator} {problem[1]}"

        return MathQuestion(
            problem=problem,
            difficulty=operators.index(operator),
            answer=eval(problem)
        )

    def check(self, result: str) -> bool:
        result = int(result)

        return result == self.answer

    def __repr__(self) -> str:
        return self.problem

