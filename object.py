class Myclass:
    def __init__(self, name, mat_no, dept):
        self.name = name
        self.mat_no = mat_no
        self.dept = dept

    def course(self, courses):
        print(f'hello,{self.name}.\n you are studying {courses}.')

adanna =Myclass('Adanna', 'PY12484', 'Python')
adanna.course('Django')

#another object
justice =Myclass('justice', 'JS23893', 'Javascript')
justice.course('React')

#another object