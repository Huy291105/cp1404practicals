sales = float(input("Enter sales: $"))
while sales >= 0:
        if sales < 1000:
                sales_bonus = sales * (10 / 100)
        else:
                sales_bonus = sales * (15 / 100)
        print("Bonus is $", sales_bonus, sep='')
        sales = float(input("Enter sales: $"))
