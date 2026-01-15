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
ColorKind: Enumeration = Enumeration(
    name="ColorKind",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="Red"),
			EnumerationLiteral(name="Green"),
			EnumerationLiteral(name="Blue"),
			EnumerationLiteral(name="Yellow")
    }
)

Operator: Enumeration = Enumeration(
    name="Operator",
    literals={
            EnumerationLiteral(name="smaller"),
			EnumerationLiteral(name="greater"),
			EnumerationLiteral(name="equal"),
			EnumerationLiteral(name="unequal")
    }
)

TimeUnit: Enumeration = Enumeration(
    name="TimeUnit",
    literals={
            EnumerationLiteral(name="nanoseconds"),
			EnumerationLiteral(name="milliseconds"),
			EnumerationLiteral(name="seconds"),
			EnumerationLiteral(name="minutes"),
			EnumerationLiteral(name="hours")
    }
)

LengthUnit: Enumeration = Enumeration(
    name="LengthUnit",
    literals={
            EnumerationLiteral(name="millimeters"),
			EnumerationLiteral(name="centimeters"),
			EnumerationLiteral(name="meters")
    }
)

VelocityUnit: Enumeration = Enumeration(
    name="VelocityUnit",
    literals={
            EnumerationLiteral(name="millimeters_per_second"),
			EnumerationLiteral(name="centimeters_per_second")
    }
)

AngleUnit: Enumeration = Enumeration(
    name="AngleUnit",
    literals={
            EnumerationLiteral(name="radians"),
			EnumerationLiteral(name="degrees")
    }
)

# Classes
rover_System = Class(name="rover::System")
rover_Rover = Class(name="rover::Rover")
rover_Program = Class(name="rover::Program")
rover_Component = Class(name="rover::Component", is_abstract=True)
rover_Block = Class(name="rover::Block")
rover_Quantity = Class(name="rover::Quantity", is_abstract=True)
rover_Actuator = Class(name="rover::Actuator", is_abstract=True)
Component = Class(name="Component")
rover_Sensor = Class(name="rover::Sensor", is_abstract=True)
rover_Motor = Class(name="rover::Motor")
Actuator = Class(name="Actuator")
rover_Light = Class(name="rover::Light")
rover_GPS = Class(name="rover::GPS")
Sensor = Class(name="Sensor")
rover_Position = Class(name="rover::Position")
rover_Distance = Class(name="rover::Distance")
rover_Length = Class(name="rover::Length")
rover_Command = Class(name="rover::Command", is_abstract=True)
rover_Transition = Class(name="rover::Transition", is_abstract=True)
rover_Repeat = Class(name="rover::Repeat")
rover_SetLightColor = Class(name="rover::SetLightColor")
Command = Class(name="Command")
rover_Wait = Class(name="rover::Wait")
rover_Time = Class(name="rover::Time")
rover_Move = Class(name="rover::Move")
rover_Compass = Class(name="rover::Compass")
rover_Angle = Class(name="rover::Angle")
rover_Rotate = Class(name="rover::Rotate")
rover_Terminate = Class(name="rover::Terminate")
rover_TriggeredTransition = Class(name="rover::TriggeredTransition", is_abstract=True)
Transition = Class(name="Transition")
rover_DistanceSensorTrigger = Class(name="rover::DistanceSensorTrigger")
TriggeredTransition = Class(name="TriggeredTransition")
rover_CompassTrigger = Class(name="rover::CompassTrigger")
rover_Velocity = Class(name="rover::Velocity")
rover_SingleQuantity = Class(name="rover::SingleQuantity", is_abstract=True)
Quantity = Class(name="Quantity")
SingleQuantity = Class(name="SingleQuantity")
rover_NormalTransition = Class(name="rover::NormalTransition")
rover_GPSTrigger = Class(name="rover::GPSTrigger")

# rover_System class attributes and methods

# rover_Rover class attributes and methods
rover_Rover_name: Property = Property(name="name", type=StringType)
rover_Rover.attributes={rover_Rover_name}

# rover_Program class attributes and methods
rover_Program_name: Property = Property(name="name", type=StringType)
rover_Program.attributes={rover_Program_name}

# rover_Component class attributes and methods
rover_Component_name: Property = Property(name="name", type=StringType)
rover_Component.attributes={rover_Component_name}

# rover_Block class attributes and methods

# rover_Quantity class attributes and methods

# rover_Actuator class attributes and methods

# Component class attributes and methods

# rover_Sensor class attributes and methods

# rover_Motor class attributes and methods

# Actuator class attributes and methods

# rover_Light class attributes and methods
rover_Light_color: Property = Property(name="color", type=StringType)
rover_Light.attributes={rover_Light_color}

# rover_GPS class attributes and methods

# Sensor class attributes and methods

# rover_Position class attributes and methods

