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
Language: Enumeration = Enumeration(
    name="Language",
    literals={
            EnumerationLiteral(name="C"),
			EnumerationLiteral(name="Other"),
			EnumerationLiteral(name="Java"),
			EnumerationLiteral(name="Cpp")
    }
)

# Classes
libraryElement_AdapterDeclaration = Class(name="libraryElement::AdapterDeclaration")
VarDeclaration = Class(name="VarDeclaration")
libraryElement_AdapterFB = Class(name="libraryElement::AdapterFB")
libraryElement_AdapterFBType = Class(name="libraryElement::AdapterFBType")
libraryElement_Algorithm = Class(name="libraryElement::Algorithm", is_abstract=True)
INamedElement = Class(name="INamedElement")
libraryElement_Application = Class(name="libraryElement::Application")
libraryElement_FBNetwork = Class(name="libraryElement::FBNetwork")
libraryElement_BasicFBType = Class(name="libraryElement::BasicFBType")
FBType = Class(name="FBType")
libraryElement_AdapterTypePaletteEntry = Class(name="libraryElement::AdapterTypePaletteEntry")
libraryElement_AdapterType = Class(name="libraryElement::AdapterType")
DataType = Class(name="DataType")
libraryElement_VarDeclaration = Class(name="libraryElement::VarDeclaration")
libraryElement_CompilerInfo = Class(name="libraryElement::CompilerInfo")
libraryElement_Compiler = Class(name="libraryElement::Compiler")
libraryElement_ECC = Class(name="libraryElement::ECC")
libraryElement_Connection = Class(name="libraryElement::Connection", is_abstract=True)
ConfigurableObject = Class(name="ConfigurableObject")
libraryElement_Device = Class(name="libraryElement::Device")
TypedConfigureableObject = Class(name="TypedConfigureableObject")
PositionableElement = Class(name="PositionableElement")
ColorizableElement = Class(name="ColorizableElement")
IVarElement = Class(name="IVarElement")
libraryElement_Resource = Class(name="libraryElement::Resource")
libraryElement_IInterfaceElement = Class(name="libraryElement::IInterfaceElement", is_abstract=True)
libraryElement_DeviceType = Class(name="libraryElement::DeviceType")
CompilableType = Class(name="CompilableType")
libraryElement_ResourceTypeName = Class(name="libraryElement::ResourceTypeName")
libraryElement_Link = Class(name="libraryElement::Link")
libraryElement_ECState = Class(name="libraryElement::ECState")
libraryElement_ECTransition = Class(name="libraryElement::ECTransition")
libraryElement_ECAction = Class(name="libraryElement::ECAction")
libraryElement_Event = Class(name="libraryElement::Event")
libraryElement_FBNetworkElement = Class(name="libraryElement::FBNetworkElement")
IInterfaceElement = Class(name="IInterfaceElement")
libraryElement_With = Class(name="libraryElement::With")
libraryElement_FB = Class(name="libraryElement::FB")
FBNetworkElement = Class(name="FBNetworkElement")
libraryElement_InterfaceList = Class(name="libraryElement::InterfaceList")
libraryElement_Mapping = Class(name="libraryElement::Mapping")
libraryElement_SubApp = Class(name="libraryElement::SubApp")
libraryElement_FBType = Class(name="libraryElement::FBType")
libraryElement_Identification = Class(name="libraryElement::Identification")
libraryElement_Service = Class(name="libraryElement::Service")
libraryElement_InputPrimitive = Class(name="libraryElement::InputPrimitive")
Primitive = Class(name="Primitive")
libraryElement_Segment = Class(name="libraryElement::Segment")
libraryElement_OtherAlgorithm = Class(name="libraryElement::OtherAlgorithm")
TextAlgorithm = Class(name="TextAlgorithm")
libraryElement_OutputPrimitive = Class(name="libraryElement::OutputPrimitive")
libraryElement_Parameter = Class(name="libraryElement::Parameter")
libraryElement_ResourceType = Class(name="libraryElement::ResourceType")
libraryElement_ServiceSequence = Class(name="libraryElement::ServiceSequence")
libraryElement_ServiceTransaction = Class(name="libraryElement::ServiceTransaction")
libraryElement_ServiceInterfaceFBType = Class(name="libraryElement::ServiceInterfaceFBType")
libraryElement_STAlgorithm = Class(name="libraryElement::STAlgorithm")
libraryElement_AdapterConnection = Class(name="libraryElement::AdapterConnection")
libraryElement_SubAppType = Class(name="libraryElement::SubAppType")
CompositeFBType = Class(name="CompositeFBType")
libraryElement_AutomationSystem = Class(name="libraryElement::AutomationSystem")
LibraryElement = Class(name="LibraryElement")
libraryElement_DataConnection = Class(name="libraryElement::DataConnection")
libraryElement_EventConnection = Class(name="libraryElement::EventConnection")
libraryElement_SystemConfiguration = Class(name="libraryElement::SystemConfiguration")
libraryElement_VarInitialization = Class(name="libraryElement::VarInitialization")
libraryElement_VersionInfo = Class(name="libraryElement::VersionInfo")
libraryElement_Palette = Class(name="libraryElement::Palette")
libraryElement_LibraryElement = Class(name="libraryElement::LibraryElement")
libraryElement_PaletteEntry = Class(name="libraryElement::PaletteEntry")
libraryElement_CompositeFBType = Class(name="libraryElement::CompositeFBType")
libraryElement_TextAlgorithm = Class(name="libraryElement::TextAlgorithm", is_abstract=True)
Algorithm = Class(name="Algorithm")
Connection = Class(name="Connection")
libraryElement_CompilableType = Class(name="libraryElement::CompilableType")
libraryElement_ConfigurableObject = Class(name="libraryElement::ConfigurableObject")
libraryElement_ServiceInterface = Class(name="libraryElement::ServiceInterface")
libraryElement_DataType = Class(name="libraryElement::DataType")
libraryElement_Value = Class(name="libraryElement::Value")
I4DIACElement = Class(name="I4DIACElement")
libraryElement_INamedElement = Class(name="libraryElement::INamedElement", is_abstract=True)
libraryElement_ResourceTypeFB = Class(name="libraryElement::ResourceTypeFB")
FB = Class(name="FB")
libraryElement_I4DIACElement = Class(name="libraryElement::I4DIACElement", is_abstract=True)
libraryElement_Annotation = Class(name="libraryElement::Annotation")
libraryElement_SegmentType = Class(name="libraryElement::SegmentType")
libraryElement_TypedConfigureableObject = Class(name="libraryElement::TypedConfigureableObject")
libraryElement_AdapterEvent = Class(name="libraryElement::AdapterEvent")
Event = Class(name="Event")
libraryElement_PositionableElement = Class(name="libraryElement::PositionableElement")
libraryElement_Color = Class(name="libraryElement::Color")
libraryElement_ColorizableElement = Class(name="libraryElement::ColorizableElement")
libraryElement_IVarElement = Class(name="libraryElement::IVarElement", is_abstract=True)
libraryElement_Primitive = Class(name="libraryElement::Primitive")

# libraryElement_AdapterDeclaration class attributes and methods

# VarDeclaration class attributes and methods

# libraryElement_AdapterFB class attributes and methods
libraryElement_AdapterFB_m_isSocket: Method = Method(name="isSocket", parameters={}, type=StringType)
libraryElement_AdapterFB_m_getType: Method = Method(name="getType", parameters={}, type=FBType)
libraryElement_AdapterFB_m_isPlug: Method = Method(name="isPlug", parameters={}, type=StringType)
libraryElement_AdapterFB.methods={libraryElement_AdapterFB_m_isSocket, libraryElement_AdapterFB_m_isPlug, libraryElement_AdapterFB_m_getType}

# libraryElement_AdapterFBType class attributes and methods

# libraryElement_Algorithm class attributes and methods

# INamedElement class attributes and methods

# libraryElement_Application class attributes and methods
libraryElement_Application_m_getAutomationSystem: Method = Method(name="getAutomationSystem", parameters={}, type=StringType)
libraryElement_Application.methods={libraryElement_Application_m_getAutomationSystem}

