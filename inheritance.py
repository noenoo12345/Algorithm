class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname, self.lastname)

    def __str__(self):
        return "%s : %s" % (self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, graduateyear):
        super().__init__(fname, lname)
        self.graduateyear = graduateyear

    def welcome(self):
        print(self.firstname, self.lastname, self.graduateyear)

x = Student("John", "Wick", "1900")
print(str(x))


# from abc import ABC, abstractmethod

# class abstractClass(ABC):
#     def __init__(self, value):
#         self.value = value
#         super().__init__()

#     @abstractmethod
#     def do_something(self):
#         pass

# class doAddValue(abstractClass):
#     def __init__(self, value):
#         super().__init__(value)

#     def do_something(self):
#         print("dosomething")


# x = doAddValue(3)
# x.do_something()
