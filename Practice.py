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
addition() 

def subtracton(): #subtraction funcion
    first_number = int(input('Enter your first number:'))
    second_number = int(input('Enter your second number:'))
    print(first_number-second_number)
subtracton()

def division(): #division funcion
    first_number = int(input('Enter your first number:'))
    second_number = int(input('Enter your second number:'))
    print(first_number/second_number)
division()

def multiplication(): #multipication funcion
    first_number = int(input('Enter your first number:'))
    second_number = int(input('Enter your second number:'))
    print(first_number*second_number)
multiplication()

def modulo(): #modulo funcion
    first_number = int(input('Enter your first number:'))
    second_number = int(input('Enter your second number:'))
    print(first_number % second_number)
modulo()