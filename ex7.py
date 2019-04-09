# Exercise for Programmer 
# Ex 7

# OUTPUT example 
# What is the length of the room in feet? 15
# What is the width of the room in feet? 20 
# You entered dimensions of 15 feet by 20 feet 
# The area is 
# 300 square feet
# 27.871 square meters 

# m^2 = f^2 x c
# 27.871 m^2 = 300 f^2 * 0.0929034


# Limitation Condition 
# seperate print part and calcuate. 
# saving transfer number. 
import math 

number_of_transfer = 9290304

length = input("What is the length of the room in feet? ")
width = input("What is the width of the room in feet? ")
print("You entered dimensions of " + length +" feet by " + width +" feet")

length = int(length)
width = int(width)

square_feet = length * width
square_meters = (square_feet * number_of_transfer) / 100000000
## 개선사항, 문제의 출력은 소숫점 4번째 자리에서 반올림을 했음. 자릿수를 다루는 방법을 알아야함.

square_feet = str(square_feet)
square_meters = str(square_meters)

print("The area is\n"
        + square_feet + " square feet\n"
        + square_meters + " square meters")
