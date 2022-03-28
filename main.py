customer_name = input("Welcome, what is your name?")
starting_price = 5000.25
print(f"Hello {customer_name} your starting balance is ${5000.25}")
pay_check = float(input("How much of your paycheck would you like to deposit?"))
  
expenditure_items= input("Looks like you went shopping. What did you buy?")
expenditure = float(input("How much did the item cost:"))
def checking_balance(user_name, balance, deposits, expense_item, expense_amount):
    global pay_check, customer_name, expenditure_items, expenditure, ending_balance, starting_price
    ending_balance = balance + deposits - expense_amount
    customer_name = user_name
    starting_price = balance
    pay_check = deposits
    expenditure_items = expense_item
    expenditure = expense_amount
    print(f"Your final balance is{ending_balance}")
checking_balance(customer_name, starting_price, pay_check,  expenditure_items, expenditure, )