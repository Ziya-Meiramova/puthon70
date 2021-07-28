from string import ascii_uppercase, ascii_lowercase
class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print_let(self):
        for i in self.letters: #"ABCDE"
            print(i, end=" ")

    def letters_num(self):
        return len(self.letters)

al1 = Alphabet("RU", "АБСДЕ")
al1.print_let()
print(al1.letters_num())

class EngAlphabet(Alphabet):
    def __init__(self, lang, letters):
        super().__init__(lang, letters)
        self.counter = len(letters)
    def is_en_alpga(self, letter):

        for i in self.letters:
            if i == letter:
                return True

        return False
    @staticmethod
    def example():
        print("Hello")

al2 = EngAlphabet("En", ascii_lowercase + ascii_uppercase)
al2.print_let()
print(al2.letters_num())
print(al2.is_en_alpga("R"))