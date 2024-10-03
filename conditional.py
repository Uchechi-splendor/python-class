grade=int(input('enter your score: '))

if grade >=75 and grade <= 100:
    print(f'Excellent, you got an A')
elif grade >=60 and grade <=74:
    print('Awesome! Your score is B')
elif grade >=50 and grade <=59:
    print('good! Your got a C')
elif grade >=40 and grade <=49:
    print('fairly good! Your got a D')
elif grade >=30 and grade <=39:
    print('Narrow Escape! Your got a E')
elif grade >=0 and grade <=34:
    print('Poor! Your got an F')
else:
    print('Invalid score.\n Input a valid score')

#check 
    number= int(input('Enter a number'))
if number % 2 ==0:
    print(f' {number} is even number')
else:
    print(f' {number} is odd number')

