age = int(input("What is your age? "))

print("Your age is %s " % (age,))

while age < 19:
    print("You are too young to view this content")
    age = int(input("What is your age? "))
else:
    print("here are the drugs :)")
