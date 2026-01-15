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
persons_Person = Class(name="persons::Person")

# persons_Person class attributes and methods
persons_Person_id: Property = Property(name="id", type=StringType)
persons_Person_firstName: Property = Property(name="firstName", type=StringType)
persons_Person_lastName: Property = Property(name="lastName", type=StringType)
persons_Person.attributes={persons_Person_firstName, persons_Person_id, persons_Person_lastName}

# Domain Model
domain_model = DomainModel(
    name="persons",
    types={persons_Person},
    associations={},
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