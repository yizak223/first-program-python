

def my_function():
    print("This is my function!")
    print("This is my second string")

my_function()

def my_function2(str1,str2):
    print(str1)
    print(str2)

my_function2("hellow",'yizak')

def print_somthing(name='yizak',age=23):
    print('my name is',name,"and my age is",age)

print_somthing()
print_somthing('moshe',11)
print_somthing(age=24)

def print_people(*poeple):
    for person in poeple:
        print('this person is',person)

print_people('yizak','moshe')

def do_math(num1,num2):
    return num1+num2

math1 = do_math(5,7)
math2 = do_math(11,34)

print(math1,math2)
