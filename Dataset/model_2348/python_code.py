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

class Key:

    pass
class simplerdbms_Primary_Key(Key):

    pass
class RModelElement:

    pass
class simplerdbms_ForeignKey(RModelElement):

    pass
class simplerdbms_Schema(RModelElement):

    pass
class simplerdbms_Table(RModelElement):

    pass
class simplerdbms_Column(RModelElement):

    def __init__(self, type: str, columns: "simplerdbms_Table" = None, columns2: set["simplerdbms_ForeignKey"] = None, columns4: set["simplerdbms_Key"] = None, Column: "simplerdbms_ForeignKey" = None, Column14: "simplerdbms_Key" = None, Column20: "simplerdbms_Table" = None):
        self.type = type
        self.columns = columns
        self.columns2 = columns2 if columns2 is not None else set()
        self.columns4 = columns4 if columns4 is not None else set()
        self.Column = Column
        self.Column14 = Column14
        self.Column20 = Column20
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def columns(self):
        return self.__columns

    @columns.setter
    def columns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplerdbms_Column__columns", None)
        self.__columns = value
        
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
    def Column20(self):
        return self.__Column20

    @Column20.setter
    def Column20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplerdbms_Column__Column20", None)
        self.__Column20 = value
        
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
    def columns2(self):
        return self.__columns2

    @columns2.setter
    def columns2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplerdbms_Column__columns2", None)
        self.__columns2 = value if value is not None else set()
        
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
    def Column14(self):
        return self.__Column14

    @Column14.setter
    def Column14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplerdbms_Column__Column14", None)
        self.__Column14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "keys13"):
                opp_val = getattr(old_value, "keys13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "keys13"):
                opp_val = getattr(value, "keys13", None)
                if opp_val is None:
                    setattr(value, "keys13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def columns4(self):
        return self.__columns4

    @columns4.setter
    def columns4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplerdbms_Column__columns4", None)
        self.__columns4 = value if value is not None else set()
        
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