from itertools import combinations

class ListPermutations:
    def __init__(self, n):
        self.n = n

    def permutations(self):
        subsets = []
        for i in range(len(self.n) + 1):
            subsets.extend(combinations(self.n, i))
        return[list(subset) for subset in subsets]

input_list = [1, 2, 3]
list_subsets = ListPermutations(input_list)
print(list_subsets.permutations())
