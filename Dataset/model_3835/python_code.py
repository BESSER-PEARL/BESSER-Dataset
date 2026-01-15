from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Database_Table:

    def __init__(self, heading: str, Database_Table: "Database_DB" = None, Database_Table2: set["Database_Column"] = None):
        self.heading = heading
        self.Database_Table = Database_Table
        self.Database_Table2 = Database_Table2 if Database_Table2 is not None else set()
        
    @property
    def heading(self) -> str:
        return self.__heading

    @heading.setter
    def heading(self, heading: str):
        self.__heading = heading

    @property
    def Database_Table2(self):
        return self.__Database_Table2

    @Database_Table2.setter
    def Database_Table2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Database_Table__Database_Table2", None)
        self.__Database_Table2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Database_Column"):
                    opp_val = getattr(item, "Database_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "Database_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Database_Column"):
                    opp_val = getattr(item, "Database_Column", None)
                    
                    setattr(item, "Database_Column", self)
                    

    @property
    def Database_Table(self):
        return self.__Database_Table

    @Database_Table.setter
    def Database_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Database_Table__Database_Table", None)
        self.__Database_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Database_DB"):
                opp_val = getattr(old_value, "Database_DB", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Database_DB"):
                opp_val = getattr(value, "Database_DB", None)
                if opp_val is None:
                    setattr(value, "Database_DB", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Database_DB:

    def __init__(self, title: str, Database_DB: set["Database_Table"] = None):
        self.title = title
        self.Database_DB = Database_DB if Database_DB is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def Database_DB(self):
        return self.__Database_DB

    @Database_DB.setter
    def Database_DB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Database_DB__Database_DB", None)
        self.__Database_DB = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Database_Table"):
                    opp_val = getattr(item, "Database_Table", None)
                    
                    if opp_val == self:
                        setattr(item, "Database_Table", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Database_Table"):
                    opp_val = getattr(item, "Database_Table", None)
                    
                    setattr(item, "Database_Table", self)
                    

class Database_Column:

    def __init__(self, name: str, Database_Column: "Database_Table" = None):
        self.name = name
        self.Database_Column = Database_Column
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Database_Column(self):
        return self.__Database_Column

    @Database_Column.setter
    def Database_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Database_Column__Database_Column", None)
        self.__Database_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Database_Table2"):
                opp_val = getattr(old_value, "Database_Table2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Database_Table2"):
                opp_val = getattr(value, "Database_Table2", None)
                if opp_val is None:
                    setattr(value, "Database_Table2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
