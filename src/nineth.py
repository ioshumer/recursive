def parse_parenthesis(string):
    left_bound = 0
    right_bound = len(string)
    result = _process(string, left_bound, right_bound)
    return result


def _process(string, left_bound, right_bound, balance_value=0):
    if left_bound == right_bound:
        return balance_value == 0
    elif balance_value < 0:
        return False
    else:
        current_element = string[left_bound]
        if current_element == "(":
            balance_value += 1
        elif current_element == ")":
            balance_value -= 1

        left_bound += 1

        return _process(string, left_bound, right_bound, balance_value)
