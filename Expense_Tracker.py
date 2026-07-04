# Expense Tracker

# Empty Containers based on basic categories
food = []
shopping = []
bills = []
miscellaneous = []

print()
# Menu
print('-----MENU-----')
print()
print('A. Food')
print('B. Shopping')
print('C. Bills')
print('D. Miscellaneous')
print('Q -----> Quit')
print()

# Entry of expenses to the lists 
while True:
    menu_entry = input('Expense Category: ')
    if menu_entry.capitalize() == 'Q':
        break
    elif menu_entry.capitalize() == 'A':
        expense_entry_A = int(input('Enter the Amount: '))
        food.append(expense_entry_A)
        print(f'{expense_entry_A} has been added to Food.')
    elif menu_entry.capitalize() == 'B':
        expense_entry_B = int(input('Enter the Amount: '))
        shopping.append(expense_entry_B)
        print(f'{expense_entry_B} has been added to Shopping.')
    elif menu_entry.capitalize() == 'C':
        expense_entry_C = int(input('Enter the Amount: '))
        bills.append(expense_entry_C)
        print(f'{expense_entry_C} has been added to Bills.')
    elif menu_entry.capitalize() == 'D':
        expense_entry_D = int(input('Enter the Amount: '))
        miscellaneous.append(expense_entry_D)
        print(f'{expense_entry_D} has been added to miscellaneous.')
print()
print()

# OPERATIONS FUNCTIONS ----- LISTS 

# Adding of expenses of single lists 
def food_expenses ():
    total_food = sum(food)
    print(f'Your Total Food Expense is ${total_food}')

def shopping_expenses ():
    total_shopping = sum(shopping)
    print(f'Your Total Shopping Expense is ${total_shopping}')

def bills_expenses ():
    total_bills = sum(bills)
    print(f'Your Total Bills Expense is ${total_bills}')

def miscellaneous_expenses ():
    total_miscellaneous = sum(miscellaneous)
    print(f'Your Total Miscellaneous Expense is ${total_miscellaneous}')

# Adding of all the expenses 
def full_expense ():
    total_expense = (
        sum(food)
        + sum(shopping)
        + sum(bills)
        + sum(miscellaneous)
    )
    print(f'Your Overall Expense is ${total_expense}')

# USER SIDED LIST OPS
# OPS MENU
print('-----OPERATIONS MENU------')
print()
print('A. Total Food Expense')
print('B. Total Shopping Expense')
print('C. Total Bills Expense')
print('D. Total Miscellaneous Expense')
print('E. Overall Expenses')
print('Q. Quit')
print()

# OPS LOGIC
while True:
    ops_entry = input('VIEW EXPENSES: ')
    if ops_entry.capitalize() == "Q":
        break
    elif ops_entry.capitalize() == 'A':
        food_expenses()
    elif ops_entry.capitalize() == 'B':
        shopping_expenses()
    elif ops_entry.capitalize() == 'C':
        bills_expenses()
    elif ops_entry.capitalize() == 'D':
        miscellaneous_expenses()
    elif ops_entry.capitalize() == 'E':
        full_expense()
    else:
        print('Invalid Option')

