from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class rm_VariableReference:

    def __init__(self, variable: str, memoryCellIndex: int, rm_VariableReference: "rm_Memory" = None):
        self.variable = variable
        self.memoryCellIndex = memoryCellIndex
        self.rm_VariableReference = rm_VariableReference
        
    @property
    def memoryCellIndex(self) -> int:
        return self.__memoryCellIndex

    @memoryCellIndex.setter
    def memoryCellIndex(self, memoryCellIndex: int):
        self.__memoryCellIndex = memoryCellIndex

    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

    @property
    def rm_VariableReference(self):
        return self.__rm_VariableReference

    @rm_VariableReference.setter
    def rm_VariableReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rm_VariableReference__rm_VariableReference", None)
        self.__rm_VariableReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rm_Memory6"):
                opp_val = getattr(old_value, "rm_Memory6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rm_Memory6"):
                opp_val = getattr(value, "rm_Memory6", None)
                if opp_val is None:
                    setattr(value, "rm_Memory6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rm_MemoryCellReference:

    def __init__(self, startCellIndex: int, endCellIndex: int, rm_MemoryCellReference: "rm_Device" = None):
        self.startCellIndex = startCellIndex
        self.endCellIndex = endCellIndex
        self.rm_MemoryCellReference = rm_MemoryCellReference
        
    @property
    def endCellIndex(self) -> int:
        return self.__endCellIndex

    @endCellIndex.setter
    def endCellIndex(self, endCellIndex: int):
        self.__endCellIndex = endCellIndex

    @property
    def startCellIndex(self) -> int:
        return self.__startCellIndex

    @startCellIndex.setter
    def startCellIndex(self, startCellIndex: int):
        self.__startCellIndex = startCellIndex

    @property
    def rm_MemoryCellReference(self):
        return self.__rm_MemoryCellReference

    @rm_MemoryCellReference.setter
    def rm_MemoryCellReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rm_MemoryCellReference__rm_MemoryCellReference", None)
        self.__rm_MemoryCellReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rm_Device4"):
                opp_val = getattr(old_value, "rm_Device4", None)
                if opp_val == self:
                    setattr(old_value, "rm_Device4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rm_Device4"):
                opp_val = getattr(value, "rm_Device4", None)
                setattr(value, "rm_Device4", self)

class rm_Memory:

    def __init__(self, size: int, rm_Memory: "rm_ResourceModel" = None, rm_Memory6: set["rm_VariableReference"] = None):
        self.size = size
        self.rm_Memory = rm_Memory
        self.rm_Memory6 = rm_Memory6 if rm_Memory6 is not None else set()
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def rm_Memory6(self):
        return self.__rm_Memory6

    @rm_Memory6.setter
    def rm_Memory6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rm_Memory__rm_Memory6", None)
        self.__rm_Memory6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rm_VariableReference"):
                    opp_val = getattr(item, "rm_VariableReference", None)
                    
                    if opp_val == self:
                        setattr(item, "rm_VariableReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rm_VariableReference"):
                    opp_val = getattr(item, "rm_VariableReference", None)
                    
                    setattr(item, "rm_VariableReference", self)
                    

    @property
    def rm_Memory(self):
        return self.__rm_Memory

    @rm_Memory.setter
    def rm_Memory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rm_Memory__rm_Memory", None)
        self.__rm_Memory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rm_ResourceModel2"):
                opp_val = getattr(old_value, "rm_ResourceModel2", None)
                if opp_val == self:
                    setattr(old_value, "rm_ResourceModel2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rm_ResourceModel2"):
                opp_val = getattr(value, "rm_ResourceModel2", None)
                setattr(value, "rm_ResourceModel2", self)

class rm_Device:

    def __init__(self, cacheSize: int, rm_Device: "rm_ResourceModel" = None, rm_Device4: "rm_MemoryCellReference" = None):
        self.cacheSize = cacheSize
        self.rm_Device = rm_Device
        self.rm_Device4 = rm_Device4
        
    @property
    def cacheSize(self) -> int:
        return self.__cacheSize

    @cacheSize.setter
    def cacheSize(self, cacheSize: int):
        self.__cacheSize = cacheSize

    @property
    def rm_Device(self):
        return self.__rm_Device

    @rm_Device.setter
    def rm_Device(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rm_Device__rm_Device", None)
        self.__rm_Device = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rm_ResourceModel"):
                opp_val = getattr(old_value, "rm_ResourceModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rm_ResourceModel"):
                opp_val = getattr(value, "rm_ResourceModel", None)
                if opp_val is None:
                    setattr(value, "rm_ResourceModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rm_Device4(self):
        return self.__rm_Device4

    @rm_Device4.setter
    def rm_Device4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rm_Device__rm_Device4", None)
        self.__rm_Device4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rm_MemoryCellReference"):
                opp_val = getattr(old_value, "rm_MemoryCellReference", None)
                if opp_val == self:
                    setattr(old_value, "rm_MemoryCellReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rm_MemoryCellReference"):
                opp_val = getattr(value, "rm_MemoryCellReference", None)
                setattr(value, "rm_MemoryCellReference", self)

class rm_ResourceModel:

    pass