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

 #pattern printing
 # get input and  print number in    , first row 1, second row 2, third row 3, fourth row 4, fifth row 5

n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ") #end is used to print in the same line
    print()

