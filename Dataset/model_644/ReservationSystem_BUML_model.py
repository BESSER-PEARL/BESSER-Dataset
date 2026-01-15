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
reservationsystem_User = Class(name="reservationsystem::User")
reservationsystem_Crew = Class(name="reservationsystem::Crew", is_abstract=True)
reservationsystem_Person = Class(name="reservationsystem::Person", is_abstract=True)
reservationsystem_SpecificFlight = Class(name="reservationsystem::SpecificFlight")
reservationsystem_Passenger = Class(name="reservationsystem::Passenger")
reservationsystem_Booking = Class(name="reservationsystem::Booking")
reservationsystem_Pilot = Class(name="reservationsystem::Pilot")
Crew = Class(name="Crew")
reservationsystem_Attendant = Class(name="reservationsystem::Attendant")
Person = Class(name="Person")
reservationsystem_Seat = Class(name="reservationsystem::Seat")
reservationsystem_GeneralFlight = Class(name="reservationsystem::GeneralFlight")
reservationsystem_Airport = Class(name="reservationsystem::Airport")
reservationsystem_PaymentInfo = Class(name="reservationsystem::PaymentInfo")
reservationsystem_Plane = Class(name="reservationsystem::Plane")
reservationsystem_City = Class(name="reservationsystem::City")
Booking = Class(name="Booking")

# reservationsystem_User class attributes and methods
reservationsystem_User_userType: Property = Property(name="userType", type=StringType)
reservationsystem_User_userName: Property = Property(name="userName", type=StringType)
reservationsystem_User_md5Pwd: Property = Property(name="md5Pwd", type=StringType)
reservationsystem_User.attributes={reservationsystem_User_md5Pwd, reservationsystem_User_userType, reservationsystem_User_userName}

# reservationsystem_Crew class attributes and methods
reservationsystem_Crew_employeeId: Property = Property(name="employeeId", type=StringType)
reservationsystem_Crew_m_setLeader: Method = Method(name="setLeader", parameters={})
reservationsystem_Crew.attributes={reservationsystem_Crew_employeeId}
reservationsystem_Crew.methods={reservationsystem_Crew_m_setLeader}

# reservationsystem_Person class attributes and methods
reservationsystem_Person_name: Property = Property(name="name", type=StringType)
reservationsystem_Person_addr: Property = Property(name="addr", type=StringType)
reservationsystem_Person_phone: Property = Property(name="phone", type=StringType)
reservationsystem_Person_citizenship: Property = Property(name="citizenship", type=StringType)
reservationsystem_Person_residence: Property = Property(name="residence", type=StringType)
reservationsystem_Person_middleName: Property = Property(name="middleName", type=StringType)
reservationsystem_Person_FamilyName: Property = Property(name="FamilyName", type=StringType)
reservationsystem_Person_birthDate: Property = Property(name="birthDate", type=DateType)
reservationsystem_Person_id: Property = Property(name="id", type=IntegerType)
reservationsystem_Person_passportId: Property = Property(name="passportId", type=StringType)
reservationsystem_Person_email: Property = Property(name="email", type=StringType)
reservationsystem_Person_gender: Property = Property(name="gender", type=IntegerType)
reservationsystem_Person.attributes={reservationsystem_Person_birthDate, reservationsystem_Person_FamilyName, reservationsystem_Person_citizenship, reservationsystem_Person_residence, reservationsystem_Person_passportId, reservationsystem_Person_id, reservationsystem_Person_email, reservationsystem_Person_name, reservationsystem_Person_middleName, reservationsystem_Person_gender, reservationsystem_Person_addr, reservationsystem_Person_phone}

# reservationsystem_SpecificFlight class attributes and methods
reservationsystem_SpecificFlight_id: Property = Property(name="id", type=IntegerType)
reservationsystem_SpecificFlight_date: Property = Property(name="date", type=DateType)
reservationsystem_SpecificFlight_realDepTime: Property = Property(name="realDepTime", type=DateType)
reservationsystem_SpecificFlight_realArriTime: Property = Property(name="realArriTime", type=DateType)
reservationsystem_SpecificFlight_status: Property = Property(name="status", type=IntegerType)
reservationsystem_SpecificFlight_m_assignPilot: Method = Method(name="assignPilot", parameters={Parameter(name='personId')})
reservationsystem_SpecificFlight_m_assignAttd: Method = Method(name="assignAttd", parameters={Parameter(name='personId')})
reservationsystem_SpecificFlight.attributes={reservationsystem_SpecificFlight_id, reservationsystem_SpecificFlight_date, reservationsystem_SpecificFlight_realDepTime, reservationsystem_SpecificFlight_realArriTime, reservationsystem_SpecificFlight_status}
reservationsystem_SpecificFlight.methods={reservationsystem_SpecificFlight_m_assignPilot, reservationsystem_SpecificFlight_m_assignAttd}

