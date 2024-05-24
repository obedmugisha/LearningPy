#loops these are the set of actions that keep working till condition become false

#we have while and for loop
count = 10
while count > 0:
    print(count)
    count -=1

while True:
    side = input("Enter the size of your square: ")

    try:
        side = float(side)
        result = side * side
        print(f"The area of the square whose side is {side} is {result}")
    except ValueError:
        print("Please enter a valid number for the size of the square.")

    # Condition to break out of the loop
    continue_loop = input("Do you want to calculate another square area? (yes/no): ").strip().lower()
    if continue_loop != 'yes':
        break

#for looping works when you know the exact number of iteration
friends = {
    'Obed', 'Gaby', 'Patience', 'Christian', 'Christophe'
}

for friend in friends:
    print(friend)