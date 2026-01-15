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

class iritpdl_ResourceConf:

    def __init__(self, name: str, ResourceConf21: "iritpdl_Resource" = None, resourceConf: "iritpdl_WorkDefinition" = None, resourceConf25: set["iritpdl_Resource"] = None, ResourceConf: "iritpdl_WorkDefinition" = None):
        self.name = name
        self.ResourceConf21 = ResourceConf21
        self.resourceConf = resourceConf
        self.resourceConf25 = resourceConf25 if resourceConf25 is not None else set()
        self.ResourceConf = ResourceConf
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ResourceConf(self):
        return self.__ResourceConf

    @ResourceConf.setter
    def ResourceConf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritpdl_ResourceConf__ResourceConf", None)
        self.__ResourceConf = value
        
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
    def ResourceConf21(self):
        return self.__ResourceConf21

    @ResourceConf21.setter
    def ResourceConf21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritpdl_ResourceConf__ResourceConf21", None)
        self.__ResourceConf21 = value
        
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

    @property
    def resourceConf(self):
        return self.__resourceConf

    @resourceConf.setter
    def resourceConf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritpdl_ResourceConf__resourceConf", None)
        self.__resourceConf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorkDefinition23"):
                opp_val = getattr(old_value, "WorkDefinition23", None)
                if opp_val == self:
                    setattr(old_value, "WorkDefinition23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorkDefinition23"):
                opp_val = getattr(value, "WorkDefinition23", None)
                setattr(value, "WorkDefinition23", self)

    @property
    def resourceConf25(self):
        return self.__resourceConf25

    @resourceConf25.setter
    def resourceConf25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritpdl_ResourceConf__resourceConf25", None)
        self.__resourceConf25 = value if value is not None else set()
        
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
                    

