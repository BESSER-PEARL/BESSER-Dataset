from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PrimitiveTypeType(Enum):
    ascii = "ascii"
    bigint = "bigint"
    blob = "blob"
    boolean = "boolean"
    counter = "counter"
    decimal = "decimal"
    double = "double"
    float = "float"
    inet = "inet"
    int = "int"
    text = "text"
    timestamp = "timestamp"
    timeuuid = "timeuuid"
    uuid = "uuid"
    varchar = "varchar"
    varint = "varint"
class ReplicaPlacementStrategies(Enum):
    SimpleStrategy = "SimpleStrategy"
    OldNetworkTopologyStrategy = "OldNetworkTopologyStrategy"
    NetworkTopologyStrategy = "NetworkTopologyStrategy"
class CollectionTypeType(Enum):
    set = "set"
    list = "list"


############################################
# Definition of Classes
############################################

class Type:

    pass
class nosql_PrimitiveType(Type):

    def __init__(self, kind: str):
        self.kind = kind
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


class ColumnFamily:

    pass
class nosql_StaticColumnFamily(ColumnFamily):

    pass
class nosql_DynamicColumnFamily(ColumnFamily):

    pass
class DataStructureType:

    pass
class nosql_CollectionType(DataStructureType):

    def __init__(self, kind: str, keyType: str):
        self.kind = kind
        self.keyType = keyType
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def keyType(self):
        return self.__keyType

    @keyType.setter
    def keyType(self, keyType: str):
        self.__keyType = keyType


class nosql_MapType(DataStructureType):

    def __init__(self, keyType: str, baseType: str):
        self.keyType = keyType
        self.baseType = baseType
        
        pass
    @property
    def keyType(self):
        return self.__keyType

    @keyType.setter
    def keyType(self, keyType: str):
        self.__keyType = keyType


    @property
    def baseType(self):
        return self.__baseType

    @baseType.setter
    def baseType(self, baseType: str):
        self.__baseType = baseType


class nosql_DataStructureType(Type):

    pass
