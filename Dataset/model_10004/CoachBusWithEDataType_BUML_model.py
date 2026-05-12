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
Sex: Enumeration = Enumeration(
    name="Sex",
    literals={
            EnumerationLiteral(name="male"),
			EnumerationLiteral(name="female")
    }
)

# Classes
CoachBusWithEDataType_SecurityGuard = Class(name="CoachBusWithEDataType_SecurityGuard")
CoachBusWithEDataType_BookingOffice = Class(name="CoachBusWithEDataType_BookingOffice")
CoachBusWithEDataType_Ticket = Class(name="CoachBusWithEDataType_Ticket")
CoachBusWithEDataType_Employee = Class(name="CoachBusWithEDataType_Employee")
CoachBusWithEDataType_Trip = Class(name="CoachBusWithEDataType_Trip")
CoachBusWithEDataType_Coach = Class(name="CoachBusWithEDataType_Coach")
CoachBusWithEDataType_Passenger = Class(name="CoachBusWithEDataType_Passenger")
CoachBusWithEDataType_RegularTrip = Class(name="CoachBusWithEDataType_RegularTrip")
Trip = Class(name="Trip")
CoachBusWithEDataType_PrivateTrip = Class(name="CoachBusWithEDataType_PrivateTrip")
CoachBusWithEDataType_VendingMachine = Class(name="CoachBusWithEDataType_VendingMachine")
Employee = Class(name="Employee")
CoachBusWithEDataType_Manager = Class(name="CoachBusWithEDataType_Manager")
CoachBusWithEDataType_AdultTicket = Class(name="CoachBusWithEDataType_AdultTicket")
Ticket = Class(name="Ticket")
CoachBusWithEDataType_ChildTicket = Class(name="CoachBusWithEDataType_ChildTicket")

# CoachBusWithEDataType_SecurityGuard class attributes and methods
CoachBusWithEDataType_SecurityGuard_shift: Property = Property(name="shift", type=StringType)
CoachBusWithEDataType_SecurityGuard.attributes={CoachBusWithEDataType_SecurityGuard_shift}

# CoachBusWithEDataType_BookingOffice class attributes and methods
CoachBusWithEDataType_BookingOffice_name: Property = Property(name="name", type=StringType)
CoachBusWithEDataType_BookingOffice_location: Property = Property(name="location", type=StringType)
CoachBusWithEDataType_BookingOffice_officeID: Property = Property(name="officeID", type=IntegerType)
CoachBusWithEDataType_BookingOffice.attributes={CoachBusWithEDataType_BookingOffice_location, CoachBusWithEDataType_BookingOffice_name, CoachBusWithEDataType_BookingOffice_officeID}

# CoachBusWithEDataType_Ticket class attributes and methods
CoachBusWithEDataType_Ticket_number: Property = Property(name="number", type=IntegerType)
CoachBusWithEDataType_Ticket_price: Property = Property(name="price", type=FloatType)
CoachBusWithEDataType_Ticket_isRoundTrip: Property = Property(name="isRoundTrip", type=BooleanType)
CoachBusWithEDataType_Ticket.attributes={CoachBusWithEDataType_Ticket_price, CoachBusWithEDataType_Ticket_isRoundTrip, CoachBusWithEDataType_Ticket_number}

# CoachBusWithEDataType_Employee class attributes and methods
CoachBusWithEDataType_Employee_id: Property = Property(name="id", type=IntegerType)
CoachBusWithEDataType_Employee_baseSalary: Property = Property(name="baseSalary", type=FloatType)
CoachBusWithEDataType_Employee.attributes={CoachBusWithEDataType_Employee_baseSalary, CoachBusWithEDataType_Employee_id}

# CoachBusWithEDataType_Trip class attributes and methods
CoachBusWithEDataType_Trip_name: Property = Property(name="name", type=StringType)
CoachBusWithEDataType_Trip_origin: Property = Property(name="origin", type=StringType)
CoachBusWithEDataType_Trip_destination: Property = Property(name="destination", type=StringType)
CoachBusWithEDataType_Trip_type: Property = Property(name="type", type=StringType)
CoachBusWithEDataType_Trip_number: Property = Property(name="number", type=IntegerType)
CoachBusWithEDataType_Trip.attributes={CoachBusWithEDataType_Trip_destination, CoachBusWithEDataType_Trip_origin, CoachBusWithEDataType_Trip_number, CoachBusWithEDataType_Trip_name, CoachBusWithEDataType_Trip_type}

# CoachBusWithEDataType_Coach class attributes and methods
CoachBusWithEDataType_Coach_id: Property = Property(name="id", type=IntegerType)
CoachBusWithEDataType_Coach_name: Property = Property(name="name", type=StringType)
CoachBusWithEDataType_Coach_model: Property = Property(name="model", type=StringType)
CoachBusWithEDataType_Coach_noOfSeats: Property = Property(name="noOfSeats", type=IntegerType)
CoachBusWithEDataType_Coach.attributes={CoachBusWithEDataType_Coach_noOfSeats, CoachBusWithEDataType_Coach_name, CoachBusWithEDataType_Coach_model, CoachBusWithEDataType_Coach_id}

