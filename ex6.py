# Exercise for Programmer 
# Ex 6

# OUTPUT example 
# What is your current age? 25
# At what age would you like to retire? 50
# You have 40 years left until you can retire.
# It's 2015, so you can retire in 2055.

# Limitation Condition 
# transform to int type before calculate 
# Don't Enter this year. use system date. 
from datetime import datetime


current_age = input("What is your current age? ")
retire_age = input("At what age would you like to retire? ")
diff = int(retire_age) - int(current_age)
this_year = datetime.today().year # 올해 날짜를 this_year라는 변수에 시스템 데이터에서 받아야 함. 
retire_year = this_year + diff 
diff = str(diff)
this_year = str(this_year)
retire_year = str(retire_year) #동시 할당에 대해서 찾아보자. 매번 str로 각각 할당하는거 귀찮다. 

print("You have" + diff + "years left until you can retire.")
print("It's " + this_year +", so you can retire in " +  retire_year)
