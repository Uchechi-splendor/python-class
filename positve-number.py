#write a program that checks if a number is positive, negative or zero
num = float(input('Enter any number'))
if num > 0:
    print(f'{num} is a positive number.')
elif num < 0:
    print(f'{num}is a negative number.')
else:
    print('zero')
#tenary operator
# statement condition else statement

number = int(input('enter a number'))

even_or_odd = 'even' if number %2 == 0 else 'odd'
print(even_or_odd)

age = int(input('enter your age'))

eligible_or_not= 'eligible' if age >=18 else 'not eligible'
print(eligible_or_not)