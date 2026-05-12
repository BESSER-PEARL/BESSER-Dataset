from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TimeType(Enum):
    Integer = "Integer"
    Real = "Real"
class HLArcType(Enum):
    Normal = "Normal"
    Test = "Test"
    Inhibitor = "Inhibitor"
    Reset = "Reset"


############################################
# Definition of Classes
############################################

class CPNToolsTransitionAddin:

    pass
class HLTransitionAddin:

    pass
class TransitionNode:

    pass
class model_Transition(TransitionNode):

    pass
class model_RefTrans(TransitionNode):

    pass
class HLPlaceAddin:

    pass
class PlaceNode:

    pass
class model_RefPlace(PlaceNode):

    pass
class model_Place(PlaceNode):

    pass
class model_Monitor:

    pass
class HasToolInfo:

    pass
class HasName:

    pass
class HasLabel:

    pass
class Object:

    pass
class HLAnnotation:

    pass
class model_HasLabel(ABC):

    pass
class model_ParameterAssignment:

    def __init__(self, parameter: str, value: str, ParameterAssignment: "model_Instance" = None, parameterAssignment: "model_Instance" = None):
        self.parameter = parameter
        self.value = value
        self.ParameterAssignment = ParameterAssignment
        self.parameterAssignment = parameterAssignment
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def parameter(self):
        return self.__parameter

    @parameter.setter
    def parameter(self, parameter: str):
        self.__parameter = parameter


    @property
    def parameterAssignment(self):
        return self.__parameterAssignment

    @parameterAssignment.setter
    def parameterAssignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ParameterAssignment__parameterAssignment", None)
        self.__parameterAssignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instance"):
                opp_val = getattr(old_value, "Instance", None)
                if opp_val == self:
                    setattr(old_value, "Instance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instance"):
                opp_val = getattr(value, "Instance", None)
                setattr(value, "Instance", self)

    @property
    def ParameterAssignment(self):
        return self.__ParameterAssignment

    @ParameterAssignment.setter
    def ParameterAssignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ParameterAssignment__ParameterAssignment", None)
        self.__ParameterAssignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "instance"):
                opp_val = getattr(old_value, "instance", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "instance"):
                opp_val = getattr(value, "instance", None)
                if opp_val is None:
                    setattr(value, "instance", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Node:

    pass
class model_TransitionNode(Node, CPNToolsTransitionAddin, HLTransitionAddin):

    pass
class model_PlaceNode(HLPlaceAddin, Node):

    pass
class model_Instance(Node):

    def __init__(self, subPageID: str, instance: set["model_ParameterAssignment"] = None, Instance: "model_ParameterAssignment" = None):
        self.subPageID = subPageID
        self.instance = instance if instance is not None else set()
        self.Instance = Instance
        
        pass
    @property
    def subPageID(self):
        return self.__subPageID

    @subPageID.setter
    def subPageID(self, subPageID: str):
        self.__subPageID = subPageID


    @property
    def Instance(self):
        return self.__Instance

    @Instance.setter
    def Instance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Instance__Instance", None)
        self.__Instance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameterAssignment"):
                opp_val = getattr(old_value, "parameterAssignment", None)
                if opp_val == self:
                    setattr(old_value, "parameterAssignment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameterAssignment"):
                opp_val = getattr(value, "parameterAssignment", None)
                setattr(value, "parameterAssignment", self)

    @property
    def instance(self):
        return self.__instance

    @instance.setter
    def instance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Instance__instance", None)
        self.__instance = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ParameterAssignment"):
                    opp_val = getattr(item, "ParameterAssignment", None)
                    
                    if opp_val == self:
                        setattr(item, "ParameterAssignment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ParameterAssignment"):
                    opp_val = getattr(item, "ParameterAssignment", None)
                    
                    setattr(item, "ParameterAssignment", self)
                    

class model_ToolInfo:

    def __init__(self, version: str, tool: str, ToolInfo: "model_HasToolInfo" = None, toolinfo: "model_HasToolInfo" = None):
        self.version = version
        self.tool = tool
        self.ToolInfo = ToolInfo
        self.toolinfo = toolinfo
        
        pass
    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def tool(self):
        return self.__tool

    @tool.setter
    def tool(self, tool: str):
        self.__tool = tool


    @property
    def toolinfo(self):
        return self.__toolinfo

    @toolinfo.setter
    def toolinfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ToolInfo__toolinfo", None)
        self.__toolinfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HasToolInfo"):
                opp_val = getattr(old_value, "HasToolInfo", None)
                if opp_val == self:
                    setattr(old_value, "HasToolInfo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HasToolInfo"):
                opp_val = getattr(value, "HasToolInfo", None)
                setattr(value, "HasToolInfo", self)

    @property
    def ToolInfo(self):
        return self.__ToolInfo

    @ToolInfo.setter
    def ToolInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ToolInfo__ToolInfo", None)
        self.__ToolInfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent19"):
                opp_val = getattr(old_value, "parent19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent19"):
                opp_val = getattr(value, "parent19", None)
                if opp_val is None:
                    setattr(value, "parent19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_HasToolInfo(ABC):

    pass
class model_Name(HLAnnotation):

    pass
class model_HasName(ABC):

    pass
class model_Label(HasToolInfo):

    def __init__(self, Label: "model_HasLabel" = None, label: "model_HasLabel" = None):
        self.Label = Label
        self.label = label
        
        pass
    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Label__label", None)
        self.__label = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HasLabel"):
                opp_val = getattr(old_value, "HasLabel", None)
                if opp_val == self:
                    setattr(old_value, "HasLabel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HasLabel"):
                opp_val = getattr(value, "HasLabel", None)
                setattr(value, "HasLabel", self)

    @property
    def Label(self):
        return self.__Label

    @Label.setter
    def Label(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Label__Label", None)
        self.__Label = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def asString(self) :
        # TODO: Implement asString method
        pass

class model_HasId(ABC):

    def __init__(self, id: str):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


class model_HLTransitionAddin(ABC):

    pass
class model_HLPlaceAddin(ABC):

    pass
class model_DeclarationStructure:

    pass
class Annotation:

    pass
class model_Sort(Annotation):

    pass
class model_HLMarking(Annotation):

    pass
class model_HLArcAddin(ABC):

    def __init__(self, kind: str, model_HLArcAddin: "model_HLAnnotation" = None):
        self.kind = kind
        self.model_HLArcAddin = model_HLArcAddin
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def model_HLArcAddin(self):
        return self.__model_HLArcAddin

    @model_HLArcAddin.setter
    def model_HLArcAddin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_HLArcAddin__model_HLArcAddin", None)
        self.__model_HLArcAddin = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_HLAnnotation"):
                opp_val = getattr(old_value, "model_HLAnnotation", None)
                if opp_val == self:
                    setattr(old_value, "model_HLAnnotation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_HLAnnotation"):
                opp_val = getattr(value, "model_HLAnnotation", None)
                setattr(value, "model_HLAnnotation", self)

class model_HLAnnotationAddin(ABC):

    def __init__(self, text: str):
        self.text = text
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


class model_HLAnnotation(Annotation):

    pass
class Place:

    pass
class model_FusionGroup(Place):

    pass
class model_Condition(Annotation):

    pass
class model_Priority(Annotation):

    pass
class model_Time(Annotation):

    pass
class model_Code(Annotation):

    pass
class model_CPNToolsTransitionAddin(ABC):

    pass
class model_Node(Object):

    pass
class HLArcAddin:

    pass
class HasId:

    pass
class model_Page(HasLabel, HasName, HasId):

    pass
class model_PetriNet(HasLabel, HasToolInfo, HasName, HasId):

    def __init__(self, timeType: str, kind: str, PetriNet: "model_FusionGroup" = None, PetriNet28: "model_Page" = None, petriNet: set["model_Page"] = None, petriNet38: set["model_Monitor"] = None, petriNet40: set["model_FusionGroup"] = None):
        self.timeType = timeType
        self.kind = kind
        self.PetriNet = PetriNet
        self.PetriNet28 = PetriNet28
        self.petriNet = petriNet if petriNet is not None else set()
        self.petriNet38 = petriNet38 if petriNet38 is not None else set()
        self.petriNet40 = petriNet40 if petriNet40 is not None else set()
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def timeType(self):
        return self.__timeType

    @timeType.setter
    def timeType(self, timeType: str):
        self.__timeType = timeType


    @property
    def PetriNet28(self):
        return self.__PetriNet28

    @PetriNet28.setter
    def PetriNet28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PetriNet__PetriNet28", None)
        self.__PetriNet28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "page"):
                opp_val = getattr(old_value, "page", None)
                if opp_val == self:
                    setattr(old_value, "page", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "page"):
                opp_val = getattr(value, "page", None)
                setattr(value, "page", self)

    @property
    def petriNet(self):
        return self.__petriNet

    @petriNet.setter
    def petriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PetriNet__petriNet", None)
        self.__petriNet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Page36"):
                    opp_val = getattr(item, "Page36", None)
                    
                    if opp_val == self:
                        setattr(item, "Page36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Page36"):
                    opp_val = getattr(item, "Page36", None)
                    
                    setattr(item, "Page36", self)
                    

    @property
    def PetriNet(self):
        return self.__PetriNet

    @PetriNet.setter
    def PetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PetriNet__PetriNet", None)
        self.__PetriNet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fusionGroups"):
                opp_val = getattr(old_value, "fusionGroups", None)
                if opp_val == self:
                    setattr(old_value, "fusionGroups", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fusionGroups"):
                opp_val = getattr(value, "fusionGroups", None)
                setattr(value, "fusionGroups", self)

    @property
    def petriNet40(self):
        return self.__petriNet40

    @petriNet40.setter
    def petriNet40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PetriNet__petriNet40", None)
        self.__petriNet40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FusionGroup"):
                    opp_val = getattr(item, "FusionGroup", None)
                    
                    if opp_val == self:
                        setattr(item, "FusionGroup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FusionGroup"):
                    opp_val = getattr(item, "FusionGroup", None)
                    
                    setattr(item, "FusionGroup", self)
                    

    @property
    def petriNet38(self):
        return self.__petriNet38

    @petriNet38.setter
    def petriNet38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PetriNet__petriNet38", None)
        self.__petriNet38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "monitors.ecoreMonitor"):
                    opp_val = getattr(item, "monitors.ecoreMonitor", None)
                    
                    if opp_val == self:
                        setattr(item, "monitors.ecoreMonitor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "monitors.ecoreMonitor"):
                    opp_val = getattr(item, "monitors.ecoreMonitor", None)
                    
                    setattr(item, "monitors.ecoreMonitor", self)
                    

class model_HLDeclaration(Annotation, HasId):

    pass
class HLAnnotationAddin:

    pass
class HasGraphics:

    pass
class model_Object(HasGraphics, HasToolInfo, HasName, HasLabel, HasId):

    pass
class model_Arc(HasId, HasGraphics, HLArcAddin):

    pass
class Label:

    pass
class model_Attribute(Label):

    pass
class model_Annotation(HLAnnotationAddin, HasGraphics, Label):

    pass