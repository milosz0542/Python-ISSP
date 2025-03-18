class ThreeElements:
    def __init__(self, n):
        self.n = n

    def findZero(self):
        triplets = []
        self.n.sort()
        for i in range(len(self.n) - 2):
            if i > 0 and self.n[i] == self.n[i - 1]:
                continue
            left, right = self.n[i+1], self.n[-1]
            while left < right:
                total = self.n[i] + self.n[left] + self.n[right]
                if total == 0:
                    triplets.append([self.n[i], self.n[left], self.n[right]])
                    while left < right and self.n[left] == self.n[left + 1]:
                        left += 1
                    while left < right and self.n[right] == self.n[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return triplets

input_list = [-1, 0, 1, 2, -1, -4]
three_elements = ThreeElements(input_list)
print(three_elements.findZero())