from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class DataType(Enum):
    String = "String"
    Int = "Int"
    Float = "Float"
    Date = "Date"


############################################
# Definition of Classes
############################################

class database_Column:

    def __init__(self, Name: str, Type: str, IsPrimaryKey: bool, Column: "database_Table" = None, TableColumn: "database_Table" = None, database_Column: "database_ForeignKey" = None, database_Column14: "database_ForeignKey" = None):
        self.Name = Name
        self.Type = Type
        self.IsPrimaryKey = IsPrimaryKey
        self.Column = Column
        self.TableColumn = TableColumn
        self.database_Column = database_Column
        self.database_Column14 = database_Column14
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def IsPrimaryKey(self) -> bool:
        return self.__IsPrimaryKey

    @IsPrimaryKey.setter
    def IsPrimaryKey(self, IsPrimaryKey: bool):
        self.__IsPrimaryKey = IsPrimaryKey

    @property
    def TableColumn(self):
        return self.__TableColumn

    @TableColumn.setter
    def TableColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__TableColumn", None)
        self.__TableColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Table5"):
                opp_val = getattr(old_value, "Table5", None)
                if opp_val == self:
                    setattr(old_value, "Table5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Table5"):
                opp_val = getattr(value, "Table5", None)
                setattr(value, "Table5", self)

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
            if hasattr(old_value, "database_ForeignKey13"):
                opp_val = getattr(old_value, "database_ForeignKey13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_ForeignKey13"):
                opp_val = getattr(value, "database_ForeignKey13", None)
                if opp_val is None:
                    setattr(value, "database_ForeignKey13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "database_ForeignKey11"):
                opp_val = getattr(old_value, "database_ForeignKey11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_ForeignKey11"):
                opp_val = getattr(value, "database_ForeignKey11", None)
                if opp_val is None:
                    setattr(value, "database_ForeignKey11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Column(self):
        return self.__Column

    @Column.setter
    def Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__Column", None)
        self.__Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColumnTable"):
                opp_val = getattr(old_value, "ColumnTable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColumnTable"):
                opp_val = getattr(value, "ColumnTable", None)
                if opp_val is None:
                    setattr(value, "ColumnTable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class database_Table:

    def __init__(self, Name: str, Table: "database_Database" = None, DbTable: "database_Database" = None, ColumnTable: set["database_Column"] = None, Table5: "database_Column" = None, database_Table: "database_ForeignKey" = None, database_Table9: "database_ForeignKey" = None):
        self.Name = Name
        self.Table = Table
        self.DbTable = DbTable
        self.ColumnTable = ColumnTable if ColumnTable is not None else set()
        self.Table5 = Table5
        self.database_Table = database_Table
        self.database_Table9 = database_Table9
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def ColumnTable(self):
        return self.__ColumnTable

    @ColumnTable.setter
    def ColumnTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Table__ColumnTable", None)
        self.__ColumnTable = value if value is not None else set()
        
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
                    

    @property
    def DbTable(self):
        return self.__DbTable

    @DbTable.setter
    def DbTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Table__DbTable", None)
        self.__DbTable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Database"):
                opp_val = getattr(old_value, "Database", None)
                if opp_val == self:
                    setattr(old_value, "Database", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Database"):
                opp_val = getattr(value, "Database", None)
                setattr(value, "Database", self)

    @property
    def Table(self):
        return self.__Table

    @Table.setter
    def Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Table__Table", None)
        self.__Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DbTableRoot"):
                opp_val = getattr(old_value, "DbTableRoot", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DbTableRoot"):
                opp_val = getattr(value, "DbTableRoot", None)
                if opp_val is None:
                    setattr(value, "DbTableRoot", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "database_ForeignKey"):
                opp_val = getattr(old_value, "database_ForeignKey", None)
                if opp_val == self:
                    setattr(old_value, "database_ForeignKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_ForeignKey"):
                opp_val = getattr(value, "database_ForeignKey", None)
                setattr(value, "database_ForeignKey", self)

    @property
    def Table5(self):
        return self.__Table5

    @Table5.setter
    def Table5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Table__Table5", None)
        self.__Table5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TableColumn"):
                opp_val = getattr(old_value, "TableColumn", None)
                if opp_val == self:
                    setattr(old_value, "TableColumn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TableColumn"):
                opp_val = getattr(value, "TableColumn", None)
                setattr(value, "TableColumn", self)

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
            if hasattr(old_value, "database_ForeignKey8"):
                opp_val = getattr(old_value, "database_ForeignKey8", None)
                if opp_val == self:
                    setattr(old_value, "database_ForeignKey8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_ForeignKey8"):
                opp_val = getattr(value, "database_ForeignKey8", None)
                setattr(value, "database_ForeignKey8", self)

class database_ForeignKey:

    def __init__(self, Name: str, ForeignKey: "database_Database" = None, database_ForeignKey: "database_Table" = None, database_ForeignKey8: "database_Table" = None, database_ForeignKey11: set["database_Column"] = None, database_ForeignKey13: set["database_Column"] = None, DbFK: "database_Database" = None):
        self.Name = Name
        self.ForeignKey = ForeignKey
        self.database_ForeignKey = database_ForeignKey
        self.database_ForeignKey8 = database_ForeignKey8
        self.database_ForeignKey11 = database_ForeignKey11 if database_ForeignKey11 is not None else set()
        self.database_ForeignKey13 = database_ForeignKey13 if database_ForeignKey13 is not None else set()
        self.DbFK = DbFK
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def database_ForeignKey8(self):
        return self.__database_ForeignKey8

    @database_ForeignKey8.setter
    def database_ForeignKey8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_ForeignKey__database_ForeignKey8", None)
        self.__database_ForeignKey8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_Table9"):
                opp_val = getattr(old_value, "database_Table9", None)
                if opp_val == self:
                    setattr(old_value, "database_Table9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_Table9"):
                opp_val = getattr(value, "database_Table9", None)
                setattr(value, "database_Table9", self)

    @property
    def ForeignKey(self):
        return self.__ForeignKey

    @ForeignKey.setter
    def ForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_ForeignKey__ForeignKey", None)
        self.__ForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DbFkRoot"):
                opp_val = getattr(old_value, "DbFkRoot", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DbFkRoot"):
                opp_val = getattr(value, "DbFkRoot", None)
                if opp_val is None:
                    setattr(value, "DbFkRoot", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def database_ForeignKey11(self):
        return self.__database_ForeignKey11

    @database_ForeignKey11.setter
    def database_ForeignKey11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_ForeignKey__database_ForeignKey11", None)
        self.__database_ForeignKey11 = value if value is not None else set()
        
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
    def database_ForeignKey(self):
        return self.__database_ForeignKey

    @database_ForeignKey.setter
    def database_ForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_ForeignKey__database_ForeignKey", None)
        self.__database_ForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_Table"):
                opp_val = getattr(old_value, "database_Table", None)
                if opp_val == self:
                    setattr(old_value, "database_Table", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_Table"):
                opp_val = getattr(value, "database_Table", None)
                setattr(value, "database_Table", self)

    @property
    def database_ForeignKey13(self):
        return self.__database_ForeignKey13

    @database_ForeignKey13.setter
    def database_ForeignKey13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_ForeignKey__database_ForeignKey13", None)
        self.__database_ForeignKey13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "database_Column14"):
                    opp_val = getattr(item, "database_Column14", None)
                    
                    if opp_val == self:
                        setattr(item, "database_Column14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "database_Column14"):
                    opp_val = getattr(item, "database_Column14", None)
                    
                    setattr(item, "database_Column14", self)
                    

    @property
    def DbFK(self):
        return self.__DbFK

    @DbFK.setter
    def DbFK(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_ForeignKey__DbFK", None)
        self.__DbFK = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Database16"):
                opp_val = getattr(old_value, "Database16", None)
                if opp_val == self:
                    setattr(old_value, "Database16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Database16"):
                opp_val = getattr(value, "Database16", None)
                setattr(value, "Database16", self)

class database_Database:

    pass