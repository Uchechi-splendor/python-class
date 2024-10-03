# write a program to check if a user is eligible to vote
age=int(input('enter your age'))

if age <=17:
    print(f'you are not Eligible to vote')
elif age >=18:
    print('you are Eligible to vote')
else:
    print('Cast your vote')  