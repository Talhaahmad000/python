print("enter ur current age")
age=input("what is ur age")# input give in string format so convert into int
print(f"ur age is {age}")
print("now calculate how many days year month reminaing when u were 90 years old")

year=90-int(age); #21 is current 69 remain
days=365*year;#1year=365 days so 69 year *365 total days in year =25000
weeks=52*year;#1year=52 week so remianing weeks 52 *69 year(total in one year * ur remain year) 
month=12*year
print(f"u have year remianing {year} \n and days remaining  {days} \n and weeks  {weeks} \n and month are {month}")