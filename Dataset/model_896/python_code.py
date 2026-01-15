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
class simplepdl_Resources(ProcessElement):

    def __init__(self, quantite: int, name: str, resources: set["simplepdl_RequeteDeRessource"] = None, Resources: "simplepdl_RequeteDeRessource" = None):
        self.quantite = quantite
        self.name = name
        self.resources = resources if resources is not None else set()
        self.Resources = Resources
        
    @property
    def quantite(self) -> int:
        return self.__quantite

    @quantite.setter
    def quantite(self, quantite: int):
        self.__quantite = quantite

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Resources(self):
        return self.__Resources

    @Resources.setter
    def Resources(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Resources__Resources", None)
        self.__Resources = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "linktoresource"):
                opp_val = getattr(old_value, "linktoresource", None)
                if opp_val == self:
                    setattr(old_value, "linktoresource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "linktoresource"):
                opp_val = getattr(value, "linktoresource", None)
                setattr(value, "linktoresource", self)

    @property
    def resources(self):
        return self.__resources

    @resources.setter
    def resources(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Resources__resources", None)
        self.__resources = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RequeteDeRessource11"):
                    opp_val = getattr(item, "RequeteDeRessource11", None)
                    
                    if opp_val == self:
                        setattr(item, "RequeteDeRessource11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RequeteDeRessource11"):
                    opp_val = getattr(item, "RequeteDeRessource11", None)
                    
                    setattr(item, "RequeteDeRessource11", self)
                    

class simplepdl_RequeteDeRessource(ProcessElement):

    def __init__(self, quantite: int, RequeteDeRessource: "simplepdl_WorkDefinition" = None, RequeteDeRessource11: "simplepdl_Resources" = None, linktoresource: "simplepdl_Resources" = None, linktoresource14: "simplepdl_WorkDefinition" = None):
        self.quantite = quantite
        self.RequeteDeRessource = RequeteDeRessource
        self.RequeteDeRessource11 = RequeteDeRessource11
        self.linktoresource = linktoresource
        self.linktoresource14 = linktoresource14
        
    @property
    def quantite(self) -> int:
        return self.__quantite

    @quantite.setter
    def quantite(self, quantite: int):
        self.__quantite = quantite

    @property
    def RequeteDeRessource11(self):
        return self.__RequeteDeRessource11

    @RequeteDeRessource11.setter
    def RequeteDeRessource11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_RequeteDeRessource__RequeteDeRessource11", None)
        self.__RequeteDeRessource11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resources"):
                opp_val = getattr(old_value, "resources", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resources"):
                opp_val = getattr(value, "resources", None)
                if opp_val is None:
                    setattr(value, "resources", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def linktoresource14(self):
        return self.__linktoresource14

    @linktoresource14.setter
    def linktoresource14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_RequeteDeRessource__linktoresource14", None)
        self.__linktoresource14 = value
        
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
    def linktoresource(self):
        return self.__linktoresource

    @linktoresource.setter
    def linktoresource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_RequeteDeRessource__linktoresource", None)
        self.__linktoresource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Resources"):
                opp_val = getattr(old_value, "Resources", None)
                if opp_val == self:
                    setattr(old_value, "Resources", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Resources"):
                opp_val = getattr(value, "Resources", None)
                setattr(value, "Resources", self)

    @property
    def RequeteDeRessource(self):
        return self.__RequeteDeRessource

    @RequeteDeRessource.setter
    def RequeteDeRessource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_RequeteDeRessource__RequeteDeRessource", None)
        self.__RequeteDeRessource = value
        
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

class simplepdl_GuidanceLink(ProcessElement):

    pass
class simplepdl_WorkSequence(ProcessElement):

    def __init__(self, linkType: str, linksToSuccessors: "simplepdl_WorkDefinition" = None, linksToPredecessors: "simplepdl_WorkDefinition" = None, WorkSequence: "simplepdl_WorkDefinition" = None, WorkSequence3: "simplepdl_WorkDefinition" = None):
        self.linkType = linkType
        self.linksToSuccessors = linksToSuccessors
        self.linksToPredecessors = linksToPredecessors
        self.WorkSequence = WorkSequence
        self.WorkSequence3 = WorkSequence3
        
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

class simplepdl_WorkDefinition(ProcessElement):

    def __init__(self, name: str, WorkDefinition: "simplepdl_WorkSequence" = None, WorkDefinition7: "simplepdl_WorkSequence" = None, successor: set["simplepdl_WorkSequence"] = None, predecessor: set["simplepdl_WorkSequence"] = None, workdefinition: set["simplepdl_RequeteDeRessource"] = None, WorkDefinition15: "simplepdl_RequeteDeRessource" = None, simplepdl_WorkDefinition: "simplepdl_GuidanceLink" = None):
        self.name = name
        self.WorkDefinition = WorkDefinition
        self.WorkDefinition7 = WorkDefinition7
        self.successor = successor if successor is not None else set()
        self.predecessor = predecessor if predecessor is not None else set()
        self.workdefinition = workdefinition if workdefinition is not None else set()
        self.WorkDefinition15 = WorkDefinition15
        self.simplepdl_WorkDefinition = simplepdl_WorkDefinition
        
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
    def WorkDefinition15(self):
        return self.__WorkDefinition15

    @WorkDefinition15.setter
    def WorkDefinition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkDefinition__WorkDefinition15", None)
        self.__WorkDefinition15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "linktoresource14"):
                opp_val = getattr(old_value, "linktoresource14", None)
                if opp_val == self:
                    setattr(old_value, "linktoresource14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "linktoresource14"):
                opp_val = getattr(value, "linktoresource14", None)
                setattr(value, "linktoresource14", self)

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
            if hasattr(old_value, "simplepdl_GuidanceLink19"):
                opp_val = getattr(old_value, "simplepdl_GuidanceLink19", None)
                if opp_val == self:
                    setattr(old_value, "simplepdl_GuidanceLink19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplepdl_GuidanceLink19"):
                opp_val = getattr(value, "simplepdl_GuidanceLink19", None)
                setattr(value, "simplepdl_GuidanceLink19", self)

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
                if hasattr(item, "RequeteDeRessource"):
                    opp_val = getattr(item, "RequeteDeRessource", None)
                    
                    if opp_val == self:
                        setattr(item, "RequeteDeRessource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RequeteDeRessource"):
                    opp_val = getattr(item, "RequeteDeRessource", None)
                    
                    setattr(item, "RequeteDeRessource", self)
                    

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
                    

class simplepdl_ProcessElement(ABC):

    pass
class simplepdl_Process:

    def __init__(self, name: str, simplepdl_Process: set["simplepdl_ProcessElement"] = None):
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
                    

class simplepdl_Guidance(ProcessElement):

    def __init__(self, text: str, simplepdl_Guidance: set["simplepdl_ProcessElement"] = None, simplepdl_Guidance17: "simplepdl_GuidanceLink" = None):
        self.text = text
        self.simplepdl_Guidance = simplepdl_Guidance if simplepdl_Guidance is not None else set()
        self.simplepdl_Guidance17 = simplepdl_Guidance17
        
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
                if hasattr(item, "simplepdl_ProcessElement9"):
                    opp_val = getattr(item, "simplepdl_ProcessElement9", None)
                    
                    if opp_val == self:
                        setattr(item, "simplepdl_ProcessElement9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simplepdl_ProcessElement9"):
                    opp_val = getattr(item, "simplepdl_ProcessElement9", None)
                    
                    setattr(item, "simplepdl_ProcessElement9", self)
                    

    @property
    def simplepdl_Guidance17(self):
        return self.__simplepdl_Guidance17

    @simplepdl_Guidance17.setter
    def simplepdl_Guidance17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Guidance__simplepdl_Guidance17", None)
        self.__simplepdl_Guidance17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplepdl_GuidanceLink"):
                opp_val = getattr(old_value, "simplepdl_GuidanceLink", None)
                if opp_val == self:
                    setattr(old_value, "simplepdl_GuidanceLink", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplepdl_GuidanceLink"):
                opp_val = getattr(value, "simplepdl_GuidanceLink", None)
                setattr(value, "simplepdl_GuidanceLink", self)
