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

# Enumerations
BookingStatus: Enumeration = Enumeration(
    name="BookingStatus",
    literals={
            
    }
)

# Classes
Guest = Class(name="Guest")
Room = Class(name="Room")
RoomType = Class(name="RoomType")
Booking = Class(name="Booking")
Hotel = Class(name="Hotel")
Guest_Actor = Class(name="Guest_Actor")
Receptionist_Actor = Class(name="Receptionist_Actor")
Manager_Actor = Class(name="Manager_Actor")
Administrator_Actor = Class(name="Administrator_Actor")
Manage_Hotels_UseCase = Class(name="Manage_Hotels_UseCase")
Manage_Room_Types_UseCase = Class(name="Manage_Room_Types_UseCase")
Manage_Rooms_UseCase = Class(name="Manage_Rooms_UseCase")
Make_Booking_UseCase = Class(name="Make_Booking_UseCase")
Cancel_Booking_UseCase = Class(name="Cancel_Booking_UseCase")
Guest_Check_in_UseCase = Class(name="Guest_Check_in_UseCase")
Guest_Check_out_UseCase = Class(name="Guest_Check_out_UseCase")
Contact = Class(name="Contact")
HotelBusiness = Class(name="HotelBusiness")

# Guest class attributes and methods

# Room class attributes and methods
Room_name: Property = Property(name="name", type=StringType)
Room.attributes={Room_name}

# RoomType class attributes and methods
RoomType_name: Property = Property(name="name", type=StringType)
RoomType_pricePerNight: Property = Property(name="pricePerNight", type=StringType)
RoomType.attributes={RoomType_pricePerNight, RoomType_name}

# Booking class attributes and methods
Booking_bookingDate: Property = Property(name="bookingDate", type=StringType)
Booking_checkInDate: Property = Property(name="checkInDate", type=StringType)
Booking_checkOutDate: Property = Property(name="checkOutDate", type=StringType)
Booking__numberOfNights: Property = Property(name="_numberOfNights", type=IntegerType)
Booking.attributes={Booking_bookingDate, Booking__numberOfNights, Booking_checkOutDate, Booking_checkInDate}

# Hotel class attributes and methods
Hotel_name: Property = Property(name="name", type=StringType)
Hotel.attributes={Hotel_name}

# Guest_Actor class attributes and methods

# Receptionist_Actor class attributes and methods

# Manager_Actor class attributes and methods

# Administrator_Actor class attributes and methods

# Manage_Hotels_UseCase class attributes and methods

# Manage_Room_Types_UseCase class attributes and methods

# Manage_Rooms_UseCase class attributes and methods

# Make_Booking_UseCase class attributes and methods

# Cancel_Booking_UseCase class attributes and methods

# Guest_Check_in_UseCase class attributes and methods

# Guest_Check_out_UseCase class attributes and methods

# Contact class attributes and methods
Contact_name: Property = Property(name="name", type=StringType)
Contact_address: Property = Property(name="address", type=StringType)
Contact_email: Property = Property(name="email", type=StringType)
Contact_phone: Property = Property(name="phone", type=StringType)
Contact.attributes={Contact_phone, Contact_name, Contact_email, Contact_address}

# HotelBusiness class attributes and methods

