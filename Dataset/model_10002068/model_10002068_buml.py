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
Qaboos_Reservation_System_Enter_flight_Details_UseCase = Class(name="Qaboos_Reservation_System_Enter_flight_Details_UseCase")
Qaboos_Reservation_System_Check_Flights_Availability_UseCase = Class(name="Qaboos_Reservation_System_Check_Flights_Availability_UseCase")
Qaboos_Reservation_System_Book_ticket__UseCase = Class(name="Qaboos_Reservation_System_Book_ticket__UseCase")
Qaboos_Reservation_System_Enter_Passengers_Details_UseCase = Class(name="Qaboos_Reservation_System_Enter_Passengers_Details_UseCase")
Qaboos_Reservation_System_Confirm_booking__UseCase = Class(name="Qaboos_Reservation_System_Confirm_booking__UseCase")
Qaboos_Reservation_System_Make_Payment_UseCase = Class(name="Qaboos_Reservation_System_Make_Payment_UseCase")
Qaboos_Reservation_System_Cancel_booking_UseCase = Class(name="Qaboos_Reservation_System_Cancel_booking_UseCase")
Qaboos_Reservation_System_Check_In_Online_UseCase = Class(name="Qaboos_Reservation_System_Check_In_Online_UseCase")
Qaboos_Reservation_System_Join__Qaboos_FPP_Club_UseCase = Class(name="Qaboos_Reservation_System_Join__Qaboos_FPP_Club_UseCase")
Qaboos_Reservation_System_Update_Flight_Details_UseCase = Class(name="Qaboos_Reservation_System_Update_Flight_Details_UseCase")
Qaboos_Reservation_System_Choose_Seats_UseCase = Class(name="Qaboos_Reservation_System_Choose_Seats_UseCase")
Qaboos_Reservation_System_Manage_Booking_UseCase = Class(name="Qaboos_Reservation_System_Manage_Booking_UseCase")
Customer_Actor = Class(name="Customer_Actor")
Contact_Center_Agent_Actor = Class(name="Contact_Center_Agent_Actor")
Qaboos_Airways = Class(name="Qaboos_Airways")
Passengers = Class(name="Passengers")
Flight = Class(name="Flight")
FFP_Members = Class(name="FFP_Members")
Offers = Class(name="Offers")
Adult = Class(name="Adult")
Child = Class(name="Child")
Infant = Class(name="Infant")
Seats = Class(name="Seats")
Economy_Seats = Class(name="Economy_Seats")
Business_Seats = Class(name="Business_Seats")
First_Class = Class(name="First_Class")

# Qaboos_Reservation_System_Enter_flight_Details_UseCase class attributes and methods

# Qaboos_Reservation_System_Check_Flights_Availability_UseCase class attributes and methods

# Qaboos_Reservation_System_Book_ticket__UseCase class attributes and methods

# Qaboos_Reservation_System_Enter_Passengers_Details_UseCase class attributes and methods

# Qaboos_Reservation_System_Confirm_booking__UseCase class attributes and methods

# Qaboos_Reservation_System_Make_Payment_UseCase class attributes and methods

# Qaboos_Reservation_System_Cancel_booking_UseCase class attributes and methods

# Qaboos_Reservation_System_Check_In_Online_UseCase class attributes and methods

# Qaboos_Reservation_System_Join__Qaboos_FPP_Club_UseCase class attributes and methods

# Qaboos_Reservation_System_Update_Flight_Details_UseCase class attributes and methods

# Qaboos_Reservation_System_Choose_Seats_UseCase class attributes and methods

# Qaboos_Reservation_System_Manage_Booking_UseCase class attributes and methods

# Customer_Actor class attributes and methods

# Contact_Center_Agent_Actor class attributes and methods

# Qaboos_Airways class attributes and methods
Qaboos_Airways_Comp_Commercial_NO: Property = Property(name="Comp_Commercial_NO", type=StringType)
Qaboos_Airways_Comp_location: Property = Property(name="Comp_location", type=StringType)
Qaboos_Airways.attributes={Qaboos_Airways_Comp_location, Qaboos_Airways_Comp_Commercial_NO}

# Passengers class attributes and methods
Passengers_passenger_name: Property = Property(name="passenger_name", type=StringType)
Passengers_Passenger_TKT_No: Property = Property(name="Passenger_TKT_No", type=StringType)
Passengers_Passenger_Details: Property = Property(name="Passenger_Details", type=StringType)
Passengers.attributes={Passengers_Passenger_TKT_No, Passengers_passenger_name, Passengers_Passenger_Details}

