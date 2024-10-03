# lambda is a keyword used to write function
# greet = lambda : 'Hello'
# print(greet())

holiday =lambda a : a.strip().upper()
print(holiday(input('')))

party =lambda b : "it's party time!"
print(party('hello'))

party =lambda b : b
print(party("hello Cynthia it's party time!"))

party =lambda b, c, d : print(b+c*d)
print(party("hello Cynthia it's party time!"))

