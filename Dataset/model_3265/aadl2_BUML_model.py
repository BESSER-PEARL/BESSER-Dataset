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
FlowKind: Enumeration = Enumeration(
    name="FlowKind",
    literals={
            EnumerationLiteral(name="source"),
			EnumerationLiteral(name="path"),
			EnumerationLiteral(name="sink")
    }
)

DirectionType: Enumeration = Enumeration(
    name="DirectionType",
    literals={
            EnumerationLiteral(name="out"),
			EnumerationLiteral(name="inOut"),
			EnumerationLiteral(name="in")
    }
)

PortCategory: Enumeration = Enumeration(
    name="PortCategory",
    literals={
            EnumerationLiteral(name="data"),
			EnumerationLiteral(name="event"),
			EnumerationLiteral(name="eventData")
    }
)

AccessType: Enumeration = Enumeration(
    name="AccessType",
    literals={
            EnumerationLiteral(name="provides"),
			EnumerationLiteral(name="requires")
    }
)

AccessCategory: Enumeration = Enumeration(
    name="AccessCategory",
    literals={
            EnumerationLiteral(name="bus"),
			EnumerationLiteral(name="data"),
			EnumerationLiteral(name="subprogram"),
			EnumerationLiteral(name="subprogramGroup"),
			EnumerationLiteral(name="virtualBus")
    }
)

ComponentCategory: Enumeration = Enumeration(
    name="ComponentCategory",
    literals={
            EnumerationLiteral(name="abstract"),
			EnumerationLiteral(name="bus"),
			EnumerationLiteral(name="data"),
			EnumerationLiteral(name="device"),
			EnumerationLiteral(name="memory"),
			EnumerationLiteral(name="process"),
			EnumerationLiteral(name="processor"),
			EnumerationLiteral(name="subprogram"),
			EnumerationLiteral(name="subprogramGroup"),
			EnumerationLiteral(name="system"),
			EnumerationLiteral(name="thread"),
			EnumerationLiteral(name="threadGroup"),
			EnumerationLiteral(name="virtualBus"),
			EnumerationLiteral(name="virtualProcessor")
    }
)

OperationKind: Enumeration = Enumeration(
    name="OperationKind",
    literals={
            EnumerationLiteral(name="and"),
			EnumerationLiteral(name="or"),
			EnumerationLiteral(name="not"),
			EnumerationLiteral(name="plus"),
			EnumerationLiteral(name="minus")
    }
)

# Classes
aadl2_Element = Class(name="aadl2::Element", is_abstract=True)
Element = Class(name="Element")
aadl2_Type = Class(name="aadl2::Type", is_abstract=True)
NamedElement = Class(name="NamedElement")
aadl2_NamedElement = Class(name="aadl2::NamedElement", is_abstract=True)
aadl2_Comment = Class(name="aadl2::Comment")
aadl2_PropertyAssociation = Class(name="aadl2::PropertyAssociation")
aadl2_Property = Class(name="aadl2::Property")
aadl2_ContainedNamedElement = Class(name="aadl2::ContainedNamedElement")
aadl2_Classifier = Class(name="aadl2::Classifier", is_abstract=True)
BasicProperty = Class(name="BasicProperty")
AbstractNamedValue = Class(name="AbstractNamedValue")
aadl2_PropertyExpression = Class(name="aadl2::PropertyExpression", is_abstract=True)
aadl2_MetaclassReference = Class(name="aadl2::MetaclassReference")
aadl2_PropertyOwner = Class(name="aadl2::PropertyOwner", is_abstract=True)
aadl2_BasicProperty = Class(name="aadl2::BasicProperty")
TypedElement = Class(name="TypedElement")
aadl2_PropertyType = Class(name="aadl2::PropertyType", is_abstract=True)
aadl2_ModalPropertyValue = Class(name="aadl2::ModalPropertyValue")
Type = Class(name="Type")
aadl2_AbstractNamedValue = Class(name="aadl2::AbstractNamedValue", is_abstract=True)
PropertyOwner = Class(name="PropertyOwner")
Namespace = Class(name="Namespace")
aadl2_ClassifierFeature = Class(name="aadl2::ClassifierFeature", is_abstract=True)
aadl2_Generalization = Class(name="aadl2::Generalization", is_abstract=True)
aadl2_TypedElement = Class(name="aadl2::TypedElement", is_abstract=True)
aadl2_Namespace = Class(name="aadl2::Namespace", is_abstract=True)
aadl2_AnnexSubclause = Class(name="aadl2::AnnexSubclause", is_abstract=True)
aadl2_Prototype = Class(name="aadl2::Prototype", is_abstract=True)
aadl2_PrototypeBinding = Class(name="aadl2::PrototypeBinding", is_abstract=True)
DirectedRelationship = Class(name="DirectedRelationship")
aadl2_DirectedRelationship = Class(name="aadl2::DirectedRelationship", is_abstract=True)
Relationship = Class(name="Relationship")
aadl2_Relationship = Class(name="aadl2::Relationship", is_abstract=True)
ModalElement = Class(name="ModalElement")
aadl2_ModalElement = Class(name="aadl2::ModalElement")
aadl2_Mode = Class(name="aadl2::Mode")
aadl2_ModeFeature = Class(name="aadl2::ModeFeature", is_abstract=True)
ClassifierFeature = Class(name="ClassifierFeature")
StructuralFeature = Class(name="StructuralFeature")
CalledSubprogram = Class(name="CalledSubprogram")
aadl2_StructuralFeature = Class(name="aadl2::StructuralFeature", is_abstract=True)
RefinableElement = Class(name="RefinableElement")
ModeFeature = Class(name="ModeFeature")
aadl2_CalledSubprogram = Class(name="aadl2::CalledSubprogram", is_abstract=True)
aadl2_ContainmentPathElement = Class(name="aadl2::ContainmentPathElement")
aadl2_RefinableElement = Class(name="aadl2::RefinableElement", is_abstract=True)
aadl2_BehavioralFeature = Class(name="aadl2::BehavioralFeature", is_abstract=True)
aadl2_ArrayDimension = Class(name="aadl2::ArrayDimension")
aadl2_ArraySize = Class(name="aadl2::ArraySize")
aadl2_ArrayRange = Class(name="aadl2::ArrayRange")
aadl2_ArrayableElement = Class(name="aadl2::ArrayableElement", is_abstract=True)
aadl2_ComponentImplementationReference = Class(name="aadl2::ComponentImplementationReference")
aadl2_ComponentImplementation = Class(name="aadl2::ComponentImplementation", is_abstract=True)
ComponentClassifier = Class(name="ComponentClassifier")
aadl2_ComponentType = Class(name="aadl2::ComponentType", is_abstract=True)
aadl2_Subcomponent = Class(name="aadl2::Subcomponent", is_abstract=True)
aadl2_ArraySizeProperty = Class(name="aadl2::ArraySizeProperty", is_abstract=True)
aadl2_Realization = Class(name="aadl2::Realization")
aadl2_EndToEndFlow = Class(name="aadl2::EndToEndFlow")
aadl2_AbstractSubcomponent = Class(name="aadl2::AbstractSubcomponent")
aadl2_AccessConnection = Class(name="aadl2::AccessConnection")
aadl2_ParameterConnection = Class(name="aadl2::ParameterConnection")
aadl2_PortConnection = Class(name="aadl2::PortConnection")
aadl2_FeatureConnection = Class(name="aadl2::FeatureConnection")
aadl2_FeatureGroupConnection = Class(name="aadl2::FeatureGroupConnection")
aadl2_FlowImplementation = Class(name="aadl2::FlowImplementation")
aadl2_Connection = Class(name="aadl2::Connection", is_abstract=True)
aadl2_ImplementationExtension = Class(name="aadl2::ImplementationExtension")
aadl2_ProcessorFeature = Class(name="aadl2::ProcessorFeature", is_abstract=True)
aadl2_InternalFeature = Class(name="aadl2::InternalFeature", is_abstract=True)
aadl2_EventSource = Class(name="aadl2::EventSource")
aadl2_EventDataSource = Class(name="aadl2::EventDataSource")
aadl2_ComponentClassifier = Class(name="aadl2::ComponentClassifier", is_abstract=True)
Classifier = Class(name="Classifier")
SubcomponentType = Class(name="SubcomponentType")
FeatureClassifier = Class(name="FeatureClassifier")
aadl2_ModeTransition = Class(name="aadl2::ModeTransition")
aadl2_SubcomponentType = Class(name="aadl2::SubcomponentType", is_abstract=True)
aadl2_FeatureClassifier = Class(name="aadl2::FeatureClassifier", is_abstract=True)
aadl2_PortProxy = Class(name="aadl2::PortProxy")
aadl2_SubprogramProxy = Class(name="aadl2::SubprogramProxy")
aadl2_Context = Class(name="aadl2::Context", is_abstract=True)
aadl2_TriggerPort = Class(name="aadl2::TriggerPort", is_abstract=True)
aadl2_Feature = Class(name="aadl2::Feature", is_abstract=True)
aadl2_FlowSpecification = Class(name="aadl2::FlowSpecification")
aadl2_TypeExtension = Class(name="aadl2::TypeExtension")
aadl2_ModeTransitionTrigger = Class(name="aadl2::ModeTransitionTrigger")
FeatureConnectionEnd = Class(name="FeatureConnectionEnd")
ArrayableElement = Class(name="ArrayableElement")
aadl2_ComponentPrototype = Class(name="aadl2::ComponentPrototype", is_abstract=True)
aadl2_FeatureConnectionEnd = Class(name="aadl2::FeatureConnectionEnd", is_abstract=True)
aadl2_FeatureGroup = Class(name="aadl2::FeatureGroup")
aadl2_AbstractFeature = Class(name="aadl2::AbstractFeature")
FlowFeature = Class(name="FlowFeature")
ModalPath = Class(name="ModalPath")
FlowElement = Class(name="FlowElement")
aadl2_FlowEnd = Class(name="aadl2::FlowEnd")
aadl2_FlowFeature = Class(name="aadl2::FlowFeature", is_abstract=True)
ConnectionEnd = Class(name="ConnectionEnd")
aadl2_ConnectionEnd = Class(name="aadl2::ConnectionEnd", is_abstract=True)
Prototype = Class(name="Prototype")
aadl2_FlowElement = Class(name="aadl2::FlowElement", is_abstract=True)
EndToEndFlowElement = Class(name="EndToEndFlowElement")
aadl2_EndToEndFlowElement = Class(name="aadl2::EndToEndFlowElement", is_abstract=True)
Flow = Class(name="Flow")
aadl2_Flow = Class(name="aadl2::Flow", is_abstract=True)
aadl2_ModalPath = Class(name="aadl2::ModalPath", is_abstract=True)
Generalization = Class(name="Generalization")
DirectedFeature = Class(name="DirectedFeature")
Context = Class(name="Context")
FeatureGroupConnectionEnd = Class(name="FeatureGroupConnectionEnd")
CallContext = Class(name="CallContext")
aadl2_FeatureType = Class(name="aadl2::FeatureType", is_abstract=True)
aadl2_FeatureGroupType = Class(name="aadl2::FeatureGroupType")
aadl2_FeatureGroupPrototype = Class(name="aadl2::FeatureGroupPrototype")
aadl2_FeatureGroupConnectionEnd = Class(name="aadl2::FeatureGroupConnectionEnd", is_abstract=True)
FeatureType = Class(name="FeatureType")
aadl2_GroupExtension = Class(name="aadl2::GroupExtension")
aadl2_BusAccess = Class(name="aadl2::BusAccess")
aadl2_DataAccess = Class(name="aadl2::DataAccess")
aadl2_DataPort = Class(name="aadl2::DataPort")
aadl2_CallContext = Class(name="aadl2::CallContext", is_abstract=True)
aadl2_EventDataPort = Class(name="aadl2::EventDataPort")
aadl2_DirectedFeature = Class(name="aadl2::DirectedFeature", is_abstract=True)
Feature = Class(name="Feature")
aadl2_SubprogramAccess = Class(name="aadl2::SubprogramAccess")
aadl2_SubprogramGroupAccess = Class(name="aadl2::SubprogramGroupAccess")
Access = Class(name="Access")
aadl2_BusFeatureClassifier = Class(name="aadl2::BusFeatureClassifier", is_abstract=True)
aadl2_Access = Class(name="aadl2::Access", is_abstract=True)
AccessConnectionEnd = Class(name="AccessConnectionEnd")
aadl2_AccessConnectionEnd = Class(name="aadl2::AccessConnectionEnd", is_abstract=True)
aadl2_EventPort = Class(name="aadl2::EventPort")
aadl2_Parameter = Class(name="aadl2::Parameter")
aadl2_DataSubcomponentType = Class(name="aadl2::DataSubcomponentType", is_abstract=True)
aadl2_ParameterConnectionEnd = Class(name="aadl2::ParameterConnectionEnd", is_abstract=True)
aadl2_PortConnectionEnd = Class(name="aadl2::PortConnectionEnd", is_abstract=True)
AbstractFeatureClassifier = Class(name="AbstractFeatureClassifier")
aadl2_AbstractFeatureClassifier = Class(name="aadl2::AbstractFeatureClassifier")
Port = Class(name="Port")
aadl2_Port = Class(name="aadl2::Port", is_abstract=True)
TriggerPort = Class(name="TriggerPort")
ParameterConnectionEnd = Class(name="ParameterConnectionEnd")
PortConnectionEnd = Class(name="PortConnectionEnd")
aadl2_SubprogramSubcomponentType = Class(name="aadl2::SubprogramSubcomponentType", is_abstract=True)
aadl2_SubprogramGroupSubcomponentType = Class(name="aadl2::SubprogramGroupSubcomponentType", is_abstract=True)
aadl2_FeaturePrototype = Class(name="aadl2::FeaturePrototype")
aadl2_ModeBinding = Class(name="aadl2::ModeBinding")
aadl2_FlowSegment = Class(name="aadl2::FlowSegment")
aadl2_ConnectedElement = Class(name="aadl2::ConnectedElement")
aadl2_EndToEndFlowSegment = Class(name="aadl2::EndToEndFlowSegment")
Subcomponent = Class(name="Subcomponent")
Abstract = Class(name="Abstract")
aadl2_AbstractSubcomponentType = Class(name="aadl2::AbstractSubcomponentType", is_abstract=True)
aadl2_Abstract = Class(name="aadl2::Abstract", is_abstract=True)
Connection = Class(name="Connection")
InternalFeature = Class(name="InternalFeature")
aadl2_DataClassifier = Class(name="aadl2::DataClassifier", is_abstract=True)
Data = Class(name="Data")
DataSubcomponentType = Class(name="DataSubcomponentType")
aadl2_Data = Class(name="aadl2::Data", is_abstract=True)
ProcessorFeature = Class(name="ProcessorFeature")
Subprogram = Class(name="Subprogram")
SubprogramSubcomponentType = Class(name="SubprogramSubcomponentType")
aadl2_Subprogram = Class(name="aadl2::Subprogram", is_abstract=True)
aadl2_AnnexLibrary = Class(name="aadl2::AnnexLibrary", is_abstract=True)
aadl2_DefaultAnnexLibrary = Class(name="aadl2::DefaultAnnexLibrary")
AnnexLibrary = Class(name="AnnexLibrary")
aadl2_DefaultAnnexSubclause = Class(name="aadl2::DefaultAnnexSubclause")
AnnexSubclause = Class(name="AnnexSubclause")
aadl2_SubprogramClassifier = Class(name="aadl2::SubprogramClassifier", is_abstract=True)
aadl2_PackageRename = Class(name="aadl2::PackageRename")
aadl2_ComponentTypeRename = Class(name="aadl2::ComponentTypeRename")
aadl2_FeatureGroupTypeRename = Class(name="aadl2::FeatureGroupTypeRename")
aadl2_ModelUnit = Class(name="aadl2::ModelUnit", is_abstract=True)
aadl2_PublicPackageSection = Class(name="aadl2::PublicPackageSection")
PackageSection = Class(name="PackageSection")
aadl2_PrivatePackageSection = Class(name="aadl2::PrivatePackageSection")
aadl2_PackageSection = Class(name="aadl2::PackageSection", is_abstract=True)
aadl2_AadlPackage = Class(name="aadl2::AadlPackage")
ModelUnit = Class(name="ModelUnit")
aadl2_FeatureGroupPrototypeBinding = Class(name="aadl2::FeatureGroupPrototypeBinding")
aadl2_FeatureGroupPrototypeActual = Class(name="aadl2::FeatureGroupPrototypeActual")
FeaturePrototypeActual = Class(name="FeaturePrototypeActual")
aadl2_ComponentPrototypeBinding = Class(name="aadl2::ComponentPrototypeBinding")
PrototypeBinding = Class(name="PrototypeBinding")
aadl2_ComponentPrototypeActual = Class(name="aadl2::ComponentPrototypeActual")
aadl2_AccessSpecification = Class(name="aadl2::AccessSpecification")
aadl2_PortSpecification = Class(name="aadl2::PortSpecification")
aadl2_FeaturePrototypeActual = Class(name="aadl2::FeaturePrototypeActual", is_abstract=True)
aadl2_FeaturePrototypeBinding = Class(name="aadl2::FeaturePrototypeBinding")
aadl2_SubprogramCallSequence = Class(name="aadl2::SubprogramCallSequence")
BehavioralFeature = Class(name="BehavioralFeature")
aadl2_SubprogramCall = Class(name="aadl2::SubprogramCall")
aadl2_BehavioredImplementation = Class(name="aadl2::BehavioredImplementation", is_abstract=True)
ComponentImplementation = Class(name="ComponentImplementation")
aadl2_AbstractType = Class(name="aadl2::AbstractType")
ComponentType = Class(name="ComponentType")
AbstractClassifier = Class(name="AbstractClassifier")
aadl2_FeaturePrototypeReference = Class(name="aadl2::FeaturePrototypeReference")
aadl2_AbstractClassifier = Class(name="aadl2::AbstractClassifier", is_abstract=True)
AbstractSubcomponentType = Class(name="AbstractSubcomponentType")
BusSubcomponentType = Class(name="BusSubcomponentType")
DeviceSubcomponentType = Class(name="DeviceSubcomponentType")
MemorySubcomponentType = Class(name="MemorySubcomponentType")
ProcessorSubcomponentType = Class(name="ProcessorSubcomponentType")
ProcessSubcomponentType = Class(name="ProcessSubcomponentType")
SubprogramGroupSubcomponentType = Class(name="SubprogramGroupSubcomponentType")
SystemSubcomponentType = Class(name="SystemSubcomponentType")
aadl2_VirtualBusSubcomponentType = Class(name="aadl2::VirtualBusSubcomponentType", is_abstract=True)
BusFeatureClassifier = Class(name="BusFeatureClassifier")
aadl2_ThreadGroupSubcomponentType = Class(name="aadl2::ThreadGroupSubcomponentType", is_abstract=True)
aadl2_ThreadSubcomponentType = Class(name="aadl2::ThreadSubcomponentType", is_abstract=True)
aadl2_SystemSubcomponentType = Class(name="aadl2::SystemSubcomponentType", is_abstract=True)
aadl2_ProcessSubcomponentType = Class(name="aadl2::ProcessSubcomponentType", is_abstract=True)
aadl2_MemorySubcomponentType = Class(name="aadl2::MemorySubcomponentType", is_abstract=True)
aadl2_DeviceSubcomponentType = Class(name="aadl2::DeviceSubcomponentType", is_abstract=True)
aadl2_BusSubcomponentType = Class(name="aadl2::BusSubcomponentType", is_abstract=True)
aadl2_ProcessorSubcomponentType = Class(name="aadl2::ProcessorSubcomponentType", is_abstract=True)
ThreadGroupSubcomponentType = Class(name="ThreadGroupSubcomponentType")
aadl2_AbstractImplementation = Class(name="aadl2::AbstractImplementation")
BehavioredImplementation = Class(name="BehavioredImplementation")
ThreadSubcomponentType = Class(name="ThreadSubcomponentType")
VirtualBusSubcomponentType = Class(name="VirtualBusSubcomponentType")
VirtualProcessorSubcomponentType = Class(name="VirtualProcessorSubcomponentType")
aadl2_VirtualProcessorSubcomponentType = Class(name="aadl2::VirtualProcessorSubcomponentType", is_abstract=True)
aadl2_DataSubcomponent = Class(name="aadl2::DataSubcomponent")
aadl2_DeviceSubcomponent = Class(name="aadl2::DeviceSubcomponent")
aadl2_MemorySubcomponent = Class(name="aadl2::MemorySubcomponent")
aadl2_ProcessSubcomponent = Class(name="aadl2::ProcessSubcomponent")
aadl2_ProcessorSubcomponent = Class(name="aadl2::ProcessorSubcomponent")
aadl2_SystemSubcomponent = Class(name="aadl2::SystemSubcomponent")
aadl2_SubprogramSubcomponent = Class(name="aadl2::SubprogramSubcomponent")
aadl2_SubprogramGroupSubcomponent = Class(name="aadl2::SubprogramGroupSubcomponent")
aadl2_ThreadSubcomponent = Class(name="aadl2::ThreadSubcomponent")
aadl2_BusSubcomponent = Class(name="aadl2::BusSubcomponent")
aadl2_VirtualBusSubcomponent = Class(name="aadl2::VirtualBusSubcomponent")
aadl2_VirtualProcessorSubcomponent = Class(name="aadl2::VirtualProcessorSubcomponent")
Bus = Class(name="Bus")
aadl2_Bus = Class(name="aadl2::Bus", is_abstract=True)
aadl2_ThreadGroupSubcomponent = Class(name="aadl2::ThreadGroupSubcomponent")
aadl2_Memory = Class(name="aadl2::Memory", is_abstract=True)
Process = Class(name="Process")
aadl2_Process = Class(name="aadl2::Process", is_abstract=True)
Device = Class(name="Device")
Processor = Class(name="Processor")
aadl2_Device = Class(name="aadl2::Device", is_abstract=True)
Memory = Class(name="Memory")
aadl2_Processor = Class(name="aadl2::Processor", is_abstract=True)
System = Class(name="System")
aadl2_System = Class(name="aadl2::System", is_abstract=True)
SubprogramGroup = Class(name="SubprogramGroup")
aadl2_SubprogramGroup = Class(name="aadl2::SubprogramGroup", is_abstract=True)
Thread = Class(name="Thread")
VirtualBus = Class(name="VirtualBus")
aadl2_VirtualBus = Class(name="aadl2::VirtualBus", is_abstract=True)
VirtualProcessor = Class(name="VirtualProcessor")
aadl2_VirtualProcessor = Class(name="aadl2::VirtualProcessor", is_abstract=True)
aadl2_AbstractPrototype = Class(name="aadl2::AbstractPrototype")
ComponentPrototype = Class(name="ComponentPrototype")
aadl2_BusClassifier = Class(name="aadl2::BusClassifier", is_abstract=True)
aadl2_Thread = Class(name="aadl2::Thread", is_abstract=True)
ThreadGroup = Class(name="ThreadGroup")
aadl2_ThreadGroup = Class(name="aadl2::ThreadGroup", is_abstract=True)
aadl2_BusImplementation = Class(name="aadl2::BusImplementation")
aadl2_BusPrototype = Class(name="aadl2::BusPrototype")
aadl2_DataType = Class(name="aadl2::DataType")
DataClassifier = Class(name="DataClassifier")
aadl2_BusType = Class(name="aadl2::BusType")
BusClassifier = Class(name="BusClassifier")
aadl2_DataPrototype = Class(name="aadl2::DataPrototype")
aadl2_DeviceClassifier = Class(name="aadl2::DeviceClassifier", is_abstract=True)
aadl2_DeviceType = Class(name="aadl2::DeviceType")
DeviceClassifier = Class(name="DeviceClassifier")
aadl2_DataImplementation = Class(name="aadl2::DataImplementation")
aadl2_DeviceImplementation = Class(name="aadl2::DeviceImplementation")
aadl2_DevicePrototype = Class(name="aadl2::DevicePrototype")
aadl2_MemoryClassifier = Class(name="aadl2::MemoryClassifier", is_abstract=True)
aadl2_MemoryType = Class(name="aadl2::MemoryType")
MemoryClassifier = Class(name="MemoryClassifier")
aadl2_MemoryImplementation = Class(name="aadl2::MemoryImplementation")
aadl2_MemoryPrototype = Class(name="aadl2::MemoryPrototype")
aadl2_SubprogramType = Class(name="aadl2::SubprogramType")
SubprogramClassifier = Class(name="SubprogramClassifier")
aadl2_SubprogramImplementation = Class(name="aadl2::SubprogramImplementation")
aadl2_SubprogramPrototype = Class(name="aadl2::SubprogramPrototype")
aadl2_SubprogramGroupClassifier = Class(name="aadl2::SubprogramGroupClassifier", is_abstract=True)
aadl2_SubprogramGroupType = Class(name="aadl2::SubprogramGroupType")
SubprogramGroupClassifier = Class(name="SubprogramGroupClassifier")
aadl2_SubprogramGroupPrototype = Class(name="aadl2::SubprogramGroupPrototype")
aadl2_SystemClassifier = Class(name="aadl2::SystemClassifier", is_abstract=True)
aadl2_SystemType = Class(name="aadl2::SystemType")
SystemClassifier = Class(name="SystemClassifier")
aadl2_SubprogramGroupImplementation = Class(name="aadl2::SubprogramGroupImplementation")
aadl2_SystemImplementation = Class(name="aadl2::SystemImplementation")
aadl2_SystemPrototype = Class(name="aadl2::SystemPrototype")
aadl2_ProcessorClassifier = Class(name="aadl2::ProcessorClassifier", is_abstract=True)
aadl2_ProcessorType = Class(name="aadl2::ProcessorType")
ProcessorClassifier = Class(name="ProcessorClassifier")
aadl2_ProcessorImplementation = Class(name="aadl2::ProcessorImplementation")
aadl2_ProcessorPrototype = Class(name="aadl2::ProcessorPrototype")
aadl2_ProcessImplementation = Class(name="aadl2::ProcessImplementation")
aadl2_ProcessClassifier = Class(name="aadl2::ProcessClassifier", is_abstract=True)
aadl2_ProcessType = Class(name="aadl2::ProcessType")
ProcessClassifier = Class(name="ProcessClassifier")
aadl2_ProcessPrototype = Class(name="aadl2::ProcessPrototype")
aadl2_ThreadClassifier = Class(name="aadl2::ThreadClassifier", is_abstract=True)
aadl2_ThreadType = Class(name="aadl2::ThreadType")
ThreadClassifier = Class(name="ThreadClassifier")
aadl2_ThreadImplementation = Class(name="aadl2::ThreadImplementation")
aadl2_ThreadPrototype = Class(name="aadl2::ThreadPrototype")
aadl2_ThreadGroupClassifier = Class(name="aadl2::ThreadGroupClassifier", is_abstract=True)
aadl2_ThreadGroupType = Class(name="aadl2::ThreadGroupType")
ThreadGroupClassifier = Class(name="ThreadGroupClassifier")
aadl2_ThreadGroupImplementation = Class(name="aadl2::ThreadGroupImplementation")
aadl2_ThreadGroupPrototype = Class(name="aadl2::ThreadGroupPrototype")
VirtualBusClassifier = Class(name="VirtualBusClassifier")
aadl2_VirtualBusClassifier = Class(name="aadl2::VirtualBusClassifier", is_abstract=True)
aadl2_VirtualBusType = Class(name="aadl2::VirtualBusType")
aadl2_VirtualBusPrototype = Class(name="aadl2::VirtualBusPrototype")
aadl2_VirtualProcessorClassifier = Class(name="aadl2::VirtualProcessorClassifier", is_abstract=True)
aadl2_VirtualBusImplementation = Class(name="aadl2::VirtualBusImplementation")
aadl2_VirtualProcessorType = Class(name="aadl2::VirtualProcessorType")
VirtualProcessorClassifier = Class(name="VirtualProcessorClassifier")
aadl2_VirtualProcessorImplementation = Class(name="aadl2::VirtualProcessorImplementation")
aadl2_PropertyConstant = Class(name="aadl2::PropertyConstant")
ArraySizeProperty = Class(name="ArraySizeProperty")
aadl2_VirtualProcessorPrototype = Class(name="aadl2::VirtualProcessorPrototype")
aadl2_BasicPropertyAssociation = Class(name="aadl2::BasicPropertyAssociation")
aadl2_StringLiteral = Class(name="aadl2::StringLiteral")
PropertyValue = Class(name="PropertyValue")
aadl2_PropertyValue = Class(name="aadl2::PropertyValue", is_abstract=True)
PropertyExpression = Class(name="PropertyExpression")
aadl2_NumberValue = Class(name="aadl2::NumberValue", is_abstract=True)
EnumerationLiteral = Class(name="EnumerationLiteral")
aadl2_EnumerationLiteral = Class(name="aadl2::EnumerationLiteral")
aadl2_UnitLiteral = Class(name="aadl2::UnitLiteral")
aadl2_ReferenceValue = Class(name="aadl2::ReferenceValue")
ContainedNamedElement = Class(name="ContainedNamedElement")
aadl2_BooleanLiteral = Class(name="aadl2::BooleanLiteral")
aadl2_RangeValue = Class(name="aadl2::RangeValue")
aadl2_ClassifierValue = Class(name="aadl2::ClassifierValue")
aadl2_IntegerLiteral = Class(name="aadl2::IntegerLiteral")
NumberValue = Class(name="NumberValue")
aadl2_RealLiteral = Class(name="aadl2::RealLiteral")
aadl2_RecordValue = Class(name="aadl2::RecordValue")
aadl2_ComputedValue = Class(name="aadl2::ComputedValue")
aadl2_Operation = Class(name="aadl2::Operation")
aadl2_NamedValue = Class(name="aadl2::NamedValue")
aadl2_PropertySet = Class(name="aadl2::PropertySet")
aadl2_ListValue = Class(name="aadl2::ListValue")
aadl2_GlobalNamespace = Class(name="aadl2::GlobalNamespace")
aadl2_AadlString = Class(name="aadl2::AadlString")
aadl2_AadlInteger = Class(name="aadl2::AadlInteger")
NumberType = Class(name="NumberType")
aadl2_NumberType = Class(name="aadl2::NumberType", is_abstract=True)
aadl2_UnitsType = Class(name="aadl2::UnitsType")
aadl2_NumericRange = Class(name="aadl2::NumericRange")
aadl2_NonListType = Class(name="aadl2::NonListType", is_abstract=True)
PropertyType = Class(name="PropertyType")
aadl2_AadlBoolean = Class(name="aadl2::AadlBoolean")
NonListType = Class(name="NonListType")
aadl2_EnumerationType = Class(name="aadl2::EnumerationType")
EnumerationType = Class(name="EnumerationType")
aadl2_RangeType = Class(name="aadl2::RangeType")
aadl2_AadlReal = Class(name="aadl2::AadlReal")
aadl2_ClassifierType = Class(name="aadl2::ClassifierType")
aadl2_RecordField = Class(name="aadl2::RecordField")
aadl2_ReferenceType = Class(name="aadl2::ReferenceType")
aadl2_ListType = Class(name="aadl2::ListType")
aadl2_RecordType = Class(name="aadl2::RecordType")

# aadl2_Element class attributes and methods
aadl2_Element_m_getOwner: Method = Method(name="getOwner", parameters={}, type=StringType)
aadl2_Element.methods={aadl2_Element_m_getOwner}

