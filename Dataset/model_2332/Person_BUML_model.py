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
Persons_PersonContainer = Class(name="Persons::PersonContainer")
Persons_Person = Class(name="Persons::Person")

# Persons_PersonContainer class attributes and methods

# Persons_Person class attributes and methods
Persons_Person_name: Property = Property(name="name", type=StringType)
Persons_Person_ID: Property = Property(name="ID", type=IntegerType)
Persons_Person.attributes={Persons_Person_name, Persons_Person_ID}

# Relationships
persons0: BinaryAssociation = BinaryAssociation(
    name="persons0",
    ends={
        Property(name="Persons_Person", type=Persons_PersonContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="Persons_PersonContainer", type=Persons_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Persons",
    types={Persons_PersonContainer, Persons_Person},
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