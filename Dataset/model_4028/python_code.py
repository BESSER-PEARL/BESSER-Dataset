from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ScopeKind(Enum):
    instance = "instance"
    classifier = "classifier"


############################################
# Definition of Classes
############################################

class uml_15_to_20_associationEndToProperty_AssociationEnd:

    def __init__(self, isNavigable: bool, connections: "uml_15_to_20_associationEndToProperty_Association" = None, AssociationEnd: "uml_15_to_20_associationEndToProperty_Class" = None, AssociationEnd7: "uml_15_to_20_associationEndToProperty_Association" = None, associations: "uml_15_to_20_associationEndToProperty_Class" = None):
        self.isNavigable = isNavigable
        self.connections = connections
        self.AssociationEnd = AssociationEnd
        self.AssociationEnd7 = AssociationEnd7
        self.associations = associations
        
    @property
    def isNavigable(self) -> bool:
        return self.__isNavigable

    @isNavigable.setter
    def isNavigable(self, isNavigable: bool):
        self.__isNavigable = isNavigable

    @property
    def connections(self):
        return self.__connections

    @connections.setter
    def connections(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_15_to_20_associationEndToProperty_AssociationEnd__connections", None)
        self.__connections = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Association"):
                opp_val = getattr(old_value, "Association", None)
                if opp_val == self:
                    setattr(old_value, "Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Association"):
                opp_val = getattr(value, "Association", None)
                setattr(value, "Association", self)

    @property
    def AssociationEnd(self):
        return self.__AssociationEnd

    @AssociationEnd.setter
    def AssociationEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_15_to_20_associationEndToProperty_AssociationEnd__AssociationEnd", None)
        self.__AssociationEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "participant"):
                opp_val = getattr(old_value, "participant", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "participant"):
                opp_val = getattr(value, "participant", None)
                if opp_val is None:
                    setattr(value, "participant", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def associations(self):
        return self.__associations

    @associations.setter
    def associations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_15_to_20_associationEndToProperty_AssociationEnd__associations", None)
        self.__associations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class"):
                opp_val = getattr(old_value, "Class", None)
                if opp_val == self:
                    setattr(old_value, "Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class"):
                opp_val = getattr(value, "Class", None)
                setattr(value, "Class", self)

    @property
    def AssociationEnd7(self):
        return self.__AssociationEnd7

    @AssociationEnd7.setter
    def AssociationEnd7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_15_to_20_associationEndToProperty_AssociationEnd__AssociationEnd7", None)
        self.__AssociationEnd7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "association"):
                opp_val = getattr(old_value, "association", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "association"):
                opp_val = getattr(value, "association", None)
                if opp_val is None:
                    setattr(value, "association", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml_15_to_20_associationEndToProperty_StructuralFeature(ABC):

    def __init__(self, ownerScope: str, targetScope: str, uml_15_to_20_associationEndToProperty_StructuralFeature: "uml_15_to_20_associationEndToProperty_Class" = None):
        self.ownerScope = ownerScope
        self.targetScope = targetScope
        self.uml_15_to_20_associationEndToProperty_StructuralFeature = uml_15_to_20_associationEndToProperty_StructuralFeature
        
    @property
    def targetScope(self) -> str:
        return self.__targetScope

    @targetScope.setter
    def targetScope(self, targetScope: str):
        self.__targetScope = targetScope

    @property
    def ownerScope(self) -> str:
        return self.__ownerScope

    @ownerScope.setter
    def ownerScope(self, ownerScope: str):
        self.__ownerScope = ownerScope

    @property
    def uml_15_to_20_associationEndToProperty_StructuralFeature(self):
        return self.__uml_15_to_20_associationEndToProperty_StructuralFeature

    @uml_15_to_20_associationEndToProperty_StructuralFeature.setter
    def uml_15_to_20_associationEndToProperty_StructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_15_to_20_associationEndToProperty_StructuralFeature__uml_15_to_20_associationEndToProperty_StructuralFeature", None)
        self.__uml_15_to_20_associationEndToProperty_StructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_15_to_20_associationEndToProperty_Class4"):
                opp_val = getattr(old_value, "uml_15_to_20_associationEndToProperty_Class4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_15_to_20_associationEndToProperty_Class4"):
                opp_val = getattr(value, "uml_15_to_20_associationEndToProperty_Class4", None)
                if opp_val is None:
                    setattr(value, "uml_15_to_20_associationEndToProperty_Class4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml_15_to_20_associationEndToProperty_Association:

    pass
class uml_15_to_20_associationEndToProperty_Class:

    pass
class uml_15_to_20_associationEndToProperty_Model:

    pass
class StructuralFeature:

    pass
class uml_15_to_20_associationEndToProperty_Operation(StructuralFeature):

    pass
class uml_15_to_20_associationEndToProperty_Attribute(StructuralFeature):

    pass