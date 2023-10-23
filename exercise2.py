import os  # import library

os.getcwd()  # check to ensure working directory is correct

text = "INITIAL BUILD"
title = text.center(70, "=")
print(title)

# First, I'll focus on retrieving the elements and setting up the for loop construct
# before I attempt to make changes to the file. This represents my initial build.


requests = []  # empty list
kitty = 500  # create "kitty" variable


with open("loan_requests.txt") as file:  # "with" ensures file is closed upon completion
    requests = [
        line.rstrip() for line in file
    ]  # remove whitespace characters and fill empty requests list
print(
    requests
)  # requests list now contains request values. Still need to convert into integers

requests = [int(line) for line in requests]  # convert strings to integers

for line in requests:
    if line <= kitty:
        print("{} - Paid!".format(line))
        kitty = kitty - line
    elif line > kitty:
        if kitty != 0:
            print(
                "{} request cannot be processed in full (Insufficient funds available). Amount paid: {}".format(
                    line, kitty
                )
            )
            kitty = 0  # crucial line: prevents kitty going into negative values
        else:
            print("Request of {} is UNPAID!".format(line))

# For loop works! Now time to implement changes to the file.
text2 = "FINAL BUILD"
title2 = text2.center(70, "=")
print(title2)


# For that, I'll first need to reset the "kitty" variable.

kitty = 500
# For loop, adding changes to the text file
with open("loan_requests.txt", "a") as file:
    for line in requests:
        if line <= kitty:
            print("{} - Paid!".format(line))
            kitty = kitty - line
            file.write("\nRequest of {} paid in full.".format(line))
        elif line > kitty:
            if kitty != 0:
                print(
                    "{} request cannot be processed in full (Insufficient funds available). Amount paid: {}".format(
                        line, kitty
                    )
                )
                file.write(
                    "\nRequest of {} could not be paid in full. Partial payment of {} made.".format(
                        line, kitty
                    )
                )
                kitty = 0
            else:
                print("Request of {} is UNPAID!".format(line))
                file.write("\nOutstanding Request:{}".format(line))
