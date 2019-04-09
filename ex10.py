# Excercise for programmer 
# Ex 10

# OUTPUT example 
# price of item 1: 25
# Quantity of item 1 : 2 
# Price of item 2: 10
# Quantity of item 2: 1
# Price of item 3: 4
# Quantity of item 3: 1
# Subtotal: $62.00
# Tax : $3.52
# Total: $67.52

# Limitation Condition 
# Tax rate = .055

p_item = [0,0,0]
q_item = [0,0,0]

p_item[0] = int(input("price of item 1: "))
q_item[0] = int(input("Quantity of item 1: "))
p_item[1] = int(input("price of item 2: "))
q_item[1] = int(input("Quantity of item 2: "))
p_item[2] = int(input("price of item 3: "))
q_item[2] = int(input("Quantity of item 3: "))

Subtotal = 0

for i in range(3):
    temp = p_item[i] * q_item[i]
    Subtotal += temp
    temp = 0

Tax = (Subtotal * 55) / 1000
Total = Subtotal + Tax
Subtotal = str(Subtotal)
Tax = str(Tax)
Total = str(Total)

print("Subtotal: $" +Subtotal+ "\nTax: $"+Tax+"\nTotal: $"+Total )
