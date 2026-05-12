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
User___Passenger_Actor = Class(name="User___Passenger_Actor")
Travel_Agent_Actor = Class(name="Travel_Agent_Actor")
Airline_Agency_Actor = Class(name="Airline_Agency_Actor")
Register__Login_UseCase = Class(name="Register__Login_UseCase")
Create_Account_UseCase = Class(name="Create_Account_UseCase")
Valid_UseCase = Class(name="Valid_UseCase")
Invalid_UseCase = Class(name="Invalid_UseCase")
Review_Order_UseCase = Class(name="Review_Order_UseCase")
Check_Tickets_UseCase = Class(name="Check_Tickets_UseCase")
Choose_Flight_UseCase = Class(name="Choose_Flight_UseCase")
Proceed_to_Checkout_UseCase = Class(name="Proceed_to_Checkout_UseCase")
Make_Payment___Checkout_UseCase = Class(name="Make_Payment___Checkout_UseCase")
Valid_Details_UseCase = Class(name="Valid_Details_UseCase")
Invalid_Details_UseCase = Class(name="Invalid_Details_UseCase")
Pay_Travel_Agent_UseCase = Class(name="Pay_Travel_Agent_UseCase")
Travel_Agent_Fee_UseCase = Class(name="Travel_Agent_Fee_UseCase")
Reserve_a_Ticket_UseCase = Class(name="Reserve_a_Ticket_UseCase")
Receive_Payment_UseCase = Class(name="Receive_Payment_UseCase")
MyClass = Class(name="MyClass")

# User___Passenger_Actor class attributes and methods

# Travel_Agent_Actor class attributes and methods

# Airline_Agency_Actor class attributes and methods

# Register__Login_UseCase class attributes and methods

# Create_Account_UseCase class attributes and methods

# Valid_UseCase class attributes and methods

# Invalid_UseCase class attributes and methods

# Review_Order_UseCase class attributes and methods

# Check_Tickets_UseCase class attributes and methods

# Choose_Flight_UseCase class attributes and methods

# Proceed_to_Checkout_UseCase class attributes and methods

# Make_Payment___Checkout_UseCase class attributes and methods

# Valid_Details_UseCase class attributes and methods

# Invalid_Details_UseCase class attributes and methods

# Pay_Travel_Agent_UseCase class attributes and methods

# Travel_Agent_Fee_UseCase class attributes and methods

# Reserve_a_Ticket_UseCase class attributes and methods

# Receive_Payment_UseCase class attributes and methods

# MyClass class attributes and methods

