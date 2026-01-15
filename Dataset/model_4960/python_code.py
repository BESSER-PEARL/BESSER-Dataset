from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Direction(Enum):
    Undirected = "Undirected"
    FirstToSecond = "FirstToSecond"
    SecondToFirst = "SecondToFirst"
class Parthood(Enum):
    Unconstrained = "Unconstrained"
    ExclusivePart = "ExclusivePart"
    SharablePart = "SharablePart"
    EssentialPart = "EssentialPart"
    MandatoryPart = "MandatoryPart"
    InseparablePart = "InseparablePart"


############################################
# Definition of Classes
############################################

class IntraRelationshipConstraint:

    pass
class crom_l1_composed_Acyclic(IntraRelationshipConstraint):

    pass
class crom_l1_composed_Total(IntraRelationshipConstraint):

    pass
class crom_l1_composed_Reflexive(IntraRelationshipConstraint):

    pass
class crom_l1_composed_Cyclic(IntraRelationshipConstraint):

    pass
class crom_l1_composed_Irreflexive(IntraRelationshipConstraint):

    pass
class InterRelationshipConstraint:

    pass
class crom_l1_composed_RelationshipExclusion(InterRelationshipConstraint):

    pass
class crom_l1_composed_RelationshipImplication(InterRelationshipConstraint):

    pass
class crom_l1_composed_ParthoodConstraint(IntraRelationshipConstraint):

    def __init__(self, kind: str):
        self.kind = kind
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

class RoleConstraint:

    pass
class crom_l1_composed_RoleProhibition(RoleConstraint):

    pass
class crom_l1_composed_RoleEquivalence(RoleConstraint):

    pass
class crom_l1_composed_RoleImplication(RoleConstraint):

    pass
class crom_l1_composed_RoleGroupElement(ABC):

    pass
class RoleGroupElement:

    pass
class crom_l1_composed_AbstractRoleRef(RoleGroupElement):

    pass
class Inheritance:

    pass
class crom_l1_composed_DataInheritance(Inheritance):

    pass
class RelationshipConstraint:

    pass
class crom_l1_composed_InterRelationshipConstraint(RelationshipConstraint):

    pass
class crom_l1_composed_RoleInheritance(Inheritance):

    pass
class crom_l1_composed_CompartmentInheritance(Inheritance):

    pass
class crom_l1_composed_NaturalInheritance(Inheritance):

    pass
class AbstractRole:

    pass
class AntiRigidType:

    pass
class crom_l1_composed_RoleType(AntiRigidType, AbstractRole):

    pass
class Constraint:

    pass
class crom_l1_composed_RelationshipConstraint(Constraint):

    pass
