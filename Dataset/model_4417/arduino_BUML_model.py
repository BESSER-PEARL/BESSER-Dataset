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
arduino_Sketch = Class(name="arduino::Sketch")
arduino_AbstractDevice = Class(name="arduino::AbstractDevice")
arduino_Precondition = Class(name="arduino::Precondition")
arduino_Sensor = Class(name="arduino::Sensor")
arduino_Handler = Class(name="arduino::Handler")
arduino_Interrupt = Class(name="arduino::Interrupt")
arduino_Poll = Class(name="arduino::Poll")
arduino_Task = Class(name="arduino::Task")
arduino_LoopItem = Class(name="arduino::LoopItem")
arduino_SystemDefinition = Class(name="arduino::SystemDefinition")
arduino_CommunicationParams = Class(name="arduino::CommunicationParams")
arduino_Message = Class(name="arduino::Message")
arduino_HighLevelOperation = Class(name="arduino::HighLevelOperation")
arduino_IODevice = Class(name="arduino::IODevice")
arduino_OutOnlyMessage = Class(name="arduino::OutOnlyMessage")
Message = Class(name="Message")
arduino_OutInMessage = Class(name="arduino::OutInMessage")
arduino_Dispatch = Class(name="arduino::Dispatch")
OutOnlyMessage = Class(name="OutOnlyMessage")
arduino_Request = Class(name="arduino::Request")
OutInMessage = Class(name="OutInMessage")
arduino_Invitation = Class(name="arduino::Invitation")
arduino_PortProtocol = Class(name="arduino::PortProtocol")
arduino_PortTCP = Class(name="arduino::PortTCP")
PortProtocol = Class(name="PortProtocol")
arduino_PortConnectionData = Class(name="arduino::PortConnectionData")
arduino_Precondition1 = Class(name="arduino::Precondition1")
arduino_EObject = Class(name="arduino::EObject")
arduino_EmptyPrecondition = Class(name="arduino::EmptyPrecondition")
arduino_SensorValuePrecondition = Class(name="arduino::SensorValuePrecondition")
arduino_Actuator = Class(name="arduino::Actuator")
AbstractDevice = Class(name="AbstractDevice")
arduino_ServeDispatch = Class(name="arduino::ServeDispatch")
arduino_AcceptInvitation = Class(name="arduino::AcceptInvitation")
arduino_Serial = Class(name="arduino::Serial")
SupportSpecification = Class(name="SupportSpecification")
arduino_TCP = Class(name="arduino::TCP")
arduino_SupportData = Class(name="arduino::SupportData")
arduino_ExplicitSupportData = Class(name="arduino::ExplicitSupportData")
SupportData = Class(name="SupportData")
arduino_OutOperation = Class(name="arduino::OutOperation")
HighLevelOperation = Class(name="HighLevelOperation")
arduino_InOperation = Class(name="arduino::InOperation")
arduino_InAcquireOperation = Class(name="arduino::InAcquireOperation")
InOperation = Class(name="InOperation")
arduino_SupportSpecification = Class(name="arduino::SupportSpecification")
arduino_DemandRequest = Class(name="arduino::DemandRequest")
OutOperation = Class(name="OutOperation")
arduino_ForwardDispatch = Class(name="arduino::ForwardDispatch")
arduino_AskInvitation = Class(name="arduino::AskInvitation")
arduino_GrantRequest = Class(name="arduino::GrantRequest")
InAcquireOperation = Class(name="InAcquireOperation")
arduino_IP = Class(name="arduino::IP")

# arduino_Sketch class attributes and methods
arduino_Sketch_name: Property = Property(name="name", type=StringType)
arduino_Sketch_hardware: Property = Property(name="hardware", type=StringType)
arduino_Sketch_defineSystem: Property = Property(name="defineSystem", type=BooleanType)
arduino_Sketch.attributes={arduino_Sketch_hardware, arduino_Sketch_name, arduino_Sketch_defineSystem}

