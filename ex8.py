# Exercise for programmer 
# Ex 8

# OUTPUT example 
# How many people? 8
# How many pizzas do you have? 2
# How many pieces are in a pizza? 8

# 8 people with 2 pizzas
# Each person gets 2 pices of pizza.
# There are 0 leftover pieces

# Limitation Condition 

people = int(input("How many people? "))
pizzas = int(input("How many pizzas do you have? "))
pieces_of_pizza = int(input("How many pieces are in a pizza? "))

pices_per_person = str((pizzas * pieces_of_pizza) // people)
leftover = str((pizzas * pieces_of_pizza) % people)

people = str(people)
pizzas = str(pizzas)
print(people + " people with " + pizzas + " pizzas") 
print("Each person get "+ pices_per_person +" pieces of pizza.")
print("There are " + leftover +" leftover pieces.")
