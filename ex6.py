#Enter an age and tell the user whether he or she can receive discounts.
#Auther: Yang Yue

# This program asks the user for their age and informs them about the discounts they are eligible for

try:
    age = int(input("Please enter your age: "))
    if age < 0:
        print("Age cannot be negative.")
    elif age < 19:
        print("You are not eligible for any age-related discounts.")
    elif age == 19:
        print("You are eligible for the student discount.")
    elif 20 <= age <= 54:
        print("You are eligible for the no-age discount.")
    else:  # age >= 55
        print("You are eligible for the senior discount.")
except ValueError:
    print("Please enter a valid age.")
