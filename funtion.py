
def myfuntion():
    print("Hello, World!")
myfuntion()

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32 
print(celsius_to_fahrenheit(25))

def print_greeting(name):
    print("Hello, " + name + "!")
print_greeting("Alice")
print_greeting("Bob")


def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)
