from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TypeRestrictionInheritance1(Enum):
    Total = "Total"
    Partial = "Partial"
class TypeIdentifier(Enum):
    NoIdentifier = "NoIdentifier"
    PrimaryIdentifier = "PrimaryIdentifier"
    AlternativeIdentifier = "AlternativeIdentifier"
class TypeAttribute(Enum):
    Normal = "Normal"
    Composite = "Composite"
    Multivalued = "Multivalued"
    Optional = "Optional"
    Derived = "Derived"
    Dependence_in_identification = "Dependence_in_identification"
class TypeRelationship(Enum):
    Regular = "Regular"
    Weak_dependence_in_existence = "Weak_dependence_in_existence"
    Weak_dependence_in_identification = "Weak_dependence_in_identification"
class TypeEntity(Enum):
    Weak = "Weak"
    Regular = "Regular"
class TypeRestrictionInheritance2(Enum):
    Exclusive = "Exclusive"
    Overlapped = "Overlapped"
class TypeRestriction(Enum):
    Exclusion = "Exclusion"
    Inclusion = "Inclusion"
class TypeRestriction2(Enum):
    Exclusiveness = "Exclusiveness"
    Inclusiveness = "Inclusiveness"


############################################
# Definition of Classes
############################################

class Connection_EntityRelationship:

    pass
class entityrelationship_Connection_EntityRelationship(ABC):

    def __init__(self, role: str, minimum_cardinality: str, maximum_cardinality: str, entityrelationship_Connection_EntityRelationship: "entityrelationship_Connection_E_R_Restriction" = None, entityrelationship_Connection_EntityRelationship62: "entityrelationship_Connection_E_R_Restriction" = None, entityrelationship_Connection_EntityRelationship95: "entityrelationship_Connection_ConnectionEntityRelationship2Attribute" = None):
        self.role = role
        self.minimum_cardinality = minimum_cardinality
        self.maximum_cardinality = maximum_cardinality
        self.entityrelationship_Connection_EntityRelationship = entityrelationship_Connection_EntityRelationship
        self.entityrelationship_Connection_EntityRelationship62 = entityrelationship_Connection_EntityRelationship62
        self.entityrelationship_Connection_EntityRelationship95 = entityrelationship_Connection_EntityRelationship95
        
    @property
    def maximum_cardinality(self) -> str:
        return self.__maximum_cardinality

    @maximum_cardinality.setter
    def maximum_cardinality(self, maximum_cardinality: str):
        self.__maximum_cardinality = maximum_cardinality

    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

    @property
    def minimum_cardinality(self) -> str:
        return self.__minimum_cardinality

    @minimum_cardinality.setter
    def minimum_cardinality(self, minimum_cardinality: str):
        self.__minimum_cardinality = minimum_cardinality

    @property
    def entityrelationship_Connection_EntityRelationship95(self):
        return self.__entityrelationship_Connection_EntityRelationship95

    @entityrelationship_Connection_EntityRelationship95.setter
    def entityrelationship_Connection_EntityRelationship95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Connection_EntityRelationship__entityrelationship_Connection_EntityRelationship95", None)
        self.__entityrelationship_Connection_EntityRelationship95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityrelationship_Connection_ConnectionEntityRelationship2Attribute"):
                opp_val = getattr(old_value, "entityrelationship_Connection_ConnectionEntityRelationship2Attribute", None)
                if opp_val == self:
                    setattr(old_value, "entityrelationship_Connection_ConnectionEntityRelationship2Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityrelationship_Connection_ConnectionEntityRelationship2Attribute"):
                opp_val = getattr(value, "entityrelationship_Connection_ConnectionEntityRelationship2Attribute", None)
                setattr(value, "entityrelationship_Connection_ConnectionEntityRelationship2Attribute", self)

    @property
    def entityrelationship_Connection_EntityRelationship(self):
        return self.__entityrelationship_Connection_EntityRelationship

    @entityrelationship_Connection_EntityRelationship.setter
    def entityrelationship_Connection_EntityRelationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Connection_EntityRelationship__entityrelationship_Connection_EntityRelationship", None)
        self.__entityrelationship_Connection_EntityRelationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityrelationship_Connection_E_R_Restriction"):
                opp_val = getattr(old_value, "entityrelationship_Connection_E_R_Restriction", None)
                if opp_val == self:
                    setattr(old_value, "entityrelationship_Connection_E_R_Restriction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityrelationship_Connection_E_R_Restriction"):
                opp_val = getattr(value, "entityrelationship_Connection_E_R_Restriction", None)
                setattr(value, "entityrelationship_Connection_E_R_Restriction", self)

    @property
    def entityrelationship_Connection_EntityRelationship62(self):
        return self.__entityrelationship_Connection_EntityRelationship62

    @entityrelationship_Connection_EntityRelationship62.setter
    def entityrelationship_Connection_EntityRelationship62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Connection_EntityRelationship__entityrelationship_Connection_EntityRelationship62", None)
        self.__entityrelationship_Connection_EntityRelationship62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityrelationship_Connection_E_R_Restriction61"):
                opp_val = getattr(old_value, "entityrelationship_Connection_E_R_Restriction61", None)
                if opp_val == self:
                    setattr(old_value, "entityrelationship_Connection_E_R_Restriction61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityrelationship_Connection_E_R_Restriction61"):
                opp_val = getattr(value, "entityrelationship_Connection_E_R_Restriction61", None)
                setattr(value, "entityrelationship_Connection_E_R_Restriction61", self)

