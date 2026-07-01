from typing import Any


class Game:

    def guess(self, guessNumber):
        self._assert_illegal_value(guessNumber)

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
