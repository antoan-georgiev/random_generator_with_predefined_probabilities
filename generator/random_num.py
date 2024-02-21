from random import choices


class RandomGen(object):

    def __init__(self):
        self._probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]
        self._random_nums = [-1, 0, 1, 2, 3]

    def next_num(self):
        """
        Returns one of the randomNums. When this method is called multiple
        times over a long period, it should return the numbers roughly with
        the initialized probabilities.
        """
        return choices(self._random_nums, self._probabilities, k=1)[0]
