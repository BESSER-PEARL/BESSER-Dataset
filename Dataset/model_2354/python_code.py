from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class rdbmsMM_RModelElement(ABC):

    def __init__(self, kind: str, name: str):
        self.kind = kind
        self.name = name
        
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
class rdbmsMM_Schema(RModelElement):

    pass
class rdbmsMM_Key(RModelElement):

    pass
class rdbmsMM_Table(RModelElement):

    pass
class rdbmsMM_ForeignKey(RModelElement):

    pass
class rdbmsMM_Column(RModelElement):

    def __init__(self, type: str, column: "rdbmsMM_Table" = None, column2: set["rdbmsMM_Key"] = None, column4: set["rdbmsMM_ForeignKey"] = None, Column: "rdbmsMM_ForeignKey" = None, Column16: "rdbmsMM_Key" = None, Column23: "rdbmsMM_Table" = None):
        self.type = type
        self.column = column
        self.column2 = column2 if column2 is not None else set()
        self.column4 = column4 if column4 is not None else set()
        self.Column = Column
        self.Column16 = Column16
        self.Column23 = Column23
        
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
        old_value = getattr(self, f"_rdbmsMM_Column__column2", None)
        self.__column2 = value if value is not None else set()
        
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
    def Column23(self):
        return self.__Column23

    @Column23.setter
    def Column23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_Column__Column23", None)
        self.__Column23 = value
        
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
    def Column16(self):
        return self.__Column16

    @Column16.setter
    def Column16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_Column__Column16", None)
        self.__Column16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "key15"):
                opp_val = getattr(old_value, "key15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "key15"):
                opp_val = getattr(value, "key15", None)
                if opp_val is None:
                    setattr(value, "key15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def column(self):
        return self.__column

    @column.setter
    def column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_Column__column", None)
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
    def column4(self):
        return self.__column4

    @column4.setter
    def column4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdbmsMM_Column__column4", None)
        self.__column4 = value if value is not None else set()
        
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
        old_value = getattr(self, f"_rdbmsMM_Column__Column", None)
        self.__Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "foreignKey11"):
                opp_val = getattr(old_value, "foreignKey11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "foreignKey11"):
                opp_val = getattr(value, "foreignKey11", None)
                if opp_val is None:
                    setattr(value, "foreignKey11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
