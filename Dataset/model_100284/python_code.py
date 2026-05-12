from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class nppn_Binding:

    pass
class org_k1s_nppn_Bindings:

    pass
class Container:

    pass
class org_k1s_nppn_Conditinoal(Container):

    pass
class org_k1s_nppn_Conditional(Container):

    pass
class org_k1s_nppn_Loop(Container):

    pass
class Block:

    pass
class org_k1s_nppn_Atomic(Block):

    pass
class org_k1s_nppn_Binding:

    def __init__(self, template: str, org_k1s_nppn_Binding: "nppn_Pragmatic" = None):
        self.template = template
        self.org_k1s_nppn_Binding = org_k1s_nppn_Binding
        
        pass
    @property
    def template(self):
        return self.__template

    @template.setter
    def template(self, template: str):
        self.__template = template


    @property
    def org_k1s_nppn_Binding(self):
        return self.__org_k1s_nppn_Binding

    @org_k1s_nppn_Binding.setter
    def org_k1s_nppn_Binding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_k1s_nppn_Binding__org_k1s_nppn_Binding", None)
        self.__org_k1s_nppn_Binding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nppn_Pragmatic45"):
                opp_val = getattr(old_value, "nppn_Pragmatic45", None)
                if opp_val == self:
                    setattr(old_value, "nppn_Pragmatic45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nppn_Pragmatic45"):
                opp_val = getattr(value, "nppn_Pragmatic45", None)
                setattr(value, "nppn_Pragmatic45", self)

class org_k1s_nppn_Container(Block):

    pass
class nppn_Transition:

    pass
class nppn_PlaceNode:

    pass
class org_k1s_nppn_Block:

    pass
class nppn_Block:

    pass
class org_k1s_nppn_Service:

    pass
class nppn_Service:

    pass
class nppn_Instance:

    pass
class org_k1s_nppn_Principal:

    pass
class org_k1s_nppn_PlacementConstraints:

    pass
class nppn_Principal:

    pass
class org_k1s_nppn_AbstractTemplateTree:

    pass
class Explicit:

    pass
class CustomPragmatics:

    pass
class org_k1s_nppn_CustomExplicitPragmatics(Explicit, CustomPragmatics):

    pass
class Derived:

    pass
class org_k1s_nppn_CustomDerivedPragmatics(CustomPragmatics, Derived):

    pass
class nppn_PlacementConstraints:

    pass
class org_k1s_nppn_PNPattern:

    pass
class nppn_PNPattern:

    pass
class Pragmatic:

    pass
class org_k1s_nppn_CustomPragmatics(Pragmatic):

    pass
class org_k1s_nppn_Explicit(Pragmatic):

    pass
class org_k1s_nppn_Derived(Pragmatic):

    pass
