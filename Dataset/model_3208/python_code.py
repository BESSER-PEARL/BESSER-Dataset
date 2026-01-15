from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ControlFlowInstruction:

    pass
class llp_ParenthesisInstruction(ControlFlowInstruction):

    pass
class llp_ControlFlowBranchingInstruction(ControlFlowInstruction):

    pass
class llp_SkipInstruction(ControlFlowInstruction):

    pass
class llp_RepetitionInstruction(ControlFlowInstruction):

    def __init__(self, numberOfRepetitions: int, llp_RepetitionInstruction: "llp_Block" = None):
        self.numberOfRepetitions = numberOfRepetitions
        self.llp_RepetitionInstruction = llp_RepetitionInstruction
        
    @property
    def numberOfRepetitions(self) -> int:
        return self.__numberOfRepetitions

    @numberOfRepetitions.setter
    def numberOfRepetitions(self, numberOfRepetitions: int):
        self.__numberOfRepetitions = numberOfRepetitions

    @property
    def llp_RepetitionInstruction(self):
        return self.__llp_RepetitionInstruction

    @llp_RepetitionInstruction.setter
    def llp_RepetitionInstruction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_llp_RepetitionInstruction__llp_RepetitionInstruction", None)
        self.__llp_RepetitionInstruction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "llp_Block19"):
                opp_val = getattr(old_value, "llp_Block19", None)
                if opp_val == self:
                    setattr(old_value, "llp_Block19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "llp_Block19"):
                opp_val = getattr(value, "llp_Block19", None)
                setattr(value, "llp_Block19", self)

class llp_MemoryReference:

    def __init__(self, address: str, llp_MemoryReference10: "llp_CommitInstruction" = None, llp_MemoryReference: "llp_IOInstruction" = None, llp_MemoryReference21: "llp_SynchronisationInstruction" = None):
        self.address = address
        self.llp_MemoryReference10 = llp_MemoryReference10
        self.llp_MemoryReference = llp_MemoryReference
        self.llp_MemoryReference21 = llp_MemoryReference21
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def llp_MemoryReference21(self):
        return self.__llp_MemoryReference21

    @llp_MemoryReference21.setter
    def llp_MemoryReference21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_llp_MemoryReference__llp_MemoryReference21", None)
        self.__llp_MemoryReference21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "llp_SynchronisationInstruction"):
                opp_val = getattr(old_value, "llp_SynchronisationInstruction", None)
                if opp_val == self:
                    setattr(old_value, "llp_SynchronisationInstruction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "llp_SynchronisationInstruction"):
                opp_val = getattr(value, "llp_SynchronisationInstruction", None)
                setattr(value, "llp_SynchronisationInstruction", self)

    @property
    def llp_MemoryReference10(self):
        return self.__llp_MemoryReference10

    @llp_MemoryReference10.setter
    def llp_MemoryReference10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_llp_MemoryReference__llp_MemoryReference10", None)
        self.__llp_MemoryReference10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "llp_CommitInstruction"):
                opp_val = getattr(old_value, "llp_CommitInstruction", None)
                if opp_val == self:
                    setattr(old_value, "llp_CommitInstruction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "llp_CommitInstruction"):
                opp_val = getattr(value, "llp_CommitInstruction", None)
                setattr(value, "llp_CommitInstruction", self)

    @property
    def llp_MemoryReference(self):
        return self.__llp_MemoryReference

    @llp_MemoryReference.setter
    def llp_MemoryReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_llp_MemoryReference__llp_MemoryReference", None)
        self.__llp_MemoryReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "llp_IOInstruction"):
                opp_val = getattr(old_value, "llp_IOInstruction", None)
                if opp_val == self:
                    setattr(old_value, "llp_IOInstruction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "llp_IOInstruction"):
                opp_val = getattr(value, "llp_IOInstruction", None)
                setattr(value, "llp_IOInstruction", self)

class DataAccessPattern:

    pass
class llp_SynchronisationInstruction(DataAccessPattern):

    pass
class llp_ControlFlowInstruction(DataAccessPattern):

    pass
class llp_IOInstruction(DataAccessPattern):

    pass
class IOInstruction:

    pass
class llp_WriteInstruction(IOInstruction):

    pass
class llp_ReadInstruction(IOInstruction):

    pass
class llp_SpawnInstruction(DataAccessPattern):

    pass
class SynchronisationInstruction:

    pass
class llp_UnlockInstruction(SynchronisationInstruction):

    pass
class llp_LockInstruction(SynchronisationInstruction):

    pass
class CacheInstruction:

    pass
class llp_CommitInstruction(CacheInstruction):

    pass
class llp_CacheInstruction(DataAccessPattern):

    pass
class llp_Task:

    def __init__(self, name: str, llp_Task4: "llp_Block" = None, llp_Task: "llp_LowLevelProgram" = None, llp_Task12: "llp_SpawnInstruction" = None):
        self.name = name
        self.llp_Task4 = llp_Task4
        self.llp_Task = llp_Task
        self.llp_Task12 = llp_Task12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def llp_Task12(self):
        return self.__llp_Task12

    @llp_Task12.setter
    def llp_Task12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_llp_Task__llp_Task12", None)
        self.__llp_Task12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "llp_SpawnInstruction"):
                opp_val = getattr(old_value, "llp_SpawnInstruction", None)
                if opp_val == self:
                    setattr(old_value, "llp_SpawnInstruction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "llp_SpawnInstruction"):
                opp_val = getattr(value, "llp_SpawnInstruction", None)
                setattr(value, "llp_SpawnInstruction", self)

    @property
    def llp_Task(self):
        return self.__llp_Task

    @llp_Task.setter
    def llp_Task(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_llp_Task__llp_Task", None)
        self.__llp_Task = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "llp_LowLevelProgram"):
                opp_val = getattr(old_value, "llp_LowLevelProgram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "llp_LowLevelProgram"):
                opp_val = getattr(value, "llp_LowLevelProgram", None)
                if opp_val is None:
                    setattr(value, "llp_LowLevelProgram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def llp_Task4(self):
        return self.__llp_Task4

    @llp_Task4.setter
    def llp_Task4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_llp_Task__llp_Task4", None)
        self.__llp_Task4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "llp_Block5"):
                opp_val = getattr(old_value, "llp_Block5", None)
                if opp_val == self:
                    setattr(old_value, "llp_Block5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "llp_Block5"):
                opp_val = getattr(value, "llp_Block5", None)
                setattr(value, "llp_Block5", self)

class llp_LowLevelProgram:

    pass
class llp_DataAccessPattern(ABC):

    pass
class llp_Block:

    pass