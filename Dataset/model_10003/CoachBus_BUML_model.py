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
CoachBus_Trip = Class(name="CoachBus_Trip")
CoachBus_PrivateTrip = Class(name="CoachBus_PrivateTrip")
CoachBus_SecurityGuard = Class(name="CoachBus_SecurityGuard")
CoachBus_BookingOffice = Class(name="CoachBus_BookingOffice")
CoachBus_Ticket = Class(name="CoachBus_Ticket")
CoachBus_Employee = Class(name="CoachBus_Employee")
CoachBus_Coach = Class(name="CoachBus_Coach")
CoachBus_Passenger = Class(name="CoachBus_Passenger")
CoachBus_RegularTrip = Class(name="CoachBus_RegularTrip")
Trip = Class(name="Trip")
CoachBus_VendingMachine = Class(name="CoachBus_VendingMachine")
CoachBus_AdultTicket = Class(name="CoachBus_AdultTicket")
Ticket = Class(name="Ticket")
CoachBus_ChildTicket = Class(name="CoachBus_ChildTicket")
Employee = Class(name="Employee")
CoachBus_Manager = Class(name="CoachBus_Manager")

# CoachBus_Trip class attributes and methods
CoachBus_Trip_name: Property = Property(name="name", type=StringType)
CoachBus_Trip_origin: Property = Property(name="origin", type=StringType)
CoachBus_Trip_destination: Property = Property(name="destination", type=StringType)
CoachBus_Trip_type: Property = Property(name="type", type=StringType)
CoachBus_Trip_number: Property = Property(name="number", type=IntegerType)
CoachBus_Trip.attributes={CoachBus_Trip_origin, CoachBus_Trip_destination, CoachBus_Trip_number, CoachBus_Trip_name, CoachBus_Trip_type}

# CoachBus_PrivateTrip class attributes and methods
CoachBus_PrivateTrip_extras: Property = Property(name="extras", type=StringType)
CoachBus_PrivateTrip.attributes={CoachBus_PrivateTrip_extras}

# CoachBus_SecurityGuard class attributes and methods
CoachBus_SecurityGuard_shift: Property = Property(name="shift", type=StringType)
CoachBus_SecurityGuard.attributes={CoachBus_SecurityGuard_shift}

# CoachBus_BookingOffice class attributes and methods
CoachBus_BookingOffice_officeID: Property = Property(name="officeID", type=IntegerType)
CoachBus_BookingOffice_name: Property = Property(name="name", type=StringType)
CoachBus_BookingOffice_location: Property = Property(name="location", type=StringType)
CoachBus_BookingOffice.attributes={CoachBus_BookingOffice_officeID, CoachBus_BookingOffice_name, CoachBus_BookingOffice_location}

# CoachBus_Ticket class attributes and methods
CoachBus_Ticket_number: Property = Property(name="number", type=IntegerType)
CoachBus_Ticket_price: Property = Property(name="price", type=FloatType)
CoachBus_Ticket_isRoundTrip: Property = Property(name="isRoundTrip", type=BooleanType)
CoachBus_Ticket.attributes={CoachBus_Ticket_number, CoachBus_Ticket_price, CoachBus_Ticket_isRoundTrip}

# CoachBus_Employee class attributes and methods
CoachBus_Employee_id: Property = Property(name="id", type=IntegerType)
CoachBus_Employee_baseSalary: Property = Property(name="baseSalary", type=FloatType)
CoachBus_Employee.attributes={CoachBus_Employee_id, CoachBus_Employee_baseSalary}

# CoachBus_Coach class attributes and methods
CoachBus_Coach_id: Property = Property(name="id", type=IntegerType)
CoachBus_Coach_name: Property = Property(name="name", type=StringType)
CoachBus_Coach_model: Property = Property(name="model", type=StringType)
CoachBus_Coach_noOfSeats: Property = Property(name="noOfSeats", type=IntegerType)
CoachBus_Coach.attributes={CoachBus_Coach_name, CoachBus_Coach_noOfSeats, CoachBus_Coach_model, CoachBus_Coach_id}

