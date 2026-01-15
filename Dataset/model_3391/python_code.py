from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class sql_Column:

    def __init__(self, name: str, type: str, PrimaryKey: bool, sql_Column: "sql_Table" = None):
        self.name = name
        self.type = type
        self.PrimaryKey = PrimaryKey
        self.sql_Column = sql_Column
        
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
    def PrimaryKey(self) -> bool:
        return self.__PrimaryKey

    @PrimaryKey.setter
    def PrimaryKey(self, PrimaryKey: bool):
        self.__PrimaryKey = PrimaryKey

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
            if hasattr(old_value, "sql_Table2"):
                opp_val = getattr(old_value, "sql_Table2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Table2"):
                opp_val = getattr(value, "sql_Table2", None)
                if opp_val is None:
                    setattr(value, "sql_Table2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sql_Table:

    def __init__(self, name: str, sql_Table: "sql_Database" = None, sql_Table2: set["sql_Column"] = None):
        self.name = name
        self.sql_Table = sql_Table
        self.sql_Table2 = sql_Table2 if sql_Table2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sql_Table2(self):
        return self.__sql_Table2

    @sql_Table2.setter
    def sql_Table2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Table__sql_Table2", None)
        self.__sql_Table2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sql_Column"):
                    opp_val = getattr(item, "sql_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "sql_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sql_Column"):
                    opp_val = getattr(item, "sql_Column", None)
                    
                    setattr(item, "sql_Column", self)
                    

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
            if hasattr(old_value, "sql_Database"):
                opp_val = getattr(old_value, "sql_Database", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sql_Database"):
                opp_val = getattr(value, "sql_Database", None)
                if opp_val is None:
                    setattr(value, "sql_Database", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sql_Database:

    def __init__(self, name: str, TypeDB: str, sql_Database: set["sql_Table"] = None):
        self.name = name
        self.TypeDB = TypeDB
        self.sql_Database = sql_Database if sql_Database is not None else set()
        
    @property
    def TypeDB(self) -> str:
        return self.__TypeDB

    @TypeDB.setter
    def TypeDB(self, TypeDB: str):
        self.__TypeDB = TypeDB

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sql_Database(self):
        return self.__sql_Database

    @sql_Database.setter
    def sql_Database(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_Database__sql_Database", None)
        self.__sql_Database = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sql_Table"):
                    opp_val = getattr(item, "sql_Table", None)
                    
                    if opp_val == self:
                        setattr(item, "sql_Table", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sql_Table"):
                    opp_val = getattr(item, "sql_Table", None)
                    
                    setattr(item, "sql_Table", self)
                    
