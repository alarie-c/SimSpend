from random import randint, uniform

class Level:
    name     = 'Undefined Level'
    income   = (0, 0)
    assets   = (0, 0)
    savings  = (0, 0)
    checking = (0, 0)
    variance = (0, 0)
    idx = 0

    def new_income(self) -> int:
        return randint(min(self.income), max(self.income))
    
    def new_assets(self) -> int:
        return randint(min(self.assets), max(self.assets))
    
    def new_savings(self) -> int:
        return randint(min(self.savings), max(self.savings))
    
    def new_checking(self) -> int:
        return randint(min(self.checking), max(self.checking))
    
    def new_variance(self) -> int:
        return uniform(min(self.variance), max(self.variance))

    def __str__(self): return self.name

class LowerClass(Level):
    name     = 'Lower Class'
    income   = (15000, 40000)
    assets   = (5000, 30000)
    savings  = (100, 2000)
    checking = (10, 1000)
    variance = (0.95, 1.15)
    idx = 0

class MiddleClass(Level):
    name     = 'Middle Class'
    income   = (45000, 12000)
    assets   = (100000, 500000)
    savings  = (5000, 15000)
    checking = (1000, 5000)
    variance = (0.90, 1.20)
    idx = 1

class UpperClass(Level):
    name     = 'Upper Class'
    income   = (150000, 1000000)
    assets   = (1000000, 5000000)
    savings  = (50000, 200000)
    checking = (10000, 50000)
    variance = (0.90, 1.80)
    idx = 2

LOWER_CLASS  = LowerClass()
MIDDLE_CLASS = MiddleClass()
UPPER_CLASS  = UpperClass()

LEVEL_IDX = {
    0: LOWER_CLASS,
    1: MIDDLE_CLASS,
    2: UPPER_CLASS
}

# --------------------------------------------------------- #
# Expenses
# --------------------------------------------------------- #

class FixedExpenses:
    rent = (800, 1500, 3000)
    utilities = (150, 200, 350)
    insurance = (200, 300, 750)
    childcare = (400, 900, 1500)

    def new_rent(self, level: Level) -> int:
        v = level.new_variance()
        return self.rent[level.idx] * v
    
    def new_utilities(self, level: Level) -> int:
        v = level.new_variance()
        return self.utilities[level.idx] * v
    
    def new_insurance(self, level: Level) -> int:
        v = level.new_variance()
        return self.insurance[level.idx] * v
    
    def new_childcare(self, level: Level) -> int:
        v = level.new_variance()
        return self.childcare[level.idx] * v        

class VariableExpenses:
    groceries = ()
    transporation = ()
    entertainment = ()
    healthcare = ()
    miscellaneous = ()

FIXED_EXPENSES    = FixedExpenses()
VARAIBLE_EXPENSES = VariableExpenses()