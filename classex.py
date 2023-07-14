//function
def first(name):
    print(f"My name is {name}")

first("ajay")


#class define
class student:
    #1.members
    age=20
    name=""
    address=""

   #2.Constructor
    def __init__(self,a):
      # self.address="mahagaon"
       self.address=a
       self.name="alisha"
       
   #3.Methods
    def show(self):
       print(f"student name is {self.name} studing in sgmcoe")
       print("student Address is "+self.address)

#create object
s=student("mahagaon")

#call class methods
s.show()


