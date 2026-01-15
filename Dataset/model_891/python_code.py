from datetime import datetime, date, time
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

    def __init__(self, count: int, simplepdl_Allocation: "simplepdl_WorkDefinition" = None, simplepdl_Allocation11: "simplepdl_Ressource" = None, simplepdl_Allocation13: "simplepdl_WorkDefinition" = None):
        self.count = count
        self.simplepdl_Allocation = simplepdl_Allocation
        self.simplepdl_Allocation11 = simplepdl_Allocation11
        self.simplepdl_Allocation13 = simplepdl_Allocation13
        
    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, count: int):
        self.__count = count

    @property
    def simplepdl_Allocation(self):
        return self.__simplepdl_Allocation

    @simplepdl_Allocation.setter
    def simplepdl_Allocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Allocation__simplepdl_Allocation", None)
        self.__simplepdl_Allocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplepdl_WorkDefinition"):
                opp_val = getattr(old_value, "simplepdl_WorkDefinition", None)
                if opp_val == self:
                    setattr(old_value, "simplepdl_WorkDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplepdl_WorkDefinition"):
                opp_val = getattr(value, "simplepdl_WorkDefinition", None)
                setattr(value, "simplepdl_WorkDefinition", self)

    @property
    def simplepdl_Allocation13(self):
        return self.__simplepdl_Allocation13

    @simplepdl_Allocation13.setter
    def simplepdl_Allocation13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Allocation__simplepdl_Allocation13", None)
        self.__simplepdl_Allocation13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplepdl_WorkDefinition14"):
                opp_val = getattr(old_value, "simplepdl_WorkDefinition14", None)
                if opp_val == self:
                    setattr(old_value, "simplepdl_WorkDefinition14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplepdl_WorkDefinition14"):
                opp_val = getattr(value, "simplepdl_WorkDefinition14", None)
                setattr(value, "simplepdl_WorkDefinition14", self)

    @property
    def simplepdl_Allocation11(self):
        return self.__simplepdl_Allocation11

    @simplepdl_Allocation11.setter
    def simplepdl_Allocation11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Allocation__simplepdl_Allocation11", None)
        self.__simplepdl_Allocation11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplepdl_Ressource"):
                opp_val = getattr(old_value, "simplepdl_Ressource", None)
                if opp_val == self:
                    setattr(old_value, "simplepdl_Ressource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplepdl_Ressource"):
                opp_val = getattr(value, "simplepdl_Ressource", None)
                setattr(value, "simplepdl_Ressource", self)

class ProcessElements:

    pass
class simplepdl_Guidance(ProcessElements):

    def __init__(self, text: str, simplepdl_Guidance: "simplepdl_ProcessElements" = None):
        self.text = text
        self.simplepdl_Guidance = simplepdl_Guidance
        
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
        self.__simplepdl_Guidance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplepdl_ProcessElements9"):
                opp_val = getattr(old_value, "simplepdl_ProcessElements9", None)
                if opp_val == self:
                    setattr(old_value, "simplepdl_ProcessElements9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplepdl_ProcessElements9"):
                opp_val = getattr(value, "simplepdl_ProcessElements9", None)
                setattr(value, "simplepdl_ProcessElements9", self)

class simplepdl_Ressource(ProcessElements):

    def __init__(self, name: str, count: int, simplepdl_Ressource: "simplepdl_Allocation" = None):
        self.name = name
        self.count = count
        self.simplepdl_Ressource = simplepdl_Ressource
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, count: int):
        self.__count = count

    @property
    def simplepdl_Ressource(self):
        return self.__simplepdl_Ressource

    @simplepdl_Ressource.setter
    def simplepdl_Ressource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Ressource__simplepdl_Ressource", None)
        self.__simplepdl_Ressource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplepdl_Allocation11"):
                opp_val = getattr(old_value, "simplepdl_Allocation11", None)
                if opp_val == self:
                    setattr(old_value, "simplepdl_Allocation11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplepdl_Allocation11"):
                opp_val = getattr(value, "simplepdl_Allocation11", None)
                setattr(value, "simplepdl_Allocation11", self)

