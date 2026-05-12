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
Enumeration_: Enumeration = Enumeration(
    name="Enumeration",
    literals={
            
    }
)

# Classes
ElevatorController = Class(name="ElevatorController")
Floor = Class(name="Floor")
Elevator = Class(name="Elevator")
Queue = Class(name="Queue")
Elevator_Button = Class(name="Elevator_Button")
EmergencyButton = Class(name="EmergencyButton")
Button_Interface = Class(name="Button_Interface")
FloorButton = Class(name="FloorButton")
OutOfServiceMechanism = Class(name="OutOfServiceMechanism")

# ElevatorController class attributes and methods
ElevatorController_floors: Property = Property(name="floors", type=Floor)
ElevatorController_elevators: Property = Property(name="elevators", type=Elevator)
ElevatorController.attributes={ElevatorController_floors, ElevatorController_elevators}

# Floor class attributes and methods
Floor_floorID: Property = Property(name="floorID", type=IntegerType)
Floor_floorButtons: Property = Property(name="floorButtons", type=FloorButton)
Floor.attributes={Floor_floorID, Floor_floorButtons}

# Elevator class attributes and methods
Elevator_emergencyButton: Property = Property(name="emergencyButton", type=EmergencyButton)
Elevator_queue: Property = Property(name="queue", type=Queue)
Elevator_outOfServiceMech: Property = Property(name="outOfServiceMech", type=OutOfServiceMechanism)
Elevator_buttons: Property = Property(name="buttons", type=Elevator_Button)
Elevator_isOutOfService: Property = Property(name="isOutOfService", type=BooleanType)
Elevator.attributes={Elevator_queue, Elevator_emergencyButton, Elevator_buttons, Elevator_outOfServiceMech, Elevator_isOutOfService}

# Queue class attributes and methods
Queue_currentDirection: Property = Property(name="currentDirection", type=Enumeration_)
Queue_floorQueue: Property = Property(name="floorQueue", type=IntegerType)
Queue.attributes={Queue_currentDirection, Queue_floorQueue}

# Elevator_Button class attributes and methods
Elevator_Button_floorID: Property = Property(name="floorID", type=IntegerType)
Elevator_Button.attributes={Elevator_Button_floorID}

# EmergencyButton class attributes and methods

# Button_Interface class attributes and methods

# FloorButton class attributes and methods
FloorButton_direction: Property = Property(name="direction", type=Enumeration_)
FloorButton.attributes={FloorButton_direction}

# OutOfServiceMechanism class attributes and methods

# Relationships
ElevatorController_Elevator: BinaryAssociation = BinaryAssociation(
    name="ElevatorController_Elevator",
    ends={
        Property(name="elevator0", type=Elevator, multiplicity=Multiplicity(2, 2)),
        Property(name="elevatorController1", type=ElevatorController, multiplicity=Multiplicity(1, 1))
    }
)
ElevatorController_Floor: BinaryAssociation = BinaryAssociation(
    name="ElevatorController_Floor",
    ends={
        Property(name="floor2", type=Floor, multiplicity=Multiplicity(5, 5)),
        Property(name="elevatorController3", type=ElevatorController, multiplicity=Multiplicity(1, 1))
    }
)
Floor_FloorButton: BinaryAssociation = BinaryAssociation(
    name="Floor_FloorButton",
    ends={
        Property(name="floorButton4", type=FloorButton, multiplicity=Multiplicity(1, 2)),
        Property(name="floor5", type=Floor, multiplicity=Multiplicity(1, 1))
    }
)
Elevator_Queue: BinaryAssociation = BinaryAssociation(
    name="Elevator_Queue",
    ends={
        Property(name="queue6", type=Queue, multiplicity=Multiplicity(1, 1)),
        Property(name="elevator7", type=Elevator, multiplicity=Multiplicity(1, 1))
    }
)
Elevator_Elevator_Button: BinaryAssociation = BinaryAssociation(
    name="Elevator_Elevator_Button",
    ends={
        Property(name="elevator_Button8", type=Elevator_Button, multiplicity=Multiplicity(5, 5)),
        Property(name="elevator9", type=Elevator, multiplicity=Multiplicity(1, 1))
    }
)
Elevator_EmergencyButton: BinaryAssociation = BinaryAssociation(
    name="Elevator_EmergencyButton",
    ends={
        Property(name="emergencyButton10", type=EmergencyButton, multiplicity=Multiplicity(1, 1)),
        Property(name="elevator11", type=Elevator, multiplicity=Multiplicity(1, 1))
    }
)
Elevator_OutOfServiceMechanism: BinaryAssociation = BinaryAssociation(
    name="Elevator_OutOfServiceMechanism",
    ends={
        Property(name="outOfServiceMechanism12", type=OutOfServiceMechanism, multiplicity=Multiplicity(1, 1)),
        Property(name="elevator13", type=Elevator, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="eee2928a_2be6_4ebc_8a43_95c899f4d0b5",
    types={ElevatorController, Floor, Elevator, Queue, Elevator_Button, EmergencyButton, Button_Interface, FloorButton, OutOfServiceMechanism, Enumeration_},
    associations={ElevatorController_Elevator, ElevatorController_Floor, Floor_FloorButton, Elevator_Queue, Elevator_Elevator_Button, Elevator_EmergencyButton, Elevator_OutOfServiceMechanism},
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