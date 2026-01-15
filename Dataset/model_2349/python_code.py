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
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class RModelElement:

    pass
class simplerdbms_Schema(RModelElement):

    pass
class simplerdbms_Column(RModelElement):

    def __init__(self, type: str, column: "simplerdbms_Table" = None, column2: set["simplerdbms_ForeignKey"] = None, column4: set["simplerdbms_Key"] = None, Column14: "simplerdbms_Key" = None, Column18: "simplerdbms_Table" = None, Column: "simplerdbms_ForeignKey" = None):
        self.type = type
        self.column = column
        self.column2 = column2 if column2 is not None else set()
        self.column4 = column4 if column4 is not None else set()
        self.Column14 = Column14
        self.Column18 = Column18
        self.Column = Column
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def column2(self):
        return self.__column2

    @column2.setter
    def column2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplerdbms_Column__column2", None)
        self.__column2 = value if value is not None else set()
        
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
    def column(self):
        return self.__column

    @column.setter
    def column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplerdbms_Column__column", None)
        self.__column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table"):
                opp_val = getattr(old_value, "Table", None)
                if opp_val == self:
                    setattr(old_value, "Table", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table"):
                opp_val = getattr(value, "Table", None)
                setattr(value, "Table", self)

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

    @property
    def Column14(self):
        return self.__Column14

    @Column14.setter
    def Column14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplerdbms_Column__Column14", None)
        self.__Column14 = value
        
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
    def Column18(self):
        return self.__Column18

    @Column18.setter
    def Column18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplerdbms_Column__Column18", None)
        self.__Column18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def column4(self):
        return self.__column4

    @column4.setter
    def column4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplerdbms_Column__column4", None)
        self.__column4 = value if value is not None else set()
        
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
                    

class simplerdbms_Key(RModelElement):

    pass
class simplerdbms_ForeignKey(RModelElement):

    pass
class simplerdbms_Table(RModelElement):

    pass