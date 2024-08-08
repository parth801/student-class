class Student():
  name = ""
  age = 14
  grade  = 9
  class_number = 4

#constructor
  def __init__(self):
    print("this is a student class")
#for changing name and age
  def change_details(self):
    self.name = input("enter your name")
    self.age = input("enter your age")
#for priniting details of tthe student
  def showdetails(self):
    print(self.name)
    print(self.age)
    print(self.grade)
    print(self.class_number)
    

parth = Student()
print(parth.grade)
parth.change_details()
parth.showdetails()

john = Student()
print(john.grade)
john.change_details()
john.showdetails()