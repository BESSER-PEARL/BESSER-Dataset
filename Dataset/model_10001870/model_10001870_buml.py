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
elevator_Elevator = Class(name="elevator_Elevator")
elevatortest_ElevatorTest = Class(name="elevatortest_ElevatorTest")
elevatortest_Person = Class(name="elevatortest_Person")
elevatortest_Patient = Class(name="elevatortest_Patient")
hw2_Building = Class(name="hw2_Building")
hw2_Elevator = Class(name="hw2_Elevator")
hw2_ElevatorFullException = Class(name="hw2_ElevatorFullException")
hw2_Floor = Class(name="hw2_Floor")
hw2test_HW2ElevatorSimulationTest = Class(name="hw2test_HW2ElevatorSimulationTest")
hw3_Building = Class(name="hw3_Building")
hw3_Elevator = Class(name="hw3_Elevator")
hw3_ElevatorFullException = Class(name="hw3_ElevatorFullException")
hw3_Floor = Class(name="hw3_Floor")
hw3_Passenger = Class(name="hw3_Passenger")
hw3test_HW3ElevatorSimulationTest = Class(name="hw3test_HW3ElevatorSimulationTest")
sec05_demoSec05 = Class(name="sec05_demoSec05")
sec05_Person = Class(name="sec05_Person")
sec05_Patient = Class(name="sec05_Patient")
genmymodelreverse_java_lang_Comparable_Interface = Class(name="genmymodelreverse_java_lang_Comparable_Interface", is_abstract=True)
genmymodelreverse_C1 = Class(name="genmymodelreverse_C1")
genmymodelreverse_java_lang_Exception = Class(name="genmymodelreverse_java_lang_Exception")
genmymodelreverse_java_lang_Object = Class(name="genmymodelreverse_java_lang_Object")
Comparable_Patient__Interface = Class(name="Comparable_Patient__Interface")

# elevator_Elevator class attributes and methods
elevator_Elevator_NUMBER_OF_FLOORS: Property = Property(name="NUMBER_OF_FLOORS", type=IntegerType)
elevator_Elevator_currentFloor: Property = Property(name="currentFloor", type=IntegerType)
elevator_Elevator_isGoingUp: Property = Property(name="isGoingUp", type=BooleanType)
elevator_Elevator_passengersToFloor: Property = Property(name="passengersToFloor", type=StringType)
elevator_Elevator_numOfPassengers: Property = Property(name="numOfPassengers", type=IntegerType)
elevator_Elevator.attributes={elevator_Elevator_currentFloor, elevator_Elevator_numOfPassengers, elevator_Elevator_isGoingUp, elevator_Elevator_passengersToFloor, elevator_Elevator_NUMBER_OF_FLOORS}

# elevatortest_ElevatorTest class attributes and methods

# elevatortest_Person class attributes and methods
elevatortest_Person_name: Property = Property(name="name", type=StringType)
elevatortest_Person.attributes={elevatortest_Person_name}

# elevatortest_Patient class attributes and methods
elevatortest_Patient_urgencyIndex: Property = Property(name="urgencyIndex", type=IntegerType)
elevatortest_Patient.attributes={elevatortest_Patient_urgencyIndex}

# hw2_Building class attributes and methods
hw2_Building_FLOORS: Property = Property(name="FLOORS", type=IntegerType)
hw2_Building_floors: Property = Property(name="floors", type=StringType)
hw2_Building.attributes={hw2_Building_floors, hw2_Building_FLOORS}

