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
PrimitiveType: Enumeration = Enumeration(
    name="PrimitiveType",
    literals={
            EnumerationLiteral(name="void"),
			EnumerationLiteral(name="int8"),
			EnumerationLiteral(name="int16"),
			EnumerationLiteral(name="int32"),
			EnumerationLiteral(name="uint8"),
			EnumerationLiteral(name="uint16"),
			EnumerationLiteral(name="uint32"),
			EnumerationLiteral(name="float32"),
			EnumerationLiteral(name="float64"),
			EnumerationLiteral(name="boolean"),
			EnumerationLiteral(name="string"),
			EnumerationLiteral(name="char")
    }
)

# Classes
room_LogicalSystem = Class(name="room::LogicalSystem")
room_RoomClass = Class(name="room::RoomClass")
room_StructureClass = Class(name="room::StructureClass")
RoomClass = Class(name="RoomClass")
room_RoomModel = Class(name="room::RoomModel")
room_Import = Class(name="room::Import")
room_DataClass = Class(name="room::DataClass")
room_ProtocolClass = Class(name="room::ProtocolClass")
room_ActorClass = Class(name="room::ActorClass")
room_SubSystemClass = Class(name="room::SubSystemClass")
room_Attribute = Class(name="room::Attribute")
room_Operation = Class(name="room::Operation")
room_Binding = Class(name="room::Binding")
room_LayerConnection = Class(name="room::LayerConnection")
room_ActorContainerClass = Class(name="room::ActorContainerClass")
StructureClass = Class(name="StructureClass")
room_SPPRef = Class(name="room::SPPRef")
room_ActorRef = Class(name="room::ActorRef")
room_TypedID = Class(name="room::TypedID")
room_Type = Class(name="room::Type")
room_FreeTypedID = Class(name="room::FreeTypedID")
room_FreeType = Class(name="room::FreeType")
room_MessageHandler = Class(name="room::MessageHandler")
room_DetailCode = Class(name="room::DetailCode")
room_Message = Class(name="room::Message")
room_PortClass = Class(name="room::PortClass")
room_ProtocolSemantics = Class(name="room::ProtocolSemantics")
room_ExternalPort = Class(name="room::ExternalPort")
room_ServiceImplementation = Class(name="room::ServiceImplementation")
room_SemanticsRule = Class(name="room::SemanticsRule")
room_SemanticsInRule = Class(name="room::SemanticsInRule")
SemanticsRule = Class(name="SemanticsRule")
room_SemanticsOutRule = Class(name="room::SemanticsOutRule")
ActorContainerClass = Class(name="ActorContainerClass")
room_Port = Class(name="room::Port")
room_SAPRef = Class(name="room::SAPRef")
room_StateGraph = Class(name="room::StateGraph")
room_InterfaceItem = Class(name="room::InterfaceItem")
InterfaceItem = Class(name="InterfaceItem")
room_ActorInstancePath = Class(name="room::ActorInstancePath")
room_BindingEndPoint = Class(name="room::BindingEndPoint")
room_SubSystemRef = Class(name="room::SubSystemRef")
room_ActorContainerRef = Class(name="room::ActorContainerRef")
ActorContainerRef = Class(name="ActorContainerRef")
room_LogicalThread = Class(name="room::LogicalThread")
room_SAPoint = Class(name="room::SAPoint")
room_SPPoint = Class(name="room::SPPoint")
room_RefSAPoint = Class(name="room::RefSAPoint")
SAPoint = Class(name="SAPoint")
room_RelaySAPoint = Class(name="room::RelaySAPoint")
room_StateGraphNode = Class(name="room::StateGraphNode")
StateGraphItem = Class(name="StateGraphItem")
room_StateGraphItem = Class(name="room::StateGraphItem")
room_State = Class(name="room::State")
StateGraphNode = Class(name="StateGraphNode")
room_NonInitialTransition = Class(name="room::NonInitialTransition")
Transition = Class(name="Transition")
room_InitialTransition = Class(name="room::InitialTransition")
room_TrPoint = Class(name="room::TrPoint")
room_ContinuationTransition = Class(name="room::ContinuationTransition")
NonInitialTransition = Class(name="NonInitialTransition")
room_ChoicePoint = Class(name="room::ChoicePoint")
room_Transition = Class(name="room::Transition")
room_BaseState = Class(name="room::BaseState")
State = Class(name="State")
room_RefinedState = Class(name="room::RefinedState")
room_TransitionPoint = Class(name="room::TransitionPoint")
TrPoint = Class(name="TrPoint")
room_EntryPoint = Class(name="room::EntryPoint")
room_ExitPoint = Class(name="room::ExitPoint")
room_TransitionTerminal = Class(name="room::TransitionTerminal")
room_ChoicepointTerminal = Class(name="room::ChoicepointTerminal")
room_MessageFromIf = Class(name="room::MessageFromIf")
room_Guard = Class(name="room::Guard")
room_TriggeredTransition = Class(name="room::TriggeredTransition")
room_Trigger = Class(name="room::Trigger")
room_CPBranchTransition = Class(name="room::CPBranchTransition")
room_StateTerminal = Class(name="room::StateTerminal")
TransitionTerminal = Class(name="TransitionTerminal")
room_TrPointTerminal = Class(name="room::TrPointTerminal")
room_SubStateTrPointTerminal = Class(name="room::SubStateTrPointTerminal")

