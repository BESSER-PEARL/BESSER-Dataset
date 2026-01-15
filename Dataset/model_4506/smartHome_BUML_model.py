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
IntegerOperator: Enumeration = Enumeration(
    name="IntegerOperator",
    literals={
            EnumerationLiteral(name="INFERIOR"),
			EnumerationLiteral(name="SUPERIOR"),
			EnumerationLiteral(name="EQUALS")
    }
)

BooleanOperator: Enumeration = Enumeration(
    name="BooleanOperator",
    literals={
            EnumerationLiteral(name="IS"),
			EnumerationLiteral(name="IS_NOT")
    }
)

DurationUnit: Enumeration = Enumeration(
    name="DurationUnit",
    literals={
            EnumerationLiteral(name="SECOND"),
			EnumerationLiteral(name="MINUTE")
    }
)

# Classes
smartHome_Sensor = Class(name="smartHome::Sensor", is_abstract=True)
smartHome_SensorType = Class(name="smartHome::SensorType")
smartHome_IntegerSensor = Class(name="smartHome::IntegerSensor")
Sensor = Class(name="Sensor")
smartHome_BooleanSensor = Class(name="smartHome::BooleanSensor")
smartHome_Location = Class(name="smartHome::Location")
smartHome_AnalogSensorType = Class(name="smartHome::AnalogSensorType")
SensorType = Class(name="SensorType")
smartHome_BooleanSensorType = Class(name="smartHome::BooleanSensorType")
smartHome_SmartHome = Class(name="smartHome::SmartHome")
smartHome_Rule = Class(name="smartHome::Rule")
smartHome_Condition = Class(name="smartHome::Condition", is_abstract=True)
smartHome_Event = Class(name="smartHome::Event")
smartHome_Duration = Class(name="smartHome::Duration")
smartHome_BooleanCondition = Class(name="smartHome::BooleanCondition")
Condition = Class(name="Condition")
smartHome_IntegerCondition = Class(name="smartHome::IntegerCondition")

# smartHome_Sensor class attributes and methods
smartHome_Sensor_dataFile: Property = Property(name="dataFile", type=StringType)
smartHome_Sensor_name: Property = Property(name="name", type=StringType)
smartHome_Sensor.attributes={smartHome_Sensor_name, smartHome_Sensor_dataFile}

# smartHome_SensorType class attributes and methods
smartHome_SensorType_name: Property = Property(name="name", type=StringType)
smartHome_SensorType.attributes={smartHome_SensorType_name}

# smartHome_IntegerSensor class attributes and methods
smartHome_IntegerSensor_value: Property = Property(name="value", type=IntegerType)
smartHome_IntegerSensor.attributes={smartHome_IntegerSensor_value}

# Sensor class attributes and methods

# smartHome_BooleanSensor class attributes and methods
smartHome_BooleanSensor_value: Property = Property(name="value", type=BooleanType)
smartHome_BooleanSensor.attributes={smartHome_BooleanSensor_value}

# smartHome_Location class attributes and methods
smartHome_Location_name: Property = Property(name="name", type=StringType)
smartHome_Location.attributes={smartHome_Location_name}

# smartHome_AnalogSensorType class attributes and methods

# SensorType class attributes and methods

# smartHome_BooleanSensorType class attributes and methods

# smartHome_SmartHome class attributes and methods

# smartHome_Rule class attributes and methods

# smartHome_Condition class attributes and methods

# smartHome_Event class attributes and methods
smartHome_Event_description: Property = Property(name="description", type=StringType)
smartHome_Event.attributes={smartHome_Event_description}

# smartHome_Duration class attributes and methods
smartHome_Duration_unit: Property = Property(name="unit", type=StringType)
smartHome_Duration_value: Property = Property(name="value", type=IntegerType)
smartHome_Duration.attributes={smartHome_Duration_unit, smartHome_Duration_value}

# smartHome_BooleanCondition class attributes and methods
smartHome_BooleanCondition_operand: Property = Property(name="operand", type=BooleanType)
smartHome_BooleanCondition_operator: Property = Property(name="operator", type=StringType)
smartHome_BooleanCondition.attributes={smartHome_BooleanCondition_operand, smartHome_BooleanCondition_operator}

# Condition class attributes and methods

# smartHome_IntegerCondition class attributes and methods
smartHome_IntegerCondition_operand: Property = Property(name="operand", type=IntegerType)
smartHome_IntegerCondition_operator: Property = Property(name="operator", type=StringType)
smartHome_IntegerCondition.attributes={smartHome_IntegerCondition_operand, smartHome_IntegerCondition_operator}

