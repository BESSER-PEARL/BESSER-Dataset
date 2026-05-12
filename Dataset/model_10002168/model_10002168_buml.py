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
User = Class(name="User")
Flight = Class(name="Flight")
Ticket = Class(name="Ticket")
Airport = Class(name="Airport")
Payment = Class(name="Payment")

# User class attributes and methods
User_name: Property = Property(name="name", type=StringType)
User_email: Property = Property(name="email", type=StringType)
User_phone: Property = Property(name="phone", type=IntegerType)
User_gender: Property = Property(name="gender", type=StringType)
User_username: Property = Property(name="username", type=StringType)
User_password: Property = Property(name="password", type=StringType)
User_age: Property = Property(name="age", type=IntegerType)
User.attributes={User_phone, User_gender, User_age, User_email, User_password, User_name, User_username}

# Flight class attributes and methods
Flight_Flightnumber: Property = Property(name="Flightnumber", type=IntegerType)
Flight_price: Property = Property(name="price", type=IntegerType)
Flight_time: Property = Property(name="time", type=IntegerType)
Flight_destination: Property = Property(name="destination", type=StringType)
Flight_arrival: Property = Property(name="arrival", type=StringType)
Flight_date: Property = Property(name="date", type=IntegerType)
Flight_Flightname: Property = Property(name="Flightname", type=StringType)
Flight.attributes={Flight_Flightname, Flight_arrival, Flight_price, Flight_date, Flight_Flightnumber, Flight_time, Flight_destination}

# Ticket class attributes and methods
Ticket_Ticketnumber: Property = Property(name="Ticketnumber", type=IntegerType)
Ticket_price: Property = Property(name="price", type=IntegerType)
Ticket_date: Property = Property(name="date", type=IntegerType)
Ticket_Flightnumber: Property = Property(name="Flightnumber", type=Flight)
Ticket_class: Property = Property(name="class", type=StringType)
Ticket_destination: Property = Property(name="destination", type=Flight)
Ticket_arrival: Property = Property(name="arrival", type=Flight)
Ticket_username: Property = Property(name="username", type=User)
Ticket_age: Property = Property(name="age", type=User)
Ticket.attributes={Ticket_price, Ticket_age, Ticket_arrival, Ticket_date, Ticket_username, Ticket_Ticketnumber, Ticket_Flightnumber, Ticket_class, Ticket_destination}

# Airport class attributes and methods
Airport_name: Property = Property(name="name", type=StringType)
Airport_code: Property = Property(name="code", type=IntegerType)
Airport_location: Property = Property(name="location", type=StringType)
Airport.attributes={Airport_location, Airport_code, Airport_name}

# Payment class attributes and methods
Payment_Ticketnumber: Property = Property(name="Ticketnumber", type=Ticket)
Payment_username: Property = Property(name="username", type=Ticket)
Payment_price: Property = Property(name="price", type=Ticket)
Payment_date: Property = Property(name="date", type=Ticket)
Payment_Method: Property = Property(name="Method", type=StringType)
Payment.attributes={Payment_Ticketnumber, Payment_date, Payment_price, Payment_Method, Payment_username}

# Relationships
assoc__o7HyFpgTEeqEM7mFKilpXw: BinaryAssociation = BinaryAssociation(
    name="assoc__o7HyFpgTEeqEM7mFKilpXw",
    ends={
        Property(name="flight0", type=Flight, multiplicity=Multiplicity(1, 9999)),
        Property(name="user1", type=User, multiplicity=Multiplicity(0, 1))
    }
)
User_Ticket: BinaryAssociation = BinaryAssociation(
    name="User_Ticket",
    ends={
        Property(name="ticket2", type=Ticket, multiplicity=Multiplicity(1, 9999)),
        Property(name="user3", type=User, multiplicity=Multiplicity(0, 1))
    }
)
Flight_Airport: BinaryAssociation = BinaryAssociation(
    name="Flight_Airport",
    ends={
        Property(name="airport4", type=Airport, multiplicity=Multiplicity(1, 9999)),
        Property(name="flight5", type=Flight, multiplicity=Multiplicity(1, 9999))
    }
)
Ticket_Payment: BinaryAssociation = BinaryAssociation(
    name="Ticket_Payment",
    ends={
        Property(name="payment6", type=Payment, multiplicity=Multiplicity(1, 1)),
        Property(name="ticket7", type=Ticket, multiplicity=Multiplicity(1, 1))
    }
)
Flight_Ticket: BinaryAssociation = BinaryAssociation(
    name="Flight_Ticket",
    ends={
        Property(name="ticket8", type=Ticket, multiplicity=Multiplicity(1, 9999)),
        Property(name="flight9", type=Flight, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_tyo9MCS1EemcRoPW7FVMlA",
    types={User, Flight, Ticket, Airport, Payment},
    associations={assoc__o7HyFpgTEeqEM7mFKilpXw, User_Ticket, Flight_Airport, Ticket_Payment, Flight_Ticket},
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