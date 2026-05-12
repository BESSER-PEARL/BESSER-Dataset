from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ForeignKey:

    pass
class Key:

    pass
class Column:

    pass
class Schema:

    pass
class Table:

    pass
class RModelElement:

    pass
class SimpleRDBMS_Key(RModelElement):

    pass
class SimpleRDBMS_Table(RModelElement):

    pass
class SimpleRDBMS_Column(RModelElement):

    def __init__(self, type: str, column: "Table" = None, column10: set["Key"] = None, column13: set["ForeignKey"] = None):
        self.type = type
        self.column = column
        self.column10 = column10 if column10 is not None else set()
        self.column13 = column13 if column13 is not None else set()
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def column10(self):
        return self.__column10

    @column10.setter
    def column10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleRDBMS_Column__column10", None)
        self.__column10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Key11"):
                    opp_val = getattr(item, "Key11", None)
                    
                    if opp_val == self:
                        setattr(item, "Key11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Key11"):
                    opp_val = getattr(item, "Key11", None)
                    
                    setattr(item, "Key11", self)
                    

    @property
    def column13(self):
        return self.__column13

    @column13.setter
    def column13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleRDBMS_Column__column13", None)
        self.__column13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ForeignKey14"):
                    opp_val = getattr(item, "ForeignKey14", None)
                    
                    if opp_val == self:
                        setattr(item, "ForeignKey14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ForeignKey14"):
                    opp_val = getattr(item, "ForeignKey14", None)
                    
                    setattr(item, "ForeignKey14", self)
                    

    @property
    def column(self):
        return self.__column

    @column.setter
    def column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleRDBMS_Column__column", None)
        self.__column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table8"):
                opp_val = getattr(old_value, "Table8", None)
                if opp_val == self:
                    setattr(old_value, "Table8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table8"):
                opp_val = getattr(value, "Table8", None)
                setattr(value, "Table8", self)

class SimpleRDBMS_ForeignKey(RModelElement):

    pass
class SimpleRDBMS_Schema(RModelElement):

    pass
class SimpleRDBMS_RModelElement(ABC):

    def __init__(self, kind: str, name: str):
        self.kind = kind
        self.name = name
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