class crom_l1_composed_ComplexConstraint(Constraint):

    def __init__(self, expression: str, crom_l1_composed_ComplexConstraint: set["crom_l1_composed_AbstractRole"] = None):
        self.expression = expression
        self.crom_l1_composed_ComplexConstraint = crom_l1_composed_ComplexConstraint if crom_l1_composed_ComplexConstraint is not None else set()
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def crom_l1_composed_ComplexConstraint(self):
        return self.__crom_l1_composed_ComplexConstraint

    @crom_l1_composed_ComplexConstraint.setter
    def crom_l1_composed_ComplexConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_ComplexConstraint__crom_l1_composed_ComplexConstraint", None)
        self.__crom_l1_composed_ComplexConstraint = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "crom_l1_composed_AbstractRole53"):
                    opp_val = getattr(item, "crom_l1_composed_AbstractRole53", None)
                    
                    if opp_val == self:
                        setattr(item, "crom_l1_composed_AbstractRole53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "crom_l1_composed_AbstractRole53"):
                    opp_val = getattr(item, "crom_l1_composed_AbstractRole53", None)
                    
                    setattr(item, "crom_l1_composed_AbstractRole53", self)
                    

class crom_l1_composed_RoleConstraint(Constraint):

    pass
class crom_l1_composed_AbstractRole(RoleGroupElement):

    pass
class crom_l1_composed_IntraRelationshipConstraint(RelationshipConstraint):

    pass
class crom_l1_composed_Place:

    def __init__(self, lower: int, upper: int, crom_l1_composed_Place: "crom_l1_composed_Relationship" = None, crom_l1_composed_Place32: "crom_l1_composed_Relationship" = None, crom_l1_composed_Place75: "crom_l1_composed_RoleType" = None):
        self.lower = lower
        self.upper = upper
        self.crom_l1_composed_Place = crom_l1_composed_Place
        self.crom_l1_composed_Place32 = crom_l1_composed_Place32
        self.crom_l1_composed_Place75 = crom_l1_composed_Place75
        
    @property
    def upper(self) -> int:
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper

    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def crom_l1_composed_Place(self):
        return self.__crom_l1_composed_Place

    @crom_l1_composed_Place.setter
    def crom_l1_composed_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_Place__crom_l1_composed_Place", None)
        self.__crom_l1_composed_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "crom_l1_composed_Relationship29"):
                opp_val = getattr(old_value, "crom_l1_composed_Relationship29", None)
                if opp_val == self:
                    setattr(old_value, "crom_l1_composed_Relationship29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "crom_l1_composed_Relationship29"):
                opp_val = getattr(value, "crom_l1_composed_Relationship29", None)
                setattr(value, "crom_l1_composed_Relationship29", self)

    @property
    def crom_l1_composed_Place32(self):
        return self.__crom_l1_composed_Place32

    @crom_l1_composed_Place32.setter
    def crom_l1_composed_Place32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_Place__crom_l1_composed_Place32", None)
        self.__crom_l1_composed_Place32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "crom_l1_composed_Relationship31"):
                opp_val = getattr(old_value, "crom_l1_composed_Relationship31", None)
                if opp_val == self:
                    setattr(old_value, "crom_l1_composed_Relationship31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "crom_l1_composed_Relationship31"):
                opp_val = getattr(value, "crom_l1_composed_Relationship31", None)
                setattr(value, "crom_l1_composed_Relationship31", self)

    @property
    def crom_l1_composed_Place75(self):
        return self.__crom_l1_composed_Place75

    @crom_l1_composed_Place75.setter
    def crom_l1_composed_Place75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_Place__crom_l1_composed_Place75", None)
        self.__crom_l1_composed_Place75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "crom_l1_composed_RoleType76"):
                opp_val = getattr(old_value, "crom_l1_composed_RoleType76", None)
                if opp_val == self:
                    setattr(old_value, "crom_l1_composed_RoleType76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "crom_l1_composed_RoleType76"):
                opp_val = getattr(value, "crom_l1_composed_RoleType76", None)
                setattr(value, "crom_l1_composed_RoleType76", self)

class Relation:

    pass
class crom_l1_composed_Inheritance(Relation):

    pass
class crom_l1_composed_Fulfillment(Relation):

    pass
class crom_l1_composed_Constraint(Relation):

    pass
class RelationTarget:

    pass
class crom_l1_composed_RoleGroup(RelationTarget, AbstractRole):

    def __init__(self, lower: int, upper: int, crom_l1_composed_RoleGroup: set["crom_l1_composed_RoleGroupElement"] = None):
        self.lower = lower
        self.upper = upper
        self.crom_l1_composed_RoleGroup = crom_l1_composed_RoleGroup if crom_l1_composed_RoleGroup is not None else set()
        
    @property
    def upper(self) -> int:
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper

    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def crom_l1_composed_RoleGroup(self):
        return self.__crom_l1_composed_RoleGroup

    @crom_l1_composed_RoleGroup.setter
    def crom_l1_composed_RoleGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_RoleGroup__crom_l1_composed_RoleGroup", None)
        self.__crom_l1_composed_RoleGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "crom_l1_composed_RoleGroupElement"):
                    opp_val = getattr(item, "crom_l1_composed_RoleGroupElement", None)
                    
                    if opp_val == self:
                        setattr(item, "crom_l1_composed_RoleGroupElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "crom_l1_composed_RoleGroupElement"):
                    opp_val = getattr(item, "crom_l1_composed_RoleGroupElement", None)
                    
                    setattr(item, "crom_l1_composed_RoleGroupElement", self)
                    

class crom_l1_composed_Type(RelationTarget):

    pass
class TypedElement:

    pass
class crom_l1_composed_Operation(TypedElement):

    def __init__(self, operation: str, Operation: "crom_l1_composed_Type" = None, crom_l1_composed_Operation: set["crom_l1_composed_Parameter"] = None, operations: "crom_l1_composed_Type" = None):
        self.operation = operation
        self.Operation = Operation
        self.crom_l1_composed_Operation = crom_l1_composed_Operation if crom_l1_composed_Operation is not None else set()
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
        old_value = getattr(self, f"_crom_l1_composed_Operation__Operation", None)
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
    def crom_l1_composed_Operation(self):
        return self.__crom_l1_composed_Operation

    @crom_l1_composed_Operation.setter
    def crom_l1_composed_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_Operation__crom_l1_composed_Operation", None)
        self.__crom_l1_composed_Operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "crom_l1_composed_Parameter"):
                    opp_val = getattr(item, "crom_l1_composed_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "crom_l1_composed_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "crom_l1_composed_Parameter"):
                    opp_val = getattr(item, "crom_l1_composed_Parameter", None)
                    
                    setattr(item, "crom_l1_composed_Parameter", self)
                    

    @property
    def operations(self):
        return self.__operations

    @operations.setter
    def operations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_Operation__operations", None)
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

