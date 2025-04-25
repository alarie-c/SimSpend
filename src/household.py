from names import get_full_name
from random import randint
from expenses import *

class Adult:
    """
    Adults are not agents but model aggregate economically
    relevant factors in a household
    
    Attributes
    ----------
    name : str
        just a basic name, not effect on the simulationy
    income : int
        how much money this adult is making per year
    """

    def __init__(self, level: Level, **kwargs):
        self.name: str = get_full_name()
        self.income: int = level.new_income()

    def last_name(self) -> str:
        _, last = self.name.split(' ', 1)
        return last

class Household:
    """
    Represent a single agent in the simulation and model a number
    of economically relevant factors

    Attributes
    ----------
    name : str
        the last name of a random adult in the house
    adults : list[Adult]
        all adults in the household, [1, 3]
    children : int
        all children in the household, [0, 5]
    savings : float
        all the money the household has in savings
    checking : float
        all the money the household has in their bank account(s)
    assets : float
        represents the aggregate sum of all assets
    """

    def __init__(self, level: Level, **kwargs):
        self.adults: list[Adult] = []
        self.children = randint(0, 5)
        self.level: Level = level

        self.assets   = self.level.new_assets()
        self.savings  = self.level.new_savings()
        self.checking = self.level.new_checking()

        self.rent      = FIXED_EXPENSES.new_rent(self.level)
        self.utilities = FIXED_EXPENSES.new_utilities(self.level)
        self.insurance = FIXED_EXPENSES.new_insurance(self.level)
        self.childcare = FIXED_EXPENSES.new_childcare(self.level)

        # Generate household adults
        n_adults = randint(1, 3)
        for i in range(0, n_adults):
            self.adults.append(Adult(self.level))
        
        # Set the name of the household
        name = self.adults[randint(0, len(self.adults) - 1)].last_name().capitalize()
        self.name = f'The {name} Household'

    def introduce(self) -> None:
        print(f'{self.name}')
        print(f'  | {self.level}')
        print(f'  | {len(self.adults)} adults')
        print(f'  | {self.children} children')
        print(f'  | {self.assets} in assets')
        print(f'  | {self.savings} in savings')
        print(f'  | {self.checking} in checking')
        print(f'  *** Fixed Expenses ***')
        print(f'  | Rent: {self.rent}')
        print(f'  | Utilities: {self.utilities}')
        print(f'  | Insurance: {self.insurance}')
        print(f'  | Childcare: {self.childcare} per child')