# libraryElement_FBNetwork class attributes and methods
libraryElement_FBNetwork_m_addConnection: Method = Method(name="addConnection", parameters={Parameter(name='connection')})
libraryElement_FBNetwork_m_removeConnection: Method = Method(name="removeConnection", parameters={Parameter(name='connection')})
libraryElement_FBNetwork_m_isApplicationNetwork: Method = Method(name="isApplicationNetwork", parameters={}, type=StringType)
libraryElement_FBNetwork_m_getAutomationSystem: Method = Method(name="getAutomationSystem", parameters={}, type=StringType)
libraryElement_FBNetwork_m_getApplication: Method = Method(name="getApplication", parameters={}, type=StringType)
libraryElement_FBNetwork_m_getFBNamed: Method = Method(name="getFBNamed", parameters={Parameter(name='name')}, type=StringType)
libraryElement_FBNetwork_m_getSubAppNamed: Method = Method(name="getSubAppNamed", parameters={Parameter(name='name')}, type=StringType)
libraryElement_FBNetwork_m_getElementNamed: Method = Method(name="getElementNamed", parameters={Parameter(name='name')}, type=FBNetworkElement)
libraryElement_FBNetwork_m_isSubApplicationNetwork: Method = Method(name="isSubApplicationNetwork", parameters={}, type=StringType)
libraryElement_FBNetwork_m_isResourceNetwork: Method = Method(name="isResourceNetwork", parameters={}, type=StringType)
libraryElement_FBNetwork_m_isCFBTypeNetwork: Method = Method(name="isCFBTypeNetwork", parameters={}, type=StringType)
libraryElement_FBNetwork.methods={libraryElement_FBNetwork_m_getSubAppNamed, libraryElement_FBNetwork_m_getFBNamed, libraryElement_FBNetwork_m_isSubApplicationNetwork, libraryElement_FBNetwork_m_addConnection, libraryElement_FBNetwork_m_removeConnection, libraryElement_FBNetwork_m_getAutomationSystem, libraryElement_FBNetwork_m_getElementNamed, libraryElement_FBNetwork_m_isResourceNetwork, libraryElement_FBNetwork_m_isCFBTypeNetwork, libraryElement_FBNetwork_m_getApplication, libraryElement_FBNetwork_m_isApplicationNetwork}

# libraryElement_BasicFBType class attributes and methods

# FBType class attributes and methods

# libraryElement_AdapterTypePaletteEntry class attributes and methods

# libraryElement_AdapterType class attributes and methods
libraryElement_AdapterType_m_getSocketType: Method = Method(name="getSocketType", parameters={}, type=StringType)
libraryElement_AdapterType_m_getInterfaceList: Method = Method(name="getInterfaceList", parameters={}, type=StringType)
libraryElement_AdapterType_m_getPlugType: Method = Method(name="getPlugType", parameters={}, type=StringType)
libraryElement_AdapterType.methods={libraryElement_AdapterType_m_getSocketType, libraryElement_AdapterType_m_getPlugType, libraryElement_AdapterType_m_getInterfaceList}

# DataType class attributes and methods

# libraryElement_VarDeclaration class attributes and methods
libraryElement_VarDeclaration_arraySize: Property = Property(name="arraySize", type=StringType)
libraryElement_VarDeclaration_m_isArray: Method = Method(name="isArray", parameters={}, type=StringType)
libraryElement_VarDeclaration.attributes={libraryElement_VarDeclaration_arraySize}
libraryElement_VarDeclaration.methods={libraryElement_VarDeclaration_m_isArray}

# libraryElement_CompilerInfo class attributes and methods
libraryElement_CompilerInfo_classdef: Property = Property(name="classdef", type=StringType)
libraryElement_CompilerInfo_header: Property = Property(name="header", type=StringType)
libraryElement_CompilerInfo.attributes={libraryElement_CompilerInfo_classdef, libraryElement_CompilerInfo_header}

# libraryElement_Compiler class attributes and methods
libraryElement_Compiler_version: Property = Property(name="version", type=StringType)
libraryElement_Compiler_language: Property = Property(name="language", type=StringType)
libraryElement_Compiler_product: Property = Property(name="product", type=StringType)
libraryElement_Compiler_vendor: Property = Property(name="vendor", type=StringType)
libraryElement_Compiler.attributes={libraryElement_Compiler_vendor, libraryElement_Compiler_version, libraryElement_Compiler_language, libraryElement_Compiler_product}

# libraryElement_ECC class attributes and methods

# libraryElement_Connection class attributes and methods
libraryElement_Connection_dx1: Property = Property(name="dx1", type=StringType)
libraryElement_Connection_dx2: Property = Property(name="dx2", type=StringType)
libraryElement_Connection_dy: Property = Property(name="dy", type=StringType)
libraryElement_Connection_resTypeConnection: Property = Property(name="resTypeConnection", type=StringType)
libraryElement_Connection_brokenConnection: Property = Property(name="brokenConnection", type=StringType)
libraryElement_Connection_m_getSourceElement: Method = Method(name="getSourceElement", parameters={}, type=StringType)
libraryElement_Connection_m_getDestinationElement: Method = Method(name="getDestinationElement", parameters={}, type=StringType)
libraryElement_Connection_m_isResourceConnection: Method = Method(name="isResourceConnection", parameters={}, type=BooleanType)
libraryElement_Connection_m_getFBNetwork: Method = Method(name="getFBNetwork", parameters={}, type=StringType)
libraryElement_Connection_m_checkIfConnectionBroken: Method = Method(name="checkIfConnectionBroken", parameters={})
libraryElement_Connection.attributes={libraryElement_Connection_brokenConnection, libraryElement_Connection_dx1, libraryElement_Connection_resTypeConnection, libraryElement_Connection_dx2, libraryElement_Connection_dy}
libraryElement_Connection.methods={libraryElement_Connection_m_getDestinationElement, libraryElement_Connection_m_getFBNetwork, libraryElement_Connection_m_isResourceConnection, libraryElement_Connection_m_getSourceElement, libraryElement_Connection_m_checkIfConnectionBroken}

# ConfigurableObject class attributes and methods

# libraryElement_Device class attributes and methods
libraryElement_Device_profile: Property = Property(name="profile", type=StringType)
libraryElement_Device_m_getAutomationSystem: Method = Method(name="getAutomationSystem", parameters={}, type=StringType)
libraryElement_Device_m_getSystemConfiguration: Method = Method(name="getSystemConfiguration", parameters={}, type=StringType)
libraryElement_Device_m_getType: Method = Method(name="getType", parameters={}, type=StringType)
libraryElement_Device_m_getResourceNamed: Method = Method(name="getResourceNamed", parameters={Parameter(name='name')}, type=StringType)
libraryElement_Device.attributes={libraryElement_Device_profile}
libraryElement_Device.methods={libraryElement_Device_m_getSystemConfiguration, libraryElement_Device_m_getResourceNamed, libraryElement_Device_m_getAutomationSystem, libraryElement_Device_m_getType}

# TypedConfigureableObject class attributes and methods

# PositionableElement class attributes and methods

# ColorizableElement class attributes and methods

# IVarElement class attributes and methods

# libraryElement_Resource class attributes and methods
libraryElement_Resource_x: Property = Property(name="x", type=StringType)
libraryElement_Resource_deviceTypeResource: Property = Property(name="deviceTypeResource", type=StringType)
libraryElement_Resource_y: Property = Property(name="y", type=StringType)
libraryElement_Resource_m_getAutomationSystem: Method = Method(name="getAutomationSystem", parameters={}, type=StringType)
libraryElement_Resource.attributes={libraryElement_Resource_x, libraryElement_Resource_y, libraryElement_Resource_deviceTypeResource}
libraryElement_Resource.methods={libraryElement_Resource_m_getAutomationSystem}

# libraryElement_IInterfaceElement class attributes and methods
libraryElement_IInterfaceElement_isInput: Property = Property(name="isInput", type=StringType)
libraryElement_IInterfaceElement_typeName: Property = Property(name="typeName", type=StringType)
libraryElement_IInterfaceElement_m_getFBNetworkElement: Method = Method(name="getFBNetworkElement", parameters={}, type=FBNetworkElement)
libraryElement_IInterfaceElement.attributes={libraryElement_IInterfaceElement_typeName, libraryElement_IInterfaceElement_isInput}
libraryElement_IInterfaceElement.methods={libraryElement_IInterfaceElement_m_getFBNetworkElement}

# libraryElement_DeviceType class attributes and methods
libraryElement_DeviceType_profile: Property = Property(name="profile", type=StringType)
libraryElement_DeviceType.attributes={libraryElement_DeviceType_profile}

# CompilableType class attributes and methods

# libraryElement_ResourceTypeName class attributes and methods
libraryElement_ResourceTypeName_name: Property = Property(name="name", type=StringType)
libraryElement_ResourceTypeName.attributes={libraryElement_ResourceTypeName_name}

# libraryElement_Link class attributes and methods

# libraryElement_ECState class attributes and methods
libraryElement_ECState_m_isStartState: Method = Method(name="isStartState", parameters={}, type=StringType)
libraryElement_ECState.methods={libraryElement_ECState_m_isStartState}

