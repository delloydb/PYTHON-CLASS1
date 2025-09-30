temp = 9
if temp > 20:
    print("It's a nice day")
    print("Drink plenty of water")
elif temp < 10:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's neither hot nor cold")
    print("Have a nice day")
print("Enjoy your day")

# tenary operator
age = 18
message = "Eligible to vote" if age >= 18 else "Not eligible to vote"
print(message)
