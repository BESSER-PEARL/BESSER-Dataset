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
Color: Enumeration = Enumeration(
    name="Color",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="red"),
			EnumerationLiteral(name="green"),
			EnumerationLiteral(name="blue"),
			EnumerationLiteral(name="yellow")
    }
)

TimeUnit: Enumeration = Enumeration(
    name="TimeUnit",
    literals={
            EnumerationLiteral(name="ns"),
			EnumerationLiteral(name="ms"),
			EnumerationLiteral(name="s"),
			EnumerationLiteral(name="min"),
			EnumerationLiteral(name="h")
    }
)

AngleUnit: Enumeration = Enumeration(
    name="AngleUnit",
    literals={
            EnumerationLiteral(name="radian"),
			EnumerationLiteral(name="degree")
    }
)

VelocityUnit: Enumeration = Enumeration(
    name="VelocityUnit",
    literals={
            EnumerationLiteral(name="mm_per_s"),
			EnumerationLiteral(name="cm_per_s")
    }
)

LengthUnit: Enumeration = Enumeration(
    name="LengthUnit",
    literals={
            EnumerationLiteral(name="mm"),
			EnumerationLiteral(name="cm"),
			EnumerationLiteral(name="m")
    }
)

ComparisonOperator: Enumeration = Enumeration(
    name="ComparisonOperator",
    literals={
            EnumerationLiteral(name="smaller"),
			EnumerationLiteral(name="equals"),
			EnumerationLiteral(name="greater"),
			EnumerationLiteral(name="unequal")
    }
)

# Classes
roverml_NamedElement = Class(name="roverml::NamedElement", is_abstract=True)
roverml_RoverProgram = Class(name="roverml::RoverProgram")
NamedElement = Class(name="NamedElement")
roverml_Block = Class(name="roverml::Block")
roverml_Rover = Class(name="roverml::Rover")
roverml_Command = Class(name="roverml::Command", is_abstract=True)
roverml_Transition = Class(name="roverml::Transition")
roverml_Move = Class(name="roverml::Move")
Command = Class(name="Command")
roverml_Velocity = Class(name="roverml::Velocity")
roverml_Length = Class(name="roverml::Length")
roverml_SetLightColor = Class(name="roverml::SetLightColor")
roverml_Time = Class(name="roverml::Time")
roverml_Repeat = Class(name="roverml::Repeat")
Block = Class(name="Block")
roverml_Component = Class(name="roverml::Component", is_abstract=True)
roverml_Light = Class(name="roverml::Light")
roverml_Rotate = Class(name="roverml::Rotate")
roverml_Angle = Class(name="roverml::Angle")
roverml_Wait = Class(name="roverml::Wait")
roverml_GPS = Class(name="roverml::GPS")
roverml_DistanceSensor = Class(name="roverml::DistanceSensor")
roverml_Compass = Class(name="roverml::Compass")
roverml_SingleQuantity = Class(name="roverml::SingleQuantity", is_abstract=True)
Quantity = Class(name="Quantity")
SingleQuantity = Class(name="SingleQuantity")
Actuator = Class(name="Actuator")
roverml_TriggeredTransition = Class(name="roverml::TriggeredTransition", is_abstract=True)
Transition = Class(name="Transition")
roverml_Motor = Class(name="roverml::Motor")
roverml_Terminate = Class(name="roverml::Terminate")
roverml_Actuator = Class(name="roverml::Actuator", is_abstract=True)
roverml_RoverSystem = Class(name="roverml::RoverSystem")
roverml_DistanceSensorTrigger = Class(name="roverml::DistanceSensorTrigger")
roverml_GpsTrigger = Class(name="roverml::GpsTrigger")
roverml_CompassTrigger = Class(name="roverml::CompassTrigger")
roverml_Quantity = Class(name="roverml::Quantity", is_abstract=True)
roverml_Position = Class(name="roverml::Position")
roverml_Sensor = Class(name="roverml::Sensor", is_abstract=True)
Component = Class(name="Component")

# roverml_NamedElement class attributes and methods
roverml_NamedElement_name: Property = Property(name="name", type=StringType)
roverml_NamedElement.attributes={roverml_NamedElement_name}

# roverml_RoverProgram class attributes and methods

# NamedElement class attributes and methods

# roverml_Block class attributes and methods

# roverml_Rover class attributes and methods

# roverml_Command class attributes and methods

# roverml_Transition class attributes and methods

# roverml_Move class attributes and methods

# Command class attributes and methods

# roverml_Velocity class attributes and methods
roverml_Velocity_velocityUnit: Property = Property(name="velocityUnit", type=StringType)
roverml_Velocity.attributes={roverml_Velocity_velocityUnit}

# roverml_Length class attributes and methods
roverml_Length_lengthUnit: Property = Property(name="lengthUnit", type=StringType)
roverml_Length.attributes={roverml_Length_lengthUnit}

# roverml_SetLightColor class attributes and methods
roverml_SetLightColor_color: Property = Property(name="color", type=StringType)
roverml_SetLightColor.attributes={roverml_SetLightColor_color}

