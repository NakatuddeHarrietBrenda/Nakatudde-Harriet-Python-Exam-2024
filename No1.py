# i)
def Circle_area():
    radius = int(input('Enter the radius of the circle:'))
    pie = 3.14
    area = pie * radius ** 2
    print(f'The area of the circle is: {area}')
Circle_area()

#ii)

numbers = [4,7,2,9,12,15]

sumOfNumbers = 0
for num in numbers:
    # Check for odd numbers
    if num % 2 != 0:
        sumOfNumbers += num
        print(f'\nThe sum of the numbers is: {sumOfNumbers}')


#iii)
number1 = int(input('\nEnter the first number:'))
number2 = int(input('\nEnter the second number:'))
import math
sum = number1 + number2
difference = number1 - number2
product =  number1 * number2
quotient =number1 / number2
print(f'The sum of the three numbers is:{sum}')
print(f'The difference of the three numbers is:{difference}')
print(f'The product of the three numbers is:{product}')
print(f'The quotient of the three numbers is:{quotient}')


#v)
Dct = {'name':'Alice', 'age': 20, 'grade':'A'}
#updated list
Dct['age'] = 26
# Adding a new
Dct['City'] = 'Kampala'
print(f'\nNew list {Dct}')


