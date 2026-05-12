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
CheckStaff = Class(name="CheckStaff")
Luggage = Class(name="Luggage")
Passenger = Class(name="Passenger")
Ticket = Class(name="Ticket")

# CheckStaff class attributes and methods
CheckStaff_name: Property = Property(name="name", type=StringType)
CheckStaff.attributes={CheckStaff_name}

# Luggage class attributes and methods
Luggage_weight: Property = Property(name="weight", type=IntegerType)
Luggage.attributes={Luggage_weight}

# Passenger class attributes and methods
Passenger_name: Property = Property(name="name", type=StringType)
Passenger.attributes={Passenger_name}

# Ticket class attributes and methods
Ticket_no: Property = Property(name="no", type=IntegerType)
Ticket.attributes={Ticket_no}

# Relationships
luggage_Passenger_Luggage_0: BinaryAssociation = BinaryAssociation(
    name="luggage_Passenger_Luggage_0",
    ends={
        Property(name="passenger0", type=Passenger, multiplicity=Multiplicity(0, 1)),
        Property(name="luggage1", type=Luggage, multiplicity=Multiplicity(0, 1))
    }
)
ticket_Passenger_Ticket_1: BinaryAssociation = BinaryAssociation(
    name="ticket_Passenger_Ticket_1",
    ends={
        Property(name="passenger2", type=Passenger, multiplicity=Multiplicity(0, 1)),
        Property(name="ticket3", type=Ticket, multiplicity=Multiplicity(0, 1))
    }
)
Luggage_CheckStaff: BinaryAssociation = BinaryAssociation(
    name="Luggage_CheckStaff",
    ends={
        Property(name="checkStaff4", type=CheckStaff, multiplicity=Multiplicity(0, 1)),
        Property(name="luggage5", type=Luggage, multiplicity=Multiplicity(0, 1))
    }
)
Passenger_CheckStaff: BinaryAssociation = BinaryAssociation(
    name="Passenger_CheckStaff",
    ends={
        Property(name="checkStaff6", type=CheckStaff, multiplicity=Multiplicity(0, 1)),
        Property(name="passenger7", type=Passenger, multiplicity=Multiplicity(0, 1))
    }
)
CheckStaff_Ticket: BinaryAssociation = BinaryAssociation(
    name="CheckStaff_Ticket",
    ends={
        Property(name="ticket8", type=Ticket, multiplicity=Multiplicity(0, 1)),
        Property(name="checkStaff9", type=CheckStaff, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_EIH10Jc6EeiLAcQp8WkNkw",
    types={CheckStaff, Luggage, Passenger, Ticket},
    associations={luggage_Passenger_Luggage_0, ticket_Passenger_Ticket_1, Luggage_CheckStaff, Passenger_CheckStaff, CheckStaff_Ticket},
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