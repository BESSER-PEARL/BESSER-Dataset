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
rover_Rover = Class(name="rover::Rover")
rover_Component = Class(name="rover::Component", is_abstract=True)
rover_Program = Class(name="rover::Program")
rover_Sensor = Class(name="rover::Sensor", is_abstract=True)
Component = Class(name="Component")
rover_Tansition = Class(name="rover::Tansition")
rover_Actuator = Class(name="rover::Actuator", is_abstract=True)
rover_GPS = Class(name="rover::GPS")
Sensor = Class(name="Sensor")
rover_DistanceSensor = Class(name="rover::DistanceSensor")
rover_directionFacing = Class(name="rover::directionFacing")
rover_Motor = Class(name="rover::Motor")
Actuator = Class(name="Actuator")
rover_Light = Class(name="rover::Light")
rover_Block = Class(name="rover::Block")
rover_Command = Class(name="rover::Command")
rover_Repeate = Class(name="rover::Repeate")
rover_Rotate = Class(name="rover::Rotate")
rover_Move = Class(name="rover::Move")
rover_Wait = Class(name="rover::Wait")
rover_SetLightColor = Class(name="rover::SetLightColor")
rover_SingleQuantity = Class(name="rover::SingleQuantity")
rover_PositionQuantity = Class(name="rover::PositionQuantity")
rover_Compass = Class(name="rover::Compass")

# rover_Rover class attributes and methods

# rover_Component class attributes and methods
rover_Component_name: Property = Property(name="name", type=StringType)
rover_Component.attributes={rover_Component_name}

# rover_Program class attributes and methods
rover_Program_name: Property = Property(name="name", type=StringType)
rover_Program.attributes={rover_Program_name}

# rover_Sensor class attributes and methods

# Component class attributes and methods

# rover_Tansition class attributes and methods
rover_Tansition_comparedQuantity: Property = Property(name="comparedQuantity", type=StringType)
rover_Tansition_operationUsed: Property = Property(name="operationUsed", type=StringType)
rover_Tansition.attributes={rover_Tansition_operationUsed, rover_Tansition_comparedQuantity}

# rover_Actuator class attributes and methods

# rover_GPS class attributes and methods
rover_GPS_currentPosition: Property = Property(name="currentPosition", type=FloatType)
rover_GPS.attributes={rover_GPS_currentPosition}

# Sensor class attributes and methods

# rover_DistanceSensor class attributes and methods
rover_DistanceSensor_remainingDistance: Property = Property(name="remainingDistance", type=FloatType)
rover_DistanceSensor.attributes={rover_DistanceSensor_remainingDistance}

# rover_directionFacing class attributes and methods
rover_directionFacing_currentlyFacing: Property = Property(name="currentlyFacing", type=FloatType)
rover_directionFacing.attributes={rover_directionFacing_currentlyFacing}

# rover_Motor class attributes and methods

# Actuator class attributes and methods

# rover_Light class attributes and methods

# rover_Block class attributes and methods
rover_Block_name: Property = Property(name="name", type=StringType)
rover_Block.attributes={rover_Block_name}

# rover_Command class attributes and methods

# rover_Repeate class attributes and methods
rover_Repeate_count: Property = Property(name="count", type=IntegerType)
rover_Repeate.attributes={rover_Repeate_count}

# rover_Rotate class attributes and methods
rover_Rotate_angel: Property = Property(name="angel", type=IntegerType)
rover_Rotate.attributes={rover_Rotate_angel}

# rover_Move class attributes and methods
rover_Move_length: Property = Property(name="length", type=IntegerType)
rover_Move_velocity: Property = Property(name="velocity", type=IntegerType)
rover_Move.attributes={rover_Move_length, rover_Move_velocity}

# rover_Wait class attributes and methods
rover_Wait_time: Property = Property(name="time", type=IntegerType)
rover_Wait.attributes={rover_Wait_time}

# rover_SetLightColor class attributes and methods
rover_SetLightColor_color: Property = Property(name="color", type=StringType)
rover_SetLightColor.attributes={rover_SetLightColor_color}

# rover_SingleQuantity class attributes and methods

# rover_PositionQuantity class attributes and methods

# rover_Compass class attributes and methods

