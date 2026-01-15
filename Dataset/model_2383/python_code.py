from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Type(Enum):
    integer = "integer"
    float = "float"
    string = "string"
    datetime = "datetime"
    bool = "bool"


############################################
# Definition of Classes
############################################

class tables_ForeignKey:

    def __init__(self, name: str, ForeignKey: "tables_Column" = None, tables_ForeignKey: "tables_Table" = None, foreign_key: "tables_Column" = None):
        self.name = name
        self.ForeignKey = ForeignKey
        self.tables_ForeignKey = tables_ForeignKey
        self.foreign_key = foreign_key
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ForeignKey(self):
        return self.__ForeignKey

    @ForeignKey.setter
    def ForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tables_ForeignKey__ForeignKey", None)
        self.__ForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "column"):
                opp_val = getattr(old_value, "column", None)
                if opp_val == self:
                    setattr(old_value, "column", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "column"):
                opp_val = getattr(value, "column", None)
                setattr(value, "column", self)

    @property
    def foreign_key(self):
        return self.__foreign_key

    @foreign_key.setter
    def foreign_key(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tables_ForeignKey__foreign_key", None)
        self.__foreign_key = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Column10"):
                opp_val = getattr(old_value, "Column10", None)
                if opp_val == self:
                    setattr(old_value, "Column10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Column10"):
                opp_val = getattr(value, "Column10", None)
                setattr(value, "Column10", self)

    @property
    def tables_ForeignKey(self):
        return self.__tables_ForeignKey

    @tables_ForeignKey.setter
    def tables_ForeignKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tables_ForeignKey__tables_ForeignKey", None)
        self.__tables_ForeignKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tables_Table8"):
                opp_val = getattr(old_value, "tables_Table8", None)
                if opp_val == self:
                    setattr(old_value, "tables_Table8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tables_Table8"):
                opp_val = getattr(value, "tables_Table8", None)
                setattr(value, "tables_Table8", self)

class tables_Column:

    def __init__(self, name: str, type: str, Column: "tables_Table" = None, tables_Column: "tables_Table" = None, column: "tables_ForeignKey" = None, Column10: "tables_ForeignKey" = None, columns: "tables_Table" = None):
        self.name = name
        self.type = type
        self.Column = Column
        self.tables_Column = tables_Column
        self.column = column
        self.Column10 = Column10
        self.columns = columns
        
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
    def tables_Column(self):
        return self.__tables_Column

    @tables_Column.setter
    def tables_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tables_Column__tables_Column", None)
        self.__tables_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tables_Table"):
                opp_val = getattr(old_value, "tables_Table", None)
                if opp_val == self:
                    setattr(old_value, "tables_Table", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tables_Table"):
                opp_val = getattr(value, "tables_Table", None)
                setattr(value, "tables_Table", self)

    @property
    def columns(self):
        return self.__columns

    @columns.setter
    def columns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tables_Column__columns", None)
        self.__columns = value
        
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
    def Column10(self):
        return self.__Column10

    @Column10.setter
    def Column10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tables_Column__Column10", None)
        self.__Column10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "foreign_key"):
                opp_val = getattr(old_value, "foreign_key", None)
                if opp_val == self:
                    setattr(old_value, "foreign_key", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "foreign_key"):
                opp_val = getattr(value, "foreign_key", None)
                setattr(value, "foreign_key", self)

    @property
    def Column(self):
        return self.__Column

    @Column.setter
    def Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tables_Column__Column", None)
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
    def column(self):
        return self.__column

    @column.setter
    def column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tables_Column__column", None)
        self.__column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ForeignKey"):
                opp_val = getattr(old_value, "ForeignKey", None)
                if opp_val == self:
                    setattr(old_value, "ForeignKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ForeignKey"):
                opp_val = getattr(value, "ForeignKey", None)
                setattr(value, "ForeignKey", self)

class tables_Table:

    def __init__(self, name: str, Table: "tables_Database" = None, table: set["tables_Column"] = None, tables: "tables_Database" = None, tables_Table: "tables_Column" = None, tables_Table8: "tables_ForeignKey" = None, Table5: "tables_Column" = None):
        self.name = name
        self.Table = Table
        self.table = table if table is not None else set()
        self.tables = tables
        self.tables_Table = tables_Table
        self.tables_Table8 = tables_Table8
        self.Table5 = Table5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tables_Table8(self):
        return self.__tables_Table8

    @tables_Table8.setter
    def tables_Table8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tables_Table__tables_Table8", None)
        self.__tables_Table8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tables_ForeignKey"):
                opp_val = getattr(old_value, "tables_ForeignKey", None)
                if opp_val == self:
                    setattr(old_value, "tables_ForeignKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tables_ForeignKey"):
                opp_val = getattr(value, "tables_ForeignKey", None)
                setattr(value, "tables_ForeignKey", self)

    @property
    def Table5(self):
        return self.__Table5

    @Table5.setter
    def Table5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tables_Table__Table5", None)
        self.__Table5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "columns"):
                opp_val = getattr(old_value, "columns", None)
                if opp_val == self:
                    setattr(old_value, "columns", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "columns"):
                opp_val = getattr(value, "columns", None)
                setattr(value, "columns", self)

    @property
    def tables_Table(self):
        return self.__tables_Table

    @tables_Table.setter
    def tables_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tables_Table__tables_Table", None)
        self.__tables_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tables_Column"):
                opp_val = getattr(old_value, "tables_Column", None)
                if opp_val == self:
                    setattr(old_value, "tables_Column", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tables_Column"):
                opp_val = getattr(value, "tables_Column", None)
                setattr(value, "tables_Column", self)

    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tables_Table__table", None)
        self.__table = value if value is not None else set()
        
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
    def Table(self):
        return self.__Table

    @Table.setter
    def Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tables_Table__Table", None)
        self.__Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database"):
                opp_val = getattr(old_value, "database", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database"):
                opp_val = getattr(value, "database", None)
                if opp_val is None:
                    setattr(value, "database", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tables(self):
        return self.__tables

    @tables.setter
    def tables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tables_Table__tables", None)
        self.__tables = value
        
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

class tables_Database:

    def __init__(self, name: str, database: set["tables_Table"] = None, Database: "tables_Table" = None):
        self.name = name
        self.database = database if database is not None else set()
        self.Database = Database
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Database(self):
        return self.__Database

    @Database.setter
    def Database(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tables_Database__Database", None)
        self.__Database = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tables"):
                opp_val = getattr(old_value, "tables", None)
                if opp_val == self:
                    setattr(old_value, "tables", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tables"):
                opp_val = getattr(value, "tables", None)
                setattr(value, "tables", self)

    @property
    def database(self):
        return self.__database

    @database.setter
    def database(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tables_Database__database", None)
        self.__database = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Table"):
                    opp_val = getattr(item, "Table", None)
                    
                    if opp_val == self:
                        setattr(item, "Table", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Table"):
                    opp_val = getattr(item, "Table", None)
                    
                    setattr(item, "Table", self)
                    
