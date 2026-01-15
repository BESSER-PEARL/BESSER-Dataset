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
PersonsRegister_PersonsRegister = Class(name="PersonsRegister::PersonsRegister")
PersonsRegister_Person = Class(name="PersonsRegister::Person")

# PersonsRegister_PersonsRegister class attributes and methods

# PersonsRegister_Person class attributes and methods
PersonsRegister_Person_lastName: Property = Property(name="lastName", type=StringType)
PersonsRegister_Person_identity: Property = Property(name="identity", type=StringType)
PersonsRegister_Person_firstName: Property = Property(name="firstName", type=StringType)
PersonsRegister_Person.attributes={PersonsRegister_Person_lastName, PersonsRegister_Person_identity, PersonsRegister_Person_firstName}

# Relationships
persons0: BinaryAssociation = BinaryAssociation(
    name="persons0",
    ends={
        Property(name="PersonsRegister_Person", type=PersonsRegister_PersonsRegister, multiplicity=Multiplicity(1, 1)),
        Property(name="PersonsRegister_PersonsRegister", type=PersonsRegister_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="PersonsRegister",
    types={PersonsRegister_PersonsRegister, PersonsRegister_Person},
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