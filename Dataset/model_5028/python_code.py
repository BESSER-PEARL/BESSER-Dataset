from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DecisionType(Enum):
    EXCLUSIVE = "EXCLUSIVE"
    INCLUSIVE = "INCLUSIVE"
class EventType(Enum):
    EEnumLiteral0 = "EEnumLiteral0"
class GatewayType(Enum):
    JOIN = "JOIN"
    SPLIT = "SPLIT"
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


############################################
# Definition of Classes
############################################

class EObject:

    pass
class cbpmn_DataObject(EObject):

    pass
class cbpmn_EObject:

    pass
class cbpmn_FlowNodeInstance:

    def __init__(self, status: str, FlowNodeInstance: "cbpmn_ProcessInstance" = None, cbpmn_FlowNodeInstance: "cbpmn_FlowNode" = None, cbpmn_FlowNodeInstance44: set["cbpmn_EObject"] = None, cbpmn_FlowNodeInstance47: set["cbpmn_EObject"] = None, executedNodes: "cbpmn_ProcessInstance" = None):
        self.status = status
        self.FlowNodeInstance = FlowNodeInstance
        self.cbpmn_FlowNodeInstance = cbpmn_FlowNodeInstance
        self.cbpmn_FlowNodeInstance44 = cbpmn_FlowNodeInstance44 if cbpmn_FlowNodeInstance44 is not None else set()
        self.cbpmn_FlowNodeInstance47 = cbpmn_FlowNodeInstance47 if cbpmn_FlowNodeInstance47 is not None else set()
        self.executedNodes = executedNodes
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

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
    def cbpmn_FlowNodeInstance(self):
        return self.__cbpmn_FlowNodeInstance

    @cbpmn_FlowNodeInstance.setter
    def cbpmn_FlowNodeInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_FlowNodeInstance__cbpmn_FlowNodeInstance", None)
        self.__cbpmn_FlowNodeInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbpmn_FlowNode"):
                opp_val = getattr(old_value, "cbpmn_FlowNode", None)
                if opp_val == self:
                    setattr(old_value, "cbpmn_FlowNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbpmn_FlowNode"):
                opp_val = getattr(value, "cbpmn_FlowNode", None)
                setattr(value, "cbpmn_FlowNode", self)

    @property
    def cbpmn_FlowNodeInstance47(self):
        return self.__cbpmn_FlowNodeInstance47

    @cbpmn_FlowNodeInstance47.setter
    def cbpmn_FlowNodeInstance47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_FlowNodeInstance__cbpmn_FlowNodeInstance47", None)
        self.__cbpmn_FlowNodeInstance47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cbpmn_EObject48"):
                    opp_val = getattr(item, "cbpmn_EObject48", None)
                    
                    if opp_val == self:
                        setattr(item, "cbpmn_EObject48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cbpmn_EObject48"):
                    opp_val = getattr(item, "cbpmn_EObject48", None)
                    
                    setattr(item, "cbpmn_EObject48", self)
                    

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
    def cbpmn_FlowNodeInstance44(self):
        return self.__cbpmn_FlowNodeInstance44

    @cbpmn_FlowNodeInstance44.setter
    def cbpmn_FlowNodeInstance44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_FlowNodeInstance__cbpmn_FlowNodeInstance44", None)
        self.__cbpmn_FlowNodeInstance44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cbpmn_EObject45"):
                    opp_val = getattr(item, "cbpmn_EObject45", None)
                    
                    if opp_val == self:
                        setattr(item, "cbpmn_EObject45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cbpmn_EObject45"):
                    opp_val = getattr(item, "cbpmn_EObject45", None)
                    
                    setattr(item, "cbpmn_EObject45", self)
                    

class cbpmn_ProcessInstance:

    def __init__(self, id: str, cbpmn_ProcessInstance: "cbpmn_ProcessModel" = None, processInstance: set["cbpmn_FlowNodeInstance"] = None, cbpmn_ProcessInstance41: set["cbpmn_EObject"] = None, ProcessInstance: "cbpmn_FlowNodeInstance" = None):
        self.id = id
        self.cbpmn_ProcessInstance = cbpmn_ProcessInstance
        self.processInstance = processInstance if processInstance is not None else set()
        self.cbpmn_ProcessInstance41 = cbpmn_ProcessInstance41 if cbpmn_ProcessInstance41 is not None else set()
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
            if hasattr(old_value, "cbpmn_ProcessModel38"):
                opp_val = getattr(old_value, "cbpmn_ProcessModel38", None)
                if opp_val == self:
                    setattr(old_value, "cbpmn_ProcessModel38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbpmn_ProcessModel38"):
                opp_val = getattr(value, "cbpmn_ProcessModel38", None)
                setattr(value, "cbpmn_ProcessModel38", self)

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
    def cbpmn_ProcessInstance41(self):
        return self.__cbpmn_ProcessInstance41

    @cbpmn_ProcessInstance41.setter
    def cbpmn_ProcessInstance41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_ProcessInstance__cbpmn_ProcessInstance41", None)
        self.__cbpmn_ProcessInstance41 = value if value is not None else set()
        
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
class OCLConstraint:

    pass