# Flight class attributes and methods
Flight_Flgt_NO: Property = Property(name="Flgt_NO", type=StringType)
Flight_Flgt_Details: Property = Property(name="Flgt_Details", type=StringType)
Flight.attributes={Flight_Flgt_Details, Flight_Flgt_NO}

# FFP_Members class attributes and methods
FFP_Members_FFP_ID: Property = Property(name="FFP_ID", type=StringType)
FFP_Members_FFP_Category: Property = Property(name="FFP_Category", type=StringType)
FFP_Members_FFP_Qmiles: Property = Property(name="FFP_Qmiles", type=StringType)
FFP_Members.attributes={FFP_Members_FFP_ID, FFP_Members_FFP_Category, FFP_Members_FFP_Qmiles}

# Offers class attributes and methods
Offers_Offer_NO: Property = Property(name="Offer_NO", type=StringType)
Offers_Offer_Det: Property = Property(name="Offer_Det", type=StringType)
Offers_Offer_Expiry_Date: Property = Property(name="Offer_Expiry_Date", type=StringType)
Offers.attributes={Offers_Offer_NO, Offers_Offer_Det, Offers_Offer_Expiry_Date}

# Adult class attributes and methods
Adult_Adult_ID: Property = Property(name="Adult_ID", type=StringType)
Adult_Adult_Seat_Price: Property = Property(name="Adult_Seat_Price", type=StringType)
Adult.attributes={Adult_Adult_ID, Adult_Adult_Seat_Price}

# Child class attributes and methods
Child_Child_ID: Property = Property(name="Child_ID", type=StringType)
Child_Child_Seat_Price: Property = Property(name="Child_Seat_Price", type=StringType)
Child.attributes={Child_Child_ID, Child_Child_Seat_Price}

# Infant class attributes and methods
Infant_Infant_No: Property = Property(name="Infant_No", type=StringType)
Infant_Infant_Seat_Price: Property = Property(name="Infant_Seat_Price", type=StringType)
Infant.attributes={Infant_Infant_No, Infant_Infant_Seat_Price}

# Seats class attributes and methods
Seats_Seat_ID: Property = Property(name="Seat_ID", type=StringType)
Seats_Seat_NO: Property = Property(name="Seat_NO", type=StringType)
Seats_Seat_Catoegry: Property = Property(name="Seat_Catoegry", type=StringType)
Seats.attributes={Seats_Seat_Catoegry, Seats_Seat_NO, Seats_Seat_ID}

# Economy_Seats class attributes and methods
Economy_Seats_Eco_Seat_ID: Property = Property(name="Eco_Seat_ID", type=StringType)
Economy_Seats_Eco_Seat_Price: Property = Property(name="Eco_Seat_Price", type=StringType)
Economy_Seats.attributes={Economy_Seats_Eco_Seat_ID, Economy_Seats_Eco_Seat_Price}

# Business_Seats class attributes and methods
Business_Seats_Buiss_Seat_ID: Property = Property(name="Buiss_Seat_ID", type=StringType)
Business_Seats_Buiss_Seat_Price: Property = Property(name="Buiss_Seat_Price", type=StringType)
Business_Seats.attributes={Business_Seats_Buiss_Seat_Price, Business_Seats_Buiss_Seat_ID}

# First_Class class attributes and methods
First_Class_First_Seat_ID: Property = Property(name="First_Seat_ID", type=StringType)
First_Class_First_Seat_Price: Property = Property(name="First_Seat_Price", type=StringType)
First_Class.attributes={First_Class_First_Seat_Price, First_Class_First_Seat_ID}

