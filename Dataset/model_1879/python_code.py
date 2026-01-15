from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class MonthEnum(Enum):
    AUGUST = "AUGUST"
    SEPTEMBER = "SEPTEMBER"
    OCTOBER = "OCTOBER"
    JANUARY = "JANUARY"
    FEBRUARY = "FEBRUARY"
    MARCH = "MARCH"
    APRIL = "APRIL"
    MAY = "MAY"
    JUNE = "JUNE"
    JULY = "JULY"
    NOVEMBER = "NOVEMBER"
    DECEMBER = "DECEMBER"


############################################
# Definition of Classes
############################################

class Transaction:

    pass
class budgeting_CardTransaction(Transaction):

    def __init__(self, day: int, from: str):
        self.day = day
        self.from = from
        
    @property
    def from(self) -> str:
        return self.__from

    @from.setter
    def from(self, from: str):
        self.__from = from

    @property
    def day(self) -> int:
        return self.__day

    @day.setter
    def day(self, day: int):
        self.__day = day

class budgeting_CashTransaction(Transaction):

    def __init__(self, day: str):
        self.day = day
        
    @property
    def day(self) -> str:
        return self.__day

    @day.setter
    def day(self, day: str):
        self.__day = day

class ActualEntry:

    pass
class budgeting_ActualTransactionEntry(ActualEntry):

    pass
class budgeting_ActualAmountEntry(ActualEntry):

    def __init__(self, amount: str):
        self.amount = amount
        
    @property
    def amount(self) -> str:
        return self.__amount

    @amount.setter
    def amount(self, amount: str):
        self.__amount = amount

class BudgetEntry:

    pass
class budgeting_BudgetAmountEntry(BudgetEntry):

    def __init__(self, amount: str):
        self.amount = amount
        
    @property
    def amount(self) -> str:
        return self.__amount

    @amount.setter
    def amount(self, amount: str):
        self.__amount = amount

class Category:

    pass
class budgeting_ExpenseCategory(Category):

    def __init__(self, patterns: str):
        self.patterns = patterns
        
    @property
    def patterns(self) -> str:
        return self.__patterns

    @patterns.setter
    def patterns(self, patterns: str):
        self.__patterns = patterns

class budgeting_IncomeCategory(Category):

    pass
