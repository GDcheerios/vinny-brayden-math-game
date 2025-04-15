class Player:
    id = 1

    name: str = f"Player{id}"
    score: int = 0
    incorrect_count: int = 0
    combo: int = 0
    max_combo: int = 0
    difficulty: int = 1

    def __init__(
        self,
        name: str,
        score: int = 0,
        incorrect_count: int = 0,
        combo: int = 0,
        max_combo: int = 0,
        difficulty: int = 1
    ) -> None:
        Player.id += 1

        self.name = name
        self.score = score
        self.incorrect_count = incorrect_count
        self.combo = combo
        self.max_combo = max_combo
        self.difficulty = difficulty

    def add_combo(self) -> None:
        self.combo += 1
        if self.combo > self.max_combo:
            self.max_combo = self.combo

    def get_scoreboard_info(self) -> list:
        return [
            self.name,
            f"{self.score:,}",
            self.incorrect_count,
            self.combo,
            self.max_combo,
            self.difficulty
        ]
