def define_max_number(list_):
    list_length = len(list_)

    if list_length == 0:
        return None, None
    elif list_length == 1:
        first_max = list_[0]
        second_max = None
        return first_max, second_max
    else:
        first_max, second_max = (list_[0], list_[1]) if list_[0] > list_[1] else (list_[1], list_[0])
        left_bound = 2
        right_bound = list_length
        first_max, second_max = process_data(list_, left_bound, right_bound, first_max, second_max)
        return first_max, second_max


def process_data(list_, left_bound, right_bound,
                 first_max, second_max):
    if left_bound == right_bound:
        return first_max, second_max

    current_value = list_[left_bound]

    if current_value > first_max:
        first_max = current_value
    elif current_value == first_max or current_value > second_max:
        second_max = current_value

    left_bound += 1
    first_max, second_max = process_data(list_, left_bound, right_bound, first_max, second_max)
    return first_max, second_max


if __name__ == '__main__':
    print(define_max_number([2, 5, 4, 5, 3]))
    print(define_max_number([2, 5]))
    print(define_max_number([5]))
    print(define_max_number([]))
