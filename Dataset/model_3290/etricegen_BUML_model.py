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
PortKind: Enumeration = Enumeration(
    name="PortKind",
    literals={
            EnumerationLiteral(name="external"),
			EnumerationLiteral(name="internal"),
			EnumerationLiteral(name="relay"),
			EnumerationLiteral(name="interface")
    }
)

# Classes
etricegen_Root = Class(name="etricegen::Root")
etricegen_WiredStructureClass = Class(name="etricegen::WiredStructureClass", is_abstract=True)
etricegen_SystemInstance = Class(name="etricegen::SystemInstance")
etricegen_SubSystemInstance = Class(name="etricegen::SubSystemInstance")
etricegen_RoomModel = Class(name="etricegen::RoomModel")
etricegen_ExpandedActorClass = Class(name="etricegen::ExpandedActorClass")
etricegen_DataClass = Class(name="etricegen::DataClass")
etricegen_ProtocolClass = Class(name="etricegen::ProtocolClass")
etricegen_ActorClass = Class(name="etricegen::ActorClass")
etricegen_EnumerationType = Class(name="etricegen::EnumerationType")
etricegen_SubSystemClass = Class(name="etricegen::SubSystemClass")
etricegen_OptionalActorInstance = Class(name="etricegen::OptionalActorInstance")
etricegen_InstanceBase = Class(name="etricegen::InstanceBase", is_abstract=True)
etricegen_AbstractInstance = Class(name="etricegen::AbstractInstance", is_abstract=True)
InstanceBase = Class(name="InstanceBase")
etricegen_PortInstance = Class(name="etricegen::PortInstance")
etricegen_ActorInterfaceInstance = Class(name="etricegen::ActorInterfaceInstance")
AbstractInstance = Class(name="AbstractInstance")
etricegen_ServiceImplInstance = Class(name="etricegen::ServiceImplInstance")
etricegen_StructureInstance = Class(name="etricegen::StructureInstance")
etricegen_SAPInstance = Class(name="etricegen::SAPInstance")
etricegen_SPPInstance = Class(name="etricegen::SPPInstance")
etricegen_BindingInstance = Class(name="etricegen::BindingInstance")
etricegen_ConnectionInstance = Class(name="etricegen::ConnectionInstance")
etricegen_ActorInstance = Class(name="etricegen::ActorInstance")
etricegen_InterfaceItemInstance = Class(name="etricegen::InterfaceItemInstance")
etricegen_LogicalSystem = Class(name="etricegen::LogicalSystem")
StructureInstance = Class(name="StructureInstance")
InterfaceItemInstance = Class(name="InterfaceItemInstance")
etricegen_Port = Class(name="etricegen::Port")
etricegen_Binding = Class(name="etricegen::Binding")
etricegen_SAP = Class(name="etricegen::SAP")
etricegen_SPP = Class(name="etricegen::SPP")
etricegen_ServiceImplementation = Class(name="etricegen::ServiceImplementation")
etricegen_LayerConnection = Class(name="etricegen::LayerConnection")
etricegen_Wire = Class(name="etricegen::Wire")
etricegen_OpenBinding = Class(name="etricegen::OpenBinding")
etricegen_OpenServiceConnection = Class(name="etricegen::OpenServiceConnection")
etricegen_WiredActorClass = Class(name="etricegen::WiredActorClass")
WiredStructureClass = Class(name="WiredStructureClass")
etricegen_WiredSubSystemClass = Class(name="etricegen::WiredSubSystemClass")
etricegen_GraphContainer = Class(name="etricegen::GraphContainer")

