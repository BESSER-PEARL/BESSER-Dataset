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
dronesStructure_DronesStructure = Class(name="dronesStructure::DronesStructure")
dronesStructure_Scenario = Class(name="dronesStructure::Scenario")
dronesStructure_DroneType = Class(name="dronesStructure::DroneType")
dronesStructure_CooperativeAction = Class(name="dronesStructure::CooperativeAction")
dronesStructure_Capability = Class(name="dronesStructure::Capability")
NamedElement = Class(name="NamedElement")
dronesStructure_Drone = Class(name="dronesStructure::Drone")
dronesStructure_ScenarioBounds = Class(name="dronesStructure::ScenarioBounds")
dronesStructure_Obstacle = Class(name="dronesStructure::Obstacle")
dronesStructure_Region = Class(name="dronesStructure::Region")
dronesStructure_Task = Class(name="dronesStructure::Task")
dronesStructure_Dimension = Class(name="dronesStructure::Dimension")
dronesStructure_MovementCapability = Class(name="dronesStructure::MovementCapability")
Capability = Class(name="Capability")
dronesStructure_Role = Class(name="dronesStructure::Role")
dronesStructure_RequiredCapability = Class(name="dronesStructure::RequiredCapability")
dronesStructure_Position = Class(name="dronesStructure::Position")
dronesStructure_ProvidedCapability = Class(name="dronesStructure::ProvidedCapability")
dronesStructure_AABB = Class(name="dronesStructure::AABB", is_abstract=True)
AABB = Class(name="AABB")
dronesStructure_Charger = Class(name="dronesStructure::Charger")
Region = Class(name="Region")
dronesStructure_NamedElement = Class(name="dronesStructure::NamedElement", is_abstract=True)
dronesStructure_ScanningCapability = Class(name="dronesStructure::ScanningCapability")

# dronesStructure_DronesStructure class attributes and methods

# dronesStructure_Scenario class attributes and methods
dronesStructure_Scenario_safeCommunicationDistance: Property = Property(name="safeCommunicationDistance", type=FloatType)
dronesStructure_Scenario_maximumCommunicationDistance: Property = Property(name="maximumCommunicationDistance", type=FloatType)
dronesStructure_Scenario.attributes={dronesStructure_Scenario_safeCommunicationDistance, dronesStructure_Scenario_maximumCommunicationDistance}

# dronesStructure_DroneType class attributes and methods
dronesStructure_DroneType_weight: Property = Property(name="weight", type=FloatType)
dronesStructure_DroneType_maxBatteryCapacity: Property = Property(name="maxBatteryCapacity", type=FloatType)
dronesStructure_DroneType_idleEneryConsumption: Property = Property(name="idleEneryConsumption", type=FloatType)
dronesStructure_DroneType.attributes={dronesStructure_DroneType_idleEneryConsumption, dronesStructure_DroneType_maxBatteryCapacity, dronesStructure_DroneType_weight}

# dronesStructure_CooperativeAction class attributes and methods
dronesStructure_CooperativeAction_startTimeout: Property = Property(name="startTimeout", type=FloatType)
dronesStructure_CooperativeAction_duration: Property = Property(name="duration", type=FloatType)
dronesStructure_CooperativeAction.attributes={dronesStructure_CooperativeAction_duration, dronesStructure_CooperativeAction_startTimeout}

# dronesStructure_Capability class attributes and methods

# NamedElement class attributes and methods

# dronesStructure_Drone class attributes and methods

# dronesStructure_ScenarioBounds class attributes and methods

# dronesStructure_Obstacle class attributes and methods

# dronesStructure_Region class attributes and methods

# dronesStructure_Task class attributes and methods

# dronesStructure_Dimension class attributes and methods
dronesStructure_Dimension_width: Property = Property(name="width", type=FloatType)
dronesStructure_Dimension_height: Property = Property(name="height", type=FloatType)
dronesStructure_Dimension_depth: Property = Property(name="depth", type=FloatType)
dronesStructure_Dimension.attributes={dronesStructure_Dimension_depth, dronesStructure_Dimension_width, dronesStructure_Dimension_height}

# dronesStructure_MovementCapability class attributes and methods

# Capability class attributes and methods

