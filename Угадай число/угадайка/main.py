class Cat:
    def __init__(self, name):
        self.name = name

    def say_mue(self):
        return 'mue'


tom = Cat('Tom')

print(tom.name)
tom.name = 'Alex'

print(tom.name)