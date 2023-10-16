#Emmanuel Lyerly Pina
#10/11/2023
#Using function


#Create function

def adding(num1, num2):
    result = num1 + num2
    return result

def subtract(num1, num2):
    result = num1 - num2
    return result


#Main function
def main():
    user_choice = 0


    while user_choice != 3:
        print('Welcome to the Main Manu')
        print('------------------------')
        print('1.Addition')
        print('2.Subtraction')
        print('3.End Program')

        user_choice = int(input('Enter a choice: '))

        if user_choice == 1:
            num1 = int(input('Enter an integer: '))
            num2 = int(input('Enter another integer: '))
            print(adding(num1, num2))
            user_choice = int(input('Enter a choice: '))

        if user_choice == 2:
            num1 = int(input('Enter an integer: '))
            num2 = int(input('Enter another integer: '))
            print(subtract(num1, num2))
            user_choice = int(input('Enter a choice: '))

        if user_choice == 3:
            print('Goodbye')
        else:
            print('You entered an invalid choice')



#Call the main function - starts the program
main()