# dronesStructure_Role class attributes and methods

# dronesStructure_RequiredCapability class attributes and methods
dronesStructure_RequiredCapability_minimalValue: Property = Property(name="minimalValue", type=FloatType)
dronesStructure_RequiredCapability.attributes={dronesStructure_RequiredCapability_minimalValue}

# dronesStructure_Position class attributes and methods
dronesStructure_Position_x: Property = Property(name="x", type=FloatType)
dronesStructure_Position_y: Property = Property(name="y", type=FloatType)
dronesStructure_Position_z: Property = Property(name="z", type=FloatType)
dronesStructure_Position.attributes={dronesStructure_Position_y, dronesStructure_Position_z, dronesStructure_Position_x}

# dronesStructure_ProvidedCapability class attributes and methods
dronesStructure_ProvidedCapability_maximalValue: Property = Property(name="maximalValue", type=FloatType)
dronesStructure_ProvidedCapability_energyConsumptionPerValue: Property = Property(name="energyConsumptionPerValue", type=FloatType)
dronesStructure_ProvidedCapability.attributes={dronesStructure_ProvidedCapability_energyConsumptionPerValue, dronesStructure_ProvidedCapability_maximalValue}

# dronesStructure_AABB class attributes and methods

# AABB class attributes and methods

# dronesStructure_Charger class attributes and methods

# Region class attributes and methods

# dronesStructure_NamedElement class attributes and methods
dronesStructure_NamedElement_name: Property = Property(name="name", type=StringType)
dronesStructure_NamedElement.attributes={dronesStructure_NamedElement_name}

# dronesStructure_ScanningCapability class attributes and methods

