def define_number_power(number, power):
    if power == 0:
        return 1
    if power == 1:
        return number
    return number * define_number_power(number, power - 1)
