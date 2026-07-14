# this is a simple coffee app that allows users to order coffee and customize their drinks

print("===Welcome to the Coffee App!===")
print("Please select your coffee type:")
print("1. Espresso")
print("2. Latte")
print("3. Cappuccino")
    
coffee_type = input("Enter the number of your choice: ")
    
if coffee_type == "1":
        coffee = "Espresso"
elif coffee_type == "2":
        coffee = "Latte"
elif coffee_type == "3":
        coffee = "Cappuccino"
else:
    print("Invalid choice. Please try again.")
        
    
size = input("Select size (small, medium, large): ")
    
milk = input("Do you want milk? (yes/no): ")
    
sugar = input("Do you want sugar? (yes/no): ")
    
print(f"Your order: {size} {coffee} with {'milk' if milk == 'yes' else 'no milk'} and {'sugar' if sugar == 'yes' else 'no sugar'}.")
print("Thank you for your order! Your coffee will be ready shortly.")

