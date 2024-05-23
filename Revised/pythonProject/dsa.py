# here we're going to cover data structures in python
#where data structures are the container to store different data

#list can store any type of data and can be modified
mylist = [2,'Obed',4, 9, 'patience', 9]
mylist[3] = 'Mugisha'
print(mylist)
print(type(mylist))

# Tuples same as list but uses parenthesis and cant be modified
mytuple = (2,'Obed',4, 9, 'patience', 9)
print(mytuple[1])
print(type(mytuple))

#Sets these are like normal sets in General life a group of unrepeated data in a storage
myset = {13, 16, 19, 90, 13, 78}

print(myset)
print(type(myset))

#dictonary with it you can store data with their meaning like

album ={
    'I adore you': 2007,
    'Love not war': 2008,
    'Katapilla': 2022,
    'Where would I be': 2018,
    'As it was': 2017
}
print(album)

print(type(album))