# rover_Distance class attributes and methods

# rover_Length class attributes and methods
rover_Length_lengthUnit: Property = Property(name="lengthUnit", type=StringType)
rover_Length.attributes={rover_Length_lengthUnit}

# rover_Command class attributes and methods

# rover_Transition class attributes and methods

# rover_Repeat class attributes and methods
rover_Repeat_count: Property = Property(name="count", type=IntegerType)
rover_Repeat.attributes={rover_Repeat_count}

# rover_SetLightColor class attributes and methods
rover_SetLightColor_lightColor: Property = Property(name="lightColor", type=StringType)
rover_SetLightColor.attributes={rover_SetLightColor_lightColor}

# Command class attributes and methods

# rover_Wait class attributes and methods

# rover_Time class attributes and methods
rover_Time_timeUnit: Property = Property(name="timeUnit", type=StringType)
rover_Time.attributes={rover_Time_timeUnit}

# rover_Move class attributes and methods

# rover_Compass class attributes and methods

# rover_Angle class attributes and methods
rover_Angle_angleUnit: Property = Property(name="angleUnit", type=StringType)
rover_Angle.attributes={rover_Angle_angleUnit}

# rover_Rotate class attributes and methods

# rover_Terminate class attributes and methods

# rover_TriggeredTransition class attributes and methods
rover_TriggeredTransition_Operator: Property = Property(name="Operator", type=StringType)
rover_TriggeredTransition.attributes={rover_TriggeredTransition_Operator}

# Transition class attributes and methods

# rover_DistanceSensorTrigger class attributes and methods

# TriggeredTransition class attributes and methods

# rover_CompassTrigger class attributes and methods

# rover_Velocity class attributes and methods
rover_Velocity_velocityUnit: Property = Property(name="velocityUnit", type=StringType)
rover_Velocity.attributes={rover_Velocity_velocityUnit}

# rover_SingleQuantity class attributes and methods
rover_SingleQuantity_value: Property = Property(name="value", type=FloatType)
rover_SingleQuantity.attributes={rover_SingleQuantity_value}

# Quantity class attributes and methods

# SingleQuantity class attributes and methods

# rover_NormalTransition class attributes and methods

# rover_GPSTrigger class attributes and methods

