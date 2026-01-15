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
LiteralType: Enumeration = Enumeration(
    name="LiteralType",
    literals={
            EnumerationLiteral(name="BOOL"),
			EnumerationLiteral(name="INT"),
			EnumerationLiteral(name="REAL"),
			EnumerationLiteral(name="CHAR")
    }
)

CommunicationType: Enumeration = Enumeration(
    name="CommunicationType",
    literals={
            EnumerationLiteral(name="EVENT_DRIVEN"),
			EnumerationLiteral(name="DATA_DRIVEN"),
			EnumerationLiteral(name="SYNCHRONOUS")
    }
)

ActorCommunicationType: Enumeration = Enumeration(
    name="ActorCommunicationType",
    literals={
            EnumerationLiteral(name="EVENT_DRIVEN"),
			EnumerationLiteral(name="DATA_DRIVEN"),
			EnumerationLiteral(name="ASYNCHRONOUS"),
			EnumerationLiteral(name="SYNCHRONOUS")
    }
)

# Classes
room_RoomModel = Class(name="room::RoomModel")
room_Documentation = Class(name="room::Documentation")
room_Import = Class(name="room::Import")
room_PrimitiveType = Class(name="room::PrimitiveType")
room_ExternalType = Class(name="room::ExternalType")
room_DataClass = Class(name="room::DataClass")
room_GeneralProtocolClass = Class(name="room::GeneralProtocolClass")
room_ActorClass = Class(name="room::ActorClass")
room_SubSystemClass = Class(name="room::SubSystemClass")
room_LogicalSystem = Class(name="room::LogicalSystem")
room_RoomClass = Class(name="room::RoomClass")
room_StructureClass = Class(name="room::StructureClass")
RoomClass = Class(name="RoomClass")
room_LayerConnection = Class(name="room::LayerConnection")
room_ActorContainerClass = Class(name="room::ActorContainerClass")
StructureClass = Class(name="StructureClass")
room_SPPRef = Class(name="room::SPPRef")
room_DetailCode = Class(name="room::DetailCode")
room_ActorRef = Class(name="room::ActorRef")
room_VarDecl = Class(name="room::VarDecl")
room_RefableType = Class(name="room::RefableType")
room_DataType = Class(name="room::DataType")
room_ComplexType = Class(name="room::ComplexType")
DataType = Class(name="DataType")
ComplexType = Class(name="ComplexType")
room_Annotation = Class(name="room::Annotation")
room_Binding = Class(name="room::Binding")
room_Attribute = Class(name="room::Attribute")
room_StandardOperation = Class(name="room::StandardOperation")
room_Operation = Class(name="room::Operation")
Operation = Class(name="Operation")
room_PortOperation = Class(name="room::PortOperation")
room_Message = Class(name="room::Message")
room_ProtocolClass = Class(name="room::ProtocolClass")
GeneralProtocolClass = Class(name="GeneralProtocolClass")
room_PortClass = Class(name="room::PortClass")
room_ProtocolSemantics = Class(name="room::ProtocolSemantics")
room_CompoundProtocolClass = Class(name="room::CompoundProtocolClass")
room_SubProtocol = Class(name="room::SubProtocol")
room_MessageHandler = Class(name="room::MessageHandler")
room_InMessageHandler = Class(name="room::InMessageHandler")
MessageHandler = Class(name="MessageHandler")
room_OutMessageHandler = Class(name="room::OutMessageHandler")
room_SemanticsRule = Class(name="room::SemanticsRule")
room_InSemanticsRule = Class(name="room::InSemanticsRule")
SemanticsRule = Class(name="SemanticsRule")
room_OutSemanticsRule = Class(name="room::OutSemanticsRule")
ActorContainerClass = Class(name="ActorContainerClass")
room_Port = Class(name="room::Port")
room_ExternalPort = Class(name="room::ExternalPort")
room_ServiceImplementation = Class(name="room::ServiceImplementation")
room_SAPRef = Class(name="room::SAPRef")
room_StateGraph = Class(name="room::StateGraph")
room_InterfaceItem = Class(name="room::InterfaceItem")
InterfaceItem = Class(name="InterfaceItem")
room_SubSystemRef = Class(name="room::SubSystemRef")
room_ActorContainerRef = Class(name="room::ActorContainerRef")
ActorContainerRef = Class(name="ActorContainerRef")
room_LogicalThread = Class(name="room::LogicalThread")
room_BindingEndPoint = Class(name="room::BindingEndPoint")
room_SAPoint = Class(name="room::SAPoint")
room_SPPoint = Class(name="room::SPPoint")
room_RefSAPoint = Class(name="room::RefSAPoint")
SAPoint = Class(name="SAPoint")
room_RelaySAPoint = Class(name="room::RelaySAPoint")
room_ActorInstancePath = Class(name="room::ActorInstancePath")
room_StateGraphNode = Class(name="room::StateGraphNode")
StateGraphItem = Class(name="StateGraphItem")
room_StateGraphItem = Class(name="room::StateGraphItem")
room_State = Class(name="room::State")
StateGraphNode = Class(name="StateGraphNode")
room_TrPoint = Class(name="room::TrPoint")
room_ChoicePoint = Class(name="room::ChoicePoint")
room_Transition = Class(name="room::Transition")
room_SimpleState = Class(name="room::SimpleState")
State = Class(name="State")
room_RefinedState = Class(name="room::RefinedState")
room_TransitionPoint = Class(name="room::TransitionPoint")
TrPoint = Class(name="TrPoint")
room_EntryPoint = Class(name="room::EntryPoint")
room_ExitPoint = Class(name="room::ExitPoint")
room_TransitionTerminal = Class(name="room::TransitionTerminal")
room_NonInitialTransition = Class(name="room::NonInitialTransition")
Transition = Class(name="Transition")
room_RefinedTransition = Class(name="room::RefinedTransition")
room_TransitionChainStartTransition = Class(name="room::TransitionChainStartTransition")
NonInitialTransition = Class(name="NonInitialTransition")
room_InitialTransition = Class(name="room::InitialTransition")
room_ContinuationTransition = Class(name="room::ContinuationTransition")
room_TriggeredTransition = Class(name="room::TriggeredTransition")
TransitionChainStartTransition = Class(name="TransitionChainStartTransition")
room_Trigger = Class(name="room::Trigger")
room_GuardedTransition = Class(name="room::GuardedTransition")
room_CPBranchTransition = Class(name="room::CPBranchTransition")
room_SubStateTrPointTerminal = Class(name="room::SubStateTrPointTerminal")
room_ChoicepointTerminal = Class(name="room::ChoicepointTerminal")
room_MessageFromIf = Class(name="room::MessageFromIf")
room_Guard = Class(name="room::Guard")
room_KeyValue = Class(name="room::KeyValue")
room_StateTerminal = Class(name="room::StateTerminal")
TransitionTerminal = Class(name="TransitionTerminal")
room_TrPointTerminal = Class(name="room::TrPointTerminal")

