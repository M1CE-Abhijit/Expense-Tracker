# Goals to acheive : [1] Stop Repeated Coding [2] Get Containers in a Dictionary [3] Try/Except for error handling

# Containers | Needed to be in a single Dictionary | Can't Get it done for the time
food = []
shopping = []
bills = []
miscellaneous = []

print()
# Menu Board
print('-----MENU-----')
print()
print('A. Food')
print('B. Shopping')
print('C. Bills')
print('D. Miscellaneous')
print('Q. Quit')
print()


# User Input of the Menu board | Added: Error Handling | Problem: Error in last category leads to input redo of all category.
while True:
    menu_entry = input('Expense Category: ').upper().strip()
# Items Selection Error Handling
    if menu_entry == 'Q':
        break
    if menu_entry not in ['A','B','C','D']:
        print('Invalid Category, Please Re-enter')
        continue
# Items Expense Entry Error Handling    
    try:
        expense_entry = int(input('Enter Expense Amount: '))
    except ValueError:
        print('Invalid Expense, Please Re-enter')
        continue
# User Input Operations
    if menu_entry == 'A':
        food.append(expense_entry)
    elif menu_entry == 'B':
        shopping.append(expense_entry)
    elif menu_entry == 'C':
        bills.append(expense_entry)
    elif menu_entry == 'D':
        miscellaneous.append(expense_entry)

# 2nd Menu
print()
print('-----View Expense Menu------')
print()
print('A. View Single Category Expense')
print('B. View Overall Expense')
print('Q. Quit')
print()

# Defining Functions
def Overall_Expenses ():
    overall_expense = sum(food + shopping + bills + miscellaneous)
    print(f'Your Overall Expense: ${overall_expense}')
    print()

def Single_Category_Expense():
    expenses = [sum(food),sum(shopping),sum(bills),sum(miscellaneous)]
    print(f'Food Expenses: ${expenses[0]}')
    print(f'Shopping Expenses: ${expenses[1]}')
    print(f'Bills Expenses: ${expenses[2]}')
    print(f'Miscellaneous Expense: ${expenses[3]}')
    print()

#  Menu Input Logic
while True:
    menu_2 = input('View Expense:' ).upper().strip()
    if menu_2 == 'Q':
        break
    if menu_2 not in ['A','B']:
        print('Invalid Input')
        continue
    if menu_2 == 'A':
        Single_Category_Expense()
    elif menu_2 == 'B':
        Overall_Expenses()