from paper import paper


class Pencil:
    def __init__(self, durability):
        self.durability = durability

    def write(self, text):
        for i in range(len(text)):
            currentCharacter = text[i]
            if self.durability > 0:
                self.writeToPaper(currentCharacter)
                if currentCharacter.isupper():
                    self.durability -= 2
                elif currentCharacter.islower():
                    self.durability -= 1
            else:
                self.writeToPaper(" ")

    def writeToPaper(self, character):
        paper.update({"text": paper.get("text") + character})