# Relationships
scenarios0: BinaryAssociation = BinaryAssociation(
    name="scenarios0",
    ends={
        Property(name="dronesStructure_Scenario", type=dronesStructure_DronesStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesStructure_DronesStructure", type=dronesStructure_Scenario, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
droneTypes1: BinaryAssociation = BinaryAssociation(
    name="droneTypes1",
    ends={
        Property(name="dronesStructure_DroneType", type=dronesStructure_DronesStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesStructure_DronesStructure2", type=dronesStructure_DroneType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cooperativeActions3: BinaryAssociation = BinaryAssociation(
    name="cooperativeActions3",
    ends={
        Property(name="dronesStructure_CooperativeAction", type=dronesStructure_DronesStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesStructure_DronesStructure4", type=dronesStructure_CooperativeAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
capabilities5: BinaryAssociation = BinaryAssociation(
    name="capabilities5",
    ends={
        Property(name="dronesStructure_Capability", type=dronesStructure_DronesStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesStructure_DronesStructure6", type=dronesStructure_Capability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
drones7: BinaryAssociation = BinaryAssociation(
    name="drones7",
    ends={
        Property(name="dronesStructure_Drone", type=dronesStructure_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesStructure_Scenario8", type=dronesStructure_Drone, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allowedBounds9: BinaryAssociation = BinaryAssociation(
    name="allowedBounds9",
    ends={
        Property(name="dronesStructure_ScenarioBounds", type=dronesStructure_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesStructure_Scenario10", type=dronesStructure_ScenarioBounds, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
obstacles11: BinaryAssociation = BinaryAssociation(
    name="obstacles11",
    ends={
        Property(name="dronesStructure_Obstacle", type=dronesStructure_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesStructure_Scenario12", type=dronesStructure_Obstacle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
regions13: BinaryAssociation = BinaryAssociation(
    name="regions13",
    ends={
        Property(name="dronesStructure_Region", type=dronesStructure_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesStructure_Scenario14", type=dronesStructure_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tasks15: BinaryAssociation = BinaryAssociation(
    name="tasks15",
    ends={
        Property(name="dronesStructure_Task", type=dronesStructure_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesStructure_Scenario16", type=dronesStructure_Task, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
movementCapability18: BinaryAssociation = BinaryAssociation(
    name="movementCapability18",
    ends={
        Property(name="dronesStructure_ProvidedCapability", type=dronesStructure_DroneType, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesStructure_DroneType19", type=dronesStructure_ProvidedCapability, multiplicity=Multiplicity(0, 1))
    }
)
dimension20: BinaryAssociation = BinaryAssociation(
    name="dimension20",
    ends={
        Property(name="dronesStructure_Dimension", type=dronesStructure_DroneType, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesStructure_DroneType21", type=dronesStructure_Dimension, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
scanningCapability22: BinaryAssociation = BinaryAssociation(
    name="scanningCapability22",
    ends={
        Property(name="dronesStructure_ProvidedCapability24", type=dronesStructure_DroneType, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesStructure_DroneType23", type=dronesStructure_ProvidedCapability, multiplicity=Multiplicity(0, 1))
    }
)
capability25: BinaryAssociation = BinaryAssociation(
    name="capability25",
    ends={
        Property(name="dronesStructure_Capability27", type=dronesStructure_ProvidedCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesStructure_ProvidedCapability26", type=dronesStructure_Capability, multiplicity=Multiplicity(1, 1))
    }
)
droneType28: BinaryAssociation = BinaryAssociation(
    name="droneType28",
    ends={
        Property(name="DroneType", type=dronesStructure_ProvidedCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="providedCapabilities", type=dronesStructure_DroneType, multiplicity=Multiplicity(1, 1))
    }
)
roles29: BinaryAssociation = BinaryAssociation(
    name="roles29",
    ends={
        Property(name="Role", type=dronesStructure_CooperativeAction, multiplicity=Multiplicity(1, 1)),
        Property(name="cooperativeAction", type=dronesStructure_Role, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
requiredCapabilities30: BinaryAssociation = BinaryAssociation(
    name="requiredCapabilities30",
    ends={
        Property(name="RequiredCapability", type=dronesStructure_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="role", type=dronesStructure_RequiredCapability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cooperativeAction31: BinaryAssociation = BinaryAssociation(
    name="cooperativeAction31",
    ends={
        Property(name="CooperativeAction", type=dronesStructure_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="roles", type=dronesStructure_CooperativeAction, multiplicity=Multiplicity(1, 1))
    }
)
capability32: BinaryAssociation = BinaryAssociation(
    name="capability32",
    ends={
        Property(name="dronesStructure_Capability33", type=dronesStructure_RequiredCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesStructure_RequiredCapability", type=dronesStructure_Capability, multiplicity=Multiplicity(1, 1))
    }
)
role34: BinaryAssociation = BinaryAssociation(
    name="role34",
    ends={
        Property(name="Role35", type=dronesStructure_RequiredCapability, multiplicity=Multiplicity(1, 1)),
        Property(name="requiredCapabilities", type=dronesStructure_Role, multiplicity=Multiplicity(1, 1))
    }
)
providedCapabilities17: BinaryAssociation = BinaryAssociation(
    name="providedCapabilities17",
    ends={
        Property(name="ProvidedCapability", type=dronesStructure_DroneType, multiplicity=Multiplicity(1, 1)),
        Property(name="droneType", type=dronesStructure_ProvidedCapability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
position41: BinaryAssociation = BinaryAssociation(
    name="position41",
    ends={
        Property(name="dronesStructure_Position42", type=dronesStructure_AABB, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesStructure_AABB", type=dronesStructure_Position, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dimension43: BinaryAssociation = BinaryAssociation(
    name="dimension43",
    ends={
        Property(name="dronesStructure_Dimension45", type=dronesStructure_AABB, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesStructure_AABB44", type=dronesStructure_Dimension, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tasks46: BinaryAssociation = BinaryAssociation(
    name="tasks46",
    ends={
        Property(name="Task", type=dronesStructure_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="region", type=dronesStructure_Task, multiplicity=Multiplicity(0, 9999))
    }
)
region47: BinaryAssociation = BinaryAssociation(
    name="region47",
    ends={
        Property(name="Region", type=dronesStructure_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="tasks", type=dronesStructure_Region, multiplicity=Multiplicity(1, 1))
    }
)
actionToPerform48: BinaryAssociation = BinaryAssociation(
    name="actionToPerform48",
    ends={
        Property(name="dronesStructure_CooperativeAction50", type=dronesStructure_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesStructure_Task49", type=dronesStructure_CooperativeAction, multiplicity=Multiplicity(0, 1))
    }
)
startPosition36: BinaryAssociation = BinaryAssociation(
    name="startPosition36",
    ends={
        Property(name="dronesStructure_Position", type=dronesStructure_Drone, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesStructure_Drone37", type=dronesStructure_Position, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dronetype38: BinaryAssociation = BinaryAssociation(
    name="dronetype38",
    ends={
        Property(name="dronesStructure_DroneType40", type=dronesStructure_Drone, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesStructure_Drone39", type=dronesStructure_DroneType, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_dronesStructure_Scenario_NamedElement = Generalization(general=NamedElement, specific=dronesStructure_Scenario)
gen_dronesStructure_Capability_NamedElement = Generalization(general=NamedElement, specific=dronesStructure_Capability)
gen_dronesStructure_DroneType_NamedElement = Generalization(general=NamedElement, specific=dronesStructure_DroneType)
gen_dronesStructure_MovementCapability_Capability = Generalization(general=Capability, specific=dronesStructure_MovementCapability)
gen_dronesStructure_CooperativeAction_NamedElement = Generalization(general=NamedElement, specific=dronesStructure_CooperativeAction)
gen_dronesStructure_Role_NamedElement = Generalization(general=NamedElement, specific=dronesStructure_Role)
gen_dronesStructure_Drone_NamedElement = Generalization(general=NamedElement, specific=dronesStructure_Drone)
gen_dronesStructure_Obstacle_AABB = Generalization(general=AABB, specific=dronesStructure_Obstacle)
gen_dronesStructure_Obstacle_NamedElement = Generalization(general=NamedElement, specific=dronesStructure_Obstacle)
gen_dronesStructure_Region_AABB = Generalization(general=AABB, specific=dronesStructure_Region)
gen_dronesStructure_Region_NamedElement = Generalization(general=NamedElement, specific=dronesStructure_Region)
gen_dronesStructure_ScenarioBounds_AABB = Generalization(general=AABB, specific=dronesStructure_ScenarioBounds)
gen_dronesStructure_Task_NamedElement = Generalization(general=NamedElement, specific=dronesStructure_Task)
gen_dronesStructure_Charger_Region = Generalization(general=Region, specific=dronesStructure_Charger)
gen_dronesStructure_ScanningCapability_Capability = Generalization(general=Capability, specific=dronesStructure_ScanningCapability)

# Domain Model
domain_model = DomainModel(
    name="dronesStructure",
    types={dronesStructure_DronesStructure, dronesStructure_Scenario, dronesStructure_DroneType, dronesStructure_CooperativeAction, dronesStructure_Capability, NamedElement, dronesStructure_Drone, dronesStructure_ScenarioBounds, dronesStructure_Obstacle, dronesStructure_Region, dronesStructure_Task, dronesStructure_Dimension, dronesStructure_MovementCapability, Capability, dronesStructure_Role, dronesStructure_RequiredCapability, dronesStructure_Position, dronesStructure_ProvidedCapability, dronesStructure_AABB, AABB, dronesStructure_Charger, Region, dronesStructure_NamedElement, dronesStructure_ScanningCapability},
    associations={scenarios0, droneTypes1, cooperativeActions3, capabilities5, drones7, allowedBounds9, obstacles11, regions13, tasks15, movementCapability18, dimension20, scanningCapability22, capability25, droneType28, roles29, requiredCapabilities30, cooperativeAction31, capability32, role34, providedCapabilities17, position41, dimension43, tasks46, region47, actionToPerform48, startPosition36, dronetype38},
    generalizations={gen_dronesStructure_Scenario_NamedElement, gen_dronesStructure_Capability_NamedElement, gen_dronesStructure_DroneType_NamedElement, gen_dronesStructure_MovementCapability_Capability, gen_dronesStructure_CooperativeAction_NamedElement, gen_dronesStructure_Role_NamedElement, gen_dronesStructure_Drone_NamedElement, gen_dronesStructure_Obstacle_AABB, gen_dronesStructure_Obstacle_NamedElement, gen_dronesStructure_Region_AABB, gen_dronesStructure_Region_NamedElement, gen_dronesStructure_ScenarioBounds_AABB, gen_dronesStructure_Task_NamedElement, gen_dronesStructure_Charger_Region, gen_dronesStructure_ScanningCapability_Capability},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)