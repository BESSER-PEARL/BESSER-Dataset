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
            EnumerationLiteral(name="path"),
			EnumerationLiteral(name="sink"),
			EnumerationLiteral(name="source")
    }
)

DirectionType: Enumeration = Enumeration(
    name="DirectionType",
    literals={
            EnumerationLiteral(name="inOut"),
			EnumerationLiteral(name="in"),
			EnumerationLiteral(name="out")
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
			EnumerationLiteral(name="subprogramGroup")
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
aadl2_Comment = Class(name="aadl2::Comment")
Element = Class(name="Element")
aadl2_Type = Class(name="aadl2::Type", is_abstract=True)
NamedElement = Class(name="NamedElement")
aadl2_NamedElement = Class(name="aadl2::NamedElement", is_abstract=True)
aadl2_PropertyAssociation = Class(name="aadl2::PropertyAssociation")
aadl2_PropertyExpression = Class(name="aadl2::PropertyExpression", is_abstract=True)
aadl2_Property = Class(name="aadl2::Property")
aadl2_ContainedNamedElement = Class(name="aadl2::ContainedNamedElement")
aadl2_Classifier = Class(name="aadl2::Classifier", is_abstract=True)
aadl2_ModalPropertyValue = Class(name="aadl2::ModalPropertyValue")
BasicProperty = Class(name="BasicProperty")
AbstractNamedValue = Class(name="AbstractNamedValue")
ArraySizeProperty = Class(name="ArraySizeProperty")
aadl2_MetaclassReference = Class(name="aadl2::MetaclassReference")
aadl2_PropertyOwner = Class(name="aadl2::PropertyOwner", is_abstract=True)
aadl2_BasicProperty = Class(name="aadl2::BasicProperty")
TypedElement = Class(name="TypedElement")
aadl2_PropertyType = Class(name="aadl2::PropertyType", is_abstract=True)
aadl2_TypedElement = Class(name="aadl2::TypedElement", is_abstract=True)
Type = Class(name="Type")
aadl2_AbstractNamedValue = Class(name="aadl2::AbstractNamedValue", is_abstract=True)
aadl2_ArraySizeProperty = Class(name="aadl2::ArraySizeProperty", is_abstract=True)
PropertyOwner = Class(name="PropertyOwner")
Namespace = Class(name="Namespace")
aadl2_ClassifierFeature = Class(name="aadl2::ClassifierFeature", is_abstract=True)
aadl2_Generalization = Class(name="aadl2::Generalization", is_abstract=True)
aadl2_AnnexSubclause = Class(name="aadl2::AnnexSubclause", is_abstract=True)
aadl2_Prototype = Class(name="aadl2::Prototype", is_abstract=True)
aadl2_PrototypeBinding = Class(name="aadl2::PrototypeBinding", is_abstract=True)
aadl2_Namespace = Class(name="aadl2::Namespace", is_abstract=True)
ModalElement = Class(name="ModalElement")
DirectedRelationship = Class(name="DirectedRelationship")
aadl2_DirectedRelationship = Class(name="aadl2::DirectedRelationship", is_abstract=True)
Relationship = Class(name="Relationship")
aadl2_Relationship = Class(name="aadl2::Relationship", is_abstract=True)
aadl2_ModalElement = Class(name="aadl2::ModalElement")
aadl2_Mode = Class(name="aadl2::Mode")
ModeFeature = Class(name="ModeFeature")
aadl2_ModeFeature = Class(name="aadl2::ModeFeature", is_abstract=True)
ClassifierFeature = Class(name="ClassifierFeature")
StructuralFeature = Class(name="StructuralFeature")
CalledSubprogram = Class(name="CalledSubprogram")
aadl2_StructuralFeature = Class(name="aadl2::StructuralFeature", is_abstract=True)
RefinableElement = Class(name="RefinableElement")
aadl2_RefinableElement = Class(name="aadl2::RefinableElement", is_abstract=True)
aadl2_CalledSubprogram = Class(name="aadl2::CalledSubprogram", is_abstract=True)
aadl2_ContainmentPathElement = Class(name="aadl2::ContainmentPathElement")
aadl2_ArrayRange = Class(name="aadl2::ArrayRange")
aadl2_BehavioralFeature = Class(name="aadl2::BehavioralFeature", is_abstract=True)
aadl2_ArrayDimension = Class(name="aadl2::ArrayDimension")
aadl2_ArraySize = Class(name="aadl2::ArraySize")
aadl2_ArrayableElement = Class(name="aadl2::ArrayableElement", is_abstract=True)
aadl2_ComponentImplementationReference = Class(name="aadl2::ComponentImplementationReference")
aadl2_ComponentImplementation = Class(name="aadl2::ComponentImplementation", is_abstract=True)
ComponentClassifier = Class(name="ComponentClassifier")
aadl2_ComponentType = Class(name="aadl2::ComponentType", is_abstract=True)
aadl2_Subcomponent = Class(name="aadl2::Subcomponent", is_abstract=True)
aadl2_FlowImplementation = Class(name="aadl2::FlowImplementation")
aadl2_Connection = Class(name="aadl2::Connection", is_abstract=True)
aadl2_ImplementationExtension = Class(name="aadl2::ImplementationExtension")
aadl2_Realization = Class(name="aadl2::Realization")
aadl2_EndToEndFlow = Class(name="aadl2::EndToEndFlow")
aadl2_AbstractSubcomponent = Class(name="aadl2::AbstractSubcomponent")
aadl2_InternalFeature = Class(name="aadl2::InternalFeature", is_abstract=True)
aadl2_AccessConnection = Class(name="aadl2::AccessConnection")
aadl2_ParameterConnection = Class(name="aadl2::ParameterConnection")
aadl2_PortConnection = Class(name="aadl2::PortConnection")
aadl2_FeatureConnection = Class(name="aadl2::FeatureConnection")
aadl2_FeatureGroupConnection = Class(name="aadl2::FeatureGroupConnection")
aadl2_ProcessorFeature = Class(name="aadl2::ProcessorFeature", is_abstract=True)
aadl2_SubprogramProxy = Class(name="aadl2::SubprogramProxy")
aadl2_EventSource = Class(name="aadl2::EventSource")
aadl2_EventDataSource = Class(name="aadl2::EventDataSource")
aadl2_PortProxy = Class(name="aadl2::PortProxy")
aadl2_SubcomponentType = Class(name="aadl2::SubcomponentType", is_abstract=True)
aadl2_ComponentClassifier = Class(name="aadl2::ComponentClassifier", is_abstract=True)
Classifier = Class(name="Classifier")
SubcomponentType = Class(name="SubcomponentType")
FeatureClassifier = Class(name="FeatureClassifier")
aadl2_ModeTransition = Class(name="aadl2::ModeTransition")
aadl2_FeatureClassifier = Class(name="aadl2::FeatureClassifier", is_abstract=True)
aadl2_ModeTransitionTrigger = Class(name="aadl2::ModeTransitionTrigger")
aadl2_Context = Class(name="aadl2::Context", is_abstract=True)
aadl2_TriggerPort = Class(name="aadl2::TriggerPort", is_abstract=True)
aadl2_Feature = Class(name="aadl2::Feature", is_abstract=True)
aadl2_FlowSpecification = Class(name="aadl2::FlowSpecification")
aadl2_TypeExtension = Class(name="aadl2::TypeExtension")
aadl2_FeatureGroup = Class(name="aadl2::FeatureGroup")
aadl2_AbstractFeature = Class(name="aadl2::AbstractFeature")
FeatureConnectionEnd = Class(name="FeatureConnectionEnd")
ArrayableElement = Class(name="ArrayableElement")
aadl2_ComponentPrototype = Class(name="aadl2::ComponentPrototype", is_abstract=True)
aadl2_FeatureConnectionEnd = Class(name="aadl2::FeatureConnectionEnd", is_abstract=True)
ConnectionEnd = Class(name="ConnectionEnd")
aadl2_ConnectionEnd = Class(name="aadl2::ConnectionEnd", is_abstract=True)
Prototype = Class(name="Prototype")
FlowFeature = Class(name="FlowFeature")
ModalPath = Class(name="ModalPath")
FlowElement = Class(name="FlowElement")
aadl2_FlowEnd = Class(name="aadl2::FlowEnd")
aadl2_FlowFeature = Class(name="aadl2::FlowFeature", is_abstract=True)
Flow = Class(name="Flow")
aadl2_Flow = Class(name="aadl2::Flow", is_abstract=True)
aadl2_ModalPath = Class(name="aadl2::ModalPath", is_abstract=True)
aadl2_FlowElement = Class(name="aadl2::FlowElement", is_abstract=True)
EndToEndFlowElement = Class(name="EndToEndFlowElement")
aadl2_EndToEndFlowElement = Class(name="aadl2::EndToEndFlowElement", is_abstract=True)
Generalization = Class(name="Generalization")
DirectedFeature = Class(name="DirectedFeature")
Context = Class(name="Context")
FeatureGroupConnectionEnd = Class(name="FeatureGroupConnectionEnd")
CallContext = Class(name="CallContext")
aadl2_FeatureGroupConnectionEnd = Class(name="aadl2::FeatureGroupConnectionEnd", is_abstract=True)
aadl2_FeatureType = Class(name="aadl2::FeatureType", is_abstract=True)
aadl2_FeatureGroupType = Class(name="aadl2::FeatureGroupType")
aadl2_FeatureGroupPrototype = Class(name="aadl2::FeatureGroupPrototype")
aadl2_CallContext = Class(name="aadl2::CallContext", is_abstract=True)
aadl2_DirectedFeature = Class(name="aadl2::DirectedFeature", is_abstract=True)
Feature = Class(name="Feature")
aadl2_BusAccess = Class(name="aadl2::BusAccess")
FeatureType = Class(name="FeatureType")
aadl2_GroupExtension = Class(name="aadl2::GroupExtension")
aadl2_DataAccess = Class(name="aadl2::DataAccess")
aadl2_DataPort = Class(name="aadl2::DataPort")
aadl2_EventDataPort = Class(name="aadl2::EventDataPort")
aadl2_EventPort = Class(name="aadl2::EventPort")
aadl2_Access = Class(name="aadl2::Access", is_abstract=True)
AccessConnectionEnd = Class(name="AccessConnectionEnd")
aadl2_Parameter = Class(name="aadl2::Parameter")
aadl2_SubprogramAccess = Class(name="aadl2::SubprogramAccess")
aadl2_SubprogramGroupAccess = Class(name="aadl2::SubprogramGroupAccess")
Access = Class(name="Access")
Bus = Class(name="Bus")
aadl2_BusSubcomponentType = Class(name="aadl2::BusSubcomponentType", is_abstract=True)
aadl2_Data = Class(name="aadl2::Data", is_abstract=True)
aadl2_AccessConnectionEnd = Class(name="aadl2::AccessConnectionEnd", is_abstract=True)
aadl2_Bus = Class(name="aadl2::Bus", is_abstract=True)
Data = Class(name="Data")
ParameterConnectionEnd = Class(name="ParameterConnectionEnd")
PortConnectionEnd = Class(name="PortConnectionEnd")
aadl2_DataSubcomponentType = Class(name="aadl2::DataSubcomponentType", is_abstract=True)
aadl2_ParameterConnectionEnd = Class(name="aadl2::ParameterConnectionEnd", is_abstract=True)
aadl2_PortConnectionEnd = Class(name="aadl2::PortConnectionEnd", is_abstract=True)
aadl2_SubprogramSubcomponentType = Class(name="aadl2::SubprogramSubcomponentType", is_abstract=True)
Port = Class(name="Port")
aadl2_Port = Class(name="aadl2::Port", is_abstract=True)
TriggerPort = Class(name="TriggerPort")
Subprogram = Class(name="Subprogram")
aadl2_Subprogram = Class(name="aadl2::Subprogram", is_abstract=True)
SubprogramGroup = Class(name="SubprogramGroup")
aadl2_SubprogramGroupSubcomponentType = Class(name="aadl2::SubprogramGroupSubcomponentType", is_abstract=True)
aadl2_SubprogramGroup = Class(name="aadl2::SubprogramGroup", is_abstract=True)
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
DataSubcomponentType = Class(name="DataSubcomponentType")
ProcessorFeature = Class(name="ProcessorFeature")
aadl2_PublicPackageSection = Class(name="aadl2::PublicPackageSection")
PackageSection = Class(name="PackageSection")
aadl2_PrivatePackageSection = Class(name="aadl2::PrivatePackageSection")
aadl2_SubprogramClassifier = Class(name="aadl2::SubprogramClassifier", is_abstract=True)
SubprogramSubcomponentType = Class(name="SubprogramSubcomponentType")
aadl2_AnnexLibrary = Class(name="aadl2::AnnexLibrary", is_abstract=True)
aadl2_DefaultAnnexLibrary = Class(name="aadl2::DefaultAnnexLibrary")
AnnexLibrary = Class(name="AnnexLibrary")
aadl2_DefaultAnnexSubclause = Class(name="aadl2::DefaultAnnexSubclause")
AnnexSubclause = Class(name="AnnexSubclause")
aadl2_PackageSection = Class(name="aadl2::PackageSection", is_abstract=True)
aadl2_PackageRename = Class(name="aadl2::PackageRename")
aadl2_ComponentTypeRename = Class(name="aadl2::ComponentTypeRename")
aadl2_FeatureGroupTypeRename = Class(name="aadl2::FeatureGroupTypeRename")
aadl2_ModelUnit = Class(name="aadl2::ModelUnit", is_abstract=True)
aadl2_AadlPackage = Class(name="aadl2::AadlPackage")
ModelUnit = Class(name="ModelUnit")
aadl2_ComponentPrototypeBinding = Class(name="aadl2::ComponentPrototypeBinding")
PrototypeBinding = Class(name="PrototypeBinding")
aadl2_ComponentPrototypeActual = Class(name="aadl2::ComponentPrototypeActual")
aadl2_FeatureGroupPrototypeBinding = Class(name="aadl2::FeatureGroupPrototypeBinding")
aadl2_FeatureGroupPrototypeActual = Class(name="aadl2::FeatureGroupPrototypeActual")
FeaturePrototypeActual = Class(name="FeaturePrototypeActual")
aadl2_FeaturePrototypeReference = Class(name="aadl2::FeaturePrototypeReference")
aadl2_FeaturePrototypeActual = Class(name="aadl2::FeaturePrototypeActual", is_abstract=True)
aadl2_FeaturePrototypeBinding = Class(name="aadl2::FeaturePrototypeBinding")
aadl2_AccessSpecification = Class(name="aadl2::AccessSpecification")
aadl2_PortSpecification = Class(name="aadl2::PortSpecification")
aadl2_SubprogramCallSequence = Class(name="aadl2::SubprogramCallSequence")
BehavioralFeature = Class(name="BehavioralFeature")
aadl2_SubprogramCall = Class(name="aadl2::SubprogramCall")
aadl2_BehavioredImplementation = Class(name="aadl2::BehavioredImplementation", is_abstract=True)
ComponentImplementation = Class(name="ComponentImplementation")
aadl2_AbstractType = Class(name="aadl2::AbstractType")
ComponentType = Class(name="ComponentType")
AbstractClassifier = Class(name="AbstractClassifier")
aadl2_VirtualProcessor = Class(name="aadl2::VirtualProcessor", is_abstract=True)
aadl2_VirtualBusSubcomponentType = Class(name="aadl2::VirtualBusSubcomponentType", is_abstract=True)
VirtualBus = Class(name="VirtualBus")
aadl2_VirtualBus = Class(name="aadl2::VirtualBus", is_abstract=True)
aadl2_AbstractClassifier = Class(name="aadl2::AbstractClassifier", is_abstract=True)
AbstractSubcomponentType = Class(name="AbstractSubcomponentType")
BusSubcomponentType = Class(name="BusSubcomponentType")
DeviceSubcomponentType = Class(name="DeviceSubcomponentType")
MemorySubcomponentType = Class(name="MemorySubcomponentType")
ProcessorSubcomponentType = Class(name="ProcessorSubcomponentType")
ProcessSubcomponentType = Class(name="ProcessSubcomponentType")
SubprogramGroupSubcomponentType = Class(name="SubprogramGroupSubcomponentType")
SystemSubcomponentType = Class(name="SystemSubcomponentType")
ThreadGroupSubcomponentType = Class(name="ThreadGroupSubcomponentType")
ThreadSubcomponentType = Class(name="ThreadSubcomponentType")
VirtualBusSubcomponentType = Class(name="VirtualBusSubcomponentType")
VirtualProcessorSubcomponentType = Class(name="VirtualProcessorSubcomponentType")
aadl2_VirtualProcessorSubcomponentType = Class(name="aadl2::VirtualProcessorSubcomponentType", is_abstract=True)
VirtualProcessor = Class(name="VirtualProcessor")
aadl2_AbstractImplementation = Class(name="aadl2::AbstractImplementation")
BehavioredImplementation = Class(name="BehavioredImplementation")
aadl2_ThreadGroupSubcomponentType = Class(name="aadl2::ThreadGroupSubcomponentType", is_abstract=True)
aadl2_BusSubcomponent = Class(name="aadl2::BusSubcomponent")
ThreadGroup = Class(name="ThreadGroup")
aadl2_ThreadGroup = Class(name="aadl2::ThreadGroup", is_abstract=True)
aadl2_ThreadSubcomponentType = Class(name="aadl2::ThreadSubcomponentType", is_abstract=True)
Thread = Class(name="Thread")
aadl2_Thread = Class(name="aadl2::Thread", is_abstract=True)
aadl2_SystemSubcomponentType = Class(name="aadl2::SystemSubcomponentType", is_abstract=True)
System = Class(name="System")
aadl2_System = Class(name="aadl2::System", is_abstract=True)
aadl2_ProcessSubcomponentType = Class(name="aadl2::ProcessSubcomponentType", is_abstract=True)
Process = Class(name="Process")
aadl2_Process = Class(name="aadl2::Process", is_abstract=True)
aadl2_MemorySubcomponentType = Class(name="aadl2::MemorySubcomponentType", is_abstract=True)
Memory = Class(name="Memory")
aadl2_Memory = Class(name="aadl2::Memory", is_abstract=True)
aadl2_DeviceSubcomponentType = Class(name="aadl2::DeviceSubcomponentType", is_abstract=True)
Device = Class(name="Device")
aadl2_Device = Class(name="aadl2::Device", is_abstract=True)
aadl2_ProcessorSubcomponentType = Class(name="aadl2::ProcessorSubcomponentType", is_abstract=True)
Processor = Class(name="Processor")
aadl2_Processor = Class(name="aadl2::Processor", is_abstract=True)
aadl2_ThreadSubcomponent = Class(name="aadl2::ThreadSubcomponent")
aadl2_ThreadGroupSubcomponent = Class(name="aadl2::ThreadGroupSubcomponent")
aadl2_DataSubcomponent = Class(name="aadl2::DataSubcomponent")
aadl2_DeviceSubcomponent = Class(name="aadl2::DeviceSubcomponent")
aadl2_MemorySubcomponent = Class(name="aadl2::MemorySubcomponent")
aadl2_ProcessSubcomponent = Class(name="aadl2::ProcessSubcomponent")
aadl2_ProcessorSubcomponent = Class(name="aadl2::ProcessorSubcomponent")
aadl2_SystemSubcomponent = Class(name="aadl2::SystemSubcomponent")
aadl2_SubprogramSubcomponent = Class(name="aadl2::SubprogramSubcomponent")
aadl2_SubprogramGroupSubcomponent = Class(name="aadl2::SubprogramGroupSubcomponent")
aadl2_VirtualBusSubcomponent = Class(name="aadl2::VirtualBusSubcomponent")
aadl2_VirtualProcessorSubcomponent = Class(name="aadl2::VirtualProcessorSubcomponent")
aadl2_AbstractPrototype = Class(name="aadl2::AbstractPrototype")
ComponentPrototype = Class(name="ComponentPrototype")
aadl2_BusClassifier = Class(name="aadl2::BusClassifier", is_abstract=True)
aadl2_BusType = Class(name="aadl2::BusType")
BusClassifier = Class(name="BusClassifier")
aadl2_DataImplementation = Class(name="aadl2::DataImplementation")
aadl2_BusImplementation = Class(name="aadl2::BusImplementation")
aadl2_BusPrototype = Class(name="aadl2::BusPrototype")
aadl2_DataType = Class(name="aadl2::DataType")
DataClassifier = Class(name="DataClassifier")
aadl2_DeviceImplementation = Class(name="aadl2::DeviceImplementation")
aadl2_DataPrototype = Class(name="aadl2::DataPrototype")
aadl2_DeviceClassifier = Class(name="aadl2::DeviceClassifier", is_abstract=True)
aadl2_DeviceType = Class(name="aadl2::DeviceType")
DeviceClassifier = Class(name="DeviceClassifier")
aadl2_DevicePrototype = Class(name="aadl2::DevicePrototype")
aadl2_MemoryClassifier = Class(name="aadl2::MemoryClassifier", is_abstract=True)
aadl2_MemoryType = Class(name="aadl2::MemoryType")
MemoryClassifier = Class(name="MemoryClassifier")
aadl2_MemoryPrototype = Class(name="aadl2::MemoryPrototype")
aadl2_SubprogramType = Class(name="aadl2::SubprogramType")
SubprogramClassifier = Class(name="SubprogramClassifier")
aadl2_MemoryImplementation = Class(name="aadl2::MemoryImplementation")
aadl2_SubprogramGroupType = Class(name="aadl2::SubprogramGroupType")
SubprogramGroupClassifier = Class(name="SubprogramGroupClassifier")
aadl2_SubprogramGroupImplementation = Class(name="aadl2::SubprogramGroupImplementation")
aadl2_SubprogramImplementation = Class(name="aadl2::SubprogramImplementation")
aadl2_SubprogramPrototype = Class(name="aadl2::SubprogramPrototype")
aadl2_SubprogramGroupClassifier = Class(name="aadl2::SubprogramGroupClassifier", is_abstract=True)
aadl2_SubprogramGroupPrototype = Class(name="aadl2::SubprogramGroupPrototype")
aadl2_SystemClassifier = Class(name="aadl2::SystemClassifier", is_abstract=True)
aadl2_SystemType = Class(name="aadl2::SystemType")
SystemClassifier = Class(name="SystemClassifier")
aadl2_SystemImplementation = Class(name="aadl2::SystemImplementation")
aadl2_ProcessorClassifier = Class(name="aadl2::ProcessorClassifier", is_abstract=True)
aadl2_ProcessorType = Class(name="aadl2::ProcessorType")
ProcessorClassifier = Class(name="ProcessorClassifier")
aadl2_SystemPrototype = Class(name="aadl2::SystemPrototype")
aadl2_ProcessorPrototype = Class(name="aadl2::ProcessorPrototype")
aadl2_ProcessClassifier = Class(name="aadl2::ProcessClassifier", is_abstract=True)
aadl2_ProcessorImplementation = Class(name="aadl2::ProcessorImplementation")
aadl2_ProcessImplementation = Class(name="aadl2::ProcessImplementation")
aadl2_ProcessType = Class(name="aadl2::ProcessType")
ProcessClassifier = Class(name="ProcessClassifier")
aadl2_ThreadPrototype = Class(name="aadl2::ThreadPrototype")
aadl2_ProcessPrototype = Class(name="aadl2::ProcessPrototype")
aadl2_ThreadClassifier = Class(name="aadl2::ThreadClassifier", is_abstract=True)
aadl2_ThreadType = Class(name="aadl2::ThreadType")
ThreadClassifier = Class(name="ThreadClassifier")
aadl2_ThreadImplementation = Class(name="aadl2::ThreadImplementation")
aadl2_ThreadGroupClassifier = Class(name="aadl2::ThreadGroupClassifier", is_abstract=True)
aadl2_ThreadGroupType = Class(name="aadl2::ThreadGroupType")
ThreadGroupClassifier = Class(name="ThreadGroupClassifier")
aadl2_ThreadGroupImplementation = Class(name="aadl2::ThreadGroupImplementation")
aadl2_VirtualBusImplementation = Class(name="aadl2::VirtualBusImplementation")
aadl2_ThreadGroupPrototype = Class(name="aadl2::ThreadGroupPrototype")
aadl2_VirtualBusClassifier = Class(name="aadl2::VirtualBusClassifier", is_abstract=True)
aadl2_VirtualBusType = Class(name="aadl2::VirtualBusType")
VirtualBusClassifier = Class(name="VirtualBusClassifier")
aadl2_VirtualProcessorImplementation = Class(name="aadl2::VirtualProcessorImplementation")
aadl2_VirtualBusPrototype = Class(name="aadl2::VirtualBusPrototype")
aadl2_VirtualProcessorClassifier = Class(name="aadl2::VirtualProcessorClassifier", is_abstract=True)
aadl2_VirtualProcessorType = Class(name="aadl2::VirtualProcessorType")
VirtualProcessorClassifier = Class(name="VirtualProcessorClassifier")
aadl2_StringLiteral = Class(name="aadl2::StringLiteral")
PropertyValue = Class(name="PropertyValue")
aadl2_VirtualProcessorPrototype = Class(name="aadl2::VirtualProcessorPrototype")
aadl2_BasicPropertyAssociation = Class(name="aadl2::BasicPropertyAssociation")
aadl2_PropertyConstant = Class(name="aadl2::PropertyConstant")
aadl2_ReferenceValue = Class(name="aadl2::ReferenceValue")
ContainedNamedElement = Class(name="ContainedNamedElement")
aadl2_PropertyValue = Class(name="aadl2::PropertyValue", is_abstract=True)
PropertyExpression = Class(name="PropertyExpression")
aadl2_NumberValue = Class(name="aadl2::NumberValue", is_abstract=True)
aadl2_UnitLiteral = Class(name="aadl2::UnitLiteral")
EnumerationLiteral = Class(name="EnumerationLiteral")
aadl2_EnumerationLiteral = Class(name="aadl2::EnumerationLiteral")
aadl2_ClassifierValue = Class(name="aadl2::ClassifierValue")
aadl2_BooleanLiteral = Class(name="aadl2::BooleanLiteral")
aadl2_RangeValue = Class(name="aadl2::RangeValue")
aadl2_IntegerLiteral = Class(name="aadl2::IntegerLiteral")
NumberValue = Class(name="NumberValue")
aadl2_RealLiteral = Class(name="aadl2::RealLiteral")
aadl2_Operation = Class(name="aadl2::Operation")
aadl2_RecordValue = Class(name="aadl2::RecordValue")
aadl2_ComputedValue = Class(name="aadl2::ComputedValue")
aadl2_ListValue = Class(name="aadl2::ListValue")
aadl2_NamedValue = Class(name="aadl2::NamedValue")
aadl2_PropertySet = Class(name="aadl2::PropertySet")
aadl2_NonListType = Class(name="aadl2::NonListType", is_abstract=True)
aadl2_GlobalNamespace = Class(name="aadl2::GlobalNamespace")
aadl2_NumericRange = Class(name="aadl2::NumericRange")
PropertyType = Class(name="PropertyType")
aadl2_AadlBoolean = Class(name="aadl2::AadlBoolean")
NonListType = Class(name="NonListType")
aadl2_AadlString = Class(name="aadl2::AadlString")
aadl2_AadlInteger = Class(name="aadl2::AadlInteger")
NumberType = Class(name="NumberType")
aadl2_NumberType = Class(name="aadl2::NumberType", is_abstract=True)
aadl2_UnitsType = Class(name="aadl2::UnitsType")
aadl2_AadlReal = Class(name="aadl2::AadlReal")
EnumerationType = Class(name="EnumerationType")
aadl2_EnumerationType = Class(name="aadl2::EnumerationType")
aadl2_ClassifierType = Class(name="aadl2::ClassifierType")
aadl2_RangeType = Class(name="aadl2::RangeType")
aadl2_RecordType = Class(name="aadl2::RecordType")
aadl2_RecordField = Class(name="aadl2::RecordField")
aadl2_ReferenceType = Class(name="aadl2::ReferenceType")
aadl2_ListType = Class(name="aadl2::ListType")

# aadl2_Element class attributes and methods
aadl2_Element_m_not_own_self: Method = Method(name="not_own_self", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
aadl2_Element_m_has_owner: Method = Method(name="has_owner", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
aadl2_Element_m_getOwner: Method = Method(name="getOwner", parameters={}, type=StringType)
aadl2_Element_m_allOwnedElements: Method = Method(name="allOwnedElements", parameters={}, type=StringType)
aadl2_Element_m_mustBeOwned: Method = Method(name="mustBeOwned", parameters={}, type=StringType)
aadl2_Element.methods={aadl2_Element_m_mustBeOwned, aadl2_Element_m_has_owner, aadl2_Element_m_allOwnedElements, aadl2_Element_m_not_own_self, aadl2_Element_m_getOwner}

# aadl2_Comment class attributes and methods
aadl2_Comment_body: Property = Property(name="body", type=StringType)
aadl2_Comment.attributes={aadl2_Comment_body}

# Element class attributes and methods

# aadl2_Type class attributes and methods
aadl2_Type_m_conformsTo: Method = Method(name="conformsTo", parameters={Parameter(name='other')}, type=StringType)
aadl2_Type.methods={aadl2_Type_m_conformsTo}

# NamedElement class attributes and methods

# aadl2_NamedElement class attributes and methods
aadl2_NamedElement_name: Property = Property(name="name", type=StringType)
aadl2_NamedElement_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
aadl2_NamedElement_m_has_no_qualified_name: Method = Method(name="has_no_qualified_name", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
aadl2_NamedElement_m_has_qualified_name: Method = Method(name="has_qualified_name", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
aadl2_NamedElement_m_qualifiedName: Method = Method(name="qualifiedName", parameters={}, type=StringType)
aadl2_NamedElement_m_getNamespace: Method = Method(name="getNamespace", parameters={}, type=StringType)
aadl2_NamedElement_m_allNamespaces: Method = Method(name="allNamespaces", parameters={}, type=StringType)
aadl2_NamedElement_m_isDistinguishableFrom: Method = Method(name="isDistinguishableFrom", parameters={Parameter(name='n'), Parameter(name='ns')}, type=StringType)
aadl2_NamedElement_m_separator: Method = Method(name="separator", parameters={}, type=StringType)
aadl2_NamedElement_m_getPropertyValues: Method = Method(name="getPropertyValues", parameters={Parameter(name='propertyName'), Parameter(name='propertySetName')}, type=StringType)
aadl2_NamedElement.attributes={aadl2_NamedElement_name, aadl2_NamedElement_qualifiedName}
aadl2_NamedElement.methods={aadl2_NamedElement_m_has_no_qualified_name, aadl2_NamedElement_m_has_qualified_name, aadl2_NamedElement_m_allNamespaces, aadl2_NamedElement_m_separator, aadl2_NamedElement_m_isDistinguishableFrom, aadl2_NamedElement_m_qualifiedName, aadl2_NamedElement_m_getPropertyValues, aadl2_NamedElement_m_getNamespace}

# aadl2_PropertyAssociation class attributes and methods
aadl2_PropertyAssociation_append: Property = Property(name="append", type=StringType)
aadl2_PropertyAssociation_constant: Property = Property(name="constant", type=StringType)
aadl2_PropertyAssociation.attributes={aadl2_PropertyAssociation_constant, aadl2_PropertyAssociation_append}

# aadl2_PropertyExpression class attributes and methods

# aadl2_Property class attributes and methods
aadl2_Property_inherit: Property = Property(name="inherit", type=StringType)
aadl2_Property_emptyListDefault: Property = Property(name="emptyListDefault", type=StringType)
aadl2_Property.attributes={aadl2_Property_emptyListDefault, aadl2_Property_inherit}

# aadl2_ContainedNamedElement class attributes and methods

# aadl2_Classifier class attributes and methods
aadl2_Classifier_noAnnexes: Property = Property(name="noAnnexes", type=StringType)
aadl2_Classifier_noPrototypes: Property = Property(name="noPrototypes", type=StringType)
aadl2_Classifier_noProperties: Property = Property(name="noProperties", type=StringType)
aadl2_Classifier_m_allFeatures: Method = Method(name="allFeatures", parameters={}, type=StringType)
aadl2_Classifier_m_no_cycles_in_generalization: Method = Method(name="no_cycles_in_generalization", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
aadl2_Classifier_m_specialize_type: Method = Method(name="specialize_type", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
aadl2_Classifier_m_inheritedMember: Method = Method(name="inheritedMember", parameters={}, type=NamedElement)
aadl2_Classifier_m_parents: Method = Method(name="parents", parameters={}, type=StringType)
aadl2_Classifier_m_allParents: Method = Method(name="allParents", parameters={}, type=StringType)
aadl2_Classifier_m_inheritableMembers: Method = Method(name="inheritableMembers", parameters={Parameter(name='c')}, type=NamedElement)
aadl2_Classifier_m_hasVisibilityOf: Method = Method(name="hasVisibilityOf", parameters={Parameter(name='n')}, type=StringType)
aadl2_Classifier_m_inherit: Method = Method(name="inherit", parameters={Parameter(name='inhs')}, type=NamedElement)
aadl2_Classifier_m_maySpecializeType: Method = Method(name="maySpecializeType", parameters={Parameter(name='c')}, type=StringType)
aadl2_Classifier.attributes={aadl2_Classifier_noPrototypes, aadl2_Classifier_noProperties, aadl2_Classifier_noAnnexes}
aadl2_Classifier.methods={aadl2_Classifier_m_allFeatures, aadl2_Classifier_m_hasVisibilityOf, aadl2_Classifier_m_parents, aadl2_Classifier_m_no_cycles_in_generalization, aadl2_Classifier_m_inheritedMember, aadl2_Classifier_m_allParents, aadl2_Classifier_m_inherit, aadl2_Classifier_m_specialize_type, aadl2_Classifier_m_inheritableMembers, aadl2_Classifier_m_maySpecializeType}

# aadl2_ModalPropertyValue class attributes and methods

# BasicProperty class attributes and methods

# AbstractNamedValue class attributes and methods

# ArraySizeProperty class attributes and methods

# aadl2_MetaclassReference class attributes and methods
aadl2_MetaclassReference_annexName: Property = Property(name="annexName", type=StringType)
aadl2_MetaclassReference_metaclassName: Property = Property(name="metaclassName", type=StringType)
aadl2_MetaclassReference.attributes={aadl2_MetaclassReference_metaclassName, aadl2_MetaclassReference_annexName}

# aadl2_PropertyOwner class attributes and methods

# aadl2_BasicProperty class attributes and methods

# TypedElement class attributes and methods

# aadl2_PropertyType class attributes and methods

# aadl2_TypedElement class attributes and methods

# Type class attributes and methods

# aadl2_AbstractNamedValue class attributes and methods

# aadl2_ArraySizeProperty class attributes and methods

# PropertyOwner class attributes and methods

# Namespace class attributes and methods

# aadl2_ClassifierFeature class attributes and methods

# aadl2_Generalization class attributes and methods

# aadl2_AnnexSubclause class attributes and methods

# aadl2_Prototype class attributes and methods
aadl2_Prototype_m_categoryConstraint: Method = Method(name="categoryConstraint", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
aadl2_Prototype.methods={aadl2_Prototype_m_categoryConstraint}

# aadl2_PrototypeBinding class attributes and methods

# aadl2_Namespace class attributes and methods
aadl2_Namespace_m_members_distinguishable: Method = Method(name="members_distinguishable", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
aadl2_Namespace_m_getNamesOfMember: Method = Method(name="getNamesOfMember", parameters={Parameter(name='element')}, type=StringType)
aadl2_Namespace_m_membersAreDistinguishable: Method = Method(name="membersAreDistinguishable", parameters={}, type=StringType)
aadl2_Namespace.methods={aadl2_Namespace_m_members_distinguishable, aadl2_Namespace_m_membersAreDistinguishable, aadl2_Namespace_m_getNamesOfMember}

# ModalElement class attributes and methods

# DirectedRelationship class attributes and methods

# aadl2_DirectedRelationship class attributes and methods

# Relationship class attributes and methods

# aadl2_Relationship class attributes and methods

# aadl2_ModalElement class attributes and methods
aadl2_ModalElement_m_getAllInModes: Method = Method(name="getAllInModes", parameters={}, type=StringType)
aadl2_ModalElement.methods={aadl2_ModalElement_m_getAllInModes}

# aadl2_Mode class attributes and methods
aadl2_Mode_initial: Property = Property(name="initial", type=StringType)
aadl2_Mode_derived: Property = Property(name="derived", type=StringType)
aadl2_Mode.attributes={aadl2_Mode_derived, aadl2_Mode_initial}

# ModeFeature class attributes and methods

# aadl2_ModeFeature class attributes and methods

# ClassifierFeature class attributes and methods

# StructuralFeature class attributes and methods

# CalledSubprogram class attributes and methods

# aadl2_StructuralFeature class attributes and methods

# RefinableElement class attributes and methods

# aadl2_RefinableElement class attributes and methods

# aadl2_CalledSubprogram class attributes and methods

# aadl2_ContainmentPathElement class attributes and methods
aadl2_ContainmentPathElement_annexName: Property = Property(name="annexName", type=StringType)
aadl2_ContainmentPathElement.attributes={aadl2_ContainmentPathElement_annexName}

# aadl2_ArrayRange class attributes and methods
aadl2_ArrayRange_lowerBound: Property = Property(name="lowerBound", type=StringType)
aadl2_ArrayRange_upperBound: Property = Property(name="upperBound", type=StringType)
aadl2_ArrayRange.attributes={aadl2_ArrayRange_lowerBound, aadl2_ArrayRange_upperBound}

# aadl2_BehavioralFeature class attributes and methods

# aadl2_ArrayDimension class attributes and methods

# aadl2_ArraySize class attributes and methods
aadl2_ArraySize_size: Property = Property(name="size", type=StringType)
aadl2_ArraySize.attributes={aadl2_ArraySize_size}

# aadl2_ArrayableElement class attributes and methods

# aadl2_ComponentImplementationReference class attributes and methods

# aadl2_ComponentImplementation class attributes and methods
aadl2_ComponentImplementation_noSubcomponents: Property = Property(name="noSubcomponents", type=StringType)
aadl2_ComponentImplementation_noConnections: Property = Property(name="noConnections", type=StringType)
aadl2_ComponentImplementation_noCalls: Property = Property(name="noCalls", type=StringType)
aadl2_ComponentImplementation_m_getAllSubcomponents: Method = Method(name="getAllSubcomponents", parameters={}, type=StringType)
aadl2_ComponentImplementation.attributes={aadl2_ComponentImplementation_noCalls, aadl2_ComponentImplementation_noConnections, aadl2_ComponentImplementation_noSubcomponents}
aadl2_ComponentImplementation.methods={aadl2_ComponentImplementation_m_getAllSubcomponents}

# ComponentClassifier class attributes and methods

# aadl2_ComponentType class attributes and methods
aadl2_ComponentType_noFeatures: Property = Property(name="noFeatures", type=StringType)
aadl2_ComponentType.attributes={aadl2_ComponentType_noFeatures}

# aadl2_Subcomponent class attributes and methods
aadl2_Subcomponent_allModes: Property = Property(name="allModes", type=StringType)
aadl2_Subcomponent.attributes={aadl2_Subcomponent_allModes}

# aadl2_FlowImplementation class attributes and methods
aadl2_FlowImplementation_kind: Property = Property(name="kind", type=StringType)
aadl2_FlowImplementation.attributes={aadl2_FlowImplementation_kind}

# aadl2_Connection class attributes and methods
aadl2_Connection_bidirectional: Property = Property(name="bidirectional", type=StringType)
aadl2_Connection.attributes={aadl2_Connection_bidirectional}

# aadl2_ImplementationExtension class attributes and methods

# aadl2_Realization class attributes and methods

# aadl2_EndToEndFlow class attributes and methods

# aadl2_AbstractSubcomponent class attributes and methods

# aadl2_InternalFeature class attributes and methods
aadl2_InternalFeature_direction: Property = Property(name="direction", type=StringType)
aadl2_InternalFeature.attributes={aadl2_InternalFeature_direction}

# aadl2_AccessConnection class attributes and methods
aadl2_AccessConnection_accessCategory: Property = Property(name="accessCategory", type=StringType)
aadl2_AccessConnection.attributes={aadl2_AccessConnection_accessCategory}

# aadl2_ParameterConnection class attributes and methods

# aadl2_PortConnection class attributes and methods

# aadl2_FeatureConnection class attributes and methods

# aadl2_FeatureGroupConnection class attributes and methods

# aadl2_ProcessorFeature class attributes and methods

# aadl2_SubprogramProxy class attributes and methods

# aadl2_EventSource class attributes and methods

# aadl2_EventDataSource class attributes and methods

# aadl2_PortProxy class attributes and methods
aadl2_PortProxy_direction: Property = Property(name="direction", type=StringType)
aadl2_PortProxy.attributes={aadl2_PortProxy_direction}

# aadl2_SubcomponentType class attributes and methods

# aadl2_ComponentClassifier class attributes and methods
aadl2_ComponentClassifier_derivedModes: Property = Property(name="derivedModes", type=StringType)
aadl2_ComponentClassifier_noFlows: Property = Property(name="noFlows", type=StringType)
aadl2_ComponentClassifier_noModes: Property = Property(name="noModes", type=StringType)
aadl2_ComponentClassifier.attributes={aadl2_ComponentClassifier_noFlows, aadl2_ComponentClassifier_derivedModes, aadl2_ComponentClassifier_noModes}

# Classifier class attributes and methods

# SubcomponentType class attributes and methods

# FeatureClassifier class attributes and methods

# aadl2_ModeTransition class attributes and methods

# aadl2_FeatureClassifier class attributes and methods

# aadl2_ModeTransitionTrigger class attributes and methods

# aadl2_Context class attributes and methods

# aadl2_TriggerPort class attributes and methods

# aadl2_Feature class attributes and methods

# aadl2_FlowSpecification class attributes and methods
aadl2_FlowSpecification_kind: Property = Property(name="kind", type=StringType)
aadl2_FlowSpecification.attributes={aadl2_FlowSpecification_kind}

# aadl2_TypeExtension class attributes and methods

# aadl2_FeatureGroup class attributes and methods
aadl2_FeatureGroup_inverse: Property = Property(name="inverse", type=StringType)
aadl2_FeatureGroup.attributes={aadl2_FeatureGroup_inverse}

# aadl2_AbstractFeature class attributes and methods

# FeatureConnectionEnd class attributes and methods

# ArrayableElement class attributes and methods

# aadl2_ComponentPrototype class attributes and methods
aadl2_ComponentPrototype_array: Property = Property(name="array", type=StringType)
aadl2_ComponentPrototype.attributes={aadl2_ComponentPrototype_array}

# aadl2_FeatureConnectionEnd class attributes and methods

# ConnectionEnd class attributes and methods

# aadl2_ConnectionEnd class attributes and methods

# Prototype class attributes and methods

# FlowFeature class attributes and methods

# ModalPath class attributes and methods

# FlowElement class attributes and methods

# aadl2_FlowEnd class attributes and methods

# aadl2_FlowFeature class attributes and methods

# Flow class attributes and methods

# aadl2_Flow class attributes and methods

# aadl2_ModalPath class attributes and methods
aadl2_ModalPath_m_getInModes: Method = Method(name="getInModes", parameters={}, type=StringType)
aadl2_ModalPath_m_getInModeTransitions: Method = Method(name="getInModeTransitions", parameters={}, type=StringType)
aadl2_ModalPath_m_getAllInModeTransitions: Method = Method(name="getAllInModeTransitions", parameters={}, type=StringType)
aadl2_ModalPath.methods={aadl2_ModalPath_m_getInModes, aadl2_ModalPath_m_getAllInModeTransitions, aadl2_ModalPath_m_getInModeTransitions}

# aadl2_FlowElement class attributes and methods

# EndToEndFlowElement class attributes and methods

# aadl2_EndToEndFlowElement class attributes and methods

# Generalization class attributes and methods

# DirectedFeature class attributes and methods

# Context class attributes and methods

# FeatureGroupConnectionEnd class attributes and methods

# CallContext class attributes and methods

# aadl2_FeatureGroupConnectionEnd class attributes and methods

# aadl2_FeatureType class attributes and methods

# aadl2_FeatureGroupType class attributes and methods

# aadl2_FeatureGroupPrototype class attributes and methods

# aadl2_CallContext class attributes and methods

# aadl2_DirectedFeature class attributes and methods
aadl2_DirectedFeature_direction: Property = Property(name="direction", type=StringType)
aadl2_DirectedFeature.attributes={aadl2_DirectedFeature_direction}

# Feature class attributes and methods

# aadl2_BusAccess class attributes and methods

# FeatureType class attributes and methods

# aadl2_GroupExtension class attributes and methods

# aadl2_DataAccess class attributes and methods

# aadl2_DataPort class attributes and methods

# aadl2_EventDataPort class attributes and methods

# aadl2_EventPort class attributes and methods

# aadl2_Access class attributes and methods
aadl2_Access_kind: Property = Property(name="kind", type=StringType)
aadl2_Access_category: Property = Property(name="category", type=StringType)
aadl2_Access.attributes={aadl2_Access_kind, aadl2_Access_category}

# AccessConnectionEnd class attributes and methods

# aadl2_Parameter class attributes and methods

# aadl2_SubprogramAccess class attributes and methods

# aadl2_SubprogramGroupAccess class attributes and methods

# Access class attributes and methods

# Bus class attributes and methods

# aadl2_BusSubcomponentType class attributes and methods

# aadl2_Data class attributes and methods

# aadl2_AccessConnectionEnd class attributes and methods

# aadl2_Bus class attributes and methods

# Data class attributes and methods

# ParameterConnectionEnd class attributes and methods

# PortConnectionEnd class attributes and methods

# aadl2_DataSubcomponentType class attributes and methods

# aadl2_ParameterConnectionEnd class attributes and methods

# aadl2_PortConnectionEnd class attributes and methods

# aadl2_SubprogramSubcomponentType class attributes and methods

# Port class attributes and methods

# aadl2_Port class attributes and methods
aadl2_Port_category: Property = Property(name="category", type=StringType)
aadl2_Port.attributes={aadl2_Port_category}

# TriggerPort class attributes and methods

# Subprogram class attributes and methods

# aadl2_Subprogram class attributes and methods

# SubprogramGroup class attributes and methods

# aadl2_SubprogramGroupSubcomponentType class attributes and methods

# aadl2_SubprogramGroup class attributes and methods

# aadl2_FeaturePrototype class attributes and methods
aadl2_FeaturePrototype_direction: Property = Property(name="direction", type=StringType)
aadl2_FeaturePrototype.attributes={aadl2_FeaturePrototype_direction}

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

# DataSubcomponentType class attributes and methods

# ProcessorFeature class attributes and methods

# aadl2_PublicPackageSection class attributes and methods

# PackageSection class attributes and methods

# aadl2_PrivatePackageSection class attributes and methods

# aadl2_SubprogramClassifier class attributes and methods

# SubprogramSubcomponentType class attributes and methods

# aadl2_AnnexLibrary class attributes and methods

# aadl2_DefaultAnnexLibrary class attributes and methods
aadl2_DefaultAnnexLibrary_sourceText: Property = Property(name="sourceText", type=StringType)
aadl2_DefaultAnnexLibrary.attributes={aadl2_DefaultAnnexLibrary_sourceText}

# AnnexLibrary class attributes and methods

# aadl2_DefaultAnnexSubclause class attributes and methods
aadl2_DefaultAnnexSubclause_sourceText: Property = Property(name="sourceText", type=StringType)
aadl2_DefaultAnnexSubclause.attributes={aadl2_DefaultAnnexSubclause_sourceText}

# AnnexSubclause class attributes and methods

# aadl2_PackageSection class attributes and methods
aadl2_PackageSection_noAnnexes: Property = Property(name="noAnnexes", type=StringType)
aadl2_PackageSection_noProperties: Property = Property(name="noProperties", type=StringType)
aadl2_PackageSection.attributes={aadl2_PackageSection_noAnnexes, aadl2_PackageSection_noProperties}

# aadl2_PackageRename class attributes and methods
aadl2_PackageRename_renameAll: Property = Property(name="renameAll", type=StringType)
aadl2_PackageRename.attributes={aadl2_PackageRename_renameAll}

# aadl2_ComponentTypeRename class attributes and methods
aadl2_ComponentTypeRename_category: Property = Property(name="category", type=StringType)
aadl2_ComponentTypeRename.attributes={aadl2_ComponentTypeRename_category}

# aadl2_FeatureGroupTypeRename class attributes and methods

# aadl2_ModelUnit class attributes and methods

# aadl2_AadlPackage class attributes and methods

# ModelUnit class attributes and methods

# aadl2_ComponentPrototypeBinding class attributes and methods

# PrototypeBinding class attributes and methods

# aadl2_ComponentPrototypeActual class attributes and methods
aadl2_ComponentPrototypeActual_category: Property = Property(name="category", type=StringType)
aadl2_ComponentPrototypeActual.attributes={aadl2_ComponentPrototypeActual_category}

# aadl2_FeatureGroupPrototypeBinding class attributes and methods

# aadl2_FeatureGroupPrototypeActual class attributes and methods

# FeaturePrototypeActual class attributes and methods

# aadl2_FeaturePrototypeReference class attributes and methods
aadl2_FeaturePrototypeReference_direction: Property = Property(name="direction", type=StringType)
aadl2_FeaturePrototypeReference.attributes={aadl2_FeaturePrototypeReference_direction}

# aadl2_FeaturePrototypeActual class attributes and methods

# aadl2_FeaturePrototypeBinding class attributes and methods

# aadl2_AccessSpecification class attributes and methods
aadl2_AccessSpecification_kind: Property = Property(name="kind", type=StringType)
aadl2_AccessSpecification_category: Property = Property(name="category", type=StringType)
aadl2_AccessSpecification.attributes={aadl2_AccessSpecification_kind, aadl2_AccessSpecification_category}

# aadl2_PortSpecification class attributes and methods
aadl2_PortSpecification_direction: Property = Property(name="direction", type=StringType)
aadl2_PortSpecification_category: Property = Property(name="category", type=StringType)
aadl2_PortSpecification.attributes={aadl2_PortSpecification_direction, aadl2_PortSpecification_category}

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

# aadl2_VirtualProcessor class attributes and methods

# aadl2_VirtualBusSubcomponentType class attributes and methods

# VirtualBus class attributes and methods

# aadl2_VirtualBus class attributes and methods

# aadl2_AbstractClassifier class attributes and methods

# AbstractSubcomponentType class attributes and methods

# BusSubcomponentType class attributes and methods

# DeviceSubcomponentType class attributes and methods

# MemorySubcomponentType class attributes and methods

# ProcessorSubcomponentType class attributes and methods

# ProcessSubcomponentType class attributes and methods

# SubprogramGroupSubcomponentType class attributes and methods

# SystemSubcomponentType class attributes and methods

# ThreadGroupSubcomponentType class attributes and methods

# ThreadSubcomponentType class attributes and methods

# VirtualBusSubcomponentType class attributes and methods

# VirtualProcessorSubcomponentType class attributes and methods

# aadl2_VirtualProcessorSubcomponentType class attributes and methods

# VirtualProcessor class attributes and methods

# aadl2_AbstractImplementation class attributes and methods

# BehavioredImplementation class attributes and methods

# aadl2_ThreadGroupSubcomponentType class attributes and methods

# aadl2_BusSubcomponent class attributes and methods

# ThreadGroup class attributes and methods

# aadl2_ThreadGroup class attributes and methods

# aadl2_ThreadSubcomponentType class attributes and methods

# Thread class attributes and methods

# aadl2_Thread class attributes and methods

# aadl2_SystemSubcomponentType class attributes and methods

# System class attributes and methods

# aadl2_System class attributes and methods

# aadl2_ProcessSubcomponentType class attributes and methods

# Process class attributes and methods

# aadl2_Process class attributes and methods

# aadl2_MemorySubcomponentType class attributes and methods

# Memory class attributes and methods

# aadl2_Memory class attributes and methods

# aadl2_DeviceSubcomponentType class attributes and methods

# Device class attributes and methods

# aadl2_Device class attributes and methods

# aadl2_ProcessorSubcomponentType class attributes and methods

# Processor class attributes and methods

# aadl2_Processor class attributes and methods

# aadl2_ThreadSubcomponent class attributes and methods

# aadl2_ThreadGroupSubcomponent class attributes and methods

# aadl2_DataSubcomponent class attributes and methods

# aadl2_DeviceSubcomponent class attributes and methods

# aadl2_MemorySubcomponent class attributes and methods

# aadl2_ProcessSubcomponent class attributes and methods

# aadl2_ProcessorSubcomponent class attributes and methods

# aadl2_SystemSubcomponent class attributes and methods

# aadl2_SubprogramSubcomponent class attributes and methods

# aadl2_SubprogramGroupSubcomponent class attributes and methods

# aadl2_VirtualBusSubcomponent class attributes and methods

# aadl2_VirtualProcessorSubcomponent class attributes and methods

# aadl2_AbstractPrototype class attributes and methods

# ComponentPrototype class attributes and methods

# aadl2_BusClassifier class attributes and methods

# aadl2_BusType class attributes and methods

# BusClassifier class attributes and methods

# aadl2_DataImplementation class attributes and methods

# aadl2_BusImplementation class attributes and methods

# aadl2_BusPrototype class attributes and methods

# aadl2_DataType class attributes and methods

# DataClassifier class attributes and methods

# aadl2_DeviceImplementation class attributes and methods

# aadl2_DataPrototype class attributes and methods

# aadl2_DeviceClassifier class attributes and methods

# aadl2_DeviceType class attributes and methods

# DeviceClassifier class attributes and methods

# aadl2_DevicePrototype class attributes and methods

# aadl2_MemoryClassifier class attributes and methods

# aadl2_MemoryType class attributes and methods

# MemoryClassifier class attributes and methods

# aadl2_MemoryPrototype class attributes and methods

# aadl2_SubprogramType class attributes and methods

# SubprogramClassifier class attributes and methods

# aadl2_MemoryImplementation class attributes and methods

# aadl2_SubprogramGroupType class attributes and methods

# SubprogramGroupClassifier class attributes and methods

# aadl2_SubprogramGroupImplementation class attributes and methods

# aadl2_SubprogramImplementation class attributes and methods

# aadl2_SubprogramPrototype class attributes and methods

# aadl2_SubprogramGroupClassifier class attributes and methods

# aadl2_SubprogramGroupPrototype class attributes and methods

# aadl2_SystemClassifier class attributes and methods

# aadl2_SystemType class attributes and methods

# SystemClassifier class attributes and methods

# aadl2_SystemImplementation class attributes and methods

# aadl2_ProcessorClassifier class attributes and methods

# aadl2_ProcessorType class attributes and methods

# ProcessorClassifier class attributes and methods

# aadl2_SystemPrototype class attributes and methods

# aadl2_ProcessorPrototype class attributes and methods

# aadl2_ProcessClassifier class attributes and methods

# aadl2_ProcessorImplementation class attributes and methods

# aadl2_ProcessImplementation class attributes and methods

# aadl2_ProcessType class attributes and methods

# ProcessClassifier class attributes and methods

# aadl2_ThreadPrototype class attributes and methods

# aadl2_ProcessPrototype class attributes and methods

# aadl2_ThreadClassifier class attributes and methods

# aadl2_ThreadType class attributes and methods

# ThreadClassifier class attributes and methods

# aadl2_ThreadImplementation class attributes and methods

# aadl2_ThreadGroupClassifier class attributes and methods

# aadl2_ThreadGroupType class attributes and methods

# ThreadGroupClassifier class attributes and methods

# aadl2_ThreadGroupImplementation class attributes and methods

# aadl2_VirtualBusImplementation class attributes and methods

# aadl2_ThreadGroupPrototype class attributes and methods

# aadl2_VirtualBusClassifier class attributes and methods

# aadl2_VirtualBusType class attributes and methods

# VirtualBusClassifier class attributes and methods

# aadl2_VirtualProcessorImplementation class attributes and methods

# aadl2_VirtualBusPrototype class attributes and methods

# aadl2_VirtualProcessorClassifier class attributes and methods

# aadl2_VirtualProcessorType class attributes and methods

# VirtualProcessorClassifier class attributes and methods

# aadl2_StringLiteral class attributes and methods
aadl2_StringLiteral_value: Property = Property(name="value", type=StringType)
aadl2_StringLiteral.attributes={aadl2_StringLiteral_value}

# PropertyValue class attributes and methods

# aadl2_VirtualProcessorPrototype class attributes and methods

# aadl2_BasicPropertyAssociation class attributes and methods

# aadl2_PropertyConstant class attributes and methods

# aadl2_ReferenceValue class attributes and methods

# ContainedNamedElement class attributes and methods

# aadl2_PropertyValue class attributes and methods

# PropertyExpression class attributes and methods

# aadl2_NumberValue class attributes and methods
aadl2_NumberValue_m_getScaledValue: Method = Method(name="getScaledValue", parameters={Parameter(name='target')}, type=StringType)
aadl2_NumberValue_m_getScaledValue: Method = Method(name="getScaledValue", parameters={}, type=StringType)
aadl2_NumberValue_m_getScaledValue: Method = Method(name="getScaledValue", parameters={Parameter(name='target')}, type=StringType)
aadl2_NumberValue.methods={aadl2_NumberValue_m_getScaledValue, aadl2_NumberValue_m_getScaledValue, aadl2_NumberValue_m_getScaledValue}

# aadl2_UnitLiteral class attributes and methods
aadl2_UnitLiteral_m_getAbsoluteFactor: Method = Method(name="getAbsoluteFactor", parameters={Parameter(name='target')}, type=StringType)
aadl2_UnitLiteral.methods={aadl2_UnitLiteral_m_getAbsoluteFactor}

# EnumerationLiteral class attributes and methods

# aadl2_EnumerationLiteral class attributes and methods

# aadl2_ClassifierValue class attributes and methods

# aadl2_BooleanLiteral class attributes and methods
aadl2_BooleanLiteral_value: Property = Property(name="value", type=StringType)
aadl2_BooleanLiteral.attributes={aadl2_BooleanLiteral_value}

# aadl2_RangeValue class attributes and methods

# aadl2_IntegerLiteral class attributes and methods
aadl2_IntegerLiteral_base: Property = Property(name="base", type=StringType)
aadl2_IntegerLiteral_value: Property = Property(name="value", type=StringType)
aadl2_IntegerLiteral.attributes={aadl2_IntegerLiteral_base, aadl2_IntegerLiteral_value}

# NumberValue class attributes and methods

# aadl2_RealLiteral class attributes and methods
aadl2_RealLiteral_value: Property = Property(name="value", type=StringType)
aadl2_RealLiteral.attributes={aadl2_RealLiteral_value}

# aadl2_Operation class attributes and methods
aadl2_Operation_op: Property = Property(name="op", type=StringType)
aadl2_Operation.attributes={aadl2_Operation_op}

# aadl2_RecordValue class attributes and methods

# aadl2_ComputedValue class attributes and methods
aadl2_ComputedValue_function: Property = Property(name="function", type=StringType)
aadl2_ComputedValue.attributes={aadl2_ComputedValue_function}

# aadl2_ListValue class attributes and methods

# aadl2_NamedValue class attributes and methods

# aadl2_PropertySet class attributes and methods

# aadl2_NonListType class attributes and methods

# aadl2_GlobalNamespace class attributes and methods

# aadl2_NumericRange class attributes and methods

# PropertyType class attributes and methods

# aadl2_AadlBoolean class attributes and methods

# NonListType class attributes and methods

# aadl2_AadlString class attributes and methods

# aadl2_AadlInteger class attributes and methods

# NumberType class attributes and methods

# aadl2_NumberType class attributes and methods

# aadl2_UnitsType class attributes and methods

# aadl2_AadlReal class attributes and methods

# EnumerationType class attributes and methods

# aadl2_EnumerationType class attributes and methods

# aadl2_ClassifierType class attributes and methods

# aadl2_RangeType class attributes and methods

# aadl2_RecordType class attributes and methods

# aadl2_RecordField class attributes and methods

# aadl2_ReferenceType class attributes and methods

# aadl2_ListType class attributes and methods

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
        Property(name="aadl2_NamedElement", type=aadl2_PropertyAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="aadl2_PropertyAssociation", type=aadl2_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
defaultValue13: BinaryAssociation = BinaryAssociation(
    name="defaultValue13",
    ends={
        Property(name="aadl2_PropertyExpression", type=aadl2_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Property14", type=aadl2_PropertyExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
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
ownedValue11: BinaryAssociation = BinaryAssociation(
    name="ownedValue11",
    ends={
        Property(name="aadl2_ModalPropertyValue", type=aadl2_PropertyAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertyAssociation12", type=aadl2_ModalPropertyValue, multiplicity=Multiplicity(1, 9999), is_composite=True)
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
propertyType22: BinaryAssociation = BinaryAssociation(
    name="propertyType22",
    ends={
        Property(name="aadl2_PropertyType", type=aadl2_BasicProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BasicProperty", type=aadl2_PropertyType, multiplicity=Multiplicity(1, 1))
    }
)
ownedPropertyType23: BinaryAssociation = BinaryAssociation(
    name="ownedPropertyType23",
    ends={
        Property(name="aadl2_PropertyType25", type=aadl2_BasicProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BasicProperty24", type=aadl2_PropertyType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type26: BinaryAssociation = BinaryAssociation(
    name="type26",
    ends={
        Property(name="aadl2_Type", type=aadl2_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_TypedElement", type=aadl2_Type, multiplicity=Multiplicity(0, 1))
    }
)
classifierFeature27: BinaryAssociation = BinaryAssociation(
    name="classifierFeature27",
    ends={
        Property(name="ClassifierFeature", type=aadl2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="featuringClassifier", type=aadl2_ClassifierFeature, multiplicity=Multiplicity(0, 9999))
    }
)
inheritedMember28: BinaryAssociation = BinaryAssociation(
    name="inheritedMember28",
    ends={
        Property(name="aadl2_NamedElement30", type=aadl2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Classifier29", type=aadl2_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
generalization31: BinaryAssociation = BinaryAssociation(
    name="generalization31",
    ends={
        Property(name="Generalization", type=aadl2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="specific", type=aadl2_Generalization, multiplicity=Multiplicity(0, 9999))
    }
)
general33: BinaryAssociation = BinaryAssociation(
    name="general33",
    ends={
        Property(name="aadl2_Classifier34", type=aadl2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Classifier32", type=aadl2_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAnnexSubclause35: BinaryAssociation = BinaryAssociation(
    name="ownedAnnexSubclause35",
    ends={
        Property(name="aadl2_AnnexSubclause", type=aadl2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Classifier36", type=aadl2_AnnexSubclause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPrototype37: BinaryAssociation = BinaryAssociation(
    name="ownedPrototype37",
    ends={
        Property(name="aadl2_Prototype", type=aadl2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Classifier38", type=aadl2_Prototype, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPrototypeBinding39: BinaryAssociation = BinaryAssociation(
    name="ownedPrototypeBinding39",
    ends={
        Property(name="aadl2_PrototypeBinding", type=aadl2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Classifier40", type=aadl2_PrototypeBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedMember41: BinaryAssociation = BinaryAssociation(
    name="ownedMember41",
    ends={
        Property(name="aadl2_NamedElement42", type=aadl2_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Namespace", type=aadl2_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
member43: BinaryAssociation = BinaryAssociation(
    name="member43",
    ends={
        Property(name="aadl2_NamedElement45", type=aadl2_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Namespace44", type=aadl2_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
featuringClassifier46: BinaryAssociation = BinaryAssociation(
    name="featuringClassifier46",
    ends={
        Property(name="Classifier", type=aadl2_ClassifierFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="classifierFeature", type=aadl2_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
general47: BinaryAssociation = BinaryAssociation(
    name="general47",
    ends={
        Property(name="aadl2_Classifier48", type=aadl2_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Generalization", type=aadl2_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
specific49: BinaryAssociation = BinaryAssociation(
    name="specific49",
    ends={
        Property(name="Classifier50", type=aadl2_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization", type=aadl2_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
source51: BinaryAssociation = BinaryAssociation(
    name="source51",
    ends={
        Property(name="aadl2_Element52", type=aadl2_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DirectedRelationship", type=aadl2_Element, multiplicity=Multiplicity(1, 9999))
    }
)
target53: BinaryAssociation = BinaryAssociation(
    name="target53",
    ends={
        Property(name="aadl2_Element55", type=aadl2_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DirectedRelationship54", type=aadl2_Element, multiplicity=Multiplicity(1, 9999))
    }
)
relatedElement56: BinaryAssociation = BinaryAssociation(
    name="relatedElement56",
    ends={
        Property(name="aadl2_Element57", type=aadl2_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Relationship", type=aadl2_Element, multiplicity=Multiplicity(1, 9999))
    }
)
inMode58: BinaryAssociation = BinaryAssociation(
    name="inMode58",
    ends={
        Property(name="aadl2_Mode", type=aadl2_ModalElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ModalElement", type=aadl2_Mode, multiplicity=Multiplicity(0, 9999))
    }
)
refined60: BinaryAssociation = BinaryAssociation(
    name="refined60",
    ends={
        Property(name="aadl2_Prototype61", type=aadl2_Prototype, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Prototype59", type=aadl2_Prototype, multiplicity=Multiplicity(0, 1))
    }
)
refinementContext62: BinaryAssociation = BinaryAssociation(
    name="refinementContext62",
    ends={
        Property(name="aadl2_Classifier63", type=aadl2_RefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_RefinableElement", type=aadl2_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
refinedElement65: BinaryAssociation = BinaryAssociation(
    name="refinedElement65",
    ends={
        Property(name="aadl2_RefinableElement66", type=aadl2_RefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_RefinableElement64", type=aadl2_RefinableElement, multiplicity=Multiplicity(0, 1))
    }
)
formal67: BinaryAssociation = BinaryAssociation(
    name="formal67",
    ends={
        Property(name="aadl2_Prototype69", type=aadl2_PrototypeBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PrototypeBinding68", type=aadl2_Prototype, multiplicity=Multiplicity(1, 1))
    }
)
containmentPathElement70: BinaryAssociation = BinaryAssociation(
    name="containmentPathElement70",
    ends={
        Property(name="aadl2_ContainmentPathElement", type=aadl2_ContainedNamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ContainedNamedElement71", type=aadl2_ContainmentPathElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
arrayRange72: BinaryAssociation = BinaryAssociation(
    name="arrayRange72",
    ends={
        Property(name="aadl2_ArrayRange", type=aadl2_ContainmentPathElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ContainmentPathElement73", type=aadl2_ArrayRange, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
namedElement74: BinaryAssociation = BinaryAssociation(
    name="namedElement74",
    ends={
        Property(name="aadl2_NamedElement76", type=aadl2_ContainmentPathElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ContainmentPathElement75", type=aadl2_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
ownedValue77: BinaryAssociation = BinaryAssociation(
    name="ownedValue77",
    ends={
        Property(name="aadl2_PropertyExpression79", type=aadl2_ModalPropertyValue, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ModalPropertyValue78", type=aadl2_PropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
size80: BinaryAssociation = BinaryAssociation(
    name="size80",
    ends={
        Property(name="aadl2_ArraySize", type=aadl2_ArrayDimension, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ArrayDimension", type=aadl2_ArraySize, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sizeProperty81: BinaryAssociation = BinaryAssociation(
    name="sizeProperty81",
    ends={
        Property(name="aadl2_ArraySizeProperty", type=aadl2_ArraySize, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ArraySize82", type=aadl2_ArraySizeProperty, multiplicity=Multiplicity(0, 1))
    }
)
arrayDimension83: BinaryAssociation = BinaryAssociation(
    name="arrayDimension83",
    ends={
        Property(name="aadl2_ArrayDimension84", type=aadl2_ArrayableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ArrayableElement", type=aadl2_ArrayDimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implementation85: BinaryAssociation = BinaryAssociation(
    name="implementation85",
    ends={
        Property(name="aadl2_ComponentImplementation", type=aadl2_ComponentImplementationReference, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementationReference", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1))
    }
)
ownedPrototypeBinding86: BinaryAssociation = BinaryAssociation(
    name="ownedPrototypeBinding86",
    ends={
        Property(name="aadl2_PrototypeBinding88", type=aadl2_ComponentImplementationReference, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementationReference87", type=aadl2_PrototypeBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type89: BinaryAssociation = BinaryAssociation(
    name="type89",
    ends={
        Property(name="aadl2_ComponentType", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation90", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1))
    }
)
ownedSubcomponent91: BinaryAssociation = BinaryAssociation(
    name="ownedSubcomponent91",
    ends={
        Property(name="aadl2_Subcomponent", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation92", type=aadl2_Subcomponent, multiplicity=Multiplicity(0, 9999))
    }
)
extended94: BinaryAssociation = BinaryAssociation(
    name="extended94",
    ends={
        Property(name="aadl2_ComponentImplementation95", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation93", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(0, 1))
    }
)
ownedFlowImplementation96: BinaryAssociation = BinaryAssociation(
    name="ownedFlowImplementation96",
    ends={
        Property(name="aadl2_FlowImplementation", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation97", type=aadl2_FlowImplementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedConnection98: BinaryAssociation = BinaryAssociation(
    name="ownedConnection98",
    ends={
        Property(name="aadl2_Connection", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation99", type=aadl2_Connection, multiplicity=Multiplicity(0, 9999))
    }
)
ownedExtension100: BinaryAssociation = BinaryAssociation(
    name="ownedExtension100",
    ends={
        Property(name="aadl2_ImplementationExtension", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation101", type=aadl2_ImplementationExtension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedRealization102: BinaryAssociation = BinaryAssociation(
    name="ownedRealization102",
    ends={
        Property(name="aadl2_Realization", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation103", type=aadl2_Realization, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedEndToEndFlow104: BinaryAssociation = BinaryAssociation(
    name="ownedEndToEndFlow104",
    ends={
        Property(name="aadl2_EndToEndFlow", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation105", type=aadl2_EndToEndFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAbstractSubcomponent106: BinaryAssociation = BinaryAssociation(
    name="ownedAbstractSubcomponent106",
    ends={
        Property(name="aadl2_AbstractSubcomponent", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation107", type=aadl2_AbstractSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedInternalFeature120: BinaryAssociation = BinaryAssociation(
    name="ownedInternalFeature120",
    ends={
        Property(name="aadl2_InternalFeature", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation121", type=aadl2_InternalFeature, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAccessConnection108: BinaryAssociation = BinaryAssociation(
    name="ownedAccessConnection108",
    ends={
        Property(name="aadl2_AccessConnection", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation109", type=aadl2_AccessConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedParameterConnection110: BinaryAssociation = BinaryAssociation(
    name="ownedParameterConnection110",
    ends={
        Property(name="aadl2_ParameterConnection", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation111", type=aadl2_ParameterConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPortConnection112: BinaryAssociation = BinaryAssociation(
    name="ownedPortConnection112",
    ends={
        Property(name="aadl2_PortConnection", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation113", type=aadl2_PortConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedFeatureConnection114: BinaryAssociation = BinaryAssociation(
    name="ownedFeatureConnection114",
    ends={
        Property(name="aadl2_FeatureConnection", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation115", type=aadl2_FeatureConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedFeatureGroupConnection116: BinaryAssociation = BinaryAssociation(
    name="ownedFeatureGroupConnection116",
    ends={
        Property(name="aadl2_FeatureGroupConnection", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation117", type=aadl2_FeatureGroupConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProcessorFeature118: BinaryAssociation = BinaryAssociation(
    name="ownedProcessorFeature118",
    ends={
        Property(name="aadl2_ProcessorFeature", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation119", type=aadl2_ProcessorFeature, multiplicity=Multiplicity(0, 9999))
    }
)
ownedEventSource122: BinaryAssociation = BinaryAssociation(
    name="ownedEventSource122",
    ends={
        Property(name="aadl2_EventSource", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation123", type=aadl2_EventSource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataSource124: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataSource124",
    ends={
        Property(name="aadl2_EventDataSource", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation125", type=aadl2_EventDataSource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPortProxy126: BinaryAssociation = BinaryAssociation(
    name="ownedPortProxy126",
    ends={
        Property(name="aadl2_PortProxy", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation127", type=aadl2_PortProxy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramProxy128: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramProxy128",
    ends={
        Property(name="aadl2_SubprogramProxy", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation129", type=aadl2_SubprogramProxy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedMode130: BinaryAssociation = BinaryAssociation(
    name="ownedMode130",
    ends={
        Property(name="aadl2_Mode131", type=aadl2_ComponentClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentClassifier", type=aadl2_Mode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedModeTransition132: BinaryAssociation = BinaryAssociation(
    name="ownedModeTransition132",
    ends={
        Property(name="aadl2_ModeTransition", type=aadl2_ComponentClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentClassifier133", type=aadl2_ModeTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source134: BinaryAssociation = BinaryAssociation(
    name="source134",
    ends={
        Property(name="aadl2_Mode136", type=aadl2_ModeTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ModeTransition135", type=aadl2_Mode, multiplicity=Multiplicity(1, 1))
    }
)
destination137: BinaryAssociation = BinaryAssociation(
    name="destination137",
    ends={
        Property(name="aadl2_Mode139", type=aadl2_ModeTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ModeTransition138", type=aadl2_Mode, multiplicity=Multiplicity(1, 1))
    }
)
ownedTrigger140: BinaryAssociation = BinaryAssociation(
    name="ownedTrigger140",
    ends={
        Property(name="aadl2_ModeTransitionTrigger", type=aadl2_ModeTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ModeTransition141", type=aadl2_ModeTransitionTrigger, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
context142: BinaryAssociation = BinaryAssociation(
    name="context142",
    ends={
        Property(name="aadl2_Context", type=aadl2_ModeTransitionTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ModeTransitionTrigger143", type=aadl2_Context, multiplicity=Multiplicity(0, 1))
    }
)
triggerPort144: BinaryAssociation = BinaryAssociation(
    name="triggerPort144",
    ends={
        Property(name="aadl2_TriggerPort", type=aadl2_ModeTransitionTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ModeTransitionTrigger145", type=aadl2_TriggerPort, multiplicity=Multiplicity(1, 1))
    }
)
ownedFeature146: BinaryAssociation = BinaryAssociation(
    name="ownedFeature146",
    ends={
        Property(name="aadl2_Feature", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentType147", type=aadl2_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
extended149: BinaryAssociation = BinaryAssociation(
    name="extended149",
    ends={
        Property(name="aadl2_ComponentType150", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentType148", type=aadl2_ComponentType, multiplicity=Multiplicity(0, 1))
    }
)
ownedFlowSpecification151: BinaryAssociation = BinaryAssociation(
    name="ownedFlowSpecification151",
    ends={
        Property(name="aadl2_FlowSpecification", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentType152", type=aadl2_FlowSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedExtension153: BinaryAssociation = BinaryAssociation(
    name="ownedExtension153",
    ends={
        Property(name="aadl2_TypeExtension", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentType154", type=aadl2_TypeExtension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedFeatureGroup155: BinaryAssociation = BinaryAssociation(
    name="ownedFeatureGroup155",
    ends={
        Property(name="aadl2_FeatureGroup", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentType156", type=aadl2_FeatureGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAbstractFeature157: BinaryAssociation = BinaryAssociation(
    name="ownedAbstractFeature157",
    ends={
        Property(name="aadl2_AbstractFeature", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentType158", type=aadl2_AbstractFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
prototype159: BinaryAssociation = BinaryAssociation(
    name="prototype159",
    ends={
        Property(name="aadl2_ComponentPrototype", type=aadl2_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Feature160", type=aadl2_ComponentPrototype, multiplicity=Multiplicity(0, 1))
    }
)
featureClassifier161: BinaryAssociation = BinaryAssociation(
    name="featureClassifier161",
    ends={
        Property(name="aadl2_FeatureClassifier", type=aadl2_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Feature162", type=aadl2_FeatureClassifier, multiplicity=Multiplicity(0, 1))
    }
)
refined164: BinaryAssociation = BinaryAssociation(
    name="refined164",
    ends={
        Property(name="aadl2_Feature165", type=aadl2_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Feature163", type=aadl2_Feature, multiplicity=Multiplicity(0, 1))
    }
)
classifier166: BinaryAssociation = BinaryAssociation(
    name="classifier166",
    ends={
        Property(name="aadl2_Classifier168", type=aadl2_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Feature167", type=aadl2_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
constrainingClassifier169: BinaryAssociation = BinaryAssociation(
    name="constrainingClassifier169",
    ends={
        Property(name="aadl2_ComponentClassifier171", type=aadl2_ComponentPrototype, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentPrototype170", type=aadl2_ComponentClassifier, multiplicity=Multiplicity(0, 1))
    }
)
refined173: BinaryAssociation = BinaryAssociation(
    name="refined173",
    ends={
        Property(name="aadl2_FlowSpecification174", type=aadl2_FlowSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FlowSpecification172", type=aadl2_FlowSpecification, multiplicity=Multiplicity(0, 1))
    }
)
outEnd175: BinaryAssociation = BinaryAssociation(
    name="outEnd175",
    ends={
        Property(name="aadl2_FlowEnd", type=aadl2_FlowSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FlowSpecification176", type=aadl2_FlowEnd, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
InEnd177: BinaryAssociation = BinaryAssociation(
    name="InEnd177",
    ends={
        Property(name="aadl2_FlowEnd179", type=aadl2_FlowSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FlowSpecification178", type=aadl2_FlowEnd, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inModeOrTransition180: BinaryAssociation = BinaryAssociation(
    name="inModeOrTransition180",
    ends={
        Property(name="aadl2_ModeFeature", type=aadl2_ModalPath, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ModalPath", type=aadl2_ModeFeature, multiplicity=Multiplicity(0, 9999))
    }
)
context181: BinaryAssociation = BinaryAssociation(
    name="context181",
    ends={
        Property(name="aadl2_Context183", type=aadl2_FlowEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FlowEnd182", type=aadl2_Context, multiplicity=Multiplicity(0, 1))
    }
)
feature184: BinaryAssociation = BinaryAssociation(
    name="feature184",
    ends={
        Property(name="aadl2_Feature186", type=aadl2_FlowEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FlowEnd185", type=aadl2_Feature, multiplicity=Multiplicity(1, 1))
    }
)
extended187: BinaryAssociation = BinaryAssociation(
    name="extended187",
    ends={
        Property(name="aadl2_ComponentType189", type=aadl2_TypeExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_TypeExtension188", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1))
    }
)
featureType190: BinaryAssociation = BinaryAssociation(
    name="featureType190",
    ends={
        Property(name="aadl2_FeatureType", type=aadl2_FeatureGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroup191", type=aadl2_FeatureType, multiplicity=Multiplicity(0, 1))
    }
)
featureGroupType192: BinaryAssociation = BinaryAssociation(
    name="featureGroupType192",
    ends={
        Property(name="aadl2_FeatureGroupType", type=aadl2_FeatureGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroup193", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(0, 1))
    }
)
featureGroupPrototype194: BinaryAssociation = BinaryAssociation(
    name="featureGroupPrototype194",
    ends={
        Property(name="aadl2_FeatureGroupPrototype", type=aadl2_FeatureGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroup195", type=aadl2_FeatureGroupPrototype, multiplicity=Multiplicity(0, 1))
    }
)
ownedBusAccess207: BinaryAssociation = BinaryAssociation(
    name="ownedBusAccess207",
    ends={
        Property(name="aadl2_BusAccess", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType208", type=aadl2_BusAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedFeature196: BinaryAssociation = BinaryAssociation(
    name="ownedFeature196",
    ends={
        Property(name="aadl2_Feature198", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType197", type=aadl2_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
extended200: BinaryAssociation = BinaryAssociation(
    name="extended200",
    ends={
        Property(name="aadl2_FeatureGroupType201", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType199", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(0, 1))
    }
)
inverse203: BinaryAssociation = BinaryAssociation(
    name="inverse203",
    ends={
        Property(name="aadl2_FeatureGroupType204", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType202", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(0, 1))
    }
)
ownedExtension205: BinaryAssociation = BinaryAssociation(
    name="ownedExtension205",
    ends={
        Property(name="aadl2_GroupExtension", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType206", type=aadl2_GroupExtension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedDataAccess209: BinaryAssociation = BinaryAssociation(
    name="ownedDataAccess209",
    ends={
        Property(name="aadl2_DataAccess", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType210", type=aadl2_DataAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataPort211: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort211",
    ends={
        Property(name="aadl2_DataPort", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType212", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort213: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort213",
    ends={
        Property(name="aadl2_EventDataPort", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType214", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort215: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort215",
    ends={
        Property(name="aadl2_EventPort", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType216", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedFeatureGroup217: BinaryAssociation = BinaryAssociation(
    name="ownedFeatureGroup217",
    ends={
        Property(name="aadl2_FeatureGroup219", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType218", type=aadl2_FeatureGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedParameter220: BinaryAssociation = BinaryAssociation(
    name="ownedParameter220",
    ends={
        Property(name="aadl2_Parameter", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType221", type=aadl2_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess222: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess222",
    ends={
        Property(name="aadl2_SubprogramAccess", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType223", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess224: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess224",
    ends={
        Property(name="aadl2_SubprogramGroupAccess", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType225", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAbstractFeature226: BinaryAssociation = BinaryAssociation(
    name="ownedAbstractFeature226",
    ends={
        Property(name="aadl2_AbstractFeature228", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType227", type=aadl2_AbstractFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extended229: BinaryAssociation = BinaryAssociation(
    name="extended229",
    ends={
        Property(name="aadl2_FeatureGroupType231", type=aadl2_GroupExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_GroupExtension230", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1))
    }
)
busFeatureClassifier232: BinaryAssociation = BinaryAssociation(
    name="busFeatureClassifier232",
    ends={
        Property(name="aadl2_BusSubcomponentType", type=aadl2_BusAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BusAccess233", type=aadl2_BusSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
dataFeatureClassifier234: BinaryAssociation = BinaryAssociation(
    name="dataFeatureClassifier234",
    ends={
        Property(name="aadl2_DataSubcomponentType", type=aadl2_DataAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DataAccess235", type=aadl2_DataSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
subprogramFeatureClassifier245: BinaryAssociation = BinaryAssociation(
    name="subprogramFeatureClassifier245",
    ends={
        Property(name="aadl2_SubprogramSubcomponentType", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramAccess246", type=aadl2_SubprogramSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
dataFeatureClassifier236: BinaryAssociation = BinaryAssociation(
    name="dataFeatureClassifier236",
    ends={
        Property(name="aadl2_DataSubcomponentType238", type=aadl2_DataPort, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DataPort237", type=aadl2_DataSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
dataFeatureClassifier239: BinaryAssociation = BinaryAssociation(
    name="dataFeatureClassifier239",
    ends={
        Property(name="aadl2_DataSubcomponentType241", type=aadl2_EventDataPort, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_EventDataPort240", type=aadl2_DataSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
dataFeatureClassifier242: BinaryAssociation = BinaryAssociation(
    name="dataFeatureClassifier242",
    ends={
        Property(name="aadl2_DataSubcomponentType244", type=aadl2_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Parameter243", type=aadl2_DataSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
subprogramGroupFeatureClassifier247: BinaryAssociation = BinaryAssociation(
    name="subprogramGroupFeatureClassifier247",
    ends={
        Property(name="aadl2_SubprogramGroupSubcomponentType", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramGroupAccess248", type=aadl2_SubprogramGroupSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
featurePrototype249: BinaryAssociation = BinaryAssociation(
    name="featurePrototype249",
    ends={
        Property(name="aadl2_FeaturePrototype", type=aadl2_AbstractFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractFeature250", type=aadl2_FeaturePrototype, multiplicity=Multiplicity(0, 1))
    }
)
constrainingClassifier251: BinaryAssociation = BinaryAssociation(
    name="constrainingClassifier251",
    ends={
        Property(name="aadl2_ComponentClassifier253", type=aadl2_FeaturePrototype, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeaturePrototype252", type=aadl2_ComponentClassifier, multiplicity=Multiplicity(0, 1))
    }
)
constrainingFeatureGroupType254: BinaryAssociation = BinaryAssociation(
    name="constrainingFeatureGroupType254",
    ends={
        Property(name="aadl2_FeatureGroupType256", type=aadl2_FeatureGroupPrototype, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupPrototype255", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(0, 1))
    }
)
parentMode276: BinaryAssociation = BinaryAssociation(
    name="parentMode276",
    ends={
        Property(name="aadl2_Mode278", type=aadl2_ModeBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ModeBinding277", type=aadl2_Mode, multiplicity=Multiplicity(1, 1))
    }
)
subcomponentType257: BinaryAssociation = BinaryAssociation(
    name="subcomponentType257",
    ends={
        Property(name="aadl2_SubcomponentType", type=aadl2_Subcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Subcomponent258", type=aadl2_SubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
ownedPrototypeBinding259: BinaryAssociation = BinaryAssociation(
    name="ownedPrototypeBinding259",
    ends={
        Property(name="aadl2_PrototypeBinding261", type=aadl2_Subcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Subcomponent260", type=aadl2_PrototypeBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
prototype262: BinaryAssociation = BinaryAssociation(
    name="prototype262",
    ends={
        Property(name="aadl2_ComponentPrototype264", type=aadl2_Subcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Subcomponent263", type=aadl2_ComponentPrototype, multiplicity=Multiplicity(0, 1))
    }
)
ownedModeBinding265: BinaryAssociation = BinaryAssociation(
    name="ownedModeBinding265",
    ends={
        Property(name="aadl2_ModeBinding", type=aadl2_Subcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Subcomponent266", type=aadl2_ModeBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implementationReference267: BinaryAssociation = BinaryAssociation(
    name="implementationReference267",
    ends={
        Property(name="aadl2_ComponentImplementationReference269", type=aadl2_Subcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Subcomponent268", type=aadl2_ComponentImplementationReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refined271: BinaryAssociation = BinaryAssociation(
    name="refined271",
    ends={
        Property(name="aadl2_Subcomponent272", type=aadl2_Subcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Subcomponent270", type=aadl2_Subcomponent, multiplicity=Multiplicity(0, 1))
    }
)
classifier273: BinaryAssociation = BinaryAssociation(
    name="classifier273",
    ends={
        Property(name="aadl2_ComponentClassifier275", type=aadl2_Subcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Subcomponent274", type=aadl2_ComponentClassifier, multiplicity=Multiplicity(0, 1))
    }
)
refined298: BinaryAssociation = BinaryAssociation(
    name="refined298",
    ends={
        Property(name="aadl2_Connection299", type=aadl2_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Connection297", type=aadl2_Connection, multiplicity=Multiplicity(0, 1))
    }
)
derivedMode279: BinaryAssociation = BinaryAssociation(
    name="derivedMode279",
    ends={
        Property(name="aadl2_Mode281", type=aadl2_ModeBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ModeBinding280", type=aadl2_Mode, multiplicity=Multiplicity(0, 1))
    }
)
specification282: BinaryAssociation = BinaryAssociation(
    name="specification282",
    ends={
        Property(name="aadl2_FlowSpecification284", type=aadl2_FlowImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FlowImplementation283", type=aadl2_FlowSpecification, multiplicity=Multiplicity(1, 1))
    }
)
ownedFlowSegment285: BinaryAssociation = BinaryAssociation(
    name="ownedFlowSegment285",
    ends={
        Property(name="aadl2_FlowSegment", type=aadl2_FlowImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FlowImplementation286", type=aadl2_FlowSegment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flowElement287: BinaryAssociation = BinaryAssociation(
    name="flowElement287",
    ends={
        Property(name="aadl2_FlowElement", type=aadl2_FlowSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FlowSegment288", type=aadl2_FlowElement, multiplicity=Multiplicity(1, 1))
    }
)
context289: BinaryAssociation = BinaryAssociation(
    name="context289",
    ends={
        Property(name="aadl2_Context291", type=aadl2_FlowSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FlowSegment290", type=aadl2_Context, multiplicity=Multiplicity(0, 1))
    }
)
destination292: BinaryAssociation = BinaryAssociation(
    name="destination292",
    ends={
        Property(name="aadl2_ConnectedElement", type=aadl2_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Connection293", type=aadl2_ConnectedElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source294: BinaryAssociation = BinaryAssociation(
    name="source294",
    ends={
        Property(name="aadl2_ConnectedElement296", type=aadl2_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Connection295", type=aadl2_ConnectedElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
context300: BinaryAssociation = BinaryAssociation(
    name="context300",
    ends={
        Property(name="aadl2_Context302", type=aadl2_ConnectedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ConnectedElement301", type=aadl2_Context, multiplicity=Multiplicity(0, 1))
    }
)
connectionEnd303: BinaryAssociation = BinaryAssociation(
    name="connectionEnd303",
    ends={
        Property(name="aadl2_ConnectionEnd", type=aadl2_ConnectedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ConnectedElement304", type=aadl2_ConnectionEnd, multiplicity=Multiplicity(1, 1))
    }
)
extended305: BinaryAssociation = BinaryAssociation(
    name="extended305",
    ends={
        Property(name="aadl2_ComponentImplementation307", type=aadl2_ImplementationExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ImplementationExtension306", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1))
    }
)
implemented308: BinaryAssociation = BinaryAssociation(
    name="implemented308",
    ends={
        Property(name="aadl2_ComponentType310", type=aadl2_Realization, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Realization309", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1))
    }
)
refined312: BinaryAssociation = BinaryAssociation(
    name="refined312",
    ends={
        Property(name="aadl2_EndToEndFlow313", type=aadl2_EndToEndFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_EndToEndFlow311", type=aadl2_EndToEndFlow, multiplicity=Multiplicity(0, 1))
    }
)
ownedEndToEndFlowSegment314: BinaryAssociation = BinaryAssociation(
    name="ownedEndToEndFlowSegment314",
    ends={
        Property(name="aadl2_EndToEndFlowSegment", type=aadl2_EndToEndFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_EndToEndFlow315", type=aadl2_EndToEndFlowSegment, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
flowElement316: BinaryAssociation = BinaryAssociation(
    name="flowElement316",
    ends={
        Property(name="aadl2_EndToEndFlowElement", type=aadl2_EndToEndFlowSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_EndToEndFlowSegment317", type=aadl2_EndToEndFlowElement, multiplicity=Multiplicity(1, 1))
    }
)
context318: BinaryAssociation = BinaryAssociation(
    name="context318",
    ends={
        Property(name="aadl2_Context320", type=aadl2_EndToEndFlowSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_EndToEndFlowSegment319", type=aadl2_Context, multiplicity=Multiplicity(0, 1))
    }
)
abstractSubcomponentType321: BinaryAssociation = BinaryAssociation(
    name="abstractSubcomponentType321",
    ends={
        Property(name="aadl2_AbstractSubcomponentType", type=aadl2_AbstractSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractSubcomponent322", type=aadl2_AbstractSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
dataClassifier325: BinaryAssociation = BinaryAssociation(
    name="dataClassifier325",
    ends={
        Property(name="aadl2_DataClassifier327", type=aadl2_PortProxy, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PortProxy326", type=aadl2_DataClassifier, multiplicity=Multiplicity(0, 1))
    }
)
dataClassifier323: BinaryAssociation = BinaryAssociation(
    name="dataClassifier323",
    ends={
        Property(name="aadl2_DataClassifier", type=aadl2_EventDataSource, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_EventDataSource324", type=aadl2_DataClassifier, multiplicity=Multiplicity(0, 1))
    }
)
privateSection333: BinaryAssociation = BinaryAssociation(
    name="privateSection333",
    ends={
        Property(name="PrivatePackageSection", type=aadl2_PublicPackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="publicSection", type=aadl2_PrivatePackageSection, multiplicity=Multiplicity(0, 1))
    }
)
subprogramClassifier328: BinaryAssociation = BinaryAssociation(
    name="subprogramClassifier328",
    ends={
        Property(name="aadl2_SubprogramClassifier", type=aadl2_SubprogramProxy, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramProxy329", type=aadl2_SubprogramClassifier, multiplicity=Multiplicity(0, 1))
    }
)
parsedAnnexLibrary330: BinaryAssociation = BinaryAssociation(
    name="parsedAnnexLibrary330",
    ends={
        Property(name="aadl2_AnnexLibrary", type=aadl2_DefaultAnnexLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DefaultAnnexLibrary", type=aadl2_AnnexLibrary, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parsedAnnexSubclause331: BinaryAssociation = BinaryAssociation(
    name="parsedAnnexSubclause331",
    ends={
        Property(name="aadl2_AnnexSubclause332", type=aadl2_DefaultAnnexSubclause, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DefaultAnnexSubclause", type=aadl2_AnnexSubclause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedPackageRename334: BinaryAssociation = BinaryAssociation(
    name="ownedPackageRename334",
    ends={
        Property(name="aadl2_PackageRename", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection", type=aadl2_PackageRename, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedComponentTypeRename335: BinaryAssociation = BinaryAssociation(
    name="ownedComponentTypeRename335",
    ends={
        Property(name="aadl2_ComponentTypeRename", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection336", type=aadl2_ComponentTypeRename, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedClassifier337: BinaryAssociation = BinaryAssociation(
    name="ownedClassifier337",
    ends={
        Property(name="aadl2_Classifier339", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection338", type=aadl2_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedFeatureGroupTypeRename340: BinaryAssociation = BinaryAssociation(
    name="ownedFeatureGroupTypeRename340",
    ends={
        Property(name="aadl2_FeatureGroupTypeRename", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection341", type=aadl2_FeatureGroupTypeRename, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAnnexLibrary342: BinaryAssociation = BinaryAssociation(
    name="ownedAnnexLibrary342",
    ends={
        Property(name="aadl2_AnnexLibrary344", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection343", type=aadl2_AnnexLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedUnit345: BinaryAssociation = BinaryAssociation(
    name="importedUnit345",
    ends={
        Property(name="aadl2_ModelUnit", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection346", type=aadl2_ModelUnit, multiplicity=Multiplicity(0, 9999))
    }
)
renamedComponentType360: BinaryAssociation = BinaryAssociation(
    name="renamedComponentType360",
    ends={
        Property(name="aadl2_ComponentType362", type=aadl2_ComponentTypeRename, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentTypeRename361", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1))
    }
)
renamedPackage347: BinaryAssociation = BinaryAssociation(
    name="renamedPackage347",
    ends={
        Property(name="aadl2_AadlPackage", type=aadl2_PackageRename, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageRename348", type=aadl2_AadlPackage, multiplicity=Multiplicity(1, 1))
    }
)
ownedPublicSection349: BinaryAssociation = BinaryAssociation(
    name="ownedPublicSection349",
    ends={
        Property(name="aadl2_PublicPackageSection", type=aadl2_AadlPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AadlPackage350", type=aadl2_PublicPackageSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedPrivateSection351: BinaryAssociation = BinaryAssociation(
    name="ownedPrivateSection351",
    ends={
        Property(name="aadl2_PrivatePackageSection", type=aadl2_AadlPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AadlPackage352", type=aadl2_PrivatePackageSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
publicSection353: BinaryAssociation = BinaryAssociation(
    name="publicSection353",
    ends={
        Property(name="aadl2_PublicPackageSection355", type=aadl2_AadlPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AadlPackage354", type=aadl2_PublicPackageSection, multiplicity=Multiplicity(0, 1))
    }
)
privateSection356: BinaryAssociation = BinaryAssociation(
    name="privateSection356",
    ends={
        Property(name="aadl2_PrivatePackageSection358", type=aadl2_AadlPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AadlPackage357", type=aadl2_PrivatePackageSection, multiplicity=Multiplicity(0, 1))
    }
)
publicSection359: BinaryAssociation = BinaryAssociation(
    name="publicSection359",
    ends={
        Property(name="PublicPackageSection", type=aadl2_PrivatePackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="privateSection", type=aadl2_PublicPackageSection, multiplicity=Multiplicity(0, 1))
    }
)
binding374: BinaryAssociation = BinaryAssociation(
    name="binding374",
    ends={
        Property(name="aadl2_PrototypeBinding376", type=aadl2_FeatureGroupPrototypeActual, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupPrototypeActual375", type=aadl2_PrototypeBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureType377: BinaryAssociation = BinaryAssociation(
    name="featureType377",
    ends={
        Property(name="aadl2_FeatureType379", type=aadl2_FeatureGroupPrototypeActual, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupPrototypeActual378", type=aadl2_FeatureType, multiplicity=Multiplicity(1, 1))
    }
)
renamedFeatureGroupType363: BinaryAssociation = BinaryAssociation(
    name="renamedFeatureGroupType363",
    ends={
        Property(name="aadl2_FeatureGroupType365", type=aadl2_FeatureGroupTypeRename, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupTypeRename364", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1))
    }
)
actual366: BinaryAssociation = BinaryAssociation(
    name="actual366",
    ends={
        Property(name="aadl2_ComponentPrototypeActual", type=aadl2_ComponentPrototypeBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentPrototypeBinding", type=aadl2_ComponentPrototypeActual, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
binding367: BinaryAssociation = BinaryAssociation(
    name="binding367",
    ends={
        Property(name="aadl2_PrototypeBinding369", type=aadl2_ComponentPrototypeActual, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentPrototypeActual368", type=aadl2_PrototypeBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subcomponentType370: BinaryAssociation = BinaryAssociation(
    name="subcomponentType370",
    ends={
        Property(name="aadl2_SubcomponentType372", type=aadl2_ComponentPrototypeActual, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentPrototypeActual371", type=aadl2_SubcomponentType, multiplicity=Multiplicity(1, 1))
    }
)
actual373: BinaryAssociation = BinaryAssociation(
    name="actual373",
    ends={
        Property(name="aadl2_FeatureGroupPrototypeActual", type=aadl2_FeatureGroupPrototypeBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupPrototypeBinding", type=aadl2_FeatureGroupPrototypeActual, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
componentPrototype388: BinaryAssociation = BinaryAssociation(
    name="componentPrototype388",
    ends={
        Property(name="aadl2_ComponentPrototype390", type=aadl2_PortSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PortSpecification389", type=aadl2_ComponentPrototype, multiplicity=Multiplicity(0, 1))
    }
)
actual380: BinaryAssociation = BinaryAssociation(
    name="actual380",
    ends={
        Property(name="aadl2_FeaturePrototypeActual", type=aadl2_FeaturePrototypeBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeaturePrototypeBinding", type=aadl2_FeaturePrototypeActual, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier381: BinaryAssociation = BinaryAssociation(
    name="classifier381",
    ends={
        Property(name="aadl2_ComponentClassifier382", type=aadl2_AccessSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AccessSpecification", type=aadl2_ComponentClassifier, multiplicity=Multiplicity(0, 1))
    }
)
componentPrototype383: BinaryAssociation = BinaryAssociation(
    name="componentPrototype383",
    ends={
        Property(name="aadl2_ComponentPrototype385", type=aadl2_AccessSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AccessSpecification384", type=aadl2_ComponentPrototype, multiplicity=Multiplicity(0, 1))
    }
)
classifier386: BinaryAssociation = BinaryAssociation(
    name="classifier386",
    ends={
        Property(name="aadl2_ComponentClassifier387", type=aadl2_PortSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PortSpecification", type=aadl2_ComponentClassifier, multiplicity=Multiplicity(0, 1))
    }
)
ownedBusAccess403: BinaryAssociation = BinaryAssociation(
    name="ownedBusAccess403",
    ends={
        Property(name="aadl2_BusAccess404", type=aadl2_AbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractType", type=aadl2_BusAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataAccess405: BinaryAssociation = BinaryAssociation(
    name="ownedDataAccess405",
    ends={
        Property(name="aadl2_DataAccess407", type=aadl2_AbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractType406", type=aadl2_DataAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
prototype391: BinaryAssociation = BinaryAssociation(
    name="prototype391",
    ends={
        Property(name="aadl2_FeaturePrototype392", type=aadl2_FeaturePrototypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeaturePrototypeReference", type=aadl2_FeaturePrototype, multiplicity=Multiplicity(1, 1))
    }
)
ownedSubprogramCall393: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramCall393",
    ends={
        Property(name="aadl2_SubprogramCall", type=aadl2_SubprogramCallSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramCallSequence", type=aadl2_SubprogramCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledSubprogram394: BinaryAssociation = BinaryAssociation(
    name="calledSubprogram394",
    ends={
        Property(name="aadl2_CalledSubprogram", type=aadl2_SubprogramCall, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramCall395", type=aadl2_CalledSubprogram, multiplicity=Multiplicity(0, 1))
    }
)
context396: BinaryAssociation = BinaryAssociation(
    name="context396",
    ends={
        Property(name="aadl2_CallContext", type=aadl2_SubprogramCall, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramCall397", type=aadl2_CallContext, multiplicity=Multiplicity(0, 1))
    }
)
subprogramCall398: BinaryAssociation = BinaryAssociation(
    name="subprogramCall398",
    ends={
        Property(name="aadl2_SubprogramCall399", type=aadl2_BehavioredImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BehavioredImplementation", type=aadl2_SubprogramCall, multiplicity=Multiplicity(0, 9999))
    }
)
ownedSubprogramCallSequence400: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramCallSequence400",
    ends={
        Property(name="aadl2_SubprogramCallSequence402", type=aadl2_BehavioredImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BehavioredImplementation401", type=aadl2_SubprogramCallSequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess408: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess408",
    ends={
        Property(name="aadl2_SubprogramAccess410", type=aadl2_AbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractType409", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataPort411: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort411",
    ends={
        Property(name="aadl2_DataPort413", type=aadl2_AbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractType412", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort414: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort414",
    ends={
        Property(name="aadl2_EventPort416", type=aadl2_AbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractType415", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort417: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort417",
    ends={
        Property(name="aadl2_EventDataPort419", type=aadl2_AbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractType418", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess420: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess420",
    ends={
        Property(name="aadl2_SubprogramGroupAccess422", type=aadl2_AbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractType421", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusSubcomponent423: BinaryAssociation = BinaryAssociation(
    name="ownedBusSubcomponent423",
    ends={
        Property(name="aadl2_BusSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation", type=aadl2_BusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedThreadSubcomponent440: BinaryAssociation = BinaryAssociation(
    name="ownedThreadSubcomponent440",
    ends={
        Property(name="aadl2_ThreadSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation441", type=aadl2_ThreadSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedThreadGroupSubcomponent442: BinaryAssociation = BinaryAssociation(
    name="ownedThreadGroupSubcomponent442",
    ends={
        Property(name="aadl2_ThreadGroupSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation443", type=aadl2_ThreadGroupSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataSubcomponent424: BinaryAssociation = BinaryAssociation(
    name="ownedDataSubcomponent424",
    ends={
        Property(name="aadl2_DataSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation425", type=aadl2_DataSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDeviceSubcomponent426: BinaryAssociation = BinaryAssociation(
    name="ownedDeviceSubcomponent426",
    ends={
        Property(name="aadl2_DeviceSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation427", type=aadl2_DeviceSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedMemorySubcomponent428: BinaryAssociation = BinaryAssociation(
    name="ownedMemorySubcomponent428",
    ends={
        Property(name="aadl2_MemorySubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation429", type=aadl2_MemorySubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProcessSubcomponent430: BinaryAssociation = BinaryAssociation(
    name="ownedProcessSubcomponent430",
    ends={
        Property(name="aadl2_ProcessSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation431", type=aadl2_ProcessSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProcessorSubcomponent432: BinaryAssociation = BinaryAssociation(
    name="ownedProcessorSubcomponent432",
    ends={
        Property(name="aadl2_ProcessorSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation433", type=aadl2_ProcessorSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSystemSubcomponent434: BinaryAssociation = BinaryAssociation(
    name="ownedSystemSubcomponent434",
    ends={
        Property(name="aadl2_SystemSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation435", type=aadl2_SystemSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramSubcomponent436: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramSubcomponent436",
    ends={
        Property(name="aadl2_SubprogramSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation437", type=aadl2_SubprogramSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupSubcomponent438: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupSubcomponent438",
    ends={
        Property(name="aadl2_SubprogramGroupSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation439", type=aadl2_SubprogramGroupSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memorySubcomponentType456: BinaryAssociation = BinaryAssociation(
    name="memorySubcomponentType456",
    ends={
        Property(name="aadl2_MemorySubcomponentType", type=aadl2_MemorySubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_MemorySubcomponent457", type=aadl2_MemorySubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
processSubcomponentType458: BinaryAssociation = BinaryAssociation(
    name="processSubcomponentType458",
    ends={
        Property(name="aadl2_ProcessSubcomponentType", type=aadl2_ProcessSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessSubcomponent459", type=aadl2_ProcessSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
ownedVirtualBusSubcomponent444: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualBusSubcomponent444",
    ends={
        Property(name="aadl2_VirtualBusSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation445", type=aadl2_VirtualBusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualProcessorSubcomponent446: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualProcessorSubcomponent446",
    ends={
        Property(name="aadl2_VirtualProcessorSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation447", type=aadl2_VirtualProcessorSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
busSubcomponentType448: BinaryAssociation = BinaryAssociation(
    name="busSubcomponentType448",
    ends={
        Property(name="aadl2_BusSubcomponentType450", type=aadl2_BusSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BusSubcomponent449", type=aadl2_BusSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
dataSubcomponentType451: BinaryAssociation = BinaryAssociation(
    name="dataSubcomponentType451",
    ends={
        Property(name="aadl2_DataSubcomponentType453", type=aadl2_DataSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DataSubcomponent452", type=aadl2_DataSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
deviceSubcomponentType454: BinaryAssociation = BinaryAssociation(
    name="deviceSubcomponentType454",
    ends={
        Property(name="aadl2_DeviceSubcomponentType", type=aadl2_DeviceSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DeviceSubcomponent455", type=aadl2_DeviceSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
threadSubcomponentType470: BinaryAssociation = BinaryAssociation(
    name="threadSubcomponentType470",
    ends={
        Property(name="aadl2_ThreadSubcomponentType", type=aadl2_ThreadSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadSubcomponent471", type=aadl2_ThreadSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
threadGroupSubcomponentType472: BinaryAssociation = BinaryAssociation(
    name="threadGroupSubcomponentType472",
    ends={
        Property(name="aadl2_ThreadGroupSubcomponentType", type=aadl2_ThreadGroupSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupSubcomponent473", type=aadl2_ThreadGroupSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
processorSubcomponentType460: BinaryAssociation = BinaryAssociation(
    name="processorSubcomponentType460",
    ends={
        Property(name="aadl2_ProcessorSubcomponentType", type=aadl2_ProcessorSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorSubcomponent461", type=aadl2_ProcessorSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
systemSubcomponentType462: BinaryAssociation = BinaryAssociation(
    name="systemSubcomponentType462",
    ends={
        Property(name="aadl2_SystemSubcomponentType", type=aadl2_SystemSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemSubcomponent463", type=aadl2_SystemSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
subprogramSubcomponentType464: BinaryAssociation = BinaryAssociation(
    name="subprogramSubcomponentType464",
    ends={
        Property(name="aadl2_SubprogramSubcomponentType466", type=aadl2_SubprogramSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramSubcomponent465", type=aadl2_SubprogramSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
subprogramGroupSubcomponentType467: BinaryAssociation = BinaryAssociation(
    name="subprogramGroupSubcomponentType467",
    ends={
        Property(name="aadl2_SubprogramGroupSubcomponentType469", type=aadl2_SubprogramGroupSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramGroupSubcomponent468", type=aadl2_SubprogramGroupSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
ownedDataPort480: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort480",
    ends={
        Property(name="aadl2_DataPort482", type=aadl2_BusType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BusType481", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort483: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort483",
    ends={
        Property(name="aadl2_EventDataPort485", type=aadl2_BusType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BusType484", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort486: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort486",
    ends={
        Property(name="aadl2_EventPort488", type=aadl2_BusType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BusType487", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
virtualBusSubcomponentType474: BinaryAssociation = BinaryAssociation(
    name="virtualBusSubcomponentType474",
    ends={
        Property(name="aadl2_VirtualBusSubcomponentType", type=aadl2_VirtualBusSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualBusSubcomponent475", type=aadl2_VirtualBusSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
virtualProcessorSubcomponentType476: BinaryAssociation = BinaryAssociation(
    name="virtualProcessorSubcomponentType476",
    ends={
        Property(name="aadl2_VirtualProcessorSubcomponentType", type=aadl2_VirtualProcessorSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualProcessorSubcomponent477", type=aadl2_VirtualProcessorSubcomponentType, multiplicity=Multiplicity(0, 1))
    }
)
ownedBusAccess478: BinaryAssociation = BinaryAssociation(
    name="ownedBusAccess478",
    ends={
        Property(name="aadl2_BusAccess479", type=aadl2_BusType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BusType", type=aadl2_BusAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataSubcomponent499: BinaryAssociation = BinaryAssociation(
    name="ownedDataSubcomponent499",
    ends={
        Property(name="aadl2_DataSubcomponent500", type=aadl2_DataImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DataImplementation", type=aadl2_DataSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualBusSubcomponent489: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualBusSubcomponent489",
    ends={
        Property(name="aadl2_VirtualBusSubcomponent490", type=aadl2_BusImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BusImplementation", type=aadl2_VirtualBusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess491: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess491",
    ends={
        Property(name="aadl2_SubprogramAccess492", type=aadl2_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DataType", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataAccess493: BinaryAssociation = BinaryAssociation(
    name="ownedDataAccess493",
    ends={
        Property(name="aadl2_DataAccess495", type=aadl2_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DataType494", type=aadl2_DataAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess496: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess496",
    ends={
        Property(name="aadl2_SubprogramGroupAccess498", type=aadl2_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DataType497", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess518: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess518",
    ends={
        Property(name="aadl2_SubprogramGroupAccess520", type=aadl2_DeviceType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DeviceType519", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramSubcomponent501: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramSubcomponent501",
    ends={
        Property(name="aadl2_SubprogramSubcomponent503", type=aadl2_DataImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DataImplementation502", type=aadl2_SubprogramSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataPort504: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort504",
    ends={
        Property(name="aadl2_DataPort505", type=aadl2_DeviceType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DeviceType", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort506: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort506",
    ends={
        Property(name="aadl2_EventDataPort508", type=aadl2_DeviceType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DeviceType507", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort509: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort509",
    ends={
        Property(name="aadl2_EventPort511", type=aadl2_DeviceType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DeviceType510", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusAccess512: BinaryAssociation = BinaryAssociation(
    name="ownedBusAccess512",
    ends={
        Property(name="aadl2_BusAccess514", type=aadl2_DeviceType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DeviceType513", type=aadl2_BusAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess515: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess515",
    ends={
        Property(name="aadl2_SubprogramAccess517", type=aadl2_DeviceType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DeviceType516", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusAccess529: BinaryAssociation = BinaryAssociation(
    name="ownedBusAccess529",
    ends={
        Property(name="aadl2_BusAccess530", type=aadl2_MemoryType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_MemoryType", type=aadl2_BusAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusSubcomponent521: BinaryAssociation = BinaryAssociation(
    name="ownedBusSubcomponent521",
    ends={
        Property(name="aadl2_BusSubcomponent522", type=aadl2_DeviceImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DeviceImplementation", type=aadl2_BusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataSubcomponent523: BinaryAssociation = BinaryAssociation(
    name="ownedDataSubcomponent523",
    ends={
        Property(name="aadl2_DataSubcomponent525", type=aadl2_DeviceImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DeviceImplementation524", type=aadl2_DataSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualBusSubcomponent526: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualBusSubcomponent526",
    ends={
        Property(name="aadl2_VirtualBusSubcomponent528", type=aadl2_DeviceImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DeviceImplementation527", type=aadl2_VirtualBusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort545: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort545",
    ends={
        Property(name="aadl2_EventDataPort546", type=aadl2_SubprogramType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramType", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort547: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort547",
    ends={
        Property(name="aadl2_EventPort549", type=aadl2_SubprogramType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramType548", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedParameter550: BinaryAssociation = BinaryAssociation(
    name="ownedParameter550",
    ends={
        Property(name="aadl2_Parameter552", type=aadl2_SubprogramType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramType551", type=aadl2_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataAccess553: BinaryAssociation = BinaryAssociation(
    name="ownedDataAccess553",
    ends={
        Property(name="aadl2_DataAccess555", type=aadl2_SubprogramType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramType554", type=aadl2_DataAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataPort531: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort531",
    ends={
        Property(name="aadl2_DataPort533", type=aadl2_MemoryType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_MemoryType532", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort534: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort534",
    ends={
        Property(name="aadl2_EventDataPort536", type=aadl2_MemoryType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_MemoryType535", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort537: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort537",
    ends={
        Property(name="aadl2_EventPort539", type=aadl2_MemoryType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_MemoryType538", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusSubcomponent540: BinaryAssociation = BinaryAssociation(
    name="ownedBusSubcomponent540",
    ends={
        Property(name="aadl2_BusSubcomponent541", type=aadl2_MemoryImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_MemoryImplementation", type=aadl2_BusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedMemorySubcomponent542: BinaryAssociation = BinaryAssociation(
    name="ownedMemorySubcomponent542",
    ends={
        Property(name="aadl2_MemorySubcomponent544", type=aadl2_MemoryImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_MemoryImplementation543", type=aadl2_MemorySubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess567: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess567",
    ends={
        Property(name="aadl2_SubprogramAccess568", type=aadl2_SubprogramGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramGroupType", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess569: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess569",
    ends={
        Property(name="aadl2_SubprogramGroupAccess571", type=aadl2_SubprogramGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramGroupType570", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess556: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess556",
    ends={
        Property(name="aadl2_SubprogramAccess558", type=aadl2_SubprogramType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramType557", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess559: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess559",
    ends={
        Property(name="aadl2_SubprogramGroupAccess561", type=aadl2_SubprogramType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramType560", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataSubcomponent562: BinaryAssociation = BinaryAssociation(
    name="ownedDataSubcomponent562",
    ends={
        Property(name="aadl2_DataSubcomponent563", type=aadl2_SubprogramImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramImplementation", type=aadl2_DataSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramSubcomponent564: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramSubcomponent564",
    ends={
        Property(name="aadl2_SubprogramSubcomponent566", type=aadl2_SubprogramImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramImplementation565", type=aadl2_SubprogramSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataAccess582: BinaryAssociation = BinaryAssociation(
    name="ownedDataAccess582",
    ends={
        Property(name="aadl2_DataAccess584", type=aadl2_SystemType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemType583", type=aadl2_DataAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataPort585: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort585",
    ends={
        Property(name="aadl2_DataPort587", type=aadl2_SystemType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemType586", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess588: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess588",
    ends={
        Property(name="aadl2_SubprogramGroupAccess590", type=aadl2_SystemType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemType589", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess591: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess591",
    ends={
        Property(name="aadl2_SubprogramAccess593", type=aadl2_SystemType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemType592", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramSubcomponent572: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramSubcomponent572",
    ends={
        Property(name="aadl2_SubprogramSubcomponent573", type=aadl2_SubprogramGroupImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramGroupImplementation", type=aadl2_SubprogramSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupSubcomponent574: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupSubcomponent574",
    ends={
        Property(name="aadl2_SubprogramGroupSubcomponent576", type=aadl2_SubprogramGroupImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramGroupImplementation575", type=aadl2_SubprogramGroupSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataSubcomponent577: BinaryAssociation = BinaryAssociation(
    name="ownedDataSubcomponent577",
    ends={
        Property(name="aadl2_DataSubcomponent579", type=aadl2_SubprogramGroupImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramGroupImplementation578", type=aadl2_DataSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusAccess580: BinaryAssociation = BinaryAssociation(
    name="ownedBusAccess580",
    ends={
        Property(name="aadl2_BusAccess581", type=aadl2_SystemType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemType", type=aadl2_BusAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDeviceSubcomponent605: BinaryAssociation = BinaryAssociation(
    name="ownedDeviceSubcomponent605",
    ends={
        Property(name="aadl2_DeviceSubcomponent607", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation606", type=aadl2_DeviceSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedMemorySubcomponent608: BinaryAssociation = BinaryAssociation(
    name="ownedMemorySubcomponent608",
    ends={
        Property(name="aadl2_MemorySubcomponent610", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation609", type=aadl2_MemorySubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProcessSubcomponent611: BinaryAssociation = BinaryAssociation(
    name="ownedProcessSubcomponent611",
    ends={
        Property(name="aadl2_ProcessSubcomponent613", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation612", type=aadl2_ProcessSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProcessorSubcomponent614: BinaryAssociation = BinaryAssociation(
    name="ownedProcessorSubcomponent614",
    ends={
        Property(name="aadl2_ProcessorSubcomponent616", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation615", type=aadl2_ProcessorSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort594: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort594",
    ends={
        Property(name="aadl2_EventPort596", type=aadl2_SystemType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemType595", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort597: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort597",
    ends={
        Property(name="aadl2_EventDataPort599", type=aadl2_SystemType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemType598", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusSubcomponent600: BinaryAssociation = BinaryAssociation(
    name="ownedBusSubcomponent600",
    ends={
        Property(name="aadl2_BusSubcomponent601", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation", type=aadl2_BusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataSubcomponent602: BinaryAssociation = BinaryAssociation(
    name="ownedDataSubcomponent602",
    ends={
        Property(name="aadl2_DataSubcomponent604", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation603", type=aadl2_DataSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataPort632: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort632",
    ends={
        Property(name="aadl2_DataPort633", type=aadl2_ProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorType", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort634: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort634",
    ends={
        Property(name="aadl2_EventDataPort636", type=aadl2_ProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorType635", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramSubcomponent617: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramSubcomponent617",
    ends={
        Property(name="aadl2_SubprogramSubcomponent619", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation618", type=aadl2_SubprogramSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupSubcomponent620: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupSubcomponent620",
    ends={
        Property(name="aadl2_SubprogramGroupSubcomponent622", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation621", type=aadl2_SubprogramGroupSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSystemSubcomponent623: BinaryAssociation = BinaryAssociation(
    name="ownedSystemSubcomponent623",
    ends={
        Property(name="aadl2_SystemSubcomponent625", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation624", type=aadl2_SystemSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualBusSubcomponent626: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualBusSubcomponent626",
    ends={
        Property(name="aadl2_VirtualBusSubcomponent628", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation627", type=aadl2_VirtualBusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualProcessorSubcomponent629: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualProcessorSubcomponent629",
    ends={
        Property(name="aadl2_VirtualProcessorSubcomponent631", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation630", type=aadl2_VirtualProcessorSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedMemorySubcomponent651: BinaryAssociation = BinaryAssociation(
    name="ownedMemorySubcomponent651",
    ends={
        Property(name="aadl2_MemorySubcomponent653", type=aadl2_ProcessorImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorImplementation652", type=aadl2_MemorySubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualBusSubcomponent654: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualBusSubcomponent654",
    ends={
        Property(name="aadl2_VirtualBusSubcomponent656", type=aadl2_ProcessorImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorImplementation655", type=aadl2_VirtualBusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualProcessorSubcomponent657: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualProcessorSubcomponent657",
    ends={
        Property(name="aadl2_VirtualProcessorSubcomponent659", type=aadl2_ProcessorImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorImplementation658", type=aadl2_VirtualProcessorSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort637: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort637",
    ends={
        Property(name="aadl2_EventPort639", type=aadl2_ProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorType638", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusAccess640: BinaryAssociation = BinaryAssociation(
    name="ownedBusAccess640",
    ends={
        Property(name="aadl2_BusAccess642", type=aadl2_ProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorType641", type=aadl2_BusAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess643: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess643",
    ends={
        Property(name="aadl2_SubprogramAccess645", type=aadl2_ProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorType644", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess646: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess646",
    ends={
        Property(name="aadl2_SubprogramGroupAccess648", type=aadl2_ProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorType647", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusSubcomponent649: BinaryAssociation = BinaryAssociation(
    name="ownedBusSubcomponent649",
    ends={
        Property(name="aadl2_BusSubcomponent650", type=aadl2_ProcessorImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorImplementation", type=aadl2_BusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess674: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess674",
    ends={
        Property(name="aadl2_SubprogramGroupAccess676", type=aadl2_ProcessType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessType675", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataSubcomponent677: BinaryAssociation = BinaryAssociation(
    name="ownedDataSubcomponent677",
    ends={
        Property(name="aadl2_DataSubcomponent678", type=aadl2_ProcessImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessImplementation", type=aadl2_DataSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataPort660: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort660",
    ends={
        Property(name="aadl2_DataPort661", type=aadl2_ProcessType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessType", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort662: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort662",
    ends={
        Property(name="aadl2_EventDataPort664", type=aadl2_ProcessType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessType663", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort665: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort665",
    ends={
        Property(name="aadl2_EventPort667", type=aadl2_ProcessType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessType666", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataAccess668: BinaryAssociation = BinaryAssociation(
    name="ownedDataAccess668",
    ends={
        Property(name="aadl2_DataAccess670", type=aadl2_ProcessType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessType669", type=aadl2_DataAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess671: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess671",
    ends={
        Property(name="aadl2_SubprogramAccess673", type=aadl2_ProcessType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessType672", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramSubcomponent679: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramSubcomponent679",
    ends={
        Property(name="aadl2_SubprogramSubcomponent681", type=aadl2_ProcessImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessImplementation680", type=aadl2_SubprogramSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupSubcomponent682: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupSubcomponent682",
    ends={
        Property(name="aadl2_SubprogramGroupSubcomponent684", type=aadl2_ProcessImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessImplementation683", type=aadl2_SubprogramGroupSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataPort691: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort691",
    ends={
        Property(name="aadl2_DataPort692", type=aadl2_ThreadType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadType", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedThreadSubcomponent685: BinaryAssociation = BinaryAssociation(
    name="ownedThreadSubcomponent685",
    ends={
        Property(name="aadl2_ThreadSubcomponent687", type=aadl2_ProcessImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessImplementation686", type=aadl2_ThreadSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort693: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort693",
    ends={
        Property(name="aadl2_EventDataPort695", type=aadl2_ThreadType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadType694", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedThreadGroupSubcomponent688: BinaryAssociation = BinaryAssociation(
    name="ownedThreadGroupSubcomponent688",
    ends={
        Property(name="aadl2_ThreadGroupSubcomponent690", type=aadl2_ProcessImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessImplementation689", type=aadl2_ThreadGroupSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort696: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort696",
    ends={
        Property(name="aadl2_EventPort698", type=aadl2_ThreadType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadType697", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataAccess699: BinaryAssociation = BinaryAssociation(
    name="ownedDataAccess699",
    ends={
        Property(name="aadl2_DataAccess701", type=aadl2_ThreadType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadType700", type=aadl2_DataAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess702: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess702",
    ends={
        Property(name="aadl2_SubprogramAccess704", type=aadl2_ThreadType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadType703", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess705: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess705",
    ends={
        Property(name="aadl2_SubprogramGroupAccess707", type=aadl2_ThreadType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadType706", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupSubcomponent708: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupSubcomponent708",
    ends={
        Property(name="aadl2_SubprogramGroupSubcomponent709", type=aadl2_ThreadImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadImplementation", type=aadl2_SubprogramGroupSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramSubcomponent710: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramSubcomponent710",
    ends={
        Property(name="aadl2_SubprogramSubcomponent712", type=aadl2_ThreadImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadImplementation711", type=aadl2_SubprogramSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataSubcomponent713: BinaryAssociation = BinaryAssociation(
    name="ownedDataSubcomponent713",
    ends={
        Property(name="aadl2_DataSubcomponent715", type=aadl2_ThreadImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadImplementation714", type=aadl2_DataSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataSubcomponent733: BinaryAssociation = BinaryAssociation(
    name="ownedDataSubcomponent733",
    ends={
        Property(name="aadl2_DataSubcomponent734", type=aadl2_ThreadGroupImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupImplementation", type=aadl2_DataSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataPort716: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort716",
    ends={
        Property(name="aadl2_DataPort717", type=aadl2_ThreadGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupType", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort718: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort718",
    ends={
        Property(name="aadl2_EventDataPort720", type=aadl2_ThreadGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupType719", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort721: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort721",
    ends={
        Property(name="aadl2_EventPort723", type=aadl2_ThreadGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupType722", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataAccess724: BinaryAssociation = BinaryAssociation(
    name="ownedDataAccess724",
    ends={
        Property(name="aadl2_DataAccess726", type=aadl2_ThreadGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupType725", type=aadl2_DataAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess727: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess727",
    ends={
        Property(name="aadl2_SubprogramAccess729", type=aadl2_ThreadGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupType728", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess730: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess730",
    ends={
        Property(name="aadl2_SubprogramGroupAccess732", type=aadl2_ThreadGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupType731", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedThreadSubcomponent735: BinaryAssociation = BinaryAssociation(
    name="ownedThreadSubcomponent735",
    ends={
        Property(name="aadl2_ThreadSubcomponent737", type=aadl2_ThreadGroupImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupImplementation736", type=aadl2_ThreadSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedThreadGroupSubcomponent738: BinaryAssociation = BinaryAssociation(
    name="ownedThreadGroupSubcomponent738",
    ends={
        Property(name="aadl2_ThreadGroupSubcomponent740", type=aadl2_ThreadGroupImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupImplementation739", type=aadl2_ThreadGroupSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramSubcomponent741: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramSubcomponent741",
    ends={
        Property(name="aadl2_SubprogramSubcomponent743", type=aadl2_ThreadGroupImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupImplementation742", type=aadl2_SubprogramSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupSubcomponent744: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupSubcomponent744",
    ends={
        Property(name="aadl2_SubprogramGroupSubcomponent746", type=aadl2_ThreadGroupImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupImplementation745", type=aadl2_SubprogramGroupSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataPort747: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort747",
    ends={
        Property(name="aadl2_DataPort748", type=aadl2_VirtualBusType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualBusType", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort749: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort749",
    ends={
        Property(name="aadl2_EventDataPort751", type=aadl2_VirtualBusType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualBusType750", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort752: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort752",
    ends={
        Property(name="aadl2_EventPort754", type=aadl2_VirtualBusType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualBusType753", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualBusSubcomponent755: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualBusSubcomponent755",
    ends={
        Property(name="aadl2_VirtualBusSubcomponent756", type=aadl2_VirtualBusImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualBusImplementation", type=aadl2_VirtualBusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataPort757: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort757",
    ends={
        Property(name="aadl2_DataPort758", type=aadl2_VirtualProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualProcessorType", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort759: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort759",
    ends={
        Property(name="aadl2_EventDataPort761", type=aadl2_VirtualProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualProcessorType760", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort762: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort762",
    ends={
        Property(name="aadl2_EventPort764", type=aadl2_VirtualProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualProcessorType763", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess765: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess765",
    ends={
        Property(name="aadl2_SubprogramAccess767", type=aadl2_VirtualProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualProcessorType766", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess768: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess768",
    ends={
        Property(name="aadl2_SubprogramGroupAccess770", type=aadl2_VirtualProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualProcessorType769", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualBusSubcomponent771: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualBusSubcomponent771",
    ends={
        Property(name="aadl2_VirtualBusSubcomponent772", type=aadl2_VirtualProcessorImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualProcessorImplementation", type=aadl2_VirtualBusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualProcessorSubcomponent773: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualProcessorSubcomponent773",
    ends={
        Property(name="aadl2_VirtualProcessorSubcomponent775", type=aadl2_VirtualProcessorImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualProcessorImplementation774", type=aadl2_VirtualProcessorSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property776: BinaryAssociation = BinaryAssociation(
    name="property776",
    ends={
        Property(name="aadl2_BasicProperty777", type=aadl2_BasicPropertyAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BasicPropertyAssociation", type=aadl2_BasicProperty, multiplicity=Multiplicity(1, 1))
    }
)
ownedValue778: BinaryAssociation = BinaryAssociation(
    name="ownedValue778",
    ends={
        Property(name="aadl2_PropertyExpression780", type=aadl2_BasicPropertyAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BasicPropertyAssociation779", type=aadl2_PropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
propertyType781: BinaryAssociation = BinaryAssociation(
    name="propertyType781",
    ends={
        Property(name="aadl2_PropertyType782", type=aadl2_PropertyConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertyConstant", type=aadl2_PropertyType, multiplicity=Multiplicity(1, 1))
    }
)
ownedPropertyType783: BinaryAssociation = BinaryAssociation(
    name="ownedPropertyType783",
    ends={
        Property(name="aadl2_PropertyType785", type=aadl2_PropertyConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertyConstant784", type=aadl2_PropertyType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classifier796: BinaryAssociation = BinaryAssociation(
    name="classifier796",
    ends={
        Property(name="aadl2_ClassifierValue", type=aadl2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Classifier797", type=aadl2_ClassifierValue, multiplicity=Multiplicity(1, 1))
    }
)
constantValue786: BinaryAssociation = BinaryAssociation(
    name="constantValue786",
    ends={
        Property(name="aadl2_PropertyExpression788", type=aadl2_PropertyConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertyConstant787", type=aadl2_PropertyExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unit789: BinaryAssociation = BinaryAssociation(
    name="unit789",
    ends={
        Property(name="aadl2_UnitLiteral", type=aadl2_NumberValue, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_NumberValue", type=aadl2_UnitLiteral, multiplicity=Multiplicity(0, 1))
    }
)
baseUnit791: BinaryAssociation = BinaryAssociation(
    name="baseUnit791",
    ends={
        Property(name="aadl2_UnitLiteral792", type=aadl2_UnitLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_UnitLiteral790", type=aadl2_UnitLiteral, multiplicity=Multiplicity(0, 1))
    }
)
factor793: BinaryAssociation = BinaryAssociation(
    name="factor793",
    ends={
        Property(name="aadl2_NumberValue795", type=aadl2_UnitLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_UnitLiteral794", type=aadl2_NumberValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
minimum798: BinaryAssociation = BinaryAssociation(
    name="minimum798",
    ends={
        Property(name="aadl2_PropertyExpression799", type=aadl2_RangeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_RangeValue", type=aadl2_PropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
maximum800: BinaryAssociation = BinaryAssociation(
    name="maximum800",
    ends={
        Property(name="aadl2_PropertyExpression802", type=aadl2_RangeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_RangeValue801", type=aadl2_PropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
delta803: BinaryAssociation = BinaryAssociation(
    name="delta803",
    ends={
        Property(name="aadl2_PropertyExpression805", type=aadl2_RangeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_RangeValue804", type=aadl2_PropertyExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedPropertyExpression806: BinaryAssociation = BinaryAssociation(
    name="ownedPropertyExpression806",
    ends={
        Property(name="aadl2_PropertyExpression807", type=aadl2_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Operation", type=aadl2_PropertyExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ownedFieldValue808: BinaryAssociation = BinaryAssociation(
    name="ownedFieldValue808",
    ends={
        Property(name="aadl2_BasicPropertyAssociation809", type=aadl2_RecordValue, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_RecordValue", type=aadl2_BasicPropertyAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProperty815: BinaryAssociation = BinaryAssociation(
    name="ownedProperty815",
    ends={
        Property(name="aadl2_Property817", type=aadl2_PropertySet, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertySet816", type=aadl2_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedListElement810: BinaryAssociation = BinaryAssociation(
    name="ownedListElement810",
    ends={
        Property(name="aadl2_PropertyExpression811", type=aadl2_ListValue, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ListValue", type=aadl2_PropertyExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
namedValue812: BinaryAssociation = BinaryAssociation(
    name="namedValue812",
    ends={
        Property(name="aadl2_AbstractNamedValue", type=aadl2_NamedValue, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_NamedValue", type=aadl2_AbstractNamedValue, multiplicity=Multiplicity(1, 1))
    }
)
ownedPropertyType813: BinaryAssociation = BinaryAssociation(
    name="ownedPropertyType813",
    ends={
        Property(name="aadl2_PropertyType814", type=aadl2_PropertySet, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertySet", type=aadl2_PropertyType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propertySet829: BinaryAssociation = BinaryAssociation(
    name="propertySet829",
    ends={
        Property(name="aadl2_PropertySet831", type=aadl2_GlobalNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_GlobalNamespace830", type=aadl2_PropertySet, multiplicity=Multiplicity(0, 9999))
    }
)
ownedPropertyConstant818: BinaryAssociation = BinaryAssociation(
    name="ownedPropertyConstant818",
    ends={
        Property(name="aadl2_PropertyConstant820", type=aadl2_PropertySet, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertySet819", type=aadl2_PropertyConstant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedUnit821: BinaryAssociation = BinaryAssociation(
    name="importedUnit821",
    ends={
        Property(name="aadl2_ModelUnit823", type=aadl2_PropertySet, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertySet822", type=aadl2_ModelUnit, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAnnexSubclause824: BinaryAssociation = BinaryAssociation(
    name="ownedAnnexSubclause824",
    ends={
        Property(name="aadl2_AnnexSubclause826", type=aadl2_PropertySet, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertySet825", type=aadl2_AnnexSubclause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package827: BinaryAssociation = BinaryAssociation(
    name="package827",
    ends={
        Property(name="aadl2_PublicPackageSection828", type=aadl2_GlobalNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_GlobalNamespace", type=aadl2_PublicPackageSection, multiplicity=Multiplicity(0, 9999))
    }
)
range836: BinaryAssociation = BinaryAssociation(
    name="range836",
    ends={
        Property(name="aadl2_NumericRange", type=aadl2_NumberType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_NumberType837", type=aadl2_NumericRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedUnitsType832: BinaryAssociation = BinaryAssociation(
    name="ownedUnitsType832",
    ends={
        Property(name="aadl2_UnitsType", type=aadl2_NumberType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_NumberType", type=aadl2_UnitsType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unitsType833: BinaryAssociation = BinaryAssociation(
    name="unitsType833",
    ends={
        Property(name="aadl2_UnitsType835", type=aadl2_NumberType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_NumberType834", type=aadl2_UnitsType, multiplicity=Multiplicity(0, 1))
    }
)
lowerBound842: BinaryAssociation = BinaryAssociation(
    name="lowerBound842",
    ends={
        Property(name="aadl2_PropertyExpression844", type=aadl2_NumericRange, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_NumericRange843", type=aadl2_PropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedLiteral838: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral838",
    ends={
        Property(name="aadl2_EnumerationLiteral", type=aadl2_EnumerationType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_EnumerationType", type=aadl2_EnumerationLiteral, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
upperBound839: BinaryAssociation = BinaryAssociation(
    name="upperBound839",
    ends={
        Property(name="aadl2_PropertyExpression841", type=aadl2_NumericRange, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_NumericRange840", type=aadl2_PropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedField852: BinaryAssociation = BinaryAssociation(
    name="ownedField852",
    ends={
        Property(name="aadl2_BasicProperty853", type=aadl2_RecordType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_RecordType", type=aadl2_BasicProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifierReference845: BinaryAssociation = BinaryAssociation(
    name="classifierReference845",
    ends={
        Property(name="aadl2_MetaclassReference846", type=aadl2_ClassifierType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ClassifierType", type=aadl2_MetaclassReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ownedNumberType847: BinaryAssociation = BinaryAssociation(
    name="ownedNumberType847",
    ends={
        Property(name="aadl2_NumberType848", type=aadl2_RangeType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_RangeType", type=aadl2_NumberType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
numberType849: BinaryAssociation = BinaryAssociation(
    name="numberType849",
    ends={
        Property(name="aadl2_NumberType851", type=aadl2_RangeType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_RangeType850", type=aadl2_NumberType, multiplicity=Multiplicity(1, 1))
    }
)
namedElementReference854: BinaryAssociation = BinaryAssociation(
    name="namedElementReference854",
    ends={
        Property(name="aadl2_MetaclassReference855", type=aadl2_ReferenceType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ReferenceType", type=aadl2_MetaclassReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ownedElementType856: BinaryAssociation = BinaryAssociation(
    name="ownedElementType856",
    ends={
        Property(name="aadl2_PropertyType857", type=aadl2_ListType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ListType", type=aadl2_PropertyType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementType858: BinaryAssociation = BinaryAssociation(
    name="elementType858",
    ends={
        Property(name="aadl2_PropertyType860", type=aadl2_ListType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ListType859", type=aadl2_PropertyType, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_aadl2_Comment_Element = Generalization(general=Element, specific=aadl2_Comment)
gen_aadl2_Type_NamedElement = Generalization(general=NamedElement, specific=aadl2_Type)
gen_aadl2_NamedElement_Element = Generalization(general=Element, specific=aadl2_NamedElement)
gen_aadl2_PropertyAssociation_Element = Generalization(general=Element, specific=aadl2_PropertyAssociation)
gen_aadl2_Property_BasicProperty = Generalization(general=BasicProperty, specific=aadl2_Property)
gen_aadl2_Property_AbstractNamedValue = Generalization(general=AbstractNamedValue, specific=aadl2_Property)
gen_aadl2_Property_ArraySizeProperty = Generalization(general=ArraySizeProperty, specific=aadl2_Property)
gen_aadl2_BasicProperty_TypedElement = Generalization(general=TypedElement, specific=aadl2_BasicProperty)
gen_aadl2_TypedElement_NamedElement = Generalization(general=NamedElement, specific=aadl2_TypedElement)
gen_aadl2_PropertyType_Type = Generalization(general=Type, specific=aadl2_PropertyType)
gen_aadl2_PropertyExpression_Element = Generalization(general=Element, specific=aadl2_PropertyExpression)
gen_aadl2_MetaclassReference_PropertyOwner = Generalization(general=PropertyOwner, specific=aadl2_MetaclassReference)
gen_aadl2_PropertyOwner_Element = Generalization(general=Element, specific=aadl2_PropertyOwner)
gen_aadl2_Classifier_Namespace = Generalization(general=Namespace, specific=aadl2_Classifier)
gen_aadl2_Classifier_Type = Generalization(general=Type, specific=aadl2_Classifier)
gen_aadl2_ClassifierFeature_NamedElement = Generalization(general=NamedElement, specific=aadl2_ClassifierFeature)
gen_aadl2_Namespace_NamedElement = Generalization(general=NamedElement, specific=aadl2_Namespace)
gen_aadl2_AnnexSubclause_ModalElement = Generalization(general=ModalElement, specific=aadl2_AnnexSubclause)
gen_aadl2_Generalization_DirectedRelationship = Generalization(general=DirectedRelationship, specific=aadl2_Generalization)
gen_aadl2_DirectedRelationship_Relationship = Generalization(general=Relationship, specific=aadl2_DirectedRelationship)
gen_aadl2_Relationship_Element = Generalization(general=Element, specific=aadl2_Relationship)
gen_aadl2_ModalElement_NamedElement = Generalization(general=NamedElement, specific=aadl2_ModalElement)
gen_aadl2_Mode_ModeFeature = Generalization(general=ModeFeature, specific=aadl2_Mode)
gen_aadl2_ModeFeature_ClassifierFeature = Generalization(general=ClassifierFeature, specific=aadl2_ModeFeature)
gen_aadl2_Prototype_StructuralFeature = Generalization(general=StructuralFeature, specific=aadl2_Prototype)
gen_aadl2_Prototype_CalledSubprogram = Generalization(general=CalledSubprogram, specific=aadl2_Prototype)
gen_aadl2_StructuralFeature_RefinableElement = Generalization(general=RefinableElement, specific=aadl2_StructuralFeature)
gen_aadl2_StructuralFeature_ClassifierFeature = Generalization(general=ClassifierFeature, specific=aadl2_StructuralFeature)
gen_aadl2_RefinableElement_NamedElement = Generalization(general=NamedElement, specific=aadl2_RefinableElement)
gen_aadl2_PrototypeBinding_Element = Generalization(general=Element, specific=aadl2_PrototypeBinding)
gen_aadl2_ContainedNamedElement_Element = Generalization(general=Element, specific=aadl2_ContainedNamedElement)
gen_aadl2_ContainmentPathElement_Element = Generalization(general=Element, specific=aadl2_ContainmentPathElement)
gen_aadl2_ArrayRange_Element = Generalization(general=Element, specific=aadl2_ArrayRange)
gen_aadl2_ModalPropertyValue_ModalElement = Generalization(general=ModalElement, specific=aadl2_ModalPropertyValue)
gen_aadl2_BehavioralFeature_ClassifierFeature = Generalization(general=ClassifierFeature, specific=aadl2_BehavioralFeature)
gen_aadl2_ArrayDimension_Element = Generalization(general=Element, specific=aadl2_ArrayDimension)
gen_aadl2_ArraySize_Element = Generalization(general=Element, specific=aadl2_ArraySize)
gen_aadl2_ArrayableElement_Element = Generalization(general=Element, specific=aadl2_ArrayableElement)
gen_aadl2_ComponentImplementationReference_Element = Generalization(general=Element, specific=aadl2_ComponentImplementationReference)
gen_aadl2_ComponentImplementation_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_ComponentImplementation)
gen_aadl2_SubcomponentType_Type = Generalization(general=Type, specific=aadl2_SubcomponentType)
gen_aadl2_ComponentClassifier_Classifier = Generalization(general=Classifier, specific=aadl2_ComponentClassifier)
gen_aadl2_ComponentClassifier_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_ComponentClassifier)
gen_aadl2_ComponentClassifier_FeatureClassifier = Generalization(general=FeatureClassifier, specific=aadl2_ComponentClassifier)
gen_aadl2_ModeTransition_ModeFeature = Generalization(general=ModeFeature, specific=aadl2_ModeTransition)
gen_aadl2_ModeTransitionTrigger_Element = Generalization(general=Element, specific=aadl2_ModeTransitionTrigger)
gen_aadl2_Context_NamedElement = Generalization(general=NamedElement, specific=aadl2_Context)
gen_aadl2_TriggerPort_NamedElement = Generalization(general=NamedElement, specific=aadl2_TriggerPort)
gen_aadl2_ComponentType_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_ComponentType)
gen_aadl2_Feature_StructuralFeature = Generalization(general=StructuralFeature, specific=aadl2_Feature)
gen_aadl2_Feature_FeatureConnectionEnd = Generalization(general=FeatureConnectionEnd, specific=aadl2_Feature)
gen_aadl2_Feature_ArrayableElement = Generalization(general=ArrayableElement, specific=aadl2_Feature)
gen_aadl2_FeatureConnectionEnd_ConnectionEnd = Generalization(general=ConnectionEnd, specific=aadl2_FeatureConnectionEnd)
gen_aadl2_ConnectionEnd_NamedElement = Generalization(general=NamedElement, specific=aadl2_ConnectionEnd)
gen_aadl2_ComponentPrototype_Prototype = Generalization(general=Prototype, specific=aadl2_ComponentPrototype)
gen_aadl2_ComponentPrototype_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_ComponentPrototype)
gen_aadl2_ComponentPrototype_FeatureClassifier = Generalization(general=FeatureClassifier, specific=aadl2_ComponentPrototype)
gen_aadl2_FlowEnd_Element = Generalization(general=Element, specific=aadl2_FlowEnd)
gen_aadl2_FlowSpecification_FlowFeature = Generalization(general=FlowFeature, specific=aadl2_FlowSpecification)
gen_aadl2_FlowSpecification_ModalPath = Generalization(general=ModalPath, specific=aadl2_FlowSpecification)
gen_aadl2_FlowSpecification_FlowElement = Generalization(general=FlowElement, specific=aadl2_FlowSpecification)
gen_aadl2_FlowFeature_StructuralFeature = Generalization(general=StructuralFeature, specific=aadl2_FlowFeature)
gen_aadl2_FlowFeature_Flow = Generalization(general=Flow, specific=aadl2_FlowFeature)
gen_aadl2_Flow_NamedElement = Generalization(general=NamedElement, specific=aadl2_Flow)
gen_aadl2_ModalPath_ModalElement = Generalization(general=ModalElement, specific=aadl2_ModalPath)
gen_aadl2_FlowElement_EndToEndFlowElement = Generalization(general=EndToEndFlowElement, specific=aadl2_FlowElement)
gen_aadl2_EndToEndFlowElement_NamedElement = Generalization(general=NamedElement, specific=aadl2_EndToEndFlowElement)
gen_aadl2_TypeExtension_Generalization = Generalization(general=Generalization, specific=aadl2_TypeExtension)
gen_aadl2_FeatureGroup_DirectedFeature = Generalization(general=DirectedFeature, specific=aadl2_FeatureGroup)
gen_aadl2_FeatureGroup_Context = Generalization(general=Context, specific=aadl2_FeatureGroup)
gen_aadl2_FeatureGroup_FeatureGroupConnectionEnd = Generalization(general=FeatureGroupConnectionEnd, specific=aadl2_FeatureGroup)
gen_aadl2_FeatureGroup_CallContext = Generalization(general=CallContext, specific=aadl2_FeatureGroup)
gen_aadl2_FeatureGroupConnectionEnd_ConnectionEnd = Generalization(general=ConnectionEnd, specific=aadl2_FeatureGroupConnectionEnd)
gen_aadl2_DirectedFeature_Feature = Generalization(general=Feature, specific=aadl2_DirectedFeature)
gen_aadl2_FeatureGroupType_Classifier = Generalization(general=Classifier, specific=aadl2_FeatureGroupType)
gen_aadl2_FeatureGroupType_FeatureType = Generalization(general=FeatureType, specific=aadl2_FeatureGroupType)
gen_aadl2_Access_Feature = Generalization(general=Feature, specific=aadl2_Access)
gen_aadl2_Access_AccessConnectionEnd = Generalization(general=AccessConnectionEnd, specific=aadl2_Access)
gen_aadl2_GroupExtension_Generalization = Generalization(general=Generalization, specific=aadl2_GroupExtension)
gen_aadl2_BusAccess_Access = Generalization(general=Access, specific=aadl2_BusAccess)
gen_aadl2_BusAccess_Bus = Generalization(general=Bus, specific=aadl2_BusAccess)
gen_aadl2_Data_NamedElement = Generalization(general=NamedElement, specific=aadl2_Data)
gen_aadl2_DataSubcomponentType_Data = Generalization(general=Data, specific=aadl2_DataSubcomponentType)
gen_aadl2_DataSubcomponentType_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_DataSubcomponentType)
gen_aadl2_DataSubcomponentType_FeatureClassifier = Generalization(general=FeatureClassifier, specific=aadl2_DataSubcomponentType)
gen_aadl2_AccessConnectionEnd_ConnectionEnd = Generalization(general=ConnectionEnd, specific=aadl2_AccessConnectionEnd)
gen_aadl2_Bus_NamedElement = Generalization(general=NamedElement, specific=aadl2_Bus)
gen_aadl2_BusSubcomponentType_Bus = Generalization(general=Bus, specific=aadl2_BusSubcomponentType)
gen_aadl2_BusSubcomponentType_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_BusSubcomponentType)
gen_aadl2_BusSubcomponentType_FeatureClassifier = Generalization(general=FeatureClassifier, specific=aadl2_BusSubcomponentType)
gen_aadl2_DataAccess_Access = Generalization(general=Access, specific=aadl2_DataAccess)
gen_aadl2_DataAccess_Data = Generalization(general=Data, specific=aadl2_DataAccess)
gen_aadl2_DataAccess_FlowElement = Generalization(general=FlowElement, specific=aadl2_DataAccess)
gen_aadl2_DataAccess_ParameterConnectionEnd = Generalization(general=ParameterConnectionEnd, specific=aadl2_DataAccess)
gen_aadl2_DataAccess_PortConnectionEnd = Generalization(general=PortConnectionEnd, specific=aadl2_DataAccess)
gen_aadl2_ParameterConnectionEnd_ConnectionEnd = Generalization(general=ConnectionEnd, specific=aadl2_ParameterConnectionEnd)
gen_aadl2_PortConnectionEnd_ConnectionEnd = Generalization(general=ConnectionEnd, specific=aadl2_PortConnectionEnd)
gen_aadl2_DataPort_Port = Generalization(general=Port, specific=aadl2_DataPort)
gen_aadl2_DataPort_Context = Generalization(general=Context, specific=aadl2_DataPort)
gen_aadl2_DataPort_Data = Generalization(general=Data, specific=aadl2_DataPort)
gen_aadl2_DataPort_ParameterConnectionEnd = Generalization(general=ParameterConnectionEnd, specific=aadl2_DataPort)
gen_aadl2_Port_DirectedFeature = Generalization(general=DirectedFeature, specific=aadl2_Port)
gen_aadl2_Port_PortConnectionEnd = Generalization(general=PortConnectionEnd, specific=aadl2_Port)
gen_aadl2_Port_TriggerPort = Generalization(general=TriggerPort, specific=aadl2_Port)
gen_aadl2_EventDataPort_Port = Generalization(general=Port, specific=aadl2_EventDataPort)
gen_aadl2_EventDataPort_Context = Generalization(general=Context, specific=aadl2_EventDataPort)
gen_aadl2_EventDataPort_Data = Generalization(general=Data, specific=aadl2_EventDataPort)
gen_aadl2_EventDataPort_ParameterConnectionEnd = Generalization(general=ParameterConnectionEnd, specific=aadl2_EventDataPort)
gen_aadl2_EventPort_Port = Generalization(general=Port, specific=aadl2_EventPort)
gen_aadl2_Parameter_DirectedFeature = Generalization(general=DirectedFeature, specific=aadl2_Parameter)
gen_aadl2_Parameter_Context = Generalization(general=Context, specific=aadl2_Parameter)
gen_aadl2_Parameter_ParameterConnectionEnd = Generalization(general=ParameterConnectionEnd, specific=aadl2_Parameter)
gen_aadl2_SubprogramAccess_Access = Generalization(general=Access, specific=aadl2_SubprogramAccess)
gen_aadl2_SubprogramAccess_Subprogram = Generalization(general=Subprogram, specific=aadl2_SubprogramAccess)
gen_aadl2_Subcomponent_StructuralFeature = Generalization(general=StructuralFeature, specific=aadl2_Subcomponent)
gen_aadl2_Subcomponent_ModalElement = Generalization(general=ModalElement, specific=aadl2_Subcomponent)
gen_aadl2_Subcomponent_Context = Generalization(general=Context, specific=aadl2_Subcomponent)
gen_aadl2_Subcomponent_FlowElement = Generalization(general=FlowElement, specific=aadl2_Subcomponent)
gen_aadl2_Subcomponent_ArrayableElement = Generalization(general=ArrayableElement, specific=aadl2_Subcomponent)
gen_aadl2_Subprogram_NamedElement = Generalization(general=NamedElement, specific=aadl2_Subprogram)
gen_aadl2_Subprogram_CalledSubprogram = Generalization(general=CalledSubprogram, specific=aadl2_Subprogram)
gen_aadl2_SubprogramSubcomponentType_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_SubprogramSubcomponentType)
gen_aadl2_SubprogramSubcomponentType_Subprogram = Generalization(general=Subprogram, specific=aadl2_SubprogramSubcomponentType)
gen_aadl2_SubprogramSubcomponentType_FeatureClassifier = Generalization(general=FeatureClassifier, specific=aadl2_SubprogramSubcomponentType)
gen_aadl2_SubprogramGroupAccess_Access = Generalization(general=Access, specific=aadl2_SubprogramGroupAccess)
gen_aadl2_SubprogramGroupAccess_SubprogramGroup = Generalization(general=SubprogramGroup, specific=aadl2_SubprogramGroupAccess)
gen_aadl2_SubprogramGroupAccess_CallContext = Generalization(general=CallContext, specific=aadl2_SubprogramGroupAccess)
gen_aadl2_SubprogramGroup_NamedElement = Generalization(general=NamedElement, specific=aadl2_SubprogramGroup)
gen_aadl2_SubprogramGroupSubcomponentType_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_SubprogramGroupSubcomponentType)
gen_aadl2_SubprogramGroupSubcomponentType_SubprogramGroup = Generalization(general=SubprogramGroup, specific=aadl2_SubprogramGroupSubcomponentType)
gen_aadl2_SubprogramGroupSubcomponentType_FeatureClassifier = Generalization(general=FeatureClassifier, specific=aadl2_SubprogramGroupSubcomponentType)
gen_aadl2_AbstractFeature_DirectedFeature = Generalization(general=DirectedFeature, specific=aadl2_AbstractFeature)
gen_aadl2_AbstractFeature_TriggerPort = Generalization(general=TriggerPort, specific=aadl2_AbstractFeature)
gen_aadl2_FeaturePrototype_Prototype = Generalization(general=Prototype, specific=aadl2_FeaturePrototype)
gen_aadl2_FeatureGroupPrototype_Prototype = Generalization(general=Prototype, specific=aadl2_FeatureGroupPrototype)
gen_aadl2_FeatureGroupPrototype_FeatureType = Generalization(general=FeatureType, specific=aadl2_FeatureGroupPrototype)
gen_aadl2_ModeBinding_Element = Generalization(general=Element, specific=aadl2_ModeBinding)
gen_aadl2_FlowImplementation_ModalPath = Generalization(general=ModalPath, specific=aadl2_FlowImplementation)
gen_aadl2_FlowImplementation_ClassifierFeature = Generalization(general=ClassifierFeature, specific=aadl2_FlowImplementation)
gen_aadl2_FlowImplementation_Flow = Generalization(general=Flow, specific=aadl2_FlowImplementation)
gen_aadl2_FlowSegment_Element = Generalization(general=Element, specific=aadl2_FlowSegment)
gen_aadl2_Connection_StructuralFeature = Generalization(general=StructuralFeature, specific=aadl2_Connection)
gen_aadl2_Connection_ModalPath = Generalization(general=ModalPath, specific=aadl2_Connection)
gen_aadl2_Connection_FlowElement = Generalization(general=FlowElement, specific=aadl2_Connection)
gen_aadl2_EndToEndFlowSegment_Element = Generalization(general=Element, specific=aadl2_EndToEndFlowSegment)
gen_aadl2_ConnectedElement_Element = Generalization(general=Element, specific=aadl2_ConnectedElement)
gen_aadl2_ImplementationExtension_Generalization = Generalization(general=Generalization, specific=aadl2_ImplementationExtension)
gen_aadl2_Realization_Generalization = Generalization(general=Generalization, specific=aadl2_Realization)
gen_aadl2_EndToEndFlow_FlowFeature = Generalization(general=FlowFeature, specific=aadl2_EndToEndFlow)
gen_aadl2_EndToEndFlow_ModalPath = Generalization(general=ModalPath, specific=aadl2_EndToEndFlow)
gen_aadl2_EndToEndFlow_EndToEndFlowElement = Generalization(general=EndToEndFlowElement, specific=aadl2_EndToEndFlow)
gen_aadl2_ProcessorFeature_StructuralFeature = Generalization(general=StructuralFeature, specific=aadl2_ProcessorFeature)
gen_aadl2_ProcessorFeature_ModalElement = Generalization(general=ModalElement, specific=aadl2_ProcessorFeature)
gen_aadl2_AbstractSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_AbstractSubcomponent)
gen_aadl2_AbstractSubcomponent_Abstract = Generalization(general=Abstract, specific=aadl2_AbstractSubcomponent)
gen_aadl2_Abstract_NamedElement = Generalization(general=NamedElement, specific=aadl2_Abstract)
gen_aadl2_AbstractSubcomponentType_Abstract = Generalization(general=Abstract, specific=aadl2_AbstractSubcomponentType)
gen_aadl2_AbstractSubcomponentType_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_AbstractSubcomponentType)
gen_aadl2_AccessConnection_Connection = Generalization(general=Connection, specific=aadl2_AccessConnection)
gen_aadl2_ParameterConnection_Connection = Generalization(general=Connection, specific=aadl2_ParameterConnection)
gen_aadl2_PortConnection_Connection = Generalization(general=Connection, specific=aadl2_PortConnection)
gen_aadl2_FeatureConnection_Connection = Generalization(general=Connection, specific=aadl2_FeatureConnection)
gen_aadl2_FeatureGroupConnection_Connection = Generalization(general=Connection, specific=aadl2_FeatureGroupConnection)
gen_aadl2_SubprogramProxy_ProcessorFeature = Generalization(general=ProcessorFeature, specific=aadl2_SubprogramProxy)
gen_aadl2_SubprogramProxy_AccessConnectionEnd = Generalization(general=AccessConnectionEnd, specific=aadl2_SubprogramProxy)
gen_aadl2_SubprogramProxy_CalledSubprogram = Generalization(general=CalledSubprogram, specific=aadl2_SubprogramProxy)
gen_aadl2_InternalFeature_StructuralFeature = Generalization(general=StructuralFeature, specific=aadl2_InternalFeature)
gen_aadl2_InternalFeature_ModalElement = Generalization(general=ModalElement, specific=aadl2_InternalFeature)
gen_aadl2_InternalFeature_FeatureConnectionEnd = Generalization(general=FeatureConnectionEnd, specific=aadl2_InternalFeature)
gen_aadl2_InternalFeature_PortConnectionEnd = Generalization(general=PortConnectionEnd, specific=aadl2_InternalFeature)
gen_aadl2_InternalFeature_TriggerPort = Generalization(general=TriggerPort, specific=aadl2_InternalFeature)
gen_aadl2_EventSource_InternalFeature = Generalization(general=InternalFeature, specific=aadl2_EventSource)
gen_aadl2_EventDataSource_InternalFeature = Generalization(general=InternalFeature, specific=aadl2_EventDataSource)
gen_aadl2_DataClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_DataClassifier)
gen_aadl2_DataClassifier_DataSubcomponentType = Generalization(general=DataSubcomponentType, specific=aadl2_DataClassifier)
gen_aadl2_PortProxy_ProcessorFeature = Generalization(general=ProcessorFeature, specific=aadl2_PortProxy)
gen_aadl2_PortProxy_FeatureConnectionEnd = Generalization(general=FeatureConnectionEnd, specific=aadl2_PortProxy)
gen_aadl2_PortProxy_PortConnectionEnd = Generalization(general=PortConnectionEnd, specific=aadl2_PortProxy)
gen_aadl2_PortProxy_TriggerPort = Generalization(general=TriggerPort, specific=aadl2_PortProxy)
gen_aadl2_PublicPackageSection_PackageSection = Generalization(general=PackageSection, specific=aadl2_PublicPackageSection)
gen_aadl2_SubprogramClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_SubprogramClassifier)
gen_aadl2_SubprogramClassifier_SubprogramSubcomponentType = Generalization(general=SubprogramSubcomponentType, specific=aadl2_SubprogramClassifier)
gen_aadl2_AnnexLibrary_NamedElement = Generalization(general=NamedElement, specific=aadl2_AnnexLibrary)
gen_aadl2_DefaultAnnexLibrary_AnnexLibrary = Generalization(general=AnnexLibrary, specific=aadl2_DefaultAnnexLibrary)
gen_aadl2_DefaultAnnexSubclause_AnnexSubclause = Generalization(general=AnnexSubclause, specific=aadl2_DefaultAnnexSubclause)
gen_aadl2_PackageRename_NamedElement = Generalization(general=NamedElement, specific=aadl2_PackageRename)
gen_aadl2_PackageSection_Namespace = Generalization(general=Namespace, specific=aadl2_PackageSection)
gen_aadl2_FeatureGroupTypeRename_NamedElement = Generalization(general=NamedElement, specific=aadl2_FeatureGroupTypeRename)
gen_aadl2_AadlPackage_ModelUnit = Generalization(general=ModelUnit, specific=aadl2_AadlPackage)
gen_aadl2_ModelUnit_NamedElement = Generalization(general=NamedElement, specific=aadl2_ModelUnit)
gen_aadl2_PrivatePackageSection_PackageSection = Generalization(general=PackageSection, specific=aadl2_PrivatePackageSection)
gen_aadl2_ComponentTypeRename_NamedElement = Generalization(general=NamedElement, specific=aadl2_ComponentTypeRename)
gen_aadl2_ComponentPrototypeBinding_PrototypeBinding = Generalization(general=PrototypeBinding, specific=aadl2_ComponentPrototypeBinding)
gen_aadl2_ComponentPrototypeActual_ArrayableElement = Generalization(general=ArrayableElement, specific=aadl2_ComponentPrototypeActual)
gen_aadl2_FeatureGroupPrototypeBinding_PrototypeBinding = Generalization(general=PrototypeBinding, specific=aadl2_FeatureGroupPrototypeBinding)
gen_aadl2_FeatureGroupPrototypeActual_FeaturePrototypeActual = Generalization(general=FeaturePrototypeActual, specific=aadl2_FeatureGroupPrototypeActual)
gen_aadl2_FeaturePrototypeReference_FeaturePrototypeActual = Generalization(general=FeaturePrototypeActual, specific=aadl2_FeaturePrototypeReference)
gen_aadl2_FeaturePrototypeActual_ArrayableElement = Generalization(general=ArrayableElement, specific=aadl2_FeaturePrototypeActual)
gen_aadl2_FeaturePrototypeBinding_PrototypeBinding = Generalization(general=PrototypeBinding, specific=aadl2_FeaturePrototypeBinding)
gen_aadl2_AccessSpecification_FeaturePrototypeActual = Generalization(general=FeaturePrototypeActual, specific=aadl2_AccessSpecification)
gen_aadl2_PortSpecification_FeaturePrototypeActual = Generalization(general=FeaturePrototypeActual, specific=aadl2_PortSpecification)
gen_aadl2_SubprogramCallSequence_BehavioralFeature = Generalization(general=BehavioralFeature, specific=aadl2_SubprogramCallSequence)
gen_aadl2_SubprogramCallSequence_ModalElement = Generalization(general=ModalElement, specific=aadl2_SubprogramCallSequence)
gen_aadl2_SubprogramCall_BehavioralFeature = Generalization(general=BehavioralFeature, specific=aadl2_SubprogramCall)
gen_aadl2_SubprogramCall_Context = Generalization(general=Context, specific=aadl2_SubprogramCall)
gen_aadl2_BehavioredImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_BehavioredImplementation)
gen_aadl2_AbstractType_ComponentType = Generalization(general=ComponentType, specific=aadl2_AbstractType)
gen_aadl2_AbstractType_AbstractClassifier = Generalization(general=AbstractClassifier, specific=aadl2_AbstractType)
gen_aadl2_AbstractType_CallContext = Generalization(general=CallContext, specific=aadl2_AbstractType)
gen_aadl2_VirtualProcessor_NamedElement = Generalization(general=NamedElement, specific=aadl2_VirtualProcessor)
gen_aadl2_VirtualBusSubcomponentType_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_VirtualBusSubcomponentType)
gen_aadl2_VirtualBusSubcomponentType_VirtualBus = Generalization(general=VirtualBus, specific=aadl2_VirtualBusSubcomponentType)
gen_aadl2_AbstractClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_AbstractClassifier)
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
gen_aadl2_AbstractClassifier_ThreadGroupSubcomponentType = Generalization(general=ThreadGroupSubcomponentType, specific=aadl2_AbstractClassifier)
gen_aadl2_AbstractClassifier_ThreadSubcomponentType = Generalization(general=ThreadSubcomponentType, specific=aadl2_AbstractClassifier)
gen_aadl2_AbstractClassifier_VirtualBusSubcomponentType = Generalization(general=VirtualBusSubcomponentType, specific=aadl2_AbstractClassifier)
gen_aadl2_AbstractClassifier_VirtualProcessorSubcomponentType = Generalization(general=VirtualProcessorSubcomponentType, specific=aadl2_AbstractClassifier)
gen_aadl2_VirtualProcessorSubcomponentType_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_VirtualProcessorSubcomponentType)
gen_aadl2_VirtualProcessorSubcomponentType_VirtualProcessor = Generalization(general=VirtualProcessor, specific=aadl2_VirtualProcessorSubcomponentType)
gen_aadl2_AbstractImplementation_BehavioredImplementation = Generalization(general=BehavioredImplementation, specific=aadl2_AbstractImplementation)
gen_aadl2_AbstractImplementation_AbstractClassifier = Generalization(general=AbstractClassifier, specific=aadl2_AbstractImplementation)
gen_aadl2_VirtualBus_NamedElement = Generalization(general=NamedElement, specific=aadl2_VirtualBus)
gen_aadl2_ThreadGroupSubcomponentType_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_ThreadGroupSubcomponentType)
gen_aadl2_ThreadGroupSubcomponentType_ThreadGroup = Generalization(general=ThreadGroup, specific=aadl2_ThreadGroupSubcomponentType)
gen_aadl2_ThreadGroup_NamedElement = Generalization(general=NamedElement, specific=aadl2_ThreadGroup)
gen_aadl2_ThreadSubcomponentType_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_ThreadSubcomponentType)
gen_aadl2_ThreadSubcomponentType_Thread = Generalization(general=Thread, specific=aadl2_ThreadSubcomponentType)
gen_aadl2_Thread_NamedElement = Generalization(general=NamedElement, specific=aadl2_Thread)
gen_aadl2_SystemSubcomponentType_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_SystemSubcomponentType)
gen_aadl2_SystemSubcomponentType_System = Generalization(general=System, specific=aadl2_SystemSubcomponentType)
gen_aadl2_System_NamedElement = Generalization(general=NamedElement, specific=aadl2_System)
gen_aadl2_ProcessSubcomponentType_Process = Generalization(general=Process, specific=aadl2_ProcessSubcomponentType)
gen_aadl2_ProcessSubcomponentType_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_ProcessSubcomponentType)
gen_aadl2_Process_NamedElement = Generalization(general=NamedElement, specific=aadl2_Process)
gen_aadl2_MemorySubcomponentType_Memory = Generalization(general=Memory, specific=aadl2_MemorySubcomponentType)
gen_aadl2_MemorySubcomponentType_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_MemorySubcomponentType)
gen_aadl2_Memory_NamedElement = Generalization(general=NamedElement, specific=aadl2_Memory)
gen_aadl2_DeviceSubcomponentType_Device = Generalization(general=Device, specific=aadl2_DeviceSubcomponentType)
gen_aadl2_DeviceSubcomponentType_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_DeviceSubcomponentType)
gen_aadl2_Device_NamedElement = Generalization(general=NamedElement, specific=aadl2_Device)
gen_aadl2_ProcessorSubcomponentType_Processor = Generalization(general=Processor, specific=aadl2_ProcessorSubcomponentType)
gen_aadl2_ProcessorSubcomponentType_SubcomponentType = Generalization(general=SubcomponentType, specific=aadl2_ProcessorSubcomponentType)
gen_aadl2_Processor_NamedElement = Generalization(general=NamedElement, specific=aadl2_Processor)
gen_aadl2_MemorySubcomponent_Memory = Generalization(general=Memory, specific=aadl2_MemorySubcomponent)
gen_aadl2_ProcessSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_ProcessSubcomponent)
gen_aadl2_ProcessSubcomponent_Process = Generalization(general=Process, specific=aadl2_ProcessSubcomponent)
gen_aadl2_BusSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_BusSubcomponent)
gen_aadl2_BusSubcomponent_AccessConnectionEnd = Generalization(general=AccessConnectionEnd, specific=aadl2_BusSubcomponent)
gen_aadl2_BusSubcomponent_Bus = Generalization(general=Bus, specific=aadl2_BusSubcomponent)
gen_aadl2_DataSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_DataSubcomponent)
gen_aadl2_DataSubcomponent_AccessConnectionEnd = Generalization(general=AccessConnectionEnd, specific=aadl2_DataSubcomponent)
gen_aadl2_DataSubcomponent_Data = Generalization(general=Data, specific=aadl2_DataSubcomponent)
gen_aadl2_DataSubcomponent_ParameterConnectionEnd = Generalization(general=ParameterConnectionEnd, specific=aadl2_DataSubcomponent)
gen_aadl2_DataSubcomponent_PortConnectionEnd = Generalization(general=PortConnectionEnd, specific=aadl2_DataSubcomponent)
gen_aadl2_DeviceSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_DeviceSubcomponent)
gen_aadl2_DeviceSubcomponent_Device = Generalization(general=Device, specific=aadl2_DeviceSubcomponent)
gen_aadl2_MemorySubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_MemorySubcomponent)
gen_aadl2_ThreadGroupSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_ThreadGroupSubcomponent)
gen_aadl2_ThreadGroupSubcomponent_ThreadGroup = Generalization(general=ThreadGroup, specific=aadl2_ThreadGroupSubcomponent)
gen_aadl2_ProcessorSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_ProcessorSubcomponent)
gen_aadl2_ProcessorSubcomponent_Processor = Generalization(general=Processor, specific=aadl2_ProcessorSubcomponent)
gen_aadl2_SystemSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_SystemSubcomponent)
gen_aadl2_SystemSubcomponent_System = Generalization(general=System, specific=aadl2_SystemSubcomponent)
gen_aadl2_SubprogramSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_SubprogramSubcomponent)
gen_aadl2_SubprogramSubcomponent_AccessConnectionEnd = Generalization(general=AccessConnectionEnd, specific=aadl2_SubprogramSubcomponent)
gen_aadl2_SubprogramSubcomponent_Subprogram = Generalization(general=Subprogram, specific=aadl2_SubprogramSubcomponent)
gen_aadl2_SubprogramGroupSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_SubprogramGroupSubcomponent)
gen_aadl2_SubprogramGroupSubcomponent_AccessConnectionEnd = Generalization(general=AccessConnectionEnd, specific=aadl2_SubprogramGroupSubcomponent)
gen_aadl2_SubprogramGroupSubcomponent_SubprogramGroup = Generalization(general=SubprogramGroup, specific=aadl2_SubprogramGroupSubcomponent)
gen_aadl2_SubprogramGroupSubcomponent_CallContext = Generalization(general=CallContext, specific=aadl2_SubprogramGroupSubcomponent)
gen_aadl2_ThreadSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_ThreadSubcomponent)
gen_aadl2_ThreadSubcomponent_Thread = Generalization(general=Thread, specific=aadl2_ThreadSubcomponent)
gen_aadl2_VirtualBusSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_VirtualBusSubcomponent)
gen_aadl2_VirtualBusSubcomponent_VirtualBus = Generalization(general=VirtualBus, specific=aadl2_VirtualBusSubcomponent)
gen_aadl2_VirtualProcessorSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_VirtualProcessorSubcomponent)
gen_aadl2_VirtualProcessorSubcomponent_VirtualProcessor = Generalization(general=VirtualProcessor, specific=aadl2_VirtualProcessorSubcomponent)
gen_aadl2_AbstractPrototype_ComponentPrototype = Generalization(general=ComponentPrototype, specific=aadl2_AbstractPrototype)
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
gen_aadl2_BusClassifier_BusSubcomponentType = Generalization(general=BusSubcomponentType, specific=aadl2_BusClassifier)
gen_aadl2_BusType_ComponentType = Generalization(general=ComponentType, specific=aadl2_BusType)
gen_aadl2_BusType_BusClassifier = Generalization(general=BusClassifier, specific=aadl2_BusType)
gen_aadl2_DataImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_DataImplementation)
gen_aadl2_DataImplementation_DataClassifier = Generalization(general=DataClassifier, specific=aadl2_DataImplementation)
gen_aadl2_BusImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_BusImplementation)
gen_aadl2_BusImplementation_BusClassifier = Generalization(general=BusClassifier, specific=aadl2_BusImplementation)
gen_aadl2_BusPrototype_ComponentPrototype = Generalization(general=ComponentPrototype, specific=aadl2_BusPrototype)
gen_aadl2_BusPrototype_BusSubcomponentType = Generalization(general=BusSubcomponentType, specific=aadl2_BusPrototype)
gen_aadl2_DataType_ComponentType = Generalization(general=ComponentType, specific=aadl2_DataType)
gen_aadl2_DataType_DataClassifier = Generalization(general=DataClassifier, specific=aadl2_DataType)
gen_aadl2_DataType_CallContext = Generalization(general=CallContext, specific=aadl2_DataType)
gen_aadl2_DeviceImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_DeviceImplementation)
gen_aadl2_DeviceImplementation_DeviceClassifier = Generalization(general=DeviceClassifier, specific=aadl2_DeviceImplementation)
gen_aadl2_DataPrototype_ComponentPrototype = Generalization(general=ComponentPrototype, specific=aadl2_DataPrototype)
gen_aadl2_DataPrototype_DataSubcomponentType = Generalization(general=DataSubcomponentType, specific=aadl2_DataPrototype)
gen_aadl2_DeviceClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_DeviceClassifier)
gen_aadl2_DeviceClassifier_DeviceSubcomponentType = Generalization(general=DeviceSubcomponentType, specific=aadl2_DeviceClassifier)
gen_aadl2_DeviceType_ComponentType = Generalization(general=ComponentType, specific=aadl2_DeviceType)
gen_aadl2_DeviceType_DeviceClassifier = Generalization(general=DeviceClassifier, specific=aadl2_DeviceType)
gen_aadl2_DevicePrototype_ComponentPrototype = Generalization(general=ComponentPrototype, specific=aadl2_DevicePrototype)
gen_aadl2_DevicePrototype_DeviceSubcomponentType = Generalization(general=DeviceSubcomponentType, specific=aadl2_DevicePrototype)
gen_aadl2_MemoryClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_MemoryClassifier)
gen_aadl2_MemoryClassifier_MemorySubcomponentType = Generalization(general=MemorySubcomponentType, specific=aadl2_MemoryClassifier)
gen_aadl2_MemoryType_ComponentType = Generalization(general=ComponentType, specific=aadl2_MemoryType)
gen_aadl2_MemoryType_MemoryClassifier = Generalization(general=MemoryClassifier, specific=aadl2_MemoryType)
gen_aadl2_MemoryPrototype_ComponentPrototype = Generalization(general=ComponentPrototype, specific=aadl2_MemoryPrototype)
gen_aadl2_MemoryPrototype_MemorySubcomponentType = Generalization(general=MemorySubcomponentType, specific=aadl2_MemoryPrototype)
gen_aadl2_SubprogramType_ComponentType = Generalization(general=ComponentType, specific=aadl2_SubprogramType)
gen_aadl2_SubprogramType_SubprogramClassifier = Generalization(general=SubprogramClassifier, specific=aadl2_SubprogramType)
gen_aadl2_SubprogramType_CallContext = Generalization(general=CallContext, specific=aadl2_SubprogramType)
gen_aadl2_MemoryImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_MemoryImplementation)
gen_aadl2_MemoryImplementation_MemoryClassifier = Generalization(general=MemoryClassifier, specific=aadl2_MemoryImplementation)
gen_aadl2_SubprogramGroupClassifier_SubprogramGroupSubcomponentType = Generalization(general=SubprogramGroupSubcomponentType, specific=aadl2_SubprogramGroupClassifier)
gen_aadl2_SubprogramGroupType_ComponentType = Generalization(general=ComponentType, specific=aadl2_SubprogramGroupType)
gen_aadl2_SubprogramGroupType_SubprogramGroupClassifier = Generalization(general=SubprogramGroupClassifier, specific=aadl2_SubprogramGroupType)
gen_aadl2_SubprogramGroupType_CallContext = Generalization(general=CallContext, specific=aadl2_SubprogramGroupType)
gen_aadl2_SubprogramGroupImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_SubprogramGroupImplementation)
gen_aadl2_SubprogramGroupImplementation_SubprogramGroupClassifier = Generalization(general=SubprogramGroupClassifier, specific=aadl2_SubprogramGroupImplementation)
gen_aadl2_SubprogramImplementation_BehavioredImplementation = Generalization(general=BehavioredImplementation, specific=aadl2_SubprogramImplementation)
gen_aadl2_SubprogramImplementation_SubprogramClassifier = Generalization(general=SubprogramClassifier, specific=aadl2_SubprogramImplementation)
gen_aadl2_SubprogramPrototype_ComponentPrototype = Generalization(general=ComponentPrototype, specific=aadl2_SubprogramPrototype)
gen_aadl2_SubprogramPrototype_SubprogramSubcomponentType = Generalization(general=SubprogramSubcomponentType, specific=aadl2_SubprogramPrototype)
gen_aadl2_SubprogramGroupClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_SubprogramGroupClassifier)
gen_aadl2_SubprogramGroupPrototype_ComponentPrototype = Generalization(general=ComponentPrototype, specific=aadl2_SubprogramGroupPrototype)
gen_aadl2_SubprogramGroupPrototype_SubprogramGroupSubcomponentType = Generalization(general=SubprogramGroupSubcomponentType, specific=aadl2_SubprogramGroupPrototype)
gen_aadl2_SystemClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_SystemClassifier)
gen_aadl2_SystemClassifier_SystemSubcomponentType = Generalization(general=SystemSubcomponentType, specific=aadl2_SystemClassifier)
gen_aadl2_SystemType_ComponentType = Generalization(general=ComponentType, specific=aadl2_SystemType)
gen_aadl2_SystemType_SystemClassifier = Generalization(general=SystemClassifier, specific=aadl2_SystemType)
gen_aadl2_SystemImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_SystemImplementation)
gen_aadl2_SystemImplementation_SystemClassifier = Generalization(general=SystemClassifier, specific=aadl2_SystemImplementation)
gen_aadl2_ProcessorClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_ProcessorClassifier)
gen_aadl2_ProcessorClassifier_ProcessorSubcomponentType = Generalization(general=ProcessorSubcomponentType, specific=aadl2_ProcessorClassifier)
gen_aadl2_ProcessorType_ComponentType = Generalization(general=ComponentType, specific=aadl2_ProcessorType)
gen_aadl2_ProcessorType_ProcessorClassifier = Generalization(general=ProcessorClassifier, specific=aadl2_ProcessorType)
gen_aadl2_SystemPrototype_ComponentPrototype = Generalization(general=ComponentPrototype, specific=aadl2_SystemPrototype)
gen_aadl2_SystemPrototype_SystemSubcomponentType = Generalization(general=SystemSubcomponentType, specific=aadl2_SystemPrototype)
gen_aadl2_ProcessorPrototype_ComponentPrototype = Generalization(general=ComponentPrototype, specific=aadl2_ProcessorPrototype)
gen_aadl2_ProcessorPrototype_ProcessorSubcomponentType = Generalization(general=ProcessorSubcomponentType, specific=aadl2_ProcessorPrototype)
gen_aadl2_ProcessClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_ProcessClassifier)
gen_aadl2_ProcessClassifier_ProcessSubcomponentType = Generalization(general=ProcessSubcomponentType, specific=aadl2_ProcessClassifier)
gen_aadl2_ProcessorImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_ProcessorImplementation)
gen_aadl2_ProcessorImplementation_ProcessorClassifier = Generalization(general=ProcessorClassifier, specific=aadl2_ProcessorImplementation)
gen_aadl2_ProcessImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_ProcessImplementation)
gen_aadl2_ProcessImplementation_ProcessClassifier = Generalization(general=ProcessClassifier, specific=aadl2_ProcessImplementation)
gen_aadl2_ProcessType_ComponentType = Generalization(general=ComponentType, specific=aadl2_ProcessType)
gen_aadl2_ProcessType_ProcessClassifier = Generalization(general=ProcessClassifier, specific=aadl2_ProcessType)
gen_aadl2_ThreadPrototype_ComponentPrototype = Generalization(general=ComponentPrototype, specific=aadl2_ThreadPrototype)
gen_aadl2_ThreadPrototype_ThreadSubcomponentType = Generalization(general=ThreadSubcomponentType, specific=aadl2_ThreadPrototype)
gen_aadl2_ProcessPrototype_ComponentPrototype = Generalization(general=ComponentPrototype, specific=aadl2_ProcessPrototype)
gen_aadl2_ProcessPrototype_ProcessSubcomponentType = Generalization(general=ProcessSubcomponentType, specific=aadl2_ProcessPrototype)
gen_aadl2_ThreadClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_ThreadClassifier)
gen_aadl2_ThreadClassifier_ThreadSubcomponentType = Generalization(general=ThreadSubcomponentType, specific=aadl2_ThreadClassifier)
gen_aadl2_ThreadType_ComponentType = Generalization(general=ComponentType, specific=aadl2_ThreadType)
gen_aadl2_ThreadType_ThreadClassifier = Generalization(general=ThreadClassifier, specific=aadl2_ThreadType)
gen_aadl2_ThreadImplementation_BehavioredImplementation = Generalization(general=BehavioredImplementation, specific=aadl2_ThreadImplementation)
gen_aadl2_ThreadImplementation_ThreadClassifier = Generalization(general=ThreadClassifier, specific=aadl2_ThreadImplementation)
gen_aadl2_ThreadGroupClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_ThreadGroupClassifier)
gen_aadl2_ThreadGroupClassifier_ThreadGroupSubcomponentType = Generalization(general=ThreadGroupSubcomponentType, specific=aadl2_ThreadGroupClassifier)
gen_aadl2_ThreadGroupType_ComponentType = Generalization(general=ComponentType, specific=aadl2_ThreadGroupType)
gen_aadl2_ThreadGroupType_ThreadGroupClassifier = Generalization(general=ThreadGroupClassifier, specific=aadl2_ThreadGroupType)
gen_aadl2_ThreadGroupImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_ThreadGroupImplementation)
gen_aadl2_ThreadGroupImplementation_ThreadGroupClassifier = Generalization(general=ThreadGroupClassifier, specific=aadl2_ThreadGroupImplementation)
gen_aadl2_ThreadGroupPrototype_ComponentPrototype = Generalization(general=ComponentPrototype, specific=aadl2_ThreadGroupPrototype)
gen_aadl2_ThreadGroupPrototype_ThreadGroupSubcomponentType = Generalization(general=ThreadGroupSubcomponentType, specific=aadl2_ThreadGroupPrototype)
gen_aadl2_VirtualBusClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_VirtualBusClassifier)
gen_aadl2_VirtualBusClassifier_VirtualBusSubcomponentType = Generalization(general=VirtualBusSubcomponentType, specific=aadl2_VirtualBusClassifier)
gen_aadl2_VirtualBusType_ComponentType = Generalization(general=ComponentType, specific=aadl2_VirtualBusType)
gen_aadl2_VirtualBusType_VirtualBusClassifier = Generalization(general=VirtualBusClassifier, specific=aadl2_VirtualBusType)
gen_aadl2_VirtualProcessorImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_VirtualProcessorImplementation)
gen_aadl2_VirtualProcessorImplementation_VirtualProcessorClassifier = Generalization(general=VirtualProcessorClassifier, specific=aadl2_VirtualProcessorImplementation)
gen_aadl2_VirtualBusImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_VirtualBusImplementation)
gen_aadl2_VirtualBusImplementation_VirtualBusClassifier = Generalization(general=VirtualBusClassifier, specific=aadl2_VirtualBusImplementation)
gen_aadl2_VirtualBusPrototype_ComponentPrototype = Generalization(general=ComponentPrototype, specific=aadl2_VirtualBusPrototype)
gen_aadl2_VirtualBusPrototype_VirtualBusSubcomponentType = Generalization(general=VirtualBusSubcomponentType, specific=aadl2_VirtualBusPrototype)
gen_aadl2_VirtualProcessorClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_VirtualProcessorClassifier)
gen_aadl2_VirtualProcessorClassifier_VirtualProcessorSubcomponentType = Generalization(general=VirtualProcessorSubcomponentType, specific=aadl2_VirtualProcessorClassifier)
gen_aadl2_VirtualProcessorType_ComponentType = Generalization(general=ComponentType, specific=aadl2_VirtualProcessorType)
gen_aadl2_VirtualProcessorType_VirtualProcessorClassifier = Generalization(general=VirtualProcessorClassifier, specific=aadl2_VirtualProcessorType)
gen_aadl2_StringLiteral_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_StringLiteral)
gen_aadl2_VirtualProcessorPrototype_ComponentPrototype = Generalization(general=ComponentPrototype, specific=aadl2_VirtualProcessorPrototype)
gen_aadl2_VirtualProcessorPrototype_VirtualProcessorSubcomponentType = Generalization(general=VirtualProcessorSubcomponentType, specific=aadl2_VirtualProcessorPrototype)
gen_aadl2_BasicPropertyAssociation_Element = Generalization(general=Element, specific=aadl2_BasicPropertyAssociation)
gen_aadl2_PropertyConstant_TypedElement = Generalization(general=TypedElement, specific=aadl2_PropertyConstant)
gen_aadl2_PropertyConstant_AbstractNamedValue = Generalization(general=AbstractNamedValue, specific=aadl2_PropertyConstant)
gen_aadl2_PropertyConstant_ArraySizeProperty = Generalization(general=ArraySizeProperty, specific=aadl2_PropertyConstant)
gen_aadl2_ReferenceValue_ContainedNamedElement = Generalization(general=ContainedNamedElement, specific=aadl2_ReferenceValue)
gen_aadl2_ReferenceValue_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_ReferenceValue)
gen_aadl2_PropertyValue_PropertyExpression = Generalization(general=PropertyExpression, specific=aadl2_PropertyValue)
gen_aadl2_NumberValue_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_NumberValue)
gen_aadl2_UnitLiteral_EnumerationLiteral = Generalization(general=EnumerationLiteral, specific=aadl2_UnitLiteral)
gen_aadl2_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=aadl2_EnumerationLiteral)
gen_aadl2_EnumerationLiteral_AbstractNamedValue = Generalization(general=AbstractNamedValue, specific=aadl2_EnumerationLiteral)
gen_aadl2_ClassifierValue_PropertyOwner = Generalization(general=PropertyOwner, specific=aadl2_ClassifierValue)
gen_aadl2_ClassifierValue_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_ClassifierValue)
gen_aadl2_BooleanLiteral_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_BooleanLiteral)
gen_aadl2_RangeValue_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_RangeValue)
gen_aadl2_IntegerLiteral_NumberValue = Generalization(general=NumberValue, specific=aadl2_IntegerLiteral)
gen_aadl2_RealLiteral_NumberValue = Generalization(general=NumberValue, specific=aadl2_RealLiteral)
gen_aadl2_Operation_PropertyExpression = Generalization(general=PropertyExpression, specific=aadl2_Operation)
gen_aadl2_RecordValue_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_RecordValue)
gen_aadl2_ComputedValue_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_ComputedValue)
gen_aadl2_ListValue_PropertyExpression = Generalization(general=PropertyExpression, specific=aadl2_ListValue)
gen_aadl2_NamedValue_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_NamedValue)
gen_aadl2_PropertySet_Namespace = Generalization(general=Namespace, specific=aadl2_PropertySet)
gen_aadl2_PropertySet_ModelUnit = Generalization(general=ModelUnit, specific=aadl2_PropertySet)
gen_aadl2_GlobalNamespace_Namespace = Generalization(general=Namespace, specific=aadl2_GlobalNamespace)
gen_aadl2_NonListType_PropertyType = Generalization(general=PropertyType, specific=aadl2_NonListType)
gen_aadl2_AadlBoolean_NonListType = Generalization(general=NonListType, specific=aadl2_AadlBoolean)
gen_aadl2_AadlString_NonListType = Generalization(general=NonListType, specific=aadl2_AadlString)
gen_aadl2_AadlInteger_NumberType = Generalization(general=NumberType, specific=aadl2_AadlInteger)
gen_aadl2_NumberType_NonListType = Generalization(general=NonListType, specific=aadl2_NumberType)
gen_aadl2_UnitsType_EnumerationType = Generalization(general=EnumerationType, specific=aadl2_UnitsType)
gen_aadl2_EnumerationType_Namespace = Generalization(general=Namespace, specific=aadl2_EnumerationType)
gen_aadl2_EnumerationType_NonListType = Generalization(general=NonListType, specific=aadl2_EnumerationType)
gen_aadl2_NumericRange_Element = Generalization(general=Element, specific=aadl2_NumericRange)
gen_aadl2_AadlReal_NumberType = Generalization(general=NumberType, specific=aadl2_AadlReal)
gen_aadl2_ClassifierType_NonListType = Generalization(general=NonListType, specific=aadl2_ClassifierType)
gen_aadl2_RangeType_NonListType = Generalization(general=NonListType, specific=aadl2_RangeType)
gen_aadl2_RecordType_Namespace = Generalization(general=Namespace, specific=aadl2_RecordType)
gen_aadl2_RecordType_NonListType = Generalization(general=NonListType, specific=aadl2_RecordType)
gen_aadl2_RecordField_BasicProperty = Generalization(general=BasicProperty, specific=aadl2_RecordField)
gen_aadl2_ReferenceType_NonListType = Generalization(general=NonListType, specific=aadl2_ReferenceType)
gen_aadl2_ListType_PropertyType = Generalization(general=PropertyType, specific=aadl2_ListType)

# Domain Model
domain_model = DomainModel(
    name="aadl2",
    types={aadl2_Element, aadl2_Comment, Element, aadl2_Type, NamedElement, aadl2_NamedElement, aadl2_PropertyAssociation, aadl2_PropertyExpression, aadl2_Property, aadl2_ContainedNamedElement, aadl2_Classifier, aadl2_ModalPropertyValue, BasicProperty, AbstractNamedValue, ArraySizeProperty, aadl2_MetaclassReference, aadl2_PropertyOwner, aadl2_BasicProperty, TypedElement, aadl2_PropertyType, aadl2_TypedElement, Type, aadl2_AbstractNamedValue, aadl2_ArraySizeProperty, PropertyOwner, Namespace, aadl2_ClassifierFeature, aadl2_Generalization, aadl2_AnnexSubclause, aadl2_Prototype, aadl2_PrototypeBinding, aadl2_Namespace, ModalElement, DirectedRelationship, aadl2_DirectedRelationship, Relationship, aadl2_Relationship, aadl2_ModalElement, aadl2_Mode, ModeFeature, aadl2_ModeFeature, ClassifierFeature, StructuralFeature, CalledSubprogram, aadl2_StructuralFeature, RefinableElement, aadl2_RefinableElement, aadl2_CalledSubprogram, aadl2_ContainmentPathElement, aadl2_ArrayRange, aadl2_BehavioralFeature, aadl2_ArrayDimension, aadl2_ArraySize, aadl2_ArrayableElement, aadl2_ComponentImplementationReference, aadl2_ComponentImplementation, ComponentClassifier, aadl2_ComponentType, aadl2_Subcomponent, aadl2_FlowImplementation, aadl2_Connection, aadl2_ImplementationExtension, aadl2_Realization, aadl2_EndToEndFlow, aadl2_AbstractSubcomponent, aadl2_InternalFeature, aadl2_AccessConnection, aadl2_ParameterConnection, aadl2_PortConnection, aadl2_FeatureConnection, aadl2_FeatureGroupConnection, aadl2_ProcessorFeature, aadl2_SubprogramProxy, aadl2_EventSource, aadl2_EventDataSource, aadl2_PortProxy, aadl2_SubcomponentType, aadl2_ComponentClassifier, Classifier, SubcomponentType, FeatureClassifier, aadl2_ModeTransition, aadl2_FeatureClassifier, aadl2_ModeTransitionTrigger, aadl2_Context, aadl2_TriggerPort, aadl2_Feature, aadl2_FlowSpecification, aadl2_TypeExtension, aadl2_FeatureGroup, aadl2_AbstractFeature, FeatureConnectionEnd, ArrayableElement, aadl2_ComponentPrototype, aadl2_FeatureConnectionEnd, ConnectionEnd, aadl2_ConnectionEnd, Prototype, FlowFeature, ModalPath, FlowElement, aadl2_FlowEnd, aadl2_FlowFeature, Flow, aadl2_Flow, aadl2_ModalPath, aadl2_FlowElement, EndToEndFlowElement, aadl2_EndToEndFlowElement, Generalization, DirectedFeature, Context, FeatureGroupConnectionEnd, CallContext, aadl2_FeatureGroupConnectionEnd, aadl2_FeatureType, aadl2_FeatureGroupType, aadl2_FeatureGroupPrototype, aadl2_CallContext, aadl2_DirectedFeature, Feature, aadl2_BusAccess, FeatureType, aadl2_GroupExtension, aadl2_DataAccess, aadl2_DataPort, aadl2_EventDataPort, aadl2_EventPort, aadl2_Access, AccessConnectionEnd, aadl2_Parameter, aadl2_SubprogramAccess, aadl2_SubprogramGroupAccess, Access, Bus, aadl2_BusSubcomponentType, aadl2_Data, aadl2_AccessConnectionEnd, aadl2_Bus, Data, ParameterConnectionEnd, PortConnectionEnd, aadl2_DataSubcomponentType, aadl2_ParameterConnectionEnd, aadl2_PortConnectionEnd, aadl2_SubprogramSubcomponentType, Port, aadl2_Port, TriggerPort, Subprogram, aadl2_Subprogram, SubprogramGroup, aadl2_SubprogramGroupSubcomponentType, aadl2_SubprogramGroup, aadl2_FeaturePrototype, aadl2_ModeBinding, aadl2_FlowSegment, aadl2_ConnectedElement, aadl2_EndToEndFlowSegment, Subcomponent, Abstract, aadl2_AbstractSubcomponentType, aadl2_Abstract, Connection, InternalFeature, aadl2_DataClassifier, DataSubcomponentType, ProcessorFeature, aadl2_PublicPackageSection, PackageSection, aadl2_PrivatePackageSection, aadl2_SubprogramClassifier, SubprogramSubcomponentType, aadl2_AnnexLibrary, aadl2_DefaultAnnexLibrary, AnnexLibrary, aadl2_DefaultAnnexSubclause, AnnexSubclause, aadl2_PackageSection, aadl2_PackageRename, aadl2_ComponentTypeRename, aadl2_FeatureGroupTypeRename, aadl2_ModelUnit, aadl2_AadlPackage, ModelUnit, aadl2_ComponentPrototypeBinding, PrototypeBinding, aadl2_ComponentPrototypeActual, aadl2_FeatureGroupPrototypeBinding, aadl2_FeatureGroupPrototypeActual, FeaturePrototypeActual, aadl2_FeaturePrototypeReference, aadl2_FeaturePrototypeActual, aadl2_FeaturePrototypeBinding, aadl2_AccessSpecification, aadl2_PortSpecification, aadl2_SubprogramCallSequence, BehavioralFeature, aadl2_SubprogramCall, aadl2_BehavioredImplementation, ComponentImplementation, aadl2_AbstractType, ComponentType, AbstractClassifier, aadl2_VirtualProcessor, aadl2_VirtualBusSubcomponentType, VirtualBus, aadl2_VirtualBus, aadl2_AbstractClassifier, AbstractSubcomponentType, BusSubcomponentType, DeviceSubcomponentType, MemorySubcomponentType, ProcessorSubcomponentType, ProcessSubcomponentType, SubprogramGroupSubcomponentType, SystemSubcomponentType, ThreadGroupSubcomponentType, ThreadSubcomponentType, VirtualBusSubcomponentType, VirtualProcessorSubcomponentType, aadl2_VirtualProcessorSubcomponentType, VirtualProcessor, aadl2_AbstractImplementation, BehavioredImplementation, aadl2_ThreadGroupSubcomponentType, aadl2_BusSubcomponent, ThreadGroup, aadl2_ThreadGroup, aadl2_ThreadSubcomponentType, Thread, aadl2_Thread, aadl2_SystemSubcomponentType, System, aadl2_System, aadl2_ProcessSubcomponentType, Process, aadl2_Process, aadl2_MemorySubcomponentType, Memory, aadl2_Memory, aadl2_DeviceSubcomponentType, Device, aadl2_Device, aadl2_ProcessorSubcomponentType, Processor, aadl2_Processor, aadl2_ThreadSubcomponent, aadl2_ThreadGroupSubcomponent, aadl2_DataSubcomponent, aadl2_DeviceSubcomponent, aadl2_MemorySubcomponent, aadl2_ProcessSubcomponent, aadl2_ProcessorSubcomponent, aadl2_SystemSubcomponent, aadl2_SubprogramSubcomponent, aadl2_SubprogramGroupSubcomponent, aadl2_VirtualBusSubcomponent, aadl2_VirtualProcessorSubcomponent, aadl2_AbstractPrototype, ComponentPrototype, aadl2_BusClassifier, aadl2_BusType, BusClassifier, aadl2_DataImplementation, aadl2_BusImplementation, aadl2_BusPrototype, aadl2_DataType, DataClassifier, aadl2_DeviceImplementation, aadl2_DataPrototype, aadl2_DeviceClassifier, aadl2_DeviceType, DeviceClassifier, aadl2_DevicePrototype, aadl2_MemoryClassifier, aadl2_MemoryType, MemoryClassifier, aadl2_MemoryPrototype, aadl2_SubprogramType, SubprogramClassifier, aadl2_MemoryImplementation, aadl2_SubprogramGroupType, SubprogramGroupClassifier, aadl2_SubprogramGroupImplementation, aadl2_SubprogramImplementation, aadl2_SubprogramPrototype, aadl2_SubprogramGroupClassifier, aadl2_SubprogramGroupPrototype, aadl2_SystemClassifier, aadl2_SystemType, SystemClassifier, aadl2_SystemImplementation, aadl2_ProcessorClassifier, aadl2_ProcessorType, ProcessorClassifier, aadl2_SystemPrototype, aadl2_ProcessorPrototype, aadl2_ProcessClassifier, aadl2_ProcessorImplementation, aadl2_ProcessImplementation, aadl2_ProcessType, ProcessClassifier, aadl2_ThreadPrototype, aadl2_ProcessPrototype, aadl2_ThreadClassifier, aadl2_ThreadType, ThreadClassifier, aadl2_ThreadImplementation, aadl2_ThreadGroupClassifier, aadl2_ThreadGroupType, ThreadGroupClassifier, aadl2_ThreadGroupImplementation, aadl2_VirtualBusImplementation, aadl2_ThreadGroupPrototype, aadl2_VirtualBusClassifier, aadl2_VirtualBusType, VirtualBusClassifier, aadl2_VirtualProcessorImplementation, aadl2_VirtualBusPrototype, aadl2_VirtualProcessorClassifier, aadl2_VirtualProcessorType, VirtualProcessorClassifier, aadl2_StringLiteral, PropertyValue, aadl2_VirtualProcessorPrototype, aadl2_BasicPropertyAssociation, aadl2_PropertyConstant, aadl2_ReferenceValue, ContainedNamedElement, aadl2_PropertyValue, PropertyExpression, aadl2_NumberValue, aadl2_UnitLiteral, EnumerationLiteral, aadl2_EnumerationLiteral, aadl2_ClassifierValue, aadl2_BooleanLiteral, aadl2_RangeValue, aadl2_IntegerLiteral, NumberValue, aadl2_RealLiteral, aadl2_Operation, aadl2_RecordValue, aadl2_ComputedValue, aadl2_ListValue, aadl2_NamedValue, aadl2_PropertySet, aadl2_NonListType, aadl2_GlobalNamespace, aadl2_NumericRange, PropertyType, aadl2_AadlBoolean, NonListType, aadl2_AadlString, aadl2_AadlInteger, NumberType, aadl2_NumberType, aadl2_UnitsType, aadl2_AadlReal, EnumerationType, aadl2_EnumerationType, aadl2_ClassifierType, aadl2_RangeType, aadl2_RecordType, aadl2_RecordField, aadl2_ReferenceType, aadl2_ListType, FlowKind, DirectionType, AccessType, AccessCategory, PortCategory, ComponentCategory, OperationKind},
    associations={ownedElement1, ownedComment2, ownedPropertyAssociation4, defaultValue13, property5, appliesTo7, inBinding9, ownedValue11, appliesToMetaclass15, appliesToClassifier17, appliesTo20, propertyType22, ownedPropertyType23, type26, classifierFeature27, inheritedMember28, generalization31, general33, ownedAnnexSubclause35, ownedPrototype37, ownedPrototypeBinding39, ownedMember41, member43, featuringClassifier46, general47, specific49, source51, target53, relatedElement56, inMode58, refined60, refinementContext62, refinedElement65, formal67, containmentPathElement70, arrayRange72, namedElement74, ownedValue77, size80, sizeProperty81, arrayDimension83, implementation85, ownedPrototypeBinding86, type89, ownedSubcomponent91, extended94, ownedFlowImplementation96, ownedConnection98, ownedExtension100, ownedRealization102, ownedEndToEndFlow104, ownedAbstractSubcomponent106, ownedInternalFeature120, ownedAccessConnection108, ownedParameterConnection110, ownedPortConnection112, ownedFeatureConnection114, ownedFeatureGroupConnection116, ownedProcessorFeature118, ownedEventSource122, ownedEventDataSource124, ownedPortProxy126, ownedSubprogramProxy128, ownedMode130, ownedModeTransition132, source134, destination137, ownedTrigger140, context142, triggerPort144, ownedFeature146, extended149, ownedFlowSpecification151, ownedExtension153, ownedFeatureGroup155, ownedAbstractFeature157, prototype159, featureClassifier161, refined164, classifier166, constrainingClassifier169, refined173, outEnd175, InEnd177, inModeOrTransition180, context181, feature184, extended187, featureType190, featureGroupType192, featureGroupPrototype194, ownedBusAccess207, ownedFeature196, extended200, inverse203, ownedExtension205, ownedDataAccess209, ownedDataPort211, ownedEventDataPort213, ownedEventPort215, ownedFeatureGroup217, ownedParameter220, ownedSubprogramAccess222, ownedSubprogramGroupAccess224, ownedAbstractFeature226, extended229, busFeatureClassifier232, dataFeatureClassifier234, subprogramFeatureClassifier245, dataFeatureClassifier236, dataFeatureClassifier239, dataFeatureClassifier242, subprogramGroupFeatureClassifier247, featurePrototype249, constrainingClassifier251, constrainingFeatureGroupType254, parentMode276, subcomponentType257, ownedPrototypeBinding259, prototype262, ownedModeBinding265, implementationReference267, refined271, classifier273, refined298, derivedMode279, specification282, ownedFlowSegment285, flowElement287, context289, destination292, source294, context300, connectionEnd303, extended305, implemented308, refined312, ownedEndToEndFlowSegment314, flowElement316, context318, abstractSubcomponentType321, dataClassifier325, dataClassifier323, privateSection333, subprogramClassifier328, parsedAnnexLibrary330, parsedAnnexSubclause331, ownedPackageRename334, ownedComponentTypeRename335, ownedClassifier337, ownedFeatureGroupTypeRename340, ownedAnnexLibrary342, importedUnit345, renamedComponentType360, renamedPackage347, ownedPublicSection349, ownedPrivateSection351, publicSection353, privateSection356, publicSection359, binding374, featureType377, renamedFeatureGroupType363, actual366, binding367, subcomponentType370, actual373, componentPrototype388, actual380, classifier381, componentPrototype383, classifier386, ownedBusAccess403, ownedDataAccess405, prototype391, ownedSubprogramCall393, calledSubprogram394, context396, subprogramCall398, ownedSubprogramCallSequence400, ownedSubprogramAccess408, ownedDataPort411, ownedEventPort414, ownedEventDataPort417, ownedSubprogramGroupAccess420, ownedBusSubcomponent423, ownedThreadSubcomponent440, ownedThreadGroupSubcomponent442, ownedDataSubcomponent424, ownedDeviceSubcomponent426, ownedMemorySubcomponent428, ownedProcessSubcomponent430, ownedProcessorSubcomponent432, ownedSystemSubcomponent434, ownedSubprogramSubcomponent436, ownedSubprogramGroupSubcomponent438, memorySubcomponentType456, processSubcomponentType458, ownedVirtualBusSubcomponent444, ownedVirtualProcessorSubcomponent446, busSubcomponentType448, dataSubcomponentType451, deviceSubcomponentType454, threadSubcomponentType470, threadGroupSubcomponentType472, processorSubcomponentType460, systemSubcomponentType462, subprogramSubcomponentType464, subprogramGroupSubcomponentType467, ownedDataPort480, ownedEventDataPort483, ownedEventPort486, virtualBusSubcomponentType474, virtualProcessorSubcomponentType476, ownedBusAccess478, ownedDataSubcomponent499, ownedVirtualBusSubcomponent489, ownedSubprogramAccess491, ownedDataAccess493, ownedSubprogramGroupAccess496, ownedSubprogramGroupAccess518, ownedSubprogramSubcomponent501, ownedDataPort504, ownedEventDataPort506, ownedEventPort509, ownedBusAccess512, ownedSubprogramAccess515, ownedBusAccess529, ownedBusSubcomponent521, ownedDataSubcomponent523, ownedVirtualBusSubcomponent526, ownedEventDataPort545, ownedEventPort547, ownedParameter550, ownedDataAccess553, ownedDataPort531, ownedEventDataPort534, ownedEventPort537, ownedBusSubcomponent540, ownedMemorySubcomponent542, ownedSubprogramAccess567, ownedSubprogramGroupAccess569, ownedSubprogramAccess556, ownedSubprogramGroupAccess559, ownedDataSubcomponent562, ownedSubprogramSubcomponent564, ownedDataAccess582, ownedDataPort585, ownedSubprogramGroupAccess588, ownedSubprogramAccess591, ownedSubprogramSubcomponent572, ownedSubprogramGroupSubcomponent574, ownedDataSubcomponent577, ownedBusAccess580, ownedDeviceSubcomponent605, ownedMemorySubcomponent608, ownedProcessSubcomponent611, ownedProcessorSubcomponent614, ownedEventPort594, ownedEventDataPort597, ownedBusSubcomponent600, ownedDataSubcomponent602, ownedDataPort632, ownedEventDataPort634, ownedSubprogramSubcomponent617, ownedSubprogramGroupSubcomponent620, ownedSystemSubcomponent623, ownedVirtualBusSubcomponent626, ownedVirtualProcessorSubcomponent629, ownedMemorySubcomponent651, ownedVirtualBusSubcomponent654, ownedVirtualProcessorSubcomponent657, ownedEventPort637, ownedBusAccess640, ownedSubprogramAccess643, ownedSubprogramGroupAccess646, ownedBusSubcomponent649, ownedSubprogramGroupAccess674, ownedDataSubcomponent677, ownedDataPort660, ownedEventDataPort662, ownedEventPort665, ownedDataAccess668, ownedSubprogramAccess671, ownedSubprogramSubcomponent679, ownedSubprogramGroupSubcomponent682, ownedDataPort691, ownedThreadSubcomponent685, ownedEventDataPort693, ownedThreadGroupSubcomponent688, ownedEventPort696, ownedDataAccess699, ownedSubprogramAccess702, ownedSubprogramGroupAccess705, ownedSubprogramGroupSubcomponent708, ownedSubprogramSubcomponent710, ownedDataSubcomponent713, ownedDataSubcomponent733, ownedDataPort716, ownedEventDataPort718, ownedEventPort721, ownedDataAccess724, ownedSubprogramAccess727, ownedSubprogramGroupAccess730, ownedThreadSubcomponent735, ownedThreadGroupSubcomponent738, ownedSubprogramSubcomponent741, ownedSubprogramGroupSubcomponent744, ownedDataPort747, ownedEventDataPort749, ownedEventPort752, ownedVirtualBusSubcomponent755, ownedDataPort757, ownedEventDataPort759, ownedEventPort762, ownedSubprogramAccess765, ownedSubprogramGroupAccess768, ownedVirtualBusSubcomponent771, ownedVirtualProcessorSubcomponent773, property776, ownedValue778, propertyType781, ownedPropertyType783, classifier796, constantValue786, unit789, baseUnit791, factor793, minimum798, maximum800, delta803, ownedPropertyExpression806, ownedFieldValue808, ownedProperty815, ownedListElement810, namedValue812, ownedPropertyType813, propertySet829, ownedPropertyConstant818, importedUnit821, ownedAnnexSubclause824, package827, range836, ownedUnitsType832, unitsType833, lowerBound842, ownedLiteral838, upperBound839, ownedField852, classifierReference845, ownedNumberType847, numberType849, namedElementReference854, ownedElementType856, elementType858},
    generalizations={gen_aadl2_Comment_Element, gen_aadl2_Type_NamedElement, gen_aadl2_NamedElement_Element, gen_aadl2_PropertyAssociation_Element, gen_aadl2_Property_BasicProperty, gen_aadl2_Property_AbstractNamedValue, gen_aadl2_Property_ArraySizeProperty, gen_aadl2_BasicProperty_TypedElement, gen_aadl2_TypedElement_NamedElement, gen_aadl2_PropertyType_Type, gen_aadl2_PropertyExpression_Element, gen_aadl2_MetaclassReference_PropertyOwner, gen_aadl2_PropertyOwner_Element, gen_aadl2_Classifier_Namespace, gen_aadl2_Classifier_Type, gen_aadl2_ClassifierFeature_NamedElement, gen_aadl2_Namespace_NamedElement, gen_aadl2_AnnexSubclause_ModalElement, gen_aadl2_Generalization_DirectedRelationship, gen_aadl2_DirectedRelationship_Relationship, gen_aadl2_Relationship_Element, gen_aadl2_ModalElement_NamedElement, gen_aadl2_Mode_ModeFeature, gen_aadl2_ModeFeature_ClassifierFeature, gen_aadl2_Prototype_StructuralFeature, gen_aadl2_Prototype_CalledSubprogram, gen_aadl2_StructuralFeature_RefinableElement, gen_aadl2_StructuralFeature_ClassifierFeature, gen_aadl2_RefinableElement_NamedElement, gen_aadl2_PrototypeBinding_Element, gen_aadl2_ContainedNamedElement_Element, gen_aadl2_ContainmentPathElement_Element, gen_aadl2_ArrayRange_Element, gen_aadl2_ModalPropertyValue_ModalElement, gen_aadl2_BehavioralFeature_ClassifierFeature, gen_aadl2_ArrayDimension_Element, gen_aadl2_ArraySize_Element, gen_aadl2_ArrayableElement_Element, gen_aadl2_ComponentImplementationReference_Element, gen_aadl2_ComponentImplementation_ComponentClassifier, gen_aadl2_SubcomponentType_Type, gen_aadl2_ComponentClassifier_Classifier, gen_aadl2_ComponentClassifier_SubcomponentType, gen_aadl2_ComponentClassifier_FeatureClassifier, gen_aadl2_ModeTransition_ModeFeature, gen_aadl2_ModeTransitionTrigger_Element, gen_aadl2_Context_NamedElement, gen_aadl2_TriggerPort_NamedElement, gen_aadl2_ComponentType_ComponentClassifier, gen_aadl2_Feature_StructuralFeature, gen_aadl2_Feature_FeatureConnectionEnd, gen_aadl2_Feature_ArrayableElement, gen_aadl2_FeatureConnectionEnd_ConnectionEnd, gen_aadl2_ConnectionEnd_NamedElement, gen_aadl2_ComponentPrototype_Prototype, gen_aadl2_ComponentPrototype_SubcomponentType, gen_aadl2_ComponentPrototype_FeatureClassifier, gen_aadl2_FlowEnd_Element, gen_aadl2_FlowSpecification_FlowFeature, gen_aadl2_FlowSpecification_ModalPath, gen_aadl2_FlowSpecification_FlowElement, gen_aadl2_FlowFeature_StructuralFeature, gen_aadl2_FlowFeature_Flow, gen_aadl2_Flow_NamedElement, gen_aadl2_ModalPath_ModalElement, gen_aadl2_FlowElement_EndToEndFlowElement, gen_aadl2_EndToEndFlowElement_NamedElement, gen_aadl2_TypeExtension_Generalization, gen_aadl2_FeatureGroup_DirectedFeature, gen_aadl2_FeatureGroup_Context, gen_aadl2_FeatureGroup_FeatureGroupConnectionEnd, gen_aadl2_FeatureGroup_CallContext, gen_aadl2_FeatureGroupConnectionEnd_ConnectionEnd, gen_aadl2_DirectedFeature_Feature, gen_aadl2_FeatureGroupType_Classifier, gen_aadl2_FeatureGroupType_FeatureType, gen_aadl2_Access_Feature, gen_aadl2_Access_AccessConnectionEnd, gen_aadl2_GroupExtension_Generalization, gen_aadl2_BusAccess_Access, gen_aadl2_BusAccess_Bus, gen_aadl2_Data_NamedElement, gen_aadl2_DataSubcomponentType_Data, gen_aadl2_DataSubcomponentType_SubcomponentType, gen_aadl2_DataSubcomponentType_FeatureClassifier, gen_aadl2_AccessConnectionEnd_ConnectionEnd, gen_aadl2_Bus_NamedElement, gen_aadl2_BusSubcomponentType_Bus, gen_aadl2_BusSubcomponentType_SubcomponentType, gen_aadl2_BusSubcomponentType_FeatureClassifier, gen_aadl2_DataAccess_Access, gen_aadl2_DataAccess_Data, gen_aadl2_DataAccess_FlowElement, gen_aadl2_DataAccess_ParameterConnectionEnd, gen_aadl2_DataAccess_PortConnectionEnd, gen_aadl2_ParameterConnectionEnd_ConnectionEnd, gen_aadl2_PortConnectionEnd_ConnectionEnd, gen_aadl2_DataPort_Port, gen_aadl2_DataPort_Context, gen_aadl2_DataPort_Data, gen_aadl2_DataPort_ParameterConnectionEnd, gen_aadl2_Port_DirectedFeature, gen_aadl2_Port_PortConnectionEnd, gen_aadl2_Port_TriggerPort, gen_aadl2_EventDataPort_Port, gen_aadl2_EventDataPort_Context, gen_aadl2_EventDataPort_Data, gen_aadl2_EventDataPort_ParameterConnectionEnd, gen_aadl2_EventPort_Port, gen_aadl2_Parameter_DirectedFeature, gen_aadl2_Parameter_Context, gen_aadl2_Parameter_ParameterConnectionEnd, gen_aadl2_SubprogramAccess_Access, gen_aadl2_SubprogramAccess_Subprogram, gen_aadl2_Subcomponent_StructuralFeature, gen_aadl2_Subcomponent_ModalElement, gen_aadl2_Subcomponent_Context, gen_aadl2_Subcomponent_FlowElement, gen_aadl2_Subcomponent_ArrayableElement, gen_aadl2_Subprogram_NamedElement, gen_aadl2_Subprogram_CalledSubprogram, gen_aadl2_SubprogramSubcomponentType_SubcomponentType, gen_aadl2_SubprogramSubcomponentType_Subprogram, gen_aadl2_SubprogramSubcomponentType_FeatureClassifier, gen_aadl2_SubprogramGroupAccess_Access, gen_aadl2_SubprogramGroupAccess_SubprogramGroup, gen_aadl2_SubprogramGroupAccess_CallContext, gen_aadl2_SubprogramGroup_NamedElement, gen_aadl2_SubprogramGroupSubcomponentType_SubcomponentType, gen_aadl2_SubprogramGroupSubcomponentType_SubprogramGroup, gen_aadl2_SubprogramGroupSubcomponentType_FeatureClassifier, gen_aadl2_AbstractFeature_DirectedFeature, gen_aadl2_AbstractFeature_TriggerPort, gen_aadl2_FeaturePrototype_Prototype, gen_aadl2_FeatureGroupPrototype_Prototype, gen_aadl2_FeatureGroupPrototype_FeatureType, gen_aadl2_ModeBinding_Element, gen_aadl2_FlowImplementation_ModalPath, gen_aadl2_FlowImplementation_ClassifierFeature, gen_aadl2_FlowImplementation_Flow, gen_aadl2_FlowSegment_Element, gen_aadl2_Connection_StructuralFeature, gen_aadl2_Connection_ModalPath, gen_aadl2_Connection_FlowElement, gen_aadl2_EndToEndFlowSegment_Element, gen_aadl2_ConnectedElement_Element, gen_aadl2_ImplementationExtension_Generalization, gen_aadl2_Realization_Generalization, gen_aadl2_EndToEndFlow_FlowFeature, gen_aadl2_EndToEndFlow_ModalPath, gen_aadl2_EndToEndFlow_EndToEndFlowElement, gen_aadl2_ProcessorFeature_StructuralFeature, gen_aadl2_ProcessorFeature_ModalElement, gen_aadl2_AbstractSubcomponent_Subcomponent, gen_aadl2_AbstractSubcomponent_Abstract, gen_aadl2_Abstract_NamedElement, gen_aadl2_AbstractSubcomponentType_Abstract, gen_aadl2_AbstractSubcomponentType_SubcomponentType, gen_aadl2_AccessConnection_Connection, gen_aadl2_ParameterConnection_Connection, gen_aadl2_PortConnection_Connection, gen_aadl2_FeatureConnection_Connection, gen_aadl2_FeatureGroupConnection_Connection, gen_aadl2_SubprogramProxy_ProcessorFeature, gen_aadl2_SubprogramProxy_AccessConnectionEnd, gen_aadl2_SubprogramProxy_CalledSubprogram, gen_aadl2_InternalFeature_StructuralFeature, gen_aadl2_InternalFeature_ModalElement, gen_aadl2_InternalFeature_FeatureConnectionEnd, gen_aadl2_InternalFeature_PortConnectionEnd, gen_aadl2_InternalFeature_TriggerPort, gen_aadl2_EventSource_InternalFeature, gen_aadl2_EventDataSource_InternalFeature, gen_aadl2_DataClassifier_ComponentClassifier, gen_aadl2_DataClassifier_DataSubcomponentType, gen_aadl2_PortProxy_ProcessorFeature, gen_aadl2_PortProxy_FeatureConnectionEnd, gen_aadl2_PortProxy_PortConnectionEnd, gen_aadl2_PortProxy_TriggerPort, gen_aadl2_PublicPackageSection_PackageSection, gen_aadl2_SubprogramClassifier_ComponentClassifier, gen_aadl2_SubprogramClassifier_SubprogramSubcomponentType, gen_aadl2_AnnexLibrary_NamedElement, gen_aadl2_DefaultAnnexLibrary_AnnexLibrary, gen_aadl2_DefaultAnnexSubclause_AnnexSubclause, gen_aadl2_PackageRename_NamedElement, gen_aadl2_PackageSection_Namespace, gen_aadl2_FeatureGroupTypeRename_NamedElement, gen_aadl2_AadlPackage_ModelUnit, gen_aadl2_ModelUnit_NamedElement, gen_aadl2_PrivatePackageSection_PackageSection, gen_aadl2_ComponentTypeRename_NamedElement, gen_aadl2_ComponentPrototypeBinding_PrototypeBinding, gen_aadl2_ComponentPrototypeActual_ArrayableElement, gen_aadl2_FeatureGroupPrototypeBinding_PrototypeBinding, gen_aadl2_FeatureGroupPrototypeActual_FeaturePrototypeActual, gen_aadl2_FeaturePrototypeReference_FeaturePrototypeActual, gen_aadl2_FeaturePrototypeActual_ArrayableElement, gen_aadl2_FeaturePrototypeBinding_PrototypeBinding, gen_aadl2_AccessSpecification_FeaturePrototypeActual, gen_aadl2_PortSpecification_FeaturePrototypeActual, gen_aadl2_SubprogramCallSequence_BehavioralFeature, gen_aadl2_SubprogramCallSequence_ModalElement, gen_aadl2_SubprogramCall_BehavioralFeature, gen_aadl2_SubprogramCall_Context, gen_aadl2_BehavioredImplementation_ComponentImplementation, gen_aadl2_AbstractType_ComponentType, gen_aadl2_AbstractType_AbstractClassifier, gen_aadl2_AbstractType_CallContext, gen_aadl2_VirtualProcessor_NamedElement, gen_aadl2_VirtualBusSubcomponentType_SubcomponentType, gen_aadl2_VirtualBusSubcomponentType_VirtualBus, gen_aadl2_AbstractClassifier_ComponentClassifier, gen_aadl2_AbstractClassifier_AbstractSubcomponentType, gen_aadl2_AbstractClassifier_BusSubcomponentType, gen_aadl2_AbstractClassifier_DataSubcomponentType, gen_aadl2_AbstractClassifier_DeviceSubcomponentType, gen_aadl2_AbstractClassifier_MemorySubcomponentType, gen_aadl2_AbstractClassifier_ProcessorSubcomponentType, gen_aadl2_AbstractClassifier_ProcessSubcomponentType, gen_aadl2_AbstractClassifier_SubprogramGroupSubcomponentType, gen_aadl2_AbstractClassifier_SubprogramSubcomponentType, gen_aadl2_AbstractClassifier_SystemSubcomponentType, gen_aadl2_AbstractClassifier_ThreadGroupSubcomponentType, gen_aadl2_AbstractClassifier_ThreadSubcomponentType, gen_aadl2_AbstractClassifier_VirtualBusSubcomponentType, gen_aadl2_AbstractClassifier_VirtualProcessorSubcomponentType, gen_aadl2_VirtualProcessorSubcomponentType_SubcomponentType, gen_aadl2_VirtualProcessorSubcomponentType_VirtualProcessor, gen_aadl2_AbstractImplementation_BehavioredImplementation, gen_aadl2_AbstractImplementation_AbstractClassifier, gen_aadl2_VirtualBus_NamedElement, gen_aadl2_ThreadGroupSubcomponentType_SubcomponentType, gen_aadl2_ThreadGroupSubcomponentType_ThreadGroup, gen_aadl2_ThreadGroup_NamedElement, gen_aadl2_ThreadSubcomponentType_SubcomponentType, gen_aadl2_ThreadSubcomponentType_Thread, gen_aadl2_Thread_NamedElement, gen_aadl2_SystemSubcomponentType_SubcomponentType, gen_aadl2_SystemSubcomponentType_System, gen_aadl2_System_NamedElement, gen_aadl2_ProcessSubcomponentType_Process, gen_aadl2_ProcessSubcomponentType_SubcomponentType, gen_aadl2_Process_NamedElement, gen_aadl2_MemorySubcomponentType_Memory, gen_aadl2_MemorySubcomponentType_SubcomponentType, gen_aadl2_Memory_NamedElement, gen_aadl2_DeviceSubcomponentType_Device, gen_aadl2_DeviceSubcomponentType_SubcomponentType, gen_aadl2_Device_NamedElement, gen_aadl2_ProcessorSubcomponentType_Processor, gen_aadl2_ProcessorSubcomponentType_SubcomponentType, gen_aadl2_Processor_NamedElement, gen_aadl2_MemorySubcomponent_Memory, gen_aadl2_ProcessSubcomponent_Subcomponent, gen_aadl2_ProcessSubcomponent_Process, gen_aadl2_BusSubcomponent_Subcomponent, gen_aadl2_BusSubcomponent_AccessConnectionEnd, gen_aadl2_BusSubcomponent_Bus, gen_aadl2_DataSubcomponent_Subcomponent, gen_aadl2_DataSubcomponent_AccessConnectionEnd, gen_aadl2_DataSubcomponent_Data, gen_aadl2_DataSubcomponent_ParameterConnectionEnd, gen_aadl2_DataSubcomponent_PortConnectionEnd, gen_aadl2_DeviceSubcomponent_Subcomponent, gen_aadl2_DeviceSubcomponent_Device, gen_aadl2_MemorySubcomponent_Subcomponent, gen_aadl2_ThreadGroupSubcomponent_Subcomponent, gen_aadl2_ThreadGroupSubcomponent_ThreadGroup, gen_aadl2_ProcessorSubcomponent_Subcomponent, gen_aadl2_ProcessorSubcomponent_Processor, gen_aadl2_SystemSubcomponent_Subcomponent, gen_aadl2_SystemSubcomponent_System, gen_aadl2_SubprogramSubcomponent_Subcomponent, gen_aadl2_SubprogramSubcomponent_AccessConnectionEnd, gen_aadl2_SubprogramSubcomponent_Subprogram, gen_aadl2_SubprogramGroupSubcomponent_Subcomponent, gen_aadl2_SubprogramGroupSubcomponent_AccessConnectionEnd, gen_aadl2_SubprogramGroupSubcomponent_SubprogramGroup, gen_aadl2_SubprogramGroupSubcomponent_CallContext, gen_aadl2_ThreadSubcomponent_Subcomponent, gen_aadl2_ThreadSubcomponent_Thread, gen_aadl2_VirtualBusSubcomponent_Subcomponent, gen_aadl2_VirtualBusSubcomponent_VirtualBus, gen_aadl2_VirtualProcessorSubcomponent_Subcomponent, gen_aadl2_VirtualProcessorSubcomponent_VirtualProcessor, gen_aadl2_AbstractPrototype_ComponentPrototype, gen_aadl2_AbstractPrototype_AbstractSubcomponentType, gen_aadl2_AbstractPrototype_BusSubcomponentType, gen_aadl2_AbstractPrototype_DataSubcomponentType, gen_aadl2_AbstractPrototype_DeviceSubcomponentType, gen_aadl2_AbstractPrototype_MemorySubcomponentType, gen_aadl2_AbstractPrototype_ProcessorSubcomponentType, gen_aadl2_AbstractPrototype_ProcessSubcomponentType, gen_aadl2_AbstractPrototype_SubprogramGroupSubcomponentType, gen_aadl2_AbstractPrototype_SubprogramSubcomponentType, gen_aadl2_AbstractPrototype_SystemSubcomponentType, gen_aadl2_AbstractPrototype_ThreadGroupSubcomponentType, gen_aadl2_AbstractPrototype_ThreadSubcomponentType, gen_aadl2_AbstractPrototype_VirtualBusSubcomponentType, gen_aadl2_AbstractPrototype_VirtualProcessorSubcomponentType, gen_aadl2_BusClassifier_ComponentClassifier, gen_aadl2_BusClassifier_BusSubcomponentType, gen_aadl2_BusType_ComponentType, gen_aadl2_BusType_BusClassifier, gen_aadl2_DataImplementation_ComponentImplementation, gen_aadl2_DataImplementation_DataClassifier, gen_aadl2_BusImplementation_ComponentImplementation, gen_aadl2_BusImplementation_BusClassifier, gen_aadl2_BusPrototype_ComponentPrototype, gen_aadl2_BusPrototype_BusSubcomponentType, gen_aadl2_DataType_ComponentType, gen_aadl2_DataType_DataClassifier, gen_aadl2_DataType_CallContext, gen_aadl2_DeviceImplementation_ComponentImplementation, gen_aadl2_DeviceImplementation_DeviceClassifier, gen_aadl2_DataPrototype_ComponentPrototype, gen_aadl2_DataPrototype_DataSubcomponentType, gen_aadl2_DeviceClassifier_ComponentClassifier, gen_aadl2_DeviceClassifier_DeviceSubcomponentType, gen_aadl2_DeviceType_ComponentType, gen_aadl2_DeviceType_DeviceClassifier, gen_aadl2_DevicePrototype_ComponentPrototype, gen_aadl2_DevicePrototype_DeviceSubcomponentType, gen_aadl2_MemoryClassifier_ComponentClassifier, gen_aadl2_MemoryClassifier_MemorySubcomponentType, gen_aadl2_MemoryType_ComponentType, gen_aadl2_MemoryType_MemoryClassifier, gen_aadl2_MemoryPrototype_ComponentPrototype, gen_aadl2_MemoryPrototype_MemorySubcomponentType, gen_aadl2_SubprogramType_ComponentType, gen_aadl2_SubprogramType_SubprogramClassifier, gen_aadl2_SubprogramType_CallContext, gen_aadl2_MemoryImplementation_ComponentImplementation, gen_aadl2_MemoryImplementation_MemoryClassifier, gen_aadl2_SubprogramGroupClassifier_SubprogramGroupSubcomponentType, gen_aadl2_SubprogramGroupType_ComponentType, gen_aadl2_SubprogramGroupType_SubprogramGroupClassifier, gen_aadl2_SubprogramGroupType_CallContext, gen_aadl2_SubprogramGroupImplementation_ComponentImplementation, gen_aadl2_SubprogramGroupImplementation_SubprogramGroupClassifier, gen_aadl2_SubprogramImplementation_BehavioredImplementation, gen_aadl2_SubprogramImplementation_SubprogramClassifier, gen_aadl2_SubprogramPrototype_ComponentPrototype, gen_aadl2_SubprogramPrototype_SubprogramSubcomponentType, gen_aadl2_SubprogramGroupClassifier_ComponentClassifier, gen_aadl2_SubprogramGroupPrototype_ComponentPrototype, gen_aadl2_SubprogramGroupPrototype_SubprogramGroupSubcomponentType, gen_aadl2_SystemClassifier_ComponentClassifier, gen_aadl2_SystemClassifier_SystemSubcomponentType, gen_aadl2_SystemType_ComponentType, gen_aadl2_SystemType_SystemClassifier, gen_aadl2_SystemImplementation_ComponentImplementation, gen_aadl2_SystemImplementation_SystemClassifier, gen_aadl2_ProcessorClassifier_ComponentClassifier, gen_aadl2_ProcessorClassifier_ProcessorSubcomponentType, gen_aadl2_ProcessorType_ComponentType, gen_aadl2_ProcessorType_ProcessorClassifier, gen_aadl2_SystemPrototype_ComponentPrototype, gen_aadl2_SystemPrototype_SystemSubcomponentType, gen_aadl2_ProcessorPrototype_ComponentPrototype, gen_aadl2_ProcessorPrototype_ProcessorSubcomponentType, gen_aadl2_ProcessClassifier_ComponentClassifier, gen_aadl2_ProcessClassifier_ProcessSubcomponentType, gen_aadl2_ProcessorImplementation_ComponentImplementation, gen_aadl2_ProcessorImplementation_ProcessorClassifier, gen_aadl2_ProcessImplementation_ComponentImplementation, gen_aadl2_ProcessImplementation_ProcessClassifier, gen_aadl2_ProcessType_ComponentType, gen_aadl2_ProcessType_ProcessClassifier, gen_aadl2_ThreadPrototype_ComponentPrototype, gen_aadl2_ThreadPrototype_ThreadSubcomponentType, gen_aadl2_ProcessPrototype_ComponentPrototype, gen_aadl2_ProcessPrototype_ProcessSubcomponentType, gen_aadl2_ThreadClassifier_ComponentClassifier, gen_aadl2_ThreadClassifier_ThreadSubcomponentType, gen_aadl2_ThreadType_ComponentType, gen_aadl2_ThreadType_ThreadClassifier, gen_aadl2_ThreadImplementation_BehavioredImplementation, gen_aadl2_ThreadImplementation_ThreadClassifier, gen_aadl2_ThreadGroupClassifier_ComponentClassifier, gen_aadl2_ThreadGroupClassifier_ThreadGroupSubcomponentType, gen_aadl2_ThreadGroupType_ComponentType, gen_aadl2_ThreadGroupType_ThreadGroupClassifier, gen_aadl2_ThreadGroupImplementation_ComponentImplementation, gen_aadl2_ThreadGroupImplementation_ThreadGroupClassifier, gen_aadl2_ThreadGroupPrototype_ComponentPrototype, gen_aadl2_ThreadGroupPrototype_ThreadGroupSubcomponentType, gen_aadl2_VirtualBusClassifier_ComponentClassifier, gen_aadl2_VirtualBusClassifier_VirtualBusSubcomponentType, gen_aadl2_VirtualBusType_ComponentType, gen_aadl2_VirtualBusType_VirtualBusClassifier, gen_aadl2_VirtualProcessorImplementation_ComponentImplementation, gen_aadl2_VirtualProcessorImplementation_VirtualProcessorClassifier, gen_aadl2_VirtualBusImplementation_ComponentImplementation, gen_aadl2_VirtualBusImplementation_VirtualBusClassifier, gen_aadl2_VirtualBusPrototype_ComponentPrototype, gen_aadl2_VirtualBusPrototype_VirtualBusSubcomponentType, gen_aadl2_VirtualProcessorClassifier_ComponentClassifier, gen_aadl2_VirtualProcessorClassifier_VirtualProcessorSubcomponentType, gen_aadl2_VirtualProcessorType_ComponentType, gen_aadl2_VirtualProcessorType_VirtualProcessorClassifier, gen_aadl2_StringLiteral_PropertyValue, gen_aadl2_VirtualProcessorPrototype_ComponentPrototype, gen_aadl2_VirtualProcessorPrototype_VirtualProcessorSubcomponentType, gen_aadl2_BasicPropertyAssociation_Element, gen_aadl2_PropertyConstant_TypedElement, gen_aadl2_PropertyConstant_AbstractNamedValue, gen_aadl2_PropertyConstant_ArraySizeProperty, gen_aadl2_ReferenceValue_ContainedNamedElement, gen_aadl2_ReferenceValue_PropertyValue, gen_aadl2_PropertyValue_PropertyExpression, gen_aadl2_NumberValue_PropertyValue, gen_aadl2_UnitLiteral_EnumerationLiteral, gen_aadl2_EnumerationLiteral_NamedElement, gen_aadl2_EnumerationLiteral_AbstractNamedValue, gen_aadl2_ClassifierValue_PropertyOwner, gen_aadl2_ClassifierValue_PropertyValue, gen_aadl2_BooleanLiteral_PropertyValue, gen_aadl2_RangeValue_PropertyValue, gen_aadl2_IntegerLiteral_NumberValue, gen_aadl2_RealLiteral_NumberValue, gen_aadl2_Operation_PropertyExpression, gen_aadl2_RecordValue_PropertyValue, gen_aadl2_ComputedValue_PropertyValue, gen_aadl2_ListValue_PropertyExpression, gen_aadl2_NamedValue_PropertyValue, gen_aadl2_PropertySet_Namespace, gen_aadl2_PropertySet_ModelUnit, gen_aadl2_GlobalNamespace_Namespace, gen_aadl2_NonListType_PropertyType, gen_aadl2_AadlBoolean_NonListType, gen_aadl2_AadlString_NonListType, gen_aadl2_AadlInteger_NumberType, gen_aadl2_NumberType_NonListType, gen_aadl2_UnitsType_EnumerationType, gen_aadl2_EnumerationType_Namespace, gen_aadl2_EnumerationType_NonListType, gen_aadl2_NumericRange_Element, gen_aadl2_AadlReal_NumberType, gen_aadl2_ClassifierType_NonListType, gen_aadl2_RangeType_NonListType, gen_aadl2_RecordType_Namespace, gen_aadl2_RecordType_NonListType, gen_aadl2_RecordField_BasicProperty, gen_aadl2_ReferenceType_NonListType, gen_aadl2_ListType_PropertyType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)