# roverml_Time class attributes and methods
roverml_Time_timeUnit: Property = Property(name="timeUnit", type=StringType)
roverml_Time.attributes={roverml_Time_timeUnit}

# roverml_Repeat class attributes and methods
roverml_Repeat_count: Property = Property(name="count", type=IntegerType)
roverml_Repeat.attributes={roverml_Repeat_count}

# Block class attributes and methods

# roverml_Component class attributes and methods
roverml_Component_kind: Property = Property(name="kind", type=StringType)
roverml_Component.attributes={roverml_Component_kind}

# roverml_Light class attributes and methods

# roverml_Rotate class attributes and methods

# roverml_Angle class attributes and methods
roverml_Angle_angleUnit: Property = Property(name="angleUnit", type=StringType)
roverml_Angle.attributes={roverml_Angle_angleUnit}

# roverml_Wait class attributes and methods

# roverml_GPS class attributes and methods

# roverml_DistanceSensor class attributes and methods

# roverml_Compass class attributes and methods

# roverml_SingleQuantity class attributes and methods
roverml_SingleQuantity_value: Property = Property(name="value", type=FloatType)
roverml_SingleQuantity.attributes={roverml_SingleQuantity_value}

# Quantity class attributes and methods

# SingleQuantity class attributes and methods

# Actuator class attributes and methods

# roverml_TriggeredTransition class attributes and methods
roverml_TriggeredTransition_operator: Property = Property(name="operator", type=StringType)
roverml_TriggeredTransition.attributes={roverml_TriggeredTransition_operator}

# Transition class attributes and methods

# roverml_Motor class attributes and methods

# roverml_Terminate class attributes and methods

# roverml_Actuator class attributes and methods

# roverml_RoverSystem class attributes and methods

# roverml_DistanceSensorTrigger class attributes and methods

# roverml_GpsTrigger class attributes and methods

# roverml_CompassTrigger class attributes and methods

# roverml_Quantity class attributes and methods

# roverml_Position class attributes and methods

# roverml_Sensor class attributes and methods

# Component class attributes and methods

