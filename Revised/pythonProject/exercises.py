#list elements addition with the help of looping

mylist =[1,2,3,4,5,6,7,8,9,10]
sum = 0

for i in range(len(mylist)):
    sum += mylist[i]
print(f'The sum of that list elements is {sum}')