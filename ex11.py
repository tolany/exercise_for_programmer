# Excercise for programmer 
# Ex 11

# OUTPUT example 
# How many Euros are you exchanging? 81
# What is the exchange rate? 137.51
# 81 Euros at an exchange rate of 137.51 is
# 111.38 dollars 

# Limitation Condition 
# amount_to = (amount_from * rate_from) / rate_to
# amount_to is usdollar , amount_from is euro, rate_from = eurorate, rate_to = dollarrate

# => amount_to = amount_from * (rate_from / rate_to) 
# => usdollar = euro * exchange_rate 
import math

euro = int(input("How many Euros are you exchanging? "))
temp_exchange_rate = float(input("What is the exchange rate? "))
exchange_rate = int(temp_exchange_rate * 100)
usdollar = euro * exchange_rate / 10000 ## 특정 소숫점 이하 자리에서 반올림 하는 방법 확인 필요.

euro = str(euro)
exchange_rate = str(temp_exchange_rate)
usdollar = str(usdollar)

print(euro+" Euros at an exchange rate of "+exchange_rate+" is\n" +usdollar +" dollars")