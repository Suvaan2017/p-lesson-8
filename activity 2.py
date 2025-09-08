string = input ("Enter a string: ")
string2 = ('')
for i in string:
    string2 = i + string2
print ("Reversed string is: ", string2)
print ("Original string is: ", string)