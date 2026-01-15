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
DroneState: Enumeration = Enumeration(
    name="DroneState",
    literals={
            EnumerationLiteral(name="CREATED"),
			EnumerationLiteral(name="HOVERING"),
			EnumerationLiteral(name="MOVING"),
			EnumerationLiteral(name="DONE")
    }
)

TaskState: Enumeration = Enumeration(
    name="TaskState",
    literals={
            EnumerationLiteral(name="NOT_STARTED"),
			EnumerationLiteral(name="WAITING"),
			EnumerationLiteral(name="IN_PROGRESS"),
			EnumerationLiteral(name="DONE")
    }
)

# Classes
dronesSimulation_Position = Class(name="dronesSimulation::Position")
dronesSimulation_RoleInstance = Class(name="dronesSimulation::RoleInstance")
dronesSimulation_Observation = Class(name="dronesSimulation::Observation", is_abstract=True)
dronesSimulation_DronesSimulation = Class(name="dronesSimulation::DronesSimulation")
dronesSimulation_Scenario = Class(name="dronesSimulation::Scenario")
dronesSimulation_TaskInstance = Class(name="dronesSimulation::TaskInstance")
dronesSimulation_DroneInstance = Class(name="dronesSimulation::DroneInstance")
dronesSimulation_Drone = Class(name="dronesSimulation::Drone")
dronesSimulation_Task = Class(name="dronesSimulation::Task")
dronesSimulation_Role = Class(name="dronesSimulation::Role")
dronesSimulation_ObstacleObservation = Class(name="dronesSimulation::ObstacleObservation")
Observation = Class(name="Observation")
dronesSimulation_Obstacle = Class(name="dronesSimulation::Obstacle")
dronesSimulation_DroneObservation = Class(name="dronesSimulation::DroneObservation")

# dronesSimulation_Position class attributes and methods

# dronesSimulation_RoleInstance class attributes and methods

# dronesSimulation_Observation class attributes and methods
dronesSimulation_Observation_time: Property = Property(name="time", type=StringType)
dronesSimulation_Observation_id: Property = Property(name="id", type=StringType)
dronesSimulation_Observation.attributes={dronesSimulation_Observation_time, dronesSimulation_Observation_id}

# dronesSimulation_DronesSimulation class attributes and methods

# dronesSimulation_Scenario class attributes and methods

# dronesSimulation_TaskInstance class attributes and methods
dronesSimulation_TaskInstance_state: Property = Property(name="state", type=StringType)
dronesSimulation_TaskInstance.attributes={dronesSimulation_TaskInstance_state}

# dronesSimulation_DroneInstance class attributes and methods
dronesSimulation_DroneInstance_currentBattery: Property = Property(name="currentBattery", type=FloatType)
dronesSimulation_DroneInstance_state: Property = Property(name="state", type=StringType)
dronesSimulation_DroneInstance.attributes={dronesSimulation_DroneInstance_state, dronesSimulation_DroneInstance_currentBattery}

# dronesSimulation_Drone class attributes and methods

# dronesSimulation_Task class attributes and methods

# dronesSimulation_Role class attributes and methods

# dronesSimulation_ObstacleObservation class attributes and methods

# Observation class attributes and methods

# dronesSimulation_Obstacle class attributes and methods

# dronesSimulation_DroneObservation class attributes and methods

