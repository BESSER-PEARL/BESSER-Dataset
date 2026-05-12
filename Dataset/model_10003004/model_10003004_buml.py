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
Gateway = Class(name="Gateway")
Alarm = Class(name="Alarm")
Datalog = Class(name="Datalog")
Sensor = Class(name="Sensor")
FireAlarm_Sensor = Class(name="FireAlarm_Sensor")
Factory_Security_System = Class(name="Factory_Security_System")
Alert = Class(name="Alert")
Door_relay = Class(name="Door_relay")
Modbus_Meter = Class(name="Modbus_Meter")
Start_Of_Day = Class(name="Start_Of_Day")
End_Of_Day = Class(name="End_Of_Day")
OPC_UA = Class(name="OPC_UA")
UPS_SNMP = Class(name="UPS_SNMP")
FactoryHolds = Class(name="FactoryHolds")
MQTT_Broker = Class(name="MQTT_Broker")
Gateway2_Interface = Class(name="Gateway2_Interface")
Gateway_01_Interface = Class(name="Gateway_01_Interface")

# Gateway class attributes and methods
Gateway_Status: Property = Property(name="Status", type=Gateway_01_Interface)
Gateway_Update: Property = Property(name="Update", type=FloatType)
Gateway_WebPLC_configure: Property = Property(name="WebPLC_configure", type=Gateway_01_Interface)
Gateway.attributes={Gateway_WebPLC_configure, Gateway_Status, Gateway_Update}

# Alarm class attributes and methods

# Datalog class attributes and methods

# Sensor class attributes and methods
Sensor_SensorID: Property = Property(name="SensorID", type=IntegerType)
Sensor_SensorType: Property = Property(name="SensorType", type=IntegerType)
Sensor.attributes={Sensor_SensorType, Sensor_SensorID}

# FireAlarm_Sensor class attributes and methods
FireAlarm_Sensor_SmokeAlarm: Property = Property(name="SmokeAlarm", type=BooleanType)
FireAlarm_Sensor_DispenseSprinkler: Property = Property(name="DispenseSprinkler", type=BooleanType)
FireAlarm_Sensor.attributes={FireAlarm_Sensor_SmokeAlarm, FireAlarm_Sensor_DispenseSprinkler}

# Factory_Security_System class attributes and methods
Factory_Security_System_UserID: Property = Property(name="UserID", type=IntegerType)
Factory_Security_System.attributes={Factory_Security_System_UserID}

# Alert class attributes and methods
Alert_AlertID: Property = Property(name="AlertID", type=IntegerType)
Alert.attributes={Alert_AlertID}

# Door_relay class attributes and methods
Door_relay_DoorID: Property = Property(name="DoorID", type=IntegerType)
Door_relay_DoorOpen: Property = Property(name="DoorOpen", type=StringType)
Door_relay.attributes={Door_relay_DoorID, Door_relay_DoorOpen}

# Modbus_Meter class attributes and methods
Modbus_Meter_MAC_ID: Property = Property(name="MAC_ID", type=IntegerType)
Modbus_Meter.attributes={Modbus_Meter_MAC_ID}

# Start_Of_Day class attributes and methods
Start_Of_Day_SOT: Property = Property(name="SOT", type=IntegerType)
Start_Of_Day.attributes={Start_Of_Day_SOT}

# End_Of_Day class attributes and methods
End_Of_Day_EOT: Property = Property(name="EOT", type=IntegerType)
End_Of_Day.attributes={End_Of_Day_EOT}

# OPC_UA class attributes and methods
OPC_UA_PC_ID: Property = Property(name="PC_ID", type=IntegerType)
OPC_UA.attributes={OPC_UA_PC_ID}

# UPS_SNMP class attributes and methods
UPS_SNMP_IP: Property = Property(name="IP", type=StringType)
UPS_SNMP.attributes={UPS_SNMP_IP}

# FactoryHolds class attributes and methods
FactoryHolds_Time: Property = Property(name="Time", type=FloatType)
FactoryHolds_Control_panel: Property = Property(name="Control_panel", type=StringType)
FactoryHolds_Alarm: Property = Property(name="Alarm", type=StringType)
FactoryHolds_Conveyor1: Property = Property(name="Conveyor1", type=StringType)
FactoryHolds_Conveyor2: Property = Property(name="Conveyor2", type=StringType)
FactoryHolds.attributes={FactoryHolds_Control_panel, FactoryHolds_Alarm, FactoryHolds_Time, FactoryHolds_Conveyor2, FactoryHolds_Conveyor1}

# MQTT_Broker class attributes and methods
MQTT_Broker_DeviceID: Property = Property(name="DeviceID", type=IntegerType)
MQTT_Broker_Publish: Property = Property(name="Publish", type=StringType)
MQTT_Broker_Subscribe: Property = Property(name="Subscribe", type=StringType)
MQTT_Broker.attributes={MQTT_Broker_Subscribe, MQTT_Broker_DeviceID, MQTT_Broker_Publish}

# Gateway2_Interface class attributes and methods

# Gateway_01_Interface class attributes and methods

# Relationships
Factory_Security_System_Alert: BinaryAssociation = BinaryAssociation(
    name="Factory_Security_System_Alert",
    ends={
        Property(name="alert0", type=Alert, multiplicity=Multiplicity(0, 1)),
        Property(name="home_Security_System1", type=Factory_Security_System, multiplicity=Multiplicity(0, 1))
    }
)
System_FactoryHolds: BinaryAssociation = BinaryAssociation(
    name="System_FactoryHolds",
    ends={
        Property(name="system5", type=Gateway, multiplicity=Multiplicity(1, 1)),
        Property(name="houseHolds4", type=FactoryHolds, multiplicity=Multiplicity(0, 1))
    }
)
Factory_Security_System_System: BinaryAssociation = BinaryAssociation(
    name="Factory_Security_System_System",
    ends={
        Property(name="system6", type=Gateway, multiplicity=Multiplicity(1, 1)),
        Property(name="Factory_Security_System7", type=Factory_Security_System, multiplicity=Multiplicity(1, 1))
    }
)
Start_Of_Day_Gateway: BinaryAssociation = BinaryAssociation(
    name="Start_Of_Day_Gateway",
    ends={
        Property(name="gateway8", type=Gateway, multiplicity=Multiplicity(0, 1)),
        Property(name="start_Of_Day9", type=Start_Of_Day, multiplicity=Multiplicity(0, 1))
    }
)
End_Of_Day_Gateway: BinaryAssociation = BinaryAssociation(
    name="End_Of_Day_Gateway",
    ends={
        Property(name="gateway10", type=Gateway, multiplicity=Multiplicity(0, 1)),
        Property(name="end_Of_Day11", type=End_Of_Day, multiplicity=Multiplicity(0, 1))
    }
)
Sensor_System: BinaryAssociation = BinaryAssociation(
    name="Sensor_System",
    ends={
        Property(name="system2", type=Gateway, multiplicity=Multiplicity(1, 1)),
        Property(name="sensor3", type=Sensor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="f4591cea_ef88_4a68_9bdb_04a35b09bd34",
    types={Gateway, Alarm, Datalog, Sensor, FireAlarm_Sensor, Factory_Security_System, Alert, Door_relay, Modbus_Meter, Start_Of_Day, End_Of_Day, OPC_UA, UPS_SNMP, FactoryHolds, MQTT_Broker, Gateway2_Interface, Gateway_01_Interface},
    associations={Factory_Security_System_Alert, System_FactoryHolds, Factory_Security_System_System, Start_Of_Day_Gateway, End_Of_Day_Gateway, Sensor_System},
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