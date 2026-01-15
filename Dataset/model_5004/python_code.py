from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class DataType:

    pass
class systemmodel_VectorType(DataType):

    def __init__(self, size: str):
        self.size = size
        
    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

class systemmodel_ScalarType(DataType):

    pass
class systemmodel_MatrixType(DataType):

    def __init__(self, rows: str, columns: str):
        self.rows = rows
        self.columns = columns
        
    @property
    def columns(self) -> str:
        return self.__columns

    @columns.setter
    def columns(self, columns: str):
        self.__columns = columns

    @property
    def rows(self) -> str:
        return self.__rows

    @rows.setter
    def rows(self, rows: str):
        self.__rows = rows

class InterfaceBlock:

    pass
class systemmodel_OutputBlock(InterfaceBlock):

    pass
class systemmodel_InputBlock(InterfaceBlock):

    pass
class Block:

    pass
class systemmodel_GainBlock(Block):

    def __init__(self, gainfactor: str):
        self.gainfactor = gainfactor
        
    @property
    def gainfactor(self) -> str:
        return self.__gainfactor

    @gainfactor.setter
    def gainfactor(self, gainfactor: str):
        self.__gainfactor = gainfactor

class systemmodel_InterfaceBlock(Block):

    pass
class systemmodel_Sum(Block):

    pass
class systemmodel_Saturation(Block):

    def __init__(self, lowerBound: str, upperBound: str):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        
    @property
    def lowerBound(self) -> str:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: str):
        self.__lowerBound = lowerBound

    @property
    def upperBound(self) -> str:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: str):
        self.__upperBound = upperBound

class systemmodel_UnitDelay(Block):

    def __init__(self, initialCondition: str):
        self.initialCondition = initialCondition
        
    @property
    def initialCondition(self) -> str:
        return self.__initialCondition

    @initialCondition.setter
    def initialCondition(self, initialCondition: str):
        self.__initialCondition = initialCondition

class Port:

    pass
class systemmodel_Inport(Port):

    pass
class systemmodel_Outport(Port):

    pass
class SMElement:

    pass
class systemmodel_Signal(SMElement):

    pass
class systemmodel_DataType(SMElement):

    def __init__(self, basetype: str, systemmodel_DataType: "systemmodel_SystemModel" = None, systemmodel_DataType19: "systemmodel_Port" = None):
        self.basetype = basetype
        self.systemmodel_DataType = systemmodel_DataType
        self.systemmodel_DataType19 = systemmodel_DataType19
        
    @property
    def basetype(self) -> str:
        return self.__basetype

    @basetype.setter
    def basetype(self, basetype: str):
        self.__basetype = basetype

    @property
    def systemmodel_DataType19(self):
        return self.__systemmodel_DataType19

    @systemmodel_DataType19.setter
    def systemmodel_DataType19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemmodel_DataType__systemmodel_DataType19", None)
        self.__systemmodel_DataType19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "systemmodel_Port"):
                opp_val = getattr(old_value, "systemmodel_Port", None)
                if opp_val == self:
                    setattr(old_value, "systemmodel_Port", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "systemmodel_Port"):
                opp_val = getattr(value, "systemmodel_Port", None)
                setattr(value, "systemmodel_Port", self)

    @property
    def systemmodel_DataType(self):
        return self.__systemmodel_DataType

    @systemmodel_DataType.setter
    def systemmodel_DataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemmodel_DataType__systemmodel_DataType", None)
        self.__systemmodel_DataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "systemmodel_SystemModel4"):
                opp_val = getattr(old_value, "systemmodel_SystemModel4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "systemmodel_SystemModel4"):
                opp_val = getattr(value, "systemmodel_SystemModel4", None)
                if opp_val is None:
                    setattr(value, "systemmodel_SystemModel4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class systemmodel_Port(SMElement):

    pass
class systemmodel_Block(SMElement):

    def __init__(self, sequenceNumber: int, systemmodel_Block: "systemmodel_SystemModel" = None, Block: "systemmodel_Inport" = None, Block17: "systemmodel_Outport" = None, parentBlock: set["systemmodel_Inport"] = None, parentBlock7: set["systemmodel_Outport"] = None):
        self.sequenceNumber = sequenceNumber
        self.systemmodel_Block = systemmodel_Block
        self.Block = Block
        self.Block17 = Block17
        self.parentBlock = parentBlock if parentBlock is not None else set()
        self.parentBlock7 = parentBlock7 if parentBlock7 is not None else set()
        
    @property
    def sequenceNumber(self) -> int:
        return self.__sequenceNumber

    @sequenceNumber.setter
    def sequenceNumber(self, sequenceNumber: int):
        self.__sequenceNumber = sequenceNumber

    @property
    def Block(self):
        return self.__Block

    @Block.setter
    def Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemmodel_Block__Block", None)
        self.__Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inports"):
                opp_val = getattr(old_value, "inports", None)
                if opp_val == self:
                    setattr(old_value, "inports", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inports"):
                opp_val = getattr(value, "inports", None)
                setattr(value, "inports", self)

    @property
    def Block17(self):
        return self.__Block17

    @Block17.setter
    def Block17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemmodel_Block__Block17", None)
        self.__Block17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outports"):
                opp_val = getattr(old_value, "outports", None)
                if opp_val == self:
                    setattr(old_value, "outports", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outports"):
                opp_val = getattr(value, "outports", None)
                setattr(value, "outports", self)

    @property
    def parentBlock7(self):
        return self.__parentBlock7

    @parentBlock7.setter
    def parentBlock7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemmodel_Block__parentBlock7", None)
        self.__parentBlock7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Outport"):
                    opp_val = getattr(item, "Outport", None)
                    
                    if opp_val == self:
                        setattr(item, "Outport", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Outport"):
                    opp_val = getattr(item, "Outport", None)
                    
                    setattr(item, "Outport", self)
                    

    @property
    def parentBlock(self):
        return self.__parentBlock

    @parentBlock.setter
    def parentBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemmodel_Block__parentBlock", None)
        self.__parentBlock = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Inport"):
                    opp_val = getattr(item, "Inport", None)
                    
                    if opp_val == self:
                        setattr(item, "Inport", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Inport"):
                    opp_val = getattr(item, "Inport", None)
                    
                    setattr(item, "Inport", self)
                    

    @property
    def systemmodel_Block(self):
        return self.__systemmodel_Block

    @systemmodel_Block.setter
    def systemmodel_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemmodel_Block__systemmodel_Block", None)
        self.__systemmodel_Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "systemmodel_SystemModel"):
                opp_val = getattr(old_value, "systemmodel_SystemModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "systemmodel_SystemModel"):
                opp_val = getattr(value, "systemmodel_SystemModel", None)
                if opp_val is None:
                    setattr(value, "systemmodel_SystemModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class systemmodel_SystemModel(SMElement):

    pass
class systemmodel_SMElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