class nosql_ColumnFamily(ABC):

    def __init__(self, name: str, nosql_ColumnFamily5: set["nosql_Column"] = None, nosql_ColumnFamily7: set["nosql_Column"] = None, nosql_ColumnFamily: "nosql_KeySpace" = None, nosql_ColumnFamily2: "nosql_KeySpace" = None):
        self.name = name
        self.nosql_ColumnFamily5 = nosql_ColumnFamily5 if nosql_ColumnFamily5 is not None else set()
        self.nosql_ColumnFamily7 = nosql_ColumnFamily7 if nosql_ColumnFamily7 is not None else set()
        self.nosql_ColumnFamily = nosql_ColumnFamily
        self.nosql_ColumnFamily2 = nosql_ColumnFamily2
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def nosql_ColumnFamily(self):
        return self.__nosql_ColumnFamily

    @nosql_ColumnFamily.setter
    def nosql_ColumnFamily(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_ColumnFamily__nosql_ColumnFamily", None)
        self.__nosql_ColumnFamily = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nosql_KeySpace"):
                opp_val = getattr(old_value, "nosql_KeySpace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nosql_KeySpace"):
                opp_val = getattr(value, "nosql_KeySpace", None)
                if opp_val is None:
                    setattr(value, "nosql_KeySpace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nosql_ColumnFamily7(self):
        return self.__nosql_ColumnFamily7

    @nosql_ColumnFamily7.setter
    def nosql_ColumnFamily7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_ColumnFamily__nosql_ColumnFamily7", None)
        self.__nosql_ColumnFamily7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nosql_Column8"):
                    opp_val = getattr(item, "nosql_Column8", None)
                    
                    if opp_val == self:
                        setattr(item, "nosql_Column8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nosql_Column8"):
                    opp_val = getattr(item, "nosql_Column8", None)
                    
                    setattr(item, "nosql_Column8", self)
                    

    @property
    def nosql_ColumnFamily2(self):
        return self.__nosql_ColumnFamily2

    @nosql_ColumnFamily2.setter
    def nosql_ColumnFamily2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_ColumnFamily__nosql_ColumnFamily2", None)
        self.__nosql_ColumnFamily2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nosql_KeySpace3"):
                opp_val = getattr(old_value, "nosql_KeySpace3", None)
                if opp_val == self:
                    setattr(old_value, "nosql_KeySpace3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nosql_KeySpace3"):
                opp_val = getattr(value, "nosql_KeySpace3", None)
                setattr(value, "nosql_KeySpace3", self)

    @property
    def nosql_ColumnFamily5(self):
        return self.__nosql_ColumnFamily5

    @nosql_ColumnFamily5.setter
    def nosql_ColumnFamily5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_ColumnFamily__nosql_ColumnFamily5", None)
        self.__nosql_ColumnFamily5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nosql_Column"):
                    opp_val = getattr(item, "nosql_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "nosql_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nosql_Column"):
                    opp_val = getattr(item, "nosql_Column", None)
                    
                    setattr(item, "nosql_Column", self)
                    

class nosql_Type(ABC):

    pass
class nosql_Column:

    def __init__(self, name: str, nosql_Column: "nosql_ColumnFamily" = None, nosql_Column8: "nosql_ColumnFamily" = None, nosql_Column10: "nosql_Type" = None, nosql_Column12: "nosql_DynamicColumnFamily" = None):
        self.name = name
        self.nosql_Column = nosql_Column
        self.nosql_Column8 = nosql_Column8
        self.nosql_Column10 = nosql_Column10
        self.nosql_Column12 = nosql_Column12
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def nosql_Column(self):
        return self.__nosql_Column

    @nosql_Column.setter
    def nosql_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_Column__nosql_Column", None)
        self.__nosql_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nosql_ColumnFamily5"):
                opp_val = getattr(old_value, "nosql_ColumnFamily5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nosql_ColumnFamily5"):
                opp_val = getattr(value, "nosql_ColumnFamily5", None)
                if opp_val is None:
                    setattr(value, "nosql_ColumnFamily5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nosql_Column12(self):
        return self.__nosql_Column12

    @nosql_Column12.setter
    def nosql_Column12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_Column__nosql_Column12", None)
        self.__nosql_Column12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nosql_DynamicColumnFamily"):
                opp_val = getattr(old_value, "nosql_DynamicColumnFamily", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nosql_DynamicColumnFamily"):
                opp_val = getattr(value, "nosql_DynamicColumnFamily", None)
                if opp_val is None:
                    setattr(value, "nosql_DynamicColumnFamily", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nosql_Column8(self):
        return self.__nosql_Column8

    @nosql_Column8.setter
    def nosql_Column8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_Column__nosql_Column8", None)
        self.__nosql_Column8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nosql_ColumnFamily7"):
                opp_val = getattr(old_value, "nosql_ColumnFamily7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nosql_ColumnFamily7"):
                opp_val = getattr(value, "nosql_ColumnFamily7", None)
                if opp_val is None:
                    setattr(value, "nosql_ColumnFamily7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nosql_Column10(self):
        return self.__nosql_Column10

    @nosql_Column10.setter
    def nosql_Column10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_Column__nosql_Column10", None)
        self.__nosql_Column10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nosql_Type"):
                opp_val = getattr(old_value, "nosql_Type", None)
                if opp_val == self:
                    setattr(old_value, "nosql_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nosql_Type"):
                opp_val = getattr(value, "nosql_Type", None)
                setattr(value, "nosql_Type", self)

class nosql_KeySpace:

    def __init__(self, name: str, replicationFactor: str, replicaPlacementStrategy: str, nosql_KeySpace: set["nosql_ColumnFamily"] = None, nosql_KeySpace3: "nosql_ColumnFamily" = None):
        self.name = name
        self.replicationFactor = replicationFactor
        self.replicaPlacementStrategy = replicaPlacementStrategy
        self.nosql_KeySpace = nosql_KeySpace if nosql_KeySpace is not None else set()
        self.nosql_KeySpace3 = nosql_KeySpace3
        
        pass
    @property
    def replicaPlacementStrategy(self):
        return self.__replicaPlacementStrategy

    @replicaPlacementStrategy.setter
    def replicaPlacementStrategy(self, replicaPlacementStrategy: str):
        self.__replicaPlacementStrategy = replicaPlacementStrategy


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def replicationFactor(self):
        return self.__replicationFactor

    @replicationFactor.setter
    def replicationFactor(self, replicationFactor: str):
        self.__replicationFactor = replicationFactor


    @property
    def nosql_KeySpace(self):
        return self.__nosql_KeySpace

    @nosql_KeySpace.setter
    def nosql_KeySpace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_KeySpace__nosql_KeySpace", None)
        self.__nosql_KeySpace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nosql_ColumnFamily"):
                    opp_val = getattr(item, "nosql_ColumnFamily", None)
                    
                    if opp_val == self:
                        setattr(item, "nosql_ColumnFamily", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nosql_ColumnFamily"):
                    opp_val = getattr(item, "nosql_ColumnFamily", None)
                    
                    setattr(item, "nosql_ColumnFamily", self)
                    

    @property
    def nosql_KeySpace3(self):
        return self.__nosql_KeySpace3

    @nosql_KeySpace3.setter
    def nosql_KeySpace3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nosql_KeySpace__nosql_KeySpace3", None)
        self.__nosql_KeySpace3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nosql_ColumnFamily2"):
                opp_val = getattr(old_value, "nosql_ColumnFamily2", None)
                if opp_val == self:
                    setattr(old_value, "nosql_ColumnFamily2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nosql_ColumnFamily2"):
                opp_val = getattr(value, "nosql_ColumnFamily2", None)
                setattr(value, "nosql_ColumnFamily2", self)
