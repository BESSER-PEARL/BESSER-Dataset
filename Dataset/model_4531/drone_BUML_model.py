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
drone_AreaObject = Class(name="drone::AreaObject")
drone_Property = Class(name="drone::Property")
drone_Position = Class(name="drone::Position")
drone_Coordinate = Class(name="drone::Coordinate")
drone_Size = Class(name="drone::Size")
drone_Mission = Class(name="drone::Mission")
NamedElement = Class(name="NamedElement")
drone_Task = Class(name="drone::Task")
drone_TaskDescriptor = Class(name="drone::TaskDescriptor")
drone_MeasureValue = Class(name="drone::MeasureValue")
drone_Capability = Class(name="drone::Capability")
drone_CapabilityProperties = Class(name="drone::CapabilityProperties")
drone_StringValue = Class(name="drone::StringValue")
PropertyValue = Class(name="PropertyValue")
drone_PropertyValue = Class(name="drone::PropertyValue", is_abstract=True)
drone_PropertyKey = Class(name="drone::PropertyKey")
drone_Robot = Class(name="drone::Robot")
drone_Battery = Class(name="drone::Battery")
drone_Equipment = Class(name="drone::Equipment")
drone_MeasureDimension = Class(name="drone::MeasureDimension")
drone_MeasureConversion = Class(name="drone::MeasureConversion")
drone_RobotMissionContainer = Class(name="drone::RobotMissionContainer")
drone_NamedElement = Class(name="drone::NamedElement", is_abstract=True)
drone_PropertyKeyContainer = Class(name="drone::PropertyKeyContainer")
drone_EObject = Class(name="drone::EObject")

# drone_AreaObject class attributes and methods

# drone_Property class attributes and methods

# drone_Position class attributes and methods

# drone_Coordinate class attributes and methods
drone_Coordinate_latitude: Property = Property(name="latitude", type=FloatType)
drone_Coordinate_longitude: Property = Property(name="longitude", type=FloatType)
drone_Coordinate_altitude: Property = Property(name="altitude", type=FloatType)
drone_Coordinate.attributes={drone_Coordinate_altitude, drone_Coordinate_latitude, drone_Coordinate_longitude}

# drone_Size class attributes and methods

# drone_Mission class attributes and methods

# NamedElement class attributes and methods

# drone_Task class attributes and methods

# drone_TaskDescriptor class attributes and methods

# drone_MeasureValue class attributes and methods
drone_MeasureValue_value: Property = Property(name="value", type=FloatType)
drone_MeasureValue.attributes={drone_MeasureValue_value}

# drone_Capability class attributes and methods

# drone_CapabilityProperties class attributes and methods

# drone_StringValue class attributes and methods
drone_StringValue_value: Property = Property(name="value", type=StringType)
drone_StringValue.attributes={drone_StringValue_value}

# PropertyValue class attributes and methods

# drone_PropertyValue class attributes and methods

# drone_PropertyKey class attributes and methods

# drone_Robot class attributes and methods

# drone_Battery class attributes and methods

# drone_Equipment class attributes and methods

# drone_MeasureDimension class attributes and methods

# drone_MeasureConversion class attributes and methods
drone_MeasureConversion_rate: Property = Property(name="rate", type=FloatType)
drone_MeasureConversion.attributes={drone_MeasureConversion_rate}

# drone_RobotMissionContainer class attributes and methods

# drone_NamedElement class attributes and methods
drone_NamedElement_name: Property = Property(name="name", type=StringType)
drone_NamedElement.attributes={drone_NamedElement_name}

# drone_PropertyKeyContainer class attributes and methods

# drone_EObject class attributes and methods

