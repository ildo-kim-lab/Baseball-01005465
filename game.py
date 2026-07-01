from typing import Any

import game_result
from game_result import GameResult

class Game:
    def __init__(self):
        self._questions = ""

    @property
    def questions(self):
        raise AttributeError("Did not Readable")

    @questions.setter
    def questions(self, value):
        self._questions = value

    def guess(self, guess_number) -> GameResult | None:
        self._assert_illegal_value(guess_number)
        if guess_number == self._questions:
            return GameResult(True, 3, 0)
        return None

    def _assert_illegal_value(self, guessNumber: str):
        if guessNumber is None:
            raise TypeError("입력이 None입니다.")

        if len(guessNumber) != 3:
            raise TypeError("입력은 3제리 문자열 이어야 합니다.")

        if not guessNumber.isdigit():
            raise TypeError("모든 문자는 숫자로 구성되어야 합니다.")

        if self._isDuplicatedNumber(guessNumber):
            raise TypeError("중복된 숫자가 존재합니다.")

    def _isDuplicatedNumber(self, guessNumber) -> Any:
        return guessNumber[0] == guessNumber[1] or \
            guessNumber[1] == guessNumber[2] or \
            guessNumber[0] == guessNumber[2]
