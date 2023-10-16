#Emmanuel Lyerly Pina
#10/4/2023
#Use if/else statements to determine gross pay

#Get input from user
name = ''
count = 0
total_pay = 0
while name != 'Done':
    

    name = input('Enter employee name: ')
    if name != 'Done':
        count = count + 1
        num_hours = float(input('Enter number of hours worked: '))
        pay_rate = float(input('Enter hourly pay rate: '))
        OT_hours = 0
        has_OT = False
        OT_pay = 0

        #Calculate overtime - yes/no - how much
        if num_hours > 40:
                    has_OT = True
                    OT_hours = num_hours - 40
        else:
            has_OT = False

        if has_OT == True:
            OT_pay = (pay_rate*1.5) * (num_hours - 40)  #Actual OT total pay
        else:
            OT_pay = 0

        #Calculate regular pay
        reg_pay = pay_rate * (num_hours - OT_hours)
        gross_pay = reg_pay + OT_pay
        total_pay = total_pay + gross_pay

        #Display name, pay rate, num hours worked, OT hours, OT pay, regular pay, gross pay

        print('Name: ', name)
        print('Overtime hours: ', OT_hours)
        print('Overtime pay: ', OT_pay)
        print('Regular hours: ', num_hours - OT_hours)
        print('Regular pay: ', reg_pay)
        print('Gross pay: ', reg_pay + OT_pay)

#While loop breaks
print('Total number of employees entered:', count)
print('Total paid to employees: ', total_pay)
