from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class DB_Column:

    def __init__(self, Name: str, DB_Column: "DB_Table" = None):
        self.Name = Name
        self.DB_Column = DB_Column
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def DB_Column(self):
        return self.__DB_Column

    @DB_Column.setter
    def DB_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_Column__DB_Column", None)
        self.__DB_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DB_Table2"):
                opp_val = getattr(old_value, "DB_Table2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DB_Table2"):
                opp_val = getattr(value, "DB_Table2", None)
                if opp_val is None:
                    setattr(value, "DB_Table2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DB_Table:

    def __init__(self, Name: str, DB_Table: "DB_Database" = None, DB_Table2: set["DB_Column"] = None):
        self.Name = Name
        self.DB_Table = DB_Table
        self.DB_Table2 = DB_Table2 if DB_Table2 is not None else set()
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def DB_Table(self):
        return self.__DB_Table

    @DB_Table.setter
    def DB_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_Table__DB_Table", None)
        self.__DB_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DB_Database"):
                opp_val = getattr(old_value, "DB_Database", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DB_Database"):
                opp_val = getattr(value, "DB_Database", None)
                if opp_val is None:
                    setattr(value, "DB_Database", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DB_Table2(self):
        return self.__DB_Table2

    @DB_Table2.setter
    def DB_Table2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_Table__DB_Table2", None)
        self.__DB_Table2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DB_Column"):
                    opp_val = getattr(item, "DB_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "DB_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DB_Column"):
                    opp_val = getattr(item, "DB_Column", None)
                    
                    setattr(item, "DB_Column", self)
                    

class DB_Database:

    def __init__(self, Name: str, DB_Database: set["DB_Table"] = None):
        self.Name = Name
        self.DB_Database = DB_Database if DB_Database is not None else set()
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def DB_Database(self):
        return self.__DB_Database

    @DB_Database.setter
    def DB_Database(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DB_Database__DB_Database", None)
        self.__DB_Database = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DB_Table"):
                    opp_val = getattr(item, "DB_Table", None)
                    
                    if opp_val == self:
                        setattr(item, "DB_Table", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DB_Table"):
                    opp_val = getattr(item, "DB_Table", None)
                    
                    setattr(item, "DB_Table", self)
                    
