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

# Enumerations
MaintenanceState: Enumeration = Enumeration(
    name="MaintenanceState",
    literals={
            
    }
)

FlightState: Enumeration = Enumeration(
    name="FlightState",
    literals={
            
    }
)

# Classes
Airline = Class(name="Airline")
Flight = Class(name="Flight")
Airport = Class(name="Airport")
Pilot = Class(name="Pilot")
Aircraft = Class(name="Aircraft")
Company = Class(name="Company")
CoPilot = Class(name="CoPilot")
Navigator = Class(name="Navigator")
Captain = Class(name="Captain")

# Airline class attributes and methods
Airline_id: Property = Property(name="id", type=StringType)
Airline.attributes={Airline_id}

# Flight class attributes and methods
Flight_id: Property = Property(name="id", type=IntegerType)
Flight_departureTime: Property = Property(name="departureTime", type=DateType)
Flight_arrivalTime: Property = Property(name="arrivalTime", type=DateType)
Flight.attributes={Flight_id, Flight_arrivalTime, Flight_departureTime}

# Airport class attributes and methods
Airport_id: Property = Property(name="id", type=StringType)
Airport.attributes={Airport_id}

# Pilot class attributes and methods

# Aircraft class attributes and methods
Aircraft_state: Property = Property(name="state", type=MaintenanceState)
Aircraft_flightState: Property = Property(name="flightState", type=FlightState)
Aircraft.attributes={Aircraft_state, Aircraft_flightState}

# Company class attributes and methods

# CoPilot class attributes and methods

# Navigator class attributes and methods

# Captain class attributes and methods

# Relationships
Airline_Aircraft: BinaryAssociation = BinaryAssociation(
    name="Airline_Aircraft",
    ends={
        Property(name="aircraft0", type=Aircraft, multiplicity=Multiplicity(0, 9999)),
        Property(name="owns1", type=Airline, multiplicity=Multiplicity(0, 9999))
    }
)
Company_Pilot: BinaryAssociation = BinaryAssociation(
    name="Company_Pilot",
    ends={
        Property(name="pilot2", type=Pilot, multiplicity=Multiplicity(1, 9999)),
        Property(name="company3", type=Company, multiplicity=Multiplicity(1, 1))
    }
)
Flights_Airport: BinaryAssociation = BinaryAssociation(
    name="Flights_Airport",
    ends={
        Property(name="airport4", type=Airport, multiplicity=Multiplicity(1, 1)),
        Property(name="arrives_at5", type=Flight, multiplicity=Multiplicity(0, 9999))
    }
)
Flights_Airport2: BinaryAssociation = BinaryAssociation(
    name="Flights_Airport2",
    ends={
        Property(name="airport6", type=Airport, multiplicity=Multiplicity(1, 1)),
        Property(name="departs_from7", type=Flight, multiplicity=Multiplicity(0, 9999))
    }
)
Airline_Flight: BinaryAssociation = BinaryAssociation(
    name="Airline_Flight",
    ends={
        Property(name="flight8", type=Flight, multiplicity=Multiplicity(0, 9999)),
        Property(name="operates9", type=Airline, multiplicity=Multiplicity(1, 1))
    }
)
Flight_Aircraft: BinaryAssociation = BinaryAssociation(
    name="Flight_Aircraft",
    ends={
        Property(name="aircraft10", type=Aircraft, multiplicity=Multiplicity(1, 1)),
        Property(name="uses11", type=Flight, multiplicity=Multiplicity(0, 9999))
    }
)
Aircraft_Pilot: BinaryAssociation = BinaryAssociation(
    name="Aircraft_Pilot",
    ends={
        Property(name="employs12", type=Pilot, multiplicity=Multiplicity(0, 9999)),
        Property(name="pilots13", type=Aircraft, multiplicity=Multiplicity(0, 9999))
    }
)
Aircraft_CoPilot: BinaryAssociation = BinaryAssociation(
    name="Aircraft_CoPilot",
    ends={
        Property(name="requires14", type=CoPilot, multiplicity=Multiplicity(1, 9999)),
        Property(name="copilots15", type=Aircraft, multiplicity=Multiplicity(0, 9999))
    }
)
Aircraft_Captain: BinaryAssociation = BinaryAssociation(
    name="Aircraft_Captain",
    ends={
        Property(name="requires16", type=Captain, multiplicity=Multiplicity(1, 9999)),
        Property(name="captains17", type=Aircraft, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_5717d9fb_895c_434f_83a9_338c5c1af43d",
    types={Airline, Flight, Airport, Pilot, Aircraft, Company, CoPilot, Navigator, Captain, MaintenanceState, FlightState},
    associations={Airline_Aircraft, Company_Pilot, Flights_Airport, Flights_Airport2, Airline_Flight, Flight_Aircraft, Aircraft_Pilot, Aircraft_CoPilot, Aircraft_Captain},
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