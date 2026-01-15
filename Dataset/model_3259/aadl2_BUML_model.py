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
DirectionType: Enumeration = Enumeration(
    name="DirectionType",
    literals={
            EnumerationLiteral(name="in"),
			EnumerationLiteral(name="out"),
			EnumerationLiteral(name="inOut")
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

FlowKind: Enumeration = Enumeration(
    name="FlowKind",
    literals={
            EnumerationLiteral(name="path"),
			EnumerationLiteral(name="sink"),
			EnumerationLiteral(name="source")
    }
)

AccessType: Enumeration = Enumeration(
    name="AccessType",
    literals={
            EnumerationLiteral(name="provided"),
			EnumerationLiteral(name="required")
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

ConnectionKind: Enumeration = Enumeration(
    name="ConnectionKind",
    literals={
            EnumerationLiteral(name="Access"),
			EnumerationLiteral(name="Feature"),
			EnumerationLiteral(name="FeatureGroup"),
			EnumerationLiteral(name="Parameter"),
			EnumerationLiteral(name="Port")
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
aadl2_Namespace = Class(name="aadl2::Namespace", is_abstract=True)
NamedElement = Class(name="NamedElement")
aadl2_NamedElement = Class(name="aadl2::NamedElement", is_abstract=True)
Element = Class(name="Element")
aadl2_Property = Class(name="aadl2::Property")
aadl2_ContainedNamedElement = Class(name="aadl2::ContainedNamedElement")
aadl2_Classifier = Class(name="aadl2::Classifier", is_abstract=True)
aadl2_ModalPropertyValue = Class(name="aadl2::ModalPropertyValue")
BasicProperty = Class(name="BasicProperty")
aadl2_PropertyExpression = Class(name="aadl2::PropertyExpression", is_abstract=True)
aadl2_PropertyAssociation = Class(name="aadl2::PropertyAssociation")
aadl2_BasicProperty = Class(name="aadl2::BasicProperty")
TypedElement = Class(name="TypedElement")
aadl2_PropertyType = Class(name="aadl2::PropertyType", is_abstract=True)
aadl2_TypedElement = Class(name="aadl2::TypedElement", is_abstract=True)
aadl2_Type = Class(name="aadl2::Type", is_abstract=True)
aadl2_MetaclassReference = Class(name="aadl2::MetaclassReference")
Type = Class(name="Type")
aadl2_PropertyOwner = Class(name="aadl2::PropertyOwner", is_abstract=True)
PropertyOwner = Class(name="PropertyOwner")
Namespace = Class(name="Namespace")
aadl2_ClassifierFeature = Class(name="aadl2::ClassifierFeature", is_abstract=True)
aadl2_Generalization = Class(name="aadl2::Generalization", is_abstract=True)
aadl2_PrototypeBinding = Class(name="aadl2::PrototypeBinding", is_abstract=True)
DirectedRelationship = Class(name="DirectedRelationship")
aadl2_AnnexSubclause = Class(name="aadl2::AnnexSubclause", is_abstract=True)
aadl2_Prototype = Class(name="aadl2::Prototype", is_abstract=True)
aadl2_DirectedRelationship = Class(name="aadl2::DirectedRelationship", is_abstract=True)
Relationship = Class(name="Relationship")
aadl2_Relationship = Class(name="aadl2::Relationship", is_abstract=True)
aadl2_Mode = Class(name="aadl2::Mode")
ModeFeature = Class(name="ModeFeature")
aadl2_ModeFeature = Class(name="aadl2::ModeFeature", is_abstract=True)
ClassifierFeature = Class(name="ClassifierFeature")
StructuralFeature = Class(name="StructuralFeature")
ModalElement = Class(name="ModalElement")
aadl2_ModalElement = Class(name="aadl2::ModalElement")
aadl2_ContainmentPathElement = Class(name="aadl2::ContainmentPathElement")
aadl2_StructuralFeature = Class(name="aadl2::StructuralFeature", is_abstract=True)
RefinableElement = Class(name="RefinableElement")
aadl2_RefinableElement = Class(name="aadl2::RefinableElement", is_abstract=True)
aadl2_BehavioralFeature = Class(name="aadl2::BehavioralFeature", is_abstract=True)
aadl2_ArraySpecification = Class(name="aadl2::ArraySpecification")
aadl2_ArraySize = Class(name="aadl2::ArraySize", is_abstract=True)
aadl2_ArrayableElement = Class(name="aadl2::ArrayableElement", is_abstract=True)
aadl2_Numeral = Class(name="aadl2::Numeral")
aadl2_ArrayRange = Class(name="aadl2::ArrayRange")
ArraySize = Class(name="ArraySize")
ComponentClassifier = Class(name="ComponentClassifier")
aadl2_ComponentImplementationReference = Class(name="aadl2::ComponentImplementationReference")
aadl2_Subcomponent = Class(name="aadl2::Subcomponent", is_abstract=True)
aadl2_ComponentImplementation = Class(name="aadl2::ComponentImplementation", is_abstract=True)
aadl2_FlowImplementation = Class(name="aadl2::FlowImplementation")
aadl2_ComponentType = Class(name="aadl2::ComponentType", is_abstract=True)
aadl2_Realization = Class(name="aadl2::Realization")
aadl2_EndToEndFlow = Class(name="aadl2::EndToEndFlow")
aadl2_AbstractSubcomponent = Class(name="aadl2::AbstractSubcomponent")
aadl2_Connection = Class(name="aadl2::Connection", is_abstract=True)
aadl2_ImplementationExtension = Class(name="aadl2::ImplementationExtension")
aadl2_ParameterConnection = Class(name="aadl2::ParameterConnection")
aadl2_PortConnection = Class(name="aadl2::PortConnection")
aadl2_FeatureConnection = Class(name="aadl2::FeatureConnection")
aadl2_AccessConnection = Class(name="aadl2::AccessConnection")
aadl2_ComponentClassifier = Class(name="aadl2::ComponentClassifier", is_abstract=True)
Classifier = Class(name="Classifier")
aadl2_ModeTransition = Class(name="aadl2::ModeTransition")
aadl2_ProcessorPort = Class(name="aadl2::ProcessorPort")
aadl2_InternalEvent = Class(name="aadl2::InternalEvent")
aadl2_FeatureGroupConnection = Class(name="aadl2::FeatureGroupConnection")
aadl2_ProcessorSubprogram = Class(name="aadl2::ProcessorSubprogram")
aadl2_TriggerPort = Class(name="aadl2::TriggerPort")
ModeTransitionTrigger = Class(name="ModeTransitionTrigger")
aadl2_Context = Class(name="aadl2::Context", is_abstract=True)
aadl2_Port = Class(name="aadl2::Port", is_abstract=True)
DirectedFeature = Class(name="DirectedFeature")
PortConnectionEnd = Class(name="PortConnectionEnd")
aadl2_ModeTransitionTrigger = Class(name="aadl2::ModeTransitionTrigger", is_abstract=True)
aadl2_FeatureConnectionEnd = Class(name="aadl2::FeatureConnectionEnd", is_abstract=True)
ConnectionEnd = Class(name="ConnectionEnd")
aadl2_ConnectionEnd = Class(name="aadl2::ConnectionEnd", is_abstract=True)
aadl2_DirectedFeature = Class(name="aadl2::DirectedFeature", is_abstract=True)
Feature = Class(name="Feature")
aadl2_Feature = Class(name="aadl2::Feature", is_abstract=True)
FeatureConnectionEnd = Class(name="FeatureConnectionEnd")
ArrayableElement = Class(name="ArrayableElement")
aadl2_FlowSpecification = Class(name="aadl2::FlowSpecification")
aadl2_TypeExtension = Class(name="aadl2::TypeExtension")
aadl2_FeatureGroup = Class(name="aadl2::FeatureGroup")
aadl2_AbstractFeature = Class(name="aadl2::AbstractFeature")
Flow = Class(name="Flow")
aadl2_PortConnectionEnd = Class(name="aadl2::PortConnectionEnd", is_abstract=True)
Generalization = Class(name="Generalization")
Context = Class(name="Context")
FeatureGroupConnectionEnd = Class(name="FeatureGroupConnectionEnd")
CallContext = Class(name="CallContext")
aadl2_FeatureGroupType = Class(name="aadl2::FeatureGroupType")
aadl2_FeatureGroupConnectionEnd = Class(name="aadl2::FeatureGroupConnectionEnd")
aadl2_CallContext = Class(name="aadl2::CallContext", is_abstract=True)
aadl2_DataPort = Class(name="aadl2::DataPort")
aadl2_EventDataPort = Class(name="aadl2::EventDataPort")
aadl2_EventPort = Class(name="aadl2::EventPort")
aadl2_Flow = Class(name="aadl2::Flow", is_abstract=True)
aadl2_GroupExtension = Class(name="aadl2::GroupExtension")
aadl2_BusAccess = Class(name="aadl2::BusAccess")
aadl2_DataAccess = Class(name="aadl2::DataAccess")
Access = Class(name="Access")
aadl2_BusClassifier = Class(name="aadl2::BusClassifier", is_abstract=True)
aadl2_Access = Class(name="aadl2::Access", is_abstract=True)
AccessConnectionEnd = Class(name="AccessConnectionEnd")
aadl2_AccessConnectionEnd = Class(name="aadl2::AccessConnectionEnd", is_abstract=True)
aadl2_Parameter = Class(name="aadl2::Parameter")
aadl2_SubprogramAccess = Class(name="aadl2::SubprogramAccess")
aadl2_SubprogramGroupAccess = Class(name="aadl2::SubprogramGroupAccess")
CalledSubprogram = Class(name="CalledSubprogram")
aadl2_SubprogramClassifier = Class(name="aadl2::SubprogramClassifier", is_abstract=True)
aadl2_CalledSubprogram = Class(name="aadl2::CalledSubprogram", is_abstract=True)
Bus = Class(name="Bus")
aadl2_Bus = Class(name="aadl2::Bus", is_abstract=True)
FlowElement = Class(name="FlowElement")
ParameterConnectionEnd = Class(name="ParameterConnectionEnd")
aadl2_DataClassifier = Class(name="aadl2::DataClassifier", is_abstract=True)
aadl2_ParameterConnectionEnd = Class(name="aadl2::ParameterConnectionEnd", is_abstract=True)
aadl2_FlowElement = Class(name="aadl2::FlowElement", is_abstract=True)
EndToEndFlowElement = Class(name="EndToEndFlowElement")
aadl2_EndToEndFlowElement = Class(name="aadl2::EndToEndFlowElement")
Data = Class(name="Data")
aadl2_Data = Class(name="aadl2::Data", is_abstract=True)
Port = Class(name="Port")
aadl2_ComponentPrototype = Class(name="aadl2::ComponentPrototype")
aadl2_ModeBinding = Class(name="aadl2::ModeBinding")
aadl2_AbstractClassifier = Class(name="aadl2::AbstractClassifier", is_abstract=True)
Subprogram = Class(name="Subprogram")
aadl2_Subprogram = Class(name="aadl2::Subprogram", is_abstract=True)
aadl2_SubprogramGroupClassifier = Class(name="aadl2::SubprogramGroupClassifier", is_abstract=True)
SubprogramGroup = Class(name="SubprogramGroup")
aadl2_SubprogramGroup = Class(name="aadl2::SubprogramGroup", is_abstract=True)
Abstract = Class(name="Abstract")
aadl2_Abstract = Class(name="aadl2::Abstract", is_abstract=True)
ModalPath = Class(name="ModalPath")
aadl2_SubcomponentFlow = Class(name="aadl2::SubcomponentFlow")
Prototype = Class(name="Prototype")
aadl2_ModalPath = Class(name="aadl2::ModalPath", is_abstract=True)
Subcomponent = Class(name="Subcomponent")
Connection = Class(name="Connection")
aadl2_PackageRename = Class(name="aadl2::PackageRename")
aadl2_ComponentTypeRename = Class(name="aadl2::ComponentTypeRename")
aadl2_FeatureGroupTypeRename = Class(name="aadl2::FeatureGroupTypeRename")
aadl2_AnnexLibrary = Class(name="aadl2::AnnexLibrary", is_abstract=True)
aadl2_DefaultAnnexLibrary = Class(name="aadl2::DefaultAnnexLibrary")
AnnexLibrary = Class(name="AnnexLibrary")
aadl2_DefaultAnnexSubclause = Class(name="aadl2::DefaultAnnexSubclause")
AnnexSubclause = Class(name="AnnexSubclause")
aadl2_PublicPackageSection = Class(name="aadl2::PublicPackageSection")
PackageSection = Class(name="PackageSection")
aadl2_PrivatePackageSection = Class(name="aadl2::PrivatePackageSection")
aadl2_PackageSection = Class(name="aadl2::PackageSection", is_abstract=True)
aadl2_BusType = Class(name="aadl2::BusType")
aadl2_BusImplementation = Class(name="aadl2::BusImplementation")
aadl2_DataType = Class(name="aadl2::DataType")
aadl2_DataImplementation = Class(name="aadl2::DataImplementation")
aadl2_DeviceType = Class(name="aadl2::DeviceType")
aadl2_AadlPackage = Class(name="aadl2::AadlPackage")
aadl2_AbstractType = Class(name="aadl2::AbstractType")
aadl2_AbstractImplementation = Class(name="aadl2::AbstractImplementation")
aadl2_ProcessorType = Class(name="aadl2::ProcessorType")
aadl2_ProcessImplementation = Class(name="aadl2::ProcessImplementation")
aadl2_ProcessorImplementation = Class(name="aadl2::ProcessorImplementation")
aadl2_SubprogramType = Class(name="aadl2::SubprogramType")
aadl2_DeviceImplementation = Class(name="aadl2::DeviceImplementation")
aadl2_MemoryType = Class(name="aadl2::MemoryType")
aadl2_MemoryImplementation = Class(name="aadl2::MemoryImplementation")
aadl2_ProcessType = Class(name="aadl2::ProcessType")
aadl2_ThreadType = Class(name="aadl2::ThreadType")
aadl2_ThreadImplementation = Class(name="aadl2::ThreadImplementation")
aadl2_ThreadGroupType = Class(name="aadl2::ThreadGroupType")
aadl2_SubprogramImplementation = Class(name="aadl2::SubprogramImplementation")
aadl2_ThreadGroupImplementation = Class(name="aadl2::ThreadGroupImplementation")
aadl2_SubprogramGroupType = Class(name="aadl2::SubprogramGroupType")
aadl2_SubprogramGroupImplementation = Class(name="aadl2::SubprogramGroupImplementation")
aadl2_SystemType = Class(name="aadl2::SystemType")
aadl2_SystemImplementation = Class(name="aadl2::SystemImplementation")
aadl2_VirtualProcessorImplementation = Class(name="aadl2::VirtualProcessorImplementation")
aadl2_PropertySet = Class(name="aadl2::PropertySet")
aadl2_VirtualBusType = Class(name="aadl2::VirtualBusType")
aadl2_VirtualBusImplementation = Class(name="aadl2::VirtualBusImplementation")
aadl2_VirtualProcessorType = Class(name="aadl2::VirtualProcessorType")
ComponentType = Class(name="ComponentType")
AbstractClassifier = Class(name="AbstractClassifier")
BehavioredImplementation = Class(name="BehavioredImplementation")
aadl2_BusSubcomponent = Class(name="aadl2::BusSubcomponent")
aadl2_SubprogramSubcomponent = Class(name="aadl2::SubprogramSubcomponent")
aadl2_SubprogramGroupSubcomponent = Class(name="aadl2::SubprogramGroupSubcomponent")
aadl2_ThreadSubcomponent = Class(name="aadl2::ThreadSubcomponent")
aadl2_DataSubcomponent = Class(name="aadl2::DataSubcomponent")
aadl2_ThreadGroupSubcomponent = Class(name="aadl2::ThreadGroupSubcomponent")
aadl2_DeviceSubcomponent = Class(name="aadl2::DeviceSubcomponent")
aadl2_VirtualBusSubcomponent = Class(name="aadl2::VirtualBusSubcomponent")
aadl2_MemorySubcomponent = Class(name="aadl2::MemorySubcomponent")
aadl2_VirtualProcessorSubcomponent = Class(name="aadl2::VirtualProcessorSubcomponent")
aadl2_ProcessSubcomponent = Class(name="aadl2::ProcessSubcomponent")
aadl2_ProcessorSubcomponent = Class(name="aadl2::ProcessorSubcomponent")
aadl2_SystemSubcomponent = Class(name="aadl2::SystemSubcomponent")
aadl2_SubprogramCallSequence = Class(name="aadl2::SubprogramCallSequence")
BehavioralFeature = Class(name="BehavioralFeature")
Device = Class(name="Device")
aadl2_DeviceClassifier = Class(name="aadl2::DeviceClassifier", is_abstract=True)
aadl2_Device = Class(name="aadl2::Device", is_abstract=True)
Memory = Class(name="Memory")
aadl2_MemoryClassifier = Class(name="aadl2::MemoryClassifier", is_abstract=True)
aadl2_Memory = Class(name="aadl2::Memory", is_abstract=True)
aadl2_BehavioredImplementation = Class(name="aadl2::BehavioredImplementation", is_abstract=True)
ComponentImplementation = Class(name="ComponentImplementation")
aadl2_CallSpecification = Class(name="aadl2::CallSpecification", is_abstract=True)
aadl2_Process = Class(name="aadl2::Process", is_abstract=True)
Processor = Class(name="Processor")
aadl2_ProcessorClassifier = Class(name="aadl2::ProcessorClassifier", is_abstract=True)
aadl2_Processor = Class(name="aadl2::Processor", is_abstract=True)
System = Class(name="System")
aadl2_SystemClassifier = Class(name="aadl2::SystemClassifier", is_abstract=True)
aadl2_System = Class(name="aadl2::System", is_abstract=True)
Thread = Class(name="Thread")
aadl2_ThreadClassifier = Class(name="aadl2::ThreadClassifier", is_abstract=True)
Process = Class(name="Process")
aadl2_ProcessClassifier = Class(name="aadl2::ProcessClassifier", is_abstract=True)
aadl2_ThreadGroup = Class(name="aadl2::ThreadGroup", is_abstract=True)
VirtualBus = Class(name="VirtualBus")
aadl2_VirtualBusClassifier = Class(name="aadl2::VirtualBusClassifier", is_abstract=True)
aadl2_VirtualBus = Class(name="aadl2::VirtualBus", is_abstract=True)
VirtualProcessor = Class(name="VirtualProcessor")
aadl2_VirtualProcessorClassifier = Class(name="aadl2::VirtualProcessorClassifier", is_abstract=True)
aadl2_VirtualProcessor = Class(name="aadl2::VirtualProcessor", is_abstract=True)
BusClassifier = Class(name="BusClassifier")
aadl2_Thread = Class(name="aadl2::Thread", is_abstract=True)
ThreadGroup = Class(name="ThreadGroup")
aadl2_ThreadGroupClassifier = Class(name="aadl2::ThreadGroupClassifier", is_abstract=True)
DeviceClassifier = Class(name="DeviceClassifier")
DataClassifier = Class(name="DataClassifier")
MemoryClassifier = Class(name="MemoryClassifier")
ProcessClassifier = Class(name="ProcessClassifier")
ProcessorClassifier = Class(name="ProcessorClassifier")
SubprogramClassifier = Class(name="SubprogramClassifier")
SubprogramGroupClassifier = Class(name="SubprogramGroupClassifier")
SystemClassifier = Class(name="SystemClassifier")
ThreadClassifier = Class(name="ThreadClassifier")
ThreadGroupClassifier = Class(name="ThreadGroupClassifier")
VirtualBusClassifier = Class(name="VirtualBusClassifier")
VirtualProcessorClassifier = Class(name="VirtualProcessorClassifier")
aadl2_PropertyConstant = Class(name="aadl2::PropertyConstant")
aadl2_ComponentPrototypeBinding = Class(name="aadl2::ComponentPrototypeBinding")
PrototypeBinding = Class(name="PrototypeBinding")
aadl2_ComponentPrototypeActual = Class(name="aadl2::ComponentPrototypeActual", is_abstract=True)
aadl2_FeatureGroupPrototypeBinding = Class(name="aadl2::FeatureGroupPrototypeBinding")
aadl2_FeatureGroupPrototypeActual = Class(name="aadl2::FeatureGroupPrototypeActual", is_abstract=True)
aadl2_FeaturePrototype = Class(name="aadl2::FeaturePrototype")
aadl2_FeatureGroupPrototype = Class(name="aadl2::FeatureGroupPrototype")
aadl2_FeaturePrototypeBinding = Class(name="aadl2::FeaturePrototypeBinding")
aadl2_FeaturePrototypeActual = Class(name="aadl2::FeaturePrototypeActual", is_abstract=True)
aadl2_AccessSpecification = Class(name="aadl2::AccessSpecification")
FeaturePrototypeActual = Class(name="FeaturePrototypeActual")
aadl2_PortSpecification = Class(name="aadl2::PortSpecification")
aadl2_FeaturePrototypeReference = Class(name="aadl2::FeaturePrototypeReference")
aadl2_ComponentPrototypeReference = Class(name="aadl2::ComponentPrototypeReference")
ComponentPrototypeActual = Class(name="ComponentPrototypeActual")
aadl2_ComponentReference = Class(name="aadl2::ComponentReference")
aadl2_BasicPropertyAssociation = Class(name="aadl2::BasicPropertyAssociation")
aadl2_FeatureGroupPrototypeReference = Class(name="aadl2::FeatureGroupPrototypeReference")
FeatureGroupPrototypeActual = Class(name="FeatureGroupPrototypeActual")
aadl2_FeatureGroupReference = Class(name="aadl2::FeatureGroupReference")
aadl2_ProcessorCall = Class(name="aadl2::ProcessorCall")
CallSpecification = Class(name="CallSpecification")
aadl2_SubprogramCall = Class(name="aadl2::SubprogramCall")
aadl2_StringLiteral = Class(name="aadl2::StringLiteral")
aadl2_EnumerationValue = Class(name="aadl2::EnumerationValue")
PropertyValue = Class(name="PropertyValue")
aadl2_EnumerationLiteral = Class(name="aadl2::EnumerationLiteral")
aadl2_PropertyValue = Class(name="aadl2::PropertyValue", is_abstract=True)
PropertyExpression = Class(name="PropertyExpression")
aadl2_UnitValue = Class(name="aadl2::UnitValue")
aadl2_UnitLiteral = Class(name="aadl2::UnitLiteral")
EnumerationLiteral = Class(name="EnumerationLiteral")
aadl2_NumberValue = Class(name="aadl2::NumberValue", is_abstract=True)
aadl2_RealLiteral = Class(name="aadl2::RealLiteral")
aadl2_ClassifierValue = Class(name="aadl2::ClassifierValue")
aadl2_ReferenceValue = Class(name="aadl2::ReferenceValue")
ContainedNamedElement = Class(name="ContainedNamedElement")
aadl2_BooleanLiteral = Class(name="aadl2::BooleanLiteral")
aadl2_RangeValue = Class(name="aadl2::RangeValue")
aadl2_IntegerLiteral = Class(name="aadl2::IntegerLiteral")
NumberValue = Class(name="NumberValue")
aadl2_RecordValue = Class(name="aadl2::RecordValue")
aadl2_ConstantValue = Class(name="aadl2::ConstantValue")
aadl2_PropertyReference = Class(name="aadl2::PropertyReference")
aadl2_Operation = Class(name="aadl2::Operation")
aadl2_NumberType = Class(name="aadl2::NumberType", is_abstract=True)
aadl2_UnitsType = Class(name="aadl2::UnitsType")
aadl2_ComputedValue = Class(name="aadl2::ComputedValue")
aadl2_ListValue = Class(name="aadl2::ListValue")
aadl2_GlobalNamespace = Class(name="aadl2::GlobalNamespace")
aadl2_AadlBoolean = Class(name="aadl2::AadlBoolean")
PropertyType = Class(name="PropertyType")
aadl2_AadlString = Class(name="aadl2::AadlString")
aadl2_AadlInteger = Class(name="aadl2::AadlInteger")
NumberType = Class(name="NumberType")
aadl2_AadlReal = Class(name="aadl2::AadlReal")
aadl2_NumericRange = Class(name="aadl2::NumericRange")
EnumerationType = Class(name="EnumerationType")
aadl2_EnumerationType = Class(name="aadl2::EnumerationType")
aadl2_ClassifierType = Class(name="aadl2::ClassifierType")
aadl2_RangeType = Class(name="aadl2::RangeType")
aadl2_RecordType = Class(name="aadl2::RecordType")
aadl2_RecordField = Class(name="aadl2::RecordField")
aadl2_ReferenceType = Class(name="aadl2::ReferenceType")

# aadl2_Element class attributes and methods
aadl2_Element_m_not_own_self: Method = Method(name="not_own_self", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
aadl2_Element_m_mustBeOwned: Method = Method(name="mustBeOwned", parameters={}, type=StringType)
aadl2_Element_m_has_owner: Method = Method(name="has_owner", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
aadl2_Element_m_allOwnedElements: Method = Method(name="allOwnedElements", parameters={}, type=StringType)
aadl2_Element.methods={aadl2_Element_m_has_owner, aadl2_Element_m_mustBeOwned, aadl2_Element_m_allOwnedElements, aadl2_Element_m_not_own_self}

# aadl2_Comment class attributes and methods
aadl2_Comment_body: Property = Property(name="body", type=StringType)
aadl2_Comment.attributes={aadl2_Comment_body}

# aadl2_Namespace class attributes and methods
aadl2_Namespace_m_members_distinguishable: Method = Method(name="members_distinguishable", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
aadl2_Namespace_m_getNamesOfMember: Method = Method(name="getNamesOfMember", parameters={Parameter(name='element')}, type=StringType)
aadl2_Namespace_m_membersAreDistinguishable: Method = Method(name="membersAreDistinguishable", parameters={}, type=StringType)
aadl2_Namespace.methods={aadl2_Namespace_m_membersAreDistinguishable, aadl2_Namespace_m_getNamesOfMember, aadl2_Namespace_m_members_distinguishable}

# NamedElement class attributes and methods

# aadl2_NamedElement class attributes and methods
aadl2_NamedElement_name: Property = Property(name="name", type=StringType)
aadl2_NamedElement_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
aadl2_NamedElement_m_has_no_qualified_name: Method = Method(name="has_no_qualified_name", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
aadl2_NamedElement_m_has_qualified_name: Method = Method(name="has_qualified_name", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
aadl2_NamedElement_m_separator: Method = Method(name="separator", parameters={}, type=StringType)
aadl2_NamedElement_m_qualifiedName: Method = Method(name="qualifiedName", parameters={}, type=StringType)
aadl2_NamedElement_m_allNamespaces: Method = Method(name="allNamespaces", parameters={}, type=StringType)
aadl2_NamedElement_m_isDistinguishableFrom: Method = Method(name="isDistinguishableFrom", parameters={Parameter(name='ns'), Parameter(name='n')}, type=StringType)
aadl2_NamedElement.attributes={aadl2_NamedElement_name, aadl2_NamedElement_qualifiedName}
aadl2_NamedElement.methods={aadl2_NamedElement_m_qualifiedName, aadl2_NamedElement_m_isDistinguishableFrom, aadl2_NamedElement_m_separator, aadl2_NamedElement_m_has_no_qualified_name, aadl2_NamedElement_m_allNamespaces, aadl2_NamedElement_m_has_qualified_name}

# Element class attributes and methods

# aadl2_Property class attributes and methods
aadl2_Property_inherit: Property = Property(name="inherit", type=StringType)
aadl2_Property_emptyListDefault: Property = Property(name="emptyListDefault", type=StringType)
aadl2_Property.attributes={aadl2_Property_inherit, aadl2_Property_emptyListDefault}

# aadl2_ContainedNamedElement class attributes and methods

# aadl2_Classifier class attributes and methods
aadl2_Classifier_noPrototypes: Property = Property(name="noPrototypes", type=StringType)
aadl2_Classifier_noAnnexes: Property = Property(name="noAnnexes", type=StringType)
aadl2_Classifier_noProperties: Property = Property(name="noProperties", type=StringType)
aadl2_Classifier_m_no_cycles_in_generalization: Method = Method(name="no_cycles_in_generalization", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
aadl2_Classifier_m_allFeatures: Method = Method(name="allFeatures", parameters={}, type=StringType)
aadl2_Classifier_m_inheritedMember: Method = Method(name="inheritedMember", parameters={}, type=NamedElement)
aadl2_Classifier_m_parents: Method = Method(name="parents", parameters={}, type=StringType)
aadl2_Classifier_m_allParents: Method = Method(name="allParents", parameters={}, type=StringType)
aadl2_Classifier_m_inheritableMembers: Method = Method(name="inheritableMembers", parameters={Parameter(name='c')}, type=NamedElement)
aadl2_Classifier_m_specialize_type: Method = Method(name="specialize_type", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
aadl2_Classifier_m_maySpecializeType: Method = Method(name="maySpecializeType", parameters={Parameter(name='c')}, type=StringType)
aadl2_Classifier_m_hasVisibilityOf: Method = Method(name="hasVisibilityOf", parameters={Parameter(name='n')}, type=StringType)
aadl2_Classifier_m_inherit: Method = Method(name="inherit", parameters={Parameter(name='inhs')}, type=NamedElement)
aadl2_Classifier.attributes={aadl2_Classifier_noAnnexes, aadl2_Classifier_noProperties, aadl2_Classifier_noPrototypes}
aadl2_Classifier.methods={aadl2_Classifier_m_specialize_type, aadl2_Classifier_m_inheritableMembers, aadl2_Classifier_m_maySpecializeType, aadl2_Classifier_m_no_cycles_in_generalization, aadl2_Classifier_m_parents, aadl2_Classifier_m_inheritedMember, aadl2_Classifier_m_allFeatures, aadl2_Classifier_m_allParents, aadl2_Classifier_m_hasVisibilityOf, aadl2_Classifier_m_inherit}

# aadl2_ModalPropertyValue class attributes and methods

# BasicProperty class attributes and methods

# aadl2_PropertyExpression class attributes and methods

# aadl2_PropertyAssociation class attributes and methods
aadl2_PropertyAssociation_append: Property = Property(name="append", type=StringType)
aadl2_PropertyAssociation_constant: Property = Property(name="constant", type=StringType)
aadl2_PropertyAssociation.attributes={aadl2_PropertyAssociation_constant, aadl2_PropertyAssociation_append}

# aadl2_BasicProperty class attributes and methods
aadl2_BasicProperty_list: Property = Property(name="list", type=StringType)
aadl2_BasicProperty.attributes={aadl2_BasicProperty_list}

# TypedElement class attributes and methods

# aadl2_PropertyType class attributes and methods

# aadl2_TypedElement class attributes and methods

# aadl2_Type class attributes and methods
aadl2_Type_m_conformsTo: Method = Method(name="conformsTo", parameters={Parameter(name='other')}, type=StringType)
aadl2_Type.methods={aadl2_Type_m_conformsTo}

# aadl2_MetaclassReference class attributes and methods
aadl2_MetaclassReference_annexName: Property = Property(name="annexName", type=StringType)
aadl2_MetaclassReference_metaclassName: Property = Property(name="metaclassName", type=StringType)
aadl2_MetaclassReference.attributes={aadl2_MetaclassReference_metaclassName, aadl2_MetaclassReference_annexName}

# Type class attributes and methods

# aadl2_PropertyOwner class attributes and methods

# PropertyOwner class attributes and methods

# Namespace class attributes and methods

# aadl2_ClassifierFeature class attributes and methods

# aadl2_Generalization class attributes and methods

# aadl2_PrototypeBinding class attributes and methods

# DirectedRelationship class attributes and methods

# aadl2_AnnexSubclause class attributes and methods

# aadl2_Prototype class attributes and methods
aadl2_Prototype_m_categoryConstraint: Method = Method(name="categoryConstraint", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
aadl2_Prototype.methods={aadl2_Prototype_m_categoryConstraint}

# aadl2_DirectedRelationship class attributes and methods

# Relationship class attributes and methods

# aadl2_Relationship class attributes and methods

# aadl2_Mode class attributes and methods
aadl2_Mode_initial: Property = Property(name="initial", type=StringType)
aadl2_Mode_derived: Property = Property(name="derived", type=StringType)
aadl2_Mode.attributes={aadl2_Mode_initial, aadl2_Mode_derived}

# ModeFeature class attributes and methods

# aadl2_ModeFeature class attributes and methods

# ClassifierFeature class attributes and methods

# StructuralFeature class attributes and methods

# ModalElement class attributes and methods

# aadl2_ModalElement class attributes and methods
aadl2_ModalElement_modesAndTransitions: Property = Property(name="modesAndTransitions", type=StringType)
aadl2_ModalElement.attributes={aadl2_ModalElement_modesAndTransitions}

# aadl2_ContainmentPathElement class attributes and methods

# aadl2_StructuralFeature class attributes and methods

# RefinableElement class attributes and methods

# aadl2_RefinableElement class attributes and methods

# aadl2_BehavioralFeature class attributes and methods

# aadl2_ArraySpecification class attributes and methods
aadl2_ArraySpecification_dimension: Property = Property(name="dimension", type=StringType)
aadl2_ArraySpecification.attributes={aadl2_ArraySpecification_dimension}

# aadl2_ArraySize class attributes and methods

# aadl2_ArrayableElement class attributes and methods

# aadl2_Numeral class attributes and methods
aadl2_Numeral_value: Property = Property(name="value", type=StringType)
aadl2_Numeral.attributes={aadl2_Numeral_value}

# aadl2_ArrayRange class attributes and methods
aadl2_ArrayRange_lowerBound: Property = Property(name="lowerBound", type=StringType)
aadl2_ArrayRange_upperBound: Property = Property(name="upperBound", type=StringType)
aadl2_ArrayRange.attributes={aadl2_ArrayRange_lowerBound, aadl2_ArrayRange_upperBound}

# ArraySize class attributes and methods

# ComponentClassifier class attributes and methods

# aadl2_ComponentImplementationReference class attributes and methods

# aadl2_Subcomponent class attributes and methods
aadl2_Subcomponent_allModes: Property = Property(name="allModes", type=StringType)
aadl2_Subcomponent.attributes={aadl2_Subcomponent_allModes}

# aadl2_ComponentImplementation class attributes and methods
aadl2_ComponentImplementation_subcomponents: Property = Property(name="subcomponents", type=StringType)
aadl2_ComponentImplementation_connections: Property = Property(name="connections", type=StringType)
aadl2_ComponentImplementation_flows: Property = Property(name="flows", type=StringType)
aadl2_ComponentImplementation_noConnections: Property = Property(name="noConnections", type=StringType)
aadl2_ComponentImplementation_noCalls: Property = Property(name="noCalls", type=StringType)
aadl2_ComponentImplementation_noSubcomponents: Property = Property(name="noSubcomponents", type=StringType)
aadl2_ComponentImplementation.attributes={aadl2_ComponentImplementation_subcomponents, aadl2_ComponentImplementation_noCalls, aadl2_ComponentImplementation_noConnections, aadl2_ComponentImplementation_connections, aadl2_ComponentImplementation_flows, aadl2_ComponentImplementation_noSubcomponents}

# aadl2_FlowImplementation class attributes and methods
aadl2_FlowImplementation_kind: Property = Property(name="kind", type=StringType)
aadl2_FlowImplementation.attributes={aadl2_FlowImplementation_kind}

# aadl2_ComponentType class attributes and methods
aadl2_ComponentType_noFeatures: Property = Property(name="noFeatures", type=StringType)
aadl2_ComponentType_features: Property = Property(name="features", type=StringType)
aadl2_ComponentType.attributes={aadl2_ComponentType_noFeatures, aadl2_ComponentType_features}

# aadl2_Realization class attributes and methods

# aadl2_EndToEndFlow class attributes and methods

# aadl2_AbstractSubcomponent class attributes and methods

# aadl2_Connection class attributes and methods
aadl2_Connection_bidirectional: Property = Property(name="bidirectional", type=StringType)
aadl2_Connection_kind: Property = Property(name="kind", type=StringType)
aadl2_Connection.attributes={aadl2_Connection_kind, aadl2_Connection_bidirectional}

# aadl2_ImplementationExtension class attributes and methods

# aadl2_ParameterConnection class attributes and methods

# aadl2_PortConnection class attributes and methods

# aadl2_FeatureConnection class attributes and methods

# aadl2_AccessConnection class attributes and methods
aadl2_AccessConnection_accessCategory: Property = Property(name="accessCategory", type=StringType)
aadl2_AccessConnection.attributes={aadl2_AccessConnection_accessCategory}

# aadl2_ComponentClassifier class attributes and methods
aadl2_ComponentClassifier_noFlows: Property = Property(name="noFlows", type=StringType)
aadl2_ComponentClassifier_noModes: Property = Property(name="noModes", type=StringType)
aadl2_ComponentClassifier.attributes={aadl2_ComponentClassifier_noFlows, aadl2_ComponentClassifier_noModes}

# Classifier class attributes and methods

# aadl2_ModeTransition class attributes and methods

# aadl2_ProcessorPort class attributes and methods

# aadl2_InternalEvent class attributes and methods

# aadl2_FeatureGroupConnection class attributes and methods

# aadl2_ProcessorSubprogram class attributes and methods

# aadl2_TriggerPort class attributes and methods

# ModeTransitionTrigger class attributes and methods

# aadl2_Context class attributes and methods

# aadl2_Port class attributes and methods
aadl2_Port_category: Property = Property(name="category", type=StringType)
aadl2_Port.attributes={aadl2_Port_category}

# DirectedFeature class attributes and methods

# PortConnectionEnd class attributes and methods

# aadl2_ModeTransitionTrigger class attributes and methods

# aadl2_FeatureConnectionEnd class attributes and methods

# ConnectionEnd class attributes and methods

# aadl2_ConnectionEnd class attributes and methods

# aadl2_DirectedFeature class attributes and methods
aadl2_DirectedFeature_direction: Property = Property(name="direction", type=StringType)
aadl2_DirectedFeature.attributes={aadl2_DirectedFeature_direction}

# Feature class attributes and methods

# aadl2_Feature class attributes and methods

# FeatureConnectionEnd class attributes and methods

# ArrayableElement class attributes and methods

# aadl2_FlowSpecification class attributes and methods
aadl2_FlowSpecification_kind: Property = Property(name="kind", type=StringType)
aadl2_FlowSpecification.attributes={aadl2_FlowSpecification_kind}

# aadl2_TypeExtension class attributes and methods

# aadl2_FeatureGroup class attributes and methods
aadl2_FeatureGroup_inverse: Property = Property(name="inverse", type=StringType)
aadl2_FeatureGroup.attributes={aadl2_FeatureGroup_inverse}

# aadl2_AbstractFeature class attributes and methods

# Flow class attributes and methods

# aadl2_PortConnectionEnd class attributes and methods

# Generalization class attributes and methods

# Context class attributes and methods

# FeatureGroupConnectionEnd class attributes and methods

# CallContext class attributes and methods

# aadl2_FeatureGroupType class attributes and methods
aadl2_FeatureGroupType_feature: Property = Property(name="feature", type=StringType)
aadl2_FeatureGroupType.attributes={aadl2_FeatureGroupType_feature}

# aadl2_FeatureGroupConnectionEnd class attributes and methods

# aadl2_CallContext class attributes and methods

# aadl2_DataPort class attributes and methods

# aadl2_EventDataPort class attributes and methods

# aadl2_EventPort class attributes and methods

# aadl2_Flow class attributes and methods

# aadl2_GroupExtension class attributes and methods

# aadl2_BusAccess class attributes and methods

# aadl2_DataAccess class attributes and methods

# Access class attributes and methods

# aadl2_BusClassifier class attributes and methods

# aadl2_Access class attributes and methods
aadl2_Access_kind: Property = Property(name="kind", type=StringType)
aadl2_Access_category: Property = Property(name="category", type=StringType)
aadl2_Access.attributes={aadl2_Access_kind, aadl2_Access_category}

# AccessConnectionEnd class attributes and methods

# aadl2_AccessConnectionEnd class attributes and methods

# aadl2_Parameter class attributes and methods

# aadl2_SubprogramAccess class attributes and methods

# aadl2_SubprogramGroupAccess class attributes and methods

# CalledSubprogram class attributes and methods

# aadl2_SubprogramClassifier class attributes and methods

# aadl2_CalledSubprogram class attributes and methods

# Bus class attributes and methods

# aadl2_Bus class attributes and methods

# FlowElement class attributes and methods

# ParameterConnectionEnd class attributes and methods

# aadl2_DataClassifier class attributes and methods

# aadl2_ParameterConnectionEnd class attributes and methods

# aadl2_FlowElement class attributes and methods

# EndToEndFlowElement class attributes and methods

# aadl2_EndToEndFlowElement class attributes and methods

# Data class attributes and methods

# aadl2_Data class attributes and methods

# Port class attributes and methods

# aadl2_ComponentPrototype class attributes and methods
aadl2_ComponentPrototype_category: Property = Property(name="category", type=StringType)
aadl2_ComponentPrototype_array: Property = Property(name="array", type=StringType)
aadl2_ComponentPrototype.attributes={aadl2_ComponentPrototype_category, aadl2_ComponentPrototype_array}

# aadl2_ModeBinding class attributes and methods

# aadl2_AbstractClassifier class attributes and methods

# Subprogram class attributes and methods

# aadl2_Subprogram class attributes and methods

# aadl2_SubprogramGroupClassifier class attributes and methods

# SubprogramGroup class attributes and methods

# aadl2_SubprogramGroup class attributes and methods

# Abstract class attributes and methods

# aadl2_Abstract class attributes and methods

# ModalPath class attributes and methods

# aadl2_SubcomponentFlow class attributes and methods

# Prototype class attributes and methods

# aadl2_ModalPath class attributes and methods

# Subcomponent class attributes and methods

# Connection class attributes and methods

# aadl2_PackageRename class attributes and methods
aadl2_PackageRename_renameAll: Property = Property(name="renameAll", type=StringType)
aadl2_PackageRename.attributes={aadl2_PackageRename_renameAll}

# aadl2_ComponentTypeRename class attributes and methods
aadl2_ComponentTypeRename_category: Property = Property(name="category", type=StringType)
aadl2_ComponentTypeRename.attributes={aadl2_ComponentTypeRename_category}

# aadl2_FeatureGroupTypeRename class attributes and methods

# aadl2_AnnexLibrary class attributes and methods

# aadl2_DefaultAnnexLibrary class attributes and methods
aadl2_DefaultAnnexLibrary_sourceText: Property = Property(name="sourceText", type=StringType)
aadl2_DefaultAnnexLibrary.attributes={aadl2_DefaultAnnexLibrary_sourceText}

# AnnexLibrary class attributes and methods

# aadl2_DefaultAnnexSubclause class attributes and methods
aadl2_DefaultAnnexSubclause_sourceText: Property = Property(name="sourceText", type=StringType)
aadl2_DefaultAnnexSubclause.attributes={aadl2_DefaultAnnexSubclause_sourceText}

# AnnexSubclause class attributes and methods

# aadl2_PublicPackageSection class attributes and methods

# PackageSection class attributes and methods

# aadl2_PrivatePackageSection class attributes and methods

# aadl2_PackageSection class attributes and methods
aadl2_PackageSection_declarations: Property = Property(name="declarations", type=StringType)
aadl2_PackageSection_imports: Property = Property(name="imports", type=StringType)
aadl2_PackageSection_aliases: Property = Property(name="aliases", type=StringType)
aadl2_PackageSection_noAnnexes: Property = Property(name="noAnnexes", type=StringType)
aadl2_PackageSection_noProperties: Property = Property(name="noProperties", type=StringType)
aadl2_PackageSection.attributes={aadl2_PackageSection_imports, aadl2_PackageSection_declarations, aadl2_PackageSection_noProperties, aadl2_PackageSection_aliases, aadl2_PackageSection_noAnnexes}

# aadl2_BusType class attributes and methods

# aadl2_BusImplementation class attributes and methods

# aadl2_DataType class attributes and methods

# aadl2_DataImplementation class attributes and methods

# aadl2_DeviceType class attributes and methods

# aadl2_AadlPackage class attributes and methods

# aadl2_AbstractType class attributes and methods

# aadl2_AbstractImplementation class attributes and methods

# aadl2_ProcessorType class attributes and methods

# aadl2_ProcessImplementation class attributes and methods

# aadl2_ProcessorImplementation class attributes and methods

# aadl2_SubprogramType class attributes and methods

# aadl2_DeviceImplementation class attributes and methods

# aadl2_MemoryType class attributes and methods

# aadl2_MemoryImplementation class attributes and methods

# aadl2_ProcessType class attributes and methods

# aadl2_ThreadType class attributes and methods

# aadl2_ThreadImplementation class attributes and methods

# aadl2_ThreadGroupType class attributes and methods

# aadl2_SubprogramImplementation class attributes and methods

# aadl2_ThreadGroupImplementation class attributes and methods

# aadl2_SubprogramGroupType class attributes and methods

# aadl2_SubprogramGroupImplementation class attributes and methods

# aadl2_SystemType class attributes and methods

# aadl2_SystemImplementation class attributes and methods

# aadl2_VirtualProcessorImplementation class attributes and methods

# aadl2_PropertySet class attributes and methods
aadl2_PropertySet_imports: Property = Property(name="imports", type=StringType)
aadl2_PropertySet_contents: Property = Property(name="contents", type=StringType)
aadl2_PropertySet.attributes={aadl2_PropertySet_imports, aadl2_PropertySet_contents}

# aadl2_VirtualBusType class attributes and methods

# aadl2_VirtualBusImplementation class attributes and methods

# aadl2_VirtualProcessorType class attributes and methods

# ComponentType class attributes and methods

# AbstractClassifier class attributes and methods

# BehavioredImplementation class attributes and methods

# aadl2_BusSubcomponent class attributes and methods

# aadl2_SubprogramSubcomponent class attributes and methods

# aadl2_SubprogramGroupSubcomponent class attributes and methods

# aadl2_ThreadSubcomponent class attributes and methods

# aadl2_DataSubcomponent class attributes and methods

# aadl2_ThreadGroupSubcomponent class attributes and methods

# aadl2_DeviceSubcomponent class attributes and methods

# aadl2_VirtualBusSubcomponent class attributes and methods

# aadl2_MemorySubcomponent class attributes and methods

# aadl2_VirtualProcessorSubcomponent class attributes and methods

# aadl2_ProcessSubcomponent class attributes and methods

# aadl2_ProcessorSubcomponent class attributes and methods

# aadl2_SystemSubcomponent class attributes and methods

# aadl2_SubprogramCallSequence class attributes and methods

# BehavioralFeature class attributes and methods

# Device class attributes and methods

# aadl2_DeviceClassifier class attributes and methods

# aadl2_Device class attributes and methods

# Memory class attributes and methods

# aadl2_MemoryClassifier class attributes and methods

# aadl2_Memory class attributes and methods

# aadl2_BehavioredImplementation class attributes and methods
aadl2_BehavioredImplementation_m_callSpecifications: Method = Method(name="callSpecifications", parameters={}, type=StringType)
aadl2_BehavioredImplementation.methods={aadl2_BehavioredImplementation_m_callSpecifications}

# ComponentImplementation class attributes and methods

# aadl2_CallSpecification class attributes and methods

# aadl2_Process class attributes and methods

# Processor class attributes and methods

# aadl2_ProcessorClassifier class attributes and methods

# aadl2_Processor class attributes and methods

# System class attributes and methods

# aadl2_SystemClassifier class attributes and methods

# aadl2_System class attributes and methods

# Thread class attributes and methods

# aadl2_ThreadClassifier class attributes and methods

# Process class attributes and methods

# aadl2_ProcessClassifier class attributes and methods

# aadl2_ThreadGroup class attributes and methods

# VirtualBus class attributes and methods

# aadl2_VirtualBusClassifier class attributes and methods

# aadl2_VirtualBus class attributes and methods

# VirtualProcessor class attributes and methods

# aadl2_VirtualProcessorClassifier class attributes and methods

# aadl2_VirtualProcessor class attributes and methods

# BusClassifier class attributes and methods

# aadl2_Thread class attributes and methods

# ThreadGroup class attributes and methods

# aadl2_ThreadGroupClassifier class attributes and methods

# DeviceClassifier class attributes and methods

# DataClassifier class attributes and methods

# MemoryClassifier class attributes and methods

# ProcessClassifier class attributes and methods

# ProcessorClassifier class attributes and methods

# SubprogramClassifier class attributes and methods

# SubprogramGroupClassifier class attributes and methods

# SystemClassifier class attributes and methods

# ThreadClassifier class attributes and methods

# ThreadGroupClassifier class attributes and methods

# VirtualBusClassifier class attributes and methods

# VirtualProcessorClassifier class attributes and methods

# aadl2_PropertyConstant class attributes and methods
aadl2_PropertyConstant_list: Property = Property(name="list", type=StringType)
aadl2_PropertyConstant.attributes={aadl2_PropertyConstant_list}

# aadl2_ComponentPrototypeBinding class attributes and methods

# PrototypeBinding class attributes and methods

# aadl2_ComponentPrototypeActual class attributes and methods
aadl2_ComponentPrototypeActual_category: Property = Property(name="category", type=StringType)
aadl2_ComponentPrototypeActual.attributes={aadl2_ComponentPrototypeActual_category}

# aadl2_FeatureGroupPrototypeBinding class attributes and methods

# aadl2_FeatureGroupPrototypeActual class attributes and methods

# aadl2_FeaturePrototype class attributes and methods
aadl2_FeaturePrototype_direction: Property = Property(name="direction", type=StringType)
aadl2_FeaturePrototype.attributes={aadl2_FeaturePrototype_direction}

# aadl2_FeatureGroupPrototype class attributes and methods

# aadl2_FeaturePrototypeBinding class attributes and methods

# aadl2_FeaturePrototypeActual class attributes and methods

# aadl2_AccessSpecification class attributes and methods
aadl2_AccessSpecification_kind: Property = Property(name="kind", type=StringType)
aadl2_AccessSpecification_category: Property = Property(name="category", type=StringType)
aadl2_AccessSpecification.attributes={aadl2_AccessSpecification_kind, aadl2_AccessSpecification_category}

# FeaturePrototypeActual class attributes and methods

# aadl2_PortSpecification class attributes and methods
aadl2_PortSpecification_category: Property = Property(name="category", type=StringType)
aadl2_PortSpecification_direction: Property = Property(name="direction", type=StringType)
aadl2_PortSpecification.attributes={aadl2_PortSpecification_category, aadl2_PortSpecification_direction}

# aadl2_FeaturePrototypeReference class attributes and methods
aadl2_FeaturePrototypeReference_direction: Property = Property(name="direction", type=StringType)
aadl2_FeaturePrototypeReference.attributes={aadl2_FeaturePrototypeReference_direction}

# aadl2_ComponentPrototypeReference class attributes and methods

# ComponentPrototypeActual class attributes and methods

# aadl2_ComponentReference class attributes and methods

# aadl2_BasicPropertyAssociation class attributes and methods

# aadl2_FeatureGroupPrototypeReference class attributes and methods

# FeatureGroupPrototypeActual class attributes and methods

# aadl2_FeatureGroupReference class attributes and methods

# aadl2_ProcessorCall class attributes and methods
aadl2_ProcessorCall_subprogramAccessName: Property = Property(name="subprogramAccessName", type=StringType)
aadl2_ProcessorCall.attributes={aadl2_ProcessorCall_subprogramAccessName}

# CallSpecification class attributes and methods

# aadl2_SubprogramCall class attributes and methods

# aadl2_StringLiteral class attributes and methods
aadl2_StringLiteral_value: Property = Property(name="value", type=StringType)
aadl2_StringLiteral.attributes={aadl2_StringLiteral_value}

# aadl2_EnumerationValue class attributes and methods

# PropertyValue class attributes and methods

# aadl2_EnumerationLiteral class attributes and methods

# aadl2_PropertyValue class attributes and methods

# PropertyExpression class attributes and methods

# aadl2_UnitValue class attributes and methods

# aadl2_UnitLiteral class attributes and methods

# EnumerationLiteral class attributes and methods

# aadl2_NumberValue class attributes and methods
aadl2_NumberValue_valueString: Property = Property(name="valueString", type=StringType)
aadl2_NumberValue.attributes={aadl2_NumberValue_valueString}

# aadl2_RealLiteral class attributes and methods
aadl2_RealLiteral_value: Property = Property(name="value", type=StringType)
aadl2_RealLiteral.attributes={aadl2_RealLiteral_value}

# aadl2_ClassifierValue class attributes and methods

# aadl2_ReferenceValue class attributes and methods

# ContainedNamedElement class attributes and methods

# aadl2_BooleanLiteral class attributes and methods
aadl2_BooleanLiteral_value: Property = Property(name="value", type=StringType)
aadl2_BooleanLiteral.attributes={aadl2_BooleanLiteral_value}

# aadl2_RangeValue class attributes and methods

# aadl2_IntegerLiteral class attributes and methods
aadl2_IntegerLiteral_value: Property = Property(name="value", type=StringType)
aadl2_IntegerLiteral_base: Property = Property(name="base", type=StringType)
aadl2_IntegerLiteral.attributes={aadl2_IntegerLiteral_value, aadl2_IntegerLiteral_base}

# NumberValue class attributes and methods

# aadl2_RecordValue class attributes and methods

# aadl2_ConstantValue class attributes and methods

# aadl2_PropertyReference class attributes and methods

# aadl2_Operation class attributes and methods
aadl2_Operation_op: Property = Property(name="op", type=StringType)
aadl2_Operation.attributes={aadl2_Operation_op}

# aadl2_NumberType class attributes and methods

# aadl2_UnitsType class attributes and methods

# aadl2_ComputedValue class attributes and methods
aadl2_ComputedValue_function: Property = Property(name="function", type=StringType)
aadl2_ComputedValue.attributes={aadl2_ComputedValue_function}

# aadl2_ListValue class attributes and methods

# aadl2_GlobalNamespace class attributes and methods

# aadl2_AadlBoolean class attributes and methods

# PropertyType class attributes and methods

# aadl2_AadlString class attributes and methods

# aadl2_AadlInteger class attributes and methods

# NumberType class attributes and methods

# aadl2_AadlReal class attributes and methods

# aadl2_NumericRange class attributes and methods

# EnumerationType class attributes and methods

# aadl2_EnumerationType class attributes and methods

# aadl2_ClassifierType class attributes and methods

# aadl2_RangeType class attributes and methods

# aadl2_RecordType class attributes and methods

# aadl2_RecordField class attributes and methods

# aadl2_ReferenceType class attributes and methods

# Relationships
ownedElement1: BinaryAssociation = BinaryAssociation(
    name="ownedElement1",
    ends={
        Property(name="Element", type=aadl2_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=aadl2_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner3: BinaryAssociation = BinaryAssociation(
    name="owner3",
    ends={
        Property(name="Element4", type=aadl2_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElement", type=aadl2_Element, multiplicity=Multiplicity(0, 1))
    }
)
ownedComment5: BinaryAssociation = BinaryAssociation(
    name="ownedComment5",
    ends={
        Property(name="aadl2_Comment", type=aadl2_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Element", type=aadl2_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedMember6: BinaryAssociation = BinaryAssociation(
    name="ownedMember6",
    ends={
        Property(name="NamedElement", type=aadl2_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=aadl2_NamedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
member7: BinaryAssociation = BinaryAssociation(
    name="member7",
    ends={
        Property(name="aadl2_NamedElement", type=aadl2_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Namespace", type=aadl2_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
property11: BinaryAssociation = BinaryAssociation(
    name="property11",
    ends={
        Property(name="aadl2_Property", type=aadl2_PropertyAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertyAssociation12", type=aadl2_Property, multiplicity=Multiplicity(1, 1))
    }
)
appliesTo13: BinaryAssociation = BinaryAssociation(
    name="appliesTo13",
    ends={
        Property(name="aadl2_ContainedNamedElement", type=aadl2_PropertyAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertyAssociation14", type=aadl2_ContainedNamedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inBinding15: BinaryAssociation = BinaryAssociation(
    name="inBinding15",
    ends={
        Property(name="aadl2_Classifier", type=aadl2_PropertyAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertyAssociation16", type=aadl2_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
ownedValue17: BinaryAssociation = BinaryAssociation(
    name="ownedValue17",
    ends={
        Property(name="aadl2_ModalPropertyValue", type=aadl2_PropertyAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertyAssociation18", type=aadl2_ModalPropertyValue, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
defaultValue19: BinaryAssociation = BinaryAssociation(
    name="defaultValue19",
    ends={
        Property(name="aadl2_PropertyExpression", type=aadl2_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Property20", type=aadl2_PropertyExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
namespace8: BinaryAssociation = BinaryAssociation(
    name="namespace8",
    ends={
        Property(name="Namespace", type=aadl2_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedMember", type=aadl2_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
ownedPropertyAssociation9: BinaryAssociation = BinaryAssociation(
    name="ownedPropertyAssociation9",
    ends={
        Property(name="aadl2_PropertyAssociation", type=aadl2_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_NamedElement10", type=aadl2_PropertyAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedType28: BinaryAssociation = BinaryAssociation(
    name="ownedType28",
    ends={
        Property(name="aadl2_PropertyType", type=aadl2_BasicProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BasicProperty", type=aadl2_PropertyType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type29: BinaryAssociation = BinaryAssociation(
    name="type29",
    ends={
        Property(name="aadl2_Type", type=aadl2_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_TypedElement", type=aadl2_Type, multiplicity=Multiplicity(0, 1))
    }
)
appliesToMetaclass21: BinaryAssociation = BinaryAssociation(
    name="appliesToMetaclass21",
    ends={
        Property(name="aadl2_MetaclassReference", type=aadl2_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Property22", type=aadl2_MetaclassReference, multiplicity=Multiplicity(0, 9999))
    }
)
appliesToClassifier23: BinaryAssociation = BinaryAssociation(
    name="appliesToClassifier23",
    ends={
        Property(name="aadl2_Classifier25", type=aadl2_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Property24", type=aadl2_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
appliesTo26: BinaryAssociation = BinaryAssociation(
    name="appliesTo26",
    ends={
        Property(name="aadl2_PropertyOwner", type=aadl2_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Property27", type=aadl2_PropertyOwner, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
        Property(name="specific", type=aadl2_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPrototypeBinding42: BinaryAssociation = BinaryAssociation(
    name="ownedPrototypeBinding42",
    ends={
        Property(name="aadl2_PrototypeBinding", type=aadl2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Classifier43", type=aadl2_PrototypeBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featuringClassifier44: BinaryAssociation = BinaryAssociation(
    name="featuringClassifier44",
    ends={
        Property(name="Classifier", type=aadl2_ClassifierFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="classifierFeature", type=aadl2_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
general36: BinaryAssociation = BinaryAssociation(
    name="general36",
    ends={
        Property(name="aadl2_Classifier37", type=aadl2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Classifier35", type=aadl2_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
general45: BinaryAssociation = BinaryAssociation(
    name="general45",
    ends={
        Property(name="aadl2_Classifier46", type=aadl2_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Generalization", type=aadl2_Classifier, multiplicity=Multiplicity(1, 1))
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
source49: BinaryAssociation = BinaryAssociation(
    name="source49",
    ends={
        Property(name="aadl2_Element50", type=aadl2_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DirectedRelationship", type=aadl2_Element, multiplicity=Multiplicity(1, 9999))
    }
)
target51: BinaryAssociation = BinaryAssociation(
    name="target51",
    ends={
        Property(name="aadl2_Element53", type=aadl2_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DirectedRelationship52", type=aadl2_Element, multiplicity=Multiplicity(1, 9999))
    }
)
relatedElement54: BinaryAssociation = BinaryAssociation(
    name="relatedElement54",
    ends={
        Property(name="aadl2_Element55", type=aadl2_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Relationship", type=aadl2_Element, multiplicity=Multiplicity(1, 9999))
    }
)
specific47: BinaryAssociation = BinaryAssociation(
    name="specific47",
    ends={
        Property(name="Classifier48", type=aadl2_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization", type=aadl2_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
inMode56: BinaryAssociation = BinaryAssociation(
    name="inMode56",
    ends={
        Property(name="aadl2_Mode", type=aadl2_ModalElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ModalElement", type=aadl2_Mode, multiplicity=Multiplicity(0, 9999))
    }
)
refinementContext60: BinaryAssociation = BinaryAssociation(
    name="refinementContext60",
    ends={
        Property(name="aadl2_Classifier61", type=aadl2_RefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_RefinableElement", type=aadl2_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
refinedElement63: BinaryAssociation = BinaryAssociation(
    name="refinedElement63",
    ends={
        Property(name="aadl2_RefinableElement64", type=aadl2_RefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_RefinableElement62", type=aadl2_RefinableElement, multiplicity=Multiplicity(0, 1))
    }
)
formal65: BinaryAssociation = BinaryAssociation(
    name="formal65",
    ends={
        Property(name="aadl2_Prototype67", type=aadl2_PrototypeBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PrototypeBinding66", type=aadl2_Prototype, multiplicity=Multiplicity(1, 1))
    }
)
containmentPathElement68: BinaryAssociation = BinaryAssociation(
    name="containmentPathElement68",
    ends={
        Property(name="aadl2_ContainmentPathElement", type=aadl2_ContainedNamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ContainedNamedElement69", type=aadl2_ContainmentPathElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
refined58: BinaryAssociation = BinaryAssociation(
    name="refined58",
    ends={
        Property(name="aadl2_Prototype59", type=aadl2_Prototype, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Prototype57", type=aadl2_Prototype, multiplicity=Multiplicity(0, 1))
    }
)
ownedValue75: BinaryAssociation = BinaryAssociation(
    name="ownedValue75",
    ends={
        Property(name="aadl2_PropertyExpression77", type=aadl2_ModalPropertyValue, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ModalPropertyValue76", type=aadl2_PropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
size78: BinaryAssociation = BinaryAssociation(
    name="size78",
    ends={
        Property(name="aadl2_ArraySize", type=aadl2_ArraySpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ArraySpecification", type=aadl2_ArraySize, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arraySpecification79: BinaryAssociation = BinaryAssociation(
    name="arraySpecification79",
    ends={
        Property(name="aadl2_ArraySpecification80", type=aadl2_ArrayableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ArrayableElement", type=aadl2_ArraySpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayRange70: BinaryAssociation = BinaryAssociation(
    name="arrayRange70",
    ends={
        Property(name="aadl2_ArrayRange", type=aadl2_ContainmentPathElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ContainmentPathElement71", type=aadl2_ArrayRange, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
namedElement72: BinaryAssociation = BinaryAssociation(
    name="namedElement72",
    ends={
        Property(name="aadl2_NamedElement74", type=aadl2_ContainmentPathElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ContainmentPathElement73", type=aadl2_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
implementation81: BinaryAssociation = BinaryAssociation(
    name="implementation81",
    ends={
        Property(name="aadl2_ComponentImplementationReference", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation", type=aadl2_ComponentImplementationReference, multiplicity=Multiplicity(1, 1))
    }
)
ownedPrototypeBinding82: BinaryAssociation = BinaryAssociation(
    name="ownedPrototypeBinding82",
    ends={
        Property(name="aadl2_PrototypeBinding84", type=aadl2_ComponentImplementationReference, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementationReference83", type=aadl2_PrototypeBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubcomponent87: BinaryAssociation = BinaryAssociation(
    name="ownedSubcomponent87",
    ends={
        Property(name="aadl2_Subcomponent", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation88", type=aadl2_Subcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extended90: BinaryAssociation = BinaryAssociation(
    name="extended90",
    ends={
        Property(name="aadl2_ComponentImplementation91", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation89", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(0, 1))
    }
)
type85: BinaryAssociation = BinaryAssociation(
    name="type85",
    ends={
        Property(name="aadl2_ComponentType", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation86", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1))
    }
)
ownedExtension96: BinaryAssociation = BinaryAssociation(
    name="ownedExtension96",
    ends={
        Property(name="aadl2_ImplementationExtension", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation97", type=aadl2_ImplementationExtension, multiplicity=Multiplicity(0, 1))
    }
)
ownedRealization98: BinaryAssociation = BinaryAssociation(
    name="ownedRealization98",
    ends={
        Property(name="aadl2_Realization", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation99", type=aadl2_Realization, multiplicity=Multiplicity(1, 1))
    }
)
ownedEndToEndFlow100: BinaryAssociation = BinaryAssociation(
    name="ownedEndToEndFlow100",
    ends={
        Property(name="aadl2_EndToEndFlow", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation101", type=aadl2_EndToEndFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedFlowImplementation92: BinaryAssociation = BinaryAssociation(
    name="ownedFlowImplementation92",
    ends={
        Property(name="aadl2_FlowImplementation", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation93", type=aadl2_FlowImplementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedConnection94: BinaryAssociation = BinaryAssociation(
    name="ownedConnection94",
    ends={
        Property(name="aadl2_Connection", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation95", type=aadl2_Connection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedParameterConnection106: BinaryAssociation = BinaryAssociation(
    name="ownedParameterConnection106",
    ends={
        Property(name="aadl2_ParameterConnection", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation107", type=aadl2_ParameterConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPortConnection108: BinaryAssociation = BinaryAssociation(
    name="ownedPortConnection108",
    ends={
        Property(name="aadl2_PortConnection", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation109", type=aadl2_PortConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedFeatureConnection110: BinaryAssociation = BinaryAssociation(
    name="ownedFeatureConnection110",
    ends={
        Property(name="aadl2_FeatureConnection", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation111", type=aadl2_FeatureConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAbstractSubcomponent102: BinaryAssociation = BinaryAssociation(
    name="ownedAbstractSubcomponent102",
    ends={
        Property(name="aadl2_AbstractSubcomponent", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation103", type=aadl2_AbstractSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAccessConnection104: BinaryAssociation = BinaryAssociation(
    name="ownedAccessConnection104",
    ends={
        Property(name="aadl2_AccessConnection", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation105", type=aadl2_AccessConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedMode116: BinaryAssociation = BinaryAssociation(
    name="ownedMode116",
    ends={
        Property(name="aadl2_Mode117", type=aadl2_ComponentClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentClassifier", type=aadl2_Mode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedModeTransition118: BinaryAssociation = BinaryAssociation(
    name="ownedModeTransition118",
    ends={
        Property(name="aadl2_ModeTransition", type=aadl2_ComponentClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentClassifier119", type=aadl2_ModeTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProcessorPort120: BinaryAssociation = BinaryAssociation(
    name="ownedProcessorPort120",
    ends={
        Property(name="aadl2_ProcessorPort", type=aadl2_ComponentClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentClassifier121", type=aadl2_ProcessorPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedInternalEvent122: BinaryAssociation = BinaryAssociation(
    name="ownedInternalEvent122",
    ends={
        Property(name="aadl2_InternalEvent", type=aadl2_ComponentClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentClassifier123", type=aadl2_InternalEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedFeatureGroupConnection112: BinaryAssociation = BinaryAssociation(
    name="ownedFeatureGroupConnection112",
    ends={
        Property(name="aadl2_FeatureGroupConnection", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation113", type=aadl2_FeatureGroupConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProcessorSubprogram114: BinaryAssociation = BinaryAssociation(
    name="ownedProcessorSubprogram114",
    ends={
        Property(name="aadl2_ProcessorSubprogram", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentImplementation115", type=aadl2_ProcessorSubprogram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trigger130: BinaryAssociation = BinaryAssociation(
    name="trigger130",
    ends={
        Property(name="aadl2_ModeTransition131", type=aadl2_ModeTransitionTrigger, multiplicity=Multiplicity(1, 9999)),
        Property(name="aadl2_ModeTransitionTrigger", type=aadl2_ModeTransition, multiplicity=Multiplicity(1, 1))
    }
)
ownedTrigger132: BinaryAssociation = BinaryAssociation(
    name="ownedTrigger132",
    ends={
        Property(name="aadl2_TriggerPort", type=aadl2_ModeTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ModeTransition133", type=aadl2_TriggerPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context134: BinaryAssociation = BinaryAssociation(
    name="context134",
    ends={
        Property(name="aadl2_Context", type=aadl2_TriggerPort, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_TriggerPort135", type=aadl2_Context, multiplicity=Multiplicity(0, 1))
    }
)
port136: BinaryAssociation = BinaryAssociation(
    name="port136",
    ends={
        Property(name="aadl2_Port", type=aadl2_TriggerPort, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_TriggerPort137", type=aadl2_Port, multiplicity=Multiplicity(1, 1))
    }
)
source124: BinaryAssociation = BinaryAssociation(
    name="source124",
    ends={
        Property(name="aadl2_Mode126", type=aadl2_ModeTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ModeTransition125", type=aadl2_Mode, multiplicity=Multiplicity(1, 1))
    }
)
destination127: BinaryAssociation = BinaryAssociation(
    name="destination127",
    ends={
        Property(name="aadl2_Mode129", type=aadl2_ModeTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ModeTransition128", type=aadl2_Mode, multiplicity=Multiplicity(1, 1))
    }
)
classifier140: BinaryAssociation = BinaryAssociation(
    name="classifier140",
    ends={
        Property(name="aadl2_ComponentClassifier142", type=aadl2_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Feature141", type=aadl2_ComponentClassifier, multiplicity=Multiplicity(0, 1))
    }
)
refined144: BinaryAssociation = BinaryAssociation(
    name="refined144",
    ends={
        Property(name="aadl2_Feature145", type=aadl2_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Feature143", type=aadl2_Feature, multiplicity=Multiplicity(0, 1))
    }
)
prototype138: BinaryAssociation = BinaryAssociation(
    name="prototype138",
    ends={
        Property(name="aadl2_Prototype139", type=aadl2_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Feature", type=aadl2_Prototype, multiplicity=Multiplicity(0, 1))
    }
)
extended150: BinaryAssociation = BinaryAssociation(
    name="extended150",
    ends={
        Property(name="aadl2_ComponentType151", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentType149", type=aadl2_ComponentType, multiplicity=Multiplicity(0, 1))
    }
)
ownedFlowSpecification152: BinaryAssociation = BinaryAssociation(
    name="ownedFlowSpecification152",
    ends={
        Property(name="aadl2_FlowSpecification", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentType153", type=aadl2_FlowSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedExtension154: BinaryAssociation = BinaryAssociation(
    name="ownedExtension154",
    ends={
        Property(name="aadl2_TypeExtension", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentType155", type=aadl2_TypeExtension, multiplicity=Multiplicity(0, 1))
    }
)
ownedFeatureGroup156: BinaryAssociation = BinaryAssociation(
    name="ownedFeatureGroup156",
    ends={
        Property(name="aadl2_FeatureGroup", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentType157", type=aadl2_FeatureGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAbstractFeature158: BinaryAssociation = BinaryAssociation(
    name="ownedAbstractFeature158",
    ends={
        Property(name="aadl2_AbstractFeature", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentType159", type=aadl2_AbstractFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refined161: BinaryAssociation = BinaryAssociation(
    name="refined161",
    ends={
        Property(name="aadl2_FlowSpecification162", type=aadl2_FlowSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FlowSpecification160", type=aadl2_FlowSpecification, multiplicity=Multiplicity(0, 1))
    }
)
inFeature163: BinaryAssociation = BinaryAssociation(
    name="inFeature163",
    ends={
        Property(name="aadl2_Feature165", type=aadl2_FlowSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FlowSpecification164", type=aadl2_Feature, multiplicity=Multiplicity(0, 1))
    }
)
inContext166: BinaryAssociation = BinaryAssociation(
    name="inContext166",
    ends={
        Property(name="aadl2_Context168", type=aadl2_FlowSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FlowSpecification167", type=aadl2_Context, multiplicity=Multiplicity(0, 1))
    }
)
outFeature169: BinaryAssociation = BinaryAssociation(
    name="outFeature169",
    ends={
        Property(name="aadl2_Feature171", type=aadl2_FlowSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FlowSpecification170", type=aadl2_Feature, multiplicity=Multiplicity(0, 1))
    }
)
ownedFeature146: BinaryAssociation = BinaryAssociation(
    name="ownedFeature146",
    ends={
        Property(name="aadl2_Feature148", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentType147", type=aadl2_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extended175: BinaryAssociation = BinaryAssociation(
    name="extended175",
    ends={
        Property(name="aadl2_ComponentType177", type=aadl2_TypeExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_TypeExtension176", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1))
    }
)
featureGroupType178: BinaryAssociation = BinaryAssociation(
    name="featureGroupType178",
    ends={
        Property(name="aadl2_FeatureGroupType", type=aadl2_FeatureGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroup179", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1))
    }
)
ownedDataPort195: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort195",
    ends={
        Property(name="aadl2_DataPort", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType196", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort197: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort197",
    ends={
        Property(name="aadl2_EventDataPort", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType198", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort199: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort199",
    ends={
        Property(name="aadl2_EventPort", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType200", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedFeatureGroup201: BinaryAssociation = BinaryAssociation(
    name="ownedFeatureGroup201",
    ends={
        Property(name="aadl2_FeatureGroup203", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType202", type=aadl2_FeatureGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outContext172: BinaryAssociation = BinaryAssociation(
    name="outContext172",
    ends={
        Property(name="aadl2_Context174", type=aadl2_FlowSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FlowSpecification173", type=aadl2_Context, multiplicity=Multiplicity(0, 1))
    }
)
ownedFeature180: BinaryAssociation = BinaryAssociation(
    name="ownedFeature180",
    ends={
        Property(name="aadl2_Feature182", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType181", type=aadl2_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extended184: BinaryAssociation = BinaryAssociation(
    name="extended184",
    ends={
        Property(name="aadl2_FeatureGroupType185", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType183", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(0, 1))
    }
)
inverse187: BinaryAssociation = BinaryAssociation(
    name="inverse187",
    ends={
        Property(name="aadl2_FeatureGroupType188", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType186", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(0, 1))
    }
)
ownedExtension189: BinaryAssociation = BinaryAssociation(
    name="ownedExtension189",
    ends={
        Property(name="aadl2_GroupExtension", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType190", type=aadl2_GroupExtension, multiplicity=Multiplicity(0, 1))
    }
)
ownedBusAccess191: BinaryAssociation = BinaryAssociation(
    name="ownedBusAccess191",
    ends={
        Property(name="aadl2_BusAccess", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType192", type=aadl2_BusAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataAccess193: BinaryAssociation = BinaryAssociation(
    name="ownedDataAccess193",
    ends={
        Property(name="aadl2_DataAccess", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType194", type=aadl2_DataAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extended213: BinaryAssociation = BinaryAssociation(
    name="extended213",
    ends={
        Property(name="aadl2_FeatureGroupType215", type=aadl2_GroupExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_GroupExtension214", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1))
    }
)
busClassifier216: BinaryAssociation = BinaryAssociation(
    name="busClassifier216",
    ends={
        Property(name="aadl2_BusClassifier", type=aadl2_BusAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BusAccess217", type=aadl2_BusClassifier, multiplicity=Multiplicity(0, 1))
    }
)
ownedParameter204: BinaryAssociation = BinaryAssociation(
    name="ownedParameter204",
    ends={
        Property(name="aadl2_Parameter", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType205", type=aadl2_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess206: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess206",
    ends={
        Property(name="aadl2_SubprogramAccess", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType207", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess208: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess208",
    ends={
        Property(name="aadl2_SubprogramGroupAccess", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType209", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAbstractFeature210: BinaryAssociation = BinaryAssociation(
    name="ownedAbstractFeature210",
    ends={
        Property(name="aadl2_AbstractFeature212", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupType211", type=aadl2_AbstractFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataClassifier223: BinaryAssociation = BinaryAssociation(
    name="dataClassifier223",
    ends={
        Property(name="aadl2_DataClassifier225", type=aadl2_EventDataPort, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_EventDataPort224", type=aadl2_DataClassifier, multiplicity=Multiplicity(0, 1))
    }
)
dataClassifier226: BinaryAssociation = BinaryAssociation(
    name="dataClassifier226",
    ends={
        Property(name="aadl2_DataClassifier228", type=aadl2_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Parameter227", type=aadl2_DataClassifier, multiplicity=Multiplicity(0, 1))
    }
)
subprogramClassifier229: BinaryAssociation = BinaryAssociation(
    name="subprogramClassifier229",
    ends={
        Property(name="aadl2_SubprogramClassifier", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramAccess230", type=aadl2_SubprogramClassifier, multiplicity=Multiplicity(0, 1))
    }
)
dataClassifier218: BinaryAssociation = BinaryAssociation(
    name="dataClassifier218",
    ends={
        Property(name="aadl2_DataClassifier", type=aadl2_DataAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DataAccess219", type=aadl2_DataClassifier, multiplicity=Multiplicity(0, 1))
    }
)
dataClassifier220: BinaryAssociation = BinaryAssociation(
    name="dataClassifier220",
    ends={
        Property(name="aadl2_DataClassifier222", type=aadl2_DataPort, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DataPort221", type=aadl2_DataClassifier, multiplicity=Multiplicity(0, 1))
    }
)
prototype242: BinaryAssociation = BinaryAssociation(
    name="prototype242",
    ends={
        Property(name="aadl2_ComponentPrototype", type=aadl2_Subcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Subcomponent243", type=aadl2_ComponentPrototype, multiplicity=Multiplicity(0, 1))
    }
)
modeBinding244: BinaryAssociation = BinaryAssociation(
    name="modeBinding244",
    ends={
        Property(name="aadl2_ModeBinding", type=aadl2_Subcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Subcomponent245", type=aadl2_ModeBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implementationReference246: BinaryAssociation = BinaryAssociation(
    name="implementationReference246",
    ends={
        Property(name="aadl2_ComponentImplementationReference248", type=aadl2_Subcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Subcomponent247", type=aadl2_ComponentImplementationReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refined250: BinaryAssociation = BinaryAssociation(
    name="refined250",
    ends={
        Property(name="aadl2_Subcomponent251", type=aadl2_Subcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Subcomponent249", type=aadl2_Subcomponent, multiplicity=Multiplicity(0, 1))
    }
)
abstractClassifier252: BinaryAssociation = BinaryAssociation(
    name="abstractClassifier252",
    ends={
        Property(name="aadl2_AbstractClassifier", type=aadl2_Subcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Subcomponent253", type=aadl2_AbstractClassifier, multiplicity=Multiplicity(0, 1))
    }
)
subprogramGroupClassifier231: BinaryAssociation = BinaryAssociation(
    name="subprogramGroupClassifier231",
    ends={
        Property(name="aadl2_SubprogramGroupClassifier", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramGroupAccess232", type=aadl2_SubprogramGroupClassifier, multiplicity=Multiplicity(0, 1))
    }
)
componentClassifier233: BinaryAssociation = BinaryAssociation(
    name="componentClassifier233",
    ends={
        Property(name="aadl2_ComponentClassifier235", type=aadl2_AbstractFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractFeature234", type=aadl2_ComponentClassifier, multiplicity=Multiplicity(0, 1))
    }
)
classifier236: BinaryAssociation = BinaryAssociation(
    name="classifier236",
    ends={
        Property(name="aadl2_ComponentClassifier238", type=aadl2_Subcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Subcomponent237", type=aadl2_ComponentClassifier, multiplicity=Multiplicity(0, 1))
    }
)
ownedPrototypeBinding239: BinaryAssociation = BinaryAssociation(
    name="ownedPrototypeBinding239",
    ends={
        Property(name="aadl2_PrototypeBinding241", type=aadl2_Subcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Subcomponent240", type=aadl2_PrototypeBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specification263: BinaryAssociation = BinaryAssociation(
    name="specification263",
    ends={
        Property(name="aadl2_FlowSpecification265", type=aadl2_FlowImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FlowImplementation264", type=aadl2_FlowSpecification, multiplicity=Multiplicity(1, 1))
    }
)
flowElement266: BinaryAssociation = BinaryAssociation(
    name="flowElement266",
    ends={
        Property(name="aadl2_FlowElement", type=aadl2_FlowImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FlowImplementation267", type=aadl2_FlowElement, multiplicity=Multiplicity(0, 9999))
    }
)
constrainingClassifier254: BinaryAssociation = BinaryAssociation(
    name="constrainingClassifier254",
    ends={
        Property(name="aadl2_ComponentClassifier256", type=aadl2_ComponentPrototype, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentPrototype255", type=aadl2_ComponentClassifier, multiplicity=Multiplicity(0, 1))
    }
)
parentMode257: BinaryAssociation = BinaryAssociation(
    name="parentMode257",
    ends={
        Property(name="aadl2_Mode259", type=aadl2_ModeBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ModeBinding258", type=aadl2_Mode, multiplicity=Multiplicity(1, 1))
    }
)
derivedMode260: BinaryAssociation = BinaryAssociation(
    name="derivedMode260",
    ends={
        Property(name="aadl2_Mode262", type=aadl2_ModeBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ModeBinding261", type=aadl2_Mode, multiplicity=Multiplicity(1, 1))
    }
)
sourceContext289: BinaryAssociation = BinaryAssociation(
    name="sourceContext289",
    ends={
        Property(name="aadl2_Context291", type=aadl2_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Connection290", type=aadl2_Context, multiplicity=Multiplicity(0, 1))
    }
)
refined293: BinaryAssociation = BinaryAssociation(
    name="refined293",
    ends={
        Property(name="aadl2_Connection294", type=aadl2_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Connection292", type=aadl2_Connection, multiplicity=Multiplicity(0, 1))
    }
)
extended295: BinaryAssociation = BinaryAssociation(
    name="extended295",
    ends={
        Property(name="aadl2_ComponentImplementation297", type=aadl2_ImplementationExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ImplementationExtension296", type=aadl2_ComponentImplementation, multiplicity=Multiplicity(1, 1))
    }
)
ownedSubcomponentFlow268: BinaryAssociation = BinaryAssociation(
    name="ownedSubcomponentFlow268",
    ends={
        Property(name="aadl2_SubcomponentFlow", type=aadl2_FlowImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FlowImplementation269", type=aadl2_SubcomponentFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implemented298: BinaryAssociation = BinaryAssociation(
    name="implemented298",
    ends={
        Property(name="aadl2_ComponentType300", type=aadl2_Realization, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Realization299", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1))
    }
)
inTransition270: BinaryAssociation = BinaryAssociation(
    name="inTransition270",
    ends={
        Property(name="aadl2_ModeTransition271", type=aadl2_ModalPath, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ModalPath", type=aadl2_ModeTransition, multiplicity=Multiplicity(0, 9999))
    }
)
context272: BinaryAssociation = BinaryAssociation(
    name="context272",
    ends={
        Property(name="aadl2_Subcomponent274", type=aadl2_SubcomponentFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubcomponentFlow273", type=aadl2_Subcomponent, multiplicity=Multiplicity(1, 1))
    }
)
flowSpecification275: BinaryAssociation = BinaryAssociation(
    name="flowSpecification275",
    ends={
        Property(name="aadl2_FlowSpecification277", type=aadl2_SubcomponentFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubcomponentFlow276", type=aadl2_FlowSpecification, multiplicity=Multiplicity(0, 1))
    }
)
dataAccess278: BinaryAssociation = BinaryAssociation(
    name="dataAccess278",
    ends={
        Property(name="aadl2_DataAccess280", type=aadl2_SubcomponentFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubcomponentFlow279", type=aadl2_DataAccess, multiplicity=Multiplicity(0, 1))
    }
)
destination281: BinaryAssociation = BinaryAssociation(
    name="destination281",
    ends={
        Property(name="aadl2_ConnectionEnd", type=aadl2_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Connection282", type=aadl2_ConnectionEnd, multiplicity=Multiplicity(1, 1))
    }
)
source283: BinaryAssociation = BinaryAssociation(
    name="source283",
    ends={
        Property(name="aadl2_ConnectionEnd285", type=aadl2_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Connection284", type=aadl2_ConnectionEnd, multiplicity=Multiplicity(1, 1))
    }
)
destinationContext286: BinaryAssociation = BinaryAssociation(
    name="destinationContext286",
    ends={
        Property(name="aadl2_Context288", type=aadl2_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Connection287", type=aadl2_Context, multiplicity=Multiplicity(0, 1))
    }
)
refined302: BinaryAssociation = BinaryAssociation(
    name="refined302",
    ends={
        Property(name="aadl2_EndToEndFlow303", type=aadl2_EndToEndFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_EndToEndFlow301", type=aadl2_EndToEndFlow, multiplicity=Multiplicity(0, 1))
    }
)
flowElement304: BinaryAssociation = BinaryAssociation(
    name="flowElement304",
    ends={
        Property(name="aadl2_EndToEndFlowElement", type=aadl2_EndToEndFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_EndToEndFlow305", type=aadl2_EndToEndFlowElement, multiplicity=Multiplicity(1, 9999))
    }
)
ownedSubcomponentFlow306: BinaryAssociation = BinaryAssociation(
    name="ownedSubcomponentFlow306",
    ends={
        Property(name="aadl2_SubcomponentFlow308", type=aadl2_EndToEndFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_EndToEndFlow307", type=aadl2_SubcomponentFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPackageRename310: BinaryAssociation = BinaryAssociation(
    name="ownedPackageRename310",
    ends={
        Property(name="aadl2_PackageRename", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection", type=aadl2_PackageRename, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedComponentTypeRename311: BinaryAssociation = BinaryAssociation(
    name="ownedComponentTypeRename311",
    ends={
        Property(name="aadl2_ComponentTypeRename", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection312", type=aadl2_ComponentTypeRename, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedClassifier313: BinaryAssociation = BinaryAssociation(
    name="ownedClassifier313",
    ends={
        Property(name="aadl2_Classifier315", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection314", type=aadl2_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
privateSection309: BinaryAssociation = BinaryAssociation(
    name="privateSection309",
    ends={
        Property(name="PrivatePackageSection", type=aadl2_PublicPackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="publicSection", type=aadl2_PrivatePackageSection, multiplicity=Multiplicity(0, 1))
    }
)
ownedBusType326: BinaryAssociation = BinaryAssociation(
    name="ownedBusType326",
    ends={
        Property(name="aadl2_BusType", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection327", type=aadl2_BusType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusImplementation328: BinaryAssociation = BinaryAssociation(
    name="ownedBusImplementation328",
    ends={
        Property(name="aadl2_BusImplementation", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection329", type=aadl2_BusImplementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataType330: BinaryAssociation = BinaryAssociation(
    name="ownedDataType330",
    ends={
        Property(name="aadl2_DataType", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection331", type=aadl2_DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataImplementation332: BinaryAssociation = BinaryAssociation(
    name="ownedDataImplementation332",
    ends={
        Property(name="aadl2_DataImplementation", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection333", type=aadl2_DataImplementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDeviceType334: BinaryAssociation = BinaryAssociation(
    name="ownedDeviceType334",
    ends={
        Property(name="aadl2_DeviceType", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection335", type=aadl2_DeviceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedFeatureGroupTypeRename316: BinaryAssociation = BinaryAssociation(
    name="ownedFeatureGroupTypeRename316",
    ends={
        Property(name="aadl2_FeatureGroupTypeRename", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection317", type=aadl2_FeatureGroupTypeRename, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAnnexLibrary318: BinaryAssociation = BinaryAssociation(
    name="ownedAnnexLibrary318",
    ends={
        Property(name="aadl2_AnnexLibrary", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection319", type=aadl2_AnnexLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedPackage320: BinaryAssociation = BinaryAssociation(
    name="importedPackage320",
    ends={
        Property(name="aadl2_AadlPackage", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection321", type=aadl2_AadlPackage, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAbstractType322: BinaryAssociation = BinaryAssociation(
    name="ownedAbstractType322",
    ends={
        Property(name="aadl2_AbstractType", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection323", type=aadl2_AbstractType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAbstractImplementation324: BinaryAssociation = BinaryAssociation(
    name="ownedAbstractImplementation324",
    ends={
        Property(name="aadl2_AbstractImplementation", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection325", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProcessorType344: BinaryAssociation = BinaryAssociation(
    name="ownedProcessorType344",
    ends={
        Property(name="aadl2_ProcessorType", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection345", type=aadl2_ProcessorType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProcessImplementation346: BinaryAssociation = BinaryAssociation(
    name="ownedProcessImplementation346",
    ends={
        Property(name="aadl2_ProcessImplementation", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection347", type=aadl2_ProcessImplementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProcessorImplementation348: BinaryAssociation = BinaryAssociation(
    name="ownedProcessorImplementation348",
    ends={
        Property(name="aadl2_ProcessorImplementation", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection349", type=aadl2_ProcessorImplementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDeviceImplementation336: BinaryAssociation = BinaryAssociation(
    name="ownedDeviceImplementation336",
    ends={
        Property(name="aadl2_DeviceImplementation", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection337", type=aadl2_DeviceImplementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedMemoryType338: BinaryAssociation = BinaryAssociation(
    name="ownedMemoryType338",
    ends={
        Property(name="aadl2_MemoryType", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection339", type=aadl2_MemoryType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedMemoryImplementation340: BinaryAssociation = BinaryAssociation(
    name="ownedMemoryImplementation340",
    ends={
        Property(name="aadl2_MemoryImplementation", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection341", type=aadl2_MemoryImplementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSystemImplementation360: BinaryAssociation = BinaryAssociation(
    name="ownedSystemImplementation360",
    ends={
        Property(name="aadl2_SystemImplementation", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection361", type=aadl2_SystemImplementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProcessType342: BinaryAssociation = BinaryAssociation(
    name="ownedProcessType342",
    ends={
        Property(name="aadl2_ProcessType", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection343", type=aadl2_ProcessType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedThreadType362: BinaryAssociation = BinaryAssociation(
    name="ownedThreadType362",
    ends={
        Property(name="aadl2_ThreadType", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection363", type=aadl2_ThreadType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedThreadImplementation364: BinaryAssociation = BinaryAssociation(
    name="ownedThreadImplementation364",
    ends={
        Property(name="aadl2_ThreadImplementation", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection365", type=aadl2_ThreadImplementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedThreadGroupType366: BinaryAssociation = BinaryAssociation(
    name="ownedThreadGroupType366",
    ends={
        Property(name="aadl2_ThreadGroupType", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection367", type=aadl2_ThreadGroupType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramType350: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramType350",
    ends={
        Property(name="aadl2_SubprogramType", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection351", type=aadl2_SubprogramType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramImplementation352: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramImplementation352",
    ends={
        Property(name="aadl2_SubprogramImplementation", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection353", type=aadl2_SubprogramImplementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedThreadGroupImplementation368: BinaryAssociation = BinaryAssociation(
    name="ownedThreadGroupImplementation368",
    ends={
        Property(name="aadl2_ThreadGroupImplementation", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection369", type=aadl2_ThreadGroupImplementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupType354: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupType354",
    ends={
        Property(name="aadl2_SubprogramGroupType", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection355", type=aadl2_SubprogramGroupType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupImplementation356: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupImplementation356",
    ends={
        Property(name="aadl2_SubprogramGroupImplementation", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection357", type=aadl2_SubprogramGroupImplementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSystemType358: BinaryAssociation = BinaryAssociation(
    name="ownedSystemType358",
    ends={
        Property(name="aadl2_SystemType", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection359", type=aadl2_SystemType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualProcessorImplementation376: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualProcessorImplementation376",
    ends={
        Property(name="aadl2_VirtualProcessorImplementation", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection377", type=aadl2_VirtualProcessorImplementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedFeatureGroupType378: BinaryAssociation = BinaryAssociation(
    name="ownedFeatureGroupType378",
    ends={
        Property(name="aadl2_FeatureGroupType380", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection379", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedPropertySet381: BinaryAssociation = BinaryAssociation(
    name="importedPropertySet381",
    ends={
        Property(name="aadl2_PropertySet", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection382", type=aadl2_PropertySet, multiplicity=Multiplicity(0, 9999))
    }
)
ownedVirtualBusType370: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualBusType370",
    ends={
        Property(name="aadl2_VirtualBusType", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection371", type=aadl2_VirtualBusType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualBusImplementation372: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualBusImplementation372",
    ends={
        Property(name="aadl2_VirtualBusImplementation", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection373", type=aadl2_VirtualBusImplementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualProcessorType374: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualProcessorType374",
    ends={
        Property(name="aadl2_VirtualProcessorType", type=aadl2_PackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageSection375", type=aadl2_VirtualProcessorType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
renamedComponentType397: BinaryAssociation = BinaryAssociation(
    name="renamedComponentType397",
    ends={
        Property(name="aadl2_ComponentType399", type=aadl2_ComponentTypeRename, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentTypeRename398", type=aadl2_ComponentType, multiplicity=Multiplicity(1, 1))
    }
)
renamedFeatureGroupType400: BinaryAssociation = BinaryAssociation(
    name="renamedFeatureGroupType400",
    ends={
        Property(name="aadl2_FeatureGroupType402", type=aadl2_FeatureGroupTypeRename, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupTypeRename401", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1))
    }
)
ownedBusAccess403: BinaryAssociation = BinaryAssociation(
    name="ownedBusAccess403",
    ends={
        Property(name="aadl2_BusAccess405", type=aadl2_AbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractType404", type=aadl2_BusAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
renamedPackage383: BinaryAssociation = BinaryAssociation(
    name="renamedPackage383",
    ends={
        Property(name="aadl2_AadlPackage385", type=aadl2_PackageRename, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PackageRename384", type=aadl2_AadlPackage, multiplicity=Multiplicity(1, 1))
    }
)
ownedPublicSection386: BinaryAssociation = BinaryAssociation(
    name="ownedPublicSection386",
    ends={
        Property(name="aadl2_PublicPackageSection", type=aadl2_AadlPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AadlPackage387", type=aadl2_PublicPackageSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedPrivateSection388: BinaryAssociation = BinaryAssociation(
    name="ownedPrivateSection388",
    ends={
        Property(name="aadl2_PrivatePackageSection", type=aadl2_AadlPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AadlPackage389", type=aadl2_PrivatePackageSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
publicSection390: BinaryAssociation = BinaryAssociation(
    name="publicSection390",
    ends={
        Property(name="aadl2_PublicPackageSection392", type=aadl2_AadlPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AadlPackage391", type=aadl2_PublicPackageSection, multiplicity=Multiplicity(0, 1))
    }
)
privateSection393: BinaryAssociation = BinaryAssociation(
    name="privateSection393",
    ends={
        Property(name="aadl2_PrivatePackageSection395", type=aadl2_AadlPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AadlPackage394", type=aadl2_PrivatePackageSection, multiplicity=Multiplicity(0, 1))
    }
)
publicSection396: BinaryAssociation = BinaryAssociation(
    name="publicSection396",
    ends={
        Property(name="PublicPackageSection", type=aadl2_PrivatePackageSection, multiplicity=Multiplicity(1, 1)),
        Property(name="privateSection", type=aadl2_PublicPackageSection, multiplicity=Multiplicity(0, 1))
    }
)
ownedBusSubcomponent424: BinaryAssociation = BinaryAssociation(
    name="ownedBusSubcomponent424",
    ends={
        Property(name="aadl2_BusSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation425", type=aadl2_BusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataAccess406: BinaryAssociation = BinaryAssociation(
    name="ownedDataAccess406",
    ends={
        Property(name="aadl2_DataAccess408", type=aadl2_AbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractType407", type=aadl2_DataAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess409: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess409",
    ends={
        Property(name="aadl2_SubprogramAccess411", type=aadl2_AbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractType410", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataPort412: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort412",
    ends={
        Property(name="aadl2_DataPort414", type=aadl2_AbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractType413", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort415: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort415",
    ends={
        Property(name="aadl2_EventPort417", type=aadl2_AbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractType416", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort418: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort418",
    ends={
        Property(name="aadl2_EventDataPort420", type=aadl2_AbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractType419", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess421: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess421",
    ends={
        Property(name="aadl2_SubprogramGroupAccess423", type=aadl2_AbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractType422", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSystemSubcomponent436: BinaryAssociation = BinaryAssociation(
    name="ownedSystemSubcomponent436",
    ends={
        Property(name="aadl2_SystemSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation437", type=aadl2_SystemSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramSubcomponent438: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramSubcomponent438",
    ends={
        Property(name="aadl2_SubprogramSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation439", type=aadl2_SubprogramSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupSubcomponent440: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupSubcomponent440",
    ends={
        Property(name="aadl2_SubprogramGroupSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation441", type=aadl2_SubprogramGroupSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedThreadSubcomponent442: BinaryAssociation = BinaryAssociation(
    name="ownedThreadSubcomponent442",
    ends={
        Property(name="aadl2_ThreadSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation443", type=aadl2_ThreadSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataSubcomponent426: BinaryAssociation = BinaryAssociation(
    name="ownedDataSubcomponent426",
    ends={
        Property(name="aadl2_DataSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation427", type=aadl2_DataSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedThreadGroupSubcomponent444: BinaryAssociation = BinaryAssociation(
    name="ownedThreadGroupSubcomponent444",
    ends={
        Property(name="aadl2_ThreadGroupSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation445", type=aadl2_ThreadGroupSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDeviceSubcomponent428: BinaryAssociation = BinaryAssociation(
    name="ownedDeviceSubcomponent428",
    ends={
        Property(name="aadl2_DeviceSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation429", type=aadl2_DeviceSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualBusSubcomponent446: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualBusSubcomponent446",
    ends={
        Property(name="aadl2_VirtualBusSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation447", type=aadl2_VirtualBusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedMemorySubcomponent430: BinaryAssociation = BinaryAssociation(
    name="ownedMemorySubcomponent430",
    ends={
        Property(name="aadl2_MemorySubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation431", type=aadl2_MemorySubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProcessSubcomponent432: BinaryAssociation = BinaryAssociation(
    name="ownedProcessSubcomponent432",
    ends={
        Property(name="aadl2_ProcessSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation433", type=aadl2_ProcessSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProcessorSubcomponent434: BinaryAssociation = BinaryAssociation(
    name="ownedProcessorSubcomponent434",
    ends={
        Property(name="aadl2_ProcessorSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation435", type=aadl2_ProcessorSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callSpecification450: BinaryAssociation = BinaryAssociation(
    name="callSpecification450",
    ends={
        Property(name="aadl2_CallSpecification", type=aadl2_BehavioredImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BehavioredImplementation", type=aadl2_CallSpecification, multiplicity=Multiplicity(0, 9999))
    }
)
ownedSubprogramCallSequence451: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramCallSequence451",
    ends={
        Property(name="aadl2_SubprogramCallSequence", type=aadl2_BehavioredImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BehavioredImplementation452", type=aadl2_SubprogramCallSequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedCallSpecification453: BinaryAssociation = BinaryAssociation(
    name="ownedCallSpecification453",
    ends={
        Property(name="aadl2_CallSpecification455", type=aadl2_SubprogramCallSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramCallSequence454", type=aadl2_CallSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
busClassifier456: BinaryAssociation = BinaryAssociation(
    name="busClassifier456",
    ends={
        Property(name="aadl2_BusClassifier458", type=aadl2_BusSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BusSubcomponent457", type=aadl2_BusClassifier, multiplicity=Multiplicity(0, 1))
    }
)
dataClassifier459: BinaryAssociation = BinaryAssociation(
    name="dataClassifier459",
    ends={
        Property(name="aadl2_DataClassifier461", type=aadl2_DataSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DataSubcomponent460", type=aadl2_DataClassifier, multiplicity=Multiplicity(0, 1))
    }
)
deviceClassifier462: BinaryAssociation = BinaryAssociation(
    name="deviceClassifier462",
    ends={
        Property(name="aadl2_DeviceClassifier", type=aadl2_DeviceSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DeviceSubcomponent463", type=aadl2_DeviceClassifier, multiplicity=Multiplicity(0, 1))
    }
)
ownedVirtualProcessorSubcomponent448: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualProcessorSubcomponent448",
    ends={
        Property(name="aadl2_VirtualProcessorSubcomponent", type=aadl2_AbstractImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AbstractImplementation449", type=aadl2_VirtualProcessorSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memoryClassifier464: BinaryAssociation = BinaryAssociation(
    name="memoryClassifier464",
    ends={
        Property(name="aadl2_MemoryClassifier", type=aadl2_MemorySubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_MemorySubcomponent465", type=aadl2_MemoryClassifier, multiplicity=Multiplicity(0, 1))
    }
)
processorClassifier468: BinaryAssociation = BinaryAssociation(
    name="processorClassifier468",
    ends={
        Property(name="aadl2_ProcessorClassifier", type=aadl2_ProcessorSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorSubcomponent469", type=aadl2_ProcessorClassifier, multiplicity=Multiplicity(0, 1))
    }
)
systemClassifier470: BinaryAssociation = BinaryAssociation(
    name="systemClassifier470",
    ends={
        Property(name="aadl2_SystemClassifier", type=aadl2_SystemSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemSubcomponent471", type=aadl2_SystemClassifier, multiplicity=Multiplicity(0, 1))
    }
)
subprogramClassifier472: BinaryAssociation = BinaryAssociation(
    name="subprogramClassifier472",
    ends={
        Property(name="aadl2_SubprogramClassifier474", type=aadl2_SubprogramSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramSubcomponent473", type=aadl2_SubprogramClassifier, multiplicity=Multiplicity(0, 1))
    }
)
subprogramGroupClassifier475: BinaryAssociation = BinaryAssociation(
    name="subprogramGroupClassifier475",
    ends={
        Property(name="aadl2_SubprogramGroupClassifier477", type=aadl2_SubprogramGroupSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramGroupSubcomponent476", type=aadl2_SubprogramGroupClassifier, multiplicity=Multiplicity(0, 1))
    }
)
threadClassifier478: BinaryAssociation = BinaryAssociation(
    name="threadClassifier478",
    ends={
        Property(name="aadl2_ThreadClassifier", type=aadl2_ThreadSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadSubcomponent479", type=aadl2_ThreadClassifier, multiplicity=Multiplicity(0, 1))
    }
)
processClassifier466: BinaryAssociation = BinaryAssociation(
    name="processClassifier466",
    ends={
        Property(name="aadl2_ProcessClassifier", type=aadl2_ProcessSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessSubcomponent467", type=aadl2_ProcessClassifier, multiplicity=Multiplicity(0, 1))
    }
)
virtualBusClassifier482: BinaryAssociation = BinaryAssociation(
    name="virtualBusClassifier482",
    ends={
        Property(name="aadl2_VirtualBusClassifier", type=aadl2_VirtualBusSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualBusSubcomponent483", type=aadl2_VirtualBusClassifier, multiplicity=Multiplicity(0, 1))
    }
)
virtualProcessorClassifier484: BinaryAssociation = BinaryAssociation(
    name="virtualProcessorClassifier484",
    ends={
        Property(name="aadl2_VirtualProcessorClassifier", type=aadl2_VirtualProcessorSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualProcessorSubcomponent485", type=aadl2_VirtualProcessorClassifier, multiplicity=Multiplicity(0, 1))
    }
)
ownedBusAccess486: BinaryAssociation = BinaryAssociation(
    name="ownedBusAccess486",
    ends={
        Property(name="aadl2_BusAccess488", type=aadl2_BusType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BusType487", type=aadl2_BusAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualBusSubcomponent489: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualBusSubcomponent489",
    ends={
        Property(name="aadl2_VirtualBusSubcomponent491", type=aadl2_BusImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BusImplementation490", type=aadl2_VirtualBusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
threadGroupClassifier480: BinaryAssociation = BinaryAssociation(
    name="threadGroupClassifier480",
    ends={
        Property(name="aadl2_ThreadGroupClassifier", type=aadl2_ThreadGroupSubcomponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupSubcomponent481", type=aadl2_ThreadGroupClassifier, multiplicity=Multiplicity(0, 1))
    }
)
ownedSubprogramGroupAccess495: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess495",
    ends={
        Property(name="aadl2_SubprogramGroupAccess497", type=aadl2_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DataType496", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataSubcomponent498: BinaryAssociation = BinaryAssociation(
    name="ownedDataSubcomponent498",
    ends={
        Property(name="aadl2_DataSubcomponent500", type=aadl2_DataImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DataImplementation499", type=aadl2_DataSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
        Property(name="aadl2_DataPort506", type=aadl2_DeviceType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DeviceType505", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort507: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort507",
    ends={
        Property(name="aadl2_EventDataPort509", type=aadl2_DeviceType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DeviceType508", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort510: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort510",
    ends={
        Property(name="aadl2_EventPort512", type=aadl2_DeviceType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DeviceType511", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess516: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess516",
    ends={
        Property(name="aadl2_SubprogramAccess518", type=aadl2_DeviceType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DeviceType517", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataPort537: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort537",
    ends={
        Property(name="aadl2_DataPort539", type=aadl2_ProcessType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessType538", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess492: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess492",
    ends={
        Property(name="aadl2_SubprogramAccess494", type=aadl2_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DataType493", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess519: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess519",
    ends={
        Property(name="aadl2_SubprogramGroupAccess521", type=aadl2_DeviceType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DeviceType520", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusSubcomponent522: BinaryAssociation = BinaryAssociation(
    name="ownedBusSubcomponent522",
    ends={
        Property(name="aadl2_BusSubcomponent524", type=aadl2_DeviceImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DeviceImplementation523", type=aadl2_BusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataSubcomponent525: BinaryAssociation = BinaryAssociation(
    name="ownedDataSubcomponent525",
    ends={
        Property(name="aadl2_DataSubcomponent527", type=aadl2_DeviceImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DeviceImplementation526", type=aadl2_DataSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusAccess528: BinaryAssociation = BinaryAssociation(
    name="ownedBusAccess528",
    ends={
        Property(name="aadl2_BusAccess530", type=aadl2_MemoryType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_MemoryType529", type=aadl2_BusAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusSubcomponent531: BinaryAssociation = BinaryAssociation(
    name="ownedBusSubcomponent531",
    ends={
        Property(name="aadl2_BusSubcomponent533", type=aadl2_MemoryImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_MemoryImplementation532", type=aadl2_BusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedMemorySubcomponent534: BinaryAssociation = BinaryAssociation(
    name="ownedMemorySubcomponent534",
    ends={
        Property(name="aadl2_MemorySubcomponent536", type=aadl2_MemoryImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_MemoryImplementation535", type=aadl2_MemorySubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusAccess513: BinaryAssociation = BinaryAssociation(
    name="ownedBusAccess513",
    ends={
        Property(name="aadl2_BusAccess515", type=aadl2_DeviceType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_DeviceType514", type=aadl2_BusAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusAccess564: BinaryAssociation = BinaryAssociation(
    name="ownedBusAccess564",
    ends={
        Property(name="aadl2_BusAccess566", type=aadl2_ProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorType565", type=aadl2_BusAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort540: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort540",
    ends={
        Property(name="aadl2_EventDataPort542", type=aadl2_ProcessType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessType541", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort543: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort543",
    ends={
        Property(name="aadl2_EventPort545", type=aadl2_ProcessType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessType544", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataAccess546: BinaryAssociation = BinaryAssociation(
    name="ownedDataAccess546",
    ends={
        Property(name="aadl2_DataAccess548", type=aadl2_ProcessType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessType547", type=aadl2_DataAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess549: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess549",
    ends={
        Property(name="aadl2_SubprogramAccess551", type=aadl2_ProcessType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessType550", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess552: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess552",
    ends={
        Property(name="aadl2_SubprogramGroupAccess554", type=aadl2_ProcessType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessType553", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataPort555: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort555",
    ends={
        Property(name="aadl2_DataPort557", type=aadl2_ProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorType556", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort558: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort558",
    ends={
        Property(name="aadl2_EventDataPort560", type=aadl2_ProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorType559", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort561: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort561",
    ends={
        Property(name="aadl2_EventPort563", type=aadl2_ProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorType562", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupSubcomponent579: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupSubcomponent579",
    ends={
        Property(name="aadl2_SubprogramGroupSubcomponent581", type=aadl2_ProcessImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessImplementation580", type=aadl2_SubprogramGroupSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess567: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess567",
    ends={
        Property(name="aadl2_SubprogramAccess569", type=aadl2_ProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorType568", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess570: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess570",
    ends={
        Property(name="aadl2_SubprogramGroupAccess572", type=aadl2_ProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorType571", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataSubcomponent573: BinaryAssociation = BinaryAssociation(
    name="ownedDataSubcomponent573",
    ends={
        Property(name="aadl2_DataSubcomponent575", type=aadl2_ProcessImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessImplementation574", type=aadl2_DataSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramSubcomponent576: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramSubcomponent576",
    ends={
        Property(name="aadl2_SubprogramSubcomponent578", type=aadl2_ProcessImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessImplementation577", type=aadl2_SubprogramSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort603: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort603",
    ends={
        Property(name="aadl2_EventPort605", type=aadl2_SubprogramType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramType604", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedThreadSubcomponent582: BinaryAssociation = BinaryAssociation(
    name="ownedThreadSubcomponent582",
    ends={
        Property(name="aadl2_ThreadSubcomponent584", type=aadl2_ProcessImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessImplementation583", type=aadl2_ThreadSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedThreadGroupSubcomponent585: BinaryAssociation = BinaryAssociation(
    name="ownedThreadGroupSubcomponent585",
    ends={
        Property(name="aadl2_ThreadGroupSubcomponent587", type=aadl2_ProcessImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessImplementation586", type=aadl2_ThreadGroupSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusSubcomponent588: BinaryAssociation = BinaryAssociation(
    name="ownedBusSubcomponent588",
    ends={
        Property(name="aadl2_BusSubcomponent590", type=aadl2_ProcessorImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorImplementation589", type=aadl2_BusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedMemorySubcomponent591: BinaryAssociation = BinaryAssociation(
    name="ownedMemorySubcomponent591",
    ends={
        Property(name="aadl2_MemorySubcomponent593", type=aadl2_ProcessorImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorImplementation592", type=aadl2_MemorySubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualBusSubcomponent594: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualBusSubcomponent594",
    ends={
        Property(name="aadl2_VirtualBusSubcomponent596", type=aadl2_ProcessorImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorImplementation595", type=aadl2_VirtualBusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualProcessorSubcomponent597: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualProcessorSubcomponent597",
    ends={
        Property(name="aadl2_VirtualProcessorSubcomponent599", type=aadl2_ProcessorImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ProcessorImplementation598", type=aadl2_VirtualProcessorSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort600: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort600",
    ends={
        Property(name="aadl2_EventDataPort602", type=aadl2_SubprogramType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramType601", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedParameter606: BinaryAssociation = BinaryAssociation(
    name="ownedParameter606",
    ends={
        Property(name="aadl2_Parameter608", type=aadl2_SubprogramType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramType607", type=aadl2_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataAccess609: BinaryAssociation = BinaryAssociation(
    name="ownedDataAccess609",
    ends={
        Property(name="aadl2_DataAccess611", type=aadl2_SubprogramType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramType610", type=aadl2_DataAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess612: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess612",
    ends={
        Property(name="aadl2_SubprogramAccess614", type=aadl2_SubprogramType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramType613", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess615: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess615",
    ends={
        Property(name="aadl2_SubprogramGroupAccess617", type=aadl2_SubprogramType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramType616", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataSubcomponent618: BinaryAssociation = BinaryAssociation(
    name="ownedDataSubcomponent618",
    ends={
        Property(name="aadl2_DataSubcomponent620", type=aadl2_SubprogramImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramImplementation619", type=aadl2_DataSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess621: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess621",
    ends={
        Property(name="aadl2_SubprogramAccess623", type=aadl2_SubprogramGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramGroupType622", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess624: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess624",
    ends={
        Property(name="aadl2_SubprogramGroupAccess626", type=aadl2_SubprogramGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramGroupType625", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort651: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort651",
    ends={
        Property(name="aadl2_EventDataPort653", type=aadl2_SystemType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemType652", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramSubcomponent627: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramSubcomponent627",
    ends={
        Property(name="aadl2_SubprogramSubcomponent629", type=aadl2_SubprogramGroupImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramGroupImplementation628", type=aadl2_SubprogramSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupSubcomponent630: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupSubcomponent630",
    ends={
        Property(name="aadl2_SubprogramGroupSubcomponent632", type=aadl2_SubprogramGroupImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramGroupImplementation631", type=aadl2_SubprogramGroupSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusAccess633: BinaryAssociation = BinaryAssociation(
    name="ownedBusAccess633",
    ends={
        Property(name="aadl2_BusAccess635", type=aadl2_SystemType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemType634", type=aadl2_BusAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataAccess636: BinaryAssociation = BinaryAssociation(
    name="ownedDataAccess636",
    ends={
        Property(name="aadl2_DataAccess638", type=aadl2_SystemType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemType637", type=aadl2_DataAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataPort639: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort639",
    ends={
        Property(name="aadl2_DataPort641", type=aadl2_SystemType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemType640", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess642: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess642",
    ends={
        Property(name="aadl2_SubprogramGroupAccess644", type=aadl2_SystemType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemType643", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess645: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess645",
    ends={
        Property(name="aadl2_SubprogramAccess647", type=aadl2_SystemType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemType646", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort648: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort648",
    ends={
        Property(name="aadl2_EventPort650", type=aadl2_SystemType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemType649", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProcessorSubcomponent669: BinaryAssociation = BinaryAssociation(
    name="ownedProcessorSubcomponent669",
    ends={
        Property(name="aadl2_ProcessorSubcomponent671", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation670", type=aadl2_ProcessorSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBusSubcomponent654: BinaryAssociation = BinaryAssociation(
    name="ownedBusSubcomponent654",
    ends={
        Property(name="aadl2_BusSubcomponent656", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation655", type=aadl2_BusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataSubcomponent657: BinaryAssociation = BinaryAssociation(
    name="ownedDataSubcomponent657",
    ends={
        Property(name="aadl2_DataSubcomponent659", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation658", type=aadl2_DataSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDeviceSubcomponent660: BinaryAssociation = BinaryAssociation(
    name="ownedDeviceSubcomponent660",
    ends={
        Property(name="aadl2_DeviceSubcomponent662", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation661", type=aadl2_DeviceSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedMemorySubcomponent663: BinaryAssociation = BinaryAssociation(
    name="ownedMemorySubcomponent663",
    ends={
        Property(name="aadl2_MemorySubcomponent665", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation664", type=aadl2_MemorySubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProcessSubcomponent666: BinaryAssociation = BinaryAssociation(
    name="ownedProcessSubcomponent666",
    ends={
        Property(name="aadl2_ProcessSubcomponent668", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation667", type=aadl2_ProcessSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataPort687: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort687",
    ends={
        Property(name="aadl2_DataPort689", type=aadl2_ThreadType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadType688", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort690: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort690",
    ends={
        Property(name="aadl2_EventDataPort692", type=aadl2_ThreadType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadType691", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramSubcomponent672: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramSubcomponent672",
    ends={
        Property(name="aadl2_SubprogramSubcomponent674", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation673", type=aadl2_SubprogramSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupSubcomponent675: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupSubcomponent675",
    ends={
        Property(name="aadl2_SubprogramGroupSubcomponent677", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation676", type=aadl2_SubprogramGroupSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSystemSubcomponent678: BinaryAssociation = BinaryAssociation(
    name="ownedSystemSubcomponent678",
    ends={
        Property(name="aadl2_SystemSubcomponent680", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation679", type=aadl2_SystemSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualBusSubcomponent681: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualBusSubcomponent681",
    ends={
        Property(name="aadl2_VirtualBusSubcomponent683", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation682", type=aadl2_VirtualBusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualProcessorSubcomponent684: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualProcessorSubcomponent684",
    ends={
        Property(name="aadl2_VirtualProcessorSubcomponent686", type=aadl2_SystemImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SystemImplementation685", type=aadl2_VirtualProcessorSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataSubcomponent711: BinaryAssociation = BinaryAssociation(
    name="ownedDataSubcomponent711",
    ends={
        Property(name="aadl2_DataSubcomponent713", type=aadl2_ThreadImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadImplementation712", type=aadl2_DataSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort693: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort693",
    ends={
        Property(name="aadl2_EventPort695", type=aadl2_ThreadType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadType694", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataAccess696: BinaryAssociation = BinaryAssociation(
    name="ownedDataAccess696",
    ends={
        Property(name="aadl2_DataAccess698", type=aadl2_ThreadType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadType697", type=aadl2_DataAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess699: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess699",
    ends={
        Property(name="aadl2_SubprogramAccess701", type=aadl2_ThreadType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadType700", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess702: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess702",
    ends={
        Property(name="aadl2_SubprogramGroupAccess704", type=aadl2_ThreadType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadType703", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupSubcomponent705: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupSubcomponent705",
    ends={
        Property(name="aadl2_SubprogramGroupSubcomponent707", type=aadl2_ThreadImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadImplementation706", type=aadl2_SubprogramGroupSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramSubcomponent708: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramSubcomponent708",
    ends={
        Property(name="aadl2_SubprogramSubcomponent710", type=aadl2_ThreadImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadImplementation709", type=aadl2_SubprogramSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess726: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess726",
    ends={
        Property(name="aadl2_SubprogramAccess728", type=aadl2_ThreadGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupType727", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataPort714: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort714",
    ends={
        Property(name="aadl2_DataPort716", type=aadl2_ThreadGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupType715", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort717: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort717",
    ends={
        Property(name="aadl2_EventDataPort719", type=aadl2_ThreadGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupType718", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventPort720: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort720",
    ends={
        Property(name="aadl2_EventPort722", type=aadl2_ThreadGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupType721", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataAccess723: BinaryAssociation = BinaryAssociation(
    name="ownedDataAccess723",
    ends={
        Property(name="aadl2_DataAccess725", type=aadl2_ThreadGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupType724", type=aadl2_DataAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupSubcomponent744: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupSubcomponent744",
    ends={
        Property(name="aadl2_SubprogramGroupSubcomponent746", type=aadl2_ThreadGroupImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupImplementation745", type=aadl2_SubprogramGroupSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess729: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess729",
    ends={
        Property(name="aadl2_SubprogramGroupAccess731", type=aadl2_ThreadGroupType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupType730", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataSubcomponent732: BinaryAssociation = BinaryAssociation(
    name="ownedDataSubcomponent732",
    ends={
        Property(name="aadl2_DataSubcomponent734", type=aadl2_ThreadGroupImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ThreadGroupImplementation733", type=aadl2_DataSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
ownedEventPort756: BinaryAssociation = BinaryAssociation(
    name="ownedEventPort756",
    ends={
        Property(name="aadl2_EventPort758", type=aadl2_VirtualProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualProcessorType757", type=aadl2_EventPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramAccess759: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramAccess759",
    ends={
        Property(name="aadl2_SubprogramAccess761", type=aadl2_VirtualProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualProcessorType760", type=aadl2_SubprogramAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualBusSubcomponent747: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualBusSubcomponent747",
    ends={
        Property(name="aadl2_VirtualBusSubcomponent749", type=aadl2_VirtualBusImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualBusImplementation748", type=aadl2_VirtualBusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDataPort750: BinaryAssociation = BinaryAssociation(
    name="ownedDataPort750",
    ends={
        Property(name="aadl2_DataPort752", type=aadl2_VirtualProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualProcessorType751", type=aadl2_DataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDataPort753: BinaryAssociation = BinaryAssociation(
    name="ownedEventDataPort753",
    ends={
        Property(name="aadl2_EventDataPort755", type=aadl2_VirtualProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualProcessorType754", type=aadl2_EventDataPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPropertyType771: BinaryAssociation = BinaryAssociation(
    name="ownedPropertyType771",
    ends={
        Property(name="aadl2_PropertyType773", type=aadl2_PropertySet, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertySet772", type=aadl2_PropertyType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSubprogramGroupAccess762: BinaryAssociation = BinaryAssociation(
    name="ownedSubprogramGroupAccess762",
    ends={
        Property(name="aadl2_SubprogramGroupAccess764", type=aadl2_VirtualProcessorType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualProcessorType763", type=aadl2_SubprogramGroupAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProperty774: BinaryAssociation = BinaryAssociation(
    name="ownedProperty774",
    ends={
        Property(name="aadl2_Property776", type=aadl2_PropertySet, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertySet775", type=aadl2_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPropertyConstant777: BinaryAssociation = BinaryAssociation(
    name="ownedPropertyConstant777",
    ends={
        Property(name="aadl2_PropertyConstant", type=aadl2_PropertySet, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertySet778", type=aadl2_PropertyConstant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualBusSubcomponent765: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualBusSubcomponent765",
    ends={
        Property(name="aadl2_VirtualBusSubcomponent767", type=aadl2_VirtualProcessorImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualProcessorImplementation766", type=aadl2_VirtualBusSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVirtualProcessorSubcomponent768: BinaryAssociation = BinaryAssociation(
    name="ownedVirtualProcessorSubcomponent768",
    ends={
        Property(name="aadl2_VirtualProcessorSubcomponent770", type=aadl2_VirtualProcessorImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_VirtualProcessorImplementation769", type=aadl2_VirtualProcessorSubcomponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedPackage782: BinaryAssociation = BinaryAssociation(
    name="importedPackage782",
    ends={
        Property(name="aadl2_AadlPackage784", type=aadl2_PropertySet, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertySet783", type=aadl2_AadlPackage, multiplicity=Multiplicity(0, 9999))
    }
)
ownedType785: BinaryAssociation = BinaryAssociation(
    name="ownedType785",
    ends={
        Property(name="aadl2_PropertyType787", type=aadl2_PropertyConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertyConstant786", type=aadl2_PropertyType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constantValue788: BinaryAssociation = BinaryAssociation(
    name="constantValue788",
    ends={
        Property(name="aadl2_PropertyExpression790", type=aadl2_PropertyConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertyConstant789", type=aadl2_PropertyExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actual791: BinaryAssociation = BinaryAssociation(
    name="actual791",
    ends={
        Property(name="aadl2_ComponentPrototypeActual", type=aadl2_ComponentPrototypeBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentPrototypeBinding", type=aadl2_ComponentPrototypeActual, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
importedPropertySet780: BinaryAssociation = BinaryAssociation(
    name="importedPropertySet780",
    ends={
        Property(name="aadl2_PropertySet781", type=aadl2_PropertySet, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertySet779", type=aadl2_PropertySet, multiplicity=Multiplicity(0, 9999))
    }
)
constrainingFeatureGroupType792: BinaryAssociation = BinaryAssociation(
    name="constrainingFeatureGroupType792",
    ends={
        Property(name="aadl2_FeatureGroupType793", type=aadl2_FeatureGroupPrototype, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupPrototype", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(0, 1))
    }
)
actual794: BinaryAssociation = BinaryAssociation(
    name="actual794",
    ends={
        Property(name="aadl2_FeatureGroupPrototypeActual", type=aadl2_FeatureGroupPrototypeBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupPrototypeBinding", type=aadl2_FeatureGroupPrototypeActual, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actual797: BinaryAssociation = BinaryAssociation(
    name="actual797",
    ends={
        Property(name="aadl2_FeaturePrototypeActual", type=aadl2_FeaturePrototypeBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeaturePrototypeBinding", type=aadl2_FeaturePrototypeActual, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier798: BinaryAssociation = BinaryAssociation(
    name="classifier798",
    ends={
        Property(name="aadl2_ComponentClassifier799", type=aadl2_AccessSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_AccessSpecification", type=aadl2_ComponentClassifier, multiplicity=Multiplicity(0, 1))
    }
)
constrainingClassifier795: BinaryAssociation = BinaryAssociation(
    name="constrainingClassifier795",
    ends={
        Property(name="aadl2_ComponentClassifier796", type=aadl2_FeaturePrototype, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeaturePrototype", type=aadl2_ComponentClassifier, multiplicity=Multiplicity(0, 1))
    }
)
classifier800: BinaryAssociation = BinaryAssociation(
    name="classifier800",
    ends={
        Property(name="aadl2_ComponentClassifier801", type=aadl2_PortSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PortSpecification", type=aadl2_ComponentClassifier, multiplicity=Multiplicity(0, 1))
    }
)
prototype802: BinaryAssociation = BinaryAssociation(
    name="prototype802",
    ends={
        Property(name="aadl2_FeaturePrototype803", type=aadl2_FeaturePrototypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeaturePrototypeReference", type=aadl2_FeaturePrototype, multiplicity=Multiplicity(1, 1))
    }
)
prototype804: BinaryAssociation = BinaryAssociation(
    name="prototype804",
    ends={
        Property(name="aadl2_ComponentPrototype805", type=aadl2_ComponentPrototypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentPrototypeReference", type=aadl2_ComponentPrototype, multiplicity=Multiplicity(1, 1))
    }
)
classifier808: BinaryAssociation = BinaryAssociation(
    name="classifier808",
    ends={
        Property(name="aadl2_ComponentReference809", type=aadl2_ComponentClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentClassifier810", type=aadl2_ComponentReference, multiplicity=Multiplicity(1, 1))
    }
)
prototype811: BinaryAssociation = BinaryAssociation(
    name="prototype811",
    ends={
        Property(name="aadl2_FeatureGroupPrototype812", type=aadl2_FeatureGroupPrototypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupPrototypeReference", type=aadl2_FeatureGroupPrototype, multiplicity=Multiplicity(1, 1))
    }
)
binding813: BinaryAssociation = BinaryAssociation(
    name="binding813",
    ends={
        Property(name="aadl2_PrototypeBinding814", type=aadl2_FeatureGroupReference, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupReference", type=aadl2_PrototypeBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureGroupType815: BinaryAssociation = BinaryAssociation(
    name="featureGroupType815",
    ends={
        Property(name="aadl2_FeatureGroupType817", type=aadl2_FeatureGroupReference, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_FeatureGroupReference816", type=aadl2_FeatureGroupType, multiplicity=Multiplicity(1, 1))
    }
)
calledSubprogram818: BinaryAssociation = BinaryAssociation(
    name="calledSubprogram818",
    ends={
        Property(name="aadl2_CalledSubprogram", type=aadl2_SubprogramCall, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramCall", type=aadl2_CalledSubprogram, multiplicity=Multiplicity(0, 1))
    }
)
prototype819: BinaryAssociation = BinaryAssociation(
    name="prototype819",
    ends={
        Property(name="aadl2_Prototype821", type=aadl2_SubprogramCall, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramCall820", type=aadl2_Prototype, multiplicity=Multiplicity(0, 1))
    }
)
binding806: BinaryAssociation = BinaryAssociation(
    name="binding806",
    ends={
        Property(name="aadl2_PrototypeBinding807", type=aadl2_ComponentReference, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ComponentReference", type=aadl2_PrototypeBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context822: BinaryAssociation = BinaryAssociation(
    name="context822",
    ends={
        Property(name="aadl2_CallContext", type=aadl2_SubprogramCall, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_SubprogramCall823", type=aadl2_CallContext, multiplicity=Multiplicity(0, 1))
    }
)
unit836: BinaryAssociation = BinaryAssociation(
    name="unit836",
    ends={
        Property(name="aadl2_UnitLiteral838", type=aadl2_NumberValue, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_NumberValue837", type=aadl2_UnitLiteral, multiplicity=Multiplicity(0, 1))
    }
)
property824: BinaryAssociation = BinaryAssociation(
    name="property824",
    ends={
        Property(name="aadl2_BasicProperty825", type=aadl2_BasicPropertyAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BasicPropertyAssociation", type=aadl2_BasicProperty, multiplicity=Multiplicity(1, 1))
    }
)
ownedValue826: BinaryAssociation = BinaryAssociation(
    name="ownedValue826",
    ends={
        Property(name="aadl2_PropertyExpression828", type=aadl2_BasicPropertyAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_BasicPropertyAssociation827", type=aadl2_PropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
literal829: BinaryAssociation = BinaryAssociation(
    name="literal829",
    ends={
        Property(name="aadl2_EnumerationLiteral", type=aadl2_EnumerationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_EnumerationValue", type=aadl2_EnumerationLiteral, multiplicity=Multiplicity(1, 1))
    }
)
literal830: BinaryAssociation = BinaryAssociation(
    name="literal830",
    ends={
        Property(name="aadl2_UnitLiteral", type=aadl2_UnitValue, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_UnitValue", type=aadl2_UnitLiteral, multiplicity=Multiplicity(1, 1))
    }
)
baseUnit832: BinaryAssociation = BinaryAssociation(
    name="baseUnit832",
    ends={
        Property(name="aadl2_UnitLiteral833", type=aadl2_UnitLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_UnitLiteral831", type=aadl2_UnitLiteral, multiplicity=Multiplicity(0, 1))
    }
)
factor834: BinaryAssociation = BinaryAssociation(
    name="factor834",
    ends={
        Property(name="aadl2_NumberValue", type=aadl2_UnitLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_UnitLiteral835", type=aadl2_NumberValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classifier839: BinaryAssociation = BinaryAssociation(
    name="classifier839",
    ends={
        Property(name="aadl2_Classifier840", type=aadl2_ClassifierValue, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ClassifierValue", type=aadl2_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
minimum841: BinaryAssociation = BinaryAssociation(
    name="minimum841",
    ends={
        Property(name="aadl2_PropertyExpression842", type=aadl2_RangeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_RangeValue", type=aadl2_PropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
maximum843: BinaryAssociation = BinaryAssociation(
    name="maximum843",
    ends={
        Property(name="aadl2_PropertyExpression845", type=aadl2_RangeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_RangeValue844", type=aadl2_PropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
delta846: BinaryAssociation = BinaryAssociation(
    name="delta846",
    ends={
        Property(name="aadl2_PropertyExpression848", type=aadl2_RangeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_RangeValue847", type=aadl2_PropertyExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant849: BinaryAssociation = BinaryAssociation(
    name="constant849",
    ends={
        Property(name="aadl2_PropertyConstant850", type=aadl2_ConstantValue, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ConstantValue", type=aadl2_PropertyConstant, multiplicity=Multiplicity(1, 1))
    }
)
property851: BinaryAssociation = BinaryAssociation(
    name="property851",
    ends={
        Property(name="aadl2_Property852", type=aadl2_PropertyReference, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_PropertyReference", type=aadl2_Property, multiplicity=Multiplicity(1, 1))
    }
)
ownedPropertyExpression853: BinaryAssociation = BinaryAssociation(
    name="ownedPropertyExpression853",
    ends={
        Property(name="aadl2_PropertyExpression854", type=aadl2_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_Operation", type=aadl2_PropertyExpression, multiplicity=Multiplicity(1, 2), is_composite=True)
    }
)
ownedFieldValue855: BinaryAssociation = BinaryAssociation(
    name="ownedFieldValue855",
    ends={
        Property(name="aadl2_BasicPropertyAssociation856", type=aadl2_RecordValue, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_RecordValue", type=aadl2_BasicPropertyAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedUnitsType864: BinaryAssociation = BinaryAssociation(
    name="ownedUnitsType864",
    ends={
        Property(name="aadl2_UnitsType", type=aadl2_NumberType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_NumberType", type=aadl2_UnitsType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedListElement857: BinaryAssociation = BinaryAssociation(
    name="ownedListElement857",
    ends={
        Property(name="aadl2_PropertyExpression858", type=aadl2_ListValue, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ListValue", type=aadl2_PropertyExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package859: BinaryAssociation = BinaryAssociation(
    name="package859",
    ends={
        Property(name="aadl2_PublicPackageSection860", type=aadl2_GlobalNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_GlobalNamespace", type=aadl2_PublicPackageSection, multiplicity=Multiplicity(0, 9999))
    }
)
propertySet861: BinaryAssociation = BinaryAssociation(
    name="propertySet861",
    ends={
        Property(name="aadl2_PropertySet863", type=aadl2_GlobalNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_GlobalNamespace862", type=aadl2_PropertySet, multiplicity=Multiplicity(0, 9999))
    }
)
lowerBound875: BinaryAssociation = BinaryAssociation(
    name="lowerBound875",
    ends={
        Property(name="aadl2_PropertyExpression877", type=aadl2_NumericRange, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_NumericRange876", type=aadl2_PropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
unitsType865: BinaryAssociation = BinaryAssociation(
    name="unitsType865",
    ends={
        Property(name="aadl2_UnitsType867", type=aadl2_NumberType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_NumberType866", type=aadl2_UnitsType, multiplicity=Multiplicity(0, 1))
    }
)
range868: BinaryAssociation = BinaryAssociation(
    name="range868",
    ends={
        Property(name="aadl2_NumericRange", type=aadl2_NumberType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_NumberType869", type=aadl2_NumericRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedLiteral870: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral870",
    ends={
        Property(name="aadl2_EnumerationLiteral871", type=aadl2_EnumerationType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_EnumerationType", type=aadl2_EnumerationLiteral, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
upperBound872: BinaryAssociation = BinaryAssociation(
    name="upperBound872",
    ends={
        Property(name="aadl2_PropertyExpression874", type=aadl2_NumericRange, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_NumericRange873", type=aadl2_PropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
namedElementReference887: BinaryAssociation = BinaryAssociation(
    name="namedElementReference887",
    ends={
        Property(name="aadl2_MetaclassReference888", type=aadl2_ReferenceType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ReferenceType", type=aadl2_MetaclassReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
classifierReference878: BinaryAssociation = BinaryAssociation(
    name="classifierReference878",
    ends={
        Property(name="aadl2_MetaclassReference879", type=aadl2_ClassifierType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_ClassifierType", type=aadl2_MetaclassReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ownedNumberType880: BinaryAssociation = BinaryAssociation(
    name="ownedNumberType880",
    ends={
        Property(name="aadl2_NumberType881", type=aadl2_RangeType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_RangeType", type=aadl2_NumberType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
numberType882: BinaryAssociation = BinaryAssociation(
    name="numberType882",
    ends={
        Property(name="aadl2_NumberType884", type=aadl2_RangeType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_RangeType883", type=aadl2_NumberType, multiplicity=Multiplicity(1, 1))
    }
)
ownedField885: BinaryAssociation = BinaryAssociation(
    name="ownedField885",
    ends={
        Property(name="aadl2_BasicProperty886", type=aadl2_RecordType, multiplicity=Multiplicity(1, 1)),
        Property(name="aadl2_RecordType", type=aadl2_BasicProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_aadl2_Namespace_NamedElement = Generalization(general=NamedElement, specific=aadl2_Namespace)
gen_aadl2_Comment_Element = Generalization(general=Element, specific=aadl2_Comment)
gen_aadl2_NamedElement_Element = Generalization(general=Element, specific=aadl2_NamedElement)
gen_aadl2_Property_BasicProperty = Generalization(general=BasicProperty, specific=aadl2_Property)
gen_aadl2_PropertyAssociation_Element = Generalization(general=Element, specific=aadl2_PropertyAssociation)
gen_aadl2_BasicProperty_TypedElement = Generalization(general=TypedElement, specific=aadl2_BasicProperty)
gen_aadl2_TypedElement_NamedElement = Generalization(general=NamedElement, specific=aadl2_TypedElement)
gen_aadl2_PropertyType_Type = Generalization(general=Type, specific=aadl2_PropertyType)
gen_aadl2_PropertyExpression_Element = Generalization(general=Element, specific=aadl2_PropertyExpression)
gen_aadl2_MetaclassReference_PropertyOwner = Generalization(general=PropertyOwner, specific=aadl2_MetaclassReference)
gen_aadl2_PropertyOwner_Element = Generalization(general=Element, specific=aadl2_PropertyOwner)
gen_aadl2_Classifier_Namespace = Generalization(general=Namespace, specific=aadl2_Classifier)
gen_aadl2_Classifier_Type = Generalization(general=Type, specific=aadl2_Classifier)
gen_aadl2_Type_NamedElement = Generalization(general=NamedElement, specific=aadl2_Type)
gen_aadl2_ClassifierFeature_NamedElement = Generalization(general=NamedElement, specific=aadl2_ClassifierFeature)
gen_aadl2_Generalization_DirectedRelationship = Generalization(general=DirectedRelationship, specific=aadl2_Generalization)
gen_aadl2_DirectedRelationship_Relationship = Generalization(general=Relationship, specific=aadl2_DirectedRelationship)
gen_aadl2_Relationship_Element = Generalization(general=Element, specific=aadl2_Relationship)
gen_aadl2_Mode_ModeFeature = Generalization(general=ModeFeature, specific=aadl2_Mode)
gen_aadl2_ModeFeature_ClassifierFeature = Generalization(general=ClassifierFeature, specific=aadl2_ModeFeature)
gen_aadl2_Prototype_StructuralFeature = Generalization(general=StructuralFeature, specific=aadl2_Prototype)
gen_aadl2_AnnexSubclause_ModalElement = Generalization(general=ModalElement, specific=aadl2_AnnexSubclause)
gen_aadl2_ModalElement_NamedElement = Generalization(general=NamedElement, specific=aadl2_ModalElement)
gen_aadl2_PrototypeBinding_Element = Generalization(general=Element, specific=aadl2_PrototypeBinding)
gen_aadl2_ContainedNamedElement_Element = Generalization(general=Element, specific=aadl2_ContainedNamedElement)
gen_aadl2_ContainmentPathElement_Element = Generalization(general=Element, specific=aadl2_ContainmentPathElement)
gen_aadl2_StructuralFeature_RefinableElement = Generalization(general=RefinableElement, specific=aadl2_StructuralFeature)
gen_aadl2_StructuralFeature_ClassifierFeature = Generalization(general=ClassifierFeature, specific=aadl2_StructuralFeature)
gen_aadl2_RefinableElement_NamedElement = Generalization(general=NamedElement, specific=aadl2_RefinableElement)
gen_aadl2_BehavioralFeature_ClassifierFeature = Generalization(general=ClassifierFeature, specific=aadl2_BehavioralFeature)
gen_aadl2_ArraySpecification_Element = Generalization(general=Element, specific=aadl2_ArraySpecification)
gen_aadl2_ArraySize_Element = Generalization(general=Element, specific=aadl2_ArraySize)
gen_aadl2_ArrayableElement_Element = Generalization(general=Element, specific=aadl2_ArrayableElement)
gen_aadl2_Numeral_ArraySize = Generalization(general=ArraySize, specific=aadl2_Numeral)
gen_aadl2_ArrayRange_Element = Generalization(general=Element, specific=aadl2_ArrayRange)
gen_aadl2_ModalPropertyValue_ModalElement = Generalization(general=ModalElement, specific=aadl2_ModalPropertyValue)
gen_aadl2_ComponentImplementation_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_ComponentImplementation)
gen_aadl2_ComponentImplementationReference_Element = Generalization(general=Element, specific=aadl2_ComponentImplementationReference)
gen_aadl2_ComponentClassifier_Classifier = Generalization(general=Classifier, specific=aadl2_ComponentClassifier)
gen_aadl2_ModeTransitionTrigger_Element = Generalization(general=Element, specific=aadl2_ModeTransitionTrigger)
gen_aadl2_TriggerPort_ModeTransitionTrigger = Generalization(general=ModeTransitionTrigger, specific=aadl2_TriggerPort)
gen_aadl2_Context_NamedElement = Generalization(general=NamedElement, specific=aadl2_Context)
gen_aadl2_Port_DirectedFeature = Generalization(general=DirectedFeature, specific=aadl2_Port)
gen_aadl2_ModeTransition_ModeFeature = Generalization(general=ModeFeature, specific=aadl2_ModeTransition)
gen_aadl2_FeatureConnectionEnd_ConnectionEnd = Generalization(general=ConnectionEnd, specific=aadl2_FeatureConnectionEnd)
gen_aadl2_ConnectionEnd_NamedElement = Generalization(general=NamedElement, specific=aadl2_ConnectionEnd)
gen_aadl2_Port_PortConnectionEnd = Generalization(general=PortConnectionEnd, specific=aadl2_Port)
gen_aadl2_DirectedFeature_Feature = Generalization(general=Feature, specific=aadl2_DirectedFeature)
gen_aadl2_Feature_StructuralFeature = Generalization(general=StructuralFeature, specific=aadl2_Feature)
gen_aadl2_Feature_FeatureConnectionEnd = Generalization(general=FeatureConnectionEnd, specific=aadl2_Feature)
gen_aadl2_Feature_ArrayableElement = Generalization(general=ArrayableElement, specific=aadl2_Feature)
gen_aadl2_FlowSpecification_Flow = Generalization(general=Flow, specific=aadl2_FlowSpecification)
gen_aadl2_FlowSpecification_ModalElement = Generalization(general=ModalElement, specific=aadl2_FlowSpecification)
gen_aadl2_PortConnectionEnd_ConnectionEnd = Generalization(general=ConnectionEnd, specific=aadl2_PortConnectionEnd)
gen_aadl2_ProcessorPort_PortConnectionEnd = Generalization(general=PortConnectionEnd, specific=aadl2_ProcessorPort)
gen_aadl2_ProcessorPort_ModeTransitionTrigger = Generalization(general=ModeTransitionTrigger, specific=aadl2_ProcessorPort)
gen_aadl2_InternalEvent_PortConnectionEnd = Generalization(general=PortConnectionEnd, specific=aadl2_InternalEvent)
gen_aadl2_InternalEvent_ModeTransitionTrigger = Generalization(general=ModeTransitionTrigger, specific=aadl2_InternalEvent)
gen_aadl2_ComponentType_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_ComponentType)
gen_aadl2_TypeExtension_Generalization = Generalization(general=Generalization, specific=aadl2_TypeExtension)
gen_aadl2_FeatureGroup_DirectedFeature = Generalization(general=DirectedFeature, specific=aadl2_FeatureGroup)
gen_aadl2_FeatureGroup_Context = Generalization(general=Context, specific=aadl2_FeatureGroup)
gen_aadl2_FeatureGroup_FeatureGroupConnectionEnd = Generalization(general=FeatureGroupConnectionEnd, specific=aadl2_FeatureGroup)
gen_aadl2_FeatureGroup_CallContext = Generalization(general=CallContext, specific=aadl2_FeatureGroup)
gen_aadl2_FeatureGroupConnectionEnd_ConnectionEnd = Generalization(general=ConnectionEnd, specific=aadl2_FeatureGroupConnectionEnd)
gen_aadl2_CallContext_Element = Generalization(general=Element, specific=aadl2_CallContext)
gen_aadl2_FeatureGroupType_Classifier = Generalization(general=Classifier, specific=aadl2_FeatureGroupType)
gen_aadl2_Flow_StructuralFeature = Generalization(general=StructuralFeature, specific=aadl2_Flow)
gen_aadl2_BusAccess_Access = Generalization(general=Access, specific=aadl2_BusAccess)
gen_aadl2_Access_Feature = Generalization(general=Feature, specific=aadl2_Access)
gen_aadl2_Access_AccessConnectionEnd = Generalization(general=AccessConnectionEnd, specific=aadl2_Access)
gen_aadl2_AccessConnectionEnd_ConnectionEnd = Generalization(general=ConnectionEnd, specific=aadl2_AccessConnectionEnd)
gen_aadl2_GroupExtension_Generalization = Generalization(general=Generalization, specific=aadl2_GroupExtension)
gen_aadl2_EventPort_Port = Generalization(general=Port, specific=aadl2_EventPort)
gen_aadl2_Parameter_DirectedFeature = Generalization(general=DirectedFeature, specific=aadl2_Parameter)
gen_aadl2_Parameter_Context = Generalization(general=Context, specific=aadl2_Parameter)
gen_aadl2_Parameter_ParameterConnectionEnd = Generalization(general=ParameterConnectionEnd, specific=aadl2_Parameter)
gen_aadl2_SubprogramAccess_Access = Generalization(general=Access, specific=aadl2_SubprogramAccess)
gen_aadl2_SubprogramAccess_CalledSubprogram = Generalization(general=CalledSubprogram, specific=aadl2_SubprogramAccess)
gen_aadl2_CalledSubprogram_Element = Generalization(general=Element, specific=aadl2_CalledSubprogram)
gen_aadl2_BusClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_BusClassifier)
gen_aadl2_BusClassifier_Bus = Generalization(general=Bus, specific=aadl2_BusClassifier)
gen_aadl2_Bus_NamedElement = Generalization(general=NamedElement, specific=aadl2_Bus)
gen_aadl2_DataAccess_Access = Generalization(general=Access, specific=aadl2_DataAccess)
gen_aadl2_DataAccess_FlowElement = Generalization(general=FlowElement, specific=aadl2_DataAccess)
gen_aadl2_DataAccess_ParameterConnectionEnd = Generalization(general=ParameterConnectionEnd, specific=aadl2_DataAccess)
gen_aadl2_DataAccess_PortConnectionEnd = Generalization(general=PortConnectionEnd, specific=aadl2_DataAccess)
gen_aadl2_ParameterConnectionEnd_ConnectionEnd = Generalization(general=ConnectionEnd, specific=aadl2_ParameterConnectionEnd)
gen_aadl2_FlowElement_EndToEndFlowElement = Generalization(general=EndToEndFlowElement, specific=aadl2_FlowElement)
gen_aadl2_EndToEndFlowElement_NamedElement = Generalization(general=NamedElement, specific=aadl2_EndToEndFlowElement)
gen_aadl2_DataClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_DataClassifier)
gen_aadl2_DataClassifier_Data = Generalization(general=Data, specific=aadl2_DataClassifier)
gen_aadl2_Data_NamedElement = Generalization(general=NamedElement, specific=aadl2_Data)
gen_aadl2_DataPort_Port = Generalization(general=Port, specific=aadl2_DataPort)
gen_aadl2_DataPort_Context = Generalization(general=Context, specific=aadl2_DataPort)
gen_aadl2_DataPort_ParameterConnectionEnd = Generalization(general=ParameterConnectionEnd, specific=aadl2_DataPort)
gen_aadl2_EventDataPort_Port = Generalization(general=Port, specific=aadl2_EventDataPort)
gen_aadl2_EventDataPort_Context = Generalization(general=Context, specific=aadl2_EventDataPort)
gen_aadl2_EventDataPort_ParameterConnectionEnd = Generalization(general=ParameterConnectionEnd, specific=aadl2_EventDataPort)
gen_aadl2_SubprogramClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_SubprogramClassifier)
gen_aadl2_SubprogramClassifier_Subprogram = Generalization(general=Subprogram, specific=aadl2_SubprogramClassifier)
gen_aadl2_Subprogram_NamedElement = Generalization(general=NamedElement, specific=aadl2_Subprogram)
gen_aadl2_Subprogram_CalledSubprogram = Generalization(general=CalledSubprogram, specific=aadl2_Subprogram)
gen_aadl2_SubprogramGroupAccess_Access = Generalization(general=Access, specific=aadl2_SubprogramGroupAccess)
gen_aadl2_SubprogramGroupAccess_CallContext = Generalization(general=CallContext, specific=aadl2_SubprogramGroupAccess)
gen_aadl2_SubprogramGroupClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_SubprogramGroupClassifier)
gen_aadl2_SubprogramGroupClassifier_SubprogramGroup = Generalization(general=SubprogramGroup, specific=aadl2_SubprogramGroupClassifier)
gen_aadl2_SubprogramGroup_NamedElement = Generalization(general=NamedElement, specific=aadl2_SubprogramGroup)
gen_aadl2_AbstractFeature_DirectedFeature = Generalization(general=DirectedFeature, specific=aadl2_AbstractFeature)
gen_aadl2_Subcomponent_StructuralFeature = Generalization(general=StructuralFeature, specific=aadl2_Subcomponent)
gen_aadl2_Subcomponent_ModalElement = Generalization(general=ModalElement, specific=aadl2_Subcomponent)
gen_aadl2_Subcomponent_Context = Generalization(general=Context, specific=aadl2_Subcomponent)
gen_aadl2_Subcomponent_FlowElement = Generalization(general=FlowElement, specific=aadl2_Subcomponent)
gen_aadl2_Subcomponent_ArrayableElement = Generalization(general=ArrayableElement, specific=aadl2_Subcomponent)
gen_aadl2_AbstractClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_AbstractClassifier)
gen_aadl2_AbstractClassifier_Abstract = Generalization(general=Abstract, specific=aadl2_AbstractClassifier)
gen_aadl2_Abstract_NamedElement = Generalization(general=NamedElement, specific=aadl2_Abstract)
gen_aadl2_FlowImplementation_ModalPath = Generalization(general=ModalPath, specific=aadl2_FlowImplementation)
gen_aadl2_FlowImplementation_StructuralFeature = Generalization(general=StructuralFeature, specific=aadl2_FlowImplementation)
gen_aadl2_ComponentPrototype_Prototype = Generalization(general=Prototype, specific=aadl2_ComponentPrototype)
gen_aadl2_ModeBinding_Element = Generalization(general=Element, specific=aadl2_ModeBinding)
gen_aadl2_ImplementationExtension_Generalization = Generalization(general=Generalization, specific=aadl2_ImplementationExtension)
gen_aadl2_Realization_Generalization = Generalization(general=Generalization, specific=aadl2_Realization)
gen_aadl2_ModalPath_ModalElement = Generalization(general=ModalElement, specific=aadl2_ModalPath)
gen_aadl2_SubcomponentFlow_FlowElement = Generalization(general=FlowElement, specific=aadl2_SubcomponentFlow)
gen_aadl2_Connection_ModalPath = Generalization(general=ModalPath, specific=aadl2_Connection)
gen_aadl2_Connection_StructuralFeature = Generalization(general=StructuralFeature, specific=aadl2_Connection)
gen_aadl2_Connection_FlowElement = Generalization(general=FlowElement, specific=aadl2_Connection)
gen_aadl2_ParameterConnection_Connection = Generalization(general=Connection, specific=aadl2_ParameterConnection)
gen_aadl2_PortConnection_Connection = Generalization(general=Connection, specific=aadl2_PortConnection)
gen_aadl2_FeatureConnection_Connection = Generalization(general=Connection, specific=aadl2_FeatureConnection)
gen_aadl2_EndToEndFlow_Flow = Generalization(general=Flow, specific=aadl2_EndToEndFlow)
gen_aadl2_EndToEndFlow_ModalPath = Generalization(general=ModalPath, specific=aadl2_EndToEndFlow)
gen_aadl2_EndToEndFlow_EndToEndFlowElement = Generalization(general=EndToEndFlowElement, specific=aadl2_EndToEndFlow)
gen_aadl2_AbstractSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_AbstractSubcomponent)
gen_aadl2_AbstractSubcomponent_Abstract = Generalization(general=Abstract, specific=aadl2_AbstractSubcomponent)
gen_aadl2_AccessConnection_Connection = Generalization(general=Connection, specific=aadl2_AccessConnection)
gen_aadl2_FeatureGroupConnection_Connection = Generalization(general=Connection, specific=aadl2_FeatureGroupConnection)
gen_aadl2_ProcessorSubprogram_AccessConnectionEnd = Generalization(general=AccessConnectionEnd, specific=aadl2_ProcessorSubprogram)
gen_aadl2_AnnexLibrary_NamedElement = Generalization(general=NamedElement, specific=aadl2_AnnexLibrary)
gen_aadl2_DefaultAnnexLibrary_AnnexLibrary = Generalization(general=AnnexLibrary, specific=aadl2_DefaultAnnexLibrary)
gen_aadl2_DefaultAnnexSubclause_AnnexSubclause = Generalization(general=AnnexSubclause, specific=aadl2_DefaultAnnexSubclause)
gen_aadl2_PublicPackageSection_PackageSection = Generalization(general=PackageSection, specific=aadl2_PublicPackageSection)
gen_aadl2_PackageSection_Namespace = Generalization(general=Namespace, specific=aadl2_PackageSection)
gen_aadl2_FeatureGroupTypeRename_NamedElement = Generalization(general=NamedElement, specific=aadl2_FeatureGroupTypeRename)
gen_aadl2_AbstractType_ComponentType = Generalization(general=ComponentType, specific=aadl2_AbstractType)
gen_aadl2_AbstractType_AbstractClassifier = Generalization(general=AbstractClassifier, specific=aadl2_AbstractType)
gen_aadl2_AbstractType_CallContext = Generalization(general=CallContext, specific=aadl2_AbstractType)
gen_aadl2_PackageRename_NamedElement = Generalization(general=NamedElement, specific=aadl2_PackageRename)
gen_aadl2_AadlPackage_NamedElement = Generalization(general=NamedElement, specific=aadl2_AadlPackage)
gen_aadl2_PrivatePackageSection_PackageSection = Generalization(general=PackageSection, specific=aadl2_PrivatePackageSection)
gen_aadl2_ComponentTypeRename_NamedElement = Generalization(general=NamedElement, specific=aadl2_ComponentTypeRename)
gen_aadl2_AbstractImplementation_BehavioredImplementation = Generalization(general=BehavioredImplementation, specific=aadl2_AbstractImplementation)
gen_aadl2_AbstractImplementation_AbstractClassifier = Generalization(general=AbstractClassifier, specific=aadl2_AbstractImplementation)
gen_aadl2_CallSpecification_BehavioralFeature = Generalization(general=BehavioralFeature, specific=aadl2_CallSpecification)
gen_aadl2_SubprogramCallSequence_ModalElement = Generalization(general=ModalElement, specific=aadl2_SubprogramCallSequence)
gen_aadl2_SubprogramCallSequence_BehavioralFeature = Generalization(general=BehavioralFeature, specific=aadl2_SubprogramCallSequence)
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
gen_aadl2_Device_NamedElement = Generalization(general=NamedElement, specific=aadl2_Device)
gen_aadl2_DeviceClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_DeviceClassifier)
gen_aadl2_DeviceClassifier_Device = Generalization(general=Device, specific=aadl2_DeviceClassifier)
gen_aadl2_MemorySubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_MemorySubcomponent)
gen_aadl2_MemorySubcomponent_Memory = Generalization(general=Memory, specific=aadl2_MemorySubcomponent)
gen_aadl2_Memory_NamedElement = Generalization(general=NamedElement, specific=aadl2_Memory)
gen_aadl2_BehavioredImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_BehavioredImplementation)
gen_aadl2_Process_NamedElement = Generalization(general=NamedElement, specific=aadl2_Process)
gen_aadl2_ProcessClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_ProcessClassifier)
gen_aadl2_ProcessClassifier_Process = Generalization(general=Process, specific=aadl2_ProcessClassifier)
gen_aadl2_ProcessorSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_ProcessorSubcomponent)
gen_aadl2_ProcessorSubcomponent_Processor = Generalization(general=Processor, specific=aadl2_ProcessorSubcomponent)
gen_aadl2_Processor_NamedElement = Generalization(general=NamedElement, specific=aadl2_Processor)
gen_aadl2_ProcessorClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_ProcessorClassifier)
gen_aadl2_ProcessorClassifier_Processor = Generalization(general=Processor, specific=aadl2_ProcessorClassifier)
gen_aadl2_SystemSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_SystemSubcomponent)
gen_aadl2_SystemSubcomponent_System = Generalization(general=System, specific=aadl2_SystemSubcomponent)
gen_aadl2_System_NamedElement = Generalization(general=NamedElement, specific=aadl2_System)
gen_aadl2_SystemClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_SystemClassifier)
gen_aadl2_SystemClassifier_System = Generalization(general=System, specific=aadl2_SystemClassifier)
gen_aadl2_SubprogramSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_SubprogramSubcomponent)
gen_aadl2_SubprogramSubcomponent_AccessConnectionEnd = Generalization(general=AccessConnectionEnd, specific=aadl2_SubprogramSubcomponent)
gen_aadl2_SubprogramSubcomponent_Subprogram = Generalization(general=Subprogram, specific=aadl2_SubprogramSubcomponent)
gen_aadl2_SubprogramGroupSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_SubprogramGroupSubcomponent)
gen_aadl2_SubprogramGroupSubcomponent_AccessConnectionEnd = Generalization(general=AccessConnectionEnd, specific=aadl2_SubprogramGroupSubcomponent)
gen_aadl2_SubprogramGroupSubcomponent_SubprogramGroup = Generalization(general=SubprogramGroup, specific=aadl2_SubprogramGroupSubcomponent)
gen_aadl2_SubprogramGroupSubcomponent_CallContext = Generalization(general=CallContext, specific=aadl2_SubprogramGroupSubcomponent)
gen_aadl2_ThreadSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_ThreadSubcomponent)
gen_aadl2_ThreadSubcomponent_Thread = Generalization(general=Thread, specific=aadl2_ThreadSubcomponent)
gen_aadl2_MemoryClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_MemoryClassifier)
gen_aadl2_MemoryClassifier_Memory = Generalization(general=Memory, specific=aadl2_MemoryClassifier)
gen_aadl2_ProcessSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_ProcessSubcomponent)
gen_aadl2_ProcessSubcomponent_Process = Generalization(general=Process, specific=aadl2_ProcessSubcomponent)
gen_aadl2_ThreadGroup_NamedElement = Generalization(general=NamedElement, specific=aadl2_ThreadGroup)
gen_aadl2_ThreadGroupClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_ThreadGroupClassifier)
gen_aadl2_ThreadGroupClassifier_ThreadGroup = Generalization(general=ThreadGroup, specific=aadl2_ThreadGroupClassifier)
gen_aadl2_VirtualBusSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_VirtualBusSubcomponent)
gen_aadl2_VirtualBusSubcomponent_VirtualBus = Generalization(general=VirtualBus, specific=aadl2_VirtualBusSubcomponent)
gen_aadl2_VirtualBus_NamedElement = Generalization(general=NamedElement, specific=aadl2_VirtualBus)
gen_aadl2_VirtualBusClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_VirtualBusClassifier)
gen_aadl2_VirtualBusClassifier_VirtualBus = Generalization(general=VirtualBus, specific=aadl2_VirtualBusClassifier)
gen_aadl2_VirtualProcessorSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_VirtualProcessorSubcomponent)
gen_aadl2_VirtualProcessorSubcomponent_VirtualProcessor = Generalization(general=VirtualProcessor, specific=aadl2_VirtualProcessorSubcomponent)
gen_aadl2_VirtualProcessor_NamedElement = Generalization(general=NamedElement, specific=aadl2_VirtualProcessor)
gen_aadl2_VirtualProcessorClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_VirtualProcessorClassifier)
gen_aadl2_VirtualProcessorClassifier_VirtualProcessor = Generalization(general=VirtualProcessor, specific=aadl2_VirtualProcessorClassifier)
gen_aadl2_BusType_ComponentType = Generalization(general=ComponentType, specific=aadl2_BusType)
gen_aadl2_BusType_BusClassifier = Generalization(general=BusClassifier, specific=aadl2_BusType)
gen_aadl2_BusImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_BusImplementation)
gen_aadl2_BusImplementation_BusClassifier = Generalization(general=BusClassifier, specific=aadl2_BusImplementation)
gen_aadl2_Thread_NamedElement = Generalization(general=NamedElement, specific=aadl2_Thread)
gen_aadl2_ThreadClassifier_ComponentClassifier = Generalization(general=ComponentClassifier, specific=aadl2_ThreadClassifier)
gen_aadl2_ThreadClassifier_Thread = Generalization(general=Thread, specific=aadl2_ThreadClassifier)
gen_aadl2_ThreadGroupSubcomponent_Subcomponent = Generalization(general=Subcomponent, specific=aadl2_ThreadGroupSubcomponent)
gen_aadl2_ThreadGroupSubcomponent_ThreadGroup = Generalization(general=ThreadGroup, specific=aadl2_ThreadGroupSubcomponent)
gen_aadl2_DataImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_DataImplementation)
gen_aadl2_DataImplementation_DataClassifier = Generalization(general=DataClassifier, specific=aadl2_DataImplementation)
gen_aadl2_DeviceType_ComponentType = Generalization(general=ComponentType, specific=aadl2_DeviceType)
gen_aadl2_DeviceType_DeviceClassifier = Generalization(general=DeviceClassifier, specific=aadl2_DeviceType)
gen_aadl2_DataType_ComponentType = Generalization(general=ComponentType, specific=aadl2_DataType)
gen_aadl2_DataType_DataClassifier = Generalization(general=DataClassifier, specific=aadl2_DataType)
gen_aadl2_DataType_CallContext = Generalization(general=CallContext, specific=aadl2_DataType)
gen_aadl2_DeviceImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_DeviceImplementation)
gen_aadl2_DeviceImplementation_DeviceClassifier = Generalization(general=DeviceClassifier, specific=aadl2_DeviceImplementation)
gen_aadl2_MemoryType_ComponentType = Generalization(general=ComponentType, specific=aadl2_MemoryType)
gen_aadl2_MemoryType_MemoryClassifier = Generalization(general=MemoryClassifier, specific=aadl2_MemoryType)
gen_aadl2_MemoryImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_MemoryImplementation)
gen_aadl2_MemoryImplementation_MemoryClassifier = Generalization(general=MemoryClassifier, specific=aadl2_MemoryImplementation)
gen_aadl2_ProcessType_ComponentType = Generalization(general=ComponentType, specific=aadl2_ProcessType)
gen_aadl2_ProcessType_ProcessClassifier = Generalization(general=ProcessClassifier, specific=aadl2_ProcessType)
gen_aadl2_ProcessorType_ComponentType = Generalization(general=ComponentType, specific=aadl2_ProcessorType)
gen_aadl2_ProcessorType_ProcessorClassifier = Generalization(general=ProcessorClassifier, specific=aadl2_ProcessorType)
gen_aadl2_ProcessImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_ProcessImplementation)
gen_aadl2_ProcessImplementation_ProcessClassifier = Generalization(general=ProcessClassifier, specific=aadl2_ProcessImplementation)
gen_aadl2_ProcessorImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_ProcessorImplementation)
gen_aadl2_ProcessorImplementation_ProcessorClassifier = Generalization(general=ProcessorClassifier, specific=aadl2_ProcessorImplementation)
gen_aadl2_SubprogramType_ComponentType = Generalization(general=ComponentType, specific=aadl2_SubprogramType)
gen_aadl2_SubprogramType_SubprogramClassifier = Generalization(general=SubprogramClassifier, specific=aadl2_SubprogramType)
gen_aadl2_SubprogramGroupImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_SubprogramGroupImplementation)
gen_aadl2_SubprogramGroupImplementation_SubprogramGroupClassifier = Generalization(general=SubprogramGroupClassifier, specific=aadl2_SubprogramGroupImplementation)
gen_aadl2_SubprogramImplementation_BehavioredImplementation = Generalization(general=BehavioredImplementation, specific=aadl2_SubprogramImplementation)
gen_aadl2_SubprogramImplementation_SubprogramClassifier = Generalization(general=SubprogramClassifier, specific=aadl2_SubprogramImplementation)
gen_aadl2_SubprogramGroupType_ComponentType = Generalization(general=ComponentType, specific=aadl2_SubprogramGroupType)
gen_aadl2_SubprogramGroupType_SubprogramGroupClassifier = Generalization(general=SubprogramGroupClassifier, specific=aadl2_SubprogramGroupType)
gen_aadl2_SubprogramGroupType_CallContext = Generalization(general=CallContext, specific=aadl2_SubprogramGroupType)
gen_aadl2_SystemType_ComponentType = Generalization(general=ComponentType, specific=aadl2_SystemType)
gen_aadl2_SystemType_SystemClassifier = Generalization(general=SystemClassifier, specific=aadl2_SystemType)
gen_aadl2_SystemImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_SystemImplementation)
gen_aadl2_SystemImplementation_SystemClassifier = Generalization(general=SystemClassifier, specific=aadl2_SystemImplementation)
gen_aadl2_ThreadType_ComponentType = Generalization(general=ComponentType, specific=aadl2_ThreadType)
gen_aadl2_ThreadType_ThreadClassifier = Generalization(general=ThreadClassifier, specific=aadl2_ThreadType)
gen_aadl2_ThreadGroupType_ComponentType = Generalization(general=ComponentType, specific=aadl2_ThreadGroupType)
gen_aadl2_ThreadImplementation_BehavioredImplementation = Generalization(general=BehavioredImplementation, specific=aadl2_ThreadImplementation)
gen_aadl2_ThreadImplementation_ThreadClassifier = Generalization(general=ThreadClassifier, specific=aadl2_ThreadImplementation)
gen_aadl2_ThreadGroupType_ThreadGroupClassifier = Generalization(general=ThreadGroupClassifier, specific=aadl2_ThreadGroupType)
gen_aadl2_VirtualBusType_ComponentType = Generalization(general=ComponentType, specific=aadl2_VirtualBusType)
gen_aadl2_VirtualBusType_VirtualBusClassifier = Generalization(general=VirtualBusClassifier, specific=aadl2_VirtualBusType)
gen_aadl2_VirtualBusImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_VirtualBusImplementation)
gen_aadl2_VirtualBusImplementation_VirtualBusClassifier = Generalization(general=VirtualBusClassifier, specific=aadl2_VirtualBusImplementation)
gen_aadl2_ThreadGroupImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_ThreadGroupImplementation)
gen_aadl2_ThreadGroupImplementation_ThreadGroupClassifier = Generalization(general=ThreadGroupClassifier, specific=aadl2_ThreadGroupImplementation)
gen_aadl2_VirtualProcessorType_ComponentType = Generalization(general=ComponentType, specific=aadl2_VirtualProcessorType)
gen_aadl2_VirtualProcessorType_VirtualProcessorClassifier = Generalization(general=VirtualProcessorClassifier, specific=aadl2_VirtualProcessorType)
gen_aadl2_PropertySet_Namespace = Generalization(general=Namespace, specific=aadl2_PropertySet)
gen_aadl2_VirtualProcessorImplementation_ComponentImplementation = Generalization(general=ComponentImplementation, specific=aadl2_VirtualProcessorImplementation)
gen_aadl2_VirtualProcessorImplementation_VirtualProcessorClassifier = Generalization(general=VirtualProcessorClassifier, specific=aadl2_VirtualProcessorImplementation)
gen_aadl2_PropertyConstant_TypedElement = Generalization(general=TypedElement, specific=aadl2_PropertyConstant)
gen_aadl2_ComponentPrototypeBinding_PrototypeBinding = Generalization(general=PrototypeBinding, specific=aadl2_ComponentPrototypeBinding)
gen_aadl2_ComponentPrototypeActual_Element = Generalization(general=Element, specific=aadl2_ComponentPrototypeActual)
gen_aadl2_FeatureGroupPrototypeBinding_PrototypeBinding = Generalization(general=PrototypeBinding, specific=aadl2_FeatureGroupPrototypeBinding)
gen_aadl2_FeatureGroupPrototypeActual_Element = Generalization(general=Element, specific=aadl2_FeatureGroupPrototypeActual)
gen_aadl2_FeaturePrototype_Prototype = Generalization(general=Prototype, specific=aadl2_FeaturePrototype)
gen_aadl2_FeatureGroupPrototype_Prototype = Generalization(general=Prototype, specific=aadl2_FeatureGroupPrototype)
gen_aadl2_FeaturePrototypeBinding_PrototypeBinding = Generalization(general=PrototypeBinding, specific=aadl2_FeaturePrototypeBinding)
gen_aadl2_FeaturePrototypeActual_Element = Generalization(general=Element, specific=aadl2_FeaturePrototypeActual)
gen_aadl2_AccessSpecification_FeaturePrototypeActual = Generalization(general=FeaturePrototypeActual, specific=aadl2_AccessSpecification)
gen_aadl2_PortSpecification_FeaturePrototypeActual = Generalization(general=FeaturePrototypeActual, specific=aadl2_PortSpecification)
gen_aadl2_FeaturePrototypeReference_FeaturePrototypeActual = Generalization(general=FeaturePrototypeActual, specific=aadl2_FeaturePrototypeReference)
gen_aadl2_ComponentPrototypeReference_ComponentPrototypeActual = Generalization(general=ComponentPrototypeActual, specific=aadl2_ComponentPrototypeReference)
gen_aadl2_ComponentReference_ComponentPrototypeActual = Generalization(general=ComponentPrototypeActual, specific=aadl2_ComponentReference)
gen_aadl2_FeatureGroupPrototypeReference_FeatureGroupPrototypeActual = Generalization(general=FeatureGroupPrototypeActual, specific=aadl2_FeatureGroupPrototypeReference)
gen_aadl2_FeatureGroupReference_FeatureGroupPrototypeActual = Generalization(general=FeatureGroupPrototypeActual, specific=aadl2_FeatureGroupReference)
gen_aadl2_ProcessorCall_CallSpecification = Generalization(general=CallSpecification, specific=aadl2_ProcessorCall)
gen_aadl2_SubprogramCall_CallSpecification = Generalization(general=CallSpecification, specific=aadl2_SubprogramCall)
gen_aadl2_SubprogramCall_Context = Generalization(general=Context, specific=aadl2_SubprogramCall)
gen_aadl2_BasicPropertyAssociation_Element = Generalization(general=Element, specific=aadl2_BasicPropertyAssociation)
gen_aadl2_StringLiteral_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_StringLiteral)
gen_aadl2_EnumerationValue_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_EnumerationValue)
gen_aadl2_PropertyValue_PropertyExpression = Generalization(general=PropertyExpression, specific=aadl2_PropertyValue)
gen_aadl2_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=aadl2_EnumerationLiteral)
gen_aadl2_UnitValue_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_UnitValue)
gen_aadl2_UnitLiteral_EnumerationLiteral = Generalization(general=EnumerationLiteral, specific=aadl2_UnitLiteral)
gen_aadl2_NumberValue_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_NumberValue)
gen_aadl2_RealLiteral_NumberValue = Generalization(general=NumberValue, specific=aadl2_RealLiteral)
gen_aadl2_ClassifierValue_PropertyOwner = Generalization(general=PropertyOwner, specific=aadl2_ClassifierValue)
gen_aadl2_ClassifierValue_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_ClassifierValue)
gen_aadl2_ReferenceValue_ContainedNamedElement = Generalization(general=ContainedNamedElement, specific=aadl2_ReferenceValue)
gen_aadl2_ReferenceValue_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_ReferenceValue)
gen_aadl2_BooleanLiteral_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_BooleanLiteral)
gen_aadl2_RangeValue_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_RangeValue)
gen_aadl2_IntegerLiteral_NumberValue = Generalization(general=NumberValue, specific=aadl2_IntegerLiteral)
gen_aadl2_RecordValue_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_RecordValue)
gen_aadl2_ConstantValue_ArraySize = Generalization(general=ArraySize, specific=aadl2_ConstantValue)
gen_aadl2_ConstantValue_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_ConstantValue)
gen_aadl2_PropertyReference_ArraySize = Generalization(general=ArraySize, specific=aadl2_PropertyReference)
gen_aadl2_PropertyReference_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_PropertyReference)
gen_aadl2_Operation_PropertyExpression = Generalization(general=PropertyExpression, specific=aadl2_Operation)
gen_aadl2_NumberType_PropertyType = Generalization(general=PropertyType, specific=aadl2_NumberType)
gen_aadl2_ComputedValue_PropertyValue = Generalization(general=PropertyValue, specific=aadl2_ComputedValue)
gen_aadl2_ListValue_PropertyExpression = Generalization(general=PropertyExpression, specific=aadl2_ListValue)
gen_aadl2_GlobalNamespace_Namespace = Generalization(general=Namespace, specific=aadl2_GlobalNamespace)
gen_aadl2_AadlBoolean_PropertyType = Generalization(general=PropertyType, specific=aadl2_AadlBoolean)
gen_aadl2_AadlString_PropertyType = Generalization(general=PropertyType, specific=aadl2_AadlString)
gen_aadl2_AadlInteger_NumberType = Generalization(general=NumberType, specific=aadl2_AadlInteger)
gen_aadl2_AadlReal_NumberType = Generalization(general=NumberType, specific=aadl2_AadlReal)
gen_aadl2_UnitsType_EnumerationType = Generalization(general=EnumerationType, specific=aadl2_UnitsType)
gen_aadl2_EnumerationType_Namespace = Generalization(general=Namespace, specific=aadl2_EnumerationType)
gen_aadl2_EnumerationType_PropertyType = Generalization(general=PropertyType, specific=aadl2_EnumerationType)
gen_aadl2_NumericRange_Element = Generalization(general=Element, specific=aadl2_NumericRange)
gen_aadl2_ClassifierType_PropertyType = Generalization(general=PropertyType, specific=aadl2_ClassifierType)
gen_aadl2_RangeType_PropertyType = Generalization(general=PropertyType, specific=aadl2_RangeType)
gen_aadl2_RecordType_Namespace = Generalization(general=Namespace, specific=aadl2_RecordType)
gen_aadl2_RecordType_PropertyType = Generalization(general=PropertyType, specific=aadl2_RecordType)
gen_aadl2_RecordField_BasicProperty = Generalization(general=BasicProperty, specific=aadl2_RecordField)
gen_aadl2_ReferenceType_PropertyType = Generalization(general=PropertyType, specific=aadl2_ReferenceType)

# Domain Model
domain_model = DomainModel(
    name="aadl2",
    types={aadl2_Element, aadl2_Comment, aadl2_Namespace, NamedElement, aadl2_NamedElement, Element, aadl2_Property, aadl2_ContainedNamedElement, aadl2_Classifier, aadl2_ModalPropertyValue, BasicProperty, aadl2_PropertyExpression, aadl2_PropertyAssociation, aadl2_BasicProperty, TypedElement, aadl2_PropertyType, aadl2_TypedElement, aadl2_Type, aadl2_MetaclassReference, Type, aadl2_PropertyOwner, PropertyOwner, Namespace, aadl2_ClassifierFeature, aadl2_Generalization, aadl2_PrototypeBinding, DirectedRelationship, aadl2_AnnexSubclause, aadl2_Prototype, aadl2_DirectedRelationship, Relationship, aadl2_Relationship, aadl2_Mode, ModeFeature, aadl2_ModeFeature, ClassifierFeature, StructuralFeature, ModalElement, aadl2_ModalElement, aadl2_ContainmentPathElement, aadl2_StructuralFeature, RefinableElement, aadl2_RefinableElement, aadl2_BehavioralFeature, aadl2_ArraySpecification, aadl2_ArraySize, aadl2_ArrayableElement, aadl2_Numeral, aadl2_ArrayRange, ArraySize, ComponentClassifier, aadl2_ComponentImplementationReference, aadl2_Subcomponent, aadl2_ComponentImplementation, aadl2_FlowImplementation, aadl2_ComponentType, aadl2_Realization, aadl2_EndToEndFlow, aadl2_AbstractSubcomponent, aadl2_Connection, aadl2_ImplementationExtension, aadl2_ParameterConnection, aadl2_PortConnection, aadl2_FeatureConnection, aadl2_AccessConnection, aadl2_ComponentClassifier, Classifier, aadl2_ModeTransition, aadl2_ProcessorPort, aadl2_InternalEvent, aadl2_FeatureGroupConnection, aadl2_ProcessorSubprogram, aadl2_TriggerPort, ModeTransitionTrigger, aadl2_Context, aadl2_Port, DirectedFeature, PortConnectionEnd, aadl2_ModeTransitionTrigger, aadl2_FeatureConnectionEnd, ConnectionEnd, aadl2_ConnectionEnd, aadl2_DirectedFeature, Feature, aadl2_Feature, FeatureConnectionEnd, ArrayableElement, aadl2_FlowSpecification, aadl2_TypeExtension, aadl2_FeatureGroup, aadl2_AbstractFeature, Flow, aadl2_PortConnectionEnd, Generalization, Context, FeatureGroupConnectionEnd, CallContext, aadl2_FeatureGroupType, aadl2_FeatureGroupConnectionEnd, aadl2_CallContext, aadl2_DataPort, aadl2_EventDataPort, aadl2_EventPort, aadl2_Flow, aadl2_GroupExtension, aadl2_BusAccess, aadl2_DataAccess, Access, aadl2_BusClassifier, aadl2_Access, AccessConnectionEnd, aadl2_AccessConnectionEnd, aadl2_Parameter, aadl2_SubprogramAccess, aadl2_SubprogramGroupAccess, CalledSubprogram, aadl2_SubprogramClassifier, aadl2_CalledSubprogram, Bus, aadl2_Bus, FlowElement, ParameterConnectionEnd, aadl2_DataClassifier, aadl2_ParameterConnectionEnd, aadl2_FlowElement, EndToEndFlowElement, aadl2_EndToEndFlowElement, Data, aadl2_Data, Port, aadl2_ComponentPrototype, aadl2_ModeBinding, aadl2_AbstractClassifier, Subprogram, aadl2_Subprogram, aadl2_SubprogramGroupClassifier, SubprogramGroup, aadl2_SubprogramGroup, Abstract, aadl2_Abstract, ModalPath, aadl2_SubcomponentFlow, Prototype, aadl2_ModalPath, Subcomponent, Connection, aadl2_PackageRename, aadl2_ComponentTypeRename, aadl2_FeatureGroupTypeRename, aadl2_AnnexLibrary, aadl2_DefaultAnnexLibrary, AnnexLibrary, aadl2_DefaultAnnexSubclause, AnnexSubclause, aadl2_PublicPackageSection, PackageSection, aadl2_PrivatePackageSection, aadl2_PackageSection, aadl2_BusType, aadl2_BusImplementation, aadl2_DataType, aadl2_DataImplementation, aadl2_DeviceType, aadl2_AadlPackage, aadl2_AbstractType, aadl2_AbstractImplementation, aadl2_ProcessorType, aadl2_ProcessImplementation, aadl2_ProcessorImplementation, aadl2_SubprogramType, aadl2_DeviceImplementation, aadl2_MemoryType, aadl2_MemoryImplementation, aadl2_ProcessType, aadl2_ThreadType, aadl2_ThreadImplementation, aadl2_ThreadGroupType, aadl2_SubprogramImplementation, aadl2_ThreadGroupImplementation, aadl2_SubprogramGroupType, aadl2_SubprogramGroupImplementation, aadl2_SystemType, aadl2_SystemImplementation, aadl2_VirtualProcessorImplementation, aadl2_PropertySet, aadl2_VirtualBusType, aadl2_VirtualBusImplementation, aadl2_VirtualProcessorType, ComponentType, AbstractClassifier, BehavioredImplementation, aadl2_BusSubcomponent, aadl2_SubprogramSubcomponent, aadl2_SubprogramGroupSubcomponent, aadl2_ThreadSubcomponent, aadl2_DataSubcomponent, aadl2_ThreadGroupSubcomponent, aadl2_DeviceSubcomponent, aadl2_VirtualBusSubcomponent, aadl2_MemorySubcomponent, aadl2_VirtualProcessorSubcomponent, aadl2_ProcessSubcomponent, aadl2_ProcessorSubcomponent, aadl2_SystemSubcomponent, aadl2_SubprogramCallSequence, BehavioralFeature, Device, aadl2_DeviceClassifier, aadl2_Device, Memory, aadl2_MemoryClassifier, aadl2_Memory, aadl2_BehavioredImplementation, ComponentImplementation, aadl2_CallSpecification, aadl2_Process, Processor, aadl2_ProcessorClassifier, aadl2_Processor, System, aadl2_SystemClassifier, aadl2_System, Thread, aadl2_ThreadClassifier, Process, aadl2_ProcessClassifier, aadl2_ThreadGroup, VirtualBus, aadl2_VirtualBusClassifier, aadl2_VirtualBus, VirtualProcessor, aadl2_VirtualProcessorClassifier, aadl2_VirtualProcessor, BusClassifier, aadl2_Thread, ThreadGroup, aadl2_ThreadGroupClassifier, DeviceClassifier, DataClassifier, MemoryClassifier, ProcessClassifier, ProcessorClassifier, SubprogramClassifier, SubprogramGroupClassifier, SystemClassifier, ThreadClassifier, ThreadGroupClassifier, VirtualBusClassifier, VirtualProcessorClassifier, aadl2_PropertyConstant, aadl2_ComponentPrototypeBinding, PrototypeBinding, aadl2_ComponentPrototypeActual, aadl2_FeatureGroupPrototypeBinding, aadl2_FeatureGroupPrototypeActual, aadl2_FeaturePrototype, aadl2_FeatureGroupPrototype, aadl2_FeaturePrototypeBinding, aadl2_FeaturePrototypeActual, aadl2_AccessSpecification, FeaturePrototypeActual, aadl2_PortSpecification, aadl2_FeaturePrototypeReference, aadl2_ComponentPrototypeReference, ComponentPrototypeActual, aadl2_ComponentReference, aadl2_BasicPropertyAssociation, aadl2_FeatureGroupPrototypeReference, FeatureGroupPrototypeActual, aadl2_FeatureGroupReference, aadl2_ProcessorCall, CallSpecification, aadl2_SubprogramCall, aadl2_StringLiteral, aadl2_EnumerationValue, PropertyValue, aadl2_EnumerationLiteral, aadl2_PropertyValue, PropertyExpression, aadl2_UnitValue, aadl2_UnitLiteral, EnumerationLiteral, aadl2_NumberValue, aadl2_RealLiteral, aadl2_ClassifierValue, aadl2_ReferenceValue, ContainedNamedElement, aadl2_BooleanLiteral, aadl2_RangeValue, aadl2_IntegerLiteral, NumberValue, aadl2_RecordValue, aadl2_ConstantValue, aadl2_PropertyReference, aadl2_Operation, aadl2_NumberType, aadl2_UnitsType, aadl2_ComputedValue, aadl2_ListValue, aadl2_GlobalNamespace, aadl2_AadlBoolean, PropertyType, aadl2_AadlString, aadl2_AadlInteger, NumberType, aadl2_AadlReal, aadl2_NumericRange, EnumerationType, aadl2_EnumerationType, aadl2_ClassifierType, aadl2_RangeType, aadl2_RecordType, aadl2_RecordField, aadl2_ReferenceType, DirectionType, PortCategory, FlowKind, AccessType, AccessCategory, ComponentCategory, ConnectionKind, OperationKind},
    associations={ownedElement1, owner3, ownedComment5, ownedMember6, member7, property11, appliesTo13, inBinding15, ownedValue17, defaultValue19, namespace8, ownedPropertyAssociation9, ownedType28, type29, appliesToMetaclass21, appliesToClassifier23, appliesTo26, classifierFeature30, inheritedMember31, generalization34, ownedPrototypeBinding42, featuringClassifier44, general36, general45, ownedAnnexSubclause38, ownedPrototype40, source49, target51, relatedElement54, specific47, inMode56, refinementContext60, refinedElement63, formal65, containmentPathElement68, refined58, ownedValue75, size78, arraySpecification79, arrayRange70, namedElement72, implementation81, ownedPrototypeBinding82, ownedSubcomponent87, extended90, type85, ownedExtension96, ownedRealization98, ownedEndToEndFlow100, ownedFlowImplementation92, ownedConnection94, ownedParameterConnection106, ownedPortConnection108, ownedFeatureConnection110, ownedAbstractSubcomponent102, ownedAccessConnection104, ownedMode116, ownedModeTransition118, ownedProcessorPort120, ownedInternalEvent122, ownedFeatureGroupConnection112, ownedProcessorSubprogram114, trigger130, ownedTrigger132, context134, port136, source124, destination127, classifier140, refined144, prototype138, extended150, ownedFlowSpecification152, ownedExtension154, ownedFeatureGroup156, ownedAbstractFeature158, refined161, inFeature163, inContext166, outFeature169, ownedFeature146, extended175, featureGroupType178, ownedDataPort195, ownedEventDataPort197, ownedEventPort199, ownedFeatureGroup201, outContext172, ownedFeature180, extended184, inverse187, ownedExtension189, ownedBusAccess191, ownedDataAccess193, extended213, busClassifier216, ownedParameter204, ownedSubprogramAccess206, ownedSubprogramGroupAccess208, ownedAbstractFeature210, dataClassifier223, dataClassifier226, subprogramClassifier229, dataClassifier218, dataClassifier220, prototype242, modeBinding244, implementationReference246, refined250, abstractClassifier252, subprogramGroupClassifier231, componentClassifier233, classifier236, ownedPrototypeBinding239, specification263, flowElement266, constrainingClassifier254, parentMode257, derivedMode260, sourceContext289, refined293, extended295, ownedSubcomponentFlow268, implemented298, inTransition270, context272, flowSpecification275, dataAccess278, destination281, source283, destinationContext286, refined302, flowElement304, ownedSubcomponentFlow306, ownedPackageRename310, ownedComponentTypeRename311, ownedClassifier313, privateSection309, ownedBusType326, ownedBusImplementation328, ownedDataType330, ownedDataImplementation332, ownedDeviceType334, ownedFeatureGroupTypeRename316, ownedAnnexLibrary318, importedPackage320, ownedAbstractType322, ownedAbstractImplementation324, ownedProcessorType344, ownedProcessImplementation346, ownedProcessorImplementation348, ownedDeviceImplementation336, ownedMemoryType338, ownedMemoryImplementation340, ownedSystemImplementation360, ownedProcessType342, ownedThreadType362, ownedThreadImplementation364, ownedThreadGroupType366, ownedSubprogramType350, ownedSubprogramImplementation352, ownedThreadGroupImplementation368, ownedSubprogramGroupType354, ownedSubprogramGroupImplementation356, ownedSystemType358, ownedVirtualProcessorImplementation376, ownedFeatureGroupType378, importedPropertySet381, ownedVirtualBusType370, ownedVirtualBusImplementation372, ownedVirtualProcessorType374, renamedComponentType397, renamedFeatureGroupType400, ownedBusAccess403, renamedPackage383, ownedPublicSection386, ownedPrivateSection388, publicSection390, privateSection393, publicSection396, ownedBusSubcomponent424, ownedDataAccess406, ownedSubprogramAccess409, ownedDataPort412, ownedEventPort415, ownedEventDataPort418, ownedSubprogramGroupAccess421, ownedSystemSubcomponent436, ownedSubprogramSubcomponent438, ownedSubprogramGroupSubcomponent440, ownedThreadSubcomponent442, ownedDataSubcomponent426, ownedThreadGroupSubcomponent444, ownedDeviceSubcomponent428, ownedVirtualBusSubcomponent446, ownedMemorySubcomponent430, ownedProcessSubcomponent432, ownedProcessorSubcomponent434, callSpecification450, ownedSubprogramCallSequence451, ownedCallSpecification453, busClassifier456, dataClassifier459, deviceClassifier462, ownedVirtualProcessorSubcomponent448, memoryClassifier464, processorClassifier468, systemClassifier470, subprogramClassifier472, subprogramGroupClassifier475, threadClassifier478, processClassifier466, virtualBusClassifier482, virtualProcessorClassifier484, ownedBusAccess486, ownedVirtualBusSubcomponent489, threadGroupClassifier480, ownedSubprogramGroupAccess495, ownedDataSubcomponent498, ownedSubprogramSubcomponent501, ownedDataPort504, ownedEventDataPort507, ownedEventPort510, ownedSubprogramAccess516, ownedDataPort537, ownedSubprogramAccess492, ownedSubprogramGroupAccess519, ownedBusSubcomponent522, ownedDataSubcomponent525, ownedBusAccess528, ownedBusSubcomponent531, ownedMemorySubcomponent534, ownedBusAccess513, ownedBusAccess564, ownedEventDataPort540, ownedEventPort543, ownedDataAccess546, ownedSubprogramAccess549, ownedSubprogramGroupAccess552, ownedDataPort555, ownedEventDataPort558, ownedEventPort561, ownedSubprogramGroupSubcomponent579, ownedSubprogramAccess567, ownedSubprogramGroupAccess570, ownedDataSubcomponent573, ownedSubprogramSubcomponent576, ownedEventPort603, ownedThreadSubcomponent582, ownedThreadGroupSubcomponent585, ownedBusSubcomponent588, ownedMemorySubcomponent591, ownedVirtualBusSubcomponent594, ownedVirtualProcessorSubcomponent597, ownedEventDataPort600, ownedParameter606, ownedDataAccess609, ownedSubprogramAccess612, ownedSubprogramGroupAccess615, ownedDataSubcomponent618, ownedSubprogramAccess621, ownedSubprogramGroupAccess624, ownedEventDataPort651, ownedSubprogramSubcomponent627, ownedSubprogramGroupSubcomponent630, ownedBusAccess633, ownedDataAccess636, ownedDataPort639, ownedSubprogramGroupAccess642, ownedSubprogramAccess645, ownedEventPort648, ownedProcessorSubcomponent669, ownedBusSubcomponent654, ownedDataSubcomponent657, ownedDeviceSubcomponent660, ownedMemorySubcomponent663, ownedProcessSubcomponent666, ownedDataPort687, ownedEventDataPort690, ownedSubprogramSubcomponent672, ownedSubprogramGroupSubcomponent675, ownedSystemSubcomponent678, ownedVirtualBusSubcomponent681, ownedVirtualProcessorSubcomponent684, ownedDataSubcomponent711, ownedEventPort693, ownedDataAccess696, ownedSubprogramAccess699, ownedSubprogramGroupAccess702, ownedSubprogramGroupSubcomponent705, ownedSubprogramSubcomponent708, ownedSubprogramAccess726, ownedDataPort714, ownedEventDataPort717, ownedEventPort720, ownedDataAccess723, ownedSubprogramGroupSubcomponent744, ownedSubprogramGroupAccess729, ownedDataSubcomponent732, ownedThreadSubcomponent735, ownedThreadGroupSubcomponent738, ownedSubprogramSubcomponent741, ownedEventPort756, ownedSubprogramAccess759, ownedVirtualBusSubcomponent747, ownedDataPort750, ownedEventDataPort753, ownedPropertyType771, ownedSubprogramGroupAccess762, ownedProperty774, ownedPropertyConstant777, ownedVirtualBusSubcomponent765, ownedVirtualProcessorSubcomponent768, importedPackage782, ownedType785, constantValue788, actual791, importedPropertySet780, constrainingFeatureGroupType792, actual794, actual797, classifier798, constrainingClassifier795, classifier800, prototype802, prototype804, classifier808, prototype811, binding813, featureGroupType815, calledSubprogram818, prototype819, binding806, context822, unit836, property824, ownedValue826, literal829, literal830, baseUnit832, factor834, classifier839, minimum841, maximum843, delta846, constant849, property851, ownedPropertyExpression853, ownedFieldValue855, ownedUnitsType864, ownedListElement857, package859, propertySet861, lowerBound875, unitsType865, range868, ownedLiteral870, upperBound872, namedElementReference887, classifierReference878, ownedNumberType880, numberType882, ownedField885},
    generalizations={gen_aadl2_Namespace_NamedElement, gen_aadl2_Comment_Element, gen_aadl2_NamedElement_Element, gen_aadl2_Property_BasicProperty, gen_aadl2_PropertyAssociation_Element, gen_aadl2_BasicProperty_TypedElement, gen_aadl2_TypedElement_NamedElement, gen_aadl2_PropertyType_Type, gen_aadl2_PropertyExpression_Element, gen_aadl2_MetaclassReference_PropertyOwner, gen_aadl2_PropertyOwner_Element, gen_aadl2_Classifier_Namespace, gen_aadl2_Classifier_Type, gen_aadl2_Type_NamedElement, gen_aadl2_ClassifierFeature_NamedElement, gen_aadl2_Generalization_DirectedRelationship, gen_aadl2_DirectedRelationship_Relationship, gen_aadl2_Relationship_Element, gen_aadl2_Mode_ModeFeature, gen_aadl2_ModeFeature_ClassifierFeature, gen_aadl2_Prototype_StructuralFeature, gen_aadl2_AnnexSubclause_ModalElement, gen_aadl2_ModalElement_NamedElement, gen_aadl2_PrototypeBinding_Element, gen_aadl2_ContainedNamedElement_Element, gen_aadl2_ContainmentPathElement_Element, gen_aadl2_StructuralFeature_RefinableElement, gen_aadl2_StructuralFeature_ClassifierFeature, gen_aadl2_RefinableElement_NamedElement, gen_aadl2_BehavioralFeature_ClassifierFeature, gen_aadl2_ArraySpecification_Element, gen_aadl2_ArraySize_Element, gen_aadl2_ArrayableElement_Element, gen_aadl2_Numeral_ArraySize, gen_aadl2_ArrayRange_Element, gen_aadl2_ModalPropertyValue_ModalElement, gen_aadl2_ComponentImplementation_ComponentClassifier, gen_aadl2_ComponentImplementationReference_Element, gen_aadl2_ComponentClassifier_Classifier, gen_aadl2_ModeTransitionTrigger_Element, gen_aadl2_TriggerPort_ModeTransitionTrigger, gen_aadl2_Context_NamedElement, gen_aadl2_Port_DirectedFeature, gen_aadl2_ModeTransition_ModeFeature, gen_aadl2_FeatureConnectionEnd_ConnectionEnd, gen_aadl2_ConnectionEnd_NamedElement, gen_aadl2_Port_PortConnectionEnd, gen_aadl2_DirectedFeature_Feature, gen_aadl2_Feature_StructuralFeature, gen_aadl2_Feature_FeatureConnectionEnd, gen_aadl2_Feature_ArrayableElement, gen_aadl2_FlowSpecification_Flow, gen_aadl2_FlowSpecification_ModalElement, gen_aadl2_PortConnectionEnd_ConnectionEnd, gen_aadl2_ProcessorPort_PortConnectionEnd, gen_aadl2_ProcessorPort_ModeTransitionTrigger, gen_aadl2_InternalEvent_PortConnectionEnd, gen_aadl2_InternalEvent_ModeTransitionTrigger, gen_aadl2_ComponentType_ComponentClassifier, gen_aadl2_TypeExtension_Generalization, gen_aadl2_FeatureGroup_DirectedFeature, gen_aadl2_FeatureGroup_Context, gen_aadl2_FeatureGroup_FeatureGroupConnectionEnd, gen_aadl2_FeatureGroup_CallContext, gen_aadl2_FeatureGroupConnectionEnd_ConnectionEnd, gen_aadl2_CallContext_Element, gen_aadl2_FeatureGroupType_Classifier, gen_aadl2_Flow_StructuralFeature, gen_aadl2_BusAccess_Access, gen_aadl2_Access_Feature, gen_aadl2_Access_AccessConnectionEnd, gen_aadl2_AccessConnectionEnd_ConnectionEnd, gen_aadl2_GroupExtension_Generalization, gen_aadl2_EventPort_Port, gen_aadl2_Parameter_DirectedFeature, gen_aadl2_Parameter_Context, gen_aadl2_Parameter_ParameterConnectionEnd, gen_aadl2_SubprogramAccess_Access, gen_aadl2_SubprogramAccess_CalledSubprogram, gen_aadl2_CalledSubprogram_Element, gen_aadl2_BusClassifier_ComponentClassifier, gen_aadl2_BusClassifier_Bus, gen_aadl2_Bus_NamedElement, gen_aadl2_DataAccess_Access, gen_aadl2_DataAccess_FlowElement, gen_aadl2_DataAccess_ParameterConnectionEnd, gen_aadl2_DataAccess_PortConnectionEnd, gen_aadl2_ParameterConnectionEnd_ConnectionEnd, gen_aadl2_FlowElement_EndToEndFlowElement, gen_aadl2_EndToEndFlowElement_NamedElement, gen_aadl2_DataClassifier_ComponentClassifier, gen_aadl2_DataClassifier_Data, gen_aadl2_Data_NamedElement, gen_aadl2_DataPort_Port, gen_aadl2_DataPort_Context, gen_aadl2_DataPort_ParameterConnectionEnd, gen_aadl2_EventDataPort_Port, gen_aadl2_EventDataPort_Context, gen_aadl2_EventDataPort_ParameterConnectionEnd, gen_aadl2_SubprogramClassifier_ComponentClassifier, gen_aadl2_SubprogramClassifier_Subprogram, gen_aadl2_Subprogram_NamedElement, gen_aadl2_Subprogram_CalledSubprogram, gen_aadl2_SubprogramGroupAccess_Access, gen_aadl2_SubprogramGroupAccess_CallContext, gen_aadl2_SubprogramGroupClassifier_ComponentClassifier, gen_aadl2_SubprogramGroupClassifier_SubprogramGroup, gen_aadl2_SubprogramGroup_NamedElement, gen_aadl2_AbstractFeature_DirectedFeature, gen_aadl2_Subcomponent_StructuralFeature, gen_aadl2_Subcomponent_ModalElement, gen_aadl2_Subcomponent_Context, gen_aadl2_Subcomponent_FlowElement, gen_aadl2_Subcomponent_ArrayableElement, gen_aadl2_AbstractClassifier_ComponentClassifier, gen_aadl2_AbstractClassifier_Abstract, gen_aadl2_Abstract_NamedElement, gen_aadl2_FlowImplementation_ModalPath, gen_aadl2_FlowImplementation_StructuralFeature, gen_aadl2_ComponentPrototype_Prototype, gen_aadl2_ModeBinding_Element, gen_aadl2_ImplementationExtension_Generalization, gen_aadl2_Realization_Generalization, gen_aadl2_ModalPath_ModalElement, gen_aadl2_SubcomponentFlow_FlowElement, gen_aadl2_Connection_ModalPath, gen_aadl2_Connection_StructuralFeature, gen_aadl2_Connection_FlowElement, gen_aadl2_ParameterConnection_Connection, gen_aadl2_PortConnection_Connection, gen_aadl2_FeatureConnection_Connection, gen_aadl2_EndToEndFlow_Flow, gen_aadl2_EndToEndFlow_ModalPath, gen_aadl2_EndToEndFlow_EndToEndFlowElement, gen_aadl2_AbstractSubcomponent_Subcomponent, gen_aadl2_AbstractSubcomponent_Abstract, gen_aadl2_AccessConnection_Connection, gen_aadl2_FeatureGroupConnection_Connection, gen_aadl2_ProcessorSubprogram_AccessConnectionEnd, gen_aadl2_AnnexLibrary_NamedElement, gen_aadl2_DefaultAnnexLibrary_AnnexLibrary, gen_aadl2_DefaultAnnexSubclause_AnnexSubclause, gen_aadl2_PublicPackageSection_PackageSection, gen_aadl2_PackageSection_Namespace, gen_aadl2_FeatureGroupTypeRename_NamedElement, gen_aadl2_AbstractType_ComponentType, gen_aadl2_AbstractType_AbstractClassifier, gen_aadl2_AbstractType_CallContext, gen_aadl2_PackageRename_NamedElement, gen_aadl2_AadlPackage_NamedElement, gen_aadl2_PrivatePackageSection_PackageSection, gen_aadl2_ComponentTypeRename_NamedElement, gen_aadl2_AbstractImplementation_BehavioredImplementation, gen_aadl2_AbstractImplementation_AbstractClassifier, gen_aadl2_CallSpecification_BehavioralFeature, gen_aadl2_SubprogramCallSequence_ModalElement, gen_aadl2_SubprogramCallSequence_BehavioralFeature, gen_aadl2_BusSubcomponent_Subcomponent, gen_aadl2_BusSubcomponent_AccessConnectionEnd, gen_aadl2_BusSubcomponent_Bus, gen_aadl2_DataSubcomponent_Subcomponent, gen_aadl2_DataSubcomponent_AccessConnectionEnd, gen_aadl2_DataSubcomponent_Data, gen_aadl2_DataSubcomponent_ParameterConnectionEnd, gen_aadl2_DataSubcomponent_PortConnectionEnd, gen_aadl2_DeviceSubcomponent_Subcomponent, gen_aadl2_DeviceSubcomponent_Device, gen_aadl2_Device_NamedElement, gen_aadl2_DeviceClassifier_ComponentClassifier, gen_aadl2_DeviceClassifier_Device, gen_aadl2_MemorySubcomponent_Subcomponent, gen_aadl2_MemorySubcomponent_Memory, gen_aadl2_Memory_NamedElement, gen_aadl2_BehavioredImplementation_ComponentImplementation, gen_aadl2_Process_NamedElement, gen_aadl2_ProcessClassifier_ComponentClassifier, gen_aadl2_ProcessClassifier_Process, gen_aadl2_ProcessorSubcomponent_Subcomponent, gen_aadl2_ProcessorSubcomponent_Processor, gen_aadl2_Processor_NamedElement, gen_aadl2_ProcessorClassifier_ComponentClassifier, gen_aadl2_ProcessorClassifier_Processor, gen_aadl2_SystemSubcomponent_Subcomponent, gen_aadl2_SystemSubcomponent_System, gen_aadl2_System_NamedElement, gen_aadl2_SystemClassifier_ComponentClassifier, gen_aadl2_SystemClassifier_System, gen_aadl2_SubprogramSubcomponent_Subcomponent, gen_aadl2_SubprogramSubcomponent_AccessConnectionEnd, gen_aadl2_SubprogramSubcomponent_Subprogram, gen_aadl2_SubprogramGroupSubcomponent_Subcomponent, gen_aadl2_SubprogramGroupSubcomponent_AccessConnectionEnd, gen_aadl2_SubprogramGroupSubcomponent_SubprogramGroup, gen_aadl2_SubprogramGroupSubcomponent_CallContext, gen_aadl2_ThreadSubcomponent_Subcomponent, gen_aadl2_ThreadSubcomponent_Thread, gen_aadl2_MemoryClassifier_ComponentClassifier, gen_aadl2_MemoryClassifier_Memory, gen_aadl2_ProcessSubcomponent_Subcomponent, gen_aadl2_ProcessSubcomponent_Process, gen_aadl2_ThreadGroup_NamedElement, gen_aadl2_ThreadGroupClassifier_ComponentClassifier, gen_aadl2_ThreadGroupClassifier_ThreadGroup, gen_aadl2_VirtualBusSubcomponent_Subcomponent, gen_aadl2_VirtualBusSubcomponent_VirtualBus, gen_aadl2_VirtualBus_NamedElement, gen_aadl2_VirtualBusClassifier_ComponentClassifier, gen_aadl2_VirtualBusClassifier_VirtualBus, gen_aadl2_VirtualProcessorSubcomponent_Subcomponent, gen_aadl2_VirtualProcessorSubcomponent_VirtualProcessor, gen_aadl2_VirtualProcessor_NamedElement, gen_aadl2_VirtualProcessorClassifier_ComponentClassifier, gen_aadl2_VirtualProcessorClassifier_VirtualProcessor, gen_aadl2_BusType_ComponentType, gen_aadl2_BusType_BusClassifier, gen_aadl2_BusImplementation_ComponentImplementation, gen_aadl2_BusImplementation_BusClassifier, gen_aadl2_Thread_NamedElement, gen_aadl2_ThreadClassifier_ComponentClassifier, gen_aadl2_ThreadClassifier_Thread, gen_aadl2_ThreadGroupSubcomponent_Subcomponent, gen_aadl2_ThreadGroupSubcomponent_ThreadGroup, gen_aadl2_DataImplementation_ComponentImplementation, gen_aadl2_DataImplementation_DataClassifier, gen_aadl2_DeviceType_ComponentType, gen_aadl2_DeviceType_DeviceClassifier, gen_aadl2_DataType_ComponentType, gen_aadl2_DataType_DataClassifier, gen_aadl2_DataType_CallContext, gen_aadl2_DeviceImplementation_ComponentImplementation, gen_aadl2_DeviceImplementation_DeviceClassifier, gen_aadl2_MemoryType_ComponentType, gen_aadl2_MemoryType_MemoryClassifier, gen_aadl2_MemoryImplementation_ComponentImplementation, gen_aadl2_MemoryImplementation_MemoryClassifier, gen_aadl2_ProcessType_ComponentType, gen_aadl2_ProcessType_ProcessClassifier, gen_aadl2_ProcessorType_ComponentType, gen_aadl2_ProcessorType_ProcessorClassifier, gen_aadl2_ProcessImplementation_ComponentImplementation, gen_aadl2_ProcessImplementation_ProcessClassifier, gen_aadl2_ProcessorImplementation_ComponentImplementation, gen_aadl2_ProcessorImplementation_ProcessorClassifier, gen_aadl2_SubprogramType_ComponentType, gen_aadl2_SubprogramType_SubprogramClassifier, gen_aadl2_SubprogramGroupImplementation_ComponentImplementation, gen_aadl2_SubprogramGroupImplementation_SubprogramGroupClassifier, gen_aadl2_SubprogramImplementation_BehavioredImplementation, gen_aadl2_SubprogramImplementation_SubprogramClassifier, gen_aadl2_SubprogramGroupType_ComponentType, gen_aadl2_SubprogramGroupType_SubprogramGroupClassifier, gen_aadl2_SubprogramGroupType_CallContext, gen_aadl2_SystemType_ComponentType, gen_aadl2_SystemType_SystemClassifier, gen_aadl2_SystemImplementation_ComponentImplementation, gen_aadl2_SystemImplementation_SystemClassifier, gen_aadl2_ThreadType_ComponentType, gen_aadl2_ThreadType_ThreadClassifier, gen_aadl2_ThreadGroupType_ComponentType, gen_aadl2_ThreadImplementation_BehavioredImplementation, gen_aadl2_ThreadImplementation_ThreadClassifier, gen_aadl2_ThreadGroupType_ThreadGroupClassifier, gen_aadl2_VirtualBusType_ComponentType, gen_aadl2_VirtualBusType_VirtualBusClassifier, gen_aadl2_VirtualBusImplementation_ComponentImplementation, gen_aadl2_VirtualBusImplementation_VirtualBusClassifier, gen_aadl2_ThreadGroupImplementation_ComponentImplementation, gen_aadl2_ThreadGroupImplementation_ThreadGroupClassifier, gen_aadl2_VirtualProcessorType_ComponentType, gen_aadl2_VirtualProcessorType_VirtualProcessorClassifier, gen_aadl2_PropertySet_Namespace, gen_aadl2_VirtualProcessorImplementation_ComponentImplementation, gen_aadl2_VirtualProcessorImplementation_VirtualProcessorClassifier, gen_aadl2_PropertyConstant_TypedElement, gen_aadl2_ComponentPrototypeBinding_PrototypeBinding, gen_aadl2_ComponentPrototypeActual_Element, gen_aadl2_FeatureGroupPrototypeBinding_PrototypeBinding, gen_aadl2_FeatureGroupPrototypeActual_Element, gen_aadl2_FeaturePrototype_Prototype, gen_aadl2_FeatureGroupPrototype_Prototype, gen_aadl2_FeaturePrototypeBinding_PrototypeBinding, gen_aadl2_FeaturePrototypeActual_Element, gen_aadl2_AccessSpecification_FeaturePrototypeActual, gen_aadl2_PortSpecification_FeaturePrototypeActual, gen_aadl2_FeaturePrototypeReference_FeaturePrototypeActual, gen_aadl2_ComponentPrototypeReference_ComponentPrototypeActual, gen_aadl2_ComponentReference_ComponentPrototypeActual, gen_aadl2_FeatureGroupPrototypeReference_FeatureGroupPrototypeActual, gen_aadl2_FeatureGroupReference_FeatureGroupPrototypeActual, gen_aadl2_ProcessorCall_CallSpecification, gen_aadl2_SubprogramCall_CallSpecification, gen_aadl2_SubprogramCall_Context, gen_aadl2_BasicPropertyAssociation_Element, gen_aadl2_StringLiteral_PropertyValue, gen_aadl2_EnumerationValue_PropertyValue, gen_aadl2_PropertyValue_PropertyExpression, gen_aadl2_EnumerationLiteral_NamedElement, gen_aadl2_UnitValue_PropertyValue, gen_aadl2_UnitLiteral_EnumerationLiteral, gen_aadl2_NumberValue_PropertyValue, gen_aadl2_RealLiteral_NumberValue, gen_aadl2_ClassifierValue_PropertyOwner, gen_aadl2_ClassifierValue_PropertyValue, gen_aadl2_ReferenceValue_ContainedNamedElement, gen_aadl2_ReferenceValue_PropertyValue, gen_aadl2_BooleanLiteral_PropertyValue, gen_aadl2_RangeValue_PropertyValue, gen_aadl2_IntegerLiteral_NumberValue, gen_aadl2_RecordValue_PropertyValue, gen_aadl2_ConstantValue_ArraySize, gen_aadl2_ConstantValue_PropertyValue, gen_aadl2_PropertyReference_ArraySize, gen_aadl2_PropertyReference_PropertyValue, gen_aadl2_Operation_PropertyExpression, gen_aadl2_NumberType_PropertyType, gen_aadl2_ComputedValue_PropertyValue, gen_aadl2_ListValue_PropertyExpression, gen_aadl2_GlobalNamespace_Namespace, gen_aadl2_AadlBoolean_PropertyType, gen_aadl2_AadlString_PropertyType, gen_aadl2_AadlInteger_NumberType, gen_aadl2_AadlReal_NumberType, gen_aadl2_UnitsType_EnumerationType, gen_aadl2_EnumerationType_Namespace, gen_aadl2_EnumerationType_PropertyType, gen_aadl2_NumericRange_Element, gen_aadl2_ClassifierType_PropertyType, gen_aadl2_RangeType_PropertyType, gen_aadl2_RecordType_Namespace, gen_aadl2_RecordType_PropertyType, gen_aadl2_RecordField_BasicProperty, gen_aadl2_ReferenceType_PropertyType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)