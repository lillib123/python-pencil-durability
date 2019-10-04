from paper import paper


class Pencil:
    def __init__(self, durability, length):
        self.durability = durability
        self.initial_durability = durability
        self.length = length

    def write(self, text):
        for i in range(len(text)):
            current_character = text[i]
            if self.durability > 0:
                self.write_to_paper(current_character)
                if current_character.isupper():
                    self.durability -= 2
                elif current_character.islower():
                    self.durability -= 1
            else:
                self.write_to_paper(" ")

    def write_to_paper(self, character):
        paper.update({"text": paper.get("text") + character})

    def sharpen(self):
        if self.length > 0:
            self.length -= 1
            self.durability = self.initial_durability


