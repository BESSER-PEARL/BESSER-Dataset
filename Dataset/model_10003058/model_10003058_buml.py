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
Customer = Class(name="Customer")
Bank = Class(name="Bank")
Flight = Class(name="Flight")
Administrator = Class(name="Administrator")
Ticket = Class(name="Ticket")

# Customer class attributes and methods
Customer_Fullname: Property = Property(name="Fullname", type=StringType)
Customer_Location: Property = Property(name="Location", type=StringType)
Customer_Card_details: Property = Property(name="Card_details", type=IntegerType)
Customer_Gender: Property = Property(name="Gender", type=StringType)
Customer.attributes={Customer_Gender, Customer_Location, Customer_Fullname, Customer_Card_details}

# Bank class attributes and methods
Bank_Name: Property = Property(name="Name", type=StringType)
Bank_Account: Property = Property(name="Account", type=IntegerType)
Bank.attributes={Bank_Account, Bank_Name}

# Flight class attributes and methods
Flight_Number_of_seats: Property = Property(name="Number_of_seats", type=IntegerType)
Flight_Name: Property = Property(name="Name", type=StringType)
Flight_Id: Property = Property(name="Id", type=Flight)
Flight_Destination: Property = Property(name="Destination", type=StringType)
Flight_Time: Property = Property(name="Time", type=IntegerType)
Flight_Source: Property = Property(name="Source", type=StringType)
Flight.attributes={Flight_Time, Flight_Source, Flight_Name, Flight_Number_of_seats, Flight_Id, Flight_Destination}

# Administrator class attributes and methods
Administrator_Fullname: Property = Property(name="Fullname", type=StringType)
Administrator_Account: Property = Property(name="Account", type=StringType)
Administrator.attributes={Administrator_Fullname, Administrator_Account}

# Ticket class attributes and methods
Ticket_Id: Property = Property(name="Id", type=IntegerType)
Ticket_Price: Property = Property(name="Price", type=BooleanType)
Ticket_Customer_Name: Property = Property(name="Customer_Name", type=StringType)
Ticket_Type: Property = Property(name="Type", type=StringType)
Ticket.attributes={Ticket_Price, Ticket_Customer_Name, Ticket_Id, Ticket_Type}

# Relationships
Customer_Administrator: BinaryAssociation = BinaryAssociation(
    name="Customer_Administrator",
    ends={
        Property(name="Request0", type=Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="Manage1", type=Customer, multiplicity=Multiplicity(1, 9999))
    }
)
Bank_Customer: BinaryAssociation = BinaryAssociation(
    name="Bank_Customer",
    ends={
        Property(name="customer2", type=Customer, multiplicity=Multiplicity(1, 9999)),
        Property(name="bank3", type=Bank, multiplicity=Multiplicity(1, 1))
    }
)
Ticket_Customer: BinaryAssociation = BinaryAssociation(
    name="Ticket_Customer",
    ends={
        Property(name="Owner4", type=Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="Owns5", type=Ticket, multiplicity=Multiplicity(1, 9999))
    }
)
Ticket_Flight: BinaryAssociation = BinaryAssociation(
    name="Ticket_Flight",
    ends={
        Property(name="flight6", type=Flight, multiplicity=Multiplicity(1, 1)),
        Property(name="ticket7", type=Ticket, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="f99b41b8_0436_47fb_a363_d5f4868c80c8",
    types={Customer, Bank, Flight, Administrator, Ticket},
    associations={Customer_Administrator, Bank_Customer, Ticket_Customer, Ticket_Flight},
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