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
SAFE_HOME_SYSTEM = Class(name="SAFE_HOME_SYSTEM")
config = Class(name="config")
securitySystem = Class(name="securitySystem")
Device_Configuration = Class(name="Device_Configuration")
Automation_System = Class(name="Automation_System")
Sensor = Class(name="Sensor")
Alarm_Signaler = Class(name="Alarm_Signaler")
Camera = Class(name="Camera")
Telephone_Answering_machine = Class(name="Telephone_Answering_machine")
Lights = Class(name="Lights")
HeatAirConditioning = Class(name="HeatAirConditioning")
Home_Entertainment_Devices = Class(name="Home_Entertainment_Devices")
Television = Class(name="Television")
Home_Theatre = Class(name="Home_Theatre")
ActivationCode = Class(name="ActivationCode")
FloorPlan = Class(name="FloorPlan")
Segment = Class(name="Segment")
FloorCoordinates = Class(name="FloorCoordinates")

# SAFE_HOME_SYSTEM class attributes and methods
SAFE_HOME_SYSTEM_userId: Property = Property(name="userId", type=StringType)
SAFE_HOME_SYSTEM_masterPwd: Property = Property(name="masterPwd", type=StringType)
SAFE_HOME_SYSTEM_streetAddress: Property = Property(name="streetAddress", type=StringType)
SAFE_HOME_SYSTEM_activationState: Property = Property(name="activationState", type=StringType)
SAFE_HOME_SYSTEM.attributes={SAFE_HOME_SYSTEM_activationState, SAFE_HOME_SYSTEM_masterPwd, SAFE_HOME_SYSTEM_userId, SAFE_HOME_SYSTEM_streetAddress}

# config class attributes and methods
config_configurationName: Property = Property(name="configurationName", type=StringType)
config.attributes={config_configurationName}

# securitySystem class attributes and methods

# Device_Configuration class attributes and methods
Device_Configuration_zone: Property = Property(name="zone", type=IntegerType)
Device_Configuration_activeOnStay: Property = Property(name="activeOnStay", type=BooleanType)
Device_Configuration_activeOnAway: Property = Property(name="activeOnAway", type=BooleanType)
Device_Configuration_alarmIfoff: Property = Property(name="alarmIfoff", type=BooleanType)
Device_Configuration.attributes={Device_Configuration_alarmIfoff, Device_Configuration_activeOnAway, Device_Configuration_activeOnStay, Device_Configuration_zone}

# Automation_System class attributes and methods

# Sensor class attributes and methods
Sensor_detectingAnomaly: Property = Property(name="detectingAnomaly", type=BooleanType)
Sensor.attributes={Sensor_detectingAnomaly}

# Alarm_Signaler class attributes and methods
Alarm_Signaler_frequency: Property = Property(name="frequency", type=IntegerType)
Alarm_Signaler.attributes={Alarm_Signaler_frequency}

# Camera class attributes and methods
Camera_panAngle: Property = Property(name="panAngle", type=IntegerType)
Camera_zoomSetting: Property = Property(name="zoomSetting", type=IntegerType)
Camera.attributes={Camera_zoomSetting, Camera_panAngle}

# Telephone_Answering_machine class attributes and methods
Telephone_Answering_machine_number: Property = Property(name="number", type=IntegerType)
Telephone_Answering_machine.attributes={Telephone_Answering_machine_number}

# Lights class attributes and methods
Lights_brightness: Property = Property(name="brightness", type=IntegerType)
Lights.attributes={Lights_brightness}

# HeatAirConditioning class attributes and methods
HeatAirConditioning_voltage: Property = Property(name="voltage", type=IntegerType)
HeatAirConditioning.attributes={HeatAirConditioning_voltage}

# Home_Entertainment_Devices class attributes and methods

# Television class attributes and methods
Television_companyName: Property = Property(name="companyName", type=StringType)
Television.attributes={Television_companyName}

# Home_Theatre class attributes and methods
Home_Theatre_companyName: Property = Property(name="companyName", type=StringType)
Home_Theatre.attributes={Home_Theatre_companyName}

# ActivationCode class attributes and methods
ActivationCode_code: Property = Property(name="code", type=IntegerType)
ActivationCode.attributes={ActivationCode_code}

# FloorPlan class attributes and methods
FloorPlan_floorName: Property = Property(name="floorName", type=StringType)
FloorPlan.attributes={FloorPlan_floorName}

# Segment class attributes and methods

# FloorCoordinates class attributes and methods
FloorCoordinates_XcoordinatePosition: Property = Property(name="XcoordinatePosition", type=IntegerType)
FloorCoordinates_YcoordinatePosition: Property = Property(name="YcoordinatePosition", type=IntegerType)
FloorCoordinates.attributes={FloorCoordinates_XcoordinatePosition, FloorCoordinates_YcoordinatePosition}

# Relationships
config_ActivationCode: BinaryAssociation = BinaryAssociation(
    name="config_ActivationCode",
    ends={
        Property(name="activationCode0", type=ActivationCode, multiplicity=Multiplicity(0, 1)),
        Property(name="config1", type=config, multiplicity=Multiplicity(0, 1))
    }
)
config_FloorPlan: BinaryAssociation = BinaryAssociation(
    name="config_FloorPlan",
    ends={
        Property(name="floorPlan2", type=FloorPlan, multiplicity=Multiplicity(0, 1)),
        Property(name="config3", type=config, multiplicity=Multiplicity(0, 1))
    }
)
FloorPlan_Segment: BinaryAssociation = BinaryAssociation(
    name="FloorPlan_Segment",
    ends={
        Property(name="segment4", type=Segment, multiplicity=Multiplicity(0, 1)),
        Property(name="floorPlan5", type=FloorPlan, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_vlLwsHNhEeqHBZyMlFJVZw",
    types={SAFE_HOME_SYSTEM, config, securitySystem, Device_Configuration, Automation_System, Sensor, Alarm_Signaler, Camera, Telephone_Answering_machine, Lights, HeatAirConditioning, Home_Entertainment_Devices, Television, Home_Theatre, ActivationCode, FloorPlan, Segment, FloorCoordinates},
    associations={config_ActivationCode, config_FloorPlan, FloorPlan_Segment},
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