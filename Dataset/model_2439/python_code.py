from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class database_Column:

    def __init__(self, name: str, type: str, NotNull: bool, PrimaryKey: bool, database_Column: "database_Scheme" = None, Column: "database_Table" = None, columns: "database_Table" = None, database_Column7: "database_Column" = None, database_Column5: "database_Column" = None):
        self.name = name
        self.type = type
        self.NotNull = NotNull
        self.PrimaryKey = PrimaryKey
        self.database_Column = database_Column
        self.Column = Column
        self.columns = columns
        self.database_Column7 = database_Column7
        self.database_Column5 = database_Column5
        
    @property
    def PrimaryKey(self) -> bool:
        return self.__PrimaryKey

    @PrimaryKey.setter
    def PrimaryKey(self, PrimaryKey: bool):
        self.__PrimaryKey = PrimaryKey

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def NotNull(self) -> bool:
        return self.__NotNull

    @NotNull.setter
    def NotNull(self, NotNull: bool):
        self.__NotNull = NotNull

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

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
            if hasattr(old_value, "database_Scheme2"):
                opp_val = getattr(old_value, "database_Scheme2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_Scheme2"):
                opp_val = getattr(value, "database_Scheme2", None)
                if opp_val is None:
                    setattr(value, "database_Scheme2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def database_Column7(self):
        return self.__database_Column7

    @database_Column7.setter
    def database_Column7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__database_Column7", None)
        self.__database_Column7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_Column5"):
                opp_val = getattr(old_value, "database_Column5", None)
                if opp_val == self:
                    setattr(old_value, "database_Column5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_Column5"):
                opp_val = getattr(value, "database_Column5", None)
                setattr(value, "database_Column5", self)

    @property
    def database_Column5(self):
        return self.__database_Column5

    @database_Column5.setter
    def database_Column5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__database_Column5", None)
        self.__database_Column5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_Column7"):
                opp_val = getattr(old_value, "database_Column7", None)
                if opp_val == self:
                    setattr(old_value, "database_Column7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_Column7"):
                opp_val = getattr(value, "database_Column7", None)
                setattr(value, "database_Column7", self)

    @property
    def columns(self):
        return self.__columns

    @columns.setter
    def columns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__columns", None)
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
    def Column(self):
        return self.__Column

    @Column.setter
    def Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__Column", None)
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

class database_Table:

    def __init__(self, name: str, database_Table: "database_Scheme" = None, table: set["database_Column"] = None, Table: "database_Column" = None):
        self.name = name
        self.database_Table = database_Table
        self.table = table if table is not None else set()
        self.Table = Table
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Table__table", None)
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
    def database_Table(self):
        return self.__database_Table

    @database_Table.setter
    def database_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Table__database_Table", None)
        self.__database_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_Scheme"):
                opp_val = getattr(old_value, "database_Scheme", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_Scheme"):
                opp_val = getattr(value, "database_Scheme", None)
                if opp_val is None:
                    setattr(value, "database_Scheme", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "columns"):
                opp_val = getattr(old_value, "columns", None)
                if opp_val == self:
                    setattr(old_value, "columns", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "columns"):
                opp_val = getattr(value, "columns", None)
                setattr(value, "columns", self)

class database_Scheme:

    def __init__(self, name: str, database_Scheme: set["database_Table"] = None, database_Scheme2: set["database_Column"] = None):
        self.name = name
        self.database_Scheme = database_Scheme if database_Scheme is not None else set()
        self.database_Scheme2 = database_Scheme2 if database_Scheme2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def database_Scheme2(self):
        return self.__database_Scheme2

    @database_Scheme2.setter
    def database_Scheme2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Scheme__database_Scheme2", None)
        self.__database_Scheme2 = value if value is not None else set()
        
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
    def database_Scheme(self):
        return self.__database_Scheme

    @database_Scheme.setter
    def database_Scheme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Scheme__database_Scheme", None)
        self.__database_Scheme = value if value is not None else set()
        
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
                    
