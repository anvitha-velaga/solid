class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age #protected
        self._email="hi@.com" #private
    def get_age(self):
        return self.__age
    def set_age(self,new_age):
        if new_age>0:
            self.__age=new_age
p=Person()
p.set_age(30)
print(p.get_age())

        

    