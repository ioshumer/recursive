class CustomList:
    def __init__(self, list_of_values):
        self._values: list = list_of_values

    def pop(self):
        if len(self._values):
            return self._values.pop()
        else:
            return None

    def _define_len(self):
        if len(self._values) == 0:
            return 0
        else:
            self.pop()
            sum = 1 + self._define_len()
            return sum

    def __len__(self):
        list_of_values = self._values.copy()
        length = self._define_len()
        self._values = list_of_values
        return length

    def len(self):
        return len(self)
