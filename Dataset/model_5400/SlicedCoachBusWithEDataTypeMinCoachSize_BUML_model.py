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
CoachBusWithEDataType_Coach = Class(name="CoachBusWithEDataType::Coach")

# CoachBusWithEDataType_Coach class attributes and methods
CoachBusWithEDataType_Coach_noOfSeats: Property = Property(name="noOfSeats", type=IntegerType)
CoachBusWithEDataType_Coach.attributes={CoachBusWithEDataType_Coach_noOfSeats}

# Domain Model
domain_model = DomainModel(
    name="CoachBusWithEDataType",
    types={CoachBusWithEDataType_Coach},
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