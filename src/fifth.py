def print_only_even(list_):
    if len(list_) == 0:
        return
    elem = list_[0]

    if isinstance(elem, int) and elem % 2 == 0:
        print(elem)

    print_only_even(list_[1:])
