def define_length(list_):
    if len(list_) == 0:
        return 0
    else:
        list_.pop()
        sum = 1 + define_length(list_)
        return sum
