def define_digit_sum(number: int):
    number_as_string = str(number)

    if len(number_as_string) == 1:
        return number

    left_digit = int(number_as_string[0])
    remaining_number = int(number_as_string[1:])

    return left_digit + define_digit_sum(remaining_number)
