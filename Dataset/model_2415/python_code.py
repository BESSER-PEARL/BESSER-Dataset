from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class DatabaseElement:

    pass
class DB_ForeignKey(DatabaseElement):

    def __init__(self, isMany: str, DB_ForeignKey: "DB_Column" = None, DB_ForeignKey8: "DB_Column" = None):
        self.isMany = isMany
        self.DB_ForeignKey = DB_ForeignKey
        self.DB_ForeignKey8 = DB_ForeignKey8
        
    @property
    def isMany(self) -> str:
        return self.__isMany

    @isMany.setter
    def isMany(self, isMany: str):
        self.__isMany = isMany

    @property
    def DB_ForeignKey(self):
        return self.__DB_ForeignKey

    @DB_ForeignKey.setter
    def DB_ForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_ForeignKey__DB_ForeignKey", None)
        self.__DB_ForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DB_Column6"):
                opp_val = getattr(old_value, "DB_Column6", None)
                if opp_val == self:
                    setattr(old_value, "DB_Column6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DB_Column6"):
                opp_val = getattr(value, "DB_Column6", None)
                setattr(value, "DB_Column6", self)

    @property
    def DB_ForeignKey8(self):
        return self.__DB_ForeignKey8

    @DB_ForeignKey8.setter
    def DB_ForeignKey8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_ForeignKey__DB_ForeignKey8", None)
        self.__DB_ForeignKey8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DB_Column9"):
                opp_val = getattr(old_value, "DB_Column9", None)
                if opp_val == self:
                    setattr(old_value, "DB_Column9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DB_Column9"):
                opp_val = getattr(value, "DB_Column9", None)
                setattr(value, "DB_Column9", self)

class DB_Table(DatabaseElement):

    pass
class NamedElement:

    pass
class DB_Column(DatabaseElement):

    def __init__(self, type: str, Column: "DB_Table" = None, DB_Column: "DB_Table" = None, columns: "DB_Table" = None, DB_Column6: "DB_ForeignKey" = None, DB_Column9: "DB_ForeignKey" = None):
        self.type = type
        self.Column = Column
        self.DB_Column = DB_Column
        self.columns = columns
        self.DB_Column6 = DB_Column6
        self.DB_Column9 = DB_Column9
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def DB_Column(self):
        return self.__DB_Column

    @DB_Column.setter
    def DB_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_Column__DB_Column", None)
        self.__DB_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DB_Table"):
                opp_val = getattr(old_value, "DB_Table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DB_Table"):
                opp_val = getattr(value, "DB_Table", None)
                if opp_val is None:
                    setattr(value, "DB_Table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Column(self):
        return self.__Column

    @Column.setter
    def Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_Column__Column", None)
        self.__Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table"):
                opp_val = getattr(old_value, "table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table"):
                opp_val = getattr(value, "table", None)
                if opp_val is None:
                    setattr(value, "table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DB_Column6(self):
        return self.__DB_Column6

    @DB_Column6.setter
    def DB_Column6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_Column__DB_Column6", None)
        self.__DB_Column6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DB_ForeignKey"):
                opp_val = getattr(old_value, "DB_ForeignKey", None)
                if opp_val == self:
                    setattr(old_value, "DB_ForeignKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DB_ForeignKey"):
                opp_val = getattr(value, "DB_ForeignKey", None)
                setattr(value, "DB_ForeignKey", self)

    @property
    def DB_Column9(self):
        return self.__DB_Column9

    @DB_Column9.setter
    def DB_Column9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_Column__DB_Column9", None)
        self.__DB_Column9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DB_ForeignKey8"):
                opp_val = getattr(old_value, "DB_ForeignKey8", None)
                if opp_val == self:
                    setattr(old_value, "DB_ForeignKey8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DB_ForeignKey8"):
                opp_val = getattr(value, "DB_ForeignKey8", None)
                setattr(value, "DB_ForeignKey8", self)

    @property
    def columns(self):
        return self.__columns

    @columns.setter
    def columns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_Column__columns", None)
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

class DB_DatabaseElement(NamedElement):

    pass
class DB_Database:

    pass
class DB_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
