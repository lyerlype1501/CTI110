#Emmanuel Lyerly Pina
#10/2/2023
#Using if statements to determine leap year


#Get input from user

input_year = int(input('Enter a Year: '))

if input_year % 4 == 0:
    if input_year % 100 == 0:
        if input_year % 400 == 0:
            print('The year is a leap year')


        else:
            print('The year is NOT a leap year')
    else:
        print('The year is a leap year')
else:
    print('The year is NOT a leap year')
