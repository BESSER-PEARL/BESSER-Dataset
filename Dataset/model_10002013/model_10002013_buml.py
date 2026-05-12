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
Firebase = Class(name="Firebase")
Sensor = Class(name="Sensor")
Gas_Smoke_Sensor = Class(name="Gas_Smoke_Sensor")
Temperature_Sensor = Class(name="Temperature_Sensor")
PressureSensor = Class(name="PressureSensor")
Mobile_App = Class(name="Mobile_App")
Alert = Class(name="Alert")
Count_people = Class(name="Count_people")
Arduino = Class(name="Arduino")
Web = Class(name="Web")
Alert2 = Class(name="Alert2")

# Firebase class attributes and methods
Firebase_Status: Property = Property(name="Status", type=BooleanType)
Firebase_Update: Property = Property(name="Update", type=FloatType)
Firebase.attributes={Firebase_Status, Firebase_Update}

# Sensor class attributes and methods
Sensor_SensorID: Property = Property(name="SensorID", type=IntegerType)
Sensor_SensorType: Property = Property(name="SensorType", type=IntegerType)
Sensor.attributes={Sensor_SensorID, Sensor_SensorType}

# Gas_Smoke_Sensor class attributes and methods
Gas_Smoke_Sensor_SmokeAlarm: Property = Property(name="SmokeAlarm", type=BooleanType)
Gas_Smoke_Sensor_DispenseSprinkler: Property = Property(name="DispenseSprinkler", type=BooleanType)
Gas_Smoke_Sensor.attributes={Gas_Smoke_Sensor_DispenseSprinkler, Gas_Smoke_Sensor_SmokeAlarm}

# Temperature_Sensor class attributes and methods

# PressureSensor class attributes and methods

# Mobile_App class attributes and methods
Mobile_App_UserID: Property = Property(name="UserID", type=IntegerType)
Mobile_App.attributes={Mobile_App_UserID}

# Alert class attributes and methods
Alert_AlertID: Property = Property(name="AlertID", type=IntegerType)
Alert.attributes={Alert_AlertID}

# Count_people class attributes and methods
Count_people__attr: Property = Property(name="_attr", type=IntegerType)
Count_people.attributes={Count_people__attr}

# Arduino class attributes and methods
Arduino_MicID: Property = Property(name="MicID", type=StringType)
Arduino.attributes={Arduino_MicID}

# Web class attributes and methods

# Alert2 class attributes and methods
Alert2_AlertID: Property = Property(name="AlertID", type=IntegerType)
Alert2.attributes={Alert2_AlertID}

# Relationships
Sensor_Door: BinaryAssociation = BinaryAssociation(
    name="Sensor_Door",
    ends={
        Property(name="door0", type=Count_people, multiplicity=Multiplicity(1, 1)),
        Property(name="sensor1", type=Sensor, multiplicity=Multiplicity(1, 1))
    }
)
Home_Security_System_Alert: BinaryAssociation = BinaryAssociation(
    name="Home_Security_System_Alert",
    ends={
        Property(name="alert2", type=Alert, multiplicity=Multiplicity(0, 1)),
        Property(name="home_Security_System3", type=Mobile_App, multiplicity=Multiplicity(0, 1))
    }
)
Sensor_System: BinaryAssociation = BinaryAssociation(
    name="Sensor_System",
    ends={
        Property(name="system4", type=Arduino, multiplicity=Multiplicity(1, 1)),
        Property(name="sensor5", type=Sensor, multiplicity=Multiplicity(1, 9999))
    }
)
Home_Security_System_System: BinaryAssociation = BinaryAssociation(
    name="Home_Security_System_System",
    ends={
        Property(name="system6", type=Firebase, multiplicity=Multiplicity(1, 1)),
        Property(name="home_Security_System7", type=Mobile_App, multiplicity=Multiplicity(1, 1))
    }
)
Arduino__Firebase: BinaryAssociation = BinaryAssociation(
    name="Arduino__Firebase",
    ends={
        Property(name="Arduino__Firebase_08", type=Firebase, multiplicity=Multiplicity(1, 1)),
        Property(name="Arduino__Firebase_19", type=Arduino, multiplicity=Multiplicity(1, 1))
    }
)
Firebase_Web: BinaryAssociation = BinaryAssociation(
    name="Firebase_Web",
    ends={
        Property(name="web10", type=Web, multiplicity=Multiplicity(0, 1)),
        Property(name="firebase11", type=Firebase, multiplicity=Multiplicity(0, 1))
    }
)
Alert2_Web: BinaryAssociation = BinaryAssociation(
    name="Alert2_Web",
    ends={
        Property(name="web12", type=Web, multiplicity=Multiplicity(0, 1)),
        Property(name="alert213", type=Alert2, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_jWHPEPVaEemTHo7LQdQL6Q",
    types={Firebase, Sensor, Gas_Smoke_Sensor, Temperature_Sensor, PressureSensor, Mobile_App, Alert, Count_people, Arduino, Web, Alert2},
    associations={Sensor_Door, Home_Security_System_Alert, Sensor_System, Home_Security_System_System, Arduino__Firebase, Firebase_Web, Alert2_Web},
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