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
TravelState: Enumeration = Enumeration(
    name="TravelState",
    literals={
            EnumerationLiteral(name="unknown"),
			EnumerationLiteral(name="checkedIn"),
			EnumerationLiteral(name="luggageDroppedOf"),
			EnumerationLiteral(name="onBoard")
    }
)

FlightState: Enumeration = Enumeration(
    name="FlightState",
    literals={
            EnumerationLiteral(name="planned"),
			EnumerationLiteral(name="inFlight"),
			EnumerationLiteral(name="completed")
    }
)

# Classes
Flights_FlightModel = Class(name="Flights_FlightModel")
Flights_FlightContainer = Class(name="Flights_FlightContainer")
Flights_Bookings = Class(name="Flights_Bookings")
Flights_Persons = Class(name="Flights_Persons")
Flights_Routes = Class(name="Flights_Routes")
Flights_Airports = Class(name="Flights_Airports")
Flights_Planes = Class(name="Flights_Planes")
Flights_TimeStamp = Class(name="Flights_TimeStamp")
Flights_FlightObject = Class(name="Flights_FlightObject", is_abstract=True)
Flights_Person = Class(name="Flights_Person")
Flights_Flight = Class(name="Flights_Flight")
FlightObject = Class(name="FlightObject")
Flights_Travel = Class(name="Flights_Travel")
Flights_Route = Class(name="Flights_Route")
Flights_Gate = Class(name="Flights_Gate")
Flights_Plane = Class(name="Flights_Plane")
Flights_Booking = Class(name="Flights_Booking")
Flights_Airport = Class(name="Flights_Airport")

# Flights_FlightModel class attributes and methods

# Flights_FlightContainer class attributes and methods

# Flights_Bookings class attributes and methods

# Flights_Persons class attributes and methods

# Flights_Routes class attributes and methods

# Flights_Airports class attributes and methods

# Flights_Planes class attributes and methods

# Flights_TimeStamp class attributes and methods
Flights_TimeStamp_time: Property = Property(name="time", type=StringType)
Flights_TimeStamp.attributes={Flights_TimeStamp_time}

# Flights_FlightObject class attributes and methods
Flights_FlightObject_ID: Property = Property(name="ID", type=StringType)
Flights_FlightObject.attributes={Flights_FlightObject_ID}

# Flights_Person class attributes and methods
Flights_Person_travelState: Property = Property(name="travelState", type=StringType)
Flights_Person.attributes={Flights_Person_travelState}

# Flights_Flight class attributes and methods
Flights_Flight_newAttribute: Property = Property(name="newAttribute", type=StringType)
Flights_Flight.attributes={Flights_Flight_newAttribute}

# FlightObject class attributes and methods

# Flights_Travel class attributes and methods

# Flights_Route class attributes and methods
Flights_Route_duration: Property = Property(name="duration", type=IntegerType)
Flights_Route.attributes={Flights_Route_duration}

# Flights_Gate class attributes and methods
Flights_Gate_position: Property = Property(name="position", type=IntegerType)
Flights_Gate.attributes={Flights_Gate_position}

# Flights_Plane class attributes and methods
Flights_Plane_capacity: Property = Property(name="capacity", type=IntegerType)
Flights_Plane.attributes={Flights_Plane_capacity}

# Flights_Booking class attributes and methods

# Flights_Airport class attributes and methods
Flights_Airport_size: Property = Property(name="size", type=FloatType)
Flights_Airport.attributes={Flights_Airport_size}

