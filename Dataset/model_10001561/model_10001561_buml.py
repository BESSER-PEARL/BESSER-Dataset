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
Users = Class(name="Users")
Hotel = Class(name="Hotel")
Room = Class(name="Room")
Service = Class(name="Service")

# Users class attributes and methods
Users_user_mail: Property = Property(name="user_mail", type=StringType)
Users_first_name: Property = Property(name="first_name", type=StringType)
Users_last_name: Property = Property(name="last_name", type=IntegerType)
Users_user_role: Property = Property(name="user_role", type=StringType)
Users_user_address: Property = Property(name="user_address", type=StringType)
Users_user_phone_no: Property = Property(name="user_phone_no", type=IntegerType)
Users_user_addr_state: Property = Property(name="user_addr_state", type=StringType)
Users_user_addr_city: Property = Property(name="user_addr_city", type=StringType)
Users_user_address1: Property = Property(name="user_address1", type=StringType)
Users.attributes={Users_user_address1, Users_user_role, Users_first_name, Users_user_addr_city, Users_user_phone_no, Users_user_address, Users_last_name, Users_user_addr_state, Users_user_mail}

# Hotel class attributes and methods
Hotel_name: Property = Property(name="name", type=StringType)
Hotel_street: Property = Property(name="street", type=StringType)
Hotel_city: Property = Property(name="city", type=StringType)
Hotel_zip: Property = Property(name="zip", type=IntegerType)
Hotel_coordinates: Property = Property(name="coordinates", type=IntegerType)
Hotel_phoneNumber: Property = Property(name="phoneNumber", type=IntegerType)
Hotel_website: Property = Property(name="website", type=StringType)
Hotel.attributes={Hotel_website, Hotel_street, Hotel_city, Hotel_phoneNumber, Hotel_name, Hotel_zip, Hotel_coordinates}

# Room class attributes and methods
Room_room_id: Property = Property(name="room_id", type=IntegerType)
Room_room_name: Property = Property(name="room_name", type=StringType)
Room_room_rent_night: Property = Property(name="room_rent_night", type=FloatType)
Room_room_no_bedroom: Property = Property(name="room_no_bedroom", type=IntegerType)
Room_room_no_bathroom: Property = Property(name="room_no_bathroom", type=IntegerType)
Room_room_size_interior: Property = Property(name="room_size_interior", type=IntegerType)
Room.attributes={Room_room_name, Room_room_size_interior, Room_room_rent_night, Room_room_id, Room_room_no_bathroom, Room_room_no_bedroom}

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
        Property(name="customer5", type=Users, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_FphYkIsyEeq3N_Xh6gsEIQ",
    types={Users, Hotel, Room, Service},
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