# CoachBus_Passenger class attributes and methods
CoachBus_Passenger_name: Property = Property(name="name", type=StringType)
CoachBus_Passenger_age: Property = Property(name="age", type=IntegerType)
CoachBus_Passenger_idCard: Property = Property(name="idCard", type=StringType)
CoachBus_Passenger.attributes={CoachBus_Passenger_age, CoachBus_Passenger_idCard, CoachBus_Passenger_name}

# CoachBus_RegularTrip class attributes and methods

# Trip class attributes and methods

# CoachBus_VendingMachine class attributes and methods
CoachBus_VendingMachine_number: Property = Property(name="number", type=IntegerType)
CoachBus_VendingMachine.attributes={CoachBus_VendingMachine_number}

# CoachBus_AdultTicket class attributes and methods
CoachBus_AdultTicket_isElderlyDiscount: Property = Property(name="isElderlyDiscount", type=BooleanType)
CoachBus_AdultTicket.attributes={CoachBus_AdultTicket_isElderlyDiscount}

# Ticket class attributes and methods

# CoachBus_ChildTicket class attributes and methods
CoachBus_ChildTicket_isSchoolTrip: Property = Property(name="isSchoolTrip", type=BooleanType)
CoachBus_ChildTicket.attributes={CoachBus_ChildTicket_isSchoolTrip}

# Employee class attributes and methods

# CoachBus_Manager class attributes and methods
CoachBus_Manager_hasMBA: Property = Property(name="hasMBA", type=BooleanType)
CoachBus_Manager.attributes={CoachBus_Manager_hasMBA}

