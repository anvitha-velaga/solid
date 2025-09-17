
class FlyinBird():
    def fly(self):
        print("bird flies")
class sparrow(FlyinBird):
    def fly(self):
        print("sparrow flies")
s:FlyinBird=sparrow()
s.fly()
