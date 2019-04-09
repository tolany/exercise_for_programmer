# Exercise for programmer 
# Ex 13

# OUTPUT example 
# What is the principal amount? 1500
# what is the rate: 4.3
# what is the number of years: 6
# what is the number of times the interest
# is compounded per year: 4

# 1500 invested at 4.3% for 6 years compounded 4 times per year is
# $1938.84

# Limitation Condition 
# A = P(1+(r/n))^nt

principal = float(input("What is the principal amount? "))
rate = int(float(input("what is the rate: "))*100)
numofyears = int(input("what is the number of years: "))
numoftimes = int(input("what is the number of times the interest\nis compounded per year: "))