# Relationships
Customer_Join__Qaboos_FPP_Club: BinaryAssociation = BinaryAssociation(
    name="Customer_Join__Qaboos_FPP_Club",
    ends={
        Property(name="customer15", type=Customer_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="join__Qaboos_FPP_Club14", type=Qaboos_Reservation_System_Join__Qaboos_FPP_Club_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Contact_Center_Agent_Update_Flight_Details: BinaryAssociation = BinaryAssociation(
    name="Contact_Center_Agent_Update_Flight_Details",
    ends={
        Property(name="update_Flight_Details16", type=Qaboos_Reservation_System_Update_Flight_Details_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="contact_Center_Agent17", type=Contact_Center_Agent_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Qaboos_Airways_Flight: BinaryAssociation = BinaryAssociation(
    name="Qaboos_Airways_Flight",
    ends={
        Property(name="flight18", type=Flight, multiplicity=Multiplicity(0, 1)),
        Property(name="qaboos_Airways19", type=Qaboos_Airways, multiplicity=Multiplicity(0, 1))
    }
)
Qaboos_Airways_Passengers: BinaryAssociation = BinaryAssociation(
    name="Qaboos_Airways_Passengers",
    ends={
        Property(name="passengers20", type=Passengers, multiplicity=Multiplicity(0, 1)),
        Property(name="qaboos_Airways21", type=Qaboos_Airways, multiplicity=Multiplicity(0, 1))
    }
)
Books: BinaryAssociation = BinaryAssociation(
    name="Books",
    ends={
        Property(name="flight22", type=Flight, multiplicity=Multiplicity(0, 1)),
        Property(name="passengers23", type=Passengers, multiplicity=Multiplicity(0, 1))
    }
)
Checks: BinaryAssociation = BinaryAssociation(
    name="Checks",
    ends={
        Property(name="offers24", type=Offers, multiplicity=Multiplicity(0, 1)),
        Property(name="passengers25", type=Passengers, multiplicity=Multiplicity(0, 1))
    }
)
joins: BinaryAssociation = BinaryAssociation(
    name="joins",
    ends={
        Property(name="fFP_Members26", type=FFP_Members, multiplicity=Multiplicity(0, 1)),
        Property(name="passengers27", type=Passengers, multiplicity=Multiplicity(0, 1))
    }
)
Selects: BinaryAssociation = BinaryAssociation(
    name="Selects",
    ends={
        Property(name="seats28", type=Seats, multiplicity=Multiplicity(0, 1)),
        Property(name="passengers29", type=Passengers, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Enter_flight_Details: BinaryAssociation = BinaryAssociation(
    name="Customer_Enter_flight_Details",
    ends={
        Property(name="enter_flight_Details0", type=Qaboos_Reservation_System_Enter_flight_Details_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer1", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Check_Flights_Availability: BinaryAssociation = BinaryAssociation(
    name="Customer_Check_Flights_Availability",
    ends={
        Property(name="check_Flights_Availability2", type=Qaboos_Reservation_System_Check_Flights_Availability_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer3", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Book_ticket: BinaryAssociation = BinaryAssociation(
    name="Customer_Book_ticket",
    ends={
        Property(name="book_ticket4", type=Qaboos_Reservation_System_Book_ticket__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer5", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Enter_Passengers_Details: BinaryAssociation = BinaryAssociation(
    name="Customer_Enter_Passengers_Details",
    ends={
        Property(name="enter_Passengers_Details6", type=Qaboos_Reservation_System_Enter_Passengers_Details_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer7", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Confirm_booking: BinaryAssociation = BinaryAssociation(
    name="Customer_Confirm_booking",
    ends={
        Property(name="confirm_booking8", type=Qaboos_Reservation_System_Confirm_booking__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer9", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Make_Payment: BinaryAssociation = BinaryAssociation(
    name="Customer_Make_Payment",
    ends={
        Property(name="make_Payment10", type=Qaboos_Reservation_System_Make_Payment_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer11", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Manage_Booking: BinaryAssociation = BinaryAssociation(
    name="Customer_Manage_Booking",
    ends={
        Property(name="manage_Booking12", type=Qaboos_Reservation_System_Manage_Booking_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer13", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_meQiMOjAEeiV94kHgjpOMg",
    types={Qaboos_Reservation_System_Enter_flight_Details_UseCase, Qaboos_Reservation_System_Check_Flights_Availability_UseCase, Qaboos_Reservation_System_Book_ticket__UseCase, Qaboos_Reservation_System_Enter_Passengers_Details_UseCase, Qaboos_Reservation_System_Confirm_booking__UseCase, Qaboos_Reservation_System_Make_Payment_UseCase, Qaboos_Reservation_System_Cancel_booking_UseCase, Qaboos_Reservation_System_Check_In_Online_UseCase, Qaboos_Reservation_System_Join__Qaboos_FPP_Club_UseCase, Qaboos_Reservation_System_Update_Flight_Details_UseCase, Qaboos_Reservation_System_Choose_Seats_UseCase, Qaboos_Reservation_System_Manage_Booking_UseCase, Customer_Actor, Contact_Center_Agent_Actor, Qaboos_Airways, Passengers, Flight, FFP_Members, Offers, Adult, Child, Infant, Seats, Economy_Seats, Business_Seats, First_Class},
    associations={Customer_Join__Qaboos_FPP_Club, Contact_Center_Agent_Update_Flight_Details, Qaboos_Airways_Flight, Qaboos_Airways_Passengers, Books, Checks, joins, Selects, Customer_Enter_flight_Details, Customer_Check_Flights_Availability, Customer_Book_ticket, Customer_Enter_Passengers_Details, Customer_Confirm_booking, Customer_Make_Payment, Customer_Manage_Booking},
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