# Relationships
component0: BinaryAssociation = BinaryAssociation(
    name="component0",
    ends={
        Property(name="rover_Component", type=rover_Rover, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Rover", type=rover_Component, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
program1: BinaryAssociation = BinaryAssociation(
    name="program1",
    ends={
        Property(name="rover_Program", type=rover_Rover, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Rover2", type=rover_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
triggered3: BinaryAssociation = BinaryAssociation(
    name="triggered3",
    ends={
        Property(name="rover_Tansition", type=rover_Sensor, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Sensor", type=rover_Tansition, multiplicity=Multiplicity(0, 1))
    }
)
outgoingTransition21: BinaryAssociation = BinaryAssociation(
    name="outgoingTransition21",
    ends={
        Property(name="Tansition", type=rover_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceCommand", type=rover_Tansition, multiplicity=Multiplicity(0, 1))
    }
)
block4: BinaryAssociation = BinaryAssociation(
    name="block4",
    ends={
        Property(name="rover_Block", type=rover_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Program5", type=rover_Block, multiplicity=Multiplicity(1, 1))
    }
)
command6: BinaryAssociation = BinaryAssociation(
    name="command6",
    ends={
        Property(name="rover_Command", type=rover_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Block7", type=rover_Command, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tansition8: BinaryAssociation = BinaryAssociation(
    name="tansition8",
    ends={
        Property(name="rover_Tansition10", type=rover_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Block9", type=rover_Tansition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
repeate11: BinaryAssociation = BinaryAssociation(
    name="repeate11",
    ends={
        Property(name="rover_Repeate", type=rover_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Command12", type=rover_Repeate, multiplicity=Multiplicity(0, 1))
    }
)
rotate13: BinaryAssociation = BinaryAssociation(
    name="rotate13",
    ends={
        Property(name="rover_Rotate", type=rover_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Command14", type=rover_Rotate, multiplicity=Multiplicity(0, 1))
    }
)
move15: BinaryAssociation = BinaryAssociation(
    name="move15",
    ends={
        Property(name="rover_Move", type=rover_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Command16", type=rover_Move, multiplicity=Multiplicity(0, 1))
    }
)
wait17: BinaryAssociation = BinaryAssociation(
    name="wait17",
    ends={
        Property(name="rover_Wait", type=rover_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Command18", type=rover_Wait, multiplicity=Multiplicity(0, 1))
    }
)
setlightcolor19: BinaryAssociation = BinaryAssociation(
    name="setlightcolor19",
    ends={
        Property(name="rover_SetLightColor", type=rover_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Command20", type=rover_SetLightColor, multiplicity=Multiplicity(0, 1))
    }
)
incomingTransition22: BinaryAssociation = BinaryAssociation(
    name="incomingTransition22",
    ends={
        Property(name="Tansition23", type=rover_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="targetCommand", type=rover_Tansition, multiplicity=Multiplicity(0, 1))
    }
)
sourceCommand24: BinaryAssociation = BinaryAssociation(
    name="sourceCommand24",
    ends={
        Property(name="Command", type=rover_Tansition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransition", type=rover_Command, multiplicity=Multiplicity(0, 1))
    }
)
targetCommand25: BinaryAssociation = BinaryAssociation(
    name="targetCommand25",
    ends={
        Property(name="Command26", type=rover_Tansition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransition", type=rover_Command, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_rover_Sensor_Component = Generalization(general=Component, specific=rover_Sensor)
gen_rover_Actuator_Component = Generalization(general=Component, specific=rover_Actuator)
gen_rover_GPS_Sensor = Generalization(general=Sensor, specific=rover_GPS)
gen_rover_DistanceSensor_Sensor = Generalization(general=Sensor, specific=rover_DistanceSensor)
gen_rover_directionFacing_Sensor = Generalization(general=Sensor, specific=rover_directionFacing)
gen_rover_Motor_Actuator = Generalization(general=Actuator, specific=rover_Motor)
gen_rover_Light_Actuator = Generalization(general=Actuator, specific=rover_Light)
gen_rover_Compass_Sensor = Generalization(general=Sensor, specific=rover_Compass)

# Domain Model
domain_model = DomainModel(
    name="rover",
    types={rover_Rover, rover_Component, rover_Program, rover_Sensor, Component, rover_Tansition, rover_Actuator, rover_GPS, Sensor, rover_DistanceSensor, rover_directionFacing, rover_Motor, Actuator, rover_Light, rover_Block, rover_Command, rover_Repeate, rover_Rotate, rover_Move, rover_Wait, rover_SetLightColor, rover_SingleQuantity, rover_PositionQuantity, rover_Compass},
    associations={component0, program1, triggered3, outgoingTransition21, block4, command6, tansition8, repeate11, rotate13, move15, wait17, setlightcolor19, incomingTransition22, sourceCommand24, targetCommand25},
    generalizations={gen_rover_Sensor_Component, gen_rover_Actuator_Component, gen_rover_GPS_Sensor, gen_rover_DistanceSensor_Sensor, gen_rover_directionFacing_Sensor, gen_rover_Motor_Actuator, gen_rover_Light_Actuator, gen_rover_Compass_Sensor},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)