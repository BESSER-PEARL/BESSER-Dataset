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
personDsl_PersonContainer = Class(name="personDsl::PersonContainer")
personDsl_Person = Class(name="personDsl::Person")

# personDsl_PersonContainer class attributes and methods

# personDsl_Person class attributes and methods
personDsl_Person_ID: Property = Property(name="ID", type=IntegerType)
personDsl_Person_name: Property = Property(name="name", type=StringType)
personDsl_Person.attributes={personDsl_Person_name, personDsl_Person_ID}

# Relationships
persons0: BinaryAssociation = BinaryAssociation(
    name="persons0",
    ends={
        Property(name="personDsl_Person", type=personDsl_PersonContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="personDsl_PersonContainer", type=personDsl_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="personDsl",
    types={personDsl_PersonContainer, personDsl_Person},
    associations={persons0},
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