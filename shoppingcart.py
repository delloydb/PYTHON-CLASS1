## Simple Shopping Cart Program

item = input("Enter the item you want to buy: ")
quantity = int(input("Enter the quantity: "))
price_per_item = float(input("Enter the price per item: "))

total_price = quantity * price_per_item

print(f"\nYou have added {quantity} {item} to your cart.")
print(f"The total price is: ${total_price:.2f}")
print("Thank you for shopping with us!")
