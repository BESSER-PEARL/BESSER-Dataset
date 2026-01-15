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

class ProcessElement:

    pass
class SimplePDL_ResourceType(ProcessElement):

    def __init__(self, name: str, occurrences: int, SimplePDL_ResourceType: "SimplePDL_Resource" = None):
        self.name = name
        self.occurrences = occurrences
        self.SimplePDL_ResourceType = SimplePDL_ResourceType
        
    @property
    def occurrences(self) -> int:
        return self.__occurrences

    @occurrences.setter
    def occurrences(self, occurrences: int):
        self.__occurrences = occurrences

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SimplePDL_ResourceType(self):
        return self.__SimplePDL_ResourceType

    @SimplePDL_ResourceType.setter
    def SimplePDL_ResourceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDL_ResourceType__SimplePDL_ResourceType", None)
        self.__SimplePDL_ResourceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplePDL_Resource"):
                opp_val = getattr(old_value, "SimplePDL_Resource", None)
                if opp_val == self:
                    setattr(old_value, "SimplePDL_Resource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplePDL_Resource"):
                opp_val = getattr(value, "SimplePDL_Resource", None)
                setattr(value, "SimplePDL_Resource", self)

class SimplePDL_WorkDefinition(ProcessElement):

    def __init__(self, name: str, minTime: int, maxTime: int, successor: set["SimplePDL_WorkSequence"] = None, predecessor: set["SimplePDL_WorkSequence"] = None, workDefinition: set["SimplePDL_Resource"] = None, parent: set["SimplePDL_ProcessElement"] = None, WorkDefinition: "SimplePDL_WorkSequence" = None, WorkDefinition10: "SimplePDL_WorkSequence" = None, WorkDefinition15: "SimplePDL_ProcessElement" = None, WorkDefinition17: "SimplePDL_Resource" = None):
        self.name = name
        self.minTime = minTime
        self.maxTime = maxTime
        self.successor = successor if successor is not None else set()
        self.predecessor = predecessor if predecessor is not None else set()
        self.workDefinition = workDefinition if workDefinition is not None else set()
        self.parent = parent if parent is not None else set()
        self.WorkDefinition = WorkDefinition
        self.WorkDefinition10 = WorkDefinition10
        self.WorkDefinition15 = WorkDefinition15
        self.WorkDefinition17 = WorkDefinition17
        
    @property
    def maxTime(self) -> int:
        return self.__maxTime

    @maxTime.setter
    def maxTime(self, maxTime: int):
        self.__maxTime = maxTime

    @property
    def minTime(self) -> int:
        return self.__minTime

    @minTime.setter
    def minTime(self, minTime: int):
        self.__minTime = minTime

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDL_WorkDefinition__parent", None)
        self.__parent = value if value is not None else set()
        
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
                    

    @property
    def WorkDefinition10(self):
        return self.__WorkDefinition10

    @WorkDefinition10.setter
    def WorkDefinition10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDL_WorkDefinition__WorkDefinition10", None)
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
    def workDefinition(self):
        return self.__workDefinition

    @workDefinition.setter
    def workDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDL_WorkDefinition__workDefinition", None)
        self.__workDefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Resource"):
                    opp_val = getattr(item, "Resource", None)
                    
                    if opp_val == self:
                        setattr(item, "Resource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Resource"):
                    opp_val = getattr(item, "Resource", None)
                    
                    setattr(item, "Resource", self)
                    

    @property
    def predecessor(self):
        return self.__predecessor

    @predecessor.setter
    def predecessor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDL_WorkDefinition__predecessor", None)
        self.__predecessor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WorkSequence5"):
                    opp_val = getattr(item, "WorkSequence5", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkSequence5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkSequence5"):
                    opp_val = getattr(item, "WorkSequence5", None)
                    
                    setattr(item, "WorkSequence5", self)
                    

    @property
    def successor(self):
        return self.__successor

    @successor.setter
    def successor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDL_WorkDefinition__successor", None)
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
        old_value = getattr(self, f"_SimplePDL_WorkDefinition__WorkDefinition15", None)
        self.__WorkDefinition15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "child"):
                opp_val = getattr(old_value, "child", None)
                if opp_val == self:
                    setattr(old_value, "child", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "child"):
                opp_val = getattr(value, "child", None)
                setattr(value, "child", self)

    @property
    def WorkDefinition(self):
        return self.__WorkDefinition

    @WorkDefinition.setter
    def WorkDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDL_WorkDefinition__WorkDefinition", None)
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
    def WorkDefinition17(self):
        return self.__WorkDefinition17

    @WorkDefinition17.setter
    def WorkDefinition17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDL_WorkDefinition__WorkDefinition17", None)
        self.__WorkDefinition17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "neededResources"):
                opp_val = getattr(old_value, "neededResources", None)
                if opp_val == self:
                    setattr(old_value, "neededResources", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "neededResources"):
                opp_val = getattr(value, "neededResources", None)
                setattr(value, "neededResources", self)

