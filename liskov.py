class Bird:
    pass
class FlyinBird(Bird):
    def fly(self):
        print("bird flies")
class sparrow(FlyinBird):
    def flying(self):
        print("sparrow flies")
s=sparrow()
s.flying()
