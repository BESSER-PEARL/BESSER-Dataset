from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PseudostateKind(Enum):
    initial = "initial"


############################################
# Definition of Classes
############################################

class AbstractState:

    pass
class compositestates_State(AbstractState):

    def __init__(self, ownerState: set["compositestates_Region"] = None, State: "compositestates_Region" = None):
        self.ownerState = ownerState if ownerState is not None else set()
        self.State = State
        
        pass
    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compositestates_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedRegions"):
                opp_val = getattr(old_value, "ownedRegions", None)
                if opp_val == self:
                    setattr(old_value, "ownedRegions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedRegions"):
                opp_val = getattr(value, "ownedRegions", None)
                setattr(value, "ownedRegions", self)

    @property
    def ownerState(self):
        return self.__ownerState

    @ownerState.setter
    def ownerState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compositestates_State__ownerState", None)
        self.__ownerState = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Region"):
                    opp_val = getattr(item, "Region", None)
                    
                    if opp_val == self:
                        setattr(item, "Region", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Region"):
                    opp_val = getattr(item, "Region", None)
                    
                    setattr(item, "Region", self)
                    

    def evalState(self, compositestates_context):
        # TODO: Implement evalState method
        pass

class compositestates_AbstractState(ABC):

    pass
class compositestates_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class compositestates_Pseudostate(AbstractState):

    def __init__(self, kind: str):
        self.kind = kind
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


class compositestates_Transition:

    pass
class NamedElement:

    pass
class compositestates_Region(NamedElement):

    def __init__(self, Region: "compositestates_State" = None, Region7: "compositestates_AbstractState" = None, ownerRegion: set["compositestates_AbstractState"] = None, ownedRegions: "compositestates_State" = None):
        self.Region = Region
        self.Region7 = Region7
        self.ownerRegion = ownerRegion if ownerRegion is not None else set()
        self.ownedRegions = ownedRegions
        
        pass
    @property
    def Region7(self):
        return self.__Region7

    @Region7.setter
    def Region7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compositestates_Region__Region7", None)
        self.__Region7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subvertex"):
                opp_val = getattr(old_value, "subvertex", None)
                if opp_val == self:
                    setattr(old_value, "subvertex", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subvertex"):
                opp_val = getattr(value, "subvertex", None)
                setattr(value, "subvertex", self)

    @property
    def ownedRegions(self):
        return self.__ownedRegions

    @ownedRegions.setter
    def ownedRegions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compositestates_Region__ownedRegions", None)
        self.__ownedRegions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State"):
                opp_val = getattr(old_value, "State", None)
                if opp_val == self:
                    setattr(old_value, "State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State"):
                opp_val = getattr(value, "State", None)
                setattr(value, "State", self)

    @property
    def ownerRegion(self):
        return self.__ownerRegion

    @ownerRegion.setter
    def ownerRegion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compositestates_Region__ownerRegion", None)
        self.__ownerRegion = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractState"):
                    opp_val = getattr(item, "AbstractState", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractState"):
                    opp_val = getattr(item, "AbstractState", None)
                    
                    setattr(item, "AbstractState", self)
                    

    @property
    def Region(self):
        return self.__Region

    @Region.setter
    def Region(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compositestates_Region__Region", None)
        self.__Region = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownerState"):
                opp_val = getattr(old_value, "ownerState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownerState"):
                opp_val = getattr(value, "ownerState", None)
                if opp_val is None:
                    setattr(value, "ownerState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def initRegion(self, compositestates_context):
        # TODO: Implement initRegion method
        pass
