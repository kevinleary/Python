class Employee():
    #constructor to initialize the object
    def __init__(self,name,salary,phone):
        self.__name = name
        self.__base_salary = salary
        self.__phone_number = phone

    #getter for name
    def get_name(self):
        return self.__name

    #getter for number
    def get_number(self):
        return self.__phone_number

    #mutator function for salary
    def mutator(self,end_salary):
        self.__base_salary = end_salary

    #calculates the total
    def salary_total(self):  
       return self.__base_salary

    #to make the infor a string 
    def __str__(self):
        return "Employee({}), {}, {}".format(self.__name,self.__phone_number,self.salary_total())

    def __repr__(self):
        return self.__str__
    
        
class Manager(Employee):
    #manger class works off of the employee class
    #constuctor for this class object
    def __init__(self, name, salary, phone,bonus):
        super().__init__(name,salary,phone)
        self.__bonus=bonus

    def salary_total(self):
        return super().salary_total()+self.__bonus
    
        
class Engineer(Employee):
    #engineer class works off the employee class

    def __init__(self,name,salary,phone):
        super().__init__(name,salary,phone)
        
        
class CEO(Manager):

    #ceo object funtions like a manager

    def __init__(self,name,base_salary,phone,bonus,stock):
        super().__init__(name,base_salary,phone,bonus)
        self.__stock_options=stock

    def salary_total(self):
        return super().salary_total()+self.__stock_options
    
#function for printing the objct
def print_staff(staff):
    for i in staff:
        print(i)
        
#initalize objects then print them to terminal
employee = Employee("Jayson Tatum", 100000, "1-800-932-0987")
engineer = Engineer("Marcus Smart", 12000000, "973-219-0441")
manager = Manager("Bob Roland", 40000, "286-813-9712", 5000)
ceo = CEO("Kevin Leary", 12000000, "000-000-0001", 55000, 78000)
              
result = [employee, engineer, manager, ceo]

print_staff(result)
   
    