# Relationships
User___Passenger_Register__Login: BinaryAssociation = BinaryAssociation(
    name="User___Passenger_Register__Login",
    ends={
        Property(name="register__Login0", type=Register__Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user___Passenger1", type=User___Passenger_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User___Passenger_Review_Order: BinaryAssociation = BinaryAssociation(
    name="User___Passenger_Review_Order",
    ends={
        Property(name="review_Order2", type=Review_Order_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user___Passenger3", type=User___Passenger_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User___Passenger_Check_Tickets: BinaryAssociation = BinaryAssociation(
    name="User___Passenger_Check_Tickets",
    ends={
        Property(name="check_Tickets4", type=Check_Tickets_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user___Passenger5", type=User___Passenger_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User___Passenger_Choose_Flight: BinaryAssociation = BinaryAssociation(
    name="User___Passenger_Choose_Flight",
    ends={
        Property(name="choose_Flight6", type=Choose_Flight_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user___Passenger7", type=User___Passenger_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User___Passenger_Proceed_to_Checkout: BinaryAssociation = BinaryAssociation(
    name="User___Passenger_Proceed_to_Checkout",
    ends={
        Property(name="proceed_to_Checkout8", type=Proceed_to_Checkout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user___Passenger9", type=User___Passenger_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User___Passenger_Make_Payment___Checkout: BinaryAssociation = BinaryAssociation(
    name="User___Passenger_Make_Payment___Checkout",
    ends={
        Property(name="make_Payment___Checkout10", type=Make_Payment___Checkout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user___Passenger11", type=User___Passenger_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User___Passenger_Pay_Travel_Agent: BinaryAssociation = BinaryAssociation(
    name="User___Passenger_Pay_Travel_Agent",
    ends={
        Property(name="pay_Travel_Agent12", type=Pay_Travel_Agent_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user___Passenger13", type=User___Passenger_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Airline_Agency_Reserve_a_Ticket: BinaryAssociation = BinaryAssociation(
    name="Airline_Agency_Reserve_a_Ticket",
    ends={
        Property(name="reserve_a_Ticket14", type=Reserve_a_Ticket_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="airline_Agency15", type=Airline_Agency_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Airline_Agency_Receive_Payment: BinaryAssociation = BinaryAssociation(
    name="Airline_Agency_Receive_Payment",
    ends={
        Property(name="receive_Payment16", type=Receive_Payment_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="airline_Agency17", type=Airline_Agency_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Airline_Agency_Review_Order: BinaryAssociation = BinaryAssociation(
    name="Airline_Agency_Review_Order",
    ends={
        Property(name="review_Order18", type=Review_Order_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="airline_Agency19", type=Airline_Agency_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Register__Login_Travel_Agent: BinaryAssociation = BinaryAssociation(
    name="Register__Login_Travel_Agent",
    ends={
        Property(name="travel_Agent20", type=Travel_Agent_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="register__Login21", type=Register__Login_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Travel_Agent_Review_Order: BinaryAssociation = BinaryAssociation(
    name="Travel_Agent_Review_Order",
    ends={
        Property(name="review_Order22", type=Review_Order_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="travel_Agent23", type=Travel_Agent_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Check_Tickets_Travel_Agent: BinaryAssociation = BinaryAssociation(
    name="Check_Tickets_Travel_Agent",
    ends={
        Property(name="travel_Agent24", type=Travel_Agent_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="check_Tickets25", type=Check_Tickets_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Choose_Flight_Travel_Agent: BinaryAssociation = BinaryAssociation(
    name="Choose_Flight_Travel_Agent",
    ends={
        Property(name="travel_Agent26", type=Travel_Agent_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="choose_Flight27", type=Choose_Flight_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Proceed_to_Checkout_Travel_Agent: BinaryAssociation = BinaryAssociation(
    name="Proceed_to_Checkout_Travel_Agent",
    ends={
        Property(name="travel_Agent28", type=Travel_Agent_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="proceed_to_Checkout29", type=Proceed_to_Checkout_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Make_Payment___Checkout_Travel_Agent: BinaryAssociation = BinaryAssociation(
    name="Make_Payment___Checkout_Travel_Agent",
    ends={
        Property(name="travel_Agent30", type=Travel_Agent_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="make_Payment___Checkout31", type=Make_Payment___Checkout_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Pay_Travel_Agent_Travel_Agent: BinaryAssociation = BinaryAssociation(
    name="Pay_Travel_Agent_Travel_Agent",
    ends={
        Property(name="travel_Agent32", type=Travel_Agent_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="pay_Travel_Agent33", type=Pay_Travel_Agent_UseCase, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_6d2642a2_c711_46f1_8fa1_f5e526dfeaac",
    types={User___Passenger_Actor, Travel_Agent_Actor, Airline_Agency_Actor, Register__Login_UseCase, Create_Account_UseCase, Valid_UseCase, Invalid_UseCase, Review_Order_UseCase, Check_Tickets_UseCase, Choose_Flight_UseCase, Proceed_to_Checkout_UseCase, Make_Payment___Checkout_UseCase, Valid_Details_UseCase, Invalid_Details_UseCase, Pay_Travel_Agent_UseCase, Travel_Agent_Fee_UseCase, Reserve_a_Ticket_UseCase, Receive_Payment_UseCase, MyClass},
    associations={User___Passenger_Register__Login, User___Passenger_Review_Order, User___Passenger_Check_Tickets, User___Passenger_Choose_Flight, User___Passenger_Proceed_to_Checkout, User___Passenger_Make_Payment___Checkout, User___Passenger_Pay_Travel_Agent, Airline_Agency_Reserve_a_Ticket, Airline_Agency_Receive_Payment, Airline_Agency_Review_Order, Register__Login_Travel_Agent, Travel_Agent_Review_Order, Check_Tickets_Travel_Agent, Choose_Flight_Travel_Agent, Proceed_to_Checkout_Travel_Agent, Make_Payment___Checkout_Travel_Agent, Pay_Travel_Agent_Travel_Agent},
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