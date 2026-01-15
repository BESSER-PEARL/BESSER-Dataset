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
MemoryType: Enumeration = Enumeration(
    name="MemoryType",
    literals={
            EnumerationLiteral(name="VOLATILE"),
			EnumerationLiteral(name="STORAGE")
    }
)

LaunchType: Enumeration = Enumeration(
    name="LaunchType",
    literals={
            EnumerationLiteral(name="VTOL"),
			EnumerationLiteral(name="HTOL"),
			EnumerationLiteral(name="OTHER")
    }
)

# Classes
drone_NamedElement = Class(name="drone::NamedElement", is_abstract=True)
drone_Drone = Class(name="drone::Drone")
NamedElement = Class(name="NamedElement")
drone_Size = Class(name="drone::Size")
drone_FlightPerformance = Class(name="drone::FlightPerformance")
drone_Battery = Class(name="drone::Battery")
drone_Processor = Class(name="drone::Processor")
drone_Memory = Class(name="drone::Memory")
drone_Device = Class(name="drone::Device")
drone_ROSDriver = Class(name="drone::ROSDriver")
drone_Parameter = Class(name="drone::Parameter")
drone_Action = Class(name="drone::Action")
drone_Property = Class(name="drone::Property")

# drone_NamedElement class attributes and methods
drone_NamedElement_name: Property = Property(name="name", type=StringType)
drone_NamedElement.attributes={drone_NamedElement_name}

# drone_Drone class attributes and methods
drone_Drone_onBoardObstacleAvoidance: Property = Property(name="onBoardObstacleAvoidance", type=BooleanType)
drone_Drone_minVoltage: Property = Property(name="minVoltage", type=FloatType)
drone_Drone_maxVoltage: Property = Property(name="maxVoltage", type=FloatType)
drone_Drone_maxPowerConsumption: Property = Property(name="maxPowerConsumption", type=FloatType)
drone_Drone_giro: Property = Property(name="giro", type=BooleanType)
drone_Drone_gps: Property = Property(name="gps", type=BooleanType)
drone_Drone_accelerometer: Property = Property(name="accelerometer", type=BooleanType)
drone_Drone_magnetometer: Property = Property(name="magnetometer", type=BooleanType)
drone_Drone_barometer: Property = Property(name="barometer", type=BooleanType)
drone_Drone_communicationRange: Property = Property(name="communicationRange", type=FloatType)
drone_Drone_dataRate: Property = Property(name="dataRate", type=IntegerType)
drone_Drone_radioFrequency: Property = Property(name="radioFrequency", type=IntegerType)
drone_Drone.attributes={drone_Drone_onBoardObstacleAvoidance, drone_Drone_accelerometer, drone_Drone_maxVoltage, drone_Drone_barometer, drone_Drone_minVoltage, drone_Drone_giro, drone_Drone_maxPowerConsumption, drone_Drone_communicationRange, drone_Drone_radioFrequency, drone_Drone_gps, drone_Drone_magnetometer, drone_Drone_dataRate}

# NamedElement class attributes and methods

# drone_Size class attributes and methods
drone_Size_width: Property = Property(name="width", type=FloatType)
drone_Size_length: Property = Property(name="length", type=FloatType)
drone_Size_height: Property = Property(name="height", type=FloatType)
drone_Size_weight: Property = Property(name="weight", type=FloatType)
drone_Size_propellers: Property = Property(name="propellers", type=IntegerType)
drone_Size_propellerSize: Property = Property(name="propellerSize", type=FloatType)
drone_Size.attributes={drone_Size_width, drone_Size_height, drone_Size_propellerSize, drone_Size_weight, drone_Size_propellers, drone_Size_length}