# Relationships
position7: BinaryAssociation = BinaryAssociation(
    name="position7",
    ends={
        Property(name="dronesSimulation_Position", type=dronesSimulation_DroneInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesSimulation_DroneInstance8", type=dronesSimulation_Position, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
currentRole9: BinaryAssociation = BinaryAssociation(
    name="currentRole9",
    ends={
        Property(name="RoleInstance", type=dronesSimulation_DroneInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="allocatedDrone", type=dronesSimulation_RoleInstance, multiplicity=Multiplicity(0, 1))
    }
)
scenario0: BinaryAssociation = BinaryAssociation(
    name="scenario0",
    ends={
        Property(name="dronesSimulation_Scenario", type=dronesSimulation_DronesSimulation, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesSimulation_DronesSimulation", type=dronesSimulation_Scenario, multiplicity=Multiplicity(1, 1))
    }
)
taskInstances1: BinaryAssociation = BinaryAssociation(
    name="taskInstances1",
    ends={
        Property(name="dronesSimulation_TaskInstance", type=dronesSimulation_DronesSimulation, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesSimulation_DronesSimulation2", type=dronesSimulation_TaskInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
droneInstances3: BinaryAssociation = BinaryAssociation(
    name="droneInstances3",
    ends={
        Property(name="dronesSimulation_DroneInstance", type=dronesSimulation_DronesSimulation, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesSimulation_DronesSimulation4", type=dronesSimulation_DroneInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
drone5: BinaryAssociation = BinaryAssociation(
    name="drone5",
    ends={
        Property(name="dronesSimulation_Drone", type=dronesSimulation_DroneInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesSimulation_DroneInstance6", type=dronesSimulation_Drone, multiplicity=Multiplicity(1, 1))
    }
)
observations10: BinaryAssociation = BinaryAssociation(
    name="observations10",
    ends={
        Property(name="dronesSimulation_Observation", type=dronesSimulation_DroneInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesSimulation_DroneInstance11", type=dronesSimulation_Observation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
task12: BinaryAssociation = BinaryAssociation(
    name="task12",
    ends={
        Property(name="dronesSimulation_Task", type=dronesSimulation_TaskInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesSimulation_TaskInstance13", type=dronesSimulation_Task, multiplicity=Multiplicity(0, 1))
    }
)
roleInstances14: BinaryAssociation = BinaryAssociation(
    name="roleInstances14",
    ends={
        Property(name="RoleInstance15", type=dronesSimulation_TaskInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="taskInstance", type=dronesSimulation_RoleInstance, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
role16: BinaryAssociation = BinaryAssociation(
    name="role16",
    ends={
        Property(name="dronesSimulation_Role", type=dronesSimulation_RoleInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesSimulation_RoleInstance", type=dronesSimulation_Role, multiplicity=Multiplicity(0, 1))
    }
)
taskInstance17: BinaryAssociation = BinaryAssociation(
    name="taskInstance17",
    ends={
        Property(name="TaskInstance", type=dronesSimulation_RoleInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="roleInstances", type=dronesSimulation_TaskInstance, multiplicity=Multiplicity(1, 1))
    }
)
allocatedDrone18: BinaryAssociation = BinaryAssociation(
    name="allocatedDrone18",
    ends={
        Property(name="DroneInstance", type=dronesSimulation_RoleInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="currentRole", type=dronesSimulation_DroneInstance, multiplicity=Multiplicity(0, 1))
    }
)
obstacle19: BinaryAssociation = BinaryAssociation(
    name="obstacle19",
    ends={
        Property(name="dronesSimulation_Obstacle", type=dronesSimulation_ObstacleObservation, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesSimulation_ObstacleObservation", type=dronesSimulation_Obstacle, multiplicity=Multiplicity(1, 1))
    }
)
drone20: BinaryAssociation = BinaryAssociation(
    name="drone20",
    ends={
        Property(name="dronesSimulation_Drone21", type=dronesSimulation_DroneObservation, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesSimulation_DroneObservation", type=dronesSimulation_Drone, multiplicity=Multiplicity(1, 1))
    }
)
position22: BinaryAssociation = BinaryAssociation(
    name="position22",
    ends={
        Property(name="dronesSimulation_Position24", type=dronesSimulation_DroneObservation, multiplicity=Multiplicity(1, 1)),
        Property(name="dronesSimulation_DroneObservation23", type=dronesSimulation_Position, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_dronesSimulation_ObstacleObservation_Observation = Generalization(general=Observation, specific=dronesSimulation_ObstacleObservation)
gen_dronesSimulation_DroneObservation_Observation = Generalization(general=Observation, specific=dronesSimulation_DroneObservation)

# Domain Model
domain_model = DomainModel(
    name="dronesSimulation",
    types={dronesSimulation_Position, dronesSimulation_RoleInstance, dronesSimulation_Observation, dronesSimulation_DronesSimulation, dronesSimulation_Scenario, dronesSimulation_TaskInstance, dronesSimulation_DroneInstance, dronesSimulation_Drone, dronesSimulation_Task, dronesSimulation_Role, dronesSimulation_ObstacleObservation, Observation, dronesSimulation_Obstacle, dronesSimulation_DroneObservation, DroneState, TaskState},
    associations={position7, currentRole9, scenario0, taskInstances1, droneInstances3, drone5, observations10, task12, roleInstances14, role16, taskInstance17, allocatedDrone18, obstacle19, drone20, position22},
    generalizations={gen_dronesSimulation_ObstacleObservation_Observation, gen_dronesSimulation_DroneObservation_Observation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)