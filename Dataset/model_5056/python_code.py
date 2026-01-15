from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class FlowNodeStatusType(Enum):
    INACTIVE = "INACTIVE"
    READY = "READY"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    ABORTED = "ABORTED"


############################################
# Definition of Classes
############################################

class cbpmni_ConstraintInst:

    pass
class cbpmni_OCLConstraint:

    pass
class cbpmni_Branch:

    pass
class cbpmni_BranchInst:

    pass
class cbpmni_EObject:

    pass
class FlowNodeInst:

    pass
class cbpmni_SplitInst(FlowNodeInst):

    pass
class cbpmni_EventInst(FlowNodeInst):

    pass
class cbpmni_ActivityInst(FlowNodeInst):

    pass
class cbpmni_FlowNode:

    pass
class cbpmni_FlowNodeInst(ABC):

    def __init__(self, status: str, cbpmni_FlowNodeInst: "cbpmni_ProcessInst" = None, cbpmni_FlowNodeInst5: "cbpmni_ProcessInst" = None, cbpmni_FlowNodeInst7: "cbpmni_FlowNode" = None, cbpmni_FlowNodeInst10: "cbpmni_FlowNodeInst" = None, cbpmni_FlowNodeInst8: "cbpmni_FlowNodeInst" = None):
        self.status = status
        self.cbpmni_FlowNodeInst = cbpmni_FlowNodeInst
        self.cbpmni_FlowNodeInst5 = cbpmni_FlowNodeInst5
        self.cbpmni_FlowNodeInst7 = cbpmni_FlowNodeInst7
        self.cbpmni_FlowNodeInst10 = cbpmni_FlowNodeInst10
        self.cbpmni_FlowNodeInst8 = cbpmni_FlowNodeInst8
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def cbpmni_FlowNodeInst8(self):
        return self.__cbpmni_FlowNodeInst8

    @cbpmni_FlowNodeInst8.setter
    def cbpmni_FlowNodeInst8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmni_FlowNodeInst__cbpmni_FlowNodeInst8", None)
        self.__cbpmni_FlowNodeInst8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbpmni_FlowNodeInst10"):
                opp_val = getattr(old_value, "cbpmni_FlowNodeInst10", None)
                if opp_val == self:
                    setattr(old_value, "cbpmni_FlowNodeInst10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbpmni_FlowNodeInst10"):
                opp_val = getattr(value, "cbpmni_FlowNodeInst10", None)
                setattr(value, "cbpmni_FlowNodeInst10", self)

    @property
    def cbpmni_FlowNodeInst5(self):
        return self.__cbpmni_FlowNodeInst5

    @cbpmni_FlowNodeInst5.setter
    def cbpmni_FlowNodeInst5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmni_FlowNodeInst__cbpmni_FlowNodeInst5", None)
        self.__cbpmni_FlowNodeInst5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbpmni_ProcessInst4"):
                opp_val = getattr(old_value, "cbpmni_ProcessInst4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbpmni_ProcessInst4"):
                opp_val = getattr(value, "cbpmni_ProcessInst4", None)
                if opp_val is None:
                    setattr(value, "cbpmni_ProcessInst4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cbpmni_FlowNodeInst7(self):
        return self.__cbpmni_FlowNodeInst7

    @cbpmni_FlowNodeInst7.setter
    def cbpmni_FlowNodeInst7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmni_FlowNodeInst__cbpmni_FlowNodeInst7", None)
        self.__cbpmni_FlowNodeInst7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbpmni_FlowNode"):
                opp_val = getattr(old_value, "cbpmni_FlowNode", None)
                if opp_val == self:
                    setattr(old_value, "cbpmni_FlowNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbpmni_FlowNode"):
                opp_val = getattr(value, "cbpmni_FlowNode", None)
                setattr(value, "cbpmni_FlowNode", self)

    @property
    def cbpmni_FlowNodeInst(self):
        return self.__cbpmni_FlowNodeInst

    @cbpmni_FlowNodeInst.setter
    def cbpmni_FlowNodeInst(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmni_FlowNodeInst__cbpmni_FlowNodeInst", None)
        self.__cbpmni_FlowNodeInst = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbpmni_ProcessInst2"):
                opp_val = getattr(old_value, "cbpmni_ProcessInst2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbpmni_ProcessInst2"):
                opp_val = getattr(value, "cbpmni_ProcessInst2", None)
                if opp_val is None:
                    setattr(value, "cbpmni_ProcessInst2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cbpmni_FlowNodeInst10(self):
        return self.__cbpmni_FlowNodeInst10

    @cbpmni_FlowNodeInst10.setter
    def cbpmni_FlowNodeInst10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmni_FlowNodeInst__cbpmni_FlowNodeInst10", None)
        self.__cbpmni_FlowNodeInst10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbpmni_FlowNodeInst8"):
                opp_val = getattr(old_value, "cbpmni_FlowNodeInst8", None)
                if opp_val == self:
                    setattr(old_value, "cbpmni_FlowNodeInst8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbpmni_FlowNodeInst8"):
                opp_val = getattr(value, "cbpmni_FlowNodeInst8", None)
                setattr(value, "cbpmni_FlowNodeInst8", self)

    def EOperation0(self):
        # TODO: Implement EOperation0 method
        pass

class cbpmni_ProcessModel:

    pass
class cbpmni_ProcessInst:

    def __init__(self, cbpmni_ProcessInst: "cbpmni_ProcessModel" = None, cbpmni_ProcessInst2: set["cbpmni_FlowNodeInst"] = None, cbpmni_ProcessInst4: set["cbpmni_FlowNodeInst"] = None):
        self.cbpmni_ProcessInst = cbpmni_ProcessInst
        self.cbpmni_ProcessInst2 = cbpmni_ProcessInst2 if cbpmni_ProcessInst2 is not None else set()
        self.cbpmni_ProcessInst4 = cbpmni_ProcessInst4 if cbpmni_ProcessInst4 is not None else set()
        
    @property
    def cbpmni_ProcessInst2(self):
        return self.__cbpmni_ProcessInst2

    @cbpmni_ProcessInst2.setter
    def cbpmni_ProcessInst2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmni_ProcessInst__cbpmni_ProcessInst2", None)
        self.__cbpmni_ProcessInst2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cbpmni_FlowNodeInst"):
                    opp_val = getattr(item, "cbpmni_FlowNodeInst", None)
                    
                    if opp_val == self:
                        setattr(item, "cbpmni_FlowNodeInst", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cbpmni_FlowNodeInst"):
                    opp_val = getattr(item, "cbpmni_FlowNodeInst", None)
                    
                    setattr(item, "cbpmni_FlowNodeInst", self)
                    

    @property
    def cbpmni_ProcessInst(self):
        return self.__cbpmni_ProcessInst

    @cbpmni_ProcessInst.setter
    def cbpmni_ProcessInst(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmni_ProcessInst__cbpmni_ProcessInst", None)
        self.__cbpmni_ProcessInst = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cbpmni_ProcessModel"):
                opp_val = getattr(old_value, "cbpmni_ProcessModel", None)
                if opp_val == self:
                    setattr(old_value, "cbpmni_ProcessModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cbpmni_ProcessModel"):
                opp_val = getattr(value, "cbpmni_ProcessModel", None)
                setattr(value, "cbpmni_ProcessModel", self)

    @property
    def cbpmni_ProcessInst4(self):
        return self.__cbpmni_ProcessInst4

    @cbpmni_ProcessInst4.setter
    def cbpmni_ProcessInst4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cbpmni_ProcessInst__cbpmni_ProcessInst4", None)
        self.__cbpmni_ProcessInst4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cbpmni_FlowNodeInst5"):
                    opp_val = getattr(item, "cbpmni_FlowNodeInst5", None)
                    
                    if opp_val == self:
                        setattr(item, "cbpmni_FlowNodeInst5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cbpmni_FlowNodeInst5"):
                    opp_val = getattr(item, "cbpmni_FlowNodeInst5", None)
                    
                    setattr(item, "cbpmni_FlowNodeInst5", self)
                    

    def setupProcessInstance(self):
        # TODO: Implement setupProcessInstance method
        pass
