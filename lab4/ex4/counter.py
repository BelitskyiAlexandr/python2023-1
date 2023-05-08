class Counter:
    def __init__(self, start_value=0, lower_limit=0, upper_limit=10):
        self.start_value = start_value
        self.current_value = start_value
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit

    def initialize(self, start_value, lower_limit, upper_limit):
        self.start_value = start_value
        self.current_value = start_value
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit

    def increase(self, step=1):
        new_value = self.current_value + step
        if new_value <= self.upper_limit:
            self.current_value = new_value
            return self.current_value
        else:
            return f"Counter can't go higher than {self.upper_limit}"

    def decrease(self, step=1):
        new_value = self.current_value - step
        if new_value >= self.lower_limit:
            self.current_value = new_value
            return self.current_value
        else:
            return f"Counter can't go lower than {self.lower_limit}"
        

#default values
print('\n---Default values---')
my_counter = Counter()
print(f"Start value: {my_counter.start_value}")
print(f"Lower limit: {my_counter.lower_limit}")
print(f"Upper limit: {my_counter.upper_limit}")

#more upper
print('\n---More than upper value---')
for i in range(15):
    value = my_counter.increase()
    if type(value) == str:
        print(value)
        break
    print(value)


#negative lower 
print('\n---Lower limit under 0---')
my_counter.initialize(start_value=5, lower_limit=-10, upper_limit=20)
print(f"Start value: {my_counter.start_value}")
print(f"Lower limit: {my_counter.lower_limit}")
print(f"Upper limit: {my_counter.upper_limit}")

for i in range(25):
    value = my_counter.decrease()
    if type(value) == str:
        print(value)
        break
    print(value)

