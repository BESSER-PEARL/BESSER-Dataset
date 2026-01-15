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
room_Import = Class(name="room::Import")
room_PrimitiveType = Class(name="room::PrimitiveType")
room_ExternalType = Class(name="room::ExternalType")
room_DataClass = Class(name="room::DataClass")
room_ProtocolClass = Class(name="room::ProtocolClass")
room_RoomModel = Class(name="room::RoomModel")
room_Documentation = Class(name="room::Documentation")
room_StructureClass = Class(name="room::StructureClass")
RoomClass = Class(name="RoomClass")
room_Binding = Class(name="room::Binding")
room_LayerConnection = Class(name="room::LayerConnection")
room_ActorContainerClass = Class(name="room::ActorContainerClass")
StructureClass = Class(name="StructureClass")
room_SPPRef = Class(name="room::SPPRef")
room_DetailCode = Class(name="room::DetailCode")
room_ActorClass = Class(name="room::ActorClass")
room_SubSystemClass = Class(name="room::SubSystemClass")
room_LogicalSystem = Class(name="room::LogicalSystem")
room_RoomClass = Class(name="room::RoomClass")
room_ActorRef = Class(name="room::ActorRef")
room_VarDecl = Class(name="room::VarDecl")
room_RefableType = Class(name="room::RefableType")
room_DataType = Class(name="room::DataType")
room_ComplexType = Class(name="room::ComplexType")
DataType = Class(name="DataType")
room_Attribute = Class(name="room::Attribute")
room_StandardOperation = Class(name="room::StandardOperation")
ComplexType = Class(name="ComplexType")
Operation = Class(name="Operation")
room_PortOperation = Class(name="room::PortOperation")
room_Message = Class(name="room::Message")
room_Operation = Class(name="room::Operation")
room_PortClass = Class(name="room::PortClass")
room_ProtocolSemantics = Class(name="room::ProtocolSemantics")
room_MessageHandler = Class(name="room::MessageHandler")
ActorContainerClass = Class(name="ActorContainerClass")
room_Port = Class(name="room::Port")
room_SemanticsRule = Class(name="room::SemanticsRule")
room_InterfaceItem = Class(name="room::InterfaceItem")
InterfaceItem = Class(name="InterfaceItem")
room_ExternalPort = Class(name="room::ExternalPort")
room_ServiceImplementation = Class(name="room::ServiceImplementation")
room_SAPRef = Class(name="room::SAPRef")
room_Annotation = Class(name="room::Annotation")
room_StateGraph = Class(name="room::StateGraph")
room_BindingEndPoint = Class(name="room::BindingEndPoint")
room_SAPoint = Class(name="room::SAPoint")
room_SPPoint = Class(name="room::SPPoint")
room_RefSAPoint = Class(name="room::RefSAPoint")
SAPoint = Class(name="SAPoint")
room_RelaySAPoint = Class(name="room::RelaySAPoint")
room_SubSystemRef = Class(name="room::SubSystemRef")
room_ActorContainerRef = Class(name="room::ActorContainerRef")
ActorContainerRef = Class(name="ActorContainerRef")
room_LogicalThread = Class(name="room::LogicalThread")
room_ActorInstancePath = Class(name="room::ActorInstancePath")
room_StateGraphNode = Class(name="room::StateGraphNode")
StateGraphItem = Class(name="StateGraphItem")
room_StateGraphItem = Class(name="room::StateGraphItem")
room_State = Class(name="room::State")
StateGraphNode = Class(name="StateGraphNode")
room_TrPoint = Class(name="room::TrPoint")
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
room_NonInitialTransition = Class(name="room::NonInitialTransition")
Transition = Class(name="Transition")
room_TransitionChainStartTransition = Class(name="room::TransitionChainStartTransition")
NonInitialTransition = Class(name="NonInitialTransition")
room_InitialTransition = Class(name="room::InitialTransition")
room_ContinuationTransition = Class(name="room::ContinuationTransition")
room_TriggeredTransition = Class(name="room::TriggeredTransition")
TransitionChainStartTransition = Class(name="TransitionChainStartTransition")
room_Trigger = Class(name="room::Trigger")
room_GuardedTransition = Class(name="room::GuardedTransition")
room_CPBranchTransition = Class(name="room::CPBranchTransition")
room_StateTerminal = Class(name="room::StateTerminal")
TransitionTerminal = Class(name="TransitionTerminal")
room_TrPointTerminal = Class(name="room::TrPointTerminal")
room_SubStateTrPointTerminal = Class(name="room::SubStateTrPointTerminal")
room_ChoicepointTerminal = Class(name="room::ChoicepointTerminal")
room_MessageFromIf = Class(name="room::MessageFromIf")
room_Guard = Class(name="room::Guard")
room_KeyValue = Class(name="room::KeyValue")

# room_Import class attributes and methods
room_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
room_Import_importURI: Property = Property(name="importURI", type=StringType)
room_Import.attributes={room_Import_importURI, room_Import_importedNamespace}

# room_PrimitiveType class attributes and methods
room_PrimitiveType_targetName: Property = Property(name="targetName", type=StringType)
room_PrimitiveType_castName: Property = Property(name="castName", type=StringType)
room_PrimitiveType_defaultValueLiteral: Property = Property(name="defaultValueLiteral", type=StringType)
room_PrimitiveType.attributes={room_PrimitiveType_castName, room_PrimitiveType_defaultValueLiteral, room_PrimitiveType_targetName}

