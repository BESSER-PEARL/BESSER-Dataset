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
panamaNeo4j_Officer = Class(name="panamaNeo4j::Officer")
panamaNeo4j_Entity = Class(name="panamaNeo4j::Entity")

# panamaNeo4j_Officer class attributes and methods
panamaNeo4j_Officer_name: Property = Property(name="name", type=StringType)
panamaNeo4j_Officer.attributes={panamaNeo4j_Officer_name}

# panamaNeo4j_Entity class attributes and methods
panamaNeo4j_Entity_name: Property = Property(name="name", type=StringType)
panamaNeo4j_Entity.attributes={panamaNeo4j_Entity_name}

# Relationships
OFFICER_OF0: BinaryAssociation = BinaryAssociation(
    name="OFFICER_OF0",
    ends={
        Property(name="panamaNeo4j_Entity", type=panamaNeo4j_Officer, multiplicity=Multiplicity(1, 1)),
        Property(name="panamaNeo4j_Officer", type=panamaNeo4j_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="panamaNeo4j",
    types={panamaNeo4j_Officer, panamaNeo4j_Entity},
    associations={OFFICER_OF0},
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