# arduino_AbstractDevice class attributes and methods
arduino_AbstractDevice_name: Property = Property(name="name", type=StringType)
arduino_AbstractDevice_pin: Property = Property(name="pin", type=StringType)
arduino_AbstractDevice.attributes={arduino_AbstractDevice_name, arduino_AbstractDevice_pin}

# arduino_Precondition class attributes and methods
arduino_Precondition_op: Property = Property(name="op", type=StringType)
arduino_Precondition.attributes={arduino_Precondition_op}

# arduino_Sensor class attributes and methods
arduino_Sensor_analog: Property = Property(name="analog", type=BooleanType)
arduino_Sensor_pullup: Property = Property(name="pullup", type=BooleanType)
arduino_Sensor.attributes={arduino_Sensor_analog, arduino_Sensor_pullup}

# arduino_Handler class attributes and methods
arduino_Handler_name: Property = Property(name="name", type=StringType)
arduino_Handler.attributes={arduino_Handler_name}

# arduino_Interrupt class attributes and methods
arduino_Interrupt_name: Property = Property(name="name", type=StringType)
arduino_Interrupt_interruptKind: Property = Property(name="interruptKind", type=StringType)
arduino_Interrupt_eventKind: Property = Property(name="eventKind", type=StringType)
arduino_Interrupt.attributes={arduino_Interrupt_name, arduino_Interrupt_interruptKind, arduino_Interrupt_eventKind}

# arduino_Poll class attributes and methods
arduino_Poll_type: Property = Property(name="type", type=StringType)
arduino_Poll_l: Property = Property(name="l", type=IntegerType)
arduino_Poll_h: Property = Property(name="h", type=IntegerType)
arduino_Poll.attributes={arduino_Poll_h, arduino_Poll_type, arduino_Poll_l}

# arduino_Task class attributes and methods
arduino_Task_name: Property = Property(name="name", type=StringType)
arduino_Task_external: Property = Property(name="external", type=BooleanType)
arduino_Task.attributes={arduino_Task_external, arduino_Task_name}

# arduino_LoopItem class attributes and methods

# arduino_SystemDefinition class attributes and methods

# arduino_CommunicationParams class attributes and methods
arduino_CommunicationParams_type: Property = Property(name="type", type=StringType)
arduino_CommunicationParams_mac: Property = Property(name="mac", type=StringType)
arduino_CommunicationParams_ip: Property = Property(name="ip", type=StringType)
arduino_CommunicationParams_dns: Property = Property(name="dns", type=StringType)
arduino_CommunicationParams_gateway: Property = Property(name="gateway", type=StringType)
arduino_CommunicationParams_subnet: Property = Property(name="subnet", type=StringType)
arduino_CommunicationParams_baudrate: Property = Property(name="baudrate", type=IntegerType)
arduino_CommunicationParams.attributes={arduino_CommunicationParams_mac, arduino_CommunicationParams_type, arduino_CommunicationParams_gateway, arduino_CommunicationParams_ip, arduino_CommunicationParams_dns, arduino_CommunicationParams_baudrate, arduino_CommunicationParams_subnet}

# arduino_Message class attributes and methods

# arduino_HighLevelOperation class attributes and methods

# arduino_IODevice class attributes and methods
arduino_IODevice_analog: Property = Property(name="analog", type=BooleanType)
arduino_IODevice_pullup: Property = Property(name="pullup", type=BooleanType)
arduino_IODevice.attributes={arduino_IODevice_analog, arduino_IODevice_pullup}

# arduino_OutOnlyMessage class attributes and methods

# Message class attributes and methods

# arduino_OutInMessage class attributes and methods
arduino_OutInMessage_name: Property = Property(name="name", type=StringType)
arduino_OutInMessage.attributes={arduino_OutInMessage_name}

# arduino_Dispatch class attributes and methods
arduino_Dispatch_name: Property = Property(name="name", type=StringType)
arduino_Dispatch.attributes={arduino_Dispatch_name}

# OutOnlyMessage class attributes and methods

# arduino_Request class attributes and methods

# OutInMessage class attributes and methods

# arduino_Invitation class attributes and methods

# arduino_PortProtocol class attributes and methods

