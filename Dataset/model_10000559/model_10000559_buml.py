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
hw3_Building = Class(name="hw3_Building")
hw3_Elevator = Class(name="hw3_Elevator")
hw3_ElevatorFullException = Class(name="hw3_ElevatorFullException")
hw3_Floor = Class(name="hw3_Floor")
hw3_Passenger = Class(name="hw3_Passenger")
genmymodelreverse_java_lang_Exception = Class(name="genmymodelreverse_java_lang_Exception")

# hw3_Building class attributes and methods
hw3_Building_FLOORS: Property = Property(name="FLOORS", type=IntegerType)
hw3_Building_floors: Property = Property(name="floors", type=StringType)
hw3_Building.attributes={hw3_Building_FLOORS, hw3_Building_floors}

# hw3_Elevator class attributes and methods
hw3_Elevator_NUMBER_OF_FLOORS: Property = Property(name="NUMBER_OF_FLOORS", type=IntegerType)
hw3_Elevator_CAPACITY: Property = Property(name="CAPACITY", type=IntegerType)
hw3_Elevator_currentFloorIndex: Property = Property(name="currentFloorIndex", type=IntegerType)
hw3_Elevator_isGoingUp: Property = Property(name="isGoingUp", type=BooleanType)
hw3_Elevator_passengersToFloor: Property = Property(name="passengersToFloor", type=StringType)
hw3_Elevator_numOfPassengers: Property = Property(name="numOfPassengers", type=IntegerType)
hw3_Elevator.attributes={hw3_Elevator_isGoingUp, hw3_Elevator_numOfPassengers, hw3_Elevator_passengersToFloor, hw3_Elevator_CAPACITY, hw3_Elevator_currentFloorIndex, hw3_Elevator_NUMBER_OF_FLOORS}

# hw3_ElevatorFullException class attributes and methods

# hw3_Floor class attributes and methods
hw3_Floor_passengersWaiting: Property = Property(name="passengersWaiting", type=IntegerType)
hw3_Floor_myFloorNumber: Property = Property(name="myFloorNumber", type=IntegerType)
hw3_Floor.attributes={hw3_Floor_myFloorNumber, hw3_Floor_passengersWaiting}

# hw3_Passenger class attributes and methods
hw3_Passenger_UNDEFINED_FLOOR: Property = Property(name="UNDEFINED_FLOOR", type=IntegerType)
hw3_Passenger_id: Property = Property(name="id", type=IntegerType)
hw3_Passenger_currentFloor: Property = Property(name="currentFloor", type=IntegerType)
hw3_Passenger_destinationFloor: Property = Property(name="destinationFloor", type=IntegerType)
hw3_Passenger.attributes={hw3_Passenger_UNDEFINED_FLOOR, hw3_Passenger_destinationFloor, hw3_Passenger_id, hw3_Passenger_currentFloor}

# genmymodelreverse_java_lang_Exception class attributes and methods

# Relationships
upwardBound_Floor_Passenger_0: BinaryAssociation = BinaryAssociation(
    name="upwardBound_Floor_Passenger_0",
    ends={
        Property(name="floor0", type=hw3_Floor, multiplicity=Multiplicity(0, 1)),
        Property(name="upwardBound1", type=hw3_Passenger, multiplicity=Multiplicity(0, 9999))
    }
)
boardedPassengers_Elevator_Passenger_3: BinaryAssociation = BinaryAssociation(
    name="boardedPassengers_Elevator_Passenger_3",
    ends={
        Property(name="elevator2", type=hw3_Elevator, multiplicity=Multiplicity(0, 1)),
        Property(name="boardedPassengers3", type=hw3_Passenger, multiplicity=Multiplicity(0, 9999))
    }
)
elevator_Building_Elevator_5: BinaryAssociation = BinaryAssociation(
    name="elevator_Building_Elevator_5",
    ends={
        Property(name="building4", type=hw3_Building, multiplicity=Multiplicity(0, 1)),
        Property(name="elevator5", type=hw3_Elevator, multiplicity=Multiplicity(0, 1))
    }
)
building_Elevator_Building_1: BinaryAssociation = BinaryAssociation(
    name="building_Elevator_Building_1",
    ends={
        Property(name="elevator6", type=hw3_Elevator, multiplicity=Multiplicity(0, 1)),
        Property(name="building7", type=hw3_Building, multiplicity=Multiplicity(0, 1))
    }
)
residents_Floor_Passenger_2: BinaryAssociation = BinaryAssociation(
    name="residents_Floor_Passenger_2",
    ends={
        Property(name="floor8", type=hw3_Floor, multiplicity=Multiplicity(0, 1)),
        Property(name="residents9", type=hw3_Passenger, multiplicity=Multiplicity(0, 9999))
    }
)
downwardBound_Floor_Passenger_4: BinaryAssociation = BinaryAssociation(
    name="downwardBound_Floor_Passenger_4",
    ends={
        Property(name="floor10", type=hw3_Floor, multiplicity=Multiplicity(0, 1)),
        Property(name="downwardBound11", type=hw3_Passenger, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_44f6c380_298e_4f27_a227_f61f700e174a",
    types={hw3_Building, hw3_Elevator, hw3_ElevatorFullException, hw3_Floor, hw3_Passenger, genmymodelreverse_java_lang_Exception},
    associations={upwardBound_Floor_Passenger_0, boardedPassengers_Elevator_Passenger_3, elevator_Building_Elevator_5, building_Elevator_Building_1, residents_Floor_Passenger_2, downwardBound_Floor_Passenger_4},
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