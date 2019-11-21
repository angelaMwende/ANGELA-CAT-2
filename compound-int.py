import math

amount = float(input("Please Enter the Principal Amount : "))
rate= float(input("Please Enter the Rate Of Interest   : "))
time = float(input("Enter Time period in Years   : "))

future_compound_interest = amount * (math.pow((1 + rate / 100), time)) 
compound_int = future_compound_interest - amount

print("Compound Interest is  {0} = {1}".format(amount, compound_int))