class SimplePDL_Guidance:

    def __init__(self, text: str, SimplePDL_Guidance: "SimplePDL_Process" = None, SimplePDL_Guidance13: "SimplePDL_ProcessElement" = None):
        self.text = text
        self.SimplePDL_Guidance = SimplePDL_Guidance
        self.SimplePDL_Guidance13 = SimplePDL_Guidance13
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def SimplePDL_Guidance13(self):
        return self.__SimplePDL_Guidance13

    @SimplePDL_Guidance13.setter
    def SimplePDL_Guidance13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDL_Guidance__SimplePDL_Guidance13", None)
        self.__SimplePDL_Guidance13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplePDL_ProcessElement12"):
                opp_val = getattr(old_value, "SimplePDL_ProcessElement12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplePDL_ProcessElement12"):
                opp_val = getattr(value, "SimplePDL_ProcessElement12", None)
                if opp_val is None:
                    setattr(value, "SimplePDL_ProcessElement12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SimplePDL_Guidance(self):
        return self.__SimplePDL_Guidance

    @SimplePDL_Guidance.setter
    def SimplePDL_Guidance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDL_Guidance__SimplePDL_Guidance", None)
        self.__SimplePDL_Guidance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplePDL_Process2"):
                opp_val = getattr(old_value, "SimplePDL_Process2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplePDL_Process2"):
                opp_val = getattr(value, "SimplePDL_Process2", None)
                if opp_val is None:
                    setattr(value, "SimplePDL_Process2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SimplePDL_ProcessElement:

    pass
class SimplePDL_Process:

    def __init__(self, name: str, minTime: int, maxTime: int, SimplePDL_Process: set["SimplePDL_ProcessElement"] = None, SimplePDL_Process2: set["SimplePDL_Guidance"] = None):
        self.name = name
        self.minTime = minTime
        self.maxTime = maxTime
        self.SimplePDL_Process = SimplePDL_Process if SimplePDL_Process is not None else set()
        self.SimplePDL_Process2 = SimplePDL_Process2 if SimplePDL_Process2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def maxTime(self) -> int:
        return self.__maxTime

    @maxTime.setter
    def maxTime(self, maxTime: int):
        self.__maxTime = maxTime

    @property
    def minTime(self) -> int:
        return self.__minTime

    @minTime.setter
    def minTime(self, minTime: int):
        self.__minTime = minTime

    @property
    def SimplePDL_Process(self):
        return self.__SimplePDL_Process

    @SimplePDL_Process.setter
    def SimplePDL_Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDL_Process__SimplePDL_Process", None)
        self.__SimplePDL_Process = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SimplePDL_ProcessElement"):
                    opp_val = getattr(item, "SimplePDL_ProcessElement", None)
                    
                    if opp_val == self:
                        setattr(item, "SimplePDL_ProcessElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SimplePDL_ProcessElement"):
                    opp_val = getattr(item, "SimplePDL_ProcessElement", None)
                    
                    setattr(item, "SimplePDL_ProcessElement", self)
                    

    @property
    def SimplePDL_Process2(self):
        return self.__SimplePDL_Process2

    @SimplePDL_Process2.setter
    def SimplePDL_Process2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDL_Process__SimplePDL_Process2", None)
        self.__SimplePDL_Process2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SimplePDL_Guidance"):
                    opp_val = getattr(item, "SimplePDL_Guidance", None)
                    
                    if opp_val == self:
                        setattr(item, "SimplePDL_Guidance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SimplePDL_Guidance"):
                    opp_val = getattr(item, "SimplePDL_Guidance", None)
                    
                    setattr(item, "SimplePDL_Guidance", self)
                    

class SimplePDL_Resource(ProcessElement):

    def __init__(self, occurrences: int, Resource: "SimplePDL_WorkDefinition" = None, neededResources: "SimplePDL_WorkDefinition" = None, SimplePDL_Resource: "SimplePDL_ResourceType" = None):
        self.occurrences = occurrences
        self.Resource = Resource
        self.neededResources = neededResources
        self.SimplePDL_Resource = SimplePDL_Resource
        
    @property
    def occurrences(self) -> int:
        return self.__occurrences

    @occurrences.setter
    def occurrences(self, occurrences: int):
        self.__occurrences = occurrences

    @property
    def SimplePDL_Resource(self):
        return self.__SimplePDL_Resource

    @SimplePDL_Resource.setter
    def SimplePDL_Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDL_Resource__SimplePDL_Resource", None)
        self.__SimplePDL_Resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplePDL_ResourceType"):
                opp_val = getattr(old_value, "SimplePDL_ResourceType", None)
                if opp_val == self:
                    setattr(old_value, "SimplePDL_ResourceType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplePDL_ResourceType"):
                opp_val = getattr(value, "SimplePDL_ResourceType", None)
                setattr(value, "SimplePDL_ResourceType", self)

    @property
    def Resource(self):
        return self.__Resource

    @Resource.setter
    def Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDL_Resource__Resource", None)
        self.__Resource = value
        
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
    def neededResources(self):
        return self.__neededResources

    @neededResources.setter
    def neededResources(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDL_Resource__neededResources", None)
        self.__neededResources = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorkDefinition17"):
                opp_val = getattr(old_value, "WorkDefinition17", None)
                if opp_val == self:
                    setattr(old_value, "WorkDefinition17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorkDefinition17"):
                opp_val = getattr(value, "WorkDefinition17", None)
                setattr(value, "WorkDefinition17", self)

class SimplePDL_WorkSequence(ProcessElement):

    def __init__(self, linkType: str, WorkSequence: "SimplePDL_WorkDefinition" = None, WorkSequence5: "SimplePDL_WorkDefinition" = None, linksToSuccessors: "SimplePDL_WorkDefinition" = None, linksToPredecessors: "SimplePDL_WorkDefinition" = None):
        self.linkType = linkType
        self.WorkSequence = WorkSequence
        self.WorkSequence5 = WorkSequence5
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
        old_value = getattr(self, f"_SimplePDL_WorkSequence__WorkSequence", None)
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
    def WorkSequence5(self):
        return self.__WorkSequence5

    @WorkSequence5.setter
    def WorkSequence5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDL_WorkSequence__WorkSequence5", None)
        self.__WorkSequence5 = value
        
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
        old_value = getattr(self, f"_SimplePDL_WorkSequence__linksToPredecessors", None)
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
    def linksToSuccessors(self):
        return self.__linksToSuccessors

    @linksToSuccessors.setter
    def linksToSuccessors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDL_WorkSequence__linksToSuccessors", None)
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
