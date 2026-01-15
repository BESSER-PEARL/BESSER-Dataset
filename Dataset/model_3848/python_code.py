from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Existence:

    pass
class model_NotExists(Existence):

    pass
class model_Exists(Existence):

    pass
class Condition:

    pass
class model_Comparison(Condition):

    def __init__(self, lhs: str, rhs: str, model_Comparison: "model_ComparisonOperator" = None):
        self.lhs = lhs
        self.rhs = rhs
        self.model_Comparison = model_Comparison
        
    @property
    def lhs(self) -> str:
        return self.__lhs

    @lhs.setter
    def lhs(self, lhs: str):
        self.__lhs = lhs

    @property
    def rhs(self) -> str:
        return self.__rhs

    @rhs.setter
    def rhs(self, rhs: str):
        self.__rhs = rhs

    @property
    def model_Comparison(self):
        return self.__model_Comparison

    @model_Comparison.setter
    def model_Comparison(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Comparison__model_Comparison", None)
        self.__model_Comparison = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ComparisonOperator"):
                opp_val = getattr(old_value, "model_ComparisonOperator", None)
                if opp_val == self:
                    setattr(old_value, "model_ComparisonOperator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ComparisonOperator"):
                opp_val = getattr(value, "model_ComparisonOperator", None)
                setattr(value, "model_ComparisonOperator", self)

class BooleanOperation:

    pass
class model_Or(BooleanOperation):

    pass
class model_And(BooleanOperation):

    pass
class model_Existence(Condition):

    pass
class ComparisonOperator:

    pass
class model_NotEquals(ComparisonOperator):

    pass
class model_GreaterThan(ComparisonOperator):

    pass
class model_LessThan(ComparisonOperator):

    pass
class model_Equals(ComparisonOperator):

    pass
class model_ComparisonOperator(ABC):

    pass
class model_BooleanOperation(ABC):

    pass
class model_Condition(ABC):

    pass
class model_TableAlias:

    def __init__(self, name: str, model_TableAlias: "model_Table" = None):
        self.name = name
        self.model_TableAlias = model_TableAlias
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_TableAlias(self):
        return self.__model_TableAlias

    @model_TableAlias.setter
    def model_TableAlias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TableAlias__model_TableAlias", None)
        self.__model_TableAlias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Table12"):
                opp_val = getattr(old_value, "model_Table12", None)
                if opp_val == self:
                    setattr(old_value, "model_Table12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Table12"):
                opp_val = getattr(value, "model_Table12", None)
                setattr(value, "model_Table12", self)

class model_Table:

    def __init__(self, name: str, model_Table: "model_From" = None, model_Table12: "model_TableAlias" = None):
        self.name = name
        self.model_Table = model_Table
        self.model_Table12 = model_Table12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_Table(self):
        return self.__model_Table

    @model_Table.setter
    def model_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Table__model_Table", None)
        self.__model_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_From10"):
                opp_val = getattr(old_value, "model_From10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_From10"):
                opp_val = getattr(value, "model_From10", None)
                if opp_val is None:
                    setattr(value, "model_From10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Table12(self):
        return self.__model_Table12

    @model_Table12.setter
    def model_Table12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Table__model_Table12", None)
        self.__model_Table12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TableAlias"):
                opp_val = getattr(old_value, "model_TableAlias", None)
                if opp_val == self:
                    setattr(old_value, "model_TableAlias", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TableAlias"):
                opp_val = getattr(value, "model_TableAlias", None)
                setattr(value, "model_TableAlias", self)

class model_ColumnAlias:

    def __init__(self, name: str, model_ColumnAlias: "model_Column" = None):
        self.name = name
        self.model_ColumnAlias = model_ColumnAlias
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_ColumnAlias(self):
        return self.__model_ColumnAlias

    @model_ColumnAlias.setter
    def model_ColumnAlias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ColumnAlias__model_ColumnAlias", None)
        self.__model_ColumnAlias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Column8"):
                opp_val = getattr(old_value, "model_Column8", None)
                if opp_val == self:
                    setattr(old_value, "model_Column8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Column8"):
                opp_val = getattr(value, "model_Column8", None)
                setattr(value, "model_Column8", self)

class model_Union:

    pass
class model_Where:

    pass
class model_From:

    pass
class model_Column:

    def __init__(self, name: str, model_Column: "model_Select" = None, model_Column8: "model_ColumnAlias" = None):
        self.name = name
        self.model_Column = model_Column
        self.model_Column8 = model_Column8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_Column(self):
        return self.__model_Column

    @model_Column.setter
    def model_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Column__model_Column", None)
        self.__model_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Select"):
                opp_val = getattr(old_value, "model_Select", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Select"):
                opp_val = getattr(value, "model_Select", None)
                if opp_val is None:
                    setattr(value, "model_Select", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Column8(self):
        return self.__model_Column8

    @model_Column8.setter
    def model_Column8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Column__model_Column8", None)
        self.__model_Column8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ColumnAlias"):
                opp_val = getattr(old_value, "model_ColumnAlias", None)
                if opp_val == self:
                    setattr(old_value, "model_ColumnAlias", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ColumnAlias"):
                opp_val = getattr(value, "model_ColumnAlias", None)
                setattr(value, "model_ColumnAlias", self)

class model_Select:

    pass