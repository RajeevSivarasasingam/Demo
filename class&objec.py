
class Person:
    def __init__(self,n,g,a):
        self.name = n
        self.gender = g
        self.age = a

person1 = Person("Rajeev","Male",30)
print(person1.name)
person2 = Person("Ravi","Male",25)
print(person2.name)
print(person2.age)  
print(person1.age)