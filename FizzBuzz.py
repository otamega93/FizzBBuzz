while (1):

    number = input("put a number here: ")
    if (float(number) % 3 == 0):
        print("Fizz!")
    elif (float(number) % 5 == 0):
        print("Buzz!")
    else:
        print("Nothing")
