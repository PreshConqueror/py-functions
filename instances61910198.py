class cat:
    'classes of cat'
    cat_count=0

    def __init__(self, name, age):
        self.name=  name
        self.age= age
        cat.cat_count+=1

        def catinformation(self):
            print('name:' , self.name, ',age:', self.age)
c1=cat(input ('enter cat name: '), input('enter cat age:'))
c2=cat(input ('enter cat name: '), input('enter cat age:'))
c3=cat(input ('enter cat name: '), input('enter cat age:'))
c4=cat(input ('enter cat name: '), input('enter cat age:'))
c5=cat(input ('enter cat name: '), input('enter cat age:'))

print('The total number of cats is:',cat.cat_count)
c1.catinformation()
c2.catinformation()
c3.catinformation()
c4.catinformation()
c5.catinformation()



          
