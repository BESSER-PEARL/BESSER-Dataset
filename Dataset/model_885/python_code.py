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
                    

class simplepdl_Ressource(ProcessElement):

    def __init__(self, type: str, quantity: int, simplepdl_Ressource: "simplepdl_RessourceConso" = None):
        self.type = type
        self.quantity = quantity
        self.simplepdl_Ressource = simplepdl_Ressource
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

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
            if hasattr(old_value, "simplepdl_RessourceConso"):
                opp_val = getattr(old_value, "simplepdl_RessourceConso", None)
                if opp_val == self:
                    setattr(old_value, "simplepdl_RessourceConso", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplepdl_RessourceConso"):
                opp_val = getattr(value, "simplepdl_RessourceConso", None)
                setattr(value, "simplepdl_RessourceConso", self)

class simplepdl_RessourceConso(ProcessElement):

    def __init__(self, quantity: int, ressourcecons: "simplepdl_WorkDefinition" = None, RessourceConso: "simplepdl_WorkDefinition" = None, simplepdl_RessourceConso: "simplepdl_Ressource" = None):
        self.quantity = quantity
        self.ressourcecons = ressourcecons
        self.RessourceConso = RessourceConso
        self.simplepdl_RessourceConso = simplepdl_RessourceConso
        
    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def ressourcecons(self):
        return self.__ressourcecons

    @ressourcecons.setter
    def ressourcecons(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_RessourceConso__ressourcecons", None)
        self.__ressourcecons = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorkDefinition14"):
                opp_val = getattr(old_value, "WorkDefinition14", None)
                if opp_val == self:
                    setattr(old_value, "WorkDefinition14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorkDefinition14"):
                opp_val = getattr(value, "WorkDefinition14", None)
                setattr(value, "WorkDefinition14", self)

    @property
    def RessourceConso(self):
        return self.__RessourceConso

    @RessourceConso.setter
    def RessourceConso(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_RessourceConso__RessourceConso", None)
        self.__RessourceConso = value
        
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

    @property
    def simplepdl_RessourceConso(self):
        return self.__simplepdl_RessourceConso

    @simplepdl_RessourceConso.setter
    def simplepdl_RessourceConso(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_RessourceConso__simplepdl_RessourceConso", None)
        self.__simplepdl_RessourceConso = value
        
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

class simplepdl_WorkDefinition(ProcessElement):

    def __init__(self, name: str, WorkDefinition14: "simplepdl_RessourceConso" = None, successor: set["simplepdl_WorkSequence"] = None, predecessor: set["simplepdl_WorkSequence"] = None, workdefinition: set["simplepdl_RessourceConso"] = None, WorkDefinition: "simplepdl_WorkSequence" = None, WorkDefinition7: "simplepdl_WorkSequence" = None):
        self.name = name
        self.WorkDefinition14 = WorkDefinition14
        self.successor = successor if successor is not None else set()
        self.predecessor = predecessor if predecessor is not None else set()
        self.workdefinition = workdefinition if workdefinition is not None else set()
        self.WorkDefinition = WorkDefinition
        self.WorkDefinition7 = WorkDefinition7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def WorkDefinition14(self):
        return self.__WorkDefinition14

    @WorkDefinition14.setter
    def WorkDefinition14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkDefinition__WorkDefinition14", None)
        self.__WorkDefinition14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ressourcecons"):
                opp_val = getattr(old_value, "ressourcecons", None)
                if opp_val == self:
                    setattr(old_value, "ressourcecons", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ressourcecons"):
                opp_val = getattr(value, "ressourcecons", None)
                setattr(value, "ressourcecons", self)

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
                if hasattr(item, "RessourceConso"):
                    opp_val = getattr(item, "RessourceConso", None)
                    
                    if opp_val == self:
                        setattr(item, "RessourceConso", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RessourceConso"):
                    opp_val = getattr(item, "RessourceConso", None)
                    
                    setattr(item, "RessourceConso", self)
                    

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
                    

class simplepdl_ProcessElement(ABC):

    pass
class simplepdl_Process:

    def __init__(self, name: str, simplepdl_Process: set["simplepdl_ProcessElement"] = None, simplepdl_Process10: "simplepdl_ProcessElement" = None):
        self.name = name
        self.simplepdl_Process = simplepdl_Process if simplepdl_Process is not None else set()
        self.simplepdl_Process10 = simplepdl_Process10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simplepdl_Process10(self):
        return self.__simplepdl_Process10

    @simplepdl_Process10.setter
    def simplepdl_Process10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Process__simplepdl_Process10", None)
        self.__simplepdl_Process10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplepdl_ProcessElement9"):
                opp_val = getattr(old_value, "simplepdl_ProcessElement9", None)
                if opp_val == self:
                    setattr(old_value, "simplepdl_ProcessElement9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplepdl_ProcessElement9"):
                opp_val = getattr(value, "simplepdl_ProcessElement9", None)
                setattr(value, "simplepdl_ProcessElement9", self)

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
                    
