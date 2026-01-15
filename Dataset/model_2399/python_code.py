from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class rdb_Key(ABC):

    pass
class Key:

    pass
class rdb_ForeignKey(Key):

    pass
class rdb_PrimaryKey(Key):

    pass
class rdb_Column:

    def __init__(self, type: str, name: str, rdb_Column: "rdb_Table" = None, rdb_Column7: "rdb_Key" = None, rdb_Column9: "rdb_ForeignKey" = None):
        self.type = type
        self.name = name
        self.rdb_Column = rdb_Column
        self.rdb_Column7 = rdb_Column7
        self.rdb_Column9 = rdb_Column9
        
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

    @property
    def rdb_Column9(self):
        return self.__rdb_Column9

    @rdb_Column9.setter
    def rdb_Column9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_Column__rdb_Column9", None)
        self.__rdb_Column9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdb_ForeignKey"):
                opp_val = getattr(old_value, "rdb_ForeignKey", None)
                if opp_val == self:
                    setattr(old_value, "rdb_ForeignKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdb_ForeignKey"):
                opp_val = getattr(value, "rdb_ForeignKey", None)
                setattr(value, "rdb_ForeignKey", self)

    @property
    def rdb_Column(self):
        return self.__rdb_Column

    @rdb_Column.setter
    def rdb_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_Column__rdb_Column", None)
        self.__rdb_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdb_Table2"):
                opp_val = getattr(old_value, "rdb_Table2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdb_Table2"):
                opp_val = getattr(value, "rdb_Table2", None)
                if opp_val is None:
                    setattr(value, "rdb_Table2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdb_Column7(self):
        return self.__rdb_Column7

    @rdb_Column7.setter
    def rdb_Column7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_Column__rdb_Column7", None)
        self.__rdb_Column7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdb_Key6"):
                opp_val = getattr(old_value, "rdb_Key6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdb_Key6"):
                opp_val = getattr(value, "rdb_Key6", None)
                if opp_val is None:
                    setattr(value, "rdb_Key6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rdb_Table:

    def __init__(self, name: str, rdb_Table: "rdb_Schema" = None, rdb_Table2: set["rdb_Column"] = None, rdb_Table4: set["rdb_Key"] = None):
        self.name = name
        self.rdb_Table = rdb_Table
        self.rdb_Table2 = rdb_Table2 if rdb_Table2 is not None else set()
        self.rdb_Table4 = rdb_Table4 if rdb_Table4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rdb_Table(self):
        return self.__rdb_Table

    @rdb_Table.setter
    def rdb_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_Table__rdb_Table", None)
        self.__rdb_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdb_Schema"):
                opp_val = getattr(old_value, "rdb_Schema", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdb_Schema"):
                opp_val = getattr(value, "rdb_Schema", None)
                if opp_val is None:
                    setattr(value, "rdb_Schema", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdb_Table2(self):
        return self.__rdb_Table2

    @rdb_Table2.setter
    def rdb_Table2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_Table__rdb_Table2", None)
        self.__rdb_Table2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdb_Column"):
                    opp_val = getattr(item, "rdb_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "rdb_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdb_Column"):
                    opp_val = getattr(item, "rdb_Column", None)
                    
                    setattr(item, "rdb_Column", self)
                    

    @property
    def rdb_Table4(self):
        return self.__rdb_Table4

    @rdb_Table4.setter
    def rdb_Table4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_Table__rdb_Table4", None)
        self.__rdb_Table4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdb_Key"):
                    opp_val = getattr(item, "rdb_Key", None)
                    
                    if opp_val == self:
                        setattr(item, "rdb_Key", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdb_Key"):
                    opp_val = getattr(item, "rdb_Key", None)
                    
                    setattr(item, "rdb_Key", self)
                    

class rdb_Schema:

    def __init__(self, name: str, rdb_Schema: set["rdb_Table"] = None):
        self.name = name
        self.rdb_Schema = rdb_Schema if rdb_Schema is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rdb_Schema(self):
        return self.__rdb_Schema

    @rdb_Schema.setter
    def rdb_Schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdb_Schema__rdb_Schema", None)
        self.__rdb_Schema = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdb_Table"):
                    opp_val = getattr(item, "rdb_Table", None)
                    
                    if opp_val == self:
                        setattr(item, "rdb_Table", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdb_Table"):
                    opp_val = getattr(item, "rdb_Table", None)
                    
                    setattr(item, "rdb_Table", self)
                    
