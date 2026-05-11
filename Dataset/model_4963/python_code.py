from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class RoleConstraint:

    pass
class crom_l1_RoleEquivalence(RoleConstraint):

    pass
class crom_l1_RoleImplication(RoleConstraint):

    pass
class Constraint:

    pass
class crom_l1_Test(Constraint):

    pass
class crom_l1_RoleConstraint(Constraint):

    pass
class crom_l1_Part:

    def __init__(self, lower: int, upper: int, crom_l1_Part: "crom_l1_AbstractRole" = None, parts: "crom_l1_CompartmentType" = None, Part: "crom_l1_CompartmentType" = None):
        self.lower = lower
        self.upper = upper
        self.crom_l1_Part = crom_l1_Part
        self.parts = parts
        self.Part = Part
        
        pass
    @property
    def upper(self):
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper


    @property
    def lower(self):
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower


    @property
    def crom_l1_Part(self):
        return self.__crom_l1_Part

    @crom_l1_Part.setter
    def crom_l1_Part(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_Part__crom_l1_Part", None)
        self.__crom_l1_Part = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "crom_l1_AbstractRole27"):
                opp_val = getattr(old_value, "crom_l1_AbstractRole27", None)
                if opp_val == self:
                    setattr(old_value, "crom_l1_AbstractRole27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "crom_l1_AbstractRole27"):
                opp_val = getattr(value, "crom_l1_AbstractRole27", None)
                setattr(value, "crom_l1_AbstractRole27", self)

    @property
    def parts(self):
        return self.__parts

    @parts.setter
    def parts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_Part__parts", None)
        self.__parts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompartmentType"):
                opp_val = getattr(old_value, "CompartmentType", None)
                if opp_val == self:
                    setattr(old_value, "CompartmentType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompartmentType"):
                opp_val = getattr(value, "CompartmentType", None)
                setattr(value, "CompartmentType", self)

    @property
    def Part(self):
        return self.__Part

    @Part.setter
    def Part(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_Part__Part", None)
        self.__Part = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whole"):
                opp_val = getattr(old_value, "whole", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whole"):
                opp_val = getattr(value, "whole", None)
                if opp_val is None:
                    setattr(value, "whole", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class crom_l1_RoleProhibition(RoleConstraint):

    pass
class crom_l1_Constraint:

    pass
class RoleGroupElement:

    pass
class Inheritance:

    pass
class crom_l1_CompartmentInheritance(Inheritance):

    pass
class crom_l1_DataInheritance(Inheritance):

    pass
class crom_l1_NaturalInheritance(Inheritance):

    pass
class crom_l1_Player(ABC):

    pass
class crom_l1_AbstractRole(RoleGroupElement):

    pass
class Relation:

    pass
class crom_l1_Inheritance(Relation):

    pass
class crom_l1_Fulfillment(Relation):

    pass
class AntiRigidType:

    pass
class AbstractRole:

    pass
class Player:

    pass
class RigidType:

    pass
class crom_l1_CompartmentType(Player, RigidType):

    pass
class crom_l1_DataType(RigidType):

    pass
class crom_l1_NaturalType(Player, RigidType):

    pass
class crom_l1_AbstractRoleRef(RoleGroupElement):

    pass
class crom_l1_RoleGroupElement(ABC):

    pass
class TypedElement:

    pass
class crom_l1_Operation(TypedElement):

    def __init__(self, operation: str, operations: "crom_l1_Type" = None, crom_l1_Operation: set["crom_l1_Parameter"] = None, Operation: "crom_l1_Type" = None):
        self.operation = operation
        self.operations = operations
        self.crom_l1_Operation = crom_l1_Operation if crom_l1_Operation is not None else set()
        self.Operation = Operation
        
        pass
    @property
    def operation(self):
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation


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
class crom_l1_AntiRigidType(Type):

    pass
class crom_l1_RigidType(ModelElement, Type):

    pass
class crom_l1_Relation(ABC):

    pass
class crom_l1_Model:

    pass
class NamedElement:

    pass
class crom_l1_TypedElement(NamedElement):

    pass
class crom_l1_RelationTarget(NamedElement):

    pass
class crom_l1_ModelElement(NamedElement):

    pass
class crom_l1_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class RelationTarget:

    pass
class crom_l1_RoleType(AntiRigidType, RelationTarget, AbstractRole):

    pass
class crom_l1_Type(RelationTarget):

    pass
class crom_l1_RoleGroup(RelationTarget, AbstractRole):

    def __init__(self, upper: int, lower: int, crom_l1_RoleGroup: set["crom_l1_RoleGroupElement"] = None):
        self.upper = upper
        self.lower = lower
        self.crom_l1_RoleGroup = crom_l1_RoleGroup if crom_l1_RoleGroup is not None else set()
        
        pass
    @property
    def upper(self):
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper


    @property
    def lower(self):
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower


    @property
    def crom_l1_RoleGroup(self):
        return self.__crom_l1_RoleGroup

    @crom_l1_RoleGroup.setter
    def crom_l1_RoleGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_RoleGroup__crom_l1_RoleGroup", None)
        self.__crom_l1_RoleGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "crom_l1_RoleGroupElement"):
                    opp_val = getattr(item, "crom_l1_RoleGroupElement", None)
                    
                    if opp_val == self:
                        setattr(item, "crom_l1_RoleGroupElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "crom_l1_RoleGroupElement"):
                    opp_val = getattr(item, "crom_l1_RoleGroupElement", None)
                    
                    setattr(item, "crom_l1_RoleGroupElement", self)
                    

class crom_l1_Attribute(TypedElement):

    pass