# Relationships
block0: BinaryAssociation = BinaryAssociation(
    name="block0",
    ends={
        Property(name="roverml_Block", type=roverml_RoverProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_RoverProgram", type=roverml_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rover1: BinaryAssociation = BinaryAssociation(
    name="rover1",
    ends={
        Property(name="roverml_Rover", type=roverml_RoverProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_RoverProgram2", type=roverml_Rover, multiplicity=Multiplicity(1, 1))
    }
)
incoming3: BinaryAssociation = BinaryAssociation(
    name="incoming3",
    ends={
        Property(name="roverml_Transition", type=roverml_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_Command", type=roverml_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing4: BinaryAssociation = BinaryAssociation(
    name="outgoing4",
    ends={
        Property(name="roverml_Transition6", type=roverml_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_Command5", type=roverml_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
speed7: BinaryAssociation = BinaryAssociation(
    name="speed7",
    ends={
        Property(name="roverml_Velocity", type=roverml_Move, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_Move", type=roverml_Velocity, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
distance8: BinaryAssociation = BinaryAssociation(
    name="distance8",
    ends={
        Property(name="roverml_Length", type=roverml_Move, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_Move9", type=roverml_Length, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duration12: BinaryAssociation = BinaryAssociation(
    name="duration12",
    ends={
        Property(name="roverml_Time", type=roverml_Wait, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_Wait", type=roverml_Time, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
components13: BinaryAssociation = BinaryAssociation(
    name="components13",
    ends={
        Property(name="roverml_Component", type=roverml_Rover, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_Rover14", type=roverml_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commands15: BinaryAssociation = BinaryAssociation(
    name="commands15",
    ends={
        Property(name="roverml_Command17", type=roverml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_Block16", type=roverml_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions18: BinaryAssociation = BinaryAssociation(
    name="transitions18",
    ends={
        Property(name="roverml_Transition20", type=roverml_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_Block19", type=roverml_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source21: BinaryAssociation = BinaryAssociation(
    name="source21",
    ends={
        Property(name="roverml_Command23", type=roverml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_Transition22", type=roverml_Command, multiplicity=Multiplicity(1, 1))
    }
)
target24: BinaryAssociation = BinaryAssociation(
    name="target24",
    ends={
        Property(name="roverml_Command26", type=roverml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_Transition25", type=roverml_Command, multiplicity=Multiplicity(1, 1))
    }
)
lights10: BinaryAssociation = BinaryAssociation(
    name="lights10",
    ends={
        Property(name="roverml_Light", type=roverml_SetLightColor, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_SetLightColor", type=roverml_Light, multiplicity=Multiplicity(1, 9999))
    }
)
angle11: BinaryAssociation = BinaryAssociation(
    name="angle11",
    ends={
        Property(name="roverml_Angle", type=roverml_Rotate, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_Rotate", type=roverml_Angle, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rovers27: BinaryAssociation = BinaryAssociation(
    name="rovers27",
    ends={
        Property(name="roverml_Rover28", type=roverml_RoverSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_RoverSystem", type=roverml_Rover, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
roverPrograms29: BinaryAssociation = BinaryAssociation(
    name="roverPrograms29",
    ends={
        Property(name="roverml_RoverProgram31", type=roverml_RoverSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_RoverSystem30", type=roverml_RoverProgram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
x32: BinaryAssociation = BinaryAssociation(
    name="x32",
    ends={
        Property(name="roverml_Length33", type=roverml_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_Position", type=roverml_Length, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
y34: BinaryAssociation = BinaryAssociation(
    name="y34",
    ends={
        Property(name="roverml_Length36", type=roverml_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="roverml_Position35", type=roverml_Length, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_roverml_RoverProgram_NamedElement = Generalization(general=NamedElement, specific=roverml_RoverProgram)
gen_roverml_Command_NamedElement = Generalization(general=NamedElement, specific=roverml_Command)
gen_roverml_Move_Command = Generalization(general=Command, specific=roverml_Move)
gen_roverml_SetLightColor_Command = Generalization(general=Command, specific=roverml_SetLightColor)
gen_roverml_Repeat_Command = Generalization(general=Command, specific=roverml_Repeat)
gen_roverml_Repeat_Block = Generalization(general=Block, specific=roverml_Repeat)
gen_roverml_Rover_NamedElement = Generalization(general=NamedElement, specific=roverml_Rover)
gen_roverml_Transition_NamedElement = Generalization(general=NamedElement, specific=roverml_Transition)
gen_roverml_Rotate_Command = Generalization(general=Command, specific=roverml_Rotate)
gen_roverml_Wait_Command = Generalization(general=Command, specific=roverml_Wait)
gen_roverml_SingleQuantity_Quantity = Generalization(general=Quantity, specific=roverml_SingleQuantity)
gen_roverml_Time_SingleQuantity = Generalization(general=SingleQuantity, specific=roverml_Time)
gen_roverml_Angle_SingleQuantity = Generalization(general=SingleQuantity, specific=roverml_Angle)
gen_roverml_Velocity_SingleQuantity = Generalization(general=SingleQuantity, specific=roverml_Velocity)
gen_roverml_Light_Actuator = Generalization(general=Actuator, specific=roverml_Light)
gen_roverml_Length_SingleQuantity = Generalization(general=SingleQuantity, specific=roverml_Length)
gen_roverml_TriggeredTransition_Transition = Generalization(general=Transition, specific=roverml_TriggeredTransition)
gen_roverml_Motor_Actuator = Generalization(general=Actuator, specific=roverml_Motor)
gen_roverml_Terminate_Command = Generalization(general=Command, specific=roverml_Terminate)
gen_roverml_Component_NamedElement = Generalization(general=NamedElement, specific=roverml_Component)
gen_roverml_Actuator_Component = Generalization(general=Component, specific=roverml_Actuator)
gen_roverml_Position_Quantity = Generalization(general=Quantity, specific=roverml_Position)
gen_roverml_Sensor_Component = Generalization(general=Component, specific=roverml_Sensor)

# Domain Model
domain_model = DomainModel(
    name="roverml",
    types={roverml_NamedElement, roverml_RoverProgram, NamedElement, roverml_Block, roverml_Rover, roverml_Command, roverml_Transition, roverml_Move, Command, roverml_Velocity, roverml_Length, roverml_SetLightColor, roverml_Time, roverml_Repeat, Block, roverml_Component, roverml_Light, roverml_Rotate, roverml_Angle, roverml_Wait, roverml_GPS, roverml_DistanceSensor, roverml_Compass, roverml_SingleQuantity, Quantity, SingleQuantity, Actuator, roverml_TriggeredTransition, Transition, roverml_Motor, roverml_Terminate, roverml_Actuator, roverml_RoverSystem, roverml_DistanceSensorTrigger, roverml_GpsTrigger, roverml_CompassTrigger, roverml_Quantity, roverml_Position, roverml_Sensor, Component, Color, TimeUnit, AngleUnit, VelocityUnit, LengthUnit, ComparisonOperator},
    associations={block0, rover1, incoming3, outgoing4, speed7, distance8, duration12, components13, commands15, transitions18, source21, target24, lights10, angle11, rovers27, roverPrograms29, x32, y34},
    generalizations={gen_roverml_RoverProgram_NamedElement, gen_roverml_Command_NamedElement, gen_roverml_Move_Command, gen_roverml_SetLightColor_Command, gen_roverml_Repeat_Command, gen_roverml_Repeat_Block, gen_roverml_Rover_NamedElement, gen_roverml_Transition_NamedElement, gen_roverml_Rotate_Command, gen_roverml_Wait_Command, gen_roverml_SingleQuantity_Quantity, gen_roverml_Time_SingleQuantity, gen_roverml_Angle_SingleQuantity, gen_roverml_Velocity_SingleQuantity, gen_roverml_Light_Actuator, gen_roverml_Length_SingleQuantity, gen_roverml_TriggeredTransition_Transition, gen_roverml_Motor_Actuator, gen_roverml_Terminate_Command, gen_roverml_Component_NamedElement, gen_roverml_Actuator_Component, gen_roverml_Position_Quantity, gen_roverml_Sensor_Component},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)