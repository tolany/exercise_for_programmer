# Excercise for Programing 
# Ex 5

# OUTPUT example 
# What is the first number? 10
# What is the second number? 5
# 10 + 5 = 15
# 10 - 5 = 5
# 10 * 5 = 50
# 10 / 5 = 2

# Limitation Condition 
# input variable as string and transer to int before caculatre
# use only one print sentence

fnumber = input("What is the first number? ")
snumber = input("What is the second number? ")

fnumber = int(fnumber)
snumber = int(snumber)

values = [fnumber + snumber, fnumber - snumber, fnumber * snumber, fnumber // snumber]
fnumber = str(fnumber) 
snumber = str(snumber)

print(fnumber + " + " + snumber + " = " + str(values[0]) +"\n"
      +fnumber + " - " + snumber + " = " + str(values[1]) +"\n"
       +fnumber + " * " + snumber + " = " + str(values[2]) +"\n"
        +fnumber + " / " + snumber + " = " + str(values[3]))