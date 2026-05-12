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
PASSENGER = Class(name="PASSENGER")
FLIGHT = Class(name="FLIGHT")
RESERVATION_SYSTEM = Class(name="RESERVATION_SYSTEM")

# PASSENGER class attributes and methods
PASSENGER_Pass_Name: Property = Property(name="Pass_Name", type=StringType)
PASSENGER_Pass_ID: Property = Property(name="Pass_ID", type=IntegerType)
PASSENGER_Pass_Address: Property = Property(name="Pass_Address", type=StringType)
PASSENGER.attributes={PASSENGER_Pass_Address, PASSENGER_Pass_Name, PASSENGER_Pass_ID}

# FLIGHT class attributes and methods
FLIGHT_Flight_No_: Property = Property(name="Flight_No_", type=IntegerType)
FLIGHT_Flight_Name: Property = Property(name="Flight_Name", type=StringType)
FLIGHT.attributes={FLIGHT_Flight_No_, FLIGHT_Flight_Name}

# RESERVATION_SYSTEM class attributes and methods
RESERVATION_SYSTEM_Reservation_ID: Property = Property(name="Reservation_ID", type=IntegerType)
RESERVATION_SYSTEM_Reservation_Date: Property = Property(name="Reservation_Date", type=IntegerType)
RESERVATION_SYSTEM.attributes={RESERVATION_SYSTEM_Reservation_ID, RESERVATION_SYSTEM_Reservation_Date}

# Relationships
FLIGHT_RESERVATION_SYSTEM: BinaryAssociation = BinaryAssociation(
    name="FLIGHT_RESERVATION_SYSTEM",
    ends={
        Property(name="FLIGHT_RESERVATION_SYSTEM_00", type=RESERVATION_SYSTEM, multiplicity=Multiplicity(0, 1)),
        Property(name="RESERVATION_SYSTEM1", type=FLIGHT, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_rZE1INXiEeiRsZPYq94rUg",
    types={PASSENGER, FLIGHT, RESERVATION_SYSTEM},
    associations={FLIGHT_RESERVATION_SYSTEM},
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