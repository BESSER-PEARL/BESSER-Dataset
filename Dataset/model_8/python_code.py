from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class TrgNetContent:

    pass
class TrgLabeledElement:

    pass
class jointPackage_PetriNet2PNML_TrgName(TrgLabeledElement):

    pass
class TrgIdedElement:

    pass
class jointPackage_PetriNet2PNML_TrgNetContentElement(TrgIdedElement, TrgNetContent):

    pass
class TrgNetContentElement:

    pass
class jointPackage_PetriNet2PNML_TrgTransition(TrgNetContentElement):

    pass
class jointPackage_PetriNet2PNML_TrgPlace(TrgNetContentElement):

    pass
class jointPackage_PetriNet2PNML_TrgArc(TrgIdedElement, TrgNetContent):

    pass
class SrcArc:

    pass
class jointPackage_PetriNet2PNML_SrcPlaceToTransition(SrcArc):

    pass
class jointPackage_PetriNet2PNML_SrcTransitionToPlace(SrcArc):

    pass
class SrcElement:

    pass
class jointPackage_PetriNet2PNML_SrcTransition(SrcElement):

    pass
class jointPackage_PetriNet2PNML_SrcPlace(SrcElement):

    pass
class jointPackage_PetriNet2PNML_TrgLocatedElement(ABC):

    def __init__(self, location: str):
        self.location = location
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

class jointPackage_PetriNet2PNML_TrgNetElement(TrgIdedElement):

    pass
class TrgLocatedElement:

    pass
class jointPackage_PetriNet2PNML_TrgLabeledElement(TrgLocatedElement):

    pass
class jointPackage_PetriNet2PNML_TrgIdedElement(TrgLocatedElement):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class jointPackage_PetriNet2PNML_TrgNetContent(TrgLocatedElement):

    pass
class jointPackage_PetriNet2PNML_TrgLabel(TrgLocatedElement):

    def __init__(self, text: str, jointPackage_PetriNet2PNML_TrgLabel: "jointPackage_PetriNet2PNML_TrgLabeledElement" = None):
        self.text = text
        self.jointPackage_PetriNet2PNML_TrgLabel = jointPackage_PetriNet2PNML_TrgLabel
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def jointPackage_PetriNet2PNML_TrgLabel(self):
        return self.__jointPackage_PetriNet2PNML_TrgLabel

    @jointPackage_PetriNet2PNML_TrgLabel.setter
    def jointPackage_PetriNet2PNML_TrgLabel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_PetriNet2PNML_TrgLabel__jointPackage_PetriNet2PNML_TrgLabel", None)
        self.__jointPackage_PetriNet2PNML_TrgLabel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_PetriNet2PNML_TrgLabeledElement"):
                opp_val = getattr(old_value, "jointPackage_PetriNet2PNML_TrgLabeledElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_PetriNet2PNML_TrgLabeledElement"):
                opp_val = getattr(value, "jointPackage_PetriNet2PNML_TrgLabeledElement", None)
                if opp_val is None:
                    setattr(value, "jointPackage_PetriNet2PNML_TrgLabeledElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jointPackage_PetriNet2PNML_TrgURI(TrgLocatedElement):

    def __init__(self, value: str, jointPackage_PetriNet2PNML_TrgURI: "jointPackage_PetriNet2PNML_TrgPNMLDocument" = None, jointPackage_PetriNet2PNML_TrgURI31: "jointPackage_PetriNet2PNML_TrgNetElement" = None):
        self.value = value
        self.jointPackage_PetriNet2PNML_TrgURI = jointPackage_PetriNet2PNML_TrgURI
        self.jointPackage_PetriNet2PNML_TrgURI31 = jointPackage_PetriNet2PNML_TrgURI31
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def jointPackage_PetriNet2PNML_TrgURI(self):
        return self.__jointPackage_PetriNet2PNML_TrgURI

    @jointPackage_PetriNet2PNML_TrgURI.setter
    def jointPackage_PetriNet2PNML_TrgURI(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_PetriNet2PNML_TrgURI__jointPackage_PetriNet2PNML_TrgURI", None)
        self.__jointPackage_PetriNet2PNML_TrgURI = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_PetriNet2PNML_TrgPNMLDocument26"):
                opp_val = getattr(old_value, "jointPackage_PetriNet2PNML_TrgPNMLDocument26", None)
                if opp_val == self:
                    setattr(old_value, "jointPackage_PetriNet2PNML_TrgPNMLDocument26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_PetriNet2PNML_TrgPNMLDocument26"):
                opp_val = getattr(value, "jointPackage_PetriNet2PNML_TrgPNMLDocument26", None)
                setattr(value, "jointPackage_PetriNet2PNML_TrgPNMLDocument26", self)

    @property
    def jointPackage_PetriNet2PNML_TrgURI31(self):
        return self.__jointPackage_PetriNet2PNML_TrgURI31

    @jointPackage_PetriNet2PNML_TrgURI31.setter
    def jointPackage_PetriNet2PNML_TrgURI31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_PetriNet2PNML_TrgURI__jointPackage_PetriNet2PNML_TrgURI31", None)
        self.__jointPackage_PetriNet2PNML_TrgURI31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_PetriNet2PNML_TrgNetElement30"):
                opp_val = getattr(old_value, "jointPackage_PetriNet2PNML_TrgNetElement30", None)
                if opp_val == self:
                    setattr(old_value, "jointPackage_PetriNet2PNML_TrgNetElement30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_PetriNet2PNML_TrgNetElement30"):
                opp_val = getattr(value, "jointPackage_PetriNet2PNML_TrgNetElement30", None)
                setattr(value, "jointPackage_PetriNet2PNML_TrgNetElement30", self)

class jointPackage_PetriNet2PNML_SrcLocatedElement(ABC):

    def __init__(self, location: str):
        self.location = location
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

class jointPackage_PetriNet2PNML_TrgPNMLDocument(TrgLocatedElement):

    pass
class jointPackage_PetriNet2PNML_JointMM:

    pass
class SrcNamedElement:

    pass
class jointPackage_PetriNet2PNML_SrcElement(SrcNamedElement):

    pass
class jointPackage_PetriNet2PNML_SrcPetriNet(SrcNamedElement):

    pass
class jointPackage_PetriNet2PNML_SrcArc(SrcNamedElement):

    def __init__(self, weight: int, SrcArc: "jointPackage_PetriNet2PNML_SrcPetriNet" = None, arcs: "jointPackage_PetriNet2PNML_SrcPetriNet" = None):
        self.weight = weight
        self.SrcArc = SrcArc
        self.arcs = arcs
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def arcs(self):
        return self.__arcs

    @arcs.setter
    def arcs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_PetriNet2PNML_SrcArc__arcs", None)
        self.__arcs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SrcPetriNet16"):
                opp_val = getattr(old_value, "SrcPetriNet16", None)
                if opp_val == self:
                    setattr(old_value, "SrcPetriNet16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SrcPetriNet16"):
                opp_val = getattr(value, "SrcPetriNet16", None)
                setattr(value, "SrcPetriNet16", self)

    @property
    def SrcArc(self):
        return self.__SrcArc

    @SrcArc.setter
    def SrcArc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_PetriNet2PNML_SrcArc__SrcArc", None)
        self.__SrcArc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "net5"):
                opp_val = getattr(old_value, "net5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "net5"):
                opp_val = getattr(value, "net5", None)
                if opp_val is None:
                    setattr(value, "net5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SrcLocatedElement:

    pass
class jointPackage_PetriNet2PNML_SrcNamedElement(SrcLocatedElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
