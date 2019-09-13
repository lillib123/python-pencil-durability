import unittest
from paper import paper
from pencil import Pencil


class MyTestCase(unittest.TestCase):
    def setUp(self):
        paper.update({"text": ""})
        self.coolPencil = Pencil(100)

    def test_something(self):
        self.assertEqual(True, True)

    def test_pencilWrites(self):
        self.coolPencil.write("something")

        self.assertEqual("something", paper.get("text"))

    def test_paper_starts_with_no_writing(self):
        self.assertEqual("", paper.get("text"))

    def test_pencil_writes_to_paper(self):
        self.coolPencil.write("going to the beach")
        self.assertEqual("going to the beach", paper.get("text"))

    def test_pencil_can_append_text_to_paper(self):
        self.coolPencil.write("something1")
        self.coolPencil.write("something2")

        self.assertEqual("something1something2", paper.get("text"))

    def test_durability_value_can_be_set_on_new_pencil(self):
        pencilWithCustomDurabilityLimit = Pencil(42)

        self.assertEqual(42, pencilWithCustomDurabilityLimit.durability)

    def test_durability_decreases_when_pencil_writes(self):
        self.coolPencil.write("hello")

        self.assertEqual(95, self.coolPencil.durability)

    def test_pencil_that_reaches_durability_limit_mid_word_will_add_spaces_for_remaining_characters(self):
        pencilWithZeroDurabilityLimit = Pencil(4)
        pencilWithZeroDurabilityLimit.write("words")

        self.assertEqual("word ", paper.get("text"))

    def test_pencil_is_dull_can_only_writes_space(self):
            dullPencil = Pencil(0)
            dullPencil.write("friday")

            self.assertEqual("      ", paper.get("text"))

    def test_pencil_can_write_spaces_without_decreasing_durability_limit(self):
        self.coolPencil.write("one two")

        self.assertEqual(94, self.coolPencil.durability)

    def test_pencil_decreases_by_two_when_writing_capital_letters(self):
        self.coolPencil.write("Hey You")

        self.assertEqual(92, self.coolPencil.durability)


if __name__ == '__main__':
    unittest.main()
    print("Everything passed")
