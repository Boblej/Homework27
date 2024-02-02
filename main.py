class Date:

    def __init__(self,year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __eq__(self, other):
        return self.year == other.year and self.month == other.month and self.day == other.day

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if self.year < other.year:
            return True
        elif self.year == other.year:
            return True
        elif self.month < other.month:
            return False

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return self.__lt__(other)

date1 = Date(2020, 3, 2)
date2 = Date(2022, 4, 5)

print(date1 == date2)
print(date1 < date2)
print(date1 > date2)