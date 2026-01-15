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
Operator: Enumeration = Enumeration(
    name="Operator",
    literals={
            EnumerationLiteral(name="INFERIOR"),
			EnumerationLiteral(name="SUPERIOR"),
			EnumerationLiteral(name="EQUALS")
    }
)

DurationUnit: Enumeration = Enumeration(
    name="DurationUnit",
    literals={
            EnumerationLiteral(name="MINUTE"),
			EnumerationLiteral(name="SECOND")
    }
)

# Classes
smartHome_SmartHome = Class(name="smartHome::SmartHome")
smartHome_Rule = Class(name="smartHome::Rule")
smartHome_Condition = Class(name="smartHome::Condition")
smartHome_Event = Class(name="smartHome::Event")
smartHome_Duration = Class(name="smartHome::Duration")
smartHome_Sensor = Class(name="smartHome::Sensor")
smartHome_SensorType = Class(name="smartHome::SensorType")
smartHome_Location = Class(name="smartHome::Location")
smartHome_SensorValue = Class(name="smartHome::SensorValue")

# smartHome_SmartHome class attributes and methods

# smartHome_Rule class attributes and methods

# smartHome_Condition class attributes and methods
smartHome_Condition_operand: Property = Property(name="operand", type=IntegerType)
smartHome_Condition_operator: Property = Property(name="operator", type=StringType)
smartHome_Condition.attributes={smartHome_Condition_operand, smartHome_Condition_operator}

# smartHome_Event class attributes and methods
smartHome_Event_description: Property = Property(name="description", type=StringType)
smartHome_Event.attributes={smartHome_Event_description}

# smartHome_Duration class attributes and methods
smartHome_Duration_unit: Property = Property(name="unit", type=StringType)
smartHome_Duration_value: Property = Property(name="value", type=IntegerType)
smartHome_Duration.attributes={smartHome_Duration_unit, smartHome_Duration_value}

# smartHome_Sensor class attributes and methods
smartHome_Sensor_dataFile: Property = Property(name="dataFile", type=StringType)
smartHome_Sensor_name: Property = Property(name="name", type=StringType)
smartHome_Sensor_value: Property = Property(name="value", type=IntegerType)
smartHome_Sensor.attributes={smartHome_Sensor_value, smartHome_Sensor_name, smartHome_Sensor_dataFile}

# smartHome_SensorType class attributes and methods
smartHome_SensorType_name: Property = Property(name="name", type=StringType)
smartHome_SensorType.attributes={smartHome_SensorType_name}

# smartHome_Location class attributes and methods
smartHome_Location_name: Property = Property(name="name", type=StringType)
smartHome_Location.attributes={smartHome_Location_name}

# smartHome_SensorValue class attributes and methods

# Relationships
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
        Property(name="smartHome_Sensor18", type=smartHome_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="smartHome_Condition17", type=smartHome_Sensor, multiplicity=Multiplicity(1, 1))
    }
)
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

# Domain Model
domain_model = DomainModel(
    name="smartHome",
    types={smartHome_SmartHome, smartHome_Rule, smartHome_Condition, smartHome_Event, smartHome_Duration, smartHome_Sensor, smartHome_SensorType, smartHome_Location, smartHome_SensorValue, Operator, DurationUnit},
    associations={locations3, sensorTypes5, rules8, conditions10, event12, duration14, sensor16, sensorType0, sensors1},
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