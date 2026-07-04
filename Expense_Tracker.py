# Goals to Achieve | [1] Expense History [2] Delete Expense [3] Get my Containers in a Dictionary

# containers | Get them in a dictionary
food = []
shopping = []
bills = []
miscellaneous = []

# Menu 2.0
menu_1 = [
    '-----EXPENSE MENU-----',
    'A. Food',
    'B. Shopping',
    'C. Bills',
    'D. Miscellaneous',
    'Q. Quit',
]
print()
for i in menu_1:
    print(i)
print()

# User Input of the Menu board | Added: Error Handling | 
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

# 2nd Menu 2.0 | Earlier there were repeated print statement Now it is just a single list
menu_2 = [
    '-----EXPENSE OPERATIONS MENU-----',
    'A. Single Category',
    'B. Overall Expense',
    'C. Expense History',
    'Q. Quit',
]
# This prints the menu line by line
print()
for i in menu_2:
    print(i)
print()

# Functions Defined 
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

def Expense_History(list, tittle):
    print(f'---{tittle}---')
    for index, entry in enumerate(list, start=1):
        print(f'{index}. {entry}')

def Expense_Delete(list):
    while True:                        
        delete = input('Y/N: ').upper()
        if delete == 'N':
            break
        if delete != 'Y':
            print('Invalid Input')
            continue    
        try:
            index = int(input('Which Expense (9999 to Quit): '))
        except ValueError:
            print('Wrong Input Type')
            continue
        if index == 9999:
            break
        if index > list.__len__():
            print('Not Possible')
            continue
        list.pop(index-1)
        break

def Expense_ReDelete(list):
    while True:
        try:
            index = int(input('Which Expense (0000 to Quit): '))
        except ValueError:
            print('Wrong Input Type')
            continue
        if index == 0000:
            break
        if index > list.__len__():
            print('Not Possible')
            continue
        list.pop(index-1)
        Expense_History(list,tittle)


#  Menu Input Logic
while True:
    menu_2 = input('Expense Operations: ').upper().strip()
    if menu_2 == 'Q':
        break
    # Error Handling 
    if menu_2 not in ['A','B','C',]:
        print('Invalid Input')
        continue
    
    if menu_2 == 'A':
        Single_Category_Expense()
    
    elif menu_2 == 'B':
        Overall_Expenses()

# Menu option C is a bit broad because it does 2 things   
    elif menu_2 == 'C':
        # take the input inside the option C 
        Category = input('Which category: ').strip().upper()
        # Error Handling for the input
        if Category not in ['A','B','C','D']:
            print('Invalid Input')
            continue
        # Logic Handling of the input
        if Category == 'A':
            list = food
            tittle = 'FOOD EXPENSE HISTORY'
        elif Category == 'B':
            list = shopping
            tittle = 'SHOPPING EXPENSE HISTORY'
        elif Category == 'C':
            list = bills
            tittle = 'BILLS EXPENSE HISTORY'
        elif Category == 'D':
            list = miscellaneous
            tittle = 'MISCELLANEOUS EXPENSE HISTORY'
        Expense_History(list,tittle)
        print('Delete An Expense?: ')
        Expense_Delete(list)
        Expense_History(list,tittle)
        Expense_ReDelete(list)