# CoachBusWithEDataType_Passenger class attributes and methods
CoachBusWithEDataType_Passenger_name: Property = Property(name="name", type=StringType)
CoachBusWithEDataType_Passenger_age: Property = Property(name="age", type=IntegerType)
CoachBusWithEDataType_Passenger_idCard: Property = Property(name="idCard", type=StringType)
CoachBusWithEDataType_Passenger_sex: Property = Property(name="sex", type=StringType)
CoachBusWithEDataType_Passenger.attributes={CoachBusWithEDataType_Passenger_idCard, CoachBusWithEDataType_Passenger_sex, CoachBusWithEDataType_Passenger_age, CoachBusWithEDataType_Passenger_name}

# CoachBusWithEDataType_RegularTrip class attributes and methods

# Trip class attributes and methods

# CoachBusWithEDataType_PrivateTrip class attributes and methods
CoachBusWithEDataType_PrivateTrip_extras: Property = Property(name="extras", type=StringType)
CoachBusWithEDataType_PrivateTrip.attributes={CoachBusWithEDataType_PrivateTrip_extras}

# CoachBusWithEDataType_VendingMachine class attributes and methods
CoachBusWithEDataType_VendingMachine_number: Property = Property(name="number", type=IntegerType)
CoachBusWithEDataType_VendingMachine.attributes={CoachBusWithEDataType_VendingMachine_number}

# Employee class attributes and methods

# CoachBusWithEDataType_Manager class attributes and methods
CoachBusWithEDataType_Manager_hasMBA: Property = Property(name="hasMBA", type=BooleanType)
CoachBusWithEDataType_Manager.attributes={CoachBusWithEDataType_Manager_hasMBA}

# CoachBusWithEDataType_AdultTicket class attributes and methods
CoachBusWithEDataType_AdultTicket_isElderlyDiscount: Property = Property(name="isElderlyDiscount", type=BooleanType)
CoachBusWithEDataType_AdultTicket.attributes={CoachBusWithEDataType_AdultTicket_isElderlyDiscount}

# Ticket class attributes and methods

# CoachBusWithEDataType_ChildTicket class attributes and methods
CoachBusWithEDataType_ChildTicket_isSchoolTrip: Property = Property(name="isSchoolTrip", type=BooleanType)
CoachBusWithEDataType_ChildTicket.attributes={CoachBusWithEDataType_ChildTicket_isSchoolTrip}

