from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class EsmLayoutDirection(Enum):
    DOWN = "DOWN"
    LEFT = "LEFT"
    UP = "UP"
    RIGHT = "RIGHT"
    DEFAULT = "DEFAULT"
class EsmStateKind(Enum):
    NORMAL = "NORMAL"
    INITIAL = "INITIAL"
    FINAL = "FINAL"


############################################
# Definition of Classes
############################################

class esm_DExpression:

    pass
class EsmState:

    pass
class esm_EsmDerivedState(EsmState):

    pass
class IEsmState:

    pass
class esm_EsmConcurrentState(IEsmState):

    pass
class esm_EsmState(IEsmState):

    pass
class esm_DStateEvent:

    pass
class esm_IEsmState(ABC):

    def __init__(self, kind: str, esm_IEsmState5: "esm_DState" = None, esm_IEsmState: "esm_IEsmStateModel" = None, esm_IEsmState7: "esm_DRichText" = None):
        self.kind = kind
        self.esm_IEsmState5 = esm_IEsmState5
        self.esm_IEsmState = esm_IEsmState
        self.esm_IEsmState7 = esm_IEsmState7
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def esm_IEsmState(self):
        return self.__esm_IEsmState

    @esm_IEsmState.setter
    def esm_IEsmState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esm_IEsmState__esm_IEsmState", None)
        self.__esm_IEsmState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esm_IEsmStateModel"):
                opp_val = getattr(old_value, "esm_IEsmStateModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esm_IEsmStateModel"):
                opp_val = getattr(value, "esm_IEsmStateModel", None)
                if opp_val is None:
                    setattr(value, "esm_IEsmStateModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def esm_IEsmState5(self):
        return self.__esm_IEsmState5

    @esm_IEsmState5.setter
    def esm_IEsmState5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esm_IEsmState__esm_IEsmState5", None)
        self.__esm_IEsmState5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esm_DState"):
                opp_val = getattr(old_value, "esm_DState", None)
                if opp_val == self:
                    setattr(old_value, "esm_DState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esm_DState"):
                opp_val = getattr(value, "esm_DState", None)
                setattr(value, "esm_DState", self)

    @property
    def esm_IEsmState7(self):
        return self.__esm_IEsmState7

    @esm_IEsmState7.setter
    def esm_IEsmState7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esm_IEsmState__esm_IEsmState7", None)
        self.__esm_IEsmState7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esm_DRichText"):
                opp_val = getattr(old_value, "esm_DRichText", None)
                if opp_val == self:
                    setattr(old_value, "esm_DRichText", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esm_DRichText"):
                opp_val = getattr(value, "esm_DRichText", None)
                setattr(value, "esm_DRichText", self)

class IEsmLayout:

    pass
class esm_EsmTransition(IEsmLayout):

    pass
class esm_IEsmStateModel(IEsmLayout):

    pass
class esm_IEsmLayout(ABC):

    def __init__(self, direction: str):
        self.direction = direction
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

class esm_DEntityType:

    pass
class IDiagramRoot:

    pass
class IStaticReferenceTarget:

    pass
class INavigableMemberContainer:

    pass
class IEsmStateModel:

    pass
class esm_EsmCompositeState(IEsmState, IEsmStateModel):

    pass
class esm_EsmSubStateModel(IEsmStateModel):

    pass
class esm_DRichText:

    pass
class esm_DState:

    pass
class DModel:

    pass
class esm_EsmEntityStateModel(IStaticReferenceTarget, INavigableMemberContainer, IDiagramRoot, IEsmStateModel, DModel):

    pass