# Relationships
flights0: BinaryAssociation = BinaryAssociation(
    name="flights0",
    ends={
        Property(name="Flights_FlightContainer", type=Flights_FlightModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Flights_FlightModel", type=Flights_FlightContainer, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bookings1: BinaryAssociation = BinaryAssociation(
    name="bookings1",
    ends={
        Property(name="Flights_Bookings", type=Flights_FlightModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Flights_FlightModel2", type=Flights_Bookings, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
persons3: BinaryAssociation = BinaryAssociation(
    name="persons3",
    ends={
        Property(name="Flights_Persons", type=Flights_FlightModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Flights_FlightModel4", type=Flights_Persons, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
routes5: BinaryAssociation = BinaryAssociation(
    name="routes5",
    ends={
        Property(name="Flights_Routes", type=Flights_FlightModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Flights_FlightModel6", type=Flights_Routes, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
airports7: BinaryAssociation = BinaryAssociation(
    name="airports7",
    ends={
        Property(name="Flights_Airports", type=Flights_FlightModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Flights_FlightModel8", type=Flights_Airports, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
planes9: BinaryAssociation = BinaryAssociation(
    name="planes9",
    ends={
        Property(name="Flights_Planes", type=Flights_FlightModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Flights_FlightModel10", type=Flights_Planes, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
globalTime11: BinaryAssociation = BinaryAssociation(
    name="globalTime11",
    ends={
        Property(name="Flights_TimeStamp", type=Flights_FlightModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Flights_FlightModel12", type=Flights_TimeStamp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
flights13: BinaryAssociation = BinaryAssociation(
    name="flights13",
    ends={
        Property(name="Flights_Flight", type=Flights_FlightContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="Flights_FlightContainer14", type=Flights_Flight, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
travels15: BinaryAssociation = BinaryAssociation(
    name="travels15",
    ends={
        Property(name="Travel", type=Flights_Flight, multiplicity=Multiplicity(1, 1)),
        Property(name="flights", type=Flights_Travel, multiplicity=Multiplicity(0, 9999))
    }
)
route16: BinaryAssociation = BinaryAssociation(
    name="route16",
    ends={
        Property(name="Route", type=Flights_Flight, multiplicity=Multiplicity(1, 1)),
        Property(name="flights17", type=Flights_Route, multiplicity=Multiplicity(1, 1))
    }
)
src18: BinaryAssociation = BinaryAssociation(
    name="src18",
    ends={
        Property(name="Gate", type=Flights_Flight, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingFlights", type=Flights_Gate, multiplicity=Multiplicity(1, 1))
    }
)
trg19: BinaryAssociation = BinaryAssociation(
    name="trg19",
    ends={
        Property(name="Gate20", type=Flights_Flight, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingFlights", type=Flights_Gate, multiplicity=Multiplicity(1, 1))
    }
)
plane21: BinaryAssociation = BinaryAssociation(
    name="plane21",
    ends={
        Property(name="Plane", type=Flights_Flight, multiplicity=Multiplicity(1, 1)),
        Property(name="flights22", type=Flights_Plane, multiplicity=Multiplicity(1, 1))
    }
)
departure23: BinaryAssociation = BinaryAssociation(
    name="departure23",
    ends={
        Property(name="Flights_TimeStamp25", type=Flights_Flight, multiplicity=Multiplicity(1, 1)),
        Property(name="Flights_Flight24", type=Flights_TimeStamp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arrival26: BinaryAssociation = BinaryAssociation(
    name="arrival26",
    ends={
        Property(name="Flights_TimeStamp28", type=Flights_Flight, multiplicity=Multiplicity(1, 1)),
        Property(name="Flights_Flight27", type=Flights_TimeStamp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bookings29: BinaryAssociation = BinaryAssociation(
    name="bookings29",
    ends={
        Property(name="Flights_Booking", type=Flights_Bookings, multiplicity=Multiplicity(1, 1)),
        Property(name="Flights_Bookings30", type=Flights_Booking, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
travels31: BinaryAssociation = BinaryAssociation(
    name="travels31",
    ends={
        Property(name="Flights_Travel", type=Flights_Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="Flights_Booking32", type=Flights_Travel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
routes33: BinaryAssociation = BinaryAssociation(
    name="routes33",
    ends={
        Property(name="Flights_Route", type=Flights_Routes, multiplicity=Multiplicity(1, 1)),
        Property(name="Flights_Routes34", type=Flights_Route, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flights35: BinaryAssociation = BinaryAssociation(
    name="flights35",
    ends={
        Property(name="Flight", type=Flights_Route, multiplicity=Multiplicity(1, 1)),
        Property(name="route", type=Flights_Flight, multiplicity=Multiplicity(0, 9999))
    }
)
src36: BinaryAssociation = BinaryAssociation(
    name="src36",
    ends={
        Property(name="Airport", type=Flights_Route, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingRoutes", type=Flights_Airport, multiplicity=Multiplicity(1, 1))
    }
)
trg37: BinaryAssociation = BinaryAssociation(
    name="trg37",
    ends={
        Property(name="Airport38", type=Flights_Route, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingRoutes", type=Flights_Airport, multiplicity=Multiplicity(1, 1))
    }
)
flights39: BinaryAssociation = BinaryAssociation(
    name="flights39",
    ends={
        Property(name="Flight40", type=Flights_Travel, multiplicity=Multiplicity(1, 1)),
        Property(name="travels", type=Flights_Flight, multiplicity=Multiplicity(0, 9999))
    }
)
person41: BinaryAssociation = BinaryAssociation(
    name="person41",
    ends={
        Property(name="Person", type=Flights_Travel, multiplicity=Multiplicity(1, 1)),
        Property(name="travels42", type=Flights_Person, multiplicity=Multiplicity(0, 1))
    }
)
persons43: BinaryAssociation = BinaryAssociation(
    name="persons43",
    ends={
        Property(name="Flights_Person", type=Flights_Persons, multiplicity=Multiplicity(1, 1)),
        Property(name="Flights_Persons44", type=Flights_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
travels45: BinaryAssociation = BinaryAssociation(
    name="travels45",
    ends={
        Property(name="Travel46", type=Flights_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="person", type=Flights_Travel, multiplicity=Multiplicity(0, 9999))
    }
)
airports47: BinaryAssociation = BinaryAssociation(
    name="airports47",
    ends={
        Property(name="Flights_Airport", type=Flights_Airports, multiplicity=Multiplicity(1, 1)),
        Property(name="Flights_Airports48", type=Flights_Airport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gates49: BinaryAssociation = BinaryAssociation(
    name="gates49",
    ends={
        Property(name="Flights_Gate", type=Flights_Airport, multiplicity=Multiplicity(1, 1)),
        Property(name="Flights_Airport50", type=Flights_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoingRoutes51: BinaryAssociation = BinaryAssociation(
    name="outgoingRoutes51",
    ends={
        Property(name="Route52", type=Flights_Airport, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=Flights_Route, multiplicity=Multiplicity(0, 9999))
    }
)
incomingRoutes53: BinaryAssociation = BinaryAssociation(
    name="incomingRoutes53",
    ends={
        Property(name="Route54", type=Flights_Airport, multiplicity=Multiplicity(1, 1)),
        Property(name="trg", type=Flights_Route, multiplicity=Multiplicity(0, 9999))
    }
)
planes55: BinaryAssociation = BinaryAssociation(
    name="planes55",
    ends={
        Property(name="Flights_Plane", type=Flights_Planes, multiplicity=Multiplicity(1, 1)),
        Property(name="Flights_Planes56", type=Flights_Plane, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flights57: BinaryAssociation = BinaryAssociation(
    name="flights57",
    ends={
        Property(name="Flight58", type=Flights_Plane, multiplicity=Multiplicity(1, 1)),
        Property(name="plane", type=Flights_Flight, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingFlights59: BinaryAssociation = BinaryAssociation(
    name="outgoingFlights59",
    ends={
        Property(name="Flight61", type=Flights_Gate, multiplicity=Multiplicity(1, 1)),
        Property(name="src60", type=Flights_Flight, multiplicity=Multiplicity(0, 9999))
    }
)
incomingFlights62: BinaryAssociation = BinaryAssociation(
    name="incomingFlights62",
    ends={
        Property(name="Flight64", type=Flights_Gate, multiplicity=Multiplicity(1, 1)),
        Property(name="trg63", type=Flights_Flight, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_Flights_Flight_FlightObject = Generalization(general=FlightObject, specific=Flights_Flight)
gen_Flights_Booking_FlightObject = Generalization(general=FlightObject, specific=Flights_Booking)
gen_Flights_Route_FlightObject = Generalization(general=FlightObject, specific=Flights_Route)
gen_Flights_Travel_FlightObject = Generalization(general=FlightObject, specific=Flights_Travel)
gen_Flights_Person_FlightObject = Generalization(general=FlightObject, specific=Flights_Person)
gen_Flights_Airport_FlightObject = Generalization(general=FlightObject, specific=Flights_Airport)
gen_Flights_Plane_FlightObject = Generalization(general=FlightObject, specific=Flights_Plane)
gen_Flights_Gate_FlightObject = Generalization(general=FlightObject, specific=Flights_Gate)

# Domain Model
domain_model = DomainModel(
    name="Flights",
    types={Flights_FlightModel, Flights_FlightContainer, Flights_Bookings, Flights_Persons, Flights_Routes, Flights_Airports, Flights_Planes, Flights_TimeStamp, Flights_FlightObject, Flights_Person, Flights_Flight, FlightObject, Flights_Travel, Flights_Route, Flights_Gate, Flights_Plane, Flights_Booking, Flights_Airport, TravelState, FlightState},
    associations={flights0, bookings1, persons3, routes5, airports7, planes9, globalTime11, flights13, travels15, route16, src18, trg19, plane21, departure23, arrival26, bookings29, travels31, routes33, flights35, src36, trg37, flights39, person41, persons43, travels45, airports47, gates49, outgoingRoutes51, incomingRoutes53, planes55, flights57, outgoingFlights59, incomingFlights62},
    generalizations={gen_Flights_Flight_FlightObject, gen_Flights_Booking_FlightObject, gen_Flights_Route_FlightObject, gen_Flights_Travel_FlightObject, gen_Flights_Person_FlightObject, gen_Flights_Airport_FlightObject, gen_Flights_Plane_FlightObject, gen_Flights_Gate_FlightObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)