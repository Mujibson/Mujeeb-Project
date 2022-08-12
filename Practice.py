name = 'Mujeeb'
if name == 'Tommy':
    print('You are wrong')
else:
    print('Alright')
# Creating a simple calculator
def addition(): # addition function
    first_number = int(input('Enter your first number:'))
    second_number = int(input('Enter your second number:'))
    print(first_number + second_number)

def subtracton(): #subtraction funcion
    first_number = int(input('Enter your first number:'))
    second_number = int(input('Enter your second number:'))
    print(first_number-second_number)

def division(): #division funcion
    first_number = int(input('Enter your first number:'))
    second_number = int(input('Enter your second number:'))
    print(first_number/second_number)

def multiplication(): #multipication funcion
    first_number = int(input('Enter your first number:'))
    second_number = int(input('Enter your second number:'))
    print(first_number*second_number)

def modulo(): #modulo funcion
    first_number = int(input('Enter your first number:'))
    second_number = int(input('Enter your second number:'))
    print(first_number % second_number)
def calc_run(): # modifying calc
    option = input('add, subtract, divide, multiply, modulo')
    if option == 'add':
        addition()
    elif option == 'subtract':
        subtracton()
    elif option == 'divide':
        division()
    elif option == 'multiply':
        multiplication()
    elif option == 'modulo':
        modulo()
    else:
        print('Please select an option!')
calc_run()