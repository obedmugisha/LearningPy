# looping in a dictionary by using for loops

album ={
    'I adore you': 2007,
    'Love not war': 2008,
    'Katapilla': 2022,
    'Where would I be': 2018,
    'As it was': 2017
}
for key in album:
    print(f'{key} released in {album[key]}')

for key, values in album.items():
    print(f'{key} released in {values}')

print(album.items())