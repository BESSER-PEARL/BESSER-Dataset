####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
entity_Entity = Class(name="entity::Entity")
Type = Class(name="Type")
entity_Reference = Class(name="entity::Reference")
entity_Attribute = Class(name="entity::Attribute")
entity_Datatype = Class(name="entity::Datatype")
entity_NamedElement = Class(name="entity::NamedElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
entity_Type = Class(name="entity::Type")
entity_Namespace = Class(name="entity::Namespace")

# entity_Entity class attributes and methods

# Type class attributes and methods

# entity_Reference class attributes and methods

# entity_Attribute class attributes and methods

# entity_Datatype class attributes and methods

# entity_NamedElement class attributes and methods
entity_NamedElement_name: Property = Property(name="name", type=StringType)
entity_NamedElement.attributes={entity_NamedElement_name}

# NamedElement class attributes and methods

# entity_Type class attributes and methods

# entity_Namespace class attributes and methods

# Relationships
references0: BinaryAssociation = BinaryAssociation(
    name="references0",
    ends={
        Property(name="entity_Reference", type=entity_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_Entity", type=entity_Reference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes1: BinaryAssociation = BinaryAssociation(
    name="attributes1",
    ends={
        Property(name="entity_Attribute", type=entity_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_Entity2", type=entity_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types3: BinaryAssociation = BinaryAssociation(
    name="types3",
    ends={
        Property(name="entity_Type", type=entity_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_Namespace", type=entity_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nested5: BinaryAssociation = BinaryAssociation(
    name="nested5",
    ends={
        Property(name="entity_Namespace6", type=entity_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_Namespace4", type=entity_Namespace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="entity_Entity9", type=entity_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_Reference8", type=entity_Entity, multiplicity=Multiplicity(0, 1))
    }
)
datatype10: BinaryAssociation = BinaryAssociation(
    name="datatype10",
    ends={
        Property(name="entity_Datatype", type=entity_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_Attribute11", type=entity_Datatype, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_entity_Entity_Type = Generalization(general=Type, specific=entity_Entity)
gen_entity_Datatype_Type = Generalization(general=Type, specific=entity_Datatype)
gen_entity_Namespace_NamedElement = Generalization(general=NamedElement, specific=entity_Namespace)
gen_entity_Reference_NamedElement = Generalization(general=NamedElement, specific=entity_Reference)
gen_entity_Type_NamedElement = Generalization(general=NamedElement, specific=entity_Type)
gen_entity_Attribute_NamedElement = Generalization(general=NamedElement, specific=entity_Attribute)

# Domain Model
domain_model = DomainModel(
    name="entity",
    types={entity_Entity, Type, entity_Reference, entity_Attribute, entity_Datatype, entity_NamedElement, NamedElement, entity_Type, entity_Namespace},
    associations={references0, attributes1, types3, nested5, type7, datatype10},
    generalizations={gen_entity_Entity_Type, gen_entity_Datatype_Type, gen_entity_Namespace_NamedElement, gen_entity_Reference_NamedElement, gen_entity_Type_NamedElement, gen_entity_Attribute_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)