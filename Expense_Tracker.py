# Goals : [1] Data Persistence 

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

def Create_file(): # Opens the file and Adds the data into the file.
    with open('Expense_File.txt','w+') as file:
        # Writes Food Data
        file.write(','.join(str(i) for i in containers['Food']))
        file.write('\n')
        # Writes Shopping Data
        file.write(','.join(str(i) for i in containers['Shopping']))
        file.write('\n')
        # Writes Bills Data
        file.write(','.join(str(i) for i in containers['Bills']))
        file.write('\n')
        # Writes Miscellaneous Data
        file.write(','.join(str(i) for i in containers['Miscellaneous']))

def Read_n_Load_data():# Read data and loads it into dictionary
    # Reads the Data Line by line and strips empty spaces
    with open('Expense_File.txt','r')as file: 
        Food = file.readline().strip()
        Shopping = file.readline().strip()
        Bills = file.readline().strip()
        Miscellaneous = file.readline().strip()
    # Loads the data into the dictionary
    for I in Food.split(','):
        if I:
            containers['Food'].append(int(I))
    for I in Shopping.split(','):
        if I:
            containers['Shopping'].append(int(I))
    for I in Bills.split(','):
        if I:
            containers['Bills'].append(int(I))
    for I in Miscellaneous.split(','):
        if I:
            containers['Miscellaneous'].append(int(I))

network = {'A':'Food','B':'Shopping','C':'Bills','D':'Miscellaneous'}
containers = {
    'Food': [],
    'Shopping': [],
    'Bills': [],
    'Miscellaneous': []
}
# MENU 
menu1 = [
    '---FILE MENU---',
    'A. Load Existing Data',
    'B. Procced Without Loading'
]
print()
for i in menu1:
    print(i)
print()

while True:
    menu1_entry = input('Enter Choice: ').strip().upper()
    if menu1_entry not in ['A','B']:
       print('Invalid Input')
       continue
    if menu1_entry == 'A':
        try:
            with open('Expense_File.txt','r')as file:
                Read_n_Load_data()
                break
        except FileNotFoundError:
            print('File non Existent')
            continue
    elif menu1_entry == 'B':
        break

# Menu 2.0
menu_2 = [
    '-----EXPENSE MENU-----',
    'A. Food',
    'B. Shopping',
    'C. Bills',
    'D. Miscellaneous',
    'Q. Quit',
]
# Menu Printer
print()
for i in menu_2:
    print(i)
print()

# User Input of the Menu board | Added: Error Handling | 
while True:
    menu_entry2 = input('Expense Category: ').upper().strip()
# Items Selection Error Handling
    if menu_entry2 == 'Q':
        break
    # New Variable added to take input of the mapping and also used it to make error handling easy (in this case)
    network_input1 = network.get(menu_entry2) 
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
# 2nd Menu 2.0 
menu_3 = [
    '-----EXPENSE OPERATIONS MENU-----',
    'A. Single Category',
    'B. Overall Expense',
    'C. Expense History',
    'Q. Quit',
]
# This prints the menu line by line
print()
for i in menu_3:
    print(i)
print()
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Menu Input Logic
while True:
    menu_entry3 = input('Expense Operations: ').upper().strip()
    if menu_entry3 == 'Q':
        break
    # Error Handling 
    if menu_entry3 not in ['A','B','C',]:
        print('Invalid Input')
        continue
    
    if menu_entry3 == 'A':
        Single_Category_Expense()
    
    elif menu_entry3 == 'B':
        Overall_Expenses()

# Menu option C is a bit broad because it does 2 things   
    elif menu_entry3 == 'C':
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
        Expense_Delete(network_input2)
Create_file() # this saves the data after every operations is complete.