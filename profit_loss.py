cost_price = float(input("Enter Cost price:"))
selling_price = float(input("Enter selling price:"))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("profit = ", profit)
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("Loss =", loss)
else:
    print("No profit No Loss")