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
communication_mode: Enumeration = Enumeration(
    name="communication_mode",
    literals={
            EnumerationLiteral(name="broadcast"),
			EnumerationLiteral(name="unicast"),
			EnumerationLiteral(name="logicast")
    }
)

RoutingType: Enumeration = Enumeration(
    name="RoutingType",
    literals={
            EnumerationLiteral(name="ch2ch"),
			EnumerationLiteral(name="node2node")
    }
)

TimerType: Enumeration = Enumeration(
    name="TimerType",
    literals={
            EnumerationLiteral(name="periodic"),
			EnumerationLiteral(name="once")
    }
)

optimizationLevel: Enumeration = Enumeration(
    name="optimizationLevel",
    literals={
            EnumerationLiteral(name="dontCare"),
			EnumerationLiteral(name="medium"),
			EnumerationLiteral(name="high"),
			EnumerationLiteral(name="critical")
    }
)

CommType: Enumeration = Enumeration(
    name="CommType",
    literals={
            EnumerationLiteral(name="broadcast"),
			EnumerationLiteral(name="unicast"),
			EnumerationLiteral(name="logicast")
    }
)

PlatformType: Enumeration = Enumeration(
    name="PlatformType",
    literals={
            EnumerationLiteral(name="Contiki"),
			EnumerationLiteral(name="TinyOS")
    }
)

MoteType: Enumeration = Enumeration(
    name="MoteType",
    literals={
            EnumerationLiteral(name="Z1"),
			EnumerationLiteral(name="TelosB"),
			EnumerationLiteral(name="Iris")
    }
)

routingProtocol: Enumeration = Enumeration(
    name="routingProtocol",
    literals={
            
    }
)

rdcType: Enumeration = Enumeration(
    name="rdcType",
    literals={
            
    }
)

macType: Enumeration = Enumeration(
    name="macType",
    literals={
            
    }
)

netstackType: Enumeration = Enumeration(
    name="netstackType",
    literals={
            
    }
)

sleepType: Enumeration = Enumeration(
    name="sleepType",
    literals={
            
    }
)

# Classes
wsn_Objectives = Class(name="wsn::Objectives")
wsn_Sensor = Class(name="wsn::Sensor")
wsn_ISensor = Class(name="wsn::ISensor")
wsn_Actuator = Class(name="wsn::Actuator")
wsn_IActuator = Class(name="wsn::IActuator")
wsn_Actuating = Class(name="wsn::Actuating")
wsn_Task = Class(name="wsn::Task")
wsn_Data = Class(name="wsn::Data")
wsn_StateMachine = Class(name="wsn::StateMachine")
wsn_Sensing = Class(name="wsn::Sensing")
wsn_Node = Class(name="wsn::Node")
wsn_Event = Class(name="wsn::Event", is_abstract=True)
wsn_Message = Class(name="wsn::Message")
Event = Class(name="Event")
unnamed_class = Class(name="")
wsn_Network = Class(name="wsn::Network")
wsn_Communication = Class(name="wsn::Communication")
wsn_Mode = Class(name="wsn::Mode")
wsn_IData = Class(name="wsn::IData")
wsn_State = Class(name="wsn::State")
wsn_Activity = Class(name="wsn::Activity")
wsn_Transition = Class(name="wsn::Transition")
wsn_InitialState = Class(name="wsn::InitialState")
State = Class(name="State")
wsn_FinalState = Class(name="wsn::FinalState")
wsn_Cluster = Class(name="wsn::Cluster")
wsn_ClusterHead = Class(name="wsn::ClusterHead")
wsn_Election = Class(name="wsn::Election")
wsn_Formation = Class(name="wsn::Formation")
Node = Class(name="Node")
wsn_Sink = Class(name="wsn::Sink")
wsn_Lifeline = Class(name="wsn::Lifeline")
wsn_InteractionMsg = Class(name="wsn::InteractionMsg")
wsn_InitialLifeline = Class(name="wsn::InitialLifeline")
Lifeline = Class(name="Lifeline")
wsn_Timing = Class(name="wsn::Timing")
wsn_Timer = Class(name="wsn::Timer")
wsn_WirelessLink = Class(name="wsn::WirelessLink")
wsn_Comm = Class(name="wsn::Comm")
wsn_Receiver = Class(name="wsn::Receiver")
Comm = Class(name="Comm")
wsn_Sender = Class(name="wsn::Sender")
wsn_NodeRole = Class(name="wsn::NodeRole")
wsn_SensorRole = Class(name="wsn::SensorRole")
wsn_ActuatorRole = Class(name="wsn::ActuatorRole")
wsn_Button = Class(name="wsn::Button")
Sensor = Class(name="Sensor")
wsn_LED = Class(name="wsn::LED")
Actuator = Class(name="Actuator")
wsn_Platform = Class(name="wsn::Platform")
wsn_Resource = Class(name="wsn::Resource")
wsn_Parameters = Class(name="wsn::Parameters")
wsn_EnergySource = Class(name="wsn::EnergySource", is_abstract=True)
wsn_Harvester = Class(name="wsn::Harvester")
EnergySource = Class(name="EnergySource")
wsn_Battery = Class(name="wsn::Battery")
wsn_Interface = Class(name="wsn::Interface", is_abstract=True)
Interface = Class(name="Interface")

