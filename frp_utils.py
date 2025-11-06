def frp_calc_wpm(chars, seconds):
    words = chars / 5
    minutes = seconds / 60
    return round(words / minutes, 2)


class FRPStats:
    def __init__(self):
        self.results = []

    def add(self, value):
        self.results.append(value)

    def last(self):
        if self.results:
            return self.results[-1]
        return None
