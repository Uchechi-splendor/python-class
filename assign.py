class Ola:
    my_name: str = input('enter your name')
    print ('welcome,', my_name)

    def calculate_length(self):
     length: int =len('Ola')
     print(f'the length of surname is:', length)

    def greeting_message(self):
     print(f'welcome Ola')


Olu =Ola()
Olu.calculate_length()
Olu.greeting_message()