# room_LogicalSystem class attributes and methods

# room_RoomClass class attributes and methods
room_RoomClass_name: Property = Property(name="name", type=StringType)
room_RoomClass.attributes={room_RoomClass_name}

# room_StructureClass class attributes and methods

# RoomClass class attributes and methods

# room_RoomModel class attributes and methods
room_RoomModel_name: Property = Property(name="name", type=StringType)
room_RoomModel.attributes={room_RoomModel_name}

# room_Import class attributes and methods
room_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
room_Import.attributes={room_Import_importedNamespace}

# room_DataClass class attributes and methods

# room_ProtocolClass class attributes and methods

# room_ActorClass class attributes and methods
room_ActorClass_abstract: Property = Property(name="abstract", type=BooleanType)
room_ActorClass.attributes={room_ActorClass_abstract}

# room_SubSystemClass class attributes and methods

# room_Attribute class attributes and methods
room_Attribute_name: Property = Property(name="name", type=StringType)
room_Attribute_size: Property = Property(name="size", type=IntegerType)
room_Attribute.attributes={room_Attribute_name, room_Attribute_size}

# room_Operation class attributes and methods
room_Operation_name: Property = Property(name="name", type=StringType)
room_Operation.attributes={room_Operation_name}

# room_Binding class attributes and methods

# room_LayerConnection class attributes and methods

# room_ActorContainerClass class attributes and methods

# StructureClass class attributes and methods

# room_SPPRef class attributes and methods

# room_ActorRef class attributes and methods

# room_TypedID class attributes and methods
room_TypedID_name: Property = Property(name="name", type=StringType)
room_TypedID.attributes={room_TypedID_name}

# room_Type class attributes and methods
room_Type_prim: Property = Property(name="prim", type=StringType)
room_Type.attributes={room_Type_prim}

# room_FreeTypedID class attributes and methods
room_FreeTypedID_name: Property = Property(name="name", type=StringType)
room_FreeTypedID.attributes={room_FreeTypedID_name}

# room_FreeType class attributes and methods
room_FreeType_prim: Property = Property(name="prim", type=StringType)
room_FreeType_type: Property = Property(name="type", type=StringType)
room_FreeType.attributes={room_FreeType_type, room_FreeType_prim}

# room_MessageHandler class attributes and methods

# room_DetailCode class attributes and methods
room_DetailCode_commands: Property = Property(name="commands", type=StringType)
room_DetailCode.attributes={room_DetailCode_commands}

# room_Message class attributes and methods
room_Message_name: Property = Property(name="name", type=StringType)
room_Message.attributes={room_Message_name}

# room_PortClass class attributes and methods

# room_ProtocolSemantics class attributes and methods

# room_ExternalPort class attributes and methods

# room_ServiceImplementation class attributes and methods

# room_SemanticsRule class attributes and methods

# room_SemanticsInRule class attributes and methods

# SemanticsRule class attributes and methods

# room_SemanticsOutRule class attributes and methods

# ActorContainerClass class attributes and methods

# room_Port class attributes and methods
room_Port_conjugated: Property = Property(name="conjugated", type=BooleanType)
room_Port_multiplicity: Property = Property(name="multiplicity", type=IntegerType)
room_Port.attributes={room_Port_multiplicity, room_Port_conjugated}

# room_SAPRef class attributes and methods

# room_StateGraph class attributes and methods

# room_InterfaceItem class attributes and methods
room_InterfaceItem_name: Property = Property(name="name", type=StringType)
room_InterfaceItem.attributes={room_InterfaceItem_name}

# InterfaceItem class attributes and methods

# room_ActorInstancePath class attributes and methods
room_ActorInstancePath_segments: Property = Property(name="segments", type=StringType)
room_ActorInstancePath.attributes={room_ActorInstancePath_segments}

# room_BindingEndPoint class attributes and methods

# room_SubSystemRef class attributes and methods

# room_ActorContainerRef class attributes and methods
room_ActorContainerRef_name: Property = Property(name="name", type=StringType)
room_ActorContainerRef.attributes={room_ActorContainerRef_name}

# ActorContainerRef class attributes and methods

# room_LogicalThread class attributes and methods
room_LogicalThread_name: Property = Property(name="name", type=StringType)
room_LogicalThread.attributes={room_LogicalThread_name}

# room_SAPoint class attributes and methods

# room_SPPoint class attributes and methods

# room_RefSAPoint class attributes and methods

# SAPoint class attributes and methods

# room_RelaySAPoint class attributes and methods

# room_StateGraphNode class attributes and methods

# StateGraphItem class attributes and methods

# room_StateGraphItem class attributes and methods

# room_State class attributes and methods
room_State_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
room_State.methods={room_State_m_getName}

# StateGraphNode class attributes and methods

# room_NonInitialTransition class attributes and methods

