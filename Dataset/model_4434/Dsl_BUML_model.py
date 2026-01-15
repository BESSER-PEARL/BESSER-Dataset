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
timeUnit: Enumeration = Enumeration(
    name="timeUnit",
    literals={
            EnumerationLiteral(name="SECONDS"),
			EnumerationLiteral(name="MILISECONDS")
    }
)

Colors: Enumeration = Enumeration(
    name="Colors",
    literals={
            EnumerationLiteral(name="BLACK"),
			EnumerationLiteral(name="BLUE"),
			EnumerationLiteral(name="CYAN"),
			EnumerationLiteral(name="DARK_GRAY"),
			EnumerationLiteral(name="GRAY"),
			EnumerationLiteral(name="GREEN"),
			EnumerationLiteral(name="LIGHT_GRAY"),
			EnumerationLiteral(name="MAGENTA"),
			EnumerationLiteral(name="ORANGE"),
			EnumerationLiteral(name="PINK"),
			EnumerationLiteral(name="RED"),
			EnumerationLiteral(name="WHITE"),
			EnumerationLiteral(name="YELLOW")
    }
)

CompareOperator: Enumeration = Enumeration(
    name="CompareOperator",
    literals={
            EnumerationLiteral(name="EQ"),
			EnumerationLiteral(name="NEQ"),
			EnumerationLiteral(name="GEQ"),
			EnumerationLiteral(name="G"),
			EnumerationLiteral(name="LEQ"),
			EnumerationLiteral(name="L")
    }
)

TouchSensorSides: Enumeration = Enumeration(
    name="TouchSensorSides",
    literals={
            EnumerationLiteral(name="LEFT"),
			EnumerationLiteral(name="RIGHT"),
			EnumerationLiteral(name="BOTH"),
			EnumerationLiteral(name="ANY")
    }
)

Actions: Enumeration = Enumeration(
    name="Actions",
    literals={
            EnumerationLiteral(name="ROTATE_L"),
			EnumerationLiteral(name="ROTATE_R"),
			EnumerationLiteral(name="DRIVE_FORWARD"),
			EnumerationLiteral(name="DRIVE_BACKWARD"),
			EnumerationLiteral(name="STOP_DRIVING"),
			EnumerationLiteral(name="TURN_AROUND"),
			EnumerationLiteral(name="BEEP"),
			EnumerationLiteral(name="MEASURE"),
			EnumerationLiteral(name="DRIVETOEDGE")
    }
)

Directions: Enumeration = Enumeration(
    name="Directions",
    literals={
            EnumerationLiteral(name="SW"),
			EnumerationLiteral(name="W"),
			EnumerationLiteral(name="NW"),
			EnumerationLiteral(name="N"),
			EnumerationLiteral(name="NE"),
			EnumerationLiteral(name="E"),
			EnumerationLiteral(name="SE"),
			EnumerationLiteral(name="S")
    }
)

# Classes
dsl_Ignorables = Class(name="dsl::Ignorables")
dsl_timeUnitValue = Class(name="dsl::timeUnitValue")
dsl_ColorSensor = Class(name="dsl::ColorSensor")
SensorType = Class(name="SensorType")
dsl_ColorValue = Class(name="dsl::ColorValue")
dsl_Mission = Class(name="dsl::Mission")
dsl_Task = Class(name="dsl::Task")
dsl_SensorType = Class(name="dsl::SensorType")
dsl_TouchSensor = Class(name="dsl::TouchSensor")
dsl_UltrasonicSensor = Class(name="dsl::UltrasonicSensor")

# dsl_Ignorables class attributes and methods
dsl_Ignorables_AVOID_OBJECTS: Property = Property(name="AVOID_OBJECTS", type=StringType)
dsl_Ignorables.attributes={dsl_Ignorables_AVOID_OBJECTS}

# dsl_timeUnitValue class attributes and methods
dsl_timeUnitValue_unit: Property = Property(name="unit", type=StringType)
dsl_timeUnitValue.attributes={dsl_timeUnitValue_unit}

