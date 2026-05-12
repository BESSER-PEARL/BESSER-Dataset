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
Passenger_Actor = Class(name="Passenger_Actor")
Admin_Actor = Class(name="Admin_Actor")
Bank_Actor = Class(name="Bank_Actor")
Airline_Reservation_System_Component = Class(name="Airline_Reservation_System_Component")
Valid_Card_Deatils_external = Class(name="Valid_Card_Deatils_external")
Check_For_Availability_external = Class(name="Check_For_Availability_external")
Login_external = Class(name="Login_external")
Payment_external = Class(name="Payment_external")
Book_Ticket_external = Class(name="Book_Ticket_external")
Cancel_Ticket_external = Class(name="Cancel_Ticket_external")
Check_Flight_Status_external = Class(name="Check_Flight_Status_external")
Update_Flight_Schedule_external = Class(name="Update_Flight_Schedule_external")
Airport = Class(name="Airport")
_Component = Class(name="_Component")
__extends___Component = Class(name="__extends___Component")
__Uses___Component = Class(name="__Uses___Component")

# Passenger_Actor class attributes and methods

# Admin_Actor class attributes and methods

# Bank_Actor class attributes and methods

# Airline_Reservation_System_Component class attributes and methods

# Valid_Card_Deatils_external class attributes and methods

# Check_For_Availability_external class attributes and methods

# Login_external class attributes and methods

# Payment_external class attributes and methods

# Book_Ticket_external class attributes and methods

# Cancel_Ticket_external class attributes and methods

# Check_Flight_Status_external class attributes and methods

# Update_Flight_Schedule_external class attributes and methods

# Airport class attributes and methods

# _Component class attributes and methods

# __extends___Component class attributes and methods

# __Uses___Component class attributes and methods

# Relationships
Valid_Card_Deatils_Bank: BinaryAssociation = BinaryAssociation(
    name="Valid_Card_Deatils_Bank",
    ends={
        Property(name="bank0", type=Bank_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="valid_Card_Deatils1", type=Valid_Card_Deatils_external, multiplicity=Multiplicity(0, 1))
    }
)
Passenger_Check_For_Availability: BinaryAssociation = BinaryAssociation(
    name="Passenger_Check_For_Availability",
    ends={
        Property(name="check_For_Availability2", type=Check_For_Availability_external, multiplicity=Multiplicity(0, 1)),
        Property(name="passenger3", type=Passenger_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Passenger_Login: BinaryAssociation = BinaryAssociation(
    name="Passenger_Login",
    ends={
        Property(name="login4", type=Login_external, multiplicity=Multiplicity(0, 1)),
        Property(name="passenger5", type=Passenger_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Passenger_Payment: BinaryAssociation = BinaryAssociation(
    name="Passenger_Payment",
    ends={
        Property(name="payment6", type=Payment_external, multiplicity=Multiplicity(0, 1)),
        Property(name="passenger7", type=Passenger_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Passenger_Book_Ticket: BinaryAssociation = BinaryAssociation(
    name="Passenger_Book_Ticket",
    ends={
        Property(name="book_Ticket8", type=Book_Ticket_external, multiplicity=Multiplicity(0, 1)),
        Property(name="passenger9", type=Passenger_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Passenger_Cancel_Ticket: BinaryAssociation = BinaryAssociation(
    name="Passenger_Cancel_Ticket",
    ends={
        Property(name="cancel_Ticket10", type=Cancel_Ticket_external, multiplicity=Multiplicity(0, 1)),
        Property(name="passenger11", type=Passenger_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Passenger_Check_Flight_Status: BinaryAssociation = BinaryAssociation(
    name="Passenger_Check_Flight_Status",
    ends={
        Property(name="check_Flight_Status12", type=Check_Flight_Status_external, multiplicity=Multiplicity(0, 1)),
        Property(name="passenger13", type=Passenger_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Update_Flight_Schedule: BinaryAssociation = BinaryAssociation(
    name="Admin_Update_Flight_Schedule",
    ends={
        Property(name="update_Flight_Schedule14", type=Update_Flight_Schedule_external, multiplicity=Multiplicity(0, 1)),
        Property(name="admin15", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Cancel_Ticket: BinaryAssociation = BinaryAssociation(
    name="Admin_Cancel_Ticket",
    ends={
        Property(name="cancel_Ticket16", type=Cancel_Ticket_external, multiplicity=Multiplicity(0, 1)),
        Property(name="admin17", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_Mj39sBYjEeirparnd37rPA",
    types={Passenger_Actor, Admin_Actor, Bank_Actor, Airline_Reservation_System_Component, Valid_Card_Deatils_external, Check_For_Availability_external, Login_external, Payment_external, Book_Ticket_external, Cancel_Ticket_external, Check_Flight_Status_external, Update_Flight_Schedule_external, Airport, _Component, __extends___Component, __Uses___Component},
    associations={Valid_Card_Deatils_Bank, Passenger_Check_For_Availability, Passenger_Login, Passenger_Payment, Passenger_Book_Ticket, Passenger_Cancel_Ticket, Passenger_Check_Flight_Status, Admin_Update_Flight_Schedule, Admin_Cancel_Ticket},
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