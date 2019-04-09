# Excercise for Programing 
# Ex 2

# OUTPUT example 
# what is the input string? Homer
# Homer has 5 characters.

# Limitation Condition 
# in output, show the string that inputed 
# use only one print sentence
# in order to count length of string, use built-in function 

#input part
string = input("What is the input string? ")

#counting length of string 
length_of_string = str(len(string))

#output
print(string + " has " + length_of_string + " characters")