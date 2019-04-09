# Excercise for programmer 
# Ex 12

# OUTPUT example 
# Enter the principal: 1500
# Enter the rate of interest: 4.3
# Enter the number of years: 4
# After 4 years at 4.3%, the investment will be worth $1758 

# Limitation Condition 
# A = P(1+rt)

import math

principal = int(input("Enter the principal: "))
rate_of_interest = float(input("Enter the rate of interest: "))
number_of_years = int(input("Enter the number of years: "))

Amount = math.ceil(principal * (1 + (rate_of_interest/100) * number_of_years))

rate_of_interest = str(rate_of_interest)
number_of_years = str(number_of_years) 
Amount = str(Amount)

print("After "+number_of_years+" years at "+rate_of_interest+"% , the investment will be worth $"+Amount)
