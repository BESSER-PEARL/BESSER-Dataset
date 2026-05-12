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
Service = Class(name="Service")

# Customer class attributes and methods
Customer_name: Property = Property(name="name", type=StringType)
Customer_surname: Property = Property(name="surname", type=StringType)
Customer_phoneNumber: Property = Property(name="phoneNumber", type=IntegerType)
Customer_ident: Property = Property(name="ident", type=StringType)
Customer_email: Property = Property(name="email", type=StringType)
Customer.attributes={Customer_phoneNumber, Customer_email, Customer_ident, Customer_surname, Customer_name}

# Hotel class attributes and methods
Hotel_street: Property = Property(name="street", type=StringType)
Hotel_city: Property = Property(name="city", type=StringType)
Hotel_zip: Property = Property(name="zip", type=IntegerType)
Hotel_coordinates: Property = Property(name="coordinates", type=IntegerType)
Hotel_name: Property = Property(name="name", type=StringType)
Hotel_phoneNumber: Property = Property(name="phoneNumber", type=IntegerType)
Hotel_website: Property = Property(name="website", type=StringType)
Hotel.attributes={Hotel_coordinates, Hotel_phoneNumber, Hotel_name, Hotel_zip, Hotel_city, Hotel_website, Hotel_street}

# Room class attributes and methods
Room_floor: Property = Property(name="floor", type=IntegerType)
Room_door: Property = Property(name="door", type=IntegerType)
Room_capacity: Property = Property(name="capacity", type=StringType)
Room_price: Property = Property(name="price", type=FloatType)
Room.attributes={Room_floor, Room_price, Room_door, Room_capacity}

# Service class attributes and methods
Service_name: Property = Property(name="name", type=StringType)
Service_description: Property = Property(name="description", type=StringType)
Service_basePrice: Property = Property(name="basePrice", type=StringType)
Service.attributes={Service_name, Service_description, Service_basePrice}

# Relationships
Hotel_Room: BinaryAssociation = BinaryAssociation(
    name="Hotel_Room",
    ends={
        Property(name="room0", type=Room, multiplicity=Multiplicity(1, 9999)),
        Property(name="hotel1", type=Hotel, multiplicity=Multiplicity(0, 1))
    }
)
Service_Hotel: BinaryAssociation = BinaryAssociation(
    name="Service_Hotel",
    ends={
        Property(name="hotel2", type=Hotel, multiplicity=Multiplicity(0, 1)),
        Property(name="service3", type=Service, multiplicity=Multiplicity(0, 9999))
    }
)
Customer_Room: BinaryAssociation = BinaryAssociation(
    name="Customer_Room",
    ends={
        Property(name="room4", type=Room, multiplicity=Multiplicity(0, 1)),
        Property(name="customer5", type=Customer, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="f4b0956f_c7bc_48a0_9e65_8bedbbab3fab",
    types={Customer, Hotel, Room, Service},
    associations={Hotel_Room, Service_Hotel, Customer_Room},
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