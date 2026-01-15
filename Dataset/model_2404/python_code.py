from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ENUM_DATA_TYPE(Enum):
    BOOLEAN = "BOOLEAN"
    CHARACTER = "CHARACTER"
    VARCHAR = "VARCHAR"
    VARYING = "VARYING"
    DATE = "DATE"
    VARBINARY = "VARBINARY"
    BINARY = "BINARY"
    INTEGER = "INTEGER"
    SMALLINT = "SMALLINT"
    INT = "INT"
    BIGINT = "BIGINT"
    DECIMAL = "DECIMAL"
    NUMERIC = "NUMERIC"
    FLOAT = "FLOAT"
    REAL = "REAL"
    VARBINARY_M = "VARBINARY_M"
    BINARY_M = "BINARY_M"
    TIME = "TIME"
    TIMESTAMP = "TIMESTAMP"
    INTERVAL = "INTERVAL"
    ARRAY = "ARRAY"
    MULTISET = "MULTISET"
    XML = "XML"
    CHARACTER_M = "CHARACTER_M"
    VARCHAR_M = "VARCHAR_M"
    VARYING_M = "VARYING_M"
    BOOLEAN_M = "BOOLEAN_M"
    TIMESTAMP_M = "TIMESTAMP_M"
    INTEGER_M = "INTEGER_M"
    SMALLINT_M = "SMALLINT_M"
    INT_M = "INT_M"
    BIGINT_M = "BIGINT_M"
    DECIMAL_M = "DECIMAL_M"
    NUMERIC_M = "NUMERIC_M"
    FLOAT_M = "FLOAT_M"
    REAL_M = "REAL_M"
    DATE_M = "DATE_M"
    TIME_M = "TIME_M"
    INTERVAL_M = "INTERVAL_M"
    ARRAY_M = "ARRAY_M"
    MULTISET_M = "MULTISET_M"
    XML_M = "XML_M"


############################################
# Definition of Classes
############################################

class sqlCrudGenerator_ForeignKey:

    pass
class sqlCrudGenerator_PrimaryKey:

    pass
