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

class ProcessElement:

    pass
class simplepdl_WorkSequence(ProcessElement):

    def __init__(self, linkType: str, WorkSequence6: "simplepdl_WorkDefinition" = None, linksToSuccessors: "simplepdl_WorkDefinition" = None, linksToPredecessors: "simplepdl_WorkDefinition" = None, WorkSequence: "simplepdl_WorkDefinition" = None):
        self.linkType = linkType
        self.WorkSequence6 = WorkSequence6
        self.linksToSuccessors = linksToSuccessors
        self.linksToPredecessors = linksToPredecessors
        self.WorkSequence = WorkSequence
        
    @property
    def linkType(self) -> str:
        return self.__linkType

    @linkType.setter
    def linkType(self, linkType: str):
        self.__linkType = linkType

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
    def linksToPredecessors(self):
        return self.__linksToPredecessors

    @linksToPredecessors.setter
    def linksToPredecessors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkSequence__linksToPredecessors", None)
        self.__linksToPredecessors = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorkDefinition10"):
                opp_val = getattr(old_value, "WorkDefinition10", None)
                if opp_val == self:
                    setattr(old_value, "WorkDefinition10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorkDefinition10"):
                opp_val = getattr(value, "WorkDefinition10", None)
                setattr(value, "WorkDefinition10", self)

    @property
    def WorkSequence6(self):
        return self.__WorkSequence6

    @WorkSequence6.setter
    def WorkSequence6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkSequence__WorkSequence6", None)
        self.__WorkSequence6 = value
        
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