# wsn_Objectives class attributes and methods
wsn_Objectives_lifetime: Property = Property(name="lifetime", type=StringType)
wsn_Objectives_memfootprint: Property = Property(name="memfootprint", type=StringType)
wsn_Objectives_delay: Property = Property(name="delay", type=StringType)
wsn_Objectives_packetloss: Property = Property(name="packetloss", type=StringType)
wsn_Objectives.attributes={wsn_Objectives_delay, wsn_Objectives_lifetime, wsn_Objectives_packetloss, wsn_Objectives_memfootprint}

# wsn_Sensor class attributes and methods
wsn_Sensor_data: Property = Property(name="data", type=FloatType)
wsn_Sensor.attributes={wsn_Sensor_data}

# wsn_ISensor class attributes and methods

# wsn_Actuator class attributes and methods
wsn_Actuator_data: Property = Property(name="data", type=FloatType)
wsn_Actuator.attributes={wsn_Actuator_data}

# wsn_IActuator class attributes and methods

# wsn_Actuating class attributes and methods

# wsn_Task class attributes and methods
wsn_Task_priority: Property = Property(name="priority", type=IntegerType)
wsn_Task.attributes={wsn_Task_priority}

# wsn_Data class attributes and methods

# wsn_StateMachine class attributes and methods

# wsn_Sensing class attributes and methods

# wsn_Node class attributes and methods

# wsn_Event class attributes and methods

# wsn_Message class attributes and methods

# Event class attributes and methods

#  class attributes and methods

# wsn_Network class attributes and methods

# wsn_Communication class attributes and methods

# wsn_Mode class attributes and methods
wsn_Mode_mode_t: Property = Property(name="mode_t", type=StringType)
wsn_Mode_destination: Property = Property(name="destination", type=FloatType)
wsn_Mode.attributes={wsn_Mode_destination, wsn_Mode_mode_t}

# wsn_IData class attributes and methods

# wsn_State class attributes and methods

# wsn_Activity class attributes and methods

# wsn_Transition class attributes and methods
wsn_Transition_guard: Property = Property(name="guard", type=StringType)
wsn_Transition.attributes={wsn_Transition_guard}

# wsn_InitialState class attributes and methods

# State class attributes and methods

# wsn_FinalState class attributes and methods

# wsn_Cluster class attributes and methods

# wsn_ClusterHead class attributes and methods

# wsn_Election class attributes and methods

# wsn_Formation class attributes and methods
wsn_Formation_routing: Property = Property(name="routing", type=StringType)
wsn_Formation.attributes={wsn_Formation_routing}

# Node class attributes and methods

# wsn_Sink class attributes and methods

# wsn_Lifeline class attributes and methods

# wsn_InteractionMsg class attributes and methods

# wsn_InitialLifeline class attributes and methods

# Lifeline class attributes and methods

# wsn_Timing class attributes and methods

# wsn_Timer class attributes and methods
wsn_Timer_time: Property = Property(name="time", type=IntegerType)
wsn_Timer_type: Property = Property(name="type", type=StringType)
wsn_Timer.attributes={wsn_Timer_type, wsn_Timer_time}

