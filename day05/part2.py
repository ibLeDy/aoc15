class StringChecker:
    def __init__(self, string):
        self.string = string

    def check_pair(self):
        for i, char in enumerate(self.string):
            try:
                if char + self.string[i + 1] in self.string[i + 2:]:
                    return True
            except IndexError:
                pass

    def check_between(self):
        for i, char in enumerate(self.string):
            try:
                if char == self.string[i + 2]:
                    return True
                elif char == self.string[i + 1]:
                    if char == self.string[i + 3] and char == self.string[i + 4]:
                        return True
            except IndexError:
                pass


with open('input.txt', 'r') as f:
    strings = f.read().splitlines()

nice_count = 0
for string in strings:
    checker = StringChecker(string)
    if checker.check_between():
        if checker.check_pair():
            nice_count += 1

print(nice_count)
