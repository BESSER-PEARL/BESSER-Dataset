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
Hotel = Class(name="Hotel")
Room = Class(name="Room")

# Customer class attributes and methods
Customer_name: Property = Property(name="name", type=StringType)
Customer_phoneNumber: Property = Property(name="phoneNumber", type=IntegerType)
Customer_ident: Property = Property(name="ident", type=StringType)
Customer_email: Property = Property(name="email", type=StringType)
Customer_roomID: Property = Property(name="roomID", type=IntegerType)
Customer.attributes={Customer_name, Customer_ident, Customer_email, Customer_phoneNumber, Customer_roomID}

# Hotel class attributes and methods
Hotel_street: Property = Property(name="street", type=StringType)
Hotel_city: Property = Property(name="city", type=StringType)
Hotel_zip: Property = Property(name="zip", type=IntegerType)
Hotel_name: Property = Property(name="name", type=StringType)
Hotel_phoneNumber: Property = Property(name="phoneNumber", type=IntegerType)
Hotel_website: Property = Property(name="website", type=StringType)
Hotel.attributes={Hotel_city, Hotel_zip, Hotel_phoneNumber, Hotel_name, Hotel_website, Hotel_street}

# Room class attributes and methods
Room_roomID: Property = Property(name="roomID", type=IntegerType)
Room_floor: Property = Property(name="floor", type=IntegerType)
Room_door: Property = Property(name="door", type=IntegerType)
Room_capacity: Property = Property(name="capacity", type=StringType)
Room_price: Property = Property(name="price", type=FloatType)
Room.attributes={Room_price, Room_floor, Room_roomID, Room_door, Room_capacity}

# Relationships
Hotel_Room: BinaryAssociation = BinaryAssociation(
    name="Hotel_Room",
    ends={
        Property(name="room0", type=Room, multiplicity=Multiplicity(1, 9999)),
        Property(name="hotel1", type=Hotel, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Room: BinaryAssociation = BinaryAssociation(
    name="Customer_Room",
    ends={
        Property(name="room2", type=Room, multiplicity=Multiplicity(0, 1)),
        Property(name="customer3", type=Customer, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_5712bd5b_37b6_4f75_a9ea_8088d5461999",
    types={Customer, Hotel, Room},
    associations={Hotel_Room, Customer_Room},
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