#this calculates the accurates sales made in a day accurately.
brand_name = str(input("enter the name of the brand "))
day = str(input("enter the day of the week "))
date = int(input("enter the date "))
month = str(input("enter the month of the year "))
price_of_item_sold = float(input("enter the price of item "))
number_of_item_sold = int(input("enter the number of items sold "))
total = int(input("enter the total of your sales"))
while total <= price_of_item_sold + number_of_item_sold :
    print(total)
    total += int(input("enter the result"))