# room_RoomModel class attributes and methods
room_RoomModel_name: Property = Property(name="name", type=StringType)
room_RoomModel.attributes={room_RoomModel_name}

# room_Documentation class attributes and methods
room_Documentation_text: Property = Property(name="text", type=StringType)
room_Documentation.attributes={room_Documentation_text}

# room_Import class attributes and methods
room_Import_importURI: Property = Property(name="importURI", type=StringType)
room_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
room_Import.attributes={room_Import_importURI, room_Import_importedNamespace}

# room_PrimitiveType class attributes and methods
room_PrimitiveType_type: Property = Property(name="type", type=StringType)
room_PrimitiveType_targetName: Property = Property(name="targetName", type=StringType)
room_PrimitiveType_castName: Property = Property(name="castName", type=StringType)
room_PrimitiveType_defaultValueLiteral: Property = Property(name="defaultValueLiteral", type=StringType)
room_PrimitiveType.attributes={room_PrimitiveType_castName, room_PrimitiveType_targetName, room_PrimitiveType_type, room_PrimitiveType_defaultValueLiteral}

# room_ExternalType class attributes and methods
room_ExternalType_targetName: Property = Property(name="targetName", type=StringType)
room_ExternalType.attributes={room_ExternalType_targetName}

# room_DataClass class attributes and methods

# room_GeneralProtocolClass class attributes and methods

# room_ActorClass class attributes and methods
room_ActorClass_abstract: Property = Property(name="abstract", type=BooleanType)
room_ActorClass_commType: Property = Property(name="commType", type=StringType)
room_ActorClass.attributes={room_ActorClass_abstract, room_ActorClass_commType}

# room_SubSystemClass class attributes and methods

# room_LogicalSystem class attributes and methods

# room_RoomClass class attributes and methods
room_RoomClass_name: Property = Property(name="name", type=StringType)
room_RoomClass.attributes={room_RoomClass_name}

# room_StructureClass class attributes and methods

# RoomClass class attributes and methods

# room_LayerConnection class attributes and methods

# room_ActorContainerClass class attributes and methods

# StructureClass class attributes and methods

# room_SPPRef class attributes and methods

# room_DetailCode class attributes and methods
room_DetailCode_commands: Property = Property(name="commands", type=StringType)
room_DetailCode.attributes={room_DetailCode_commands}

# room_ActorRef class attributes and methods
room_ActorRef_size: Property = Property(name="size", type=IntegerType)
room_ActorRef.attributes={room_ActorRef_size}

# room_VarDecl class attributes and methods
room_VarDecl_name: Property = Property(name="name", type=StringType)
room_VarDecl.attributes={room_VarDecl_name}

# room_RefableType class attributes and methods
room_RefableType_ref: Property = Property(name="ref", type=BooleanType)
room_RefableType.attributes={room_RefableType_ref}

# room_DataType class attributes and methods

# room_ComplexType class attributes and methods

# DataType class attributes and methods

# ComplexType class attributes and methods

# room_Annotation class attributes and methods
room_Annotation_name: Property = Property(name="name", type=StringType)
room_Annotation.attributes={room_Annotation_name}

# room_Binding class attributes and methods

# room_Attribute class attributes and methods
room_Attribute_name: Property = Property(name="name", type=StringType)
room_Attribute_size: Property = Property(name="size", type=IntegerType)
room_Attribute_defaultValueLiteral: Property = Property(name="defaultValueLiteral", type=StringType)
room_Attribute.attributes={room_Attribute_defaultValueLiteral, room_Attribute_size, room_Attribute_name}

# room_StandardOperation class attributes and methods
room_StandardOperation_destructor: Property = Property(name="destructor", type=BooleanType)
room_StandardOperation.attributes={room_StandardOperation_destructor}

# room_Operation class attributes and methods
room_Operation_name: Property = Property(name="name", type=StringType)
room_Operation.attributes={room_Operation_name}

# Operation class attributes and methods

# room_PortOperation class attributes and methods

# room_Message class attributes and methods
room_Message_priv: Property = Property(name="priv", type=BooleanType)
room_Message_name: Property = Property(name="name", type=StringType)
room_Message.attributes={room_Message_priv, room_Message_name}

# room_ProtocolClass class attributes and methods
room_ProtocolClass_commType: Property = Property(name="commType", type=StringType)
room_ProtocolClass.attributes={room_ProtocolClass_commType}

# GeneralProtocolClass class attributes and methods

# room_PortClass class attributes and methods

# room_ProtocolSemantics class attributes and methods

# room_CompoundProtocolClass class attributes and methods

# room_SubProtocol class attributes and methods
room_SubProtocol_name: Property = Property(name="name", type=StringType)
room_SubProtocol.attributes={room_SubProtocol_name}

# room_MessageHandler class attributes and methods

# room_InMessageHandler class attributes and methods

# MessageHandler class attributes and methods

# room_OutMessageHandler class attributes and methods

# room_SemanticsRule class attributes and methods

# room_InSemanticsRule class attributes and methods

# SemanticsRule class attributes and methods

# room_OutSemanticsRule class attributes and methods

# ActorContainerClass class attributes and methods

# room_Port class attributes and methods
room_Port_conjugated: Property = Property(name="conjugated", type=BooleanType)
room_Port_multiplicity: Property = Property(name="multiplicity", type=IntegerType)
room_Port_m_isReplicated: Method = Method(name="isReplicated", parameters={}, type=BooleanType)
room_Port.attributes={room_Port_conjugated, room_Port_multiplicity}
room_Port.methods={room_Port_m_isReplicated}

# room_ExternalPort class attributes and methods

# room_ServiceImplementation class attributes and methods

# room_SAPRef class attributes and methods

# room_StateGraph class attributes and methods

# room_InterfaceItem class attributes and methods
room_InterfaceItem_name: Property = Property(name="name", type=StringType)
room_InterfaceItem_m_getGeneralProtocol: Method = Method(name="getGeneralProtocol", parameters={}, type=GeneralProtocolClass)
room_InterfaceItem.attributes={room_InterfaceItem_name}
room_InterfaceItem.methods={room_InterfaceItem_m_getGeneralProtocol}

# InterfaceItem class attributes and methods

# room_SubSystemRef class attributes and methods

# room_ActorContainerRef class attributes and methods
room_ActorContainerRef_name: Property = Property(name="name", type=StringType)
room_ActorContainerRef.attributes={room_ActorContainerRef_name}

# ActorContainerRef class attributes and methods

# room_LogicalThread class attributes and methods
room_LogicalThread_name: Property = Property(name="name", type=StringType)
room_LogicalThread_prio: Property = Property(name="prio", type=IntegerType)
room_LogicalThread.attributes={room_LogicalThread_prio, room_LogicalThread_name}

# room_BindingEndPoint class attributes and methods

# room_SAPoint class attributes and methods

