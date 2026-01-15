from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class database_Table:

    def __init__(self, name: str, is_local: bool, database_Table2: set["database_Column"] = None, database_Table4: set["database_ForeignKey"] = None, database_Table6: set["database_Column"] = None, database_Table: "database_Schema" = None, database_Table13: "database_ForeignKey" = None):
        self.name = name
        self.is_local = is_local
        self.database_Table2 = database_Table2 if database_Table2 is not None else set()
        self.database_Table4 = database_Table4 if database_Table4 is not None else set()
        self.database_Table6 = database_Table6 if database_Table6 is not None else set()
        self.database_Table = database_Table
        self.database_Table13 = database_Table13
        
    @property
    def is_local(self) -> bool:
        return self.__is_local

    @is_local.setter
    def is_local(self, is_local: bool):
        self.__is_local = is_local

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "database_Schema"):
                opp_val = getattr(old_value, "database_Schema", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_Schema"):
                opp_val = getattr(value, "database_Schema", None)
                if opp_val is None:
                    setattr(value, "database_Schema", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                if hasattr(item, "database_ForeignKey"):
                    opp_val = getattr(item, "database_ForeignKey", None)
                    
                    if opp_val == self:
                        setattr(item, "database_ForeignKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "database_ForeignKey"):
                    opp_val = getattr(item, "database_ForeignKey", None)
                    
                    setattr(item, "database_ForeignKey", self)
                    

    @property
    def database_Table6(self):
        return self.__database_Table6

    @database_Table6.setter
    def database_Table6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Table__database_Table6", None)
        self.__database_Table6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "database_Column7"):
                    opp_val = getattr(item, "database_Column7", None)
                    
                    if opp_val == self:
                        setattr(item, "database_Column7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "database_Column7"):
                    opp_val = getattr(item, "database_Column7", None)
                    
                    setattr(item, "database_Column7", self)
                    

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
    def database_Table13(self):
        return self.__database_Table13

    @database_Table13.setter
    def database_Table13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Table__database_Table13", None)
        self.__database_Table13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_ForeignKey12"):
                opp_val = getattr(old_value, "database_ForeignKey12", None)
                if opp_val == self:
                    setattr(old_value, "database_ForeignKey12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_ForeignKey12"):
                opp_val = getattr(value, "database_ForeignKey12", None)
                setattr(value, "database_ForeignKey12", self)

class database_Schema:

    def __init__(self, name: str, database_Schema: set["database_Table"] = None):
        self.name = name
        self.database_Schema = database_Schema if database_Schema is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def database_Schema(self):
        return self.__database_Schema

    @database_Schema.setter
    def database_Schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Schema__database_Schema", None)
        self.__database_Schema = value if value is not None else set()
        
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
                    

class database_ForeignKey:

    pass
class database_Column:

    def __init__(self, type: str, name: str, database_Column: "database_Table" = None, database_Column7: "database_Table" = None, database_Column10: "database_ForeignKey" = None):
        self.type = type
        self.name = name
        self.database_Column = database_Column
        self.database_Column7 = database_Column7
        self.database_Column10 = database_Column10
        
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
    def database_Column(self):
        return self.__database_Column

    @database_Column.setter
    def database_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__database_Column", None)
        self.__database_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_Table2"):
                opp_val = getattr(old_value, "database_Table2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_Table2"):
                opp_val = getattr(value, "database_Table2", None)
                if opp_val is None:
                    setattr(value, "database_Table2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def database_Column10(self):
        return self.__database_Column10

    @database_Column10.setter
    def database_Column10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_database_Column__database_Column10", None)
        self.__database_Column10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "database_ForeignKey9"):
                opp_val = getattr(old_value, "database_ForeignKey9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_ForeignKey9"):
                opp_val = getattr(value, "database_ForeignKey9", None)
                if opp_val is None:
                    setattr(value, "database_ForeignKey9", set([self]))
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
            if hasattr(old_value, "database_Table6"):
                opp_val = getattr(old_value, "database_Table6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "database_Table6"):
                opp_val = getattr(value, "database_Table6", None)
                if opp_val is None:
                    setattr(value, "database_Table6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
