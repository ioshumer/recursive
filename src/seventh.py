def define_max_number(list_):

    def _recursive_call(sliced_list):
        nonlocal first_max
        nonlocal second_max
        if len(sliced_list) == 0:
            return
        else:
            current_value = sliced_list[0]
            if current_value > first_max:
                first_max = current_value
            elif current_value == first_max or current_value > second_max:
                second_max = current_value
            _recursive_call(sliced_list[1:])

    list_length = len(list_)

    if list_length == 0:
        return (None, None)
    elif list_length == 1:
        first_max = list_[0]
        second_max = None
        return first_max, second_max
    else:
        first_max, second_max = (list_[0], list_[1]) if list_[0] > list_[1] else (list_[1], list_[0])
        _recursive_call(list_[2:])

    return first_max, second_max


print(define_max_number([2, 5, 4, 5, 3]))
print(define_max_number([2, 5]))
print(define_max_number([5]))
print(define_max_number([]))


