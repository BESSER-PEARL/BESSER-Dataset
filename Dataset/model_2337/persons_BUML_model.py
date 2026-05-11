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
persons_Person = Class(name="persons_Person")
persons_PersonGroup = Class(name="persons_PersonGroup")

# persons_Person class attributes and methods
persons_Person_name: Property = Property(name="name", type=StringType)
persons_Person.attributes={persons_Person_name}

# persons_PersonGroup class attributes and methods

# Relationships
persons0: BinaryAssociation = BinaryAssociation(
    name="persons0",
    ends={
        Property(name="persons_Person", type=persons_PersonGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="persons_PersonGroup", type=persons_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="persons",
    types={persons_Person, persons_PersonGroup},
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