class iritpdl_Resource:

    def __init__(self, occurrences: int, iritpdl_Resource: "iritpdl_ResourceType" = None, neededResources: "iritpdl_ResourceConf" = None, Resource: "iritpdl_ResourceConf" = None):
        self.occurrences = occurrences
        self.iritpdl_Resource = iritpdl_Resource
        self.neededResources = neededResources
        self.Resource = Resource
        
    @property
    def occurrences(self) -> int:
        return self.__occurrences

    @occurrences.setter
    def occurrences(self, occurrences: int):
        self.__occurrences = occurrences

    @property
    def Resource(self):
        return self.__Resource

    @Resource.setter
    def Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritpdl_Resource__Resource", None)
        self.__Resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceConf25"):
                opp_val = getattr(old_value, "resourceConf25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceConf25"):
                opp_val = getattr(value, "resourceConf25", None)
                if opp_val is None:
                    setattr(value, "resourceConf25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iritpdl_Resource(self):
        return self.__iritpdl_Resource

    @iritpdl_Resource.setter
    def iritpdl_Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritpdl_Resource__iritpdl_Resource", None)
        self.__iritpdl_Resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iritpdl_ResourceType19"):
                opp_val = getattr(old_value, "iritpdl_ResourceType19", None)
                if opp_val == self:
                    setattr(old_value, "iritpdl_ResourceType19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iritpdl_ResourceType19"):
                opp_val = getattr(value, "iritpdl_ResourceType19", None)
                setattr(value, "iritpdl_ResourceType19", self)

    @property
    def neededResources(self):
        return self.__neededResources

    @neededResources.setter
    def neededResources(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritpdl_Resource__neededResources", None)
        self.__neededResources = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceConf21"):
                opp_val = getattr(old_value, "ResourceConf21", None)
                if opp_val == self:
                    setattr(old_value, "ResourceConf21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceConf21"):
                opp_val = getattr(value, "ResourceConf21", None)
                setattr(value, "ResourceConf21", self)

class iritpdl_Process:

    def __init__(self, name: str, minTime: int, maxTime: int, iritpdl_Process: set["iritpdl_ProcessElement"] = None, iritpdl_Process2: set["iritpdl_Guidance"] = None, iritpdl_Process4: set["iritpdl_ResourceType"] = None):
        self.name = name
        self.minTime = minTime
        self.maxTime = maxTime
        self.iritpdl_Process = iritpdl_Process if iritpdl_Process is not None else set()
        self.iritpdl_Process2 = iritpdl_Process2 if iritpdl_Process2 is not None else set()
        self.iritpdl_Process4 = iritpdl_Process4 if iritpdl_Process4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def minTime(self) -> int:
        return self.__minTime

    @minTime.setter
    def minTime(self, minTime: int):
        self.__minTime = minTime

    @property
    def maxTime(self) -> int:
        return self.__maxTime

    @maxTime.setter
    def maxTime(self, maxTime: int):
        self.__maxTime = maxTime

    @property
    def iritpdl_Process2(self):
        return self.__iritpdl_Process2

    @iritpdl_Process2.setter
    def iritpdl_Process2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritpdl_Process__iritpdl_Process2", None)
        self.__iritpdl_Process2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iritpdl_Guidance"):
                    opp_val = getattr(item, "iritpdl_Guidance", None)
                    
                    if opp_val == self:
                        setattr(item, "iritpdl_Guidance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iritpdl_Guidance"):
                    opp_val = getattr(item, "iritpdl_Guidance", None)
                    
                    setattr(item, "iritpdl_Guidance", self)
                    

    @property
    def iritpdl_Process4(self):
        return self.__iritpdl_Process4

    @iritpdl_Process4.setter
    def iritpdl_Process4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritpdl_Process__iritpdl_Process4", None)
        self.__iritpdl_Process4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iritpdl_ResourceType"):
                    opp_val = getattr(item, "iritpdl_ResourceType", None)
                    
                    if opp_val == self:
                        setattr(item, "iritpdl_ResourceType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iritpdl_ResourceType"):
                    opp_val = getattr(item, "iritpdl_ResourceType", None)
                    
                    setattr(item, "iritpdl_ResourceType", self)
                    

    @property
    def iritpdl_Process(self):
        return self.__iritpdl_Process

    @iritpdl_Process.setter
    def iritpdl_Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritpdl_Process__iritpdl_Process", None)
        self.__iritpdl_Process = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iritpdl_ProcessElement"):
                    opp_val = getattr(item, "iritpdl_ProcessElement", None)
                    
                    if opp_val == self:
                        setattr(item, "iritpdl_ProcessElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iritpdl_ProcessElement"):
                    opp_val = getattr(item, "iritpdl_ProcessElement", None)
                    
                    setattr(item, "iritpdl_ProcessElement", self)
                    

class ProcessElement:

    pass
class iritpdl_WorkSequence(ProcessElement):

    def __init__(self, linkType: str, WorkSequence: "iritpdl_WorkDefinition" = None, WorkSequence7: "iritpdl_WorkDefinition" = None, linksToSuccessors: "iritpdl_WorkDefinition" = None, linksToPredecessors: "iritpdl_WorkDefinition" = None):
        self.linkType = linkType
        self.WorkSequence = WorkSequence
        self.WorkSequence7 = WorkSequence7
        self.linksToSuccessors = linksToSuccessors
        self.linksToPredecessors = linksToPredecessors
        
    @property
    def linkType(self) -> str:
        return self.__linkType

    @linkType.setter
    def linkType(self, linkType: str):
        self.__linkType = linkType

    @property
    def WorkSequence7(self):
        return self.__WorkSequence7

    @WorkSequence7.setter
    def WorkSequence7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritpdl_WorkSequence__WorkSequence7", None)
        self.__WorkSequence7 = value
        
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
        old_value = getattr(self, f"_iritpdl_WorkSequence__linksToSuccessors", None)
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
        old_value = getattr(self, f"_iritpdl_WorkSequence__WorkSequence", None)
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
        old_value = getattr(self, f"_iritpdl_WorkSequence__linksToPredecessors", None)
        self.__linksToPredecessors = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorkDefinition12"):
                opp_val = getattr(old_value, "WorkDefinition12", None)
                if opp_val == self:
                    setattr(old_value, "WorkDefinition12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorkDefinition12"):
                opp_val = getattr(value, "WorkDefinition12", None)
                setattr(value, "WorkDefinition12", self)

class iritpdl_WorkDefinition(ProcessElement):

    def __init__(self, name: str, minTime: int, maxTime: int, successor: set["iritpdl_WorkSequence"] = None, WorkDefinition23: "iritpdl_ResourceConf" = None, predecessor: set["iritpdl_WorkSequence"] = None, workDefinition: set["iritpdl_ResourceConf"] = None, parent: set["iritpdl_ProcessElement"] = None, WorkDefinition: "iritpdl_WorkSequence" = None, WorkDefinition12: "iritpdl_WorkSequence" = None, WorkDefinition17: "iritpdl_ProcessElement" = None):
        self.name = name
        self.minTime = minTime
        self.maxTime = maxTime
        self.successor = successor if successor is not None else set()
        self.WorkDefinition23 = WorkDefinition23
        self.predecessor = predecessor if predecessor is not None else set()
        self.workDefinition = workDefinition if workDefinition is not None else set()
        self.parent = parent if parent is not None else set()
        self.WorkDefinition = WorkDefinition
        self.WorkDefinition12 = WorkDefinition12
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
    def workDefinition(self):
        return self.__workDefinition

    @workDefinition.setter
    def workDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritpdl_WorkDefinition__workDefinition", None)
        self.__workDefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ResourceConf"):
                    opp_val = getattr(item, "ResourceConf", None)
                    
                    if opp_val == self:
                        setattr(item, "ResourceConf", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ResourceConf"):
                    opp_val = getattr(item, "ResourceConf", None)
                    
                    setattr(item, "ResourceConf", self)
                    

    @property
    def predecessor(self):
        return self.__predecessor

    @predecessor.setter
    def predecessor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritpdl_WorkDefinition__predecessor", None)
        self.__predecessor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WorkSequence7"):
                    opp_val = getattr(item, "WorkSequence7", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkSequence7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkSequence7"):
                    opp_val = getattr(item, "WorkSequence7", None)
                    
                    setattr(item, "WorkSequence7", self)
                    

    @property
    def WorkDefinition17(self):
        return self.__WorkDefinition17

    @WorkDefinition17.setter
    def WorkDefinition17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritpdl_WorkDefinition__WorkDefinition17", None)
        self.__WorkDefinition17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children"):
                opp_val = getattr(old_value, "children", None)
                if opp_val == self:
                    setattr(old_value, "children", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children"):
                opp_val = getattr(value, "children", None)
                setattr(value, "children", self)

    @property
    def WorkDefinition23(self):
        return self.__WorkDefinition23

    @WorkDefinition23.setter
    def WorkDefinition23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritpdl_WorkDefinition__WorkDefinition23", None)
        self.__WorkDefinition23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourceConf"):
                opp_val = getattr(old_value, "resourceConf", None)
                if opp_val == self:
                    setattr(old_value, "resourceConf", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourceConf"):
                opp_val = getattr(value, "resourceConf", None)
                setattr(value, "resourceConf", self)

    @property
    def WorkDefinition12(self):
        return self.__WorkDefinition12

    @WorkDefinition12.setter
    def WorkDefinition12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritpdl_WorkDefinition__WorkDefinition12", None)
        self.__WorkDefinition12 = value
        
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
    def WorkDefinition(self):
        return self.__WorkDefinition

    @WorkDefinition.setter
    def WorkDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritpdl_WorkDefinition__WorkDefinition", None)
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
        old_value = getattr(self, f"_iritpdl_WorkDefinition__successor", None)
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
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritpdl_WorkDefinition__parent", None)
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
                    

class iritpdl_ResourceType:

    def __init__(self, name: str, occurrences: int, iritpdl_ResourceType: "iritpdl_Process" = None, iritpdl_ResourceType19: "iritpdl_Resource" = None):
        self.name = name
        self.occurrences = occurrences
        self.iritpdl_ResourceType = iritpdl_ResourceType
        self.iritpdl_ResourceType19 = iritpdl_ResourceType19
        
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
    def iritpdl_ResourceType19(self):
        return self.__iritpdl_ResourceType19

    @iritpdl_ResourceType19.setter
    def iritpdl_ResourceType19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritpdl_ResourceType__iritpdl_ResourceType19", None)
        self.__iritpdl_ResourceType19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iritpdl_Resource"):
                opp_val = getattr(old_value, "iritpdl_Resource", None)
                if opp_val == self:
                    setattr(old_value, "iritpdl_Resource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iritpdl_Resource"):
                opp_val = getattr(value, "iritpdl_Resource", None)
                setattr(value, "iritpdl_Resource", self)

    @property
    def iritpdl_ResourceType(self):
        return self.__iritpdl_ResourceType

    @iritpdl_ResourceType.setter
    def iritpdl_ResourceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritpdl_ResourceType__iritpdl_ResourceType", None)
        self.__iritpdl_ResourceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iritpdl_Process4"):
                opp_val = getattr(old_value, "iritpdl_Process4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iritpdl_Process4"):
                opp_val = getattr(value, "iritpdl_Process4", None)
                if opp_val is None:
                    setattr(value, "iritpdl_Process4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class iritpdl_Guidance:

    def __init__(self, text: str, iritpdl_Guidance: "iritpdl_Process" = None, iritpdl_Guidance15: "iritpdl_ProcessElement" = None):
        self.text = text
        self.iritpdl_Guidance = iritpdl_Guidance
        self.iritpdl_Guidance15 = iritpdl_Guidance15
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def iritpdl_Guidance(self):
        return self.__iritpdl_Guidance

    @iritpdl_Guidance.setter
    def iritpdl_Guidance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritpdl_Guidance__iritpdl_Guidance", None)
        self.__iritpdl_Guidance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iritpdl_Process2"):
                opp_val = getattr(old_value, "iritpdl_Process2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iritpdl_Process2"):
                opp_val = getattr(value, "iritpdl_Process2", None)
                if opp_val is None:
                    setattr(value, "iritpdl_Process2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iritpdl_Guidance15(self):
        return self.__iritpdl_Guidance15

    @iritpdl_Guidance15.setter
    def iritpdl_Guidance15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritpdl_Guidance__iritpdl_Guidance15", None)
        self.__iritpdl_Guidance15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iritpdl_ProcessElement14"):
                opp_val = getattr(old_value, "iritpdl_ProcessElement14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iritpdl_ProcessElement14"):
                opp_val = getattr(value, "iritpdl_ProcessElement14", None)
                if opp_val is None:
                    setattr(value, "iritpdl_ProcessElement14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class iritpdl_ProcessElement:

    pass