from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class qvtimperativecs_QueryCS:

    pass
class qvtimperativecs_TransformationCS:

    pass
class RootPackageCS:

    pass
class qvtimperativecs_TopLevelCS(RootPackageCS):

    pass
class ModelElementCS:

    pass
class qvtimperativecs_MappingStatementCS(ModelElementCS):

    pass
class qvtimperativecs_VariableCS:

    pass
class qvtimperativecs_Mapping:

    pass
class qvtimperativecs_Variable:

    pass
class qvtimperativecs_ExpCS:

    pass
class ExpCS:

    pass
class qvtimperativecs_MappingCallBindingCS(ExpCS):

    def __init__(self, isPolled: bool, qvtimperativecs_MappingCallBindingCS: "qvtimperativecs_ExpCS" = None, ownedBindings: "qvtimperativecs_MappingCallCS" = None, qvtimperativecs_MappingCallBindingCS11: "qvtimperativecs_Variable" = None, MappingCallBindingCS: "qvtimperativecs_MappingCallCS" = None):
        self.isPolled = isPolled
        self.qvtimperativecs_MappingCallBindingCS = qvtimperativecs_MappingCallBindingCS
        self.ownedBindings = ownedBindings
        self.qvtimperativecs_MappingCallBindingCS11 = qvtimperativecs_MappingCallBindingCS11
        self.MappingCallBindingCS = MappingCallBindingCS
        
    @property
    def isPolled(self) -> bool:
        return self.__isPolled

    @isPolled.setter
    def isPolled(self, isPolled: bool):
        self.__isPolled = isPolled

    @property
    def ownedBindings(self):
        return self.__ownedBindings

    @ownedBindings.setter
    def ownedBindings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtimperativecs_MappingCallBindingCS__ownedBindings", None)
        self.__ownedBindings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MappingCallCS"):
                opp_val = getattr(old_value, "MappingCallCS", None)
                if opp_val == self:
                    setattr(old_value, "MappingCallCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MappingCallCS"):
                opp_val = getattr(value, "MappingCallCS", None)
                setattr(value, "MappingCallCS", self)

    @property
    def MappingCallBindingCS(self):
        return self.__MappingCallBindingCS

    @MappingCallBindingCS.setter
    def MappingCallBindingCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtimperativecs_MappingCallBindingCS__MappingCallBindingCS", None)
        self.__MappingCallBindingCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningMappingCall"):
                opp_val = getattr(old_value, "owningMappingCall", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningMappingCall"):
                opp_val = getattr(value, "owningMappingCall", None)
                if opp_val is None:
                    setattr(value, "owningMappingCall", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def qvtimperativecs_MappingCallBindingCS11(self):
        return self.__qvtimperativecs_MappingCallBindingCS11

    @qvtimperativecs_MappingCallBindingCS11.setter
    def qvtimperativecs_MappingCallBindingCS11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtimperativecs_MappingCallBindingCS__qvtimperativecs_MappingCallBindingCS11", None)
        self.__qvtimperativecs_MappingCallBindingCS11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qvtimperativecs_Variable"):
                opp_val = getattr(old_value, "qvtimperativecs_Variable", None)
                if opp_val == self:
                    setattr(old_value, "qvtimperativecs_Variable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qvtimperativecs_Variable"):
                opp_val = getattr(value, "qvtimperativecs_Variable", None)
                setattr(value, "qvtimperativecs_Variable", self)

    @property
    def qvtimperativecs_MappingCallBindingCS(self):
        return self.__qvtimperativecs_MappingCallBindingCS

    @qvtimperativecs_MappingCallBindingCS.setter
    def qvtimperativecs_MappingCallBindingCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtimperativecs_MappingCallBindingCS__qvtimperativecs_MappingCallBindingCS", None)
        self.__qvtimperativecs_MappingCallBindingCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qvtimperativecs_ExpCS"):
                opp_val = getattr(old_value, "qvtimperativecs_ExpCS", None)
                if opp_val == self:
                    setattr(old_value, "qvtimperativecs_ExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qvtimperativecs_ExpCS"):
                opp_val = getattr(value, "qvtimperativecs_ExpCS", None)
                setattr(value, "qvtimperativecs_ExpCS", self)

class AbstractMappingCS:

    pass
class qvtimperativecs_MappingCS(AbstractMappingCS):

    pass
class PredicateOrAssignmentCS:

    pass
class MappingStatementCS:

    pass
class qvtimperativecs_MappingCallCS(MappingStatementCS):

    def __init__(self, isInfinite: bool, MappingCallCS: "qvtimperativecs_MappingCallBindingCS" = None, owningMappingCall: set["qvtimperativecs_MappingCallBindingCS"] = None, qvtimperativecs_MappingCallCS: "qvtimperativecs_PathNameCS" = None, qvtimperativecs_MappingCallCS16: "qvtimperativecs_Mapping" = None):
        self.isInfinite = isInfinite
        self.MappingCallCS = MappingCallCS
        self.owningMappingCall = owningMappingCall if owningMappingCall is not None else set()
        self.qvtimperativecs_MappingCallCS = qvtimperativecs_MappingCallCS
        self.qvtimperativecs_MappingCallCS16 = qvtimperativecs_MappingCallCS16
        
    @property
    def isInfinite(self) -> bool:
        return self.__isInfinite

    @isInfinite.setter
    def isInfinite(self, isInfinite: bool):
        self.__isInfinite = isInfinite

    @property
    def qvtimperativecs_MappingCallCS(self):
        return self.__qvtimperativecs_MappingCallCS

    @qvtimperativecs_MappingCallCS.setter
    def qvtimperativecs_MappingCallCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtimperativecs_MappingCallCS__qvtimperativecs_MappingCallCS", None)
        self.__qvtimperativecs_MappingCallCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qvtimperativecs_PathNameCS14"):
                opp_val = getattr(old_value, "qvtimperativecs_PathNameCS14", None)
                if opp_val == self:
                    setattr(old_value, "qvtimperativecs_PathNameCS14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qvtimperativecs_PathNameCS14"):
                opp_val = getattr(value, "qvtimperativecs_PathNameCS14", None)
                setattr(value, "qvtimperativecs_PathNameCS14", self)

    @property
    def owningMappingCall(self):
        return self.__owningMappingCall

    @owningMappingCall.setter
    def owningMappingCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtimperativecs_MappingCallCS__owningMappingCall", None)
        self.__owningMappingCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MappingCallBindingCS"):
                    opp_val = getattr(item, "MappingCallBindingCS", None)
                    
                    if opp_val == self:
                        setattr(item, "MappingCallBindingCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MappingCallBindingCS"):
                    opp_val = getattr(item, "MappingCallBindingCS", None)
                    
                    setattr(item, "MappingCallBindingCS", self)
                    

    @property
    def qvtimperativecs_MappingCallCS16(self):
        return self.__qvtimperativecs_MappingCallCS16

    @qvtimperativecs_MappingCallCS16.setter
    def qvtimperativecs_MappingCallCS16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtimperativecs_MappingCallCS__qvtimperativecs_MappingCallCS16", None)
        self.__qvtimperativecs_MappingCallCS16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qvtimperativecs_Mapping"):
                opp_val = getattr(old_value, "qvtimperativecs_Mapping", None)
                if opp_val == self:
                    setattr(old_value, "qvtimperativecs_Mapping", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qvtimperativecs_Mapping"):
                opp_val = getattr(value, "qvtimperativecs_Mapping", None)
                setattr(value, "qvtimperativecs_Mapping", self)

    @property
    def MappingCallCS(self):
        return self.__MappingCallCS

    @MappingCallCS.setter
    def MappingCallCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtimperativecs_MappingCallCS__MappingCallCS", None)
        self.__MappingCallCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedBindings"):
                opp_val = getattr(old_value, "ownedBindings", None)
                if opp_val == self:
                    setattr(old_value, "ownedBindings", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedBindings"):
                opp_val = getattr(value, "ownedBindings", None)
                setattr(value, "ownedBindings", self)

class qvtimperativecs_MappingSequenceCS(MappingStatementCS):

    pass
class qvtimperativecs_MappingLoopCS(MappingStatementCS):

    pass
class qvtimperativecs_ImperativePredicateOrAssignmentCS(PredicateOrAssignmentCS):

    def __init__(self, isAccumulate: bool):
        self.isAccumulate = isAccumulate
        
    @property
    def isAccumulate(self) -> bool:
        return self.__isAccumulate

    @isAccumulate.setter
    def isAccumulate(self, isAccumulate: bool):
        self.__isAccumulate = isAccumulate

class qvtimperativecs_PathNameCS:

    pass
class DomainCS:

    pass
class qvtimperativecs_ImperativeDomainCS(DomainCS):

    pass