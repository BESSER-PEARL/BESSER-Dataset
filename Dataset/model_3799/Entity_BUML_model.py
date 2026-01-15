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
era_Attribute = Class(name="era::Attribute")
era_System = Class(name="era::System")
era_Entity = Class(name="era::Entity")
era_Relationship = Class(name="era::Relationship")

# era_Attribute class attributes and methods
era_Attribute_name: Property = Property(name="name", type=StringType)
era_Attribute.attributes={era_Attribute_name}

# era_System class attributes and methods

# era_Entity class attributes and methods
era_Entity_name: Property = Property(name="name", type=StringType)
era_Entity_inDomain: Property = Property(name="inDomain", type=StringType)
era_Entity.attributes={era_Entity_name, era_Entity_inDomain}

# era_Relationship class attributes and methods
era_Relationship_name: Property = Property(name="name", type=StringType)
era_Relationship.attributes={era_Relationship_name}

# Relationships
entities3: BinaryAssociation = BinaryAssociation(
    name="entities3",
    ends={
        Property(name="Entity4", type=era_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="relationships", type=era_Entity, multiplicity=Multiplicity(2, 9999))
    }
)
entity0: BinaryAssociation = BinaryAssociation(
    name="entity0",
    ends={
        Property(name="Entity", type=era_System, multiplicity=Multiplicity(1, 1)),
        Property(name="system", type=era_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
system1: BinaryAssociation = BinaryAssociation(
    name="system1",
    ends={
        Property(name="System", type=era_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entity", type=era_System, multiplicity=Multiplicity(0, 1))
    }
)
relationships2: BinaryAssociation = BinaryAssociation(
    name="relationships2",
    ends={
        Property(name="Relationship", type=era_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entities", type=era_Relationship, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="era",
    types={era_Attribute, era_System, era_Entity, era_Relationship},
    associations={entities3, entity0, system1, relationships2},
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