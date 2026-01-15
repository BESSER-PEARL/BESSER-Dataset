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
TouchSensorSides: Enumeration = Enumeration(
    name="TouchSensorSides",
    literals={
            EnumerationLiteral(name="LEFT"),
			EnumerationLiteral(name="RIGHT"),
			EnumerationLiteral(name="BOTH")
    }
)

Actions: Enumeration = Enumeration(
    name="Actions",
    literals={
            EnumerationLiteral(name="DRIVE_BACKWARD"),
			EnumerationLiteral(name="ROTATE_L"),
			EnumerationLiteral(name="ROTATE_R"),
			EnumerationLiteral(name="DRIVE_FORWARD"),
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
            EnumerationLiteral(name="N"),
			EnumerationLiteral(name="NE"),
			EnumerationLiteral(name="E"),
			EnumerationLiteral(name="SE"),
			EnumerationLiteral(name="S"),
			EnumerationLiteral(name="SW"),
			EnumerationLiteral(name="W"),
			EnumerationLiteral(name="NW")
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

# Classes
dsl_Mission = Class(name="dsl::Mission")
dsl_Task = Class(name="dsl::Task")
dsl_SensorType = Class(name="dsl::SensorType")
dsl_Ignorables = Class(name="dsl::Ignorables")
dsl_ColorSensor = Class(name="dsl::ColorSensor")
SensorType = Class(name="SensorType")
dsl_TouchSensor = Class(name="dsl::TouchSensor")
dsl_UltrasonicSensor = Class(name="dsl::UltrasonicSensor")

# dsl_Mission class attributes and methods

# dsl_Task class attributes and methods
dsl_Task_name: Property = Property(name="name", type=StringType)
dsl_Task_action: Property = Property(name="action", type=StringType)
dsl_Task_ignoreBehavior: Property = Property(name="ignoreBehavior", type=BooleanType)
dsl_Task.attributes={dsl_Task_action, dsl_Task_ignoreBehavior, dsl_Task_name}

# dsl_SensorType class attributes and methods

# dsl_Ignorables class attributes and methods
dsl_Ignorables_AVOID_OBJECTS: Property = Property(name="AVOID_OBJECTS", type=StringType)
dsl_Ignorables.attributes={dsl_Ignorables_AVOID_OBJECTS}

# dsl_ColorSensor class attributes and methods
dsl_ColorSensor_key: Property = Property(name="key", type=StringType)
dsl_ColorSensor.attributes={dsl_ColorSensor_key}

# SensorType class attributes and methods

# dsl_TouchSensor class attributes and methods
dsl_TouchSensor_key: Property = Property(name="key", type=StringType)
dsl_TouchSensor.attributes={dsl_TouchSensor_key}

# dsl_UltrasonicSensor class attributes and methods
dsl_UltrasonicSensor_comparator: Property = Property(name="comparator", type=StringType)
dsl_UltrasonicSensor_distance: Property = Property(name="distance", type=StringType)
dsl_UltrasonicSensor.attributes={dsl_UltrasonicSensor_distance, dsl_UltrasonicSensor_comparator}

# Relationships
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

# Generalizations
gen_dsl_ColorSensor_SensorType = Generalization(general=SensorType, specific=dsl_ColorSensor)
gen_dsl_TouchSensor_SensorType = Generalization(general=SensorType, specific=dsl_TouchSensor)
gen_dsl_UltrasonicSensor_SensorType = Generalization(general=SensorType, specific=dsl_UltrasonicSensor)

# Domain Model
domain_model = DomainModel(
    name="dsl",
    types={dsl_Mission, dsl_Task, dsl_SensorType, dsl_Ignorables, dsl_ColorSensor, SensorType, dsl_TouchSensor, dsl_UltrasonicSensor, TouchSensorSides, Actions, Directions, Colors, CompareOperator},
    associations={tasks0, sensor1},
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