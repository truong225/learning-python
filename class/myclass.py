# coding: utf-8


"""
    Khai báo class:
        class myclass([parentclass]):
            assignment
            def __init__(self):
                statements
            def method():
                statements
            def method2():
                statements

    __init__(self, ): constructor
    self: truy cập ngược lại object đang gọi
"""


class Person:
    name = ''
    weight = 0

    def __init__(self, name='', weight=0):
        self.name = name
        self.weight = weight

    def show(self):
        print 'The name: ', self.name

    def run(self):
        print 'Person is running'


class Student(Person):
    # Override
    def run(self):
        print 'Student is running'


myperson = Person()
myperson.show()
myperson.run()

mystudent = Student('Kobayashi')
mystudent.show()
mystudent.run()
