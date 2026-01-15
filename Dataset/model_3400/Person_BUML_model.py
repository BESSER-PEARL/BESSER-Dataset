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
Person_Model = Class(name="Person::Model")
Person_Person = Class(name="Person::Person")

# Person_Model class attributes and methods

# Person_Person class attributes and methods
Person_Person_firstName: Property = Property(name="firstName", type=StringType)
Person_Person_lastName: Property = Property(name="lastName", type=StringType)
Person_Person.attributes={Person_Person_lastName, Person_Person_firstName}

# Relationships
people0: BinaryAssociation = BinaryAssociation(
    name="people0",
    ends={
        Property(name="Person_Person", type=Person_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="Person_Model", type=Person_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parents2: BinaryAssociation = BinaryAssociation(
    name="parents2",
    ends={
        Property(name="Person_Person3", type=Person_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="Person_Person1", type=Person_Person, multiplicity=Multiplicity(0, 2))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Person",
    types={Person_Model, Person_Person},
    associations={people0, parents2},
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