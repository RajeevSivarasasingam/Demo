#Tuples are used to store multiple items in a single variable.
#4 built-in data types in Python used to store collections of data,
# tuples, lists, dictionaries, and sets.


#Let's create a tuple of 3 elements
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)


# it allows duplicate values
thistuple = ("apple", "banana", "cherry", "apple", "cherry")    #here we have duplicate values "apple" and "cherry"
print(thistuple)

# Tuples are immutable, which means you cannot change their values after they are created. However, you can create a new tuple by concatenating existing tuples.
# Concatenating tuples
tuple1 = ("apple", "banana", "cherry")
tuple2 = ("orange", "grape", "melon")
new_tuple = tuple1 + tuple2
print(new_tuple)

# You can also repeat a tuple using the multiplication operator
# Repeating a tuple
my_tuple = ("apple", "banana", "cherry")    
repeated_tuple = my_tuple * 2
print(repeated_tuple)

    