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
User_Actor = Class(name="User_Actor")
Login_UseCase = Class(name="Login_UseCase")
Register_UseCase = Class(name="Register_UseCase")
Book_Airline_Ticket_UseCase = Class(name="Book_Airline_Ticket_UseCase")
Enter_flight_search_details_UseCase = Class(name="Enter_flight_search_details_UseCase")
Select_flight__seat__meals_UseCase = Class(name="Select_flight__seat__meals_UseCase")
Enter_passenger_details_UseCase = Class(name="Enter_passenger_details_UseCase")
Payment_UseCase = Class(name="Payment_UseCase")
View_Print_Ticket_UseCase = Class(name="View_Print_Ticket_UseCase")
Show_Ticket_History_UseCase = Class(name="Show_Ticket_History_UseCase")
Cancel_Ticket_UseCase = Class(name="Cancel_Ticket_UseCase")
Reschedule_Ticket_UseCase = Class(name="Reschedule_Ticket_UseCase")
Administrator_Actor = Class(name="Administrator_Actor")
Update_Flight_Schedule_UseCase = Class(name="Update_Flight_Schedule_UseCase")
Pay_by_Debit_Credit_Card_UseCase = Class(name="Pay_by_Debit_Credit_Card_UseCase")
Use_Frequent_Flyer_Miles_UseCase = Class(name="Use_Frequent_Flyer_Miles_UseCase")
Pay_by_E_Wallet_UseCase = Class(name="Pay_by_E_Wallet_UseCase")
Class_ = Class(name="Class")

# User_Actor class attributes and methods

# Login_UseCase class attributes and methods

# Register_UseCase class attributes and methods

# Book_Airline_Ticket_UseCase class attributes and methods

# Enter_flight_search_details_UseCase class attributes and methods

# Select_flight__seat__meals_UseCase class attributes and methods

# Enter_passenger_details_UseCase class attributes and methods

# Payment_UseCase class attributes and methods

# View_Print_Ticket_UseCase class attributes and methods

# Show_Ticket_History_UseCase class attributes and methods

# Cancel_Ticket_UseCase class attributes and methods

# Reschedule_Ticket_UseCase class attributes and methods

# Administrator_Actor class attributes and methods

# Update_Flight_Schedule_UseCase class attributes and methods

# Pay_by_Debit_Credit_Card_UseCase class attributes and methods

# Use_Frequent_Flyer_Miles_UseCase class attributes and methods

# Pay_by_E_Wallet_UseCase class attributes and methods

# Class class attributes and methods

# Relationships
Book_Airline_Ticket_Payment: BinaryAssociation = BinaryAssociation(
    name="Book_Airline_Ticket_Payment",
    ends={
        Property(name="payment0", type=Payment_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="book_Airline_Ticket1", type=Book_Airline_Ticket_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
User_Login: BinaryAssociation = BinaryAssociation(
    name="User_Login",
    ends={
        Property(name="login2", type=Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user3", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Book_Airline_Ticket: BinaryAssociation = BinaryAssociation(
    name="User_Book_Airline_Ticket",
    ends={
        Property(name="book_Airline_Ticket4", type=Book_Airline_Ticket_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user5", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Show_Ticket_History: BinaryAssociation = BinaryAssociation(
    name="User_Show_Ticket_History",
    ends={
        Property(name="show_Ticket_History6", type=Show_Ticket_History_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user7", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Cancel_Ticket: BinaryAssociation = BinaryAssociation(
    name="User_Cancel_Ticket",
    ends={
        Property(name="cancel_Ticket8", type=Cancel_Ticket_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user9", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Reschedule_Ticket: BinaryAssociation = BinaryAssociation(
    name="User_Reschedule_Ticket",
    ends={
        Property(name="reschedule_Ticket10", type=Reschedule_Ticket_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user11", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Cancel_Ticket: BinaryAssociation = BinaryAssociation(
    name="Administrator_Cancel_Ticket",
    ends={
        Property(name="cancel_Ticket12", type=Cancel_Ticket_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator13", type=Administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Reschedule_Ticket: BinaryAssociation = BinaryAssociation(
    name="Administrator_Reschedule_Ticket",
    ends={
        Property(name="reschedule_Ticket14", type=Reschedule_Ticket_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator15", type=Administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Update_Flight_Schedule: BinaryAssociation = BinaryAssociation(
    name="Administrator_Update_Flight_Schedule",
    ends={
        Property(name="update_Flight_Schedule16", type=Update_Flight_Schedule_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator17", type=Administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Login_Show_Ticket_History: BinaryAssociation = BinaryAssociation(
    name="Login_Show_Ticket_History",
    ends={
        Property(name="show_Ticket_History18", type=Show_Ticket_History_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="login19", type=Login_UseCase, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_90947e15_73f6_45c5_8b6d_d52624de89cd",
    types={User_Actor, Login_UseCase, Register_UseCase, Book_Airline_Ticket_UseCase, Enter_flight_search_details_UseCase, Select_flight__seat__meals_UseCase, Enter_passenger_details_UseCase, Payment_UseCase, View_Print_Ticket_UseCase, Show_Ticket_History_UseCase, Cancel_Ticket_UseCase, Reschedule_Ticket_UseCase, Administrator_Actor, Update_Flight_Schedule_UseCase, Pay_by_Debit_Credit_Card_UseCase, Use_Frequent_Flyer_Miles_UseCase, Pay_by_E_Wallet_UseCase, Class_},
    associations={Book_Airline_Ticket_Payment, User_Login, User_Book_Airline_Ticket, User_Show_Ticket_History, User_Cancel_Ticket, User_Reschedule_Ticket, Administrator_Cancel_Ticket, Administrator_Reschedule_Ticket, Administrator_Update_Flight_Schedule, Login_Show_Ticket_History},
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