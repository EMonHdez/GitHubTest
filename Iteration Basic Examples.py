def DigitCounter(number): # This function will count how many digits does the given number has.
    if isinstance(number, int):
        num = abs(number)
        result = 0
        while num != 0:
            num //= 10
            result += 1
        return result
    else:
        return "Argument must be an integer"

def Replace_Odds(number_list): # This function will replace every odd number in the list with the word "odd"
    if isinstance(number_list, list):
        for i in range (len(number_list)):
            if number_list[i]%2 != 0:
                number_list[i] = 'odd'
        return number_list
    else:
        return "Argument must be a number list"