# Transition class attributes and methods

# room_InitialTransition class attributes and methods

# room_TrPoint class attributes and methods
room_TrPoint_name: Property = Property(name="name", type=StringType)
room_TrPoint.attributes={room_TrPoint_name}

# room_ContinuationTransition class attributes and methods

# NonInitialTransition class attributes and methods

# room_ChoicePoint class attributes and methods
room_ChoicePoint_name: Property = Property(name="name", type=StringType)
room_ChoicePoint.attributes={room_ChoicePoint_name}

# room_Transition class attributes and methods
room_Transition_name: Property = Property(name="name", type=StringType)
room_Transition.attributes={room_Transition_name}

# room_BaseState class attributes and methods
room_BaseState_name: Property = Property(name="name", type=StringType)
room_BaseState.attributes={room_BaseState_name}

# State class attributes and methods

# room_RefinedState class attributes and methods

# room_TransitionPoint class attributes and methods
room_TransitionPoint_handler: Property = Property(name="handler", type=BooleanType)
room_TransitionPoint.attributes={room_TransitionPoint_handler}

# TrPoint class attributes and methods

# room_EntryPoint class attributes and methods

# room_ExitPoint class attributes and methods

# room_TransitionTerminal class attributes and methods

# room_ChoicepointTerminal class attributes and methods

# room_MessageFromIf class attributes and methods

# room_Guard class attributes and methods

# room_TriggeredTransition class attributes and methods

# room_Trigger class attributes and methods

# room_CPBranchTransition class attributes and methods

# room_StateTerminal class attributes and methods

# TransitionTerminal class attributes and methods

# room_TrPointTerminal class attributes and methods

# room_SubStateTrPointTerminal class attributes and methods

