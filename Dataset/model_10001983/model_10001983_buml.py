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
Car = Class(name="Car")
Floor = Class(name="Floor")
Call = Class(name="Call")
Controller = Class(name="Controller")
FloorCallBox = Class(name="FloorCallBox")
array_enum_ = Class(name="array_enum_")
BackgroundStopLoader = Class(name="BackgroundStopLoader")
BackgroundCallListener = Class(name="BackgroundCallListener")
Sim = Class(name="Sim")
CarCallBox = Class(name="CarCallBox")
Passenger = Class(name="Passenger")
Test_Report = Class(name="Test_Report")

# Car class attributes and methods
Car_WEIGHT_LIMIT: Property = Property(name="WEIGHT_LIMIT", type=IntegerType)
Car_destination: Property = Property(name="destination", type=Floor)
Car_direction: Property = Property(name="direction", type=StringType)
Car_floorNum: Property = Property(name="floorNum", type=IntegerType)
Car_location: Property = Property(name="location", type=IntegerType)
Car_stopQueue: Property = Property(name="stopQueue", type=StringType)
Car_destQueue: Property = Property(name="destQueue", type=StringType)
Car_weightLoad: Property = Property(name="weightLoad", type=IntegerType)
Car_box: Property = Property(name="box", type=CarCallBox)
Car_stopLoader: Property = Property(name="stopLoader", type=BackgroundStopLoader)
Car.attributes={Car_direction, Car_WEIGHT_LIMIT, Car_stopLoader, Car_location, Car_box, Car_destQueue, Car_floorNum, Car_stopQueue, Car_destination, Car_weightLoad}

# Floor class attributes and methods
Floor_BOTTOM: Property = Property(name="BOTTOM", type=IntegerType)
Floor_TOP: Property = Property(name="TOP", type=IntegerType)
Floor_number: Property = Property(name="number", type=IntegerType)
Floor_LOCATION: Property = Property(name="LOCATION", type=IntegerType)
Floor_box: Property = Property(name="box", type=FloorCallBox)
Floor.attributes={Floor_number, Floor_LOCATION, Floor_box, Floor_TOP, Floor_BOTTOM}

# Call class attributes and methods
Call_location: Property = Property(name="location", type=Floor)
Call_created: Property = Property(name="created", type=StringType)
Call_direction: Property = Property(name="direction", type=StringType)
Call.attributes={Call_direction, Call_created, Call_location}

# Controller class attributes and methods
Controller_callQueue: Property = Property(name="callQueue", type=StringType)
Controller_cars: Property = Property(name="cars", type=StringType)
Controller_floors: Property = Property(name="floors", type=StringType)
Controller_callAdmin: Property = Property(name="callAdmin", type=BackgroundCallListener)
Controller.attributes={Controller_cars, Controller_floors, Controller_callAdmin, Controller_callQueue}

# FloorCallBox class attributes and methods
FloorCallBox_LOCATION: Property = Property(name="LOCATION", type=IntegerType)
FloorCallBox_BUTTONS: Property = Property(name="BUTTONS", type=array_enum_)
FloorCallBox.attributes={FloorCallBox_BUTTONS, FloorCallBox_LOCATION}

# array_enum_ class attributes and methods

# BackgroundStopLoader class attributes and methods
BackgroundStopLoader_stops: Property = Property(name="stops", type=StringType)
BackgroundStopLoader.attributes={BackgroundStopLoader_stops}

# BackgroundCallListener class attributes and methods

# Sim class attributes and methods
Sim_elevator: Property = Property(name="elevator", type=Controller)
Sim_people: Property = Property(name="people", type=StringType)
Sim.attributes={Sim_elevator, Sim_people}

# CarCallBox class attributes and methods
CarCallBox_buttons: Property = Property(name="buttons", type=StringType)
CarCallBox.attributes={CarCallBox_buttons}