# dsl_ColorSensor class attributes and methods
dsl_ColorSensor_distinct: Property = Property(name="distinct", type=BooleanType)
dsl_ColorSensor.attributes={dsl_ColorSensor_distinct}

# SensorType class attributes and methods

# dsl_ColorValue class attributes and methods
dsl_ColorValue_color: Property = Property(name="color", type=StringType)
dsl_ColorValue.attributes={dsl_ColorValue_color}

# dsl_Mission class attributes and methods

# dsl_Task class attributes and methods
dsl_Task_action: Property = Property(name="action", type=StringType)
dsl_Task_nrOfTimes: Property = Property(name="nrOfTimes", type=IntegerType)
dsl_Task_time: Property = Property(name="time", type=IntegerType)
dsl_Task_name: Property = Property(name="name", type=StringType)
dsl_Task.attributes={dsl_Task_name, dsl_Task_nrOfTimes, dsl_Task_time, dsl_Task_action}

# dsl_SensorType class attributes and methods

# dsl_TouchSensor class attributes and methods
dsl_TouchSensor_key: Property = Property(name="key", type=StringType)
dsl_TouchSensor.attributes={dsl_TouchSensor_key}

# dsl_UltrasonicSensor class attributes and methods
dsl_UltrasonicSensor_comparator: Property = Property(name="comparator", type=StringType)
dsl_UltrasonicSensor_distance: Property = Property(name="distance", type=StringType)
dsl_UltrasonicSensor.attributes={dsl_UltrasonicSensor_comparator, dsl_UltrasonicSensor_distance}

# Relationships
ignoreBehavior3: BinaryAssociation = BinaryAssociation(
    name="ignoreBehavior3",
    ends={
        Property(name="dsl_Ignorables", type=dsl_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Task4", type=dsl_Ignorables, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timeunit5: BinaryAssociation = BinaryAssociation(
    name="timeunit5",
    ends={
        Property(name="dsl_timeUnitValue", type=dsl_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Task6", type=dsl_timeUnitValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
key7: BinaryAssociation = BinaryAssociation(
    name="key7",
    ends={
        Property(name="dsl_ColorValue", type=dsl_ColorSensor, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ColorSensor", type=dsl_ColorValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tasks0: BinaryAssociation = BinaryAssociation(
    name="tasks0",
    ends={
        Property(name="dsl_Task", type=dsl_Mission, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Mission", type=dsl_Task, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sensor1: BinaryAssociation = BinaryAssociation(
    name="sensor1",
    ends={
        Property(name="dsl_SensorType", type=dsl_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Task2", type=dsl_SensorType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
keys8: BinaryAssociation = BinaryAssociation(
    name="keys8",
    ends={
        Property(name="dsl_ColorValue10", type=dsl_ColorSensor, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ColorSensor9", type=dsl_ColorValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_dsl_ColorSensor_SensorType = Generalization(general=SensorType, specific=dsl_ColorSensor)
gen_dsl_TouchSensor_SensorType = Generalization(general=SensorType, specific=dsl_TouchSensor)
gen_dsl_UltrasonicSensor_SensorType = Generalization(general=SensorType, specific=dsl_UltrasonicSensor)

# Domain Model
domain_model = DomainModel(
    name="dsl",
    types={dsl_Ignorables, dsl_timeUnitValue, dsl_ColorSensor, SensorType, dsl_ColorValue, dsl_Mission, dsl_Task, dsl_SensorType, dsl_TouchSensor, dsl_UltrasonicSensor, timeUnit, Colors, CompareOperator, TouchSensorSides, Actions, Directions},
    associations={ignoreBehavior3, timeunit5, key7, tasks0, sensor1, keys8},
    generalizations={gen_dsl_ColorSensor_SensorType, gen_dsl_TouchSensor_SensorType, gen_dsl_UltrasonicSensor_SensorType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)