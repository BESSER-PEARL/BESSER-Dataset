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
Direction: Enumeration = Enumeration(
    name="Direction",
    literals={
            
    }
)

# Classes
object = Class(name="object")
Button = Class(name="Button", is_abstract=True)
FloorButton = Class(name="FloorButton")
UpDownButton = Class(name="UpDownButton")
ElevatorBay = Class(name="ElevatorBay")
Controller = Class(name="Controller")
Building = Class(name="Building")
Elevator = Class(name="Elevator")
Algorithm = Class(name="Algorithm", is_abstract=True)

# object class attributes and methods

# Button class attributes and methods
Button_IsOn: Property = Property(name="IsOn", type=BooleanType)
Button_FloorNumber: Property = Property(name="FloorNumber", type=IntegerType)
Button_Clicked: Property = Property(name="Clicked", type=StringType)
Button.attributes={Button_Clicked, Button_IsOn, Button_FloorNumber}

# FloorButton class attributes and methods
FloorButton_Elevator: Property = Property(name="Elevator", type=Elevator)
FloorButton.attributes={FloorButton_Elevator}

# UpDownButton class attributes and methods
UpDownButton_Direction: Property = Property(name="Direction", type=Direction)
UpDownButton_ElevatorBay: Property = Property(name="ElevatorBay", type=ElevatorBay)
UpDownButton.attributes={UpDownButton_Direction, UpDownButton_ElevatorBay}

# ElevatorBay class attributes and methods
ElevatorBay_Elevators: Property = Property(name="Elevators", type=StringType)
ElevatorBay_BayNumber: Property = Property(name="BayNumber", type=IntegerType)
ElevatorBay_UpDownButtons: Property = Property(name="UpDownButtons", type=StringType)
ElevatorBay.attributes={ElevatorBay_Elevators, ElevatorBay_UpDownButtons, ElevatorBay_BayNumber}

# Controller class attributes and methods

# Building class attributes and methods
Building_ElevatorBays: Property = Property(name="ElevatorBays", type=StringType)
Building_Controller: Property = Property(name="Controller", type=Controller)
Building.attributes={Building_Controller, Building_ElevatorBays}

# Elevator class attributes and methods
Elevator_ElevatorNumber: Property = Property(name="ElevatorNumber", type=IntegerType)
Elevator_ElevatorBayNumber: Property = Property(name="ElevatorBayNumber", type=IntegerType)
Elevator_CurrentFloor: Property = Property(name="CurrentFloor", type=IntegerType)
Elevator_FloorButtons: Property = Property(name="FloorButtons", type=StringType)
Elevator_CurrentMovement: Property = Property(name="CurrentMovement", type=StringType)
Elevator_ArrivedAtFloor: Property = Property(name="ArrivedAtFloor", type=StringType)
Elevator.attributes={Elevator_CurrentFloor, Elevator_ArrivedAtFloor, Elevator_ElevatorNumber, Elevator_CurrentMovement, Elevator_ElevatorBayNumber, Elevator_FloorButtons}

# Algorithm class attributes and methods
Algorithm_TimeBetweenFloors: Property = Property(name="TimeBetweenFloors", type=StringType)
Algorithm.attributes={Algorithm_TimeBetweenFloors}

# Relationships
Building_ElevatorBay: BinaryAssociation = BinaryAssociation(
    name="Building_ElevatorBay",
    ends={
        Property(name="elevatorBay6", type=ElevatorBay, multiplicity=Multiplicity(1, 9999)),
        Property(name="building7", type=Building, multiplicity=Multiplicity(1, 1))
    }
)
Elevator_Button: BinaryAssociation = BinaryAssociation(
    name="Elevator_Button",
    ends={
        Property(name="button8", type=Button, multiplicity=Multiplicity(0, 1)),
        Property(name="elevator9", type=Elevator, multiplicity=Multiplicity(0, 1))
    }
)
Building_Controller: BinaryAssociation = BinaryAssociation(
    name="Building_Controller",
    ends={
        Property(name="controller10", type=Controller, multiplicity=Multiplicity(0, 1)),
        Property(name="building11", type=Building, multiplicity=Multiplicity(0, 1))
    }
)
Elevator_FloorButton: BinaryAssociation = BinaryAssociation(
    name="Elevator_FloorButton",
    ends={
        Property(name="floorButton0", type=FloorButton, multiplicity=Multiplicity(1, 9999)),
        Property(name="elevator1", type=Elevator, multiplicity=Multiplicity(1, 1))
    }
)
ElevatorBay_Elevator: BinaryAssociation = BinaryAssociation(
    name="ElevatorBay_Elevator",
    ends={
        Property(name="elevator2", type=Elevator, multiplicity=Multiplicity(1, 9999)),
        Property(name="elevatorBay3", type=ElevatorBay, multiplicity=Multiplicity(1, 1))
    }
)
ElevatorBay_UpDownButton: BinaryAssociation = BinaryAssociation(
    name="ElevatorBay_UpDownButton",
    ends={
        Property(name="upDownButton4", type=UpDownButton, multiplicity=Multiplicity(1, 9999)),
        Property(name="elevatorBay5", type=ElevatorBay, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_18G9EOBgEeeAyLDAJ12_fg",
    types={object, Button, FloorButton, UpDownButton, ElevatorBay, Controller, Building, Elevator, Algorithm, Direction},
    associations={Building_ElevatorBay, Elevator_Button, Building_Controller, Elevator_FloorButton, ElevatorBay_Elevator, ElevatorBay_UpDownButton},
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