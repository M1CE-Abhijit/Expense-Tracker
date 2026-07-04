# Goals : Dictionary Mapping 
# Containers | Get them in a dictionary | Got them in the dictionary 
# New thing : Dictionary Mapping | eliminates if else

network = {'A':'Food','B':'Shopping','C':'Bills','D':'Miscellaneous'}

containers = {
    'Food': [],
    'Shopping': [],
    'Bills': [],
    'Miscellaneous': []
}
# Menu 2.0
menu_1 = [
    '-----EXPENSE MENU-----',
    'A. Food',
    'B. Shopping',
    'C. Bills',
    'D. Miscellaneous',
    'Q. Quit',
]

# Menu Printer
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
    # New Variable added to take input of the mapping and also used it to make error handling easy (in this case)
    network_input1 = network.get(menu_entry) 
    if network_input1 is None:
        print('Invalid Category, Please Re-enter')
        print()
        continue
# Items Expense Entry Error Handling    
    try:
        expense_entry = int(input('Enter Expense Amount: '))
    except ValueError:
        print('Invalid Expense, Please Re-enter')
        continue
    # User Input Operations
    containers[network_input1].append(expense_entry)

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Functions Defined 
def Overall_Expenses ():
    overall_expense = sum(containers['Food'] + containers['Shopping'] + containers['Bills'] + containers['Miscellaneous'])
    print(f'Your Overall Expense: ${overall_expense}')
    print()

def Single_Category_Expense():
    expenses = [sum(containers['Food']),sum(containers['Shopping']),sum(containers['Bills']),sum(containers['Miscellaneous'])]
    print(f'Food Expenses: ${expenses[0]}')
    print(f'Shopping Expenses: ${expenses[1]}')
    print(f'Bills Expenses: ${expenses[2]}')
    print(f'Miscellaneous Expense: ${expenses[3]}')
    print()

def Expense_History(network_input2):
    print(f'-----{network_input2} Expense History-----')
    for i , e in enumerate(containers[network_input2],start=1):
        print(f'{i}. {e}')

def Expense_Delete(network_input2):
    while True:                        
        delete = input('Y/N: ').upper()
        if delete == 'N':
            break    
        if delete != 'Y':
            print('Invalid Input')
            continue    
        try:
            index = int(input('Which Expense (0 to Quit): '))
        except ValueError:
            print('Wrong Input Type')
            continue
        if index == 0:
            break
        if index > containers[network_input2].__len__():
            print('Not Possible')
            continue
        containers[network_input2].pop(index-1)
        Expense_History(network_input2)
        print('Delete an Expense: ')

# 2nd Menu 2.0 
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

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
        # takes the input inside the option C 
        Category = input('Which category: ').strip().upper()
        # Error Handling for the input
        network_input2 = network.get(Category)
        if network_input2 is None:
            print('Invalid Input')
            print()
            continue
        else:
            Expense_History(network_input2)
            print('Delete an Expense: ')
        Expense_Delete(network_input2)