# wsn_WirelessLink class attributes and methods

# wsn_Comm class attributes and methods

# wsn_Receiver class attributes and methods
wsn_Receiver_type: Property = Property(name="type", type=StringType)
wsn_Receiver.attributes={wsn_Receiver_type}

# Comm class attributes and methods

# wsn_Sender class attributes and methods
wsn_Sender_type: Property = Property(name="type", type=StringType)
wsn_Sender.attributes={wsn_Sender_type}

# wsn_NodeRole class attributes and methods

# wsn_SensorRole class attributes and methods

# wsn_ActuatorRole class attributes and methods

# wsn_Button class attributes and methods

# Sensor class attributes and methods

# wsn_LED class attributes and methods

# Actuator class attributes and methods

# wsn_Platform class attributes and methods
wsn_Platform_platform: Property = Property(name="platform", type=StringType)
wsn_Platform_mote: Property = Property(name="mote", type=StringType)
wsn_Platform.attributes={wsn_Platform_platform, wsn_Platform_mote}

# wsn_Resource class attributes and methods
wsn_Resource_memory: Property = Property(name="memory", type=IntegerType)
wsn_Resource_flash: Property = Property(name="flash", type=IntegerType)
wsn_Resource.attributes={wsn_Resource_memory, wsn_Resource_flash}

# wsn_Parameters class attributes and methods
wsn_Parameters_netStack: Property = Property(name="netStack", type=StringType)
wsn_Parameters_macProtocol: Property = Property(name="macProtocol", type=StringType)
wsn_Parameters_rdcProtocol: Property = Property(name="rdcProtocol", type=StringType)
wsn_Parameters_routingProtocol: Property = Property(name="routingProtocol", type=StringType)
wsn_Parameters_sleepScheduling: Property = Property(name="sleepScheduling", type=StringType)
wsn_Parameters.attributes={wsn_Parameters_netStack, wsn_Parameters_rdcProtocol, wsn_Parameters_sleepScheduling, wsn_Parameters_macProtocol, wsn_Parameters_routingProtocol}

# wsn_EnergySource class attributes and methods

# wsn_Harvester class attributes and methods

# EnergySource class attributes and methods

# wsn_Battery class attributes and methods
wsn_Battery_full: Property = Property(name="full", type=FloatType)
wsn_Battery_empty: Property = Property(name="empty", type=FloatType)
wsn_Battery.attributes={wsn_Battery_empty, wsn_Battery_full}

# wsn_Interface class attributes and methods

# Interface class attributes and methods

