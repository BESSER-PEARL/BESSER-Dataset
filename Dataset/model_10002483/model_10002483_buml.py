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
Owner = Class(name="Owner")
Hotels = Class(name="Hotels")
Rooms = Class(name="Rooms")
Location = Class(name="Location")
User = Class(name="User")
Booking = Class(name="Booking")
occupancy = Class(name="occupancy")

# Owner class attributes and methods
Owner_Name: Property = Property(name="Name", type=StringType)
Owner_ID: Property = Property(name="ID", type=IntegerType)
Owner_Phn_no_: Property = Property(name="Phn_no_", type=Owner)
Owner_Address: Property = Property(name="Address", type=StringType)
Owner_email_id: Property = Property(name="email_id", type=IntegerType)
Owner_password: Property = Property(name="password", type=IntegerType)
Owner.attributes={Owner_email_id, Owner_ID, Owner_Name, Owner_Phn_no_, Owner_password, Owner_Address}

# Hotels class attributes and methods
Hotels_id: Property = Property(name="id", type=IntegerType)
Hotels_name: Property = Property(name="name", type=IntegerType)
Hotels_hotel_description: Property = Property(name="hotel_description", type=IntegerType)
Hotels.attributes={Hotels_name, Hotels_id, Hotels_hotel_description}

# Rooms class attributes and methods
Rooms_id: Property = Property(name="id", type=IntegerType)
Rooms_name: Property = Property(name="name", type=StringType)
Rooms_room_description: Property = Property(name="room_description", type=StringType)
Rooms_price: Property = Property(name="price", type=IntegerType)
Rooms_checkin_date: Property = Property(name="checkin_date", type=IntegerType)
Rooms_checkout_date: Property = Property(name="checkout_date", type=IntegerType)
Rooms.attributes={Rooms_room_description, Rooms_name, Rooms_checkout_date, Rooms_price, Rooms_id, Rooms_checkin_date}

# Location class attributes and methods
Location_loc_name: Property = Property(name="loc_name", type=StringType)
Location_loc_id: Property = Property(name="loc_id", type=IntegerType)
Location_attribute: Property = Property(name="attribute", type=StringType)
Location.attributes={Location_attribute, Location_loc_name, Location_loc_id}

# User class attributes and methods
User_Name: Property = Property(name="Name", type=StringType)
User_phn_no: Property = Property(name="phn_no", type=IntegerType)
User_id: Property = Property(name="id", type=IntegerType)
User_mail_id: Property = Property(name="mail_id", type=StringType)
User_address: Property = Property(name="address", type=StringType)
User_password: Property = Property(name="password", type=IntegerType)
User.attributes={User_phn_no, User_mail_id, User_address, User_Name, User_password, User_id}

# Booking class attributes and methods
Booking_booking_id: Property = Property(name="booking_id", type=IntegerType)
Booking_user_id: Property = Property(name="user_id", type=IntegerType)
Booking_guest_name: Property = Property(name="guest_name", type=IntegerType)
Booking_guest_id: Property = Property(name="guest_id", type=IntegerType)
Booking_guestphn_no: Property = Property(name="guestphn_no", type=IntegerType)
Booking_guest_adress: Property = Property(name="guest_adress", type=StringType)
Booking.attributes={Booking_guest_id, Booking_booking_id, Booking_guest_adress, Booking_user_id, Booking_guest_name, Booking_guestphn_no}

# occupancy class attributes and methods
occupancy_booking_id: Property = Property(name="booking_id", type=IntegerType)
occupancy.attributes={occupancy_booking_id}

# Relationships
Hotels_Rooms: BinaryAssociation = BinaryAssociation(
    name="Hotels_Rooms",
    ends={
        Property(name="rooms2", type=Rooms, multiplicity=Multiplicity(0, 1)),
        Property(name="hotels3", type=Hotels, multiplicity=Multiplicity(0, 1))
    }
)
User_Booking: BinaryAssociation = BinaryAssociation(
    name="User_Booking",
    ends={
        Property(name="User_Booking_04", type=Booking, multiplicity=Multiplicity(0, 1)),
        Property(name="User_Booking_15", type=User, multiplicity=Multiplicity(0, 1))
    }
)
Hotels_Owner: BinaryAssociation = BinaryAssociation(
    name="Hotels_Owner",
    ends={
        Property(name="owner6", type=Owner, multiplicity=Multiplicity(0, 1)),
        Property(name="hotels7", type=Hotels, multiplicity=Multiplicity(0, 1))
    }
)
Rooms_Booking: BinaryAssociation = BinaryAssociation(
    name="Rooms_Booking",
    ends={
        Property(name="booking8", type=Booking, multiplicity=Multiplicity(0, 1)),
        Property(name="rooms9", type=Rooms, multiplicity=Multiplicity(0, 1))
    }
)
occupancy_Booking: BinaryAssociation = BinaryAssociation(
    name="occupancy_Booking",
    ends={
        Property(name="occupancy_Booking_010", type=Booking, multiplicity=Multiplicity(0, 1)),
        Property(name="occupancy_Booking_111", type=occupancy, multiplicity=Multiplicity(0, 1))
    }
)
City_Hotels: BinaryAssociation = BinaryAssociation(
    name="City_Hotels",
    ends={
        Property(name="hotels0", type=Hotels, multiplicity=Multiplicity(0, 1)),
        Property(name="city1", type=Location, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="b8ca60f2_dbf5_4436_a9a6_b69d752118cf",
    types={Owner, Hotels, Rooms, Location, User, Booking, occupancy},
    associations={Hotels_Rooms, User_Booking, Hotels_Owner, Rooms_Booking, occupancy_Booking, City_Hotels},
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