# Element class attributes and methods

# aadl2_Type class attributes and methods

# NamedElement class attributes and methods

# aadl2_NamedElement class attributes and methods
aadl2_NamedElement_name: Property = Property(name="name", type=StringType)
aadl2_NamedElement_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
aadl2_NamedElement_m_getNamespace: Method = Method(name="getNamespace", parameters={}, type=StringType)
aadl2_NamedElement_m_qualifiedName: Method = Method(name="qualifiedName", parameters={}, type=StringType)
aadl2_NamedElement_m_getPropertyValues: Method = Method(name="getPropertyValues", parameters={Parameter(name='propertySetName'), Parameter(name='propertyName')}, type=StringType)
aadl2_NamedElement.attributes={aadl2_NamedElement_name, aadl2_NamedElement_qualifiedName}
aadl2_NamedElement.methods={aadl2_NamedElement_m_qualifiedName, aadl2_NamedElement_m_getNamespace, aadl2_NamedElement_m_getPropertyValues}

# aadl2_Comment class attributes and methods
aadl2_Comment_body: Property = Property(name="body", type=StringType)
aadl2_Comment.attributes={aadl2_Comment_body}

# aadl2_PropertyAssociation class attributes and methods
aadl2_PropertyAssociation_append: Property = Property(name="append", type=StringType)
aadl2_PropertyAssociation_constant: Property = Property(name="constant", type=StringType)
aadl2_PropertyAssociation.attributes={aadl2_PropertyAssociation_constant, aadl2_PropertyAssociation_append}

# aadl2_Property class attributes and methods
aadl2_Property_inherit: Property = Property(name="inherit", type=StringType)
aadl2_Property_emptyListDefault: Property = Property(name="emptyListDefault", type=StringType)
aadl2_Property.attributes={aadl2_Property_emptyListDefault, aadl2_Property_inherit}

# aadl2_ContainedNamedElement class attributes and methods

# aadl2_Classifier class attributes and methods
aadl2_Classifier_noPrototypes: Property = Property(name="noPrototypes", type=StringType)
aadl2_Classifier_noAnnexes: Property = Property(name="noAnnexes", type=StringType)
aadl2_Classifier_noProperties: Property = Property(name="noProperties", type=StringType)
aadl2_Classifier.attributes={aadl2_Classifier_noAnnexes, aadl2_Classifier_noPrototypes, aadl2_Classifier_noProperties}

# BasicProperty class attributes and methods

# AbstractNamedValue class attributes and methods

# aadl2_PropertyExpression class attributes and methods

# aadl2_MetaclassReference class attributes and methods
aadl2_MetaclassReference_annexName: Property = Property(name="annexName", type=StringType)
aadl2_MetaclassReference_metaclassName: Property = Property(name="metaclassName", type=StringType)
aadl2_MetaclassReference.attributes={aadl2_MetaclassReference_metaclassName, aadl2_MetaclassReference_annexName}

# aadl2_PropertyOwner class attributes and methods

# aadl2_BasicProperty class attributes and methods

# TypedElement class attributes and methods

# aadl2_PropertyType class attributes and methods

# aadl2_ModalPropertyValue class attributes and methods

# Type class attributes and methods

# aadl2_AbstractNamedValue class attributes and methods

# PropertyOwner class attributes and methods

# Namespace class attributes and methods

# aadl2_ClassifierFeature class attributes and methods

# aadl2_Generalization class attributes and methods

# aadl2_TypedElement class attributes and methods

# aadl2_Namespace class attributes and methods

# aadl2_AnnexSubclause class attributes and methods

# aadl2_Prototype class attributes and methods

# aadl2_PrototypeBinding class attributes and methods

# DirectedRelationship class attributes and methods

# aadl2_DirectedRelationship class attributes and methods

# Relationship class attributes and methods

# aadl2_Relationship class attributes and methods

# ModalElement class attributes and methods

# aadl2_ModalElement class attributes and methods
aadl2_ModalElement_m_getAllInModes: Method = Method(name="getAllInModes", parameters={}, type=StringType)
aadl2_ModalElement.methods={aadl2_ModalElement_m_getAllInModes}

# aadl2_Mode class attributes and methods
aadl2_Mode_initial: Property = Property(name="initial", type=StringType)
aadl2_Mode_derived: Property = Property(name="derived", type=StringType)
aadl2_Mode.attributes={aadl2_Mode_derived, aadl2_Mode_initial}

# aadl2_ModeFeature class attributes and methods

# ClassifierFeature class attributes and methods

# StructuralFeature class attributes and methods

# CalledSubprogram class attributes and methods

# aadl2_StructuralFeature class attributes and methods

# RefinableElement class attributes and methods

# ModeFeature class attributes and methods

# aadl2_CalledSubprogram class attributes and methods

# aadl2_ContainmentPathElement class attributes and methods
aadl2_ContainmentPathElement_annexName: Property = Property(name="annexName", type=StringType)
aadl2_ContainmentPathElement.attributes={aadl2_ContainmentPathElement_annexName}

# aadl2_RefinableElement class attributes and methods

# aadl2_BehavioralFeature class attributes and methods

# aadl2_ArrayDimension class attributes and methods

# aadl2_ArraySize class attributes and methods
aadl2_ArraySize_size: Property = Property(name="size", type=StringType)
aadl2_ArraySize.attributes={aadl2_ArraySize_size}

# aadl2_ArrayRange class attributes and methods
aadl2_ArrayRange_lowerBound: Property = Property(name="lowerBound", type=StringType)
aadl2_ArrayRange_upperBound: Property = Property(name="upperBound", type=StringType)
aadl2_ArrayRange.attributes={aadl2_ArrayRange_upperBound, aadl2_ArrayRange_lowerBound}

# aadl2_ArrayableElement class attributes and methods

# aadl2_ComponentImplementationReference class attributes and methods

# aadl2_ComponentImplementation class attributes and methods
aadl2_ComponentImplementation_noSubcomponents: Property = Property(name="noSubcomponents", type=StringType)
aadl2_ComponentImplementation_noConnections: Property = Property(name="noConnections", type=StringType)
aadl2_ComponentImplementation_noCalls: Property = Property(name="noCalls", type=StringType)
aadl2_ComponentImplementation_m_getAllSubcomponents: Method = Method(name="getAllSubcomponents", parameters={}, type=StringType)
aadl2_ComponentImplementation.attributes={aadl2_ComponentImplementation_noSubcomponents, aadl2_ComponentImplementation_noCalls, aadl2_ComponentImplementation_noConnections}
aadl2_ComponentImplementation.methods={aadl2_ComponentImplementation_m_getAllSubcomponents}

# ComponentClassifier class attributes and methods

# aadl2_ComponentType class attributes and methods
aadl2_ComponentType_noFeatures: Property = Property(name="noFeatures", type=StringType)
aadl2_ComponentType.attributes={aadl2_ComponentType_noFeatures}

# aadl2_Subcomponent class attributes and methods
aadl2_Subcomponent_allModes: Property = Property(name="allModes", type=StringType)
aadl2_Subcomponent.attributes={aadl2_Subcomponent_allModes}

# aadl2_ArraySizeProperty class attributes and methods

# aadl2_Realization class attributes and methods

# aadl2_EndToEndFlow class attributes and methods

# aadl2_AbstractSubcomponent class attributes and methods

# aadl2_AccessConnection class attributes and methods
aadl2_AccessConnection_accessCategory: Property = Property(name="accessCategory", type=StringType)
aadl2_AccessConnection.attributes={aadl2_AccessConnection_accessCategory}

# aadl2_ParameterConnection class attributes and methods

# aadl2_PortConnection class attributes and methods

# aadl2_FeatureConnection class attributes and methods

# aadl2_FeatureGroupConnection class attributes and methods

# aadl2_FlowImplementation class attributes and methods
aadl2_FlowImplementation_kind: Property = Property(name="kind", type=StringType)
aadl2_FlowImplementation.attributes={aadl2_FlowImplementation_kind}

# aadl2_Connection class attributes and methods
aadl2_Connection_bidirectional: Property = Property(name="bidirectional", type=StringType)
aadl2_Connection.attributes={aadl2_Connection_bidirectional}

# aadl2_ImplementationExtension class attributes and methods

# aadl2_ProcessorFeature class attributes and methods

# aadl2_InternalFeature class attributes and methods
aadl2_InternalFeature_direction: Property = Property(name="direction", type=StringType)
aadl2_InternalFeature_in: Property = Property(name="in", type=StringType)
aadl2_InternalFeature_out: Property = Property(name="out", type=StringType)
aadl2_InternalFeature.attributes={aadl2_InternalFeature_direction, aadl2_InternalFeature_in, aadl2_InternalFeature_out}

# aadl2_EventSource class attributes and methods

# aadl2_EventDataSource class attributes and methods

# aadl2_ComponentClassifier class attributes and methods
aadl2_ComponentClassifier_derivedModes: Property = Property(name="derivedModes", type=StringType)
aadl2_ComponentClassifier_noFlows: Property = Property(name="noFlows", type=StringType)
aadl2_ComponentClassifier_noModes: Property = Property(name="noModes", type=StringType)
aadl2_ComponentClassifier.attributes={aadl2_ComponentClassifier_noFlows, aadl2_ComponentClassifier_noModes, aadl2_ComponentClassifier_derivedModes}

# Classifier class attributes and methods

# SubcomponentType class attributes and methods

# FeatureClassifier class attributes and methods

# aadl2_ModeTransition class attributes and methods

# aadl2_SubcomponentType class attributes and methods

# aadl2_FeatureClassifier class attributes and methods

# aadl2_PortProxy class attributes and methods
aadl2_PortProxy_direction: Property = Property(name="direction", type=StringType)
aadl2_PortProxy_in: Property = Property(name="in", type=StringType)
aadl2_PortProxy_out: Property = Property(name="out", type=StringType)
aadl2_PortProxy.attributes={aadl2_PortProxy_direction, aadl2_PortProxy_out, aadl2_PortProxy_in}

# aadl2_SubprogramProxy class attributes and methods

# aadl2_Context class attributes and methods

# aadl2_TriggerPort class attributes and methods

# aadl2_Feature class attributes and methods

# aadl2_FlowSpecification class attributes and methods
aadl2_FlowSpecification_kind: Property = Property(name="kind", type=StringType)
aadl2_FlowSpecification.attributes={aadl2_FlowSpecification_kind}

# aadl2_TypeExtension class attributes and methods

# aadl2_ModeTransitionTrigger class attributes and methods

# FeatureConnectionEnd class attributes and methods

# ArrayableElement class attributes and methods

# aadl2_ComponentPrototype class attributes and methods
aadl2_ComponentPrototype_array: Property = Property(name="array", type=StringType)
aadl2_ComponentPrototype.attributes={aadl2_ComponentPrototype_array}

# aadl2_FeatureConnectionEnd class attributes and methods

# aadl2_FeatureGroup class attributes and methods
aadl2_FeatureGroup_inverse: Property = Property(name="inverse", type=StringType)
aadl2_FeatureGroup.attributes={aadl2_FeatureGroup_inverse}

# aadl2_AbstractFeature class attributes and methods

# FlowFeature class attributes and methods

# ModalPath class attributes and methods

# FlowElement class attributes and methods

# aadl2_FlowEnd class attributes and methods

# aadl2_FlowFeature class attributes and methods

# ConnectionEnd class attributes and methods

# aadl2_ConnectionEnd class attributes and methods

# Prototype class attributes and methods

# aadl2_FlowElement class attributes and methods

# EndToEndFlowElement class attributes and methods

# aadl2_EndToEndFlowElement class attributes and methods

# Flow class attributes and methods

# aadl2_Flow class attributes and methods

# aadl2_ModalPath class attributes and methods
aadl2_ModalPath_m_getInModes: Method = Method(name="getInModes", parameters={}, type=StringType)
aadl2_ModalPath_m_getInModeTransitions: Method = Method(name="getInModeTransitions", parameters={}, type=StringType)
aadl2_ModalPath_m_getAllInModeTransitions: Method = Method(name="getAllInModeTransitions", parameters={}, type=StringType)
aadl2_ModalPath.methods={aadl2_ModalPath_m_getInModes, aadl2_ModalPath_m_getInModeTransitions, aadl2_ModalPath_m_getAllInModeTransitions}

# Generalization class attributes and methods

# DirectedFeature class attributes and methods

# Context class attributes and methods

# FeatureGroupConnectionEnd class attributes and methods

# CallContext class attributes and methods

# aadl2_FeatureType class attributes and methods

# aadl2_FeatureGroupType class attributes and methods

# aadl2_FeatureGroupPrototype class attributes and methods

# aadl2_FeatureGroupConnectionEnd class attributes and methods

# FeatureType class attributes and methods

# aadl2_GroupExtension class attributes and methods

# aadl2_BusAccess class attributes and methods
aadl2_BusAccess_virtual: Property = Property(name="virtual", type=StringType)
aadl2_BusAccess.attributes={aadl2_BusAccess_virtual}

# aadl2_DataAccess class attributes and methods

# aadl2_DataPort class attributes and methods

# aadl2_CallContext class attributes and methods

# aadl2_EventDataPort class attributes and methods

# aadl2_DirectedFeature class attributes and methods
aadl2_DirectedFeature_direction: Property = Property(name="direction", type=StringType)
aadl2_DirectedFeature_in: Property = Property(name="in", type=StringType)
aadl2_DirectedFeature_out: Property = Property(name="out", type=StringType)
aadl2_DirectedFeature.attributes={aadl2_DirectedFeature_in, aadl2_DirectedFeature_out, aadl2_DirectedFeature_direction}

# Feature class attributes and methods

# aadl2_SubprogramAccess class attributes and methods

# aadl2_SubprogramGroupAccess class attributes and methods

# Access class attributes and methods

# aadl2_BusFeatureClassifier class attributes and methods

# aadl2_Access class attributes and methods
aadl2_Access_kind: Property = Property(name="kind", type=StringType)
aadl2_Access_category: Property = Property(name="category", type=StringType)
aadl2_Access.attributes={aadl2_Access_kind, aadl2_Access_category}

# AccessConnectionEnd class attributes and methods

# aadl2_AccessConnectionEnd class attributes and methods

# aadl2_EventPort class attributes and methods

# aadl2_Parameter class attributes and methods

# aadl2_DataSubcomponentType class attributes and methods

# aadl2_ParameterConnectionEnd class attributes and methods

# aadl2_PortConnectionEnd class attributes and methods

# AbstractFeatureClassifier class attributes and methods

# aadl2_AbstractFeatureClassifier class attributes and methods

# Port class attributes and methods

# aadl2_Port class attributes and methods
aadl2_Port_category: Property = Property(name="category", type=StringType)
aadl2_Port.attributes={aadl2_Port_category}

# TriggerPort class attributes and methods

# ParameterConnectionEnd class attributes and methods

# PortConnectionEnd class attributes and methods

# aadl2_SubprogramSubcomponentType class attributes and methods

# aadl2_SubprogramGroupSubcomponentType class attributes and methods

# aadl2_FeaturePrototype class attributes and methods
aadl2_FeaturePrototype_in: Property = Property(name="in", type=StringType)
aadl2_FeaturePrototype_out: Property = Property(name="out", type=StringType)
aadl2_FeaturePrototype_direction: Property = Property(name="direction", type=StringType)
aadl2_FeaturePrototype.attributes={aadl2_FeaturePrototype_in, aadl2_FeaturePrototype_out, aadl2_FeaturePrototype_direction}

# aadl2_ModeBinding class attributes and methods

# aadl2_FlowSegment class attributes and methods

# aadl2_ConnectedElement class attributes and methods

# aadl2_EndToEndFlowSegment class attributes and methods

# Subcomponent class attributes and methods

# Abstract class attributes and methods

# aadl2_AbstractSubcomponentType class attributes and methods

# aadl2_Abstract class attributes and methods

# Connection class attributes and methods

# InternalFeature class attributes and methods

# aadl2_DataClassifier class attributes and methods

# Data class attributes and methods

# DataSubcomponentType class attributes and methods

# aadl2_Data class attributes and methods

# ProcessorFeature class attributes and methods

# Subprogram class attributes and methods

# SubprogramSubcomponentType class attributes and methods

# aadl2_Subprogram class attributes and methods

# aadl2_AnnexLibrary class attributes and methods

# aadl2_DefaultAnnexLibrary class attributes and methods
aadl2_DefaultAnnexLibrary_sourceText: Property = Property(name="sourceText", type=StringType)
aadl2_DefaultAnnexLibrary.attributes={aadl2_DefaultAnnexLibrary_sourceText}

# AnnexLibrary class attributes and methods

# aadl2_DefaultAnnexSubclause class attributes and methods
aadl2_DefaultAnnexSubclause_sourceText: Property = Property(name="sourceText", type=StringType)
aadl2_DefaultAnnexSubclause.attributes={aadl2_DefaultAnnexSubclause_sourceText}

# AnnexSubclause class attributes and methods

# aadl2_SubprogramClassifier class attributes and methods

# aadl2_PackageRename class attributes and methods
aadl2_PackageRename_renameAll: Property = Property(name="renameAll", type=StringType)
aadl2_PackageRename.attributes={aadl2_PackageRename_renameAll}

# aadl2_ComponentTypeRename class attributes and methods
aadl2_ComponentTypeRename_category: Property = Property(name="category", type=StringType)
aadl2_ComponentTypeRename.attributes={aadl2_ComponentTypeRename_category}

# aadl2_FeatureGroupTypeRename class attributes and methods

# aadl2_ModelUnit class attributes and methods

# aadl2_PublicPackageSection class attributes and methods

# PackageSection class attributes and methods

# aadl2_PrivatePackageSection class attributes and methods

# aadl2_PackageSection class attributes and methods
aadl2_PackageSection_noAnnexes: Property = Property(name="noAnnexes", type=StringType)
aadl2_PackageSection_noProperties: Property = Property(name="noProperties", type=StringType)
aadl2_PackageSection.attributes={aadl2_PackageSection_noProperties, aadl2_PackageSection_noAnnexes}

# aadl2_AadlPackage class attributes and methods

# ModelUnit class attributes and methods

# aadl2_FeatureGroupPrototypeBinding class attributes and methods

# aadl2_FeatureGroupPrototypeActual class attributes and methods

# FeaturePrototypeActual class attributes and methods

# aadl2_ComponentPrototypeBinding class attributes and methods

# PrototypeBinding class attributes and methods

# aadl2_ComponentPrototypeActual class attributes and methods
aadl2_ComponentPrototypeActual_category: Property = Property(name="category", type=StringType)
aadl2_ComponentPrototypeActual.attributes={aadl2_ComponentPrototypeActual_category}

# aadl2_AccessSpecification class attributes and methods
aadl2_AccessSpecification_kind: Property = Property(name="kind", type=StringType)
aadl2_AccessSpecification_category: Property = Property(name="category", type=StringType)
aadl2_AccessSpecification.attributes={aadl2_AccessSpecification_kind, aadl2_AccessSpecification_category}

# aadl2_PortSpecification class attributes and methods
aadl2_PortSpecification_direction: Property = Property(name="direction", type=StringType)
aadl2_PortSpecification_category: Property = Property(name="category", type=StringType)
aadl2_PortSpecification_in: Property = Property(name="in", type=StringType)
aadl2_PortSpecification_out: Property = Property(name="out", type=StringType)
aadl2_PortSpecification.attributes={aadl2_PortSpecification_out, aadl2_PortSpecification_direction, aadl2_PortSpecification_in, aadl2_PortSpecification_category}

# aadl2_FeaturePrototypeActual class attributes and methods

# aadl2_FeaturePrototypeBinding class attributes and methods

# aadl2_SubprogramCallSequence class attributes and methods

# BehavioralFeature class attributes and methods

# aadl2_SubprogramCall class attributes and methods

# aadl2_BehavioredImplementation class attributes and methods
aadl2_BehavioredImplementation_m_subprogramCalls: Method = Method(name="subprogramCalls", parameters={}, type=StringType)
aadl2_BehavioredImplementation.methods={aadl2_BehavioredImplementation_m_subprogramCalls}

# ComponentImplementation class attributes and methods

# aadl2_AbstractType class attributes and methods

# ComponentType class attributes and methods

# AbstractClassifier class attributes and methods

# aadl2_FeaturePrototypeReference class attributes and methods
aadl2_FeaturePrototypeReference_out: Property = Property(name="out", type=StringType)
aadl2_FeaturePrototypeReference_direction: Property = Property(name="direction", type=StringType)
aadl2_FeaturePrototypeReference_in: Property = Property(name="in", type=StringType)
aadl2_FeaturePrototypeReference.attributes={aadl2_FeaturePrototypeReference_in, aadl2_FeaturePrototypeReference_out, aadl2_FeaturePrototypeReference_direction}

# aadl2_AbstractClassifier class attributes and methods

# AbstractSubcomponentType class attributes and methods

# BusSubcomponentType class attributes and methods

# DeviceSubcomponentType class attributes and methods

# MemorySubcomponentType class attributes and methods

# ProcessorSubcomponentType class attributes and methods

# ProcessSubcomponentType class attributes and methods

# SubprogramGroupSubcomponentType class attributes and methods

# SystemSubcomponentType class attributes and methods

# aadl2_VirtualBusSubcomponentType class attributes and methods

# BusFeatureClassifier class attributes and methods

# aadl2_ThreadGroupSubcomponentType class attributes and methods

# aadl2_ThreadSubcomponentType class attributes and methods

# aadl2_SystemSubcomponentType class attributes and methods

# aadl2_ProcessSubcomponentType class attributes and methods

# aadl2_MemorySubcomponentType class attributes and methods

# aadl2_DeviceSubcomponentType class attributes and methods

# aadl2_BusSubcomponentType class attributes and methods

# aadl2_ProcessorSubcomponentType class attributes and methods

# ThreadGroupSubcomponentType class attributes and methods

# aadl2_AbstractImplementation class attributes and methods

# BehavioredImplementation class attributes and methods

# ThreadSubcomponentType class attributes and methods

# VirtualBusSubcomponentType class attributes and methods

# VirtualProcessorSubcomponentType class attributes and methods

# aadl2_VirtualProcessorSubcomponentType class attributes and methods

# aadl2_DataSubcomponent class attributes and methods

# aadl2_DeviceSubcomponent class attributes and methods

# aadl2_MemorySubcomponent class attributes and methods

# aadl2_ProcessSubcomponent class attributes and methods

# aadl2_ProcessorSubcomponent class attributes and methods

# aadl2_SystemSubcomponent class attributes and methods

# aadl2_SubprogramSubcomponent class attributes and methods

# aadl2_SubprogramGroupSubcomponent class attributes and methods

# aadl2_ThreadSubcomponent class attributes and methods

# aadl2_BusSubcomponent class attributes and methods

# aadl2_VirtualBusSubcomponent class attributes and methods

# aadl2_VirtualProcessorSubcomponent class attributes and methods

# Bus class attributes and methods

# aadl2_Bus class attributes and methods

# aadl2_ThreadGroupSubcomponent class attributes and methods

# aadl2_Memory class attributes and methods

# Process class attributes and methods

# aadl2_Process class attributes and methods

# Device class attributes and methods

# Processor class attributes and methods

# aadl2_Device class attributes and methods

# Memory class attributes and methods

# aadl2_Processor class attributes and methods

# System class attributes and methods

# aadl2_System class attributes and methods

# SubprogramGroup class attributes and methods

# aadl2_SubprogramGroup class attributes and methods

# Thread class attributes and methods

# VirtualBus class attributes and methods

# aadl2_VirtualBus class attributes and methods

# VirtualProcessor class attributes and methods

# aadl2_VirtualProcessor class attributes and methods

# aadl2_AbstractPrototype class attributes and methods

# ComponentPrototype class attributes and methods

# aadl2_BusClassifier class attributes and methods

# aadl2_Thread class attributes and methods

# ThreadGroup class attributes and methods

# aadl2_ThreadGroup class attributes and methods

# aadl2_BusImplementation class attributes and methods

# aadl2_BusPrototype class attributes and methods

# aadl2_DataType class attributes and methods

# DataClassifier class attributes and methods

# aadl2_BusType class attributes and methods

# BusClassifier class attributes and methods

# aadl2_DataPrototype class attributes and methods

# aadl2_DeviceClassifier class attributes and methods

# aadl2_DeviceType class attributes and methods

# DeviceClassifier class attributes and methods

# aadl2_DataImplementation class attributes and methods

# aadl2_DeviceImplementation class attributes and methods

# aadl2_DevicePrototype class attributes and methods

# aadl2_MemoryClassifier class attributes and methods

# aadl2_MemoryType class attributes and methods

# MemoryClassifier class attributes and methods

# aadl2_MemoryImplementation class attributes and methods

# aadl2_MemoryPrototype class attributes and methods

# aadl2_SubprogramType class attributes and methods

# SubprogramClassifier class attributes and methods

# aadl2_SubprogramImplementation class attributes and methods

# aadl2_SubprogramPrototype class attributes and methods

# aadl2_SubprogramGroupClassifier class attributes and methods

# aadl2_SubprogramGroupType class attributes and methods

# SubprogramGroupClassifier class attributes and methods

# aadl2_SubprogramGroupPrototype class attributes and methods

# aadl2_SystemClassifier class attributes and methods

# aadl2_SystemType class attributes and methods

# SystemClassifier class attributes and methods

# aadl2_SubprogramGroupImplementation class attributes and methods

# aadl2_SystemImplementation class attributes and methods

# aadl2_SystemPrototype class attributes and methods

# aadl2_ProcessorClassifier class attributes and methods

# aadl2_ProcessorType class attributes and methods

# ProcessorClassifier class attributes and methods

# aadl2_ProcessorImplementation class attributes and methods

# aadl2_ProcessorPrototype class attributes and methods

# aadl2_ProcessImplementation class attributes and methods

# aadl2_ProcessClassifier class attributes and methods

# aadl2_ProcessType class attributes and methods

# ProcessClassifier class attributes and methods

# aadl2_ProcessPrototype class attributes and methods

# aadl2_ThreadClassifier class attributes and methods

# aadl2_ThreadType class attributes and methods

# ThreadClassifier class attributes and methods

# aadl2_ThreadImplementation class attributes and methods

# aadl2_ThreadPrototype class attributes and methods

# aadl2_ThreadGroupClassifier class attributes and methods

# aadl2_ThreadGroupType class attributes and methods

# ThreadGroupClassifier class attributes and methods

# aadl2_ThreadGroupImplementation class attributes and methods

# aadl2_ThreadGroupPrototype class attributes and methods

# VirtualBusClassifier class attributes and methods

# aadl2_VirtualBusClassifier class attributes and methods

# aadl2_VirtualBusType class attributes and methods

# aadl2_VirtualBusPrototype class attributes and methods

# aadl2_VirtualProcessorClassifier class attributes and methods

# aadl2_VirtualBusImplementation class attributes and methods

# aadl2_VirtualProcessorType class attributes and methods

# VirtualProcessorClassifier class attributes and methods

# aadl2_VirtualProcessorImplementation class attributes and methods

# aadl2_PropertyConstant class attributes and methods

# ArraySizeProperty class attributes and methods

# aadl2_VirtualProcessorPrototype class attributes and methods

# aadl2_BasicPropertyAssociation class attributes and methods

# aadl2_StringLiteral class attributes and methods
aadl2_StringLiteral_value: Property = Property(name="value", type=StringType)
aadl2_StringLiteral.attributes={aadl2_StringLiteral_value}

# PropertyValue class attributes and methods

# aadl2_PropertyValue class attributes and methods

# PropertyExpression class attributes and methods

# aadl2_NumberValue class attributes and methods
aadl2_NumberValue_m_getScaledValue: Method = Method(name="getScaledValue", parameters={Parameter(name='target')}, type=StringType)
aadl2_NumberValue_m_getScaledValue: Method = Method(name="getScaledValue", parameters={}, type=StringType)
aadl2_NumberValue_m_getScaledValue: Method = Method(name="getScaledValue", parameters={Parameter(name='target')}, type=StringType)
aadl2_NumberValue.methods={aadl2_NumberValue_m_getScaledValue, aadl2_NumberValue_m_getScaledValue, aadl2_NumberValue_m_getScaledValue}

# EnumerationLiteral class attributes and methods

# aadl2_EnumerationLiteral class attributes and methods

# aadl2_UnitLiteral class attributes and methods
aadl2_UnitLiteral_m_getAbsoluteFactor: Method = Method(name="getAbsoluteFactor", parameters={Parameter(name='target')}, type=StringType)
aadl2_UnitLiteral.methods={aadl2_UnitLiteral_m_getAbsoluteFactor}

# aadl2_ReferenceValue class attributes and methods

# ContainedNamedElement class attributes and methods

# aadl2_BooleanLiteral class attributes and methods
aadl2_BooleanLiteral_value: Property = Property(name="value", type=StringType)
aadl2_BooleanLiteral.attributes={aadl2_BooleanLiteral_value}

# aadl2_RangeValue class attributes and methods

# aadl2_ClassifierValue class attributes and methods

# aadl2_IntegerLiteral class attributes and methods
aadl2_IntegerLiteral_base: Property = Property(name="base", type=StringType)
aadl2_IntegerLiteral_value: Property = Property(name="value", type=StringType)
aadl2_IntegerLiteral.attributes={aadl2_IntegerLiteral_value, aadl2_IntegerLiteral_base}

# NumberValue class attributes and methods

# aadl2_RealLiteral class attributes and methods
aadl2_RealLiteral_value: Property = Property(name="value", type=StringType)
aadl2_RealLiteral.attributes={aadl2_RealLiteral_value}

# aadl2_RecordValue class attributes and methods

# aadl2_ComputedValue class attributes and methods
aadl2_ComputedValue_function: Property = Property(name="function", type=StringType)
aadl2_ComputedValue.attributes={aadl2_ComputedValue_function}

# aadl2_Operation class attributes and methods
aadl2_Operation_op: Property = Property(name="op", type=StringType)
aadl2_Operation.attributes={aadl2_Operation_op}

# aadl2_NamedValue class attributes and methods

# aadl2_PropertySet class attributes and methods

# aadl2_ListValue class attributes and methods

# aadl2_GlobalNamespace class attributes and methods

# aadl2_AadlString class attributes and methods

# aadl2_AadlInteger class attributes and methods

# NumberType class attributes and methods

# aadl2_NumberType class attributes and methods

# aadl2_UnitsType class attributes and methods

# aadl2_NumericRange class attributes and methods

# aadl2_NonListType class attributes and methods

# PropertyType class attributes and methods

# aadl2_AadlBoolean class attributes and methods

# NonListType class attributes and methods

# aadl2_EnumerationType class attributes and methods

# EnumerationType class attributes and methods

# aadl2_RangeType class attributes and methods

# aadl2_AadlReal class attributes and methods

# aadl2_ClassifierType class attributes and methods

# aadl2_RecordField class attributes and methods

# aadl2_ReferenceType class attributes and methods

# aadl2_ListType class attributes and methods

# aadl2_RecordType class attributes and methods

