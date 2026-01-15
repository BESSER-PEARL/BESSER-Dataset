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
TimeUnits: Enumeration = Enumeration(
    name="TimeUnits",
    literals={
            EnumerationLiteral(name="NANOSECONDS"),
			EnumerationLiteral(name="MILLISECONDS"),
			EnumerationLiteral(name="SECONDS"),
			EnumerationLiteral(name="MINUTES"),
			EnumerationLiteral(name="HOURS")
    }
)

VelocityUnits: Enumeration = Enumeration(
    name="VelocityUnits",
    literals={
            EnumerationLiteral(name="MILLIMETERS_PER_SECOND"),
			EnumerationLiteral(name="CENTIMETERS_PER_SECOND")
    }
)

LengthUnits: Enumeration = Enumeration(
    name="LengthUnits",
    literals={
            EnumerationLiteral(name="MILLIMETERS"),
			EnumerationLiteral(name="CENTIMETERS"),
			EnumerationLiteral(name="METERS")
    }
)

AngleUnits: Enumeration = Enumeration(
    name="AngleUnits",
    literals={
            EnumerationLiteral(name="RADIANS"),
			EnumerationLiteral(name="DEGREES")
    }
)

Colours: Enumeration = Enumeration(
    name="Colours",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="RED"),
			EnumerationLiteral(name="GREEN"),
			EnumerationLiteral(name="BLUE"),
			EnumerationLiteral(name="YELLOW")
    }
)

# Classes
roverml_System = Class(name="roverml::System")
NamedElement = Class(name="NamedElement")
roverml_Program = Class(name="roverml::Program")
roverml_Rover = Class(name="roverml::Rover")
roverml_Component = Class(name="roverml::Component")
roverml_Sensor = Class(name="roverml::Sensor")
Component = Class(name="Component")
roverml_Actuator = Class(name="roverml::Actuator")
roverml_GPS = Class(name="roverml::GPS")
Sensor = Class(name="Sensor")
roverml_Compass = Class(name="roverml::Compass")
roverml_Block = Class(name="roverml::Block")
roverml_NamedElement = Class(name="roverml::NamedElement", is_abstract=True)
roverml_Time = Class(name="roverml::Time")
roverml_Move = Class(name="roverml::Move")
roverml_DistanceSensor = Class(name="roverml::DistanceSensor")
roverml_Motor = Class(name="roverml::Motor")
Actuator = Class(name="Actuator")
roverml_Light = Class(name="roverml::Light")
roverml_Transition = Class(name="roverml::Transition")
roverml_Command = Class(name="roverml::Command")
roverml_SetLightColor = Class(name="roverml::SetLightColor")
Command = Class(name="Command")
roverml_Wait = Class(name="roverml::Wait")
roverml_GPSTrigger = Class(name="roverml::GPSTrigger")
roverml_Position = Class(name="roverml::Position")
roverml_Velocity = Class(name="roverml::Velocity")
roverml_Length = Class(name="roverml::Length")
roverml_Rotate = Class(name="roverml::Rotate")
roverml_Angle = Class(name="roverml::Angle")
roverml_Terminate = Class(name="roverml::Terminate")
roverml_Repeat = Class(name="roverml::Repeat")
roverml_Triggered = Class(name="roverml::Triggered")
Transition = Class(name="Transition")
roverml_Regular = Class(name="roverml::Regular")
roverml_DistanceSensorTrigger = Class(name="roverml::DistanceSensorTrigger")
Triggered = Class(name="Triggered")
roverml_CompassTrigger = Class(name="roverml::CompassTrigger")
roverml_Quantity = Class(name="roverml::Quantity")
roverml_SingleQuantity = Class(name="roverml::SingleQuantity")
Quantity = Class(name="Quantity")
SingleQuantity = Class(name="SingleQuantity")

# roverml_System class attributes and methods

# NamedElement class attributes and methods

# roverml_Program class attributes and methods

# roverml_Rover class attributes and methods

# roverml_Component class attributes and methods

# roverml_Sensor class attributes and methods

# Component class attributes and methods

# roverml_Actuator class attributes and methods

# roverml_GPS class attributes and methods
roverml_GPS_x: Property = Property(name="x", type=FloatType)
roverml_GPS_y: Property = Property(name="y", type=FloatType)
roverml_GPS.attributes={roverml_GPS_x, roverml_GPS_y}

# Sensor class attributes and methods

# roverml_Compass class attributes and methods
roverml_Compass_angle: Property = Property(name="angle", type=IntegerType)
roverml_Compass.attributes={roverml_Compass_angle}

# roverml_Block class attributes and methods