# libraryElement_ECTransition class attributes and methods
libraryElement_ECTransition_comment: Property = Property(name="comment", type=StringType)
libraryElement_ECTransition_conditionExpression: Property = Property(name="conditionExpression", type=StringType)
libraryElement_ECTransition_m_getConditionText: Method = Method(name="getConditionText", parameters={}, type=StringType)
libraryElement_ECTransition.attributes={libraryElement_ECTransition_comment, libraryElement_ECTransition_conditionExpression}
libraryElement_ECTransition.methods={libraryElement_ECTransition_m_getConditionText}

# libraryElement_ECAction class attributes and methods

# libraryElement_Event class attributes and methods

# libraryElement_FBNetworkElement class attributes and methods
libraryElement_FBNetworkElement_m_getResource: Method = Method(name="getResource", parameters={}, type=StringType)
libraryElement_FBNetworkElement_m_getInterfaceElement: Method = Method(name="getInterfaceElement", parameters={Parameter(name='name')}, type=IInterfaceElement)
libraryElement_FBNetworkElement_m_getOpposite: Method = Method(name="getOpposite", parameters={}, type=FBNetworkElement)
libraryElement_FBNetworkElement_m_isMapped: Method = Method(name="isMapped", parameters={}, type=BooleanType)
libraryElement_FBNetworkElement_m_getFbNetwork: Method = Method(name="getFbNetwork", parameters={}, type=StringType)
libraryElement_FBNetworkElement_m_checkConnections: Method = Method(name="checkConnections", parameters={})
libraryElement_FBNetworkElement.methods={libraryElement_FBNetworkElement_m_checkConnections, libraryElement_FBNetworkElement_m_getOpposite, libraryElement_FBNetworkElement_m_getInterfaceElement, libraryElement_FBNetworkElement_m_getResource, libraryElement_FBNetworkElement_m_isMapped, libraryElement_FBNetworkElement_m_getFbNetwork}

# IInterfaceElement class attributes and methods

# libraryElement_With class attributes and methods

# libraryElement_FB class attributes and methods
libraryElement_FB_m_getType: Method = Method(name="getType", parameters={}, type=FBType)
libraryElement_FB_m_isResourceFB: Method = Method(name="isResourceFB", parameters={}, type=BooleanType)
libraryElement_FB_m_isResourceTypeFB: Method = Method(name="isResourceTypeFB", parameters={}, type=BooleanType)
libraryElement_FB.methods={libraryElement_FB_m_getType, libraryElement_FB_m_isResourceTypeFB, libraryElement_FB_m_isResourceFB}

# FBNetworkElement class attributes and methods

# libraryElement_InterfaceList class attributes and methods
libraryElement_InterfaceList_m_getAllInterfaceElements: Method = Method(name="getAllInterfaceElements", parameters={})
libraryElement_InterfaceList_m_getEvent: Method = Method(name="getEvent", parameters={Parameter(name='name')}, type=StringType)
libraryElement_InterfaceList_m_getVariable: Method = Method(name="getVariable", parameters={Parameter(name='name')}, type=VarDeclaration)
libraryElement_InterfaceList_m_getInterfaceElement: Method = Method(name="getInterfaceElement", parameters={Parameter(name='name')}, type=IInterfaceElement)
libraryElement_InterfaceList_m_getFBNetworkElement: Method = Method(name="getFBNetworkElement", parameters={}, type=FBNetworkElement)
libraryElement_InterfaceList.methods={libraryElement_InterfaceList_m_getAllInterfaceElements, libraryElement_InterfaceList_m_getInterfaceElement, libraryElement_InterfaceList_m_getVariable, libraryElement_InterfaceList_m_getFBNetworkElement, libraryElement_InterfaceList_m_getEvent}

# libraryElement_Mapping class attributes and methods
libraryElement_Mapping_m_getAutomationSystem: Method = Method(name="getAutomationSystem", parameters={}, type=StringType)
libraryElement_Mapping.methods={libraryElement_Mapping_m_getAutomationSystem}

# libraryElement_SubApp class attributes and methods
libraryElement_SubApp_m_getType: Method = Method(name="getType", parameters={}, type=StringType)
libraryElement_SubApp.methods={libraryElement_SubApp_m_getType}

# libraryElement_FBType class attributes and methods

# libraryElement_Identification class attributes and methods
libraryElement_Identification_applicationDomain: Property = Property(name="applicationDomain", type=StringType)
libraryElement_Identification_classification: Property = Property(name="classification", type=StringType)
libraryElement_Identification_description: Property = Property(name="description", type=StringType)
libraryElement_Identification_function: Property = Property(name="function", type=StringType)
libraryElement_Identification_standard: Property = Property(name="standard", type=StringType)
libraryElement_Identification_type: Property = Property(name="type", type=StringType)
libraryElement_Identification.attributes={libraryElement_Identification_function, libraryElement_Identification_type, libraryElement_Identification_description, libraryElement_Identification_applicationDomain, libraryElement_Identification_standard, libraryElement_Identification_classification}

# libraryElement_Service class attributes and methods

# libraryElement_InputPrimitive class attributes and methods

# Primitive class attributes and methods

# libraryElement_Segment class attributes and methods
libraryElement_Segment_width: Property = Property(name="width", type=StringType)
libraryElement_Segment.attributes={libraryElement_Segment_width}

# libraryElement_OtherAlgorithm class attributes and methods
libraryElement_OtherAlgorithm_language: Property = Property(name="language", type=StringType)
libraryElement_OtherAlgorithm.attributes={libraryElement_OtherAlgorithm_language}

# TextAlgorithm class attributes and methods

# libraryElement_OutputPrimitive class attributes and methods
libraryElement_OutputPrimitive_TestResult: Property = Property(name="TestResult", type=StringType)
libraryElement_OutputPrimitive.attributes={libraryElement_OutputPrimitive_TestResult}

# libraryElement_Parameter class attributes and methods
libraryElement_Parameter_name: Property = Property(name="name", type=StringType)
libraryElement_Parameter_value: Property = Property(name="value", type=StringType)
libraryElement_Parameter_comment: Property = Property(name="comment", type=StringType)
libraryElement_Parameter.attributes={libraryElement_Parameter_value, libraryElement_Parameter_name, libraryElement_Parameter_comment}

# libraryElement_ResourceType class attributes and methods

# libraryElement_ServiceSequence class attributes and methods
libraryElement_ServiceSequence_TestResult: Property = Property(name="TestResult", type=StringType)
libraryElement_ServiceSequence.attributes={libraryElement_ServiceSequence_TestResult}

# libraryElement_ServiceTransaction class attributes and methods
libraryElement_ServiceTransaction_TestResult: Property = Property(name="TestResult", type=StringType)
libraryElement_ServiceTransaction.attributes={libraryElement_ServiceTransaction_TestResult}

# libraryElement_ServiceInterfaceFBType class attributes and methods

# libraryElement_STAlgorithm class attributes and methods

# libraryElement_AdapterConnection class attributes and methods
libraryElement_AdapterConnection_m_getDestination: Method = Method(name="getDestination", parameters={}, type=StringType)
libraryElement_AdapterConnection_m_getSource: Method = Method(name="getSource", parameters={}, type=StringType)
libraryElement_AdapterConnection.methods={libraryElement_AdapterConnection_m_getSource, libraryElement_AdapterConnection_m_getDestination}

# libraryElement_SubAppType class attributes and methods

# CompositeFBType class attributes and methods

# libraryElement_AutomationSystem class attributes and methods
libraryElement_AutomationSystem_project: Property = Property(name="project", type=StringType)
libraryElement_AutomationSystem_m_getDeviceNamed: Method = Method(name="getDeviceNamed", parameters={Parameter(name='name')}, type=StringType)
libraryElement_AutomationSystem_m_getApplicationNamed: Method = Method(name="getApplicationNamed", parameters={Parameter(name='name')}, type=StringType)
libraryElement_AutomationSystem.attributes={libraryElement_AutomationSystem_project}
libraryElement_AutomationSystem.methods={libraryElement_AutomationSystem_m_getApplicationNamed, libraryElement_AutomationSystem_m_getDeviceNamed}

# LibraryElement class attributes and methods

# libraryElement_DataConnection class attributes and methods
libraryElement_DataConnection_m_getSource: Method = Method(name="getSource", parameters={}, type=VarDeclaration)
libraryElement_DataConnection_m_getDestination: Method = Method(name="getDestination", parameters={}, type=VarDeclaration)
libraryElement_DataConnection.methods={libraryElement_DataConnection_m_getDestination, libraryElement_DataConnection_m_getSource}