# hw2_Elevator class attributes and methods
hw2_Elevator_NUMBER_OF_FLOORS: Property = Property(name="NUMBER_OF_FLOORS", type=IntegerType)
hw2_Elevator_CAPACITY: Property = Property(name="CAPACITY", type=IntegerType)
hw2_Elevator_currentFloorIndex: Property = Property(name="currentFloorIndex", type=IntegerType)
hw2_Elevator_isGoingUp: Property = Property(name="isGoingUp", type=BooleanType)
hw2_Elevator_passengersToFloor: Property = Property(name="passengersToFloor", type=StringType)
hw2_Elevator_numOfPassengers: Property = Property(name="numOfPassengers", type=IntegerType)
hw2_Elevator.attributes={hw2_Elevator_passengersToFloor, hw2_Elevator_isGoingUp, hw2_Elevator_currentFloorIndex, hw2_Elevator_NUMBER_OF_FLOORS, hw2_Elevator_numOfPassengers, hw2_Elevator_CAPACITY}

# hw2_ElevatorFullException class attributes and methods

# hw2_Floor class attributes and methods
hw2_Floor_passengersWaiting: Property = Property(name="passengersWaiting", type=IntegerType)
hw2_Floor.attributes={hw2_Floor_passengersWaiting}

# hw2test_HW2ElevatorSimulationTest class attributes and methods

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
hw3_Elevator.attributes={hw3_Elevator_numOfPassengers, hw3_Elevator_passengersToFloor, hw3_Elevator_isGoingUp, hw3_Elevator_currentFloorIndex, hw3_Elevator_CAPACITY, hw3_Elevator_NUMBER_OF_FLOORS}

# hw3_ElevatorFullException class attributes and methods

# hw3_Floor class attributes and methods
hw3_Floor_passengersWaiting: Property = Property(name="passengersWaiting", type=IntegerType)
hw3_Floor_myFloorNumber: Property = Property(name="myFloorNumber", type=IntegerType)
hw3_Floor.attributes={hw3_Floor_passengersWaiting, hw3_Floor_myFloorNumber}

# hw3_Passenger class attributes and methods
hw3_Passenger_UNDEFINED_FLOOR: Property = Property(name="UNDEFINED_FLOOR", type=IntegerType)
hw3_Passenger_id: Property = Property(name="id", type=IntegerType)
hw3_Passenger_currentFloor: Property = Property(name="currentFloor", type=IntegerType)
hw3_Passenger_destinationFloor: Property = Property(name="destinationFloor", type=IntegerType)
hw3_Passenger.attributes={hw3_Passenger_UNDEFINED_FLOOR, hw3_Passenger_id, hw3_Passenger_destinationFloor, hw3_Passenger_currentFloor}

# hw3test_HW3ElevatorSimulationTest class attributes and methods

# sec05_demoSec05 class attributes and methods

# sec05_Person class attributes and methods
sec05_Person_name: Property = Property(name="name", type=StringType)
sec05_Person.attributes={sec05_Person_name}

# sec05_Patient class attributes and methods
sec05_Patient_urgencyIndex: Property = Property(name="urgencyIndex", type=IntegerType)
sec05_Patient.attributes={sec05_Patient_urgencyIndex}

# genmymodelreverse_java_lang_Comparable_Interface class attributes and methods

# genmymodelreverse_C1 class attributes and methods

# genmymodelreverse_java_lang_Exception class attributes and methods

# genmymodelreverse_java_lang_Object class attributes and methods

# Comparable_Patient__Interface class attributes and methods

