from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class WorkSequenceType(Enum):
    startToStart = "startToStart"
    finishToStart = "finishToStart"
    startToFinish = "startToFinish"
    finishToFinish = "finishToFinish"


############################################
# Definition of Classes
############################################

class simplepdl_Allocation:

    def __init__(self, count: int, Allocation11: "simplepdl_Ressource" = None, allocations: "simplepdl_WorkDefinition" = None, Allocation: "simplepdl_WorkDefinition" = None, allocations15: "simplepdl_Ressource" = None):
        self.count = count
        self.Allocation11 = Allocation11
        self.allocations = allocations
        self.Allocation = Allocation
        self.allocations15 = allocations15
        
    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, count: int):
        self.__count = count

    @property
    def Allocation(self):
        return self.__Allocation

    @Allocation.setter
    def Allocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Allocation__Allocation", None)
        self.__Allocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workDefinition"):
                opp_val = getattr(old_value, "workDefinition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workDefinition"):
                opp_val = getattr(value, "workDefinition", None)
                if opp_val is None:
                    setattr(value, "workDefinition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def allocations(self):
        return self.__allocations

    @allocations.setter
    def allocations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Allocation__allocations", None)
        self.__allocations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorkDefinition13"):
                opp_val = getattr(old_value, "WorkDefinition13", None)
                if opp_val == self:
                    setattr(old_value, "WorkDefinition13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorkDefinition13"):
                opp_val = getattr(value, "WorkDefinition13", None)
                setattr(value, "WorkDefinition13", self)

    @property
    def allocations15(self):
        return self.__allocations15

    @allocations15.setter
    def allocations15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Allocation__allocations15", None)
        self.__allocations15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ressource"):
                opp_val = getattr(old_value, "Ressource", None)
                if opp_val == self:
                    setattr(old_value, "Ressource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ressource"):
                opp_val = getattr(value, "Ressource", None)
                setattr(value, "Ressource", self)

    @property
    def Allocation11(self):
        return self.__Allocation11

    @Allocation11.setter
    def Allocation11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Allocation__Allocation11", None)
        self.__Allocation11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ressource"):
                opp_val = getattr(old_value, "ressource", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ressource"):
                opp_val = getattr(value, "ressource", None)
                if opp_val is None:
                    setattr(value, "ressource", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simplepdl_ProcessElement(ABC):

    pass
class simplepdl_Process:

    def __init__(self, name: str, process: set["simplepdl_ProcessElement"] = None, Process: "simplepdl_ProcessElement" = None):
        self.name = name
        self.process = process if process is not None else set()
        self.Process = Process
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Process(self):
        return self.__Process

    @Process.setter
    def Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Process__Process", None)
        self.__Process = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "processElements"):
                opp_val = getattr(old_value, "processElements", None)
                if opp_val == self:
                    setattr(old_value, "processElements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "processElements"):
                opp_val = getattr(value, "processElements", None)
                setattr(value, "processElements", self)

    @property
    def process(self):
        return self.__process

    @process.setter
    def process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Process__process", None)
        self.__process = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProcessElement"):
                    opp_val = getattr(item, "ProcessElement", None)
                    
                    if opp_val == self:
                        setattr(item, "ProcessElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProcessElement"):
                    opp_val = getattr(item, "ProcessElement", None)
                    
                    setattr(item, "ProcessElement", self)
                    

class ProcessElement:

    pass
class simplepdl_Guidance(ProcessElement):

    def __init__(self, text: str, simplepdl_Guidance: set["simplepdl_ProcessElement"] = None):
        self.text = text
        self.simplepdl_Guidance = simplepdl_Guidance if simplepdl_Guidance is not None else set()
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def simplepdl_Guidance(self):
        return self.__simplepdl_Guidance

    @simplepdl_Guidance.setter
    def simplepdl_Guidance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Guidance__simplepdl_Guidance", None)
        self.__simplepdl_Guidance = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simplepdl_ProcessElement"):
                    opp_val = getattr(item, "simplepdl_ProcessElement", None)
                    
                    if opp_val == self:
                        setattr(item, "simplepdl_ProcessElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simplepdl_ProcessElement"):
                    opp_val = getattr(item, "simplepdl_ProcessElement", None)
                    
                    setattr(item, "simplepdl_ProcessElement", self)
                    

class simplepdl_Ressource(ProcessElement):

    def __init__(self, count: int, name: str, ressource: set["simplepdl_Allocation"] = None, Ressource: "simplepdl_Allocation" = None):
        self.count = count
        self.name = name
        self.ressource = ressource if ressource is not None else set()
        self.Ressource = Ressource
        
    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, count: int):
        self.__count = count

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Ressource(self):
        return self.__Ressource

    @Ressource.setter
    def Ressource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Ressource__Ressource", None)
        self.__Ressource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "allocations15"):
                opp_val = getattr(old_value, "allocations15", None)
                if opp_val == self:
                    setattr(old_value, "allocations15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "allocations15"):
                opp_val = getattr(value, "allocations15", None)
                setattr(value, "allocations15", self)

    @property
    def ressource(self):
        return self.__ressource

    @ressource.setter
    def ressource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Ressource__ressource", None)
        self.__ressource = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Allocation11"):
                    opp_val = getattr(item, "Allocation11", None)
                    
                    if opp_val == self:
                        setattr(item, "Allocation11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Allocation11"):
                    opp_val = getattr(item, "Allocation11", None)
                    
                    setattr(item, "Allocation11", self)
                    

class simplepdl_WorkSequence(ProcessElement):

    def __init__(self, linkType: str, WorkSequence: "simplepdl_WorkDefinition" = None, WorkSequence3: "simplepdl_WorkDefinition" = None, linksToSuccessors: "simplepdl_WorkDefinition" = None, linksToPredecessors: "simplepdl_WorkDefinition" = None):
        self.linkType = linkType
        self.WorkSequence = WorkSequence
        self.WorkSequence3 = WorkSequence3
        self.linksToSuccessors = linksToSuccessors
        self.linksToPredecessors = linksToPredecessors
        
    @property
    def linkType(self) -> str:
        return self.__linkType

    @linkType.setter
    def linkType(self, linkType: str):
        self.__linkType = linkType

    @property
    def WorkSequence3(self):
        return self.__WorkSequence3

    @WorkSequence3.setter
    def WorkSequence3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkSequence__WorkSequence3", None)
        self.__WorkSequence3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "predecessor"):
                opp_val = getattr(old_value, "predecessor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "predecessor"):
                opp_val = getattr(value, "predecessor", None)
                if opp_val is None:
                    setattr(value, "predecessor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def WorkSequence(self):
        return self.__WorkSequence

    @WorkSequence.setter
    def WorkSequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkSequence__WorkSequence", None)
        self.__WorkSequence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "successor"):
                opp_val = getattr(old_value, "successor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "successor"):
                opp_val = getattr(value, "successor", None)
                if opp_val is None:
                    setattr(value, "successor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def linksToSuccessors(self):
        return self.__linksToSuccessors

    @linksToSuccessors.setter
    def linksToSuccessors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkSequence__linksToSuccessors", None)
        self.__linksToSuccessors = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorkDefinition"):
                opp_val = getattr(old_value, "WorkDefinition", None)
                if opp_val == self:
                    setattr(old_value, "WorkDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorkDefinition"):
                opp_val = getattr(value, "WorkDefinition", None)
                setattr(value, "WorkDefinition", self)

    @property
    def linksToPredecessors(self):
        return self.__linksToPredecessors

    @linksToPredecessors.setter
    def linksToPredecessors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkSequence__linksToPredecessors", None)
        self.__linksToPredecessors = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorkDefinition7"):
                opp_val = getattr(old_value, "WorkDefinition7", None)
                if opp_val == self:
                    setattr(old_value, "WorkDefinition7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorkDefinition7"):
                opp_val = getattr(value, "WorkDefinition7", None)
                setattr(value, "WorkDefinition7", self)

class simplepdl_WorkDefinition(ProcessElement):

    def __init__(self, name: str, WorkDefinition13: "simplepdl_Allocation" = None, successor: set["simplepdl_WorkSequence"] = None, predecessor: set["simplepdl_WorkSequence"] = None, workDefinition: set["simplepdl_Allocation"] = None, WorkDefinition: "simplepdl_WorkSequence" = None, WorkDefinition7: "simplepdl_WorkSequence" = None):
        self.name = name
        self.WorkDefinition13 = WorkDefinition13
        self.successor = successor if successor is not None else set()
        self.predecessor = predecessor if predecessor is not None else set()
        self.workDefinition = workDefinition if workDefinition is not None else set()
        self.WorkDefinition = WorkDefinition
        self.WorkDefinition7 = WorkDefinition7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def WorkDefinition13(self):
        return self.__WorkDefinition13

    @WorkDefinition13.setter
    def WorkDefinition13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkDefinition__WorkDefinition13", None)
        self.__WorkDefinition13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "allocations"):
                opp_val = getattr(old_value, "allocations", None)
                if opp_val == self:
                    setattr(old_value, "allocations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "allocations"):
                opp_val = getattr(value, "allocations", None)
                setattr(value, "allocations", self)

    @property
    def WorkDefinition(self):
        return self.__WorkDefinition

    @WorkDefinition.setter
    def WorkDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkDefinition__WorkDefinition", None)
        self.__WorkDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "linksToSuccessors"):
                opp_val = getattr(old_value, "linksToSuccessors", None)
                if opp_val == self:
                    setattr(old_value, "linksToSuccessors", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "linksToSuccessors"):
                opp_val = getattr(value, "linksToSuccessors", None)
                setattr(value, "linksToSuccessors", self)

    @property
    def workDefinition(self):
        return self.__workDefinition

    @workDefinition.setter
    def workDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkDefinition__workDefinition", None)
        self.__workDefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Allocation"):
                    opp_val = getattr(item, "Allocation", None)
                    
                    if opp_val == self:
                        setattr(item, "Allocation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Allocation"):
                    opp_val = getattr(item, "Allocation", None)
                    
                    setattr(item, "Allocation", self)
                    

    @property
    def predecessor(self):
        return self.__predecessor

    @predecessor.setter
    def predecessor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkDefinition__predecessor", None)
        self.__predecessor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WorkSequence3"):
                    opp_val = getattr(item, "WorkSequence3", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkSequence3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkSequence3"):
                    opp_val = getattr(item, "WorkSequence3", None)
                    
                    setattr(item, "WorkSequence3", self)
                    

    @property
    def WorkDefinition7(self):
        return self.__WorkDefinition7

    @WorkDefinition7.setter
    def WorkDefinition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkDefinition__WorkDefinition7", None)
        self.__WorkDefinition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "linksToPredecessors"):
                opp_val = getattr(old_value, "linksToPredecessors", None)
                if opp_val == self:
                    setattr(old_value, "linksToPredecessors", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "linksToPredecessors"):
                opp_val = getattr(value, "linksToPredecessors", None)
                setattr(value, "linksToPredecessors", self)

    @property
    def successor(self):
        return self.__successor

    @successor.setter
    def successor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkDefinition__successor", None)
        self.__successor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WorkSequence"):
                    opp_val = getattr(item, "WorkSequence", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkSequence", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkSequence"):
                    opp_val = getattr(item, "WorkSequence", None)
                    
                    setattr(item, "WorkSequence", self)
                    
