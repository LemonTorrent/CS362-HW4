def get_Full(first, last):
    fullName = first + " " + last
    return fullName

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")

fullName = get_Full(firstName, lastName)
print("Full name:", fullName)
