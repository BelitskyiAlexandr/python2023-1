class UpperString:
    def __init__(self):
        self.string = ""

    def get_string(self):
        self.string = input("Введіть рядок: ")

    def print_upper_string(self):
        print(self.string.upper())

my_string = UpperString()
my_string.get_string()
my_string.print_upper_string()
