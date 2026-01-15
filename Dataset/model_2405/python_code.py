from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class database_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Index:

    pass
class database_Unique(Index):

    pass
class database_PrimaryKey(Index):

    pass
class NamedElement:

    pass
class database_Index(NamedElement):

    pass
class database_Column(NamedElement):

    def __init__(self, type: str, nullable: bool, default: str, length: int, collation: str, database_Column: "database_Table" = None, database_Column14: "database_Index" = None):
        self.type = type
        self.nullable = nullable
        self.default = default
        self.length = length
        self.collation = collation
        self.database_Column = database_Column
        self.database_Column14 = database_Column14
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def collation(self) -> str:
        return self.__collation

    @collation.setter
    def collation(self, collation: str):
        self.__collation = collation

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def nullable(self) -> bool:
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

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
            if hasattr(old_value, "database_Table5"):
                opp_val = getattr(old_value, "database_Table5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_Table5"):
                opp_val = getattr(value, "database_Table5", None)
                if opp_val is None:
                    setattr(value, "database_Table5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def database_Column14(self):
        return self.__database_Column14

    @database_Column14.setter
    def database_Column14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__database_Column14", None)
        self.__database_Column14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_Index13"):
                opp_val = getattr(old_value, "database_Index13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_Index13"):
                opp_val = getattr(value, "database_Index13", None)
                if opp_val is None:
                    setattr(value, "database_Index13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class database_Table(NamedElement):

    def __init__(self, storageEngine: str, collation: str, database_Table: "database_DataBase" = None, database_Table2: "database_DataBase" = None, database_Table5: set["database_Column"] = None, database_Table7: set["database_Index"] = None, database_Table9: "database_PrimaryKey" = None, database_Table11: set["database_Unique"] = None):
        self.storageEngine = storageEngine
        self.collation = collation
        self.database_Table = database_Table
        self.database_Table2 = database_Table2
        self.database_Table5 = database_Table5 if database_Table5 is not None else set()
        self.database_Table7 = database_Table7 if database_Table7 is not None else set()
        self.database_Table9 = database_Table9
        self.database_Table11 = database_Table11 if database_Table11 is not None else set()
        
    @property
    def collation(self) -> str:
        return self.__collation

    @collation.setter
    def collation(self, collation: str):
        self.__collation = collation

    @property
    def storageEngine(self) -> str:
        return self.__storageEngine

    @storageEngine.setter
    def storageEngine(self, storageEngine: str):
        self.__storageEngine = storageEngine

    @property
    def database_Table(self):
        return self.__database_Table

    @database_Table.setter
    def database_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Table__database_Table", None)
        self.__database_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_DataBase"):
                opp_val = getattr(old_value, "database_DataBase", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_DataBase"):
                opp_val = getattr(value, "database_DataBase", None)
                if opp_val is None:
                    setattr(value, "database_DataBase", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def database_Table2(self):
        return self.__database_Table2

    @database_Table2.setter
    def database_Table2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Table__database_Table2", None)
        self.__database_Table2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_DataBase3"):
                opp_val = getattr(old_value, "database_DataBase3", None)
                if opp_val == self:
                    setattr(old_value, "database_DataBase3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_DataBase3"):
                opp_val = getattr(value, "database_DataBase3", None)
                setattr(value, "database_DataBase3", self)

    @property
    def database_Table7(self):
        return self.__database_Table7

    @database_Table7.setter
    def database_Table7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Table__database_Table7", None)
        self.__database_Table7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "database_Index"):
                    opp_val = getattr(item, "database_Index", None)
                    
                    if opp_val == self:
                        setattr(item, "database_Index", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "database_Index"):
                    opp_val = getattr(item, "database_Index", None)
                    
                    setattr(item, "database_Index", self)
                    

    @property
    def database_Table5(self):
        return self.__database_Table5

    @database_Table5.setter
    def database_Table5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Table__database_Table5", None)
        self.__database_Table5 = value if value is not None else set()
        
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
                    

    @property
    def database_Table11(self):
        return self.__database_Table11

    @database_Table11.setter
    def database_Table11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Table__database_Table11", None)
        self.__database_Table11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "database_Unique"):
                    opp_val = getattr(item, "database_Unique", None)
                    
                    if opp_val == self:
                        setattr(item, "database_Unique", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "database_Unique"):
                    opp_val = getattr(item, "database_Unique", None)
                    
                    setattr(item, "database_Unique", self)
                    

    @property
    def database_Table9(self):
        return self.__database_Table9

    @database_Table9.setter
    def database_Table9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Table__database_Table9", None)
        self.__database_Table9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_PrimaryKey"):
                opp_val = getattr(old_value, "database_PrimaryKey", None)
                if opp_val == self:
                    setattr(old_value, "database_PrimaryKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_PrimaryKey"):
                opp_val = getattr(value, "database_PrimaryKey", None)
                setattr(value, "database_PrimaryKey", self)

    def getIndex(self, indexName: str) -> str:
        # TODO: Implement getIndex method
        pass

    def getColumn(self, columnName: str) -> str:
        # TODO: Implement getColumn method
        pass

class database_DataBase:

    def __init__(self, database_DataBase: set["database_Table"] = None, database_DataBase3: "database_Table" = None):
        self.database_DataBase = database_DataBase if database_DataBase is not None else set()
        self.database_DataBase3 = database_DataBase3
        
    @property
    def database_DataBase(self):
        return self.__database_DataBase

    @database_DataBase.setter
    def database_DataBase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_DataBase__database_DataBase", None)
        self.__database_DataBase = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "database_Table"):
                    opp_val = getattr(item, "database_Table", None)
                    
                    if opp_val == self:
                        setattr(item, "database_Table", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "database_Table"):
                    opp_val = getattr(item, "database_Table", None)
                    
                    setattr(item, "database_Table", self)
                    

    @property
    def database_DataBase3(self):
        return self.__database_DataBase3

    @database_DataBase3.setter
    def database_DataBase3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_DataBase__database_DataBase3", None)
        self.__database_DataBase3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_Table2"):
                opp_val = getattr(old_value, "database_Table2", None)
                if opp_val == self:
                    setattr(old_value, "database_Table2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_Table2"):
                opp_val = getattr(value, "database_Table2", None)
                setattr(value, "database_Table2", self)

    def getTable(self, tableName: str) -> str:
        # TODO: Implement getTable method
        pass
