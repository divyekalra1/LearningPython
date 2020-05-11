# import math
# name = input("What is your name? ")
#
# mystring = f'''Hey , this is Samuel I heard about your promotion to senior vice president of the company.
# Congrats man. My favourite color is  as well !!!!'''    #'''......''' is used to define a multi line string, or strings in which both '...' and "..." are used.
# print(mystring)
# print(len(mystring))    #can be used to calculate the number of entries in a dictionary, list, etc as well.
# my_string = "This is a STRING"
# print(my_string.capitalize())   #capitalizes only the first character of the string. All the other characters in the string are converted to lowercase.
# print(my_string.replace('is','IS'))   #Syntax string_name.replace(old_string_to_find, new_string,count) -- count is the number of occurences it has to replace.
#                                     # Default is all occurences
# print('is' in my_string)    #expression returns a boolean value
# print(my_string.find('i'))  #returns index value of the first occurence of the character 'i' in the string.
# print(math.floor(2.9))
#
#
# mytuple = ([1,2,3],[4,5,6],[7,8,9])
# mytuple[1][2] = 97  #the tuple elements are themselves not mutable, but the elements of a list which is a part of a tuple are mutable
# # mytuple[0] = 4 is not allowed
# # mytuple[0][1] = 7 #However, this is allowed.
# print(mytuple[1][2])
#
# a_tuple = (7,8,9) #let the tuple elements be a set of coordinates in the coordinate system.
# x,y,z = a_tuple #short-hand notation to unpack a tuple or a list and assign the elements to seperate variables.
# print(x,y,z)
#
#     #OOPS

class Employee: #Regular methods in a class by default take the instance as a parameter (self/any other name).

    raise_amount = 1.04 #giving employees a raise of 4%. This variable is called a class variable.
                        #It can only be accessed using an instance of the class, or the class itself.
                        #However, an instance of the class does not itself have its own copy of the class variable. It checks if the class variable is a part of the class it is
                        # an instance of, or any other class it has been inherited from.
    def __init__(self,pay,first,last): #init is a built in magic/dunder method,that basically acts like a constructor. It is called when a class instance is declared.
                                 #self parameter takes the instance of the class. Not like in C++ where the compiler automatically knows which instance's attribute we want to refer to.
        self.salary = pay
        self.firstname = first
        self.lastname = last

    def details(self):
        print("Name of the Employee : " + self.firstname + " " + self.lastname)
        print(f"Salary of the Employee : {self.salary}")

    def raise_salary(self):
        self.salary *= self.raise_amount #or self.salary *= Employee.raise_amount
                                         #it is a good practice to use self instead of Employee to reference a class variable, since the class variable can later be modified
                                         #for a particular instance of the class as shown in lines 81-89.
    @classmethod    #class method decorator
    def set_raise_amt(cls, amt): #cls is a class parameter. Accepts a class.
        cls.raise_amount = amt

    @staticmethod
    def is_weekday(day):
        return day.weekday()


class Developer(Employee):
    raise_amount = 1.10 #changes the value of raise_amount for any instances of the class Developer that may access it directly/indirectly,and also changes the method resolution order.
    def __init__(self,pay,first,last,language):  #adding another parameter that is specific and essential to know about a particular developer.
        super().__init__(pay,first,last) #Will look for the init method in classes the Developer class inherits from, that contains these 3 parametes, and bring that code in.
        self.prog_lang = language
    def details(self):
        super().details()
        print(f"Programming Language : {self.prog_lang}\n")

emp1 = Employee(20000,"John","Blunt")
emp2 = Employee(50000,"Emily","Krasinski")
emp1.details()
emp2.details()
# print(Employee.__dict__) #__dict__ is used to display the atrritubes and methods of a class(or an instance of the class)
# print(emp1.__dict__)
#
# emp1.raise_amount = 1.1 #trying to modify the value of the class variable through an instance of the class. This gives emp1 a copy of the raise_amount attribute and adds it
#                         # to its writable attribute dictionary
#                         #However, Employee.raise_amount can modify the value of the class variable for every instance of the class.
# print(emp1.__dict__) #This shows us that the instance emp1 now contains a copy of the raise_amount attribute with the modified value assigned to it.
#
# print(Employee.raise_amount)
# print(emp1.raise_amount) #Accessing this attribute now does not let the instance of the class go searching for the class variable named raise_amount,
#                          #instead it returns its own raise_amount attribute with the modified value
# emp1.details()



# print("Before raise : ")
# print(emp1.salary)
# print(emp2.salary)
# emp1.raise_amount = 1.1
# emp1.raise_salary()
# emp2.raise_salary()
# print("After raise : ")
# print(emp1.salary)
# print(emp2.salary)

#
dev1 = Developer(90000,"Jordan","Gilbert","Python")
dev1.details()
# import datetime
# theday = dev1.is_weekday(datetime.date(2019,7,10))
# print(f"{dev1.firstname} {dev1.lastname} has to work on the {theday+1}rd day of the week as well" )


# print(help(dev1))

# print(isinstance(dev1, Employee))    #tells us if an object is an instance of a class. Will print True in this case.
# print(issubclass(E)