# roverml_NamedElement class attributes and methods
roverml_NamedElement_name: Property = Property(name="name", type=StringType)
roverml_NamedElement.attributes={roverml_NamedElement_name}

# roverml_Time class attributes and methods
roverml_Time_units: Property = Property(name="units", type=StringType)
roverml_Time.attributes={roverml_Time_units}

# roverml_Move class attributes and methods
roverml_Move_length: Property = Property(name="length", type=FloatType)
roverml_Move_velocity: Property = Property(name="velocity", type=FloatType)
roverml_Move.attributes={roverml_Move_velocity, roverml_Move_length}

# roverml_DistanceSensor class attributes and methods
roverml_DistanceSensor_distance: Property = Property(name="distance", type=FloatType)
roverml_DistanceSensor.attributes={roverml_DistanceSensor_distance}

# roverml_Motor class attributes and methods

# Actuator class attributes and methods

# roverml_Light class attributes and methods

# roverml_Transition class attributes and methods

# roverml_Command class attributes and methods

# roverml_SetLightColor class attributes and methods
roverml_SetLightColor_color: Property = Property(name="color", type=StringType)
roverml_SetLightColor.attributes={roverml_SetLightColor_color}

# Command class attributes and methods

# roverml_Wait class attributes and methods
roverml_Wait_time: Property = Property(name="time", type=IntegerType)
roverml_Wait.attributes={roverml_Wait_time}

# roverml_GPSTrigger class attributes and methods
roverml_GPSTrigger_x: Property = Property(name="x", type=FloatType)
roverml_GPSTrigger_y: Property = Property(name="y", type=FloatType)
roverml_GPSTrigger.attributes={roverml_GPSTrigger_y, roverml_GPSTrigger_x}

# roverml_Position class attributes and methods
roverml_Position_x: Property = Property(name="x", type=FloatType)
roverml_Position_y: Property = Property(name="y", type=FloatType)
roverml_Position.attributes={roverml_Position_x, roverml_Position_y}

# roverml_Velocity class attributes and methods
roverml_Velocity_units: Property = Property(name="units", type=StringType)
roverml_Velocity.attributes={roverml_Velocity_units}

# roverml_Length class attributes and methods
roverml_Length_units: Property = Property(name="units", type=StringType)
roverml_Length.attributes={roverml_Length_units}

# roverml_Rotate class attributes and methods
roverml_Rotate_angle: Property = Property(name="angle", type=IntegerType)
roverml_Rotate.attributes={roverml_Rotate_angle}

# roverml_Angle class attributes and methods
roverml_Angle_units: Property = Property(name="units", type=StringType)
roverml_Angle.attributes={roverml_Angle_units}

# roverml_Terminate class attributes and methods

# roverml_Repeat class attributes and methods
roverml_Repeat_numberOfReps: Property = Property(name="numberOfReps", type=IntegerType)
roverml_Repeat.attributes={roverml_Repeat_numberOfReps}

# roverml_Triggered class attributes and methods
roverml_Triggered_operator: Property = Property(name="operator", type=StringType)
roverml_Triggered.attributes={roverml_Triggered_operator}

# Transition class attributes and methods

# roverml_Regular class attributes and methods

# roverml_DistanceSensorTrigger class attributes and methods
roverml_DistanceSensorTrigger_dist: Property = Property(name="dist", type=FloatType)
roverml_DistanceSensorTrigger.attributes={roverml_DistanceSensorTrigger_dist}

# Triggered class attributes and methods

# roverml_CompassTrigger class attributes and methods
roverml_CompassTrigger_angle: Property = Property(name="angle", type=IntegerType)
roverml_CompassTrigger.attributes={roverml_CompassTrigger_angle}

# roverml_Quantity class attributes and methods

# roverml_SingleQuantity class attributes and methods

# Quantity class attributes and methods

# SingleQuantity class attributes and methods