# Relationships
targets3: BinaryAssociation = BinaryAssociation(
    name="targets3",
    ends={
        Property(name="drone_AreaObject", type=drone_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_TaskDescriptor", type=drone_AreaObject, multiplicity=Multiplicity(0, 9999))
    }
)
properties4: BinaryAssociation = BinaryAssociation(
    name="properties4",
    ends={
        Property(name="drone_Property", type=drone_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_TaskDescriptor5", type=drone_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
task6: BinaryAssociation = BinaryAssociation(
    name="task6",
    ends={
        Property(name="Task7", type=drone_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="descriptor", type=drone_Task, multiplicity=Multiplicity(0, 1))
    }
)
coordinates8: BinaryAssociation = BinaryAssociation(
    name="coordinates8",
    ends={
        Property(name="drone_Coordinate", type=drone_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Position", type=drone_Coordinate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties9: BinaryAssociation = BinaryAssociation(
    name="properties9",
    ends={
        Property(name="drone_Property11", type=drone_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Position10", type=drone_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
positions12: BinaryAssociation = BinaryAssociation(
    name="positions12",
    ends={
        Property(name="drone_Position14", type=drone_AreaObject, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_AreaObject13", type=drone_Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
size15: BinaryAssociation = BinaryAssociation(
    name="size15",
    ends={
        Property(name="drone_Size", type=drone_AreaObject, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_AreaObject16", type=drone_Size, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties17: BinaryAssociation = BinaryAssociation(
    name="properties17",
    ends={
        Property(name="drone_Property19", type=drone_AreaObject, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_AreaObject18", type=drone_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tasks0: BinaryAssociation = BinaryAssociation(
    name="tasks0",
    ends={
        Property(name="Task", type=drone_Mission, multiplicity=Multiplicity(1, 1)),
        Property(name="mission", type=drone_Task, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
mission1: BinaryAssociation = BinaryAssociation(
    name="mission1",
    ends={
        Property(name="Mission", type=drone_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="tasks", type=drone_Mission, multiplicity=Multiplicity(1, 1))
    }
)
descriptor2: BinaryAssociation = BinaryAssociation(
    name="descriptor2",
    ends={
        Property(name="TaskDescriptor", type=drone_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="task", type=drone_TaskDescriptor, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
communicationRange38: BinaryAssociation = BinaryAssociation(
    name="communicationRange38",
    ends={
        Property(name="drone_MeasureValue", type=drone_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Robot39", type=drone_MeasureValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
weight40: BinaryAssociation = BinaryAssociation(
    name="weight40",
    ends={
        Property(name="drone_MeasureValue42", type=drone_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Robot41", type=drone_MeasureValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mission43: BinaryAssociation = BinaryAssociation(
    name="mission43",
    ends={
        Property(name="drone_Mission", type=drone_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Robot44", type=drone_Mission, multiplicity=Multiplicity(0, 1))
    }
)
capabilities45: BinaryAssociation = BinaryAssociation(
    name="capabilities45",
    ends={
        Property(name="drone_Capability", type=drone_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Robot46", type=drone_Capability, multiplicity=Multiplicity(0, 9999))
    }
)
capabilityProperties47: BinaryAssociation = BinaryAssociation(
    name="capabilityProperties47",
    ends={
        Property(name="drone_CapabilityProperties", type=drone_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Robot48", type=drone_CapabilityProperties, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
width49: BinaryAssociation = BinaryAssociation(
    name="width49",
    ends={
        Property(name="drone_MeasureValue51", type=drone_Size, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Size50", type=drone_MeasureValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value20: BinaryAssociation = BinaryAssociation(
    name="value20",
    ends={
        Property(name="drone_PropertyValue", type=drone_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Property21", type=drone_PropertyValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
key22: BinaryAssociation = BinaryAssociation(
    name="key22",
    ends={
        Property(name="drone_PropertyKey", type=drone_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Property23", type=drone_PropertyKey, multiplicity=Multiplicity(1, 1))
    }
)
position24: BinaryAssociation = BinaryAssociation(
    name="position24",
    ends={
        Property(name="drone_Position25", type=drone_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Robot", type=drone_Position, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
size26: BinaryAssociation = BinaryAssociation(
    name="size26",
    ends={
        Property(name="drone_Size28", type=drone_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Robot27", type=drone_Size, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
batteries29: BinaryAssociation = BinaryAssociation(
    name="batteries29",
    ends={
        Property(name="drone_Battery", type=drone_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Robot30", type=drone_Battery, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equipments31: BinaryAssociation = BinaryAssociation(
    name="equipments31",
    ends={
        Property(name="drone_Equipment", type=drone_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Robot32", type=drone_Equipment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tasks33: BinaryAssociation = BinaryAssociation(
    name="tasks33",
    ends={
        Property(name="drone_Task", type=drone_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Robot34", type=drone_Task, multiplicity=Multiplicity(0, 9999))
    }
)
properties35: BinaryAssociation = BinaryAssociation(
    name="properties35",
    ends={
        Property(name="drone_Property37", type=drone_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Robot36", type=drone_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dimension76: BinaryAssociation = BinaryAssociation(
    name="dimension76",
    ends={
        Property(name="drone_MeasureDimension", type=drone_MeasureValue, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_MeasureValue77", type=drone_MeasureDimension, multiplicity=Multiplicity(1, 1))
    }
)
dimension78: BinaryAssociation = BinaryAssociation(
    name="dimension78",
    ends={
        Property(name="drone_MeasureDimension79", type=drone_MeasureConversion, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_MeasureConversion", type=drone_MeasureDimension, multiplicity=Multiplicity(1, 1))
    }
)
conversions80: BinaryAssociation = BinaryAssociation(
    name="conversions80",
    ends={
        Property(name="drone_MeasureConversion82", type=drone_MeasureDimension, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_MeasureDimension81", type=drone_MeasureConversion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
missions83: BinaryAssociation = BinaryAssociation(
    name="missions83",
    ends={
        Property(name="drone_Mission84", type=drone_RobotMissionContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_RobotMissionContainer", type=drone_Mission, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
robots85: BinaryAssociation = BinaryAssociation(
    name="robots85",
    ends={
        Property(name="drone_Robot87", type=drone_RobotMissionContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_RobotMissionContainer86", type=drone_Robot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
measureDimensions88: BinaryAssociation = BinaryAssociation(
    name="measureDimensions88",
    ends={
        Property(name="drone_MeasureDimension90", type=drone_RobotMissionContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_RobotMissionContainer89", type=drone_MeasureDimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
areaObjects91: BinaryAssociation = BinaryAssociation(
    name="areaObjects91",
    ends={
        Property(name="drone_AreaObject93", type=drone_RobotMissionContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_RobotMissionContainer92", type=drone_AreaObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
height52: BinaryAssociation = BinaryAssociation(
    name="height52",
    ends={
        Property(name="drone_MeasureValue54", type=drone_Size, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Size53", type=drone_MeasureValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
length55: BinaryAssociation = BinaryAssociation(
    name="length55",
    ends={
        Property(name="drone_MeasureValue57", type=drone_Size, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Size56", type=drone_MeasureValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
capacity58: BinaryAssociation = BinaryAssociation(
    name="capacity58",
    ends={
        Property(name="drone_MeasureValue60", type=drone_Battery, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Battery59", type=drone_MeasureValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
voltage61: BinaryAssociation = BinaryAssociation(
    name="voltage61",
    ends={
        Property(name="drone_MeasureValue63", type=drone_Battery, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Battery62", type=drone_MeasureValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rechargeTime64: BinaryAssociation = BinaryAssociation(
    name="rechargeTime64",
    ends={
        Property(name="drone_MeasureValue66", type=drone_Battery, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Battery65", type=drone_MeasureValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
properties67: BinaryAssociation = BinaryAssociation(
    name="properties67",
    ends={
        Property(name="drone_Property69", type=drone_Battery, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Battery68", type=drone_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties70: BinaryAssociation = BinaryAssociation(
    name="properties70",
    ends={
        Property(name="drone_Property72", type=drone_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Equipment71", type=drone_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
facilitate73: BinaryAssociation = BinaryAssociation(
    name="facilitate73",
    ends={
        Property(name="drone_Capability75", type=drone_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_Equipment74", type=drone_Capability, multiplicity=Multiplicity(0, 9999))
    }
)
capabilities94: BinaryAssociation = BinaryAssociation(
    name="capabilities94",
    ends={
        Property(name="drone_Capability96", type=drone_RobotMissionContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_RobotMissionContainer95", type=drone_Capability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propertyKeyContainer97: BinaryAssociation = BinaryAssociation(
    name="propertyKeyContainer97",
    ends={
        Property(name="drone_PropertyKeyContainer", type=drone_RobotMissionContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_RobotMissionContainer98", type=drone_PropertyKeyContainer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
temporalElements99: BinaryAssociation = BinaryAssociation(
    name="temporalElements99",
    ends={
        Property(name="drone_EObject", type=drone_RobotMissionContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_RobotMissionContainer100", type=drone_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keys101: BinaryAssociation = BinaryAssociation(
    name="keys101",
    ends={
        Property(name="drone_PropertyKey103", type=drone_PropertyKeyContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_PropertyKeyContainer102", type=drone_PropertyKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties104: BinaryAssociation = BinaryAssociation(
    name="properties104",
    ends={
        Property(name="drone_Property106", type=drone_CapabilityProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_CapabilityProperties105", type=drone_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
capability107: BinaryAssociation = BinaryAssociation(
    name="capability107",
    ends={
        Property(name="drone_Capability109", type=drone_CapabilityProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="drone_CapabilityProperties108", type=drone_Capability, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_drone_AreaObject_NamedElement = Generalization(general=NamedElement, specific=drone_AreaObject)
gen_drone_Mission_NamedElement = Generalization(general=NamedElement, specific=drone_Mission)
gen_drone_Task_NamedElement = Generalization(general=NamedElement, specific=drone_Task)
gen_drone_StringValue_PropertyValue = Generalization(general=PropertyValue, specific=drone_StringValue)
gen_drone_Robot_NamedElement = Generalization(general=NamedElement, specific=drone_Robot)
gen_drone_MeasureValue_PropertyValue = Generalization(general=PropertyValue, specific=drone_MeasureValue)
gen_drone_MeasureDimension_NamedElement = Generalization(general=NamedElement, specific=drone_MeasureDimension)
gen_drone_Equipment_NamedElement = Generalization(general=NamedElement, specific=drone_Equipment)
gen_drone_PropertyKeyContainer_NamedElement = Generalization(general=NamedElement, specific=drone_PropertyKeyContainer)
gen_drone_PropertyKey_NamedElement = Generalization(general=NamedElement, specific=drone_PropertyKey)
gen_drone_Capability_NamedElement = Generalization(general=NamedElement, specific=drone_Capability)

# Domain Model
domain_model = DomainModel(
    name="drone",
    types={drone_AreaObject, drone_Property, drone_Position, drone_Coordinate, drone_Size, drone_Mission, NamedElement, drone_Task, drone_TaskDescriptor, drone_MeasureValue, drone_Capability, drone_CapabilityProperties, drone_StringValue, PropertyValue, drone_PropertyValue, drone_PropertyKey, drone_Robot, drone_Battery, drone_Equipment, drone_MeasureDimension, drone_MeasureConversion, drone_RobotMissionContainer, drone_NamedElement, drone_PropertyKeyContainer, drone_EObject},
    associations={targets3, properties4, task6, coordinates8, properties9, positions12, size15, properties17, tasks0, mission1, descriptor2, communicationRange38, weight40, mission43, capabilities45, capabilityProperties47, width49, value20, key22, position24, size26, batteries29, equipments31, tasks33, properties35, dimension76, dimension78, conversions80, missions83, robots85, measureDimensions88, areaObjects91, height52, length55, capacity58, voltage61, rechargeTime64, properties67, properties70, facilitate73, capabilities94, propertyKeyContainer97, temporalElements99, keys101, properties104, capability107},
    generalizations={gen_drone_AreaObject_NamedElement, gen_drone_Mission_NamedElement, gen_drone_Task_NamedElement, gen_drone_StringValue_PropertyValue, gen_drone_Robot_NamedElement, gen_drone_MeasureValue_PropertyValue, gen_drone_MeasureDimension_NamedElement, gen_drone_Equipment_NamedElement, gen_drone_PropertyKeyContainer_NamedElement, gen_drone_PropertyKey_NamedElement, gen_drone_Capability_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)