# Relationships
guards4: BinaryAssociation = BinaryAssociation(
    name="guards4",
    ends={
        Property(name="SecurityGuard", type=CoachBusWithEDataType_Coach, multiplicity=Multiplicity(1, 1)),
        Property(name="coach", type=CoachBusWithEDataType_SecurityGuard, multiplicity=Multiplicity(0, 9999))
    }
)
offices5: BinaryAssociation = BinaryAssociation(
    name="offices5",
    ends={
        Property(name="BookingOffice", type=CoachBusWithEDataType_Coach, multiplicity=Multiplicity(1, 1)),
        Property(name="coaches6", type=CoachBusWithEDataType_BookingOffice, multiplicity=Multiplicity(0, 9999))
    }
)
trips7: BinaryAssociation = BinaryAssociation(
    name="trips7",
    ends={
        Property(name="Trip8", type=CoachBusWithEDataType_Passenger, multiplicity=Multiplicity(1, 1)),
        Property(name="passengers", type=CoachBusWithEDataType_Trip, multiplicity=Multiplicity(1, 9999))
    }
)
tickets9: BinaryAssociation = BinaryAssociation(
    name="tickets9",
    ends={
        Property(name="Ticket", type=CoachBusWithEDataType_Passenger, multiplicity=Multiplicity(1, 1)),
        Property(name="psg", type=CoachBusWithEDataType_Ticket, multiplicity=Multiplicity(0, 9999))
    }
)
coaches0: BinaryAssociation = BinaryAssociation(
    name="coaches0",
    ends={
        Property(name="Coach", type=CoachBusWithEDataType_Trip, multiplicity=Multiplicity(1, 1)),
        Property(name="trips", type=CoachBusWithEDataType_Coach, multiplicity=Multiplicity(1, 9999))
    }
)
passengers1: BinaryAssociation = BinaryAssociation(
    name="passengers1",
    ends={
        Property(name="Passenger", type=CoachBusWithEDataType_Trip, multiplicity=Multiplicity(1, 1)),
        Property(name="trips2", type=CoachBusWithEDataType_Passenger, multiplicity=Multiplicity(1, 9999))
    }
)
trips3: BinaryAssociation = BinaryAssociation(
    name="trips3",
    ends={
        Property(name="Trip", type=CoachBusWithEDataType_Coach, multiplicity=Multiplicity(1, 1)),
        Property(name="coaches", type=CoachBusWithEDataType_Trip, multiplicity=Multiplicity(1, 9999))
    }
)
coaches14: BinaryAssociation = BinaryAssociation(
    name="coaches14",
    ends={
        Property(name="Coach15", type=CoachBusWithEDataType_BookingOffice, multiplicity=Multiplicity(1, 1)),
        Property(name="offices", type=CoachBusWithEDataType_Coach, multiplicity=Multiplicity(1, 9999))
    }
)
manager16: BinaryAssociation = BinaryAssociation(
    name="manager16",
    ends={
        Property(name="Manager", type=CoachBusWithEDataType_BookingOffice, multiplicity=Multiplicity(1, 1)),
        Property(name="office", type=CoachBusWithEDataType_Manager, multiplicity=Multiplicity(0, 1))
    }
)
vms17: BinaryAssociation = BinaryAssociation(
    name="vms17",
    ends={
        Property(name="VendingMachine", type=CoachBusWithEDataType_BookingOffice, multiplicity=Multiplicity(1, 1)),
        Property(name="office18", type=CoachBusWithEDataType_VendingMachine, multiplicity=Multiplicity(0, 9999))
    }
)
psg19: BinaryAssociation = BinaryAssociation(
    name="psg19",
    ends={
        Property(name="Passenger20", type=CoachBusWithEDataType_Ticket, multiplicity=Multiplicity(1, 1)),
        Property(name="tickets", type=CoachBusWithEDataType_Passenger, multiplicity=Multiplicity(1, 1))
    }
)
coach10: BinaryAssociation = BinaryAssociation(
    name="coach10",
    ends={
        Property(name="Coach11", type=CoachBusWithEDataType_SecurityGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="guards", type=CoachBusWithEDataType_Coach, multiplicity=Multiplicity(1, 1))
    }
)
office12: BinaryAssociation = BinaryAssociation(
    name="office12",
    ends={
        Property(name="BookingOffice13", type=CoachBusWithEDataType_Manager, multiplicity=Multiplicity(1, 1)),
        Property(name="manager", type=CoachBusWithEDataType_BookingOffice, multiplicity=Multiplicity(0, 1))
    }
)
vm21: BinaryAssociation = BinaryAssociation(
    name="vm21",
    ends={
        Property(name="VendingMachine23", type=CoachBusWithEDataType_Ticket, multiplicity=Multiplicity(1, 1)),
        Property(name="tickets22", type=CoachBusWithEDataType_VendingMachine, multiplicity=Multiplicity(1, 1))
    }
)
tickets24: BinaryAssociation = BinaryAssociation(
    name="tickets24",
    ends={
        Property(name="Ticket25", type=CoachBusWithEDataType_VendingMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="vm", type=CoachBusWithEDataType_Ticket, multiplicity=Multiplicity(0, 9999))
    }
)
office26: BinaryAssociation = BinaryAssociation(
    name="office26",
    ends={
        Property(name="BookingOffice27", type=CoachBusWithEDataType_VendingMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="vms", type=CoachBusWithEDataType_BookingOffice, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_CoachBusWithEDataType_RegularTrip_Trip = Generalization(general=Trip, specific=CoachBusWithEDataType_RegularTrip)
gen_CoachBusWithEDataType_PrivateTrip_Trip = Generalization(general=Trip, specific=CoachBusWithEDataType_PrivateTrip)
gen_CoachBusWithEDataType_SecurityGuard_Employee = Generalization(general=Employee, specific=CoachBusWithEDataType_SecurityGuard)
gen_CoachBusWithEDataType_Manager_Employee = Generalization(general=Employee, specific=CoachBusWithEDataType_Manager)
gen_CoachBusWithEDataType_AdultTicket_Ticket = Generalization(general=Ticket, specific=CoachBusWithEDataType_AdultTicket)
gen_CoachBusWithEDataType_ChildTicket_Ticket = Generalization(general=Ticket, specific=CoachBusWithEDataType_ChildTicket)

# Domain Model
domain_model = DomainModel(
    name="CoachBusWithEDataType",
    types={CoachBusWithEDataType_SecurityGuard, CoachBusWithEDataType_BookingOffice, CoachBusWithEDataType_Ticket, CoachBusWithEDataType_Employee, CoachBusWithEDataType_Trip, CoachBusWithEDataType_Coach, CoachBusWithEDataType_Passenger, CoachBusWithEDataType_RegularTrip, Trip, CoachBusWithEDataType_PrivateTrip, CoachBusWithEDataType_VendingMachine, Employee, CoachBusWithEDataType_Manager, CoachBusWithEDataType_AdultTicket, Ticket, CoachBusWithEDataType_ChildTicket, Sex},
    associations={guards4, offices5, trips7, tickets9, coaches0, passengers1, trips3, coaches14, manager16, vms17, psg19, coach10, office12, vm21, tickets24, office26},
    generalizations={gen_CoachBusWithEDataType_RegularTrip_Trip, gen_CoachBusWithEDataType_PrivateTrip_Trip, gen_CoachBusWithEDataType_SecurityGuard_Employee, gen_CoachBusWithEDataType_Manager_Employee, gen_CoachBusWithEDataType_AdultTicket_Ticket, gen_CoachBusWithEDataType_ChildTicket_Ticket},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)