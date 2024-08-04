def expense_tracker():
    expenses={}
    while True:
        category=input("Enter expense category ('quit' to exit):").lower()
        if category =="quit":
            break
        amount=float(input("Enter expense amount:"))
        if category in expenses :
            expenses[category]+=amount
        else:
            expenses[category]=amount
    print("Expenses :")
    for category , amount in expenses.items():
        print(f"{category.capitalize()}: ${amount:.2f}")
expense_tracker()
