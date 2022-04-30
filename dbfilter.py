
# Bash (test) inspired names
EQ = 0  # Equal          ==
NE = 1  # Not equal      !=
LT = 2  # Less than      <
GT = 3  # Greater than   >
GE = 4  # Greater equal  >=
LE = 5  # Less equal     <=

CMP_MAPPING = {EQ: lambda a, b: a == b,
               NE: lambda a, b: a != b,
               LT: lambda a, b: a < b,
               GT: lambda a, b: a > b,
               GE: lambda a, b: a >= b,
               LE: lambda a, b: a <= b}


class DBFilter:

    def __init__(self, param, cmp, param_value):
        """

        :param param: Column of the table
        :param cmp: Type of comparison
        :param param_value: Value to compare
        """

        self.param = param
        self.cmp = cmp
        self.param_value = param_value

    def apply(self, db):
        # THE HORROR -> lluc, are u okey?
        return db[CMP_MAPPING[self.cmp](db[self.param], self.param_value)]
