from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class DataType(Enum):
    VARCHAR255 = "VARCHAR255"
    VARCHAR = "VARCHAR"
    INT = "INT"
    CHAR = "CHAR"
    BOOL = "BOOL"
    DATE = "DATE"
    TIME = "TIME"
    FLOAT = "FLOAT"
    DECIMAL = "DECIMAL"
    NUMERIC = "NUMERIC"


############################################
# Definition of Classes
############################################

class sQL_foreignKey:

    def __init__(self, name: str, sQL_foreignKey8: "sQL_Table" = None, sQL_foreignKey11: "sQL_column" = None, sQL_foreignKey: "sQL_Table" = None):
        self.name = name
        self.sQL_foreignKey8 = sQL_foreignKey8
        self.sQL_foreignKey11 = sQL_foreignKey11
        self.sQL_foreignKey = sQL_foreignKey
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sQL_foreignKey8(self):
        return self.__sQL_foreignKey8

    @sQL_foreignKey8.setter
    def sQL_foreignKey8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sQL_foreignKey__sQL_foreignKey8", None)
        self.__sQL_foreignKey8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sQL_Table9"):
                opp_val = getattr(old_value, "sQL_Table9", None)
                if opp_val == self:
                    setattr(old_value, "sQL_Table9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sQL_Table9"):
                opp_val = getattr(value, "sQL_Table9", None)
                setattr(value, "sQL_Table9", self)

    @property
    def sQL_foreignKey(self):
        return self.__sQL_foreignKey

    @sQL_foreignKey.setter
    def sQL_foreignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sQL_foreignKey__sQL_foreignKey", None)
        self.__sQL_foreignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sQL_Table6"):
                opp_val = getattr(old_value, "sQL_Table6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sQL_Table6"):
                opp_val = getattr(value, "sQL_Table6", None)
                if opp_val is None:
                    setattr(value, "sQL_Table6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sQL_foreignKey11(self):
        return self.__sQL_foreignKey11

    @sQL_foreignKey11.setter
    def sQL_foreignKey11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sQL_foreignKey__sQL_foreignKey11", None)
        self.__sQL_foreignKey11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sQL_column12"):
                opp_val = getattr(old_value, "sQL_column12", None)
                if opp_val == self:
                    setattr(old_value, "sQL_column12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sQL_column12"):
                opp_val = getattr(value, "sQL_column12", None)
                setattr(value, "sQL_column12", self)

class sQL_primaryKey:

    def __init__(self, name: str, sQL_primaryKey: "sQL_Table" = None):
        self.name = name
        self.sQL_primaryKey = sQL_primaryKey
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sQL_primaryKey(self):
        return self.__sQL_primaryKey

    @sQL_primaryKey.setter
    def sQL_primaryKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sQL_primaryKey__sQL_primaryKey", None)
        self.__sQL_primaryKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sQL_Table4"):
                opp_val = getattr(old_value, "sQL_Table4", None)
                if opp_val == self:
                    setattr(old_value, "sQL_Table4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sQL_Table4"):
                opp_val = getattr(value, "sQL_Table4", None)
                setattr(value, "sQL_Table4", self)

class sQL_column:

    def __init__(self, name: str, type: str, sQL_column12: "sQL_foreignKey" = None, sQL_column: "sQL_Table" = None):
        self.name = name
        self.type = type
        self.sQL_column12 = sQL_column12
        self.sQL_column = sQL_column
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def sQL_column12(self):
        return self.__sQL_column12

    @sQL_column12.setter
    def sQL_column12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sQL_column__sQL_column12", None)
        self.__sQL_column12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sQL_foreignKey11"):
                opp_val = getattr(old_value, "sQL_foreignKey11", None)
                if opp_val == self:
                    setattr(old_value, "sQL_foreignKey11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sQL_foreignKey11"):
                opp_val = getattr(value, "sQL_foreignKey11", None)
                setattr(value, "sQL_foreignKey11", self)

    @property
    def sQL_column(self):
        return self.__sQL_column

    @sQL_column.setter
    def sQL_column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sQL_column__sQL_column", None)
        self.__sQL_column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sQL_Table2"):
                opp_val = getattr(old_value, "sQL_Table2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sQL_Table2"):
                opp_val = getattr(value, "sQL_Table2", None)
                if opp_val is None:
                    setattr(value, "sQL_Table2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sQL_Table:

    def __init__(self, name: str, sQL_Table: "sQL_DataBase" = None, sQL_Table9: "sQL_foreignKey" = None, sQL_Table2: set["sQL_column"] = None, sQL_Table4: "sQL_primaryKey" = None, sQL_Table6: set["sQL_foreignKey"] = None):
        self.name = name
        self.sQL_Table = sQL_Table
        self.sQL_Table9 = sQL_Table9
        self.sQL_Table2 = sQL_Table2 if sQL_Table2 is not None else set()
        self.sQL_Table4 = sQL_Table4
        self.sQL_Table6 = sQL_Table6 if sQL_Table6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sQL_Table4(self):
        return self.__sQL_Table4

    @sQL_Table4.setter
    def sQL_Table4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sQL_Table__sQL_Table4", None)
        self.__sQL_Table4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sQL_primaryKey"):
                opp_val = getattr(old_value, "sQL_primaryKey", None)
                if opp_val == self:
                    setattr(old_value, "sQL_primaryKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sQL_primaryKey"):
                opp_val = getattr(value, "sQL_primaryKey", None)
                setattr(value, "sQL_primaryKey", self)

    @property
    def sQL_Table2(self):
        return self.__sQL_Table2

    @sQL_Table2.setter
    def sQL_Table2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sQL_Table__sQL_Table2", None)
        self.__sQL_Table2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sQL_column"):
                    opp_val = getattr(item, "sQL_column", None)
                    
                    if opp_val == self:
                        setattr(item, "sQL_column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sQL_column"):
                    opp_val = getattr(item, "sQL_column", None)
                    
                    setattr(item, "sQL_column", self)
                    

    @property
    def sQL_Table9(self):
        return self.__sQL_Table9

    @sQL_Table9.setter
    def sQL_Table9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sQL_Table__sQL_Table9", None)
        self.__sQL_Table9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sQL_foreignKey8"):
                opp_val = getattr(old_value, "sQL_foreignKey8", None)
                if opp_val == self:
                    setattr(old_value, "sQL_foreignKey8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sQL_foreignKey8"):
                opp_val = getattr(value, "sQL_foreignKey8", None)
                setattr(value, "sQL_foreignKey8", self)

    @property
    def sQL_Table(self):
        return self.__sQL_Table

    @sQL_Table.setter
    def sQL_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sQL_Table__sQL_Table", None)
        self.__sQL_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sQL_DataBase"):
                opp_val = getattr(old_value, "sQL_DataBase", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sQL_DataBase"):
                opp_val = getattr(value, "sQL_DataBase", None)
                if opp_val is None:
                    setattr(value, "sQL_DataBase", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sQL_Table6(self):
        return self.__sQL_Table6

    @sQL_Table6.setter
    def sQL_Table6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sQL_Table__sQL_Table6", None)
        self.__sQL_Table6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sQL_foreignKey"):
                    opp_val = getattr(item, "sQL_foreignKey", None)
                    
                    if opp_val == self:
                        setattr(item, "sQL_foreignKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sQL_foreignKey"):
                    opp_val = getattr(item, "sQL_foreignKey", None)
                    
                    setattr(item, "sQL_foreignKey", self)
                    

class sQL_DataBase:

    pass