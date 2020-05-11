class Cat:
    def __init__(self):
        self.catname = "MEOW"

    def say_hello(self):
        return ('Hello '+self.catname)

    class Kitten:
        def __init__(self):
            self.kittenname = "KITTEN"
        def say_hello(self):
             return ('Hello '+self.kittenname)



k = Kitten()
print(k.say_hello())
