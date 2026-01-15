from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class GatewayType(Enum):
    SPLIT = "SPLIT"
    JOIN = "JOIN"
class ActivityType(Enum):
    MANUAL = "MANUAL"
    RECEIVE = "RECEIVE"
    SEND = "SEND"
    SERVICE = "SERVICE"
    USER = "USER"
    BUSINESSRULE = "BUSINESSRULE"
class DataObjectType(Enum):
    PHYSICAL = "PHYSICAL"
    INFORMATIONAL = "INFORMATIONAL"
class FlowNodeInstanceStatus(Enum):
    INIT = "INIT"
    STARTED = "STARTED"
    INTERRUPTED = "INTERRUPTED"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
class DecisionType(Enum):
    EXCLUSIVE = "EXCLUSIVE"
    INCLUSIVE = "INCLUSIVE"
class EventType(Enum):
    EEnumLiteral0 = "EEnumLiteral0"


############################################
# Definition of Classes
############################################

class Event:

    pass
class cbpmn_IntermediateEvent(Event):

    pass
class cbpmn_EndEvent(Event):

    pass
class cbpmn_StartEvent(Event):

    pass
class EObject:

    pass
class cbpmn_DataObject(EObject):

    pass
class cbpmn_EObject:

    pass
class cbpmn_FlowNodeInstance:

    def __init__(self, status: str, FlowNodeInstance: "cbpmn_ProcessInstance" = None, cbpmn_FlowNodeInstance: "cbpmn_FlowNode" = None, cbpmn_FlowNodeInstance42: set["cbpmn_EObject"] = None, cbpmn_FlowNodeInstance45: set["cbpmn_EObject"] = None, executedNodes: "cbpmn_ProcessInstance" = None):
        self.status = status
        self.FlowNodeInstance = FlowNodeInstance
        self.cbpmn_FlowNodeInstance = cbpmn_FlowNodeInstance
        self.cbpmn_FlowNodeInstance42 = cbpmn_FlowNodeInstance42 if cbpmn_FlowNodeInstance42 is not None else set()
        self.cbpmn_FlowNodeInstance45 = cbpmn_FlowNodeInstance45 if cbpmn_FlowNodeInstance45 is not None else set()
        self.executedNodes = executedNodes
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def cbpmn_FlowNodeInstance42(self):
        return self.__cbpmn_FlowNodeInstance42

    @cbpmn_FlowNodeInstance42.setter
    def cbpmn_FlowNodeInstance42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_FlowNodeInstance__cbpmn_FlowNodeInstance42", None)
        self.__cbpmn_FlowNodeInstance42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cbpmn_EObject43"):
                    opp_val = getattr(item, "cbpmn_EObject43", None)
                    
                    if opp_val == self:
                        setattr(item, "cbpmn_EObject43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cbpmn_EObject43"):
                    opp_val = getattr(item, "cbpmn_EObject43", None)
                    
                    setattr(item, "cbpmn_EObject43", self)
                    

    @property
    def cbpmn_FlowNodeInstance(self):
        return self.__cbpmn_FlowNodeInstance

    @cbpmn_FlowNodeInstance.setter
    def cbpmn_FlowNodeInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_FlowNodeInstance__cbpmn_FlowNodeInstance", None)
        self.__cbpmn_FlowNodeInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbpmn_FlowNode40"):
                opp_val = getattr(old_value, "cbpmn_FlowNode40", None)
                if opp_val == self:
                    setattr(old_value, "cbpmn_FlowNode40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbpmn_FlowNode40"):
                opp_val = getattr(value, "cbpmn_FlowNode40", None)
                setattr(value, "cbpmn_FlowNode40", self)

    @property
    def executedNodes(self):
        return self.__executedNodes

    @executedNodes.setter
    def executedNodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_FlowNodeInstance__executedNodes", None)
        self.__executedNodes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProcessInstance"):
                opp_val = getattr(old_value, "ProcessInstance", None)
                if opp_val == self:
                    setattr(old_value, "ProcessInstance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessInstance"):
                opp_val = getattr(value, "ProcessInstance", None)
                setattr(value, "ProcessInstance", self)

    @property
    def FlowNodeInstance(self):
        return self.__FlowNodeInstance

    @FlowNodeInstance.setter
    def FlowNodeInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_FlowNodeInstance__FlowNodeInstance", None)
        self.__FlowNodeInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "processInstance"):
                opp_val = getattr(old_value, "processInstance", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "processInstance"):
                opp_val = getattr(value, "processInstance", None)
                if opp_val is None:
                    setattr(value, "processInstance", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cbpmn_FlowNodeInstance45(self):
        return self.__cbpmn_FlowNodeInstance45

    @cbpmn_FlowNodeInstance45.setter
    def cbpmn_FlowNodeInstance45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_FlowNodeInstance__cbpmn_FlowNodeInstance45", None)
        self.__cbpmn_FlowNodeInstance45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cbpmn_EObject46"):
                    opp_val = getattr(item, "cbpmn_EObject46", None)
                    
                    if opp_val == self:
                        setattr(item, "cbpmn_EObject46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cbpmn_EObject46"):
                    opp_val = getattr(item, "cbpmn_EObject46", None)
                    
                    setattr(item, "cbpmn_EObject46", self)
                    

class cbpmn_ProcessInstance:

    def __init__(self, id: str, cbpmn_ProcessInstance: "cbpmn_ProcessModel" = None, processInstance: set["cbpmn_FlowNodeInstance"] = None, cbpmn_ProcessInstance38: set["cbpmn_EObject"] = None, ProcessInstance: "cbpmn_FlowNodeInstance" = None):
        self.id = id
        self.cbpmn_ProcessInstance = cbpmn_ProcessInstance
        self.processInstance = processInstance if processInstance is not None else set()
        self.cbpmn_ProcessInstance38 = cbpmn_ProcessInstance38 if cbpmn_ProcessInstance38 is not None else set()
        self.ProcessInstance = ProcessInstance
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def ProcessInstance(self):
        return self.__ProcessInstance

    @ProcessInstance.setter
    def ProcessInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_ProcessInstance__ProcessInstance", None)
        self.__ProcessInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executedNodes"):
                opp_val = getattr(old_value, "executedNodes", None)
                if opp_val == self:
                    setattr(old_value, "executedNodes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executedNodes"):
                opp_val = getattr(value, "executedNodes", None)
                setattr(value, "executedNodes", self)

    @property
    def cbpmn_ProcessInstance(self):
        return self.__cbpmn_ProcessInstance

    @cbpmn_ProcessInstance.setter
    def cbpmn_ProcessInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_ProcessInstance__cbpmn_ProcessInstance", None)
        self.__cbpmn_ProcessInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbpmn_ProcessModel35"):
                opp_val = getattr(old_value, "cbpmn_ProcessModel35", None)
                if opp_val == self:
                    setattr(old_value, "cbpmn_ProcessModel35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbpmn_ProcessModel35"):
                opp_val = getattr(value, "cbpmn_ProcessModel35", None)
                setattr(value, "cbpmn_ProcessModel35", self)

    @property
    def processInstance(self):
        return self.__processInstance

    @processInstance.setter
    def processInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_ProcessInstance__processInstance", None)
        self.__processInstance = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FlowNodeInstance"):
                    opp_val = getattr(item, "FlowNodeInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "FlowNodeInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FlowNodeInstance"):
                    opp_val = getattr(item, "FlowNodeInstance", None)
                    
                    setattr(item, "FlowNodeInstance", self)
                    

    @property
    def cbpmn_ProcessInstance38(self):
        return self.__cbpmn_ProcessInstance38

    @cbpmn_ProcessInstance38.setter
    def cbpmn_ProcessInstance38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_ProcessInstance__cbpmn_ProcessInstance38", None)
        self.__cbpmn_ProcessInstance38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cbpmn_EObject"):
                    opp_val = getattr(item, "cbpmn_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "cbpmn_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cbpmn_EObject"):
                    opp_val = getattr(item, "cbpmn_EObject", None)
                    
                    setattr(item, "cbpmn_EObject", self)
                    

class cbpmn_EClass:

    pass
class SplitGateway:

    pass
class cbpmn_ParallelGateway(SplitGateway):

    pass
class cbpmn_DecisionGateway(SplitGateway):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    def getDefaultBranch(self) -> str:
        # TODO: Implement getDefaultBranch method
        pass

    def addBranchWithCondition(self, default: bool, condition: str, branch: str):
        # TODO: Implement addBranchWithCondition method
        pass

    def getRandomBranch(self) -> str:
        # TODO: Implement getRandomBranch method
        pass

class cbpmn_FlowNode(ABC):

    def __init__(self, name: str, FlowNode: "cbpmn_Branch" = None, nodes: "cbpmn_Branch" = None, FlowNode20: "cbpmn_FlowNode" = None, previous: "cbpmn_FlowNode" = None, FlowNode23: "cbpmn_FlowNode" = None, next: "cbpmn_FlowNode" = None, cbpmn_FlowNode: set["cbpmn_DataObjectReference"] = None, cbpmn_FlowNode40: "cbpmn_FlowNodeInstance" = None):
        self.name = name
        self.FlowNode = FlowNode
        self.nodes = nodes
        self.FlowNode20 = FlowNode20
        self.previous = previous
        self.FlowNode23 = FlowNode23
        self.next = next
        self.cbpmn_FlowNode = cbpmn_FlowNode if cbpmn_FlowNode is not None else set()
        self.cbpmn_FlowNode40 = cbpmn_FlowNode40
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_FlowNode__nodes", None)
        self.__nodes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Branch"):
                opp_val = getattr(old_value, "Branch", None)
                if opp_val == self:
                    setattr(old_value, "Branch", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Branch"):
                opp_val = getattr(value, "Branch", None)
                setattr(value, "Branch", self)

    @property
    def FlowNode20(self):
        return self.__FlowNode20

    @FlowNode20.setter
    def FlowNode20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_FlowNode__FlowNode20", None)
        self.__FlowNode20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "previous"):
                opp_val = getattr(old_value, "previous", None)
                if opp_val == self:
                    setattr(old_value, "previous", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "previous"):
                opp_val = getattr(value, "previous", None)
                setattr(value, "previous", self)

    @property
    def FlowNode(self):
        return self.__FlowNode

    @FlowNode.setter
    def FlowNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_FlowNode__FlowNode", None)
        self.__FlowNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "branch"):
                opp_val = getattr(old_value, "branch", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "branch"):
                opp_val = getattr(value, "branch", None)
                if opp_val is None:
                    setattr(value, "branch", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cbpmn_FlowNode(self):
        return self.__cbpmn_FlowNode

    @cbpmn_FlowNode.setter
    def cbpmn_FlowNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_FlowNode__cbpmn_FlowNode", None)
        self.__cbpmn_FlowNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cbpmn_DataObjectReference25"):
                    opp_val = getattr(item, "cbpmn_DataObjectReference25", None)
                    
                    if opp_val == self:
                        setattr(item, "cbpmn_DataObjectReference25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cbpmn_DataObjectReference25"):
                    opp_val = getattr(item, "cbpmn_DataObjectReference25", None)
                    
                    setattr(item, "cbpmn_DataObjectReference25", self)
                    

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_FlowNode__next", None)
        self.__next = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FlowNode23"):
                opp_val = getattr(old_value, "FlowNode23", None)
                if opp_val == self:
                    setattr(old_value, "FlowNode23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FlowNode23"):
                opp_val = getattr(value, "FlowNode23", None)
                setattr(value, "FlowNode23", self)

    @property
    def previous(self):
        return self.__previous

    @previous.setter
    def previous(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_FlowNode__previous", None)
        self.__previous = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FlowNode20"):
                opp_val = getattr(old_value, "FlowNode20", None)
                if opp_val == self:
                    setattr(old_value, "FlowNode20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FlowNode20"):
                opp_val = getattr(value, "FlowNode20", None)
                setattr(value, "FlowNode20", self)

    @property
    def FlowNode23(self):
        return self.__FlowNode23

    @FlowNode23.setter
    def FlowNode23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_FlowNode__FlowNode23", None)
        self.__FlowNode23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "next"):
                opp_val = getattr(old_value, "next", None)
                if opp_val == self:
                    setattr(old_value, "next", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "next"):
                opp_val = getattr(value, "next", None)
                setattr(value, "next", self)

    @property
    def cbpmn_FlowNode40(self):
        return self.__cbpmn_FlowNode40

    @cbpmn_FlowNode40.setter
    def cbpmn_FlowNode40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_FlowNode__cbpmn_FlowNode40", None)
        self.__cbpmn_FlowNode40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbpmn_FlowNodeInstance"):
                opp_val = getattr(old_value, "cbpmn_FlowNodeInstance", None)
                if opp_val == self:
                    setattr(old_value, "cbpmn_FlowNodeInstance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbpmn_FlowNodeInstance"):
                opp_val = getattr(value, "cbpmn_FlowNodeInstance", None)
                setattr(value, "cbpmn_FlowNodeInstance", self)

class cbpmn_DataObjectReference:

    def __init__(self, name: str, lowerBound: int, higherBound: int, cbpmn_DataObjectReference: "cbpmn_Activity" = None, cbpmn_DataObjectReference25: "cbpmn_FlowNode" = None, cbpmn_DataObjectReference33: "cbpmn_EClass" = None):
        self.name = name
        self.lowerBound = lowerBound
        self.higherBound = higherBound
        self.cbpmn_DataObjectReference = cbpmn_DataObjectReference
        self.cbpmn_DataObjectReference25 = cbpmn_DataObjectReference25
        self.cbpmn_DataObjectReference33 = cbpmn_DataObjectReference33
        
    @property
    def higherBound(self) -> int:
        return self.__higherBound

    @higherBound.setter
    def higherBound(self, higherBound: int):
        self.__higherBound = higherBound

    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cbpmn_DataObjectReference33(self):
        return self.__cbpmn_DataObjectReference33

    @cbpmn_DataObjectReference33.setter
    def cbpmn_DataObjectReference33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_DataObjectReference__cbpmn_DataObjectReference33", None)
        self.__cbpmn_DataObjectReference33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbpmn_EClass"):
                opp_val = getattr(old_value, "cbpmn_EClass", None)
                if opp_val == self:
                    setattr(old_value, "cbpmn_EClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbpmn_EClass"):
                opp_val = getattr(value, "cbpmn_EClass", None)
                setattr(value, "cbpmn_EClass", self)

    @property
    def cbpmn_DataObjectReference(self):
        return self.__cbpmn_DataObjectReference

    @cbpmn_DataObjectReference.setter
    def cbpmn_DataObjectReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_DataObjectReference__cbpmn_DataObjectReference", None)
        self.__cbpmn_DataObjectReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbpmn_Activity9"):
                opp_val = getattr(old_value, "cbpmn_Activity9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbpmn_Activity9"):
                opp_val = getattr(value, "cbpmn_Activity9", None)
                if opp_val is None:
                    setattr(value, "cbpmn_Activity9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cbpmn_DataObjectReference25(self):
        return self.__cbpmn_DataObjectReference25

    @cbpmn_DataObjectReference25.setter
    def cbpmn_DataObjectReference25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_DataObjectReference__cbpmn_DataObjectReference25", None)
        self.__cbpmn_DataObjectReference25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbpmn_FlowNode"):
                opp_val = getattr(old_value, "cbpmn_FlowNode", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbpmn_FlowNode"):
                opp_val = getattr(value, "cbpmn_FlowNode", None)
                if opp_val is None:
                    setattr(value, "cbpmn_FlowNode", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class FlowNode:

    pass
class cbpmn_Event(FlowNode):

    pass
class cbpmn_SplitGateway(FlowNode):

    pass
class cbpmn_Activity(FlowNode):

    def __init__(self, type: str, cbpmn_Activity: set["cbpmn_OCLConstraint"] = None, cbpmn_Activity6: set["cbpmn_OCLConstraint"] = None, cbpmn_Activity9: set["cbpmn_DataObjectReference"] = None, cbpmn_Activity11: set["cbpmn_OCLConstraint"] = None):
        self.type = type
        self.cbpmn_Activity = cbpmn_Activity if cbpmn_Activity is not None else set()
        self.cbpmn_Activity6 = cbpmn_Activity6 if cbpmn_Activity6 is not None else set()
        self.cbpmn_Activity9 = cbpmn_Activity9 if cbpmn_Activity9 is not None else set()
        self.cbpmn_Activity11 = cbpmn_Activity11 if cbpmn_Activity11 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def cbpmn_Activity9(self):
        return self.__cbpmn_Activity9

    @cbpmn_Activity9.setter
    def cbpmn_Activity9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_Activity__cbpmn_Activity9", None)
        self.__cbpmn_Activity9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cbpmn_DataObjectReference"):
                    opp_val = getattr(item, "cbpmn_DataObjectReference", None)
                    
                    if opp_val == self:
                        setattr(item, "cbpmn_DataObjectReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cbpmn_DataObjectReference"):
                    opp_val = getattr(item, "cbpmn_DataObjectReference", None)
                    
                    setattr(item, "cbpmn_DataObjectReference", self)
                    

    @property
    def cbpmn_Activity11(self):
        return self.__cbpmn_Activity11

    @cbpmn_Activity11.setter
    def cbpmn_Activity11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_Activity__cbpmn_Activity11", None)
        self.__cbpmn_Activity11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cbpmn_OCLConstraint12"):
                    opp_val = getattr(item, "cbpmn_OCLConstraint12", None)
                    
                    if opp_val == self:
                        setattr(item, "cbpmn_OCLConstraint12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cbpmn_OCLConstraint12"):
                    opp_val = getattr(item, "cbpmn_OCLConstraint12", None)
                    
                    setattr(item, "cbpmn_OCLConstraint12", self)
                    

    @property
    def cbpmn_Activity(self):
        return self.__cbpmn_Activity

    @cbpmn_Activity.setter
    def cbpmn_Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_Activity__cbpmn_Activity", None)
        self.__cbpmn_Activity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cbpmn_OCLConstraint4"):
                    opp_val = getattr(item, "cbpmn_OCLConstraint4", None)
                    
                    if opp_val == self:
                        setattr(item, "cbpmn_OCLConstraint4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cbpmn_OCLConstraint4"):
                    opp_val = getattr(item, "cbpmn_OCLConstraint4", None)
                    
                    setattr(item, "cbpmn_OCLConstraint4", self)
                    

    @property
    def cbpmn_Activity6(self):
        return self.__cbpmn_Activity6

    @cbpmn_Activity6.setter
    def cbpmn_Activity6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_Activity__cbpmn_Activity6", None)
        self.__cbpmn_Activity6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cbpmn_OCLConstraint7"):
                    opp_val = getattr(item, "cbpmn_OCLConstraint7", None)
                    
                    if opp_val == self:
                        setattr(item, "cbpmn_OCLConstraint7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cbpmn_OCLConstraint7"):
                    opp_val = getattr(item, "cbpmn_OCLConstraint7", None)
                    
                    setattr(item, "cbpmn_OCLConstraint7", self)
                    

class cbpmn_OCLConstraint:

    def __init__(self, constraintName: str, constraintStr: str, cbpmn_OCLConstraint: "cbpmn_ProcessModel" = None, cbpmn_OCLConstraint4: "cbpmn_Activity" = None, cbpmn_OCLConstraint7: "cbpmn_Activity" = None, cbpmn_OCLConstraint12: "cbpmn_Activity" = None, entryConditions: "cbpmn_Branch" = None, cbpmn_OCLConstraint29: "cbpmn_Event" = None, OCLConstraint: "cbpmn_Branch" = None):
        self.constraintName = constraintName
        self.constraintStr = constraintStr
        self.cbpmn_OCLConstraint = cbpmn_OCLConstraint
        self.cbpmn_OCLConstraint4 = cbpmn_OCLConstraint4
        self.cbpmn_OCLConstraint7 = cbpmn_OCLConstraint7
        self.cbpmn_OCLConstraint12 = cbpmn_OCLConstraint12
        self.entryConditions = entryConditions
        self.cbpmn_OCLConstraint29 = cbpmn_OCLConstraint29
        self.OCLConstraint = OCLConstraint
        
    @property
    def constraintStr(self) -> str:
        return self.__constraintStr

    @constraintStr.setter
    def constraintStr(self, constraintStr: str):
        self.__constraintStr = constraintStr

    @property
    def constraintName(self) -> str:
        return self.__constraintName

    @constraintName.setter
    def constraintName(self, constraintName: str):
        self.__constraintName = constraintName

    @property
    def OCLConstraint(self):
        return self.__OCLConstraint

    @OCLConstraint.setter
    def OCLConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_OCLConstraint__OCLConstraint", None)
        self.__OCLConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "branch15"):
                opp_val = getattr(old_value, "branch15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "branch15"):
                opp_val = getattr(value, "branch15", None)
                if opp_val is None:
                    setattr(value, "branch15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cbpmn_OCLConstraint12(self):
        return self.__cbpmn_OCLConstraint12

    @cbpmn_OCLConstraint12.setter
    def cbpmn_OCLConstraint12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_OCLConstraint__cbpmn_OCLConstraint12", None)
        self.__cbpmn_OCLConstraint12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbpmn_Activity11"):
                opp_val = getattr(old_value, "cbpmn_Activity11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbpmn_Activity11"):
                opp_val = getattr(value, "cbpmn_Activity11", None)
                if opp_val is None:
                    setattr(value, "cbpmn_Activity11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cbpmn_OCLConstraint7(self):
        return self.__cbpmn_OCLConstraint7

    @cbpmn_OCLConstraint7.setter
    def cbpmn_OCLConstraint7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_OCLConstraint__cbpmn_OCLConstraint7", None)
        self.__cbpmn_OCLConstraint7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbpmn_Activity6"):
                opp_val = getattr(old_value, "cbpmn_Activity6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbpmn_Activity6"):
                opp_val = getattr(value, "cbpmn_Activity6", None)
                if opp_val is None:
                    setattr(value, "cbpmn_Activity6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cbpmn_OCLConstraint29(self):
        return self.__cbpmn_OCLConstraint29

    @cbpmn_OCLConstraint29.setter
    def cbpmn_OCLConstraint29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_OCLConstraint__cbpmn_OCLConstraint29", None)
        self.__cbpmn_OCLConstraint29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbpmn_Event"):
                opp_val = getattr(old_value, "cbpmn_Event", None)
                if opp_val == self:
                    setattr(old_value, "cbpmn_Event", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbpmn_Event"):
                opp_val = getattr(value, "cbpmn_Event", None)
                setattr(value, "cbpmn_Event", self)

    @property
    def entryConditions(self):
        return self.__entryConditions

    @entryConditions.setter
    def entryConditions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_OCLConstraint__entryConditions", None)
        self.__entryConditions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Branch27"):
                opp_val = getattr(old_value, "Branch27", None)
                if opp_val == self:
                    setattr(old_value, "Branch27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Branch27"):
                opp_val = getattr(value, "Branch27", None)
                setattr(value, "Branch27", self)

    @property
    def cbpmn_OCLConstraint(self):
        return self.__cbpmn_OCLConstraint

    @cbpmn_OCLConstraint.setter
    def cbpmn_OCLConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_OCLConstraint__cbpmn_OCLConstraint", None)
        self.__cbpmn_OCLConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbpmn_ProcessModel2"):
                opp_val = getattr(old_value, "cbpmn_ProcessModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbpmn_ProcessModel2"):
                opp_val = getattr(value, "cbpmn_ProcessModel2", None)
                if opp_val is None:
                    setattr(value, "cbpmn_ProcessModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cbpmn_OCLConstraint4(self):
        return self.__cbpmn_OCLConstraint4

    @cbpmn_OCLConstraint4.setter
    def cbpmn_OCLConstraint4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_OCLConstraint__cbpmn_OCLConstraint4", None)
        self.__cbpmn_OCLConstraint4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbpmn_Activity"):
                opp_val = getattr(old_value, "cbpmn_Activity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbpmn_Activity"):
                opp_val = getattr(value, "cbpmn_Activity", None)
                if opp_val is None:
                    setattr(value, "cbpmn_Activity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cbpmn_Branch:

    def __init__(self, default: bool, cbpmn_Branch: "cbpmn_ProcessModel" = None, branch: set["cbpmn_FlowNode"] = None, Branch: "cbpmn_FlowNode" = None, Branch27: "cbpmn_OCLConstraint" = None, branch15: set["cbpmn_OCLConstraint"] = None, branches: "cbpmn_SplitGateway" = None, Branch31: "cbpmn_SplitGateway" = None):
        self.default = default
        self.cbpmn_Branch = cbpmn_Branch
        self.branch = branch if branch is not None else set()
        self.Branch = Branch
        self.Branch27 = Branch27
        self.branch15 = branch15 if branch15 is not None else set()
        self.branches = branches
        self.Branch31 = Branch31
        
    @property
    def default(self) -> bool:
        return self.__default

    @default.setter
    def default(self, default: bool):
        self.__default = default

    @property
    def branches(self):
        return self.__branches

    @branches.setter
    def branches(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_Branch__branches", None)
        self.__branches = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SplitGateway"):
                opp_val = getattr(old_value, "SplitGateway", None)
                if opp_val == self:
                    setattr(old_value, "SplitGateway", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SplitGateway"):
                opp_val = getattr(value, "SplitGateway", None)
                setattr(value, "SplitGateway", self)

    @property
    def Branch31(self):
        return self.__Branch31

    @Branch31.setter
    def Branch31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_Branch__Branch31", None)
        self.__Branch31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gateway"):
                opp_val = getattr(old_value, "gateway", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gateway"):
                opp_val = getattr(value, "gateway", None)
                if opp_val is None:
                    setattr(value, "gateway", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Branch27(self):
        return self.__Branch27

    @Branch27.setter
    def Branch27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_Branch__Branch27", None)
        self.__Branch27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entryConditions"):
                opp_val = getattr(old_value, "entryConditions", None)
                if opp_val == self:
                    setattr(old_value, "entryConditions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entryConditions"):
                opp_val = getattr(value, "entryConditions", None)
                setattr(value, "entryConditions", self)

    @property
    def cbpmn_Branch(self):
        return self.__cbpmn_Branch

    @cbpmn_Branch.setter
    def cbpmn_Branch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_Branch__cbpmn_Branch", None)
        self.__cbpmn_Branch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbpmn_ProcessModel"):
                opp_val = getattr(old_value, "cbpmn_ProcessModel", None)
                if opp_val == self:
                    setattr(old_value, "cbpmn_ProcessModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbpmn_ProcessModel"):
                opp_val = getattr(value, "cbpmn_ProcessModel", None)
                setattr(value, "cbpmn_ProcessModel", self)

    @property
    def Branch(self):
        return self.__Branch

    @Branch.setter
    def Branch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_Branch__Branch", None)
        self.__Branch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nodes"):
                opp_val = getattr(old_value, "nodes", None)
                if opp_val == self:
                    setattr(old_value, "nodes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nodes"):
                opp_val = getattr(value, "nodes", None)
                setattr(value, "nodes", self)

    @property
    def branch15(self):
        return self.__branch15

    @branch15.setter
    def branch15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_Branch__branch15", None)
        self.__branch15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OCLConstraint"):
                    opp_val = getattr(item, "OCLConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "OCLConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OCLConstraint"):
                    opp_val = getattr(item, "OCLConstraint", None)
                    
                    setattr(item, "OCLConstraint", self)
                    

    @property
    def branch(self):
        return self.__branch

    @branch.setter
    def branch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_Branch__branch", None)
        self.__branch = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FlowNode"):
                    opp_val = getattr(item, "FlowNode", None)
                    
                    if opp_val == self:
                        setattr(item, "FlowNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FlowNode"):
                    opp_val = getattr(item, "FlowNode", None)
                    
                    setattr(item, "FlowNode", self)
                    

    def getFirstNode(self) -> FlowNode:
        # TODO: Implement getFirstNode method
        pass

    def getLastNode(self) -> FlowNode:
        # TODO: Implement getLastNode method
        pass

class cbpmn_ProcessModel:

    def __init__(self, name: str, cbpmn_ProcessModel: "cbpmn_Branch" = None, cbpmn_ProcessModel2: set["cbpmn_OCLConstraint"] = None, cbpmn_ProcessModel35: "cbpmn_ProcessInstance" = None):
        self.name = name
        self.cbpmn_ProcessModel = cbpmn_ProcessModel
        self.cbpmn_ProcessModel2 = cbpmn_ProcessModel2 if cbpmn_ProcessModel2 is not None else set()
        self.cbpmn_ProcessModel35 = cbpmn_ProcessModel35
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cbpmn_ProcessModel35(self):
        return self.__cbpmn_ProcessModel35

    @cbpmn_ProcessModel35.setter
    def cbpmn_ProcessModel35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_ProcessModel__cbpmn_ProcessModel35", None)
        self.__cbpmn_ProcessModel35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbpmn_ProcessInstance"):
                opp_val = getattr(old_value, "cbpmn_ProcessInstance", None)
                if opp_val == self:
                    setattr(old_value, "cbpmn_ProcessInstance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbpmn_ProcessInstance"):
                opp_val = getattr(value, "cbpmn_ProcessInstance", None)
                setattr(value, "cbpmn_ProcessInstance", self)

    @property
    def cbpmn_ProcessModel(self):
        return self.__cbpmn_ProcessModel

    @cbpmn_ProcessModel.setter
    def cbpmn_ProcessModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_ProcessModel__cbpmn_ProcessModel", None)
        self.__cbpmn_ProcessModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbpmn_Branch"):
                opp_val = getattr(old_value, "cbpmn_Branch", None)
                if opp_val == self:
                    setattr(old_value, "cbpmn_Branch", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbpmn_Branch"):
                opp_val = getattr(value, "cbpmn_Branch", None)
                setattr(value, "cbpmn_Branch", self)

    @property
    def cbpmn_ProcessModel2(self):
        return self.__cbpmn_ProcessModel2

    @cbpmn_ProcessModel2.setter
    def cbpmn_ProcessModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_ProcessModel__cbpmn_ProcessModel2", None)
        self.__cbpmn_ProcessModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cbpmn_OCLConstraint"):
                    opp_val = getattr(item, "cbpmn_OCLConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "cbpmn_OCLConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cbpmn_OCLConstraint"):
                    opp_val = getattr(item, "cbpmn_OCLConstraint", None)
                    
                    setattr(item, "cbpmn_OCLConstraint", self)
                    

    def iterator(self, iterator: str) -> str:
        # TODO: Implement iterator method
        pass

    def getRandomStartEvent(self) -> str:
        # TODO: Implement getRandomStartEvent method
        pass

    def iterator(self, iterator: str, start: str) -> str:
        # TODO: Implement iterator method
        pass
