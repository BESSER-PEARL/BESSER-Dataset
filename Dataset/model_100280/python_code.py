from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class HLArcType(Enum):
    Normal = "Normal"
    Test = "Test"


############################################
# Definition of Classes
############################################

class model_HLArcType_1(ABC):

    pass
class model_ParameterAssignment:

    def __init__(self, parameter: str, value: str, parameterAssignment: "model_Instance" = None, ParameterAssignment: "model_Instance" = None):
        self.parameter = parameter
        self.value = value
        self.parameterAssignment = parameterAssignment
        self.ParameterAssignment = ParameterAssignment
        
        pass
    @property
    def parameter(self):
        return self.__parameter

    @parameter.setter
    def parameter(self, parameter: str):
        self.__parameter = parameter


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


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

class model_DeclarationStructure:

    pass
class Place:

    pass
class model_HLArcAddin(ABC):

    def __init__(self, type: str, model_HLArcAddin: "model_HLAnnotation" = None):
        self.type = type
        self.model_HLArcAddin = model_HLArcAddin
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


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


class model_CPNToolsTransitionAddin(ABC):

    pass
class model_HLTransitionAddin(ABC):

    pass
class model_HLPlaceAddin(ABC):

    pass
class TransitionNode:

    pass
class model_RefTrans(TransitionNode):

    pass
class Annotation:

    pass
class model_Time(Annotation):

    pass
class model_Type(Annotation):

    pass
class model_HLAnnotation(Annotation):

    pass
class model_Condition(Annotation):

    pass
class model_Code(Annotation):

    pass
class model_HLMarking(Annotation):

    pass
class CPNToolsTransitionAddin:

    pass
class HLTransitionAddin:

    pass
class model_Transition(TransitionNode):

    pass
class PlaceNode:

    pass
class model_Place(PlaceNode):

    pass
class model_FusionGroup(Place):

    pass
class HLPlaceAddin:

    pass
class Node:

    pass
class model_Instance(Node):

    def __init__(self, subPageID: str, Instance: "model_ParameterAssignment" = None, instance: set["model_ParameterAssignment"] = None):
        self.subPageID = subPageID
        self.Instance = Instance
        self.instance = instance if instance is not None else set()
        
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
                    

class model_TransitionNode(Node, HLTransitionAddin, CPNToolsTransitionAddin):

    pass
class model_PlaceNode(HLPlaceAddin, Node):

    pass
class model_RefPlace(PlaceNode):

    pass
class HasName:

    pass
class HasLabel:

    pass
class HLAnnotation:

    pass
class HasToolInfo:

    pass
class model_ToolInfo:

    def __init__(self, tool: str, version: str, ToolInfo: "model_HasToolInfo" = None, toolinfo: "model_HasToolInfo" = None):
        self.tool = tool
        self.version = version
        self.ToolInfo = ToolInfo
        self.toolinfo = toolinfo
        
        pass
    @property
    def tool(self):
        return self.__tool

    @tool.setter
    def tool(self, tool: str):
        self.__tool = tool


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


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
            if hasattr(old_value, "parent7"):
                opp_val = getattr(old_value, "parent7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent7"):
                opp_val = getattr(value, "parent7", None)
                if opp_val is None:
                    setattr(value, "parent7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_HasToolInfo(ABC):

    pass
class model_Name(HLAnnotation):

    pass
class model_HasName(ABC):

    pass
class Object:

    pass
class model_Node(Object):

    pass
class HasId:

    pass
class model_PetriNet(HasLabel, HasToolInfo, HasId, HasName):

    def __init__(self, type: str, PetriNet: "model_Page" = None, petriNet: set["model_Page"] = None, petriNet23: set["model_FusionGroup"] = None, PetriNet40: "model_FusionGroup" = None):
        self.type = type
        self.PetriNet = PetriNet
        self.petriNet = petriNet if petriNet is not None else set()
        self.petriNet23 = petriNet23 if petriNet23 is not None else set()
        self.PetriNet40 = PetriNet40
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


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
                if hasattr(item, "Page21"):
                    opp_val = getattr(item, "Page21", None)
                    
                    if opp_val == self:
                        setattr(item, "Page21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Page21"):
                    opp_val = getattr(item, "Page21", None)
                    
                    setattr(item, "Page21", self)
                    

    @property
    def petriNet23(self):
        return self.__petriNet23

    @petriNet23.setter
    def petriNet23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PetriNet__petriNet23", None)
        self.__petriNet23 = value if value is not None else set()
        
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
    def PetriNet(self):
        return self.__PetriNet

    @PetriNet.setter
    def PetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PetriNet__PetriNet", None)
        self.__PetriNet = value
        
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
    def PetriNet40(self):
        return self.__PetriNet40

    @PetriNet40.setter
    def PetriNet40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PetriNet__PetriNet40", None)
        self.__PetriNet40 = value
        
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

class model_HLDeclaration(HasId, Annotation):

    pass
class HLArcAddin:

    pass
class model_Arc(HasId, HLArcAddin):

    pass
class HLAnnotationAddin:

    pass
class HasGraphics:

    pass
class model_Object(HasGraphics, HasLabel, HasId, HasToolInfo, HasName):

    pass
class Label:

    pass
class model_Annotation(Label, HLAnnotationAddin, HasGraphics):

    pass
class model_Label(HasToolInfo):

    def __init__(self, Label: "model_HasLabel" = None, label: "model_HasLabel" = None):
        self.Label = Label
        self.label = label
        
        pass
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

    def asString(self) :
        # TODO: Implement asString method
        pass

class model_HasLabel(ABC):

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


class model_Attribute(Label):

    pass
class model_Page(HasLabel, HasId, HasName):

    pass