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
ER_ERSchema = Class(name="ER::ERSchema")
ER_Entity = Class(name="ER::Entity")
ER_Relship = Class(name="ER::Relship")
ER_ERAttribute = Class(name="ER::ERAttribute")
ER_RelshipEnd = Class(name="ER::RelshipEnd")

# ER_ERSchema class attributes and methods
ER_ERSchema_name: Property = Property(name="name", type=StringType)
ER_ERSchema.attributes={ER_ERSchema_name}

# ER_Entity class attributes and methods
ER_Entity_name: Property = Property(name="name", type=StringType)
ER_Entity.attributes={ER_Entity_name}

# ER_Relship class attributes and methods
ER_Relship_name: Property = Property(name="name", type=StringType)
ER_Relship.attributes={ER_Relship_name}

# ER_ERAttribute class attributes and methods
ER_ERAttribute_name: Property = Property(name="name", type=StringType)
ER_ERAttribute_isKey: Property = Property(name="isKey", type=BooleanType)
ER_ERAttribute.attributes={ER_ERAttribute_name, ER_ERAttribute_isKey}

# ER_RelshipEnd class attributes and methods
ER_RelshipEnd_name: Property = Property(name="name", type=StringType)
ER_RelshipEnd.attributes={ER_RelshipEnd_name}

# Relationships
entities0: BinaryAssociation = BinaryAssociation(
    name="entities0",
    ends={
        Property(name="Entity", type=ER_ERSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema", type=ER_Entity, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
relships1: BinaryAssociation = BinaryAssociation(
    name="relships1",
    ends={
        Property(name="Relship", type=ER_ERSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema2", type=ER_Relship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attrs3: BinaryAssociation = BinaryAssociation(
    name="attrs3",
    ends={
        Property(name="ERAttribute", type=ER_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entity", type=ER_ERAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ends4: BinaryAssociation = BinaryAssociation(
    name="ends4",
    ends={
        Property(name="RelshipEnd", type=ER_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entity5", type=ER_RelshipEnd, multiplicity=Multiplicity(0, 9999))
    }
)
schema6: BinaryAssociation = BinaryAssociation(
    name="schema6",
    ends={
        Property(name="ERSchema", type=ER_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entities", type=ER_ERSchema, multiplicity=Multiplicity(1, 1))
    }
)
attrs7: BinaryAssociation = BinaryAssociation(
    name="attrs7",
    ends={
        Property(name="ERAttribute8", type=ER_Relship, multiplicity=Multiplicity(1, 1)),
        Property(name="relship", type=ER_ERAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ends9: BinaryAssociation = BinaryAssociation(
    name="ends9",
    ends={
        Property(name="RelshipEnd11", type=ER_Relship, multiplicity=Multiplicity(1, 1)),
        Property(name="relship10", type=ER_RelshipEnd, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
schema12: BinaryAssociation = BinaryAssociation(
    name="schema12",
    ends={
        Property(name="ERSchema13", type=ER_Relship, multiplicity=Multiplicity(1, 1)),
        Property(name="relships", type=ER_ERSchema, multiplicity=Multiplicity(1, 1))
    }
)
relship14: BinaryAssociation = BinaryAssociation(
    name="relship14",
    ends={
        Property(name="Relship15", type=ER_RelshipEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="ends", type=ER_Relship, multiplicity=Multiplicity(1, 1))
    }
)
entity16: BinaryAssociation = BinaryAssociation(
    name="entity16",
    ends={
        Property(name="Entity18", type=ER_RelshipEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="ends17", type=ER_Entity, multiplicity=Multiplicity(1, 1))
    }
)
entity19: BinaryAssociation = BinaryAssociation(
    name="entity19",
    ends={
        Property(name="Entity20", type=ER_ERAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attrs", type=ER_Entity, multiplicity=Multiplicity(0, 1))
    }
)
relship21: BinaryAssociation = BinaryAssociation(
    name="relship21",
    ends={
        Property(name="attrs22", type=ER_Relship, multiplicity=Multiplicity(0, 1)),
        Property(name="Relship23", type=ER_ERAttribute, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="ER",
    types={ER_ERSchema, ER_Entity, ER_Relship, ER_ERAttribute, ER_RelshipEnd},
    associations={entities0, relships1, attrs3, ends4, schema6, attrs7, ends9, schema12, relship14, entity16, entity19, relship21},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)