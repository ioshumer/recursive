def check_palindrom(string):
    if len(string) < 2:
        return True
    if string[0] != string[-1]:
        return False
    return check_palindrom(string[1:-1])