# arduino_PortTCP class attributes and methods
arduino_PortTCP_supportType: Property = Property(name="supportType", type=StringType)
arduino_PortTCP.attributes={arduino_PortTCP_supportType}

# PortProtocol class attributes and methods

# arduino_PortConnectionData class attributes and methods
arduino_PortConnectionData_host: Property = Property(name="host", type=StringType)
arduino_PortConnectionData_port: Property = Property(name="port", type=IntegerType)
arduino_PortConnectionData.attributes={arduino_PortConnectionData_port, arduino_PortConnectionData_host}

# arduino_Precondition1 class attributes and methods

# arduino_EObject class attributes and methods

# arduino_EmptyPrecondition class attributes and methods
arduino_EmptyPrecondition_name: Property = Property(name="name", type=StringType)
arduino_EmptyPrecondition.attributes={arduino_EmptyPrecondition_name}

# arduino_SensorValuePrecondition class attributes and methods
arduino_SensorValuePrecondition_cond: Property = Property(name="cond", type=StringType)
arduino_SensorValuePrecondition_value: Property = Property(name="value", type=StringType)
arduino_SensorValuePrecondition.attributes={arduino_SensorValuePrecondition_cond, arduino_SensorValuePrecondition_value}

# arduino_Actuator class attributes and methods

# AbstractDevice class attributes and methods

# arduino_ServeDispatch class attributes and methods

# arduino_AcceptInvitation class attributes and methods

# arduino_Serial class attributes and methods

# SupportSpecification class attributes and methods

# arduino_TCP class attributes and methods

# arduino_SupportData class attributes and methods

# arduino_ExplicitSupportData class attributes and methods
arduino_ExplicitSupportData_host: Property = Property(name="host", type=StringType)
arduino_ExplicitSupportData_port: Property = Property(name="port", type=IntegerType)
arduino_ExplicitSupportData.attributes={arduino_ExplicitSupportData_port, arduino_ExplicitSupportData_host}

# SupportData class attributes and methods

# arduino_OutOperation class attributes and methods

# HighLevelOperation class attributes and methods

# arduino_InOperation class attributes and methods

# arduino_InAcquireOperation class attributes and methods

# InOperation class attributes and methods

# arduino_SupportSpecification class attributes and methods
arduino_SupportSpecification_supportType: Property = Property(name="supportType", type=StringType)
arduino_SupportSpecification.attributes={arduino_SupportSpecification_supportType}

# arduino_DemandRequest class attributes and methods

# OutOperation class attributes and methods

# arduino_ForwardDispatch class attributes and methods

# arduino_AskInvitation class attributes and methods

# arduino_GrantRequest class attributes and methods

# InAcquireOperation class attributes and methods

# arduino_IP class attributes and methods
arduino_IP_value: Property = Property(name="value", type=StringType)
arduino_IP.attributes={arduino_IP_value}

