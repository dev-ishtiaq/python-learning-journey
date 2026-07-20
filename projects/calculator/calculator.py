rent = int(input("Enter your flat rent = "))
food = int(input("Enter your food cost = "))
electricity = (int(input("Electric Bill = ")))
charge_per_unit = (int(input("Enter unit charge = ")))
persons = int(input("Enter persons = "))


total_bill = electricity * charge_per_unit

output = (food + rent + total_bill) // persons

print("Each person will pay =" , output)

