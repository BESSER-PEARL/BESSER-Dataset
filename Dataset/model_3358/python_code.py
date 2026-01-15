from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class RefType:

    pass
class database_Type(RefType):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class RefPKey:

    pass
class database_PKey(RefPKey):

    def __init__(self, name: str, database_PKey: set["database_Column"] = None):
        self.name = name
        self.database_PKey = database_PKey if database_PKey is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def database_PKey(self):
        return self.__database_PKey

    @database_PKey.setter
    def database_PKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_PKey__database_PKey", None)
        self.__database_PKey = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "database_Column21"):
                    opp_val = getattr(item, "database_Column21", None)
                    
                    if opp_val == self:
                        setattr(item, "database_Column21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "database_Column21"):
                    opp_val = getattr(item, "database_Column21", None)
                    
                    setattr(item, "database_Column21", self)
                    

class RefDatabase:

    pass
class database_Database(RefDatabase):

    def __init__(self, name: str, database_Database: set["database_RefTable"] = None, database_Database13: set["database_RefProcedure"] = None):
        self.name = name
        self.database_Database = database_Database if database_Database is not None else set()
        self.database_Database13 = database_Database13 if database_Database13 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def database_Database13(self):
        return self.__database_Database13

    @database_Database13.setter
    def database_Database13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Database__database_Database13", None)
        self.__database_Database13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "database_RefProcedure"):
                    opp_val = getattr(item, "database_RefProcedure", None)
                    
                    if opp_val == self:
                        setattr(item, "database_RefProcedure", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "database_RefProcedure"):
                    opp_val = getattr(item, "database_RefProcedure", None)
                    
                    setattr(item, "database_RefProcedure", self)
                    

    @property
    def database_Database(self):
        return self.__database_Database

    @database_Database.setter
    def database_Database(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Database__database_Database", None)
        self.__database_Database = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "database_RefTable11"):
                    opp_val = getattr(item, "database_RefTable11", None)
                    
                    if opp_val == self:
                        setattr(item, "database_RefTable11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "database_RefTable11"):
                    opp_val = getattr(item, "database_RefTable11", None)
                    
                    setattr(item, "database_RefTable11", self)
                    

class database_RefType(ABC):

    pass
class RefParameter:

    pass
class database_Parameter(RefParameter):

    def __init__(self, name: str, database_Parameter: "database_RefType" = None):
        self.name = name
        self.database_Parameter = database_Parameter
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def database_Parameter(self):
        return self.__database_Parameter

    @database_Parameter.setter
    def database_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Parameter__database_Parameter", None)
        self.__database_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_RefType19"):
                opp_val = getattr(old_value, "database_RefType19", None)
                if opp_val == self:
                    setattr(old_value, "database_RefType19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_RefType19"):
                opp_val = getattr(value, "database_RefType19", None)
                setattr(value, "database_RefType19", self)

class database_RefParameter(ABC):

    pass
class RefProcedure:

    pass
class database_Procedure(RefProcedure):

    def __init__(self, name: str, database_Procedure: set["database_RefParameter"] = None, database_Procedure16: "database_RefType" = None):
        self.name = name
        self.database_Procedure = database_Procedure if database_Procedure is not None else set()
        self.database_Procedure16 = database_Procedure16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def database_Procedure16(self):
        return self.__database_Procedure16

    @database_Procedure16.setter
    def database_Procedure16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Procedure__database_Procedure16", None)
        self.__database_Procedure16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_RefType17"):
                opp_val = getattr(old_value, "database_RefType17", None)
                if opp_val == self:
                    setattr(old_value, "database_RefType17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_RefType17"):
                opp_val = getattr(value, "database_RefType17", None)
                setattr(value, "database_RefType17", self)

    @property
    def database_Procedure(self):
        return self.__database_Procedure

    @database_Procedure.setter
    def database_Procedure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Procedure__database_Procedure", None)
        self.__database_Procedure = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "database_RefParameter"):
                    opp_val = getattr(item, "database_RefParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "database_RefParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "database_RefParameter"):
                    opp_val = getattr(item, "database_RefParameter", None)
                    
                    setattr(item, "database_RefParameter", self)
                    

class database_RefDatabase(ABC):

    pass
class database_RefProcedure(ABC):

    pass
class database_RefFKey(ABC):

    pass
class RefColumn:

    pass
class database_RefTable(ABC):

    pass
