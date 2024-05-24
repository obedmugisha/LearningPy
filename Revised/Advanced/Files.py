#creating a file
import os.path

file = open('./name.csv', 'w')

#reading and writing a file
file = open('./data.csv','r+')
file.write('1,obed,obed@gmail.com\n')
file.write('2,James,james@gmail.com\n')
file.write('3,patience,patience@gmail.com')
file.close()

#reading a file
file = open('./data.csv','r')
print(file.read())
file.close()


#reading line by line
file = open('./data.csv','r')
#for line in file:
#    print(line)
print(file.readlines())

#if we don't want to close each and everytime we access file we can use this way
with open('./data.csv', 'r') as file:
    print(file.read())

filename = './dataq.csv'
if os.path.isfile(filename):
    with open('./data.csv', 'r') as file:
        print(file.read())
else:
    print('filename does not exist')