# Relationships
devices0: BinaryAssociation = BinaryAssociation(
    name="devices0",
    ends={
        Property(name="arduino_AbstractDevice", type=arduino_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Sketch", type=arduino_AbstractDevice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
precondition22: BinaryAssociation = BinaryAssociation(
    name="precondition22",
    ends={
        Property(name="arduino_Precondition", type=arduino_LoopItem, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_LoopItem23", type=arduino_Precondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sensor24: BinaryAssociation = BinaryAssociation(
    name="sensor24",
    ends={
        Property(name="arduino_Sensor", type=arduino_Interrupt, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Interrupt25", type=arduino_Sensor, multiplicity=Multiplicity(0, 1))
    }
)
handler26: BinaryAssociation = BinaryAssociation(
    name="handler26",
    ends={
        Property(name="arduino_Handler28", type=arduino_Interrupt, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Interrupt27", type=arduino_Handler, multiplicity=Multiplicity(0, 1))
    }
)
sensor29: BinaryAssociation = BinaryAssociation(
    name="sensor29",
    ends={
        Property(name="arduino_Sensor31", type=arduino_Poll, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Poll30", type=arduino_Sensor, multiplicity=Multiplicity(0, 1))
    }
)
handlers1: BinaryAssociation = BinaryAssociation(
    name="handlers1",
    ends={
        Property(name="arduino_Handler", type=arduino_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Sketch2", type=arduino_Handler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interrupts3: BinaryAssociation = BinaryAssociation(
    name="interrupts3",
    ends={
        Property(name="arduino_Interrupt", type=arduino_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Sketch4", type=arduino_Interrupt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pollings5: BinaryAssociation = BinaryAssociation(
    name="pollings5",
    ends={
        Property(name="arduino_Poll", type=arduino_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Sketch6", type=arduino_Poll, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tasks7: BinaryAssociation = BinaryAssociation(
    name="tasks7",
    ends={
        Property(name="arduino_Task", type=arduino_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Sketch8", type=arduino_Task, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loop9: BinaryAssociation = BinaryAssociation(
    name="loop9",
    ends={
        Property(name="arduino_LoopItem", type=arduino_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Sketch10", type=arduino_LoopItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
systemDefinition11: BinaryAssociation = BinaryAssociation(
    name="systemDefinition11",
    ends={
        Property(name="arduino_SystemDefinition", type=arduino_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Sketch12", type=arduino_SystemDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mydata13: BinaryAssociation = BinaryAssociation(
    name="mydata13",
    ends={
        Property(name="arduino_CommunicationParams", type=arduino_SystemDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_SystemDefinition14", type=arduino_CommunicationParams, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messages15: BinaryAssociation = BinaryAssociation(
    name="messages15",
    ends={
        Property(name="arduino_Message", type=arduino_SystemDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_SystemDefinition16", type=arduino_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operation17: BinaryAssociation = BinaryAssociation(
    name="operation17",
    ends={
        Property(name="arduino_HighLevelOperation", type=arduino_SystemDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_SystemDefinition18", type=arduino_HighLevelOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
task19: BinaryAssociation = BinaryAssociation(
    name="task19",
    ends={
        Property(name="arduino_Task21", type=arduino_LoopItem, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_LoopItem20", type=arduino_Task, multiplicity=Multiplicity(0, 1))
    }
)
handler32: BinaryAssociation = BinaryAssociation(
    name="handler32",
    ends={
        Property(name="arduino_Handler34", type=arduino_Poll, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Poll33", type=arduino_Handler, multiplicity=Multiplicity(0, 1))
    }
)
info35: BinaryAssociation = BinaryAssociation(
    name="info35",
    ends={
        Property(name="arduino_PortConnectionData", type=arduino_PortTCP, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_PortTCP", type=arduino_PortConnectionData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pre136: BinaryAssociation = BinaryAssociation(
    name="pre136",
    ends={
        Property(name="arduino_Precondition1", type=arduino_Precondition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Precondition37", type=arduino_Precondition1, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pre39: BinaryAssociation = BinaryAssociation(
    name="pre39",
    ends={
        Property(name="arduino_Precondition40", type=arduino_Precondition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Precondition38", type=arduino_Precondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pre41: BinaryAssociation = BinaryAssociation(
    name="pre41",
    ends={
        Property(name="arduino_EObject", type=arduino_Precondition1, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_Precondition142", type=arduino_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sensor43: BinaryAssociation = BinaryAssociation(
    name="sensor43",
    ends={
        Property(name="arduino_Sensor44", type=arduino_SensorValuePrecondition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_SensorValuePrecondition", type=arduino_Sensor, multiplicity=Multiplicity(0, 1))
    }
)
grant63: BinaryAssociation = BinaryAssociation(
    name="grant63",
    ends={
        Property(name="arduino_Request64", type=arduino_GrantRequest, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_GrantRequest", type=arduino_Request, multiplicity=Multiplicity(0, 1))
    }
)
serve65: BinaryAssociation = BinaryAssociation(
    name="serve65",
    ends={
        Property(name="arduino_Dispatch66", type=arduino_ServeDispatch, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_ServeDispatch", type=arduino_Dispatch, multiplicity=Multiplicity(0, 1))
    }
)
accept67: BinaryAssociation = BinaryAssociation(
    name="accept67",
    ends={
        Property(name="arduino_Invitation68", type=arduino_AcceptInvitation, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_AcceptInvitation", type=arduino_Invitation, multiplicity=Multiplicity(0, 1))
    }
)
info69: BinaryAssociation = BinaryAssociation(
    name="info69",
    ends={
        Property(name="arduino_SupportData", type=arduino_TCP, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_TCP", type=arduino_SupportData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sender45: BinaryAssociation = BinaryAssociation(
    name="sender45",
    ends={
        Property(name="arduino_Task46", type=arduino_OutOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_OutOperation", type=arduino_Task, multiplicity=Multiplicity(0, 1))
    }
)
receiver47: BinaryAssociation = BinaryAssociation(
    name="receiver47",
    ends={
        Property(name="arduino_Task48", type=arduino_InAcquireOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_InAcquireOperation", type=arduino_Task, multiplicity=Multiplicity(0, 1))
    }
)
support49: BinaryAssociation = BinaryAssociation(
    name="support49",
    ends={
        Property(name="arduino_SupportSpecification", type=arduino_InAcquireOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_InAcquireOperation50", type=arduino_SupportSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
demand51: BinaryAssociation = BinaryAssociation(
    name="demand51",
    ends={
        Property(name="arduino_Request", type=arduino_DemandRequest, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_DemandRequest", type=arduino_Request, multiplicity=Multiplicity(0, 1))
    }
)
receiver52: BinaryAssociation = BinaryAssociation(
    name="receiver52",
    ends={
        Property(name="arduino_Task54", type=arduino_DemandRequest, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_DemandRequest53", type=arduino_Task, multiplicity=Multiplicity(0, 9999))
    }
)
forward55: BinaryAssociation = BinaryAssociation(
    name="forward55",
    ends={
        Property(name="arduino_Dispatch", type=arduino_ForwardDispatch, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_ForwardDispatch", type=arduino_Dispatch, multiplicity=Multiplicity(0, 1))
    }
)
receiver56: BinaryAssociation = BinaryAssociation(
    name="receiver56",
    ends={
        Property(name="arduino_Task58", type=arduino_ForwardDispatch, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_ForwardDispatch57", type=arduino_Task, multiplicity=Multiplicity(0, 1))
    }
)
ask59: BinaryAssociation = BinaryAssociation(
    name="ask59",
    ends={
        Property(name="arduino_Invitation", type=arduino_AskInvitation, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_AskInvitation", type=arduino_Invitation, multiplicity=Multiplicity(0, 1))
    }
)
receiver60: BinaryAssociation = BinaryAssociation(
    name="receiver60",
    ends={
        Property(name="arduino_Task62", type=arduino_AskInvitation, multiplicity=Multiplicity(1, 1)),
        Property(name="arduino_AskInvitation61", type=arduino_Task, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_arduino_Actuator_AbstractDevice = Generalization(general=AbstractDevice, specific=arduino_Actuator)
gen_arduino_Sensor_AbstractDevice = Generalization(general=AbstractDevice, specific=arduino_Sensor)
gen_arduino_IODevice_AbstractDevice = Generalization(general=AbstractDevice, specific=arduino_IODevice)
gen_arduino_OutOnlyMessage_Message = Generalization(general=Message, specific=arduino_OutOnlyMessage)
gen_arduino_OutInMessage_Message = Generalization(general=Message, specific=arduino_OutInMessage)
gen_arduino_Dispatch_OutOnlyMessage = Generalization(general=OutOnlyMessage, specific=arduino_Dispatch)
gen_arduino_Request_OutInMessage = Generalization(general=OutInMessage, specific=arduino_Request)
gen_arduino_Invitation_OutInMessage = Generalization(general=OutInMessage, specific=arduino_Invitation)
gen_arduino_PortTCP_PortProtocol = Generalization(general=PortProtocol, specific=arduino_PortTCP)
gen_arduino_ServeDispatch_InAcquireOperation = Generalization(general=InAcquireOperation, specific=arduino_ServeDispatch)
gen_arduino_AcceptInvitation_InAcquireOperation = Generalization(general=InAcquireOperation, specific=arduino_AcceptInvitation)
gen_arduino_Serial_SupportSpecification = Generalization(general=SupportSpecification, specific=arduino_Serial)
gen_arduino_TCP_SupportSpecification = Generalization(general=SupportSpecification, specific=arduino_TCP)
gen_arduino_ExplicitSupportData_SupportData = Generalization(general=SupportData, specific=arduino_ExplicitSupportData)
gen_arduino_OutOperation_HighLevelOperation = Generalization(general=HighLevelOperation, specific=arduino_OutOperation)
gen_arduino_InOperation_HighLevelOperation = Generalization(general=HighLevelOperation, specific=arduino_InOperation)
gen_arduino_InAcquireOperation_InOperation = Generalization(general=InOperation, specific=arduino_InAcquireOperation)
gen_arduino_DemandRequest_OutOperation = Generalization(general=OutOperation, specific=arduino_DemandRequest)
gen_arduino_ForwardDispatch_OutOperation = Generalization(general=OutOperation, specific=arduino_ForwardDispatch)
gen_arduino_AskInvitation_OutOperation = Generalization(general=OutOperation, specific=arduino_AskInvitation)
gen_arduino_GrantRequest_InAcquireOperation = Generalization(general=InAcquireOperation, specific=arduino_GrantRequest)

# Domain Model
domain_model = DomainModel(
    name="arduino",
    types={arduino_Sketch, arduino_AbstractDevice, arduino_Precondition, arduino_Sensor, arduino_Handler, arduino_Interrupt, arduino_Poll, arduino_Task, arduino_LoopItem, arduino_SystemDefinition, arduino_CommunicationParams, arduino_Message, arduino_HighLevelOperation, arduino_IODevice, arduino_OutOnlyMessage, Message, arduino_OutInMessage, arduino_Dispatch, OutOnlyMessage, arduino_Request, OutInMessage, arduino_Invitation, arduino_PortProtocol, arduino_PortTCP, PortProtocol, arduino_PortConnectionData, arduino_Precondition1, arduino_EObject, arduino_EmptyPrecondition, arduino_SensorValuePrecondition, arduino_Actuator, AbstractDevice, arduino_ServeDispatch, arduino_AcceptInvitation, arduino_Serial, SupportSpecification, arduino_TCP, arduino_SupportData, arduino_ExplicitSupportData, SupportData, arduino_OutOperation, HighLevelOperation, arduino_InOperation, arduino_InAcquireOperation, InOperation, arduino_SupportSpecification, arduino_DemandRequest, OutOperation, arduino_ForwardDispatch, arduino_AskInvitation, arduino_GrantRequest, InAcquireOperation, arduino_IP},
    associations={devices0, precondition22, sensor24, handler26, sensor29, handlers1, interrupts3, pollings5, tasks7, loop9, systemDefinition11, mydata13, messages15, operation17, task19, handler32, info35, pre136, pre39, pre41, sensor43, grant63, serve65, accept67, info69, sender45, receiver47, support49, demand51, receiver52, forward55, receiver56, ask59, receiver60},
    generalizations={gen_arduino_Actuator_AbstractDevice, gen_arduino_Sensor_AbstractDevice, gen_arduino_IODevice_AbstractDevice, gen_arduino_OutOnlyMessage_Message, gen_arduino_OutInMessage_Message, gen_arduino_Dispatch_OutOnlyMessage, gen_arduino_Request_OutInMessage, gen_arduino_Invitation_OutInMessage, gen_arduino_PortTCP_PortProtocol, gen_arduino_ServeDispatch_InAcquireOperation, gen_arduino_AcceptInvitation_InAcquireOperation, gen_arduino_Serial_SupportSpecification, gen_arduino_TCP_SupportSpecification, gen_arduino_ExplicitSupportData_SupportData, gen_arduino_OutOperation_HighLevelOperation, gen_arduino_InOperation_HighLevelOperation, gen_arduino_InAcquireOperation_InOperation, gen_arduino_DemandRequest_OutOperation, gen_arduino_ForwardDispatch_OutOperation, gen_arduino_AskInvitation_OutOperation, gen_arduino_GrantRequest_InAcquireOperation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)