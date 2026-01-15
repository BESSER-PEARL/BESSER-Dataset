from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class db_Database:

    pass
class DatabaseElement:

    pass
class db_ForeignKey(DatabaseElement):

    def __init__(self, isMany: str, db_ForeignKey: "db_Column" = None, db_ForeignKey8: "db_Column" = None):
        self.isMany = isMany
        self.db_ForeignKey = db_ForeignKey
        self.db_ForeignKey8 = db_ForeignKey8
        
    @property
    def isMany(self) -> str:
        return self.__isMany

    @isMany.setter
    def isMany(self, isMany: str):
        self.__isMany = isMany

    @property
    def db_ForeignKey8(self):
        return self.__db_ForeignKey8

    @db_ForeignKey8.setter
    def db_ForeignKey8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_ForeignKey__db_ForeignKey8", None)
        self.__db_ForeignKey8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "db_Column9"):
                opp_val = getattr(old_value, "db_Column9", None)
                if opp_val == self:
                    setattr(old_value, "db_Column9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "db_Column9"):
                opp_val = getattr(value, "db_Column9", None)
                setattr(value, "db_Column9", self)

    @property
    def db_ForeignKey(self):
        return self.__db_ForeignKey

    @db_ForeignKey.setter
    def db_ForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_ForeignKey__db_ForeignKey", None)
        self.__db_ForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "db_Column6"):
                opp_val = getattr(old_value, "db_Column6", None)
                if opp_val == self:
                    setattr(old_value, "db_Column6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "db_Column6"):
                opp_val = getattr(value, "db_Column6", None)
                setattr(value, "db_Column6", self)

class db_Column(DatabaseElement):

    def __init__(self, type: str, Column: "db_Table" = None, db_Column: "db_Table" = None, columns: "db_Table" = None, db_Column6: "db_ForeignKey" = None, db_Column9: "db_ForeignKey" = None):
        self.type = type
        self.Column = Column
        self.db_Column = db_Column
        self.columns = columns
        self.db_Column6 = db_Column6
        self.db_Column9 = db_Column9
        
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
        old_value = getattr(self, f"_db_Column__columns", None)
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
    def db_Column9(self):
        return self.__db_Column9

    @db_Column9.setter
    def db_Column9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_Column__db_Column9", None)
        self.__db_Column9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "db_ForeignKey8"):
                opp_val = getattr(old_value, "db_ForeignKey8", None)
                if opp_val == self:
                    setattr(old_value, "db_ForeignKey8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "db_ForeignKey8"):
                opp_val = getattr(value, "db_ForeignKey8", None)
                setattr(value, "db_ForeignKey8", self)

    @property
    def Column(self):
        return self.__Column

    @Column.setter
    def Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_Column__Column", None)
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
    def db_Column(self):
        return self.__db_Column

    @db_Column.setter
    def db_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_Column__db_Column", None)
        self.__db_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "db_Table"):
                opp_val = getattr(old_value, "db_Table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "db_Table"):
                opp_val = getattr(value, "db_Table", None)
                if opp_val is None:
                    setattr(value, "db_Table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def db_Column6(self):
        return self.__db_Column6

    @db_Column6.setter
    def db_Column6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_Column__db_Column6", None)
        self.__db_Column6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "db_ForeignKey"):
                opp_val = getattr(old_value, "db_ForeignKey", None)
                if opp_val == self:
                    setattr(old_value, "db_ForeignKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "db_ForeignKey"):
                opp_val = getattr(value, "db_ForeignKey", None)
                setattr(value, "db_ForeignKey", self)

class db_Table(DatabaseElement):

    pass
class NamedElement:

    pass
class db_DatabaseElement(NamedElement):

    pass
class db_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