# Relationships
building_Elevator_Building_8: BinaryAssociation = BinaryAssociation(
    name="building_Elevator_Building_8",
    ends={
        Property(name="elevator0", type=hw3_Elevator, multiplicity=Multiplicity(0, 1)),
        Property(name="building1", type=hw3_Building, multiplicity=Multiplicity(0, 1))
    }
)
residents_Floor_Passenger_3: BinaryAssociation = BinaryAssociation(
    name="residents_Floor_Passenger_3",
    ends={
        Property(name="floor2", type=hw3_Floor, multiplicity=Multiplicity(0, 1)),
        Property(name="residents3", type=hw3_Passenger, multiplicity=Multiplicity(0, 9999))
    }
)
elevator_Building_Elevator_6: BinaryAssociation = BinaryAssociation(
    name="elevator_Building_Elevator_6",
    ends={
        Property(name="building4", type=hw3_Building, multiplicity=Multiplicity(0, 1)),
        Property(name="elevator5", type=hw3_Elevator, multiplicity=Multiplicity(0, 1))
    }
)
downwardBound_Floor_Passenger_2: BinaryAssociation = BinaryAssociation(
    name="downwardBound_Floor_Passenger_2",
    ends={
        Property(name="floor6", type=hw3_Floor, multiplicity=Multiplicity(0, 1)),
        Property(name="downwardBound7", type=hw3_Passenger, multiplicity=Multiplicity(0, 9999))
    }
)
boardedPassengers_Elevator_Passenger_0: BinaryAssociation = BinaryAssociation(
    name="boardedPassengers_Elevator_Passenger_0",
    ends={
        Property(name="elevator8", type=hw3_Elevator, multiplicity=Multiplicity(0, 1)),
        Property(name="boardedPassengers9", type=hw3_Passenger, multiplicity=Multiplicity(0, 9999))
    }
)
person_Patient_Person_4: BinaryAssociation = BinaryAssociation(
    name="person_Patient_Person_4",
    ends={
        Property(name="patient10", type=elevatortest_Patient, multiplicity=Multiplicity(0, 1)),
        Property(name="person11", type=elevatortest_Person, multiplicity=Multiplicity(0, 1))
    }
)
building_Elevator_Building_1: BinaryAssociation = BinaryAssociation(
    name="building_Elevator_Building_1",
    ends={
        Property(name="elevator12", type=hw2_Elevator, multiplicity=Multiplicity(0, 1)),
        Property(name="building13", type=hw2_Building, multiplicity=Multiplicity(0, 1))
    }
)
elevator_Building_Elevator_7: BinaryAssociation = BinaryAssociation(
    name="elevator_Building_Elevator_7",
    ends={
        Property(name="building14", type=hw2_Building, multiplicity=Multiplicity(0, 1)),
        Property(name="elevator15", type=hw2_Elevator, multiplicity=Multiplicity(0, 1))
    }
)
person_Patient_Person_5: BinaryAssociation = BinaryAssociation(
    name="person_Patient_Person_5",
    ends={
        Property(name="patient16", type=sec05_Patient, multiplicity=Multiplicity(0, 1)),
        Property(name="person17", type=sec05_Person, multiplicity=Multiplicity(0, 1))
    }
)
upwardBound_Floor_Passenger_9: BinaryAssociation = BinaryAssociation(
    name="upwardBound_Floor_Passenger_9",
    ends={
        Property(name="floor18", type=hw3_Floor, multiplicity=Multiplicity(0, 1)),
        Property(name="upwardBound19", type=hw3_Passenger, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_al6A8Kg5EeeEQN1ZyOr__g",
    types={elevator_Elevator, elevatortest_ElevatorTest, elevatortest_Person, elevatortest_Patient, hw2_Building, hw2_Elevator, hw2_ElevatorFullException, hw2_Floor, hw2test_HW2ElevatorSimulationTest, hw3_Building, hw3_Elevator, hw3_ElevatorFullException, hw3_Floor, hw3_Passenger, hw3test_HW3ElevatorSimulationTest, sec05_demoSec05, sec05_Person, sec05_Patient, genmymodelreverse_java_lang_Comparable_Interface, genmymodelreverse_C1, genmymodelreverse_java_lang_Exception, genmymodelreverse_java_lang_Object, Comparable_Patient__Interface},
    associations={building_Elevator_Building_8, residents_Floor_Passenger_3, elevator_Building_Elevator_6, downwardBound_Floor_Passenger_2, boardedPassengers_Elevator_Passenger_0, person_Patient_Person_4, building_Elevator_Building_1, elevator_Building_Elevator_7, person_Patient_Person_5, upwardBound_Floor_Passenger_9},
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