class SplitGateway:

    pass
class cbpmn_ParallelGateway(SplitGateway):

    pass
class cbpmn_DecisionGateway(SplitGateway):

    def __init__(self, type: str, cbpmn_DecisionGateway: set["cbpmn_DecisionCondition"] = None):
        self.type = type
        self.cbpmn_DecisionGateway = cbpmn_DecisionGateway if cbpmn_DecisionGateway is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def cbpmn_DecisionGateway(self):
        return self.__cbpmn_DecisionGateway

    @cbpmn_DecisionGateway.setter
    def cbpmn_DecisionGateway(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_DecisionGateway__cbpmn_DecisionGateway", None)
        self.__cbpmn_DecisionGateway = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cbpmn_DecisionCondition20"):
                    opp_val = getattr(item, "cbpmn_DecisionCondition20", None)
                    
                    if opp_val == self:
                        setattr(item, "cbpmn_DecisionCondition20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cbpmn_DecisionCondition20"):
                    opp_val = getattr(item, "cbpmn_DecisionCondition20", None)
                    
                    setattr(item, "cbpmn_DecisionCondition20", self)
                    

    def addBranchWithCondition(self, condition: str, default: bool, branch: str):
        # TODO: Implement addBranchWithCondition method
        pass

class cbpmn_FlowNode(ABC):

    def __init__(self, name: str, FlowNode: "cbpmn_Branch" = None, nodes: "cbpmn_Branch" = None, FlowNode27: "cbpmn_FlowNode" = None, previous: "cbpmn_FlowNode" = None, FlowNode30: "cbpmn_FlowNode" = None, next: "cbpmn_FlowNode" = None, cbpmn_FlowNode: "cbpmn_FlowNodeInstance" = None):
        self.name = name
        self.FlowNode = FlowNode
        self.nodes = nodes
        self.FlowNode27 = FlowNode27
        self.previous = previous
        self.FlowNode30 = FlowNode30
        self.next = next
        self.cbpmn_FlowNode = cbpmn_FlowNode
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def FlowNode27(self):
        return self.__FlowNode27

    @FlowNode27.setter
    def FlowNode27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_FlowNode__FlowNode27", None)
        self.__FlowNode27 = value
        
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
    def FlowNode30(self):
        return self.__FlowNode30

    @FlowNode30.setter
    def FlowNode30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_FlowNode__FlowNode30", None)
        self.__FlowNode30 = value
        
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
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_FlowNode__next", None)
        self.__next = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FlowNode30"):
                opp_val = getattr(old_value, "FlowNode30", None)
                if opp_val == self:
                    setattr(old_value, "FlowNode30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FlowNode30"):
                opp_val = getattr(value, "FlowNode30", None)
                setattr(value, "FlowNode30", self)

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
    def cbpmn_FlowNode(self):
        return self.__cbpmn_FlowNode

    @cbpmn_FlowNode.setter
    def cbpmn_FlowNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_FlowNode__cbpmn_FlowNode", None)
        self.__cbpmn_FlowNode = value
        
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
            if hasattr(old_value, "FlowNode27"):
                opp_val = getattr(old_value, "FlowNode27", None)
                if opp_val == self:
                    setattr(old_value, "FlowNode27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FlowNode27"):
                opp_val = getattr(value, "FlowNode27", None)
                setattr(value, "FlowNode27", self)

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

class cbpmn_DecisionCondition(OCLConstraint):

    def __init__(self, isDefault: bool, cbpmn_DecisionCondition: "cbpmn_Branch" = None, cbpmn_DecisionCondition20: "cbpmn_DecisionGateway" = None, cbpmn_DecisionCondition22: "cbpmn_Branch" = None):
        self.isDefault = isDefault
        self.cbpmn_DecisionCondition = cbpmn_DecisionCondition
        self.cbpmn_DecisionCondition20 = cbpmn_DecisionCondition20
        self.cbpmn_DecisionCondition22 = cbpmn_DecisionCondition22
        
    @property
    def isDefault(self) -> bool:
        return self.__isDefault

    @isDefault.setter
    def isDefault(self, isDefault: bool):
        self.__isDefault = isDefault

    @property
    def cbpmn_DecisionCondition22(self):
        return self.__cbpmn_DecisionCondition22

    @cbpmn_DecisionCondition22.setter
    def cbpmn_DecisionCondition22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_DecisionCondition__cbpmn_DecisionCondition22", None)
        self.__cbpmn_DecisionCondition22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbpmn_Branch23"):
                opp_val = getattr(old_value, "cbpmn_Branch23", None)
                if opp_val == self:
                    setattr(old_value, "cbpmn_Branch23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbpmn_Branch23"):
                opp_val = getattr(value, "cbpmn_Branch23", None)
                setattr(value, "cbpmn_Branch23", self)

    @property
    def cbpmn_DecisionCondition(self):
        return self.__cbpmn_DecisionCondition

    @cbpmn_DecisionCondition.setter
    def cbpmn_DecisionCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_DecisionCondition__cbpmn_DecisionCondition", None)
        self.__cbpmn_DecisionCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbpmn_Branch17"):
                opp_val = getattr(old_value, "cbpmn_Branch17", None)
                if opp_val == self:
                    setattr(old_value, "cbpmn_Branch17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbpmn_Branch17"):
                opp_val = getattr(value, "cbpmn_Branch17", None)
                setattr(value, "cbpmn_Branch17", self)

    @property
    def cbpmn_DecisionCondition20(self):
        return self.__cbpmn_DecisionCondition20

    @cbpmn_DecisionCondition20.setter
    def cbpmn_DecisionCondition20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_DecisionCondition__cbpmn_DecisionCondition20", None)
        self.__cbpmn_DecisionCondition20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbpmn_DecisionGateway"):
                opp_val = getattr(old_value, "cbpmn_DecisionGateway", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbpmn_DecisionGateway"):
                opp_val = getattr(value, "cbpmn_DecisionGateway", None)
                if opp_val is None:
                    setattr(value, "cbpmn_DecisionGateway", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cbpmn_DataObjectReference:

    def __init__(self, name: str, lowerBound: int, higherBound: int, cbpmn_DataObjectReference: "cbpmn_Activity" = None, cbpmn_DataObjectReference12: "cbpmn_Activity" = None, cbpmn_DataObjectReference36: "cbpmn_EClass" = None):
        self.name = name
        self.lowerBound = lowerBound
        self.higherBound = higherBound
        self.cbpmn_DataObjectReference = cbpmn_DataObjectReference
        self.cbpmn_DataObjectReference12 = cbpmn_DataObjectReference12
        self.cbpmn_DataObjectReference36 = cbpmn_DataObjectReference36
        
    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def higherBound(self) -> int:
        return self.__higherBound

    @higherBound.setter
    def higherBound(self, higherBound: int):
        self.__higherBound = higherBound

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cbpmn_DataObjectReference36(self):
        return self.__cbpmn_DataObjectReference36

    @cbpmn_DataObjectReference36.setter
    def cbpmn_DataObjectReference36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_DataObjectReference__cbpmn_DataObjectReference36", None)
        self.__cbpmn_DataObjectReference36 = value
        
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
    def cbpmn_DataObjectReference12(self):
        return self.__cbpmn_DataObjectReference12

    @cbpmn_DataObjectReference12.setter
    def cbpmn_DataObjectReference12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_DataObjectReference__cbpmn_DataObjectReference12", None)
        self.__cbpmn_DataObjectReference12 = value
        
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

class FlowNode:

    pass
class cbpmn_Event(FlowNode):

    pass
class cbpmn_SplitGateway(FlowNode):

    pass
class cbpmn_Activity(FlowNode):

    def __init__(self, type: str, cbpmn_Activity: set["cbpmn_OCLConstraint"] = None, cbpmn_Activity6: set["cbpmn_OCLConstraint"] = None, cbpmn_Activity9: set["cbpmn_DataObjectReference"] = None, cbpmn_Activity11: set["cbpmn_DataObjectReference"] = None, cbpmn_Activity14: set["cbpmn_OCLConstraint"] = None):
        self.type = type
        self.cbpmn_Activity = cbpmn_Activity if cbpmn_Activity is not None else set()
        self.cbpmn_Activity6 = cbpmn_Activity6 if cbpmn_Activity6 is not None else set()
        self.cbpmn_Activity9 = cbpmn_Activity9 if cbpmn_Activity9 is not None else set()
        self.cbpmn_Activity11 = cbpmn_Activity11 if cbpmn_Activity11 is not None else set()
        self.cbpmn_Activity14 = cbpmn_Activity14 if cbpmn_Activity14 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def cbpmn_Activity14(self):
        return self.__cbpmn_Activity14

    @cbpmn_Activity14.setter
    def cbpmn_Activity14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_Activity__cbpmn_Activity14", None)
        self.__cbpmn_Activity14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cbpmn_OCLConstraint15"):
                    opp_val = getattr(item, "cbpmn_OCLConstraint15", None)
                    
                    if opp_val == self:
                        setattr(item, "cbpmn_OCLConstraint15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cbpmn_OCLConstraint15"):
                    opp_val = getattr(item, "cbpmn_OCLConstraint15", None)
                    
                    setattr(item, "cbpmn_OCLConstraint15", self)
                    

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
                if hasattr(item, "cbpmn_DataObjectReference12"):
                    opp_val = getattr(item, "cbpmn_DataObjectReference12", None)
                    
                    if opp_val == self:
                        setattr(item, "cbpmn_DataObjectReference12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cbpmn_DataObjectReference12"):
                    opp_val = getattr(item, "cbpmn_DataObjectReference12", None)
                    
                    setattr(item, "cbpmn_DataObjectReference12", self)
                    

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
                    

class cbpmn_OCLConstraint:

    def __init__(self, constraintName: str, constraintStr: str, cbpmn_OCLConstraint: "cbpmn_ProcessModel" = None, cbpmn_OCLConstraint4: "cbpmn_Activity" = None, cbpmn_OCLConstraint7: "cbpmn_Activity" = None, cbpmn_OCLConstraint15: "cbpmn_Activity" = None, cbpmn_OCLConstraint32: "cbpmn_Event" = None):
        self.constraintName = constraintName
        self.constraintStr = constraintStr
        self.cbpmn_OCLConstraint = cbpmn_OCLConstraint
        self.cbpmn_OCLConstraint4 = cbpmn_OCLConstraint4
        self.cbpmn_OCLConstraint7 = cbpmn_OCLConstraint7
        self.cbpmn_OCLConstraint15 = cbpmn_OCLConstraint15
        self.cbpmn_OCLConstraint32 = cbpmn_OCLConstraint32
        
    @property
    def constraintName(self) -> str:
        return self.__constraintName

    @constraintName.setter
    def constraintName(self, constraintName: str):
        self.__constraintName = constraintName

    @property
    def constraintStr(self) -> str:
        return self.__constraintStr

    @constraintStr.setter
    def constraintStr(self, constraintStr: str):
        self.__constraintStr = constraintStr

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

    @property
    def cbpmn_OCLConstraint32(self):
        return self.__cbpmn_OCLConstraint32

    @cbpmn_OCLConstraint32.setter
    def cbpmn_OCLConstraint32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_OCLConstraint__cbpmn_OCLConstraint32", None)
        self.__cbpmn_OCLConstraint32 = value
        
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
    def cbpmn_OCLConstraint15(self):
        return self.__cbpmn_OCLConstraint15

    @cbpmn_OCLConstraint15.setter
    def cbpmn_OCLConstraint15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_OCLConstraint__cbpmn_OCLConstraint15", None)
        self.__cbpmn_OCLConstraint15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbpmn_Activity14"):
                opp_val = getattr(old_value, "cbpmn_Activity14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbpmn_Activity14"):
                opp_val = getattr(value, "cbpmn_Activity14", None)
                if opp_val is None:
                    setattr(value, "cbpmn_Activity14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

class cbpmn_Branch:

    pass
class cbpmn_ProcessModel:

    def __init__(self, name: str, cbpmn_ProcessModel: "cbpmn_Branch" = None, cbpmn_ProcessModel2: set["cbpmn_OCLConstraint"] = None, cbpmn_ProcessModel38: "cbpmn_ProcessInstance" = None):
        self.name = name
        self.cbpmn_ProcessModel = cbpmn_ProcessModel
        self.cbpmn_ProcessModel2 = cbpmn_ProcessModel2 if cbpmn_ProcessModel2 is not None else set()
        self.cbpmn_ProcessModel38 = cbpmn_ProcessModel38
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def cbpmn_ProcessModel38(self):
        return self.__cbpmn_ProcessModel38

    @cbpmn_ProcessModel38.setter
    def cbpmn_ProcessModel38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmn_ProcessModel__cbpmn_ProcessModel38", None)
        self.__cbpmn_ProcessModel38 = value
        
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
