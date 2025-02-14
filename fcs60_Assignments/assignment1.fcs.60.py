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

print("\nExercise 2 ")
print("Even or Odd Number Checker")

n = input("Enter a random number: ")

if n.isdigit():
    n = int(n)

    if n%2 == 0:
        print(f"{n} is an even number")
    else:
        print(f"{n} is an odd number")
else:
    print("Invalid input!")

print("\nExercise 3 ")
print("Simple Login System")

username = "admin" 
password ="1234" 

username_inp = input ("Enter your username:")
password_inp = input("Enter your password")

if username_inp == username and password_inp == password : 
    print("Access granted") 
else:
    print("Access denied")
