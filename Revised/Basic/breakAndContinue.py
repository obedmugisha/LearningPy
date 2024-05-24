#we can use break and continue to either stops the excution
#or skip certain thing when the condition mets

number = 14
while number > 0:
    if number == 4 or number == 8:
        number -= 1  # Ensure the loop progresses
        continue
    if number == 3:
        break
    number -= 1
    print(number)
