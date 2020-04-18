from collections import Counter


class StringChecker:
    def __init__(self, string):
        self.string = string

    def check_excluded(self):
        return not any(exc in self.string for exc in excluded)

    def check_vowels(self):
        count = Counter(self.string)
        vowel_count = 0
        for vowel in vowels:
            vowel_count += count[vowel]

        if vowel_count >= 3:
            return True

    def check_twice(self):
        twice_count = 0
        for i, char in enumerate(self.string):
            try:
                if char == self.string[i + 1]:
                    twice_count += 1
            except IndexError:
                pass

        if twice_count >= 1:
            return True


with open('input.txt', 'r') as f:
    strings = f.read().splitlines()

vowels = ['a', 'e', 'i', 'o', 'u']
excluded = ['ab', 'cd', 'pq', 'xy']

nice_count = 0
for string in strings:
    checker = StringChecker(string)
    if checker.check_excluded():
        if checker.check_vowels():
            if checker.check_twice():
                nice_count += 1

print(nice_count)
