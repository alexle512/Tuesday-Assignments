meal = float(input("Enter the cost of the meal:$ "))
tip = (input("Enter the tip percentage desired: "))
tip = float(tip)/100
Total_amount = meal * tip + meal
print("Your total bill with tip included will be " + str(Total_amount))