# etricegen_Root class attributes and methods
etricegen_Root_library: Property = Property(name="library", type=BooleanType)
etricegen_Root_m_getReferencedProtocolClasses: Method = Method(name="getReferencedProtocolClasses", parameters={Parameter(name='cls')}, type=StringType)
etricegen_Root_m_getReferencedModels: Method = Method(name="getReferencedModels", parameters={Parameter(name='cls')}, type=StringType)
etricegen_Root_m_getReferencedDataClasses: Method = Method(name="getReferencedDataClasses", parameters={Parameter(name='cls')}, type=StringType)
etricegen_Root_m_getReferencedEnumClasses: Method = Method(name="getReferencedEnumClasses", parameters={Parameter(name='cls')}, type=StringType)
etricegen_Root_m_getReferencedActorClasses: Method = Method(name="getReferencedActorClasses", parameters={Parameter(name='cls')}, type=StringType)
etricegen_Root_m_getExpandedActorClass: Method = Method(name="getExpandedActorClass", parameters={Parameter(name='ai')}, type=StringType)
etricegen_Root_m_getExpandedActorClass: Method = Method(name="getExpandedActorClass", parameters={Parameter(name='ac')}, type=StringType)
etricegen_Root_m_getInstance: Method = Method(name="getInstance", parameters={Parameter(name='path')}, type=StringType)
etricegen_Root_m_getSubClasses: Method = Method(name="getSubClasses", parameters={Parameter(name='ac')}, type=StringType)
etricegen_Root_m_computeSubClasses: Method = Method(name="computeSubClasses", parameters={})
etricegen_Root.attributes={etricegen_Root_library}
etricegen_Root.methods={etricegen_Root_m_getReferencedModels, etricegen_Root_m_getReferencedProtocolClasses, etricegen_Root_m_getReferencedActorClasses, etricegen_Root_m_computeSubClasses, etricegen_Root_m_getReferencedDataClasses, etricegen_Root_m_getInstance, etricegen_Root_m_getSubClasses, etricegen_Root_m_getExpandedActorClass, etricegen_Root_m_getReferencedEnumClasses, etricegen_Root_m_getExpandedActorClass}

# etricegen_WiredStructureClass class attributes and methods

# etricegen_SystemInstance class attributes and methods

# etricegen_SubSystemInstance class attributes and methods
etricegen_SubSystemInstance_maxObjId: Property = Property(name="maxObjId", type=IntegerType)
etricegen_SubSystemInstance_m_getThreadId: Method = Method(name="getThreadId", parameters={Parameter(name='instance')}, type=IntegerType)
etricegen_SubSystemInstance.attributes={etricegen_SubSystemInstance_maxObjId}
etricegen_SubSystemInstance.methods={etricegen_SubSystemInstance_m_getThreadId}

# etricegen_RoomModel class attributes and methods

# etricegen_ExpandedActorClass class attributes and methods
etricegen_ExpandedActorClass_m_getInterfaceItemLocalId: Method = Method(name="getInterfaceItemLocalId", parameters={Parameter(name='ifitem')}, type=IntegerType)
etricegen_ExpandedActorClass.methods={etricegen_ExpandedActorClass_m_getInterfaceItemLocalId}

# etricegen_DataClass class attributes and methods

# etricegen_ProtocolClass class attributes and methods

# etricegen_ActorClass class attributes and methods

# etricegen_EnumerationType class attributes and methods

# etricegen_SubSystemClass class attributes and methods

# etricegen_OptionalActorInstance class attributes and methods

# etricegen_InstanceBase class attributes and methods
etricegen_InstanceBase_name: Property = Property(name="name", type=StringType)
etricegen_InstanceBase_path: Property = Property(name="path", type=StringType)
etricegen_InstanceBase_objId: Property = Property(name="objId", type=IntegerType)
etricegen_InstanceBase_threadId: Property = Property(name="threadId", type=IntegerType)
etricegen_InstanceBase_nObjIDs: Property = Property(name="nObjIDs", type=IntegerType)
etricegen_InstanceBase.attributes={etricegen_InstanceBase_nObjIDs, etricegen_InstanceBase_threadId, etricegen_InstanceBase_objId, etricegen_InstanceBase_name, etricegen_InstanceBase_path}

# etricegen_AbstractInstance class attributes and methods

# InstanceBase class attributes and methods

# etricegen_PortInstance class attributes and methods
etricegen_PortInstance_kind: Property = Property(name="kind", type=StringType)
etricegen_PortInstance.attributes={etricegen_PortInstance_kind}

