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
Problem = Class(name="Problem")
Client = Class(name="Client")
Booking = Class(name="Booking")
Ticket = Class(name="Ticket")
Answer = Class(name="Answer")
Flight = Class(name="Flight")

# Problem class attributes and methods
Problem_Id: Property = Property(name="Id", type=StringType)
Problem_Type: Property = Property(name="Type", type=StringType)
Problem_Content: Property = Property(name="Content", type=StringType)
Problem.attributes={Problem_Type, Problem_Id, Problem_Content}

# Client class attributes and methods
Client_Id: Property = Property(name="Id", type=StringType)
Client_Name: Property = Property(name="Name", type=StringType)
Client_Bookings: Property = Property(name="Bookings", type=Booking)
Client_Loyalty_card: Property = Property(name="Loyalty_card", type=StringType)
Client.attributes={Client_Name, Client_Bookings, Client_Id, Client_Loyalty_card}

# Booking class attributes and methods
Booking_Id: Property = Property(name="Id", type=StringType)
Booking_Tickets: Property = Property(name="Tickets", type=Ticket)
Booking_Luggage: Property = Property(name="Luggage", type=StringType)
Booking_Origin: Property = Property(name="Origin", type=StringType)
Booking_Destination: Property = Property(name="Destination", type=StringType)
Booking_Time: Property = Property(name="Time", type=StringType)
Booking.attributes={Booking_Luggage, Booking_Time, Booking_Destination, Booking_Origin, Booking_Id, Booking_Tickets}

# Ticket class attributes and methods
Ticket_Id: Property = Property(name="Id", type=StringType)
Ticket_Clients: Property = Property(name="Clients", type=Client)
Ticket_Seat: Property = Property(name="Seat", type=StringType)
Ticket_Booking_Class: Property = Property(name="Booking_Class", type=StringType)
Ticket.attributes={Ticket_Booking_Class, Ticket_Seat, Ticket_Id, Ticket_Clients}

# Answer class attributes and methods

# Flight class attributes and methods
Flight_Id: Property = Property(name="Id", type=StringType)
Flight_Company: Property = Property(name="Company", type=StringType)
Flight_Origin: Property = Property(name="Origin", type=StringType)
Flight_Destination: Property = Property(name="Destination", type=StringType)
Flight_Time: Property = Property(name="Time", type=StringType)
Flight_Max_Passangers: Property = Property(name="Max_Passangers", type=IntegerType)
Flight.attributes={Flight_Company, Flight_Origin, Flight_Id, Flight_Max_Passangers, Flight_Time, Flight_Destination}

# Relationships
Answer_Problem: BinaryAssociation = BinaryAssociation(
    name="Answer_Problem",
    ends={
        Property(name="Answer_Problem_00", type=Problem, multiplicity=Multiplicity(1, 1)),
        Property(name="Answer_Problem_11", type=Answer, multiplicity=Multiplicity(1, 9999))
    }
)
Client_Problem: BinaryAssociation = BinaryAssociation(
    name="Client_Problem",
    ends={
        Property(name="Client_Problem_02", type=Problem, multiplicity=Multiplicity(0, 9999)),
        Property(name="Client_Problem_13", type=Client, multiplicity=Multiplicity(1, 1))
    }
)
Client_Ticket: BinaryAssociation = BinaryAssociation(
    name="Client_Ticket",
    ends={
        Property(name="Client_Ticket_04", type=Ticket, multiplicity=Multiplicity(1, 9999)),
        Property(name="Client_Ticket_15", type=Client, multiplicity=Multiplicity(1, 1))
    }
)
Booking_Ticket: BinaryAssociation = BinaryAssociation(
    name="Booking_Ticket",
    ends={
        Property(name="Booking_Ticket_06", type=Ticket, multiplicity=Multiplicity(1, 9999)),
        Property(name="Booking_Ticket_17", type=Booking, multiplicity=Multiplicity(1, 1))
    }
)
Client_Booking: BinaryAssociation = BinaryAssociation(
    name="Client_Booking",
    ends={
        Property(name="Client_Booking_08", type=Booking, multiplicity=Multiplicity(1, 9999)),
        Property(name="One_clinet_makes_the_booking_9", type=Client, multiplicity=Multiplicity(1, 1))
    }
)
Ticket_Flight: BinaryAssociation = BinaryAssociation(
    name="Ticket_Flight",
    ends={
        Property(name="Ticket_Flight_010", type=Flight, multiplicity=Multiplicity(1, 1)),
        Property(name="Ticket_Flight_111", type=Ticket, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_4cc7da76_b1a3_48c5_a3fa_350bf38db2bf",
    types={Problem, Client, Booking, Ticket, Answer, Flight},
    associations={Answer_Problem, Client_Problem, Client_Ticket, Booking_Ticket, Client_Booking, Ticket_Flight},
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