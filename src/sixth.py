def print_only_even_idx(list_):
    total_list_length = len(list_)
    index_elements = list(range(total_list_length))

    def _recursive_call(list_indexes):
        if len(list_indexes) == 0:
            return
        current_index = list_indexes[0]
        print(current_index)
        if current_index % 2 == 0:
            print(list_[current_index])
        _recursive_call(list_indexes[1:])

    _recursive_call(index_elements)
