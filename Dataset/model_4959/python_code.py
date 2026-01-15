from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Parthood(Enum):
    Unconstrained = "Unconstrained"
    ExclusivePart = "ExclusivePart"
    SharablePart = "SharablePart"
    EssentialPart = "EssentialPart"
    MandatoryPart = "MandatoryPart"
    InseparablePart = "InseparablePart"
class Direction(Enum):
    Undirected = "Undirected"
    FirstToSecond = "FirstToSecond"
    SecondToFirst = "SecondToFirst"


############################################
# Definition of Classes
############################################

class crom_l1_composed_RoleGroupElement(ABC):

    pass
class RoleGroupElement:

    pass
class crom_l1_composed_AbstractRoleRef(RoleGroupElement):

    pass
class IntraRelationshipConstraint:

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

class crom_l1_composed_Total(IntraRelationshipConstraint):

    pass
class crom_l1_composed_Cyclic(IntraRelationshipConstraint):

    pass
class crom_l1_composed_Irreflexive(IntraRelationshipConstraint):

    pass
class InterRelationshipConstraint:

    pass
class crom_l1_composed_RelationshipImplication(InterRelationshipConstraint):

    pass
class RoleConstraint:

    pass
class crom_l1_composed_RoleImplication(RoleConstraint):

    pass
class crom_l1_composed_RoleEquivalence(RoleConstraint):

    pass
class crom_l1_composed_RoleProhibition(RoleConstraint):

    pass
class Inheritance:

    pass
class crom_l1_composed_RoleInheritance(Inheritance):

    pass
class crom_l1_composed_NaturalInheritance(Inheritance):

    pass
class crom_l1_composed_CompartmentInheritance(Inheritance):

    pass
class crom_l1_composed_DataInheritance(Inheritance):

    pass
class RelationshipConstraint:

    pass
class crom_l1_composed_InterRelationshipConstraint(RelationshipConstraint):

    pass
