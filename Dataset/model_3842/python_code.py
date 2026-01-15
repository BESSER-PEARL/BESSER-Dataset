from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Column:

    pass
class RDBMS_Schema:

    def __init__(self, name: str, RDBMS_Schema: set["Table"] = None):
        self.name = name
        self.RDBMS_Schema = RDBMS_Schema if RDBMS_Schema is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def RDBMS_Schema(self):
        return self.__RDBMS_Schema

    @RDBMS_Schema.setter
    def RDBMS_Schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMS_Schema__RDBMS_Schema", None)
        self.__RDBMS_Schema = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Table11"):
                    opp_val = getattr(item, "Table11", None)
                    
                    if opp_val == self:
                        setattr(item, "Table11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Table11"):
                    opp_val = getattr(item, "Table11", None)
                    
                    setattr(item, "Table11", self)
                    

class Table:

    pass
class RDBMS_FKey:

    pass
class RDBMS_Column:

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class FKey:

    pass
class RDBMS_Table:

    def __init__(self, name: str, tipo: str, RDBMS_Table: set["FKey"] = None, RDBMS_Table2: set["Column"] = None, RDBMS_Table4: set["Column"] = None):
        self.name = name
        self.tipo = tipo
        self.RDBMS_Table = RDBMS_Table if RDBMS_Table is not None else set()
        self.RDBMS_Table2 = RDBMS_Table2 if RDBMS_Table2 is not None else set()
        self.RDBMS_Table4 = RDBMS_Table4 if RDBMS_Table4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tipo(self) -> str:
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: str):
        self.__tipo = tipo

    @property
    def RDBMS_Table4(self):
        return self.__RDBMS_Table4

    @RDBMS_Table4.setter
    def RDBMS_Table4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMS_Table__RDBMS_Table4", None)
        self.__RDBMS_Table4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Column5"):
                    opp_val = getattr(item, "Column5", None)
                    
                    if opp_val == self:
                        setattr(item, "Column5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Column5"):
                    opp_val = getattr(item, "Column5", None)
                    
                    setattr(item, "Column5", self)
                    

    @property
    def RDBMS_Table(self):
        return self.__RDBMS_Table

    @RDBMS_Table.setter
    def RDBMS_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMS_Table__RDBMS_Table", None)
        self.__RDBMS_Table = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FKey"):
                    opp_val = getattr(item, "FKey", None)
                    
                    if opp_val == self:
                        setattr(item, "FKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FKey"):
                    opp_val = getattr(item, "FKey", None)
                    
                    setattr(item, "FKey", self)
                    

    @property
    def RDBMS_Table2(self):
        return self.__RDBMS_Table2

    @RDBMS_Table2.setter
    def RDBMS_Table2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RDBMS_Table__RDBMS_Table2", None)
        self.__RDBMS_Table2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Column"):
                    opp_val = getattr(item, "Column", None)
                    
                    if opp_val == self:
                        setattr(item, "Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Column"):
                    opp_val = getattr(item, "Column", None)
                    
                    setattr(item, "Column", self)
                    
