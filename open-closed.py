class Discount:
    def getdiscount(self):
        return 0
class StudentDiscount(Discount):
    def getdiscount(self):
        print("discount avalid is 20%")
class EmployeeDiscount(Discount):
    def getdiscount(self):
        print("discount avalid is 30%")
s=StudentDiscount()
s.getdiscount()
