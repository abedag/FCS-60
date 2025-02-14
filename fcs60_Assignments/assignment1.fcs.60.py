print("Exercise 1")
print("Movie Ticket Price Calculator \n")

age = input("Enter your age: ")

if age.isdigit():
    age = int(age)

    if 1 <= age <= 3:
        print("This age is not allowed")
    elif 4 <= age <= 12:
        print("Ticket costs 5$")
    elif age > 12:
        print("Ticket costs 10$")
    else:
        print("Invalid age")
else:
    print("Invalid input!")