# Relationships
trips3: BinaryAssociation = BinaryAssociation(
    name="trips3",
    ends={
        Property(name="Trip", type=CoachBus_Coach, multiplicity=Multiplicity(1, 1)),
        Property(name="coaches", type=CoachBus_Trip, multiplicity=Multiplicity(1, 9999))
    }
)
guards4: BinaryAssociation = BinaryAssociation(
    name="guards4",
    ends={
        Property(name="SecurityGuard", type=CoachBus_Coach, multiplicity=Multiplicity(1, 1)),
        Property(name="coach", type=CoachBus_SecurityGuard, multiplicity=Multiplicity(0, 9999))
    }
)
offices5: BinaryAssociation = BinaryAssociation(
    name="offices5",
    ends={
        Property(name="BookingOffice", type=CoachBus_Coach, multiplicity=Multiplicity(1, 1)),
        Property(name="coaches6", type=CoachBus_BookingOffice, multiplicity=Multiplicity(0, 9999))
    }
)
trips7: BinaryAssociation = BinaryAssociation(
    name="trips7",
    ends={
        Property(name="Trip8", type=CoachBus_Passenger, multiplicity=Multiplicity(1, 1)),
        Property(name="passengers", type=CoachBus_Trip, multiplicity=Multiplicity(1, 9999))
    }
)
tickets9: BinaryAssociation = BinaryAssociation(
    name="tickets9",
    ends={
        Property(name="Ticket", type=CoachBus_Passenger, multiplicity=Multiplicity(1, 1)),
        Property(name="psg", type=CoachBus_Ticket, multiplicity=Multiplicity(0, 9999))
    }
)
coaches0: BinaryAssociation = BinaryAssociation(
    name="coaches0",
    ends={
        Property(name="Coach", type=CoachBus_Trip, multiplicity=Multiplicity(1, 1)),
        Property(name="trips", type=CoachBus_Coach, multiplicity=Multiplicity(1, 9999))
    }
)
passengers1: BinaryAssociation = BinaryAssociation(
    name="passengers1",
    ends={
        Property(name="Passenger", type=CoachBus_Trip, multiplicity=Multiplicity(1, 1)),
        Property(name="trips2", type=CoachBus_Passenger, multiplicity=Multiplicity(1, 9999))
    }
)
coaches14: BinaryAssociation = BinaryAssociation(
    name="coaches14",
    ends={
        Property(name="Coach15", type=CoachBus_BookingOffice, multiplicity=Multiplicity(1, 1)),
        Property(name="offices", type=CoachBus_Coach, multiplicity=Multiplicity(1, 9999))
    }
)
manager16: BinaryAssociation = BinaryAssociation(
    name="manager16",
    ends={
        Property(name="Manager", type=CoachBus_BookingOffice, multiplicity=Multiplicity(1, 1)),
        Property(name="office", type=CoachBus_Manager, multiplicity=Multiplicity(0, 1))
    }
)
vms17: BinaryAssociation = BinaryAssociation(
    name="vms17",
    ends={
        Property(name="VendingMachine", type=CoachBus_BookingOffice, multiplicity=Multiplicity(1, 1)),
        Property(name="office18", type=CoachBus_VendingMachine, multiplicity=Multiplicity(0, 9999))
    }
)
psg19: BinaryAssociation = BinaryAssociation(
    name="psg19",
    ends={
        Property(name="Passenger20", type=CoachBus_Ticket, multiplicity=Multiplicity(1, 1)),
        Property(name="tickets", type=CoachBus_Passenger, multiplicity=Multiplicity(1, 1))
    }
)
vm21: BinaryAssociation = BinaryAssociation(
    name="vm21",
    ends={
        Property(name="VendingMachine23", type=CoachBus_Ticket, multiplicity=Multiplicity(1, 1)),
        Property(name="tickets22", type=CoachBus_VendingMachine, multiplicity=Multiplicity(1, 1))
    }
)
tickets24: BinaryAssociation = BinaryAssociation(
    name="tickets24",
    ends={
        Property(name="Ticket25", type=CoachBus_VendingMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="vm", type=CoachBus_Ticket, multiplicity=Multiplicity(0, 9999))
    }
)
office26: BinaryAssociation = BinaryAssociation(
    name="office26",
    ends={
        Property(name="BookingOffice27", type=CoachBus_VendingMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="vms", type=CoachBus_BookingOffice, multiplicity=Multiplicity(1, 1))
    }
)
coach10: BinaryAssociation = BinaryAssociation(
    name="coach10",
    ends={
        Property(name="Coach11", type=CoachBus_SecurityGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="guards", type=CoachBus_Coach, multiplicity=Multiplicity(1, 1))
    }
)
office12: BinaryAssociation = BinaryAssociation(
    name="office12",
    ends={
        Property(name="BookingOffice13", type=CoachBus_Manager, multiplicity=Multiplicity(1, 1)),
        Property(name="manager", type=CoachBus_BookingOffice, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_CoachBus_PrivateTrip_Trip = Generalization(general=Trip, specific=CoachBus_PrivateTrip)
gen_CoachBus_RegularTrip_Trip = Generalization(general=Trip, specific=CoachBus_RegularTrip)
gen_CoachBus_AdultTicket_Ticket = Generalization(general=Ticket, specific=CoachBus_AdultTicket)
gen_CoachBus_ChildTicket_Ticket = Generalization(general=Ticket, specific=CoachBus_ChildTicket)
gen_CoachBus_SecurityGuard_Employee = Generalization(general=Employee, specific=CoachBus_SecurityGuard)
gen_CoachBus_Manager_Employee = Generalization(general=Employee, specific=CoachBus_Manager)

# Domain Model
domain_model = DomainModel(
    name="CoachBus",
    types={CoachBus_Trip, CoachBus_PrivateTrip, CoachBus_SecurityGuard, CoachBus_BookingOffice, CoachBus_Ticket, CoachBus_Employee, CoachBus_Coach, CoachBus_Passenger, CoachBus_RegularTrip, Trip, CoachBus_VendingMachine, CoachBus_AdultTicket, Ticket, CoachBus_ChildTicket, Employee, CoachBus_Manager},
    associations={trips3, guards4, offices5, trips7, tickets9, coaches0, passengers1, coaches14, manager16, vms17, psg19, vm21, tickets24, office26, coach10, office12},
    generalizations={gen_CoachBus_PrivateTrip_Trip, gen_CoachBus_RegularTrip_Trip, gen_CoachBus_AdultTicket_Ticket, gen_CoachBus_ChildTicket_Ticket, gen_CoachBus_SecurityGuard_Employee, gen_CoachBus_Manager_Employee},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)