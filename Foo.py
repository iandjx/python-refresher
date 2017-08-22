class Foo():
    def __init__(self, one):
        self.one = one

    @classmethod
    def new_foo(cls, origin, two,three):
        return cls(origin.one, two, three)

foo = Foo(2)
print(foo.one)

class Bar(Foo):
    def __init__(self, one, two):
        super().__init__(one)
        self.two = two

bar = Bar(2,3)

isol = Foo.new_foo(bar, 41, 312)
print(isol.one)
