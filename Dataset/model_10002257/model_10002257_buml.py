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
Elevator = Class(name="Elevator")
Button = Class(name="Button")
ElevatorComponent = Class(name="ElevatorComponent", is_abstract=True)
ElevatorControl = Class(name="ElevatorControl")

# Elevator class attributes and methods
Elevator_number: Property = Property(name="number", type=IntegerType)
Elevator_currentFloor: Property = Property(name="currentFloor", type=IntegerType)
Elevator_destinationFloor: Property = Property(name="destinationFloor", type=IntegerType)
Elevator.attributes={Elevator_destinationFloor, Elevator_currentFloor, Elevator_number}

# Button class attributes and methods
Button_floor: Property = Property(name="floor", type=IntegerType)
Button_pressed: Property = Property(name="pressed", type=BooleanType)
Button.attributes={Button_floor, Button_pressed}

# ElevatorComponent class attributes and methods
ElevatorComponent_direction: Property = Property(name="direction", type=Direction)
ElevatorComponent.attributes={ElevatorComponent_direction}

# ElevatorControl class attributes and methods

# Relationships
Elevator_ElevatorControl: BinaryAssociation = BinaryAssociation(
    name="Elevator_ElevatorControl",
    ends={
        Property(name="elevatorControl0", type=ElevatorControl, multiplicity=Multiplicity(1, 1)),
        Property(name="elevator1", type=Elevator, multiplicity=Multiplicity(0, 9999))
    }
)
Button_ElevatorControl: BinaryAssociation = BinaryAssociation(
    name="Button_ElevatorControl",
    ends={
        Property(name="elevatorControl2", type=ElevatorControl, multiplicity=Multiplicity(1, 1)),
        Property(name="button3", type=Button, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_zsDrwDO_Eei8i88GzKaw4w",
    types={Elevator, Button, ElevatorComponent, ElevatorControl, Direction},
    associations={Elevator_ElevatorControl, Button_ElevatorControl},
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