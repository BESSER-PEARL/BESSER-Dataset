from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PrimitiveType(Enum):
    INT = "INT"
    FLOAT = "FLOAT"
    TEXT = "TEXT"
    DATE = "DATE"
    TIMESTAMP = "TIMESTAMP"
    ID = "ID"
    BOOLEAN = "BOOLEAN"


############################################
# Definition of Classes
############################################

class Key:

    pass
class columnFamilyDataModel_Key(ABC):

    pass
class columnFamilyDataModel_Type(ABC):

    pass
class columnFamilyDataModel_ClusteringKey(Key):

    pass
class columnFamilyDataModel_PartitionKey(Key):

    pass
class columnFamilyDataModel_Column:

    def __init__(self, name: str, columnFamilyDataModel_Column: "columnFamilyDataModel_Table" = None, columnFamilyDataModel_Column10: "columnFamilyDataModel_Type" = None, columnFamilyDataModel_Column12: "columnFamilyDataModel_ColumnFamily" = None, columnFamilyDataModel_Column19: "columnFamilyDataModel_Key" = None):
        self.name = name
        self.columnFamilyDataModel_Column = columnFamilyDataModel_Column
        self.columnFamilyDataModel_Column10 = columnFamilyDataModel_Column10
        self.columnFamilyDataModel_Column12 = columnFamilyDataModel_Column12
        self.columnFamilyDataModel_Column19 = columnFamilyDataModel_Column19
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def columnFamilyDataModel_Column10(self):
        return self.__columnFamilyDataModel_Column10

    @columnFamilyDataModel_Column10.setter
    def columnFamilyDataModel_Column10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_columnFamilyDataModel_Column__columnFamilyDataModel_Column10", None)
        self.__columnFamilyDataModel_Column10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "columnFamilyDataModel_Type"):
                opp_val = getattr(old_value, "columnFamilyDataModel_Type", None)
                if opp_val == self:
                    setattr(old_value, "columnFamilyDataModel_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "columnFamilyDataModel_Type"):
                opp_val = getattr(value, "columnFamilyDataModel_Type", None)
                setattr(value, "columnFamilyDataModel_Type", self)

    @property
    def columnFamilyDataModel_Column19(self):
        return self.__columnFamilyDataModel_Column19

    @columnFamilyDataModel_Column19.setter
    def columnFamilyDataModel_Column19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_columnFamilyDataModel_Column__columnFamilyDataModel_Column19", None)
        self.__columnFamilyDataModel_Column19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "columnFamilyDataModel_Key"):
                opp_val = getattr(old_value, "columnFamilyDataModel_Key", None)
                if opp_val == self:
                    setattr(old_value, "columnFamilyDataModel_Key", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "columnFamilyDataModel_Key"):
                opp_val = getattr(value, "columnFamilyDataModel_Key", None)
                setattr(value, "columnFamilyDataModel_Key", self)

    @property
    def columnFamilyDataModel_Column(self):
        return self.__columnFamilyDataModel_Column

    @columnFamilyDataModel_Column.setter
    def columnFamilyDataModel_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_columnFamilyDataModel_Column__columnFamilyDataModel_Column", None)
        self.__columnFamilyDataModel_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "columnFamilyDataModel_Table4"):
                opp_val = getattr(old_value, "columnFamilyDataModel_Table4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "columnFamilyDataModel_Table4"):
                opp_val = getattr(value, "columnFamilyDataModel_Table4", None)
                if opp_val is None:
                    setattr(value, "columnFamilyDataModel_Table4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def columnFamilyDataModel_Column12(self):
        return self.__columnFamilyDataModel_Column12

    @columnFamilyDataModel_Column12.setter
    def columnFamilyDataModel_Column12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_columnFamilyDataModel_Column__columnFamilyDataModel_Column12", None)
        self.__columnFamilyDataModel_Column12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "columnFamilyDataModel_ColumnFamily13"):
                opp_val = getattr(old_value, "columnFamilyDataModel_ColumnFamily13", None)
                if opp_val == self:
                    setattr(old_value, "columnFamilyDataModel_ColumnFamily13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "columnFamilyDataModel_ColumnFamily13"):
                opp_val = getattr(value, "columnFamilyDataModel_ColumnFamily13", None)
                setattr(value, "columnFamilyDataModel_ColumnFamily13", self)

class columnFamilyDataModel_Field:

    def __init__(self, name: str, columnFamilyDataModel_Field: "columnFamilyDataModel_UserDefinedType" = None, columnFamilyDataModel_Field16: "columnFamilyDataModel_Type" = None):
        self.name = name
        self.columnFamilyDataModel_Field = columnFamilyDataModel_Field
        self.columnFamilyDataModel_Field16 = columnFamilyDataModel_Field16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def columnFamilyDataModel_Field(self):
        return self.__columnFamilyDataModel_Field

    @columnFamilyDataModel_Field.setter
    def columnFamilyDataModel_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_columnFamilyDataModel_Field__columnFamilyDataModel_Field", None)
        self.__columnFamilyDataModel_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "columnFamilyDataModel_UserDefinedType"):
                opp_val = getattr(old_value, "columnFamilyDataModel_UserDefinedType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "columnFamilyDataModel_UserDefinedType"):
                opp_val = getattr(value, "columnFamilyDataModel_UserDefinedType", None)
                if opp_val is None:
                    setattr(value, "columnFamilyDataModel_UserDefinedType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def columnFamilyDataModel_Field16(self):
        return self.__columnFamilyDataModel_Field16

    @columnFamilyDataModel_Field16.setter
    def columnFamilyDataModel_Field16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_columnFamilyDataModel_Field__columnFamilyDataModel_Field16", None)
        self.__columnFamilyDataModel_Field16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "columnFamilyDataModel_Type17"):
                opp_val = getattr(old_value, "columnFamilyDataModel_Type17", None)
                if opp_val == self:
                    setattr(old_value, "columnFamilyDataModel_Type17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "columnFamilyDataModel_Type17"):
                opp_val = getattr(value, "columnFamilyDataModel_Type17", None)
                setattr(value, "columnFamilyDataModel_Type17", self)

class Collection:

    pass
class columnFamilyDataModel_Set(Collection):

    pass
class columnFamilyDataModel_Map(Collection):

    def __init__(self, keyType: str):
        self.keyType = keyType
        
    @property
    def keyType(self) -> str:
        return self.__keyType

    @keyType.setter
    def keyType(self, keyType: str):
        self.__keyType = keyType

class columnFamilyDataModel_List(Collection):

    pass
class Type:

    pass
class columnFamilyDataModel_UserDefinedType(Type):

    def __init__(self, name: str, columnFamilyDataModel_UserDefinedType: set["columnFamilyDataModel_Field"] = None):
        self.name = name
        self.columnFamilyDataModel_UserDefinedType = columnFamilyDataModel_UserDefinedType if columnFamilyDataModel_UserDefinedType is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def columnFamilyDataModel_UserDefinedType(self):
        return self.__columnFamilyDataModel_UserDefinedType

    @columnFamilyDataModel_UserDefinedType.setter
    def columnFamilyDataModel_UserDefinedType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_columnFamilyDataModel_UserDefinedType__columnFamilyDataModel_UserDefinedType", None)
        self.__columnFamilyDataModel_UserDefinedType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "columnFamilyDataModel_Field"):
                    opp_val = getattr(item, "columnFamilyDataModel_Field", None)
                    
                    if opp_val == self:
                        setattr(item, "columnFamilyDataModel_Field", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "columnFamilyDataModel_Field"):
                    opp_val = getattr(item, "columnFamilyDataModel_Field", None)
                    
                    setattr(item, "columnFamilyDataModel_Field", self)
                    

class columnFamilyDataModel_Tuple(Type):

    def __init__(self, types: str):
        self.types = types
        
    @property
    def types(self) -> str:
        return self.__types

    @types.setter
    def types(self, types: str):
        self.__types = types

class columnFamilyDataModel_Collection(Type):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class columnFamilyDataModel_SimpleType(Type):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class columnFamilyDataModel_ColumnFamily:

    def __init__(self, name: str, columnFamilyDataModel_ColumnFamily: "columnFamilyDataModel_Table" = None, columnFamilyDataModel_ColumnFamily13: "columnFamilyDataModel_Column" = None):
        self.name = name
        self.columnFamilyDataModel_ColumnFamily = columnFamilyDataModel_ColumnFamily
        self.columnFamilyDataModel_ColumnFamily13 = columnFamilyDataModel_ColumnFamily13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def columnFamilyDataModel_ColumnFamily(self):
        return self.__columnFamilyDataModel_ColumnFamily

    @columnFamilyDataModel_ColumnFamily.setter
    def columnFamilyDataModel_ColumnFamily(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_columnFamilyDataModel_ColumnFamily__columnFamilyDataModel_ColumnFamily", None)
        self.__columnFamilyDataModel_ColumnFamily = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "columnFamilyDataModel_Table2"):
                opp_val = getattr(old_value, "columnFamilyDataModel_Table2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "columnFamilyDataModel_Table2"):
                opp_val = getattr(value, "columnFamilyDataModel_Table2", None)
                if opp_val is None:
                    setattr(value, "columnFamilyDataModel_Table2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def columnFamilyDataModel_ColumnFamily13(self):
        return self.__columnFamilyDataModel_ColumnFamily13

    @columnFamilyDataModel_ColumnFamily13.setter
    def columnFamilyDataModel_ColumnFamily13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_columnFamilyDataModel_ColumnFamily__columnFamilyDataModel_ColumnFamily13", None)
        self.__columnFamilyDataModel_ColumnFamily13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "columnFamilyDataModel_Column12"):
                opp_val = getattr(old_value, "columnFamilyDataModel_Column12", None)
                if opp_val == self:
                    setattr(old_value, "columnFamilyDataModel_Column12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "columnFamilyDataModel_Column12"):
                opp_val = getattr(value, "columnFamilyDataModel_Column12", None)
                setattr(value, "columnFamilyDataModel_Column12", self)

class columnFamilyDataModel_Table:

    def __init__(self, name: str, columnFamilyDataModel_Table: "columnFamilyDataModel_ColumnFamilyDataModel" = None, columnFamilyDataModel_Table2: set["columnFamilyDataModel_ColumnFamily"] = None, columnFamilyDataModel_Table4: set["columnFamilyDataModel_Column"] = None, columnFamilyDataModel_Table6: set["columnFamilyDataModel_PartitionKey"] = None, columnFamilyDataModel_Table8: set["columnFamilyDataModel_ClusteringKey"] = None):
        self.name = name
        self.columnFamilyDataModel_Table = columnFamilyDataModel_Table
        self.columnFamilyDataModel_Table2 = columnFamilyDataModel_Table2 if columnFamilyDataModel_Table2 is not None else set()
        self.columnFamilyDataModel_Table4 = columnFamilyDataModel_Table4 if columnFamilyDataModel_Table4 is not None else set()
        self.columnFamilyDataModel_Table6 = columnFamilyDataModel_Table6 if columnFamilyDataModel_Table6 is not None else set()
        self.columnFamilyDataModel_Table8 = columnFamilyDataModel_Table8 if columnFamilyDataModel_Table8 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def columnFamilyDataModel_Table6(self):
        return self.__columnFamilyDataModel_Table6

    @columnFamilyDataModel_Table6.setter
    def columnFamilyDataModel_Table6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_columnFamilyDataModel_Table__columnFamilyDataModel_Table6", None)
        self.__columnFamilyDataModel_Table6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "columnFamilyDataModel_PartitionKey"):
                    opp_val = getattr(item, "columnFamilyDataModel_PartitionKey", None)
                    
                    if opp_val == self:
                        setattr(item, "columnFamilyDataModel_PartitionKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "columnFamilyDataModel_PartitionKey"):
                    opp_val = getattr(item, "columnFamilyDataModel_PartitionKey", None)
                    
                    setattr(item, "columnFamilyDataModel_PartitionKey", self)
                    

    @property
    def columnFamilyDataModel_Table8(self):
        return self.__columnFamilyDataModel_Table8

    @columnFamilyDataModel_Table8.setter
    def columnFamilyDataModel_Table8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_columnFamilyDataModel_Table__columnFamilyDataModel_Table8", None)
        self.__columnFamilyDataModel_Table8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "columnFamilyDataModel_ClusteringKey"):
                    opp_val = getattr(item, "columnFamilyDataModel_ClusteringKey", None)
                    
                    if opp_val == self:
                        setattr(item, "columnFamilyDataModel_ClusteringKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "columnFamilyDataModel_ClusteringKey"):
                    opp_val = getattr(item, "columnFamilyDataModel_ClusteringKey", None)
                    
                    setattr(item, "columnFamilyDataModel_ClusteringKey", self)
                    

    @property
    def columnFamilyDataModel_Table2(self):
        return self.__columnFamilyDataModel_Table2

    @columnFamilyDataModel_Table2.setter
    def columnFamilyDataModel_Table2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_columnFamilyDataModel_Table__columnFamilyDataModel_Table2", None)
        self.__columnFamilyDataModel_Table2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "columnFamilyDataModel_ColumnFamily"):
                    opp_val = getattr(item, "columnFamilyDataModel_ColumnFamily", None)
                    
                    if opp_val == self:
                        setattr(item, "columnFamilyDataModel_ColumnFamily", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "columnFamilyDataModel_ColumnFamily"):
                    opp_val = getattr(item, "columnFamilyDataModel_ColumnFamily", None)
                    
                    setattr(item, "columnFamilyDataModel_ColumnFamily", self)
                    

    @property
    def columnFamilyDataModel_Table(self):
        return self.__columnFamilyDataModel_Table

    @columnFamilyDataModel_Table.setter
    def columnFamilyDataModel_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_columnFamilyDataModel_Table__columnFamilyDataModel_Table", None)
        self.__columnFamilyDataModel_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "columnFamilyDataModel_ColumnFamilyDataModel"):
                opp_val = getattr(old_value, "columnFamilyDataModel_ColumnFamilyDataModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "columnFamilyDataModel_ColumnFamilyDataModel"):
                opp_val = getattr(value, "columnFamilyDataModel_ColumnFamilyDataModel", None)
                if opp_val is None:
                    setattr(value, "columnFamilyDataModel_ColumnFamilyDataModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def columnFamilyDataModel_Table4(self):
        return self.__columnFamilyDataModel_Table4

    @columnFamilyDataModel_Table4.setter
    def columnFamilyDataModel_Table4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_columnFamilyDataModel_Table__columnFamilyDataModel_Table4", None)
        self.__columnFamilyDataModel_Table4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "columnFamilyDataModel_Column"):
                    opp_val = getattr(item, "columnFamilyDataModel_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "columnFamilyDataModel_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "columnFamilyDataModel_Column"):
                    opp_val = getattr(item, "columnFamilyDataModel_Column", None)
                    
                    setattr(item, "columnFamilyDataModel_Column", self)
                    

class columnFamilyDataModel_ColumnFamilyDataModel:

    pass