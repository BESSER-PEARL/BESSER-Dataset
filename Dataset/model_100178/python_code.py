from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class RelationalDBContent_TupleElement:

    def __init__(self, value: str, elements: "Tuple" = None):
        self.value = value
        self.elements = elements
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def elements(self):
        return self.__elements

    @elements.setter
    def elements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RelationalDBContent_TupleElement__elements", None)
        self.__elements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Tuple7"):
                opp_val = getattr(old_value, "Tuple7", None)
                if opp_val == self:
                    setattr(old_value, "Tuple7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Tuple7"):
                opp_val = getattr(value, "Tuple7", None)
                setattr(value, "Tuple7", self)

class TupleElement:

    pass
class RelationalDBContent_Tuple:

    pass
class Tuple:

    pass
class DataBase:

    pass
class Table:

    pass
class NamedElement:

    pass
class RelationalDBContent_Table(NamedElement):

    pass
class RelationalDBContent_DataBase(NamedElement):

    def __init__(self, SGBDname: str, database: set["Table"] = None):
        self.SGBDname = SGBDname
        self.database = database if database is not None else set()
        
        pass
    @property
    def SGBDname(self):
        return self.__SGBDname

    @SGBDname.setter
    def SGBDname(self, SGBDname: str):
        self.__SGBDname = SGBDname


    @property
    def database(self):
        return self.__database

    @database.setter
    def database(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RelationalDBContent_DataBase__database", None)
        self.__database = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Table"):
                    opp_val = getattr(item, "Table", None)
                    
                    if opp_val == self:
                        setattr(item, "Table", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Table"):
                    opp_val = getattr(item, "Table", None)
                    
                    setattr(item, "Table", self)
                    

class RelationalDBContent_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

