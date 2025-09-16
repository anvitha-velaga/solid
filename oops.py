#creating a class
#class Anvitha:
  # print("hello anvitha!")
#creating object
#class Student:

   # def display_info(self):
       # name=input("enter your name:")
        #marks=int(input("enter your marks:"))
        #print(f"hi {name}")
        #print(f"you scored{marks}")
#s=Student() #object
#s.display_info()
#encapsulation
'''class Student:
    def __init__(self,name,id,marks):
        self.name=name #public
        self._id=id #protected
        self.__marks=marks #private
    def get_marks(self): #to get/print marks
        return self.__marks
    def set_marks(self,new_marks): #to update marks
        self.__marks=new_marks #private var cant be accessed directly
        if new_marks>=90:
            print("A")
        elif new_marks>=80:
            print('B')
        elif new_marks>=70:
            print('C')
        elif new_marks >=60:
            print('D')
        else:
            print('F')
s=Student("anvi",33,80)
s.set_marks(90)
s.get_marks()'''
'''class overriding:

    def add(self,a,b):
        self.a=a
        self.b=b
        sum= a+b
        print(f"sum is {sum}")
o=overriding()
o.add(3,4)
o.add(1.2,3.3) #add function behaves diff based on args passed'''

'''class overloading:
    def add(self,*args): #*args is used to achieve overloading
        c=sum(args)
        print(f"sum is {c}")
o=overloading()
o.add(1,2,3,4,4,4,4,4,4)
o.add(1.2,3.3,7.9)'''
#inheritence
class Animal:
    def walks(self):
        print("Animals walk")
class Tiger(Animal):
    def walks(self):
        print("walks")
t=Tiger()
t.walks() #single-inheritence
class Mother: #multiple
    def hobbies(self):
        print("hobbies of mom are:cooking,watchin tv")
class Father:
    def activites(self):
        print("father's fav actitivites to do are racing,cooking")
class Child(Mother,Father):
    def self(self):
        print("his own self int are drawing,playing")
c=Child()
c.self()
class Livinbeing: #multilevel
    def breathes(self):
        print("livin beings breathe")
class Animal(Livinbeing):
    def walks(self):
        print("animals walk")
class Tiger(Animal):
    def fourlegged(self):
        print("four legged animal")
t=Tiger()
t.walks()
t.breathes()
t.fourlegged()






    