# libraryElement_EventConnection class attributes and methods
libraryElement_EventConnection_m_getSource: Method = Method(name="getSource", parameters={}, type=StringType)
libraryElement_EventConnection_m_getDestination: Method = Method(name="getDestination", parameters={}, type=StringType)
libraryElement_EventConnection.methods={libraryElement_EventConnection_m_getSource, libraryElement_EventConnection_m_getDestination}

# libraryElement_SystemConfiguration class attributes and methods
libraryElement_SystemConfiguration_m_getAutomationSystem: Method = Method(name="getAutomationSystem", parameters={}, type=StringType)
libraryElement_SystemConfiguration_m_getSegmentNamed: Method = Method(name="getSegmentNamed", parameters={Parameter(name='name')}, type=StringType)
libraryElement_SystemConfiguration_m_getDeviceNamed: Method = Method(name="getDeviceNamed", parameters={Parameter(name='name')}, type=StringType)
libraryElement_SystemConfiguration.methods={libraryElement_SystemConfiguration_m_getAutomationSystem, libraryElement_SystemConfiguration_m_getSegmentNamed, libraryElement_SystemConfiguration_m_getDeviceNamed}

# libraryElement_VarInitialization class attributes and methods

# libraryElement_VersionInfo class attributes and methods
libraryElement_VersionInfo_author: Property = Property(name="author", type=StringType)
libraryElement_VersionInfo_remarks: Property = Property(name="remarks", type=StringType)
libraryElement_VersionInfo_version: Property = Property(name="version", type=StringType)
libraryElement_VersionInfo_date: Property = Property(name="date", type=StringType)
libraryElement_VersionInfo_organization: Property = Property(name="organization", type=StringType)
libraryElement_VersionInfo.attributes={libraryElement_VersionInfo_date, libraryElement_VersionInfo_remarks, libraryElement_VersionInfo_author, libraryElement_VersionInfo_organization, libraryElement_VersionInfo_version}

# libraryElement_Palette class attributes and methods

# libraryElement_LibraryElement class attributes and methods

# libraryElement_PaletteEntry class attributes and methods

# libraryElement_CompositeFBType class attributes and methods

# libraryElement_TextAlgorithm class attributes and methods
libraryElement_TextAlgorithm_text: Property = Property(name="text", type=StringType)
libraryElement_TextAlgorithm.attributes={libraryElement_TextAlgorithm_text}

# Algorithm class attributes and methods

# Connection class attributes and methods

# libraryElement_CompilableType class attributes and methods

# libraryElement_ConfigurableObject class attributes and methods
libraryElement_ConfigurableObject_m_getParameter: Method = Method(name="getParameter", parameters={Parameter(name='parameterName')}, type=StringType)
libraryElement_ConfigurableObject_m_setParameter: Method = Method(name="setParameter", parameters={Parameter(name='parameterName'), Parameter(name='value')})
libraryElement_ConfigurableObject.methods={libraryElement_ConfigurableObject_m_getParameter, libraryElement_ConfigurableObject_m_setParameter}

# libraryElement_ServiceInterface class attributes and methods

# libraryElement_DataType class attributes and methods

# libraryElement_Value class attributes and methods
libraryElement_Value_value: Property = Property(name="value", type=StringType)
libraryElement_Value_m_getVarDeclaration: Method = Method(name="getVarDeclaration", parameters={}, type=VarDeclaration)
libraryElement_Value.attributes={libraryElement_Value_value}
libraryElement_Value.methods={libraryElement_Value_m_getVarDeclaration}

# I4DIACElement class attributes and methods

# libraryElement_INamedElement class attributes and methods
libraryElement_INamedElement_name: Property = Property(name="name", type=StringType)
libraryElement_INamedElement_comment: Property = Property(name="comment", type=StringType)
libraryElement_INamedElement.attributes={libraryElement_INamedElement_comment, libraryElement_INamedElement_name}

# libraryElement_ResourceTypeFB class attributes and methods
libraryElement_ResourceTypeFB_m_isResourceTypeFB: Method = Method(name="isResourceTypeFB", parameters={}, type=BooleanType)
libraryElement_ResourceTypeFB.methods={libraryElement_ResourceTypeFB_m_isResourceTypeFB}

# FB class attributes and methods

# libraryElement_I4DIACElement class attributes and methods
libraryElement_I4DIACElement_m_createAnnotation: Method = Method(name="createAnnotation", parameters={Parameter(name='name')}, type=StringType)
libraryElement_I4DIACElement_m_removeAnnotation: Method = Method(name="removeAnnotation", parameters={Parameter(name='annotation')})
libraryElement_I4DIACElement.methods={libraryElement_I4DIACElement_m_createAnnotation, libraryElement_I4DIACElement_m_removeAnnotation}

# libraryElement_Annotation class attributes and methods
libraryElement_Annotation_name: Property = Property(name="name", type=StringType)
libraryElement_Annotation_servity: Property = Property(name="servity", type=StringType)
libraryElement_Annotation.attributes={libraryElement_Annotation_servity, libraryElement_Annotation_name}

# libraryElement_SegmentType class attributes and methods

# libraryElement_TypedConfigureableObject class attributes and methods
libraryElement_TypedConfigureableObject_m_getTypeName: Method = Method(name="getTypeName", parameters={}, type=StringType)
libraryElement_TypedConfigureableObject_m_getType: Method = Method(name="getType", parameters={}, type=LibraryElement)
libraryElement_TypedConfigureableObject.methods={libraryElement_TypedConfigureableObject_m_getType, libraryElement_TypedConfigureableObject_m_getTypeName}

# libraryElement_AdapterEvent class attributes and methods

# Event class attributes and methods

# libraryElement_PositionableElement class attributes and methods
libraryElement_PositionableElement_x: Property = Property(name="x", type=StringType)
libraryElement_PositionableElement_y: Property = Property(name="y", type=StringType)
libraryElement_PositionableElement.attributes={libraryElement_PositionableElement_y, libraryElement_PositionableElement_x}

# libraryElement_Color class attributes and methods
libraryElement_Color_red: Property = Property(name="red", type=StringType)
libraryElement_Color_green: Property = Property(name="green", type=StringType)
libraryElement_Color_blue: Property = Property(name="blue", type=StringType)
libraryElement_Color.attributes={libraryElement_Color_blue, libraryElement_Color_red, libraryElement_Color_green}

# libraryElement_ColorizableElement class attributes and methods

# libraryElement_IVarElement class attributes and methods

# libraryElement_Primitive class attributes and methods
libraryElement_Primitive_event: Property = Property(name="event", type=StringType)
libraryElement_Primitive_parameters: Property = Property(name="parameters", type=StringType)
libraryElement_Primitive.attributes={libraryElement_Primitive_parameters, libraryElement_Primitive_event}

