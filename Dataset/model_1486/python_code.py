from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class TrgArc:

    pass
class jointPackage_Grafcet2PetriNet_TrgPlaceToTransition(TrgArc):

    pass
class jointPackage_Grafcet2PetriNet_TrgTransitionToPlace(TrgArc):

    pass
class TrgElement:

    pass
class jointPackage_Grafcet2PetriNet_TrgTransition(TrgElement):

    pass
class jointPackage_Grafcet2PetriNet_TrgPlace(TrgElement):

    pass
class TrgNamedElement:

    pass
class jointPackage_Grafcet2PetriNet_TrgArc(TrgNamedElement):

    def __init__(self, weight: int, TrgArc: "jointPackage_Grafcet2PetriNet_TrgPetriNet" = None, arcs: "jointPackage_Grafcet2PetriNet_TrgPetriNet" = None):
        self.weight = weight
        self.TrgArc = TrgArc
        self.arcs = arcs
        
        pass
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight


    @property
    def TrgArc(self):
        return self.__TrgArc

    @TrgArc.setter
    def TrgArc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Grafcet2PetriNet_TrgArc__TrgArc", None)
        self.__TrgArc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "net27"):
                opp_val = getattr(old_value, "net27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "net27"):
                opp_val = getattr(value, "net27", None)
                if opp_val is None:
                    setattr(value, "net27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def arcs(self):
        return self.__arcs

    @arcs.setter
    def arcs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Grafcet2PetriNet_TrgArc__arcs", None)
        self.__arcs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TrgPetriNet41"):
                opp_val = getattr(old_value, "TrgPetriNet41", None)
                if opp_val == self:
                    setattr(old_value, "TrgPetriNet41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TrgPetriNet41"):
                opp_val = getattr(value, "TrgPetriNet41", None)
                setattr(value, "TrgPetriNet41", self)

class jointPackage_Grafcet2PetriNet_TrgElement(TrgNamedElement):

    pass
class TrgLocatedElement:

    pass
class jointPackage_Grafcet2PetriNet_TrgNamedElement(TrgLocatedElement):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class jointPackage_Grafcet2PetriNet_TrgLocatedElement(ABC):

    def __init__(self, location: str):
        self.location = location
        
        pass
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


class SrcLocatedElement:

    pass
class jointPackage_Grafcet2PetriNet_SrcNamedElement(SrcLocatedElement):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class SrcConnection:

    pass
class jointPackage_Grafcet2PetriNet_SrcStepToTransition(SrcConnection):

    pass
class jointPackage_Grafcet2PetriNet_SrcTransitionToStep(SrcConnection):

    pass
class SrcElement:

    pass
class jointPackage_Grafcet2PetriNet_SrcTransition(SrcElement):

    def __init__(self, condition: str, to10: set["jointPackage_Grafcet2PetriNet_SrcStepToTransition"] = None, from_13: set["jointPackage_Grafcet2PetriNet_SrcTransitionToStep"] = None, SrcTransition: "jointPackage_Grafcet2PetriNet_SrcStepToTransition" = None, SrcTransition21: "jointPackage_Grafcet2PetriNet_SrcTransitionToStep" = None):
        self.condition = condition
        self.to10 = to10 if to10 is not None else set()
        self.from_13 = from_13 if from_13 is not None else set()
        self.SrcTransition = SrcTransition
        self.SrcTransition21 = SrcTransition21
        
        pass
    @property
    def condition(self):
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition


    @property
    def SrcTransition(self):
        return self.__SrcTransition

    @SrcTransition.setter
    def SrcTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Grafcet2PetriNet_SrcTransition__SrcTransition", None)
        self.__SrcTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingConnections"):
                opp_val = getattr(old_value, "incomingConnections", None)
                if opp_val == self:
                    setattr(old_value, "incomingConnections", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingConnections"):
                opp_val = getattr(value, "incomingConnections", None)
                setattr(value, "incomingConnections", self)

    @property
    def to10(self):
        return self.__to10

    @to10.setter
    def to10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Grafcet2PetriNet_SrcTransition__to10", None)
        self.__to10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SrcStepToTransition11"):
                    opp_val = getattr(item, "SrcStepToTransition11", None)
                    
                    if opp_val == self:
                        setattr(item, "SrcStepToTransition11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SrcStepToTransition11"):
                    opp_val = getattr(item, "SrcStepToTransition11", None)
                    
                    setattr(item, "SrcStepToTransition11", self)
                    

    @property
    def SrcTransition21(self):
        return self.__SrcTransition21

    @SrcTransition21.setter
    def SrcTransition21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Grafcet2PetriNet_SrcTransition__SrcTransition21", None)
        self.__SrcTransition21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingConnections20"):
                opp_val = getattr(old_value, "outgoingConnections20", None)
                if opp_val == self:
                    setattr(old_value, "outgoingConnections20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingConnections20"):
                opp_val = getattr(value, "outgoingConnections20", None)
                setattr(value, "outgoingConnections20", self)

    @property
    def from_13(self):
        return self.__from_13

    @from_13.setter
    def from_13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Grafcet2PetriNet_SrcTransition__from_13", None)
        self.__from_13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SrcTransitionToStep14"):
                    opp_val = getattr(item, "SrcTransitionToStep14", None)
                    
                    if opp_val == self:
                        setattr(item, "SrcTransitionToStep14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SrcTransitionToStep14"):
                    opp_val = getattr(item, "SrcTransitionToStep14", None)
                    
                    setattr(item, "SrcTransitionToStep14", self)
                    

class jointPackage_Grafcet2PetriNet_SrcStep(SrcElement):

    def __init__(self, isInitial: bool, isActive: bool, action: str, SrcStep: "jointPackage_Grafcet2PetriNet_SrcStepToTransition" = None, SrcStep24: "jointPackage_Grafcet2PetriNet_SrcTransitionToStep" = None, to: set["jointPackage_Grafcet2PetriNet_SrcTransitionToStep"] = None, from_: set["jointPackage_Grafcet2PetriNet_SrcStepToTransition"] = None):
        self.isInitial = isInitial
        self.isActive = isActive
        self.action = action
        self.SrcStep = SrcStep
        self.SrcStep24 = SrcStep24
        self.to = to if to is not None else set()
        self.from_ = from_ if from_ is not None else set()
        
        pass
    @property
    def isActive(self):
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: bool):
        self.__isActive = isActive


    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action


    @property
    def isInitial(self):
        return self.__isInitial

    @isInitial.setter
    def isInitial(self, isInitial: bool):
        self.__isInitial = isInitial


    @property
    def SrcStep(self):
        return self.__SrcStep

    @SrcStep.setter
    def SrcStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Grafcet2PetriNet_SrcStep__SrcStep", None)
        self.__SrcStep = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingConnections"):
                opp_val = getattr(old_value, "outgoingConnections", None)
                if opp_val == self:
                    setattr(old_value, "outgoingConnections", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingConnections"):
                opp_val = getattr(value, "outgoingConnections", None)
                setattr(value, "outgoingConnections", self)

    @property
    def from_(self):
        return self.__from_

    @from_.setter
    def from_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Grafcet2PetriNet_SrcStep__from_", None)
        self.__from_ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SrcStepToTransition"):
                    opp_val = getattr(item, "SrcStepToTransition", None)
                    
                    if opp_val == self:
                        setattr(item, "SrcStepToTransition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SrcStepToTransition"):
                    opp_val = getattr(item, "SrcStepToTransition", None)
                    
                    setattr(item, "SrcStepToTransition", self)
                    

    @property
    def to(self):
        return self.__to

    @to.setter
    def to(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Grafcet2PetriNet_SrcStep__to", None)
        self.__to = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SrcTransitionToStep"):
                    opp_val = getattr(item, "SrcTransitionToStep", None)
                    
                    if opp_val == self:
                        setattr(item, "SrcTransitionToStep", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SrcTransitionToStep"):
                    opp_val = getattr(item, "SrcTransitionToStep", None)
                    
                    setattr(item, "SrcTransitionToStep", self)
                    

    @property
    def SrcStep24(self):
        return self.__SrcStep24

    @SrcStep24.setter
    def SrcStep24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Grafcet2PetriNet_SrcStep__SrcStep24", None)
        self.__SrcStep24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingConnections23"):
                opp_val = getattr(old_value, "incomingConnections23", None)
                if opp_val == self:
                    setattr(old_value, "incomingConnections23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingConnections23"):
                opp_val = getattr(value, "incomingConnections23", None)
                setattr(value, "incomingConnections23", self)

class SrcNamedElement:

    pass
class jointPackage_Grafcet2PetriNet_SrcElement(SrcNamedElement):

    pass
class jointPackage_Grafcet2PetriNet_SrcConnection(SrcNamedElement):

    pass
class jointPackage_Grafcet2PetriNet_SrcLocatedElement(ABC):

    def __init__(self, location: str):
        self.location = location
        
        pass
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


class jointPackage_Grafcet2PetriNet_TrgPetriNet(TrgNamedElement):

    pass
class jointPackage_Grafcet2PetriNet_SrcGrafcet(SrcNamedElement):

    pass
class jointPackage_Grafcet2PetriNet_JointMM:

    pass