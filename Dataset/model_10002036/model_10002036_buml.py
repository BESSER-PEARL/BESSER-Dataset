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
Class_ = Class(name="Class")
SuperFast = Class(name="SuperFast")
Express = Class(name="Express")
SuperFast1 = Class(name="SuperFast1")
Express1 = Class(name="Express1")
Information_Interface = Class(name="Information_Interface")
Pessanger = Class(name="Pessanger")
Traveler_Actor = Class(name="Traveler_Actor")
Check_ticket_availability_UseCase = Class(name="Check_ticket_availability_UseCase")
Pay_fare_amount_UseCase = Class(name="Pay_fare_amount_UseCase")
Book_ticket_UseCase = Class(name="Book_ticket_UseCase")
Fill_the_details_UseCase = Class(name="Fill_the_details_UseCase")
Cancel_ticket_UseCase = Class(name="Cancel_ticket_UseCase")
Refund_money_UseCase = Class(name="Refund_money_UseCase")
Clerk_Actor = Class(name="Clerk_Actor")
Railway_website_Actor = Class(name="Railway_website_Actor")

# Class class attributes and methods

# SuperFast class attributes and methods
SuperFast_AC_1: Property = Property(name="AC_1", type=StringType)
SuperFast_AC_2: Property = Property(name="AC_2", type=StringType)
SuperFast_AC_3: Property = Property(name="AC_3", type=StringType)
SuperFast_Sleeper: Property = Property(name="Sleeper", type=StringType)
SuperFast.attributes={SuperFast_AC_1, SuperFast_AC_2, SuperFast_AC_3, SuperFast_Sleeper}

# Express class attributes and methods
Express_SecondSitting: Property = Property(name="SecondSitting", type=StringType)
Express_General: Property = Property(name="General", type=StringType)
Express.attributes={Express_SecondSitting, Express_General}

# SuperFast1 class attributes and methods
SuperFast1_AC_1: Property = Property(name="AC_1", type=StringType)
SuperFast1_AC_2: Property = Property(name="AC_2", type=StringType)
SuperFast1_AC_3: Property = Property(name="AC_3", type=StringType)
SuperFast1_Sleeper: Property = Property(name="Sleeper", type=StringType)
SuperFast1_Ladies: Property = Property(name="Ladies", type=StringType)
SuperFast1_Handicamp: Property = Property(name="Handicamp", type=StringType)
SuperFast1.attributes={SuperFast1_AC_2, SuperFast1_AC_3, SuperFast1_Handicamp, SuperFast1_Sleeper, SuperFast1_AC_1, SuperFast1_Ladies}

# Express1 class attributes and methods
Express1_SecondSitting: Property = Property(name="SecondSitting", type=StringType)
Express1.attributes={Express1_SecondSitting}

# Information_Interface class attributes and methods

# Pessanger class attributes and methods
Pessanger_AadharNo: Property = Property(name="AadharNo", type=IntegerType)
Pessanger_Children: Property = Property(name="Children", type=IntegerType)
Pessanger.attributes={Pessanger_AadharNo, Pessanger_Children}

# Traveler_Actor class attributes and methods

# Check_ticket_availability_UseCase class attributes and methods

# Pay_fare_amount_UseCase class attributes and methods

# Book_ticket_UseCase class attributes and methods

# Fill_the_details_UseCase class attributes and methods

# Cancel_ticket_UseCase class attributes and methods

# Refund_money_UseCase class attributes and methods

# Clerk_Actor class attributes and methods

# Railway_website_Actor class attributes and methods

# Relationships
Clerk_Cancel_ticket: BinaryAssociation = BinaryAssociation(
    name="Clerk_Cancel_ticket",
    ends={
        Property(name="cancel_ticket0", type=Cancel_ticket_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="clerk1", type=Clerk_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Traveler_Check_ticket_availability: BinaryAssociation = BinaryAssociation(
    name="Traveler_Check_ticket_availability",
    ends={
        Property(name="check_ticket_availability2", type=Check_ticket_availability_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="traveler3", type=Traveler_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Traveler_Pay_fare_amount: BinaryAssociation = BinaryAssociation(
    name="Traveler_Pay_fare_amount",
    ends={
        Property(name="pay_fare_amount4", type=Pay_fare_amount_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="traveler5", type=Traveler_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Traveler_Book_ticket: BinaryAssociation = BinaryAssociation(
    name="Traveler_Book_ticket",
    ends={
        Property(name="book_ticket6", type=Book_ticket_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="traveler7", type=Traveler_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Traveler_Fill_the_details: BinaryAssociation = BinaryAssociation(
    name="Traveler_Fill_the_details",
    ends={
        Property(name="fill_the_details8", type=Fill_the_details_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="traveler9", type=Traveler_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Traveler_Cancel_ticket: BinaryAssociation = BinaryAssociation(
    name="Traveler_Cancel_ticket",
    ends={
        Property(name="cancel_ticket10", type=Cancel_ticket_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="traveler11", type=Traveler_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Check_ticket_availability_Railway_website: BinaryAssociation = BinaryAssociation(
    name="Check_ticket_availability_Railway_website",
    ends={
        Property(name="railway_website12", type=Railway_website_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="check_ticket_availability13", type=Check_ticket_availability_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Pay_fare_amount_Railway_website: BinaryAssociation = BinaryAssociation(
    name="Pay_fare_amount_Railway_website",
    ends={
        Property(name="railway_website14", type=Railway_website_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="pay_fare_amount15", type=Pay_fare_amount_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Book_ticket_Railway_website: BinaryAssociation = BinaryAssociation(
    name="Book_ticket_Railway_website",
    ends={
        Property(name="railway_website16", type=Railway_website_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="book_ticket17", type=Book_ticket_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Fill_the_details_Railway_website: BinaryAssociation = BinaryAssociation(
    name="Fill_the_details_Railway_website",
    ends={
        Property(name="railway_website18", type=Railway_website_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="fill_the_details19", type=Fill_the_details_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Cancel_ticket_Railway_website: BinaryAssociation = BinaryAssociation(
    name="Cancel_ticket_Railway_website",
    ends={
        Property(name="railway_website20", type=Railway_website_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="cancel_ticket21", type=Cancel_ticket_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Refund_money_Railway_website: BinaryAssociation = BinaryAssociation(
    name="Refund_money_Railway_website",
    ends={
        Property(name="railway_website22", type=Railway_website_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="refund_money23", type=Refund_money_UseCase, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_kqopoADrEeiLEbIzy5aHfg",
    types={Class_, SuperFast, Express, SuperFast1, Express1, Information_Interface, Pessanger, Traveler_Actor, Check_ticket_availability_UseCase, Pay_fare_amount_UseCase, Book_ticket_UseCase, Fill_the_details_UseCase, Cancel_ticket_UseCase, Refund_money_UseCase, Clerk_Actor, Railway_website_Actor},
    associations={Clerk_Cancel_ticket, Traveler_Check_ticket_availability, Traveler_Pay_fare_amount, Traveler_Book_ticket, Traveler_Fill_the_details, Traveler_Cancel_ticket, Check_ticket_availability_Railway_website, Pay_fare_amount_Railway_website, Book_ticket_Railway_website, Fill_the_details_Railway_website, Cancel_ticket_Railway_website, Refund_money_Railway_website},
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