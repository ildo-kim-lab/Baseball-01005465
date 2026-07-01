class Game:

    def guess(self, guessNumber):
        if guessNumber is None:
            raise TypeError()
        if len(guessNumber) != 3:
            raise TypeError()

        for num in guessNumber:
            if not ord('0') <= ord(num) <= ord('9'):
                raise TypeError()