class Constraint:

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
                if hasattr(item, "crom_l1_composed_AbstractRole47"):
                    opp_val = getattr(item, "crom_l1_composed_AbstractRole47", None)
                    
                    if opp_val == self:
                        setattr(item, "crom_l1_composed_AbstractRole47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "crom_l1_composed_AbstractRole47"):
                    opp_val = getattr(item, "crom_l1_composed_AbstractRole47", None)
                    
                    setattr(item, "crom_l1_composed_AbstractRole47", self)
                    

class crom_l1_composed_RoleConstraint(Constraint):

    pass
class crom_l1_composed_AbstractRole(RoleGroupElement):

    pass
class crom_l1_composed_IntraRelationshipConstraint(RelationshipConstraint):

    pass
class crom_l1_composed_Place:

    def __init__(self, lower: int, upper: int, crom_l1_composed_Place: "crom_l1_composed_Relationship" = None, crom_l1_composed_Place27: "crom_l1_composed_Relationship" = None, crom_l1_composed_Place69: "crom_l1_composed_RoleType" = None):
        self.lower = lower
        self.upper = upper
        self.crom_l1_composed_Place = crom_l1_composed_Place
        self.crom_l1_composed_Place27 = crom_l1_composed_Place27
        self.crom_l1_composed_Place69 = crom_l1_composed_Place69
        
    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def upper(self) -> int:
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper

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
            if hasattr(old_value, "crom_l1_composed_Relationship24"):
                opp_val = getattr(old_value, "crom_l1_composed_Relationship24", None)
                if opp_val == self:
                    setattr(old_value, "crom_l1_composed_Relationship24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "crom_l1_composed_Relationship24"):
                opp_val = getattr(value, "crom_l1_composed_Relationship24", None)
                setattr(value, "crom_l1_composed_Relationship24", self)

    @property
    def crom_l1_composed_Place69(self):
        return self.__crom_l1_composed_Place69

    @crom_l1_composed_Place69.setter
    def crom_l1_composed_Place69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_Place__crom_l1_composed_Place69", None)
        self.__crom_l1_composed_Place69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "crom_l1_composed_RoleType70"):
                opp_val = getattr(old_value, "crom_l1_composed_RoleType70", None)
                if opp_val == self:
                    setattr(old_value, "crom_l1_composed_RoleType70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "crom_l1_composed_RoleType70"):
                opp_val = getattr(value, "crom_l1_composed_RoleType70", None)
                setattr(value, "crom_l1_composed_RoleType70", self)

    @property
    def crom_l1_composed_Place27(self):
        return self.__crom_l1_composed_Place27

    @crom_l1_composed_Place27.setter
    def crom_l1_composed_Place27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_Place__crom_l1_composed_Place27", None)
        self.__crom_l1_composed_Place27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "crom_l1_composed_Relationship26"):
                opp_val = getattr(old_value, "crom_l1_composed_Relationship26", None)
                if opp_val == self:
                    setattr(old_value, "crom_l1_composed_Relationship26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "crom_l1_composed_Relationship26"):
                opp_val = getattr(value, "crom_l1_composed_Relationship26", None)
                setattr(value, "crom_l1_composed_Relationship26", self)

class Relation:

    pass
class crom_l1_composed_Fulfillment(Relation):

    pass
class crom_l1_composed_Inheritance(Relation):

    pass
class AbstractRole:

    pass
class AntiRigidType:

    pass
class crom_l1_composed_RoleType(AbstractRole, AntiRigidType):

    pass
class crom_l1_composed_Constraint(Relation):

    pass
class crom_l1_composed_RelationshipConstraint(Constraint):

    pass
class RigidType:

    pass
class crom_l1_composed_DataType(RigidType):

    def __init__(self, serializable: bool, crom_l1_composed_DataType: "crom_l1_composed_DataType" = None, crom_l1_composed_DataType10: "crom_l1_composed_DataType" = None, crom_l1_composed_DataType49: "crom_l1_composed_DataInheritance" = None, crom_l1_composed_DataType52: "crom_l1_composed_DataInheritance" = None):
        self.serializable = serializable
        self.crom_l1_composed_DataType = crom_l1_composed_DataType
        self.crom_l1_composed_DataType10 = crom_l1_composed_DataType10
        self.crom_l1_composed_DataType49 = crom_l1_composed_DataType49
        self.crom_l1_composed_DataType52 = crom_l1_composed_DataType52
        
    @property
    def serializable(self) -> bool:
        return self.__serializable

    @serializable.setter
    def serializable(self, serializable: bool):
        self.__serializable = serializable

    @property
    def crom_l1_composed_DataType49(self):
        return self.__crom_l1_composed_DataType49

    @crom_l1_composed_DataType49.setter
    def crom_l1_composed_DataType49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_DataType__crom_l1_composed_DataType49", None)
        self.__crom_l1_composed_DataType49 = value
        
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
    def crom_l1_composed_DataType52(self):
        return self.__crom_l1_composed_DataType52

    @crom_l1_composed_DataType52.setter
    def crom_l1_composed_DataType52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_DataType__crom_l1_composed_DataType52", None)
        self.__crom_l1_composed_DataType52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "crom_l1_composed_DataInheritance51"):
                opp_val = getattr(old_value, "crom_l1_composed_DataInheritance51", None)
                if opp_val == self:
                    setattr(old_value, "crom_l1_composed_DataInheritance51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "crom_l1_composed_DataInheritance51"):
                opp_val = getattr(value, "crom_l1_composed_DataInheritance51", None)
                setattr(value, "crom_l1_composed_DataInheritance51", self)

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

class RelationTarget:

    pass
class crom_l1_composed_RoleGroup(AbstractRole, RelationTarget):

    def __init__(self, lower: int, upper: int, crom_l1_composed_RoleGroup: set["crom_l1_composed_RoleGroupElement"] = None):
        self.lower = lower
        self.upper = upper
        self.crom_l1_composed_RoleGroup = crom_l1_composed_RoleGroup if crom_l1_composed_RoleGroup is not None else set()
        
    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def upper(self) -> int:
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper

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
class crom_l1_composed_Attribute(TypedElement):

    pass
class crom_l1_composed_Operation(TypedElement):

    def __init__(self, operation: str, crom_l1_composed_Operation: set["crom_l1_composed_Parameter"] = None, operations: "crom_l1_composed_Type" = None, Operation: "crom_l1_composed_Type" = None):
        self.operation = operation
        self.crom_l1_composed_Operation = crom_l1_composed_Operation if crom_l1_composed_Operation is not None else set()
        self.operations = operations
        self.Operation = Operation
        
    @property
    def operation(self) -> str:
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation

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

class crom_l1_composed_Parameter(TypedElement):

    pass
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
class crom_l1_composed_RigidType(ModelElement, Type):

    pass
class crom_l1_composed_Relation(ABC):

    def __init__(self, crom_l1_composed_Relation: "crom_l1_composed_Model" = None, crom_l1_composed_Relation72: "crom_l1_composed_RelationTarget" = None, crom_l1_composed_Relation75: "crom_l1_composed_RelationTarget" = None):
        self.crom_l1_composed_Relation = crom_l1_composed_Relation
        self.crom_l1_composed_Relation72 = crom_l1_composed_Relation72
        self.crom_l1_composed_Relation75 = crom_l1_composed_Relation75
        
    @property
    def crom_l1_composed_Relation72(self):
        return self.__crom_l1_composed_Relation72

    @crom_l1_composed_Relation72.setter
    def crom_l1_composed_Relation72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_Relation__crom_l1_composed_Relation72", None)
        self.__crom_l1_composed_Relation72 = value
        
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
    def crom_l1_composed_Relation75(self):
        return self.__crom_l1_composed_Relation75

    @crom_l1_composed_Relation75.setter
    def crom_l1_composed_Relation75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_Relation__crom_l1_composed_Relation75", None)
        self.__crom_l1_composed_Relation75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "crom_l1_composed_RelationTarget74"):
                opp_val = getattr(old_value, "crom_l1_composed_RelationTarget74", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "crom_l1_composed_RelationTarget74"):
                opp_val = getattr(value, "crom_l1_composed_RelationTarget74", None)
                if opp_val is None:
                    setattr(value, "crom_l1_composed_RelationTarget74", set([self]))
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

    def getTarget(self) -> str:
        # TODO: Implement getTarget method
        pass

    def getSource(self) -> str:
        # TODO: Implement getSource method
        pass

class crom_l1_composed_Model:

    pass
class NamedElement:

    pass
class crom_l1_composed_Relationship(NamedElement, Relation):

    def __init__(self, direction: str, crom_l1_composed_Relationship: "crom_l1_composed_CompartmentType" = None, crom_l1_composed_Relationship24: "crom_l1_composed_Place" = None, crom_l1_composed_Relationship26: "crom_l1_composed_Place" = None, crom_l1_composed_Relationship29: set["crom_l1_composed_IntraRelationshipConstraint"] = None, crom_l1_composed_Relationship40: "crom_l1_composed_IntraRelationshipConstraint" = None, crom_l1_composed_Relationship42: "crom_l1_composed_InterRelationshipConstraint" = None, crom_l1_composed_Relationship45: "crom_l1_composed_InterRelationshipConstraint" = None):
        self.direction = direction
        self.crom_l1_composed_Relationship = crom_l1_composed_Relationship
        self.crom_l1_composed_Relationship24 = crom_l1_composed_Relationship24
        self.crom_l1_composed_Relationship26 = crom_l1_composed_Relationship26
        self.crom_l1_composed_Relationship29 = crom_l1_composed_Relationship29 if crom_l1_composed_Relationship29 is not None else set()
        self.crom_l1_composed_Relationship40 = crom_l1_composed_Relationship40
        self.crom_l1_composed_Relationship42 = crom_l1_composed_Relationship42
        self.crom_l1_composed_Relationship45 = crom_l1_composed_Relationship45
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

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
        self.__crom_l1_composed_Relationship29 = value if value is not None else set()
        
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
    def crom_l1_composed_Relationship45(self):
        return self.__crom_l1_composed_Relationship45

    @crom_l1_composed_Relationship45.setter
    def crom_l1_composed_Relationship45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_Relationship__crom_l1_composed_Relationship45", None)
        self.__crom_l1_composed_Relationship45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "crom_l1_composed_InterRelationshipConstraint44"):
                opp_val = getattr(old_value, "crom_l1_composed_InterRelationshipConstraint44", None)
                if opp_val == self:
                    setattr(old_value, "crom_l1_composed_InterRelationshipConstraint44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "crom_l1_composed_InterRelationshipConstraint44"):
                opp_val = getattr(value, "crom_l1_composed_InterRelationshipConstraint44", None)
                setattr(value, "crom_l1_composed_InterRelationshipConstraint44", self)

    @property
    def crom_l1_composed_Relationship26(self):
        return self.__crom_l1_composed_Relationship26

    @crom_l1_composed_Relationship26.setter
    def crom_l1_composed_Relationship26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_Relationship__crom_l1_composed_Relationship26", None)
        self.__crom_l1_composed_Relationship26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "crom_l1_composed_Place27"):
                opp_val = getattr(old_value, "crom_l1_composed_Place27", None)
                if opp_val == self:
                    setattr(old_value, "crom_l1_composed_Place27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "crom_l1_composed_Place27"):
                opp_val = getattr(value, "crom_l1_composed_Place27", None)
                setattr(value, "crom_l1_composed_Place27", self)

    @property
    def crom_l1_composed_Relationship42(self):
        return self.__crom_l1_composed_Relationship42

    @crom_l1_composed_Relationship42.setter
    def crom_l1_composed_Relationship42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_Relationship__crom_l1_composed_Relationship42", None)
        self.__crom_l1_composed_Relationship42 = value
        
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
    def crom_l1_composed_Relationship24(self):
        return self.__crom_l1_composed_Relationship24

    @crom_l1_composed_Relationship24.setter
    def crom_l1_composed_Relationship24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_Relationship__crom_l1_composed_Relationship24", None)
        self.__crom_l1_composed_Relationship24 = value
        
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
    def crom_l1_composed_Relationship40(self):
        return self.__crom_l1_composed_Relationship40

    @crom_l1_composed_Relationship40.setter
    def crom_l1_composed_Relationship40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_crom_l1_composed_Relationship__crom_l1_composed_Relationship40", None)
        self.__crom_l1_composed_Relationship40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "crom_l1_composed_IntraRelationshipConstraint39"):
                opp_val = getattr(old_value, "crom_l1_composed_IntraRelationshipConstraint39", None)
                if opp_val == self:
                    setattr(old_value, "crom_l1_composed_IntraRelationshipConstraint39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "crom_l1_composed_IntraRelationshipConstraint39"):
                opp_val = getattr(value, "crom_l1_composed_IntraRelationshipConstraint39", None)
                setattr(value, "crom_l1_composed_IntraRelationshipConstraint39", self)

class crom_l1_composed_RelationTarget(NamedElement):

    pass
class crom_l1_composed_TypedElement(NamedElement):

    pass
class crom_l1_composed_ModelElement(NamedElement):

    pass
class crom_l1_composed_Part:

    def __init__(self, lower: int, upper: int, Part: "crom_l1_composed_CompartmentType" = None, parts: "crom_l1_composed_CompartmentType" = None, crom_l1_composed_Part: "crom_l1_composed_AbstractRole" = None):
        self.lower = lower
        self.upper = upper
        self.Part = Part
        self.parts = parts
        self.crom_l1_composed_Part = crom_l1_composed_Part
        
    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def upper(self) -> int:
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper

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
            if hasattr(old_value, "crom_l1_composed_AbstractRole79"):
                opp_val = getattr(old_value, "crom_l1_composed_AbstractRole79", None)
                if opp_val == self:
                    setattr(old_value, "crom_l1_composed_AbstractRole79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "crom_l1_composed_AbstractRole79"):
                opp_val = getattr(value, "crom_l1_composed_AbstractRole79", None)
                setattr(value, "crom_l1_composed_AbstractRole79", self)

class crom_l1_composed_CompartmentType(RigidType):

    pass
class crom_l1_composed_NaturalType(RigidType):

    pass
class crom_l1_composed_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
