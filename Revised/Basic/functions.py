def greeting(name,age):
    print(f'Hello, {name} \n How are you doing')
    print(f'I know your age is {age}')
greeting('Obed', 20)

#when you have set of code that can be called and used at any place in your program

def is_adult(age):
    if age >= 18:
        print('you are an adult')
    else:
        print('you are a kid ')
age = int(input('enter your age'))
is_adult(age)