cars = ["Ford", "Volvo", "BMW"]

x = cars[0]
print(x) # this will print "Ford"
y = cars[1]
print(y) # this will print "Volvo"
z = cars[2]
print(z) # this will print "BMW"

for x in cars:
  print(x)

  cars.append("Honda")
  cars.pop(1)
  print(cars)

  cars.insert(1, "Toyota")
  print(cars)
  cars.remove("Ford")
  print(cars)
  


  