class Walking:
    def walk(self):
        print("walking")
class flying:
    def fly(self):
        print("flying")
class dog(Walking):
    pass
class bird(flying):
    pass
d=dog()
d.walk()