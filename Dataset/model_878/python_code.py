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

class simplepdl_RessourceConfig(ProcessElement):

    def __init__(self, name: str, RessourceConfig: "simplepdl_WorkDefinition" = None, RessourceConfig12: "simplepdl_RessourceInstance" = None, linksToRessources: "simplepdl_WorkDefinition" = None, config: set["simplepdl_RessourceInstance"] = None):
        self.name = name
        self.RessourceConfig = RessourceConfig
        self.RessourceConfig12 = RessourceConfig12
        self.linksToRessources = linksToRessources
        self.config = config if config is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def RessourceConfig(self):
        return self.__RessourceConfig

    @RessourceConfig.setter
    def RessourceConfig(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_RessourceConfig__RessourceConfig", None)
        self.__RessourceConfig = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activity"):
                opp_val = getattr(old_value, "activity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activity"):
                opp_val = getattr(value, "activity", None)
                if opp_val is None:
                    setattr(value, "activity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RessourceConfig12(self):
        return self.__RessourceConfig12

    @RessourceConfig12.setter
    def RessourceConfig12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_RessourceConfig__RessourceConfig12", None)
        self.__RessourceConfig12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ressources"):
                opp_val = getattr(old_value, "ressources", None)
                if opp_val == self:
                    setattr(old_value, "ressources", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ressources"):
                opp_val = getattr(value, "ressources", None)
                setattr(value, "ressources", self)

    @property
    def linksToRessources(self):
        return self.__linksToRessources

    @linksToRessources.setter
    def linksToRessources(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_RessourceConfig__linksToRessources", None)
        self.__linksToRessources = value
        
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
    def config(self):
        return self.__config

    @config.setter
    def config(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_RessourceConfig__config", None)
        self.__config = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RessourceInstance"):
                    opp_val = getattr(item, "RessourceInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "RessourceInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RessourceInstance"):
                    opp_val = getattr(item, "RessourceInstance", None)
                    
                    setattr(item, "RessourceInstance", self)
                    

class simplepdl_WorkDefinition(ProcessElement):

    def __init__(self, name: str, min_time: int, max_time: int, successor: set["simplepdl_WorkSequence"] = None, predecessor: set["simplepdl_WorkSequence"] = None, activity: set["simplepdl_RessourceConfig"] = None, WorkDefinition: "simplepdl_WorkSequence" = None, WorkDefinition7: "simplepdl_WorkSequence" = None, WorkDefinition14: "simplepdl_RessourceConfig" = None):
        self.name = name
        self.min_time = min_time
        self.max_time = max_time
        self.successor = successor if successor is not None else set()
        self.predecessor = predecessor if predecessor is not None else set()
        self.activity = activity if activity is not None else set()
        self.WorkDefinition = WorkDefinition
        self.WorkDefinition7 = WorkDefinition7
        self.WorkDefinition14 = WorkDefinition14
        
    @property
    def max_time(self) -> int:
        return self.__max_time

    @max_time.setter
    def max_time(self, max_time: int):
        self.__max_time = max_time

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def min_time(self) -> int:
        return self.__min_time

    @min_time.setter
    def min_time(self, min_time: int):
        self.__min_time = min_time

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
            if hasattr(old_value, "linksToRessources"):
                opp_val = getattr(old_value, "linksToRessources", None)
                if opp_val == self:
                    setattr(old_value, "linksToRessources", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "linksToRessources"):
                opp_val = getattr(value, "linksToRessources", None)
                setattr(value, "linksToRessources", self)

    @property
    def activity(self):
        return self.__activity

    @activity.setter
    def activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkDefinition__activity", None)
        self.__activity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RessourceConfig"):
                    opp_val = getattr(item, "RessourceConfig", None)
                    
                    if opp_val == self:
                        setattr(item, "RessourceConfig", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RessourceConfig"):
                    opp_val = getattr(item, "RessourceConfig", None)
                    
                    setattr(item, "RessourceConfig", self)
                    

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
class simplepdl_RessourceInstance(ProcessElement):

    def __init__(self, instances: int, simplepdl_RessourceInstance: "simplepdl_RessourceDefinition" = None, ressources: "simplepdl_RessourceConfig" = None, RessourceInstance: "simplepdl_RessourceConfig" = None):
        self.instances = instances
        self.simplepdl_RessourceInstance = simplepdl_RessourceInstance
        self.ressources = ressources
        self.RessourceInstance = RessourceInstance
        
    @property
    def instances(self) -> int:
        return self.__instances

    @instances.setter
    def instances(self, instances: int):
        self.__instances = instances

    @property
    def ressources(self):
        return self.__ressources

    @ressources.setter
    def ressources(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_RessourceInstance__ressources", None)
        self.__ressources = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RessourceConfig12"):
                opp_val = getattr(old_value, "RessourceConfig12", None)
                if opp_val == self:
                    setattr(old_value, "RessourceConfig12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RessourceConfig12"):
                opp_val = getattr(value, "RessourceConfig12", None)
                setattr(value, "RessourceConfig12", self)

    @property
    def RessourceInstance(self):
        return self.__RessourceInstance

    @RessourceInstance.setter
    def RessourceInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_RessourceInstance__RessourceInstance", None)
        self.__RessourceInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "config"):
                opp_val = getattr(old_value, "config", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "config"):
                opp_val = getattr(value, "config", None)
                if opp_val is None:
                    setattr(value, "config", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simplepdl_RessourceInstance(self):
        return self.__simplepdl_RessourceInstance

    @simplepdl_RessourceInstance.setter
    def simplepdl_RessourceInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_RessourceInstance__simplepdl_RessourceInstance", None)
        self.__simplepdl_RessourceInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplepdl_RessourceDefinition"):
                opp_val = getattr(old_value, "simplepdl_RessourceDefinition", None)
                if opp_val == self:
                    setattr(old_value, "simplepdl_RessourceDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplepdl_RessourceDefinition"):
                opp_val = getattr(value, "simplepdl_RessourceDefinition", None)
                setattr(value, "simplepdl_RessourceDefinition", self)

class simplepdl_RessourceDefinition(ProcessElement):

    def __init__(self, name: str, number: int, simplepdl_RessourceDefinition: "simplepdl_RessourceInstance" = None):
        self.name = name
        self.number = number
        self.simplepdl_RessourceDefinition = simplepdl_RessourceDefinition
        
    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simplepdl_RessourceDefinition(self):
        return self.__simplepdl_RessourceDefinition

    @simplepdl_RessourceDefinition.setter
    def simplepdl_RessourceDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_RessourceDefinition__simplepdl_RessourceDefinition", None)
        self.__simplepdl_RessourceDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplepdl_RessourceInstance"):
                opp_val = getattr(old_value, "simplepdl_RessourceInstance", None)
                if opp_val == self:
                    setattr(old_value, "simplepdl_RessourceInstance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplepdl_RessourceInstance"):
                opp_val = getattr(value, "simplepdl_RessourceInstance", None)
                setattr(value, "simplepdl_RessourceInstance", self)

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
                    

class simplepdl_Process:

    def __init__(self, name: str, min_time: int, max_time: int, simplepdl_Process: set["simplepdl_ProcessElement"] = None):
        self.name = name
        self.min_time = min_time
        self.max_time = max_time
        self.simplepdl_Process = simplepdl_Process if simplepdl_Process is not None else set()
        
    @property
    def min_time(self) -> int:
        return self.__min_time

    @min_time.setter
    def min_time(self, min_time: int):
        self.__min_time = min_time

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def max_time(self) -> int:
        return self.__max_time

    @max_time.setter
    def max_time(self, max_time: int):
        self.__max_time = max_time

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
                    
