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
Relay = Class(name="Relay")
Home_Security_System = Class(name="Home_Security_System")
Alert = Class(name="Alert")
Lamp = Class(name="Lamp")
MicroPhone = Class(name="MicroPhone")
Start_Of_Day = Class(name="Start_Of_Day")
End_Of_Day = Class(name="End_Of_Day")
HouseHolds = Class(name="HouseHolds")

# System class attributes and methods
System_Status: Property = Property(name="Status", type=BooleanType)
System_Update: Property = Property(name="Update", type=FloatType)
System.attributes={System_Update, System_Status}

# Relay class attributes and methods
Relay_SensorID: Property = Property(name="SensorID", type=IntegerType)
Relay_SensorType: Property = Property(name="SensorType", type=IntegerType)
Relay.attributes={Relay_SensorType, Relay_SensorID}

# Home_Security_System class attributes and methods
Home_Security_System_UserID: Property = Property(name="UserID", type=IntegerType)
Home_Security_System.attributes={Home_Security_System_UserID}

# Alert class attributes and methods
Alert_AlertID: Property = Property(name="AlertID", type=IntegerType)
Alert.attributes={Alert_AlertID}

# Lamp class attributes and methods
Lamp_LampID: Property = Property(name="LampID", type=IntegerType)
Lamp.attributes={Lamp_LampID}

# MicroPhone class attributes and methods
MicroPhone_MicID: Property = Property(name="MicID", type=StringType)
MicroPhone.attributes={MicroPhone_MicID}

# Start_Of_Day class attributes and methods
Start_Of_Day_SOT: Property = Property(name="SOT", type=IntegerType)
Start_Of_Day.attributes={Start_Of_Day_SOT}

# End_Of_Day class attributes and methods
End_Of_Day_EOT: Property = Property(name="EOT", type=IntegerType)
End_Of_Day.attributes={End_Of_Day_EOT}

# HouseHolds class attributes and methods
HouseHolds_TimeID: Property = Property(name="TimeID", type=StringType)
HouseHolds_LampLight: Property = Property(name="LampLight", type=StringType)
HouseHolds.attributes={HouseHolds_TimeID, HouseHolds_LampLight}

# Relationships
Sensor_Door: BinaryAssociation = BinaryAssociation(
    name="Sensor_Door",
    ends={
        Property(name="door0", type=Lamp, multiplicity=Multiplicity(1, 1)),
        Property(name="sensor1", type=Relay, multiplicity=Multiplicity(1, 1))
    }
)
HouseHolds_Start_Of_Day: BinaryAssociation = BinaryAssociation(
    name="HouseHolds_Start_Of_Day",
    ends={
        Property(name="start_Of_Day2", type=Start_Of_Day, multiplicity=Multiplicity(0, 1)),
        Property(name="houseHolds3", type=HouseHolds, multiplicity=Multiplicity(0, 1))
    }
)
HouseHolds_End_Of_Day: BinaryAssociation = BinaryAssociation(
    name="HouseHolds_End_Of_Day",
    ends={
        Property(name="end_Of_Day4", type=End_Of_Day, multiplicity=Multiplicity(0, 1)),
        Property(name="houseHolds5", type=HouseHolds, multiplicity=Multiplicity(0, 1))
    }
)
MicroPhone_System: BinaryAssociation = BinaryAssociation(
    name="MicroPhone_System",
    ends={
        Property(name="system6", type=System, multiplicity=Multiplicity(1, 1)),
        Property(name="microPhone7", type=MicroPhone, multiplicity=Multiplicity(1, 9999))
    }
)
Home_Security_System_Alert: BinaryAssociation = BinaryAssociation(
    name="Home_Security_System_Alert",
    ends={
        Property(name="alert8", type=Alert, multiplicity=Multiplicity(0, 1)),
        Property(name="home_Security_System9", type=Home_Security_System, multiplicity=Multiplicity(0, 1))
    }
)
Sensor_System: BinaryAssociation = BinaryAssociation(
    name="Sensor_System",
    ends={
        Property(name="system10", type=System, multiplicity=Multiplicity(1, 1)),
        Property(name="sensor11", type=Relay, multiplicity=Multiplicity(1, 9999))
    }
)
System_HouseHolds: BinaryAssociation = BinaryAssociation(
    name="System_HouseHolds",
    ends={
        Property(name="houseHolds12", type=HouseHolds, multiplicity=Multiplicity(0, 1)),
        Property(name="system13", type=System, multiplicity=Multiplicity(1, 1))
    }
)
Home_Security_System_System: BinaryAssociation = BinaryAssociation(
    name="Home_Security_System_System",
    ends={
        Property(name="system14", type=System, multiplicity=Multiplicity(1, 1)),
        Property(name="home_Security_System15", type=Home_Security_System, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_tzhGkP20EemrrdzmwAEMcA",
    types={System, Relay, Home_Security_System, Alert, Lamp, MicroPhone, Start_Of_Day, End_Of_Day, HouseHolds},
    associations={Sensor_Door, HouseHolds_Start_Of_Day, HouseHolds_End_Of_Day, MicroPhone_System, Home_Security_System_Alert, Sensor_System, System_HouseHolds, Home_Security_System_System},
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