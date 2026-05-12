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
Home_Security = Class(name="Home_Security")
Camera_sensor = Class(name="Camera_sensor")
Event_Log = Class(name="Event_Log")
Light_Sensor = Class(name="Light_Sensor")
Lock_doors_sensors = Class(name="Lock_doors_sensors")
Server = Class(name="Server")
Temperature_sensor = Class(name="Temperature_sensor")

# Home_Security class attributes and methods

# Camera_sensor class attributes and methods
Camera_sensor_Image_ID: Property = Property(name="Image_ID", type=IntegerType)
Camera_sensor_Video_ID: Property = Property(name="Video_ID", type=IntegerType)
Camera_sensor.attributes={Camera_sensor_Video_ID, Camera_sensor_Image_ID}

# Event_Log class attributes and methods
Event_Log_attribute: Property = Property(name="attribute", type=StringType)
Event_Log.attributes={Event_Log_attribute}

# Light_Sensor class attributes and methods
Light_Sensor_attribute: Property = Property(name="attribute", type=StringType)
Light_Sensor.attributes={Light_Sensor_attribute}

# Lock_doors_sensors class attributes and methods
Lock_doors_sensors_attribute: Property = Property(name="attribute", type=StringType)
Lock_doors_sensors.attributes={Lock_doors_sensors_attribute}

# Server class attributes and methods
Server_attribute: Property = Property(name="attribute", type=StringType)
Server.attributes={Server_attribute}

# Temperature_sensor class attributes and methods
Temperature_sensor_attribute: Property = Property(name="attribute", type=StringType)
Temperature_sensor.attributes={Temperature_sensor_attribute}

# Relationships
Home_Security_Event_Log: BinaryAssociation = BinaryAssociation(
    name="Home_Security_Event_Log",
    ends={
        Property(name="event_Log4", type=Event_Log, multiplicity=Multiplicity(1, 9999)),
        Property(name="home_Security5", type=Home_Security, multiplicity=Multiplicity(1, 1))
    }
)
Home_Security_Light_Sensor: BinaryAssociation = BinaryAssociation(
    name="Home_Security_Light_Sensor",
    ends={
        Property(name="light_Sensor6", type=Light_Sensor, multiplicity=Multiplicity(1, 9999)),
        Property(name="home_Security7", type=Home_Security, multiplicity=Multiplicity(1, 1))
    }
)
Home_Security_Server: BinaryAssociation = BinaryAssociation(
    name="Home_Security_Server",
    ends={
        Property(name="server0", type=Server, multiplicity=Multiplicity(1, 1)),
        Property(name="home_Security1", type=Home_Security, multiplicity=Multiplicity(1, 1))
    }
)
Home_Security_Camera: BinaryAssociation = BinaryAssociation(
    name="Home_Security_Camera",
    ends={
        Property(name="camera2", type=Camera_sensor, multiplicity=Multiplicity(1, 9999)),
        Property(name="home_Security3", type=Home_Security, multiplicity=Multiplicity(1, 1))
    }
)
Home_Security_Doors: BinaryAssociation = BinaryAssociation(
    name="Home_Security_Doors",
    ends={
        Property(name="doors8", type=Lock_doors_sensors, multiplicity=Multiplicity(1, 1)),
        Property(name="home_Security9", type=Home_Security, multiplicity=Multiplicity(1, 1))
    }
)
Home_Security_Temperature_sensor: BinaryAssociation = BinaryAssociation(
    name="Home_Security_Temperature_sensor",
    ends={
        Property(name="temperature_sensor10", type=Temperature_sensor, multiplicity=Multiplicity(1, 9999)),
        Property(name="home_Security11", type=Home_Security, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="f0b8335e_c46d_4f92_8dfb_332f9de2e0b0",
    types={Home_Security, Camera_sensor, Event_Log, Light_Sensor, Lock_doors_sensors, Server, Temperature_sensor},
    associations={Home_Security_Event_Log, Home_Security_Light_Sensor, Home_Security_Server, Home_Security_Camera, Home_Security_Doors, Home_Security_Temperature_sensor},
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