# reservationsystem_Passenger class attributes and methods
reservationsystem_Passenger_specialNeeds: Property = Property(name="specialNeeds", type=StringType)
reservationsystem_Passenger_foodPref: Property = Property(name="foodPref", type=StringType)
reservationsystem_Passenger.attributes={reservationsystem_Passenger_specialNeeds, reservationsystem_Passenger_foodPref}

# reservationsystem_Booking class attributes and methods
reservationsystem_Booking_bookNo: Property = Property(name="bookNo", type=StringType)
reservationsystem_Booking_bookingStatus: Property = Property(name="bookingStatus", type=IntegerType)
reservationsystem_Booking_baggageInfo: Property = Property(name="baggageInfo", type=StringType)
reservationsystem_Booking.attributes={reservationsystem_Booking_baggageInfo, reservationsystem_Booking_bookNo, reservationsystem_Booking_bookingStatus}

# reservationsystem_Pilot class attributes and methods
reservationsystem_Pilot_certificationId: Property = Property(name="certificationId", type=StringType)
reservationsystem_Pilot_experience: Property = Property(name="experience", type=IntegerType)
reservationsystem_Pilot.attributes={reservationsystem_Pilot_experience, reservationsystem_Pilot_certificationId}

# Crew class attributes and methods

# reservationsystem_Attendant class attributes and methods

# Person class attributes and methods

# reservationsystem_Seat class attributes and methods
reservationsystem_Seat_no: Property = Property(name="no", type=StringType)
reservationsystem_Seat_type: Property = Property(name="type", type=IntegerType)
reservationsystem_Seat_isExit: Property = Property(name="isExit", type=BooleanType)
reservationsystem_Seat.attributes={reservationsystem_Seat_no, reservationsystem_Seat_isExit, reservationsystem_Seat_type}

# reservationsystem_GeneralFlight class attributes and methods
reservationsystem_GeneralFlight_flightNo: Property = Property(name="flightNo", type=StringType)
reservationsystem_GeneralFlight_departureTime: Property = Property(name="departureTime", type=StringType)
reservationsystem_GeneralFlight_arrivalTime: Property = Property(name="arrivalTime", type=StringType)
reservationsystem_GeneralFlight.attributes={reservationsystem_GeneralFlight_arrivalTime, reservationsystem_GeneralFlight_flightNo, reservationsystem_GeneralFlight_departureTime}

# reservationsystem_Airport class attributes and methods
reservationsystem_Airport_id: Property = Property(name="id", type=IntegerType)
reservationsystem_Airport_name: Property = Property(name="name", type=StringType)
reservationsystem_Airport_abbr: Property = Property(name="abbr", type=StringType)
reservationsystem_Airport.attributes={reservationsystem_Airport_name, reservationsystem_Airport_id, reservationsystem_Airport_abbr}

# reservationsystem_PaymentInfo class attributes and methods
reservationsystem_PaymentInfo_id: Property = Property(name="id", type=StringType)
reservationsystem_PaymentInfo_createTime: Property = Property(name="createTime", type=DateType)
reservationsystem_PaymentInfo_status: Property = Property(name="status", type=IntegerType)
reservationsystem_PaymentInfo_payTime: Property = Property(name="payTime", type=DateType)
reservationsystem_PaymentInfo_type: Property = Property(name="type", type=IntegerType)
reservationsystem_PaymentInfo_cardNo: Property = Property(name="cardNo", type=StringType)
reservationsystem_PaymentInfo_cardOwner: Property = Property(name="cardOwner", type=StringType)
reservationsystem_PaymentInfo_cardAddr: Property = Property(name="cardAddr", type=StringType)
reservationsystem_PaymentInfo.attributes={reservationsystem_PaymentInfo_payTime, reservationsystem_PaymentInfo_status, reservationsystem_PaymentInfo_id, reservationsystem_PaymentInfo_cardNo, reservationsystem_PaymentInfo_createTime, reservationsystem_PaymentInfo_cardOwner, reservationsystem_PaymentInfo_type, reservationsystem_PaymentInfo_cardAddr}

# reservationsystem_Plane class attributes and methods
reservationsystem_Plane_id: Property = Property(name="id", type=StringType)
reservationsystem_Plane_model: Property = Property(name="model", type=StringType)
reservationsystem_Plane_crewNum: Property = Property(name="crewNum", type=IntegerType)
reservationsystem_Plane_capacity: Property = Property(name="capacity", type=IntegerType)
reservationsystem_Plane.attributes={reservationsystem_Plane_capacity, reservationsystem_Plane_model, reservationsystem_Plane_id, reservationsystem_Plane_crewNum}

