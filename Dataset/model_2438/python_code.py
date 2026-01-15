from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class NamedElement:

    pass
class Sql_Table(NamedElement):

    pass
class Sql_Database(NamedElement):

    pass
class Sql_Column(NamedElement):

    def __init__(self, type: str, Sql_Column: "Sql_Table" = None):
        self.type = type
        self.Sql_Column = Sql_Column
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def Sql_Column(self):
        return self.__Sql_Column

    @Sql_Column.setter
    def Sql_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sql_Column__Sql_Column", None)
        self.__Sql_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sql_Table2"):
                opp_val = getattr(old_value, "Sql_Table2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sql_Table2"):
                opp_val = getattr(value, "Sql_Table2", None)
                if opp_val is None:
                    setattr(value, "Sql_Table2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Sql_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