# Relationships
sensorType0: BinaryAssociation = BinaryAssociation(
    name="sensorType0",
    ends={
        Property(name="smartHome_SensorType", type=smartHome_Sensor, multiplicity=Multiplicity(1, 1)),
        Property(name="smartHome_Sensor", type=smartHome_SensorType, multiplicity=Multiplicity(1, 1))
    }
)
sensors1: BinaryAssociation = BinaryAssociation(
    name="sensors1",
    ends={
        Property(name="smartHome_Sensor2", type=smartHome_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="smartHome_Location", type=smartHome_Sensor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locations3: BinaryAssociation = BinaryAssociation(
    name="locations3",
    ends={
        Property(name="smartHome_Location4", type=smartHome_SmartHome, multiplicity=Multiplicity(1, 1)),
        Property(name="smartHome_SmartHome", type=smartHome_Location, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
sensorTypes5: BinaryAssociation = BinaryAssociation(
    name="sensorTypes5",
    ends={
        Property(name="smartHome_SensorType7", type=smartHome_SmartHome, multiplicity=Multiplicity(1, 1)),
        Property(name="smartHome_SmartHome6", type=smartHome_SensorType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
rules8: BinaryAssociation = BinaryAssociation(
    name="rules8",
    ends={
        Property(name="smartHome_Rule", type=smartHome_SmartHome, multiplicity=Multiplicity(1, 1)),
        Property(name="smartHome_SmartHome9", type=smartHome_Rule, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
conditions10: BinaryAssociation = BinaryAssociation(
    name="conditions10",
    ends={
        Property(name="smartHome_Condition", type=smartHome_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="smartHome_Rule11", type=smartHome_Condition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
event12: BinaryAssociation = BinaryAssociation(
    name="event12",
    ends={
        Property(name="smartHome_Event", type=smartHome_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="smartHome_Rule13", type=smartHome_Event, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
duration14: BinaryAssociation = BinaryAssociation(
    name="duration14",
    ends={
        Property(name="smartHome_Duration", type=smartHome_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="smartHome_Rule15", type=smartHome_Duration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sensor16: BinaryAssociation = BinaryAssociation(
    name="sensor16",
    ends={
        Property(name="smartHome_BooleanSensor", type=smartHome_BooleanCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="smartHome_BooleanCondition", type=smartHome_BooleanSensor, multiplicity=Multiplicity(1, 1))
    }
)
sensor17: BinaryAssociation = BinaryAssociation(
    name="sensor17",
    ends={
        Property(name="smartHome_IntegerSensor", type=smartHome_IntegerCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="smartHome_IntegerCondition", type=smartHome_IntegerSensor, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_smartHome_IntegerSensor_Sensor = Generalization(general=Sensor, specific=smartHome_IntegerSensor)
gen_smartHome_BooleanSensor_Sensor = Generalization(general=Sensor, specific=smartHome_BooleanSensor)
gen_smartHome_AnalogSensorType_SensorType = Generalization(general=SensorType, specific=smartHome_AnalogSensorType)
gen_smartHome_BooleanSensorType_SensorType = Generalization(general=SensorType, specific=smartHome_BooleanSensorType)
gen_smartHome_BooleanCondition_Condition = Generalization(general=Condition, specific=smartHome_BooleanCondition)
gen_smartHome_IntegerCondition_Condition = Generalization(general=Condition, specific=smartHome_IntegerCondition)

# Domain Model
domain_model = DomainModel(
    name="smartHome",
    types={smartHome_Sensor, smartHome_SensorType, smartHome_IntegerSensor, Sensor, smartHome_BooleanSensor, smartHome_Location, smartHome_AnalogSensorType, SensorType, smartHome_BooleanSensorType, smartHome_SmartHome, smartHome_Rule, smartHome_Condition, smartHome_Event, smartHome_Duration, smartHome_BooleanCondition, Condition, smartHome_IntegerCondition, IntegerOperator, BooleanOperator, DurationUnit},
    associations={sensorType0, sensors1, locations3, sensorTypes5, rules8, conditions10, event12, duration14, sensor16, sensor17},
    generalizations={gen_smartHome_IntegerSensor_Sensor, gen_smartHome_BooleanSensor_Sensor, gen_smartHome_AnalogSensorType_SensorType, gen_smartHome_BooleanSensorType_SensorType, gen_smartHome_BooleanCondition_Condition, gen_smartHome_IntegerCondition_Condition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)