# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
#   "year": 2020        # note that we have duplicate key "year", the last value will overwrite the previous one
}
print(thisdict)


print(thisdict["brand"])
# You can also use the get() method to access the value of a specific key.
x = thisdict.get("model")
print(x)

print("########") 
#
thisdict = dict(name = "John", age = 36, country = "Norway")    # another way to create a dictionary using the dict() constructor
print(thisdict)