class simplepdl_WorkSequence(ProcessElements):

    def __init__(self, linkType: str, linksToSuccessors: "simplepdl_WorkDefinition" = None, WorkSequence: "simplepdl_WorkDefinition" = None, WorkSequence3: "simplepdl_WorkDefinition" = None, linksToPredecessors: "simplepdl_WorkDefinition" = None):
        self.linkType = linkType
        self.linksToSuccessors = linksToSuccessors
        self.WorkSequence = WorkSequence
        self.WorkSequence3 = WorkSequence3
        self.linksToPredecessors = linksToPredecessors
        
    @property
    def linkType(self) -> str:
        return self.__linkType

    @linkType.setter
    def linkType(self, linkType: str):
        self.__linkType = linkType

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

class simplepdl_WorkDefinition(ProcessElements):

    def __init__(self, name: str, WorkDefinition: "simplepdl_WorkSequence" = None, successor: set["simplepdl_WorkSequence"] = None, predecessor: set["simplepdl_WorkSequence"] = None, simplepdl_WorkDefinition: "simplepdl_Allocation" = None, WorkDefinition7: "simplepdl_WorkSequence" = None, simplepdl_WorkDefinition14: "simplepdl_Allocation" = None):
        self.name = name
        self.WorkDefinition = WorkDefinition
        self.successor = successor if successor is not None else set()
        self.predecessor = predecessor if predecessor is not None else set()
        self.simplepdl_WorkDefinition = simplepdl_WorkDefinition
        self.WorkDefinition7 = WorkDefinition7
        self.simplepdl_WorkDefinition14 = simplepdl_WorkDefinition14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def simplepdl_WorkDefinition(self):
        return self.__simplepdl_WorkDefinition

    @simplepdl_WorkDefinition.setter
    def simplepdl_WorkDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkDefinition__simplepdl_WorkDefinition", None)
        self.__simplepdl_WorkDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplepdl_Allocation"):
                opp_val = getattr(old_value, "simplepdl_Allocation", None)
                if opp_val == self:
                    setattr(old_value, "simplepdl_Allocation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplepdl_Allocation"):
                opp_val = getattr(value, "simplepdl_Allocation", None)
                setattr(value, "simplepdl_Allocation", self)

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
                    

    @property
    def simplepdl_WorkDefinition14(self):
        return self.__simplepdl_WorkDefinition14

    @simplepdl_WorkDefinition14.setter
    def simplepdl_WorkDefinition14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkDefinition__simplepdl_WorkDefinition14", None)
        self.__simplepdl_WorkDefinition14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplepdl_Allocation13"):
                opp_val = getattr(old_value, "simplepdl_Allocation13", None)
                if opp_val == self:
                    setattr(old_value, "simplepdl_Allocation13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplepdl_Allocation13"):
                opp_val = getattr(value, "simplepdl_Allocation13", None)
                setattr(value, "simplepdl_Allocation13", self)

class simplepdl_ProcessElements:

    pass
class simplepdl_Process:

    def __init__(self, name: str, simplepdl_Process: set["simplepdl_ProcessElements"] = None):
        self.name = name
        self.simplepdl_Process = simplepdl_Process if simplepdl_Process is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simplepdl_Process(self):
        return self.__simplepdl_Process

    @simplepdl_Process.setter
    def simplepdl_Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Process__simplepdl_Process", None)
        self.__simplepdl_Process = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simplepdl_ProcessElements"):
                    opp_val = getattr(item, "simplepdl_ProcessElements", None)
                    
                    if opp_val == self:
                        setattr(item, "simplepdl_ProcessElements", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simplepdl_ProcessElements"):
                    opp_val = getattr(item, "simplepdl_ProcessElements", None)
                    
                    setattr(item, "simplepdl_ProcessElements", self)
                    