# drone_FlightPerformance class attributes and methods
drone_FlightPerformance_launchType: Property = Property(name="launchType", type=StringType)
drone_FlightPerformance_minSpeed: Property = Property(name="minSpeed", type=IntegerType)
drone_FlightPerformance_maxSpeed: Property = Property(name="maxSpeed", type=IntegerType)
drone_FlightPerformance_minAcceleration: Property = Property(name="minAcceleration", type=IntegerType)
drone_FlightPerformance_maxAcceleration: Property = Property(name="maxAcceleration", type=IntegerType)
drone_FlightPerformance_maxAltitude: Property = Property(name="maxAltitude", type=IntegerType)
drone_FlightPerformance_maxTurnRate: Property = Property(name="maxTurnRate", type=FloatType)
drone_FlightPerformance_minTurnRate: Property = Property(name="minTurnRate", type=FloatType)
drone_FlightPerformance_maxClimbRate: Property = Property(name="maxClimbRate", type=FloatType)
drone_FlightPerformance_maxDescendRate: Property = Property(name="maxDescendRate", type=FloatType)
drone_FlightPerformance_positionHold: Property = Property(name="positionHold", type=FloatType)
drone_FlightPerformance_maxPayload: Property = Property(name="maxPayload", type=IntegerType)
drone_FlightPerformance_maxFlightTime: Property = Property(name="maxFlightTime", type=IntegerType)
drone_FlightPerformance_maxFlightTimeWithMaxPayload: Property = Property(name="maxFlightTimeWithMaxPayload", type=IntegerType)
drone_FlightPerformance_minOperatingTemperature: Property = Property(name="minOperatingTemperature", type=FloatType)
drone_FlightPerformance_maxOperatingTemperature: Property = Property(name="maxOperatingTemperature", type=FloatType)
drone_FlightPerformance.attributes={drone_FlightPerformance_maxTurnRate, drone_FlightPerformance_maxOperatingTemperature, drone_FlightPerformance_maxFlightTime, drone_FlightPerformance_maxFlightTimeWithMaxPayload, drone_FlightPerformance_maxPayload, drone_FlightPerformance_maxAltitude, drone_FlightPerformance_maxDescendRate, drone_FlightPerformance_minSpeed, drone_FlightPerformance_maxClimbRate, drone_FlightPerformance_minOperatingTemperature, drone_FlightPerformance_positionHold, drone_FlightPerformance_maxSpeed, drone_FlightPerformance_launchType, drone_FlightPerformance_maxAcceleration, drone_FlightPerformance_minTurnRate, drone_FlightPerformance_minAcceleration}

# drone_Battery class attributes and methods
drone_Battery_cellType: Property = Property(name="cellType", type=StringType)
drone_Battery_capacity: Property = Property(name="capacity", type=IntegerType)
drone_Battery_voltage: Property = Property(name="voltage", type=FloatType)
drone_Battery_rechargeTime: Property = Property(name="rechargeTime", type=IntegerType)
drone_Battery.attributes={drone_Battery_cellType, drone_Battery_voltage, drone_Battery_rechargeTime, drone_Battery_capacity}

# drone_Processor class attributes and methods
drone_Processor_architecture: Property = Property(name="architecture", type=StringType)
drone_Processor_frequency: Property = Property(name="frequency", type=IntegerType)
drone_Processor.attributes={drone_Processor_frequency, drone_Processor_architecture}

# drone_Memory class attributes and methods
drone_Memory_type: Property = Property(name="type", type=StringType)
drone_Memory_subType: Property = Property(name="subType", type=StringType)
drone_Memory_size: Property = Property(name="size", type=IntegerType)
drone_Memory.attributes={drone_Memory_type, drone_Memory_subType, drone_Memory_size}

# drone_Device class attributes and methods

# drone_ROSDriver class attributes and methods
drone_ROSDriver_version: Property = Property(name="version", type=StringType)
drone_ROSDriver_url: Property = Property(name="url", type=StringType)
drone_ROSDriver.attributes={drone_ROSDriver_url, drone_ROSDriver_version}

