print("-------------------------------------CLASS FORMATION-------------------------------------------------------------------")
class student:
    country="India"
    def __init__(self,name,age):
        self.name=name
        self.age=age
student1=student("yash",20)
student2=student("ram",21)
print(student1.name, student1.age,student1.country)
print(student2.name, student2.age,student2.country)


print("--------------------------------------Book details------------------------------------------------------------------")
class book:
    def __init__(self,title,price):
        self.title=title
        self.price=price
book1=book("Python Basics",499)
print(book1.title,book1.price)
class std:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks


    def hello(self):
        print("HELLO,",self.name)

    def marks(self):
        return self.marks
    
s1=std("RAM",77)
s1.hello()
print(s1.marks)


print("--------------------------------------Sub details----(@staticmethod)------------------------------------------------------------------")
class sub():
    @staticmethod
    def hello():
        print("HELLO")
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg_score(self):
        sum=0
        for mark in self.marks:
            sum+=mark
        print("Hi,",self.name,"Your average score is",sum/len(self.marks))
s1=sub("RAM",[77,88,99])
s1.avg_score()
s1.hello()


print("----------------------------------------------ACCOUNT FUNCTIONALITY----------------------------------------------------------")
class account:
    def __init__(self,bal,acc):
        self.bal=bal
        self.acc=acc
    def credit(self):
        print("Available balance is",self.bal)
        C=int(input("Enter the amount to credit:"))
        self.bal+=C
        #self.bal=new_bal
        print("Your new balance is",self.bal)
    def debit(self):
        print("Available balance is",self.bal)
        D=int(input("Enter the amount to debit:"))
        if D>self.bal:
            print("Insufficient balance")
        else:
            self.bal-=D
            #self.bal=new_bal
            print("Your new balance is",self.bal)
    def balance(self):
        return self.bal
acc1=account(45000,"ABC123")
acc1.credit()
acc1.debit()
print("Your available balance is",acc1.balance())


print("---------------------------------------------INHERITENCE-----------------------------------------------------------")

print("-----------------------------------------------Single inheritance--------------------------------------------------------------------")
class car:
    colour="white"
    @staticmethod
    def start():
        print("Car is starting")
    @staticmethod
    def stop():
        print("Car is stopped")    
class Honda(car):
    def __init__(self,name):
        self.name=name

# c1=Honda("city")
# c2=Honda("civic")
# print(c2.name,c2.stop(),c2.colour)
# print(c1.name,c1.start(),c1.colour)


print("-----------------------------------------------Multilevel inheritance--------------------------------------------------------------------")
class type(Honda):
    def __init__(self,oil):
        self.oil=oil
        super().__init__(H1.name)
        print("The oil type is",self.oil)
H1=Honda("Honda city")
T1=type("Petrol")
print(T1.name,T1.oil)


print("-----------------------------------------------multiple inheritance--------------------------------------------------------------------")
class brand:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("Car is starting")    
    @staticmethod
    def stop():
        print("Car is stopped")
class vehicle(brand):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name
v1=vehicle("City","petrol")
print(v1.name,v1.type)


print("----------------------------------------------------Property----------------------------------------------------------------------")
class stm():
    def __init__(self,phy,math,chem):
        self.phy=phy
        self.math=math
        self.chem=chem
    @property
    def percentage(self):
        return str((self.phy+self.math+self.chem)/3)+"%"
    
std1=stm(90,95,85)
print("Percentage is",std1.percentage)
std1.phy=80
print("Updated percentage is",std1.percentage)


print("-------------------------------------------Dunder Function---------polymorphism--------------------------------------------------")
class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def showno(self):
        print(self.real,"i+",self.img,"j")
    def __add__(self,num2):
        newreal=self.real+num2.real
        newimg=self.img+num2.img
        return complex(newreal,newimg)
num1=complex(1,3)
num1.showno()
num2=complex(3,6)
num2.showno()
num3=num1+num2
num3.showno()


print("-------------------------------------------Circle area and perimeter--------------------------------------------------")
class circle:
    def __init__(self,radius):
        self.radius=radius
    @property
    def area(self):
        return 3.14*self.radius**2
    @property
    def perimeter(self):
        return 2*3.14*self.radius
c1=circle(5)
c2=circle(10)
print("Area of the circle of radius",c1.radius,"is",c1.area,"sq units")
print("Perimeter of the circle of radius",c1.radius,"is",c1.perimeter,"units")
print("Area of the circle of radius",c2.radius,"is",c2.area,"sq units")
print("Perimeter of the circle of radius",c2.radius,"is",c2.perimeter,"units")


print("-------------------------------------------Employee details--------------------------------------------------")
class employee:
    def __init__(self, role, dept, sal):
        self.role = role
        self.dept = dept
        self.sal = sal

    def showdetails(self):
        print("Role:", self.role)
        print("Department:", self.dept)
        print("Salary:", self.sal)


class engineer(employee):
    def __init__(self, name, age, role, dept, sal):
        self.name = name
        self.age = age

        super().__init__(role, dept, sal)


eng1 = engineer("Yash",20,"Software Engineer","IT",50000)

eng1.showdetails()


print("------------------------__gt__  i.e = greater than operator overloading-----------------------------")
class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,ord2):
        return self.price>ord2.price
    
ord1=order("Chips",20)
ord2=order("Tea",15)
print(ord1 > ord2)

print("---------------------------------End of object oriented programming--------------------------------------------------")

print("Thank you for learning Object Oriented Programming (OOPS)")