# etricegen_ActorInterfaceInstance class attributes and methods
etricegen_ActorInterfaceInstance_array: Property = Property(name="array", type=BooleanType)
etricegen_ActorInterfaceInstance.attributes={etricegen_ActorInterfaceInstance_array}

# AbstractInstance class attributes and methods

# etricegen_ServiceImplInstance class attributes and methods

# etricegen_StructureInstance class attributes and methods
etricegen_StructureInstance_m_getActorInstances: Method = Method(name="getActorInstances", parameters={}, type=StringType)
etricegen_StructureInstance.methods={etricegen_StructureInstance_m_getActorInstances}

# etricegen_SAPInstance class attributes and methods

# etricegen_SPPInstance class attributes and methods

# etricegen_BindingInstance class attributes and methods

# etricegen_ConnectionInstance class attributes and methods

# etricegen_ActorInstance class attributes and methods
etricegen_ActorInstance_replIdx: Property = Property(name="replIdx", type=IntegerType)
etricegen_ActorInstance_unindexedName: Property = Property(name="unindexedName", type=StringType)
etricegen_ActorInstance.attributes={etricegen_ActorInstance_replIdx, etricegen_ActorInstance_unindexedName}

# etricegen_InterfaceItemInstance class attributes and methods
etricegen_InterfaceItemInstance_m_isReplicated: Method = Method(name="isReplicated", parameters={}, type=BooleanType)
etricegen_InterfaceItemInstance_m_isSimple: Method = Method(name="isSimple", parameters={}, type=BooleanType)
etricegen_InterfaceItemInstance_m_isRelay: Method = Method(name="isRelay", parameters={}, type=BooleanType)
etricegen_InterfaceItemInstance_m_getInterfaceItem: Method = Method(name="getInterfaceItem", parameters={}, type=StringType)
etricegen_InterfaceItemInstance.methods={etricegen_InterfaceItemInstance_m_isReplicated, etricegen_InterfaceItemInstance_m_isSimple, etricegen_InterfaceItemInstance_m_isRelay, etricegen_InterfaceItemInstance_m_getInterfaceItem}

# etricegen_LogicalSystem class attributes and methods

# StructureInstance class attributes and methods

# InterfaceItemInstance class attributes and methods

# etricegen_Port class attributes and methods

# etricegen_Binding class attributes and methods

# etricegen_SAP class attributes and methods

# etricegen_SPP class attributes and methods

# etricegen_ServiceImplementation class attributes and methods

# etricegen_LayerConnection class attributes and methods

# etricegen_Wire class attributes and methods
etricegen_Wire_dataDriven: Property = Property(name="dataDriven", type=BooleanType)
etricegen_Wire_path1: Property = Property(name="path1", type=StringType)
etricegen_Wire_path2: Property = Property(name="path2", type=StringType)
etricegen_Wire.attributes={etricegen_Wire_dataDriven, etricegen_Wire_path2, etricegen_Wire_path1}

# etricegen_OpenBinding class attributes and methods
etricegen_OpenBinding_path: Property = Property(name="path", type=StringType)
etricegen_OpenBinding.attributes={etricegen_OpenBinding_path}

# etricegen_OpenServiceConnection class attributes and methods
etricegen_OpenServiceConnection_path: Property = Property(name="path", type=StringType)
etricegen_OpenServiceConnection.attributes={etricegen_OpenServiceConnection_path}

# etricegen_WiredActorClass class attributes and methods

# WiredStructureClass class attributes and methods

# etricegen_WiredSubSystemClass class attributes and methods

# etricegen_GraphContainer class attributes and methods

