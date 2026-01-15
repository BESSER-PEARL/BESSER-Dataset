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
                    

class simplepdl_WorkSequence(ProcessElement):

    def __init__(self, linkType: str, WorkSequence: "simplepdl_WorkDefinition" = None, WorkSequence4: "simplepdl_WorkDefinition" = None, linksToPredecessors: "simplepdl_WorkDefinition" = None, linksToSuccessors: "simplepdl_WorkDefinition" = None):
        self.linkType = linkType
        self.WorkSequence = WorkSequence
        self.WorkSequence4 = WorkSequence4
        self.linksToPredecessors = linksToPredecessors
        self.linksToSuccessors = linksToSuccessors
        
    @property
    def linkType(self) -> str:
        return self.__linkType

    @linkType.setter
    def linkType(self, linkType: str):
        self.__linkType = linkType

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
            if hasattr(old_value, "WorkDefinition8"):
                opp_val = getattr(old_value, "WorkDefinition8", None)
                if opp_val == self:
                    setattr(old_value, "WorkDefinition8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorkDefinition8"):
                opp_val = getattr(value, "WorkDefinition8", None)
                setattr(value, "WorkDefinition8", self)

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
    def WorkSequence4(self):
        return self.__WorkSequence4

    @WorkSequence4.setter
    def WorkSequence4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkSequence__WorkSequence4", None)
        self.__WorkSequence4 = value
        
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

class simplepdl_Need(ProcessElement):

    def __init__(self, quantity: int, simplepdl_Need: "simplepdl_Ressource" = None, needs: "simplepdl_NeedSet" = None, Need: "simplepdl_NeedSet" = None):
        self.quantity = quantity
        self.simplepdl_Need = simplepdl_Need
        self.needs = needs
        self.Need = Need
        
    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def Need(self):
        return self.__Need

    @Need.setter
    def Need(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Need__Need", None)
        self.__Need = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "needSet"):
                opp_val = getattr(old_value, "needSet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "needSet"):
                opp_val = getattr(value, "needSet", None)
                if opp_val is None:
                    setattr(value, "needSet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simplepdl_Need(self):
        return self.__simplepdl_Need

    @simplepdl_Need.setter
    def simplepdl_Need(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Need__simplepdl_Need", None)
        self.__simplepdl_Need = value
        
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
    def needs(self):
        return self.__needs

    @needs.setter
    def needs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Need__needs", None)
        self.__needs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NeedSet12"):
                opp_val = getattr(old_value, "NeedSet12", None)
                if opp_val == self:
                    setattr(old_value, "NeedSet12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NeedSet12"):
                opp_val = getattr(value, "NeedSet12", None)
                setattr(value, "NeedSet12", self)

class simplepdl_NeedSet(ProcessElement):

    def __init__(self, name: str, NeedSet: "simplepdl_WorkDefinition" = None, NeedSet12: "simplepdl_Need" = None, needSet: set["simplepdl_Need"] = None, needSets: "simplepdl_WorkDefinition" = None):
        self.name = name
        self.NeedSet = NeedSet
        self.NeedSet12 = NeedSet12
        self.needSet = needSet if needSet is not None else set()
        self.needSets = needSets
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def NeedSet12(self):
        return self.__NeedSet12

    @NeedSet12.setter
    def NeedSet12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_NeedSet__NeedSet12", None)
        self.__NeedSet12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "needs"):
                opp_val = getattr(old_value, "needs", None)
                if opp_val == self:
                    setattr(old_value, "needs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "needs"):
                opp_val = getattr(value, "needs", None)
                setattr(value, "needs", self)

    @property
    def needSets(self):
        return self.__needSets

    @needSets.setter
    def needSets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_NeedSet__needSets", None)
        self.__needSets = value
        
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
    def needSet(self):
        return self.__needSet

    @needSet.setter
    def needSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_NeedSet__needSet", None)
        self.__needSet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Need"):
                    opp_val = getattr(item, "Need", None)
                    
                    if opp_val == self:
                        setattr(item, "Need", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Need"):
                    opp_val = getattr(item, "Need", None)
                    
                    setattr(item, "Need", self)
                    

    @property
    def NeedSet(self):
        return self.__NeedSet

    @NeedSet.setter
    def NeedSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_NeedSet__NeedSet", None)
        self.__NeedSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wd"):
                opp_val = getattr(old_value, "wd", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wd"):
                opp_val = getattr(value, "wd", None)
                if opp_val is None:
                    setattr(value, "wd", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simplepdl_Ressource(ProcessElement):

    def __init__(self, name: str, quantity: int, simplepdl_Ressource: "simplepdl_Need" = None):
        self.name = name
        self.quantity = quantity
        self.simplepdl_Ressource = simplepdl_Ressource
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "simplepdl_Need"):
                opp_val = getattr(old_value, "simplepdl_Need", None)
                if opp_val == self:
                    setattr(old_value, "simplepdl_Need", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplepdl_Need"):
                opp_val = getattr(value, "simplepdl_Need", None)
                setattr(value, "simplepdl_Need", self)

class simplepdl_WorkDefinition(ProcessElement):

    def __init__(self, name: str, successor: set["simplepdl_WorkSequence"] = None, predecessor: set["simplepdl_WorkSequence"] = None, wd: set["simplepdl_NeedSet"] = None, WorkDefinition8: "simplepdl_WorkSequence" = None, WorkDefinition: "simplepdl_WorkSequence" = None, WorkDefinition15: "simplepdl_NeedSet" = None):
        self.name = name
        self.successor = successor if successor is not None else set()
        self.predecessor = predecessor if predecessor is not None else set()
        self.wd = wd if wd is not None else set()
        self.WorkDefinition8 = WorkDefinition8
        self.WorkDefinition = WorkDefinition
        self.WorkDefinition15 = WorkDefinition15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "needSets"):
                opp_val = getattr(old_value, "needSets", None)
                if opp_val == self:
                    setattr(old_value, "needSets", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "needSets"):
                opp_val = getattr(value, "needSets", None)
                setattr(value, "needSets", self)

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
    def wd(self):
        return self.__wd

    @wd.setter
    def wd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkDefinition__wd", None)
        self.__wd = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NeedSet"):
                    opp_val = getattr(item, "NeedSet", None)
                    
                    if opp_val == self:
                        setattr(item, "NeedSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NeedSet"):
                    opp_val = getattr(item, "NeedSet", None)
                    
                    setattr(item, "NeedSet", self)
                    

    @property
    def WorkDefinition8(self):
        return self.__WorkDefinition8

    @WorkDefinition8.setter
    def WorkDefinition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkDefinition__WorkDefinition8", None)
        self.__WorkDefinition8 = value
        
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
                if hasattr(item, "WorkSequence4"):
                    opp_val = getattr(item, "WorkSequence4", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkSequence4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkSequence4"):
                    opp_val = getattr(item, "WorkSequence4", None)
                    
                    setattr(item, "WorkSequence4", self)
                    

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
                    