class org_k1s_nppn_Pragmatic:

    def __init__(self, name: str, org_k1s_nppn_Pragmatic: set["nppn_PlacementConstraints"] = None):
        self.name = name
        self.org_k1s_nppn_Pragmatic = org_k1s_nppn_Pragmatic if org_k1s_nppn_Pragmatic is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def org_k1s_nppn_Pragmatic(self):
        return self.__org_k1s_nppn_Pragmatic

    @org_k1s_nppn_Pragmatic.setter
    def org_k1s_nppn_Pragmatic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_k1s_nppn_Pragmatic__org_k1s_nppn_Pragmatic", None)
        self.__org_k1s_nppn_Pragmatic = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nppn_PlacementConstraints"):
                    opp_val = getattr(item, "nppn_PlacementConstraints", None)
                    
                    if opp_val == self:
                        setattr(item, "nppn_PlacementConstraints", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nppn_PlacementConstraints"):
                    opp_val = getattr(item, "nppn_PlacementConstraints", None)
                    
                    setattr(item, "nppn_PlacementConstraints", self)
                    

class nppn_TransitionNode:

    pass
class TransitionNode:

    pass
class org_k1s_nppn_Transition(TransitionNode):

    pass
class org_k1s_nppn_RefTrans(TransitionNode):

    pass
class nppn_Place:

    pass
class nppn_RefPlace:

    pass
class PlaceNode:

    pass
class org_k1s_nppn_RefPlace(PlaceNode):

    pass
class org_k1s_nppn_Place(PlaceNode):

    pass
class nppn_Monitor:

    pass
class nppn_Object:

    pass
class nppn_PetriNet:

    pass
class HasName:

    pass
class HasLabel:

    pass
class org_k1s_nppn_Page(HasLabel, HasName):

    pass
class org_k1s_nppn_PetriNet(HasLabel, HasName):

    def __init__(self, kind: str, timeType: str, petriNet23: set["nppn_Monitor"] = None, petriNet: set["nppn_Page"] = None):
        self.kind = kind
        self.timeType = timeType
        self.petriNet23 = petriNet23 if petriNet23 is not None else set()
        self.petriNet = petriNet if petriNet is not None else set()
        
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
    def petriNet(self):
        return self.__petriNet

    @petriNet.setter
    def petriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_k1s_nppn_PetriNet__petriNet", None)
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
        old_value = getattr(self, f"_org_k1s_nppn_PetriNet__petriNet23", None)
        self.__petriNet23 = value if value is not None else set()
        
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
                    

class org_k1s_nppn_Label(ABC):

    def __init__(self, label: "nppn_HasLabel" = None):
        self.label = label
        
        pass
    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_k1s_nppn_Label__label", None)
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

class nppn_Pragmatic:

    pass
class nppn_Arc:

    pass
class Object:

    pass
class org_k1s_nppn_Node(Object):

    pass
class HLAnnotation:

    pass
class org_k1s_nppn_Name(HLAnnotation):

    pass
class nppn_HasLabel:

    pass
class nppn_HLAnnotation:

    pass
class org_k1s_nppn_HLArcAddin(ABC):

    def __init__(self, kind: str, org_k1s_nppn_HLArcAddin: "nppn_HLAnnotation" = None):
        self.kind = kind
        self.org_k1s_nppn_HLArcAddin = org_k1s_nppn_HLArcAddin
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def org_k1s_nppn_HLArcAddin(self):
        return self.__org_k1s_nppn_HLArcAddin

    @org_k1s_nppn_HLArcAddin.setter
    def org_k1s_nppn_HLArcAddin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_k1s_nppn_HLArcAddin__org_k1s_nppn_HLArcAddin", None)
        self.__org_k1s_nppn_HLArcAddin = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nppn_HLAnnotation"):
                opp_val = getattr(old_value, "nppn_HLAnnotation", None)
                if opp_val == self:
                    setattr(old_value, "nppn_HLAnnotation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nppn_HLAnnotation"):
                opp_val = getattr(value, "nppn_HLAnnotation", None)
                setattr(value, "nppn_HLAnnotation", self)

class Node:

    pass
class org_k1s_nppn_TransitionNode(Node):

    pass
class org_k1s_nppn_PlaceNode(Node):

    pass
class org_k1s_nppn_HLAnnotation:

    pass
class org_k1s_nppn_Instance(Node):

    def __init__(self, subPageID: str):
        self.subPageID = subPageID
        
        pass
    @property
    def subPageID(self):
        return self.__subPageID

    @subPageID.setter
    def subPageID(self, subPageID: str):
        self.__subPageID = subPageID


class nppn_Page:

    pass
class nppn_Name:

    pass
class org_k1s_nppn_HasName(ABC):

    pass
class nppn_Label:

    pass
class org_k1s_nppn_HasLabel(ABC):

    pass
class nppn_Node:

    pass
class HLArcAddin:

    pass
class HasGraphics:

    pass
class org_k1s_nppn_Object(HasLabel, HasGraphics, HasName):

    pass
class org_k1s_nppn_Arc(HasGraphics, HLArcAddin):

    pass