# room_ExternalType class attributes and methods
room_ExternalType_targetName: Property = Property(name="targetName", type=StringType)
room_ExternalType.attributes={room_ExternalType_targetName}

# room_DataClass class attributes and methods

# room_ProtocolClass class attributes and methods
room_ProtocolClass_commType: Property = Property(name="commType", type=StringType)
room_ProtocolClass.attributes={room_ProtocolClass_commType}

# room_RoomModel class attributes and methods
room_RoomModel_name: Property = Property(name="name", type=StringType)
room_RoomModel.attributes={room_RoomModel_name}

# room_Documentation class attributes and methods
room_Documentation_text: Property = Property(name="text", type=StringType)
room_Documentation.attributes={room_Documentation_text}

# room_StructureClass class attributes and methods

# RoomClass class attributes and methods

# room_Binding class attributes and methods

# room_LayerConnection class attributes and methods

# room_ActorContainerClass class attributes and methods

# StructureClass class attributes and methods

# room_SPPRef class attributes and methods

# room_DetailCode class attributes and methods
room_DetailCode_commands: Property = Property(name="commands", type=StringType)
room_DetailCode.attributes={room_DetailCode_commands}

# room_ActorClass class attributes and methods
room_ActorClass_abstract: Property = Property(name="abstract", type=BooleanType)
room_ActorClass_commType: Property = Property(name="commType", type=StringType)
room_ActorClass.attributes={room_ActorClass_abstract, room_ActorClass_commType}

# room_SubSystemClass class attributes and methods

# room_LogicalSystem class attributes and methods

# room_RoomClass class attributes and methods
room_RoomClass_name: Property = Property(name="name", type=StringType)
room_RoomClass.attributes={room_RoomClass_name}

# room_ActorRef class attributes and methods

# room_VarDecl class attributes and methods
room_VarDecl_name: Property = Property(name="name", type=StringType)
room_VarDecl.attributes={room_VarDecl_name}

# room_RefableType class attributes and methods
room_RefableType_ref: Property = Property(name="ref", type=BooleanType)
room_RefableType.attributes={room_RefableType_ref}

# room_DataType class attributes and methods

# room_ComplexType class attributes and methods

# DataType class attributes and methods

# room_Attribute class attributes and methods
room_Attribute_name: Property = Property(name="name", type=StringType)
room_Attribute_size: Property = Property(name="size", type=IntegerType)
room_Attribute_defaultValueLiteral: Property = Property(name="defaultValueLiteral", type=StringType)
room_Attribute.attributes={room_Attribute_defaultValueLiteral, room_Attribute_name, room_Attribute_size}

# room_StandardOperation class attributes and methods

# ComplexType class attributes and methods

# Operation class attributes and methods

# room_PortOperation class attributes and methods

# room_Message class attributes and methods
room_Message_priv: Property = Property(name="priv", type=BooleanType)
room_Message_name: Property = Property(name="name", type=StringType)
room_Message.attributes={room_Message_priv, room_Message_name}

# room_Operation class attributes and methods
room_Operation_name: Property = Property(name="name", type=StringType)
room_Operation.attributes={room_Operation_name}

# room_PortClass class attributes and methods

# room_ProtocolSemantics class attributes and methods

# room_MessageHandler class attributes and methods

# ActorContainerClass class attributes and methods

# room_Port class attributes and methods
room_Port_conjugated: Property = Property(name="conjugated", type=BooleanType)
room_Port_multiplicity: Property = Property(name="multiplicity", type=IntegerType)
room_Port_m_isReplicated: Method = Method(name="isReplicated", parameters={}, type=BooleanType)
room_Port.attributes={room_Port_conjugated, room_Port_multiplicity}
room_Port.methods={room_Port_m_isReplicated}

# room_SemanticsRule class attributes and methods

# room_InterfaceItem class attributes and methods
room_InterfaceItem_name: Property = Property(name="name", type=StringType)
room_InterfaceItem.attributes={room_InterfaceItem_name}

# InterfaceItem class attributes and methods

# room_ExternalPort class attributes and methods

# room_ServiceImplementation class attributes and methods

# room_SAPRef class attributes and methods

# room_Annotation class attributes and methods
room_Annotation_name: Property = Property(name="name", type=StringType)
room_Annotation.attributes={room_Annotation_name}

# room_StateGraph class attributes and methods

# room_BindingEndPoint class attributes and methods

# room_SAPoint class attributes and methods

# room_SPPoint class attributes and methods

# room_RefSAPoint class attributes and methods

# SAPoint class attributes and methods

# room_RelaySAPoint class attributes and methods

# room_SubSystemRef class attributes and methods

# room_ActorContainerRef class attributes and methods
room_ActorContainerRef_name: Property = Property(name="name", type=StringType)
room_ActorContainerRef.attributes={room_ActorContainerRef_name}

# ActorContainerRef class attributes and methods

# room_LogicalThread class attributes and methods
room_LogicalThread_name: Property = Property(name="name", type=StringType)
room_LogicalThread_prio: Property = Property(name="prio", type=IntegerType)
room_LogicalThread.attributes={room_LogicalThread_name, room_LogicalThread_prio}

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

