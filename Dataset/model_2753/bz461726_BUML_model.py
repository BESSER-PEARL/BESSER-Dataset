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
PK461726_B461726 = Class(name="PK461726::B461726")
PK461726_A461726 = Class(name="PK461726::A461726")

# PK461726_B461726 class attributes and methods
PK461726_B461726_name: Property = Property(name="name", type=StringType)
PK461726_B461726.attributes={PK461726_B461726_name}

# PK461726_A461726 class attributes and methods
PK461726_A461726_name: Property = Property(name="name", type=StringType)
PK461726_A461726.attributes={PK461726_A461726_name}

# Relationships
bs0: BinaryAssociation = BinaryAssociation(
    name="bs0",
    ends={
        Property(name="B461726", type=PK461726_A461726, multiplicity=Multiplicity(1, 1)),
        Property(name="as", type=PK461726_B461726, multiplicity=Multiplicity(0, 9999))
    }
)
as1: BinaryAssociation = BinaryAssociation(
    name="as1",
    ends={
        Property(name="A461726", type=PK461726_B461726, multiplicity=Multiplicity(1, 1)),
        Property(name="bs", type=PK461726_A461726, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="PK461726",
    types={PK461726_B461726, PK461726_A461726},
    associations={bs0, as1},
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