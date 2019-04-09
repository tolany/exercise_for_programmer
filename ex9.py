# Exercise for programmer 
# Ex 9

# OUTPUT example 
# You will need to purchase 2 liters of 
# paint to cover 10 square meters. 

# in order to paint 9m^2 square, 1L 
# must ceil 
# input length, width

length = int(input("Enter a length of room : "))
width = int(input("Enter a width of room :  "))

square_of_room = length * width
liter_of_paint = square_of_room // 9

if square_of_room % 9 == 0:
    liter_of_paint += 0
else:
    liter_of_paint += 1   

liter_of_paint = str(liter_of_paint) 
square_of_room = str(square_of_room)

print("You wil need to purchase " + liter_of_paint +" liters of\npaint to cover "+ square_of_room +" square meters." )

