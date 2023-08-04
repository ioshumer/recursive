def print_only_even(list_):
    left_bound = 0
    right_bound = len(list_)
    process_data(list_, left_bound, right_bound)


def process_data(list_, left_bound, right_bound):
    if left_bound == right_bound:
        return
    pointer = left_bound
    elem = list_[pointer]

    is_int_element = isinstance(elem, int)
    is_even_element = elem % 2 == 0

    if is_int_element and is_even_element:
        print(elem)

    left_bound += 1
    process_data(list_, left_bound, right_bound)


if __name__ == '__main__':
    data = list(range(1, 11))
    print_only_even(data)
