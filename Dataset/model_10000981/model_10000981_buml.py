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
Door_Security = Class(name="Door_Security")
Camera_sensor = Class(name="Camera_sensor")
Event_Log = Class(name="Event_Log")
Light_PIR_Sensor = Class(name="Light_PIR_Sensor")
Lock_doors_sensors = Class(name="Lock_doors_sensors")

# Door_Security class attributes and methods

# Camera_sensor class attributes and methods
Camera_sensor_Image_ID: Property = Property(name="Image_ID", type=IntegerType)
Camera_sensor_Video_ID: Property = Property(name="Video_ID", type=IntegerType)
Camera_sensor.attributes={Camera_sensor_Video_ID, Camera_sensor_Image_ID}

# Event_Log class attributes and methods
Event_Log_attribute: Property = Property(name="attribute", type=StringType)
Event_Log.attributes={Event_Log_attribute}

# Light_PIR_Sensor class attributes and methods
Light_PIR_Sensor_attribute: Property = Property(name="attribute", type=StringType)
Light_PIR_Sensor.attributes={Light_PIR_Sensor_attribute}

# Lock_doors_sensors class attributes and methods
Lock_doors_sensors_attribute: Property = Property(name="attribute", type=StringType)
Lock_doors_sensors.attributes={Lock_doors_sensors_attribute}

# Relationships
Home_Security_Camera: BinaryAssociation = BinaryAssociation(
    name="Home_Security_Camera",
    ends={
        Property(name="camera0", type=Camera_sensor, multiplicity=Multiplicity(1, 9999)),
        Property(name="home_Security1", type=Door_Security, multiplicity=Multiplicity(1, 1))
    }
)
Home_Security_Event_Log: BinaryAssociation = BinaryAssociation(
    name="Home_Security_Event_Log",
    ends={
        Property(name="event_Log2", type=Event_Log, multiplicity=Multiplicity(1, 9999)),
        Property(name="home_Security3", type=Door_Security, multiplicity=Multiplicity(1, 1))
    }
)
Home_Security_Light_Sensor: BinaryAssociation = BinaryAssociation(
    name="Home_Security_Light_Sensor",
    ends={
        Property(name="light_Sensor4", type=Light_PIR_Sensor, multiplicity=Multiplicity(1, 9999)),
        Property(name="home_Security5", type=Door_Security, multiplicity=Multiplicity(1, 1))
    }
)
Home_Security_Doors: BinaryAssociation = BinaryAssociation(
    name="Home_Security_Doors",
    ends={
        Property(name="doors6", type=Lock_doors_sensors, multiplicity=Multiplicity(1, 1)),
        Property(name="home_Security7", type=Door_Security, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_77516aa5_4d28_41e8_ac43_fd11b25ba419",
    types={Door_Security, Camera_sensor, Event_Log, Light_PIR_Sensor, Lock_doors_sensors},
    associations={Home_Security_Camera, Home_Security_Event_Log, Home_Security_Light_Sensor, Home_Security_Doors},
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