class budgeting_Transaction:

    def __init__(self, amount: str, budgeting_Transaction: "budgeting_ActualTransactionEntry" = None):
        self.amount = amount
        self.budgeting_Transaction = budgeting_Transaction
        
    @property
    def amount(self) -> str:
        return self.__amount

    @amount.setter
    def amount(self, amount: str):
        self.__amount = amount

    @property
    def budgeting_Transaction(self):
        return self.__budgeting_Transaction

    @budgeting_Transaction.setter
    def budgeting_Transaction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_budgeting_Transaction__budgeting_Transaction", None)
        self.__budgeting_Transaction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "budgeting_ActualTransactionEntry"):
                opp_val = getattr(old_value, "budgeting_ActualTransactionEntry", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "budgeting_ActualTransactionEntry"):
                opp_val = getattr(value, "budgeting_ActualTransactionEntry", None)
                if opp_val is None:
                    setattr(value, "budgeting_ActualTransactionEntry", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class budgeting_BudgetFactorEntry(BudgetEntry):

    def __init__(self, factor: float, budgeting_BudgetFactorEntry: "budgeting_BudgetEntry" = None):
        self.factor = factor
        self.budgeting_BudgetFactorEntry = budgeting_BudgetFactorEntry
        
    @property
    def factor(self) -> float:
        return self.__factor

    @factor.setter
    def factor(self, factor: float):
        self.__factor = factor

    @property
    def budgeting_BudgetFactorEntry(self):
        return self.__budgeting_BudgetFactorEntry

    @budgeting_BudgetFactorEntry.setter
    def budgeting_BudgetFactorEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_budgeting_BudgetFactorEntry__budgeting_BudgetFactorEntry", None)
        self.__budgeting_BudgetFactorEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "budgeting_BudgetEntry16"):
                opp_val = getattr(old_value, "budgeting_BudgetEntry16", None)
                if opp_val == self:
                    setattr(old_value, "budgeting_BudgetEntry16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "budgeting_BudgetEntry16"):
                opp_val = getattr(value, "budgeting_BudgetEntry16", None)
                setattr(value, "budgeting_BudgetEntry16", self)

class budgeting_ActualEntry:

    pass
class budgeting_BudgetEntry:

    pass
class budgeting_Month:

    def __init__(self, name: str, budgeting_Month: "budgeting_Year" = None, budgeting_Month6: set["budgeting_BudgetEntry"] = None, budgeting_Month8: set["budgeting_ActualEntry"] = None):
        self.name = name
        self.budgeting_Month = budgeting_Month
        self.budgeting_Month6 = budgeting_Month6 if budgeting_Month6 is not None else set()
        self.budgeting_Month8 = budgeting_Month8 if budgeting_Month8 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def budgeting_Month8(self):
        return self.__budgeting_Month8

    @budgeting_Month8.setter
    def budgeting_Month8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_budgeting_Month__budgeting_Month8", None)
        self.__budgeting_Month8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "budgeting_ActualEntry"):
                    opp_val = getattr(item, "budgeting_ActualEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "budgeting_ActualEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "budgeting_ActualEntry"):
                    opp_val = getattr(item, "budgeting_ActualEntry", None)
                    
                    setattr(item, "budgeting_ActualEntry", self)
                    

    @property
    def budgeting_Month(self):
        return self.__budgeting_Month

    @budgeting_Month.setter
    def budgeting_Month(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_budgeting_Month__budgeting_Month", None)
        self.__budgeting_Month = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "budgeting_Year4"):
                opp_val = getattr(old_value, "budgeting_Year4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "budgeting_Year4"):
                opp_val = getattr(value, "budgeting_Year4", None)
                if opp_val is None:
                    setattr(value, "budgeting_Year4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def budgeting_Month6(self):
        return self.__budgeting_Month6

    @budgeting_Month6.setter
    def budgeting_Month6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_budgeting_Month__budgeting_Month6", None)
        self.__budgeting_Month6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "budgeting_BudgetEntry"):
                    opp_val = getattr(item, "budgeting_BudgetEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "budgeting_BudgetEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "budgeting_BudgetEntry"):
                    opp_val = getattr(item, "budgeting_BudgetEntry", None)
                    
                    setattr(item, "budgeting_BudgetEntry", self)
                    

class budgeting_Category:

    def __init__(self, name: str, budgeting_Category: "budgeting_Library" = None, budgeting_Category11: "budgeting_BudgetEntry" = None, budgeting_Category14: "budgeting_ActualEntry" = None):
        self.name = name
        self.budgeting_Category = budgeting_Category
        self.budgeting_Category11 = budgeting_Category11
        self.budgeting_Category14 = budgeting_Category14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def budgeting_Category11(self):
        return self.__budgeting_Category11

    @budgeting_Category11.setter
    def budgeting_Category11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_budgeting_Category__budgeting_Category11", None)
        self.__budgeting_Category11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "budgeting_BudgetEntry10"):
                opp_val = getattr(old_value, "budgeting_BudgetEntry10", None)
                if opp_val == self:
                    setattr(old_value, "budgeting_BudgetEntry10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "budgeting_BudgetEntry10"):
                opp_val = getattr(value, "budgeting_BudgetEntry10", None)
                setattr(value, "budgeting_BudgetEntry10", self)

    @property
    def budgeting_Category(self):
        return self.__budgeting_Category

    @budgeting_Category.setter
    def budgeting_Category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_budgeting_Category__budgeting_Category", None)
        self.__budgeting_Category = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "budgeting_Library"):
                opp_val = getattr(old_value, "budgeting_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "budgeting_Library"):
                opp_val = getattr(value, "budgeting_Library", None)
                if opp_val is None:
                    setattr(value, "budgeting_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def budgeting_Category14(self):
        return self.__budgeting_Category14

    @budgeting_Category14.setter
    def budgeting_Category14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_budgeting_Category__budgeting_Category14", None)
        self.__budgeting_Category14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "budgeting_ActualEntry13"):
                opp_val = getattr(old_value, "budgeting_ActualEntry13", None)
                if opp_val == self:
                    setattr(old_value, "budgeting_ActualEntry13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "budgeting_ActualEntry13"):
                opp_val = getattr(value, "budgeting_ActualEntry13", None)
                setattr(value, "budgeting_ActualEntry13", self)

class BudgetingFile:

    pass
class budgeting_Year(BudgetingFile):

    def __init__(self, name: int, budgeting_Year: "budgeting_Library" = None, budgeting_Year4: set["budgeting_Month"] = None):
        self.name = name
        self.budgeting_Year = budgeting_Year
        self.budgeting_Year4 = budgeting_Year4 if budgeting_Year4 is not None else set()
        
    @property
    def name(self) -> int:
        return self.__name

    @name.setter
    def name(self, name: int):
        self.__name = name

    @property
    def budgeting_Year(self):
        return self.__budgeting_Year

    @budgeting_Year.setter
    def budgeting_Year(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_budgeting_Year__budgeting_Year", None)
        self.__budgeting_Year = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "budgeting_Library2"):
                opp_val = getattr(old_value, "budgeting_Library2", None)
                if opp_val == self:
                    setattr(old_value, "budgeting_Library2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "budgeting_Library2"):
                opp_val = getattr(value, "budgeting_Library2", None)
                setattr(value, "budgeting_Library2", self)

    @property
    def budgeting_Year4(self):
        return self.__budgeting_Year4

    @budgeting_Year4.setter
    def budgeting_Year4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_budgeting_Year__budgeting_Year4", None)
        self.__budgeting_Year4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "budgeting_Month"):
                    opp_val = getattr(item, "budgeting_Month", None)
                    
                    if opp_val == self:
                        setattr(item, "budgeting_Month", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "budgeting_Month"):
                    opp_val = getattr(item, "budgeting_Month", None)
                    
                    setattr(item, "budgeting_Month", self)
                    

class budgeting_Library(BudgetingFile):

    def __init__(self, name: str, budgeting_Library2: "budgeting_Year" = None, budgeting_Library: set["budgeting_Category"] = None):
        self.name = name
        self.budgeting_Library2 = budgeting_Library2
        self.budgeting_Library = budgeting_Library if budgeting_Library is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def budgeting_Library(self):
        return self.__budgeting_Library

    @budgeting_Library.setter
    def budgeting_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_budgeting_Library__budgeting_Library", None)
        self.__budgeting_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "budgeting_Category"):
                    opp_val = getattr(item, "budgeting_Category", None)
                    
                    if opp_val == self:
                        setattr(item, "budgeting_Category", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "budgeting_Category"):
                    opp_val = getattr(item, "budgeting_Category", None)
                    
                    setattr(item, "budgeting_Category", self)
                    

    @property
    def budgeting_Library2(self):
        return self.__budgeting_Library2

    @budgeting_Library2.setter
    def budgeting_Library2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_budgeting_Library__budgeting_Library2", None)
        self.__budgeting_Library2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "budgeting_Year"):
                opp_val = getattr(old_value, "budgeting_Year", None)
                if opp_val == self:
                    setattr(old_value, "budgeting_Year", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "budgeting_Year"):
                opp_val = getattr(value, "budgeting_Year", None)
                setattr(value, "budgeting_Year", self)

class budgeting_BudgetingFile:

    pass