class Employee:
    def details_employee(self,name_of_employee,age_of_employee,role_of_employee,salary_of_employee):
        self.name_of_employee=name_of_employee
        self._age_of_employee=age_of_employee
        self.role_of_employee=role_of_employee
        self.__salary_of_employee=salary_of_employee
    def get_salary_of_employee(self):
        return self.__salary_of_employee
    def set_salary_of_employee(self,new_sal):
        if new_sal>0:
            self.__salary_of_employee=new_sal

e=Employee()

e.set_salary_of_employee(50000)
print(e.get_salary_of_employee())



