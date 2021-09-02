class cat1:
    def __init__(self, name, age):
        self.name= name
        self.age= age

    def populate (self, name, age):
        self.name= name
        self.age= age

    def display(self):
        print('The cats name is:', self.name)
        print ('The cats age is:', self.age)

print('enter variables to demonstrate the cat class')
name=input('enter name')
age=input('enter age')
CatObj= cat1(name, age)
CatObj.display()
