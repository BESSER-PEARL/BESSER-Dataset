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
class simplerdbms_ForeignKey(RModelElement):

    pass
class simplerdbms_Key(RModelElement):

    def __init__(self, isPrimary: bool, keys: "simplerdbms_Table" = None, keys13: set["simplerdbms_Column"] = None, Key: "simplerdbms_Column" = None, simplerdbms_Key: "simplerdbms_ForeignKey" = None, Key22: "simplerdbms_Table" = None):
        self.isPrimary = isPrimary
        self.keys = keys
        self.keys13 = keys13 if keys13 is not None else set()
        self.Key = Key
        self.simplerdbms_Key = simplerdbms_Key
        self.Key22 = Key22
        
    @property
    def isPrimary(self) -> bool:
        return self.__isPrimary

    @isPrimary.setter
    def isPrimary(self, isPrimary: bool):
        self.__isPrimary = isPrimary

    @property
    def simplerdbms_Key(self):
        return self.__simplerdbms_Key

    @simplerdbms_Key.setter
    def simplerdbms_Key(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplerdbms_Key__simplerdbms_Key", None)
        self.__simplerdbms_Key = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplerdbms_ForeignKey"):
                opp_val = getattr(old_value, "simplerdbms_ForeignKey", None)
                if opp_val == self:
                    setattr(old_value, "simplerdbms_ForeignKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplerdbms_ForeignKey"):
                opp_val = getattr(value, "simplerdbms_ForeignKey", None)
                setattr(value, "simplerdbms_ForeignKey", self)

    @property
    def Key22(self):
        return self.__Key22

    @Key22.setter
    def Key22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplerdbms_Key__Key22", None)
        self.__Key22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner21"):
                opp_val = getattr(old_value, "owner21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner21"):
                opp_val = getattr(value, "owner21", None)
                if opp_val is None:
                    setattr(value, "owner21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def keys(self):
        return self.__keys

    @keys.setter
    def keys(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplerdbms_Key__keys", None)
        self.__keys = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table11"):
                opp_val = getattr(old_value, "Table11", None)
                if opp_val == self:
                    setattr(old_value, "Table11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table11"):
                opp_val = getattr(value, "Table11", None)
                setattr(value, "Table11", self)

    @property
    def Key(self):
        return self.__Key

    @Key.setter
    def Key(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplerdbms_Key__Key", None)
        self.__Key = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "columns4"):
                opp_val = getattr(old_value, "columns4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "columns4"):
                opp_val = getattr(value, "columns4", None)
                if opp_val is None:
                    setattr(value, "columns4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def keys13(self):
        return self.__keys13

    @keys13.setter
    def keys13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplerdbms_Key__keys13", None)
        self.__keys13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Column14"):
                    opp_val = getattr(item, "Column14", None)
                    
                    if opp_val == self:
                        setattr(item, "Column14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Column14"):
                    opp_val = getattr(item, "Column14", None)
                    
                    setattr(item, "Column14", self)
                    

class simplerdbms_Table(RModelElement):

    pass
class simplerdbms_Column(RModelElement):

    def __init__(self, type: str, columns: "simplerdbms_Table" = None, Column14: "simplerdbms_Key" = None, columns2: set["simplerdbms_ForeignKey"] = None, columns4: set["simplerdbms_Key"] = None, Column: "simplerdbms_ForeignKey" = None, Column18: "simplerdbms_Table" = None):
        self.type = type
        self.columns = columns
        self.Column14 = Column14
        self.columns2 = columns2 if columns2 is not None else set()
        self.columns4 = columns4 if columns4 is not None else set()
        self.Column = Column
        self.Column18 = Column18
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

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
                    
