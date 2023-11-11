'''write a program to find hee sale price of an item with a given cost and discount(%)'''

# input cost and disount percenage 

cost = float(input("enter the cost of the item : $"))

discount_percentage = float(input("enter the disxcount percentage : "))

# Calulate the discount amount

discount_amount = (cost * discount_percentage)/100

# calculate the sale price 

sale_price = cost - discount_amount

# display the sale price

print(f"the sale price of item after a {discount_percentage}% discount is : $ {discount_amount} sale price {sale_price}")