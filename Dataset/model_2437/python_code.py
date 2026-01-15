from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class DataType(Enum):
    VARCHAR255 = "VARCHAR255"
    INT = "INT"


############################################
# Definition of Classes
############################################

class sql_PrimaryKey:

    pass
class sql_Column:

    def __init__(self, name: str, type: str, isNotNull: bool, sql_Column: "sql_PrimaryKey" = None, sql_Column7: "sql_ForeignKey" = None, sql_Column13: "sql_ForeignKey" = None):
        self.name = name
        self.type = type
        self.isNotNull = isNotNull
        self.sql_Column = sql_Column
        self.sql_Column7 = sql_Column7
        self.sql_Column13 = sql_Column13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isNotNull(self) -> bool:
        return self.__isNotNull

    @isNotNull.setter
    def isNotNull(self, isNotNull: bool):
        self.__isNotNull = isNotNull

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def sql_Column13(self):
        return self.__sql_Column13

    @sql_Column13.setter
    def sql_Column13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Column__sql_Column13", None)
        self.__sql_Column13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_ForeignKey12"):
                opp_val = getattr(old_value, "sql_ForeignKey12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_ForeignKey12"):
                opp_val = getattr(value, "sql_ForeignKey12", None)
                if opp_val is None:
                    setattr(value, "sql_ForeignKey12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sql_Column(self):
        return self.__sql_Column

    @sql_Column.setter
    def sql_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Column__sql_Column", None)
        self.__sql_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_PrimaryKey"):
                opp_val = getattr(old_value, "sql_PrimaryKey", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_PrimaryKey"):
                opp_val = getattr(value, "sql_PrimaryKey", None)
                if opp_val is None:
                    setattr(value, "sql_PrimaryKey", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sql_Column7(self):
        return self.__sql_Column7

    @sql_Column7.setter
    def sql_Column7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Column__sql_Column7", None)
        self.__sql_Column7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_ForeignKey"):
                opp_val = getattr(old_value, "sql_ForeignKey", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_ForeignKey"):
                opp_val = getattr(value, "sql_ForeignKey", None)
                if opp_val is None:
                    setattr(value, "sql_ForeignKey", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sql_EObject:

    pass
class sql_ForeignKey:

    pass
class sql_Table:

    def __init__(self, name: str, sql_Table10: "sql_ForeignKey" = None, sql_Table: "sql_Database" = None, sql_Table4: set["sql_EObject"] = None):
        self.name = name
        self.sql_Table10 = sql_Table10
        self.sql_Table = sql_Table
        self.sql_Table4 = sql_Table4 if sql_Table4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sql_Table10(self):
        return self.__sql_Table10

    @sql_Table10.setter
    def sql_Table10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Table__sql_Table10", None)
        self.__sql_Table10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_ForeignKey9"):
                opp_val = getattr(old_value, "sql_ForeignKey9", None)
                if opp_val == self:
                    setattr(old_value, "sql_ForeignKey9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_ForeignKey9"):
                opp_val = getattr(value, "sql_ForeignKey9", None)
                setattr(value, "sql_ForeignKey9", self)

    @property
    def sql_Table4(self):
        return self.__sql_Table4

    @sql_Table4.setter
    def sql_Table4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Table__sql_Table4", None)
        self.__sql_Table4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sql_EObject"):
                    opp_val = getattr(item, "sql_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "sql_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sql_EObject"):
                    opp_val = getattr(item, "sql_EObject", None)
                    
                    setattr(item, "sql_EObject", self)
                    

    @property
    def sql_Table(self):
        return self.__sql_Table

    @sql_Table.setter
    def sql_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Table__sql_Table", None)
        self.__sql_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sql_Database2"):
                opp_val = getattr(old_value, "sql_Database2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Database2"):
                opp_val = getattr(value, "sql_Database2", None)
                if opp_val is None:
                    setattr(value, "sql_Database2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sql_Database:

    pass
class sql_Model:

    pass