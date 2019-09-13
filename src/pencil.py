from paper import paper


class Pencil:
    def __init__(self, durability):
        self.durability = durability

    def write(self, text):
        hi = paper.get("text") + text
        paper.update({"text": hi})

        self.durability -= len(text)
