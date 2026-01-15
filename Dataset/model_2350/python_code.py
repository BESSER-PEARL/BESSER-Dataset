from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class simplerdbms_RModelElement(ABC):

    def __init__(self, name: str, kind: str):
        self.name = name
        self.kind = kind
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

class RModelElement:

    pass
class simplerdbms_Key(RModelElement):

    pass
class simplerdbms_ForeignKey(RModelElement):

    pass
class simplerdbms_Table(RModelElement):

    pass
class simplerdbms_Schema(RModelElement):

    pass
class simplerdbms_Column(RModelElement):

    def __init__(self, type: str, simplerdbms_Column: "simplerdbms_Table" = None, column: set["simplerdbms_ForeignKey"] = None, column3: set["simplerdbms_Key"] = None, Column: "simplerdbms_ForeignKey" = None, Column13: "simplerdbms_Key" = None, simplerdbms_Column18: "simplerdbms_Table" = None):
        self.type = type
        self.simplerdbms_Column = simplerdbms_Column
        self.column = column if column is not None else set()
        self.column3 = column3 if column3 is not None else set()
        self.Column = Column
        self.Column13 = Column13
        self.simplerdbms_Column18 = simplerdbms_Column18
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def column(self):
        return self.__column

    @column.setter
    def column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplerdbms_Column__column", None)
        self.__column = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ForeignKey"):
                    opp_val = getattr(item, "ForeignKey", None)
                    
                    if opp_val == self:
                        setattr(item, "ForeignKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ForeignKey"):
                    opp_val = getattr(item, "ForeignKey", None)
                    
                    setattr(item, "ForeignKey", self)
                    

    @property
    def simplerdbms_Column(self):
        return self.__simplerdbms_Column

    @simplerdbms_Column.setter
    def simplerdbms_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplerdbms_Column__simplerdbms_Column", None)
        self.__simplerdbms_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplerdbms_Table"):
                opp_val = getattr(old_value, "simplerdbms_Table", None)
                if opp_val == self:
                    setattr(old_value, "simplerdbms_Table", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplerdbms_Table"):
                opp_val = getattr(value, "simplerdbms_Table", None)
                setattr(value, "simplerdbms_Table", self)

    @property
    def column3(self):
        return self.__column3

    @column3.setter
    def column3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplerdbms_Column__column3", None)
        self.__column3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Key"):
                    opp_val = getattr(item, "Key", None)
                    
                    if opp_val == self:
                        setattr(item, "Key", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Key"):
                    opp_val = getattr(item, "Key", None)
                    
                    setattr(item, "Key", self)
                    

    @property
    def simplerdbms_Column18(self):
        return self.__simplerdbms_Column18

    @simplerdbms_Column18.setter
    def simplerdbms_Column18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplerdbms_Column__simplerdbms_Column18", None)
        self.__simplerdbms_Column18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplerdbms_Table17"):
                opp_val = getattr(old_value, "simplerdbms_Table17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplerdbms_Table17"):
                opp_val = getattr(value, "simplerdbms_Table17", None)
                if opp_val is None:
                    setattr(value, "simplerdbms_Table17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Column13(self):
        return self.__Column13

    @Column13.setter
    def Column13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplerdbms_Column__Column13", None)
        self.__Column13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "key"):
                opp_val = getattr(old_value, "key", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "key"):
                opp_val = getattr(value, "key", None)
                if opp_val is None:
                    setattr(value, "key", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Column(self):
        return self.__Column

    @Column.setter
    def Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplerdbms_Column__Column", None)
        self.__Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "foreignKeys"):
                opp_val = getattr(old_value, "foreignKeys", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "foreignKeys"):
                opp_val = getattr(value, "foreignKeys", None)
                if opp_val is None:
                    setattr(value, "foreignKeys", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