# Relationships
rover0: BinaryAssociation = BinaryAssociation(
    name="rover0",
    ends={
        Property(name="rover_Rover", type=rover_System, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_System", type=rover_Rover, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
program1: BinaryAssociation = BinaryAssociation(
    name="program1",
    ends={
        Property(name="rover_Program", type=rover_System, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_System2", type=rover_Program, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
component3: BinaryAssociation = BinaryAssociation(
    name="component3",
    ends={
        Property(name="rover_Component", type=rover_Rover, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Rover4", type=rover_Component, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
rover5: BinaryAssociation = BinaryAssociation(
    name="rover5",
    ends={
        Property(name="rover_Rover7", type=rover_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Program6", type=rover_Rover, multiplicity=Multiplicity(1, 1))
    }
)
block8: BinaryAssociation = BinaryAssociation(
    name="block8",
    ends={
        Property(name="rover_Block", type=rover_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Program9", type=rover_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
quantity10: BinaryAssociation = BinaryAssociation(
    name="quantity10",
    ends={
        Property(name="rover_Quantity", type=rover_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Program11", type=rover_Quantity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
angle13: BinaryAssociation = BinaryAssociation(
    name="angle13",
    ends={
        Property(name="rover_Angle", type=rover_Compass, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Compass", type=rover_Angle, multiplicity=Multiplicity(1, 1))
    }
)
length14: BinaryAssociation = BinaryAssociation(
    name="length14",
    ends={
        Property(name="rover_Length", type=rover_Distance, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Distance", type=rover_Length, multiplicity=Multiplicity(1, 1))
    }
)
command15: BinaryAssociation = BinaryAssociation(
    name="command15",
    ends={
        Property(name="rover_Command", type=rover_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Block16", type=rover_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition17: BinaryAssociation = BinaryAssociation(
    name="transition17",
    ends={
        Property(name="rover_Transition", type=rover_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Block18", type=rover_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repeat19: BinaryAssociation = BinaryAssociation(
    name="repeat19",
    ends={
        Property(name="rover_Repeat", type=rover_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Block20", type=rover_Repeat, multiplicity=Multiplicity(0, 1))
    }
)
outgoingTransition21: BinaryAssociation = BinaryAssociation(
    name="outgoingTransition21",
    ends={
        Property(name="Transition", type=rover_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=rover_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransition22: BinaryAssociation = BinaryAssociation(
    name="incomingTransition22",
    ends={
        Property(name="Transition23", type=rover_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=rover_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source24: BinaryAssociation = BinaryAssociation(
    name="source24",
    ends={
        Property(name="Command", type=rover_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransition", type=rover_Command, multiplicity=Multiplicity(1, 1))
    }
)
target25: BinaryAssociation = BinaryAssociation(
    name="target25",
    ends={
        Property(name="Command26", type=rover_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransition", type=rover_Command, multiplicity=Multiplicity(1, 1))
    }
)
light27: BinaryAssociation = BinaryAssociation(
    name="light27",
    ends={
        Property(name="rover_Light", type=rover_SetLightColor, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_SetLightColor", type=rover_Light, multiplicity=Multiplicity(1, 1))
    }
)
time28: BinaryAssociation = BinaryAssociation(
    name="time28",
    ends={
        Property(name="rover_Time", type=rover_Wait, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Wait", type=rover_Time, multiplicity=Multiplicity(1, 1))
    }
)
motor29: BinaryAssociation = BinaryAssociation(
    name="motor29",
    ends={
        Property(name="rover_Motor", type=rover_Move, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Move", type=rover_Motor, multiplicity=Multiplicity(1, 1))
    }
)
position12: BinaryAssociation = BinaryAssociation(
    name="position12",
    ends={
        Property(name="rover_Position", type=rover_GPS, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_GPS", type=rover_Position, multiplicity=Multiplicity(1, 1))
    }
)
angle35: BinaryAssociation = BinaryAssociation(
    name="angle35",
    ends={
        Property(name="rover_Angle36", type=rover_Rotate, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Rotate", type=rover_Angle, multiplicity=Multiplicity(1, 1))
    }
)
setlightcolor37: BinaryAssociation = BinaryAssociation(
    name="setlightcolor37",
    ends={
        Property(name="rover_SetLightColor39", type=rover_Repeat, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Repeat38", type=rover_SetLightColor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wait40: BinaryAssociation = BinaryAssociation(
    name="wait40",
    ends={
        Property(name="rover_Wait42", type=rover_Repeat, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Repeat41", type=rover_Wait, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
move43: BinaryAssociation = BinaryAssociation(
    name="move43",
    ends={
        Property(name="rover_Move45", type=rover_Repeat, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Repeat44", type=rover_Move, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rotate46: BinaryAssociation = BinaryAssociation(
    name="rotate46",
    ends={
        Property(name="rover_Rotate48", type=rover_Repeat, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Repeat47", type=rover_Rotate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
distance49: BinaryAssociation = BinaryAssociation(
    name="distance49",
    ends={
        Property(name="rover_Distance50", type=rover_DistanceSensorTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_DistanceSensorTrigger", type=rover_Distance, multiplicity=Multiplicity(1, 1))
    }
)
length51: BinaryAssociation = BinaryAssociation(
    name="length51",
    ends={
        Property(name="rover_Length53", type=rover_DistanceSensorTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_DistanceSensorTrigger52", type=rover_Length, multiplicity=Multiplicity(1, 1))
    }
)
compass54: BinaryAssociation = BinaryAssociation(
    name="compass54",
    ends={
        Property(name="rover_Compass55", type=rover_CompassTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_CompassTrigger", type=rover_Compass, multiplicity=Multiplicity(1, 1))
    }
)
length30: BinaryAssociation = BinaryAssociation(
    name="length30",
    ends={
        Property(name="rover_Length32", type=rover_Move, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Move31", type=rover_Length, multiplicity=Multiplicity(0, 1))
    }
)
velocity33: BinaryAssociation = BinaryAssociation(
    name="velocity33",
    ends={
        Property(name="rover_Velocity", type=rover_Move, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Move34", type=rover_Velocity, multiplicity=Multiplicity(1, 1))
    }
)
gps59: BinaryAssociation = BinaryAssociation(
    name="gps59",
    ends={
        Property(name="rover_GPS60", type=rover_GPSTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_GPSTrigger", type=rover_GPS, multiplicity=Multiplicity(1, 1))
    }
)
position61: BinaryAssociation = BinaryAssociation(
    name="position61",
    ends={
        Property(name="rover_Position63", type=rover_GPSTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_GPSTrigger62", type=rover_Position, multiplicity=Multiplicity(1, 1))
    }
)
X64: BinaryAssociation = BinaryAssociation(
    name="X64",
    ends={
        Property(name="rover_Length66", type=rover_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Position65", type=rover_Length, multiplicity=Multiplicity(1, 1))
    }
)
Y67: BinaryAssociation = BinaryAssociation(
    name="Y67",
    ends={
        Property(name="rover_Length69", type=rover_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_Position68", type=rover_Length, multiplicity=Multiplicity(1, 1))
    }
)
angle56: BinaryAssociation = BinaryAssociation(
    name="angle56",
    ends={
        Property(name="rover_Angle58", type=rover_CompassTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="rover_CompassTrigger57", type=rover_Angle, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_rover_Actuator_Component = Generalization(general=Component, specific=rover_Actuator)
gen_rover_Sensor_Component = Generalization(general=Component, specific=rover_Sensor)
gen_rover_Motor_Actuator = Generalization(general=Actuator, specific=rover_Motor)
gen_rover_Light_Actuator = Generalization(general=Actuator, specific=rover_Light)
gen_rover_GPS_Sensor = Generalization(general=Sensor, specific=rover_GPS)
gen_rover_Distance_Sensor = Generalization(general=Sensor, specific=rover_Distance)
gen_rover_SetLightColor_Command = Generalization(general=Command, specific=rover_SetLightColor)
gen_rover_Wait_Command = Generalization(general=Command, specific=rover_Wait)
gen_rover_Move_Command = Generalization(general=Command, specific=rover_Move)
gen_rover_Compass_Sensor = Generalization(general=Sensor, specific=rover_Compass)
gen_rover_Rotate_Command = Generalization(general=Command, specific=rover_Rotate)
gen_rover_Terminate_Command = Generalization(general=Command, specific=rover_Terminate)
gen_rover_Repeat_Command = Generalization(general=Command, specific=rover_Repeat)
gen_rover_TriggeredTransition_Transition = Generalization(general=Transition, specific=rover_TriggeredTransition)
gen_rover_DistanceSensorTrigger_TriggeredTransition = Generalization(general=TriggeredTransition, specific=rover_DistanceSensorTrigger)
gen_rover_CompassTrigger_TriggeredTransition = Generalization(general=TriggeredTransition, specific=rover_CompassTrigger)
gen_rover_SingleQuantity_Quantity = Generalization(general=Quantity, specific=rover_SingleQuantity)
gen_rover_Position_Quantity = Generalization(general=Quantity, specific=rover_Position)
gen_rover_Time_SingleQuantity = Generalization(general=SingleQuantity, specific=rover_Time)
gen_rover_Velocity_SingleQuantity = Generalization(general=SingleQuantity, specific=rover_Velocity)
gen_rover_Angle_SingleQuantity = Generalization(general=SingleQuantity, specific=rover_Angle)
gen_rover_Length_SingleQuantity = Generalization(general=SingleQuantity, specific=rover_Length)
gen_rover_NormalTransition_Transition = Generalization(general=Transition, specific=rover_NormalTransition)
gen_rover_GPSTrigger_TriggeredTransition = Generalization(general=TriggeredTransition, specific=rover_GPSTrigger)

# Domain Model
domain_model = DomainModel(
    name="rover",
    types={rover_System, rover_Rover, rover_Program, rover_Component, rover_Block, rover_Quantity, rover_Actuator, Component, rover_Sensor, rover_Motor, Actuator, rover_Light, rover_GPS, Sensor, rover_Position, rover_Distance, rover_Length, rover_Command, rover_Transition, rover_Repeat, rover_SetLightColor, Command, rover_Wait, rover_Time, rover_Move, rover_Compass, rover_Angle, rover_Rotate, rover_Terminate, rover_TriggeredTransition, Transition, rover_DistanceSensorTrigger, TriggeredTransition, rover_CompassTrigger, rover_Velocity, rover_SingleQuantity, Quantity, SingleQuantity, rover_NormalTransition, rover_GPSTrigger, ColorKind, Operator, TimeUnit, LengthUnit, VelocityUnit, AngleUnit},
    associations={rover0, program1, component3, rover5, block8, quantity10, angle13, length14, command15, transition17, repeat19, outgoingTransition21, incomingTransition22, source24, target25, light27, time28, motor29, position12, angle35, setlightcolor37, wait40, move43, rotate46, distance49, length51, compass54, length30, velocity33, gps59, position61, X64, Y67, angle56},
    generalizations={gen_rover_Actuator_Component, gen_rover_Sensor_Component, gen_rover_Motor_Actuator, gen_rover_Light_Actuator, gen_rover_GPS_Sensor, gen_rover_Distance_Sensor, gen_rover_SetLightColor_Command, gen_rover_Wait_Command, gen_rover_Move_Command, gen_rover_Compass_Sensor, gen_rover_Rotate_Command, gen_rover_Terminate_Command, gen_rover_Repeat_Command, gen_rover_TriggeredTransition_Transition, gen_rover_DistanceSensorTrigger_TriggeredTransition, gen_rover_CompassTrigger_TriggeredTransition, gen_rover_SingleQuantity_Quantity, gen_rover_Position_Quantity, gen_rover_Time_SingleQuantity, gen_rover_Velocity_SingleQuantity, gen_rover_Angle_SingleQuantity, gen_rover_Length_SingleQuantity, gen_rover_NormalTransition_Transition, gen_rover_GPSTrigger_TriggeredTransition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)