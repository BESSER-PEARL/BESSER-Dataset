from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ColumnType(Enum):
    Date = "Date"
    Char = "Char"
    Number = "Number"


############################################
# Definition of Classes
############################################

class NamedElement:

    pass
class my_Column(NamedElement):

    def __init__(self, unique: bool, primary: bool, size: int, type: str, my_Column: "my_Table" = None, my_Column7: "my_FKRelation" = None, my_Column10: "my_FKRelation" = None):
        self.unique = unique
        self.primary = primary
        self.size = size
        self.type = type
        self.my_Column = my_Column
        self.my_Column7 = my_Column7
        self.my_Column10 = my_Column10
        
    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def primary(self) -> bool:
        return self.__primary

    @primary.setter
    def primary(self, primary: bool):
        self.__primary = primary

    @property
    def my_Column(self):
        return self.__my_Column

    @my_Column.setter
    def my_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_my_Column__my_Column", None)
        self.__my_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "my_Table"):
                opp_val = getattr(old_value, "my_Table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "my_Table"):
                opp_val = getattr(value, "my_Table", None)
                if opp_val is None:
                    setattr(value, "my_Table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def my_Column7(self):
        return self.__my_Column7

    @my_Column7.setter
    def my_Column7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_my_Column__my_Column7", None)
        self.__my_Column7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "my_FKRelation6"):
                opp_val = getattr(old_value, "my_FKRelation6", None)
                if opp_val == self:
                    setattr(old_value, "my_FKRelation6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "my_FKRelation6"):
                opp_val = getattr(value, "my_FKRelation6", None)
                setattr(value, "my_FKRelation6", self)

    @property
    def my_Column10(self):
        return self.__my_Column10

    @my_Column10.setter
    def my_Column10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_my_Column__my_Column10", None)
        self.__my_Column10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "my_FKRelation9"):
                opp_val = getattr(old_value, "my_FKRelation9", None)
                if opp_val == self:
                    setattr(old_value, "my_FKRelation9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "my_FKRelation9"):
                opp_val = getattr(value, "my_FKRelation9", None)
                setattr(value, "my_FKRelation9", self)

class my_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class my_FKRelation:

    def __init__(self, label: str, my_FKRelation: "my_Database" = None, my_FKRelation6: "my_Column" = None, my_FKRelation9: "my_Column" = None):
        self.label = label
        self.my_FKRelation = my_FKRelation
        self.my_FKRelation6 = my_FKRelation6
        self.my_FKRelation9 = my_FKRelation9
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def my_FKRelation(self):
        return self.__my_FKRelation

    @my_FKRelation.setter
    def my_FKRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_my_FKRelation__my_FKRelation", None)
        self.__my_FKRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "my_Database4"):
                opp_val = getattr(old_value, "my_Database4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "my_Database4"):
                opp_val = getattr(value, "my_Database4", None)
                if opp_val is None:
                    setattr(value, "my_Database4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def my_FKRelation9(self):
        return self.__my_FKRelation9

    @my_FKRelation9.setter
    def my_FKRelation9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_my_FKRelation__my_FKRelation9", None)
        self.__my_FKRelation9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "my_Column10"):
                opp_val = getattr(old_value, "my_Column10", None)
                if opp_val == self:
                    setattr(old_value, "my_Column10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "my_Column10"):
                opp_val = getattr(value, "my_Column10", None)
                setattr(value, "my_Column10", self)

    @property
    def my_FKRelation6(self):
        return self.__my_FKRelation6

    @my_FKRelation6.setter
    def my_FKRelation6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_my_FKRelation__my_FKRelation6", None)
        self.__my_FKRelation6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "my_Column7"):
                opp_val = getattr(old_value, "my_Column7", None)
                if opp_val == self:
                    setattr(old_value, "my_Column7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "my_Column7"):
                opp_val = getattr(value, "my_Column7", None)
                setattr(value, "my_Column7", self)

class my_Database(NamedElement):

    pass
class my_Table(NamedElement):

    pass