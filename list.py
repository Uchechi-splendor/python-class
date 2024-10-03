car={
    'brand': 'Toyota',
     'model': 'spider',
     'year': '2020',
     'color': ['ash', 'black' ],
     'color':'blue'
    }

print(car)
print(car['brand'])
print(car.get('color'))
print(car.keys())
car.update({'engines': 'v6'})
print(car)
# car.pop('color')
# print(car)
# car.popitem()
# print(car)
# car.clear()
# print(car)

for x in car:
    print(x)

    #loop through values
for x in car:
     print(car[x])

for c in car.values():
    print(c)

for y in car.keys():
    print(y)

for i in car.items():
    print(i)   

    carr={'brands':'lexus'}
    carr=car.copy()
    print(carr)     

    cars=dict(carr)  
    print(cars)

    python_class={
        'student1':{
            'name': 'john',
            'age':17,
            'course':'Ethical hacking',
            'complexion':'caramel',
        },

        'student2':{
            'name': 'Mummy happy',
            'age':45,
            'course':'data science',
            'complexion':'dark',
        },

        'student3':{
            'name': 'justice',
            'age':40,
            'course':'AI/ML',
            'complexion':'fair',
        },

        'student4':{
            'name': 'ifeanyi',
            'age':11,
            'course':'Cyber Security',
            'complexion':'fair',
        },

        'student5':{
            'name': 'Rejoice',
            'age':14,
            'course':'Cyber Security',
            'complexion':'dark',
        },

        'student6':{
            'name': 'chigameziue',
            'age':6,
            'course':'marketing',
            'complexion':'caramel',
        },

        'student7':{
            'name': 'Roy',
            'age':26,
            'course':'Money',
            'complexion':'dark',
        }


    }      
print(python_class['student7']['name'])
print(python_class['student2']['course'])
print(python_class['student5']['age'])
print(python_class.items())()