# Relationships
HotelBusiness_Hotel: BinaryAssociation = BinaryAssociation(
    name="HotelBusiness_Hotel",
    ends={
        Property(name="hotel0", type=Hotel, multiplicity=Multiplicity(1, 9999)),
        Property(name="hotelBusiness1", type=HotelBusiness, multiplicity=Multiplicity(1, 1))
    }
)
Hotel_RoomType: BinaryAssociation = BinaryAssociation(
    name="Hotel_RoomType",
    ends={
        Property(name="roomType2", type=RoomType, multiplicity=Multiplicity(1, 9999)),
        Property(name="hotel3", type=Hotel, multiplicity=Multiplicity(1, 1))
    }
)
RoomType_Room: BinaryAssociation = BinaryAssociation(
    name="RoomType_Room",
    ends={
        Property(name="room4", type=Room, multiplicity=Multiplicity(0, 9999)),
        Property(name="roomType5", type=RoomType, multiplicity=Multiplicity(1, 1))
    }
)
Guest_Room: BinaryAssociation = BinaryAssociation(
    name="Guest_Room",
    ends={
        Property(name="occupied6", type=Room, multiplicity=Multiplicity(0, 9999)),
        Property(name="occupant7", type=Guest, multiplicity=Multiplicity(1, 1))
    }
)
_hotel: BinaryAssociation = BinaryAssociation(
    name="_hotel",
    ends={
        Property(name="hotel8", type=Hotel, multiplicity=Multiplicity(1, 1)),
        Property(name="booking9", type=Booking, multiplicity=Multiplicity(0, 9999))
    }
)
Add_delete_Hotels_Administrator: BinaryAssociation = BinaryAssociation(
    name="Add_delete_Hotels_Administrator",
    ends={
        Property(name="administrator10", type=Administrator_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="add_delete_Hotels11", type=Manage_Hotels_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Manager_Add_delete_Room_Types: BinaryAssociation = BinaryAssociation(
    name="Manager_Add_delete_Room_Types",
    ends={
        Property(name="add_delete_Room_Types12", type=Manage_Room_Types_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="manager13", type=Manager_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Manager_Add_delete_Rooms: BinaryAssociation = BinaryAssociation(
    name="Manager_Add_delete_Rooms",
    ends={
        Property(name="add_delete_Rooms14", type=Manage_Rooms_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="manager15", type=Manager_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Guest_Make_Booking: BinaryAssociation = BinaryAssociation(
    name="Guest_Make_Booking",
    ends={
        Property(name="make_Booking16", type=Make_Booking_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="guest17", type=Guest_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Guest_Cancel_Booking: BinaryAssociation = BinaryAssociation(
    name="Guest_Cancel_Booking",
    ends={
        Property(name="cancel_Booking18", type=Cancel_Booking_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="guest19", type=Guest_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Receptionist_Make_Booking: BinaryAssociation = BinaryAssociation(
    name="Receptionist_Make_Booking",
    ends={
        Property(name="make_Booking20", type=Make_Booking_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="receptionist21", type=Receptionist_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Receptionist_Cancel_Booking: BinaryAssociation = BinaryAssociation(
    name="Receptionist_Cancel_Booking",
    ends={
        Property(name="cancel_Booking22", type=Cancel_Booking_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="receptionist23", type=Receptionist_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Receptionist_Guest_Check_in: BinaryAssociation = BinaryAssociation(
    name="Receptionist_Guest_Check_in",
    ends={
        Property(name="guest_Check_in24", type=Guest_Check_in_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="receptionist25", type=Receptionist_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Receptionist_Guest_Check_out: BinaryAssociation = BinaryAssociation(
    name="Receptionist_Guest_Check_out",
    ends={
        Property(name="guest_Check_out26", type=Guest_Check_out_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="receptionist27", type=Receptionist_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Booking_Contact: BinaryAssociation = BinaryAssociation(
    name="Booking_Contact",
    ends={
        Property(name="bookedBy28", type=Contact, multiplicity=Multiplicity(0, 1)),
        Property(name="booking29", type=Booking, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_lFM4sIEyEeipCpVU7M5dbw",
    types={Guest, Room, RoomType, Booking, Hotel, Guest_Actor, Receptionist_Actor, Manager_Actor, Administrator_Actor, Manage_Hotels_UseCase, Manage_Room_Types_UseCase, Manage_Rooms_UseCase, Make_Booking_UseCase, Cancel_Booking_UseCase, Guest_Check_in_UseCase, Guest_Check_out_UseCase, Contact, HotelBusiness, BookingStatus},
    associations={HotelBusiness_Hotel, Hotel_RoomType, RoomType_Room, Guest_Room, _hotel, Add_delete_Hotels_Administrator, Manager_Add_delete_Room_Types, Manager_Add_delete_Rooms, Guest_Make_Booking, Guest_Cancel_Booking, Receptionist_Make_Booking, Receptionist_Cancel_Booking, Receptionist_Guest_Check_in, Receptionist_Guest_Check_out, Booking_Contact},
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