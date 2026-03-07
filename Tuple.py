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

# You can access tuple items by referring to their index number, inside square brackets.
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])         # Output: "banana" (index starts at 0)

# -1 refers to the last item, -2 refers to the second last item, and so on.
print(thistuple[-1])        # Output: "cherry"
print(thistuple[-2])        # Output: "banana"

# You can specify a range of indexes by specifying where to start and where to end the range.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4]) # Output: ('apple', 'banana', 'cherry', 'orange') (from index 0 to index 3)

# If you omit the start value, the range will start at the first item, and if you omit the end value, the range will go to the end of the tuple.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])    # Output: ('cherry', 'orange', 'kiwi', 'melon', 'mango') (from index 2 to the end of the tuple)