# room_SPPoint class attributes and methods

# room_RefSAPoint class attributes and methods

# SAPoint class attributes and methods

# room_RelaySAPoint class attributes and methods

# room_ActorInstancePath class attributes and methods
room_ActorInstancePath_segments: Property = Property(name="segments", type=StringType)
room_ActorInstancePath.attributes={room_ActorInstancePath_segments}

# room_StateGraphNode class attributes and methods

# StateGraphItem class attributes and methods

# room_StateGraphItem class attributes and methods
room_StateGraphItem_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
room_StateGraphItem.methods={room_StateGraphItem_m_getName}

# room_State class attributes and methods
room_State_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
room_State.methods={room_State_m_getName}

# StateGraphNode class attributes and methods

# room_TrPoint class attributes and methods
room_TrPoint_name: Property = Property(name="name", type=StringType)
room_TrPoint.attributes={room_TrPoint_name}

# room_ChoicePoint class attributes and methods
room_ChoicePoint_name: Property = Property(name="name", type=StringType)
room_ChoicePoint.attributes={room_ChoicePoint_name}

# room_Transition class attributes and methods
room_Transition_name: Property = Property(name="name", type=StringType)
room_Transition.attributes={room_Transition_name}

# room_SimpleState class attributes and methods
room_SimpleState_name: Property = Property(name="name", type=StringType)
room_SimpleState.attributes={room_SimpleState_name}

# State class attributes and methods

# room_RefinedState class attributes and methods

# room_TransitionPoint class attributes and methods
room_TransitionPoint_handler: Property = Property(name="handler", type=BooleanType)
room_TransitionPoint.attributes={room_TransitionPoint_handler}

# TrPoint class attributes and methods

# room_EntryPoint class attributes and methods

# room_ExitPoint class attributes and methods

# room_TransitionTerminal class attributes and methods

# room_NonInitialTransition class attributes and methods

# Transition class attributes and methods

# room_RefinedTransition class attributes and methods

# room_TransitionChainStartTransition class attributes and methods

# NonInitialTransition class attributes and methods

# room_InitialTransition class attributes and methods

# room_ContinuationTransition class attributes and methods

# room_TriggeredTransition class attributes and methods

# TransitionChainStartTransition class attributes and methods

# room_Trigger class attributes and methods

# room_GuardedTransition class attributes and methods

# room_CPBranchTransition class attributes and methods

# room_SubStateTrPointTerminal class attributes and methods

# room_ChoicepointTerminal class attributes and methods

# room_MessageFromIf class attributes and methods

# room_Guard class attributes and methods

# room_KeyValue class attributes and methods
room_KeyValue_key: Property = Property(name="key", type=StringType)
room_KeyValue_value: Property = Property(name="value", type=StringType)
room_KeyValue.attributes={room_KeyValue_value, room_KeyValue_key}

# room_StateTerminal class attributes and methods

# TransitionTerminal class attributes and methods

# room_TrPointTerminal class attributes and methods

