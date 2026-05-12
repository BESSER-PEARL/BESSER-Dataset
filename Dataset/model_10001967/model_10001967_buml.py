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
Home_Security__Hub_ = Class(name="Home_Security__Hub_")
Camera_1 = Class(name="Camera_1")
Event_Log = Class(name="Event_Log")
Light_Sensor = Class(name="Light_Sensor")
Lock_doors = Class(name="Lock_doors")
Security_logs = Class(name="Security_logs")
Temperature_sensor = Class(name="Temperature_sensor")
Dispatch_drown = Class(name="Dispatch_drown")
T = Class(name="T")
Motion_Sensor = Class(name="Motion_Sensor")

# Home_Security__Hub_ class attributes and methods
Home_Security__Hub__Sensor_ID: Property = Property(name="Sensor_ID", type=StringType)
Home_Security__Hub__Camera_ID: Property = Property(name="Camera_ID", type=StringType)
Home_Security__Hub__Hub_ID: Property = Property(name="Hub_ID", type=StringType)
Home_Security__Hub__Login_ID: Property = Property(name="Login_ID", type=StringType)
Home_Security__Hub_.attributes={Home_Security__Hub__Login_ID, Home_Security__Hub__Sensor_ID, Home_Security__Hub__Camera_ID, Home_Security__Hub__Hub_ID}

# Camera_1 class attributes and methods
Camera_1_Camera_ID: Property = Property(name="Camera_ID", type=StringType)
Camera_1_Sensor_ID: Property = Property(name="Sensor_ID", type=StringType)
Camera_1.attributes={Camera_1_Sensor_ID, Camera_1_Camera_ID}

# Event_Log class attributes and methods
Event_Log_Status: Property = Property(name="Status", type=BooleanType)
Event_Log.attributes={Event_Log_Status}

# Light_Sensor class attributes and methods
Light_Sensor_Sensor_ID: Property = Property(name="Sensor_ID", type=StringType)
Light_Sensor.attributes={Light_Sensor_Sensor_ID}

# Lock_doors class attributes and methods
Lock_doors_Door_ID: Property = Property(name="Door_ID", type=StringType)
Lock_doors.attributes={Lock_doors_Door_ID}

# Security_logs class attributes and methods
Security_logs_Log_ID: Property = Property(name="Log_ID", type=StringType)
Security_logs_Sensor_ID: Property = Property(name="Sensor_ID", type=StringType)
Security_logs_Camera_ID: Property = Property(name="Camera_ID", type=StringType)
Security_logs.attributes={Security_logs_Camera_ID, Security_logs_Sensor_ID, Security_logs_Log_ID}

# Temperature_sensor class attributes and methods
Temperature_sensor_Temp_ID: Property = Property(name="Temp_ID", type=StringType)
Temperature_sensor.attributes={Temperature_sensor_Temp_ID}

# Dispatch_drown class attributes and methods
Dispatch_drown_Drown_ID: Property = Property(name="Drown_ID", type=StringType)
Dispatch_drown_Camera_ID: Property = Property(name="Camera_ID", type=StringType)
Dispatch_drown.attributes={Dispatch_drown_Drown_ID, Dispatch_drown_Camera_ID}

# T class attributes and methods

# Motion_Sensor class attributes and methods
Motion_Sensor_Sensor_ID: Property = Property(name="Sensor_ID", type=StringType)
Motion_Sensor.attributes={Motion_Sensor_Sensor_ID}

# Relationships
Home_Security_Server: BinaryAssociation = BinaryAssociation(
    name="Home_Security_Server",
    ends={
        Property(name="server0", type=Security_logs, multiplicity=Multiplicity(1, 1)),
        Property(name="home_Security1", type=Home_Security__Hub_, multiplicity=Multiplicity(1, 1))
    }
)
Home_Security_Camera: BinaryAssociation = BinaryAssociation(
    name="Home_Security_Camera",
    ends={
        Property(name="camera2", type=Camera_1, multiplicity=Multiplicity(1, 9999)),
        Property(name="home_Security3", type=Home_Security__Hub_, multiplicity=Multiplicity(1, 1))
    }
)
Home_Security_Event_Log: BinaryAssociation = BinaryAssociation(
    name="Home_Security_Event_Log",
    ends={
        Property(name="event_Log4", type=Event_Log, multiplicity=Multiplicity(1, 9999)),
        Property(name="home_Security5", type=Home_Security__Hub_, multiplicity=Multiplicity(1, 1))
    }
)
Home_Security_Light_Sensor: BinaryAssociation = BinaryAssociation(
    name="Home_Security_Light_Sensor",
    ends={
        Property(name="light_Sensor6", type=Light_Sensor, multiplicity=Multiplicity(1, 9999)),
        Property(name="home_Security7", type=Camera_1, multiplicity=Multiplicity(1, 1))
    }
)
Home_Security_Doors: BinaryAssociation = BinaryAssociation(
    name="Home_Security_Doors",
    ends={
        Property(name="doors8", type=Lock_doors, multiplicity=Multiplicity(1, 1)),
        Property(name="home_Security9", type=Home_Security__Hub_, multiplicity=Multiplicity(1, 1))
    }
)
Home_Security_Temperature_sensor: BinaryAssociation = BinaryAssociation(
    name="Home_Security_Temperature_sensor",
    ends={
        Property(name="temperature_sensor10", type=Temperature_sensor, multiplicity=Multiplicity(1, 9999)),
        Property(name="home_Security11", type=Camera_1, multiplicity=Multiplicity(1, 1))
    }
)
Camera_1_Camera_1: BinaryAssociation = BinaryAssociation(
    name="Camera_1_Camera_1",
    ends={
        Property(name="camera_112", type=Camera_1, multiplicity=Multiplicity(0, 1)),
        Property(name="camera_113", type=Camera_1, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_gJRfwFV6EeqK2M3E1LfZ7Q",
    types={Home_Security__Hub_, Camera_1, Event_Log, Light_Sensor, Lock_doors, Security_logs, Temperature_sensor, Dispatch_drown, T, Motion_Sensor},
    associations={Home_Security_Server, Home_Security_Camera, Home_Security_Event_Log, Home_Security_Light_Sensor, Home_Security_Doors, Home_Security_Temperature_sensor, Camera_1_Camera_1},
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