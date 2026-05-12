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
System = Class(name="System")
Sensor = Class(name="Sensor")
FireAlarm_Sensor = Class(name="FireAlarm_Sensor")
Home_Security_System = Class(name="Home_Security_System")
Alert = Class(name="Alert")
MicroPhone = Class(name="MicroPhone")
Light = Class(name="Light")
HouseHolds = Class(name="HouseHolds")
FAN = Class(name="FAN")
Control_Box = Class(name="Control_Box")
Fan_Regulator_Box = Class(name="Fan_Regulator_Box")

# System class attributes and methods
System_Status: Property = Property(name="Status", type=BooleanType)
System_Update: Property = Property(name="Update", type=FloatType)
System.attributes={System_Status, System_Update}

# Sensor class attributes and methods
Sensor_SensorID: Property = Property(name="SensorID", type=IntegerType)
Sensor_SensorType: Property = Property(name="SensorType", type=IntegerType)
Sensor.attributes={Sensor_SensorID, Sensor_SensorType}

# FireAlarm_Sensor class attributes and methods
FireAlarm_Sensor_SmokeAlarm: Property = Property(name="SmokeAlarm", type=BooleanType)
FireAlarm_Sensor_DispenseSprinkler: Property = Property(name="DispenseSprinkler", type=BooleanType)
FireAlarm_Sensor.attributes={FireAlarm_Sensor_SmokeAlarm, FireAlarm_Sensor_DispenseSprinkler}

# Home_Security_System class attributes and methods
Home_Security_System_UserID: Property = Property(name="UserID", type=IntegerType)
Home_Security_System.attributes={Home_Security_System_UserID}

# Alert class attributes and methods
Alert_AlertID: Property = Property(name="AlertID", type=IntegerType)
Alert.attributes={Alert_AlertID}

# MicroPhone class attributes and methods
MicroPhone_MicID: Property = Property(name="MicID", type=StringType)
MicroPhone.attributes={MicroPhone_MicID}

# Light class attributes and methods
Light_LightID: Property = Property(name="LightID", type=StringType)
Light.attributes={Light_LightID}

# HouseHolds class attributes and methods
HouseHolds_TimeID: Property = Property(name="TimeID", type=StringType)
HouseHolds_Alarm: Property = Property(name="Alarm", type=StringType)
HouseHolds_WashingMachine: Property = Property(name="WashingMachine", type=StringType)
HouseHolds.attributes={HouseHolds_WashingMachine, HouseHolds_Alarm, HouseHolds_TimeID}

# FAN class attributes and methods
FAN_FAN_ID: Property = Property(name="FAN_ID", type=StringType)
FAN.attributes={FAN_FAN_ID}

# Control_Box class attributes and methods
Control_Box_Status: Property = Property(name="Status", type=BooleanType)
Control_Box_Update: Property = Property(name="Update", type=FloatType)
Control_Box.attributes={Control_Box_Status, Control_Box_Update}

# Fan_Regulator_Box class attributes and methods
Fan_Regulator_Box_FAN_ID: Property = Property(name="FAN_ID", type=StringType)
Fan_Regulator_Box.attributes={Fan_Regulator_Box_FAN_ID}

# Relationships
MicroPhone_System: BinaryAssociation = BinaryAssociation(
    name="MicroPhone_System",
    ends={
        Property(name="system0", type=System, multiplicity=Multiplicity(1, 1)),
        Property(name="microPhone1", type=MicroPhone, multiplicity=Multiplicity(1, 9999))
    }
)
Home_Security_System_Alert: BinaryAssociation = BinaryAssociation(
    name="Home_Security_System_Alert",
    ends={
        Property(name="alert2", type=Alert, multiplicity=Multiplicity(0, 1)),
        Property(name="home_Security_System3", type=Home_Security_System, multiplicity=Multiplicity(0, 1))
    }
)
System_HouseHolds: BinaryAssociation = BinaryAssociation(
    name="System_HouseHolds",
    ends={
        Property(name="houseHolds4", type=HouseHolds, multiplicity=Multiplicity(0, 1)),
        Property(name="system5", type=System, multiplicity=Multiplicity(1, 1))
    }
)
Home_Security_System_System: BinaryAssociation = BinaryAssociation(
    name="Home_Security_System_System",
    ends={
        Property(name="system6", type=System, multiplicity=Multiplicity(1, 1)),
        Property(name="home_Security_System7", type=Home_Security_System, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_58XScNk7EemDUejBZMo4Qg",
    types={System, Sensor, FireAlarm_Sensor, Home_Security_System, Alert, MicroPhone, Light, HouseHolds, FAN, Control_Box, Fan_Regulator_Box},
    associations={MicroPhone_System, Home_Security_System_Alert, System_HouseHolds, Home_Security_System_System},
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