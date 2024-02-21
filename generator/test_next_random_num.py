import unittest
from collections import Counter
from random_num import RandomGen


class TestRandomGen(unittest.TestCase):

    def test_probabilities_respected_in_results(self):
        generator = RandomGen()
        probabilities = generator._probabilities
        values_set = generator._random_nums
        iterations = (len(values_set) * int(100 / min(probabilities)))
        generated_nums = [generator.next_num() for _ in range(iterations + 1)]
        count = dict(Counter(generated_nums).items())
        for index, probability in enumerate(probabilities):
            result_av = count[values_set[index]] / iterations
            self.assertAlmostEqual(result_av,
                                   probability,
                                   places=2,
                                   msg=f"Probability ({result_av}) does not match"
                                       f" expected probability ({probability}).")

    def test_generator_values_are_in_valid_values_set(self):
        generator = RandomGen()
        probabilities = generator._probabilities
        values_set = generator._random_nums
        iterations = (len(values_set) * int(10 / min(probabilities)))

        for i in range(iterations + 1):
            num = generator.next_num()
            self.assertTrue(num in values_set)


if __name__ == "__main__":
    unittest.main()
