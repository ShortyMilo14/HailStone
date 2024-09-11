def GetNumber():
    number = input("Please enter a number: ")
    return int(number)

    # TODO: verify user enters valid number

def IsTheNumberOdd(number):
    # first, get remainder
    # if remainder is zero, number is even
    # if remainder is one, number is odd

    remainder = number % 2

    if (remainder == 0):
        return False
    else:
        return True
    
def CalculateHailStone(number):
    # if number is even, divide by 2
    # if number is odd, multiply by 3 and add one
    # repeat until number equals 1
    
    result = number
    count = 0

    while (result != 1):
        if (IsTheNumberOdd(result) == False):
            result = result / 2
        else:
            result = result * 3 + 1

        print(result)
        count += 1

    print(f"This took {count} steps")


number = GetNumber()
CalculateHailStone(number)