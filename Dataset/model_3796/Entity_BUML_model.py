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
Entity_System = Class(name="Entity::System")
Entity_Entity = Class(name="Entity::Entity")

# Entity_System class attributes and methods

# Entity_Entity class attributes and methods
Entity_Entity_name: Property = Property(name="name", type=StringType)
Entity_Entity_inDomain: Property = Property(name="inDomain", type=StringType)
Entity_Entity.attributes={Entity_Entity_inDomain, Entity_Entity_name}

# Relationships
entity0: BinaryAssociation = BinaryAssociation(
    name="entity0",
    ends={
        Property(name="Entity", type=Entity_System, multiplicity=Multiplicity(1, 1)),
        Property(name="system", type=Entity_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
system1: BinaryAssociation = BinaryAssociation(
    name="system1",
    ends={
        Property(name="System", type=Entity_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entity", type=Entity_System, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Entity",
    types={Entity_System, Entity_Entity},
    associations={entity0, system1},
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