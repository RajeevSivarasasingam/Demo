
str="welcome to python programming language"
print(str)

str="Tim said, \"Python is awesome!\"" #\ used for escape character
print(str)

#multiline string
str="""welcome to python programming language
This is a multiline string in Python"""
print(str)
print(len(str)) #length of string(including spaces)

name="Rahulan"
for i in name:
    print(i)
print(name[0]) #first character
print(name[-1]) #last character
print(name[0:3]) #first 3 characters
print(name[3:]) #from 4th character to end
print(name.upper()) #convert to uppercase
print(name.lower()) #convert to lowercase

print(name.find("a")) #find the index of first occurrence of "a"
name=name.replace("a","o") #replace "a" with "o"
print(name.split("a")) #split the string at "a"

st1="hey"
st2="there"
st3="all"
stg="{} {} {}".format(st1,st2,st3) #string formatting
print(stg)
