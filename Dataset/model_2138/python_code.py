from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Status(Enum):
    INACTIVE = "INACTIVE"
    ACTIVE = "ACTIVE"
    DONE = "DONE"
class Direction(Enum):
    IN = "IN"
    OUT = "OUT"
class ExpansionMode(Enum):
    PARALLEL = "PARALLEL"
    ITERATIVE = "ITERATIVE"


############################################
# Definition of Classes
############################################

class ObjectNode:

    pass
class UML_Activity_mine_ActivityParameterNode(ObjectNode):

    def __init__(self, parameter: str):
        self.parameter = parameter
        
    @property
    def parameter(self) -> str:
        return self.__parameter

    @parameter.setter
    def parameter(self, parameter: str):
        self.__parameter = parameter

class UML_Activity_mine_ExpansionNode(ObjectNode):

    pass
class UML_Activity_mine_DatastoreNode(ObjectNode):

    pass
class ControlNode:

    pass
class UML_Activity_mine_Join(ControlNode):

    pass
class UML_Activity_mine_ActivityInitialNode(ControlNode):

    pass
class UML_Activity_mine_ActivityFinalNode(ControlNode):

    pass
class UML_Activity_mine_Fork(ControlNode):

    pass
class ActivityNode:

    pass
class UML_Activity_mine_ObjectNode(ActivityNode):

    def __init__(self, objects: str, upperBound: str):
        self.objects = objects
        self.upperBound = upperBound
        
    @property
    def upperBound(self) -> str:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: str):
        self.__upperBound = upperBound

    @property
    def objects(self) -> str:
        return self.__objects

    @objects.setter
    def objects(self, objects: str):
        self.__objects = objects

class UML_Activity_mine_Action(ActivityNode):

    def __init__(self, inputs: str, outputs: str):
        self.inputs = inputs
        self.outputs = outputs
        
    @property
    def outputs(self) -> str:
        return self.__outputs

    @outputs.setter
    def outputs(self, outputs: str):
        self.__outputs = outputs

    @property
    def inputs(self) -> str:
        return self.__inputs

    @inputs.setter
    def inputs(self, inputs: str):
        self.__inputs = inputs

class UML_Activity_mine_ControlNode(ActivityNode):

    pass
class Action:

    pass
class UML_Activity_mine_ExpansionRegion(Action):

    pass
class Element:

    pass
class UML_Activity_mine_ActivityNode(Element):

    pass
class UML_Activity_mine_Activity(Element):

    pass
class UML_Activity_mine_Element(ABC):

    def __init__(self, name: str, elementID: str, properties: str):
        self.name = name
        self.elementID = elementID
        self.properties = properties
        
    @property
    def elementID(self) -> str:
        return self.__elementID

    @elementID.setter
    def elementID(self, elementID: str):
        self.__elementID = elementID

    @property
    def properties(self) -> str:
        return self.__properties

    @properties.setter
    def properties(self, properties: str):
        self.__properties = properties

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class UML_Activity_mine_ActivityEdge(Element):

    def __init__(self, objectFlow: bool, UML_Activity_mine_ActivityEdge: "UML_Activity_mine_Activity" = None, incoming: "UML_Activity_mine_ActivityNode" = None, outgoing: "UML_Activity_mine_ActivityNode" = None, ActivityEdge: "UML_Activity_mine_ActivityNode" = None, ActivityEdge8: "UML_Activity_mine_ActivityNode" = None, UML_Activity_mine_ActivityEdge15: "UML_Activity_mine_ExpansionRegion" = None):
        self.objectFlow = objectFlow
        self.UML_Activity_mine_ActivityEdge = UML_Activity_mine_ActivityEdge
        self.incoming = incoming
        self.outgoing = outgoing
        self.ActivityEdge = ActivityEdge
        self.ActivityEdge8 = ActivityEdge8
        self.UML_Activity_mine_ActivityEdge15 = UML_Activity_mine_ActivityEdge15
        
    @property
    def objectFlow(self) -> bool:
        return self.__objectFlow

    @objectFlow.setter
    def objectFlow(self, objectFlow: bool):
        self.__objectFlow = objectFlow

    @property
    def ActivityEdge8(self):
        return self.__ActivityEdge8

    @ActivityEdge8.setter
    def ActivityEdge8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_Activity_mine_ActivityEdge__ActivityEdge8", None)
        self.__ActivityEdge8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_Activity_mine_ActivityEdge__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActivityNode"):
                opp_val = getattr(old_value, "ActivityNode", None)
                if opp_val == self:
                    setattr(old_value, "ActivityNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActivityNode"):
                opp_val = getattr(value, "ActivityNode", None)
                setattr(value, "ActivityNode", self)

    @property
    def UML_Activity_mine_ActivityEdge15(self):
        return self.__UML_Activity_mine_ActivityEdge15

    @UML_Activity_mine_ActivityEdge15.setter
    def UML_Activity_mine_ActivityEdge15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_Activity_mine_ActivityEdge__UML_Activity_mine_ActivityEdge15", None)
        self.__UML_Activity_mine_ActivityEdge15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_Activity_mine_ExpansionRegion14"):
                opp_val = getattr(old_value, "UML_Activity_mine_ExpansionRegion14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_Activity_mine_ExpansionRegion14"):
                opp_val = getattr(value, "UML_Activity_mine_ExpansionRegion14", None)
                if opp_val is None:
                    setattr(value, "UML_Activity_mine_ExpansionRegion14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ActivityEdge(self):
        return self.__ActivityEdge

    @ActivityEdge.setter
    def ActivityEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_Activity_mine_ActivityEdge__ActivityEdge", None)
        self.__ActivityEdge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML_Activity_mine_ActivityEdge(self):
        return self.__UML_Activity_mine_ActivityEdge

    @UML_Activity_mine_ActivityEdge.setter
    def UML_Activity_mine_ActivityEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_Activity_mine_ActivityEdge__UML_Activity_mine_ActivityEdge", None)
        self.__UML_Activity_mine_ActivityEdge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_Activity_mine_Activity2"):
                opp_val = getattr(old_value, "UML_Activity_mine_Activity2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_Activity_mine_Activity2"):
                opp_val = getattr(value, "UML_Activity_mine_Activity2", None)
                if opp_val is None:
                    setattr(value, "UML_Activity_mine_Activity2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_Activity_mine_ActivityEdge__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActivityNode5"):
                opp_val = getattr(old_value, "ActivityNode5", None)
                if opp_val == self:
                    setattr(old_value, "ActivityNode5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActivityNode5"):
                opp_val = getattr(value, "ActivityNode5", None)
                setattr(value, "ActivityNode5", self)
