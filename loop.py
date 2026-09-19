print("I'm Rajeev")

#while loop,for loop,break,continue,pass

#1.while loop
i=1
while i <= 10:
    print(i)
    i += 1

#2.for loop
for i in range(1, 11):
    print(i)

#3.break statement
for i in range(1, 11):
    if i == 5:
        break
    print(i)

#4.continue statement
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

#5.pass statement
for i in range(1, 11):
    if i == 5:
        pass
    print(i)