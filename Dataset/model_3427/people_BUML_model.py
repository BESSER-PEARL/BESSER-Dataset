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
people_Model = Class(name="people::Model")
people_Person = Class(name="people::Person")

# people_Model class attributes and methods

# people_Person class attributes and methods
people_Person_name: Property = Property(name="name", type=StringType)
people_Person.attributes={people_Person_name}

# Relationships
people0: BinaryAssociation = BinaryAssociation(
    name="people0",
    ends={
        Property(name="people_Person", type=people_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="people_Model", type=people_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="people",
    types={people_Model, people_Person},
    associations={people0},
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