# Relationships
interface0: BinaryAssociation = BinaryAssociation(
    name="interface0",
    ends={
        Property(name="wsn_ISensor", type=wsn_Sensor, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Sensor", type=wsn_ISensor, multiplicity=Multiplicity(0, 1))
    }
)
interface1: BinaryAssociation = BinaryAssociation(
    name="interface1",
    ends={
        Property(name="wsn_IActuator", type=wsn_Actuator, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Actuator", type=wsn_IActuator, multiplicity=Multiplicity(0, 1))
    }
)
task2: BinaryAssociation = BinaryAssociation(
    name="task2",
    ends={
        Property(name="wsn_Task", type=wsn_Actuating, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Actuating", type=wsn_Task, multiplicity=Multiplicity(0, 1))
    }
)
actuator3: BinaryAssociation = BinaryAssociation(
    name="actuator3",
    ends={
        Property(name="wsn_Actuator5", type=wsn_Actuating, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Actuating4", type=wsn_Actuator, multiplicity=Multiplicity(0, 1))
    }
)
data6: BinaryAssociation = BinaryAssociation(
    name="data6",
    ends={
        Property(name="wsn_Data", type=wsn_Actuating, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Actuating7", type=wsn_Data, multiplicity=Multiplicity(0, 1))
    }
)
behavior8: BinaryAssociation = BinaryAssociation(
    name="behavior8",
    ends={
        Property(name="wsn_StateMachine", type=wsn_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Task9", type=wsn_StateMachine, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
task10: BinaryAssociation = BinaryAssociation(
    name="task10",
    ends={
        Property(name="wsn_Task11", type=wsn_Sensing, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Sensing", type=wsn_Task, multiplicity=Multiplicity(0, 1))
    }
)
sensor12: BinaryAssociation = BinaryAssociation(
    name="sensor12",
    ends={
        Property(name="wsn_Sensor14", type=wsn_Sensing, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Sensing13", type=wsn_Sensor, multiplicity=Multiplicity(0, 1))
    }
)
data15: BinaryAssociation = BinaryAssociation(
    name="data15",
    ends={
        Property(name="wsn_Data17", type=wsn_Sensing, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Sensing16", type=wsn_Data, multiplicity=Multiplicity(0, 1))
    }
)
task18: BinaryAssociation = BinaryAssociation(
    name="task18",
    ends={
        Property(name="wsn_Task19", type=wsn_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Node", type=wsn_Task, multiplicity=Multiplicity(1, 10), is_composite=True)
    }
)
msgSource20: BinaryAssociation = BinaryAssociation(
    name="msgSource20",
    ends={
        Property(name="wsn_Task21", type=wsn_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Message", type=wsn_Task, multiplicity=Multiplicity(0, 1))
    }
)
msgTarget22: BinaryAssociation = BinaryAssociation(
    name="msgTarget22",
    ends={
        Property(name="wsn_Task24", type=wsn_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Message23", type=wsn_Task, multiplicity=Multiplicity(0, 1))
    }
)
data25: BinaryAssociation = BinaryAssociation(
    name="data25",
    ends={
        Property(name="wsn_Data27", type=wsn_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Message26", type=wsn_Data, multiplicity=Multiplicity(0, 1))
    }
)
objectives28: BinaryAssociation = BinaryAssociation(
    name="objectives28",
    ends={
        Property(name="wsn_Objectives", type=wsn_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Network", type=wsn_Objectives, multiplicity=Multiplicity(0, 1))
    }
)
nodes29: BinaryAssociation = BinaryAssociation(
    name="nodes29",
    ends={
        Property(name="wsn_Network30", type=wsn_Node, multiplicity=Multiplicity(0, 10), is_composite=True),
        Property(name="wsn_Node31", type=wsn_Network, multiplicity=Multiplicity(1, 1))
    }
)
commSource32: BinaryAssociation = BinaryAssociation(
    name="commSource32",
    ends={
        Property(name="wsn_Node33", type=wsn_Communication, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Communication", type=wsn_Node, multiplicity=Multiplicity(0, 1))
    }
)
commDestination34: BinaryAssociation = BinaryAssociation(
    name="commDestination34",
    ends={
        Property(name="wsn_Node36", type=wsn_Communication, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Communication35", type=wsn_Node, multiplicity=Multiplicity(0, 1))
    }
)
originating37: BinaryAssociation = BinaryAssociation(
    name="originating37",
    ends={
        Property(name="wsn_Task39", type=wsn_Communication, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Communication38", type=wsn_Task, multiplicity=Multiplicity(0, 1))
    }
)
receiving40: BinaryAssociation = BinaryAssociation(
    name="receiving40",
    ends={
        Property(name="wsn_Task42", type=wsn_Communication, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Communication41", type=wsn_Task, multiplicity=Multiplicity(0, 1))
    }
)
mode43: BinaryAssociation = BinaryAssociation(
    name="mode43",
    ends={
        Property(name="wsn_Mode", type=wsn_Communication, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Communication44", type=wsn_Mode, multiplicity=Multiplicity(0, 1))
    }
)
interface45: BinaryAssociation = BinaryAssociation(
    name="interface45",
    ends={
        Property(name="wsn_IData", type=wsn_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Data46", type=wsn_IData, multiplicity=Multiplicity(0, 1))
    }
)
entryActivity47: BinaryAssociation = BinaryAssociation(
    name="entryActivity47",
    ends={
        Property(name="wsn_Activity", type=wsn_State, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_State", type=wsn_Activity, multiplicity=Multiplicity(0, 1))
    }
)
exitActivity48: BinaryAssociation = BinaryAssociation(
    name="exitActivity48",
    ends={
        Property(name="wsn_Activity50", type=wsn_State, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_State49", type=wsn_Activity, multiplicity=Multiplicity(0, 1))
    }
)
transitionFrom51: BinaryAssociation = BinaryAssociation(
    name="transitionFrom51",
    ends={
        Property(name="wsn_State52", type=wsn_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Transition", type=wsn_State, multiplicity=Multiplicity(0, 1))
    }
)
transitionTo53: BinaryAssociation = BinaryAssociation(
    name="transitionTo53",
    ends={
        Property(name="wsn_State55", type=wsn_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Transition54", type=wsn_State, multiplicity=Multiplicity(0, 1))
    }
)
trigger56: BinaryAssociation = BinaryAssociation(
    name="trigger56",
    ends={
        Property(name="wsn_Event", type=wsn_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Transition57", type=wsn_Event, multiplicity=Multiplicity(0, 1))
    }
)
node58: BinaryAssociation = BinaryAssociation(
    name="node58",
    ends={
        Property(name="wsn_Node59", type=wsn_Cluster, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Cluster", type=wsn_Node, multiplicity=Multiplicity(0, 9999))
    }
)
head60: BinaryAssociation = BinaryAssociation(
    name="head60",
    ends={
        Property(name="wsn_ClusterHead", type=wsn_Cluster, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Cluster61", type=wsn_ClusterHead, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
election62: BinaryAssociation = BinaryAssociation(
    name="election62",
    ends={
        Property(name="wsn_Election", type=wsn_Cluster, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Cluster63", type=wsn_Election, multiplicity=Multiplicity(0, 1))
    }
)
formation64: BinaryAssociation = BinaryAssociation(
    name="formation64",
    ends={
        Property(name="wsn_Formation", type=wsn_Cluster, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Cluster65", type=wsn_Formation, multiplicity=Multiplicity(0, 1))
    }
)
msgFrom66: BinaryAssociation = BinaryAssociation(
    name="msgFrom66",
    ends={
        Property(name="wsn_Lifeline", type=wsn_InteractionMsg, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_InteractionMsg", type=wsn_Lifeline, multiplicity=Multiplicity(0, 1))
    }
)
msgTo67: BinaryAssociation = BinaryAssociation(
    name="msgTo67",
    ends={
        Property(name="wsn_Lifeline69", type=wsn_InteractionMsg, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_InteractionMsg68", type=wsn_Lifeline, multiplicity=Multiplicity(0, 1))
    }
)
electionActivity70: BinaryAssociation = BinaryAssociation(
    name="electionActivity70",
    ends={
        Property(name="wsn_Activity72", type=wsn_Election, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Election71", type=wsn_Activity, multiplicity=Multiplicity(1, 1))
    }
)
formationActivity73: BinaryAssociation = BinaryAssociation(
    name="formationActivity73",
    ends={
        Property(name="wsn_Activity75", type=wsn_Formation, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Formation74", type=wsn_Activity, multiplicity=Multiplicity(1, 1))
    }
)
timer76: BinaryAssociation = BinaryAssociation(
    name="timer76",
    ends={
        Property(name="wsn_Timer", type=wsn_Timing, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Timing", type=wsn_Timer, multiplicity=Multiplicity(0, 1))
    }
)
task77: BinaryAssociation = BinaryAssociation(
    name="task77",
    ends={
        Property(name="wsn_Task79", type=wsn_Timing, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Timing78", type=wsn_Task, multiplicity=Multiplicity(0, 1))
    }
)
task80: BinaryAssociation = BinaryAssociation(
    name="task80",
    ends={
        Property(name="wsn_Task81", type=wsn_WirelessLink, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_WirelessLink", type=wsn_Task, multiplicity=Multiplicity(0, 1))
    }
)
comm82: BinaryAssociation = BinaryAssociation(
    name="comm82",
    ends={
        Property(name="wsn_Comm", type=wsn_WirelessLink, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_WirelessLink83", type=wsn_Comm, multiplicity=Multiplicity(0, 1))
    }
)
data84: BinaryAssociation = BinaryAssociation(
    name="data84",
    ends={
        Property(name="wsn_Data86", type=wsn_Comm, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_Comm85", type=wsn_Data, multiplicity=Multiplicity(0, 1))
    }
)
node87: BinaryAssociation = BinaryAssociation(
    name="node87",
    ends={
        Property(name="wsn_Node88", type=wsn_NodeRole, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_NodeRole", type=wsn_Node, multiplicity=Multiplicity(0, 1))
    }
)
sensor89: BinaryAssociation = BinaryAssociation(
    name="sensor89",
    ends={
        Property(name="wsn_Sensor90", type=wsn_SensorRole, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_SensorRole", type=wsn_Sensor, multiplicity=Multiplicity(0, 1))
    }
)
actuator91: BinaryAssociation = BinaryAssociation(
    name="actuator91",
    ends={
        Property(name="wsn_Actuator92", type=wsn_ActuatorRole, multiplicity=Multiplicity(1, 1)),
        Property(name="wsn_ActuatorRole", type=wsn_Actuator, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_wsn_Message_Event = Generalization(general=Event, specific=wsn_Message)
gen_wsn_Message_ = Generalization(general=unnamed_class, specific=wsn_Message)
gen_wsn_InitialState_State = Generalization(general=State, specific=wsn_InitialState)
gen_wsn_InitialState_ = Generalization(general=unnamed_class, specific=wsn_InitialState)
gen_wsn_FinalState_State = Generalization(general=State, specific=wsn_FinalState)
gen_wsn_FinalState_ = Generalization(general=unnamed_class, specific=wsn_FinalState)
gen_wsn_ClusterHead_Node = Generalization(general=Node, specific=wsn_ClusterHead)
gen_wsn_ClusterHead_ = Generalization(general=unnamed_class, specific=wsn_ClusterHead)
gen_wsn_Sink_Node = Generalization(general=Node, specific=wsn_Sink)
gen_wsn_Sink_ = Generalization(general=unnamed_class, specific=wsn_Sink)
gen_wsn_InitialLifeline_Lifeline = Generalization(general=Lifeline, specific=wsn_InitialLifeline)
gen_wsn_InitialLifeline_ = Generalization(general=unnamed_class, specific=wsn_InitialLifeline)
gen_wsn_Timing_Event = Generalization(general=Event, specific=wsn_Timing)
gen_wsn_Timing_ = Generalization(general=unnamed_class, specific=wsn_Timing)
gen_wsn_Comm_Event = Generalization(general=Event, specific=wsn_Comm)
gen_wsn_Comm_ = Generalization(general=unnamed_class, specific=wsn_Comm)
gen_wsn_Receiver_Comm = Generalization(general=Comm, specific=wsn_Receiver)
gen_wsn_Receiver_ = Generalization(general=unnamed_class, specific=wsn_Receiver)
gen_wsn_Sender_Comm = Generalization(general=Comm, specific=wsn_Sender)
gen_wsn_Sender_ = Generalization(general=unnamed_class, specific=wsn_Sender)
gen_wsn_NodeRole_Lifeline = Generalization(general=Lifeline, specific=wsn_NodeRole)
gen_wsn_NodeRole_ = Generalization(general=unnamed_class, specific=wsn_NodeRole)
gen_wsn_SensorRole_Lifeline = Generalization(general=Lifeline, specific=wsn_SensorRole)
gen_wsn_SensorRole_ = Generalization(general=unnamed_class, specific=wsn_SensorRole)
gen_wsn_ActuatorRole_Lifeline = Generalization(general=Lifeline, specific=wsn_ActuatorRole)
gen_wsn_ActuatorRole_ = Generalization(general=unnamed_class, specific=wsn_ActuatorRole)
gen_wsn_Button_Sensor = Generalization(general=Sensor, specific=wsn_Button)
gen_wsn_Button_ = Generalization(general=unnamed_class, specific=wsn_Button)
gen_wsn_LED_Actuator = Generalization(general=Actuator, specific=wsn_LED)
gen_wsn_LED_ = Generalization(general=unnamed_class, specific=wsn_LED)
gen_wsn_Harvester_EnergySource = Generalization(general=EnergySource, specific=wsn_Harvester)
gen_wsn_Harvester_ = Generalization(general=unnamed_class, specific=wsn_Harvester)
gen_wsn_Battery_EnergySource = Generalization(general=EnergySource, specific=wsn_Battery)
gen_wsn_Battery_ = Generalization(general=unnamed_class, specific=wsn_Battery)
gen_wsn_ISensor_Interface = Generalization(general=Interface, specific=wsn_ISensor)
gen_wsn_ISensor_ = Generalization(general=unnamed_class, specific=wsn_ISensor)
gen_wsn_IActuator_Interface = Generalization(general=Interface, specific=wsn_IActuator)
gen_wsn_IActuator_ = Generalization(general=unnamed_class, specific=wsn_IActuator)
gen_wsn_IData_Interface = Generalization(general=Interface, specific=wsn_IData)
gen_wsn_IData_ = Generalization(general=unnamed_class, specific=wsn_IData)

# Domain Model
domain_model = DomainModel(
    name="wsn",
    types={wsn_Objectives, wsn_Sensor, wsn_ISensor, wsn_Actuator, wsn_IActuator, wsn_Actuating, wsn_Task, wsn_Data, wsn_StateMachine, wsn_Sensing, wsn_Node, wsn_Event, wsn_Message, Event, unnamed_class, wsn_Network, wsn_Communication, wsn_Mode, wsn_IData, wsn_State, wsn_Activity, wsn_Transition, wsn_InitialState, State, wsn_FinalState, wsn_Cluster, wsn_ClusterHead, wsn_Election, wsn_Formation, Node, wsn_Sink, wsn_Lifeline, wsn_InteractionMsg, wsn_InitialLifeline, Lifeline, wsn_Timing, wsn_Timer, wsn_WirelessLink, wsn_Comm, wsn_Receiver, Comm, wsn_Sender, wsn_NodeRole, wsn_SensorRole, wsn_ActuatorRole, wsn_Button, Sensor, wsn_LED, Actuator, wsn_Platform, wsn_Resource, wsn_Parameters, wsn_EnergySource, wsn_Harvester, EnergySource, wsn_Battery, wsn_Interface, Interface, communication_mode, RoutingType, TimerType, optimizationLevel, CommType, PlatformType, MoteType, routingProtocol, rdcType, macType, netstackType, sleepType},
    associations={interface0, interface1, task2, actuator3, data6, behavior8, task10, sensor12, data15, task18, msgSource20, msgTarget22, data25, objectives28, nodes29, commSource32, commDestination34, originating37, receiving40, mode43, interface45, entryActivity47, exitActivity48, transitionFrom51, transitionTo53, trigger56, node58, head60, election62, formation64, msgFrom66, msgTo67, electionActivity70, formationActivity73, timer76, task77, task80, comm82, data84, node87, sensor89, actuator91},
    generalizations={gen_wsn_Message_Event, gen_wsn_Message_, gen_wsn_InitialState_State, gen_wsn_InitialState_, gen_wsn_FinalState_State, gen_wsn_FinalState_, gen_wsn_ClusterHead_Node, gen_wsn_ClusterHead_, gen_wsn_Sink_Node, gen_wsn_Sink_, gen_wsn_InitialLifeline_Lifeline, gen_wsn_InitialLifeline_, gen_wsn_Timing_Event, gen_wsn_Timing_, gen_wsn_Comm_Event, gen_wsn_Comm_, gen_wsn_Receiver_Comm, gen_wsn_Receiver_, gen_wsn_Sender_Comm, gen_wsn_Sender_, gen_wsn_NodeRole_Lifeline, gen_wsn_NodeRole_, gen_wsn_SensorRole_Lifeline, gen_wsn_SensorRole_, gen_wsn_ActuatorRole_Lifeline, gen_wsn_ActuatorRole_, gen_wsn_Button_Sensor, gen_wsn_Button_, gen_wsn_LED_Actuator, gen_wsn_LED_, gen_wsn_Harvester_EnergySource, gen_wsn_Harvester_, gen_wsn_Battery_EnergySource, gen_wsn_Battery_, gen_wsn_ISensor_Interface, gen_wsn_ISensor_, gen_wsn_IActuator_Interface, gen_wsn_IActuator_, gen_wsn_IData_Interface, gen_wsn_IData_},
    metadata=None
)
