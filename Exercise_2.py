# Exercise 2 : Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

# print(total)
print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${total}")