class simplepdl_Ressource(ProcessElement):

    def __init__(self, quantity: int, name: str, simplepdl_Ressource: "simplepdl_RessourceSequence" = None):
        self.quantity = quantity
        self.name = name
        self.simplepdl_Ressource = simplepdl_Ressource
        
    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "simplepdl_RessourceSequence"):
                opp_val = getattr(old_value, "simplepdl_RessourceSequence", None)
                if opp_val == self:
                    setattr(old_value, "simplepdl_RessourceSequence", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplepdl_RessourceSequence"):
                opp_val = getattr(value, "simplepdl_RessourceSequence", None)
                setattr(value, "simplepdl_RessourceSequence", self)

class simplepdl_WorkDefinition(ProcessElement):

    def __init__(self, name: str, predecessor: set["simplepdl_WorkSequence"] = None, workdefinition: set["simplepdl_RessourceSequence"] = None, WorkDefinition: "simplepdl_WorkSequence" = None, WorkDefinition10: "simplepdl_WorkSequence" = None, successor: set["simplepdl_WorkSequence"] = None, WorkDefinition15: "simplepdl_RessourceSequence" = None):
        self.name = name
        self.predecessor = predecessor if predecessor is not None else set()
        self.workdefinition = workdefinition if workdefinition is not None else set()
        self.WorkDefinition = WorkDefinition
        self.WorkDefinition10 = WorkDefinition10
        self.successor = successor if successor is not None else set()
        self.WorkDefinition15 = WorkDefinition15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def workdefinition(self):
        return self.__workdefinition

    @workdefinition.setter
    def workdefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkDefinition__workdefinition", None)
        self.__workdefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RessourceSequence"):
                    opp_val = getattr(item, "RessourceSequence", None)
                    
                    if opp_val == self:
                        setattr(item, "RessourceSequence", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RessourceSequence"):
                    opp_val = getattr(item, "RessourceSequence", None)
                    
                    setattr(item, "RessourceSequence", self)
                    

    @property
    def WorkDefinition10(self):
        return self.__WorkDefinition10

    @WorkDefinition10.setter
    def WorkDefinition10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkDefinition__WorkDefinition10", None)
        self.__WorkDefinition10 = value
        
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
                    

    @property
    def WorkDefinition15(self):
        return self.__WorkDefinition15

    @WorkDefinition15.setter
    def WorkDefinition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkDefinition__WorkDefinition15", None)
        self.__WorkDefinition15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ressourcesequence"):
                opp_val = getattr(old_value, "ressourcesequence", None)
                if opp_val == self:
                    setattr(old_value, "ressourcesequence", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ressourcesequence"):
                opp_val = getattr(value, "ressourcesequence", None)
                setattr(value, "ressourcesequence", self)

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
                if hasattr(item, "WorkSequence6"):
                    opp_val = getattr(item, "WorkSequence6", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkSequence6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkSequence6"):
                    opp_val = getattr(item, "WorkSequence6", None)
                    
                    setattr(item, "WorkSequence6", self)
                    

class simplepdl_ProcessElement(ABC):

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
                if hasattr(item, "simplepdl_ProcessElement12"):
                    opp_val = getattr(item, "simplepdl_ProcessElement12", None)
                    
                    if opp_val == self:
                        setattr(item, "simplepdl_ProcessElement12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simplepdl_ProcessElement12"):
                    opp_val = getattr(item, "simplepdl_ProcessElement12", None)
                    
                    setattr(item, "simplepdl_ProcessElement12", self)
                    

class simplepdl_RessourceSequence(ProcessElement):

    def __init__(self, quantity: int, RessourceSequence: "simplepdl_WorkDefinition" = None, simplepdl_RessourceSequence: "simplepdl_Ressource" = None, ressourcesequence: "simplepdl_WorkDefinition" = None):
        self.quantity = quantity
        self.RessourceSequence = RessourceSequence
        self.simplepdl_RessourceSequence = simplepdl_RessourceSequence
        self.ressourcesequence = ressourcesequence
        
    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def simplepdl_RessourceSequence(self):
        return self.__simplepdl_RessourceSequence

    @simplepdl_RessourceSequence.setter
    def simplepdl_RessourceSequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_RessourceSequence__simplepdl_RessourceSequence", None)
        self.__simplepdl_RessourceSequence = value
        
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

    @property
    def ressourcesequence(self):
        return self.__ressourcesequence

    @ressourcesequence.setter
    def ressourcesequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_RessourceSequence__ressourcesequence", None)
        self.__ressourcesequence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorkDefinition15"):
                opp_val = getattr(old_value, "WorkDefinition15", None)
                if opp_val == self:
                    setattr(old_value, "WorkDefinition15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorkDefinition15"):
                opp_val = getattr(value, "WorkDefinition15", None)
                setattr(value, "WorkDefinition15", self)

    @property
    def RessourceSequence(self):
        return self.__RessourceSequence

    @RessourceSequence.setter
    def RessourceSequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_RessourceSequence__RessourceSequence", None)
        self.__RessourceSequence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workdefinition"):
                opp_val = getattr(old_value, "workdefinition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workdefinition"):
                opp_val = getattr(value, "workdefinition", None)
                if opp_val is None:
                    setattr(value, "workdefinition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simplepdl_Process:

    def __init__(self, name: str, simplepdl_Process: set["simplepdl_ProcessElement"] = None, simplepdl_Process3: "simplepdl_ProcessElement" = None):
        self.name = name
        self.simplepdl_Process = simplepdl_Process if simplepdl_Process is not None else set()
        self.simplepdl_Process3 = simplepdl_Process3
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simplepdl_Process3(self):
        return self.__simplepdl_Process3

    @simplepdl_Process3.setter
    def simplepdl_Process3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Process__simplepdl_Process3", None)
        self.__simplepdl_Process3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplepdl_ProcessElement2"):
                opp_val = getattr(old_value, "simplepdl_ProcessElement2", None)
                if opp_val == self:
                    setattr(old_value, "simplepdl_ProcessElement2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplepdl_ProcessElement2"):
                opp_val = getattr(value, "simplepdl_ProcessElement2", None)
                setattr(value, "simplepdl_ProcessElement2", self)

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
                    
