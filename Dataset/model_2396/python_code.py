from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TypeData(Enum):
    INT = "INT"
    STRING = "STRING"
    DOUBLE = "DOUBLE"
    BOOLEAN = "BOOLEAN"
    FLOAT = "FLOAT"
    DATE = "DATE"


############################################
# Definition of Classes
############################################

class SqlMetamodel_Column:

    def __init__(self, name: str, type: str, nullable: bool, SqlMetamodel_Column: "SqlMetamodel_Table" = None):
        self.name = name
        self.type = type
        self.nullable = nullable
        self.SqlMetamodel_Column = SqlMetamodel_Column
        
    @property
    def nullable(self) -> bool:
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable

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
    def SqlMetamodel_Column(self):
        return self.__SqlMetamodel_Column

    @SqlMetamodel_Column.setter
    def SqlMetamodel_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SqlMetamodel_Column__SqlMetamodel_Column", None)
        self.__SqlMetamodel_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SqlMetamodel_Table2"):
                opp_val = getattr(old_value, "SqlMetamodel_Table2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SqlMetamodel_Table2"):
                opp_val = getattr(value, "SqlMetamodel_Table2", None)
                if opp_val is None:
                    setattr(value, "SqlMetamodel_Table2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Constraint:

    pass
class SqlMetamodel_ForeingKey(Constraint):

    pass
class SqlMetamodel_PrimaryKey(Constraint):

    pass
class SqlMetamodel_Constraint:

    def __init__(self, name: str, SqlMetamodel_Constraint: "SqlMetamodel_Table" = None):
        self.name = name
        self.SqlMetamodel_Constraint = SqlMetamodel_Constraint
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SqlMetamodel_Constraint(self):
        return self.__SqlMetamodel_Constraint

    @SqlMetamodel_Constraint.setter
    def SqlMetamodel_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SqlMetamodel_Constraint__SqlMetamodel_Constraint", None)
        self.__SqlMetamodel_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SqlMetamodel_Table4"):
                opp_val = getattr(old_value, "SqlMetamodel_Table4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SqlMetamodel_Table4"):
                opp_val = getattr(value, "SqlMetamodel_Table4", None)
                if opp_val is None:
                    setattr(value, "SqlMetamodel_Table4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SqlMetamodel_Table:

    def __init__(self, name: str, SqlMetamodel_Table: "SqlMetamodel_Schema" = None, SqlMetamodel_Table4: set["SqlMetamodel_Constraint"] = None, SqlMetamodel_Table6: "SqlMetamodel_PrimaryKey" = None, SqlMetamodel_Table8: "SqlMetamodel_ForeingKey" = None, SqlMetamodel_Table2: set["SqlMetamodel_Column"] = None):
        self.name = name
        self.SqlMetamodel_Table = SqlMetamodel_Table
        self.SqlMetamodel_Table4 = SqlMetamodel_Table4 if SqlMetamodel_Table4 is not None else set()
        self.SqlMetamodel_Table6 = SqlMetamodel_Table6
        self.SqlMetamodel_Table8 = SqlMetamodel_Table8
        self.SqlMetamodel_Table2 = SqlMetamodel_Table2 if SqlMetamodel_Table2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SqlMetamodel_Table2(self):
        return self.__SqlMetamodel_Table2

    @SqlMetamodel_Table2.setter
    def SqlMetamodel_Table2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SqlMetamodel_Table__SqlMetamodel_Table2", None)
        self.__SqlMetamodel_Table2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SqlMetamodel_Column"):
                    opp_val = getattr(item, "SqlMetamodel_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "SqlMetamodel_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SqlMetamodel_Column"):
                    opp_val = getattr(item, "SqlMetamodel_Column", None)
                    
                    setattr(item, "SqlMetamodel_Column", self)
                    

    @property
    def SqlMetamodel_Table8(self):
        return self.__SqlMetamodel_Table8

    @SqlMetamodel_Table8.setter
    def SqlMetamodel_Table8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SqlMetamodel_Table__SqlMetamodel_Table8", None)
        self.__SqlMetamodel_Table8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SqlMetamodel_ForeingKey"):
                opp_val = getattr(old_value, "SqlMetamodel_ForeingKey", None)
                if opp_val == self:
                    setattr(old_value, "SqlMetamodel_ForeingKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SqlMetamodel_ForeingKey"):
                opp_val = getattr(value, "SqlMetamodel_ForeingKey", None)
                setattr(value, "SqlMetamodel_ForeingKey", self)

    @property
    def SqlMetamodel_Table6(self):
        return self.__SqlMetamodel_Table6

    @SqlMetamodel_Table6.setter
    def SqlMetamodel_Table6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SqlMetamodel_Table__SqlMetamodel_Table6", None)
        self.__SqlMetamodel_Table6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SqlMetamodel_PrimaryKey"):
                opp_val = getattr(old_value, "SqlMetamodel_PrimaryKey", None)
                if opp_val == self:
                    setattr(old_value, "SqlMetamodel_PrimaryKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SqlMetamodel_PrimaryKey"):
                opp_val = getattr(value, "SqlMetamodel_PrimaryKey", None)
                setattr(value, "SqlMetamodel_PrimaryKey", self)

    @property
    def SqlMetamodel_Table(self):
        return self.__SqlMetamodel_Table

    @SqlMetamodel_Table.setter
    def SqlMetamodel_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SqlMetamodel_Table__SqlMetamodel_Table", None)
        self.__SqlMetamodel_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SqlMetamodel_Schema"):
                opp_val = getattr(old_value, "SqlMetamodel_Schema", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SqlMetamodel_Schema"):
                opp_val = getattr(value, "SqlMetamodel_Schema", None)
                if opp_val is None:
                    setattr(value, "SqlMetamodel_Schema", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SqlMetamodel_Table4(self):
        return self.__SqlMetamodel_Table4

    @SqlMetamodel_Table4.setter
    def SqlMetamodel_Table4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SqlMetamodel_Table__SqlMetamodel_Table4", None)
        self.__SqlMetamodel_Table4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SqlMetamodel_Constraint"):
                    opp_val = getattr(item, "SqlMetamodel_Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "SqlMetamodel_Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SqlMetamodel_Constraint"):
                    opp_val = getattr(item, "SqlMetamodel_Constraint", None)
                    
                    setattr(item, "SqlMetamodel_Constraint", self)
                    

class SqlMetamodel_Schema:

    def __init__(self, name: str, SqlMetamodel_Schema: set["SqlMetamodel_Table"] = None):
        self.name = name
        self.SqlMetamodel_Schema = SqlMetamodel_Schema if SqlMetamodel_Schema is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SqlMetamodel_Schema(self):
        return self.__SqlMetamodel_Schema

    @SqlMetamodel_Schema.setter
    def SqlMetamodel_Schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SqlMetamodel_Schema__SqlMetamodel_Schema", None)
        self.__SqlMetamodel_Schema = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SqlMetamodel_Table"):
                    opp_val = getattr(item, "SqlMetamodel_Table", None)
                    
                    if opp_val == self:
                        setattr(item, "SqlMetamodel_Table", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SqlMetamodel_Table"):
                    opp_val = getattr(item, "SqlMetamodel_Table", None)
                    
                    setattr(item, "SqlMetamodel_Table", self)
                    
