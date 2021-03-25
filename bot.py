print('Hello! My name is Alesya.')
print('I was created in 2021.')
print('Please, remind me your name.')

name = input()

print('What a great name you have, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

rem3 = int(input())
rem5 = int(input())
rem7 = int(input())

age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

print("Your age is " + str(age) + "; that's a good time to start programming!")
print('Now I will prove to you that I can count to any number you want.')

# read a number and count to it here
number = int(input())
count = 0
while count <= number:
    print(str(count) + "!")
    count += 1

print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")


def test():
    answer = input()
    while answer != "1":
        print("Please, try again.")
        answer = input()
    if answer == "1":
        print("Completed, have a nice day!")
        print("Congratulations, have a nice day!")


test()
