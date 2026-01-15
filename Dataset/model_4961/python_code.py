from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class crom_l1_Part:

    pass
class Inheritance:

    pass
class crom_l1_NaturalInheritance(Inheritance):

    pass
class crom_l1_Player(ABC):

    pass
class crom_l1_AbstractRole(ABC):

    pass
class Relation:

    pass
class crom_l1_Inheritance(Relation):

    pass
class crom_l1_Fulfillment(Relation):

    pass
class TypedElement:

    pass
class crom_l1_Operation(TypedElement):

    def __init__(self, operation: str, Operation: "crom_l1_Type" = None, crom_l1_Operation: set["crom_l1_Parameter"] = None, operations: "crom_l1_Type" = None):
        self.operation = operation
        self.Operation = Operation
        self.crom_l1_Operation = crom_l1_Operation if crom_l1_Operation is not None else set()
        self.operations = operations
        
    @property
    def operation(self) -> str:
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation

    @property
    def Operation(self):
        return self.__Operation

    @Operation.setter
    def Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_Operation__Operation", None)
        self.__Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner9"):
                opp_val = getattr(old_value, "owner9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner9"):
                opp_val = getattr(value, "owner9", None)
                if opp_val is None:
                    setattr(value, "owner9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def crom_l1_Operation(self):
        return self.__crom_l1_Operation

    @crom_l1_Operation.setter
    def crom_l1_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_Operation__crom_l1_Operation", None)
        self.__crom_l1_Operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "crom_l1_Parameter"):
                    opp_val = getattr(item, "crom_l1_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "crom_l1_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "crom_l1_Parameter"):
                    opp_val = getattr(item, "crom_l1_Parameter", None)
                    
                    setattr(item, "crom_l1_Parameter", self)
                    

    @property
    def operations(self):
        return self.__operations

    @operations.setter
    def operations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_Operation__operations", None)
        self.__operations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Type"):
                opp_val = getattr(old_value, "Type", None)
                if opp_val == self:
                    setattr(old_value, "Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Type"):
                opp_val = getattr(value, "Type", None)
                setattr(value, "Type", self)

class crom_l1_Parameter(TypedElement):

    pass
class Model:

    pass
class ModelElement:

    pass
class crom_l1_Group(ModelElement, Model):

    pass
class Type:

    pass
class crom_l1_RigidType(Type, ModelElement):

    pass
class crom_l1_Model:

    pass
class crom_l1_Relation(ABC):

    pass
class NamedElement:

    pass
class crom_l1_RelationTarget(NamedElement):

    pass
class crom_l1_TypedElement(NamedElement):

    pass
class crom_l1_ModelElement(NamedElement):

    pass
class crom_l1_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class AbstractRole:

    pass
class Player:

    pass
class RigidType:

    pass
class crom_l1_NaturalType(Player, RigidType):

    pass
class RelationTarget:

    pass
class crom_l1_RoleType(Player, AbstractRole, RelationTarget):

    pass
class crom_l1_Type(RelationTarget):

    pass
class crom_l1_CompartmentType(Player, ModelElement, RelationTarget):

    pass
class crom_l1_Attribute(TypedElement):

    pass