class sqlCrudGenerator_Column:

    def __init__(self, name: str, sqlCrudGenerator_Column8: "sqlCrudGenerator_DataType" = None, sqlCrudGenerator_Column11: "sqlCrudGenerator_PrimaryKey" = None, sqlCrudGenerator_Column14: "sqlCrudGenerator_ForeignKey" = None, sqlCrudGenerator_Column20: "sqlCrudGenerator_ForeignKey" = None, sqlCrudGenerator_Column: "sqlCrudGenerator_Table" = None):
        self.name = name
        self.sqlCrudGenerator_Column8 = sqlCrudGenerator_Column8
        self.sqlCrudGenerator_Column11 = sqlCrudGenerator_Column11
        self.sqlCrudGenerator_Column14 = sqlCrudGenerator_Column14
        self.sqlCrudGenerator_Column20 = sqlCrudGenerator_Column20
        self.sqlCrudGenerator_Column = sqlCrudGenerator_Column
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sqlCrudGenerator_Column14(self):
        return self.__sqlCrudGenerator_Column14

    @sqlCrudGenerator_Column14.setter
    def sqlCrudGenerator_Column14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlCrudGenerator_Column__sqlCrudGenerator_Column14", None)
        self.__sqlCrudGenerator_Column14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlCrudGenerator_ForeignKey13"):
                opp_val = getattr(old_value, "sqlCrudGenerator_ForeignKey13", None)
                if opp_val == self:
                    setattr(old_value, "sqlCrudGenerator_ForeignKey13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlCrudGenerator_ForeignKey13"):
                opp_val = getattr(value, "sqlCrudGenerator_ForeignKey13", None)
                setattr(value, "sqlCrudGenerator_ForeignKey13", self)

    @property
    def sqlCrudGenerator_Column(self):
        return self.__sqlCrudGenerator_Column

    @sqlCrudGenerator_Column.setter
    def sqlCrudGenerator_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlCrudGenerator_Column__sqlCrudGenerator_Column", None)
        self.__sqlCrudGenerator_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlCrudGenerator_Table2"):
                opp_val = getattr(old_value, "sqlCrudGenerator_Table2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlCrudGenerator_Table2"):
                opp_val = getattr(value, "sqlCrudGenerator_Table2", None)
                if opp_val is None:
                    setattr(value, "sqlCrudGenerator_Table2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sqlCrudGenerator_Column20(self):
        return self.__sqlCrudGenerator_Column20

    @sqlCrudGenerator_Column20.setter
    def sqlCrudGenerator_Column20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlCrudGenerator_Column__sqlCrudGenerator_Column20", None)
        self.__sqlCrudGenerator_Column20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlCrudGenerator_ForeignKey19"):
                opp_val = getattr(old_value, "sqlCrudGenerator_ForeignKey19", None)
                if opp_val == self:
                    setattr(old_value, "sqlCrudGenerator_ForeignKey19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlCrudGenerator_ForeignKey19"):
                opp_val = getattr(value, "sqlCrudGenerator_ForeignKey19", None)
                setattr(value, "sqlCrudGenerator_ForeignKey19", self)

    @property
    def sqlCrudGenerator_Column8(self):
        return self.__sqlCrudGenerator_Column8

    @sqlCrudGenerator_Column8.setter
    def sqlCrudGenerator_Column8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlCrudGenerator_Column__sqlCrudGenerator_Column8", None)
        self.__sqlCrudGenerator_Column8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlCrudGenerator_DataType"):
                opp_val = getattr(old_value, "sqlCrudGenerator_DataType", None)
                if opp_val == self:
                    setattr(old_value, "sqlCrudGenerator_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlCrudGenerator_DataType"):
                opp_val = getattr(value, "sqlCrudGenerator_DataType", None)
                setattr(value, "sqlCrudGenerator_DataType", self)

    @property
    def sqlCrudGenerator_Column11(self):
        return self.__sqlCrudGenerator_Column11

    @sqlCrudGenerator_Column11.setter
    def sqlCrudGenerator_Column11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlCrudGenerator_Column__sqlCrudGenerator_Column11", None)
        self.__sqlCrudGenerator_Column11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlCrudGenerator_PrimaryKey10"):
                opp_val = getattr(old_value, "sqlCrudGenerator_PrimaryKey10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlCrudGenerator_PrimaryKey10"):
                opp_val = getattr(value, "sqlCrudGenerator_PrimaryKey10", None)
                if opp_val is None:
                    setattr(value, "sqlCrudGenerator_PrimaryKey10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sqlCrudGenerator_DataType:

    def __init__(self, dataType: str, precision: int, sqlCrudGenerator_DataType: "sqlCrudGenerator_Column" = None):
        self.dataType = dataType
        self.precision = precision
        self.sqlCrudGenerator_DataType = sqlCrudGenerator_DataType
        
    @property
    def precision(self) -> int:
        return self.__precision

    @precision.setter
    def precision(self, precision: int):
        self.__precision = precision

    @property
    def dataType(self) -> str:
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType

    @property
    def sqlCrudGenerator_DataType(self):
        return self.__sqlCrudGenerator_DataType

    @sqlCrudGenerator_DataType.setter
    def sqlCrudGenerator_DataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlCrudGenerator_DataType__sqlCrudGenerator_DataType", None)
        self.__sqlCrudGenerator_DataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlCrudGenerator_Column8"):
                opp_val = getattr(old_value, "sqlCrudGenerator_Column8", None)
                if opp_val == self:
                    setattr(old_value, "sqlCrudGenerator_Column8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlCrudGenerator_Column8"):
                opp_val = getattr(value, "sqlCrudGenerator_Column8", None)
                setattr(value, "sqlCrudGenerator_Column8", self)

class sqlCrudGenerator_Table:

    def __init__(self, name: str, sqlCrudGenerator_Table: "sqlCrudGenerator_Schema" = None, sqlCrudGenerator_Table6: set["sqlCrudGenerator_ForeignKey"] = None, sqlCrudGenerator_Table17: "sqlCrudGenerator_ForeignKey" = None, sqlCrudGenerator_Table2: set["sqlCrudGenerator_Column"] = None, sqlCrudGenerator_Table4: "sqlCrudGenerator_PrimaryKey" = None):
        self.name = name
        self.sqlCrudGenerator_Table = sqlCrudGenerator_Table
        self.sqlCrudGenerator_Table6 = sqlCrudGenerator_Table6 if sqlCrudGenerator_Table6 is not None else set()
        self.sqlCrudGenerator_Table17 = sqlCrudGenerator_Table17
        self.sqlCrudGenerator_Table2 = sqlCrudGenerator_Table2 if sqlCrudGenerator_Table2 is not None else set()
        self.sqlCrudGenerator_Table4 = sqlCrudGenerator_Table4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sqlCrudGenerator_Table4(self):
        return self.__sqlCrudGenerator_Table4

    @sqlCrudGenerator_Table4.setter
    def sqlCrudGenerator_Table4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlCrudGenerator_Table__sqlCrudGenerator_Table4", None)
        self.__sqlCrudGenerator_Table4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlCrudGenerator_PrimaryKey"):
                opp_val = getattr(old_value, "sqlCrudGenerator_PrimaryKey", None)
                if opp_val == self:
                    setattr(old_value, "sqlCrudGenerator_PrimaryKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlCrudGenerator_PrimaryKey"):
                opp_val = getattr(value, "sqlCrudGenerator_PrimaryKey", None)
                setattr(value, "sqlCrudGenerator_PrimaryKey", self)

    @property
    def sqlCrudGenerator_Table2(self):
        return self.__sqlCrudGenerator_Table2

    @sqlCrudGenerator_Table2.setter
    def sqlCrudGenerator_Table2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlCrudGenerator_Table__sqlCrudGenerator_Table2", None)
        self.__sqlCrudGenerator_Table2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqlCrudGenerator_Column"):
                    opp_val = getattr(item, "sqlCrudGenerator_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "sqlCrudGenerator_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqlCrudGenerator_Column"):
                    opp_val = getattr(item, "sqlCrudGenerator_Column", None)
                    
                    setattr(item, "sqlCrudGenerator_Column", self)
                    

    @property
    def sqlCrudGenerator_Table17(self):
        return self.__sqlCrudGenerator_Table17

    @sqlCrudGenerator_Table17.setter
    def sqlCrudGenerator_Table17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlCrudGenerator_Table__sqlCrudGenerator_Table17", None)
        self.__sqlCrudGenerator_Table17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlCrudGenerator_ForeignKey16"):
                opp_val = getattr(old_value, "sqlCrudGenerator_ForeignKey16", None)
                if opp_val == self:
                    setattr(old_value, "sqlCrudGenerator_ForeignKey16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlCrudGenerator_ForeignKey16"):
                opp_val = getattr(value, "sqlCrudGenerator_ForeignKey16", None)
                setattr(value, "sqlCrudGenerator_ForeignKey16", self)

    @property
    def sqlCrudGenerator_Table6(self):
        return self.__sqlCrudGenerator_Table6

    @sqlCrudGenerator_Table6.setter
    def sqlCrudGenerator_Table6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlCrudGenerator_Table__sqlCrudGenerator_Table6", None)
        self.__sqlCrudGenerator_Table6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqlCrudGenerator_ForeignKey"):
                    opp_val = getattr(item, "sqlCrudGenerator_ForeignKey", None)
                    
                    if opp_val == self:
                        setattr(item, "sqlCrudGenerator_ForeignKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqlCrudGenerator_ForeignKey"):
                    opp_val = getattr(item, "sqlCrudGenerator_ForeignKey", None)
                    
                    setattr(item, "sqlCrudGenerator_ForeignKey", self)
                    

    @property
    def sqlCrudGenerator_Table(self):
        return self.__sqlCrudGenerator_Table

    @sqlCrudGenerator_Table.setter
    def sqlCrudGenerator_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlCrudGenerator_Table__sqlCrudGenerator_Table", None)
        self.__sqlCrudGenerator_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlCrudGenerator_Schema"):
                opp_val = getattr(old_value, "sqlCrudGenerator_Schema", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlCrudGenerator_Schema"):
                opp_val = getattr(value, "sqlCrudGenerator_Schema", None)
                if opp_val is None:
                    setattr(value, "sqlCrudGenerator_Schema", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sqlCrudGenerator_Schema:

    def __init__(self, name: str, sqlCrudGenerator_Schema: set["sqlCrudGenerator_Table"] = None):
        self.name = name
        self.sqlCrudGenerator_Schema = sqlCrudGenerator_Schema if sqlCrudGenerator_Schema is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sqlCrudGenerator_Schema(self):
        return self.__sqlCrudGenerator_Schema

    @sqlCrudGenerator_Schema.setter
    def sqlCrudGenerator_Schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlCrudGenerator_Schema__sqlCrudGenerator_Schema", None)
        self.__sqlCrudGenerator_Schema = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqlCrudGenerator_Table"):
                    opp_val = getattr(item, "sqlCrudGenerator_Table", None)
                    
                    if opp_val == self:
                        setattr(item, "sqlCrudGenerator_Table", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqlCrudGenerator_Table"):
                    opp_val = getattr(item, "sqlCrudGenerator_Table", None)
                    
                    setattr(item, "sqlCrudGenerator_Table", self)
                    
