def DigitCounter(number): # This function will count how many digits does the given number has.
    if isinstance(number, int):
        result = 0
        while number != 0:
            number //= 10
            result += 1
        return result
    else:
        return "Argument must be a positive integer"

def Delete_Odds(number_list): # This function will delete every odd number in the list
    if isinstance(number_list, list):
        number_list = [i for i in number_list if i%2 == 0]
        return number_list
    else:
        return "Argument must be a number list"