# Relationships
docu0: BinaryAssociation = BinaryAssociation(
    name="docu0",
    ends={
        Property(name="room_Documentation", type=room_RoomModel, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RoomModel", type=room_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
imports1: BinaryAssociation = BinaryAssociation(
    name="imports1",
    ends={
        Property(name="room_Import", type=room_RoomModel, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RoomModel2", type=room_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primitiveTypes3: BinaryAssociation = BinaryAssociation(
    name="primitiveTypes3",
    ends={
        Property(name="room_PrimitiveType", type=room_RoomModel, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RoomModel4", type=room_PrimitiveType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalTypes5: BinaryAssociation = BinaryAssociation(
    name="externalTypes5",
    ends={
        Property(name="room_ExternalType", type=room_RoomModel, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RoomModel6", type=room_ExternalType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataClasses7: BinaryAssociation = BinaryAssociation(
    name="dataClasses7",
    ends={
        Property(name="room_DataClass", type=room_RoomModel, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RoomModel8", type=room_DataClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
protocolClasses9: BinaryAssociation = BinaryAssociation(
    name="protocolClasses9",
    ends={
        Property(name="room_GeneralProtocolClass", type=room_RoomModel, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RoomModel10", type=room_GeneralProtocolClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actorClasses11: BinaryAssociation = BinaryAssociation(
    name="actorClasses11",
    ends={
        Property(name="room_ActorClass", type=room_RoomModel, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RoomModel12", type=room_ActorClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subSystemClasses13: BinaryAssociation = BinaryAssociation(
    name="subSystemClasses13",
    ends={
        Property(name="room_SubSystemClass", type=room_RoomModel, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RoomModel14", type=room_SubSystemClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
systems15: BinaryAssociation = BinaryAssociation(
    name="systems15",
    ends={
        Property(name="room_LogicalSystem", type=room_RoomModel, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RoomModel16", type=room_LogicalSystem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
docu17: BinaryAssociation = BinaryAssociation(
    name="docu17",
    ends={
        Property(name="room_Documentation18", type=room_RoomClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RoomClass", type=room_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bindings20: BinaryAssociation = BinaryAssociation(
    name="bindings20",
    ends={
        Property(name="room_Binding", type=room_StructureClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_StructureClass21", type=room_Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connections22: BinaryAssociation = BinaryAssociation(
    name="connections22",
    ends={
        Property(name="room_LayerConnection", type=room_StructureClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_StructureClass23", type=room_LayerConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ifSPPs24: BinaryAssociation = BinaryAssociation(
    name="ifSPPs24",
    ends={
        Property(name="room_SPPRef", type=room_ActorContainerClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorContainerClass", type=room_SPPRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userCode125: BinaryAssociation = BinaryAssociation(
    name="userCode125",
    ends={
        Property(name="room_DetailCode", type=room_ActorContainerClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorContainerClass26", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
userCode227: BinaryAssociation = BinaryAssociation(
    name="userCode227",
    ends={
        Property(name="room_DetailCode29", type=room_ActorContainerClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorContainerClass28", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
userCode330: BinaryAssociation = BinaryAssociation(
    name="userCode330",
    ends={
        Property(name="room_DetailCode32", type=room_ActorContainerClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorContainerClass31", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actorRefs33: BinaryAssociation = BinaryAssociation(
    name="actorRefs33",
    ends={
        Property(name="room_ActorRef", type=room_ActorContainerClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorContainerClass34", type=room_ActorRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refType35: BinaryAssociation = BinaryAssociation(
    name="refType35",
    ends={
        Property(name="room_RefableType", type=room_VarDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="room_VarDecl", type=room_RefableType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type36: BinaryAssociation = BinaryAssociation(
    name="type36",
    ends={
        Property(name="room_DataType", type=room_RefableType, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RefableType37", type=room_DataType, multiplicity=Multiplicity(0, 1))
    }
)
base39: BinaryAssociation = BinaryAssociation(
    name="base39",
    ends={
        Property(name="room_DataClass40", type=room_DataClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_DataClass38", type=room_DataClass, multiplicity=Multiplicity(0, 1))
    }
)
annotations41: BinaryAssociation = BinaryAssociation(
    name="annotations41",
    ends={
        Property(name="room_Annotation43", type=room_DataClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_DataClass42", type=room_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userCode144: BinaryAssociation = BinaryAssociation(
    name="userCode144",
    ends={
        Property(name="room_DetailCode46", type=room_DataClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_DataClass45", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
userCode247: BinaryAssociation = BinaryAssociation(
    name="userCode247",
    ends={
        Property(name="room_DetailCode49", type=room_DataClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_DataClass48", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations19: BinaryAssociation = BinaryAssociation(
    name="annotations19",
    ends={
        Property(name="room_Annotation", type=room_StructureClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_StructureClass", type=room_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes53: BinaryAssociation = BinaryAssociation(
    name="attributes53",
    ends={
        Property(name="room_Attribute", type=room_DataClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_DataClass54", type=room_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations55: BinaryAssociation = BinaryAssociation(
    name="operations55",
    ends={
        Property(name="room_StandardOperation", type=room_DataClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_DataClass56", type=room_StandardOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refType57: BinaryAssociation = BinaryAssociation(
    name="refType57",
    ends={
        Property(name="room_RefableType59", type=room_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Attribute58", type=room_RefableType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docu60: BinaryAssociation = BinaryAssociation(
    name="docu60",
    ends={
        Property(name="room_Documentation62", type=room_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Attribute61", type=room_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments63: BinaryAssociation = BinaryAssociation(
    name="arguments63",
    ends={
        Property(name="room_VarDecl64", type=room_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Operation", type=room_VarDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returntype65: BinaryAssociation = BinaryAssociation(
    name="returntype65",
    ends={
        Property(name="room_RefableType67", type=room_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Operation66", type=room_RefableType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docu68: BinaryAssociation = BinaryAssociation(
    name="docu68",
    ends={
        Property(name="room_Documentation70", type=room_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Operation69", type=room_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
detailCode71: BinaryAssociation = BinaryAssociation(
    name="detailCode71",
    ends={
        Property(name="room_DetailCode73", type=room_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Operation72", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sendsMsg74: BinaryAssociation = BinaryAssociation(
    name="sendsMsg74",
    ends={
        Property(name="room_Message", type=room_PortOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="room_PortOperation", type=room_Message, multiplicity=Multiplicity(0, 1))
    }
)
annotations75: BinaryAssociation = BinaryAssociation(
    name="annotations75",
    ends={
        Property(name="room_Annotation77", type=room_GeneralProtocolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_GeneralProtocolClass76", type=room_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userCode350: BinaryAssociation = BinaryAssociation(
    name="userCode350",
    ends={
        Property(name="room_DetailCode52", type=room_DataClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_DataClass51", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
userCode180: BinaryAssociation = BinaryAssociation(
    name="userCode180",
    ends={
        Property(name="room_DetailCode82", type=room_ProtocolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ProtocolClass81", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
userCode283: BinaryAssociation = BinaryAssociation(
    name="userCode283",
    ends={
        Property(name="room_DetailCode85", type=room_ProtocolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ProtocolClass84", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
userCode386: BinaryAssociation = BinaryAssociation(
    name="userCode386",
    ends={
        Property(name="room_DetailCode88", type=room_ProtocolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ProtocolClass87", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
incomingMessages89: BinaryAssociation = BinaryAssociation(
    name="incomingMessages89",
    ends={
        Property(name="room_Message91", type=room_ProtocolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ProtocolClass90", type=room_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoingMessages92: BinaryAssociation = BinaryAssociation(
    name="outgoingMessages92",
    ends={
        Property(name="room_Message94", type=room_ProtocolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ProtocolClass93", type=room_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base79: BinaryAssociation = BinaryAssociation(
    name="base79",
    ends={
        Property(name="room_ProtocolClass", type=room_ProtocolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ProtocolClass78", type=room_ProtocolClass, multiplicity=Multiplicity(0, 1))
    }
)
regular95: BinaryAssociation = BinaryAssociation(
    name="regular95",
    ends={
        Property(name="room_PortClass", type=room_ProtocolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ProtocolClass96", type=room_PortClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conjugate97: BinaryAssociation = BinaryAssociation(
    name="conjugate97",
    ends={
        Property(name="room_PortClass99", type=room_ProtocolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ProtocolClass98", type=room_PortClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
semantics100: BinaryAssociation = BinaryAssociation(
    name="semantics100",
    ends={
        Property(name="room_ProtocolSemantics", type=room_ProtocolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ProtocolClass101", type=room_ProtocolSemantics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subProtocols102: BinaryAssociation = BinaryAssociation(
    name="subProtocols102",
    ends={
        Property(name="room_SubProtocol", type=room_CompoundProtocolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_CompoundProtocolClass", type=room_SubProtocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
protocol103: BinaryAssociation = BinaryAssociation(
    name="protocol103",
    ends={
        Property(name="room_GeneralProtocolClass105", type=room_SubProtocol, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SubProtocol104", type=room_GeneralProtocolClass, multiplicity=Multiplicity(0, 1))
    }
)
data106: BinaryAssociation = BinaryAssociation(
    name="data106",
    ends={
        Property(name="room_VarDecl108", type=room_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Message107", type=room_VarDecl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docu109: BinaryAssociation = BinaryAssociation(
    name="docu109",
    ends={
        Property(name="room_Documentation111", type=room_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Message110", type=room_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
userCode112: BinaryAssociation = BinaryAssociation(
    name="userCode112",
    ends={
        Property(name="room_DetailCode114", type=room_PortClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_PortClass113", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes115: BinaryAssociation = BinaryAssociation(
    name="attributes115",
    ends={
        Property(name="room_Attribute117", type=room_PortClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_PortClass116", type=room_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
msgHandlers121: BinaryAssociation = BinaryAssociation(
    name="msgHandlers121",
    ends={
        Property(name="room_MessageHandler", type=room_PortClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_PortClass122", type=room_MessageHandler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
msg123: BinaryAssociation = BinaryAssociation(
    name="msg123",
    ends={
        Property(name="room_Message125", type=room_MessageHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="room_MessageHandler124", type=room_Message, multiplicity=Multiplicity(0, 1))
    }
)
detailCode126: BinaryAssociation = BinaryAssociation(
    name="detailCode126",
    ends={
        Property(name="room_DetailCode128", type=room_MessageHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="room_MessageHandler127", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rules129: BinaryAssociation = BinaryAssociation(
    name="rules129",
    ends={
        Property(name="room_SemanticsRule", type=room_ProtocolSemantics, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ProtocolSemantics130", type=room_SemanticsRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
msg131: BinaryAssociation = BinaryAssociation(
    name="msg131",
    ends={
        Property(name="room_Message133", type=room_SemanticsRule, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SemanticsRule132", type=room_Message, multiplicity=Multiplicity(0, 1))
    }
)
followUps135: BinaryAssociation = BinaryAssociation(
    name="followUps135",
    ends={
        Property(name="room_SemanticsRule136", type=room_SemanticsRule, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SemanticsRule134", type=room_SemanticsRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base138: BinaryAssociation = BinaryAssociation(
    name="base138",
    ends={
        Property(name="room_ActorClass139", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass137", type=room_ActorClass, multiplicity=Multiplicity(0, 1))
    }
)
ifPorts140: BinaryAssociation = BinaryAssociation(
    name="ifPorts140",
    ends={
        Property(name="room_Port", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass141", type=room_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations118: BinaryAssociation = BinaryAssociation(
    name="operations118",
    ends={
        Property(name="room_PortOperation120", type=room_PortClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_PortClass119", type=room_PortOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intPorts145: BinaryAssociation = BinaryAssociation(
    name="intPorts145",
    ends={
        Property(name="room_Port147", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass146", type=room_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extPorts148: BinaryAssociation = BinaryAssociation(
    name="extPorts148",
    ends={
        Property(name="room_ExternalPort", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass149", type=room_ExternalPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceImplementations150: BinaryAssociation = BinaryAssociation(
    name="serviceImplementations150",
    ends={
        Property(name="room_ServiceImplementation", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass151", type=room_ServiceImplementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strSAPs152: BinaryAssociation = BinaryAssociation(
    name="strSAPs152",
    ends={
        Property(name="room_SAPRef", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass153", type=room_SAPRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes154: BinaryAssociation = BinaryAssociation(
    name="attributes154",
    ends={
        Property(name="room_Attribute156", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass155", type=room_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
behaviorDocu157: BinaryAssociation = BinaryAssociation(
    name="behaviorDocu157",
    ends={
        Property(name="room_Documentation159", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass158", type=room_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
behaviorAnnotations160: BinaryAssociation = BinaryAssociation(
    name="behaviorAnnotations160",
    ends={
        Property(name="room_Annotation162", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass161", type=room_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations163: BinaryAssociation = BinaryAssociation(
    name="operations163",
    ends={
        Property(name="room_StandardOperation165", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass164", type=room_StandardOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateMachine166: BinaryAssociation = BinaryAssociation(
    name="stateMachine166",
    ends={
        Property(name="room_StateGraph", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass167", type=room_StateGraph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structureDocu142: BinaryAssociation = BinaryAssociation(
    name="structureDocu142",
    ends={
        Property(name="room_Documentation144", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass143", type=room_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifport174: BinaryAssociation = BinaryAssociation(
    name="ifport174",
    ends={
        Property(name="room_Port176", type=room_ExternalPort, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ExternalPort175", type=room_Port, multiplicity=Multiplicity(0, 1))
    }
)
protocol177: BinaryAssociation = BinaryAssociation(
    name="protocol177",
    ends={
        Property(name="room_ProtocolClass179", type=room_SAPRef, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SAPRef178", type=room_ProtocolClass, multiplicity=Multiplicity(0, 1))
    }
)
protocol180: BinaryAssociation = BinaryAssociation(
    name="protocol180",
    ends={
        Property(name="room_ProtocolClass182", type=room_SPPRef, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SPPRef181", type=room_ProtocolClass, multiplicity=Multiplicity(0, 1))
    }
)
spp183: BinaryAssociation = BinaryAssociation(
    name="spp183",
    ends={
        Property(name="room_SPPRef185", type=room_ServiceImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ServiceImplementation184", type=room_SPPRef, multiplicity=Multiplicity(0, 1))
    }
)
subSystems186: BinaryAssociation = BinaryAssociation(
    name="subSystems186",
    ends={
        Property(name="room_SubSystemRef", type=room_LogicalSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="room_LogicalSystem187", type=room_SubSystemRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
docu188: BinaryAssociation = BinaryAssociation(
    name="docu188",
    ends={
        Property(name="room_Documentation189", type=room_ActorContainerRef, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorContainerRef", type=room_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type190: BinaryAssociation = BinaryAssociation(
    name="type190",
    ends={
        Property(name="room_SubSystemClass192", type=room_SubSystemRef, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SubSystemRef191", type=room_SubSystemClass, multiplicity=Multiplicity(0, 1))
    }
)
relayPorts193: BinaryAssociation = BinaryAssociation(
    name="relayPorts193",
    ends={
        Property(name="room_Port195", type=room_SubSystemClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SubSystemClass194", type=room_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
threads196: BinaryAssociation = BinaryAssociation(
    name="threads196",
    ends={
        Property(name="room_LogicalThread", type=room_SubSystemClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SubSystemClass197", type=room_LogicalThread, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
protocol168: BinaryAssociation = BinaryAssociation(
    name="protocol168",
    ends={
        Property(name="room_GeneralProtocolClass170", type=room_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Port169", type=room_GeneralProtocolClass, multiplicity=Multiplicity(0, 1))
    }
)
docu171: BinaryAssociation = BinaryAssociation(
    name="docu171",
    ends={
        Property(name="room_Documentation173", type=room_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Port172", type=room_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instances198: BinaryAssociation = BinaryAssociation(
    name="instances198",
    ends={
        Property(name="room_ActorInstancePath", type=room_LogicalThread, multiplicity=Multiplicity(1, 1)),
        Property(name="room_LogicalThread199", type=room_ActorInstancePath, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endpoint1200: BinaryAssociation = BinaryAssociation(
    name="endpoint1200",
    ends={
        Property(name="room_BindingEndPoint", type=room_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Binding201", type=room_BindingEndPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
endpoint2202: BinaryAssociation = BinaryAssociation(
    name="endpoint2202",
    ends={
        Property(name="room_BindingEndPoint204", type=room_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Binding203", type=room_BindingEndPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actorRef205: BinaryAssociation = BinaryAssociation(
    name="actorRef205",
    ends={
        Property(name="room_ActorContainerRef207", type=room_BindingEndPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="room_BindingEndPoint206", type=room_ActorContainerRef, multiplicity=Multiplicity(0, 1))
    }
)
port208: BinaryAssociation = BinaryAssociation(
    name="port208",
    ends={
        Property(name="room_Port210", type=room_BindingEndPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="room_BindingEndPoint209", type=room_Port, multiplicity=Multiplicity(0, 1))
    }
)
sub211: BinaryAssociation = BinaryAssociation(
    name="sub211",
    ends={
        Property(name="room_SubProtocol213", type=room_BindingEndPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="room_BindingEndPoint212", type=room_SubProtocol, multiplicity=Multiplicity(0, 1))
    }
)
from214: BinaryAssociation = BinaryAssociation(
    name="from214",
    ends={
        Property(name="room_SAPoint", type=room_LayerConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="room_LayerConnection215", type=room_SAPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
to216: BinaryAssociation = BinaryAssociation(
    name="to216",
    ends={
        Property(name="room_SPPoint", type=room_LayerConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="room_LayerConnection217", type=room_SPPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref218: BinaryAssociation = BinaryAssociation(
    name="ref218",
    ends={
        Property(name="room_ActorContainerRef219", type=room_RefSAPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RefSAPoint", type=room_ActorContainerRef, multiplicity=Multiplicity(0, 1))
    }
)
relay220: BinaryAssociation = BinaryAssociation(
    name="relay220",
    ends={
        Property(name="room_SPPRef221", type=room_RelaySAPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RelaySAPoint", type=room_SPPRef, multiplicity=Multiplicity(0, 1))
    }
)
ref222: BinaryAssociation = BinaryAssociation(
    name="ref222",
    ends={
        Property(name="room_ActorContainerRef224", type=room_SPPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SPPoint223", type=room_ActorContainerRef, multiplicity=Multiplicity(0, 1))
    }
)
service225: BinaryAssociation = BinaryAssociation(
    name="service225",
    ends={
        Property(name="room_SPPRef227", type=room_SPPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SPPoint226", type=room_SPPRef, multiplicity=Multiplicity(0, 1))
    }
)
type228: BinaryAssociation = BinaryAssociation(
    name="type228",
    ends={
        Property(name="room_ActorClass230", type=room_ActorRef, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorRef229", type=room_ActorClass, multiplicity=Multiplicity(0, 1))
    }
)
docu231: BinaryAssociation = BinaryAssociation(
    name="docu231",
    ends={
        Property(name="room_Documentation232", type=room_State, multiplicity=Multiplicity(1, 1)),
        Property(name="room_State", type=room_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entryCode233: BinaryAssociation = BinaryAssociation(
    name="entryCode233",
    ends={
        Property(name="room_DetailCode235", type=room_State, multiplicity=Multiplicity(1, 1)),
        Property(name="room_State234", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exitCode236: BinaryAssociation = BinaryAssociation(
    name="exitCode236",
    ends={
        Property(name="room_DetailCode238", type=room_State, multiplicity=Multiplicity(1, 1)),
        Property(name="room_State237", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
doCode239: BinaryAssociation = BinaryAssociation(
    name="doCode239",
    ends={
        Property(name="room_DetailCode241", type=room_State, multiplicity=Multiplicity(1, 1)),
        Property(name="room_State240", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subgraph242: BinaryAssociation = BinaryAssociation(
    name="subgraph242",
    ends={
        Property(name="room_StateGraph244", type=room_State, multiplicity=Multiplicity(1, 1)),
        Property(name="room_State243", type=room_StateGraph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
states245: BinaryAssociation = BinaryAssociation(
    name="states245",
    ends={
        Property(name="room_State247", type=room_StateGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="room_StateGraph246", type=room_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trPoints248: BinaryAssociation = BinaryAssociation(
    name="trPoints248",
    ends={
        Property(name="room_TrPoint", type=room_StateGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="room_StateGraph249", type=room_TrPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
chPoints250: BinaryAssociation = BinaryAssociation(
    name="chPoints250",
    ends={
        Property(name="room_ChoicePoint", type=room_StateGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="room_StateGraph251", type=room_ChoicePoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions252: BinaryAssociation = BinaryAssociation(
    name="transitions252",
    ends={
        Property(name="room_Transition", type=room_StateGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="room_StateGraph253", type=room_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target256: BinaryAssociation = BinaryAssociation(
    name="target256",
    ends={
        Property(name="room_State257", type=room_RefinedState, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RefinedState", type=room_State, multiplicity=Multiplicity(0, 1))
    }
)
docu258: BinaryAssociation = BinaryAssociation(
    name="docu258",
    ends={
        Property(name="room_Documentation260", type=room_ChoicePoint, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ChoicePoint259", type=room_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
to261: BinaryAssociation = BinaryAssociation(
    name="to261",
    ends={
        Property(name="room_TransitionTerminal", type=room_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Transition262", type=room_TransitionTerminal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docu263: BinaryAssociation = BinaryAssociation(
    name="docu263",
    ends={
        Property(name="room_Documentation265", type=room_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Transition264", type=room_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action266: BinaryAssociation = BinaryAssociation(
    name="action266",
    ends={
        Property(name="room_DetailCode268", type=room_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Transition267", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refinedTransitions254: BinaryAssociation = BinaryAssociation(
    name="refinedTransitions254",
    ends={
        Property(name="room_RefinedTransition", type=room_StateGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="room_StateGraph255", type=room_RefinedTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triggers271: BinaryAssociation = BinaryAssociation(
    name="triggers271",
    ends={
        Property(name="room_Trigger", type=room_TriggeredTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="room_TriggeredTransition", type=room_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard272: BinaryAssociation = BinaryAssociation(
    name="guard272",
    ends={
        Property(name="room_DetailCode273", type=room_GuardedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="room_GuardedTransition", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition274: BinaryAssociation = BinaryAssociation(
    name="condition274",
    ends={
        Property(name="room_DetailCode275", type=room_CPBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="room_CPBranchTransition", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target276: BinaryAssociation = BinaryAssociation(
    name="target276",
    ends={
        Property(name="room_Transition278", type=room_RefinedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RefinedTransition277", type=room_Transition, multiplicity=Multiplicity(0, 1))
    }
)
docu279: BinaryAssociation = BinaryAssociation(
    name="docu279",
    ends={
        Property(name="room_Documentation281", type=room_RefinedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RefinedTransition280", type=room_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action282: BinaryAssociation = BinaryAssociation(
    name="action282",
    ends={
        Property(name="room_DetailCode284", type=room_RefinedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RefinedTransition283", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trPoint287: BinaryAssociation = BinaryAssociation(
    name="trPoint287",
    ends={
        Property(name="room_TrPoint288", type=room_TrPointTerminal, multiplicity=Multiplicity(1, 1)),
        Property(name="room_TrPointTerminal", type=room_TrPoint, multiplicity=Multiplicity(0, 1))
    }
)
from269: BinaryAssociation = BinaryAssociation(
    name="from269",
    ends={
        Property(name="room_TransitionTerminal270", type=room_NonInitialTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="room_NonInitialTransition", type=room_TransitionTerminal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trPoint289: BinaryAssociation = BinaryAssociation(
    name="trPoint289",
    ends={
        Property(name="room_TrPoint290", type=room_SubStateTrPointTerminal, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SubStateTrPointTerminal", type=room_TrPoint, multiplicity=Multiplicity(0, 1))
    }
)
state291: BinaryAssociation = BinaryAssociation(
    name="state291",
    ends={
        Property(name="room_State293", type=room_SubStateTrPointTerminal, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SubStateTrPointTerminal292", type=room_State, multiplicity=Multiplicity(0, 1))
    }
)
cp294: BinaryAssociation = BinaryAssociation(
    name="cp294",
    ends={
        Property(name="room_ChoicePoint295", type=room_ChoicepointTerminal, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ChoicepointTerminal", type=room_ChoicePoint, multiplicity=Multiplicity(0, 1))
    }
)
msgFromIfPairs296: BinaryAssociation = BinaryAssociation(
    name="msgFromIfPairs296",
    ends={
        Property(name="room_MessageFromIf", type=room_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Trigger297", type=room_MessageFromIf, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard298: BinaryAssociation = BinaryAssociation(
    name="guard298",
    ends={
        Property(name="room_Guard", type=room_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Trigger299", type=room_Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
message300: BinaryAssociation = BinaryAssociation(
    name="message300",
    ends={
        Property(name="room_Message302", type=room_MessageFromIf, multiplicity=Multiplicity(1, 1)),
        Property(name="room_MessageFromIf301", type=room_Message, multiplicity=Multiplicity(0, 1))
    }
)
from303: BinaryAssociation = BinaryAssociation(
    name="from303",
    ends={
        Property(name="room_InterfaceItem", type=room_MessageFromIf, multiplicity=Multiplicity(1, 1)),
        Property(name="room_MessageFromIf304", type=room_InterfaceItem, multiplicity=Multiplicity(0, 1))
    }
)
guard305: BinaryAssociation = BinaryAssociation(
    name="guard305",
    ends={
        Property(name="room_DetailCode307", type=room_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Guard306", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes308: BinaryAssociation = BinaryAssociation(
    name="attributes308",
    ends={
        Property(name="room_KeyValue", type=room_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Annotation309", type=room_KeyValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state285: BinaryAssociation = BinaryAssociation(
    name="state285",
    ends={
        Property(name="room_State286", type=room_StateTerminal, multiplicity=Multiplicity(1, 1)),
        Property(name="room_StateTerminal", type=room_State, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_room_StructureClass_RoomClass = Generalization(general=RoomClass, specific=room_StructureClass)
gen_room_ActorContainerClass_StructureClass = Generalization(general=StructureClass, specific=room_ActorContainerClass)
gen_room_DataType_RoomClass = Generalization(general=RoomClass, specific=room_DataType)
gen_room_ComplexType_DataType = Generalization(general=DataType, specific=room_ComplexType)
gen_room_PrimitiveType_DataType = Generalization(general=DataType, specific=room_PrimitiveType)
gen_room_ExternalType_ComplexType = Generalization(general=ComplexType, specific=room_ExternalType)
gen_room_DataClass_ComplexType = Generalization(general=ComplexType, specific=room_DataClass)
gen_room_StandardOperation_Operation = Generalization(general=Operation, specific=room_StandardOperation)
gen_room_PortOperation_Operation = Generalization(general=Operation, specific=room_PortOperation)
gen_room_GeneralProtocolClass_RoomClass = Generalization(general=RoomClass, specific=room_GeneralProtocolClass)
gen_room_ProtocolClass_GeneralProtocolClass = Generalization(general=GeneralProtocolClass, specific=room_ProtocolClass)
gen_room_CompoundProtocolClass_GeneralProtocolClass = Generalization(general=GeneralProtocolClass, specific=room_CompoundProtocolClass)
gen_room_InMessageHandler_MessageHandler = Generalization(general=MessageHandler, specific=room_InMessageHandler)
gen_room_OutMessageHandler_MessageHandler = Generalization(general=MessageHandler, specific=room_OutMessageHandler)
gen_room_InSemanticsRule_SemanticsRule = Generalization(general=SemanticsRule, specific=room_InSemanticsRule)
gen_room_OutSemanticsRule_SemanticsRule = Generalization(general=SemanticsRule, specific=room_OutSemanticsRule)
gen_room_ActorClass_ActorContainerClass = Generalization(general=ActorContainerClass, specific=room_ActorClass)
gen_room_Port_InterfaceItem = Generalization(general=InterfaceItem, specific=room_Port)
gen_room_SAPRef_InterfaceItem = Generalization(general=InterfaceItem, specific=room_SAPRef)
gen_room_SPPRef_InterfaceItem = Generalization(general=InterfaceItem, specific=room_SPPRef)
gen_room_LogicalSystem_StructureClass = Generalization(general=StructureClass, specific=room_LogicalSystem)
gen_room_SubSystemRef_ActorContainerRef = Generalization(general=ActorContainerRef, specific=room_SubSystemRef)
gen_room_SubSystemClass_ActorContainerClass = Generalization(general=ActorContainerClass, specific=room_SubSystemClass)
gen_room_RefSAPoint_SAPoint = Generalization(general=SAPoint, specific=room_RefSAPoint)
gen_room_RelaySAPoint_SAPoint = Generalization(general=SAPoint, specific=room_RelaySAPoint)
gen_room_StateGraphNode_StateGraphItem = Generalization(general=StateGraphItem, specific=room_StateGraphNode)
gen_room_State_StateGraphNode = Generalization(general=StateGraphNode, specific=room_State)
gen_room_ActorRef_ActorContainerRef = Generalization(general=ActorContainerRef, specific=room_ActorRef)
gen_room_SimpleState_State = Generalization(general=State, specific=room_SimpleState)
gen_room_RefinedState_State = Generalization(general=State, specific=room_RefinedState)
gen_room_TrPoint_StateGraphNode = Generalization(general=StateGraphNode, specific=room_TrPoint)
gen_room_TransitionPoint_TrPoint = Generalization(general=TrPoint, specific=room_TransitionPoint)
gen_room_EntryPoint_TrPoint = Generalization(general=TrPoint, specific=room_EntryPoint)
gen_room_ExitPoint_TrPoint = Generalization(general=TrPoint, specific=room_ExitPoint)
gen_room_ChoicePoint_StateGraphNode = Generalization(general=StateGraphNode, specific=room_ChoicePoint)
gen_room_Transition_StateGraphItem = Generalization(general=StateGraphItem, specific=room_Transition)
gen_room_NonInitialTransition_Transition = Generalization(general=Transition, specific=room_NonInitialTransition)
gen_room_TransitionChainStartTransition_NonInitialTransition = Generalization(general=NonInitialTransition, specific=room_TransitionChainStartTransition)
gen_room_InitialTransition_Transition = Generalization(general=Transition, specific=room_InitialTransition)
gen_room_ContinuationTransition_NonInitialTransition = Generalization(general=NonInitialTransition, specific=room_ContinuationTransition)
gen_room_TriggeredTransition_TransitionChainStartTransition = Generalization(general=TransitionChainStartTransition, specific=room_TriggeredTransition)
gen_room_GuardedTransition_TransitionChainStartTransition = Generalization(general=TransitionChainStartTransition, specific=room_GuardedTransition)
gen_room_CPBranchTransition_NonInitialTransition = Generalization(general=NonInitialTransition, specific=room_CPBranchTransition)
gen_room_SubStateTrPointTerminal_TransitionTerminal = Generalization(general=TransitionTerminal, specific=room_SubStateTrPointTerminal)
gen_room_ChoicepointTerminal_TransitionTerminal = Generalization(general=TransitionTerminal, specific=room_ChoicepointTerminal)
gen_room_StateTerminal_TransitionTerminal = Generalization(general=TransitionTerminal, specific=room_StateTerminal)
gen_room_TrPointTerminal_TransitionTerminal = Generalization(general=TransitionTerminal, specific=room_TrPointTerminal)

# Domain Model
domain_model = DomainModel(
    name="room",
    types={room_RoomModel, room_Documentation, room_Import, room_PrimitiveType, room_ExternalType, room_DataClass, room_GeneralProtocolClass, room_ActorClass, room_SubSystemClass, room_LogicalSystem, room_RoomClass, room_StructureClass, RoomClass, room_LayerConnection, room_ActorContainerClass, StructureClass, room_SPPRef, room_DetailCode, room_ActorRef, room_VarDecl, room_RefableType, room_DataType, room_ComplexType, DataType, ComplexType, room_Annotation, room_Binding, room_Attribute, room_StandardOperation, room_Operation, Operation, room_PortOperation, room_Message, room_ProtocolClass, GeneralProtocolClass, room_PortClass, room_ProtocolSemantics, room_CompoundProtocolClass, room_SubProtocol, room_MessageHandler, room_InMessageHandler, MessageHandler, room_OutMessageHandler, room_SemanticsRule, room_InSemanticsRule, SemanticsRule, room_OutSemanticsRule, ActorContainerClass, room_Port, room_ExternalPort, room_ServiceImplementation, room_SAPRef, room_StateGraph, room_InterfaceItem, InterfaceItem, room_SubSystemRef, room_ActorContainerRef, ActorContainerRef, room_LogicalThread, room_BindingEndPoint, room_SAPoint, room_SPPoint, room_RefSAPoint, SAPoint, room_RelaySAPoint, room_ActorInstancePath, room_StateGraphNode, StateGraphItem, room_StateGraphItem, room_State, StateGraphNode, room_TrPoint, room_ChoicePoint, room_Transition, room_SimpleState, State, room_RefinedState, room_TransitionPoint, TrPoint, room_EntryPoint, room_ExitPoint, room_TransitionTerminal, room_NonInitialTransition, Transition, room_RefinedTransition, room_TransitionChainStartTransition, NonInitialTransition, room_InitialTransition, room_ContinuationTransition, room_TriggeredTransition, TransitionChainStartTransition, room_Trigger, room_GuardedTransition, room_CPBranchTransition, room_SubStateTrPointTerminal, room_ChoicepointTerminal, room_MessageFromIf, room_Guard, room_KeyValue, room_StateTerminal, TransitionTerminal, room_TrPointTerminal, LiteralType, CommunicationType, ActorCommunicationType},
    associations={docu0, imports1, primitiveTypes3, externalTypes5, dataClasses7, protocolClasses9, actorClasses11, subSystemClasses13, systems15, docu17, bindings20, connections22, ifSPPs24, userCode125, userCode227, userCode330, actorRefs33, refType35, type36, base39, annotations41, userCode144, userCode247, annotations19, attributes53, operations55, refType57, docu60, arguments63, returntype65, docu68, detailCode71, sendsMsg74, annotations75, userCode350, userCode180, userCode283, userCode386, incomingMessages89, outgoingMessages92, base79, regular95, conjugate97, semantics100, subProtocols102, protocol103, data106, docu109, userCode112, attributes115, msgHandlers121, msg123, detailCode126, rules129, msg131, followUps135, base138, ifPorts140, operations118, intPorts145, extPorts148, serviceImplementations150, strSAPs152, attributes154, behaviorDocu157, behaviorAnnotations160, operations163, stateMachine166, structureDocu142, ifport174, protocol177, protocol180, spp183, subSystems186, docu188, type190, relayPorts193, threads196, protocol168, docu171, instances198, endpoint1200, endpoint2202, actorRef205, port208, sub211, from214, to216, ref218, relay220, ref222, service225, type228, docu231, entryCode233, exitCode236, doCode239, subgraph242, states245, trPoints248, chPoints250, transitions252, target256, docu258, to261, docu263, action266, refinedTransitions254, triggers271, guard272, condition274, target276, docu279, action282, trPoint287, from269, trPoint289, state291, cp294, msgFromIfPairs296, guard298, message300, from303, guard305, attributes308, state285},
    generalizations={gen_room_StructureClass_RoomClass, gen_room_ActorContainerClass_StructureClass, gen_room_DataType_RoomClass, gen_room_ComplexType_DataType, gen_room_PrimitiveType_DataType, gen_room_ExternalType_ComplexType, gen_room_DataClass_ComplexType, gen_room_StandardOperation_Operation, gen_room_PortOperation_Operation, gen_room_GeneralProtocolClass_RoomClass, gen_room_ProtocolClass_GeneralProtocolClass, gen_room_CompoundProtocolClass_GeneralProtocolClass, gen_room_InMessageHandler_MessageHandler, gen_room_OutMessageHandler_MessageHandler, gen_room_InSemanticsRule_SemanticsRule, gen_room_OutSemanticsRule_SemanticsRule, gen_room_ActorClass_ActorContainerClass, gen_room_Port_InterfaceItem, gen_room_SAPRef_InterfaceItem, gen_room_SPPRef_InterfaceItem, gen_room_LogicalSystem_StructureClass, gen_room_SubSystemRef_ActorContainerRef, gen_room_SubSystemClass_ActorContainerClass, gen_room_RefSAPoint_SAPoint, gen_room_RelaySAPoint_SAPoint, gen_room_StateGraphNode_StateGraphItem, gen_room_State_StateGraphNode, gen_room_ActorRef_ActorContainerRef, gen_room_SimpleState_State, gen_room_RefinedState_State, gen_room_TrPoint_StateGraphNode, gen_room_TransitionPoint_TrPoint, gen_room_EntryPoint_TrPoint, gen_room_ExitPoint_TrPoint, gen_room_ChoicePoint_StateGraphNode, gen_room_Transition_StateGraphItem, gen_room_NonInitialTransition_Transition, gen_room_TransitionChainStartTransition_NonInitialTransition, gen_room_InitialTransition_Transition, gen_room_ContinuationTransition_NonInitialTransition, gen_room_TriggeredTransition_TransitionChainStartTransition, gen_room_GuardedTransition_TransitionChainStartTransition, gen_room_CPBranchTransition_NonInitialTransition, gen_room_SubStateTrPointTerminal_TransitionTerminal, gen_room_ChoicepointTerminal_TransitionTerminal, gen_room_StateTerminal_TransitionTerminal, gen_room_TrPointTerminal_TransitionTerminal},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)