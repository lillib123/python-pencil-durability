import unittest
from paper import paper
from pencil import Pencil


class MyTestCase(unittest.TestCase):
    def setUp(self):
        paper.update({"text": ""})
        self.cool_pencil = Pencil(100, 20, 10)

    def test_something(self):
        self.assertEqual(True, True)

    def test_pencilWrites(self):
        self.cool_pencil.write("something")

        self.assertEqual("something", paper.get("text"))

    def test_paper_starts_with_no_writing(self):
        self.assertEqual("", paper.get("text"))

    def test_pencil_writes_to_paper(self):
        self.cool_pencil.write("going to the beach")
        self.assertEqual("going to the beach", paper.get("text"))

    def test_pencil_can_append_text_to_paper(self):
        self.cool_pencil.write("something1")
        self.cool_pencil.write("something2")

        self.assertEqual("something1something2", paper.get("text"))

    def test_durability_value_can_be_set_on_new_pencil(self):
        pencil_with_custom_durability_limit = Pencil(42, 20, 10)

        self.assertEqual(42, pencil_with_custom_durability_limit.durability)

    def test_durability_decreases_when_pencil_writes(self):
        self.cool_pencil.write("hello")

        self.assertEqual(95, self.cool_pencil.durability)

    def test_pencil_that_reaches_durability_limit_mid_word_will_add_spaces_for_remaining_characters(self):
        pencil_with_zero_durability_limit = Pencil(4, 20, 10)
        pencil_with_zero_durability_limit.write("words")

        self.assertEqual("word ", paper.get("text"))

    def test_pencil_is_dull_can_only_writes_space(self):
        dull_pencil = Pencil(0, 20, 10)
        dull_pencil.write("friday")

        self.assertEqual("      ", paper.get("text"))

    def test_pencil_can_write_spaces_without_decreasing_durability_limit(self):
        self.cool_pencil.write("one two")

        self.assertEqual(94, self.cool_pencil.durability)

    def test_pencil_decreases_by_two_when_writing_capital_letters(self):
        self.cool_pencil.write("Hey You")

        self.assertEqual(92, self.cool_pencil.durability)

    def test_pencil_sharpened_gains_points_durability(self):
        pencil_with_ten_durability_limit = Pencil(10, 20, 10)
        pencil_with_ten_durability_limit.write("hello")

        self.assertEqual(5, pencil_with_ten_durability_limit.durability)
        pencil_with_ten_durability_limit.sharpen()
        self.assertEqual(10, pencil_with_ten_durability_limit.durability)

    def test_durability_and_length_value_can_be_set_to_a_new_pencil(self):
        pencil_with_custom_durability_and_length = Pencil(10, 20, 10)

        self.assertEqual(10, pencil_with_custom_durability_and_length.durability)
        self.assertEqual(20, pencil_with_custom_durability_and_length.length)

    def test_pencil_length_decreases_by_one_when_sharpened(self):
        self.cool_pencil.sharpen()
        self.assertEqual(19, self.cool_pencil.length)

    def test_pencil_length_cannot_be_negative(self):
        pencil_with_zero_length = Pencil(10, 0, 10)
        pencil_with_zero_length.sharpen()

        self.assertEqual(0, pencil_with_zero_length.length)

    def test_pencil_durability_cannot_be_restored_when_the_length_is_zero(self):
        pencil_with_zero_length = Pencil(10, 0, 10)
        pencil_with_zero_length.write("hello")
        pencil_with_zero_length.sharpen()

        self.assertEqual(5, pencil_with_zero_length.durability)

    def test_pencil_can_erase_one_character_and_replace_with_space(self):
        self.cool_pencil.write("abcd")
        self.cool_pencil.erase("d")

        self.assertEqual("abc ", paper.get("text"))

    def test_pencil_can_erase_last_occurence_of_d_and_replace_with_space(self):
        self.cool_pencil.write("abcdabcd")
        self.cool_pencil.erase("d")

        self.assertEqual("abcdabc ", paper.get("text"))

    def test_pencil_can_erase_last_occurence_of_e_and_replace_with_space(self):
        self.cool_pencil.write("abcdeabcde")
        self.cool_pencil.erase("e")

        self.assertEqual("abcdeabcd ", paper.get("text"))

    def test_pencil_can_erase_last_occurence_of_e_and_replace_with_space(self):
        self.cool_pencil.write("abcdeabcdefg")
        self.cool_pencil.erase("e")

        self.assertEqual("abcdeabcd fg", paper.get("text"))

    def test_pencil_can_erase_last_occurence_text_and_replace_with_spaces(self):
        self.cool_pencil.write("helloworldhello")
        self.cool_pencil.erase("hello")

        self.assertEqual("helloworld     ", paper.get("text"))

    def test_pencil_can_be_created_with_eraser_durability(self):
        pencil_with_eraser = Pencil(0, 20, 10)

        self.assertEqual(10, pencil_with_eraser.eraser_durability)

    def test_pencil_eraser_durability_degrades_1_per_character_erased(self):
        pencil_with_eraser = Pencil(0, 20, 10)

        pencil_with_eraser.write('hello')
        pencil_with_eraser.erase('hello')

        self.assertEqual(5, pencil_with_eraser.eraser_durability)

    def test_eraser_durability_does_not_go_below_zero(self):
        pencil_with_eraser = Pencil(20, 20, 0)

        pencil_with_eraser.write('hello')
        pencil_with_eraser.erase('hello')

        self.assertEqual(0, pencil_with_eraser.eraser_durability)

    def test_pencil_will_stop_erasing_after_hitting_durability_limit(self):
        pencil_with_eraser = Pencil(20, 20, 3)

        pencil_with_eraser.write('hello')
        pencil_with_eraser.erase('hello')

        self.assertEqual('he   ', paper.get("text"))

    def test_spaces_should_not_degrade_eraser(self):
        self.cool_pencil.write("     ")
        self.cool_pencil.erase("     ")

        self.assertEqual(10, self.cool_pencil.eraser_durability)

    def test_erase_can_also_replace_white_space(self):
        self.cool_pencil.write("goodbye")
        self.cool_pencil.erase("good", "bad")

        self.assertEqual("bad bye", paper.get("text"))

    def test_overlapping_replacement_text_will_replace_with_at_symbol(self):
        self.cool_pencil.write("goodbye")
        self.cool_pencil.erase("good", "goodpie")

        self.assertEqual("good@@@", paper.get("text"))


if __name__ == '__main__':
    unittest.main()
    print("Everything passed")