# Relationships
systems9: BinaryAssociation = BinaryAssociation(
    name="systems9",
    ends={
        Property(name="room_LogicalSystem", type=room_RoomModel, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RoomModel10", type=room_LogicalSystem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="room_Import", type=room_RoomModel, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RoomModel", type=room_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataClasses1: BinaryAssociation = BinaryAssociation(
    name="dataClasses1",
    ends={
        Property(name="room_DataClass", type=room_RoomModel, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RoomModel2", type=room_DataClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
protocolClasses3: BinaryAssociation = BinaryAssociation(
    name="protocolClasses3",
    ends={
        Property(name="room_ProtocolClass", type=room_RoomModel, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RoomModel4", type=room_ProtocolClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actorClasses5: BinaryAssociation = BinaryAssociation(
    name="actorClasses5",
    ends={
        Property(name="room_ActorClass", type=room_RoomModel, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RoomModel6", type=room_ActorClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subSystemClasses7: BinaryAssociation = BinaryAssociation(
    name="subSystemClasses7",
    ends={
        Property(name="room_SubSystemClass", type=room_RoomModel, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RoomModel8", type=room_SubSystemClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base23: BinaryAssociation = BinaryAssociation(
    name="base23",
    ends={
        Property(name="room_DataClass24", type=room_DataClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_DataClass22", type=room_DataClass, multiplicity=Multiplicity(0, 1))
    }
)
imports25: BinaryAssociation = BinaryAssociation(
    name="imports25",
    ends={
        Property(name="room_Import27", type=room_DataClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_DataClass26", type=room_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes28: BinaryAssociation = BinaryAssociation(
    name="attributes28",
    ends={
        Property(name="room_Attribute", type=room_DataClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_DataClass29", type=room_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations30: BinaryAssociation = BinaryAssociation(
    name="operations30",
    ends={
        Property(name="room_Operation", type=room_DataClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_DataClass31", type=room_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindings11: BinaryAssociation = BinaryAssociation(
    name="bindings11",
    ends={
        Property(name="room_Binding", type=room_StructureClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_StructureClass", type=room_Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connections12: BinaryAssociation = BinaryAssociation(
    name="connections12",
    ends={
        Property(name="room_LayerConnection", type=room_StructureClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_StructureClass13", type=room_LayerConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ifSPPs14: BinaryAssociation = BinaryAssociation(
    name="ifSPPs14",
    ends={
        Property(name="room_SPPRef", type=room_ActorContainerClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorContainerClass", type=room_SPPRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actorRefs15: BinaryAssociation = BinaryAssociation(
    name="actorRefs15",
    ends={
        Property(name="room_ActorRef", type=room_ActorContainerClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorContainerClass16", type=room_ActorRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type17: BinaryAssociation = BinaryAssociation(
    name="type17",
    ends={
        Property(name="room_Type", type=room_TypedID, multiplicity=Multiplicity(1, 1)),
        Property(name="room_TypedID", type=room_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type18: BinaryAssociation = BinaryAssociation(
    name="type18",
    ends={
        Property(name="room_FreeType", type=room_FreeTypedID, multiplicity=Multiplicity(1, 1)),
        Property(name="room_FreeTypedID", type=room_FreeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type19: BinaryAssociation = BinaryAssociation(
    name="type19",
    ends={
        Property(name="room_DataClass21", type=room_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Type20", type=room_DataClass, multiplicity=Multiplicity(0, 1))
    }
)
arguments64: BinaryAssociation = BinaryAssociation(
    name="arguments64",
    ends={
        Property(name="room_TypedID66", type=room_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Message65", type=room_TypedID, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userCode67: BinaryAssociation = BinaryAssociation(
    name="userCode67",
    ends={
        Property(name="room_DetailCode69", type=room_PortClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_PortClass68", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes70: BinaryAssociation = BinaryAssociation(
    name="attributes70",
    ends={
        Property(name="room_Attribute72", type=room_PortClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_PortClass71", type=room_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations73: BinaryAssociation = BinaryAssociation(
    name="operations73",
    ends={
        Property(name="room_Operation75", type=room_PortClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_PortClass74", type=room_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
msgHandlers76: BinaryAssociation = BinaryAssociation(
    name="msgHandlers76",
    ends={
        Property(name="room_MessageHandler", type=room_PortClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_PortClass77", type=room_MessageHandler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type32: BinaryAssociation = BinaryAssociation(
    name="type32",
    ends={
        Property(name="room_Type34", type=room_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Attribute33", type=room_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments35: BinaryAssociation = BinaryAssociation(
    name="arguments35",
    ends={
        Property(name="room_FreeTypedID37", type=room_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Operation36", type=room_FreeTypedID, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returntype38: BinaryAssociation = BinaryAssociation(
    name="returntype38",
    ends={
        Property(name="room_FreeType40", type=room_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Operation39", type=room_FreeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
detailCode41: BinaryAssociation = BinaryAssociation(
    name="detailCode41",
    ends={
        Property(name="room_DetailCode", type=room_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Operation42", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base44: BinaryAssociation = BinaryAssociation(
    name="base44",
    ends={
        Property(name="room_ProtocolClass45", type=room_ProtocolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ProtocolClass43", type=room_ProtocolClass, multiplicity=Multiplicity(0, 1))
    }
)
userCode146: BinaryAssociation = BinaryAssociation(
    name="userCode146",
    ends={
        Property(name="room_DetailCode48", type=room_ProtocolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ProtocolClass47", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
userCode249: BinaryAssociation = BinaryAssociation(
    name="userCode249",
    ends={
        Property(name="room_DetailCode51", type=room_ProtocolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ProtocolClass50", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
incomingMessages52: BinaryAssociation = BinaryAssociation(
    name="incomingMessages52",
    ends={
        Property(name="room_Message", type=room_ProtocolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ProtocolClass53", type=room_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoingMessages54: BinaryAssociation = BinaryAssociation(
    name="outgoingMessages54",
    ends={
        Property(name="room_Message56", type=room_ProtocolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ProtocolClass55", type=room_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
regular57: BinaryAssociation = BinaryAssociation(
    name="regular57",
    ends={
        Property(name="room_PortClass", type=room_ProtocolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ProtocolClass58", type=room_PortClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conjugate59: BinaryAssociation = BinaryAssociation(
    name="conjugate59",
    ends={
        Property(name="room_PortClass61", type=room_ProtocolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ProtocolClass60", type=room_PortClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
semantics62: BinaryAssociation = BinaryAssociation(
    name="semantics62",
    ends={
        Property(name="room_ProtocolSemantics", type=room_ProtocolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ProtocolClass63", type=room_ProtocolSemantics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
intPorts103: BinaryAssociation = BinaryAssociation(
    name="intPorts103",
    ends={
        Property(name="room_Port105", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass104", type=room_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extPorts106: BinaryAssociation = BinaryAssociation(
    name="extPorts106",
    ends={
        Property(name="room_ExternalPort", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass107", type=room_ExternalPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceImplementations108: BinaryAssociation = BinaryAssociation(
    name="serviceImplementations108",
    ends={
        Property(name="room_ServiceImplementation", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass109", type=room_ServiceImplementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
msg78: BinaryAssociation = BinaryAssociation(
    name="msg78",
    ends={
        Property(name="room_Message80", type=room_MessageHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="room_MessageHandler79", type=room_Message, multiplicity=Multiplicity(0, 1))
    }
)
detailCode81: BinaryAssociation = BinaryAssociation(
    name="detailCode81",
    ends={
        Property(name="room_DetailCode83", type=room_MessageHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="room_MessageHandler82", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rules84: BinaryAssociation = BinaryAssociation(
    name="rules84",
    ends={
        Property(name="room_SemanticsRule", type=room_ProtocolSemantics, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ProtocolSemantics85", type=room_SemanticsRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
msg86: BinaryAssociation = BinaryAssociation(
    name="msg86",
    ends={
        Property(name="room_Message88", type=room_SemanticsRule, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SemanticsRule87", type=room_Message, multiplicity=Multiplicity(0, 1))
    }
)
followUps90: BinaryAssociation = BinaryAssociation(
    name="followUps90",
    ends={
        Property(name="room_SemanticsRule91", type=room_SemanticsRule, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SemanticsRule89", type=room_SemanticsRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base93: BinaryAssociation = BinaryAssociation(
    name="base93",
    ends={
        Property(name="room_ActorClass94", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass92", type=room_ActorClass, multiplicity=Multiplicity(0, 1))
    }
)
ifPorts95: BinaryAssociation = BinaryAssociation(
    name="ifPorts95",
    ends={
        Property(name="room_Port", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass96", type=room_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userCode197: BinaryAssociation = BinaryAssociation(
    name="userCode197",
    ends={
        Property(name="room_DetailCode99", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass98", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
userCode2100: BinaryAssociation = BinaryAssociation(
    name="userCode2100",
    ends={
        Property(name="room_DetailCode102", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass101", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifport122: BinaryAssociation = BinaryAssociation(
    name="ifport122",
    ends={
        Property(name="room_Port124", type=room_ExternalPort, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ExternalPort123", type=room_Port, multiplicity=Multiplicity(0, 1))
    }
)
strSAPs110: BinaryAssociation = BinaryAssociation(
    name="strSAPs110",
    ends={
        Property(name="room_SAPRef", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass111", type=room_SAPRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes112: BinaryAssociation = BinaryAssociation(
    name="attributes112",
    ends={
        Property(name="room_Attribute114", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass113", type=room_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations115: BinaryAssociation = BinaryAssociation(
    name="operations115",
    ends={
        Property(name="room_Operation117", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass116", type=room_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateMachine118: BinaryAssociation = BinaryAssociation(
    name="stateMachine118",
    ends={
        Property(name="room_StateGraph", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass119", type=room_StateGraph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
protocol120: BinaryAssociation = BinaryAssociation(
    name="protocol120",
    ends={
        Property(name="room_ProtocolClass121", type=room_InterfaceItem, multiplicity=Multiplicity(1, 1)),
        Property(name="room_InterfaceItem", type=room_ProtocolClass, multiplicity=Multiplicity(0, 1))
    }
)
instances138: BinaryAssociation = BinaryAssociation(
    name="instances138",
    ends={
        Property(name="room_ActorInstancePath", type=room_LogicalThread, multiplicity=Multiplicity(1, 1)),
        Property(name="room_LogicalThread139", type=room_ActorInstancePath, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endpoint1140: BinaryAssociation = BinaryAssociation(
    name="endpoint1140",
    ends={
        Property(name="room_BindingEndPoint", type=room_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Binding141", type=room_BindingEndPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
endpoint2142: BinaryAssociation = BinaryAssociation(
    name="endpoint2142",
    ends={
        Property(name="room_BindingEndPoint144", type=room_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Binding143", type=room_BindingEndPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
spp125: BinaryAssociation = BinaryAssociation(
    name="spp125",
    ends={
        Property(name="room_SPPRef127", type=room_ServiceImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ServiceImplementation126", type=room_SPPRef, multiplicity=Multiplicity(0, 1))
    }
)
subSystems128: BinaryAssociation = BinaryAssociation(
    name="subSystems128",
    ends={
        Property(name="room_SubSystemRef", type=room_LogicalSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="room_LogicalSystem129", type=room_SubSystemRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type130: BinaryAssociation = BinaryAssociation(
    name="type130",
    ends={
        Property(name="room_SubSystemClass132", type=room_SubSystemRef, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SubSystemRef131", type=room_SubSystemClass, multiplicity=Multiplicity(0, 1))
    }
)
relayPorts133: BinaryAssociation = BinaryAssociation(
    name="relayPorts133",
    ends={
        Property(name="room_Port135", type=room_SubSystemClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SubSystemClass134", type=room_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
threads136: BinaryAssociation = BinaryAssociation(
    name="threads136",
    ends={
        Property(name="room_LogicalThread", type=room_SubSystemClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SubSystemClass137", type=room_LogicalThread, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entryCode167: BinaryAssociation = BinaryAssociation(
    name="entryCode167",
    ends={
        Property(name="room_State", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="room_DetailCode168", type=room_State, multiplicity=Multiplicity(1, 1))
    }
)
exitCode169: BinaryAssociation = BinaryAssociation(
    name="exitCode169",
    ends={
        Property(name="room_DetailCode171", type=room_State, multiplicity=Multiplicity(1, 1)),
        Property(name="room_State170", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subgraph172: BinaryAssociation = BinaryAssociation(
    name="subgraph172",
    ends={
        Property(name="room_StateGraph174", type=room_State, multiplicity=Multiplicity(1, 1)),
        Property(name="room_State173", type=room_StateGraph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
states175: BinaryAssociation = BinaryAssociation(
    name="states175",
    ends={
        Property(name="room_State177", type=room_StateGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="room_StateGraph176", type=room_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actorRef145: BinaryAssociation = BinaryAssociation(
    name="actorRef145",
    ends={
        Property(name="room_ActorContainerRef", type=room_BindingEndPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="room_BindingEndPoint146", type=room_ActorContainerRef, multiplicity=Multiplicity(0, 1))
    }
)
port147: BinaryAssociation = BinaryAssociation(
    name="port147",
    ends={
        Property(name="room_Port149", type=room_BindingEndPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="room_BindingEndPoint148", type=room_Port, multiplicity=Multiplicity(0, 1))
    }
)
from150: BinaryAssociation = BinaryAssociation(
    name="from150",
    ends={
        Property(name="room_SAPoint", type=room_LayerConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="room_LayerConnection151", type=room_SAPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
to152: BinaryAssociation = BinaryAssociation(
    name="to152",
    ends={
        Property(name="room_SPPoint", type=room_LayerConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="room_LayerConnection153", type=room_SPPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref154: BinaryAssociation = BinaryAssociation(
    name="ref154",
    ends={
        Property(name="room_ActorContainerRef155", type=room_RefSAPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RefSAPoint", type=room_ActorContainerRef, multiplicity=Multiplicity(0, 1))
    }
)
relay156: BinaryAssociation = BinaryAssociation(
    name="relay156",
    ends={
        Property(name="room_SPPRef157", type=room_RelaySAPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RelaySAPoint", type=room_SPPRef, multiplicity=Multiplicity(0, 1))
    }
)
ref158: BinaryAssociation = BinaryAssociation(
    name="ref158",
    ends={
        Property(name="room_ActorContainerRef160", type=room_SPPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SPPoint159", type=room_ActorContainerRef, multiplicity=Multiplicity(0, 1))
    }
)
service161: BinaryAssociation = BinaryAssociation(
    name="service161",
    ends={
        Property(name="room_SPPRef163", type=room_SPPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SPPoint162", type=room_SPPRef, multiplicity=Multiplicity(0, 1))
    }
)
type164: BinaryAssociation = BinaryAssociation(
    name="type164",
    ends={
        Property(name="room_ActorClass166", type=room_ActorRef, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorRef165", type=room_ActorClass, multiplicity=Multiplicity(0, 1))
    }
)
action187: BinaryAssociation = BinaryAssociation(
    name="action187",
    ends={
        Property(name="room_Transition188", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="room_DetailCode189", type=room_Transition, multiplicity=Multiplicity(1, 1))
    }
)
from190: BinaryAssociation = BinaryAssociation(
    name="from190",
    ends={
        Property(name="room_TransitionTerminal191", type=room_NonInitialTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="room_NonInitialTransition", type=room_TransitionTerminal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trPoints178: BinaryAssociation = BinaryAssociation(
    name="trPoints178",
    ends={
        Property(name="room_TrPoint", type=room_StateGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="room_StateGraph179", type=room_TrPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
chPoints180: BinaryAssociation = BinaryAssociation(
    name="chPoints180",
    ends={
        Property(name="room_ChoicePoint", type=room_StateGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="room_StateGraph181", type=room_ChoicePoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions182: BinaryAssociation = BinaryAssociation(
    name="transitions182",
    ends={
        Property(name="room_Transition", type=room_StateGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="room_StateGraph183", type=room_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base184: BinaryAssociation = BinaryAssociation(
    name="base184",
    ends={
        Property(name="room_BaseState", type=room_RefinedState, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RefinedState", type=room_BaseState, multiplicity=Multiplicity(0, 1))
    }
)
to185: BinaryAssociation = BinaryAssociation(
    name="to185",
    ends={
        Property(name="room_TransitionTerminal", type=room_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Transition186", type=room_TransitionTerminal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cp204: BinaryAssociation = BinaryAssociation(
    name="cp204",
    ends={
        Property(name="room_ChoicePoint205", type=room_ChoicepointTerminal, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ChoicepointTerminal", type=room_ChoicePoint, multiplicity=Multiplicity(0, 1))
    }
)
msgFromIfPairs206: BinaryAssociation = BinaryAssociation(
    name="msgFromIfPairs206",
    ends={
        Property(name="room_MessageFromIf", type=room_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Trigger207", type=room_MessageFromIf, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard208: BinaryAssociation = BinaryAssociation(
    name="guard208",
    ends={
        Property(name="room_Guard", type=room_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Trigger209", type=room_Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
message210: BinaryAssociation = BinaryAssociation(
    name="message210",
    ends={
        Property(name="room_Message212", type=room_MessageFromIf, multiplicity=Multiplicity(1, 1)),
        Property(name="room_MessageFromIf211", type=room_Message, multiplicity=Multiplicity(0, 1))
    }
)
from213: BinaryAssociation = BinaryAssociation(
    name="from213",
    ends={
        Property(name="room_InterfaceItem215", type=room_MessageFromIf, multiplicity=Multiplicity(1, 1)),
        Property(name="room_MessageFromIf214", type=room_InterfaceItem, multiplicity=Multiplicity(0, 1))
    }
)
guard216: BinaryAssociation = BinaryAssociation(
    name="guard216",
    ends={
        Property(name="room_DetailCode218", type=room_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Guard217", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
triggers192: BinaryAssociation = BinaryAssociation(
    name="triggers192",
    ends={
        Property(name="room_Trigger", type=room_TriggeredTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="room_TriggeredTransition", type=room_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition193: BinaryAssociation = BinaryAssociation(
    name="condition193",
    ends={
        Property(name="room_DetailCode194", type=room_CPBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="room_CPBranchTransition", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
state195: BinaryAssociation = BinaryAssociation(
    name="state195",
    ends={
        Property(name="room_BaseState196", type=room_StateTerminal, multiplicity=Multiplicity(1, 1)),
        Property(name="room_StateTerminal", type=room_BaseState, multiplicity=Multiplicity(0, 1))
    }
)
trPoint197: BinaryAssociation = BinaryAssociation(
    name="trPoint197",
    ends={
        Property(name="room_TrPoint198", type=room_TrPointTerminal, multiplicity=Multiplicity(1, 1)),
        Property(name="room_TrPointTerminal", type=room_TrPoint, multiplicity=Multiplicity(0, 1))
    }
)
trPoint199: BinaryAssociation = BinaryAssociation(
    name="trPoint199",
    ends={
        Property(name="room_TrPoint200", type=room_SubStateTrPointTerminal, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SubStateTrPointTerminal", type=room_TrPoint, multiplicity=Multiplicity(0, 1))
    }
)
state201: BinaryAssociation = BinaryAssociation(
    name="state201",
    ends={
        Property(name="room_BaseState203", type=room_SubStateTrPointTerminal, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SubStateTrPointTerminal202", type=room_BaseState, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_room_StructureClass_RoomClass = Generalization(general=RoomClass, specific=room_StructureClass)
gen_room_DataClass_RoomClass = Generalization(general=RoomClass, specific=room_DataClass)
gen_room_ActorContainerClass_StructureClass = Generalization(general=StructureClass, specific=room_ActorContainerClass)
gen_room_ProtocolClass_RoomClass = Generalization(general=RoomClass, specific=room_ProtocolClass)
gen_room_SemanticsInRule_SemanticsRule = Generalization(general=SemanticsRule, specific=room_SemanticsInRule)
gen_room_SemanticsOutRule_SemanticsRule = Generalization(general=SemanticsRule, specific=room_SemanticsOutRule)
gen_room_ActorClass_ActorContainerClass = Generalization(general=ActorContainerClass, specific=room_ActorClass)
gen_room_SAPRef_InterfaceItem = Generalization(general=InterfaceItem, specific=room_SAPRef)
gen_room_Port_InterfaceItem = Generalization(general=InterfaceItem, specific=room_Port)
gen_room_SPPRef_InterfaceItem = Generalization(general=InterfaceItem, specific=room_SPPRef)
gen_room_LogicalSystem_StructureClass = Generalization(general=StructureClass, specific=room_LogicalSystem)
gen_room_SubSystemRef_ActorContainerRef = Generalization(general=ActorContainerRef, specific=room_SubSystemRef)
gen_room_SubSystemClass_ActorContainerClass = Generalization(general=ActorContainerClass, specific=room_SubSystemClass)
gen_room_RefSAPoint_SAPoint = Generalization(general=SAPoint, specific=room_RefSAPoint)
gen_room_RelaySAPoint_SAPoint = Generalization(general=SAPoint, specific=room_RelaySAPoint)
gen_room_ActorRef_ActorContainerRef = Generalization(general=ActorContainerRef, specific=room_ActorRef)
gen_room_StateGraphNode_StateGraphItem = Generalization(general=StateGraphItem, specific=room_StateGraphNode)
gen_room_State_StateGraphNode = Generalization(general=StateGraphNode, specific=room_State)
gen_room_NonInitialTransition_Transition = Generalization(general=Transition, specific=room_NonInitialTransition)
gen_room_InitialTransition_Transition = Generalization(general=Transition, specific=room_InitialTransition)
gen_room_ContinuationTransition_NonInitialTransition = Generalization(general=NonInitialTransition, specific=room_ContinuationTransition)
gen_room_BaseState_State = Generalization(general=State, specific=room_BaseState)
gen_room_RefinedState_State = Generalization(general=State, specific=room_RefinedState)
gen_room_TrPoint_StateGraphNode = Generalization(general=StateGraphNode, specific=room_TrPoint)
gen_room_TransitionPoint_TrPoint = Generalization(general=TrPoint, specific=room_TransitionPoint)
gen_room_EntryPoint_TrPoint = Generalization(general=TrPoint, specific=room_EntryPoint)
gen_room_ExitPoint_TrPoint = Generalization(general=TrPoint, specific=room_ExitPoint)
gen_room_ChoicePoint_StateGraphNode = Generalization(general=StateGraphNode, specific=room_ChoicePoint)
gen_room_Transition_StateGraphItem = Generalization(general=StateGraphItem, specific=room_Transition)
gen_room_ChoicepointTerminal_TransitionTerminal = Generalization(general=TransitionTerminal, specific=room_ChoicepointTerminal)
gen_room_TriggeredTransition_NonInitialTransition = Generalization(general=NonInitialTransition, specific=room_TriggeredTransition)
gen_room_CPBranchTransition_NonInitialTransition = Generalization(general=NonInitialTransition, specific=room_CPBranchTransition)
gen_room_StateTerminal_TransitionTerminal = Generalization(general=TransitionTerminal, specific=room_StateTerminal)
gen_room_TrPointTerminal_TransitionTerminal = Generalization(general=TransitionTerminal, specific=room_TrPointTerminal)
gen_room_SubStateTrPointTerminal_TransitionTerminal = Generalization(general=TransitionTerminal, specific=room_SubStateTrPointTerminal)

# Domain Model
domain_model = DomainModel(
    name="room",
    types={room_LogicalSystem, room_RoomClass, room_StructureClass, RoomClass, room_RoomModel, room_Import, room_DataClass, room_ProtocolClass, room_ActorClass, room_SubSystemClass, room_Attribute, room_Operation, room_Binding, room_LayerConnection, room_ActorContainerClass, StructureClass, room_SPPRef, room_ActorRef, room_TypedID, room_Type, room_FreeTypedID, room_FreeType, room_MessageHandler, room_DetailCode, room_Message, room_PortClass, room_ProtocolSemantics, room_ExternalPort, room_ServiceImplementation, room_SemanticsRule, room_SemanticsInRule, SemanticsRule, room_SemanticsOutRule, ActorContainerClass, room_Port, room_SAPRef, room_StateGraph, room_InterfaceItem, InterfaceItem, room_ActorInstancePath, room_BindingEndPoint, room_SubSystemRef, room_ActorContainerRef, ActorContainerRef, room_LogicalThread, room_SAPoint, room_SPPoint, room_RefSAPoint, SAPoint, room_RelaySAPoint, room_StateGraphNode, StateGraphItem, room_StateGraphItem, room_State, StateGraphNode, room_NonInitialTransition, Transition, room_InitialTransition, room_TrPoint, room_ContinuationTransition, NonInitialTransition, room_ChoicePoint, room_Transition, room_BaseState, State, room_RefinedState, room_TransitionPoint, TrPoint, room_EntryPoint, room_ExitPoint, room_TransitionTerminal, room_ChoicepointTerminal, room_MessageFromIf, room_Guard, room_TriggeredTransition, room_Trigger, room_CPBranchTransition, room_StateTerminal, TransitionTerminal, room_TrPointTerminal, room_SubStateTrPointTerminal, PrimitiveType},
    associations={systems9, imports0, dataClasses1, protocolClasses3, actorClasses5, subSystemClasses7, base23, imports25, attributes28, operations30, bindings11, connections12, ifSPPs14, actorRefs15, type17, type18, type19, arguments64, userCode67, attributes70, operations73, msgHandlers76, type32, arguments35, returntype38, detailCode41, base44, userCode146, userCode249, incomingMessages52, outgoingMessages54, regular57, conjugate59, semantics62, intPorts103, extPorts106, serviceImplementations108, msg78, detailCode81, rules84, msg86, followUps90, base93, ifPorts95, userCode197, userCode2100, ifport122, strSAPs110, attributes112, operations115, stateMachine118, protocol120, instances138, endpoint1140, endpoint2142, spp125, subSystems128, type130, relayPorts133, threads136, entryCode167, exitCode169, subgraph172, states175, actorRef145, port147, from150, to152, ref154, relay156, ref158, service161, type164, action187, from190, trPoints178, chPoints180, transitions182, base184, to185, cp204, msgFromIfPairs206, guard208, message210, from213, guard216, triggers192, condition193, state195, trPoint197, trPoint199, state201},
    generalizations={gen_room_StructureClass_RoomClass, gen_room_DataClass_RoomClass, gen_room_ActorContainerClass_StructureClass, gen_room_ProtocolClass_RoomClass, gen_room_SemanticsInRule_SemanticsRule, gen_room_SemanticsOutRule_SemanticsRule, gen_room_ActorClass_ActorContainerClass, gen_room_SAPRef_InterfaceItem, gen_room_Port_InterfaceItem, gen_room_SPPRef_InterfaceItem, gen_room_LogicalSystem_StructureClass, gen_room_SubSystemRef_ActorContainerRef, gen_room_SubSystemClass_ActorContainerClass, gen_room_RefSAPoint_SAPoint, gen_room_RelaySAPoint_SAPoint, gen_room_ActorRef_ActorContainerRef, gen_room_StateGraphNode_StateGraphItem, gen_room_State_StateGraphNode, gen_room_NonInitialTransition_Transition, gen_room_InitialTransition_Transition, gen_room_ContinuationTransition_NonInitialTransition, gen_room_BaseState_State, gen_room_RefinedState_State, gen_room_TrPoint_StateGraphNode, gen_room_TransitionPoint_TrPoint, gen_room_EntryPoint_TrPoint, gen_room_ExitPoint_TrPoint, gen_room_ChoicePoint_StateGraphNode, gen_room_Transition_StateGraphItem, gen_room_ChoicepointTerminal_TransitionTerminal, gen_room_TriggeredTransition_NonInitialTransition, gen_room_CPBranchTransition_NonInitialTransition, gen_room_StateTerminal_TransitionTerminal, gen_room_TrPointTerminal_TransitionTerminal, gen_room_SubStateTrPointTerminal_TransitionTerminal},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)