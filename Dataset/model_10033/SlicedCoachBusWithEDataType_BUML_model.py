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
CoachBusWithEDataType_Coach = Class(name="CoachBusWithEDataType_Coach")
CoachBusWithEDataType_ChildTicket = Class(name="CoachBusWithEDataType_ChildTicket")
Ticket = Class(name="Ticket")
CoachBusWithEDataType_Trip = Class(name="CoachBusWithEDataType_Trip")
CoachBusWithEDataType_RegularTrip = Class(name="CoachBusWithEDataType_RegularTrip")
Trip = Class(name="Trip")
CoachBusWithEDataType_Ticket = Class(name="CoachBusWithEDataType_Ticket")
CoachBusWithEDataType_PrivateTrip = Class(name="CoachBusWithEDataType_PrivateTrip")
CoachBusWithEDataType_Passenger = Class(name="CoachBusWithEDataType_Passenger")
CoachBusWithEDataType_AdultTicket = Class(name="CoachBusWithEDataType_AdultTicket")

# CoachBusWithEDataType_Coach class attributes and methods
CoachBusWithEDataType_Coach_noOfSeats: Property = Property(name="noOfSeats", type=IntegerType)
CoachBusWithEDataType_Coach.attributes={CoachBusWithEDataType_Coach_noOfSeats}

# CoachBusWithEDataType_ChildTicket class attributes and methods

# Ticket class attributes and methods

# CoachBusWithEDataType_Trip class attributes and methods
CoachBusWithEDataType_Trip_type: Property = Property(name="type", type=StringType)
CoachBusWithEDataType_Trip.attributes={CoachBusWithEDataType_Trip_type}

# CoachBusWithEDataType_RegularTrip class attributes and methods

# Trip class attributes and methods

# CoachBusWithEDataType_Ticket class attributes and methods
CoachBusWithEDataType_Ticket_number: Property = Property(name="number", type=IntegerType)
CoachBusWithEDataType_Ticket.attributes={CoachBusWithEDataType_Ticket_number}

# CoachBusWithEDataType_PrivateTrip class attributes and methods

# CoachBusWithEDataType_Passenger class attributes and methods
CoachBusWithEDataType_Passenger_age: Property = Property(name="age", type=IntegerType)
CoachBusWithEDataType_Passenger_sex: Property = Property(name="sex", type=StringType)
CoachBusWithEDataType_Passenger.attributes={CoachBusWithEDataType_Passenger_age, CoachBusWithEDataType_Passenger_sex}

# CoachBusWithEDataType_AdultTicket class attributes and methods

# Relationships
trips0: BinaryAssociation = BinaryAssociation(
    name="trips0",
    ends={
        Property(name="CoachBusWithEDataType_Trip", type=CoachBusWithEDataType_Coach, multiplicity=Multiplicity(1, 1)),
        Property(name="CoachBusWithEDataType_Coach", type=CoachBusWithEDataType_Trip, multiplicity=Multiplicity(1, 9999))
    }
)
passengers1: BinaryAssociation = BinaryAssociation(
    name="passengers1",
    ends={
        Property(name="CoachBusWithEDataType_Passenger", type=CoachBusWithEDataType_Trip, multiplicity=Multiplicity(1, 1)),
        Property(name="CoachBusWithEDataType_Trip2", type=CoachBusWithEDataType_Passenger, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_CoachBusWithEDataType_ChildTicket_Ticket = Generalization(general=Ticket, specific=CoachBusWithEDataType_ChildTicket)
gen_CoachBusWithEDataType_RegularTrip_Trip = Generalization(general=Trip, specific=CoachBusWithEDataType_RegularTrip)
gen_CoachBusWithEDataType_PrivateTrip_Trip = Generalization(general=Trip, specific=CoachBusWithEDataType_PrivateTrip)
gen_CoachBusWithEDataType_AdultTicket_Ticket = Generalization(general=Ticket, specific=CoachBusWithEDataType_AdultTicket)


# OCL Constraints
MaleOrFemale: Constraint = Constraint(
    name="MaleOrFemale",
    context=CoachBusWithEDataType_Passenger,
    expression="context Passenger inv: self.sex =(CoachBusWithEDataType_Sex_male) =(self.sex =(CoachBusWithEDataType_Sex_female))",
    language="OCL"
)
TripType: Constraint = Constraint(
    name="TripType",
    context=CoachBusWithEDataType_Trip,
    expression="context Trip inv: self.type.oclIsKindOf(CoachBusWithEDataType_TType)",
    language="OCL"
)
MinCoachSize: Constraint = Constraint(
    name="MinCoachSize",
    context=CoachBusWithEDataType_Coach,
    expression="context Coach inv: self.noOfSeats >=(10)",
    language="OCL"
)
UniqueTicketNumber: Constraint = Constraint(
    name="UniqueTicketNumber",
    context=CoachBusWithEDataType_Ticket,
    expression="context Ticket inv: CoachBusWithEDataType_Ticket.allInstances()->isUnique(t : Ticket | t.number)",
    language="OCL"
)
MaxCoachSize: Constraint = Constraint(
    name="MaxCoachSize",
    context=CoachBusWithEDataType_Coach,
    expression="context Coach inv: self.trips->forAll(t : Trip | t.passengers->size() <=(self.noOfSeats))",
    language="OCL"
)
NonNegativeAge: Constraint = Constraint(
    name="NonNegativeAge",
    context=CoachBusWithEDataType_Passenger,
    expression="context Passenger inv: self.age >=(0)",
    language="OCL"
)

# Domain Model
domain_model = DomainModel(
    name="CoachBusWithEDataType",
    types={CoachBusWithEDataType_Coach, CoachBusWithEDataType_ChildTicket, Ticket, CoachBusWithEDataType_Trip, CoachBusWithEDataType_RegularTrip, Trip, CoachBusWithEDataType_Ticket, CoachBusWithEDataType_PrivateTrip, CoachBusWithEDataType_Passenger, CoachBusWithEDataType_AdultTicket, Sex},
    associations={trips0, passengers1},
    constraints={MaleOrFemale, TripType, MinCoachSize, UniqueTicketNumber, MaxCoachSize, NonNegativeAge},
    generalizations={gen_CoachBusWithEDataType_ChildTicket_Ticket, gen_CoachBusWithEDataType_RegularTrip_Trip, gen_CoachBusWithEDataType_PrivateTrip_Trip, gen_CoachBusWithEDataType_AdultTicket_Ticket},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)