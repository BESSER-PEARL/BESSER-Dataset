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
RobotStatus: Enumeration = Enumeration(
    name="RobotStatus",
    literals={
            EnumerationLiteral(name="Ready"),
			EnumerationLiteral(name="TurnedOff"),
			EnumerationLiteral(name="Waiting"),
			EnumerationLiteral(name="Executing")
    }
)

TaskExecutionStatus: Enumeration = Enumeration(
    name="TaskExecutionStatus",
    literals={
            EnumerationLiteral(name="Ready"),
			EnumerationLiteral(name="Finished"),
			EnumerationLiteral(name="Suspended"),
			EnumerationLiteral(name="InProgress"),
			EnumerationLiteral(name="Waiting")
    }
)

# Classes
behaviour_TaskRequirement = Class(name="behaviour::TaskRequirement")
behaviour_BehaviouralPropertyKeyContainer = Class(name="behaviour::BehaviouralPropertyKeyContainer")
behaviour_Message = Class(name="behaviour::Message")
NamedElement = Class(name="NamedElement")
behaviour_Property = Class(name="behaviour::Property")
behaviour_AreaObject = Class(name="behaviour::AreaObject")
behaviour_MeasureValue = Class(name="behaviour::MeasureValue")
behaviour_CommunicationAction = Class(name="behaviour::CommunicationAction", is_abstract=True)
Action = Class(name="Action")
behaviour_BehaviourContainer = Class(name="behaviour::BehaviourContainer")
behaviour_DynamicRobot = Class(name="behaviour::DynamicRobot")
behaviour_TaskExecution = Class(name="behaviour::TaskExecution")
behaviour_Action = Class(name="behaviour::Action")
behaviour_Task = Class(name="behaviour::Task")
behaviour_UnicastCommunication = Class(name="behaviour::UnicastCommunication")
CommunicationAction = Class(name="CommunicationAction")
behaviour_MulticastCommunication = Class(name="behaviour::MulticastCommunication")
behaviour_BroadcastCommunication = Class(name="behaviour::BroadcastCommunication")
behaviour_MessageRepository = Class(name="behaviour::MessageRepository")
behaviour_Robot = Class(name="behaviour::Robot")
behaviour_RobotCollaboration = Class(name="behaviour::RobotCollaboration")
behaviour_DetectedObject = Class(name="behaviour::DetectedObject")
PropertyKeyContainer = Class(name="PropertyKeyContainer")
behaviour_Capability = Class(name="behaviour::Capability")
behaviour_CapabilityProperties = Class(name="behaviour::CapabilityProperties")
behaviour_TaskDescriptor = Class(name="behaviour::TaskDescriptor")

# behaviour_TaskRequirement class attributes and methods
behaviour_TaskRequirement_participants: Property = Property(name="participants", type=IntegerType)
behaviour_TaskRequirement.attributes={behaviour_TaskRequirement_participants}

# behaviour_BehaviouralPropertyKeyContainer class attributes and methods

# behaviour_Message class attributes and methods
behaviour_Message_timestamp: Property = Property(name="timestamp", type=DateType)
behaviour_Message_needResponse: Property = Property(name="needResponse", type=BooleanType)
behaviour_Message.attributes={behaviour_Message_needResponse, behaviour_Message_timestamp}

# NamedElement class attributes and methods

# behaviour_Property class attributes and methods

# behaviour_AreaObject class attributes and methods

# behaviour_MeasureValue class attributes and methods

# behaviour_CommunicationAction class attributes and methods

# Action class attributes and methods

# behaviour_BehaviourContainer class attributes and methods

# behaviour_DynamicRobot class attributes and methods
behaviour_DynamicRobot_status: Property = Property(name="status", type=StringType)
behaviour_DynamicRobot.attributes={behaviour_DynamicRobot_status}

# behaviour_TaskExecution class attributes and methods
behaviour_TaskExecution_status: Property = Property(name="status", type=StringType)
behaviour_TaskExecution.attributes={behaviour_TaskExecution_status}

# behaviour_Action class attributes and methods

# behaviour_Task class attributes and methods

# behaviour_UnicastCommunication class attributes and methods

# CommunicationAction class attributes and methods

# behaviour_MulticastCommunication class attributes and methods

# behaviour_BroadcastCommunication class attributes and methods

# behaviour_MessageRepository class attributes and methods

# behaviour_Robot class attributes and methods

# behaviour_RobotCollaboration class attributes and methods

# behaviour_DetectedObject class attributes and methods
behaviour_DetectedObject_obstacle: Property = Property(name="obstacle", type=BooleanType)
behaviour_DetectedObject.attributes={behaviour_DetectedObject_obstacle}

# PropertyKeyContainer class attributes and methods

# behaviour_Capability class attributes and methods

# behaviour_CapabilityProperties class attributes and methods

