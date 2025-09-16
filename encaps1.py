class Student:
    def student_info(self,name,id,marks):
        self.name=name
        self._id=id
        self.__marks=marks
    def get_marks(self):
        return self.__marks
    def set_marks(self,new_marks):
        if new_marks>0:
            self.__marks=new_marks
s=Student()
s.set_marks(100)
print(s.get_marks())

