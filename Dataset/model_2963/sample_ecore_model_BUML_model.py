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
sample_Person = Class(name="sample::Person")
sample_Car = Class(name="sample::Car")

# sample_Person class attributes and methods
sample_Person_firstName: Property = Property(name="firstName", type=StringType)
sample_Person_lastName: Property = Property(name="lastName", type=StringType)
sample_Person_m_buy: Method = Method(name="buy", parameters={Parameter(name='car')})
sample_Person.attributes={sample_Person_lastName, sample_Person_firstName}
sample_Person.methods={sample_Person_m_buy}

# sample_Car class attributes and methods
sample_Car_horsePower: Property = Property(name="horsePower", type=IntegerType)
sample_Car.attributes={sample_Car_horsePower}

# Relationships
ownedCars0: BinaryAssociation = BinaryAssociation(
    name="ownedCars0",
    ends={
        Property(name="sample_Car", type=sample_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_Person", type=sample_Car, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="sample",
    types={sample_Person, sample_Car},
    associations={ownedCars0},
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