# room_NonInitialTransition class attributes and methods

# Transition class attributes and methods

# room_TransitionChainStartTransition class attributes and methods

# NonInitialTransition class attributes and methods

# room_InitialTransition class attributes and methods

# room_ContinuationTransition class attributes and methods

# room_TriggeredTransition class attributes and methods

# TransitionChainStartTransition class attributes and methods

# room_Trigger class attributes and methods

# room_GuardedTransition class attributes and methods

# room_CPBranchTransition class attributes and methods

# room_StateTerminal class attributes and methods

# TransitionTerminal class attributes and methods

# room_TrPointTerminal class attributes and methods

# room_SubStateTrPointTerminal class attributes and methods

# room_ChoicepointTerminal class attributes and methods

# room_MessageFromIf class attributes and methods

# room_Guard class attributes and methods

# room_KeyValue class attributes and methods
room_KeyValue_key: Property = Property(name="key", type=StringType)
room_KeyValue_value: Property = Property(name="value", type=StringType)
room_KeyValue.attributes={room_KeyValue_value, room_KeyValue_key}

# Relationships
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
        Property(name="room_ProtocolClass", type=room_RoomModel, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RoomModel10", type=room_ProtocolClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
docu0: BinaryAssociation = BinaryAssociation(
    name="docu0",
    ends={
        Property(name="room_Documentation", type=room_RoomModel, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RoomModel", type=room_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bindings19: BinaryAssociation = BinaryAssociation(
    name="bindings19",
    ends={
        Property(name="room_Binding", type=room_StructureClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_StructureClass", type=room_Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connections20: BinaryAssociation = BinaryAssociation(
    name="connections20",
    ends={
        Property(name="room_LayerConnection", type=room_StructureClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_StructureClass21", type=room_LayerConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ifSPPs22: BinaryAssociation = BinaryAssociation(
    name="ifSPPs22",
    ends={
        Property(name="room_SPPRef", type=room_ActorContainerClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorContainerClass", type=room_SPPRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userCode123: BinaryAssociation = BinaryAssociation(
    name="userCode123",
    ends={
        Property(name="room_DetailCode", type=room_ActorContainerClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorContainerClass24", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
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
userCode225: BinaryAssociation = BinaryAssociation(
    name="userCode225",
    ends={
        Property(name="room_DetailCode27", type=room_ActorContainerClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorContainerClass26", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
userCode328: BinaryAssociation = BinaryAssociation(
    name="userCode328",
    ends={
        Property(name="room_DetailCode30", type=room_ActorContainerClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorContainerClass29", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actorRefs31: BinaryAssociation = BinaryAssociation(
    name="actorRefs31",
    ends={
        Property(name="room_ActorRef", type=room_ActorContainerClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorContainerClass32", type=room_ActorRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type34: BinaryAssociation = BinaryAssociation(
    name="type34",
    ends={
        Property(name="room_DataType", type=room_RefableType, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RefableType35", type=room_DataType, multiplicity=Multiplicity(0, 1))
    }
)
refType33: BinaryAssociation = BinaryAssociation(
    name="refType33",
    ends={
        Property(name="room_RefableType", type=room_VarDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="room_VarDecl", type=room_RefableType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
userCode345: BinaryAssociation = BinaryAssociation(
    name="userCode345",
    ends={
        Property(name="room_DetailCode47", type=room_DataClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_DataClass46", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes48: BinaryAssociation = BinaryAssociation(
    name="attributes48",
    ends={
        Property(name="room_Attribute", type=room_DataClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_DataClass49", type=room_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations50: BinaryAssociation = BinaryAssociation(
    name="operations50",
    ends={
        Property(name="room_StandardOperation", type=room_DataClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_DataClass51", type=room_StandardOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refType52: BinaryAssociation = BinaryAssociation(
    name="refType52",
    ends={
        Property(name="room_RefableType54", type=room_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Attribute53", type=room_RefableType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base37: BinaryAssociation = BinaryAssociation(
    name="base37",
    ends={
        Property(name="room_DataClass38", type=room_DataClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_DataClass36", type=room_DataClass, multiplicity=Multiplicity(0, 1))
    }
)
userCode139: BinaryAssociation = BinaryAssociation(
    name="userCode139",
    ends={
        Property(name="room_DetailCode41", type=room_DataClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_DataClass40", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
userCode242: BinaryAssociation = BinaryAssociation(
    name="userCode242",
    ends={
        Property(name="room_DetailCode44", type=room_DataClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_DataClass43", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
detailCode66: BinaryAssociation = BinaryAssociation(
    name="detailCode66",
    ends={
        Property(name="room_DetailCode68", type=room_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Operation67", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sendsMsg69: BinaryAssociation = BinaryAssociation(
    name="sendsMsg69",
    ends={
        Property(name="room_Message", type=room_PortOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="room_PortOperation", type=room_Message, multiplicity=Multiplicity(0, 1))
    }
)
docu55: BinaryAssociation = BinaryAssociation(
    name="docu55",
    ends={
        Property(name="room_Documentation57", type=room_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Attribute56", type=room_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments58: BinaryAssociation = BinaryAssociation(
    name="arguments58",
    ends={
        Property(name="room_VarDecl59", type=room_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Operation", type=room_VarDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returntype60: BinaryAssociation = BinaryAssociation(
    name="returntype60",
    ends={
        Property(name="room_RefableType62", type=room_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Operation61", type=room_RefableType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docu63: BinaryAssociation = BinaryAssociation(
    name="docu63",
    ends={
        Property(name="room_Documentation65", type=room_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Operation64", type=room_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
incomingMessages82: BinaryAssociation = BinaryAssociation(
    name="incomingMessages82",
    ends={
        Property(name="room_ProtocolClass83", type=room_Message, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="room_Message84", type=room_ProtocolClass, multiplicity=Multiplicity(1, 1))
    }
)
outgoingMessages85: BinaryAssociation = BinaryAssociation(
    name="outgoingMessages85",
    ends={
        Property(name="room_Message87", type=room_ProtocolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ProtocolClass86", type=room_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
regular88: BinaryAssociation = BinaryAssociation(
    name="regular88",
    ends={
        Property(name="room_PortClass", type=room_ProtocolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ProtocolClass89", type=room_PortClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conjugate90: BinaryAssociation = BinaryAssociation(
    name="conjugate90",
    ends={
        Property(name="room_PortClass92", type=room_ProtocolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ProtocolClass91", type=room_PortClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
semantics93: BinaryAssociation = BinaryAssociation(
    name="semantics93",
    ends={
        Property(name="room_ProtocolSemantics", type=room_ProtocolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ProtocolClass94", type=room_ProtocolSemantics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base71: BinaryAssociation = BinaryAssociation(
    name="base71",
    ends={
        Property(name="room_ProtocolClass72", type=room_ProtocolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ProtocolClass70", type=room_ProtocolClass, multiplicity=Multiplicity(0, 1))
    }
)
userCode173: BinaryAssociation = BinaryAssociation(
    name="userCode173",
    ends={
        Property(name="room_DetailCode75", type=room_ProtocolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ProtocolClass74", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
userCode276: BinaryAssociation = BinaryAssociation(
    name="userCode276",
    ends={
        Property(name="room_DetailCode78", type=room_ProtocolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ProtocolClass77", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
userCode379: BinaryAssociation = BinaryAssociation(
    name="userCode379",
    ends={
        Property(name="room_DetailCode81", type=room_ProtocolClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ProtocolClass80", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes104: BinaryAssociation = BinaryAssociation(
    name="attributes104",
    ends={
        Property(name="room_Attribute106", type=room_PortClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_PortClass105", type=room_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations107: BinaryAssociation = BinaryAssociation(
    name="operations107",
    ends={
        Property(name="room_PortOperation109", type=room_PortClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_PortClass108", type=room_PortOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
msgHandlers110: BinaryAssociation = BinaryAssociation(
    name="msgHandlers110",
    ends={
        Property(name="room_MessageHandler", type=room_PortClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_PortClass111", type=room_MessageHandler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
msg112: BinaryAssociation = BinaryAssociation(
    name="msg112",
    ends={
        Property(name="room_Message114", type=room_MessageHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="room_MessageHandler113", type=room_Message, multiplicity=Multiplicity(0, 1))
    }
)
detailCode115: BinaryAssociation = BinaryAssociation(
    name="detailCode115",
    ends={
        Property(name="room_DetailCode117", type=room_MessageHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="room_MessageHandler116", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
data95: BinaryAssociation = BinaryAssociation(
    name="data95",
    ends={
        Property(name="room_VarDecl97", type=room_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Message96", type=room_VarDecl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docu98: BinaryAssociation = BinaryAssociation(
    name="docu98",
    ends={
        Property(name="room_Documentation100", type=room_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Message99", type=room_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
userCode101: BinaryAssociation = BinaryAssociation(
    name="userCode101",
    ends={
        Property(name="room_DetailCode103", type=room_PortClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_PortClass102", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
followUps124: BinaryAssociation = BinaryAssociation(
    name="followUps124",
    ends={
        Property(name="room_SemanticsRule125", type=room_SemanticsRule, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SemanticsRule123", type=room_SemanticsRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base127: BinaryAssociation = BinaryAssociation(
    name="base127",
    ends={
        Property(name="room_ActorClass128", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass126", type=room_ActorClass, multiplicity=Multiplicity(0, 1))
    }
)
ifPorts129: BinaryAssociation = BinaryAssociation(
    name="ifPorts129",
    ends={
        Property(name="room_Port", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass130", type=room_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structureDocu131: BinaryAssociation = BinaryAssociation(
    name="structureDocu131",
    ends={
        Property(name="room_Documentation133", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass132", type=room_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rules118: BinaryAssociation = BinaryAssociation(
    name="rules118",
    ends={
        Property(name="room_SemanticsRule", type=room_ProtocolSemantics, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ProtocolSemantics119", type=room_SemanticsRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
msg120: BinaryAssociation = BinaryAssociation(
    name="msg120",
    ends={
        Property(name="room_Message122", type=room_SemanticsRule, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SemanticsRule121", type=room_Message, multiplicity=Multiplicity(0, 1))
    }
)
stateMachine154: BinaryAssociation = BinaryAssociation(
    name="stateMachine154",
    ends={
        Property(name="room_ActorClass155", type=room_StateGraph, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="room_StateGraph", type=room_ActorClass, multiplicity=Multiplicity(1, 1))
    }
)
protocol156: BinaryAssociation = BinaryAssociation(
    name="protocol156",
    ends={
        Property(name="room_ProtocolClass157", type=room_InterfaceItem, multiplicity=Multiplicity(1, 1)),
        Property(name="room_InterfaceItem", type=room_ProtocolClass, multiplicity=Multiplicity(0, 1))
    }
)
docu158: BinaryAssociation = BinaryAssociation(
    name="docu158",
    ends={
        Property(name="room_Documentation160", type=room_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Port159", type=room_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifport161: BinaryAssociation = BinaryAssociation(
    name="ifport161",
    ends={
        Property(name="room_Port163", type=room_ExternalPort, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ExternalPort162", type=room_Port, multiplicity=Multiplicity(0, 1))
    }
)
spp164: BinaryAssociation = BinaryAssociation(
    name="spp164",
    ends={
        Property(name="room_SPPRef166", type=room_ServiceImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ServiceImplementation165", type=room_SPPRef, multiplicity=Multiplicity(0, 1))
    }
)
intPorts134: BinaryAssociation = BinaryAssociation(
    name="intPorts134",
    ends={
        Property(name="room_Port136", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass135", type=room_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extPorts137: BinaryAssociation = BinaryAssociation(
    name="extPorts137",
    ends={
        Property(name="room_ExternalPort", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass138", type=room_ExternalPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceImplementations139: BinaryAssociation = BinaryAssociation(
    name="serviceImplementations139",
    ends={
        Property(name="room_ServiceImplementation", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass140", type=room_ServiceImplementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strSAPs141: BinaryAssociation = BinaryAssociation(
    name="strSAPs141",
    ends={
        Property(name="room_SAPRef", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass142", type=room_SAPRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes143: BinaryAssociation = BinaryAssociation(
    name="attributes143",
    ends={
        Property(name="room_Attribute145", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass144", type=room_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
behaviorDocu146: BinaryAssociation = BinaryAssociation(
    name="behaviorDocu146",
    ends={
        Property(name="room_Documentation148", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass147", type=room_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations149: BinaryAssociation = BinaryAssociation(
    name="annotations149",
    ends={
        Property(name="room_Annotation", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass150", type=room_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations151: BinaryAssociation = BinaryAssociation(
    name="operations151",
    ends={
        Property(name="room_StandardOperation153", type=room_ActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorClass152", type=room_StandardOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endpoint1181: BinaryAssociation = BinaryAssociation(
    name="endpoint1181",
    ends={
        Property(name="room_BindingEndPoint", type=room_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Binding182", type=room_BindingEndPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
endpoint2183: BinaryAssociation = BinaryAssociation(
    name="endpoint2183",
    ends={
        Property(name="room_BindingEndPoint185", type=room_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Binding184", type=room_BindingEndPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actorRef186: BinaryAssociation = BinaryAssociation(
    name="actorRef186",
    ends={
        Property(name="room_ActorContainerRef188", type=room_BindingEndPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="room_BindingEndPoint187", type=room_ActorContainerRef, multiplicity=Multiplicity(0, 1))
    }
)
port189: BinaryAssociation = BinaryAssociation(
    name="port189",
    ends={
        Property(name="room_Port191", type=room_BindingEndPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="room_BindingEndPoint190", type=room_Port, multiplicity=Multiplicity(0, 1))
    }
)
from192: BinaryAssociation = BinaryAssociation(
    name="from192",
    ends={
        Property(name="room_SAPoint", type=room_LayerConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="room_LayerConnection193", type=room_SAPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
to194: BinaryAssociation = BinaryAssociation(
    name="to194",
    ends={
        Property(name="room_SPPoint", type=room_LayerConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="room_LayerConnection195", type=room_SPPoint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref196: BinaryAssociation = BinaryAssociation(
    name="ref196",
    ends={
        Property(name="room_ActorContainerRef197", type=room_RefSAPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RefSAPoint", type=room_ActorContainerRef, multiplicity=Multiplicity(0, 1))
    }
)
subSystems167: BinaryAssociation = BinaryAssociation(
    name="subSystems167",
    ends={
        Property(name="room_SubSystemRef", type=room_LogicalSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="room_LogicalSystem168", type=room_SubSystemRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
docu169: BinaryAssociation = BinaryAssociation(
    name="docu169",
    ends={
        Property(name="room_Documentation170", type=room_ActorContainerRef, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorContainerRef", type=room_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type171: BinaryAssociation = BinaryAssociation(
    name="type171",
    ends={
        Property(name="room_SubSystemClass173", type=room_SubSystemRef, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SubSystemRef172", type=room_SubSystemClass, multiplicity=Multiplicity(0, 1))
    }
)
relayPorts174: BinaryAssociation = BinaryAssociation(
    name="relayPorts174",
    ends={
        Property(name="room_Port176", type=room_SubSystemClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SubSystemClass175", type=room_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
threads177: BinaryAssociation = BinaryAssociation(
    name="threads177",
    ends={
        Property(name="room_LogicalThread", type=room_SubSystemClass, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SubSystemClass178", type=room_LogicalThread, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instances179: BinaryAssociation = BinaryAssociation(
    name="instances179",
    ends={
        Property(name="room_ActorInstancePath", type=room_LogicalThread, multiplicity=Multiplicity(1, 1)),
        Property(name="room_LogicalThread180", type=room_ActorInstancePath, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relay198: BinaryAssociation = BinaryAssociation(
    name="relay198",
    ends={
        Property(name="room_SPPRef199", type=room_RelaySAPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RelaySAPoint", type=room_SPPRef, multiplicity=Multiplicity(0, 1))
    }
)
doCode217: BinaryAssociation = BinaryAssociation(
    name="doCode217",
    ends={
        Property(name="room_State218", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="room_DetailCode219", type=room_State, multiplicity=Multiplicity(1, 1))
    }
)
ref200: BinaryAssociation = BinaryAssociation(
    name="ref200",
    ends={
        Property(name="room_ActorContainerRef202", type=room_SPPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SPPoint201", type=room_ActorContainerRef, multiplicity=Multiplicity(0, 1))
    }
)
service203: BinaryAssociation = BinaryAssociation(
    name="service203",
    ends={
        Property(name="room_SPPRef205", type=room_SPPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SPPoint204", type=room_SPPRef, multiplicity=Multiplicity(0, 1))
    }
)
type206: BinaryAssociation = BinaryAssociation(
    name="type206",
    ends={
        Property(name="room_ActorClass208", type=room_ActorRef, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ActorRef207", type=room_ActorClass, multiplicity=Multiplicity(0, 1))
    }
)
docu209: BinaryAssociation = BinaryAssociation(
    name="docu209",
    ends={
        Property(name="room_Documentation210", type=room_State, multiplicity=Multiplicity(1, 1)),
        Property(name="room_State", type=room_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entryCode211: BinaryAssociation = BinaryAssociation(
    name="entryCode211",
    ends={
        Property(name="room_DetailCode213", type=room_State, multiplicity=Multiplicity(1, 1)),
        Property(name="room_State212", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exitCode214: BinaryAssociation = BinaryAssociation(
    name="exitCode214",
    ends={
        Property(name="room_DetailCode216", type=room_State, multiplicity=Multiplicity(1, 1)),
        Property(name="room_State215", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subgraph220: BinaryAssociation = BinaryAssociation(
    name="subgraph220",
    ends={
        Property(name="room_StateGraph222", type=room_State, multiplicity=Multiplicity(1, 1)),
        Property(name="room_State221", type=room_StateGraph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
states223: BinaryAssociation = BinaryAssociation(
    name="states223",
    ends={
        Property(name="room_State225", type=room_StateGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="room_StateGraph224", type=room_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trPoints226: BinaryAssociation = BinaryAssociation(
    name="trPoints226",
    ends={
        Property(name="room_TrPoint", type=room_StateGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="room_StateGraph227", type=room_TrPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
chPoints228: BinaryAssociation = BinaryAssociation(
    name="chPoints228",
    ends={
        Property(name="room_ChoicePoint", type=room_StateGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="room_StateGraph229", type=room_ChoicePoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions230: BinaryAssociation = BinaryAssociation(
    name="transitions230",
    ends={
        Property(name="room_Transition", type=room_StateGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="room_StateGraph231", type=room_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base232: BinaryAssociation = BinaryAssociation(
    name="base232",
    ends={
        Property(name="room_BaseState", type=room_RefinedState, multiplicity=Multiplicity(1, 1)),
        Property(name="room_RefinedState", type=room_BaseState, multiplicity=Multiplicity(0, 1))
    }
)
docu233: BinaryAssociation = BinaryAssociation(
    name="docu233",
    ends={
        Property(name="room_Documentation235", type=room_ChoicePoint, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ChoicePoint234", type=room_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard247: BinaryAssociation = BinaryAssociation(
    name="guard247",
    ends={
        Property(name="room_DetailCode248", type=room_GuardedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="room_GuardedTransition", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
to236: BinaryAssociation = BinaryAssociation(
    name="to236",
    ends={
        Property(name="room_TransitionTerminal", type=room_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Transition237", type=room_TransitionTerminal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docu238: BinaryAssociation = BinaryAssociation(
    name="docu238",
    ends={
        Property(name="room_Documentation240", type=room_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Transition239", type=room_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action241: BinaryAssociation = BinaryAssociation(
    name="action241",
    ends={
        Property(name="room_DetailCode243", type=room_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Transition242", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
from244: BinaryAssociation = BinaryAssociation(
    name="from244",
    ends={
        Property(name="room_TransitionTerminal245", type=room_NonInitialTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="room_NonInitialTransition", type=room_TransitionTerminal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
triggers246: BinaryAssociation = BinaryAssociation(
    name="triggers246",
    ends={
        Property(name="room_Trigger", type=room_TriggeredTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="room_TriggeredTransition", type=room_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition249: BinaryAssociation = BinaryAssociation(
    name="condition249",
    ends={
        Property(name="room_DetailCode250", type=room_CPBranchTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="room_CPBranchTransition", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
state251: BinaryAssociation = BinaryAssociation(
    name="state251",
    ends={
        Property(name="room_BaseState252", type=room_StateTerminal, multiplicity=Multiplicity(1, 1)),
        Property(name="room_StateTerminal", type=room_BaseState, multiplicity=Multiplicity(0, 1))
    }
)
trPoint253: BinaryAssociation = BinaryAssociation(
    name="trPoint253",
    ends={
        Property(name="room_TrPoint254", type=room_TrPointTerminal, multiplicity=Multiplicity(1, 1)),
        Property(name="room_TrPointTerminal", type=room_TrPoint, multiplicity=Multiplicity(0, 1))
    }
)
message266: BinaryAssociation = BinaryAssociation(
    name="message266",
    ends={
        Property(name="room_Message268", type=room_MessageFromIf, multiplicity=Multiplicity(1, 1)),
        Property(name="room_MessageFromIf267", type=room_Message, multiplicity=Multiplicity(0, 1))
    }
)
from269: BinaryAssociation = BinaryAssociation(
    name="from269",
    ends={
        Property(name="room_InterfaceItem271", type=room_MessageFromIf, multiplicity=Multiplicity(1, 1)),
        Property(name="room_MessageFromIf270", type=room_InterfaceItem, multiplicity=Multiplicity(0, 1))
    }
)
trPoint255: BinaryAssociation = BinaryAssociation(
    name="trPoint255",
    ends={
        Property(name="room_TrPoint256", type=room_SubStateTrPointTerminal, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SubStateTrPointTerminal", type=room_TrPoint, multiplicity=Multiplicity(0, 1))
    }
)
state257: BinaryAssociation = BinaryAssociation(
    name="state257",
    ends={
        Property(name="room_BaseState259", type=room_SubStateTrPointTerminal, multiplicity=Multiplicity(1, 1)),
        Property(name="room_SubStateTrPointTerminal258", type=room_BaseState, multiplicity=Multiplicity(0, 1))
    }
)
cp260: BinaryAssociation = BinaryAssociation(
    name="cp260",
    ends={
        Property(name="room_ChoicePoint261", type=room_ChoicepointTerminal, multiplicity=Multiplicity(1, 1)),
        Property(name="room_ChoicepointTerminal", type=room_ChoicePoint, multiplicity=Multiplicity(0, 1))
    }
)
msgFromIfPairs262: BinaryAssociation = BinaryAssociation(
    name="msgFromIfPairs262",
    ends={
        Property(name="room_MessageFromIf", type=room_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Trigger263", type=room_MessageFromIf, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard264: BinaryAssociation = BinaryAssociation(
    name="guard264",
    ends={
        Property(name="room_Guard", type=room_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Trigger265", type=room_Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard272: BinaryAssociation = BinaryAssociation(
    name="guard272",
    ends={
        Property(name="room_DetailCode274", type=room_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Guard273", type=room_DetailCode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes275: BinaryAssociation = BinaryAssociation(
    name="attributes275",
    ends={
        Property(name="room_KeyValue", type=room_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="room_Annotation276", type=room_KeyValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
gen_room_ProtocolClass_RoomClass = Generalization(general=RoomClass, specific=room_ProtocolClass)
gen_room_ActorClass_ActorContainerClass = Generalization(general=ActorContainerClass, specific=room_ActorClass)
gen_room_Port_InterfaceItem = Generalization(general=InterfaceItem, specific=room_Port)
gen_room_SAPRef_InterfaceItem = Generalization(general=InterfaceItem, specific=room_SAPRef)
gen_room_SPPRef_InterfaceItem = Generalization(general=InterfaceItem, specific=room_SPPRef)
gen_room_RefSAPoint_SAPoint = Generalization(general=SAPoint, specific=room_RefSAPoint)
gen_room_RelaySAPoint_SAPoint = Generalization(general=SAPoint, specific=room_RelaySAPoint)
gen_room_LogicalSystem_StructureClass = Generalization(general=StructureClass, specific=room_LogicalSystem)
gen_room_SubSystemRef_ActorContainerRef = Generalization(general=ActorContainerRef, specific=room_SubSystemRef)
gen_room_SubSystemClass_ActorContainerClass = Generalization(general=ActorContainerClass, specific=room_SubSystemClass)
gen_room_StateGraphNode_StateGraphItem = Generalization(general=StateGraphItem, specific=room_StateGraphNode)
gen_room_State_StateGraphNode = Generalization(general=StateGraphNode, specific=room_State)
gen_room_ActorRef_ActorContainerRef = Generalization(general=ActorContainerRef, specific=room_ActorRef)
gen_room_BaseState_State = Generalization(general=State, specific=room_BaseState)
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
gen_room_StateTerminal_TransitionTerminal = Generalization(general=TransitionTerminal, specific=room_StateTerminal)
gen_room_TrPointTerminal_TransitionTerminal = Generalization(general=TransitionTerminal, specific=room_TrPointTerminal)
gen_room_SubStateTrPointTerminal_TransitionTerminal = Generalization(general=TransitionTerminal, specific=room_SubStateTrPointTerminal)
gen_room_ChoicepointTerminal_TransitionTerminal = Generalization(general=TransitionTerminal, specific=room_ChoicepointTerminal)

# Domain Model
domain_model = DomainModel(
    name="room",
    types={room_Import, room_PrimitiveType, room_ExternalType, room_DataClass, room_ProtocolClass, room_RoomModel, room_Documentation, room_StructureClass, RoomClass, room_Binding, room_LayerConnection, room_ActorContainerClass, StructureClass, room_SPPRef, room_DetailCode, room_ActorClass, room_SubSystemClass, room_LogicalSystem, room_RoomClass, room_ActorRef, room_VarDecl, room_RefableType, room_DataType, room_ComplexType, DataType, room_Attribute, room_StandardOperation, ComplexType, Operation, room_PortOperation, room_Message, room_Operation, room_PortClass, room_ProtocolSemantics, room_MessageHandler, ActorContainerClass, room_Port, room_SemanticsRule, room_InterfaceItem, InterfaceItem, room_ExternalPort, room_ServiceImplementation, room_SAPRef, room_Annotation, room_StateGraph, room_BindingEndPoint, room_SAPoint, room_SPPoint, room_RefSAPoint, SAPoint, room_RelaySAPoint, room_SubSystemRef, room_ActorContainerRef, ActorContainerRef, room_LogicalThread, room_ActorInstancePath, room_StateGraphNode, StateGraphItem, room_StateGraphItem, room_State, StateGraphNode, room_TrPoint, room_ChoicePoint, room_Transition, room_BaseState, State, room_RefinedState, room_TransitionPoint, TrPoint, room_EntryPoint, room_ExitPoint, room_TransitionTerminal, room_NonInitialTransition, Transition, room_TransitionChainStartTransition, NonInitialTransition, room_InitialTransition, room_ContinuationTransition, room_TriggeredTransition, TransitionChainStartTransition, room_Trigger, room_GuardedTransition, room_CPBranchTransition, room_StateTerminal, TransitionTerminal, room_TrPointTerminal, room_SubStateTrPointTerminal, room_ChoicepointTerminal, room_MessageFromIf, room_Guard, room_KeyValue, CommunicationType, ActorCommunicationType},
    associations={imports1, primitiveTypes3, externalTypes5, dataClasses7, protocolClasses9, docu0, bindings19, connections20, ifSPPs22, userCode123, actorClasses11, subSystemClasses13, systems15, docu17, userCode225, userCode328, actorRefs31, type34, refType33, userCode345, attributes48, operations50, refType52, base37, userCode139, userCode242, detailCode66, sendsMsg69, docu55, arguments58, returntype60, docu63, incomingMessages82, outgoingMessages85, regular88, conjugate90, semantics93, base71, userCode173, userCode276, userCode379, attributes104, operations107, msgHandlers110, msg112, detailCode115, data95, docu98, userCode101, followUps124, base127, ifPorts129, structureDocu131, rules118, msg120, stateMachine154, protocol156, docu158, ifport161, spp164, intPorts134, extPorts137, serviceImplementations139, strSAPs141, attributes143, behaviorDocu146, annotations149, operations151, endpoint1181, endpoint2183, actorRef186, port189, from192, to194, ref196, subSystems167, docu169, type171, relayPorts174, threads177, instances179, relay198, doCode217, ref200, service203, type206, docu209, entryCode211, exitCode214, subgraph220, states223, trPoints226, chPoints228, transitions230, base232, docu233, guard247, to236, docu238, action241, from244, triggers246, condition249, state251, trPoint253, message266, from269, trPoint255, state257, cp260, msgFromIfPairs262, guard264, guard272, attributes275},
    generalizations={gen_room_StructureClass_RoomClass, gen_room_ActorContainerClass_StructureClass, gen_room_DataType_RoomClass, gen_room_ComplexType_DataType, gen_room_PrimitiveType_DataType, gen_room_ExternalType_ComplexType, gen_room_DataClass_ComplexType, gen_room_StandardOperation_Operation, gen_room_PortOperation_Operation, gen_room_ProtocolClass_RoomClass, gen_room_ActorClass_ActorContainerClass, gen_room_Port_InterfaceItem, gen_room_SAPRef_InterfaceItem, gen_room_SPPRef_InterfaceItem, gen_room_RefSAPoint_SAPoint, gen_room_RelaySAPoint_SAPoint, gen_room_LogicalSystem_StructureClass, gen_room_SubSystemRef_ActorContainerRef, gen_room_SubSystemClass_ActorContainerClass, gen_room_StateGraphNode_StateGraphItem, gen_room_State_StateGraphNode, gen_room_ActorRef_ActorContainerRef, gen_room_BaseState_State, gen_room_RefinedState_State, gen_room_TrPoint_StateGraphNode, gen_room_TransitionPoint_TrPoint, gen_room_EntryPoint_TrPoint, gen_room_ExitPoint_TrPoint, gen_room_ChoicePoint_StateGraphNode, gen_room_Transition_StateGraphItem, gen_room_NonInitialTransition_Transition, gen_room_TransitionChainStartTransition_NonInitialTransition, gen_room_InitialTransition_Transition, gen_room_ContinuationTransition_NonInitialTransition, gen_room_TriggeredTransition_TransitionChainStartTransition, gen_room_GuardedTransition_TransitionChainStartTransition, gen_room_CPBranchTransition_NonInitialTransition, gen_room_StateTerminal_TransitionTerminal, gen_room_TrPointTerminal_TransitionTerminal, gen_room_SubStateTrPointTerminal_TransitionTerminal, gen_room_ChoicepointTerminal_TransitionTerminal},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)