# behaviour_TaskDescriptor class attributes and methods

# Relationships
taskRequirements3: BinaryAssociation = BinaryAssociation(
    name="taskRequirements3",
    ends={
        Property(name="behaviour_TaskRequirement", type=behaviour_BehaviourContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_BehaviourContainer4", type=behaviour_TaskRequirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
behaviourKeysContainer5: BinaryAssociation = BinaryAssociation(
    name="behaviourKeysContainer5",
    ends={
        Property(name="behaviour_BehaviouralPropertyKeyContainer", type=behaviour_BehaviourContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_BehaviourContainer6", type=behaviour_BehaviouralPropertyKeyContainer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
involvedTaskExecutions7: BinaryAssociation = BinaryAssociation(
    name="involvedTaskExecutions7",
    ends={
        Property(name="behaviour_TaskExecution8", type=behaviour_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Message", type=behaviour_TaskExecution, multiplicity=Multiplicity(0, 9999))
    }
)
properties9: BinaryAssociation = BinaryAssociation(
    name="properties9",
    ends={
        Property(name="behaviour_Property", type=behaviour_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Message10", type=behaviour_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredObjects11: BinaryAssociation = BinaryAssociation(
    name="referredObjects11",
    ends={
        Property(name="behaviour_AreaObject", type=behaviour_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Message12", type=behaviour_AreaObject, multiplicity=Multiplicity(0, 9999))
    }
)
TTL13: BinaryAssociation = BinaryAssociation(
    name="TTL13",
    ends={
        Property(name="behaviour_MeasureValue", type=behaviour_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Message14", type=behaviour_MeasureValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
follows16: BinaryAssociation = BinaryAssociation(
    name="follows16",
    ends={
        Property(name="behaviour_Message17", type=behaviour_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Message15", type=behaviour_Message, multiplicity=Multiplicity(0, 1))
    }
)
dynamicRobots0: BinaryAssociation = BinaryAssociation(
    name="dynamicRobots0",
    ends={
        Property(name="behaviour_DynamicRobot", type=behaviour_BehaviourContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_BehaviourContainer", type=behaviour_DynamicRobot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskExecutions1: BinaryAssociation = BinaryAssociation(
    name="taskExecutions1",
    ends={
        Property(name="behaviour_TaskExecution", type=behaviour_BehaviourContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_BehaviourContainer2", type=behaviour_TaskExecution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sendedMessages29: BinaryAssociation = BinaryAssociation(
    name="sendedMessages29",
    ends={
        Property(name="behaviour_Message31", type=behaviour_MessageRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_MessageRepository30", type=behaviour_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties32: BinaryAssociation = BinaryAssociation(
    name="properties32",
    ends={
        Property(name="behaviour_Property33", type=behaviour_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Action", type=behaviour_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
currentTaskExecution34: BinaryAssociation = BinaryAssociation(
    name="currentTaskExecution34",
    ends={
        Property(name="behaviour_TaskExecution36", type=behaviour_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Action35", type=behaviour_TaskExecution, multiplicity=Multiplicity(0, 1))
    }
)
currentTask37: BinaryAssociation = BinaryAssociation(
    name="currentTask37",
    ends={
        Property(name="behaviour_Task", type=behaviour_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Action38", type=behaviour_Task, multiplicity=Multiplicity(0, 1))
    }
)
executors39: BinaryAssociation = BinaryAssociation(
    name="executors39",
    ends={
        Property(name="behaviour_DynamicRobot41", type=behaviour_TaskExecution, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_TaskExecution40", type=behaviour_DynamicRobot, multiplicity=Multiplicity(0, 9999))
    }
)
executionTime42: BinaryAssociation = BinaryAssociation(
    name="executionTime42",
    ends={
        Property(name="behaviour_MeasureValue44", type=behaviour_TaskExecution, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_TaskExecution43", type=behaviour_MeasureValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
message18: BinaryAssociation = BinaryAssociation(
    name="message18",
    ends={
        Property(name="behaviour_Message19", type=behaviour_CommunicationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_CommunicationAction", type=behaviour_Message, multiplicity=Multiplicity(1, 1))
    }
)
target20: BinaryAssociation = BinaryAssociation(
    name="target20",
    ends={
        Property(name="behaviour_DynamicRobot21", type=behaviour_UnicastCommunication, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_UnicastCommunication", type=behaviour_DynamicRobot, multiplicity=Multiplicity(1, 1))
    }
)
targets22: BinaryAssociation = BinaryAssociation(
    name="targets22",
    ends={
        Property(name="behaviour_DynamicRobot23", type=behaviour_MulticastCommunication, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_MulticastCommunication", type=behaviour_DynamicRobot, multiplicity=Multiplicity(1, 9999))
    }
)
targets24: BinaryAssociation = BinaryAssociation(
    name="targets24",
    ends={
        Property(name="behaviour_DynamicRobot25", type=behaviour_BroadcastCommunication, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_BroadcastCommunication", type=behaviour_DynamicRobot, multiplicity=Multiplicity(1, 9999))
    }
)
robot26: BinaryAssociation = BinaryAssociation(
    name="robot26",
    ends={
        Property(name="DynamicRobot", type=behaviour_MessageRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="messageRepository", type=behaviour_DynamicRobot, multiplicity=Multiplicity(1, 1))
    }
)
receivedMessages27: BinaryAssociation = BinaryAssociation(
    name="receivedMessages27",
    ends={
        Property(name="behaviour_Message28", type=behaviour_MessageRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_MessageRepository", type=behaviour_Message, multiplicity=Multiplicity(0, 9999))
    }
)
object57: BinaryAssociation = BinaryAssociation(
    name="object57",
    ends={
        Property(name="behaviour_AreaObject58", type=behaviour_DetectedObject, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_DetectedObject", type=behaviour_AreaObject, multiplicity=Multiplicity(1, 1))
    }
)
robot59: BinaryAssociation = BinaryAssociation(
    name="robot59",
    ends={
        Property(name="behaviour_Robot", type=behaviour_DynamicRobot, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_DynamicRobot60", type=behaviour_Robot, multiplicity=Multiplicity(1, 1))
    }
)
detectedObjects61: BinaryAssociation = BinaryAssociation(
    name="detectedObjects61",
    ends={
        Property(name="behaviour_DetectedObject63", type=behaviour_DynamicRobot, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_DynamicRobot62", type=behaviour_DetectedObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collaborations64: BinaryAssociation = BinaryAssociation(
    name="collaborations64",
    ends={
        Property(name="behaviour_RobotCollaboration66", type=behaviour_DynamicRobot, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_DynamicRobot65", type=behaviour_RobotCollaboration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageRepository67: BinaryAssociation = BinaryAssociation(
    name="messageRepository67",
    ends={
        Property(name="MessageRepository", type=behaviour_DynamicRobot, multiplicity=Multiplicity(1, 1)),
        Property(name="robot", type=behaviour_MessageRepository, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actions68: BinaryAssociation = BinaryAssociation(
    name="actions68",
    ends={
        Property(name="behaviour_Action70", type=behaviour_DynamicRobot, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_DynamicRobot69", type=behaviour_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
executedTasks71: BinaryAssociation = BinaryAssociation(
    name="executedTasks71",
    ends={
        Property(name="behaviour_TaskExecution73", type=behaviour_DynamicRobot, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_DynamicRobot72", type=behaviour_TaskExecution, multiplicity=Multiplicity(0, 9999))
    }
)
task45: BinaryAssociation = BinaryAssociation(
    name="task45",
    ends={
        Property(name="behaviour_Task47", type=behaviour_TaskExecution, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_TaskExecution46", type=behaviour_Task, multiplicity=Multiplicity(1, 1))
    }
)
requirement48: BinaryAssociation = BinaryAssociation(
    name="requirement48",
    ends={
        Property(name="TaskRequirement", type=behaviour_TaskExecution, multiplicity=Multiplicity(1, 1)),
        Property(name="taskExecution", type=behaviour_TaskRequirement, multiplicity=Multiplicity(0, 1))
    }
)
collaborator49: BinaryAssociation = BinaryAssociation(
    name="collaborator49",
    ends={
        Property(name="behaviour_DynamicRobot50", type=behaviour_RobotCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_RobotCollaboration", type=behaviour_DynamicRobot, multiplicity=Multiplicity(1, 1))
    }
)
availabilityRange51: BinaryAssociation = BinaryAssociation(
    name="availabilityRange51",
    ends={
        Property(name="behaviour_MeasureValue53", type=behaviour_RobotCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_RobotCollaboration52", type=behaviour_MeasureValue, multiplicity=Multiplicity(0, 1))
    }
)
properties54: BinaryAssociation = BinaryAssociation(
    name="properties54",
    ends={
        Property(name="behaviour_Property56", type=behaviour_RobotCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_RobotCollaboration55", type=behaviour_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskExecution74: BinaryAssociation = BinaryAssociation(
    name="taskExecution74",
    ends={
        Property(name="TaskExecution", type=behaviour_TaskRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="requirement", type=behaviour_TaskExecution, multiplicity=Multiplicity(1, 1))
    }
)
prerequisite75: BinaryAssociation = BinaryAssociation(
    name="prerequisite75",
    ends={
        Property(name="behaviour_TaskExecution77", type=behaviour_TaskRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_TaskRequirement76", type=behaviour_TaskExecution, multiplicity=Multiplicity(0, 1))
    }
)
properties78: BinaryAssociation = BinaryAssociation(
    name="properties78",
    ends={
        Property(name="behaviour_Property80", type=behaviour_TaskRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_TaskRequirement79", type=behaviour_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredCapabilities81: BinaryAssociation = BinaryAssociation(
    name="requiredCapabilities81",
    ends={
        Property(name="behaviour_Capability", type=behaviour_TaskRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_TaskRequirement82", type=behaviour_Capability, multiplicity=Multiplicity(0, 9999))
    }
)
capabilityProperties83: BinaryAssociation = BinaryAssociation(
    name="capabilityProperties83",
    ends={
        Property(name="behaviour_CapabilityProperties", type=behaviour_TaskRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_TaskRequirement84", type=behaviour_CapabilityProperties, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
descriptor85: BinaryAssociation = BinaryAssociation(
    name="descriptor85",
    ends={
        Property(name="behaviour_TaskDescriptor", type=behaviour_TaskRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_TaskRequirement86", type=behaviour_TaskDescriptor, multiplicity=Multiplicity(0, 1))
    }
)
task87: BinaryAssociation = BinaryAssociation(
    name="task87",
    ends={
        Property(name="behaviour_Task89", type=behaviour_TaskRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_TaskRequirement88", type=behaviour_Task, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_behaviour_Message_NamedElement = Generalization(general=NamedElement, specific=behaviour_Message)
gen_behaviour_CommunicationAction_Action = Generalization(general=Action, specific=behaviour_CommunicationAction)
gen_behaviour_Action_NamedElement = Generalization(general=NamedElement, specific=behaviour_Action)
gen_behaviour_TaskExecution_NamedElement = Generalization(general=NamedElement, specific=behaviour_TaskExecution)
gen_behaviour_UnicastCommunication_CommunicationAction = Generalization(general=CommunicationAction, specific=behaviour_UnicastCommunication)
gen_behaviour_MulticastCommunication_CommunicationAction = Generalization(general=CommunicationAction, specific=behaviour_MulticastCommunication)
gen_behaviour_BroadcastCommunication_CommunicationAction = Generalization(general=CommunicationAction, specific=behaviour_BroadcastCommunication)
gen_behaviour_MessageRepository_NamedElement = Generalization(general=NamedElement, specific=behaviour_MessageRepository)
gen_behaviour_DynamicRobot_NamedElement = Generalization(general=NamedElement, specific=behaviour_DynamicRobot)
gen_behaviour_TaskRequirement_NamedElement = Generalization(general=NamedElement, specific=behaviour_TaskRequirement)
gen_behaviour_BehaviouralPropertyKeyContainer_PropertyKeyContainer = Generalization(general=PropertyKeyContainer, specific=behaviour_BehaviouralPropertyKeyContainer)

# Domain Model
domain_model = DomainModel(
    name="behaviour",
    types={behaviour_TaskRequirement, behaviour_BehaviouralPropertyKeyContainer, behaviour_Message, NamedElement, behaviour_Property, behaviour_AreaObject, behaviour_MeasureValue, behaviour_CommunicationAction, Action, behaviour_BehaviourContainer, behaviour_DynamicRobot, behaviour_TaskExecution, behaviour_Action, behaviour_Task, behaviour_UnicastCommunication, CommunicationAction, behaviour_MulticastCommunication, behaviour_BroadcastCommunication, behaviour_MessageRepository, behaviour_Robot, behaviour_RobotCollaboration, behaviour_DetectedObject, PropertyKeyContainer, behaviour_Capability, behaviour_CapabilityProperties, behaviour_TaskDescriptor, RobotStatus, TaskExecutionStatus},
    associations={taskRequirements3, behaviourKeysContainer5, involvedTaskExecutions7, properties9, referredObjects11, TTL13, follows16, dynamicRobots0, taskExecutions1, sendedMessages29, properties32, currentTaskExecution34, currentTask37, executors39, executionTime42, message18, target20, targets22, targets24, robot26, receivedMessages27, object57, robot59, detectedObjects61, collaborations64, messageRepository67, actions68, executedTasks71, task45, requirement48, collaborator49, availabilityRange51, properties54, taskExecution74, prerequisite75, properties78, requiredCapabilities81, capabilityProperties83, descriptor85, task87},
    generalizations={gen_behaviour_Message_NamedElement, gen_behaviour_CommunicationAction_Action, gen_behaviour_Action_NamedElement, gen_behaviour_TaskExecution_NamedElement, gen_behaviour_UnicastCommunication_CommunicationAction, gen_behaviour_MulticastCommunication_CommunicationAction, gen_behaviour_BroadcastCommunication_CommunicationAction, gen_behaviour_MessageRepository_NamedElement, gen_behaviour_DynamicRobot_NamedElement, gen_behaviour_TaskRequirement_NamedElement, gen_behaviour_BehaviouralPropertyKeyContainer_PropertyKeyContainer},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)