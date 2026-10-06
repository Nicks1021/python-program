age = int(input("Enetr your age: "))

if age < 0:
    print("Invalid Age")
elif age >= 18:
    print("Eligible for Voting")
else:
    print("Not Eligible for voting")
    