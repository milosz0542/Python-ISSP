class CiagFibonacciego:
    def __new__(cls, *args, **kwargs):
        if len(args) != 2:
            raise ValueError("Podano złą ilość argumentów")
        return super().__new__(cls)
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2
        self.ciag = [a1, a2]

    def new_element(self):
        self.ciag.append(self.ciag[-1] + self.ciag[-2])

    def __str__(self):
        return str(self.ciag)

if __name__ == '__main__':
    a1 = int(input("Podaj pierwszy element ciągu: "))
    a2 = int(input("Podaj drugi element ciągu: "))

    ciag = CiagFibonacciego(a1, a2)

    while True:
        prompt = input("Czy chcesz dodać nowy element do ciągu? (t/n): ")
        if prompt == "t" or prompt == "T":
            ciag.new_element()
            print(ciag)
        else:
            break