# reservationsystem_City class attributes and methods
reservationsystem_City_id: Property = Property(name="id", type=IntegerType)
reservationsystem_City_name: Property = Property(name="name", type=StringType)
reservationsystem_City_abbr: Property = Property(name="abbr", type=StringType)
reservationsystem_City.attributes={reservationsystem_City_abbr, reservationsystem_City_id, reservationsystem_City_name}

# Booking class attributes and methods

# Relationships
belongsTo0: BinaryAssociation = BinaryAssociation(
    name="belongsTo0",
    ends={
        Property(name="reservationsystem_Person", type=reservationsystem_User, multiplicity=Multiplicity(1, 1)),
        Property(name="reservationsystem_User", type=reservationsystem_Person, multiplicity=Multiplicity(1, 1))
    }
)
Leader2: BinaryAssociation = BinaryAssociation(
    name="Leader2",
    ends={
        Property(name="reservationsystem_Crew", type=reservationsystem_Crew, multiplicity=Multiplicity(1, 1)),
        Property(name="reservationsystem_Crew1", type=reservationsystem_Crew, multiplicity=Multiplicity(1, 1))
    }
)
specificFlight3: BinaryAssociation = BinaryAssociation(
    name="specificFlight3",
    ends={
        Property(name="SpecificFlight", type=reservationsystem_Crew, multiplicity=Multiplicity(1, 1)),
        Property(name="crew", type=reservationsystem_SpecificFlight, multiplicity=Multiplicity(0, 9999))
    }
)
passenger4: BinaryAssociation = BinaryAssociation(
    name="passenger4",
    ends={
        Property(name="reservationsystem_Booking", type=reservationsystem_Passenger, multiplicity=Multiplicity(1, 1)),
        Property(name="reservationsystem_Passenger", type=reservationsystem_Booking, multiplicity=Multiplicity(0, 1))
    }
)
booking5: BinaryAssociation = BinaryAssociation(
    name="booking5",
    ends={
        Property(name="Booking", type=reservationsystem_Passenger, multiplicity=Multiplicity(1, 1)),
        Property(name="passenger", type=reservationsystem_Booking, multiplicity=Multiplicity(1, 1))
    }
)
passenger8: BinaryAssociation = BinaryAssociation(
    name="passenger8",
    ends={
        Property(name="Passenger", type=reservationsystem_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="booking", type=reservationsystem_Passenger, multiplicity=Multiplicity(1, 9999))
    }
)
specificFlight9: BinaryAssociation = BinaryAssociation(
    name="specificFlight9",
    ends={
        Property(name="SpecificFlight11", type=reservationsystem_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="booking10", type=reservationsystem_SpecificFlight, multiplicity=Multiplicity(1, 9999))
    }
)
seats12: BinaryAssociation = BinaryAssociation(
    name="seats12",
    ends={
        Property(name="Seat", type=reservationsystem_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="book", type=reservationsystem_Seat, multiplicity=Multiplicity(1, 9999))
    }
)
specificFlight13: BinaryAssociation = BinaryAssociation(
    name="specificFlight13",
    ends={
        Property(name="SpecificFlight14", type=reservationsystem_GeneralFlight, multiplicity=Multiplicity(1, 1)),
        Property(name="generalFlight", type=reservationsystem_SpecificFlight, multiplicity=Multiplicity(1, 9999))
    }
)
from15: BinaryAssociation = BinaryAssociation(
    name="from15",
    ends={
        Property(name="reservationsystem_Airport", type=reservationsystem_GeneralFlight, multiplicity=Multiplicity(1, 1)),
        Property(name="reservationsystem_GeneralFlight", type=reservationsystem_Airport, multiplicity=Multiplicity(1, 1))
    }
)
to16: BinaryAssociation = BinaryAssociation(
    name="to16",
    ends={
        Property(name="reservationsystem_Airport18", type=reservationsystem_GeneralFlight, multiplicity=Multiplicity(1, 1)),
        Property(name="reservationsystem_GeneralFlight17", type=reservationsystem_Airport, multiplicity=Multiplicity(1, 1))
    }
)
paymentInfo6: BinaryAssociation = BinaryAssociation(
    name="paymentInfo6",
    ends={
        Property(name="reservationsystem_PaymentInfo", type=reservationsystem_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="reservationsystem_Booking7", type=reservationsystem_PaymentInfo, multiplicity=Multiplicity(0, 9999))
    }
)
generalFlight19: BinaryAssociation = BinaryAssociation(
    name="generalFlight19",
    ends={
        Property(name="GeneralFlight", type=reservationsystem_SpecificFlight, multiplicity=Multiplicity(1, 1)),
        Property(name="specificFlight", type=reservationsystem_GeneralFlight, multiplicity=Multiplicity(1, 1))
    }
)
plane20: BinaryAssociation = BinaryAssociation(
    name="plane20",
    ends={
        Property(name="Plane", type=reservationsystem_SpecificFlight, multiplicity=Multiplicity(1, 1)),
        Property(name="specificFlight21", type=reservationsystem_Plane, multiplicity=Multiplicity(1, 1))
    }
)
crew22: BinaryAssociation = BinaryAssociation(
    name="crew22",
    ends={
        Property(name="Crew", type=reservationsystem_SpecificFlight, multiplicity=Multiplicity(1, 1)),
        Property(name="specificFlight23", type=reservationsystem_Crew, multiplicity=Multiplicity(1, 9999))
    }
)
booking24: BinaryAssociation = BinaryAssociation(
    name="booking24",
    ends={
        Property(name="Booking26", type=reservationsystem_SpecificFlight, multiplicity=Multiplicity(1, 1)),
        Property(name="specificFlight25", type=reservationsystem_Booking, multiplicity=Multiplicity(0, 9999))
    }
)
specificFlight27: BinaryAssociation = BinaryAssociation(
    name="specificFlight27",
    ends={
        Property(name="SpecificFlight28", type=reservationsystem_Plane, multiplicity=Multiplicity(1, 1)),
        Property(name="plane", type=reservationsystem_SpecificFlight, multiplicity=Multiplicity(0, 9999))
    }
)
seats29: BinaryAssociation = BinaryAssociation(
    name="seats29",
    ends={
        Property(name="Seat31", type=reservationsystem_Plane, multiplicity=Multiplicity(1, 1)),
        Property(name="plane30", type=reservationsystem_Seat, multiplicity=Multiplicity(1, 9999))
    }
)
city32: BinaryAssociation = BinaryAssociation(
    name="city32",
    ends={
        Property(name="City", type=reservationsystem_Airport, multiplicity=Multiplicity(1, 1)),
        Property(name="airport", type=reservationsystem_City, multiplicity=Multiplicity(1, 1))
    }
)
airport33: BinaryAssociation = BinaryAssociation(
    name="airport33",
    ends={
        Property(name="Airport", type=reservationsystem_City, multiplicity=Multiplicity(1, 1)),
        Property(name="city", type=reservationsystem_Airport, multiplicity=Multiplicity(0, 9999))
    }
)
plane34: BinaryAssociation = BinaryAssociation(
    name="plane34",
    ends={
        Property(name="Plane35", type=reservationsystem_Seat, multiplicity=Multiplicity(1, 1)),
        Property(name="seats", type=reservationsystem_Plane, multiplicity=Multiplicity(1, 1))
    }
)
book36: BinaryAssociation = BinaryAssociation(
    name="book36",
    ends={
        Property(name="Booking38", type=reservationsystem_Seat, multiplicity=Multiplicity(1, 1)),
        Property(name="seats37", type=reservationsystem_Booking, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_reservationsystem_Passenger_Person = Generalization(general=Person, specific=reservationsystem_Passenger)
gen_reservationsystem_Pilot_Crew = Generalization(general=Crew, specific=reservationsystem_Pilot)
gen_reservationsystem_Attendant_Crew = Generalization(general=Crew, specific=reservationsystem_Attendant)
gen_reservationsystem_Crew_Person = Generalization(general=Person, specific=reservationsystem_Crew)
gen_reservationsystem_PaymentInfo_Booking = Generalization(general=Booking, specific=reservationsystem_PaymentInfo)

# Domain Model
domain_model = DomainModel(
    name="reservationsystem",
    types={reservationsystem_User, reservationsystem_Crew, reservationsystem_Person, reservationsystem_SpecificFlight, reservationsystem_Passenger, reservationsystem_Booking, reservationsystem_Pilot, Crew, reservationsystem_Attendant, Person, reservationsystem_Seat, reservationsystem_GeneralFlight, reservationsystem_Airport, reservationsystem_PaymentInfo, reservationsystem_Plane, reservationsystem_City, Booking},
    associations={belongsTo0, Leader2, specificFlight3, passenger4, booking5, passenger8, specificFlight9, seats12, specificFlight13, from15, to16, paymentInfo6, generalFlight19, plane20, crew22, booking24, specificFlight27, seats29, city32, airport33, plane34, book36},
    generalizations={gen_reservationsystem_Passenger_Person, gen_reservationsystem_Pilot_Crew, gen_reservationsystem_Attendant_Crew, gen_reservationsystem_Crew_Person, gen_reservationsystem_PaymentInfo_Booking},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)