# Relationships
systemInstances0: BinaryAssociation = BinaryAssociation(
    name="systemInstances0",
    ends={
        Property(name="etricegen_SystemInstance", type=etricegen_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_Root", type=etricegen_SystemInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownSubSystemInstances1: BinaryAssociation = BinaryAssociation(
    name="ownSubSystemInstances1",
    ends={
        Property(name="etricegen_SubSystemInstance", type=etricegen_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_Root2", type=etricegen_SubSystemInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subSystemInstances3: BinaryAssociation = BinaryAssociation(
    name="subSystemInstances3",
    ends={
        Property(name="etricegen_SubSystemInstance5", type=etricegen_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_Root4", type=etricegen_SubSystemInstance, multiplicity=Multiplicity(0, 9999))
    }
)
models6: BinaryAssociation = BinaryAssociation(
    name="models6",
    ends={
        Property(name="etricegen_RoomModel", type=etricegen_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_Root7", type=etricegen_RoomModel, multiplicity=Multiplicity(0, 9999))
    }
)
importedModels8: BinaryAssociation = BinaryAssociation(
    name="importedModels8",
    ends={
        Property(name="etricegen_RoomModel10", type=etricegen_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_Root9", type=etricegen_RoomModel, multiplicity=Multiplicity(0, 9999))
    }
)
xpActorClasses11: BinaryAssociation = BinaryAssociation(
    name="xpActorClasses11",
    ends={
        Property(name="etricegen_ExpandedActorClass", type=etricegen_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_Root12", type=etricegen_ExpandedActorClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataClasses13: BinaryAssociation = BinaryAssociation(
    name="dataClasses13",
    ends={
        Property(name="etricegen_DataClass", type=etricegen_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_Root14", type=etricegen_DataClass, multiplicity=Multiplicity(0, 9999))
    }
)
protocolClasses15: BinaryAssociation = BinaryAssociation(
    name="protocolClasses15",
    ends={
        Property(name="etricegen_ProtocolClass", type=etricegen_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_Root16", type=etricegen_ProtocolClass, multiplicity=Multiplicity(0, 9999))
    }
)
actorClasses17: BinaryAssociation = BinaryAssociation(
    name="actorClasses17",
    ends={
        Property(name="etricegen_ActorClass", type=etricegen_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_Root18", type=etricegen_ActorClass, multiplicity=Multiplicity(0, 9999))
    }
)
enumClasses19: BinaryAssociation = BinaryAssociation(
    name="enumClasses19",
    ends={
        Property(name="etricegen_EnumerationType", type=etricegen_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_Root20", type=etricegen_EnumerationType, multiplicity=Multiplicity(0, 9999))
    }
)
subSystemClasses21: BinaryAssociation = BinaryAssociation(
    name="subSystemClasses21",
    ends={
        Property(name="etricegen_SubSystemClass", type=etricegen_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_Root22", type=etricegen_SubSystemClass, multiplicity=Multiplicity(0, 9999))
    }
)
optionalInstances23: BinaryAssociation = BinaryAssociation(
    name="optionalInstances23",
    ends={
        Property(name="etricegen_OptionalActorInstance", type=etricegen_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_Root24", type=etricegen_OptionalActorInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
optionalActorClasses25: BinaryAssociation = BinaryAssociation(
    name="optionalActorClasses25",
    ends={
        Property(name="etricegen_ActorClass27", type=etricegen_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_Root26", type=etricegen_ActorClass, multiplicity=Multiplicity(0, 9999))
    }
)
wiredInstances28: BinaryAssociation = BinaryAssociation(
    name="wiredInstances28",
    ends={
        Property(name="etricegen_WiredStructureClass", type=etricegen_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_Root29", type=etricegen_WiredStructureClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ports30: BinaryAssociation = BinaryAssociation(
    name="ports30",
    ends={
        Property(name="etricegen_PortInstance", type=etricegen_AbstractInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_AbstractInstance", type=etricegen_PortInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actorClass31: BinaryAssociation = BinaryAssociation(
    name="actorClass31",
    ends={
        Property(name="etricegen_ActorClass32", type=etricegen_ActorInterfaceInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_ActorInterfaceInstance", type=etricegen_ActorClass, multiplicity=Multiplicity(0, 1))
    }
)
providedServices33: BinaryAssociation = BinaryAssociation(
    name="providedServices33",
    ends={
        Property(name="etricegen_ServiceImplInstance", type=etricegen_ActorInterfaceInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_ActorInterfaceInstance34", type=etricegen_ServiceImplInstance, multiplicity=Multiplicity(0, 9999))
    }
)
optionalInstances35: BinaryAssociation = BinaryAssociation(
    name="optionalInstances35",
    ends={
        Property(name="etricegen_OptionalActorInstance37", type=etricegen_ActorInterfaceInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_ActorInterfaceInstance36", type=etricegen_OptionalActorInstance, multiplicity=Multiplicity(0, 9999))
    }
)
instances38: BinaryAssociation = BinaryAssociation(
    name="instances38",
    ends={
        Property(name="etricegen_AbstractInstance39", type=etricegen_StructureInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_StructureInstance", type=etricegen_AbstractInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
saps40: BinaryAssociation = BinaryAssociation(
    name="saps40",
    ends={
        Property(name="etricegen_SAPInstance", type=etricegen_StructureInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_StructureInstance41", type=etricegen_SAPInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
spps42: BinaryAssociation = BinaryAssociation(
    name="spps42",
    ends={
        Property(name="etricegen_SPPInstance", type=etricegen_StructureInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_StructureInstance43", type=etricegen_SPPInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
services44: BinaryAssociation = BinaryAssociation(
    name="services44",
    ends={
        Property(name="etricegen_ServiceImplInstance46", type=etricegen_StructureInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_StructureInstance45", type=etricegen_ServiceImplInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindings47: BinaryAssociation = BinaryAssociation(
    name="bindings47",
    ends={
        Property(name="etricegen_BindingInstance", type=etricegen_StructureInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_StructureInstance48", type=etricegen_BindingInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connections49: BinaryAssociation = BinaryAssociation(
    name="connections49",
    ends={
        Property(name="etricegen_ConnectionInstance", type=etricegen_StructureInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_StructureInstance50", type=etricegen_ConnectionInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allContainedInstances51: BinaryAssociation = BinaryAssociation(
    name="allContainedInstances51",
    ends={
        Property(name="etricegen_ActorInstance", type=etricegen_StructureInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_StructureInstance52", type=etricegen_ActorInstance, multiplicity=Multiplicity(0, 9999))
    }
)
orderedIfItemInstances53: BinaryAssociation = BinaryAssociation(
    name="orderedIfItemInstances53",
    ends={
        Property(name="etricegen_InterfaceItemInstance", type=etricegen_StructureInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_StructureInstance54", type=etricegen_InterfaceItemInstance, multiplicity=Multiplicity(0, 9999))
    }
)
instances55: BinaryAssociation = BinaryAssociation(
    name="instances55",
    ends={
        Property(name="etricegen_SubSystemInstance57", type=etricegen_SystemInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_SystemInstance56", type=etricegen_SubSystemInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
logicalSystem58: BinaryAssociation = BinaryAssociation(
    name="logicalSystem58",
    ends={
        Property(name="etricegen_LogicalSystem", type=etricegen_SystemInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_SystemInstance59", type=etricegen_LogicalSystem, multiplicity=Multiplicity(0, 1))
    }
)
svcImpl91: BinaryAssociation = BinaryAssociation(
    name="svcImpl91",
    ends={
        Property(name="etricegen_ServiceImplementation", type=etricegen_ServiceImplInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_ServiceImplInstance92", type=etricegen_ServiceImplementation, multiplicity=Multiplicity(0, 1))
    }
)
subSystemClass60: BinaryAssociation = BinaryAssociation(
    name="subSystemClass60",
    ends={
        Property(name="etricegen_SubSystemClass62", type=etricegen_SubSystemInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_SubSystemInstance61", type=etricegen_SubSystemClass, multiplicity=Multiplicity(0, 1))
    }
)
actorClass63: BinaryAssociation = BinaryAssociation(
    name="actorClass63",
    ends={
        Property(name="etricegen_ActorClass65", type=etricegen_ActorInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_ActorInstance64", type=etricegen_ActorClass, multiplicity=Multiplicity(0, 1))
    }
)
actorClass66: BinaryAssociation = BinaryAssociation(
    name="actorClass66",
    ends={
        Property(name="etricegen_ActorClass68", type=etricegen_OptionalActorInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_OptionalActorInstance67", type=etricegen_ActorClass, multiplicity=Multiplicity(0, 1))
    }
)
requiredServices69: BinaryAssociation = BinaryAssociation(
    name="requiredServices69",
    ends={
        Property(name="etricegen_SAPInstance71", type=etricegen_OptionalActorInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_OptionalActorInstance70", type=etricegen_SAPInstance, multiplicity=Multiplicity(0, 9999))
    }
)
protocol72: BinaryAssociation = BinaryAssociation(
    name="protocol72",
    ends={
        Property(name="etricegen_ProtocolClass74", type=etricegen_InterfaceItemInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_InterfaceItemInstance73", type=etricegen_ProtocolClass, multiplicity=Multiplicity(0, 1))
    }
)
peers76: BinaryAssociation = BinaryAssociation(
    name="peers76",
    ends={
        Property(name="etricegen_InterfaceItemInstance77", type=etricegen_InterfaceItemInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_InterfaceItemInstance75", type=etricegen_InterfaceItemInstance, multiplicity=Multiplicity(0, 9999))
    }
)
port78: BinaryAssociation = BinaryAssociation(
    name="port78",
    ends={
        Property(name="etricegen_Port", type=etricegen_PortInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_PortInstance79", type=etricegen_Port, multiplicity=Multiplicity(0, 1))
    }
)
bindings80: BinaryAssociation = BinaryAssociation(
    name="bindings80",
    ends={
        Property(name="BindingInstance", type=etricegen_PortInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="ports", type=etricegen_BindingInstance, multiplicity=Multiplicity(0, 9999))
    }
)
ports81: BinaryAssociation = BinaryAssociation(
    name="ports81",
    ends={
        Property(name="PortInstance", type=etricegen_BindingInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="bindings", type=etricegen_PortInstance, multiplicity=Multiplicity(0, 2))
    }
)
binding82: BinaryAssociation = BinaryAssociation(
    name="binding82",
    ends={
        Property(name="etricegen_Binding", type=etricegen_BindingInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_BindingInstance83", type=etricegen_Binding, multiplicity=Multiplicity(0, 1))
    }
)
sap84: BinaryAssociation = BinaryAssociation(
    name="sap84",
    ends={
        Property(name="etricegen_SAP", type=etricegen_SAPInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_SAPInstance85", type=etricegen_SAP, multiplicity=Multiplicity(0, 1))
    }
)
spp86: BinaryAssociation = BinaryAssociation(
    name="spp86",
    ends={
        Property(name="etricegen_SPP", type=etricegen_SPPInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_SPPInstance87", type=etricegen_SPP, multiplicity=Multiplicity(0, 1))
    }
)
incoming88: BinaryAssociation = BinaryAssociation(
    name="incoming88",
    ends={
        Property(name="ConnectionInstance", type=etricegen_SPPInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="toSPP", type=etricegen_ConnectionInstance, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing89: BinaryAssociation = BinaryAssociation(
    name="outgoing89",
    ends={
        Property(name="ConnectionInstance90", type=etricegen_SPPInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="fromSPP", type=etricegen_ConnectionInstance, multiplicity=Multiplicity(0, 1))
    }
)
fromAI93: BinaryAssociation = BinaryAssociation(
    name="fromAI93",
    ends={
        Property(name="etricegen_AbstractInstance95", type=etricegen_ConnectionInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_ConnectionInstance94", type=etricegen_AbstractInstance, multiplicity=Multiplicity(0, 1))
    }
)
fromSPP96: BinaryAssociation = BinaryAssociation(
    name="fromSPP96",
    ends={
        Property(name="SPPInstance", type=etricegen_ConnectionInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=etricegen_SPPInstance, multiplicity=Multiplicity(0, 1))
    }
)
toSPP97: BinaryAssociation = BinaryAssociation(
    name="toSPP97",
    ends={
        Property(name="SPPInstance98", type=etricegen_ConnectionInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=etricegen_SPPInstance, multiplicity=Multiplicity(0, 1))
    }
)
connection99: BinaryAssociation = BinaryAssociation(
    name="connection99",
    ends={
        Property(name="etricegen_LayerConnection", type=etricegen_ConnectionInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_ConnectionInstance100", type=etricegen_LayerConnection, multiplicity=Multiplicity(0, 1))
    }
)
wires101: BinaryAssociation = BinaryAssociation(
    name="wires101",
    ends={
        Property(name="etricegen_Wire", type=etricegen_WiredStructureClass, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_WiredStructureClass102", type=etricegen_Wire, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
openBindings103: BinaryAssociation = BinaryAssociation(
    name="openBindings103",
    ends={
        Property(name="etricegen_OpenBinding", type=etricegen_WiredStructureClass, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_WiredStructureClass104", type=etricegen_OpenBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedServices105: BinaryAssociation = BinaryAssociation(
    name="providedServices105",
    ends={
        Property(name="etricegen_OpenServiceConnection", type=etricegen_WiredStructureClass, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_WiredStructureClass106", type=etricegen_OpenServiceConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredServices107: BinaryAssociation = BinaryAssociation(
    name="requiredServices107",
    ends={
        Property(name="etricegen_OpenServiceConnection109", type=etricegen_WiredStructureClass, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_WiredStructureClass108", type=etricegen_OpenServiceConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
port110: BinaryAssociation = BinaryAssociation(
    name="port110",
    ends={
        Property(name="etricegen_Port112", type=etricegen_OpenBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_OpenBinding111", type=etricegen_Port, multiplicity=Multiplicity(0, 1))
    }
)
protocol113: BinaryAssociation = BinaryAssociation(
    name="protocol113",
    ends={
        Property(name="etricegen_ProtocolClass115", type=etricegen_OpenServiceConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_OpenServiceConnection114", type=etricegen_ProtocolClass, multiplicity=Multiplicity(0, 1))
    }
)
actorClass116: BinaryAssociation = BinaryAssociation(
    name="actorClass116",
    ends={
        Property(name="etricegen_ActorClass117", type=etricegen_WiredActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_WiredActorClass", type=etricegen_ActorClass, multiplicity=Multiplicity(0, 1))
    }
)
subSystemClass118: BinaryAssociation = BinaryAssociation(
    name="subSystemClass118",
    ends={
        Property(name="etricegen_SubSystemClass119", type=etricegen_WiredSubSystemClass, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_WiredSubSystemClass", type=etricegen_SubSystemClass, multiplicity=Multiplicity(0, 1))
    }
)
actorClass120: BinaryAssociation = BinaryAssociation(
    name="actorClass120",
    ends={
        Property(name="etricegen_ActorClass122", type=etricegen_ExpandedActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_ExpandedActorClass121", type=etricegen_ActorClass, multiplicity=Multiplicity(0, 1))
    }
)
graphContainer123: BinaryAssociation = BinaryAssociation(
    name="graphContainer123",
    ends={
        Property(name="etricegen_GraphContainer", type=etricegen_ExpandedActorClass, multiplicity=Multiplicity(1, 1)),
        Property(name="etricegen_ExpandedActorClass124", type=etricegen_GraphContainer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_etricegen_SubSystemInstance_StructureInstance = Generalization(general=StructureInstance, specific=etricegen_SubSystemInstance)
gen_etricegen_AbstractInstance_InstanceBase = Generalization(general=InstanceBase, specific=etricegen_AbstractInstance)
gen_etricegen_ActorInterfaceInstance_AbstractInstance = Generalization(general=AbstractInstance, specific=etricegen_ActorInterfaceInstance)
gen_etricegen_StructureInstance_AbstractInstance = Generalization(general=AbstractInstance, specific=etricegen_StructureInstance)
gen_etricegen_SystemInstance_InstanceBase = Generalization(general=InstanceBase, specific=etricegen_SystemInstance)
gen_etricegen_ActorInstance_StructureInstance = Generalization(general=StructureInstance, specific=etricegen_ActorInstance)
gen_etricegen_OptionalActorInstance_StructureInstance = Generalization(general=StructureInstance, specific=etricegen_OptionalActorInstance)
gen_etricegen_InterfaceItemInstance_InstanceBase = Generalization(general=InstanceBase, specific=etricegen_InterfaceItemInstance)
gen_etricegen_PortInstance_InterfaceItemInstance = Generalization(general=InterfaceItemInstance, specific=etricegen_PortInstance)
gen_etricegen_SAPInstance_InterfaceItemInstance = Generalization(general=InterfaceItemInstance, specific=etricegen_SAPInstance)
gen_etricegen_SPPInstance_InstanceBase = Generalization(general=InstanceBase, specific=etricegen_SPPInstance)
gen_etricegen_ServiceImplInstance_InterfaceItemInstance = Generalization(general=InterfaceItemInstance, specific=etricegen_ServiceImplInstance)
gen_etricegen_WiredActorClass_WiredStructureClass = Generalization(general=WiredStructureClass, specific=etricegen_WiredActorClass)
gen_etricegen_WiredSubSystemClass_WiredStructureClass = Generalization(general=WiredStructureClass, specific=etricegen_WiredSubSystemClass)

# Domain Model
domain_model = DomainModel(
    name="etricegen",
    types={etricegen_Root, etricegen_WiredStructureClass, etricegen_SystemInstance, etricegen_SubSystemInstance, etricegen_RoomModel, etricegen_ExpandedActorClass, etricegen_DataClass, etricegen_ProtocolClass, etricegen_ActorClass, etricegen_EnumerationType, etricegen_SubSystemClass, etricegen_OptionalActorInstance, etricegen_InstanceBase, etricegen_AbstractInstance, InstanceBase, etricegen_PortInstance, etricegen_ActorInterfaceInstance, AbstractInstance, etricegen_ServiceImplInstance, etricegen_StructureInstance, etricegen_SAPInstance, etricegen_SPPInstance, etricegen_BindingInstance, etricegen_ConnectionInstance, etricegen_ActorInstance, etricegen_InterfaceItemInstance, etricegen_LogicalSystem, StructureInstance, InterfaceItemInstance, etricegen_Port, etricegen_Binding, etricegen_SAP, etricegen_SPP, etricegen_ServiceImplementation, etricegen_LayerConnection, etricegen_Wire, etricegen_OpenBinding, etricegen_OpenServiceConnection, etricegen_WiredActorClass, WiredStructureClass, etricegen_WiredSubSystemClass, etricegen_GraphContainer, PortKind},
    associations={systemInstances0, ownSubSystemInstances1, subSystemInstances3, models6, importedModels8, xpActorClasses11, dataClasses13, protocolClasses15, actorClasses17, enumClasses19, subSystemClasses21, optionalInstances23, optionalActorClasses25, wiredInstances28, ports30, actorClass31, providedServices33, optionalInstances35, instances38, saps40, spps42, services44, bindings47, connections49, allContainedInstances51, orderedIfItemInstances53, instances55, logicalSystem58, svcImpl91, subSystemClass60, actorClass63, actorClass66, requiredServices69, protocol72, peers76, port78, bindings80, ports81, binding82, sap84, spp86, incoming88, outgoing89, fromAI93, fromSPP96, toSPP97, connection99, wires101, openBindings103, providedServices105, requiredServices107, port110, protocol113, actorClass116, subSystemClass118, actorClass120, graphContainer123},
    generalizations={gen_etricegen_SubSystemInstance_StructureInstance, gen_etricegen_AbstractInstance_InstanceBase, gen_etricegen_ActorInterfaceInstance_AbstractInstance, gen_etricegen_StructureInstance_AbstractInstance, gen_etricegen_SystemInstance_InstanceBase, gen_etricegen_ActorInstance_StructureInstance, gen_etricegen_OptionalActorInstance_StructureInstance, gen_etricegen_InterfaceItemInstance_InstanceBase, gen_etricegen_PortInstance_InterfaceItemInstance, gen_etricegen_SAPInstance_InterfaceItemInstance, gen_etricegen_SPPInstance_InstanceBase, gen_etricegen_ServiceImplInstance_InterfaceItemInstance, gen_etricegen_WiredActorClass_WiredStructureClass, gen_etricegen_WiredSubSystemClass_WiredStructureClass},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)