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
            else:
                self.update_paper(" ")
            self.degrade_pencil(current_character)

    def degrade_pencil(self, character):
        if character.isupper():
            self.durability -= 2
        elif character.islower():
            self.durability -= 1

    @staticmethod
    def update_paper(character):
        paper.update({"text": paper.get("text") + character})

    def sharpen(self):
        if self.length > 0:
            self.length -= 1
            self.durability = self.initial_durability

    def erase(self, erase_text, new_text=""):
        replacement_index = 0

        if re.search(r"" + erase_text + "(?!.*" + erase_text + ")", paper.get("text")):
            replacement_index = re.search(r"" + erase_text + "(?!.*" + erase_text + ")", paper.get("text")).start()

        for i in range(len(erase_text)):
            current_character = erase_text[::-1][i]
            if self.eraser_durability > 0 and current_character != " ":
                replacement_text = re.sub(r"" + current_character + "(?!.*" + current_character + ")", " ", paper.get("text"))
                paper.update({"text": replacement_text})
                self.eraser_durability -= 1

        for i in range(len(new_text)):
            replacement_character = new_text[i]
            if paper.get("text")[replacement_index] != " ":
                replacement_character = "@"
            if self.durability > 0:
                replacement_text = paper.get("text")[:replacement_index] + replacement_character + paper.get("text")[replacement_index + 1:]
                paper.update({"text": replacement_text})
                replacement_index += 1
                self.degrade_pencil(replacement_character)