# Relationships
adapterFB0: BinaryAssociation = BinaryAssociation(
    name="adapterFB0",
    ends={
        Property(name="AdapterFB", type=libraryElement_AdapterDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adapterDecl", type=libraryElement_AdapterFB, multiplicity=Multiplicity(0, 1))
    }
)
adapterFBType2: BinaryAssociation = BinaryAssociation(
    name="adapterFBType2",
    ends={
        Property(name="libraryElement_AdapterFBType", type=libraryElement_AdapterType, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_AdapterType", type=libraryElement_AdapterFBType, multiplicity=Multiplicity(0, 1))
    }
)
fBNetwork3: BinaryAssociation = BinaryAssociation(
    name="fBNetwork3",
    ends={
        Property(name="libraryElement_FBNetwork", type=libraryElement_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_Application", type=libraryElement_FBNetwork, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
paletteEntry1: BinaryAssociation = BinaryAssociation(
    name="paletteEntry1",
    ends={
        Property(name="libraryElement_AdapterTypePaletteEntry", type=libraryElement_AdapterDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_AdapterDeclaration", type=libraryElement_AdapterTypePaletteEntry, multiplicity=Multiplicity(0, 1))
    }
)
internalVars7: BinaryAssociation = BinaryAssociation(
    name="internalVars7",
    ends={
        Property(name="libraryElement_VarDeclaration", type=libraryElement_BasicFBType, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_BasicFBType8", type=libraryElement_VarDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compiler9: BinaryAssociation = BinaryAssociation(
    name="compiler9",
    ends={
        Property(name="libraryElement_Compiler", type=libraryElement_CompilerInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_CompilerInfo", type=libraryElement_Compiler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eCC4: BinaryAssociation = BinaryAssociation(
    name="eCC4",
    ends={
        Property(name="libraryElement_ECC", type=libraryElement_BasicFBType, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_BasicFBType", type=libraryElement_ECC, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
algorithm5: BinaryAssociation = BinaryAssociation(
    name="algorithm5",
    ends={
        Property(name="libraryElement_Algorithm", type=libraryElement_BasicFBType, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_BasicFBType6", type=libraryElement_Algorithm, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
destination11: BinaryAssociation = BinaryAssociation(
    name="destination11",
    ends={
        Property(name="IInterfaceElement12", type=libraryElement_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="inputConnections", type=libraryElement_IInterfaceElement, multiplicity=Multiplicity(0, 1))
    }
)
resource13: BinaryAssociation = BinaryAssociation(
    name="resource13",
    ends={
        Property(name="Resource", type=libraryElement_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="device", type=libraryElement_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="IInterfaceElement", type=libraryElement_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="outputConnections", type=libraryElement_IInterfaceElement, multiplicity=Multiplicity(0, 1))
    }
)
varDeclaration16: BinaryAssociation = BinaryAssociation(
    name="varDeclaration16",
    ends={
        Property(name="libraryElement_VarDeclaration17", type=libraryElement_DeviceType, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_DeviceType", type=libraryElement_VarDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceTypeName18: BinaryAssociation = BinaryAssociation(
    name="resourceTypeName18",
    ends={
        Property(name="libraryElement_ResourceTypeName", type=libraryElement_DeviceType, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_DeviceType19", type=libraryElement_ResourceTypeName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resource20: BinaryAssociation = BinaryAssociation(
    name="resource20",
    ends={
        Property(name="libraryElement_Resource", type=libraryElement_DeviceType, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_DeviceType21", type=libraryElement_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fBNetwork22: BinaryAssociation = BinaryAssociation(
    name="fBNetwork22",
    ends={
        Property(name="libraryElement_FBNetwork24", type=libraryElement_DeviceType, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_DeviceType23", type=libraryElement_FBNetwork, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inConnections14: BinaryAssociation = BinaryAssociation(
    name="inConnections14",
    ends={
        Property(name="Link", type=libraryElement_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="device15", type=libraryElement_Link, multiplicity=Multiplicity(0, 9999))
    }
)
eCState29: BinaryAssociation = BinaryAssociation(
    name="eCState29",
    ends={
        Property(name="libraryElement_ECState", type=libraryElement_ECC, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_ECC30", type=libraryElement_ECState, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
eCTransition31: BinaryAssociation = BinaryAssociation(
    name="eCTransition31",
    ends={
        Property(name="libraryElement_ECTransition", type=libraryElement_ECC, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_ECC32", type=libraryElement_ECTransition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
start33: BinaryAssociation = BinaryAssociation(
    name="start33",
    ends={
        Property(name="libraryElement_ECState35", type=libraryElement_ECC, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_ECC34", type=libraryElement_ECState, multiplicity=Multiplicity(0, 1))
    }
)
algorithm25: BinaryAssociation = BinaryAssociation(
    name="algorithm25",
    ends={
        Property(name="libraryElement_Algorithm26", type=libraryElement_ECAction, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_ECAction", type=libraryElement_Algorithm, multiplicity=Multiplicity(0, 1))
    }
)
output27: BinaryAssociation = BinaryAssociation(
    name="output27",
    ends={
        Property(name="libraryElement_Event", type=libraryElement_ECAction, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_ECAction28", type=libraryElement_Event, multiplicity=Multiplicity(0, 1))
    }
)
source42: BinaryAssociation = BinaryAssociation(
    name="source42",
    ends={
        Property(name="ECState", type=libraryElement_ECTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="outTransitions", type=libraryElement_ECState, multiplicity=Multiplicity(1, 1))
    }
)
destination43: BinaryAssociation = BinaryAssociation(
    name="destination43",
    ends={
        Property(name="ECState44", type=libraryElement_ECTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="inTransitions", type=libraryElement_ECState, multiplicity=Multiplicity(1, 1))
    }
)
conditionEvent45: BinaryAssociation = BinaryAssociation(
    name="conditionEvent45",
    ends={
        Property(name="libraryElement_Event47", type=libraryElement_ECTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_ECTransition46", type=libraryElement_Event, multiplicity=Multiplicity(0, 1))
    }
)
eCAction36: BinaryAssociation = BinaryAssociation(
    name="eCAction36",
    ends={
        Property(name="libraryElement_ECAction38", type=libraryElement_ECState, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_ECState37", type=libraryElement_ECAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outTransitions39: BinaryAssociation = BinaryAssociation(
    name="outTransitions39",
    ends={
        Property(name="ECTransition", type=libraryElement_ECState, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=libraryElement_ECTransition, multiplicity=Multiplicity(0, 9999))
    }
)
inTransitions40: BinaryAssociation = BinaryAssociation(
    name="inTransitions40",
    ends={
        Property(name="ECTransition41", type=libraryElement_ECState, multiplicity=Multiplicity(1, 1)),
        Property(name="destination", type=libraryElement_ECTransition, multiplicity=Multiplicity(0, 9999))
    }
)
with48: BinaryAssociation = BinaryAssociation(
    name="with48",
    ends={
        Property(name="libraryElement_With", type=libraryElement_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_Event49", type=libraryElement_With, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interface50: BinaryAssociation = BinaryAssociation(
    name="interface50",
    ends={
        Property(name="libraryElement_InterfaceList", type=libraryElement_FBNetworkElement, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_FBNetworkElement", type=libraryElement_InterfaceList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mapping51: BinaryAssociation = BinaryAssociation(
    name="mapping51",
    ends={
        Property(name="libraryElement_Mapping", type=libraryElement_FBNetworkElement, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_FBNetworkElement52", type=libraryElement_Mapping, multiplicity=Multiplicity(0, 1))
    }
)
subAppNetwork53: BinaryAssociation = BinaryAssociation(
    name="subAppNetwork53",
    ends={
        Property(name="libraryElement_FBNetwork54", type=libraryElement_SubApp, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_SubApp", type=libraryElement_FBNetwork, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
interfaceList55: BinaryAssociation = BinaryAssociation(
    name="interfaceList55",
    ends={
        Property(name="libraryElement_InterfaceList56", type=libraryElement_FBType, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_FBType", type=libraryElement_InterfaceList, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
service57: BinaryAssociation = BinaryAssociation(
    name="service57",
    ends={
        Property(name="libraryElement_Service", type=libraryElement_FBType, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_FBType58", type=libraryElement_Service, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
plugs59: BinaryAssociation = BinaryAssociation(
    name="plugs59",
    ends={
        Property(name="libraryElement_AdapterDeclaration61", type=libraryElement_InterfaceList, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_InterfaceList60", type=libraryElement_AdapterDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventInputs65: BinaryAssociation = BinaryAssociation(
    name="eventInputs65",
    ends={
        Property(name="libraryElement_Event67", type=libraryElement_InterfaceList, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_InterfaceList66", type=libraryElement_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventOutputs68: BinaryAssociation = BinaryAssociation(
    name="eventOutputs68",
    ends={
        Property(name="libraryElement_Event70", type=libraryElement_InterfaceList, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_InterfaceList69", type=libraryElement_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputVars71: BinaryAssociation = BinaryAssociation(
    name="inputVars71",
    ends={
        Property(name="libraryElement_VarDeclaration73", type=libraryElement_InterfaceList, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_InterfaceList72", type=libraryElement_VarDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputVars74: BinaryAssociation = BinaryAssociation(
    name="outputVars74",
    ends={
        Property(name="libraryElement_VarDeclaration76", type=libraryElement_InterfaceList, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_InterfaceList75", type=libraryElement_VarDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sockets62: BinaryAssociation = BinaryAssociation(
    name="sockets62",
    ends={
        Property(name="libraryElement_AdapterDeclaration64", type=libraryElement_InterfaceList, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_InterfaceList63", type=libraryElement_AdapterDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
segment77: BinaryAssociation = BinaryAssociation(
    name="segment77",
    ends={
        Property(name="Segment", type=libraryElement_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="outConnections", type=libraryElement_Segment, multiplicity=Multiplicity(0, 1))
    }
)
device78: BinaryAssociation = BinaryAssociation(
    name="device78",
    ends={
        Property(name="Device", type=libraryElement_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="inConnections", type=libraryElement_Device, multiplicity=Multiplicity(0, 1))
    }
)
from79: BinaryAssociation = BinaryAssociation(
    name="from79",
    ends={
        Property(name="libraryElement_FBNetworkElement81", type=libraryElement_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_Mapping80", type=libraryElement_FBNetworkElement, multiplicity=Multiplicity(0, 1))
    }
)
to82: BinaryAssociation = BinaryAssociation(
    name="to82",
    ends={
        Property(name="libraryElement_FBNetworkElement84", type=libraryElement_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_Mapping83", type=libraryElement_FBNetworkElement, multiplicity=Multiplicity(0, 1))
    }
)
fBNetwork85: BinaryAssociation = BinaryAssociation(
    name="fBNetwork85",
    ends={
        Property(name="libraryElement_FBNetwork87", type=libraryElement_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_Resource86", type=libraryElement_FBNetwork, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
device88: BinaryAssociation = BinaryAssociation(
    name="device88",
    ends={
        Property(name="Device89", type=libraryElement_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="resource", type=libraryElement_Device, multiplicity=Multiplicity(0, 1))
    }
)
varDeclaration90: BinaryAssociation = BinaryAssociation(
    name="varDeclaration90",
    ends={
        Property(name="libraryElement_VarDeclaration91", type=libraryElement_ResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_ResourceType", type=libraryElement_VarDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fBNetwork92: BinaryAssociation = BinaryAssociation(
    name="fBNetwork92",
    ends={
        Property(name="libraryElement_FBNetwork94", type=libraryElement_ResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_ResourceType93", type=libraryElement_FBNetwork, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
varDeclarations98: BinaryAssociation = BinaryAssociation(
    name="varDeclarations98",
    ends={
        Property(name="libraryElement_VarDeclaration99", type=libraryElement_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_Segment", type=libraryElement_VarDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outConnections100: BinaryAssociation = BinaryAssociation(
    name="outConnections100",
    ends={
        Property(name="Link101", type=libraryElement_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="segment", type=libraryElement_Link, multiplicity=Multiplicity(0, 9999))
    }
)
serviceTransaction102: BinaryAssociation = BinaryAssociation(
    name="serviceTransaction102",
    ends={
        Property(name="libraryElement_ServiceTransaction", type=libraryElement_ServiceSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_ServiceSequence", type=libraryElement_ServiceTransaction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
supportedFBTypes95: BinaryAssociation = BinaryAssociation(
    name="supportedFBTypes95",
    ends={
        Property(name="libraryElement_FBType97", type=libraryElement_ResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_ResourceType96", type=libraryElement_FBType, multiplicity=Multiplicity(0, 1))
    }
)
outputPrimitive105: BinaryAssociation = BinaryAssociation(
    name="outputPrimitive105",
    ends={
        Property(name="libraryElement_ServiceTransaction106", type=libraryElement_OutputPrimitive, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="libraryElement_OutputPrimitive", type=libraryElement_ServiceTransaction, multiplicity=Multiplicity(1, 1))
    }
)
inputPrimitive103: BinaryAssociation = BinaryAssociation(
    name="inputPrimitive103",
    ends={
        Property(name="libraryElement_InputPrimitive", type=libraryElement_ServiceTransaction, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_ServiceTransaction104", type=libraryElement_InputPrimitive, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
networkElements107: BinaryAssociation = BinaryAssociation(
    name="networkElements107",
    ends={
        Property(name="libraryElement_FBNetworkElement109", type=libraryElement_FBNetwork, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_FBNetwork108", type=libraryElement_FBNetworkElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
adapterConnections114: BinaryAssociation = BinaryAssociation(
    name="adapterConnections114",
    ends={
        Property(name="libraryElement_AdapterConnection", type=libraryElement_FBNetwork, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_FBNetwork115", type=libraryElement_AdapterConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
application116: BinaryAssociation = BinaryAssociation(
    name="application116",
    ends={
        Property(name="libraryElement_Application117", type=libraryElement_AutomationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_AutomationSystem", type=libraryElement_Application, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataConnections110: BinaryAssociation = BinaryAssociation(
    name="dataConnections110",
    ends={
        Property(name="libraryElement_DataConnection", type=libraryElement_FBNetwork, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_FBNetwork111", type=libraryElement_DataConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventConnections112: BinaryAssociation = BinaryAssociation(
    name="eventConnections112",
    ends={
        Property(name="libraryElement_EventConnection", type=libraryElement_FBNetwork, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_FBNetwork113", type=libraryElement_EventConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
systemConfiguration122: BinaryAssociation = BinaryAssociation(
    name="systemConfiguration122",
    ends={
        Property(name="libraryElement_SystemConfiguration", type=libraryElement_AutomationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_AutomationSystem123", type=libraryElement_SystemConfiguration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
varInitialization124: BinaryAssociation = BinaryAssociation(
    name="varInitialization124",
    ends={
        Property(name="libraryElement_VarInitialization", type=libraryElement_VarDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_VarDeclaration125", type=libraryElement_VarInitialization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
withs126: BinaryAssociation = BinaryAssociation(
    name="withs126",
    ends={
        Property(name="With", type=libraryElement_VarDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variables", type=libraryElement_With, multiplicity=Multiplicity(0, 9999))
    }
)
mapping118: BinaryAssociation = BinaryAssociation(
    name="mapping118",
    ends={
        Property(name="libraryElement_Mapping120", type=libraryElement_AutomationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_AutomationSystem119", type=libraryElement_Mapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
palette121: BinaryAssociation = BinaryAssociation(
    name="palette121",
    ends={
        Property(name="palette.ecorePalette", type=libraryElement_AutomationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="automationSystem", type=libraryElement_Palette, multiplicity=Multiplicity(1, 1))
    }
)
variables127: BinaryAssociation = BinaryAssociation(
    name="variables127",
    ends={
        Property(name="VarDeclaration", type=libraryElement_With, multiplicity=Multiplicity(1, 1)),
        Property(name="withs", type=libraryElement_VarDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
versionInfo128: BinaryAssociation = BinaryAssociation(
    name="versionInfo128",
    ends={
        Property(name="libraryElement_VersionInfo", type=libraryElement_LibraryElement, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_LibraryElement", type=libraryElement_VersionInfo, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
identification129: BinaryAssociation = BinaryAssociation(
    name="identification129",
    ends={
        Property(name="libraryElement_Identification", type=libraryElement_LibraryElement, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_LibraryElement130", type=libraryElement_Identification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
paletteEntry131: BinaryAssociation = BinaryAssociation(
    name="paletteEntry131",
    ends={
        Property(name="palette.ecorePaletteEntry", type=libraryElement_LibraryElement, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=libraryElement_PaletteEntry, multiplicity=Multiplicity(0, 1))
    }
)
parameter134: BinaryAssociation = BinaryAssociation(
    name="parameter134",
    ends={
        Property(name="libraryElement_Parameter", type=libraryElement_ConfigurableObject, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_ConfigurableObject", type=libraryElement_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fBNetwork135: BinaryAssociation = BinaryAssociation(
    name="fBNetwork135",
    ends={
        Property(name="libraryElement_FBNetwork136", type=libraryElement_CompositeFBType, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_CompositeFBType", type=libraryElement_FBNetwork, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
compilerInfo132: BinaryAssociation = BinaryAssociation(
    name="compilerInfo132",
    ends={
        Property(name="libraryElement_CompilerInfo133", type=libraryElement_CompilableType, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_CompilableType", type=libraryElement_CompilerInfo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inputConnections137: BinaryAssociation = BinaryAssociation(
    name="inputConnections137",
    ends={
        Property(name="Connection", type=libraryElement_IInterfaceElement, multiplicity=Multiplicity(1, 1)),
        Property(name="destination138", type=libraryElement_Connection, multiplicity=Multiplicity(0, 9999))
    }
)
outputConnections139: BinaryAssociation = BinaryAssociation(
    name="outputConnections139",
    ends={
        Property(name="Connection141", type=libraryElement_IInterfaceElement, multiplicity=Multiplicity(1, 1)),
        Property(name="source140", type=libraryElement_Connection, multiplicity=Multiplicity(0, 9999))
    }
)
type142: BinaryAssociation = BinaryAssociation(
    name="type142",
    ends={
        Property(name="libraryElement_DataType", type=libraryElement_IInterfaceElement, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_IInterfaceElement", type=libraryElement_DataType, multiplicity=Multiplicity(1, 1))
    }
)
value143: BinaryAssociation = BinaryAssociation(
    name="value143",
    ends={
        Property(name="libraryElement_Value", type=libraryElement_IInterfaceElement, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_IInterfaceElement144", type=libraryElement_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
links150: BinaryAssociation = BinaryAssociation(
    name="links150",
    ends={
        Property(name="libraryElement_Link", type=libraryElement_SystemConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_SystemConfiguration151", type=libraryElement_Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations152: BinaryAssociation = BinaryAssociation(
    name="annotations152",
    ends={
        Property(name="libraryElement_Annotation", type=libraryElement_I4DIACElement, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_I4DIACElement", type=libraryElement_Annotation, multiplicity=Multiplicity(0, 9999))
    }
)
varDeclaration153: BinaryAssociation = BinaryAssociation(
    name="varDeclaration153",
    ends={
        Property(name="libraryElement_VarDeclaration154", type=libraryElement_SegmentType, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_SegmentType", type=libraryElement_VarDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
adapterType155: BinaryAssociation = BinaryAssociation(
    name="adapterType155",
    ends={
        Property(name="libraryElement_AdapterType157", type=libraryElement_AdapterFBType, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_AdapterFBType156", type=libraryElement_AdapterType, multiplicity=Multiplicity(0, 1))
    }
)
devices145: BinaryAssociation = BinaryAssociation(
    name="devices145",
    ends={
        Property(name="libraryElement_Device", type=libraryElement_SystemConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_SystemConfiguration146", type=libraryElement_Device, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
segments147: BinaryAssociation = BinaryAssociation(
    name="segments147",
    ends={
        Property(name="libraryElement_Segment149", type=libraryElement_SystemConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_SystemConfiguration148", type=libraryElement_Segment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rightInterface160: BinaryAssociation = BinaryAssociation(
    name="rightInterface160",
    ends={
        Property(name="libraryElement_ServiceInterface", type=libraryElement_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_Service161", type=libraryElement_ServiceInterface, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftInterface162: BinaryAssociation = BinaryAssociation(
    name="leftInterface162",
    ends={
        Property(name="libraryElement_ServiceInterface164", type=libraryElement_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_Service163", type=libraryElement_ServiceInterface, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
serviceSequence165: BinaryAssociation = BinaryAssociation(
    name="serviceSequence165",
    ends={
        Property(name="libraryElement_ServiceSequence167", type=libraryElement_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_Service166", type=libraryElement_ServiceSequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paletteEntry168: BinaryAssociation = BinaryAssociation(
    name="paletteEntry168",
    ends={
        Property(name="libraryElement_PaletteEntry", type=libraryElement_TypedConfigureableObject, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_TypedConfigureableObject", type=libraryElement_PaletteEntry, multiplicity=Multiplicity(1, 1))
    }
)
adapterDeclaration158: BinaryAssociation = BinaryAssociation(
    name="adapterDeclaration158",
    ends={
        Property(name="libraryElement_AdapterDeclaration159", type=libraryElement_AdapterEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_AdapterEvent", type=libraryElement_AdapterDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
interface170: BinaryAssociation = BinaryAssociation(
    name="interface170",
    ends={
        Property(name="libraryElement_ServiceInterface171", type=libraryElement_Primitive, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_Primitive", type=libraryElement_ServiceInterface, multiplicity=Multiplicity(1, 1))
    }
)
color172: BinaryAssociation = BinaryAssociation(
    name="color172",
    ends={
        Property(name="libraryElement_Color", type=libraryElement_ColorizableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_ColorizableElement", type=libraryElement_Color, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
varDeclarations173: BinaryAssociation = BinaryAssociation(
    name="varDeclarations173",
    ends={
        Property(name="libraryElement_VarDeclaration174", type=libraryElement_IVarElement, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryElement_IVarElement", type=libraryElement_VarDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
adapterDecl169: BinaryAssociation = BinaryAssociation(
    name="adapterDecl169",
    ends={
        Property(name="AdapterDeclaration", type=libraryElement_AdapterFB, multiplicity=Multiplicity(1, 1)),
        Property(name="adapterFB", type=libraryElement_AdapterDeclaration, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_libraryElement_AdapterDeclaration_VarDeclaration = Generalization(general=VarDeclaration, specific=libraryElement_AdapterDeclaration)
gen_libraryElement_Algorithm_INamedElement = Generalization(general=INamedElement, specific=libraryElement_Algorithm)
gen_libraryElement_Application_INamedElement = Generalization(general=INamedElement, specific=libraryElement_Application)
gen_libraryElement_BasicFBType_FBType = Generalization(general=FBType, specific=libraryElement_BasicFBType)
gen_libraryElement_AdapterType_DataType = Generalization(general=DataType, specific=libraryElement_AdapterType)
gen_libraryElement_Connection_ConfigurableObject = Generalization(general=ConfigurableObject, specific=libraryElement_Connection)
gen_libraryElement_Device_TypedConfigureableObject = Generalization(general=TypedConfigureableObject, specific=libraryElement_Device)
gen_libraryElement_Device_PositionableElement = Generalization(general=PositionableElement, specific=libraryElement_Device)
gen_libraryElement_Device_ColorizableElement = Generalization(general=ColorizableElement, specific=libraryElement_Device)
gen_libraryElement_Device_IVarElement = Generalization(general=IVarElement, specific=libraryElement_Device)
gen_libraryElement_DeviceType_CompilableType = Generalization(general=CompilableType, specific=libraryElement_DeviceType)
gen_libraryElement_ECState_INamedElement = Generalization(general=INamedElement, specific=libraryElement_ECState)
gen_libraryElement_ECState_PositionableElement = Generalization(general=PositionableElement, specific=libraryElement_ECState)
gen_libraryElement_ECTransition_PositionableElement = Generalization(general=PositionableElement, specific=libraryElement_ECTransition)
gen_libraryElement_FBNetworkElement_TypedConfigureableObject = Generalization(general=TypedConfigureableObject, specific=libraryElement_FBNetworkElement)
gen_libraryElement_FBNetworkElement_PositionableElement = Generalization(general=PositionableElement, specific=libraryElement_FBNetworkElement)
gen_libraryElement_Event_IInterfaceElement = Generalization(general=IInterfaceElement, specific=libraryElement_Event)
gen_libraryElement_FB_FBNetworkElement = Generalization(general=FBNetworkElement, specific=libraryElement_FB)
gen_libraryElement_SubApp_FBNetworkElement = Generalization(general=FBNetworkElement, specific=libraryElement_SubApp)
gen_libraryElement_FBType_CompilableType = Generalization(general=CompilableType, specific=libraryElement_FBType)
gen_libraryElement_InputPrimitive_Primitive = Generalization(general=Primitive, specific=libraryElement_InputPrimitive)
gen_libraryElement_OtherAlgorithm_TextAlgorithm = Generalization(general=TextAlgorithm, specific=libraryElement_OtherAlgorithm)
gen_libraryElement_Link_ConfigurableObject = Generalization(general=ConfigurableObject, specific=libraryElement_Link)
gen_libraryElement_Resource_TypedConfigureableObject = Generalization(general=TypedConfigureableObject, specific=libraryElement_Resource)
gen_libraryElement_Resource_IVarElement = Generalization(general=IVarElement, specific=libraryElement_Resource)
gen_libraryElement_OutputPrimitive_Primitive = Generalization(general=Primitive, specific=libraryElement_OutputPrimitive)
gen_libraryElement_ResourceType_CompilableType = Generalization(general=CompilableType, specific=libraryElement_ResourceType)
gen_libraryElement_ServiceSequence_INamedElement = Generalization(general=INamedElement, specific=libraryElement_ServiceSequence)
gen_libraryElement_Segment_TypedConfigureableObject = Generalization(general=TypedConfigureableObject, specific=libraryElement_Segment)
gen_libraryElement_Segment_PositionableElement = Generalization(general=PositionableElement, specific=libraryElement_Segment)
gen_libraryElement_Segment_ColorizableElement = Generalization(general=ColorizableElement, specific=libraryElement_Segment)
gen_libraryElement_ServiceInterfaceFBType_FBType = Generalization(general=FBType, specific=libraryElement_ServiceInterfaceFBType)
gen_libraryElement_STAlgorithm_TextAlgorithm = Generalization(general=TextAlgorithm, specific=libraryElement_STAlgorithm)
gen_libraryElement_SubAppType_CompositeFBType = Generalization(general=CompositeFBType, specific=libraryElement_SubAppType)
gen_libraryElement_AutomationSystem_LibraryElement = Generalization(general=LibraryElement, specific=libraryElement_AutomationSystem)
gen_libraryElement_VarDeclaration_IInterfaceElement = Generalization(general=IInterfaceElement, specific=libraryElement_VarDeclaration)
gen_libraryElement_LibraryElement_INamedElement = Generalization(general=INamedElement, specific=libraryElement_LibraryElement)
gen_libraryElement_CompositeFBType_FBType = Generalization(general=FBType, specific=libraryElement_CompositeFBType)
gen_libraryElement_TextAlgorithm_Algorithm = Generalization(general=Algorithm, specific=libraryElement_TextAlgorithm)
gen_libraryElement_DataConnection_Connection = Generalization(general=Connection, specific=libraryElement_DataConnection)
gen_libraryElement_CompilableType_LibraryElement = Generalization(general=LibraryElement, specific=libraryElement_CompilableType)
gen_libraryElement_ConfigurableObject_INamedElement = Generalization(general=INamedElement, specific=libraryElement_ConfigurableObject)
gen_libraryElement_ServiceInterface_INamedElement = Generalization(general=INamedElement, specific=libraryElement_ServiceInterface)
gen_libraryElement_IInterfaceElement_INamedElement = Generalization(general=INamedElement, specific=libraryElement_IInterfaceElement)
gen_libraryElement_SystemConfiguration_I4DIACElement = Generalization(general=I4DIACElement, specific=libraryElement_SystemConfiguration)
gen_libraryElement_EventConnection_Connection = Generalization(general=Connection, specific=libraryElement_EventConnection)
gen_libraryElement_AdapterConnection_Connection = Generalization(general=Connection, specific=libraryElement_AdapterConnection)
gen_libraryElement_INamedElement_I4DIACElement = Generalization(general=I4DIACElement, specific=libraryElement_INamedElement)
gen_libraryElement_ResourceTypeFB_FB = Generalization(general=FB, specific=libraryElement_ResourceTypeFB)
gen_libraryElement_SegmentType_CompilableType = Generalization(general=CompilableType, specific=libraryElement_SegmentType)
gen_libraryElement_AdapterFBType_FBType = Generalization(general=FBType, specific=libraryElement_AdapterFBType)
gen_libraryElement_Service_I4DIACElement = Generalization(general=I4DIACElement, specific=libraryElement_Service)
gen_libraryElement_TypedConfigureableObject_ConfigurableObject = Generalization(general=ConfigurableObject, specific=libraryElement_TypedConfigureableObject)
gen_libraryElement_AdapterFB_FB = Generalization(general=FB, specific=libraryElement_AdapterFB)
gen_libraryElement_AdapterEvent_Event = Generalization(general=Event, specific=libraryElement_AdapterEvent)

# Domain Model
domain_model = DomainModel(
    name="libraryElement",
    types={libraryElement_AdapterDeclaration, VarDeclaration, libraryElement_AdapterFB, libraryElement_AdapterFBType, libraryElement_Algorithm, INamedElement, libraryElement_Application, libraryElement_FBNetwork, libraryElement_BasicFBType, FBType, libraryElement_AdapterTypePaletteEntry, libraryElement_AdapterType, DataType, libraryElement_VarDeclaration, libraryElement_CompilerInfo, libraryElement_Compiler, libraryElement_ECC, libraryElement_Connection, ConfigurableObject, libraryElement_Device, TypedConfigureableObject, PositionableElement, ColorizableElement, IVarElement, libraryElement_Resource, libraryElement_IInterfaceElement, libraryElement_DeviceType, CompilableType, libraryElement_ResourceTypeName, libraryElement_Link, libraryElement_ECState, libraryElement_ECTransition, libraryElement_ECAction, libraryElement_Event, libraryElement_FBNetworkElement, IInterfaceElement, libraryElement_With, libraryElement_FB, FBNetworkElement, libraryElement_InterfaceList, libraryElement_Mapping, libraryElement_SubApp, libraryElement_FBType, libraryElement_Identification, libraryElement_Service, libraryElement_InputPrimitive, Primitive, libraryElement_Segment, libraryElement_OtherAlgorithm, TextAlgorithm, libraryElement_OutputPrimitive, libraryElement_Parameter, libraryElement_ResourceType, libraryElement_ServiceSequence, libraryElement_ServiceTransaction, libraryElement_ServiceInterfaceFBType, libraryElement_STAlgorithm, libraryElement_AdapterConnection, libraryElement_SubAppType, CompositeFBType, libraryElement_AutomationSystem, LibraryElement, libraryElement_DataConnection, libraryElement_EventConnection, libraryElement_SystemConfiguration, libraryElement_VarInitialization, libraryElement_VersionInfo, libraryElement_Palette, libraryElement_LibraryElement, libraryElement_PaletteEntry, libraryElement_CompositeFBType, libraryElement_TextAlgorithm, Algorithm, Connection, libraryElement_CompilableType, libraryElement_ConfigurableObject, libraryElement_ServiceInterface, libraryElement_DataType, libraryElement_Value, I4DIACElement, libraryElement_INamedElement, libraryElement_ResourceTypeFB, FB, libraryElement_I4DIACElement, libraryElement_Annotation, libraryElement_SegmentType, libraryElement_TypedConfigureableObject, libraryElement_AdapterEvent, Event, libraryElement_PositionableElement, libraryElement_Color, libraryElement_ColorizableElement, libraryElement_IVarElement, libraryElement_Primitive, Language},
    associations={adapterFB0, adapterFBType2, fBNetwork3, paletteEntry1, internalVars7, compiler9, eCC4, algorithm5, destination11, resource13, source10, varDeclaration16, resourceTypeName18, resource20, fBNetwork22, inConnections14, eCState29, eCTransition31, start33, algorithm25, output27, source42, destination43, conditionEvent45, eCAction36, outTransitions39, inTransitions40, with48, interface50, mapping51, subAppNetwork53, interfaceList55, service57, plugs59, eventInputs65, eventOutputs68, inputVars71, outputVars74, sockets62, segment77, device78, from79, to82, fBNetwork85, device88, varDeclaration90, fBNetwork92, varDeclarations98, outConnections100, serviceTransaction102, supportedFBTypes95, outputPrimitive105, inputPrimitive103, networkElements107, adapterConnections114, application116, dataConnections110, eventConnections112, systemConfiguration122, varInitialization124, withs126, mapping118, palette121, variables127, versionInfo128, identification129, paletteEntry131, parameter134, fBNetwork135, compilerInfo132, inputConnections137, outputConnections139, type142, value143, links150, annotations152, varDeclaration153, adapterType155, devices145, segments147, rightInterface160, leftInterface162, serviceSequence165, paletteEntry168, adapterDeclaration158, interface170, color172, varDeclarations173, adapterDecl169},
    generalizations={gen_libraryElement_AdapterDeclaration_VarDeclaration, gen_libraryElement_Algorithm_INamedElement, gen_libraryElement_Application_INamedElement, gen_libraryElement_BasicFBType_FBType, gen_libraryElement_AdapterType_DataType, gen_libraryElement_Connection_ConfigurableObject, gen_libraryElement_Device_TypedConfigureableObject, gen_libraryElement_Device_PositionableElement, gen_libraryElement_Device_ColorizableElement, gen_libraryElement_Device_IVarElement, gen_libraryElement_DeviceType_CompilableType, gen_libraryElement_ECState_INamedElement, gen_libraryElement_ECState_PositionableElement, gen_libraryElement_ECTransition_PositionableElement, gen_libraryElement_FBNetworkElement_TypedConfigureableObject, gen_libraryElement_FBNetworkElement_PositionableElement, gen_libraryElement_Event_IInterfaceElement, gen_libraryElement_FB_FBNetworkElement, gen_libraryElement_SubApp_FBNetworkElement, gen_libraryElement_FBType_CompilableType, gen_libraryElement_InputPrimitive_Primitive, gen_libraryElement_OtherAlgorithm_TextAlgorithm, gen_libraryElement_Link_ConfigurableObject, gen_libraryElement_Resource_TypedConfigureableObject, gen_libraryElement_Resource_IVarElement, gen_libraryElement_OutputPrimitive_Primitive, gen_libraryElement_ResourceType_CompilableType, gen_libraryElement_ServiceSequence_INamedElement, gen_libraryElement_Segment_TypedConfigureableObject, gen_libraryElement_Segment_PositionableElement, gen_libraryElement_Segment_ColorizableElement, gen_libraryElement_ServiceInterfaceFBType_FBType, gen_libraryElement_STAlgorithm_TextAlgorithm, gen_libraryElement_SubAppType_CompositeFBType, gen_libraryElement_AutomationSystem_LibraryElement, gen_libraryElement_VarDeclaration_IInterfaceElement, gen_libraryElement_LibraryElement_INamedElement, gen_libraryElement_CompositeFBType_FBType, gen_libraryElement_TextAlgorithm_Algorithm, gen_libraryElement_DataConnection_Connection, gen_libraryElement_CompilableType_LibraryElement, gen_libraryElement_ConfigurableObject_INamedElement, gen_libraryElement_ServiceInterface_INamedElement, gen_libraryElement_IInterfaceElement_INamedElement, gen_libraryElement_SystemConfiguration_I4DIACElement, gen_libraryElement_EventConnection_Connection, gen_libraryElement_AdapterConnection_Connection, gen_libraryElement_INamedElement_I4DIACElement, gen_libraryElement_ResourceTypeFB_FB, gen_libraryElement_SegmentType_CompilableType, gen_libraryElement_AdapterFBType_FBType, gen_libraryElement_Service_I4DIACElement, gen_libraryElement_TypedConfigureableObject_ConfigurableObject, gen_libraryElement_AdapterFB_FB, gen_libraryElement_AdapterEvent_Event},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)