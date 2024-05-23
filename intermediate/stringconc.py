x = 'Mugisha '
b = 13
x = "Mugisha {}"
print(x.format(b))#we use format to concatenate strings with non-string variables.
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) # we use index {0} to mention which word is going to concatenate in string.