class crom_l1_composed_Attribute(TypedElement):

    pass
class crom_l1_composed_Parameter(TypedElement):

    pass
class crom_l1_composed_Part:

    def __init__(self, lower: int, upper: int, Part: "crom_l1_composed_CompartmentType" = None, parts: "crom_l1_composed_CompartmentType" = None, crom_l1_composed_Part: "crom_l1_composed_AbstractRole" = None):
        self.lower = lower
        self.upper = upper
        self.Part = Part
        self.parts = parts
        self.crom_l1_composed_Part = crom_l1_composed_Part
        
    @property
    def upper(self) -> int:
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper

    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def crom_l1_composed_Part(self):
        return self.__crom_l1_composed_Part

    @crom_l1_composed_Part.setter
    def crom_l1_composed_Part(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_Part__crom_l1_composed_Part", None)
        self.__crom_l1_composed_Part = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "crom_l1_composed_AbstractRole85"):
                opp_val = getattr(old_value, "crom_l1_composed_AbstractRole85", None)
                if opp_val == self:
                    setattr(old_value, "crom_l1_composed_AbstractRole85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "crom_l1_composed_AbstractRole85"):
                opp_val = getattr(value, "crom_l1_composed_AbstractRole85", None)
                setattr(value, "crom_l1_composed_AbstractRole85", self)

    @property
    def parts(self):
        return self.__parts

    @parts.setter
    def parts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_Part__parts", None)
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
        old_value = getattr(self, f"_crom_l1_composed_Part__Part", None)
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

class RigidType:

    pass
class crom_l1_composed_NaturalType(RigidType):

    pass
class crom_l1_composed_CompartmentType(RigidType):

    pass
class crom_l1_composed_DataType(RigidType):

    def __init__(self, serializable: bool, crom_l1_composed_DataType: "crom_l1_composed_DataType" = None, crom_l1_composed_DataType10: "crom_l1_composed_DataType" = None, crom_l1_composed_DataType55: "crom_l1_composed_DataInheritance" = None, crom_l1_composed_DataType58: "crom_l1_composed_DataInheritance" = None):
        self.serializable = serializable
        self.crom_l1_composed_DataType = crom_l1_composed_DataType
        self.crom_l1_composed_DataType10 = crom_l1_composed_DataType10
        self.crom_l1_composed_DataType55 = crom_l1_composed_DataType55
        self.crom_l1_composed_DataType58 = crom_l1_composed_DataType58
        
    @property
    def serializable(self) -> bool:
        return self.__serializable

    @serializable.setter
    def serializable(self, serializable: bool):
        self.__serializable = serializable

    @property
    def crom_l1_composed_DataType(self):
        return self.__crom_l1_composed_DataType

    @crom_l1_composed_DataType.setter
    def crom_l1_composed_DataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_DataType__crom_l1_composed_DataType", None)
        self.__crom_l1_composed_DataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "crom_l1_composed_DataType10"):
                opp_val = getattr(old_value, "crom_l1_composed_DataType10", None)
                if opp_val == self:
                    setattr(old_value, "crom_l1_composed_DataType10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "crom_l1_composed_DataType10"):
                opp_val = getattr(value, "crom_l1_composed_DataType10", None)
                setattr(value, "crom_l1_composed_DataType10", self)

    @property
    def crom_l1_composed_DataType58(self):
        return self.__crom_l1_composed_DataType58

    @crom_l1_composed_DataType58.setter
    def crom_l1_composed_DataType58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_DataType__crom_l1_composed_DataType58", None)
        self.__crom_l1_composed_DataType58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "crom_l1_composed_DataInheritance57"):
                opp_val = getattr(old_value, "crom_l1_composed_DataInheritance57", None)
                if opp_val == self:
                    setattr(old_value, "crom_l1_composed_DataInheritance57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "crom_l1_composed_DataInheritance57"):
                opp_val = getattr(value, "crom_l1_composed_DataInheritance57", None)
                setattr(value, "crom_l1_composed_DataInheritance57", self)

    @property
    def crom_l1_composed_DataType55(self):
        return self.__crom_l1_composed_DataType55

    @crom_l1_composed_DataType55.setter
    def crom_l1_composed_DataType55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_DataType__crom_l1_composed_DataType55", None)
        self.__crom_l1_composed_DataType55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "crom_l1_composed_DataInheritance"):
                opp_val = getattr(old_value, "crom_l1_composed_DataInheritance", None)
                if opp_val == self:
                    setattr(old_value, "crom_l1_composed_DataInheritance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "crom_l1_composed_DataInheritance"):
                opp_val = getattr(value, "crom_l1_composed_DataInheritance", None)
                setattr(value, "crom_l1_composed_DataInheritance", self)

    @property
    def crom_l1_composed_DataType10(self):
        return self.__crom_l1_composed_DataType10

    @crom_l1_composed_DataType10.setter
    def crom_l1_composed_DataType10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_DataType__crom_l1_composed_DataType10", None)
        self.__crom_l1_composed_DataType10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "crom_l1_composed_DataType"):
                opp_val = getattr(old_value, "crom_l1_composed_DataType", None)
                if opp_val == self:
                    setattr(old_value, "crom_l1_composed_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "crom_l1_composed_DataType"):
                opp_val = getattr(value, "crom_l1_composed_DataType", None)
                setattr(value, "crom_l1_composed_DataType", self)

class crom_l1_composed_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Model:

    pass
class ModelElement:

    pass
class crom_l1_composed_Group(Model, ModelElement):

    pass
class Type:

    pass
class crom_l1_composed_AntiRigidType(Type):

    pass
class crom_l1_composed_RigidType(Type, ModelElement):

    pass
class crom_l1_composed_Relation(ABC):

    def __init__(self, crom_l1_composed_Relation: "crom_l1_composed_Model" = None, crom_l1_composed_Relation78: "crom_l1_composed_RelationTarget" = None, crom_l1_composed_Relation81: "crom_l1_composed_RelationTarget" = None):
        self.crom_l1_composed_Relation = crom_l1_composed_Relation
        self.crom_l1_composed_Relation78 = crom_l1_composed_Relation78
        self.crom_l1_composed_Relation81 = crom_l1_composed_Relation81
        
    @property
    def crom_l1_composed_Relation78(self):
        return self.__crom_l1_composed_Relation78

    @crom_l1_composed_Relation78.setter
    def crom_l1_composed_Relation78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_Relation__crom_l1_composed_Relation78", None)
        self.__crom_l1_composed_Relation78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "crom_l1_composed_RelationTarget"):
                opp_val = getattr(old_value, "crom_l1_composed_RelationTarget", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "crom_l1_composed_RelationTarget"):
                opp_val = getattr(value, "crom_l1_composed_RelationTarget", None)
                if opp_val is None:
                    setattr(value, "crom_l1_composed_RelationTarget", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def crom_l1_composed_Relation81(self):
        return self.__crom_l1_composed_Relation81

    @crom_l1_composed_Relation81.setter
    def crom_l1_composed_Relation81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_Relation__crom_l1_composed_Relation81", None)
        self.__crom_l1_composed_Relation81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "crom_l1_composed_RelationTarget80"):
                opp_val = getattr(old_value, "crom_l1_composed_RelationTarget80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "crom_l1_composed_RelationTarget80"):
                opp_val = getattr(value, "crom_l1_composed_RelationTarget80", None)
                if opp_val is None:
                    setattr(value, "crom_l1_composed_RelationTarget80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def crom_l1_composed_Relation(self):
        return self.__crom_l1_composed_Relation

    @crom_l1_composed_Relation.setter
    def crom_l1_composed_Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_Relation__crom_l1_composed_Relation", None)
        self.__crom_l1_composed_Relation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "crom_l1_composed_Model2"):
                opp_val = getattr(old_value, "crom_l1_composed_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "crom_l1_composed_Model2"):
                opp_val = getattr(value, "crom_l1_composed_Model2", None)
                if opp_val is None:
                    setattr(value, "crom_l1_composed_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getSource(self) -> str:
        # TODO: Implement getSource method
        pass

    def getTarget(self) -> str:
        # TODO: Implement getTarget method
        pass

class crom_l1_composed_Model:

    pass
class NamedElement:

    pass
class crom_l1_composed_TypedElement(NamedElement):

    pass
class crom_l1_composed_Relationship(NamedElement, Relation):

    def __init__(self, direction: str, crom_l1_composed_Relationship29: "crom_l1_composed_Place" = None, crom_l1_composed_Relationship31: "crom_l1_composed_Place" = None, crom_l1_composed_Relationship34: set["crom_l1_composed_IntraRelationshipConstraint"] = None, crom_l1_composed_Relationship: "crom_l1_composed_CompartmentType" = None, crom_l1_composed_Relationship46: "crom_l1_composed_IntraRelationshipConstraint" = None, crom_l1_composed_Relationship48: "crom_l1_composed_InterRelationshipConstraint" = None, crom_l1_composed_Relationship51: "crom_l1_composed_InterRelationshipConstraint" = None):
        self.direction = direction
        self.crom_l1_composed_Relationship29 = crom_l1_composed_Relationship29
        self.crom_l1_composed_Relationship31 = crom_l1_composed_Relationship31
        self.crom_l1_composed_Relationship34 = crom_l1_composed_Relationship34 if crom_l1_composed_Relationship34 is not None else set()
        self.crom_l1_composed_Relationship = crom_l1_composed_Relationship
        self.crom_l1_composed_Relationship46 = crom_l1_composed_Relationship46
        self.crom_l1_composed_Relationship48 = crom_l1_composed_Relationship48
        self.crom_l1_composed_Relationship51 = crom_l1_composed_Relationship51
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def crom_l1_composed_Relationship51(self):
        return self.__crom_l1_composed_Relationship51

    @crom_l1_composed_Relationship51.setter
    def crom_l1_composed_Relationship51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_Relationship__crom_l1_composed_Relationship51", None)
        self.__crom_l1_composed_Relationship51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "crom_l1_composed_InterRelationshipConstraint50"):
                opp_val = getattr(old_value, "crom_l1_composed_InterRelationshipConstraint50", None)
                if opp_val == self:
                    setattr(old_value, "crom_l1_composed_InterRelationshipConstraint50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "crom_l1_composed_InterRelationshipConstraint50"):
                opp_val = getattr(value, "crom_l1_composed_InterRelationshipConstraint50", None)
                setattr(value, "crom_l1_composed_InterRelationshipConstraint50", self)

    @property
    def crom_l1_composed_Relationship46(self):
        return self.__crom_l1_composed_Relationship46

    @crom_l1_composed_Relationship46.setter
    def crom_l1_composed_Relationship46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_Relationship__crom_l1_composed_Relationship46", None)
        self.__crom_l1_composed_Relationship46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "crom_l1_composed_IntraRelationshipConstraint45"):
                opp_val = getattr(old_value, "crom_l1_composed_IntraRelationshipConstraint45", None)
                if opp_val == self:
                    setattr(old_value, "crom_l1_composed_IntraRelationshipConstraint45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "crom_l1_composed_IntraRelationshipConstraint45"):
                opp_val = getattr(value, "crom_l1_composed_IntraRelationshipConstraint45", None)
                setattr(value, "crom_l1_composed_IntraRelationshipConstraint45", self)

    @property
    def crom_l1_composed_Relationship34(self):
        return self.__crom_l1_composed_Relationship34

    @crom_l1_composed_Relationship34.setter
    def crom_l1_composed_Relationship34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_Relationship__crom_l1_composed_Relationship34", None)
        self.__crom_l1_composed_Relationship34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "crom_l1_composed_IntraRelationshipConstraint"):
                    opp_val = getattr(item, "crom_l1_composed_IntraRelationshipConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "crom_l1_composed_IntraRelationshipConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "crom_l1_composed_IntraRelationshipConstraint"):
                    opp_val = getattr(item, "crom_l1_composed_IntraRelationshipConstraint", None)
                    
                    setattr(item, "crom_l1_composed_IntraRelationshipConstraint", self)
                    

    @property
    def crom_l1_composed_Relationship(self):
        return self.__crom_l1_composed_Relationship

    @crom_l1_composed_Relationship.setter
    def crom_l1_composed_Relationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_Relationship__crom_l1_composed_Relationship", None)
        self.__crom_l1_composed_Relationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "crom_l1_composed_CompartmentType"):
                opp_val = getattr(old_value, "crom_l1_composed_CompartmentType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "crom_l1_composed_CompartmentType"):
                opp_val = getattr(value, "crom_l1_composed_CompartmentType", None)
                if opp_val is None:
                    setattr(value, "crom_l1_composed_CompartmentType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def crom_l1_composed_Relationship29(self):
        return self.__crom_l1_composed_Relationship29

    @crom_l1_composed_Relationship29.setter
    def crom_l1_composed_Relationship29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_Relationship__crom_l1_composed_Relationship29", None)
        self.__crom_l1_composed_Relationship29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "crom_l1_composed_Place"):
                opp_val = getattr(old_value, "crom_l1_composed_Place", None)
                if opp_val == self:
                    setattr(old_value, "crom_l1_composed_Place", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "crom_l1_composed_Place"):
                opp_val = getattr(value, "crom_l1_composed_Place", None)
                setattr(value, "crom_l1_composed_Place", self)

    @property
    def crom_l1_composed_Relationship48(self):
        return self.__crom_l1_composed_Relationship48

    @crom_l1_composed_Relationship48.setter
    def crom_l1_composed_Relationship48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_Relationship__crom_l1_composed_Relationship48", None)
        self.__crom_l1_composed_Relationship48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "crom_l1_composed_InterRelationshipConstraint"):
                opp_val = getattr(old_value, "crom_l1_composed_InterRelationshipConstraint", None)
                if opp_val == self:
                    setattr(old_value, "crom_l1_composed_InterRelationshipConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "crom_l1_composed_InterRelationshipConstraint"):
                opp_val = getattr(value, "crom_l1_composed_InterRelationshipConstraint", None)
                setattr(value, "crom_l1_composed_InterRelationshipConstraint", self)

    @property
    def crom_l1_composed_Relationship31(self):
        return self.__crom_l1_composed_Relationship31

    @crom_l1_composed_Relationship31.setter
    def crom_l1_composed_Relationship31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_Relationship__crom_l1_composed_Relationship31", None)
        self.__crom_l1_composed_Relationship31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "crom_l1_composed_Place32"):
                opp_val = getattr(old_value, "crom_l1_composed_Place32", None)
                if opp_val == self:
                    setattr(old_value, "crom_l1_composed_Place32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "crom_l1_composed_Place32"):
                opp_val = getattr(value, "crom_l1_composed_Place32", None)
                setattr(value, "crom_l1_composed_Place32", self)

class crom_l1_composed_RelationTarget(NamedElement):

    pass
class crom_l1_composed_ModelElement(NamedElement):

    pass