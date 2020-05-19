import unittest
from random import randint

from TeamGenerator import TeamGenerator


class test_TeamGenerator(unittest.TestCase):
    def setUp(self):
        self.orchestrator = TeamGenerator()

    def test_read_input_file(self):
        expected = ["Matt", "Marco", "Vasu"]
        self.assertEqual(self.orchestrator.read_input_file("input.csv"), expected)

    def test_append_with_random_number(self):
        list_of_names = ["Matt", "Marco", "Vasu"]
        expected_range = range(1, 3)
        self.assertIn(
            int(self.orchestrator.append_with_random_number(list_of_names)[0][-1]),
            expected_range,
        )


if __name__ == "__main__":
    unittest.main()
