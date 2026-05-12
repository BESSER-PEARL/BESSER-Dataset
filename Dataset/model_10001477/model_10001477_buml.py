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
Vehicle_Interface = Class(name="Vehicle_Interface")
small = Class(name="small")
medium = Class(name="medium")
large = Class(name="large")
XL = Class(name="XL")
spot = Class(name="spot")
ValleyParking = Class(name="ValleyParking")
Ticket = Class(name="Ticket")

# Vehicle_Interface class attributes and methods

# small class attributes and methods

# medium class attributes and methods

# large class attributes and methods

# XL class attributes and methods

# spot class attributes and methods
spot_size: Property = Property(name="size", type=IntegerType)
spot_id: Property = Property(name="id", type=StringType)
spot_parkedVehicle: Property = Property(name="parkedVehicle", type=Vehicle_Interface)
spot.attributes={spot_parkedVehicle, spot_id, spot_size}

# ValleyParking class attributes and methods

# Ticket class attributes and methods
Ticket_id: Property = Property(name="id", type=StringType)
Ticket.attributes={Ticket_id}

# Domain Model
domain_model = DomainModel(
    name="_9Y2WAHONEeivVvskFc69VA",
    types={Vehicle_Interface, small, medium, large, XL, spot, ValleyParking, Ticket},
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