class database_Column(RefColumn):

    def __init__(self, name: str, database_Column: "database_FKey" = None, database_Column9: "database_RefType" = None, database_Column21: "database_PKey" = None):
        self.name = name
        self.database_Column = database_Column
        self.database_Column9 = database_Column9
        self.database_Column21 = database_Column21
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def database_Column(self):
        return self.__database_Column

    @database_Column.setter
    def database_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__database_Column", None)
        self.__database_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_FKey"):
                opp_val = getattr(old_value, "database_FKey", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_FKey"):
                opp_val = getattr(value, "database_FKey", None)
                if opp_val is None:
                    setattr(value, "database_FKey", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def database_Column9(self):
        return self.__database_Column9

    @database_Column9.setter
    def database_Column9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__database_Column9", None)
        self.__database_Column9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_RefType"):
                opp_val = getattr(old_value, "database_RefType", None)
                if opp_val == self:
                    setattr(old_value, "database_RefType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_RefType"):
                opp_val = getattr(value, "database_RefType", None)
                setattr(value, "database_RefType", self)

    @property
    def database_Column21(self):
        return self.__database_Column21

    @database_Column21.setter
    def database_Column21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__database_Column21", None)
        self.__database_Column21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_PKey"):
                opp_val = getattr(old_value, "database_PKey", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_PKey"):
                opp_val = getattr(value, "database_PKey", None)
                if opp_val is None:
                    setattr(value, "database_PKey", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class RefFKey:

    pass
class database_FKey(RefFKey):

    def __init__(self, name: str, database_FKey: set["database_Column"] = None, database_FKey7: "database_RefTable" = None):
        self.name = name
        self.database_FKey = database_FKey if database_FKey is not None else set()
        self.database_FKey7 = database_FKey7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def database_FKey7(self):
        return self.__database_FKey7

    @database_FKey7.setter
    def database_FKey7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_FKey__database_FKey7", None)
        self.__database_FKey7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_RefTable"):
                opp_val = getattr(old_value, "database_RefTable", None)
                if opp_val == self:
                    setattr(old_value, "database_RefTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_RefTable"):
                opp_val = getattr(value, "database_RefTable", None)
                setattr(value, "database_RefTable", self)

    @property
    def database_FKey(self):
        return self.__database_FKey

    @database_FKey.setter
    def database_FKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_FKey__database_FKey", None)
        self.__database_FKey = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "database_Column"):
                    opp_val = getattr(item, "database_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "database_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "database_Column"):
                    opp_val = getattr(item, "database_Column", None)
                    
                    setattr(item, "database_Column", self)
                    

class database_RefPKey(ABC):

    pass
class database_RefColumn(ABC):

    pass
class RefTable:

    pass
class database_Table(RefTable):

    def __init__(self, name: str, database_Table: set["database_RefColumn"] = None, database_Table2: set["database_RefPKey"] = None, database_Table4: set["database_RefFKey"] = None):
        self.name = name
        self.database_Table = database_Table if database_Table is not None else set()
        self.database_Table2 = database_Table2 if database_Table2 is not None else set()
        self.database_Table4 = database_Table4 if database_Table4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def database_Table4(self):
        return self.__database_Table4

    @database_Table4.setter
    def database_Table4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Table__database_Table4", None)
        self.__database_Table4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "database_RefFKey"):
                    opp_val = getattr(item, "database_RefFKey", None)
                    
                    if opp_val == self:
                        setattr(item, "database_RefFKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "database_RefFKey"):
                    opp_val = getattr(item, "database_RefFKey", None)
                    
                    setattr(item, "database_RefFKey", self)
                    

    @property
    def database_Table2(self):
        return self.__database_Table2

    @database_Table2.setter
    def database_Table2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Table__database_Table2", None)
        self.__database_Table2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "database_RefPKey"):
                    opp_val = getattr(item, "database_RefPKey", None)
                    
                    if opp_val == self:
                        setattr(item, "database_RefPKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "database_RefPKey"):
                    opp_val = getattr(item, "database_RefPKey", None)
                    
                    setattr(item, "database_RefPKey", self)
                    

    @property
    def database_Table(self):
        return self.__database_Table

    @database_Table.setter
    def database_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Table__database_Table", None)
        self.__database_Table = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "database_RefColumn"):
                    opp_val = getattr(item, "database_RefColumn", None)
                    
                    if opp_val == self:
                        setattr(item, "database_RefColumn", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "database_RefColumn"):
                    opp_val = getattr(item, "database_RefColumn", None)
                    
                    setattr(item, "database_RefColumn", self)
                    
