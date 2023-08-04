def print_only_even_idx(list_):
    left_bound = 0
    right_bound = len(list_)
    process_data(list_, left_bound, right_bound)


def process_data(list_, left_bound, right_bound):
    if left_bound == right_bound:
        return

    pointer = left_bound
    is_even_index = pointer % 2 == 0

    if is_even_index:
        elem = list_[pointer]
        is_int_element = isinstance(elem, int)
        if is_int_element:
            print(elem)

    left_bound += 1
    process_data(list_, left_bound, right_bound)


if __name__ == '__main__':
    data = list(range(1, 11))
    print_only_even_idx(data)
