
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

tuple1=("cat", "dog", "rabbit")
for x in tuple1:
  print(x)
mystr = "banana"
for x in mystr:
  print(x)

print("----------------------")

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))

print("----------------------")

#stopleration is a technique used to stop a loop from iterating too many times.
class MyNumbers2:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
myclass2 = MyNumbers2()
myiter2 = iter(myclass2)
for x in myiter2:
    print(x)