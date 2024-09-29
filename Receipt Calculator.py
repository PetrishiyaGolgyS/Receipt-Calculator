import math

print('-'*52)
print("\tWelcome to Our recepit calculator")
print('-'*52)

print("\t\tNOTE!!!!!")
print("*"*52)
print("1. Avoid using symbols like '$' ',' '%' ,Instead use '+' in step1 ")
print("2. If you are not splitting the bill with anyone, just type '1' ")
print("*"*52,"\n")
print("Calculate the total cost per person....\n")

price_all = eval(input("Step 1: Please enter the cost of each product: "))

tax_p = float(input("Step 2: What is the sales tax in ur area: "))

tip = float(input("Step 3: What percentage would you like to give as a tip: "))

split = int(input("Step 4: How many people are you splitting the bill with: "))

total_p = (price_all + (price_all*(tax_p/100.0)) + (price_all*(tip/100.0))) / split

final_p = round(total_p,2)

print("The total cost per person is: Rs",final_p)