# Relationships
programs0: BinaryAssociation = BinaryAssociation(
    name="programs0",
    ends={
        Property(name="roverml_Program", type=roverml_System, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_System", type=roverml_Program, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rovers1: BinaryAssociation = BinaryAssociation(
    name="rovers1",
    ends={
        Property(name="roverml_Rover", type=roverml_System, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_System2", type=roverml_Rover, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components3: BinaryAssociation = BinaryAssociation(
    name="components3",
    ends={
        Property(name="roverml_Component", type=roverml_Rover, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_Rover4", type=roverml_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
roverExec5: BinaryAssociation = BinaryAssociation(
    name="roverExec5",
    ends={
        Property(name="roverml_Rover7", type=roverml_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_Program6", type=roverml_Rover, multiplicity=Multiplicity(0, 1))
    }
)
blocks8: BinaryAssociation = BinaryAssociation(
    name="blocks8",
    ends={
        Property(name="roverml_Block", type=roverml_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_Program9", type=roverml_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeUnit23: BinaryAssociation = BinaryAssociation(
    name="timeUnit23",
    ends={
        Property(name="roverml_Time", type=roverml_Wait, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_Wait", type=roverml_Time, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
transitions10: BinaryAssociation = BinaryAssociation(
    name="transitions10",
    ends={
        Property(name="roverml_Transition", type=roverml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_Block11", type=roverml_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commands12: BinaryAssociation = BinaryAssociation(
    name="commands12",
    ends={
        Property(name="roverml_Command", type=roverml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_Block13", type=roverml_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoingTransitions14: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions14",
    ends={
        Property(name="Transition", type=roverml_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=roverml_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransitions15: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions15",
    ends={
        Property(name="Transition16", type=roverml_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=roverml_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
components17: BinaryAssociation = BinaryAssociation(
    name="components17",
    ends={
        Property(name="roverml_Component19", type=roverml_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_Command18", type=roverml_Component, multiplicity=Multiplicity(0, 9999))
    }
)
source20: BinaryAssociation = BinaryAssociation(
    name="source20",
    ends={
        Property(name="Command", type=roverml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions", type=roverml_Command, multiplicity=Multiplicity(1, 1))
    }
)
target21: BinaryAssociation = BinaryAssociation(
    name="target21",
    ends={
        Property(name="Command22", type=roverml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=roverml_Command, multiplicity=Multiplicity(1, 1))
    }
)
compass36: BinaryAssociation = BinaryAssociation(
    name="compass36",
    ends={
        Property(name="roverml_Compass", type=roverml_CompassTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_CompassTrigger37", type=roverml_Compass, multiplicity=Multiplicity(0, 1))
    }
)
position38: BinaryAssociation = BinaryAssociation(
    name="position38",
    ends={
        Property(name="roverml_Position", type=roverml_GPSTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_GPSTrigger", type=roverml_Position, multiplicity=Multiplicity(0, 1))
    }
)
velocityUnits24: BinaryAssociation = BinaryAssociation(
    name="velocityUnits24",
    ends={
        Property(name="roverml_Velocity", type=roverml_Move, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_Move", type=roverml_Velocity, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lengthUnits25: BinaryAssociation = BinaryAssociation(
    name="lengthUnits25",
    ends={
        Property(name="roverml_Length", type=roverml_Move, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_Move26", type=roverml_Length, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
angleUnits27: BinaryAssociation = BinaryAssociation(
    name="angleUnits27",
    ends={
        Property(name="roverml_Angle", type=roverml_Rotate, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_Rotate", type=roverml_Angle, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
commands28: BinaryAssociation = BinaryAssociation(
    name="commands28",
    ends={
        Property(name="roverml_Command29", type=roverml_Repeat, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_Repeat", type=roverml_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
length30: BinaryAssociation = BinaryAssociation(
    name="length30",
    ends={
        Property(name="roverml_Length31", type=roverml_DistanceSensorTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_DistanceSensorTrigger", type=roverml_Length, multiplicity=Multiplicity(0, 1))
    }
)
distancesensor32: BinaryAssociation = BinaryAssociation(
    name="distancesensor32",
    ends={
        Property(name="roverml_DistanceSensor", type=roverml_DistanceSensorTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_DistanceSensorTrigger33", type=roverml_DistanceSensor, multiplicity=Multiplicity(0, 1))
    }
)
angles34: BinaryAssociation = BinaryAssociation(
    name="angles34",
    ends={
        Property(name="roverml_Angle35", type=roverml_CompassTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_CompassTrigger", type=roverml_Angle, multiplicity=Multiplicity(0, 1))
    }
)
gps39: BinaryAssociation = BinaryAssociation(
    name="gps39",
    ends={
        Property(name="roverml_GPS", type=roverml_GPSTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_GPSTrigger40", type=roverml_GPS, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_roverml_System_NamedElement = Generalization(general=NamedElement, specific=roverml_System)
gen_roverml_Rover_NamedElement = Generalization(general=NamedElement, specific=roverml_Rover)
gen_roverml_Sensor_Component = Generalization(general=Component, specific=roverml_Sensor)
gen_roverml_Actuator_Component = Generalization(general=Component, specific=roverml_Actuator)
gen_roverml_GPS_Sensor = Generalization(general=Sensor, specific=roverml_GPS)
gen_roverml_Compass_Sensor = Generalization(general=Sensor, specific=roverml_Compass)
gen_roverml_Program_NamedElement = Generalization(general=NamedElement, specific=roverml_Program)
gen_roverml_Component_NamedElement = Generalization(general=NamedElement, specific=roverml_Component)
gen_roverml_Move_Command = Generalization(general=Command, specific=roverml_Move)
gen_roverml_DistanceSensor_Sensor = Generalization(general=Sensor, specific=roverml_DistanceSensor)
gen_roverml_Motor_Actuator = Generalization(general=Actuator, specific=roverml_Motor)
gen_roverml_Light_Actuator = Generalization(general=Actuator, specific=roverml_Light)
gen_roverml_SetLightColor_Command = Generalization(general=Command, specific=roverml_SetLightColor)
gen_roverml_Wait_Command = Generalization(general=Command, specific=roverml_Wait)
gen_roverml_GPSTrigger_Triggered = Generalization(general=Triggered, specific=roverml_GPSTrigger)
gen_roverml_Rotate_Command = Generalization(general=Command, specific=roverml_Rotate)
gen_roverml_Terminate_Command = Generalization(general=Command, specific=roverml_Terminate)
gen_roverml_Repeat_Command = Generalization(general=Command, specific=roverml_Repeat)
gen_roverml_Triggered_Transition = Generalization(general=Transition, specific=roverml_Triggered)
gen_roverml_Regular_Transition = Generalization(general=Transition, specific=roverml_Regular)
gen_roverml_DistanceSensorTrigger_Triggered = Generalization(general=Triggered, specific=roverml_DistanceSensorTrigger)
gen_roverml_CompassTrigger_Triggered = Generalization(general=Triggered, specific=roverml_CompassTrigger)
gen_roverml_SingleQuantity_Quantity = Generalization(general=Quantity, specific=roverml_SingleQuantity)
gen_roverml_Position_Quantity = Generalization(general=Quantity, specific=roverml_Position)
gen_roverml_Time_SingleQuantity = Generalization(general=SingleQuantity, specific=roverml_Time)
gen_roverml_Velocity_SingleQuantity = Generalization(general=SingleQuantity, specific=roverml_Velocity)
gen_roverml_Length_SingleQuantity = Generalization(general=SingleQuantity, specific=roverml_Length)
gen_roverml_Angle_SingleQuantity = Generalization(general=SingleQuantity, specific=roverml_Angle)

# Domain Model
domain_model = DomainModel(
    name="roverml",
    types={roverml_System, NamedElement, roverml_Program, roverml_Rover, roverml_Component, roverml_Sensor, Component, roverml_Actuator, roverml_GPS, Sensor, roverml_Compass, roverml_Block, roverml_NamedElement, roverml_Time, roverml_Move, roverml_DistanceSensor, roverml_Motor, Actuator, roverml_Light, roverml_Transition, roverml_Command, roverml_SetLightColor, Command, roverml_Wait, roverml_GPSTrigger, roverml_Position, roverml_Velocity, roverml_Length, roverml_Rotate, roverml_Angle, roverml_Terminate, roverml_Repeat, roverml_Triggered, Transition, roverml_Regular, roverml_DistanceSensorTrigger, Triggered, roverml_CompassTrigger, roverml_Quantity, roverml_SingleQuantity, Quantity, SingleQuantity, TimeUnits, VelocityUnits, LengthUnits, AngleUnits, Colours},
    associations={programs0, rovers1, components3, roverExec5, blocks8, timeUnit23, transitions10, commands12, outgoingTransitions14, incomingTransitions15, components17, source20, target21, compass36, position38, velocityUnits24, lengthUnits25, angleUnits27, commands28, length30, distancesensor32, angles34, gps39},
    generalizations={gen_roverml_System_NamedElement, gen_roverml_Rover_NamedElement, gen_roverml_Sensor_Component, gen_roverml_Actuator_Component, gen_roverml_GPS_Sensor, gen_roverml_Compass_Sensor, gen_roverml_Program_NamedElement, gen_roverml_Component_NamedElement, gen_roverml_Move_Command, gen_roverml_DistanceSensor_Sensor, gen_roverml_Motor_Actuator, gen_roverml_Light_Actuator, gen_roverml_SetLightColor_Command, gen_roverml_Wait_Command, gen_roverml_GPSTrigger_Triggered, gen_roverml_Rotate_Command, gen_roverml_Terminate_Command, gen_roverml_Repeat_Command, gen_roverml_Triggered_Transition, gen_roverml_Regular_Transition, gen_roverml_DistanceSensorTrigger_Triggered, gen_roverml_CompassTrigger_Triggered, gen_roverml_SingleQuantity_Quantity, gen_roverml_Position_Quantity, gen_roverml_Time_SingleQuantity, gen_roverml_Velocity_SingleQuantity, gen_roverml_Length_SingleQuantity, gen_roverml_Angle_SingleQuantity},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)