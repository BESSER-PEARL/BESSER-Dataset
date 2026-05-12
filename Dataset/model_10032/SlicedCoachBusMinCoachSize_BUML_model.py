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
CoachBus_Coach = Class(name="CoachBus_Coach")

# CoachBus_Coach class attributes and methods
CoachBus_Coach_noOfSeats: Property = Property(name="noOfSeats", type=IntegerType)
CoachBus_Coach.attributes={CoachBus_Coach_noOfSeats}


# OCL Constraints
MinCoachSize: Constraint = Constraint(
    name="MinCoachSize",
    context=CoachBus_Coach,
    expression="context Coach inv: self.noOfSeats >=(10)",
    language="OCL"
)

# Domain Model
domain_model = DomainModel(
    name="CoachBus",
    types={CoachBus_Coach},
    associations={},
    constraints={MinCoachSize},
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