# Relationships
ownedElement1: BinaryAssociation = BinaryAssociation(
    name="ownedElement1",
    ends={
        Property(name="aadl2_Element", type=aadl2_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Element0", type=aadl2_Element, multiplicity=Multiplicity(0, 9999))
    }
)
ownedComment2: BinaryAssociation = BinaryAssociation(
    name="ownedComment2",
    ends={
        Property(name="aadl2_Comment", type=aadl2_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Element3", type=aadl2_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPropertyAssociation4: BinaryAssociation = BinaryAssociation(
    name="ownedPropertyAssociation4",
    ends={
        Property(name="aadl2_PropertyAssociation", type=aadl2_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_NamedElement", type=aadl2_PropertyAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property5: BinaryAssociation = BinaryAssociation(
    name="property5",
    ends={
        Property(name="aadl2_Property", type=aadl2_PropertyAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertyAssociation6", type=aadl2_Property, multiplicity=Multiplicity(1, 1))
    }
)
appliesTo7: BinaryAssociation = BinaryAssociation(
    name="appliesTo7",
    ends={
        Property(name="aadl2_ContainedNamedElement", type=aadl2_PropertyAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertyAssociation8", type=aadl2_ContainedNamedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inBinding9: BinaryAssociation = BinaryAssociation(
    name="inBinding9",
    ends={
        Property(name="aadl2_Classifier", type=aadl2_PropertyAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertyAssociation10", type=aadl2_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
defaultValue13: BinaryAssociation = BinaryAssociation(
    name="defaultValue13",
    ends={
        Property(name="aadl2_PropertyExpression", type=aadl2_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Property14", type=aadl2_PropertyExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
appliesToMetaclass15: BinaryAssociation = BinaryAssociation(
    name="appliesToMetaclass15",
    ends={
        Property(name="aadl2_MetaclassReference", type=aadl2_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Property16", type=aadl2_MetaclassReference, multiplicity=Multiplicity(0, 9999))
    }
)
appliesToClassifier17: BinaryAssociation = BinaryAssociation(
    name="appliesToClassifier17",
    ends={
        Property(name="aadl2_Classifier19", type=aadl2_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Property18", type=aadl2_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
appliesTo20: BinaryAssociation = BinaryAssociation(
    name="appliesTo20",
    ends={
        Property(name="aadl2_PropertyOwner", type=aadl2_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Property21", type=aadl2_PropertyOwner, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedPropertyType22: BinaryAssociation = BinaryAssociation(
    name="referencedPropertyType22",
    ends={
        Property(name="aadl2_PropertyType", type=aadl2_BasicProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BasicProperty", type=aadl2_PropertyType, multiplicity=Multiplicity(0, 1))
    }
)
ownedValue11: BinaryAssociation = BinaryAssociation(
    name="ownedValue11",
    ends={
        Property(name="aadl2_ModalPropertyValue", type=aadl2_PropertyAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertyAssociation12", type=aadl2_ModalPropertyValue, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
classifierFeature30: BinaryAssociation = BinaryAssociation(
    name="classifierFeature30",
    ends={
        Property(name="ClassifierFeature", type=aadl2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="featuringClassifier", type=aadl2_ClassifierFeature, multiplicity=Multiplicity(0, 9999))
    }
)
inheritedMember31: BinaryAssociation = BinaryAssociation(
    name="inheritedMember31",
    ends={
        Property(name="aadl2_NamedElement33", type=aadl2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Classifier32", type=aadl2_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
generalization34: BinaryAssociation = BinaryAssociation(
    name="generalization34",
    ends={
        Property(name="Generalization", type=aadl2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="specific", type=aadl2_Generalization, multiplicity=Multiplicity(0, 9999))
    }
)
general36: BinaryAssociation = BinaryAssociation(
    name="general36",
    ends={
        Property(name="aadl2_Classifier37", type=aadl2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Classifier35", type=aadl2_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
ownedPropertyType23: BinaryAssociation = BinaryAssociation(
    name="ownedPropertyType23",
    ends={
        Property(name="aadl2_PropertyType25", type=aadl2_BasicProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BasicProperty24", type=aadl2_PropertyType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyType26: BinaryAssociation = BinaryAssociation(
    name="propertyType26",
    ends={
        Property(name="aadl2_PropertyType28", type=aadl2_BasicProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BasicProperty27", type=aadl2_PropertyType, multiplicity=Multiplicity(1, 1))
    }
)
type29: BinaryAssociation = BinaryAssociation(
    name="type29",
    ends={
        Property(name="aadl2_Type", type=aadl2_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_TypedElement", type=aadl2_Type, multiplicity=Multiplicity(0, 1))
    }
)
ownedMember44: BinaryAssociation = BinaryAssociation(
    name="ownedMember44",
    ends={
        Property(name="aadl2_NamedElement45", type=aadl2_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Namespace", type=aadl2_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
member46: BinaryAssociation = BinaryAssociation(
    name="member46",
    ends={
        Property(name="aadl2_NamedElement48", type=aadl2_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Namespace47", type=aadl2_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAnnexSubclause38: BinaryAssociation = BinaryAssociation(
    name="ownedAnnexSubclause38",
    ends={
        Property(name="aadl2_AnnexSubclause", type=aadl2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Classifier39", type=aadl2_AnnexSubclause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPrototype40: BinaryAssociation = BinaryAssociation(
    name="ownedPrototype40",
    ends={
        Property(name="aadl2_Prototype", type=aadl2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Classifier41", type=aadl2_Prototype, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPrototypeBinding42: BinaryAssociation = BinaryAssociation(
    name="ownedPrototypeBinding42",
    ends={
        Property(name="aadl2_PrototypeBinding", type=aadl2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Classifier43", type=aadl2_PrototypeBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
general50: BinaryAssociation = BinaryAssociation(
    name="general50",
    ends={
        Property(name="aadl2_Classifier51", type=aadl2_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Generalization", type=aadl2_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
specific52: BinaryAssociation = BinaryAssociation(
    name="specific52",
    ends={
        Property(name="Classifier53", type=aadl2_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization", type=aadl2_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
featuringClassifier49: BinaryAssociation = BinaryAssociation(
    name="featuringClassifier49",
    ends={
        Property(name="Classifier", type=aadl2_ClassifierFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="classifierFeature", type=aadl2_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
relatedElement59: BinaryAssociation = BinaryAssociation(
    name="relatedElement59",
    ends={
        Property(name="aadl2_Element60", type=aadl2_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Relationship", type=aadl2_Element, multiplicity=Multiplicity(1, 9999))
    }
)
inMode61: BinaryAssociation = BinaryAssociation(
    name="inMode61",
    ends={
        Property(name="aadl2_Mode", type=aadl2_ModalElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ModalElement", type=aadl2_Mode, multiplicity=Multiplicity(0, 9999))
    }
)
source54: BinaryAssociation = BinaryAssociation(
    name="source54",
    ends={
        Property(name="aadl2_Element55", type=aadl2_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DirectedRelationship", type=aadl2_Element, multiplicity=Multiplicity(1, 9999))
    }
)
target56: BinaryAssociation = BinaryAssociation(
    name="target56",
    ends={
        Property(name="aadl2_Element58", type=aadl2_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DirectedRelationship57", type=aadl2_Element, multiplicity=Multiplicity(1, 9999))
    }
)
refined63: BinaryAssociation = BinaryAssociation(
    name="refined63",
    ends={
        Property(name="aadl2_Prototype64", type=aadl2_Prototype, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Prototype62", type=aadl2_Prototype, multiplicity=Multiplicity(0, 1))
    }
)
refinedElement68: BinaryAssociation = BinaryAssociation(
    name="refinedElement68",
    ends={
        Property(name="aadl2_RefinableElement69", type=aadl2_RefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_RefinableElement67", type=aadl2_RefinableElement, multiplicity=Multiplicity(0, 1))
    }
)
formal70: BinaryAssociation = BinaryAssociation(
    name="formal70",
    ends={
        Property(name="aadl2_Prototype72", type=aadl2_PrototypeBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PrototypeBinding71", type=aadl2_Prototype, multiplicity=Multiplicity(1, 1))
    }
)
path73: BinaryAssociation = BinaryAssociation(
    name="path73",
    ends={
        Property(name="aadl2_ContainmentPathElement", type=aadl2_ContainedNamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ContainedNamedElement74", type=aadl2_ContainmentPathElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
containmentPathElement75: BinaryAssociation = BinaryAssociation(
    name="containmentPathElement75",
    ends={
        Property(name="aadl2_ContainmentPathElement77", type=aadl2_ContainedNamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ContainedNamedElement76", type=aadl2_ContainmentPathElement, multiplicity=Multiplicity(0, 9999))
    }
)
refinementContext65: BinaryAssociation = BinaryAssociation(
    name="refinementContext65",
    ends={
        Property(name="aadl2_Classifier66", type=aadl2_RefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_RefinableElement", type=aadl2_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
path84: BinaryAssociation = BinaryAssociation(
    name="path84",
    ends={
        Property(name="aadl2_ContainmentPathElement85", type=aadl2_ContainmentPathElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ContainmentPathElement83", type=aadl2_ContainmentPathElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedValue86: BinaryAssociation = BinaryAssociation(
    name="ownedValue86",
    ends={
        Property(name="aadl2_PropertyExpression88", type=aadl2_ModalPropertyValue, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ModalPropertyValue87", type=aadl2_PropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
size89: BinaryAssociation = BinaryAssociation(
    name="size89",
    ends={
        Property(name="aadl2_ArraySize", type=aadl2_ArrayDimension, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ArrayDimension", type=aadl2_ArraySize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayRange78: BinaryAssociation = BinaryAssociation(
    name="arrayRange78",
    ends={
        Property(name="aadl2_ArrayRange", type=aadl2_ContainmentPathElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ContainmentPathElement79", type=aadl2_ArrayRange, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
namedElement80: BinaryAssociation = BinaryAssociation(
    name="namedElement80",
    ends={
        Property(name="aadl2_NamedElement82", type=aadl2_ContainmentPathElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ContainmentPathElement81", type=aadl2_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
arrayDimension92: BinaryAssociation = BinaryAssociation(
    name="arrayDimension92",
    ends={
        Property(name="aadl2_ArrayDimension93", type=aadl2_ArrayableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ArrayableElement", type=aadl2_ArrayDimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implementation94: BinaryAssociation = BinaryAssociation(
    name="implementation94",
    ends={
        Property(name="aadl2_ComponentImplementation", type=aadl2_ComponentImplementationReference, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementationReference", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1))
    }
)
ownedPrototypeBinding95: BinaryAssociation = BinaryAssociation(
    name="ownedPrototypeBinding95",
    ends={
        Property(name="aadl2_PrototypeBinding97", type=aadl2_ComponentImplementationReference, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementationReference96", type=aadl2_PrototypeBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type98: BinaryAssociation = BinaryAssociation(
    name="type98",
    ends={
        Property(name="aadl2_ComponentType", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation99", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1))
    }
)
ownedSubcomponent100: BinaryAssociation = BinaryAssociation(
    name="ownedSubcomponent100",
    ends={
        Property(name="aadl2_Subcomponent", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation101", type=aadl2_Subcomponent, multiplicity=Multiplicity(0, 9999))
    }
)
extended103: BinaryAssociation = BinaryAssociation(
    name="extended103",
    ends={
        Property(name="aadl2_ComponentImplementation104", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation102", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(0, 1))
    }
)
sizeProperty90: BinaryAssociation = BinaryAssociation(
    name="sizeProperty90",
    ends={
        Property(name="aadl2_ArraySizeProperty", type=aadl2_ArraySize, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ArraySize91", type=aadl2_ArraySizeProperty, multiplicity=Multiplicity(0, 1))
    }
)
ownedRealization111: BinaryAssociation = BinaryAssociation(
    name="ownedRealization111",
    ends={
        Property(name="aadl2_Realization", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation112", type=aadl2_Realization, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedEndToEndFlow113: BinaryAssociation = BinaryAssociation(
    name="ownedEndToEndFlow113",
    ends={
        Property(name="aadl2_EndToEndFlow", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation114", type=aadl2_EndToEndFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAbstractSubcomponent115: BinaryAssociation = BinaryAssociation(
    name="ownedAbstractSubcomponent115",
    ends={
        Property(name="aadl2_AbstractSubcomponent", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation116", type=aadl2_AbstractSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAccessConnection117: BinaryAssociation = BinaryAssociation(
    name="ownedAccessConnection117",
    ends={
        Property(name="aadl2_AccessConnection", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation118", type=aadl2_AccessConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedParameterConnection119: BinaryAssociation = BinaryAssociation(
    name="ownedParameterConnection119",
    ends={
        Property(name="aadl2_ParameterConnection", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation120", type=aadl2_ParameterConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPortConnection121: BinaryAssociation = BinaryAssociation(
    name="ownedPortConnection121",
    ends={
        Property(name="aadl2_PortConnection", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation122", type=aadl2_PortConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedFeatureConnection123: BinaryAssociation = BinaryAssociation(
    name="ownedFeatureConnection123",
    ends={
        Property(name="aadl2_FeatureConnection", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation124", type=aadl2_FeatureConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedFeatureGroupConnection125: BinaryAssociation = BinaryAssociation(
    name="ownedFeatureGroupConnection125",
    ends={
        Property(name="aadl2_FeatureGroupConnection", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation126", type=aadl2_FeatureGroupConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedFlowImplementation105: BinaryAssociation = BinaryAssociation(
    name="ownedFlowImplementation105",
    ends={
        Property(name="aadl2_FlowImplementation", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation106", type=aadl2_FlowImplementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedConnection107: BinaryAssociation = BinaryAssociation(
    name="ownedConnection107",
    ends={
        Property(name="aadl2_Connection", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation108", type=aadl2_Connection, multiplicity=Multiplicity(0, 9999))
    }
)
ownedExtension109: BinaryAssociation = BinaryAssociation(
    name="ownedExtension109",
    ends={
        Property(name="aadl2_ImplementationExtension", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation110", type=aadl2_ImplementationExtension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedProcessorFeature127: BinaryAssociation = BinaryAssociation(
    name="ownedProcessorFeature127",
    ends={
        Property(name="aadl2_ProcessorFeature", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation128", type=aadl2_ProcessorFeature, multiplicity=Multiplicity(0, 9999))
    }
)
ownedInternalFeature129: BinaryAssociation = BinaryAssociation(
    name="ownedInternalFeature129",
    ends={
        Property(name="aadl2_InternalFeature", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation130", type=aadl2_InternalFeature, multiplicity=Multiplicity(0, 9999))
    }
)
ownedEventSource131: BinaryAssociation = BinaryAssociation(
    name="ownedEventSource131",
    ends={
        Property(name="aadl2_EventSource", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation132", type=aadl2_EventSource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataSource133: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataSource133",
    ends={
        Property(name="aadl2_EventDataSource", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation134", type=aadl2_EventDataSource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedMode139: BinaryAssociation = BinaryAssociation(
    name="ownedMode139",
    ends={
        Property(name="aadl2_Mode140", type=aadl2_ComponentClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentClassifier", type=aadl2_Mode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedModeTransition141: BinaryAssociation = BinaryAssociation(
    name="ownedModeTransition141",
    ends={
        Property(name="aadl2_ModeTransition", type=aadl2_ComponentClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentClassifier142", type=aadl2_ModeTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source143: BinaryAssociation = BinaryAssociation(
    name="source143",
    ends={
        Property(name="aadl2_Mode145", type=aadl2_ModeTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ModeTransition144", type=aadl2_Mode, multiplicity=Multiplicity(1, 1))
    }
)
ownedPortProxy135: BinaryAssociation = BinaryAssociation(
    name="ownedPortProxy135",
    ends={
        Property(name="aadl2_PortProxy", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation136", type=aadl2_PortProxy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramProxy137: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramProxy137",
    ends={
        Property(name="aadl2_SubprogramProxy", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation138", type=aadl2_SubprogramProxy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context151: BinaryAssociation = BinaryAssociation(
    name="context151",
    ends={
        Property(name="aadl2_Context", type=aadl2_ModeTransitionTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ModeTransitionTrigger152", type=aadl2_Context, multiplicity=Multiplicity(0, 1))
    }
)
triggerPort153: BinaryAssociation = BinaryAssociation(
    name="triggerPort153",
    ends={
        Property(name="aadl2_TriggerPort", type=aadl2_ModeTransitionTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ModeTransitionTrigger154", type=aadl2_TriggerPort, multiplicity=Multiplicity(1, 1))
    }
)
ownedFeature155: BinaryAssociation = BinaryAssociation(
    name="ownedFeature155",
    ends={
        Property(name="aadl2_Feature", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentType156", type=aadl2_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
extended158: BinaryAssociation = BinaryAssociation(
    name="extended158",
    ends={
        Property(name="aadl2_ComponentType159", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentType157", type=aadl2_ComponentType, multiplicity=Multiplicity(0, 1))
    }
)
ownedFlowSpecification160: BinaryAssociation = BinaryAssociation(
    name="ownedFlowSpecification160",
    ends={
        Property(name="aadl2_FlowSpecification", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentType161", type=aadl2_FlowSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
destination146: BinaryAssociation = BinaryAssociation(
    name="destination146",
    ends={
        Property(name="aadl2_Mode148", type=aadl2_ModeTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ModeTransition147", type=aadl2_Mode, multiplicity=Multiplicity(1, 1))
    }
)
ownedTrigger149: BinaryAssociation = BinaryAssociation(
    name="ownedTrigger149",
    ends={
        Property(name="aadl2_ModeTransitionTrigger", type=aadl2_ModeTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ModeTransition150", type=aadl2_ModeTransitionTrigger, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
prototype168: BinaryAssociation = BinaryAssociation(
    name="prototype168",
    ends={
        Property(name="aadl2_ComponentPrototype", type=aadl2_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Feature169", type=aadl2_ComponentPrototype, multiplicity=Multiplicity(0, 1))
    }
)
featureClassifier170: BinaryAssociation = BinaryAssociation(
    name="featureClassifier170",
    ends={
        Property(name="aadl2_FeatureClassifier", type=aadl2_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Feature171", type=aadl2_FeatureClassifier, multiplicity=Multiplicity(0, 1))
    }
)
refined173: BinaryAssociation = BinaryAssociation(
    name="refined173",
    ends={
        Property(name="aadl2_Feature174", type=aadl2_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Feature172", type=aadl2_Feature, multiplicity=Multiplicity(0, 1))
    }
)
classifier175: BinaryAssociation = BinaryAssociation(
    name="classifier175",
    ends={
        Property(name="aadl2_Classifier177", type=aadl2_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Feature176", type=aadl2_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
ownedExtension162: BinaryAssociation = BinaryAssociation(
    name="ownedExtension162",
    ends={
        Property(name="aadl2_TypeExtension", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentType163", type=aadl2_TypeExtension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedFeatureGroup164: BinaryAssociation = BinaryAssociation(
    name="ownedFeatureGroup164",
    ends={
        Property(name="aadl2_FeatureGroup", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentType165", type=aadl2_FeatureGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAbstractFeature166: BinaryAssociation = BinaryAssociation(
    name="ownedAbstractFeature166",
    ends={
        Property(name="aadl2_AbstractFeature", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentType167", type=aadl2_AbstractFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constrainingClassifier178: BinaryAssociation = BinaryAssociation(
    name="constrainingClassifier178",
    ends={
        Property(name="aadl2_ComponentClassifier180", type=aadl2_ComponentPrototype, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentPrototype179", type=aadl2_ComponentClassifier, multiplicity=Multiplicity(0, 1))
    }
)
refined182: BinaryAssociation = BinaryAssociation(
    name="refined182",
    ends={
        Property(name="aadl2_FlowSpecification183", type=aadl2_FlowSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FlowSpecification181", type=aadl2_FlowSpecification, multiplicity=Multiplicity(0, 1))
    }
)
outEnd184: BinaryAssociation = BinaryAssociation(
    name="outEnd184",
    ends={
        Property(name="aadl2_FlowEnd", type=aadl2_FlowSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FlowSpecification185", type=aadl2_FlowEnd, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
InEnd186: BinaryAssociation = BinaryAssociation(
    name="InEnd186",
    ends={
        Property(name="aadl2_FlowEnd188", type=aadl2_FlowSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FlowSpecification187", type=aadl2_FlowEnd, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inModeOrTransition189: BinaryAssociation = BinaryAssociation(
    name="inModeOrTransition189",
    ends={
        Property(name="aadl2_ModeFeature", type=aadl2_ModalPath, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ModalPath", type=aadl2_ModeFeature, multiplicity=Multiplicity(0, 9999))
    }
)
context190: BinaryAssociation = BinaryAssociation(
    name="context190",
    ends={
        Property(name="aadl2_Context192", type=aadl2_FlowEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FlowEnd191", type=aadl2_Context, multiplicity=Multiplicity(0, 1))
    }
)
extended196: BinaryAssociation = BinaryAssociation(
    name="extended196",
    ends={
        Property(name="aadl2_ComponentType198", type=aadl2_TypeExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_TypeExtension197", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1))
    }
)
featureType199: BinaryAssociation = BinaryAssociation(
    name="featureType199",
    ends={
        Property(name="aadl2_FeatureType", type=aadl2_FeatureGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroup200", type=aadl2_FeatureType, multiplicity=Multiplicity(0, 1))
    }
)
featureGroupType201: BinaryAssociation = BinaryAssociation(
    name="featureGroupType201",
    ends={
        Property(name="aadl2_FeatureGroupType", type=aadl2_FeatureGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroup202", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(0, 1))
    }
)
featureGroupPrototype203: BinaryAssociation = BinaryAssociation(
    name="featureGroupPrototype203",
    ends={
        Property(name="aadl2_FeatureGroupPrototype", type=aadl2_FeatureGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroup204", type=aadl2_FeatureGroupPrototype, multiplicity=Multiplicity(0, 1))
    }
)
feature193: BinaryAssociation = BinaryAssociation(
    name="feature193",
    ends={
        Property(name="aadl2_Feature195", type=aadl2_FlowEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FlowEnd194", type=aadl2_Feature, multiplicity=Multiplicity(1, 1))
    }
)
ownedFeature205: BinaryAssociation = BinaryAssociation(
    name="ownedFeature205",
    ends={
        Property(name="aadl2_Feature207", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType206", type=aadl2_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
extended209: BinaryAssociation = BinaryAssociation(
    name="extended209",
    ends={
        Property(name="aadl2_FeatureGroupType210", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType208", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(0, 1))
    }
)
inverse212: BinaryAssociation = BinaryAssociation(
    name="inverse212",
    ends={
        Property(name="aadl2_FeatureGroupType213", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType211", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(0, 1))
    }
)
ownedExtension214: BinaryAssociation = BinaryAssociation(
    name="ownedExtension214",
    ends={
        Property(name="aadl2_GroupExtension", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType215", type=aadl2_GroupExtension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedBusAccess216: BinaryAssociation = BinaryAssociation(
    name="ownedBusAccess216",
    ends={
        Property(name="aadl2_BusAccess", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType217", type=aadl2_BusAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataAccess218: BinaryAssociation = BinaryAssociation(
    name="ownedDataAccess218",
    ends={
        Property(name="aadl2_DataAccess", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType219", type=aadl2_DataAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataPort220: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort220",
    ends={
        Property(name="aadl2_DataPort", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType221", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess231: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess231",
    ends={
        Property(name="aadl2_SubprogramAccess", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType232", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess233: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess233",
    ends={
        Property(name="aadl2_SubprogramGroupAccess", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType234", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAbstractFeature235: BinaryAssociation = BinaryAssociation(
    name="ownedAbstractFeature235",
    ends={
        Property(name="aadl2_AbstractFeature237", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType236", type=aadl2_AbstractFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extended238: BinaryAssociation = BinaryAssociation(
    name="extended238",
    ends={
        Property(name="aadl2_FeatureGroupType240", type=aadl2_GroupExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_GroupExtension239", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1))
    }
)
busFeatureClassifier241: BinaryAssociation = BinaryAssociation(
    name="busFeatureClassifier241",
    ends={
        Property(name="aadl2_BusFeatureClassifier", type=aadl2_BusAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BusAccess242", type=aadl2_BusFeatureClassifier, multiplicity=Multiplicity(0, 1))
    }
)
ownedEventDataPort222: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort222",
    ends={
        Property(name="aadl2_EventDataPort", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType223", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort224: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort224",
    ends={
        Property(name="aadl2_EventPort", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType225", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedFeatureGroup226: BinaryAssociation = BinaryAssociation(
    name="ownedFeatureGroup226",
    ends={
        Property(name="aadl2_FeatureGroup228", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType227", type=aadl2_FeatureGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedParameter229: BinaryAssociation = BinaryAssociation(
    name="ownedParameter229",
    ends={
        Property(name="aadl2_Parameter", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType230", type=aadl2_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataFeatureClassifier243: BinaryAssociation = BinaryAssociation(
    name="dataFeatureClassifier243",
    ends={
        Property(name="aadl2_DataSubcomponentType", type=aadl2_DataAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DataAccess244", type=aadl2_DataSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
dataFeatureClassifier245: BinaryAssociation = BinaryAssociation(
    name="dataFeatureClassifier245",
    ends={
        Property(name="aadl2_DataSubcomponentType247", type=aadl2_DataPort, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DataPort246", type=aadl2_DataSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
dataFeatureClassifier251: BinaryAssociation = BinaryAssociation(
    name="dataFeatureClassifier251",
    ends={
        Property(name="aadl2_DataSubcomponentType253", type=aadl2_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Parameter252", type=aadl2_DataSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
subprogramFeatureClassifier254: BinaryAssociation = BinaryAssociation(
    name="subprogramFeatureClassifier254",
    ends={
        Property(name="aadl2_SubprogramSubcomponentType", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramAccess255", type=aadl2_SubprogramSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
subprogramGroupFeatureClassifier256: BinaryAssociation = BinaryAssociation(
    name="subprogramGroupFeatureClassifier256",
    ends={
        Property(name="aadl2_SubprogramGroupSubcomponentType", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramGroupAccess257", type=aadl2_SubprogramGroupSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
featurePrototype258: BinaryAssociation = BinaryAssociation(
    name="featurePrototype258",
    ends={
        Property(name="aadl2_FeaturePrototype", type=aadl2_AbstractFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractFeature259", type=aadl2_FeaturePrototype, multiplicity=Multiplicity(0, 1))
    }
)
dataFeatureClassifier248: BinaryAssociation = BinaryAssociation(
    name="dataFeatureClassifier248",
    ends={
        Property(name="aadl2_DataSubcomponentType250", type=aadl2_EventDataPort, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_EventDataPort249", type=aadl2_DataSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
constrainingFeatureGroupType265: BinaryAssociation = BinaryAssociation(
    name="constrainingFeatureGroupType265",
    ends={
        Property(name="aadl2_FeatureGroupType267", type=aadl2_FeatureGroupPrototype, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupPrototype266", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(0, 1))
    }
)
subcomponentType268: BinaryAssociation = BinaryAssociation(
    name="subcomponentType268",
    ends={
        Property(name="aadl2_SubcomponentType", type=aadl2_Subcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Subcomponent269", type=aadl2_SubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
ownedPrototypeBinding270: BinaryAssociation = BinaryAssociation(
    name="ownedPrototypeBinding270",
    ends={
        Property(name="aadl2_PrototypeBinding272", type=aadl2_Subcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Subcomponent271", type=aadl2_PrototypeBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
prototype273: BinaryAssociation = BinaryAssociation(
    name="prototype273",
    ends={
        Property(name="aadl2_ComponentPrototype275", type=aadl2_Subcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Subcomponent274", type=aadl2_ComponentPrototype, multiplicity=Multiplicity(0, 1))
    }
)
abstractFeatureClassifier260: BinaryAssociation = BinaryAssociation(
    name="abstractFeatureClassifier260",
    ends={
        Property(name="aadl2_AbstractFeatureClassifier", type=aadl2_AbstractFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractFeature261", type=aadl2_AbstractFeatureClassifier, multiplicity=Multiplicity(0, 1))
    }
)
constrainingClassifier262: BinaryAssociation = BinaryAssociation(
    name="constrainingClassifier262",
    ends={
        Property(name="aadl2_ComponentClassifier264", type=aadl2_FeaturePrototype, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeaturePrototype263", type=aadl2_ComponentClassifier, multiplicity=Multiplicity(0, 1))
    }
)
classifier284: BinaryAssociation = BinaryAssociation(
    name="classifier284",
    ends={
        Property(name="aadl2_ComponentClassifier286", type=aadl2_Subcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Subcomponent285", type=aadl2_ComponentClassifier, multiplicity=Multiplicity(0, 1))
    }
)
parentMode287: BinaryAssociation = BinaryAssociation(
    name="parentMode287",
    ends={
        Property(name="aadl2_Mode289", type=aadl2_ModeBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ModeBinding288", type=aadl2_Mode, multiplicity=Multiplicity(1, 1))
    }
)
derivedMode290: BinaryAssociation = BinaryAssociation(
    name="derivedMode290",
    ends={
        Property(name="aadl2_Mode292", type=aadl2_ModeBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ModeBinding291", type=aadl2_Mode, multiplicity=Multiplicity(0, 1))
    }
)
specification293: BinaryAssociation = BinaryAssociation(
    name="specification293",
    ends={
        Property(name="aadl2_FlowSpecification295", type=aadl2_FlowImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FlowImplementation294", type=aadl2_FlowSpecification, multiplicity=Multiplicity(1, 1))
    }
)
ownedFlowSegment296: BinaryAssociation = BinaryAssociation(
    name="ownedFlowSegment296",
    ends={
        Property(name="aadl2_FlowSegment", type=aadl2_FlowImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FlowImplementation297", type=aadl2_FlowSegment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inEnd298: BinaryAssociation = BinaryAssociation(
    name="inEnd298",
    ends={
        Property(name="aadl2_FlowEnd300", type=aadl2_FlowImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FlowImplementation299", type=aadl2_FlowEnd, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outEnd301: BinaryAssociation = BinaryAssociation(
    name="outEnd301",
    ends={
        Property(name="aadl2_FlowEnd303", type=aadl2_FlowImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FlowImplementation302", type=aadl2_FlowEnd, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedModeBinding276: BinaryAssociation = BinaryAssociation(
    name="ownedModeBinding276",
    ends={
        Property(name="aadl2_ModeBinding", type=aadl2_Subcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Subcomponent277", type=aadl2_ModeBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implementationReference278: BinaryAssociation = BinaryAssociation(
    name="implementationReference278",
    ends={
        Property(name="aadl2_ComponentImplementationReference280", type=aadl2_Subcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Subcomponent279", type=aadl2_ComponentImplementationReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refined282: BinaryAssociation = BinaryAssociation(
    name="refined282",
    ends={
        Property(name="aadl2_Subcomponent283", type=aadl2_Subcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Subcomponent281", type=aadl2_Subcomponent, multiplicity=Multiplicity(0, 1))
    }
)
destination309: BinaryAssociation = BinaryAssociation(
    name="destination309",
    ends={
        Property(name="aadl2_ConnectedElement", type=aadl2_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Connection310", type=aadl2_ConnectedElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source311: BinaryAssociation = BinaryAssociation(
    name="source311",
    ends={
        Property(name="aadl2_ConnectedElement313", type=aadl2_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Connection312", type=aadl2_ConnectedElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refined315: BinaryAssociation = BinaryAssociation(
    name="refined315",
    ends={
        Property(name="aadl2_Connection316", type=aadl2_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Connection314", type=aadl2_Connection, multiplicity=Multiplicity(0, 1))
    }
)
context317: BinaryAssociation = BinaryAssociation(
    name="context317",
    ends={
        Property(name="aadl2_Context319", type=aadl2_ConnectedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ConnectedElement318", type=aadl2_Context, multiplicity=Multiplicity(0, 1))
    }
)
connectionEnd320: BinaryAssociation = BinaryAssociation(
    name="connectionEnd320",
    ends={
        Property(name="aadl2_ConnectionEnd", type=aadl2_ConnectedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ConnectedElement321", type=aadl2_ConnectionEnd, multiplicity=Multiplicity(1, 1))
    }
)
next323: BinaryAssociation = BinaryAssociation(
    name="next323",
    ends={
        Property(name="aadl2_ConnectedElement324", type=aadl2_ConnectedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ConnectedElement322", type=aadl2_ConnectedElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extended325: BinaryAssociation = BinaryAssociation(
    name="extended325",
    ends={
        Property(name="aadl2_ComponentImplementation327", type=aadl2_ImplementationExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ImplementationExtension326", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1))
    }
)
flowElement304: BinaryAssociation = BinaryAssociation(
    name="flowElement304",
    ends={
        Property(name="aadl2_FlowElement", type=aadl2_FlowSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FlowSegment305", type=aadl2_FlowElement, multiplicity=Multiplicity(1, 1))
    }
)
context306: BinaryAssociation = BinaryAssociation(
    name="context306",
    ends={
        Property(name="aadl2_Context308", type=aadl2_FlowSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FlowSegment307", type=aadl2_Context, multiplicity=Multiplicity(0, 1))
    }
)
ownedEndToEndFlowSegment334: BinaryAssociation = BinaryAssociation(
    name="ownedEndToEndFlowSegment334",
    ends={
        Property(name="aadl2_EndToEndFlowSegment", type=aadl2_EndToEndFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_EndToEndFlow335", type=aadl2_EndToEndFlowSegment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flowElement336: BinaryAssociation = BinaryAssociation(
    name="flowElement336",
    ends={
        Property(name="aadl2_EndToEndFlowElement", type=aadl2_EndToEndFlowSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_EndToEndFlowSegment337", type=aadl2_EndToEndFlowElement, multiplicity=Multiplicity(1, 1))
    }
)
context338: BinaryAssociation = BinaryAssociation(
    name="context338",
    ends={
        Property(name="aadl2_Context340", type=aadl2_EndToEndFlowSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_EndToEndFlowSegment339", type=aadl2_Context, multiplicity=Multiplicity(0, 1))
    }
)
abstractSubcomponentType341: BinaryAssociation = BinaryAssociation(
    name="abstractSubcomponentType341",
    ends={
        Property(name="aadl2_AbstractSubcomponentType", type=aadl2_AbstractSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractSubcomponent342", type=aadl2_AbstractSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
implemented328: BinaryAssociation = BinaryAssociation(
    name="implemented328",
    ends={
        Property(name="aadl2_ComponentType330", type=aadl2_Realization, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Realization329", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1))
    }
)
refined332: BinaryAssociation = BinaryAssociation(
    name="refined332",
    ends={
        Property(name="aadl2_EndToEndFlow333", type=aadl2_EndToEndFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_EndToEndFlow331", type=aadl2_EndToEndFlow, multiplicity=Multiplicity(0, 1))
    }
)
dataClassifier343: BinaryAssociation = BinaryAssociation(
    name="dataClassifier343",
    ends={
        Property(name="aadl2_DataClassifier", type=aadl2_EventDataSource, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_EventDataSource344", type=aadl2_DataClassifier, multiplicity=Multiplicity(0, 1))
    }
)
dataClassifier345: BinaryAssociation = BinaryAssociation(
    name="dataClassifier345",
    ends={
        Property(name="aadl2_DataClassifier347", type=aadl2_PortProxy, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PortProxy346", type=aadl2_DataClassifier, multiplicity=Multiplicity(0, 1))
    }
)
parsedAnnexLibrary350: BinaryAssociation = BinaryAssociation(
    name="parsedAnnexLibrary350",
    ends={
        Property(name="aadl2_AnnexLibrary", type=aadl2_DefaultAnnexLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DefaultAnnexLibrary", type=aadl2_AnnexLibrary, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parsedAnnexSubclause351: BinaryAssociation = BinaryAssociation(
    name="parsedAnnexSubclause351",
    ends={
        Property(name="aadl2_AnnexSubclause352", type=aadl2_DefaultAnnexSubclause, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DefaultAnnexSubclause", type=aadl2_AnnexSubclause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subprogramClassifier348: BinaryAssociation = BinaryAssociation(
    name="subprogramClassifier348",
    ends={
        Property(name="aadl2_SubprogramClassifier", type=aadl2_SubprogramProxy, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramProxy349", type=aadl2_SubprogramClassifier, multiplicity=Multiplicity(0, 1))
    }
)
ownedPackageRename354: BinaryAssociation = BinaryAssociation(
    name="ownedPackageRename354",
    ends={
        Property(name="aadl2_PackageRename", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection", type=aadl2_PackageRename, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedComponentTypeRename355: BinaryAssociation = BinaryAssociation(
    name="ownedComponentTypeRename355",
    ends={
        Property(name="aadl2_ComponentTypeRename", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection356", type=aadl2_ComponentTypeRename, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedClassifier357: BinaryAssociation = BinaryAssociation(
    name="ownedClassifier357",
    ends={
        Property(name="aadl2_Classifier359", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection358", type=aadl2_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedFeatureGroupTypeRename360: BinaryAssociation = BinaryAssociation(
    name="ownedFeatureGroupTypeRename360",
    ends={
        Property(name="aadl2_FeatureGroupTypeRename", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection361", type=aadl2_FeatureGroupTypeRename, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAnnexLibrary362: BinaryAssociation = BinaryAssociation(
    name="ownedAnnexLibrary362",
    ends={
        Property(name="aadl2_AnnexLibrary364", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection363", type=aadl2_AnnexLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedUnit365: BinaryAssociation = BinaryAssociation(
    name="importedUnit365",
    ends={
        Property(name="aadl2_ModelUnit", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection366", type=aadl2_ModelUnit, multiplicity=Multiplicity(0, 9999))
    }
)
privateSection353: BinaryAssociation = BinaryAssociation(
    name="privateSection353",
    ends={
        Property(name="PrivatePackageSection", type=aadl2_PublicPackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="publicSection", type=aadl2_PrivatePackageSection, multiplicity=Multiplicity(0, 1))
    }
)
ownedPublicSection369: BinaryAssociation = BinaryAssociation(
    name="ownedPublicSection369",
    ends={
        Property(name="aadl2_PublicPackageSection", type=aadl2_AadlPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AadlPackage370", type=aadl2_PublicPackageSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedPrivateSection371: BinaryAssociation = BinaryAssociation(
    name="ownedPrivateSection371",
    ends={
        Property(name="aadl2_PrivatePackageSection", type=aadl2_AadlPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AadlPackage372", type=aadl2_PrivatePackageSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
publicSection373: BinaryAssociation = BinaryAssociation(
    name="publicSection373",
    ends={
        Property(name="aadl2_PublicPackageSection375", type=aadl2_AadlPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AadlPackage374", type=aadl2_PublicPackageSection, multiplicity=Multiplicity(0, 1))
    }
)
privateSection376: BinaryAssociation = BinaryAssociation(
    name="privateSection376",
    ends={
        Property(name="aadl2_PrivatePackageSection378", type=aadl2_AadlPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AadlPackage377", type=aadl2_PrivatePackageSection, multiplicity=Multiplicity(0, 1))
    }
)
publicSection379: BinaryAssociation = BinaryAssociation(
    name="publicSection379",
    ends={
        Property(name="PublicPackageSection", type=aadl2_PrivatePackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="privateSection", type=aadl2_PublicPackageSection, multiplicity=Multiplicity(0, 1))
    }
)
renamedComponentType380: BinaryAssociation = BinaryAssociation(
    name="renamedComponentType380",
    ends={
        Property(name="aadl2_ComponentType382", type=aadl2_ComponentTypeRename, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentTypeRename381", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1))
    }
)
renamedPackage367: BinaryAssociation = BinaryAssociation(
    name="renamedPackage367",
    ends={
        Property(name="aadl2_AadlPackage", type=aadl2_PackageRename, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageRename368", type=aadl2_AadlPackage, multiplicity=Multiplicity(1, 1))
    }
)
actual386: BinaryAssociation = BinaryAssociation(
    name="actual386",
    ends={
        Property(name="aadl2_ComponentPrototypeActual", type=aadl2_ComponentPrototypeBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentPrototypeBinding", type=aadl2_ComponentPrototypeActual, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
binding387: BinaryAssociation = BinaryAssociation(
    name="binding387",
    ends={
        Property(name="aadl2_PrototypeBinding389", type=aadl2_ComponentPrototypeActual, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentPrototypeActual388", type=aadl2_PrototypeBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subcomponentType390: BinaryAssociation = BinaryAssociation(
    name="subcomponentType390",
    ends={
        Property(name="aadl2_SubcomponentType392", type=aadl2_ComponentPrototypeActual, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentPrototypeActual391", type=aadl2_SubcomponentType, multiplicity=Multiplicity(1, 1))
    }
)
actual393: BinaryAssociation = BinaryAssociation(
    name="actual393",
    ends={
        Property(name="aadl2_FeatureGroupPrototypeActual", type=aadl2_FeatureGroupPrototypeBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupPrototypeBinding", type=aadl2_FeatureGroupPrototypeActual, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
binding394: BinaryAssociation = BinaryAssociation(
    name="binding394",
    ends={
        Property(name="aadl2_PrototypeBinding396", type=aadl2_FeatureGroupPrototypeActual, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupPrototypeActual395", type=aadl2_PrototypeBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureType397: BinaryAssociation = BinaryAssociation(
    name="featureType397",
    ends={
        Property(name="aadl2_FeatureType399", type=aadl2_FeatureGroupPrototypeActual, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupPrototypeActual398", type=aadl2_FeatureType, multiplicity=Multiplicity(1, 1))
    }
)
renamedFeatureGroupType383: BinaryAssociation = BinaryAssociation(
    name="renamedFeatureGroupType383",
    ends={
        Property(name="aadl2_FeatureGroupType385", type=aadl2_FeatureGroupTypeRename, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupTypeRename384", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1))
    }
)
actual400: BinaryAssociation = BinaryAssociation(
    name="actual400",
    ends={
        Property(name="aadl2_FeaturePrototypeActual", type=aadl2_FeaturePrototypeBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeaturePrototypeBinding", type=aadl2_FeaturePrototypeActual, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier401: BinaryAssociation = BinaryAssociation(
    name="classifier401",
    ends={
        Property(name="aadl2_ComponentClassifier402", type=aadl2_AccessSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AccessSpecification", type=aadl2_ComponentClassifier, multiplicity=Multiplicity(0, 1))
    }
)
componentPrototype403: BinaryAssociation = BinaryAssociation(
    name="componentPrototype403",
    ends={
        Property(name="aadl2_ComponentPrototype405", type=aadl2_AccessSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AccessSpecification404", type=aadl2_ComponentPrototype, multiplicity=Multiplicity(0, 1))
    }
)
classifier406: BinaryAssociation = BinaryAssociation(
    name="classifier406",
    ends={
        Property(name="aadl2_ComponentClassifier407", type=aadl2_PortSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PortSpecification", type=aadl2_ComponentClassifier, multiplicity=Multiplicity(0, 1))
    }
)
componentPrototype408: BinaryAssociation = BinaryAssociation(
    name="componentPrototype408",
    ends={
        Property(name="aadl2_ComponentPrototype410", type=aadl2_PortSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PortSpecification409", type=aadl2_ComponentPrototype, multiplicity=Multiplicity(0, 1))
    }
)
ownedSubprogramCall413: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramCall413",
    ends={
        Property(name="aadl2_SubprogramCall", type=aadl2_SubprogramCallSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramCallSequence", type=aadl2_SubprogramCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledSubprogram414: BinaryAssociation = BinaryAssociation(
    name="calledSubprogram414",
    ends={
        Property(name="aadl2_CalledSubprogram", type=aadl2_SubprogramCall, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramCall415", type=aadl2_CalledSubprogram, multiplicity=Multiplicity(0, 1))
    }
)
context416: BinaryAssociation = BinaryAssociation(
    name="context416",
    ends={
        Property(name="aadl2_CallContext", type=aadl2_SubprogramCall, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramCall417", type=aadl2_CallContext, multiplicity=Multiplicity(0, 1))
    }
)
subprogramCall418: BinaryAssociation = BinaryAssociation(
    name="subprogramCall418",
    ends={
        Property(name="aadl2_SubprogramCall419", type=aadl2_BehavioredImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BehavioredImplementation", type=aadl2_SubprogramCall, multiplicity=Multiplicity(0, 9999))
    }
)
ownedSubprogramCallSequence420: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramCallSequence420",
    ends={
        Property(name="aadl2_SubprogramCallSequence422", type=aadl2_BehavioredImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BehavioredImplementation421", type=aadl2_SubprogramCallSequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
prototype411: BinaryAssociation = BinaryAssociation(
    name="prototype411",
    ends={
        Property(name="aadl2_FeaturePrototype412", type=aadl2_FeaturePrototypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeaturePrototypeReference", type=aadl2_FeaturePrototype, multiplicity=Multiplicity(1, 1))
    }
)
ownedSubprogramAccess428: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess428",
    ends={
        Property(name="aadl2_SubprogramAccess430", type=aadl2_AbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractType429", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataPort431: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort431",
    ends={
        Property(name="aadl2_DataPort433", type=aadl2_AbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractType432", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort434: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort434",
    ends={
        Property(name="aadl2_EventPort436", type=aadl2_AbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractType435", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort437: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort437",
    ends={
        Property(name="aadl2_EventDataPort439", type=aadl2_AbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractType438", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess440: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess440",
    ends={
        Property(name="aadl2_SubprogramGroupAccess442", type=aadl2_AbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractType441", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusAccess423: BinaryAssociation = BinaryAssociation(
    name="ownedBusAccess423",
    ends={
        Property(name="aadl2_BusAccess424", type=aadl2_AbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractType", type=aadl2_BusAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataAccess425: BinaryAssociation = BinaryAssociation(
    name="ownedDataAccess425",
    ends={
        Property(name="aadl2_DataAccess427", type=aadl2_AbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractType426", type=aadl2_DataAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataSubcomponent444: BinaryAssociation = BinaryAssociation(
    name="ownedDataSubcomponent444",
    ends={
        Property(name="aadl2_DataSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation445", type=aadl2_DataSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDeviceSubcomponent446: BinaryAssociation = BinaryAssociation(
    name="ownedDeviceSubcomponent446",
    ends={
        Property(name="aadl2_DeviceSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation447", type=aadl2_DeviceSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedMemorySubcomponent448: BinaryAssociation = BinaryAssociation(
    name="ownedMemorySubcomponent448",
    ends={
        Property(name="aadl2_MemorySubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation449", type=aadl2_MemorySubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProcessSubcomponent450: BinaryAssociation = BinaryAssociation(
    name="ownedProcessSubcomponent450",
    ends={
        Property(name="aadl2_ProcessSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation451", type=aadl2_ProcessSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProcessorSubcomponent452: BinaryAssociation = BinaryAssociation(
    name="ownedProcessorSubcomponent452",
    ends={
        Property(name="aadl2_ProcessorSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation453", type=aadl2_ProcessorSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSystemSubcomponent454: BinaryAssociation = BinaryAssociation(
    name="ownedSystemSubcomponent454",
    ends={
        Property(name="aadl2_SystemSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation455", type=aadl2_SystemSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramSubcomponent456: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramSubcomponent456",
    ends={
        Property(name="aadl2_SubprogramSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation457", type=aadl2_SubprogramSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupSubcomponent458: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupSubcomponent458",
    ends={
        Property(name="aadl2_SubprogramGroupSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation459", type=aadl2_SubprogramGroupSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedThreadSubcomponent460: BinaryAssociation = BinaryAssociation(
    name="ownedThreadSubcomponent460",
    ends={
        Property(name="aadl2_ThreadSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation461", type=aadl2_ThreadSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusSubcomponent443: BinaryAssociation = BinaryAssociation(
    name="ownedBusSubcomponent443",
    ends={
        Property(name="aadl2_BusSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation", type=aadl2_BusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedThreadGroupSubcomponent462: BinaryAssociation = BinaryAssociation(
    name="ownedThreadGroupSubcomponent462",
    ends={
        Property(name="aadl2_ThreadGroupSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation463", type=aadl2_ThreadGroupSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualBusSubcomponent464: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualBusSubcomponent464",
    ends={
        Property(name="aadl2_VirtualBusSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation465", type=aadl2_VirtualBusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualProcessorSubcomponent466: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualProcessorSubcomponent466",
    ends={
        Property(name="aadl2_VirtualProcessorSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation467", type=aadl2_VirtualProcessorSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
busSubcomponentType468: BinaryAssociation = BinaryAssociation(
    name="busSubcomponentType468",
    ends={
        Property(name="aadl2_BusSubcomponentType", type=aadl2_BusSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BusSubcomponent469", type=aadl2_BusSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
dataSubcomponentType470: BinaryAssociation = BinaryAssociation(
    name="dataSubcomponentType470",
    ends={
        Property(name="aadl2_DataSubcomponentType472", type=aadl2_DataSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DataSubcomponent471", type=aadl2_DataSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
memorySubcomponentType475: BinaryAssociation = BinaryAssociation(
    name="memorySubcomponentType475",
    ends={
        Property(name="aadl2_MemorySubcomponentType", type=aadl2_MemorySubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_MemorySubcomponent476", type=aadl2_MemorySubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
processSubcomponentType477: BinaryAssociation = BinaryAssociation(
    name="processSubcomponentType477",
    ends={
        Property(name="aadl2_ProcessSubcomponentType", type=aadl2_ProcessSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessSubcomponent478", type=aadl2_ProcessSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
deviceSubcomponentType473: BinaryAssociation = BinaryAssociation(
    name="deviceSubcomponentType473",
    ends={
        Property(name="aadl2_DeviceSubcomponentType", type=aadl2_DeviceSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DeviceSubcomponent474", type=aadl2_DeviceSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
systemSubcomponentType481: BinaryAssociation = BinaryAssociation(
    name="systemSubcomponentType481",
    ends={
        Property(name="aadl2_SystemSubcomponentType", type=aadl2_SystemSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemSubcomponent482", type=aadl2_SystemSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
subprogramSubcomponentType483: BinaryAssociation = BinaryAssociation(
    name="subprogramSubcomponentType483",
    ends={
        Property(name="aadl2_SubprogramSubcomponentType485", type=aadl2_SubprogramSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramSubcomponent484", type=aadl2_SubprogramSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
processorSubcomponentType479: BinaryAssociation = BinaryAssociation(
    name="processorSubcomponentType479",
    ends={
        Property(name="aadl2_ProcessorSubcomponentType", type=aadl2_ProcessorSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorSubcomponent480", type=aadl2_ProcessorSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
subprogramGroupSubcomponentType486: BinaryAssociation = BinaryAssociation(
    name="subprogramGroupSubcomponentType486",
    ends={
        Property(name="aadl2_SubprogramGroupSubcomponentType488", type=aadl2_SubprogramGroupSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramGroupSubcomponent487", type=aadl2_SubprogramGroupSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
threadSubcomponentType489: BinaryAssociation = BinaryAssociation(
    name="threadSubcomponentType489",
    ends={
        Property(name="aadl2_ThreadSubcomponentType", type=aadl2_ThreadSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadSubcomponent490", type=aadl2_ThreadSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
virtualBusSubcomponentType493: BinaryAssociation = BinaryAssociation(
    name="virtualBusSubcomponentType493",
    ends={
        Property(name="aadl2_VirtualBusSubcomponentType", type=aadl2_VirtualBusSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualBusSubcomponent494", type=aadl2_VirtualBusSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
virtualProcessorSubcomponentType495: BinaryAssociation = BinaryAssociation(
    name="virtualProcessorSubcomponentType495",
    ends={
        Property(name="aadl2_VirtualProcessorSubcomponentType", type=aadl2_VirtualProcessorSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualProcessorSubcomponent496", type=aadl2_VirtualProcessorSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
threadGroupSubcomponentType491: BinaryAssociation = BinaryAssociation(
    name="threadGroupSubcomponentType491",
    ends={
        Property(name="aadl2_ThreadGroupSubcomponentType", type=aadl2_ThreadGroupSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupSubcomponent492", type=aadl2_ThreadGroupSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
ownedDataPort499: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort499",
    ends={
        Property(name="aadl2_DataPort501", type=aadl2_BusType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BusType500", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort502: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort502",
    ends={
        Property(name="aadl2_EventDataPort504", type=aadl2_BusType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BusType503", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort505: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort505",
    ends={
        Property(name="aadl2_EventPort507", type=aadl2_BusType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BusType506", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualBusSubcomponent508: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualBusSubcomponent508",
    ends={
        Property(name="aadl2_VirtualBusSubcomponent509", type=aadl2_BusImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BusImplementation", type=aadl2_VirtualBusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess510: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess510",
    ends={
        Property(name="aadl2_SubprogramAccess511", type=aadl2_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DataType", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusAccess497: BinaryAssociation = BinaryAssociation(
    name="ownedBusAccess497",
    ends={
        Property(name="aadl2_BusAccess498", type=aadl2_BusType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BusType", type=aadl2_BusAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataSubcomponent518: BinaryAssociation = BinaryAssociation(
    name="ownedDataSubcomponent518",
    ends={
        Property(name="aadl2_DataSubcomponent519", type=aadl2_DataImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DataImplementation", type=aadl2_DataSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramSubcomponent520: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramSubcomponent520",
    ends={
        Property(name="aadl2_SubprogramSubcomponent522", type=aadl2_DataImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DataImplementation521", type=aadl2_SubprogramSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataPort523: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort523",
    ends={
        Property(name="aadl2_DataPort524", type=aadl2_DeviceType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DeviceType", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort525: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort525",
    ends={
        Property(name="aadl2_EventDataPort527", type=aadl2_DeviceType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DeviceType526", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort528: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort528",
    ends={
        Property(name="aadl2_EventPort530", type=aadl2_DeviceType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DeviceType529", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataAccess512: BinaryAssociation = BinaryAssociation(
    name="ownedDataAccess512",
    ends={
        Property(name="aadl2_DataAccess514", type=aadl2_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DataType513", type=aadl2_DataAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess515: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess515",
    ends={
        Property(name="aadl2_SubprogramGroupAccess517", type=aadl2_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DataType516", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusSubcomponent540: BinaryAssociation = BinaryAssociation(
    name="ownedBusSubcomponent540",
    ends={
        Property(name="aadl2_BusSubcomponent541", type=aadl2_DeviceImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DeviceImplementation", type=aadl2_BusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataSubcomponent542: BinaryAssociation = BinaryAssociation(
    name="ownedDataSubcomponent542",
    ends={
        Property(name="aadl2_DataSubcomponent544", type=aadl2_DeviceImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DeviceImplementation543", type=aadl2_DataSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualBusSubcomponent545: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualBusSubcomponent545",
    ends={
        Property(name="aadl2_VirtualBusSubcomponent547", type=aadl2_DeviceImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DeviceImplementation546", type=aadl2_VirtualBusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusAccess531: BinaryAssociation = BinaryAssociation(
    name="ownedBusAccess531",
    ends={
        Property(name="aadl2_BusAccess533", type=aadl2_DeviceType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DeviceType532", type=aadl2_BusAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess534: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess534",
    ends={
        Property(name="aadl2_SubprogramAccess536", type=aadl2_DeviceType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DeviceType535", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess537: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess537",
    ends={
        Property(name="aadl2_SubprogramGroupAccess539", type=aadl2_DeviceType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DeviceType538", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort556: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort556",
    ends={
        Property(name="aadl2_EventPort558", type=aadl2_MemoryType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_MemoryType557", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusSubcomponent559: BinaryAssociation = BinaryAssociation(
    name="ownedBusSubcomponent559",
    ends={
        Property(name="aadl2_BusSubcomponent560", type=aadl2_MemoryImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_MemoryImplementation", type=aadl2_BusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedMemorySubcomponent561: BinaryAssociation = BinaryAssociation(
    name="ownedMemorySubcomponent561",
    ends={
        Property(name="aadl2_MemorySubcomponent563", type=aadl2_MemoryImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_MemoryImplementation562", type=aadl2_MemorySubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort564: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort564",
    ends={
        Property(name="aadl2_EventDataPort565", type=aadl2_SubprogramType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramType", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort566: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort566",
    ends={
        Property(name="aadl2_EventPort568", type=aadl2_SubprogramType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramType567", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusAccess548: BinaryAssociation = BinaryAssociation(
    name="ownedBusAccess548",
    ends={
        Property(name="aadl2_BusAccess549", type=aadl2_MemoryType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_MemoryType", type=aadl2_BusAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataPort550: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort550",
    ends={
        Property(name="aadl2_DataPort552", type=aadl2_MemoryType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_MemoryType551", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort553: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort553",
    ends={
        Property(name="aadl2_EventDataPort555", type=aadl2_MemoryType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_MemoryType554", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess575: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess575",
    ends={
        Property(name="aadl2_SubprogramType576", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="aadl2_SubprogramAccess577", type=aadl2_SubprogramType, multiplicity=Multiplicity(1, 1))
    }
)
ownedSubprogramGroupAccess578: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess578",
    ends={
        Property(name="aadl2_SubprogramGroupAccess580", type=aadl2_SubprogramType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramType579", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataSubcomponent581: BinaryAssociation = BinaryAssociation(
    name="ownedDataSubcomponent581",
    ends={
        Property(name="aadl2_DataSubcomponent582", type=aadl2_SubprogramImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramImplementation", type=aadl2_DataSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramSubcomponent583: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramSubcomponent583",
    ends={
        Property(name="aadl2_SubprogramSubcomponent585", type=aadl2_SubprogramImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramImplementation584", type=aadl2_SubprogramSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedParameter569: BinaryAssociation = BinaryAssociation(
    name="ownedParameter569",
    ends={
        Property(name="aadl2_Parameter571", type=aadl2_SubprogramType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramType570", type=aadl2_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataAccess572: BinaryAssociation = BinaryAssociation(
    name="ownedDataAccess572",
    ends={
        Property(name="aadl2_DataAccess574", type=aadl2_SubprogramType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramType573", type=aadl2_DataAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramSubcomponent591: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramSubcomponent591",
    ends={
        Property(name="aadl2_SubprogramSubcomponent592", type=aadl2_SubprogramGroupImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramGroupImplementation", type=aadl2_SubprogramSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupSubcomponent593: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupSubcomponent593",
    ends={
        Property(name="aadl2_SubprogramGroupSubcomponent595", type=aadl2_SubprogramGroupImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramGroupImplementation594", type=aadl2_SubprogramGroupSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataSubcomponent596: BinaryAssociation = BinaryAssociation(
    name="ownedDataSubcomponent596",
    ends={
        Property(name="aadl2_DataSubcomponent598", type=aadl2_SubprogramGroupImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramGroupImplementation597", type=aadl2_DataSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusAccess599: BinaryAssociation = BinaryAssociation(
    name="ownedBusAccess599",
    ends={
        Property(name="aadl2_BusAccess600", type=aadl2_SystemType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemType", type=aadl2_BusAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess586: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess586",
    ends={
        Property(name="aadl2_SubprogramAccess587", type=aadl2_SubprogramGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramGroupType", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess588: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess588",
    ends={
        Property(name="aadl2_SubprogramGroupAccess590", type=aadl2_SubprogramGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramGroupType589", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess610: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess610",
    ends={
        Property(name="aadl2_SubprogramAccess612", type=aadl2_SystemType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemType611", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort613: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort613",
    ends={
        Property(name="aadl2_EventPort615", type=aadl2_SystemType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemType614", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort616: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort616",
    ends={
        Property(name="aadl2_EventDataPort618", type=aadl2_SystemType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemType617", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusSubcomponent619: BinaryAssociation = BinaryAssociation(
    name="ownedBusSubcomponent619",
    ends={
        Property(name="aadl2_BusSubcomponent620", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation", type=aadl2_BusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataSubcomponent621: BinaryAssociation = BinaryAssociation(
    name="ownedDataSubcomponent621",
    ends={
        Property(name="aadl2_DataSubcomponent623", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation622", type=aadl2_DataSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDeviceSubcomponent624: BinaryAssociation = BinaryAssociation(
    name="ownedDeviceSubcomponent624",
    ends={
        Property(name="aadl2_DeviceSubcomponent626", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation625", type=aadl2_DeviceSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataAccess601: BinaryAssociation = BinaryAssociation(
    name="ownedDataAccess601",
    ends={
        Property(name="aadl2_DataAccess603", type=aadl2_SystemType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemType602", type=aadl2_DataAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataPort604: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort604",
    ends={
        Property(name="aadl2_DataPort606", type=aadl2_SystemType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemType605", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess607: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess607",
    ends={
        Property(name="aadl2_SubprogramGroupAccess609", type=aadl2_SystemType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemType608", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProcessorSubcomponent633: BinaryAssociation = BinaryAssociation(
    name="ownedProcessorSubcomponent633",
    ends={
        Property(name="aadl2_ProcessorSubcomponent635", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation634", type=aadl2_ProcessorSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramSubcomponent636: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramSubcomponent636",
    ends={
        Property(name="aadl2_SubprogramSubcomponent638", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation637", type=aadl2_SubprogramSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupSubcomponent639: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupSubcomponent639",
    ends={
        Property(name="aadl2_SubprogramGroupSubcomponent641", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation640", type=aadl2_SubprogramGroupSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSystemSubcomponent642: BinaryAssociation = BinaryAssociation(
    name="ownedSystemSubcomponent642",
    ends={
        Property(name="aadl2_SystemSubcomponent644", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation643", type=aadl2_SystemSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualBusSubcomponent645: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualBusSubcomponent645",
    ends={
        Property(name="aadl2_VirtualBusSubcomponent647", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation646", type=aadl2_VirtualBusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualProcessorSubcomponent648: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualProcessorSubcomponent648",
    ends={
        Property(name="aadl2_VirtualProcessorSubcomponent650", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation649", type=aadl2_VirtualProcessorSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedMemorySubcomponent627: BinaryAssociation = BinaryAssociation(
    name="ownedMemorySubcomponent627",
    ends={
        Property(name="aadl2_MemorySubcomponent629", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation628", type=aadl2_MemorySubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProcessSubcomponent630: BinaryAssociation = BinaryAssociation(
    name="ownedProcessSubcomponent630",
    ends={
        Property(name="aadl2_ProcessSubcomponent632", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation631", type=aadl2_ProcessSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataPort651: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort651",
    ends={
        Property(name="aadl2_DataPort652", type=aadl2_ProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorType", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort653: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort653",
    ends={
        Property(name="aadl2_EventDataPort655", type=aadl2_ProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorType654", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort656: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort656",
    ends={
        Property(name="aadl2_EventPort658", type=aadl2_ProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorType657", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess665: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess665",
    ends={
        Property(name="aadl2_SubprogramGroupAccess667", type=aadl2_ProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorType666", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusSubcomponent668: BinaryAssociation = BinaryAssociation(
    name="ownedBusSubcomponent668",
    ends={
        Property(name="aadl2_BusSubcomponent669", type=aadl2_ProcessorImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorImplementation", type=aadl2_BusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedMemorySubcomponent670: BinaryAssociation = BinaryAssociation(
    name="ownedMemorySubcomponent670",
    ends={
        Property(name="aadl2_MemorySubcomponent672", type=aadl2_ProcessorImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorImplementation671", type=aadl2_MemorySubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualBusSubcomponent673: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualBusSubcomponent673",
    ends={
        Property(name="aadl2_VirtualBusSubcomponent675", type=aadl2_ProcessorImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorImplementation674", type=aadl2_VirtualBusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualProcessorSubcomponent676: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualProcessorSubcomponent676",
    ends={
        Property(name="aadl2_VirtualProcessorSubcomponent678", type=aadl2_ProcessorImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorImplementation677", type=aadl2_VirtualProcessorSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusAccess659: BinaryAssociation = BinaryAssociation(
    name="ownedBusAccess659",
    ends={
        Property(name="aadl2_BusAccess661", type=aadl2_ProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorType660", type=aadl2_BusAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess662: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess662",
    ends={
        Property(name="aadl2_SubprogramAccess664", type=aadl2_ProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorType663", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataPort679: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort679",
    ends={
        Property(name="aadl2_DataPort680", type=aadl2_ProcessType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessType", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort681: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort681",
    ends={
        Property(name="aadl2_EventDataPort683", type=aadl2_ProcessType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessType682", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort684: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort684",
    ends={
        Property(name="aadl2_EventPort686", type=aadl2_ProcessType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessType685", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataAccess687: BinaryAssociation = BinaryAssociation(
    name="ownedDataAccess687",
    ends={
        Property(name="aadl2_DataAccess689", type=aadl2_ProcessType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessType688", type=aadl2_DataAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess690: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess690",
    ends={
        Property(name="aadl2_SubprogramAccess692", type=aadl2_ProcessType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessType691", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess693: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess693",
    ends={
        Property(name="aadl2_SubprogramGroupAccess695", type=aadl2_ProcessType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessType694", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataSubcomponent696: BinaryAssociation = BinaryAssociation(
    name="ownedDataSubcomponent696",
    ends={
        Property(name="aadl2_DataSubcomponent697", type=aadl2_ProcessImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessImplementation", type=aadl2_DataSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupSubcomponent701: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupSubcomponent701",
    ends={
        Property(name="aadl2_SubprogramGroupSubcomponent703", type=aadl2_ProcessImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessImplementation702", type=aadl2_SubprogramGroupSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedThreadSubcomponent704: BinaryAssociation = BinaryAssociation(
    name="ownedThreadSubcomponent704",
    ends={
        Property(name="aadl2_ThreadSubcomponent706", type=aadl2_ProcessImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessImplementation705", type=aadl2_ThreadSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramSubcomponent698: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramSubcomponent698",
    ends={
        Property(name="aadl2_SubprogramSubcomponent700", type=aadl2_ProcessImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessImplementation699", type=aadl2_SubprogramSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedThreadGroupSubcomponent707: BinaryAssociation = BinaryAssociation(
    name="ownedThreadGroupSubcomponent707",
    ends={
        Property(name="aadl2_ThreadGroupSubcomponent709", type=aadl2_ProcessImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessImplementation708", type=aadl2_ThreadGroupSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort712: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort712",
    ends={
        Property(name="aadl2_EventDataPort714", type=aadl2_ThreadType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadType713", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort715: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort715",
    ends={
        Property(name="aadl2_EventPort717", type=aadl2_ThreadType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadType716", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataAccess718: BinaryAssociation = BinaryAssociation(
    name="ownedDataAccess718",
    ends={
        Property(name="aadl2_DataAccess720", type=aadl2_ThreadType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadType719", type=aadl2_DataAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataPort710: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort710",
    ends={
        Property(name="aadl2_DataPort711", type=aadl2_ThreadType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadType", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess724: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess724",
    ends={
        Property(name="aadl2_SubprogramGroupAccess726", type=aadl2_ThreadType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadType725", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess721: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess721",
    ends={
        Property(name="aadl2_SubprogramAccess723", type=aadl2_ThreadType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadType722", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupSubcomponent727: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupSubcomponent727",
    ends={
        Property(name="aadl2_SubprogramGroupSubcomponent728", type=aadl2_ThreadImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadImplementation", type=aadl2_SubprogramGroupSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramSubcomponent729: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramSubcomponent729",
    ends={
        Property(name="aadl2_SubprogramSubcomponent731", type=aadl2_ThreadImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadImplementation730", type=aadl2_SubprogramSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataSubcomponent732: BinaryAssociation = BinaryAssociation(
    name="ownedDataSubcomponent732",
    ends={
        Property(name="aadl2_DataSubcomponent734", type=aadl2_ThreadImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadImplementation733", type=aadl2_DataSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort737: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort737",
    ends={
        Property(name="aadl2_EventDataPort739", type=aadl2_ThreadGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupType738", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort740: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort740",
    ends={
        Property(name="aadl2_EventPort742", type=aadl2_ThreadGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupType741", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataPort735: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort735",
    ends={
        Property(name="aadl2_DataPort736", type=aadl2_ThreadGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupType", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess749: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess749",
    ends={
        Property(name="aadl2_SubprogramGroupAccess751", type=aadl2_ThreadGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupType750", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataAccess743: BinaryAssociation = BinaryAssociation(
    name="ownedDataAccess743",
    ends={
        Property(name="aadl2_DataAccess745", type=aadl2_ThreadGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupType744", type=aadl2_DataAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess746: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess746",
    ends={
        Property(name="aadl2_SubprogramAccess748", type=aadl2_ThreadGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupType747", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedThreadGroupSubcomponent757: BinaryAssociation = BinaryAssociation(
    name="ownedThreadGroupSubcomponent757",
    ends={
        Property(name="aadl2_ThreadGroupSubcomponent759", type=aadl2_ThreadGroupImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupImplementation758", type=aadl2_ThreadGroupSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramSubcomponent760: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramSubcomponent760",
    ends={
        Property(name="aadl2_SubprogramSubcomponent762", type=aadl2_ThreadGroupImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupImplementation761", type=aadl2_SubprogramSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupSubcomponent763: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupSubcomponent763",
    ends={
        Property(name="aadl2_SubprogramGroupSubcomponent765", type=aadl2_ThreadGroupImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupImplementation764", type=aadl2_SubprogramGroupSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataSubcomponent752: BinaryAssociation = BinaryAssociation(
    name="ownedDataSubcomponent752",
    ends={
        Property(name="aadl2_DataSubcomponent753", type=aadl2_ThreadGroupImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupImplementation", type=aadl2_DataSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedThreadSubcomponent754: BinaryAssociation = BinaryAssociation(
    name="ownedThreadSubcomponent754",
    ends={
        Property(name="aadl2_ThreadSubcomponent756", type=aadl2_ThreadGroupImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupImplementation755", type=aadl2_ThreadSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataPort766: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort766",
    ends={
        Property(name="aadl2_DataPort767", type=aadl2_VirtualBusType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualBusType", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort768: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort768",
    ends={
        Property(name="aadl2_EventDataPort770", type=aadl2_VirtualBusType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualBusType769", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort771: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort771",
    ends={
        Property(name="aadl2_EventPort773", type=aadl2_VirtualBusType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualBusType772", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualBusSubcomponent777: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualBusSubcomponent777",
    ends={
        Property(name="aadl2_VirtualBusSubcomponent778", type=aadl2_VirtualBusImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualBusImplementation", type=aadl2_VirtualBusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusAccess774: BinaryAssociation = BinaryAssociation(
    name="ownedBusAccess774",
    ends={
        Property(name="aadl2_BusAccess776", type=aadl2_VirtualBusType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualBusType775", type=aadl2_BusAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort781: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort781",
    ends={
        Property(name="aadl2_EventDataPort783", type=aadl2_VirtualProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualProcessorType782", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort784: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort784",
    ends={
        Property(name="aadl2_EventPort786", type=aadl2_VirtualProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualProcessorType785", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess787: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess787",
    ends={
        Property(name="aadl2_SubprogramAccess789", type=aadl2_VirtualProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualProcessorType788", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataPort779: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort779",
    ends={
        Property(name="aadl2_DataPort780", type=aadl2_VirtualProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualProcessorType", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualBusSubcomponent796: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualBusSubcomponent796",
    ends={
        Property(name="aadl2_VirtualBusSubcomponent797", type=aadl2_VirtualProcessorImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualProcessorImplementation", type=aadl2_VirtualBusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualProcessorSubcomponent798: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualProcessorSubcomponent798",
    ends={
        Property(name="aadl2_VirtualProcessorSubcomponent800", type=aadl2_VirtualProcessorImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualProcessorImplementation799", type=aadl2_VirtualProcessorSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess790: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess790",
    ends={
        Property(name="aadl2_SubprogramGroupAccess792", type=aadl2_VirtualProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualProcessorType791", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusAccess793: BinaryAssociation = BinaryAssociation(
    name="ownedBusAccess793",
    ends={
        Property(name="aadl2_BusAccess795", type=aadl2_VirtualProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualProcessorType794", type=aadl2_BusAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property801: BinaryAssociation = BinaryAssociation(
    name="property801",
    ends={
        Property(name="aadl2_BasicProperty802", type=aadl2_BasicPropertyAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BasicPropertyAssociation", type=aadl2_BasicProperty, multiplicity=Multiplicity(1, 1))
    }
)
ownedValue803: BinaryAssociation = BinaryAssociation(
    name="ownedValue803",
    ends={
        Property(name="aadl2_PropertyExpression805", type=aadl2_BasicPropertyAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BasicPropertyAssociation804", type=aadl2_PropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referencedPropertyType806: BinaryAssociation = BinaryAssociation(
    name="referencedPropertyType806",
    ends={
        Property(name="aadl2_PropertyType807", type=aadl2_PropertyConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertyConstant", type=aadl2_PropertyType, multiplicity=Multiplicity(0, 1))
    }
)
ownedPropertyType808: BinaryAssociation = BinaryAssociation(
    name="ownedPropertyType808",
    ends={
        Property(name="aadl2_PropertyType810", type=aadl2_PropertyConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertyConstant809", type=aadl2_PropertyType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constantValue811: BinaryAssociation = BinaryAssociation(
    name="constantValue811",
    ends={
        Property(name="aadl2_PropertyExpression813", type=aadl2_PropertyConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertyConstant812", type=aadl2_PropertyExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertyType814: BinaryAssociation = BinaryAssociation(
    name="propertyType814",
    ends={
        Property(name="aadl2_PropertyType816", type=aadl2_PropertyConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertyConstant815", type=aadl2_PropertyType, multiplicity=Multiplicity(1, 1))
    }
)
baseUnit819: BinaryAssociation = BinaryAssociation(
    name="baseUnit819",
    ends={
        Property(name="aadl2_UnitLiteral820", type=aadl2_UnitLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_UnitLiteral818", type=aadl2_UnitLiteral, multiplicity=Multiplicity(0, 1))
    }
)
factor821: BinaryAssociation = BinaryAssociation(
    name="factor821",
    ends={
        Property(name="aadl2_NumberValue823", type=aadl2_UnitLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_UnitLiteral822", type=aadl2_NumberValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unit817: BinaryAssociation = BinaryAssociation(
    name="unit817",
    ends={
        Property(name="aadl2_UnitLiteral", type=aadl2_NumberValue, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_NumberValue", type=aadl2_UnitLiteral, multiplicity=Multiplicity(0, 1))
    }
)
minimum826: BinaryAssociation = BinaryAssociation(
    name="minimum826",
    ends={
        Property(name="aadl2_PropertyExpression827", type=aadl2_RangeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_RangeValue", type=aadl2_PropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier824: BinaryAssociation = BinaryAssociation(
    name="classifier824",
    ends={
        Property(name="aadl2_Classifier825", type=aadl2_ClassifierValue, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ClassifierValue", type=aadl2_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
maximum828: BinaryAssociation = BinaryAssociation(
    name="maximum828",
    ends={
        Property(name="aadl2_PropertyExpression830", type=aadl2_RangeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_RangeValue829", type=aadl2_PropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
delta831: BinaryAssociation = BinaryAssociation(
    name="delta831",
    ends={
        Property(name="aadl2_PropertyExpression833", type=aadl2_RangeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_RangeValue832", type=aadl2_PropertyExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedFieldValue836: BinaryAssociation = BinaryAssociation(
    name="ownedFieldValue836",
    ends={
        Property(name="aadl2_BasicPropertyAssociation837", type=aadl2_RecordValue, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_RecordValue", type=aadl2_BasicPropertyAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPropertyExpression834: BinaryAssociation = BinaryAssociation(
    name="ownedPropertyExpression834",
    ends={
        Property(name="aadl2_PropertyExpression835", type=aadl2_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Operation", type=aadl2_PropertyExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
namedValue840: BinaryAssociation = BinaryAssociation(
    name="namedValue840",
    ends={
        Property(name="aadl2_AbstractNamedValue", type=aadl2_NamedValue, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_NamedValue", type=aadl2_AbstractNamedValue, multiplicity=Multiplicity(1, 1))
    }
)
ownedPropertyType841: BinaryAssociation = BinaryAssociation(
    name="ownedPropertyType841",
    ends={
        Property(name="aadl2_PropertyType842", type=aadl2_PropertySet, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertySet", type=aadl2_PropertyType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProperty843: BinaryAssociation = BinaryAssociation(
    name="ownedProperty843",
    ends={
        Property(name="aadl2_Property845", type=aadl2_PropertySet, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertySet844", type=aadl2_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedListElement838: BinaryAssociation = BinaryAssociation(
    name="ownedListElement838",
    ends={
        Property(name="aadl2_PropertyExpression839", type=aadl2_ListValue, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ListValue", type=aadl2_PropertyExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedUnit849: BinaryAssociation = BinaryAssociation(
    name="importedUnit849",
    ends={
        Property(name="aadl2_ModelUnit851", type=aadl2_PropertySet, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertySet850", type=aadl2_ModelUnit, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAnnexSubclause852: BinaryAssociation = BinaryAssociation(
    name="ownedAnnexSubclause852",
    ends={
        Property(name="aadl2_AnnexSubclause854", type=aadl2_PropertySet, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertySet853", type=aadl2_AnnexSubclause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package855: BinaryAssociation = BinaryAssociation(
    name="package855",
    ends={
        Property(name="aadl2_PublicPackageSection856", type=aadl2_GlobalNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_GlobalNamespace", type=aadl2_PublicPackageSection, multiplicity=Multiplicity(0, 9999))
    }
)
propertySet857: BinaryAssociation = BinaryAssociation(
    name="propertySet857",
    ends={
        Property(name="aadl2_PropertySet859", type=aadl2_GlobalNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_GlobalNamespace858", type=aadl2_PropertySet, multiplicity=Multiplicity(0, 9999))
    }
)
ownedPropertyConstant846: BinaryAssociation = BinaryAssociation(
    name="ownedPropertyConstant846",
    ends={
        Property(name="aadl2_PropertyConstant848", type=aadl2_PropertySet, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertySet847", type=aadl2_PropertyConstant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedUnitsType860: BinaryAssociation = BinaryAssociation(
    name="ownedUnitsType860",
    ends={
        Property(name="aadl2_UnitsType", type=aadl2_NumberType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_NumberType", type=aadl2_UnitsType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referencedUnitsType861: BinaryAssociation = BinaryAssociation(
    name="referencedUnitsType861",
    ends={
        Property(name="aadl2_UnitsType863", type=aadl2_NumberType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_NumberType862", type=aadl2_UnitsType, multiplicity=Multiplicity(0, 1))
    }
)
range864: BinaryAssociation = BinaryAssociation(
    name="range864",
    ends={
        Property(name="aadl2_NumericRange", type=aadl2_NumberType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_NumberType865", type=aadl2_NumericRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedLiteral869: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral869",
    ends={
        Property(name="aadl2_EnumerationLiteral", type=aadl2_EnumerationType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_EnumerationType", type=aadl2_EnumerationLiteral, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
upperBound870: BinaryAssociation = BinaryAssociation(
    name="upperBound870",
    ends={
        Property(name="aadl2_PropertyExpression872", type=aadl2_NumericRange, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_NumericRange871", type=aadl2_PropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
unitsType866: BinaryAssociation = BinaryAssociation(
    name="unitsType866",
    ends={
        Property(name="aadl2_UnitsType868", type=aadl2_NumberType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_NumberType867", type=aadl2_UnitsType, multiplicity=Multiplicity(0, 1))
    }
)
classifierReference876: BinaryAssociation = BinaryAssociation(
    name="classifierReference876",
    ends={
        Property(name="aadl2_MetaclassReference877", type=aadl2_ClassifierType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ClassifierType", type=aadl2_MetaclassReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedNumberType878: BinaryAssociation = BinaryAssociation(
    name="ownedNumberType878",
    ends={
        Property(name="aadl2_NumberType879", type=aadl2_RangeType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_RangeType", type=aadl2_NumberType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
numberType880: BinaryAssociation = BinaryAssociation(
    name="numberType880",
    ends={
        Property(name="aadl2_NumberType882", type=aadl2_RangeType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_RangeType881", type=aadl2_NumberType, multiplicity=Multiplicity(1, 1))
    }
)
lowerBound873: BinaryAssociation = BinaryAssociation(
    name="lowerBound873",
    ends={
        Property(name="aadl2_PropertyExpression875", type=aadl2_NumericRange, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_NumericRange874", type=aadl2_PropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedField886: BinaryAssociation = BinaryAssociation(
    name="ownedField886",
    ends={
        Property(name="aadl2_BasicProperty887", type=aadl2_RecordType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_RecordType", type=aadl2_BasicProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
namedElementReference888: BinaryAssociation = BinaryAssociation(
    name="namedElementReference888",
    ends={
        Property(name="aadl2_MetaclassReference889", type=aadl2_ReferenceType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ReferenceType", type=aadl2_MetaclassReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedNumberType883: BinaryAssociation = BinaryAssociation(
    name="referencedNumberType883",
    ends={
        Property(name="aadl2_NumberType885", type=aadl2_RangeType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_RangeType884", type=aadl2_NumberType, multiplicity=Multiplicity(0, 1))
    }
)
elementType895: BinaryAssociation = BinaryAssociation(
    name="elementType895",
    ends={
        Property(name="aadl2_PropertyType897", type=aadl2_ListType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ListType896", type=aadl2_PropertyType, multiplicity=Multiplicity(1, 1))
    }
)
ownedElementType890: BinaryAssociation = BinaryAssociation(
    name="ownedElementType890",
    ends={
        Property(name="aadl2_PropertyType891", type=aadl2_ListType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ListType", type=aadl2_PropertyType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referencedElementType892: BinaryAssociation = BinaryAssociation(
    name="referencedElementType892",
    ends={
        Property(name="aadl2_PropertyType894", type=aadl2_ListType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ListType893", type=aadl2_PropertyType, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_aadl2_Comment_Element = Generalization(general=Element, specific=aadl2_Comment)
gen_aadl2_Type_NamedElement = Generalization(general=NamedElement, specific=aadl2_Type)
gen_aadl2_NamedElement_Element = Generalization(general=Element, specific=aadl2_NamedElement)
gen_aadl2_PropertyAssociation_Element = Generalization(general=Element, specific=aadl2_PropertyAssociation)
gen_aadl2_Property_BasicProperty = Generalization(general=BasicProperty, specific=aadl2_Property)
gen_aadl2_Property_AbstractNamedValue = Generalization(general=AbstractNamedValue, specific=aadl2_Property)
gen_aadl2_BasicProperty_TypedElement = Generalization(general=TypedElement, specific=aadl2_BasicProperty)
gen_aadl2_PropertyType_Type = Generalization(general=Type, specific=aadl2_PropertyType)
gen_aadl2_PropertyExpression_Element = Generalization(general=Element, specific=aadl2_PropertyExpression)
gen_aadl2_MetaclassReference_PropertyOwner = Generalization(general=PropertyOwner, specific=aadl2_MetaclassReference)
gen_aadl2_PropertyOwner_Element = Generalization(general=Element, specific=aadl2_PropertyOwner)
gen_aadl2_Classifier_Namespace = Generalization(general=Namespace, specific=aadl2_Classifier)
gen_aadl2_Classifier_Type = Generalization(general=Type, specific=aadl2_Classifier)
gen_aadl2_TypedElement_NamedElement = Generalization(general=NamedElement, specific=aadl2_TypedElement)
gen_aadl2_Namespace_NamedElement = Generalization(general=NamedElement, specific=aadl2_Namespace)
gen_aadl2_Generalization_DirectedRelationship = Generalization(general=DirectedRelationship, specific=aadl2_Generalization)
gen_aadl2_DirectedRelationship_Relationship = Generalization(general=Relationship, specific=aadl2_DirectedRelationship)
gen_aadl2_ClassifierFeature_NamedElement = Generalization(general=NamedElement, specific=aadl2_ClassifierFeature)
gen_aadl2_Relationship_Element = Generalization(general=Element, specific=aadl2_Relationship)
gen_aadl2_AnnexSubclause_ModalElement = Generalization(general=ModalElement, specific=aadl2_AnnexSubclause)
gen_aadl2_ModalElement_NamedElement = Generalization(general=NamedElement, specific=aadl2_ModalElement)
gen_aadl2_ModeFeature_ClassifierFeature = Generalization(general=ClassifierFeature, specific=aadl2_ModeFeature)
gen_aadl2_Prototype_StructuralFeature = Generalization(general=StructuralFeature, specific=aadl2_Prototype)
gen_aadl2_Prototype_CalledSubprogram = Generalization(general=CalledSubprogram, specific=aadl2_Prototype)
gen_aadl2_StructuralFeature_RefinableElement = Generalization(general=RefinableElement, specific=aadl2_StructuralFeature)
gen_aadl2_StructuralFeature_ClassifierFeature = Generalization(general=ClassifierFeature, specific=aadl2_StructuralFeature)
gen_aadl2_Mode_ModeFeature = Generalization(general=ModeFeature, specific=aadl2_Mode)
gen_aadl2_PrototypeBinding_Element = Generalization(general=Element, specific=aadl2_PrototypeBinding)
gen_aadl2_ContainedNamedElement_Element = Generalization(general=Element, specific=aadl2_ContainedNamedElement)
gen_aadl2_RefinableElement_NamedElement = Generalization(general=NamedElement, specific=aadl2_RefinableElement)
gen_aadl2_ArrayRange_Element = Generalization(general=Element, specific=aadl2_ArrayRange)
gen_aadl2_ModalPropertyValue_ModalElement = Generalization(general=ModalElement, specific=aadl2_ModalPropertyValue)
gen_aadl2_BehavioralFeature_ClassifierFeature = Generalization(general=ClassifierFeature, specific=aadl2_BehavioralFeature)
gen_aadl2_ArrayDimension_Element = Generalization(general=Element, specific=aadl2_ArrayDimension)
gen_aadl2_ContainmentPathElement_Element = Generalization(general=Element, specific=aadl2_ContainmentPathElement)
gen_aadl2_ArrayableElement_Element = Generalization(general=Element, specific=aadl2_ArrayableElement)
gen_aadl2_ComponentImplementationReference_Element = Generalization(general=Element, specific=aadl2_ComponentImplementationReference)
gen_aadl2_ComponentImplementation_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_ComponentImplementation)
gen_aadl2_ArraySize_Element = Generalization(general=Element, specific=aadl2_ArraySize)
gen_aadl2_ComponentClassifier_Classifier = Generalization(general=Classifier, specific=aadl2_ComponentClassifier)
gen_aadl2_ComponentClassifier_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_ComponentClassifier)
gen_aadl2_ComponentClassifier_FeatureClassifier = Generalization(general=FeatureClassifier, specific=aadl2_ComponentClassifier)
gen_aadl2_SubcomponentType_Type = Generalization(general=Type, specific=aadl2_SubcomponentType)
gen_aadl2_ModeTransition_ModeFeature = Generalization(general=ModeFeature, specific=aadl2_ModeTransition)
gen_aadl2_Context_NamedElement = Generalization(general=NamedElement, specific=aadl2_Context)
gen_aadl2_TriggerPort_NamedElement = Generalization(general=NamedElement, specific=aadl2_TriggerPort)
gen_aadl2_ComponentType_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_ComponentType)
gen_aadl2_ModeTransitionTrigger_Element = Generalization(general=Element, specific=aadl2_ModeTransitionTrigger)
gen_aadl2_Feature_StructuralFeature = Generalization(general=StructuralFeature, specific=aadl2_Feature)
gen_aadl2_Feature_FeatureConnectionEnd = Generalization(general=FeatureConnectionEnd, specific=aadl2_Feature)
gen_aadl2_Feature_ArrayableElement = Generalization(general=ArrayableElement, specific=aadl2_Feature)
gen_aadl2_FlowSpecification_FlowFeature = Generalization(general=FlowFeature, specific=aadl2_FlowSpecification)
gen_aadl2_FlowSpecification_ModalPath = Generalization(general=ModalPath, specific=aadl2_FlowSpecification)
gen_aadl2_FlowSpecification_FlowElement = Generalization(general=FlowElement, specific=aadl2_FlowSpecification)
gen_aadl2_FeatureConnectionEnd_ConnectionEnd = Generalization(general=ConnectionEnd, specific=aadl2_FeatureConnectionEnd)
gen_aadl2_ConnectionEnd_NamedElement = Generalization(general=NamedElement, specific=aadl2_ConnectionEnd)
gen_aadl2_ComponentPrototype_Prototype = Generalization(general=Prototype, specific=aadl2_ComponentPrototype)
gen_aadl2_ComponentPrototype_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_ComponentPrototype)
gen_aadl2_ComponentPrototype_FeatureClassifier = Generalization(general=FeatureClassifier, specific=aadl2_ComponentPrototype)
gen_aadl2_FlowElement_EndToEndFlowElement = Generalization(general=EndToEndFlowElement, specific=aadl2_FlowElement)
gen_aadl2_EndToEndFlowElement_NamedElement = Generalization(general=NamedElement, specific=aadl2_EndToEndFlowElement)
gen_aadl2_FlowEnd_Element = Generalization(general=Element, specific=aadl2_FlowEnd)
gen_aadl2_FlowFeature_StructuralFeature = Generalization(general=StructuralFeature, specific=aadl2_FlowFeature)
gen_aadl2_FlowFeature_Flow = Generalization(general=Flow, specific=aadl2_FlowFeature)
gen_aadl2_Flow_NamedElement = Generalization(general=NamedElement, specific=aadl2_Flow)
gen_aadl2_ModalPath_ModalElement = Generalization(general=ModalElement, specific=aadl2_ModalPath)
gen_aadl2_TypeExtension_Generalization = Generalization(general=Generalization, specific=aadl2_TypeExtension)
gen_aadl2_FeatureGroup_DirectedFeature = Generalization(general=DirectedFeature, specific=aadl2_FeatureGroup)
gen_aadl2_FeatureGroup_Context = Generalization(general=Context, specific=aadl2_FeatureGroup)
gen_aadl2_FeatureGroup_FeatureGroupConnectionEnd = Generalization(general=FeatureGroupConnectionEnd, specific=aadl2_FeatureGroup)
gen_aadl2_FeatureGroup_CallContext = Generalization(general=CallContext, specific=aadl2_FeatureGroup)
gen_aadl2_FeatureGroupConnectionEnd_ConnectionEnd = Generalization(general=ConnectionEnd, specific=aadl2_FeatureGroupConnectionEnd)
gen_aadl2_FeatureGroupType_Classifier = Generalization(general=Classifier, specific=aadl2_FeatureGroupType)
gen_aadl2_FeatureGroupType_FeatureType = Generalization(general=FeatureType, specific=aadl2_FeatureGroupType)
gen_aadl2_DirectedFeature_Feature = Generalization(general=Feature, specific=aadl2_DirectedFeature)
gen_aadl2_GroupExtension_Generalization = Generalization(general=Generalization, specific=aadl2_GroupExtension)
gen_aadl2_BusAccess_Access = Generalization(general=Access, specific=aadl2_BusAccess)
gen_aadl2_Access_Feature = Generalization(general=Feature, specific=aadl2_Access)
gen_aadl2_Access_AccessConnectionEnd = Generalization(general=AccessConnectionEnd, specific=aadl2_Access)
gen_aadl2_AccessConnectionEnd_ConnectionEnd = Generalization(general=ConnectionEnd, specific=aadl2_AccessConnectionEnd)
gen_aadl2_ParameterConnectionEnd_ConnectionEnd = Generalization(general=ConnectionEnd, specific=aadl2_ParameterConnectionEnd)
gen_aadl2_PortConnectionEnd_ConnectionEnd = Generalization(general=ConnectionEnd, specific=aadl2_PortConnectionEnd)
gen_aadl2_DataSubcomponentType_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_DataSubcomponentType)
gen_aadl2_DataSubcomponentType_AbstractFeatureClassifier = Generalization(general=AbstractFeatureClassifier, specific=aadl2_DataSubcomponentType)
gen_aadl2_AbstractFeatureClassifier_FeatureClassifier = Generalization(general=FeatureClassifier, specific=aadl2_AbstractFeatureClassifier)
gen_aadl2_DataPort_Port = Generalization(general=Port, specific=aadl2_DataPort)
gen_aadl2_DataPort_Context = Generalization(general=Context, specific=aadl2_DataPort)
gen_aadl2_DataPort_ParameterConnectionEnd = Generalization(general=ParameterConnectionEnd, specific=aadl2_DataPort)
gen_aadl2_Port_DirectedFeature = Generalization(general=DirectedFeature, specific=aadl2_Port)
gen_aadl2_Port_PortConnectionEnd = Generalization(general=PortConnectionEnd, specific=aadl2_Port)
gen_aadl2_Port_TriggerPort = Generalization(general=TriggerPort, specific=aadl2_Port)
gen_aadl2_BusFeatureClassifier_FeatureClassifier = Generalization(general=FeatureClassifier, specific=aadl2_BusFeatureClassifier)
gen_aadl2_DataAccess_Access = Generalization(general=Access, specific=aadl2_DataAccess)
gen_aadl2_DataAccess_FlowElement = Generalization(general=FlowElement, specific=aadl2_DataAccess)
gen_aadl2_DataAccess_ParameterConnectionEnd = Generalization(general=ParameterConnectionEnd, specific=aadl2_DataAccess)
gen_aadl2_DataAccess_PortConnectionEnd = Generalization(general=PortConnectionEnd, specific=aadl2_DataAccess)
gen_aadl2_Parameter_DirectedFeature = Generalization(general=DirectedFeature, specific=aadl2_Parameter)
gen_aadl2_Parameter_Context = Generalization(general=Context, specific=aadl2_Parameter)
gen_aadl2_Parameter_ParameterConnectionEnd = Generalization(general=ParameterConnectionEnd, specific=aadl2_Parameter)
gen_aadl2_SubprogramAccess_Access = Generalization(general=Access, specific=aadl2_SubprogramAccess)
gen_aadl2_SubprogramAccess_Context = Generalization(general=Context, specific=aadl2_SubprogramAccess)
gen_aadl2_SubprogramAccess_CalledSubprogram = Generalization(general=CalledSubprogram, specific=aadl2_SubprogramAccess)
gen_aadl2_SubprogramSubcomponentType_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_SubprogramSubcomponentType)
gen_aadl2_SubprogramSubcomponentType_AbstractFeatureClassifier = Generalization(general=AbstractFeatureClassifier, specific=aadl2_SubprogramSubcomponentType)
gen_aadl2_SubprogramGroupAccess_Access = Generalization(general=Access, specific=aadl2_SubprogramGroupAccess)
gen_aadl2_SubprogramGroupAccess_CallContext = Generalization(general=CallContext, specific=aadl2_SubprogramGroupAccess)
gen_aadl2_SubprogramGroupSubcomponentType_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_SubprogramGroupSubcomponentType)
gen_aadl2_SubprogramGroupSubcomponentType_AbstractFeatureClassifier = Generalization(general=AbstractFeatureClassifier, specific=aadl2_SubprogramGroupSubcomponentType)
gen_aadl2_AbstractFeature_DirectedFeature = Generalization(general=DirectedFeature, specific=aadl2_AbstractFeature)
gen_aadl2_AbstractFeature_TriggerPort = Generalization(general=TriggerPort, specific=aadl2_AbstractFeature)
gen_aadl2_EventDataPort_Port = Generalization(general=Port, specific=aadl2_EventDataPort)
gen_aadl2_EventDataPort_Context = Generalization(general=Context, specific=aadl2_EventDataPort)
gen_aadl2_EventDataPort_ParameterConnectionEnd = Generalization(general=ParameterConnectionEnd, specific=aadl2_EventDataPort)
gen_aadl2_EventPort_Port = Generalization(general=Port, specific=aadl2_EventPort)
gen_aadl2_FeatureGroupPrototype_Prototype = Generalization(general=Prototype, specific=aadl2_FeatureGroupPrototype)
gen_aadl2_FeatureGroupPrototype_FeatureType = Generalization(general=FeatureType, specific=aadl2_FeatureGroupPrototype)
gen_aadl2_Subcomponent_StructuralFeature = Generalization(general=StructuralFeature, specific=aadl2_Subcomponent)
gen_aadl2_Subcomponent_ModalElement = Generalization(general=ModalElement, specific=aadl2_Subcomponent)
gen_aadl2_Subcomponent_Context = Generalization(general=Context, specific=aadl2_Subcomponent)
gen_aadl2_Subcomponent_FlowElement = Generalization(general=FlowElement, specific=aadl2_Subcomponent)
gen_aadl2_Subcomponent_ArrayableElement = Generalization(general=ArrayableElement, specific=aadl2_Subcomponent)
gen_aadl2_FeaturePrototype_Prototype = Generalization(general=Prototype, specific=aadl2_FeaturePrototype)
gen_aadl2_ModeBinding_Element = Generalization(general=Element, specific=aadl2_ModeBinding)
gen_aadl2_FlowImplementation_ModalPath = Generalization(general=ModalPath, specific=aadl2_FlowImplementation)
gen_aadl2_FlowImplementation_ClassifierFeature = Generalization(general=ClassifierFeature, specific=aadl2_FlowImplementation)
gen_aadl2_FlowImplementation_Flow = Generalization(general=Flow, specific=aadl2_FlowImplementation)
gen_aadl2_Connection_FlowElement = Generalization(general=FlowElement, specific=aadl2_Connection)
gen_aadl2_ConnectedElement_Element = Generalization(general=Element, specific=aadl2_ConnectedElement)
gen_aadl2_ImplementationExtension_Generalization = Generalization(general=Generalization, specific=aadl2_ImplementationExtension)
gen_aadl2_FlowSegment_Element = Generalization(general=Element, specific=aadl2_FlowSegment)
gen_aadl2_Connection_StructuralFeature = Generalization(general=StructuralFeature, specific=aadl2_Connection)
gen_aadl2_Connection_ModalPath = Generalization(general=ModalPath, specific=aadl2_Connection)
gen_aadl2_EndToEndFlowSegment_Element = Generalization(general=Element, specific=aadl2_EndToEndFlowSegment)
gen_aadl2_AbstractSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_AbstractSubcomponent)
gen_aadl2_AbstractSubcomponent_Abstract = Generalization(general=Abstract, specific=aadl2_AbstractSubcomponent)
gen_aadl2_Abstract_NamedElement = Generalization(general=NamedElement, specific=aadl2_Abstract)
gen_aadl2_AbstractSubcomponentType_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_AbstractSubcomponentType)
gen_aadl2_AbstractSubcomponentType_AbstractFeatureClassifier = Generalization(general=AbstractFeatureClassifier, specific=aadl2_AbstractSubcomponentType)
gen_aadl2_AccessConnection_Connection = Generalization(general=Connection, specific=aadl2_AccessConnection)
gen_aadl2_ParameterConnection_Connection = Generalization(general=Connection, specific=aadl2_ParameterConnection)
gen_aadl2_Realization_Generalization = Generalization(general=Generalization, specific=aadl2_Realization)
gen_aadl2_EndToEndFlow_FlowFeature = Generalization(general=FlowFeature, specific=aadl2_EndToEndFlow)
gen_aadl2_EndToEndFlow_ModalPath = Generalization(general=ModalPath, specific=aadl2_EndToEndFlow)
gen_aadl2_EndToEndFlow_EndToEndFlowElement = Generalization(general=EndToEndFlowElement, specific=aadl2_EndToEndFlow)
gen_aadl2_InternalFeature_TriggerPort = Generalization(general=TriggerPort, specific=aadl2_InternalFeature)
gen_aadl2_EventSource_InternalFeature = Generalization(general=InternalFeature, specific=aadl2_EventSource)
gen_aadl2_EventDataSource_InternalFeature = Generalization(general=InternalFeature, specific=aadl2_EventDataSource)
gen_aadl2_DataClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_DataClassifier)
gen_aadl2_DataClassifier_Data = Generalization(general=Data, specific=aadl2_DataClassifier)
gen_aadl2_DataClassifier_DataSubcomponentType = Generalization(general=DataSubcomponentType, specific=aadl2_DataClassifier)
gen_aadl2_Data_NamedElement = Generalization(general=NamedElement, specific=aadl2_Data)
gen_aadl2_PortProxy_ProcessorFeature = Generalization(general=ProcessorFeature, specific=aadl2_PortProxy)
gen_aadl2_PortProxy_FeatureConnectionEnd = Generalization(general=FeatureConnectionEnd, specific=aadl2_PortProxy)
gen_aadl2_PortProxy_PortConnectionEnd = Generalization(general=PortConnectionEnd, specific=aadl2_PortProxy)
gen_aadl2_PortProxy_TriggerPort = Generalization(general=TriggerPort, specific=aadl2_PortProxy)
gen_aadl2_PortConnection_Connection = Generalization(general=Connection, specific=aadl2_PortConnection)
gen_aadl2_FeatureConnection_Connection = Generalization(general=Connection, specific=aadl2_FeatureConnection)
gen_aadl2_FeatureGroupConnection_Connection = Generalization(general=Connection, specific=aadl2_FeatureGroupConnection)
gen_aadl2_ProcessorFeature_StructuralFeature = Generalization(general=StructuralFeature, specific=aadl2_ProcessorFeature)
gen_aadl2_InternalFeature_StructuralFeature = Generalization(general=StructuralFeature, specific=aadl2_InternalFeature)
gen_aadl2_InternalFeature_FeatureConnectionEnd = Generalization(general=FeatureConnectionEnd, specific=aadl2_InternalFeature)
gen_aadl2_InternalFeature_PortConnectionEnd = Generalization(general=PortConnectionEnd, specific=aadl2_InternalFeature)
gen_aadl2_SubprogramClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_SubprogramClassifier)
gen_aadl2_SubprogramClassifier_Subprogram = Generalization(general=Subprogram, specific=aadl2_SubprogramClassifier)
gen_aadl2_SubprogramClassifier_SubprogramSubcomponentType = Generalization(general=SubprogramSubcomponentType, specific=aadl2_SubprogramClassifier)
gen_aadl2_Subprogram_NamedElement = Generalization(general=NamedElement, specific=aadl2_Subprogram)
gen_aadl2_Subprogram_CalledSubprogram = Generalization(general=CalledSubprogram, specific=aadl2_Subprogram)
gen_aadl2_AnnexLibrary_NamedElement = Generalization(general=NamedElement, specific=aadl2_AnnexLibrary)
gen_aadl2_DefaultAnnexLibrary_AnnexLibrary = Generalization(general=AnnexLibrary, specific=aadl2_DefaultAnnexLibrary)
gen_aadl2_DefaultAnnexSubclause_AnnexSubclause = Generalization(general=AnnexSubclause, specific=aadl2_DefaultAnnexSubclause)
gen_aadl2_SubprogramProxy_ProcessorFeature = Generalization(general=ProcessorFeature, specific=aadl2_SubprogramProxy)
gen_aadl2_SubprogramProxy_AccessConnectionEnd = Generalization(general=AccessConnectionEnd, specific=aadl2_SubprogramProxy)
gen_aadl2_SubprogramProxy_CalledSubprogram = Generalization(general=CalledSubprogram, specific=aadl2_SubprogramProxy)
gen_aadl2_PackageRename_NamedElement = Generalization(general=NamedElement, specific=aadl2_PackageRename)
gen_aadl2_PublicPackageSection_PackageSection = Generalization(general=PackageSection, specific=aadl2_PublicPackageSection)
gen_aadl2_PackageSection_Namespace = Generalization(general=Namespace, specific=aadl2_PackageSection)
gen_aadl2_ModelUnit_NamedElement = Generalization(general=NamedElement, specific=aadl2_ModelUnit)
gen_aadl2_PrivatePackageSection_PackageSection = Generalization(general=PackageSection, specific=aadl2_PrivatePackageSection)
gen_aadl2_ComponentTypeRename_NamedElement = Generalization(general=NamedElement, specific=aadl2_ComponentTypeRename)
gen_aadl2_FeatureGroupTypeRename_NamedElement = Generalization(general=NamedElement, specific=aadl2_FeatureGroupTypeRename)
gen_aadl2_AadlPackage_ModelUnit = Generalization(general=ModelUnit, specific=aadl2_AadlPackage)
gen_aadl2_ComponentPrototypeActual_ArrayableElement = Generalization(general=ArrayableElement, specific=aadl2_ComponentPrototypeActual)
gen_aadl2_FeatureGroupPrototypeBinding_PrototypeBinding = Generalization(general=PrototypeBinding, specific=aadl2_FeatureGroupPrototypeBinding)
gen_aadl2_FeatureGroupPrototypeActual_FeaturePrototypeActual = Generalization(general=FeaturePrototypeActual, specific=aadl2_FeatureGroupPrototypeActual)
gen_aadl2_ComponentPrototypeBinding_PrototypeBinding = Generalization(general=PrototypeBinding, specific=aadl2_ComponentPrototypeBinding)
gen_aadl2_AccessSpecification_FeaturePrototypeActual = Generalization(general=FeaturePrototypeActual, specific=aadl2_AccessSpecification)
gen_aadl2_PortSpecification_FeaturePrototypeActual = Generalization(general=FeaturePrototypeActual, specific=aadl2_PortSpecification)
gen_aadl2_FeaturePrototypeActual_ArrayableElement = Generalization(general=ArrayableElement, specific=aadl2_FeaturePrototypeActual)
gen_aadl2_FeaturePrototypeBinding_PrototypeBinding = Generalization(general=PrototypeBinding, specific=aadl2_FeaturePrototypeBinding)
gen_aadl2_SubprogramCallSequence_BehavioralFeature = Generalization(general=BehavioralFeature, specific=aadl2_SubprogramCallSequence)
gen_aadl2_SubprogramCallSequence_ModalElement = Generalization(general=ModalElement, specific=aadl2_SubprogramCallSequence)
gen_aadl2_SubprogramCall_BehavioralFeature = Generalization(general=BehavioralFeature, specific=aadl2_SubprogramCall)
gen_aadl2_SubprogramCall_Context = Generalization(general=Context, specific=aadl2_SubprogramCall)
gen_aadl2_BehavioredImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_BehavioredImplementation)
gen_aadl2_AbstractType_ComponentType = Generalization(general=ComponentType, specific=aadl2_AbstractType)
gen_aadl2_FeaturePrototypeReference_FeaturePrototypeActual = Generalization(general=FeaturePrototypeActual, specific=aadl2_FeaturePrototypeReference)
gen_aadl2_AbstractClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_AbstractClassifier)
gen_aadl2_AbstractClassifier_Abstract = Generalization(general=Abstract, specific=aadl2_AbstractClassifier)
gen_aadl2_AbstractClassifier_AbstractSubcomponentType = Generalization(general=AbstractSubcomponentType, specific=aadl2_AbstractClassifier)
gen_aadl2_AbstractClassifier_BusSubcomponentType = Generalization(general=BusSubcomponentType, specific=aadl2_AbstractClassifier)
gen_aadl2_AbstractClassifier_DataSubcomponentType = Generalization(general=DataSubcomponentType, specific=aadl2_AbstractClassifier)
gen_aadl2_AbstractClassifier_DeviceSubcomponentType = Generalization(general=DeviceSubcomponentType, specific=aadl2_AbstractClassifier)
gen_aadl2_AbstractClassifier_MemorySubcomponentType = Generalization(general=MemorySubcomponentType, specific=aadl2_AbstractClassifier)
gen_aadl2_AbstractClassifier_ProcessorSubcomponentType = Generalization(general=ProcessorSubcomponentType, specific=aadl2_AbstractClassifier)
gen_aadl2_AbstractClassifier_ProcessSubcomponentType = Generalization(general=ProcessSubcomponentType, specific=aadl2_AbstractClassifier)
gen_aadl2_AbstractClassifier_SubprogramGroupSubcomponentType = Generalization(general=SubprogramGroupSubcomponentType, specific=aadl2_AbstractClassifier)
gen_aadl2_AbstractClassifier_SubprogramSubcomponentType = Generalization(general=SubprogramSubcomponentType, specific=aadl2_AbstractClassifier)
gen_aadl2_AbstractClassifier_SystemSubcomponentType = Generalization(general=SystemSubcomponentType, specific=aadl2_AbstractClassifier)
gen_aadl2_AbstractType_AbstractClassifier = Generalization(general=AbstractClassifier, specific=aadl2_AbstractType)
gen_aadl2_AbstractType_CallContext = Generalization(general=CallContext, specific=aadl2_AbstractType)
gen_aadl2_VirtualBusSubcomponentType_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_VirtualBusSubcomponentType)
gen_aadl2_VirtualBusSubcomponentType_AbstractFeatureClassifier = Generalization(general=AbstractFeatureClassifier, specific=aadl2_VirtualBusSubcomponentType)
gen_aadl2_VirtualBusSubcomponentType_BusFeatureClassifier = Generalization(general=BusFeatureClassifier, specific=aadl2_VirtualBusSubcomponentType)
gen_aadl2_ThreadGroupSubcomponentType_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_ThreadGroupSubcomponentType)
gen_aadl2_ThreadSubcomponentType_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_ThreadSubcomponentType)
gen_aadl2_SystemSubcomponentType_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_SystemSubcomponentType)
gen_aadl2_ProcessSubcomponentType_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_ProcessSubcomponentType)
gen_aadl2_MemorySubcomponentType_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_MemorySubcomponentType)
gen_aadl2_DeviceSubcomponentType_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_DeviceSubcomponentType)
gen_aadl2_BusSubcomponentType_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_BusSubcomponentType)
gen_aadl2_BusSubcomponentType_AbstractFeatureClassifier = Generalization(general=AbstractFeatureClassifier, specific=aadl2_BusSubcomponentType)
gen_aadl2_BusSubcomponentType_BusFeatureClassifier = Generalization(general=BusFeatureClassifier, specific=aadl2_BusSubcomponentType)
gen_aadl2_ProcessorSubcomponentType_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_ProcessorSubcomponentType)
gen_aadl2_AbstractClassifier_ThreadGroupSubcomponentType = Generalization(general=ThreadGroupSubcomponentType, specific=aadl2_AbstractClassifier)
gen_aadl2_AbstractImplementation_BehavioredImplementation = Generalization(general=BehavioredImplementation, specific=aadl2_AbstractImplementation)
gen_aadl2_AbstractImplementation_AbstractClassifier = Generalization(general=AbstractClassifier, specific=aadl2_AbstractImplementation)
gen_aadl2_AbstractClassifier_ThreadSubcomponentType = Generalization(general=ThreadSubcomponentType, specific=aadl2_AbstractClassifier)
gen_aadl2_AbstractClassifier_VirtualBusSubcomponentType = Generalization(general=VirtualBusSubcomponentType, specific=aadl2_AbstractClassifier)
gen_aadl2_AbstractClassifier_VirtualProcessorSubcomponentType = Generalization(general=VirtualProcessorSubcomponentType, specific=aadl2_AbstractClassifier)
gen_aadl2_VirtualProcessorSubcomponentType_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_VirtualProcessorSubcomponentType)
gen_aadl2_BusSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_BusSubcomponent)
gen_aadl2_BusSubcomponent_AccessConnectionEnd = Generalization(general=AccessConnectionEnd, specific=aadl2_BusSubcomponent)
gen_aadl2_BusSubcomponent_Bus = Generalization(general=Bus, specific=aadl2_BusSubcomponent)
gen_aadl2_Bus_NamedElement = Generalization(general=NamedElement, specific=aadl2_Bus)
gen_aadl2_DataSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_DataSubcomponent)
gen_aadl2_DataSubcomponent_AccessConnectionEnd = Generalization(general=AccessConnectionEnd, specific=aadl2_DataSubcomponent)
gen_aadl2_DataSubcomponent_Data = Generalization(general=Data, specific=aadl2_DataSubcomponent)
gen_aadl2_DataSubcomponent_ParameterConnectionEnd = Generalization(general=ParameterConnectionEnd, specific=aadl2_DataSubcomponent)
gen_aadl2_DataSubcomponent_PortConnectionEnd = Generalization(general=PortConnectionEnd, specific=aadl2_DataSubcomponent)
gen_aadl2_DeviceSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_DeviceSubcomponent)
gen_aadl2_Memory_NamedElement = Generalization(general=NamedElement, specific=aadl2_Memory)
gen_aadl2_ProcessSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_ProcessSubcomponent)
gen_aadl2_ProcessSubcomponent_Process = Generalization(general=Process, specific=aadl2_ProcessSubcomponent)
gen_aadl2_Process_NamedElement = Generalization(general=NamedElement, specific=aadl2_Process)
gen_aadl2_ProcessorSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_ProcessorSubcomponent)
gen_aadl2_DeviceSubcomponent_Device = Generalization(general=Device, specific=aadl2_DeviceSubcomponent)
gen_aadl2_Device_NamedElement = Generalization(general=NamedElement, specific=aadl2_Device)
gen_aadl2_MemorySubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_MemorySubcomponent)
gen_aadl2_MemorySubcomponent_Memory = Generalization(general=Memory, specific=aadl2_MemorySubcomponent)
gen_aadl2_Processor_NamedElement = Generalization(general=NamedElement, specific=aadl2_Processor)
gen_aadl2_SystemSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_SystemSubcomponent)
gen_aadl2_SystemSubcomponent_System = Generalization(general=System, specific=aadl2_SystemSubcomponent)
gen_aadl2_System_NamedElement = Generalization(general=NamedElement, specific=aadl2_System)
gen_aadl2_SubprogramSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_SubprogramSubcomponent)
gen_aadl2_SubprogramSubcomponent_AccessConnectionEnd = Generalization(general=AccessConnectionEnd, specific=aadl2_SubprogramSubcomponent)
gen_aadl2_SubprogramSubcomponent_Subprogram = Generalization(general=Subprogram, specific=aadl2_SubprogramSubcomponent)
gen_aadl2_ProcessorSubcomponent_Processor = Generalization(general=Processor, specific=aadl2_ProcessorSubcomponent)
gen_aadl2_SubprogramGroupSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_SubprogramGroupSubcomponent)
gen_aadl2_SubprogramGroupSubcomponent_AccessConnectionEnd = Generalization(general=AccessConnectionEnd, specific=aadl2_SubprogramGroupSubcomponent)
gen_aadl2_SubprogramGroupSubcomponent_SubprogramGroup = Generalization(general=SubprogramGroup, specific=aadl2_SubprogramGroupSubcomponent)
gen_aadl2_SubprogramGroupSubcomponent_CallContext = Generalization(general=CallContext, specific=aadl2_SubprogramGroupSubcomponent)
gen_aadl2_SubprogramGroup_NamedElement = Generalization(general=NamedElement, specific=aadl2_SubprogramGroup)
gen_aadl2_ThreadSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_ThreadSubcomponent)
gen_aadl2_ThreadSubcomponent_Thread = Generalization(general=Thread, specific=aadl2_ThreadSubcomponent)
gen_aadl2_VirtualBusSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_VirtualBusSubcomponent)
gen_aadl2_VirtualBusSubcomponent_AccessConnectionEnd = Generalization(general=AccessConnectionEnd, specific=aadl2_VirtualBusSubcomponent)
gen_aadl2_VirtualBusSubcomponent_VirtualBus = Generalization(general=VirtualBus, specific=aadl2_VirtualBusSubcomponent)
gen_aadl2_VirtualBus_NamedElement = Generalization(general=NamedElement, specific=aadl2_VirtualBus)
gen_aadl2_VirtualProcessorSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_VirtualProcessorSubcomponent)
gen_aadl2_VirtualProcessorSubcomponent_VirtualProcessor = Generalization(general=VirtualProcessor, specific=aadl2_VirtualProcessorSubcomponent)
gen_aadl2_VirtualProcessor_NamedElement = Generalization(general=NamedElement, specific=aadl2_VirtualProcessor)
gen_aadl2_AbstractPrototype_ComponentPrototype = Generalization(general=ComponentPrototype, specific=aadl2_AbstractPrototype)
gen_aadl2_AbstractPrototype_Abstract = Generalization(general=Abstract, specific=aadl2_AbstractPrototype)
gen_aadl2_AbstractPrototype_AbstractSubcomponentType = Generalization(general=AbstractSubcomponentType, specific=aadl2_AbstractPrototype)
gen_aadl2_AbstractPrototype_BusSubcomponentType = Generalization(general=BusSubcomponentType, specific=aadl2_AbstractPrototype)
gen_aadl2_AbstractPrototype_DataSubcomponentType = Generalization(general=DataSubcomponentType, specific=aadl2_AbstractPrototype)
gen_aadl2_AbstractPrototype_DeviceSubcomponentType = Generalization(general=DeviceSubcomponentType, specific=aadl2_AbstractPrototype)
gen_aadl2_AbstractPrototype_MemorySubcomponentType = Generalization(general=MemorySubcomponentType, specific=aadl2_AbstractPrototype)
gen_aadl2_AbstractPrototype_ProcessorSubcomponentType = Generalization(general=ProcessorSubcomponentType, specific=aadl2_AbstractPrototype)
gen_aadl2_AbstractPrototype_ProcessSubcomponentType = Generalization(general=ProcessSubcomponentType, specific=aadl2_AbstractPrototype)
gen_aadl2_AbstractPrototype_SubprogramGroupSubcomponentType = Generalization(general=SubprogramGroupSubcomponentType, specific=aadl2_AbstractPrototype)
gen_aadl2_AbstractPrototype_SubprogramSubcomponentType = Generalization(general=SubprogramSubcomponentType, specific=aadl2_AbstractPrototype)
gen_aadl2_AbstractPrototype_SystemSubcomponentType = Generalization(general=SystemSubcomponentType, specific=aadl2_AbstractPrototype)
gen_aadl2_AbstractPrototype_ThreadGroupSubcomponentType = Generalization(general=ThreadGroupSubcomponentType, specific=aadl2_AbstractPrototype)
gen_aadl2_AbstractPrototype_ThreadSubcomponentType = Generalization(general=ThreadSubcomponentType, specific=aadl2_AbstractPrototype)
gen_aadl2_AbstractPrototype_VirtualBusSubcomponentType = Generalization(general=VirtualBusSubcomponentType, specific=aadl2_AbstractPrototype)
gen_aadl2_AbstractPrototype_VirtualProcessorSubcomponentType = Generalization(general=VirtualProcessorSubcomponentType, specific=aadl2_AbstractPrototype)
gen_aadl2_BusClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_BusClassifier)
gen_aadl2_BusClassifier_Bus = Generalization(general=Bus, specific=aadl2_BusClassifier)
gen_aadl2_BusClassifier_BusSubcomponentType = Generalization(general=BusSubcomponentType, specific=aadl2_BusClassifier)
gen_aadl2_Thread_NamedElement = Generalization(general=NamedElement, specific=aadl2_Thread)
gen_aadl2_ThreadGroupSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_ThreadGroupSubcomponent)
gen_aadl2_ThreadGroupSubcomponent_ThreadGroup = Generalization(general=ThreadGroup, specific=aadl2_ThreadGroupSubcomponent)
gen_aadl2_ThreadGroup_NamedElement = Generalization(general=NamedElement, specific=aadl2_ThreadGroup)
gen_aadl2_BusImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_BusImplementation)
gen_aadl2_BusImplementation_BusClassifier = Generalization(general=BusClassifier, specific=aadl2_BusImplementation)
gen_aadl2_BusPrototype_ComponentPrototype = Generalization(general=ComponentPrototype, specific=aadl2_BusPrototype)
gen_aadl2_BusPrototype_Bus = Generalization(general=Bus, specific=aadl2_BusPrototype)
gen_aadl2_BusPrototype_BusSubcomponentType = Generalization(general=BusSubcomponentType, specific=aadl2_BusPrototype)
gen_aadl2_DataType_ComponentType = Generalization(general=ComponentType, specific=aadl2_DataType)
gen_aadl2_DataType_DataClassifier = Generalization(general=DataClassifier, specific=aadl2_DataType)
gen_aadl2_DataType_CallContext = Generalization(general=CallContext, specific=aadl2_DataType)
gen_aadl2_BusType_ComponentType = Generalization(general=ComponentType, specific=aadl2_BusType)
gen_aadl2_BusType_BusClassifier = Generalization(general=BusClassifier, specific=aadl2_BusType)
gen_aadl2_DataPrototype_ComponentPrototype = Generalization(general=ComponentPrototype, specific=aadl2_DataPrototype)
gen_aadl2_DataPrototype_Data = Generalization(general=Data, specific=aadl2_DataPrototype)
gen_aadl2_DataPrototype_DataSubcomponentType = Generalization(general=DataSubcomponentType, specific=aadl2_DataPrototype)
gen_aadl2_DeviceClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_DeviceClassifier)
gen_aadl2_DeviceClassifier_Device = Generalization(general=Device, specific=aadl2_DeviceClassifier)
gen_aadl2_DeviceClassifier_DeviceSubcomponentType = Generalization(general=DeviceSubcomponentType, specific=aadl2_DeviceClassifier)
gen_aadl2_DeviceType_ComponentType = Generalization(general=ComponentType, specific=aadl2_DeviceType)
gen_aadl2_DeviceType_DeviceClassifier = Generalization(general=DeviceClassifier, specific=aadl2_DeviceType)
gen_aadl2_DataImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_DataImplementation)
gen_aadl2_DataImplementation_DataClassifier = Generalization(general=DataClassifier, specific=aadl2_DataImplementation)
gen_aadl2_DeviceImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_DeviceImplementation)
gen_aadl2_DeviceImplementation_DeviceClassifier = Generalization(general=DeviceClassifier, specific=aadl2_DeviceImplementation)
gen_aadl2_DevicePrototype_ComponentPrototype = Generalization(general=ComponentPrototype, specific=aadl2_DevicePrototype)
gen_aadl2_DevicePrototype_Device = Generalization(general=Device, specific=aadl2_DevicePrototype)
gen_aadl2_DevicePrototype_DeviceSubcomponentType = Generalization(general=DeviceSubcomponentType, specific=aadl2_DevicePrototype)
gen_aadl2_MemoryClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_MemoryClassifier)
gen_aadl2_MemoryClassifier_Memory = Generalization(general=Memory, specific=aadl2_MemoryClassifier)
gen_aadl2_MemoryClassifier_MemorySubcomponentType = Generalization(general=MemorySubcomponentType, specific=aadl2_MemoryClassifier)
gen_aadl2_MemoryType_ComponentType = Generalization(general=ComponentType, specific=aadl2_MemoryType)
gen_aadl2_MemoryType_MemoryClassifier = Generalization(general=MemoryClassifier, specific=aadl2_MemoryType)
gen_aadl2_MemoryImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_MemoryImplementation)
gen_aadl2_MemoryImplementation_MemoryClassifier = Generalization(general=MemoryClassifier, specific=aadl2_MemoryImplementation)
gen_aadl2_MemoryPrototype_ComponentPrototype = Generalization(general=ComponentPrototype, specific=aadl2_MemoryPrototype)
gen_aadl2_MemoryPrototype_Memory = Generalization(general=Memory, specific=aadl2_MemoryPrototype)
gen_aadl2_MemoryPrototype_MemorySubcomponentType = Generalization(general=MemorySubcomponentType, specific=aadl2_MemoryPrototype)
gen_aadl2_SubprogramType_ComponentType = Generalization(general=ComponentType, specific=aadl2_SubprogramType)
gen_aadl2_SubprogramType_SubprogramClassifier = Generalization(general=SubprogramClassifier, specific=aadl2_SubprogramType)
gen_aadl2_SubprogramType_CallContext = Generalization(general=CallContext, specific=aadl2_SubprogramType)
gen_aadl2_SubprogramImplementation_BehavioredImplementation = Generalization(general=BehavioredImplementation, specific=aadl2_SubprogramImplementation)
gen_aadl2_SubprogramImplementation_SubprogramClassifier = Generalization(general=SubprogramClassifier, specific=aadl2_SubprogramImplementation)
gen_aadl2_SubprogramPrototype_ComponentPrototype = Generalization(general=ComponentPrototype, specific=aadl2_SubprogramPrototype)
gen_aadl2_SubprogramPrototype_Subprogram = Generalization(general=Subprogram, specific=aadl2_SubprogramPrototype)
gen_aadl2_SubprogramPrototype_SubprogramSubcomponentType = Generalization(general=SubprogramSubcomponentType, specific=aadl2_SubprogramPrototype)
gen_aadl2_SubprogramGroupClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_SubprogramGroupClassifier)
gen_aadl2_SubprogramGroupClassifier_SubprogramGroup = Generalization(general=SubprogramGroup, specific=aadl2_SubprogramGroupClassifier)
gen_aadl2_SubprogramGroupClassifier_SubprogramGroupSubcomponentType = Generalization(general=SubprogramGroupSubcomponentType, specific=aadl2_SubprogramGroupClassifier)
gen_aadl2_SubprogramGroupType_ComponentType = Generalization(general=ComponentType, specific=aadl2_SubprogramGroupType)
gen_aadl2_SubprogramGroupType_SubprogramGroupClassifier = Generalization(general=SubprogramGroupClassifier, specific=aadl2_SubprogramGroupType)
gen_aadl2_SubprogramGroupType_CallContext = Generalization(general=CallContext, specific=aadl2_SubprogramGroupType)
gen_aadl2_SubprogramGroupPrototype_ComponentPrototype = Generalization(general=ComponentPrototype, specific=aadl2_SubprogramGroupPrototype)
gen_aadl2_SubprogramGroupPrototype_SubprogramGroup = Generalization(general=SubprogramGroup, specific=aadl2_SubprogramGroupPrototype)
gen_aadl2_SubprogramGroupPrototype_SubprogramGroupSubcomponentType = Generalization(general=SubprogramGroupSubcomponentType, specific=aadl2_SubprogramGroupPrototype)
gen_aadl2_SystemClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_SystemClassifier)
gen_aadl2_SystemClassifier_System = Generalization(general=System, specific=aadl2_SystemClassifier)
gen_aadl2_SystemClassifier_SystemSubcomponentType = Generalization(general=SystemSubcomponentType, specific=aadl2_SystemClassifier)
gen_aadl2_SystemType_ComponentType = Generalization(general=ComponentType, specific=aadl2_SystemType)
gen_aadl2_SystemType_SystemClassifier = Generalization(general=SystemClassifier, specific=aadl2_SystemType)
gen_aadl2_SubprogramGroupImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_SubprogramGroupImplementation)
gen_aadl2_SubprogramGroupImplementation_SubprogramGroupClassifier = Generalization(general=SubprogramGroupClassifier, specific=aadl2_SubprogramGroupImplementation)
gen_aadl2_SystemImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_SystemImplementation)
gen_aadl2_SystemImplementation_SystemClassifier = Generalization(general=SystemClassifier, specific=aadl2_SystemImplementation)
gen_aadl2_SystemPrototype_ComponentPrototype = Generalization(general=ComponentPrototype, specific=aadl2_SystemPrototype)
gen_aadl2_SystemPrototype_System = Generalization(general=System, specific=aadl2_SystemPrototype)
gen_aadl2_SystemPrototype_SystemSubcomponentType = Generalization(general=SystemSubcomponentType, specific=aadl2_SystemPrototype)
gen_aadl2_ProcessorClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_ProcessorClassifier)
gen_aadl2_ProcessorClassifier_Processor = Generalization(general=Processor, specific=aadl2_ProcessorClassifier)
gen_aadl2_ProcessorClassifier_ProcessorSubcomponentType = Generalization(general=ProcessorSubcomponentType, specific=aadl2_ProcessorClassifier)
gen_aadl2_ProcessorType_ProcessorClassifier = Generalization(general=ProcessorClassifier, specific=aadl2_ProcessorType)
gen_aadl2_ProcessorType_ComponentType = Generalization(general=ComponentType, specific=aadl2_ProcessorType)
gen_aadl2_ProcessorImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_ProcessorImplementation)
gen_aadl2_ProcessorImplementation_ProcessorClassifier = Generalization(general=ProcessorClassifier, specific=aadl2_ProcessorImplementation)
gen_aadl2_ProcessImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_ProcessImplementation)
gen_aadl2_ProcessImplementation_ProcessClassifier = Generalization(general=ProcessClassifier, specific=aadl2_ProcessImplementation)
gen_aadl2_ProcessorPrototype_ComponentPrototype = Generalization(general=ComponentPrototype, specific=aadl2_ProcessorPrototype)
gen_aadl2_ProcessorPrototype_Processor = Generalization(general=Processor, specific=aadl2_ProcessorPrototype)
gen_aadl2_ProcessorPrototype_ProcessorSubcomponentType = Generalization(general=ProcessorSubcomponentType, specific=aadl2_ProcessorPrototype)
gen_aadl2_ProcessClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_ProcessClassifier)
gen_aadl2_ProcessClassifier_Process = Generalization(general=Process, specific=aadl2_ProcessClassifier)
gen_aadl2_ProcessClassifier_ProcessSubcomponentType = Generalization(general=ProcessSubcomponentType, specific=aadl2_ProcessClassifier)
gen_aadl2_ProcessType_ComponentType = Generalization(general=ComponentType, specific=aadl2_ProcessType)
gen_aadl2_ProcessType_ProcessClassifier = Generalization(general=ProcessClassifier, specific=aadl2_ProcessType)
gen_aadl2_ProcessPrototype_ComponentPrototype = Generalization(general=ComponentPrototype, specific=aadl2_ProcessPrototype)
gen_aadl2_ProcessPrototype_Process = Generalization(general=Process, specific=aadl2_ProcessPrototype)
gen_aadl2_ProcessPrototype_ProcessSubcomponentType = Generalization(general=ProcessSubcomponentType, specific=aadl2_ProcessPrototype)
gen_aadl2_ThreadClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_ThreadClassifier)
gen_aadl2_ThreadClassifier_Thread = Generalization(general=Thread, specific=aadl2_ThreadClassifier)
gen_aadl2_ThreadClassifier_ThreadSubcomponentType = Generalization(general=ThreadSubcomponentType, specific=aadl2_ThreadClassifier)
gen_aadl2_ThreadType_ComponentType = Generalization(general=ComponentType, specific=aadl2_ThreadType)
gen_aadl2_ThreadType_ThreadClassifier = Generalization(general=ThreadClassifier, specific=aadl2_ThreadType)
gen_aadl2_ThreadImplementation_BehavioredImplementation = Generalization(general=BehavioredImplementation, specific=aadl2_ThreadImplementation)
gen_aadl2_ThreadImplementation_ThreadClassifier = Generalization(general=ThreadClassifier, specific=aadl2_ThreadImplementation)
gen_aadl2_ThreadPrototype_ComponentPrototype = Generalization(general=ComponentPrototype, specific=aadl2_ThreadPrototype)
gen_aadl2_ThreadPrototype_Thread = Generalization(general=Thread, specific=aadl2_ThreadPrototype)
gen_aadl2_ThreadPrototype_ThreadSubcomponentType = Generalization(general=ThreadSubcomponentType, specific=aadl2_ThreadPrototype)
gen_aadl2_ThreadGroupClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_ThreadGroupClassifier)
gen_aadl2_ThreadGroupClassifier_ThreadGroup = Generalization(general=ThreadGroup, specific=aadl2_ThreadGroupClassifier)
gen_aadl2_ThreadGroupClassifier_ThreadGroupSubcomponentType = Generalization(general=ThreadGroupSubcomponentType, specific=aadl2_ThreadGroupClassifier)
gen_aadl2_ThreadGroupType_ComponentType = Generalization(general=ComponentType, specific=aadl2_ThreadGroupType)
gen_aadl2_ThreadGroupType_ThreadGroupClassifier = Generalization(general=ThreadGroupClassifier, specific=aadl2_ThreadGroupType)
gen_aadl2_ThreadGroupImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_ThreadGroupImplementation)
gen_aadl2_ThreadGroupImplementation_ThreadGroupClassifier = Generalization(general=ThreadGroupClassifier, specific=aadl2_ThreadGroupImplementation)
gen_aadl2_ThreadGroupPrototype_ComponentPrototype = Generalization(general=ComponentPrototype, specific=aadl2_ThreadGroupPrototype)
gen_aadl2_VirtualBusType_VirtualBusClassifier = Generalization(general=VirtualBusClassifier, specific=aadl2_VirtualBusType)
gen_aadl2_ThreadGroupPrototype_ThreadGroup = Generalization(general=ThreadGroup, specific=aadl2_ThreadGroupPrototype)
gen_aadl2_ThreadGroupPrototype_ThreadGroupSubcomponentType = Generalization(general=ThreadGroupSubcomponentType, specific=aadl2_ThreadGroupPrototype)
gen_aadl2_VirtualBusClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_VirtualBusClassifier)
gen_aadl2_VirtualBusClassifier_VirtualBus = Generalization(general=VirtualBus, specific=aadl2_VirtualBusClassifier)
gen_aadl2_VirtualBusClassifier_VirtualBusSubcomponentType = Generalization(general=VirtualBusSubcomponentType, specific=aadl2_VirtualBusClassifier)
gen_aadl2_VirtualBusType_ComponentType = Generalization(general=ComponentType, specific=aadl2_VirtualBusType)
gen_aadl2_VirtualBusPrototype_ComponentPrototype = Generalization(general=ComponentPrototype, specific=aadl2_VirtualBusPrototype)
gen_aadl2_VirtualBusPrototype_VirtualBus = Generalization(general=VirtualBus, specific=aadl2_VirtualBusPrototype)
gen_aadl2_VirtualBusPrototype_VirtualBusSubcomponentType = Generalization(general=VirtualBusSubcomponentType, specific=aadl2_VirtualBusPrototype)
gen_aadl2_VirtualProcessorClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_VirtualProcessorClassifier)
gen_aadl2_VirtualProcessorClassifier_VirtualProcessor = Generalization(general=VirtualProcessor, specific=aadl2_VirtualProcessorClassifier)
gen_aadl2_VirtualProcessorClassifier_VirtualProcessorSubcomponentType = Generalization(general=VirtualProcessorSubcomponentType, specific=aadl2_VirtualProcessorClassifier)
gen_aadl2_VirtualBusImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_VirtualBusImplementation)
gen_aadl2_VirtualBusImplementation_VirtualBusClassifier = Generalization(general=VirtualBusClassifier, specific=aadl2_VirtualBusImplementation)
gen_aadl2_VirtualProcessorType_ComponentType = Generalization(general=ComponentType, specific=aadl2_VirtualProcessorType)
gen_aadl2_VirtualProcessorType_VirtualProcessorClassifier = Generalization(general=VirtualProcessorClassifier, specific=aadl2_VirtualProcessorType)
gen_aadl2_VirtualProcessorImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_VirtualProcessorImplementation)
gen_aadl2_VirtualProcessorImplementation_VirtualProcessorClassifier = Generalization(general=VirtualProcessorClassifier, specific=aadl2_VirtualProcessorImplementation)
gen_aadl2_PropertyConstant_TypedElement = Generalization(general=TypedElement, specific=aadl2_PropertyConstant)
gen_aadl2_PropertyConstant_AbstractNamedValue = Generalization(general=AbstractNamedValue, specific=aadl2_PropertyConstant)
gen_aadl2_PropertyConstant_ArraySizeProperty = Generalization(general=ArraySizeProperty, specific=aadl2_PropertyConstant)
gen_aadl2_VirtualProcessorPrototype_ComponentPrototype = Generalization(general=ComponentPrototype, specific=aadl2_VirtualProcessorPrototype)
gen_aadl2_VirtualProcessorPrototype_VirtualProcessor = Generalization(general=VirtualProcessor, specific=aadl2_VirtualProcessorPrototype)
gen_aadl2_VirtualProcessorPrototype_VirtualProcessorSubcomponentType = Generalization(general=VirtualProcessorSubcomponentType, specific=aadl2_VirtualProcessorPrototype)
gen_aadl2_BasicPropertyAssociation_Element = Generalization(general=Element, specific=aadl2_BasicPropertyAssociation)
gen_aadl2_StringLiteral_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_StringLiteral)
gen_aadl2_PropertyValue_PropertyExpression = Generalization(general=PropertyExpression, specific=aadl2_PropertyValue)
gen_aadl2_NumberValue_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_NumberValue)
gen_aadl2_UnitLiteral_EnumerationLiteral = Generalization(general=EnumerationLiteral, specific=aadl2_UnitLiteral)
gen_aadl2_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=aadl2_EnumerationLiteral)
gen_aadl2_EnumerationLiteral_AbstractNamedValue = Generalization(general=AbstractNamedValue, specific=aadl2_EnumerationLiteral)
gen_aadl2_ReferenceValue_ContainedNamedElement = Generalization(general=ContainedNamedElement, specific=aadl2_ReferenceValue)
gen_aadl2_ReferenceValue_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_ReferenceValue)
gen_aadl2_BooleanLiteral_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_BooleanLiteral)
gen_aadl2_RangeValue_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_RangeValue)
gen_aadl2_ClassifierValue_PropertyOwner = Generalization(general=PropertyOwner, specific=aadl2_ClassifierValue)
gen_aadl2_ClassifierValue_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_ClassifierValue)
gen_aadl2_IntegerLiteral_NumberValue = Generalization(general=NumberValue, specific=aadl2_IntegerLiteral)
gen_aadl2_RealLiteral_NumberValue = Generalization(general=NumberValue, specific=aadl2_RealLiteral)
gen_aadl2_RecordValue_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_RecordValue)
gen_aadl2_ComputedValue_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_ComputedValue)
gen_aadl2_Operation_PropertyExpression = Generalization(general=PropertyExpression, specific=aadl2_Operation)
gen_aadl2_NamedValue_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_NamedValue)
gen_aadl2_PropertySet_Namespace = Generalization(general=Namespace, specific=aadl2_PropertySet)
gen_aadl2_PropertySet_ModelUnit = Generalization(general=ModelUnit, specific=aadl2_PropertySet)
gen_aadl2_ListValue_PropertyExpression = Generalization(general=PropertyExpression, specific=aadl2_ListValue)
gen_aadl2_GlobalNamespace_Namespace = Generalization(general=Namespace, specific=aadl2_GlobalNamespace)
gen_aadl2_AadlString_NonListType = Generalization(general=NonListType, specific=aadl2_AadlString)
gen_aadl2_AadlInteger_NumberType = Generalization(general=NumberType, specific=aadl2_AadlInteger)
gen_aadl2_NumberType_NonListType = Generalization(general=NonListType, specific=aadl2_NumberType)
gen_aadl2_NonListType_PropertyType = Generalization(general=PropertyType, specific=aadl2_NonListType)
gen_aadl2_AadlBoolean_NonListType = Generalization(general=NonListType, specific=aadl2_AadlBoolean)
gen_aadl2_EnumerationType_Namespace = Generalization(general=Namespace, specific=aadl2_EnumerationType)
gen_aadl2_EnumerationType_NonListType = Generalization(general=NonListType, specific=aadl2_EnumerationType)
gen_aadl2_NumericRange_Element = Generalization(general=Element, specific=aadl2_NumericRange)
gen_aadl2_UnitsType_EnumerationType = Generalization(general=EnumerationType, specific=aadl2_UnitsType)
gen_aadl2_RangeType_NonListType = Generalization(general=NonListType, specific=aadl2_RangeType)
gen_aadl2_AadlReal_NumberType = Generalization(general=NumberType, specific=aadl2_AadlReal)
gen_aadl2_ClassifierType_NonListType = Generalization(general=NonListType, specific=aadl2_ClassifierType)
gen_aadl2_RecordField_BasicProperty = Generalization(general=BasicProperty, specific=aadl2_RecordField)
gen_aadl2_ReferenceType_NonListType = Generalization(general=NonListType, specific=aadl2_ReferenceType)
gen_aadl2_ListType_PropertyType = Generalization(general=PropertyType, specific=aadl2_ListType)
gen_aadl2_RecordType_Namespace = Generalization(general=Namespace, specific=aadl2_RecordType)
gen_aadl2_RecordType_NonListType = Generalization(general=NonListType, specific=aadl2_RecordType)

# Domain Model
domain_model = DomainModel(
    name="aadl2",
    types={aadl2_Element, Element, aadl2_Type, NamedElement, aadl2_NamedElement, aadl2_Comment, aadl2_PropertyAssociation, aadl2_Property, aadl2_ContainedNamedElement, aadl2_Classifier, BasicProperty, AbstractNamedValue, aadl2_PropertyExpression, aadl2_MetaclassReference, aadl2_PropertyOwner, aadl2_BasicProperty, TypedElement, aadl2_PropertyType, aadl2_ModalPropertyValue, Type, aadl2_AbstractNamedValue, PropertyOwner, Namespace, aadl2_ClassifierFeature, aadl2_Generalization, aadl2_TypedElement, aadl2_Namespace, aadl2_AnnexSubclause, aadl2_Prototype, aadl2_PrototypeBinding, DirectedRelationship, aadl2_DirectedRelationship, Relationship, aadl2_Relationship, ModalElement, aadl2_ModalElement, aadl2_Mode, aadl2_ModeFeature, ClassifierFeature, StructuralFeature, CalledSubprogram, aadl2_StructuralFeature, RefinableElement, ModeFeature, aadl2_CalledSubprogram, aadl2_ContainmentPathElement, aadl2_RefinableElement, aadl2_BehavioralFeature, aadl2_ArrayDimension, aadl2_ArraySize, aadl2_ArrayRange, aadl2_ArrayableElement, aadl2_ComponentImplementationReference, aadl2_ComponentImplementation, ComponentClassifier, aadl2_ComponentType, aadl2_Subcomponent, aadl2_ArraySizeProperty, aadl2_Realization, aadl2_EndToEndFlow, aadl2_AbstractSubcomponent, aadl2_AccessConnection, aadl2_ParameterConnection, aadl2_PortConnection, aadl2_FeatureConnection, aadl2_FeatureGroupConnection, aadl2_FlowImplementation, aadl2_Connection, aadl2_ImplementationExtension, aadl2_ProcessorFeature, aadl2_InternalFeature, aadl2_EventSource, aadl2_EventDataSource, aadl2_ComponentClassifier, Classifier, SubcomponentType, FeatureClassifier, aadl2_ModeTransition, aadl2_SubcomponentType, aadl2_FeatureClassifier, aadl2_PortProxy, aadl2_SubprogramProxy, aadl2_Context, aadl2_TriggerPort, aadl2_Feature, aadl2_FlowSpecification, aadl2_TypeExtension, aadl2_ModeTransitionTrigger, FeatureConnectionEnd, ArrayableElement, aadl2_ComponentPrototype, aadl2_FeatureConnectionEnd, aadl2_FeatureGroup, aadl2_AbstractFeature, FlowFeature, ModalPath, FlowElement, aadl2_FlowEnd, aadl2_FlowFeature, ConnectionEnd, aadl2_ConnectionEnd, Prototype, aadl2_FlowElement, EndToEndFlowElement, aadl2_EndToEndFlowElement, Flow, aadl2_Flow, aadl2_ModalPath, Generalization, DirectedFeature, Context, FeatureGroupConnectionEnd, CallContext, aadl2_FeatureType, aadl2_FeatureGroupType, aadl2_FeatureGroupPrototype, aadl2_FeatureGroupConnectionEnd, FeatureType, aadl2_GroupExtension, aadl2_BusAccess, aadl2_DataAccess, aadl2_DataPort, aadl2_CallContext, aadl2_EventDataPort, aadl2_DirectedFeature, Feature, aadl2_SubprogramAccess, aadl2_SubprogramGroupAccess, Access, aadl2_BusFeatureClassifier, aadl2_Access, AccessConnectionEnd, aadl2_AccessConnectionEnd, aadl2_EventPort, aadl2_Parameter, aadl2_DataSubcomponentType, aadl2_ParameterConnectionEnd, aadl2_PortConnectionEnd, AbstractFeatureClassifier, aadl2_AbstractFeatureClassifier, Port, aadl2_Port, TriggerPort, ParameterConnectionEnd, PortConnectionEnd, aadl2_SubprogramSubcomponentType, aadl2_SubprogramGroupSubcomponentType, aadl2_FeaturePrototype, aadl2_ModeBinding, aadl2_FlowSegment, aadl2_ConnectedElement, aadl2_EndToEndFlowSegment, Subcomponent, Abstract, aadl2_AbstractSubcomponentType, aadl2_Abstract, Connection, InternalFeature, aadl2_DataClassifier, Data, DataSubcomponentType, aadl2_Data, ProcessorFeature, Subprogram, SubprogramSubcomponentType, aadl2_Subprogram, aadl2_AnnexLibrary, aadl2_DefaultAnnexLibrary, AnnexLibrary, aadl2_DefaultAnnexSubclause, AnnexSubclause, aadl2_SubprogramClassifier, aadl2_PackageRename, aadl2_ComponentTypeRename, aadl2_FeatureGroupTypeRename, aadl2_ModelUnit, aadl2_PublicPackageSection, PackageSection, aadl2_PrivatePackageSection, aadl2_PackageSection, aadl2_AadlPackage, ModelUnit, aadl2_FeatureGroupPrototypeBinding, aadl2_FeatureGroupPrototypeActual, FeaturePrototypeActual, aadl2_ComponentPrototypeBinding, PrototypeBinding, aadl2_ComponentPrototypeActual, aadl2_AccessSpecification, aadl2_PortSpecification, aadl2_FeaturePrototypeActual, aadl2_FeaturePrototypeBinding, aadl2_SubprogramCallSequence, BehavioralFeature, aadl2_SubprogramCall, aadl2_BehavioredImplementation, ComponentImplementation, aadl2_AbstractType, ComponentType, AbstractClassifier, aadl2_FeaturePrototypeReference, aadl2_AbstractClassifier, AbstractSubcomponentType, BusSubcomponentType, DeviceSubcomponentType, MemorySubcomponentType, ProcessorSubcomponentType, ProcessSubcomponentType, SubprogramGroupSubcomponentType, SystemSubcomponentType, aadl2_VirtualBusSubcomponentType, BusFeatureClassifier, aadl2_ThreadGroupSubcomponentType, aadl2_ThreadSubcomponentType, aadl2_SystemSubcomponentType, aadl2_ProcessSubcomponentType, aadl2_MemorySubcomponentType, aadl2_DeviceSubcomponentType, aadl2_BusSubcomponentType, aadl2_ProcessorSubcomponentType, ThreadGroupSubcomponentType, aadl2_AbstractImplementation, BehavioredImplementation, ThreadSubcomponentType, VirtualBusSubcomponentType, VirtualProcessorSubcomponentType, aadl2_VirtualProcessorSubcomponentType, aadl2_DataSubcomponent, aadl2_DeviceSubcomponent, aadl2_MemorySubcomponent, aadl2_ProcessSubcomponent, aadl2_ProcessorSubcomponent, aadl2_SystemSubcomponent, aadl2_SubprogramSubcomponent, aadl2_SubprogramGroupSubcomponent, aadl2_ThreadSubcomponent, aadl2_BusSubcomponent, aadl2_VirtualBusSubcomponent, aadl2_VirtualProcessorSubcomponent, Bus, aadl2_Bus, aadl2_ThreadGroupSubcomponent, aadl2_Memory, Process, aadl2_Process, Device, Processor, aadl2_Device, Memory, aadl2_Processor, System, aadl2_System, SubprogramGroup, aadl2_SubprogramGroup, Thread, VirtualBus, aadl2_VirtualBus, VirtualProcessor, aadl2_VirtualProcessor, aadl2_AbstractPrototype, ComponentPrototype, aadl2_BusClassifier, aadl2_Thread, ThreadGroup, aadl2_ThreadGroup, aadl2_BusImplementation, aadl2_BusPrototype, aadl2_DataType, DataClassifier, aadl2_BusType, BusClassifier, aadl2_DataPrototype, aadl2_DeviceClassifier, aadl2_DeviceType, DeviceClassifier, aadl2_DataImplementation, aadl2_DeviceImplementation, aadl2_DevicePrototype, aadl2_MemoryClassifier, aadl2_MemoryType, MemoryClassifier, aadl2_MemoryImplementation, aadl2_MemoryPrototype, aadl2_SubprogramType, SubprogramClassifier, aadl2_SubprogramImplementation, aadl2_SubprogramPrototype, aadl2_SubprogramGroupClassifier, aadl2_SubprogramGroupType, SubprogramGroupClassifier, aadl2_SubprogramGroupPrototype, aadl2_SystemClassifier, aadl2_SystemType, SystemClassifier, aadl2_SubprogramGroupImplementation, aadl2_SystemImplementation, aadl2_SystemPrototype, aadl2_ProcessorClassifier, aadl2_ProcessorType, ProcessorClassifier, aadl2_ProcessorImplementation, aadl2_ProcessorPrototype, aadl2_ProcessImplementation, aadl2_ProcessClassifier, aadl2_ProcessType, ProcessClassifier, aadl2_ProcessPrototype, aadl2_ThreadClassifier, aadl2_ThreadType, ThreadClassifier, aadl2_ThreadImplementation, aadl2_ThreadPrototype, aadl2_ThreadGroupClassifier, aadl2_ThreadGroupType, ThreadGroupClassifier, aadl2_ThreadGroupImplementation, aadl2_ThreadGroupPrototype, VirtualBusClassifier, aadl2_VirtualBusClassifier, aadl2_VirtualBusType, aadl2_VirtualBusPrototype, aadl2_VirtualProcessorClassifier, aadl2_VirtualBusImplementation, aadl2_VirtualProcessorType, VirtualProcessorClassifier, aadl2_VirtualProcessorImplementation, aadl2_PropertyConstant, ArraySizeProperty, aadl2_VirtualProcessorPrototype, aadl2_BasicPropertyAssociation, aadl2_StringLiteral, PropertyValue, aadl2_PropertyValue, PropertyExpression, aadl2_NumberValue, EnumerationLiteral, aadl2_EnumerationLiteral, aadl2_UnitLiteral, aadl2_ReferenceValue, ContainedNamedElement, aadl2_BooleanLiteral, aadl2_RangeValue, aadl2_ClassifierValue, aadl2_IntegerLiteral, NumberValue, aadl2_RealLiteral, aadl2_RecordValue, aadl2_ComputedValue, aadl2_Operation, aadl2_NamedValue, aadl2_PropertySet, aadl2_ListValue, aadl2_GlobalNamespace, aadl2_AadlString, aadl2_AadlInteger, NumberType, aadl2_NumberType, aadl2_UnitsType, aadl2_NumericRange, aadl2_NonListType, PropertyType, aadl2_AadlBoolean, NonListType, aadl2_EnumerationType, EnumerationType, aadl2_RangeType, aadl2_AadlReal, aadl2_ClassifierType, aadl2_RecordField, aadl2_ReferenceType, aadl2_ListType, aadl2_RecordType, FlowKind, DirectionType, PortCategory, AccessType, AccessCategory, ComponentCategory, OperationKind},
    associations={ownedElement1, ownedComment2, ownedPropertyAssociation4, property5, appliesTo7, inBinding9, defaultValue13, appliesToMetaclass15, appliesToClassifier17, appliesTo20, referencedPropertyType22, ownedValue11, classifierFeature30, inheritedMember31, generalization34, general36, ownedPropertyType23, propertyType26, type29, ownedMember44, member46, ownedAnnexSubclause38, ownedPrototype40, ownedPrototypeBinding42, general50, specific52, featuringClassifier49, relatedElement59, inMode61, source54, target56, refined63, refinedElement68, formal70, path73, containmentPathElement75, refinementContext65, path84, ownedValue86, size89, arrayRange78, namedElement80, arrayDimension92, implementation94, ownedPrototypeBinding95, type98, ownedSubcomponent100, extended103, sizeProperty90, ownedRealization111, ownedEndToEndFlow113, ownedAbstractSubcomponent115, ownedAccessConnection117, ownedParameterConnection119, ownedPortConnection121, ownedFeatureConnection123, ownedFeatureGroupConnection125, ownedFlowImplementation105, ownedConnection107, ownedExtension109, ownedProcessorFeature127, ownedInternalFeature129, ownedEventSource131, ownedEventDataSource133, ownedMode139, ownedModeTransition141, source143, ownedPortProxy135, ownedSubprogramProxy137, context151, triggerPort153, ownedFeature155, extended158, ownedFlowSpecification160, destination146, ownedTrigger149, prototype168, featureClassifier170, refined173, classifier175, ownedExtension162, ownedFeatureGroup164, ownedAbstractFeature166, constrainingClassifier178, refined182, outEnd184, InEnd186, inModeOrTransition189, context190, extended196, featureType199, featureGroupType201, featureGroupPrototype203, feature193, ownedFeature205, extended209, inverse212, ownedExtension214, ownedBusAccess216, ownedDataAccess218, ownedDataPort220, ownedSubprogramAccess231, ownedSubprogramGroupAccess233, ownedAbstractFeature235, extended238, busFeatureClassifier241, ownedEventDataPort222, ownedEventPort224, ownedFeatureGroup226, ownedParameter229, dataFeatureClassifier243, dataFeatureClassifier245, dataFeatureClassifier251, subprogramFeatureClassifier254, subprogramGroupFeatureClassifier256, featurePrototype258, dataFeatureClassifier248, constrainingFeatureGroupType265, subcomponentType268, ownedPrototypeBinding270, prototype273, abstractFeatureClassifier260, constrainingClassifier262, classifier284, parentMode287, derivedMode290, specification293, ownedFlowSegment296, inEnd298, outEnd301, ownedModeBinding276, implementationReference278, refined282, destination309, source311, refined315, context317, connectionEnd320, next323, extended325, flowElement304, context306, ownedEndToEndFlowSegment334, flowElement336, context338, abstractSubcomponentType341, implemented328, refined332, dataClassifier343, dataClassifier345, parsedAnnexLibrary350, parsedAnnexSubclause351, subprogramClassifier348, ownedPackageRename354, ownedComponentTypeRename355, ownedClassifier357, ownedFeatureGroupTypeRename360, ownedAnnexLibrary362, importedUnit365, privateSection353, ownedPublicSection369, ownedPrivateSection371, publicSection373, privateSection376, publicSection379, renamedComponentType380, renamedPackage367, actual386, binding387, subcomponentType390, actual393, binding394, featureType397, renamedFeatureGroupType383, actual400, classifier401, componentPrototype403, classifier406, componentPrototype408, ownedSubprogramCall413, calledSubprogram414, context416, subprogramCall418, ownedSubprogramCallSequence420, prototype411, ownedSubprogramAccess428, ownedDataPort431, ownedEventPort434, ownedEventDataPort437, ownedSubprogramGroupAccess440, ownedBusAccess423, ownedDataAccess425, ownedDataSubcomponent444, ownedDeviceSubcomponent446, ownedMemorySubcomponent448, ownedProcessSubcomponent450, ownedProcessorSubcomponent452, ownedSystemSubcomponent454, ownedSubprogramSubcomponent456, ownedSubprogramGroupSubcomponent458, ownedThreadSubcomponent460, ownedBusSubcomponent443, ownedThreadGroupSubcomponent462, ownedVirtualBusSubcomponent464, ownedVirtualProcessorSubcomponent466, busSubcomponentType468, dataSubcomponentType470, memorySubcomponentType475, processSubcomponentType477, deviceSubcomponentType473, systemSubcomponentType481, subprogramSubcomponentType483, processorSubcomponentType479, subprogramGroupSubcomponentType486, threadSubcomponentType489, virtualBusSubcomponentType493, virtualProcessorSubcomponentType495, threadGroupSubcomponentType491, ownedDataPort499, ownedEventDataPort502, ownedEventPort505, ownedVirtualBusSubcomponent508, ownedSubprogramAccess510, ownedBusAccess497, ownedDataSubcomponent518, ownedSubprogramSubcomponent520, ownedDataPort523, ownedEventDataPort525, ownedEventPort528, ownedDataAccess512, ownedSubprogramGroupAccess515, ownedBusSubcomponent540, ownedDataSubcomponent542, ownedVirtualBusSubcomponent545, ownedBusAccess531, ownedSubprogramAccess534, ownedSubprogramGroupAccess537, ownedEventPort556, ownedBusSubcomponent559, ownedMemorySubcomponent561, ownedEventDataPort564, ownedEventPort566, ownedBusAccess548, ownedDataPort550, ownedEventDataPort553, ownedSubprogramAccess575, ownedSubprogramGroupAccess578, ownedDataSubcomponent581, ownedSubprogramSubcomponent583, ownedParameter569, ownedDataAccess572, ownedSubprogramSubcomponent591, ownedSubprogramGroupSubcomponent593, ownedDataSubcomponent596, ownedBusAccess599, ownedSubprogramAccess586, ownedSubprogramGroupAccess588, ownedSubprogramAccess610, ownedEventPort613, ownedEventDataPort616, ownedBusSubcomponent619, ownedDataSubcomponent621, ownedDeviceSubcomponent624, ownedDataAccess601, ownedDataPort604, ownedSubprogramGroupAccess607, ownedProcessorSubcomponent633, ownedSubprogramSubcomponent636, ownedSubprogramGroupSubcomponent639, ownedSystemSubcomponent642, ownedVirtualBusSubcomponent645, ownedVirtualProcessorSubcomponent648, ownedMemorySubcomponent627, ownedProcessSubcomponent630, ownedDataPort651, ownedEventDataPort653, ownedEventPort656, ownedSubprogramGroupAccess665, ownedBusSubcomponent668, ownedMemorySubcomponent670, ownedVirtualBusSubcomponent673, ownedVirtualProcessorSubcomponent676, ownedBusAccess659, ownedSubprogramAccess662, ownedDataPort679, ownedEventDataPort681, ownedEventPort684, ownedDataAccess687, ownedSubprogramAccess690, ownedSubprogramGroupAccess693, ownedDataSubcomponent696, ownedSubprogramGroupSubcomponent701, ownedThreadSubcomponent704, ownedSubprogramSubcomponent698, ownedThreadGroupSubcomponent707, ownedEventDataPort712, ownedEventPort715, ownedDataAccess718, ownedDataPort710, ownedSubprogramGroupAccess724, ownedSubprogramAccess721, ownedSubprogramGroupSubcomponent727, ownedSubprogramSubcomponent729, ownedDataSubcomponent732, ownedEventDataPort737, ownedEventPort740, ownedDataPort735, ownedSubprogramGroupAccess749, ownedDataAccess743, ownedSubprogramAccess746, ownedThreadGroupSubcomponent757, ownedSubprogramSubcomponent760, ownedSubprogramGroupSubcomponent763, ownedDataSubcomponent752, ownedThreadSubcomponent754, ownedDataPort766, ownedEventDataPort768, ownedEventPort771, ownedVirtualBusSubcomponent777, ownedBusAccess774, ownedEventDataPort781, ownedEventPort784, ownedSubprogramAccess787, ownedDataPort779, ownedVirtualBusSubcomponent796, ownedVirtualProcessorSubcomponent798, ownedSubprogramGroupAccess790, ownedBusAccess793, property801, ownedValue803, referencedPropertyType806, ownedPropertyType808, constantValue811, propertyType814, baseUnit819, factor821, unit817, minimum826, classifier824, maximum828, delta831, ownedFieldValue836, ownedPropertyExpression834, namedValue840, ownedPropertyType841, ownedProperty843, ownedListElement838, importedUnit849, ownedAnnexSubclause852, package855, propertySet857, ownedPropertyConstant846, ownedUnitsType860, referencedUnitsType861, range864, ownedLiteral869, upperBound870, unitsType866, classifierReference876, ownedNumberType878, numberType880, lowerBound873, ownedField886, namedElementReference888, referencedNumberType883, elementType895, ownedElementType890, referencedElementType892},
    generalizations={gen_aadl2_Comment_Element, gen_aadl2_Type_NamedElement, gen_aadl2_NamedElement_Element, gen_aadl2_PropertyAssociation_Element, gen_aadl2_Property_BasicProperty, gen_aadl2_Property_AbstractNamedValue, gen_aadl2_BasicProperty_TypedElement, gen_aadl2_PropertyType_Type, gen_aadl2_PropertyExpression_Element, gen_aadl2_MetaclassReference_PropertyOwner, gen_aadl2_PropertyOwner_Element, gen_aadl2_Classifier_Namespace, gen_aadl2_Classifier_Type, gen_aadl2_TypedElement_NamedElement, gen_aadl2_Namespace_NamedElement, gen_aadl2_Generalization_DirectedRelationship, gen_aadl2_DirectedRelationship_Relationship, gen_aadl2_ClassifierFeature_NamedElement, gen_aadl2_Relationship_Element, gen_aadl2_AnnexSubclause_ModalElement, gen_aadl2_ModalElement_NamedElement, gen_aadl2_ModeFeature_ClassifierFeature, gen_aadl2_Prototype_StructuralFeature, gen_aadl2_Prototype_CalledSubprogram, gen_aadl2_StructuralFeature_RefinableElement, gen_aadl2_StructuralFeature_ClassifierFeature, gen_aadl2_Mode_ModeFeature, gen_aadl2_PrototypeBinding_Element, gen_aadl2_ContainedNamedElement_Element, gen_aadl2_RefinableElement_NamedElement, gen_aadl2_ArrayRange_Element, gen_aadl2_ModalPropertyValue_ModalElement, gen_aadl2_BehavioralFeature_ClassifierFeature, gen_aadl2_ArrayDimension_Element, gen_aadl2_ContainmentPathElement_Element, gen_aadl2_ArrayableElement_Element, gen_aadl2_ComponentImplementationReference_Element, gen_aadl2_ComponentImplementation_ComponentClassifier, gen_aadl2_ArraySize_Element, gen_aadl2_ComponentClassifier_Classifier, gen_aadl2_ComponentClassifier_SubcomponentType, gen_aadl2_ComponentClassifier_FeatureClassifier, gen_aadl2_SubcomponentType_Type, gen_aadl2_ModeTransition_ModeFeature, gen_aadl2_Context_NamedElement, gen_aadl2_TriggerPort_NamedElement, gen_aadl2_ComponentType_ComponentClassifier, gen_aadl2_ModeTransitionTrigger_Element, gen_aadl2_Feature_StructuralFeature, gen_aadl2_Feature_FeatureConnectionEnd, gen_aadl2_Feature_ArrayableElement, gen_aadl2_FlowSpecification_FlowFeature, gen_aadl2_FlowSpecification_ModalPath, gen_aadl2_FlowSpecification_FlowElement, gen_aadl2_FeatureConnectionEnd_ConnectionEnd, gen_aadl2_ConnectionEnd_NamedElement, gen_aadl2_ComponentPrototype_Prototype, gen_aadl2_ComponentPrototype_SubcomponentType, gen_aadl2_ComponentPrototype_FeatureClassifier, gen_aadl2_FlowElement_EndToEndFlowElement, gen_aadl2_EndToEndFlowElement_NamedElement, gen_aadl2_FlowEnd_Element, gen_aadl2_FlowFeature_StructuralFeature, gen_aadl2_FlowFeature_Flow, gen_aadl2_Flow_NamedElement, gen_aadl2_ModalPath_ModalElement, gen_aadl2_TypeExtension_Generalization, gen_aadl2_FeatureGroup_DirectedFeature, gen_aadl2_FeatureGroup_Context, gen_aadl2_FeatureGroup_FeatureGroupConnectionEnd, gen_aadl2_FeatureGroup_CallContext, gen_aadl2_FeatureGroupConnectionEnd_ConnectionEnd, gen_aadl2_FeatureGroupType_Classifier, gen_aadl2_FeatureGroupType_FeatureType, gen_aadl2_DirectedFeature_Feature, gen_aadl2_GroupExtension_Generalization, gen_aadl2_BusAccess_Access, gen_aadl2_Access_Feature, gen_aadl2_Access_AccessConnectionEnd, gen_aadl2_AccessConnectionEnd_ConnectionEnd, gen_aadl2_ParameterConnectionEnd_ConnectionEnd, gen_aadl2_PortConnectionEnd_ConnectionEnd, gen_aadl2_DataSubcomponentType_SubcomponentType, gen_aadl2_DataSubcomponentType_AbstractFeatureClassifier, gen_aadl2_AbstractFeatureClassifier_FeatureClassifier, gen_aadl2_DataPort_Port, gen_aadl2_DataPort_Context, gen_aadl2_DataPort_ParameterConnectionEnd, gen_aadl2_Port_DirectedFeature, gen_aadl2_Port_PortConnectionEnd, gen_aadl2_Port_TriggerPort, gen_aadl2_BusFeatureClassifier_FeatureClassifier, gen_aadl2_DataAccess_Access, gen_aadl2_DataAccess_FlowElement, gen_aadl2_DataAccess_ParameterConnectionEnd, gen_aadl2_DataAccess_PortConnectionEnd, gen_aadl2_Parameter_DirectedFeature, gen_aadl2_Parameter_Context, gen_aadl2_Parameter_ParameterConnectionEnd, gen_aadl2_SubprogramAccess_Access, gen_aadl2_SubprogramAccess_Context, gen_aadl2_SubprogramAccess_CalledSubprogram, gen_aadl2_SubprogramSubcomponentType_SubcomponentType, gen_aadl2_SubprogramSubcomponentType_AbstractFeatureClassifier, gen_aadl2_SubprogramGroupAccess_Access, gen_aadl2_SubprogramGroupAccess_CallContext, gen_aadl2_SubprogramGroupSubcomponentType_SubcomponentType, gen_aadl2_SubprogramGroupSubcomponentType_AbstractFeatureClassifier, gen_aadl2_AbstractFeature_DirectedFeature, gen_aadl2_AbstractFeature_TriggerPort, gen_aadl2_EventDataPort_Port, gen_aadl2_EventDataPort_Context, gen_aadl2_EventDataPort_ParameterConnectionEnd, gen_aadl2_EventPort_Port, gen_aadl2_FeatureGroupPrototype_Prototype, gen_aadl2_FeatureGroupPrototype_FeatureType, gen_aadl2_Subcomponent_StructuralFeature, gen_aadl2_Subcomponent_ModalElement, gen_aadl2_Subcomponent_Context, gen_aadl2_Subcomponent_FlowElement, gen_aadl2_Subcomponent_ArrayableElement, gen_aadl2_FeaturePrototype_Prototype, gen_aadl2_ModeBinding_Element, gen_aadl2_FlowImplementation_ModalPath, gen_aadl2_FlowImplementation_ClassifierFeature, gen_aadl2_FlowImplementation_Flow, gen_aadl2_Connection_FlowElement, gen_aadl2_ConnectedElement_Element, gen_aadl2_ImplementationExtension_Generalization, gen_aadl2_FlowSegment_Element, gen_aadl2_Connection_StructuralFeature, gen_aadl2_Connection_ModalPath, gen_aadl2_EndToEndFlowSegment_Element, gen_aadl2_AbstractSubcomponent_Subcomponent, gen_aadl2_AbstractSubcomponent_Abstract, gen_aadl2_Abstract_NamedElement, gen_aadl2_AbstractSubcomponentType_SubcomponentType, gen_aadl2_AbstractSubcomponentType_AbstractFeatureClassifier, gen_aadl2_AccessConnection_Connection, gen_aadl2_ParameterConnection_Connection, gen_aadl2_Realization_Generalization, gen_aadl2_EndToEndFlow_FlowFeature, gen_aadl2_EndToEndFlow_ModalPath, gen_aadl2_EndToEndFlow_EndToEndFlowElement, gen_aadl2_InternalFeature_TriggerPort, gen_aadl2_EventSource_InternalFeature, gen_aadl2_EventDataSource_InternalFeature, gen_aadl2_DataClassifier_ComponentClassifier, gen_aadl2_DataClassifier_Data, gen_aadl2_DataClassifier_DataSubcomponentType, gen_aadl2_Data_NamedElement, gen_aadl2_PortProxy_ProcessorFeature, gen_aadl2_PortProxy_FeatureConnectionEnd, gen_aadl2_PortProxy_PortConnectionEnd, gen_aadl2_PortProxy_TriggerPort, gen_aadl2_PortConnection_Connection, gen_aadl2_FeatureConnection_Connection, gen_aadl2_FeatureGroupConnection_Connection, gen_aadl2_ProcessorFeature_StructuralFeature, gen_aadl2_InternalFeature_StructuralFeature, gen_aadl2_InternalFeature_FeatureConnectionEnd, gen_aadl2_InternalFeature_PortConnectionEnd, gen_aadl2_SubprogramClassifier_ComponentClassifier, gen_aadl2_SubprogramClassifier_Subprogram, gen_aadl2_SubprogramClassifier_SubprogramSubcomponentType, gen_aadl2_Subprogram_NamedElement, gen_aadl2_Subprogram_CalledSubprogram, gen_aadl2_AnnexLibrary_NamedElement, gen_aadl2_DefaultAnnexLibrary_AnnexLibrary, gen_aadl2_DefaultAnnexSubclause_AnnexSubclause, gen_aadl2_SubprogramProxy_ProcessorFeature, gen_aadl2_SubprogramProxy_AccessConnectionEnd, gen_aadl2_SubprogramProxy_CalledSubprogram, gen_aadl2_PackageRename_NamedElement, gen_aadl2_PublicPackageSection_PackageSection, gen_aadl2_PackageSection_Namespace, gen_aadl2_ModelUnit_NamedElement, gen_aadl2_PrivatePackageSection_PackageSection, gen_aadl2_ComponentTypeRename_NamedElement, gen_aadl2_FeatureGroupTypeRename_NamedElement, gen_aadl2_AadlPackage_ModelUnit, gen_aadl2_ComponentPrototypeActual_ArrayableElement, gen_aadl2_FeatureGroupPrototypeBinding_PrototypeBinding, gen_aadl2_FeatureGroupPrototypeActual_FeaturePrototypeActual, gen_aadl2_ComponentPrototypeBinding_PrototypeBinding, gen_aadl2_AccessSpecification_FeaturePrototypeActual, gen_aadl2_PortSpecification_FeaturePrototypeActual, gen_aadl2_FeaturePrototypeActual_ArrayableElement, gen_aadl2_FeaturePrototypeBinding_PrototypeBinding, gen_aadl2_SubprogramCallSequence_BehavioralFeature, gen_aadl2_SubprogramCallSequence_ModalElement, gen_aadl2_SubprogramCall_BehavioralFeature, gen_aadl2_SubprogramCall_Context, gen_aadl2_BehavioredImplementation_ComponentImplementation, gen_aadl2_AbstractType_ComponentType, gen_aadl2_FeaturePrototypeReference_FeaturePrototypeActual, gen_aadl2_AbstractClassifier_ComponentClassifier, gen_aadl2_AbstractClassifier_Abstract, gen_aadl2_AbstractClassifier_AbstractSubcomponentType, gen_aadl2_AbstractClassifier_BusSubcomponentType, gen_aadl2_AbstractClassifier_DataSubcomponentType, gen_aadl2_AbstractClassifier_DeviceSubcomponentType, gen_aadl2_AbstractClassifier_MemorySubcomponentType, gen_aadl2_AbstractClassifier_ProcessorSubcomponentType, gen_aadl2_AbstractClassifier_ProcessSubcomponentType, gen_aadl2_AbstractClassifier_SubprogramGroupSubcomponentType, gen_aadl2_AbstractClassifier_SubprogramSubcomponentType, gen_aadl2_AbstractClassifier_SystemSubcomponentType, gen_aadl2_AbstractType_AbstractClassifier, gen_aadl2_AbstractType_CallContext, gen_aadl2_VirtualBusSubcomponentType_SubcomponentType, gen_aadl2_VirtualBusSubcomponentType_AbstractFeatureClassifier, gen_aadl2_VirtualBusSubcomponentType_BusFeatureClassifier, gen_aadl2_ThreadGroupSubcomponentType_SubcomponentType, gen_aadl2_ThreadSubcomponentType_SubcomponentType, gen_aadl2_SystemSubcomponentType_SubcomponentType, gen_aadl2_ProcessSubcomponentType_SubcomponentType, gen_aadl2_MemorySubcomponentType_SubcomponentType, gen_aadl2_DeviceSubcomponentType_SubcomponentType, gen_aadl2_BusSubcomponentType_SubcomponentType, gen_aadl2_BusSubcomponentType_AbstractFeatureClassifier, gen_aadl2_BusSubcomponentType_BusFeatureClassifier, gen_aadl2_ProcessorSubcomponentType_SubcomponentType, gen_aadl2_AbstractClassifier_ThreadGroupSubcomponentType, gen_aadl2_AbstractImplementation_BehavioredImplementation, gen_aadl2_AbstractImplementation_AbstractClassifier, gen_aadl2_AbstractClassifier_ThreadSubcomponentType, gen_aadl2_AbstractClassifier_VirtualBusSubcomponentType, gen_aadl2_AbstractClassifier_VirtualProcessorSubcomponentType, gen_aadl2_VirtualProcessorSubcomponentType_SubcomponentType, gen_aadl2_BusSubcomponent_Subcomponent, gen_aadl2_BusSubcomponent_AccessConnectionEnd, gen_aadl2_BusSubcomponent_Bus, gen_aadl2_Bus_NamedElement, gen_aadl2_DataSubcomponent_Subcomponent, gen_aadl2_DataSubcomponent_AccessConnectionEnd, gen_aadl2_DataSubcomponent_Data, gen_aadl2_DataSubcomponent_ParameterConnectionEnd, gen_aadl2_DataSubcomponent_PortConnectionEnd, gen_aadl2_DeviceSubcomponent_Subcomponent, gen_aadl2_Memory_NamedElement, gen_aadl2_ProcessSubcomponent_Subcomponent, gen_aadl2_ProcessSubcomponent_Process, gen_aadl2_Process_NamedElement, gen_aadl2_ProcessorSubcomponent_Subcomponent, gen_aadl2_DeviceSubcomponent_Device, gen_aadl2_Device_NamedElement, gen_aadl2_MemorySubcomponent_Subcomponent, gen_aadl2_MemorySubcomponent_Memory, gen_aadl2_Processor_NamedElement, gen_aadl2_SystemSubcomponent_Subcomponent, gen_aadl2_SystemSubcomponent_System, gen_aadl2_System_NamedElement, gen_aadl2_SubprogramSubcomponent_Subcomponent, gen_aadl2_SubprogramSubcomponent_AccessConnectionEnd, gen_aadl2_SubprogramSubcomponent_Subprogram, gen_aadl2_ProcessorSubcomponent_Processor, gen_aadl2_SubprogramGroupSubcomponent_Subcomponent, gen_aadl2_SubprogramGroupSubcomponent_AccessConnectionEnd, gen_aadl2_SubprogramGroupSubcomponent_SubprogramGroup, gen_aadl2_SubprogramGroupSubcomponent_CallContext, gen_aadl2_SubprogramGroup_NamedElement, gen_aadl2_ThreadSubcomponent_Subcomponent, gen_aadl2_ThreadSubcomponent_Thread, gen_aadl2_VirtualBusSubcomponent_Subcomponent, gen_aadl2_VirtualBusSubcomponent_AccessConnectionEnd, gen_aadl2_VirtualBusSubcomponent_VirtualBus, gen_aadl2_VirtualBus_NamedElement, gen_aadl2_VirtualProcessorSubcomponent_Subcomponent, gen_aadl2_VirtualProcessorSubcomponent_VirtualProcessor, gen_aadl2_VirtualProcessor_NamedElement, gen_aadl2_AbstractPrototype_ComponentPrototype, gen_aadl2_AbstractPrototype_Abstract, gen_aadl2_AbstractPrototype_AbstractSubcomponentType, gen_aadl2_AbstractPrototype_BusSubcomponentType, gen_aadl2_AbstractPrototype_DataSubcomponentType, gen_aadl2_AbstractPrototype_DeviceSubcomponentType, gen_aadl2_AbstractPrototype_MemorySubcomponentType, gen_aadl2_AbstractPrototype_ProcessorSubcomponentType, gen_aadl2_AbstractPrototype_ProcessSubcomponentType, gen_aadl2_AbstractPrototype_SubprogramGroupSubcomponentType, gen_aadl2_AbstractPrototype_SubprogramSubcomponentType, gen_aadl2_AbstractPrototype_SystemSubcomponentType, gen_aadl2_AbstractPrototype_ThreadGroupSubcomponentType, gen_aadl2_AbstractPrototype_ThreadSubcomponentType, gen_aadl2_AbstractPrototype_VirtualBusSubcomponentType, gen_aadl2_AbstractPrototype_VirtualProcessorSubcomponentType, gen_aadl2_BusClassifier_ComponentClassifier, gen_aadl2_BusClassifier_Bus, gen_aadl2_BusClassifier_BusSubcomponentType, gen_aadl2_Thread_NamedElement, gen_aadl2_ThreadGroupSubcomponent_Subcomponent, gen_aadl2_ThreadGroupSubcomponent_ThreadGroup, gen_aadl2_ThreadGroup_NamedElement, gen_aadl2_BusImplementation_ComponentImplementation, gen_aadl2_BusImplementation_BusClassifier, gen_aadl2_BusPrototype_ComponentPrototype, gen_aadl2_BusPrototype_Bus, gen_aadl2_BusPrototype_BusSubcomponentType, gen_aadl2_DataType_ComponentType, gen_aadl2_DataType_DataClassifier, gen_aadl2_DataType_CallContext, gen_aadl2_BusType_ComponentType, gen_aadl2_BusType_BusClassifier, gen_aadl2_DataPrototype_ComponentPrototype, gen_aadl2_DataPrototype_Data, gen_aadl2_DataPrototype_DataSubcomponentType, gen_aadl2_DeviceClassifier_ComponentClassifier, gen_aadl2_DeviceClassifier_Device, gen_aadl2_DeviceClassifier_DeviceSubcomponentType, gen_aadl2_DeviceType_ComponentType, gen_aadl2_DeviceType_DeviceClassifier, gen_aadl2_DataImplementation_ComponentImplementation, gen_aadl2_DataImplementation_DataClassifier, gen_aadl2_DeviceImplementation_ComponentImplementation, gen_aadl2_DeviceImplementation_DeviceClassifier, gen_aadl2_DevicePrototype_ComponentPrototype, gen_aadl2_DevicePrototype_Device, gen_aadl2_DevicePrototype_DeviceSubcomponentType, gen_aadl2_MemoryClassifier_ComponentClassifier, gen_aadl2_MemoryClassifier_Memory, gen_aadl2_MemoryClassifier_MemorySubcomponentType, gen_aadl2_MemoryType_ComponentType, gen_aadl2_MemoryType_MemoryClassifier, gen_aadl2_MemoryImplementation_ComponentImplementation, gen_aadl2_MemoryImplementation_MemoryClassifier, gen_aadl2_MemoryPrototype_ComponentPrototype, gen_aadl2_MemoryPrototype_Memory, gen_aadl2_MemoryPrototype_MemorySubcomponentType, gen_aadl2_SubprogramType_ComponentType, gen_aadl2_SubprogramType_SubprogramClassifier, gen_aadl2_SubprogramType_CallContext, gen_aadl2_SubprogramImplementation_BehavioredImplementation, gen_aadl2_SubprogramImplementation_SubprogramClassifier, gen_aadl2_SubprogramPrototype_ComponentPrototype, gen_aadl2_SubprogramPrototype_Subprogram, gen_aadl2_SubprogramPrototype_SubprogramSubcomponentType, gen_aadl2_SubprogramGroupClassifier_ComponentClassifier, gen_aadl2_SubprogramGroupClassifier_SubprogramGroup, gen_aadl2_SubprogramGroupClassifier_SubprogramGroupSubcomponentType, gen_aadl2_SubprogramGroupType_ComponentType, gen_aadl2_SubprogramGroupType_SubprogramGroupClassifier, gen_aadl2_SubprogramGroupType_CallContext, gen_aadl2_SubprogramGroupPrototype_ComponentPrototype, gen_aadl2_SubprogramGroupPrototype_SubprogramGroup, gen_aadl2_SubprogramGroupPrototype_SubprogramGroupSubcomponentType, gen_aadl2_SystemClassifier_ComponentClassifier, gen_aadl2_SystemClassifier_System, gen_aadl2_SystemClassifier_SystemSubcomponentType, gen_aadl2_SystemType_ComponentType, gen_aadl2_SystemType_SystemClassifier, gen_aadl2_SubprogramGroupImplementation_ComponentImplementation, gen_aadl2_SubprogramGroupImplementation_SubprogramGroupClassifier, gen_aadl2_SystemImplementation_ComponentImplementation, gen_aadl2_SystemImplementation_SystemClassifier, gen_aadl2_SystemPrototype_ComponentPrototype, gen_aadl2_SystemPrototype_System, gen_aadl2_SystemPrototype_SystemSubcomponentType, gen_aadl2_ProcessorClassifier_ComponentClassifier, gen_aadl2_ProcessorClassifier_Processor, gen_aadl2_ProcessorClassifier_ProcessorSubcomponentType, gen_aadl2_ProcessorType_ProcessorClassifier, gen_aadl2_ProcessorType_ComponentType, gen_aadl2_ProcessorImplementation_ComponentImplementation, gen_aadl2_ProcessorImplementation_ProcessorClassifier, gen_aadl2_ProcessImplementation_ComponentImplementation, gen_aadl2_ProcessImplementation_ProcessClassifier, gen_aadl2_ProcessorPrototype_ComponentPrototype, gen_aadl2_ProcessorPrototype_Processor, gen_aadl2_ProcessorPrototype_ProcessorSubcomponentType, gen_aadl2_ProcessClassifier_ComponentClassifier, gen_aadl2_ProcessClassifier_Process, gen_aadl2_ProcessClassifier_ProcessSubcomponentType, gen_aadl2_ProcessType_ComponentType, gen_aadl2_ProcessType_ProcessClassifier, gen_aadl2_ProcessPrototype_ComponentPrototype, gen_aadl2_ProcessPrototype_Process, gen_aadl2_ProcessPrototype_ProcessSubcomponentType, gen_aadl2_ThreadClassifier_ComponentClassifier, gen_aadl2_ThreadClassifier_Thread, gen_aadl2_ThreadClassifier_ThreadSubcomponentType, gen_aadl2_ThreadType_ComponentType, gen_aadl2_ThreadType_ThreadClassifier, gen_aadl2_ThreadImplementation_BehavioredImplementation, gen_aadl2_ThreadImplementation_ThreadClassifier, gen_aadl2_ThreadPrototype_ComponentPrototype, gen_aadl2_ThreadPrototype_Thread, gen_aadl2_ThreadPrototype_ThreadSubcomponentType, gen_aadl2_ThreadGroupClassifier_ComponentClassifier, gen_aadl2_ThreadGroupClassifier_ThreadGroup, gen_aadl2_ThreadGroupClassifier_ThreadGroupSubcomponentType, gen_aadl2_ThreadGroupType_ComponentType, gen_aadl2_ThreadGroupType_ThreadGroupClassifier, gen_aadl2_ThreadGroupImplementation_ComponentImplementation, gen_aadl2_ThreadGroupImplementation_ThreadGroupClassifier, gen_aadl2_ThreadGroupPrototype_ComponentPrototype, gen_aadl2_VirtualBusType_VirtualBusClassifier, gen_aadl2_ThreadGroupPrototype_ThreadGroup, gen_aadl2_ThreadGroupPrototype_ThreadGroupSubcomponentType, gen_aadl2_VirtualBusClassifier_ComponentClassifier, gen_aadl2_VirtualBusClassifier_VirtualBus, gen_aadl2_VirtualBusClassifier_VirtualBusSubcomponentType, gen_aadl2_VirtualBusType_ComponentType, gen_aadl2_VirtualBusPrototype_ComponentPrototype, gen_aadl2_VirtualBusPrototype_VirtualBus, gen_aadl2_VirtualBusPrototype_VirtualBusSubcomponentType, gen_aadl2_VirtualProcessorClassifier_ComponentClassifier, gen_aadl2_VirtualProcessorClassifier_VirtualProcessor, gen_aadl2_VirtualProcessorClassifier_VirtualProcessorSubcomponentType, gen_aadl2_VirtualBusImplementation_ComponentImplementation, gen_aadl2_VirtualBusImplementation_VirtualBusClassifier, gen_aadl2_VirtualProcessorType_ComponentType, gen_aadl2_VirtualProcessorType_VirtualProcessorClassifier, gen_aadl2_VirtualProcessorImplementation_ComponentImplementation, gen_aadl2_VirtualProcessorImplementation_VirtualProcessorClassifier, gen_aadl2_PropertyConstant_TypedElement, gen_aadl2_PropertyConstant_AbstractNamedValue, gen_aadl2_PropertyConstant_ArraySizeProperty, gen_aadl2_VirtualProcessorPrototype_ComponentPrototype, gen_aadl2_VirtualProcessorPrototype_VirtualProcessor, gen_aadl2_VirtualProcessorPrototype_VirtualProcessorSubcomponentType, gen_aadl2_BasicPropertyAssociation_Element, gen_aadl2_StringLiteral_PropertyValue, gen_aadl2_PropertyValue_PropertyExpression, gen_aadl2_NumberValue_PropertyValue, gen_aadl2_UnitLiteral_EnumerationLiteral, gen_aadl2_EnumerationLiteral_NamedElement, gen_aadl2_EnumerationLiteral_AbstractNamedValue, gen_aadl2_ReferenceValue_ContainedNamedElement, gen_aadl2_ReferenceValue_PropertyValue, gen_aadl2_BooleanLiteral_PropertyValue, gen_aadl2_RangeValue_PropertyValue, gen_aadl2_ClassifierValue_PropertyOwner, gen_aadl2_ClassifierValue_PropertyValue, gen_aadl2_IntegerLiteral_NumberValue, gen_aadl2_RealLiteral_NumberValue, gen_aadl2_RecordValue_PropertyValue, gen_aadl2_ComputedValue_PropertyValue, gen_aadl2_Operation_PropertyExpression, gen_aadl2_NamedValue_PropertyValue, gen_aadl2_PropertySet_Namespace, gen_aadl2_PropertySet_ModelUnit, gen_aadl2_ListValue_PropertyExpression, gen_aadl2_GlobalNamespace_Namespace, gen_aadl2_AadlString_NonListType, gen_aadl2_AadlInteger_NumberType, gen_aadl2_NumberType_NonListType, gen_aadl2_NonListType_PropertyType, gen_aadl2_AadlBoolean_NonListType, gen_aadl2_EnumerationType_Namespace, gen_aadl2_EnumerationType_NonListType, gen_aadl2_NumericRange_Element, gen_aadl2_UnitsType_EnumerationType, gen_aadl2_RangeType_NonListType, gen_aadl2_AadlReal_NumberType, gen_aadl2_ClassifierType_NonListType, gen_aadl2_RecordField_BasicProperty, gen_aadl2_ReferenceType_NonListType, gen_aadl2_ListType_PropertyType, gen_aadl2_RecordType_Namespace, gen_aadl2_RecordType_NonListType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)