class entityrelationship_Attribute_Composite:

    def __init__(self, name_at_composite: str, identifier_at_composite: str, Attribute_Composite: "entityrelationship_Attribute" = None, entityrelationship_Attribute_Composite: "entityrelationship_Attribute" = None, attributes_composites: "entityrelationship_Attribute" = None):
        self.name_at_composite = name_at_composite
        self.identifier_at_composite = identifier_at_composite
        self.Attribute_Composite = Attribute_Composite
        self.entityrelationship_Attribute_Composite = entityrelationship_Attribute_Composite
        self.attributes_composites = attributes_composites
        
    @property
    def identifier_at_composite(self) -> str:
        return self.__identifier_at_composite

    @identifier_at_composite.setter
    def identifier_at_composite(self, identifier_at_composite: str):
        self.__identifier_at_composite = identifier_at_composite

    @property
    def name_at_composite(self) -> str:
        return self.__name_at_composite

    @name_at_composite.setter
    def name_at_composite(self, name_at_composite: str):
        self.__name_at_composite = name_at_composite

    @property
    def entityrelationship_Attribute_Composite(self):
        return self.__entityrelationship_Attribute_Composite

    @entityrelationship_Attribute_Composite.setter
    def entityrelationship_Attribute_Composite(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Attribute_Composite__entityrelationship_Attribute_Composite", None)
        self.__entityrelationship_Attribute_Composite = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityrelationship_Attribute50"):
                opp_val = getattr(old_value, "entityrelationship_Attribute50", None)
                if opp_val == self:
                    setattr(old_value, "entityrelationship_Attribute50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityrelationship_Attribute50"):
                opp_val = getattr(value, "entityrelationship_Attribute50", None)
                setattr(value, "entityrelationship_Attribute50", self)

    @property
    def Attribute_Composite(self):
        return self.__Attribute_Composite

    @Attribute_Composite.setter
    def Attribute_Composite(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Attribute_Composite__Attribute_Composite", None)
        self.__Attribute_Composite = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inAttribute"):
                opp_val = getattr(old_value, "inAttribute", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inAttribute"):
                opp_val = getattr(value, "inAttribute", None)
                if opp_val is None:
                    setattr(value, "inAttribute", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def attributes_composites(self):
        return self.__attributes_composites

    @attributes_composites.setter
    def attributes_composites(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Attribute_Composite__attributes_composites", None)
        self.__attributes_composites = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attribute52"):
                opp_val = getattr(old_value, "Attribute52", None)
                if opp_val == self:
                    setattr(old_value, "Attribute52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attribute52"):
                opp_val = getattr(value, "Attribute52", None)
                setattr(value, "Attribute52", self)

class Elements_with_Attributes:

    pass
class entityrelationship_Relationship(Elements_with_Attributes):

    def __init__(self, name_relationship: str, order: int, cardinality: str, type_relationship: str, entityrelationship_Relationship: "entityrelationship_Relationships_Restriction" = None, target_relationship: set["entityrelationship_Relationships_Restriction"] = None, target_relationship31: set["entityrelationship_Connection_Entity2Relationship"] = None, source_relationship: set["entityrelationship_Connection_Relationship2Entity"] = None, entityrelationship_Relationship55: "entityrelationship_Relationships_Restriction" = None, Relationship: "entityrelationship_Relationships_Restriction" = None, Relationship85: "entityrelationship_Connection_Entity2Relationship" = None, Relationship89: "entityrelationship_Connection_Relationship2Entity" = None):
        self.name_relationship = name_relationship
        self.order = order
        self.cardinality = cardinality
        self.type_relationship = type_relationship
        self.entityrelationship_Relationship = entityrelationship_Relationship
        self.target_relationship = target_relationship if target_relationship is not None else set()
        self.target_relationship31 = target_relationship31 if target_relationship31 is not None else set()
        self.source_relationship = source_relationship if source_relationship is not None else set()
        self.entityrelationship_Relationship55 = entityrelationship_Relationship55
        self.Relationship = Relationship
        self.Relationship85 = Relationship85
        self.Relationship89 = Relationship89
        
    @property
    def order(self) -> int:
        return self.__order

    @order.setter
    def order(self, order: int):
        self.__order = order

    @property
    def cardinality(self) -> str:
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: str):
        self.__cardinality = cardinality

    @property
    def type_relationship(self) -> str:
        return self.__type_relationship

    @type_relationship.setter
    def type_relationship(self, type_relationship: str):
        self.__type_relationship = type_relationship

    @property
    def name_relationship(self) -> str:
        return self.__name_relationship

    @name_relationship.setter
    def name_relationship(self, name_relationship: str):
        self.__name_relationship = name_relationship

    @property
    def entityrelationship_Relationship(self):
        return self.__entityrelationship_Relationship

    @entityrelationship_Relationship.setter
    def entityrelationship_Relationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Relationship__entityrelationship_Relationship", None)
        self.__entityrelationship_Relationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityrelationship_Relationships_Restriction"):
                opp_val = getattr(old_value, "entityrelationship_Relationships_Restriction", None)
                if opp_val == self:
                    setattr(old_value, "entityrelationship_Relationships_Restriction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityrelationship_Relationships_Restriction"):
                opp_val = getattr(value, "entityrelationship_Relationships_Restriction", None)
                setattr(value, "entityrelationship_Relationships_Restriction", self)

    @property
    def Relationship(self):
        return self.__Relationship

    @Relationship.setter
    def Relationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Relationship__Relationship", None)
        self.__Relationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target_restrictions"):
                opp_val = getattr(old_value, "target_restrictions", None)
                if opp_val == self:
                    setattr(old_value, "target_restrictions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target_restrictions"):
                opp_val = getattr(value, "target_restrictions", None)
                setattr(value, "target_restrictions", self)

    @property
    def Relationship89(self):
        return self.__Relationship89

    @Relationship89.setter
    def Relationship89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Relationship__Relationship89", None)
        self.__Relationship89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationship_connected_to_relationship2entity"):
                opp_val = getattr(old_value, "relationship_connected_to_relationship2entity", None)
                if opp_val == self:
                    setattr(old_value, "relationship_connected_to_relationship2entity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationship_connected_to_relationship2entity"):
                opp_val = getattr(value, "relationship_connected_to_relationship2entity", None)
                setattr(value, "relationship_connected_to_relationship2entity", self)

    @property
    def entityrelationship_Relationship55(self):
        return self.__entityrelationship_Relationship55

    @entityrelationship_Relationship55.setter
    def entityrelationship_Relationship55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Relationship__entityrelationship_Relationship55", None)
        self.__entityrelationship_Relationship55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityrelationship_Relationships_Restriction54"):
                opp_val = getattr(old_value, "entityrelationship_Relationships_Restriction54", None)
                if opp_val == self:
                    setattr(old_value, "entityrelationship_Relationships_Restriction54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityrelationship_Relationships_Restriction54"):
                opp_val = getattr(value, "entityrelationship_Relationships_Restriction54", None)
                setattr(value, "entityrelationship_Relationships_Restriction54", self)

    @property
    def source_relationship(self):
        return self.__source_relationship

    @source_relationship.setter
    def source_relationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Relationship__source_relationship", None)
        self.__source_relationship = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Connection_Relationship2Entity34"):
                    opp_val = getattr(item, "Connection_Relationship2Entity34", None)
                    
                    if opp_val == self:
                        setattr(item, "Connection_Relationship2Entity34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Connection_Relationship2Entity34"):
                    opp_val = getattr(item, "Connection_Relationship2Entity34", None)
                    
                    setattr(item, "Connection_Relationship2Entity34", self)
                    

    @property
    def target_relationship31(self):
        return self.__target_relationship31

    @target_relationship31.setter
    def target_relationship31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Relationship__target_relationship31", None)
        self.__target_relationship31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Connection_Entity2Relationship32"):
                    opp_val = getattr(item, "Connection_Entity2Relationship32", None)
                    
                    if opp_val == self:
                        setattr(item, "Connection_Entity2Relationship32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Connection_Entity2Relationship32"):
                    opp_val = getattr(item, "Connection_Entity2Relationship32", None)
                    
                    setattr(item, "Connection_Entity2Relationship32", self)
                    

    @property
    def target_relationship(self):
        return self.__target_relationship

    @target_relationship.setter
    def target_relationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Relationship__target_relationship", None)
        self.__target_relationship = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Relationships_Restriction29"):
                    opp_val = getattr(item, "Relationships_Restriction29", None)
                    
                    if opp_val == self:
                        setattr(item, "Relationships_Restriction29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Relationships_Restriction29"):
                    opp_val = getattr(item, "Relationships_Restriction29", None)
                    
                    setattr(item, "Relationships_Restriction29", self)
                    

    @property
    def Relationship85(self):
        return self.__Relationship85

    @Relationship85.setter
    def Relationship85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Relationship__Relationship85", None)
        self.__Relationship85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationship_connected_to_entity2relationship"):
                opp_val = getattr(old_value, "relationship_connected_to_entity2relationship", None)
                if opp_val == self:
                    setattr(old_value, "relationship_connected_to_entity2relationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationship_connected_to_entity2relationship"):
                opp_val = getattr(value, "relationship_connected_to_entity2relationship", None)
                setattr(value, "relationship_connected_to_entity2relationship", self)

class entityrelationship_Entity(Elements_with_Attributes):

    def __init__(self, name_entity: str, type_entity: str, source_entity: set["entityrelationship_Connection_Entity2Relationship"] = None, target_entity: set["entityrelationship_Connection_Relationship2Entity"] = None, subclasses: set["entityrelationship_Generalization"] = None, entityrelationship_Entity: "entityrelationship_Generalization" = None, Entity: "entityrelationship_Generalization" = None, entityrelationship_Entity79: "entityrelationship_Connection_Generalization_Entity" = None, Entity83: "entityrelationship_Connection_Entity2Relationship" = None, Entity91: "entityrelationship_Connection_Relationship2Entity" = None):
        self.name_entity = name_entity
        self.type_entity = type_entity
        self.source_entity = source_entity if source_entity is not None else set()
        self.target_entity = target_entity if target_entity is not None else set()
        self.subclasses = subclasses if subclasses is not None else set()
        self.entityrelationship_Entity = entityrelationship_Entity
        self.Entity = Entity
        self.entityrelationship_Entity79 = entityrelationship_Entity79
        self.Entity83 = Entity83
        self.Entity91 = Entity91
        
    @property
    def type_entity(self) -> str:
        return self.__type_entity

    @type_entity.setter
    def type_entity(self, type_entity: str):
        self.__type_entity = type_entity

    @property
    def name_entity(self) -> str:
        return self.__name_entity

    @name_entity.setter
    def name_entity(self, name_entity: str):
        self.__name_entity = name_entity

    @property
    def entityrelationship_Entity(self):
        return self.__entityrelationship_Entity

    @entityrelationship_Entity.setter
    def entityrelationship_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Entity__entityrelationship_Entity", None)
        self.__entityrelationship_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityrelationship_Generalization"):
                opp_val = getattr(old_value, "entityrelationship_Generalization", None)
                if opp_val == self:
                    setattr(old_value, "entityrelationship_Generalization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityrelationship_Generalization"):
                opp_val = getattr(value, "entityrelationship_Generalization", None)
                setattr(value, "entityrelationship_Generalization", self)

    @property
    def source_entity(self):
        return self.__source_entity

    @source_entity.setter
    def source_entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Entity__source_entity", None)
        self.__source_entity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Connection_Entity2Relationship22"):
                    opp_val = getattr(item, "Connection_Entity2Relationship22", None)
                    
                    if opp_val == self:
                        setattr(item, "Connection_Entity2Relationship22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Connection_Entity2Relationship22"):
                    opp_val = getattr(item, "Connection_Entity2Relationship22", None)
                    
                    setattr(item, "Connection_Entity2Relationship22", self)
                    

    @property
    def subclasses(self):
        return self.__subclasses

    @subclasses.setter
    def subclasses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Entity__subclasses", None)
        self.__subclasses = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Generalization26"):
                    opp_val = getattr(item, "Generalization26", None)
                    
                    if opp_val == self:
                        setattr(item, "Generalization26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Generalization26"):
                    opp_val = getattr(item, "Generalization26", None)
                    
                    setattr(item, "Generalization26", self)
                    

    @property
    def entityrelationship_Entity79(self):
        return self.__entityrelationship_Entity79

    @entityrelationship_Entity79.setter
    def entityrelationship_Entity79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Entity__entityrelationship_Entity79", None)
        self.__entityrelationship_Entity79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityrelationship_Connection_Generalization_Entity78"):
                opp_val = getattr(old_value, "entityrelationship_Connection_Generalization_Entity78", None)
                if opp_val == self:
                    setattr(old_value, "entityrelationship_Connection_Generalization_Entity78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityrelationship_Connection_Generalization_Entity78"):
                opp_val = getattr(value, "entityrelationship_Connection_Generalization_Entity78", None)
                setattr(value, "entityrelationship_Connection_Generalization_Entity78", self)

    @property
    def target_entity(self):
        return self.__target_entity

    @target_entity.setter
    def target_entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Entity__target_entity", None)
        self.__target_entity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Connection_Relationship2Entity24"):
                    opp_val = getattr(item, "Connection_Relationship2Entity24", None)
                    
                    if opp_val == self:
                        setattr(item, "Connection_Relationship2Entity24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Connection_Relationship2Entity24"):
                    opp_val = getattr(item, "Connection_Relationship2Entity24", None)
                    
                    setattr(item, "Connection_Relationship2Entity24", self)
                    

    @property
    def Entity(self):
        return self.__Entity

    @Entity.setter
    def Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Entity__Entity", None)
        self.__Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subclass_generalizations"):
                opp_val = getattr(old_value, "subclass_generalizations", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subclass_generalizations"):
                opp_val = getattr(value, "subclass_generalizations", None)
                if opp_val is None:
                    setattr(value, "subclass_generalizations", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Entity83(self):
        return self.__Entity83

    @Entity83.setter
    def Entity83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Entity__Entity83", None)
        self.__Entity83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entity_connected_to_entity2relationship"):
                opp_val = getattr(old_value, "entity_connected_to_entity2relationship", None)
                if opp_val == self:
                    setattr(old_value, "entity_connected_to_entity2relationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entity_connected_to_entity2relationship"):
                opp_val = getattr(value, "entity_connected_to_entity2relationship", None)
                setattr(value, "entity_connected_to_entity2relationship", self)

    @property
    def Entity91(self):
        return self.__Entity91

    @Entity91.setter
    def Entity91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Entity__Entity91", None)
        self.__Entity91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entity_connected_to_relationship2entity"):
                opp_val = getattr(old_value, "entity_connected_to_relationship2entity", None)
                if opp_val == self:
                    setattr(old_value, "entity_connected_to_relationship2entity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entity_connected_to_relationship2entity"):
                opp_val = getattr(value, "entity_connected_to_relationship2entity", None)
                setattr(value, "entity_connected_to_relationship2entity", self)

class entityrelationship_Generalization:

    def __init__(self, restriction_inheritance_1: str, restriction_inheritance_2: str, Generalization: "entityrelationship_Entity_Relationship_Model" = None, Generalization26: "entityrelationship_Entity" = None, entityrelationship_Generalization: "entityrelationship_Entity" = None, ERM_Has_G: "entityrelationship_Entity_Relationship_Model" = None, subclass_generalizations: set["entityrelationship_Entity"] = None, entityrelationship_Generalization76: "entityrelationship_Connection_Generalization_Entity" = None):
        self.restriction_inheritance_1 = restriction_inheritance_1
        self.restriction_inheritance_2 = restriction_inheritance_2
        self.Generalization = Generalization
        self.Generalization26 = Generalization26
        self.entityrelationship_Generalization = entityrelationship_Generalization
        self.ERM_Has_G = ERM_Has_G
        self.subclass_generalizations = subclass_generalizations if subclass_generalizations is not None else set()
        self.entityrelationship_Generalization76 = entityrelationship_Generalization76
        
    @property
    def restriction_inheritance_2(self) -> str:
        return self.__restriction_inheritance_2

    @restriction_inheritance_2.setter
    def restriction_inheritance_2(self, restriction_inheritance_2: str):
        self.__restriction_inheritance_2 = restriction_inheritance_2

    @property
    def restriction_inheritance_1(self) -> str:
        return self.__restriction_inheritance_1

    @restriction_inheritance_1.setter
    def restriction_inheritance_1(self, restriction_inheritance_1: str):
        self.__restriction_inheritance_1 = restriction_inheritance_1

    @property
    def Generalization26(self):
        return self.__Generalization26

    @Generalization26.setter
    def Generalization26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Generalization__Generalization26", None)
        self.__Generalization26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subclasses"):
                opp_val = getattr(old_value, "subclasses", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subclasses"):
                opp_val = getattr(value, "subclasses", None)
                if opp_val is None:
                    setattr(value, "subclasses", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def entityrelationship_Generalization76(self):
        return self.__entityrelationship_Generalization76

    @entityrelationship_Generalization76.setter
    def entityrelationship_Generalization76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Generalization__entityrelationship_Generalization76", None)
        self.__entityrelationship_Generalization76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityrelationship_Connection_Generalization_Entity"):
                opp_val = getattr(old_value, "entityrelationship_Connection_Generalization_Entity", None)
                if opp_val == self:
                    setattr(old_value, "entityrelationship_Connection_Generalization_Entity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityrelationship_Connection_Generalization_Entity"):
                opp_val = getattr(value, "entityrelationship_Connection_Generalization_Entity", None)
                setattr(value, "entityrelationship_Connection_Generalization_Entity", self)

    @property
    def ERM_Has_G(self):
        return self.__ERM_Has_G

    @ERM_Has_G.setter
    def ERM_Has_G(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Generalization__ERM_Has_G", None)
        self.__ERM_Has_G = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Entity_Relationship_Model68"):
                opp_val = getattr(old_value, "Entity_Relationship_Model68", None)
                if opp_val == self:
                    setattr(old_value, "Entity_Relationship_Model68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Entity_Relationship_Model68"):
                opp_val = getattr(value, "Entity_Relationship_Model68", None)
                setattr(value, "Entity_Relationship_Model68", self)

    @property
    def Generalization(self):
        return self.__Generalization

    @Generalization.setter
    def Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Generalization__Generalization", None)
        self.__Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inEntityRelationshipModel17"):
                opp_val = getattr(old_value, "inEntityRelationshipModel17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inEntityRelationshipModel17"):
                opp_val = getattr(value, "inEntityRelationshipModel17", None)
                if opp_val is None:
                    setattr(value, "inEntityRelationshipModel17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def entityrelationship_Generalization(self):
        return self.__entityrelationship_Generalization

    @entityrelationship_Generalization.setter
    def entityrelationship_Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Generalization__entityrelationship_Generalization", None)
        self.__entityrelationship_Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityrelationship_Entity"):
                opp_val = getattr(old_value, "entityrelationship_Entity", None)
                if opp_val == self:
                    setattr(old_value, "entityrelationship_Entity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityrelationship_Entity"):
                opp_val = getattr(value, "entityrelationship_Entity", None)
                setattr(value, "entityrelationship_Entity", self)

    @property
    def subclass_generalizations(self):
        return self.__subclass_generalizations

    @subclass_generalizations.setter
    def subclass_generalizations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Generalization__subclass_generalizations", None)
        self.__subclass_generalizations = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Entity"):
                    opp_val = getattr(item, "Entity", None)
                    
                    if opp_val == self:
                        setattr(item, "Entity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Entity"):
                    opp_val = getattr(item, "Entity", None)
                    
                    setattr(item, "Entity", self)
                    

class entityrelationship_Attribute:

    def __init__(self, name_attribute: str, identifier: str, entityrelationship_Attribute: "entityrelationship_Entity_Relationship_Model" = None, inAttribute: set["entityrelationship_Attribute_Composite"] = None, Attribute: "entityrelationship_Attribute" = None, inAttribute38: set["entityrelationship_Attribute"] = None, connection_attribute: "entityrelationship_Connection_With_Attribute" = None, Attribute43: "entityrelationship_Attribute" = None, attributes_identification: "entityrelationship_Attribute" = None, entityrelationship_Attribute45: "entityrelationship_Entity_Relationship_Model" = None, target_attribute: "entityrelationship_Connection_ConnectionEntityRelationship2Attribute" = None, entityrelationship_Attribute50: "entityrelationship_Attribute_Composite" = None, Attribute52: "entityrelationship_Attribute_Composite" = None, Attribute70: "entityrelationship_Connection_With_Attribute" = None, Attribute97: "entityrelationship_Connection_ConnectionEntityRelationship2Attribute" = None):
        self.name_attribute = name_attribute
        self.identifier = identifier
        self.entityrelationship_Attribute = entityrelationship_Attribute
        self.inAttribute = inAttribute if inAttribute is not None else set()
        self.Attribute = Attribute
        self.inAttribute38 = inAttribute38 if inAttribute38 is not None else set()
        self.connection_attribute = connection_attribute
        self.Attribute43 = Attribute43
        self.attributes_identification = attributes_identification
        self.entityrelationship_Attribute45 = entityrelationship_Attribute45
        self.target_attribute = target_attribute
        self.entityrelationship_Attribute50 = entityrelationship_Attribute50
        self.Attribute52 = Attribute52
        self.Attribute70 = Attribute70
        self.Attribute97 = Attribute97
        
    @property
    def name_attribute(self) -> str:
        return self.__name_attribute

    @name_attribute.setter
    def name_attribute(self, name_attribute: str):
        self.__name_attribute = name_attribute

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Attribute__Attribute", None)
        self.__Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inAttribute38"):
                opp_val = getattr(old_value, "inAttribute38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inAttribute38"):
                opp_val = getattr(value, "inAttribute38", None)
                if opp_val is None:
                    setattr(value, "inAttribute38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Attribute43(self):
        return self.__Attribute43

    @Attribute43.setter
    def Attribute43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Attribute__Attribute43", None)
        self.__Attribute43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attributes_identification"):
                opp_val = getattr(old_value, "attributes_identification", None)
                if opp_val == self:
                    setattr(old_value, "attributes_identification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attributes_identification"):
                opp_val = getattr(value, "attributes_identification", None)
                setattr(value, "attributes_identification", self)

    @property
    def entityrelationship_Attribute50(self):
        return self.__entityrelationship_Attribute50

    @entityrelationship_Attribute50.setter
    def entityrelationship_Attribute50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Attribute__entityrelationship_Attribute50", None)
        self.__entityrelationship_Attribute50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityrelationship_Attribute_Composite"):
                opp_val = getattr(old_value, "entityrelationship_Attribute_Composite", None)
                if opp_val == self:
                    setattr(old_value, "entityrelationship_Attribute_Composite", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityrelationship_Attribute_Composite"):
                opp_val = getattr(value, "entityrelationship_Attribute_Composite", None)
                setattr(value, "entityrelationship_Attribute_Composite", self)

    @property
    def Attribute70(self):
        return self.__Attribute70

    @Attribute70.setter
    def Attribute70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Attribute__Attribute70", None)
        self.__Attribute70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connected"):
                opp_val = getattr(old_value, "connected", None)
                if opp_val == self:
                    setattr(old_value, "connected", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connected"):
                opp_val = getattr(value, "connected", None)
                setattr(value, "connected", self)

    @property
    def inAttribute(self):
        return self.__inAttribute

    @inAttribute.setter
    def inAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Attribute__inAttribute", None)
        self.__inAttribute = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute_Composite"):
                    opp_val = getattr(item, "Attribute_Composite", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute_Composite", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute_Composite"):
                    opp_val = getattr(item, "Attribute_Composite", None)
                    
                    setattr(item, "Attribute_Composite", self)
                    

    @property
    def target_attribute(self):
        return self.__target_attribute

    @target_attribute.setter
    def target_attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Attribute__target_attribute", None)
        self.__target_attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Connection_ConnectionEntityRelationship2Attribute48"):
                opp_val = getattr(old_value, "Connection_ConnectionEntityRelationship2Attribute48", None)
                if opp_val == self:
                    setattr(old_value, "Connection_ConnectionEntityRelationship2Attribute48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Connection_ConnectionEntityRelationship2Attribute48"):
                opp_val = getattr(value, "Connection_ConnectionEntityRelationship2Attribute48", None)
                setattr(value, "Connection_ConnectionEntityRelationship2Attribute48", self)

    @property
    def Attribute52(self):
        return self.__Attribute52

    @Attribute52.setter
    def Attribute52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Attribute__Attribute52", None)
        self.__Attribute52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attributes_composites"):
                opp_val = getattr(old_value, "attributes_composites", None)
                if opp_val == self:
                    setattr(old_value, "attributes_composites", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attributes_composites"):
                opp_val = getattr(value, "attributes_composites", None)
                setattr(value, "attributes_composites", self)

    @property
    def Attribute97(self):
        return self.__Attribute97

    @Attribute97.setter
    def Attribute97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Attribute__Attribute97", None)
        self.__Attribute97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attribute_connected_to_conection_entityrelationship_to_attribute"):
                opp_val = getattr(old_value, "attribute_connected_to_conection_entityrelationship_to_attribute", None)
                if opp_val == self:
                    setattr(old_value, "attribute_connected_to_conection_entityrelationship_to_attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attribute_connected_to_conection_entityrelationship_to_attribute"):
                opp_val = getattr(value, "attribute_connected_to_conection_entityrelationship_to_attribute", None)
                setattr(value, "attribute_connected_to_conection_entityrelationship_to_attribute", self)

    @property
    def attributes_identification(self):
        return self.__attributes_identification

    @attributes_identification.setter
    def attributes_identification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Attribute__attributes_identification", None)
        self.__attributes_identification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attribute43"):
                opp_val = getattr(old_value, "Attribute43", None)
                if opp_val == self:
                    setattr(old_value, "Attribute43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attribute43"):
                opp_val = getattr(value, "Attribute43", None)
                setattr(value, "Attribute43", self)

    @property
    def entityrelationship_Attribute45(self):
        return self.__entityrelationship_Attribute45

    @entityrelationship_Attribute45.setter
    def entityrelationship_Attribute45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Attribute__entityrelationship_Attribute45", None)
        self.__entityrelationship_Attribute45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityrelationship_Entity_Relationship_Model46"):
                opp_val = getattr(old_value, "entityrelationship_Entity_Relationship_Model46", None)
                if opp_val == self:
                    setattr(old_value, "entityrelationship_Entity_Relationship_Model46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityrelationship_Entity_Relationship_Model46"):
                opp_val = getattr(value, "entityrelationship_Entity_Relationship_Model46", None)
                setattr(value, "entityrelationship_Entity_Relationship_Model46", self)

    @property
    def entityrelationship_Attribute(self):
        return self.__entityrelationship_Attribute

    @entityrelationship_Attribute.setter
    def entityrelationship_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Attribute__entityrelationship_Attribute", None)
        self.__entityrelationship_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityrelationship_Entity_Relationship_Model"):
                opp_val = getattr(old_value, "entityrelationship_Entity_Relationship_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityrelationship_Entity_Relationship_Model"):
                opp_val = getattr(value, "entityrelationship_Entity_Relationship_Model", None)
                if opp_val is None:
                    setattr(value, "entityrelationship_Entity_Relationship_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def inAttribute38(self):
        return self.__inAttribute38

    @inAttribute38.setter
    def inAttribute38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Attribute__inAttribute38", None)
        self.__inAttribute38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    setattr(item, "Attribute", self)
                    

    @property
    def connection_attribute(self):
        return self.__connection_attribute

    @connection_attribute.setter
    def connection_attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Attribute__connection_attribute", None)
        self.__connection_attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Connection_With_Attribute40"):
                opp_val = getattr(old_value, "Connection_With_Attribute40", None)
                if opp_val == self:
                    setattr(old_value, "Connection_With_Attribute40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Connection_With_Attribute40"):
                opp_val = getattr(value, "Connection_With_Attribute40", None)
                setattr(value, "Connection_With_Attribute40", self)

class entityrelationship_Connection_With_Attribute:

    def __init__(self, type_attribute: str, Connection_With_Attribute: "entityrelationship_Entity_Relationship_Model" = None, Connection_With_Attribute19: "entityrelationship_Elements_with_Attributes" = None, Connection_With_Attribute40: "entityrelationship_Attribute" = None, connected: "entityrelationship_Attribute" = None, connected_with_attribute: "entityrelationship_Elements_with_Attributes" = None, ERM_Has_CEA: "entityrelationship_Entity_Relationship_Model" = None):
        self.type_attribute = type_attribute
        self.Connection_With_Attribute = Connection_With_Attribute
        self.Connection_With_Attribute19 = Connection_With_Attribute19
        self.Connection_With_Attribute40 = Connection_With_Attribute40
        self.connected = connected
        self.connected_with_attribute = connected_with_attribute
        self.ERM_Has_CEA = ERM_Has_CEA
        
    @property
    def type_attribute(self) -> str:
        return self.__type_attribute

    @type_attribute.setter
    def type_attribute(self, type_attribute: str):
        self.__type_attribute = type_attribute

    @property
    def connected(self):
        return self.__connected

    @connected.setter
    def connected(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Connection_With_Attribute__connected", None)
        self.__connected = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attribute70"):
                opp_val = getattr(old_value, "Attribute70", None)
                if opp_val == self:
                    setattr(old_value, "Attribute70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attribute70"):
                opp_val = getattr(value, "Attribute70", None)
                setattr(value, "Attribute70", self)

    @property
    def connected_with_attribute(self):
        return self.__connected_with_attribute

    @connected_with_attribute.setter
    def connected_with_attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Connection_With_Attribute__connected_with_attribute", None)
        self.__connected_with_attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Elements_with_Attributes72"):
                opp_val = getattr(old_value, "Elements_with_Attributes72", None)
                if opp_val == self:
                    setattr(old_value, "Elements_with_Attributes72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Elements_with_Attributes72"):
                opp_val = getattr(value, "Elements_with_Attributes72", None)
                setattr(value, "Elements_with_Attributes72", self)

    @property
    def Connection_With_Attribute(self):
        return self.__Connection_With_Attribute

    @Connection_With_Attribute.setter
    def Connection_With_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Connection_With_Attribute__Connection_With_Attribute", None)
        self.__Connection_With_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inEntityRelationshipModel14"):
                opp_val = getattr(old_value, "inEntityRelationshipModel14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inEntityRelationshipModel14"):
                opp_val = getattr(value, "inEntityRelationshipModel14", None)
                if opp_val is None:
                    setattr(value, "inEntityRelationshipModel14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ERM_Has_CEA(self):
        return self.__ERM_Has_CEA

    @ERM_Has_CEA.setter
    def ERM_Has_CEA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Connection_With_Attribute__ERM_Has_CEA", None)
        self.__ERM_Has_CEA = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Entity_Relationship_Model74"):
                opp_val = getattr(old_value, "Entity_Relationship_Model74", None)
                if opp_val == self:
                    setattr(old_value, "Entity_Relationship_Model74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Entity_Relationship_Model74"):
                opp_val = getattr(value, "Entity_Relationship_Model74", None)
                setattr(value, "Entity_Relationship_Model74", self)

    @property
    def Connection_With_Attribute19(self):
        return self.__Connection_With_Attribute19

    @Connection_With_Attribute19.setter
    def Connection_With_Attribute19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Connection_With_Attribute__Connection_With_Attribute19", None)
        self.__Connection_With_Attribute19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "element"):
                opp_val = getattr(old_value, "element", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "element"):
                opp_val = getattr(value, "element", None)
                if opp_val is None:
                    setattr(value, "element", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Connection_With_Attribute40(self):
        return self.__Connection_With_Attribute40

    @Connection_With_Attribute40.setter
    def Connection_With_Attribute40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Connection_With_Attribute__Connection_With_Attribute40", None)
        self.__Connection_With_Attribute40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_attribute"):
                opp_val = getattr(old_value, "connection_attribute", None)
                if opp_val == self:
                    setattr(old_value, "connection_attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_attribute"):
                opp_val = getattr(value, "connection_attribute", None)
                setattr(value, "connection_attribute", self)

class entityrelationship_Connection_ConnectionEntityRelationship2Attribute:

    pass
class entityrelationship_Connection_Relationship2Entity(Connection_EntityRelationship):

    pass
class entityrelationship_Connection_Entity2Relationship(Connection_EntityRelationship):

    pass
class entityrelationship_Relationships_Restriction:

    def __init__(self, type_restriction: str, Relationships_Restriction: "entityrelationship_Entity_Relationship_Model" = None, entityrelationship_Relationships_Restriction: "entityrelationship_Relationship" = None, Relationships_Restriction29: "entityrelationship_Relationship" = None, entityrelationship_Relationships_Restriction54: "entityrelationship_Relationship" = None, target_restrictions: "entityrelationship_Relationship" = None, ERM_Has_Rt: "entityrelationship_Entity_Relationship_Model" = None):
        self.type_restriction = type_restriction
        self.Relationships_Restriction = Relationships_Restriction
        self.entityrelationship_Relationships_Restriction = entityrelationship_Relationships_Restriction
        self.Relationships_Restriction29 = Relationships_Restriction29
        self.entityrelationship_Relationships_Restriction54 = entityrelationship_Relationships_Restriction54
        self.target_restrictions = target_restrictions
        self.ERM_Has_Rt = ERM_Has_Rt
        
    @property
    def type_restriction(self) -> str:
        return self.__type_restriction

    @type_restriction.setter
    def type_restriction(self, type_restriction: str):
        self.__type_restriction = type_restriction

    @property
    def Relationships_Restriction29(self):
        return self.__Relationships_Restriction29

    @Relationships_Restriction29.setter
    def Relationships_Restriction29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Relationships_Restriction__Relationships_Restriction29", None)
        self.__Relationships_Restriction29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target_relationship"):
                opp_val = getattr(old_value, "target_relationship", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target_relationship"):
                opp_val = getattr(value, "target_relationship", None)
                if opp_val is None:
                    setattr(value, "target_relationship", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ERM_Has_Rt(self):
        return self.__ERM_Has_Rt

    @ERM_Has_Rt.setter
    def ERM_Has_Rt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Relationships_Restriction__ERM_Has_Rt", None)
        self.__ERM_Has_Rt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Entity_Relationship_Model58"):
                opp_val = getattr(old_value, "Entity_Relationship_Model58", None)
                if opp_val == self:
                    setattr(old_value, "Entity_Relationship_Model58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Entity_Relationship_Model58"):
                opp_val = getattr(value, "Entity_Relationship_Model58", None)
                setattr(value, "Entity_Relationship_Model58", self)

    @property
    def entityrelationship_Relationships_Restriction54(self):
        return self.__entityrelationship_Relationships_Restriction54

    @entityrelationship_Relationships_Restriction54.setter
    def entityrelationship_Relationships_Restriction54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Relationships_Restriction__entityrelationship_Relationships_Restriction54", None)
        self.__entityrelationship_Relationships_Restriction54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityrelationship_Relationship55"):
                opp_val = getattr(old_value, "entityrelationship_Relationship55", None)
                if opp_val == self:
                    setattr(old_value, "entityrelationship_Relationship55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityrelationship_Relationship55"):
                opp_val = getattr(value, "entityrelationship_Relationship55", None)
                setattr(value, "entityrelationship_Relationship55", self)

    @property
    def target_restrictions(self):
        return self.__target_restrictions

    @target_restrictions.setter
    def target_restrictions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Relationships_Restriction__target_restrictions", None)
        self.__target_restrictions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Relationship"):
                opp_val = getattr(old_value, "Relationship", None)
                if opp_val == self:
                    setattr(old_value, "Relationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Relationship"):
                opp_val = getattr(value, "Relationship", None)
                setattr(value, "Relationship", self)

    @property
    def Relationships_Restriction(self):
        return self.__Relationships_Restriction

    @Relationships_Restriction.setter
    def Relationships_Restriction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Relationships_Restriction__Relationships_Restriction", None)
        self.__Relationships_Restriction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inEntityRelationshipModel2"):
                opp_val = getattr(old_value, "inEntityRelationshipModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inEntityRelationshipModel2"):
                opp_val = getattr(value, "inEntityRelationshipModel2", None)
                if opp_val is None:
                    setattr(value, "inEntityRelationshipModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def entityrelationship_Relationships_Restriction(self):
        return self.__entityrelationship_Relationships_Restriction

    @entityrelationship_Relationships_Restriction.setter
    def entityrelationship_Relationships_Restriction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Relationships_Restriction__entityrelationship_Relationships_Restriction", None)
        self.__entityrelationship_Relationships_Restriction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityrelationship_Relationship"):
                opp_val = getattr(old_value, "entityrelationship_Relationship", None)
                if opp_val == self:
                    setattr(old_value, "entityrelationship_Relationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityrelationship_Relationship"):
                opp_val = getattr(value, "entityrelationship_Relationship", None)
                setattr(value, "entityrelationship_Relationship", self)

class entityrelationship_Elements_with_Attributes:

    pass
class entityrelationship_Entity_Relationship_Model:

    def __init__(self, name: str, inEntityRelationshipModel10: set["entityrelationship_Connection_Generalization_Entity"] = None, inEntityRelationshipModel12: set["entityrelationship_Connection_E_R_Restriction"] = None, inEntityRelationshipModel: set["entityrelationship_Elements_with_Attributes"] = None, inEntityRelationshipModel2: set["entityrelationship_Relationships_Restriction"] = None, inEntityRelationshipModel4: set["entityrelationship_Connection_Entity2Relationship"] = None, inEntityRelationshipModel6: set["entityrelationship_Connection_Relationship2Entity"] = None, inEntityRelationshipModel8: set["entityrelationship_Connection_ConnectionEntityRelationship2Attribute"] = None, inEntityRelationshipModel14: set["entityrelationship_Connection_With_Attribute"] = None, entityrelationship_Entity_Relationship_Model: set["entityrelationship_Attribute"] = None, inEntityRelationshipModel17: set["entityrelationship_Generalization"] = None, Entity_Relationship_Model: "entityrelationship_Elements_with_Attributes" = None, entityrelationship_Entity_Relationship_Model46: "entityrelationship_Attribute" = None, Entity_Relationship_Model68: "entityrelationship_Generalization" = None, Entity_Relationship_Model58: "entityrelationship_Relationships_Restriction" = None, Entity_Relationship_Model64: "entityrelationship_Connection_E_R_Restriction" = None, Entity_Relationship_Model74: "entityrelationship_Connection_With_Attribute" = None, Entity_Relationship_Model81: "entityrelationship_Connection_Generalization_Entity" = None, Entity_Relationship_Model99: "entityrelationship_Connection_ConnectionEntityRelationship2Attribute" = None, Entity_Relationship_Model87: "entityrelationship_Connection_Entity2Relationship" = None, Entity_Relationship_Model93: "entityrelationship_Connection_Relationship2Entity" = None):
        self.name = name
        self.inEntityRelationshipModel10 = inEntityRelationshipModel10 if inEntityRelationshipModel10 is not None else set()
        self.inEntityRelationshipModel12 = inEntityRelationshipModel12 if inEntityRelationshipModel12 is not None else set()
        self.inEntityRelationshipModel = inEntityRelationshipModel if inEntityRelationshipModel is not None else set()
        self.inEntityRelationshipModel2 = inEntityRelationshipModel2 if inEntityRelationshipModel2 is not None else set()
        self.inEntityRelationshipModel4 = inEntityRelationshipModel4 if inEntityRelationshipModel4 is not None else set()
        self.inEntityRelationshipModel6 = inEntityRelationshipModel6 if inEntityRelationshipModel6 is not None else set()
        self.inEntityRelationshipModel8 = inEntityRelationshipModel8 if inEntityRelationshipModel8 is not None else set()
        self.inEntityRelationshipModel14 = inEntityRelationshipModel14 if inEntityRelationshipModel14 is not None else set()
        self.entityrelationship_Entity_Relationship_Model = entityrelationship_Entity_Relationship_Model if entityrelationship_Entity_Relationship_Model is not None else set()
        self.inEntityRelationshipModel17 = inEntityRelationshipModel17 if inEntityRelationshipModel17 is not None else set()
        self.Entity_Relationship_Model = Entity_Relationship_Model
        self.entityrelationship_Entity_Relationship_Model46 = entityrelationship_Entity_Relationship_Model46
        self.Entity_Relationship_Model68 = Entity_Relationship_Model68
        self.Entity_Relationship_Model58 = Entity_Relationship_Model58
        self.Entity_Relationship_Model64 = Entity_Relationship_Model64
        self.Entity_Relationship_Model74 = Entity_Relationship_Model74
        self.Entity_Relationship_Model81 = Entity_Relationship_Model81
        self.Entity_Relationship_Model99 = Entity_Relationship_Model99
        self.Entity_Relationship_Model87 = Entity_Relationship_Model87
        self.Entity_Relationship_Model93 = Entity_Relationship_Model93
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def inEntityRelationshipModel4(self):
        return self.__inEntityRelationshipModel4

    @inEntityRelationshipModel4.setter
    def inEntityRelationshipModel4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Entity_Relationship_Model__inEntityRelationshipModel4", None)
        self.__inEntityRelationshipModel4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Connection_Entity2Relationship"):
                    opp_val = getattr(item, "Connection_Entity2Relationship", None)
                    
                    if opp_val == self:
                        setattr(item, "Connection_Entity2Relationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Connection_Entity2Relationship"):
                    opp_val = getattr(item, "Connection_Entity2Relationship", None)
                    
                    setattr(item, "Connection_Entity2Relationship", self)
                    

    @property
    def inEntityRelationshipModel2(self):
        return self.__inEntityRelationshipModel2

    @inEntityRelationshipModel2.setter
    def inEntityRelationshipModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Entity_Relationship_Model__inEntityRelationshipModel2", None)
        self.__inEntityRelationshipModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Relationships_Restriction"):
                    opp_val = getattr(item, "Relationships_Restriction", None)
                    
                    if opp_val == self:
                        setattr(item, "Relationships_Restriction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Relationships_Restriction"):
                    opp_val = getattr(item, "Relationships_Restriction", None)
                    
                    setattr(item, "Relationships_Restriction", self)
                    

    @property
    def Entity_Relationship_Model93(self):
        return self.__Entity_Relationship_Model93

    @Entity_Relationship_Model93.setter
    def Entity_Relationship_Model93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Entity_Relationship_Model__Entity_Relationship_Model93", None)
        self.__Entity_Relationship_Model93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ERM_Has_ConnectionRelationship2Entity"):
                opp_val = getattr(old_value, "ERM_Has_ConnectionRelationship2Entity", None)
                if opp_val == self:
                    setattr(old_value, "ERM_Has_ConnectionRelationship2Entity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ERM_Has_ConnectionRelationship2Entity"):
                opp_val = getattr(value, "ERM_Has_ConnectionRelationship2Entity", None)
                setattr(value, "ERM_Has_ConnectionRelationship2Entity", self)

    @property
    def Entity_Relationship_Model58(self):
        return self.__Entity_Relationship_Model58

    @Entity_Relationship_Model58.setter
    def Entity_Relationship_Model58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Entity_Relationship_Model__Entity_Relationship_Model58", None)
        self.__Entity_Relationship_Model58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ERM_Has_Rt"):
                opp_val = getattr(old_value, "ERM_Has_Rt", None)
                if opp_val == self:
                    setattr(old_value, "ERM_Has_Rt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ERM_Has_Rt"):
                opp_val = getattr(value, "ERM_Has_Rt", None)
                setattr(value, "ERM_Has_Rt", self)

    @property
    def inEntityRelationshipModel10(self):
        return self.__inEntityRelationshipModel10

    @inEntityRelationshipModel10.setter
    def inEntityRelationshipModel10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Entity_Relationship_Model__inEntityRelationshipModel10", None)
        self.__inEntityRelationshipModel10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Connection_Generalization_Entity"):
                    opp_val = getattr(item, "Connection_Generalization_Entity", None)
                    
                    if opp_val == self:
                        setattr(item, "Connection_Generalization_Entity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Connection_Generalization_Entity"):
                    opp_val = getattr(item, "Connection_Generalization_Entity", None)
                    
                    setattr(item, "Connection_Generalization_Entity", self)
                    

    @property
    def entityrelationship_Entity_Relationship_Model46(self):
        return self.__entityrelationship_Entity_Relationship_Model46

    @entityrelationship_Entity_Relationship_Model46.setter
    def entityrelationship_Entity_Relationship_Model46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Entity_Relationship_Model__entityrelationship_Entity_Relationship_Model46", None)
        self.__entityrelationship_Entity_Relationship_Model46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityrelationship_Attribute45"):
                opp_val = getattr(old_value, "entityrelationship_Attribute45", None)
                if opp_val == self:
                    setattr(old_value, "entityrelationship_Attribute45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityrelationship_Attribute45"):
                opp_val = getattr(value, "entityrelationship_Attribute45", None)
                setattr(value, "entityrelationship_Attribute45", self)

    @property
    def Entity_Relationship_Model99(self):
        return self.__Entity_Relationship_Model99

    @Entity_Relationship_Model99.setter
    def Entity_Relationship_Model99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Entity_Relationship_Model__Entity_Relationship_Model99", None)
        self.__Entity_Relationship_Model99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ERM_HasConnectionEntityRelationship2Attribute"):
                opp_val = getattr(old_value, "ERM_HasConnectionEntityRelationship2Attribute", None)
                if opp_val == self:
                    setattr(old_value, "ERM_HasConnectionEntityRelationship2Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ERM_HasConnectionEntityRelationship2Attribute"):
                opp_val = getattr(value, "ERM_HasConnectionEntityRelationship2Attribute", None)
                setattr(value, "ERM_HasConnectionEntityRelationship2Attribute", self)

    @property
    def inEntityRelationshipModel(self):
        return self.__inEntityRelationshipModel

    @inEntityRelationshipModel.setter
    def inEntityRelationshipModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Entity_Relationship_Model__inEntityRelationshipModel", None)
        self.__inEntityRelationshipModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Elements_with_Attributes"):
                    opp_val = getattr(item, "Elements_with_Attributes", None)
                    
                    if opp_val == self:
                        setattr(item, "Elements_with_Attributes", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Elements_with_Attributes"):
                    opp_val = getattr(item, "Elements_with_Attributes", None)
                    
                    setattr(item, "Elements_with_Attributes", self)
                    

    @property
    def inEntityRelationshipModel12(self):
        return self.__inEntityRelationshipModel12

    @inEntityRelationshipModel12.setter
    def inEntityRelationshipModel12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Entity_Relationship_Model__inEntityRelationshipModel12", None)
        self.__inEntityRelationshipModel12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Connection_E_R_Restriction"):
                    opp_val = getattr(item, "Connection_E_R_Restriction", None)
                    
                    if opp_val == self:
                        setattr(item, "Connection_E_R_Restriction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Connection_E_R_Restriction"):
                    opp_val = getattr(item, "Connection_E_R_Restriction", None)
                    
                    setattr(item, "Connection_E_R_Restriction", self)
                    

    @property
    def entityrelationship_Entity_Relationship_Model(self):
        return self.__entityrelationship_Entity_Relationship_Model

    @entityrelationship_Entity_Relationship_Model.setter
    def entityrelationship_Entity_Relationship_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Entity_Relationship_Model__entityrelationship_Entity_Relationship_Model", None)
        self.__entityrelationship_Entity_Relationship_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "entityrelationship_Attribute"):
                    opp_val = getattr(item, "entityrelationship_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "entityrelationship_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entityrelationship_Attribute"):
                    opp_val = getattr(item, "entityrelationship_Attribute", None)
                    
                    setattr(item, "entityrelationship_Attribute", self)
                    

    @property
    def inEntityRelationshipModel6(self):
        return self.__inEntityRelationshipModel6

    @inEntityRelationshipModel6.setter
    def inEntityRelationshipModel6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Entity_Relationship_Model__inEntityRelationshipModel6", None)
        self.__inEntityRelationshipModel6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Connection_Relationship2Entity"):
                    opp_val = getattr(item, "Connection_Relationship2Entity", None)
                    
                    if opp_val == self:
                        setattr(item, "Connection_Relationship2Entity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Connection_Relationship2Entity"):
                    opp_val = getattr(item, "Connection_Relationship2Entity", None)
                    
                    setattr(item, "Connection_Relationship2Entity", self)
                    

    @property
    def Entity_Relationship_Model68(self):
        return self.__Entity_Relationship_Model68

    @Entity_Relationship_Model68.setter
    def Entity_Relationship_Model68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Entity_Relationship_Model__Entity_Relationship_Model68", None)
        self.__Entity_Relationship_Model68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ERM_Has_G"):
                opp_val = getattr(old_value, "ERM_Has_G", None)
                if opp_val == self:
                    setattr(old_value, "ERM_Has_G", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ERM_Has_G"):
                opp_val = getattr(value, "ERM_Has_G", None)
                setattr(value, "ERM_Has_G", self)

    @property
    def inEntityRelationshipModel17(self):
        return self.__inEntityRelationshipModel17

    @inEntityRelationshipModel17.setter
    def inEntityRelationshipModel17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Entity_Relationship_Model__inEntityRelationshipModel17", None)
        self.__inEntityRelationshipModel17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Generalization"):
                    opp_val = getattr(item, "Generalization", None)
                    
                    if opp_val == self:
                        setattr(item, "Generalization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Generalization"):
                    opp_val = getattr(item, "Generalization", None)
                    
                    setattr(item, "Generalization", self)
                    

    @property
    def Entity_Relationship_Model(self):
        return self.__Entity_Relationship_Model

    @Entity_Relationship_Model.setter
    def Entity_Relationship_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Entity_Relationship_Model__Entity_Relationship_Model", None)
        self.__Entity_Relationship_Model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ERM_Has_E"):
                opp_val = getattr(old_value, "ERM_Has_E", None)
                if opp_val == self:
                    setattr(old_value, "ERM_Has_E", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ERM_Has_E"):
                opp_val = getattr(value, "ERM_Has_E", None)
                setattr(value, "ERM_Has_E", self)

    @property
    def Entity_Relationship_Model64(self):
        return self.__Entity_Relationship_Model64

    @Entity_Relationship_Model64.setter
    def Entity_Relationship_Model64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Entity_Relationship_Model__Entity_Relationship_Model64", None)
        self.__Entity_Relationship_Model64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ERM_Has_Rt2"):
                opp_val = getattr(old_value, "ERM_Has_Rt2", None)
                if opp_val == self:
                    setattr(old_value, "ERM_Has_Rt2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ERM_Has_Rt2"):
                opp_val = getattr(value, "ERM_Has_Rt2", None)
                setattr(value, "ERM_Has_Rt2", self)

    @property
    def inEntityRelationshipModel14(self):
        return self.__inEntityRelationshipModel14

    @inEntityRelationshipModel14.setter
    def inEntityRelationshipModel14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Entity_Relationship_Model__inEntityRelationshipModel14", None)
        self.__inEntityRelationshipModel14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Connection_With_Attribute"):
                    opp_val = getattr(item, "Connection_With_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "Connection_With_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Connection_With_Attribute"):
                    opp_val = getattr(item, "Connection_With_Attribute", None)
                    
                    setattr(item, "Connection_With_Attribute", self)
                    

    @property
    def Entity_Relationship_Model74(self):
        return self.__Entity_Relationship_Model74

    @Entity_Relationship_Model74.setter
    def Entity_Relationship_Model74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Entity_Relationship_Model__Entity_Relationship_Model74", None)
        self.__Entity_Relationship_Model74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ERM_Has_CEA"):
                opp_val = getattr(old_value, "ERM_Has_CEA", None)
                if opp_val == self:
                    setattr(old_value, "ERM_Has_CEA", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ERM_Has_CEA"):
                opp_val = getattr(value, "ERM_Has_CEA", None)
                setattr(value, "ERM_Has_CEA", self)

    @property
    def inEntityRelationshipModel8(self):
        return self.__inEntityRelationshipModel8

    @inEntityRelationshipModel8.setter
    def inEntityRelationshipModel8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Entity_Relationship_Model__inEntityRelationshipModel8", None)
        self.__inEntityRelationshipModel8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Connection_ConnectionEntityRelationship2Attribute"):
                    opp_val = getattr(item, "Connection_ConnectionEntityRelationship2Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "Connection_ConnectionEntityRelationship2Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Connection_ConnectionEntityRelationship2Attribute"):
                    opp_val = getattr(item, "Connection_ConnectionEntityRelationship2Attribute", None)
                    
                    setattr(item, "Connection_ConnectionEntityRelationship2Attribute", self)
                    

    @property
    def Entity_Relationship_Model81(self):
        return self.__Entity_Relationship_Model81

    @Entity_Relationship_Model81.setter
    def Entity_Relationship_Model81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Entity_Relationship_Model__Entity_Relationship_Model81", None)
        self.__Entity_Relationship_Model81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ERM_Has_Gen"):
                opp_val = getattr(old_value, "ERM_Has_Gen", None)
                if opp_val == self:
                    setattr(old_value, "ERM_Has_Gen", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ERM_Has_Gen"):
                opp_val = getattr(value, "ERM_Has_Gen", None)
                setattr(value, "ERM_Has_Gen", self)

    @property
    def Entity_Relationship_Model87(self):
        return self.__Entity_Relationship_Model87

    @Entity_Relationship_Model87.setter
    def Entity_Relationship_Model87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Entity_Relationship_Model__Entity_Relationship_Model87", None)
        self.__Entity_Relationship_Model87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ERM_Has_ConnectionEntity2Relationship"):
                opp_val = getattr(old_value, "ERM_Has_ConnectionEntity2Relationship", None)
                if opp_val == self:
                    setattr(old_value, "ERM_Has_ConnectionEntity2Relationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ERM_Has_ConnectionEntity2Relationship"):
                opp_val = getattr(value, "ERM_Has_ConnectionEntity2Relationship", None)
                setattr(value, "ERM_Has_ConnectionEntity2Relationship", self)

class entityrelationship_Connection_E_R_Restriction:

    def __init__(self, type_restriction: str, Connection_E_R_Restriction: "entityrelationship_Entity_Relationship_Model" = None, entityrelationship_Connection_E_R_Restriction: "entityrelationship_Connection_EntityRelationship" = None, entityrelationship_Connection_E_R_Restriction61: "entityrelationship_Connection_EntityRelationship" = None, ERM_Has_Rt2: "entityrelationship_Entity_Relationship_Model" = None):
        self.type_restriction = type_restriction
        self.Connection_E_R_Restriction = Connection_E_R_Restriction
        self.entityrelationship_Connection_E_R_Restriction = entityrelationship_Connection_E_R_Restriction
        self.entityrelationship_Connection_E_R_Restriction61 = entityrelationship_Connection_E_R_Restriction61
        self.ERM_Has_Rt2 = ERM_Has_Rt2
        
    @property
    def type_restriction(self) -> str:
        return self.__type_restriction

    @type_restriction.setter
    def type_restriction(self, type_restriction: str):
        self.__type_restriction = type_restriction

    @property
    def entityrelationship_Connection_E_R_Restriction61(self):
        return self.__entityrelationship_Connection_E_R_Restriction61

    @entityrelationship_Connection_E_R_Restriction61.setter
    def entityrelationship_Connection_E_R_Restriction61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Connection_E_R_Restriction__entityrelationship_Connection_E_R_Restriction61", None)
        self.__entityrelationship_Connection_E_R_Restriction61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityrelationship_Connection_EntityRelationship62"):
                opp_val = getattr(old_value, "entityrelationship_Connection_EntityRelationship62", None)
                if opp_val == self:
                    setattr(old_value, "entityrelationship_Connection_EntityRelationship62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityrelationship_Connection_EntityRelationship62"):
                opp_val = getattr(value, "entityrelationship_Connection_EntityRelationship62", None)
                setattr(value, "entityrelationship_Connection_EntityRelationship62", self)

    @property
    def ERM_Has_Rt2(self):
        return self.__ERM_Has_Rt2

    @ERM_Has_Rt2.setter
    def ERM_Has_Rt2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Connection_E_R_Restriction__ERM_Has_Rt2", None)
        self.__ERM_Has_Rt2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Entity_Relationship_Model64"):
                opp_val = getattr(old_value, "Entity_Relationship_Model64", None)
                if opp_val == self:
                    setattr(old_value, "Entity_Relationship_Model64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Entity_Relationship_Model64"):
                opp_val = getattr(value, "Entity_Relationship_Model64", None)
                setattr(value, "Entity_Relationship_Model64", self)

    @property
    def entityrelationship_Connection_E_R_Restriction(self):
        return self.__entityrelationship_Connection_E_R_Restriction

    @entityrelationship_Connection_E_R_Restriction.setter
    def entityrelationship_Connection_E_R_Restriction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Connection_E_R_Restriction__entityrelationship_Connection_E_R_Restriction", None)
        self.__entityrelationship_Connection_E_R_Restriction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityrelationship_Connection_EntityRelationship"):
                opp_val = getattr(old_value, "entityrelationship_Connection_EntityRelationship", None)
                if opp_val == self:
                    setattr(old_value, "entityrelationship_Connection_EntityRelationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityrelationship_Connection_EntityRelationship"):
                opp_val = getattr(value, "entityrelationship_Connection_EntityRelationship", None)
                setattr(value, "entityrelationship_Connection_EntityRelationship", self)

    @property
    def Connection_E_R_Restriction(self):
        return self.__Connection_E_R_Restriction

    @Connection_E_R_Restriction.setter
    def Connection_E_R_Restriction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Connection_E_R_Restriction__Connection_E_R_Restriction", None)
        self.__Connection_E_R_Restriction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inEntityRelationshipModel12"):
                opp_val = getattr(old_value, "inEntityRelationshipModel12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inEntityRelationshipModel12"):
                opp_val = getattr(value, "inEntityRelationshipModel12", None)
                if opp_val is None:
                    setattr(value, "inEntityRelationshipModel12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class entityrelationship_Connection_Generalization_Entity:

    def __init__(self, minimum_cardinality: str, maximum_cardinality: str, Connection_Generalization_Entity: "entityrelationship_Entity_Relationship_Model" = None, entityrelationship_Connection_Generalization_Entity: "entityrelationship_Generalization" = None, entityrelationship_Connection_Generalization_Entity78: "entityrelationship_Entity" = None, ERM_Has_Gen: "entityrelationship_Entity_Relationship_Model" = None):
        self.minimum_cardinality = minimum_cardinality
        self.maximum_cardinality = maximum_cardinality
        self.Connection_Generalization_Entity = Connection_Generalization_Entity
        self.entityrelationship_Connection_Generalization_Entity = entityrelationship_Connection_Generalization_Entity
        self.entityrelationship_Connection_Generalization_Entity78 = entityrelationship_Connection_Generalization_Entity78
        self.ERM_Has_Gen = ERM_Has_Gen
        
    @property
    def maximum_cardinality(self) -> str:
        return self.__maximum_cardinality

    @maximum_cardinality.setter
    def maximum_cardinality(self, maximum_cardinality: str):
        self.__maximum_cardinality = maximum_cardinality

    @property
    def minimum_cardinality(self) -> str:
        return self.__minimum_cardinality

    @minimum_cardinality.setter
    def minimum_cardinality(self, minimum_cardinality: str):
        self.__minimum_cardinality = minimum_cardinality

    @property
    def Connection_Generalization_Entity(self):
        return self.__Connection_Generalization_Entity

    @Connection_Generalization_Entity.setter
    def Connection_Generalization_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Connection_Generalization_Entity__Connection_Generalization_Entity", None)
        self.__Connection_Generalization_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inEntityRelationshipModel10"):
                opp_val = getattr(old_value, "inEntityRelationshipModel10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inEntityRelationshipModel10"):
                opp_val = getattr(value, "inEntityRelationshipModel10", None)
                if opp_val is None:
                    setattr(value, "inEntityRelationshipModel10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def entityrelationship_Connection_Generalization_Entity78(self):
        return self.__entityrelationship_Connection_Generalization_Entity78

    @entityrelationship_Connection_Generalization_Entity78.setter
    def entityrelationship_Connection_Generalization_Entity78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Connection_Generalization_Entity__entityrelationship_Connection_Generalization_Entity78", None)
        self.__entityrelationship_Connection_Generalization_Entity78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityrelationship_Entity79"):
                opp_val = getattr(old_value, "entityrelationship_Entity79", None)
                if opp_val == self:
                    setattr(old_value, "entityrelationship_Entity79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityrelationship_Entity79"):
                opp_val = getattr(value, "entityrelationship_Entity79", None)
                setattr(value, "entityrelationship_Entity79", self)

    @property
    def entityrelationship_Connection_Generalization_Entity(self):
        return self.__entityrelationship_Connection_Generalization_Entity

    @entityrelationship_Connection_Generalization_Entity.setter
    def entityrelationship_Connection_Generalization_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Connection_Generalization_Entity__entityrelationship_Connection_Generalization_Entity", None)
        self.__entityrelationship_Connection_Generalization_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityrelationship_Generalization76"):
                opp_val = getattr(old_value, "entityrelationship_Generalization76", None)
                if opp_val == self:
                    setattr(old_value, "entityrelationship_Generalization76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityrelationship_Generalization76"):
                opp_val = getattr(value, "entityrelationship_Generalization76", None)
                setattr(value, "entityrelationship_Generalization76", self)

    @property
    def ERM_Has_Gen(self):
        return self.__ERM_Has_Gen

    @ERM_Has_Gen.setter
    def ERM_Has_Gen(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityrelationship_Connection_Generalization_Entity__ERM_Has_Gen", None)
        self.__ERM_Has_Gen = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Entity_Relationship_Model81"):
                opp_val = getattr(old_value, "Entity_Relationship_Model81", None)
                if opp_val == self:
                    setattr(old_value, "Entity_Relationship_Model81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Entity_Relationship_Model81"):
                opp_val = getattr(value, "Entity_Relationship_Model81", None)
                setattr(value, "Entity_Relationship_Model81", self)
