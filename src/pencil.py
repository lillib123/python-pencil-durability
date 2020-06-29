from paper import paper
import re


class Pencil:
    def __init__(self, durability, length, eraser_durability):
        self.durability = durability
        self.initial_durability = durability
        self.length = length
        self.eraser_durability = eraser_durability

    def write(self, text):
        for i in range(len(text)):
            current_character = text[i]
            if self.durability > 0:
                self.update_paper(current_character)
                if current_character.isupper():
                    self.durability -= 2
                elif current_character.islower():
                    self.durability -= 1
            else:
                self.update_paper(" ")

    @staticmethod
    def update_paper(character):
        paper.update({"text": paper.get("text") + character})

    def sharpen(self):
        if self.length > 0:
            self.length -= 1
            self.durability = self.initial_durability

    def erase(self, text):
        for i in range(len(text)):
            current_character = text[::-1][i]
            if self.eraser_durability > 0 and current_character != " ":
                replacement_text = re.sub(r"" + current_character + "(?!.*" + current_character + ")", " ", paper.get("text"))
                paper.update({"text": replacement_text})
                self.eraser_durability -= 1