# Passenger class attributes and methods
Passenger_WEIGHT: Property = Property(name="WEIGHT", type=IntegerType)
Passenger_START_FLOOR: Property = Property(name="START_FLOOR", type=IntegerType)
Passenger_DEST: Property = Property(name="DEST", type=IntegerType)
Passenger_carNum: Property = Property(name="carNum", type=IntegerType)
Passenger_waiting: Property = Property(name="waiting", type=BooleanType)
Passenger_traveling: Property = Property(name="traveling", type=BooleanType)
Passenger_readyToDie: Property = Property(name="readyToDie", type=BooleanType)
Passenger.attributes={Passenger_carNum, Passenger_START_FLOOR, Passenger_readyToDie, Passenger_traveling, Passenger_DEST, Passenger_WEIGHT, Passenger_waiting}

# Test_Report class attributes and methods

# Relationships
Car_Call: BinaryAssociation = BinaryAssociation(
    name="Car_Call",
    ends={
        Property(name="call10", type=Call, multiplicity=Multiplicity(0, 9999)),
        Property(name="car11", type=Car, multiplicity=Multiplicity(0, 1))
    }
)
Director_Car: BinaryAssociation = BinaryAssociation(
    name="Director_Car",
    ends={
        Property(name="car12", type=Car, multiplicity=Multiplicity(0, 9999)),
        Property(name="director13", type=Controller, multiplicity=Multiplicity(0, 1))
    }
)
Sim_Director: BinaryAssociation = BinaryAssociation(
    name="Sim_Director",
    ends={
        Property(name="director14", type=Controller, multiplicity=Multiplicity(1, 1)),
        Property(name="sim15", type=Sim, multiplicity=Multiplicity(1, 1))
    }
)
Sim_Passenger: BinaryAssociation = BinaryAssociation(
    name="Sim_Passenger",
    ends={
        Property(name="passenger16", type=Passenger, multiplicity=Multiplicity(0, 9999)),
        Property(name="sim17", type=Sim, multiplicity=Multiplicity(1, 1))
    }
)
Director_Floor: BinaryAssociation = BinaryAssociation(
    name="Director_Floor",
    ends={
        Property(name="floor18", type=Floor, multiplicity=Multiplicity(1, 9999)),
        Property(name="director19", type=Controller, multiplicity=Multiplicity(1, 1))
    }
)
Car_BackgroundStopLoader: BinaryAssociation = BinaryAssociation(
    name="Car_BackgroundStopLoader",
    ends={
        Property(name="backgroundStopLoader0", type=BackgroundStopLoader, multiplicity=Multiplicity(1, 1)),
        Property(name="car1", type=Car, multiplicity=Multiplicity(0, 1))
    }
)
Car_CarCallBox: BinaryAssociation = BinaryAssociation(
    name="Car_CarCallBox",
    ends={
        Property(name="carCallBox2", type=CarCallBox, multiplicity=Multiplicity(1, 1)),
        Property(name="car3", type=Car, multiplicity=Multiplicity(0, 1))
    }
)
Director_BackgroundCallListener: BinaryAssociation = BinaryAssociation(
    name="Director_BackgroundCallListener",
    ends={
        Property(name="backgroundCallListener4", type=BackgroundCallListener, multiplicity=Multiplicity(1, 1)),
        Property(name="director5", type=Controller, multiplicity=Multiplicity(0, 1))
    }
)
Director_Call: BinaryAssociation = BinaryAssociation(
    name="Director_Call",
    ends={
        Property(name="call6", type=Call, multiplicity=Multiplicity(0, 9999)),
        Property(name="director7", type=Controller, multiplicity=Multiplicity(0, 1))
    }
)
Floor_FloorCallBox: BinaryAssociation = BinaryAssociation(
    name="Floor_FloorCallBox",
    ends={
        Property(name="floorCallBox8", type=FloorCallBox, multiplicity=Multiplicity(1, 1)),
        Property(name="floor9", type=Floor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_hjO7kAYUEeipbtix_oa2Dg",
    types={Car, Floor, Call, Controller, FloorCallBox, array_enum_, BackgroundStopLoader, BackgroundCallListener, Sim, CarCallBox, Passenger, Test_Report},
    associations={Car_Call, Director_Car, Sim_Director, Sim_Passenger, Director_Floor, Car_BackgroundStopLoader, Car_CarCallBox, Director_BackgroundCallListener, Director_Call, Floor_FloorCallBox},
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