# drone_Parameter class attributes and methods
drone_Parameter_key: Property = Property(name="key", type=StringType)
drone_Parameter_description: Property = Property(name="description", type=StringType)
drone_Parameter.attributes={drone_Parameter_description, drone_Parameter_key}

# drone_Action class attributes and methods

# drone_Property class attributes and methods
drone_Property_value: Property = Property(name="value", type=StringType)
drone_Property.attributes={drone_Property_value}

# Relationships
size0: BinaryAssociation = BinaryAssociation(
    name="size0",
    ends={
        Property(name="drone_Size", type=drone_Drone, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Drone", type=drone_Size, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
flightPerf1: BinaryAssociation = BinaryAssociation(
    name="flightPerf1",
    ends={
        Property(name="drone_FlightPerformance", type=drone_Drone, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Drone2", type=drone_FlightPerformance, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
batteries3: BinaryAssociation = BinaryAssociation(
    name="batteries3",
    ends={
        Property(name="drone_Battery", type=drone_Drone, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Drone4", type=drone_Battery, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processors5: BinaryAssociation = BinaryAssociation(
    name="processors5",
    ends={
        Property(name="drone_Processor", type=drone_Drone, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Drone6", type=drone_Processor, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
memory7: BinaryAssociation = BinaryAssociation(
    name="memory7",
    ends={
        Property(name="drone_Memory", type=drone_Drone, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Drone8", type=drone_Memory, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
dataEquipment9: BinaryAssociation = BinaryAssociation(
    name="dataEquipment9",
    ends={
        Property(name="drone_Device", type=drone_Drone, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Drone10", type=drone_Device, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rosDriver11: BinaryAssociation = BinaryAssociation(
    name="rosDriver11",
    ends={
        Property(name="drone_ROSDriver", type=drone_Drone, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Drone12", type=drone_ROSDriver, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters17: BinaryAssociation = BinaryAssociation(
    name="parameters17",
    ends={
        Property(name="drone_Parameter", type=drone_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Action18", type=drone_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
supportedActions13: BinaryAssociation = BinaryAssociation(
    name="supportedActions13",
    ends={
        Property(name="drone_Action", type=drone_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Device14", type=drone_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties15: BinaryAssociation = BinaryAssociation(
    name="properties15",
    ends={
        Property(name="drone_Property", type=drone_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Device16", type=drone_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_drone_Drone_NamedElement = Generalization(general=NamedElement, specific=drone_Drone)
gen_drone_Processor_NamedElement = Generalization(general=NamedElement, specific=drone_Processor)
gen_drone_Memory_NamedElement = Generalization(general=NamedElement, specific=drone_Memory)
gen_drone_Action_NamedElement = Generalization(general=NamedElement, specific=drone_Action)
gen_drone_Property_NamedElement = Generalization(general=NamedElement, specific=drone_Property)
gen_drone_ROSDriver_NamedElement = Generalization(general=NamedElement, specific=drone_ROSDriver)
gen_drone_Battery_NamedElement = Generalization(general=NamedElement, specific=drone_Battery)
gen_drone_Device_NamedElement = Generalization(general=NamedElement, specific=drone_Device)

# Domain Model
domain_model = DomainModel(
    name="drone",
    types={drone_NamedElement, drone_Drone, NamedElement, drone_Size, drone_FlightPerformance, drone_Battery, drone_Processor, drone_Memory, drone_Device, drone_ROSDriver, drone_Parameter, drone_Action, drone_Property, MemoryType, LaunchType},
    associations={size0, flightPerf1, batteries3, processors5, memory7, dataEquipment9, rosDriver11, parameters17, supportedActions13, properties15},
    generalizations={gen_drone_Drone_NamedElement, gen_drone_Processor_NamedElement, gen_drone_Memory_NamedElement, gen_drone_Action_NamedElement, gen_drone_Property_NamedElement, gen_drone_ROSDriver_NamedElement, gen_drone_Battery_NamedElement, gen_drone_Device_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)