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
Enumeration_: Enumeration = Enumeration(
    name="Enumeration",
    literals={
            
    }
)

# Classes
Customers = Class(name="Customers")
Flight = Class(name="Flight")
Routes = Class(name="Routes")
Plane = Class(name="Plane")
Airport = Class(name="Airport")
Ticket = Class(name="Ticket")
Reservation = Class(name="Reservation")
Seats = Class(name="Seats")

# Customers class attributes and methods
Customers_IdCustomer: Property = Property(name="IdCustomer", type=StringType)
Customers_NameCustomer: Property = Property(name="NameCustomer", type=StringType)
Customers_Email: Property = Property(name="Email", type=StringType)
Customers_Password: Property = Property(name="Password", type=StringType)
Customers.attributes={Customers_Email, Customers_IdCustomer, Customers_Password, Customers_NameCustomer}

# Flight class attributes and methods
Flight_FlightNumber: Property = Property(name="FlightNumber", type=StringType)
Flight_Date: Property = Property(name="Date", type=StringType)
Flight.attributes={Flight_Date, Flight_FlightNumber}

# Routes class attributes and methods
Routes_RouteID: Property = Property(name="RouteID", type=StringType)
Routes_OriginAirport: Property = Property(name="OriginAirport", type=StringType)
Routes_DestinationAirport: Property = Property(name="DestinationAirport", type=StringType)
Routes.attributes={Routes_RouteID, Routes_OriginAirport, Routes_DestinationAirport}

# Plane class attributes and methods
Plane_PlaneId: Property = Property(name="PlaneId", type=StringType)
Plane_PlaneName: Property = Property(name="PlaneName", type=StringType)
Plane_Capacity: Property = Property(name="Capacity", type=IntegerType)
Plane.attributes={Plane_PlaneId, Plane_Capacity, Plane_PlaneName}

# Airport class attributes and methods
Airport_AirportID: Property = Property(name="AirportID", type=StringType)
Airport_AirportName: Property = Property(name="AirportName", type=StringType)
Airport_Address: Property = Property(name="Address", type=StringType)
Airport.attributes={Airport_Address, Airport_AirportID, Airport_AirportName}

# Ticket class attributes and methods
Ticket_TicketID: Property = Property(name="TicketID", type=StringType)
Ticket_TicketType: Property = Property(name="TicketType", type=StringType)
Ticket_Price: Property = Property(name="Price", type=StringType)
Ticket_Gate: Property = Property(name="Gate", type=StringType)
Ticket_DateTime: Property = Property(name="DateTime", type=StringType)
Ticket.attributes={Ticket_Gate, Ticket_Price, Ticket_DateTime, Ticket_TicketID, Ticket_TicketType}

# Reservation class attributes and methods

# Seats class attributes and methods
Seats_SeatNumber: Property = Property(name="SeatNumber", type=IntegerType)
Seats_Availability: Property = Property(name="Availability", type=BooleanType)
Seats.attributes={Seats_SeatNumber, Seats_Availability}

# Relationships
Customers_Reservation: BinaryAssociation = BinaryAssociation(
    name="Customers_Reservation",
    ends={
        Property(name="reservation0", type=Reservation, multiplicity=Multiplicity(1, 1)),
        Property(name="customers1", type=Customers, multiplicity=Multiplicity(0, 9999))
    }
)
Flight_Reservation: BinaryAssociation = BinaryAssociation(
    name="Flight_Reservation",
    ends={
        Property(name="reservation2", type=Reservation, multiplicity=Multiplicity(1, 9999)),
        Property(name="flight3", type=Flight, multiplicity=Multiplicity(1, 9999))
    }
)
Plane_Flight: BinaryAssociation = BinaryAssociation(
    name="Plane_Flight",
    ends={
        Property(name="flight4", type=Flight, multiplicity=Multiplicity(1, 9999)),
        Property(name="plane5", type=Plane, multiplicity=Multiplicity(1, 9999))
    }
)
Routes_Airport: BinaryAssociation = BinaryAssociation(
    name="Routes_Airport",
    ends={
        Property(name="airport6", type=Airport, multiplicity=Multiplicity(1, 9999)),
        Property(name="routes7", type=Routes, multiplicity=Multiplicity(1, 9999))
    }
)
Flight_Routes: BinaryAssociation = BinaryAssociation(
    name="Flight_Routes",
    ends={
        Property(name="routes8", type=Routes, multiplicity=Multiplicity(1, 1)),
        Property(name="flight9", type=Flight, multiplicity=Multiplicity(1, 9999))
    }
)
Flight_Ticket: BinaryAssociation = BinaryAssociation(
    name="Flight_Ticket",
    ends={
        Property(name="ticket10", type=Ticket, multiplicity=Multiplicity(1, 9999)),
        Property(name="flight11", type=Flight, multiplicity=Multiplicity(1, 9999))
    }
)
Seats_Plane: BinaryAssociation = BinaryAssociation(
    name="Seats_Plane",
    ends={
        Property(name="plane12", type=Plane, multiplicity=Multiplicity(1, 9999)),
        Property(name="seats13", type=Seats, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_hBZIAMKjEeeEXb8Dudo6PQ",
    types={Customers, Flight, Routes, Plane, Airport, Ticket, Reservation, Seats, Enumeration_},
    associations={Customers_Reservation, Flight_Reservation, Plane_Flight, Routes_Airport, Flight_Routes, Flight_Ticket, Seats_Plane},
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