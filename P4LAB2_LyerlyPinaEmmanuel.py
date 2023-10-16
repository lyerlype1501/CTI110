#Emmanuel Lyerly Pian
#10/4/2023
#Intro to Loops using range()

int_1 = int(input('Enter a num: '))
int_2 = int(input('Enter a num: '))

#If first num is smaller
if int_1 <= int_2:
    #Execute for loop using range(start, stop, step)
    for x in range(int_1, int_2+1, 5):
        print(x)

else:
    print('The first number must be smaller.')
