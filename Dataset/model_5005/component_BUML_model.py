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
SystemDiagramKind: Enumeration = Enumeration(
    name="SystemDiagramKind",
    literals={
            EnumerationLiteral(name="ONLINE"),
			EnumerationLiteral(name="OFFLINE")
    }
)

# Classes
component_SystemDiagram = Class(name="component::SystemDiagram")
ModelElement = Class(name="ModelElement")
IPropertyMap = Class(name="IPropertyMap")
component_ConfigurationSet = Class(name="component::ConfigurationSet")
component_Port = Class(name="component::Port")
component_InPort = Class(name="component::InPort")
component_Component = Class(name="component::Component", is_abstract=True)
WrapperObject = Class(name="WrapperObject")
component_ComponentSpecification = Class(name="component::ComponentSpecification")
Component = Class(name="Component")
component_OutPort = Class(name="component::OutPort")
component_ServicePort = Class(name="component::ServicePort")
component_ExecutionContext = Class(name="component::ExecutionContext")
component_ContextHandler = Class(name="component::ContextHandler")
component_NameValue = Class(name="component::NameValue")
IAdaptable = Class(name="IAdaptable")
component_EIntegerObjectToPointMapEntry = Class(name="component::EIntegerObjectToPointMapEntry")
component_PortSynchronizer = Class(name="component::PortSynchronizer")
component_ConnectorProfile = Class(name="component::ConnectorProfile")
Port = Class(name="Port")
component_PortConnector = Class(name="component::PortConnector", is_abstract=True)
component_IPropertyMap = Class(name="component::IPropertyMap", is_abstract=True)
component_CorbaStatusObserver = Class(name="component::CorbaStatusObserver")
component_CorbaLogObserver = Class(name="component::CorbaLogObserver")
component_CorbaPortSynchronizer = Class(name="component::CorbaPortSynchronizer")
PortSynchronizer = Class(name="PortSynchronizer")
component_CorbaConnectorProfile = Class(name="component::CorbaConnectorProfile")
ConnectorProfile = Class(name="ConnectorProfile")
component_CorbaConfigurationSet = Class(name="component::CorbaConfigurationSet")
component_CorbaComponent = Class(name="component::CorbaComponent")
CorbaWrapperObject = Class(name="CorbaWrapperObject")
ConfigurationSet = Class(name="ConfigurationSet")
component_CorbaExecutionContext = Class(name="component::CorbaExecutionContext")
ExecutionContext = Class(name="ExecutionContext")
component_CorbaContextHandler = Class(name="component::CorbaContextHandler")
ContextHandler = Class(name="ContextHandler")
component_CorbaObserver = Class(name="component::CorbaObserver")
CorbaObserver = Class(name="CorbaObserver")

# component_SystemDiagram class attributes and methods
component_SystemDiagram_kind: Property = Property(name="kind", type=StringType)
component_SystemDiagram_ConnectorProcessing: Property = Property(name="ConnectorProcessing", type=BooleanType)
component_SystemDiagram_systemId: Property = Property(name="systemId", type=StringType)
component_SystemDiagram_creationDate: Property = Property(name="creationDate", type=StringType)
component_SystemDiagram_updateDate: Property = Property(name="updateDate", type=StringType)
component_SystemDiagram_m_setSynchronizeInterval: Method = Method(name="setSynchronizeInterval", parameters={Parameter(name='milliSecond')})
component_SystemDiagram_m_addPropertyChangeListener: Method = Method(name="addPropertyChangeListener", parameters={Parameter(name='listener')})
component_SystemDiagram_m_removePropertyChangeListener: Method = Method(name="removePropertyChangeListener", parameters={Parameter(name='listener')})
component_SystemDiagram.attributes={component_SystemDiagram_ConnectorProcessing, component_SystemDiagram_kind, component_SystemDiagram_updateDate, component_SystemDiagram_creationDate, component_SystemDiagram_systemId}
component_SystemDiagram.methods={component_SystemDiagram_m_setSynchronizeInterval, component_SystemDiagram_m_removePropertyChangeListener, component_SystemDiagram_m_addPropertyChangeListener}

# ModelElement class attributes and methods

# IPropertyMap class attributes and methods

# component_ConfigurationSet class attributes and methods
component_ConfigurationSet_id: Property = Property(name="id", type=StringType)
component_ConfigurationSet.attributes={component_ConfigurationSet_id}

# component_Port class attributes and methods
component_Port_originalPortString: Property = Property(name="originalPortString", type=StringType)
component_Port_nameL: Property = Property(name="nameL", type=StringType)
component_Port_allowAnyDataType: Property = Property(name="allowAnyDataType", type=BooleanType)
component_Port_allowAnyInterfaceType: Property = Property(name="allowAnyInterfaceType", type=BooleanType)
component_Port_allowAnyDataflowType: Property = Property(name="allowAnyDataflowType", type=BooleanType)
component_Port_allowAnySubscriptionType: Property = Property(name="allowAnySubscriptionType", type=BooleanType)
component_Port_interfaces: Property = Property(name="interfaces", type=StringType)
component_Port_dataflowType: Property = Property(name="dataflowType", type=StringType)
component_Port_subscriptionType: Property = Property(name="subscriptionType", type=StringType)
component_Port_dataType: Property = Property(name="dataType", type=StringType)
component_Port_interfaceType: Property = Property(name="interfaceType", type=StringType)
component_Port_m_disconnectAll: Method = Method(name="disconnectAll", parameters={})
component_Port_m_findPort: Method = Method(name="findPort", parameters={Parameter(name='originalPortString'), Parameter(name='diagram')}, type=StringType)
component_Port_m_validateTargetConnector: Method = Method(name="validateTargetConnector", parameters={Parameter(name='target')}, type=BooleanType)
component_Port_m_validateSourceConnector: Method = Method(name="validateSourceConnector", parameters={Parameter(name='source')}, type=BooleanType)
component_Port.attributes={component_Port_subscriptionType, component_Port_interfaceType, component_Port_interfaces, component_Port_allowAnyDataflowType, component_Port_dataType, component_Port_dataflowType, component_Port_allowAnyDataType, component_Port_nameL, component_Port_allowAnyInterfaceType, component_Port_allowAnySubscriptionType, component_Port_originalPortString}
component_Port.methods={component_Port_m_findPort, component_Port_m_validateSourceConnector, component_Port_m_validateTargetConnector, component_Port_m_disconnectAll}

# component_InPort class attributes and methods

# component_Component class attributes and methods
component_Component_shutDown: Property = Property(name="shutDown", type=StringType)
component_Component_activation: Property = Property(name="activation", type=StringType)
component_Component_deActivation: Property = Property(name="deActivation", type=StringType)
component_Component_resetting: Property = Property(name="resetting", type=StringType)
component_Component_initialize: Property = Property(name="initialize", type=StringType)
component_Component_finalize: Property = Property(name="finalize", type=StringType)
component_Component_instanceNameL: Property = Property(name="instanceNameL", type=StringType)
component_Component_venderL: Property = Property(name="venderL", type=StringType)
component_Component_descriptionL: Property = Property(name="descriptionL", type=StringType)
component_Component_categoryL: Property = Property(name="categoryL", type=StringType)
component_Component_typeNameL: Property = Property(name="typeNameL", type=StringType)
component_Component_versionL: Property = Property(name="versionL", type=StringType)
component_Component_pathId: Property = Property(name="pathId", type=StringType)
component_Component_outportDirection: Property = Property(name="outportDirection", type=StringType)
component_Component_compositeTypeL: Property = Property(name="compositeTypeL", type=StringType)
component_Component_componentId: Property = Property(name="componentId", type=StringType)
component_Component_required: Property = Property(name="required", type=BooleanType)
component_Component_startUp: Property = Property(name="startUp", type=StringType)
component_Component_m_getAllComponents: Method = Method(name="getAllComponents", parameters={}, type=StringType)
component_Component_m_isCompositeComponent: Method = Method(name="isCompositeComponent", parameters={}, type=BooleanType)
component_Component_m_isGroupingCompositeComponent: Method = Method(name="isGroupingCompositeComponent", parameters={}, type=BooleanType)
component_Component_m_hasComponentAction: Method = Method(name="hasComponentAction", parameters={}, type=BooleanType)
component_Component_m_inOnlineSystemDiagram: Method = Method(name="inOnlineSystemDiagram", parameters={}, type=BooleanType)
component_Component_m_setComponentsR: Method = Method(name="setComponentsR", parameters={Parameter(name='componentList')}, type=BooleanType)
component_Component_m_addComponentsR: Method = Method(name="addComponentsR", parameters={Parameter(name='componentList')}, type=BooleanType)
component_Component_m_removeComponentR: Method = Method(name="removeComponentR", parameters={Parameter(name='component')}, type=BooleanType)
component_Component_m_setExportedPorts: Method = Method(name="setExportedPorts", parameters={Parameter(name='values')}, type=BooleanType)
component_Component_m_updateConfigurationSetR: Method = Method(name="updateConfigurationSetR", parameters={Parameter(name='configSet'), Parameter(name='isActive')}, type=BooleanType)
component_Component_m_updateConfigurationSetListR: Method = Method(name="updateConfigurationSetListR", parameters={Parameter(name='originallist'), Parameter(name='list'), Parameter(name='activeConfigurationSet')}, type=BooleanType)
component_Component_m_getPath: Method = Method(name="getPath", parameters={}, type=StringType)
component_Component.attributes={component_Component_componentId, component_Component_typeNameL, component_Component_pathId, component_Component_deActivation, component_Component_instanceNameL, component_Component_startUp, component_Component_outportDirection, component_Component_categoryL, component_Component_activation, component_Component_initialize, component_Component_compositeTypeL, component_Component_required, component_Component_resetting, component_Component_venderL, component_Component_finalize, component_Component_shutDown, component_Component_versionL, component_Component_descriptionL}
component_Component.methods={component_Component_m_hasComponentAction, component_Component_m_isGroupingCompositeComponent, component_Component_m_removeComponentR, component_Component_m_setComponentsR, component_Component_m_addComponentsR, component_Component_m_inOnlineSystemDiagram, component_Component_m_updateConfigurationSetR, component_Component_m_updateConfigurationSetListR, component_Component_m_getPath, component_Component_m_getAllComponents, component_Component_m_setExportedPorts, component_Component_m_isCompositeComponent}

# WrapperObject class attributes and methods

# component_ComponentSpecification class attributes and methods
component_ComponentSpecification_aliasName: Property = Property(name="aliasName", type=StringType)
component_ComponentSpecification_specUnLoad: Property = Property(name="specUnLoad", type=BooleanType)
component_ComponentSpecification_rtcType: Property = Property(name="rtcType", type=StringType)
component_ComponentSpecification.attributes={component_ComponentSpecification_aliasName, component_ComponentSpecification_specUnLoad, component_ComponentSpecification_rtcType}

# Component class attributes and methods

# component_OutPort class attributes and methods

# component_ServicePort class attributes and methods

# component_ExecutionContext class attributes and methods
component_ExecutionContext_kindL: Property = Property(name="kindL", type=IntegerType)
component_ExecutionContext_rateL: Property = Property(name="rateL", type=StringType)
component_ExecutionContext_stateL: Property = Property(name="stateL", type=IntegerType)
component_ExecutionContext_m_getId: Method = Method(name="getId", parameters={}, type=StringType)
component_ExecutionContext_m_getKindName: Method = Method(name="getKindName", parameters={}, type=StringType)
component_ExecutionContext_m_getStateName: Method = Method(name="getStateName", parameters={}, type=StringType)
component_ExecutionContext_m_setRateR: Method = Method(name="setRateR", parameters={Parameter(name='rate')}, type=BooleanType)
component_ExecutionContext_m_addComponentR: Method = Method(name="addComponentR", parameters={Parameter(name='comp')}, type=BooleanType)
component_ExecutionContext_m_removeComponentR: Method = Method(name="removeComponentR", parameters={Parameter(name='comp')}, type=BooleanType)
component_ExecutionContext_m_containsComponent: Method = Method(name="containsComponent", parameters={Parameter(name='comp')}, type=BooleanType)
component_ExecutionContext_m_isOwner: Method = Method(name="isOwner", parameters={Parameter(name='comp')}, type=BooleanType)
component_ExecutionContext.attributes={component_ExecutionContext_rateL, component_ExecutionContext_stateL, component_ExecutionContext_kindL}
component_ExecutionContext.methods={component_ExecutionContext_m_getId, component_ExecutionContext_m_getKindName, component_ExecutionContext_m_setRateR, component_ExecutionContext_m_addComponentR, component_ExecutionContext_m_removeComponentR, component_ExecutionContext_m_getStateName, component_ExecutionContext_m_containsComponent, component_ExecutionContext_m_isOwner}

# component_ContextHandler class attributes and methods
component_ContextHandler_m_setContext: Method = Method(name="setContext", parameters={Parameter(name='ec'), Parameter(name='id')}, type=StringType)
component_ContextHandler_m_getContext: Method = Method(name="getContext", parameters={Parameter(name='id')}, type=StringType)
component_ContextHandler_m_getId: Method = Method(name="getId", parameters={Parameter(name='ec')}, type=StringType)
component_ContextHandler_m_removeContext: Method = Method(name="removeContext", parameters={Parameter(name='id')}, type=StringType)
component_ContextHandler_m_removeId: Method = Method(name="removeId", parameters={Parameter(name='ec')}, type=StringType)
component_ContextHandler_m_sync: Method = Method(name="sync", parameters={})
component_ContextHandler_m_values: Method = Method(name="values", parameters={}, type=StringType)
component_ContextHandler_m_keys: Method = Method(name="keys", parameters={}, type=StringType)
component_ContextHandler_m_clear: Method = Method(name="clear", parameters={})
component_ContextHandler_m_getType: Method = Method(name="getType", parameters={}, type=StringType)
component_ContextHandler_m_getOwnerContexts: Method = Method(name="getOwnerContexts", parameters={}, type=StringType)
component_ContextHandler.methods={component_ContextHandler_m_sync, component_ContextHandler_m_clear, component_ContextHandler_m_keys, component_ContextHandler_m_getContext, component_ContextHandler_m_values, component_ContextHandler_m_removeId, component_ContextHandler_m_getId, component_ContextHandler_m_removeContext, component_ContextHandler_m_getType, component_ContextHandler_m_getOwnerContexts, component_ContextHandler_m_setContext}

# component_NameValue class attributes and methods
component_NameValue_name: Property = Property(name="name", type=StringType)
component_NameValue_value: Property = Property(name="value", type=StringType)
component_NameValue_typeName: Property = Property(name="typeName", type=StringType)
component_NameValue.attributes={component_NameValue_typeName, component_NameValue_name, component_NameValue_value}

# IAdaptable class attributes and methods

# component_EIntegerObjectToPointMapEntry class attributes and methods
component_EIntegerObjectToPointMapEntry_key: Property = Property(name="key", type=StringType)
component_EIntegerObjectToPointMapEntry_value: Property = Property(name="value", type=StringType)
component_EIntegerObjectToPointMapEntry.attributes={component_EIntegerObjectToPointMapEntry_value, component_EIntegerObjectToPointMapEntry_key}

# component_PortSynchronizer class attributes and methods
component_PortSynchronizer_originalPortString: Property = Property(name="originalPortString", type=StringType)
component_PortSynchronizer_m_disconnect: Method = Method(name="disconnect", parameters={Parameter(name='conn_id')}, type=BooleanType)
component_PortSynchronizer_m_disconnect: Method = Method(name="disconnect", parameters={Parameter(name='conn_prof')}, type=BooleanType)
component_PortSynchronizer_m_disconnectAll: Method = Method(name="disconnectAll", parameters={}, type=BooleanType)
component_PortSynchronizer.attributes={component_PortSynchronizer_originalPortString}
component_PortSynchronizer.methods={component_PortSynchronizer_m_disconnect, component_PortSynchronizer_m_disconnect, component_PortSynchronizer_m_disconnectAll}

# component_ConnectorProfile class attributes and methods
component_ConnectorProfile_dataflowType: Property = Property(name="dataflowType", type=StringType)
component_ConnectorProfile_subscriptionType: Property = Property(name="subscriptionType", type=StringType)
component_ConnectorProfile_subscriptionTypeAvailable: Property = Property(name="subscriptionTypeAvailable", type=BooleanType)
component_ConnectorProfile_pushIntervalAvailable: Property = Property(name="pushIntervalAvailable", type=BooleanType)
component_ConnectorProfile_name: Property = Property(name="name", type=StringType)
component_ConnectorProfile_connectorId: Property = Property(name="connectorId", type=StringType)
component_ConnectorProfile_dataType: Property = Property(name="dataType", type=StringType)
component_ConnectorProfile_interfaceType: Property = Property(name="interfaceType", type=StringType)
component_ConnectorProfile_pushRate: Property = Property(name="pushRate", type=StringType)
component_ConnectorProfile_pushPolicy: Property = Property(name="pushPolicy", type=StringType)
component_ConnectorProfile_skipCount: Property = Property(name="skipCount", type=StringType)
component_ConnectorProfile_pushPolicyAvailable: Property = Property(name="pushPolicyAvailable", type=BooleanType)
component_ConnectorProfile_skipCountAvailable: Property = Property(name="skipCountAvailable", type=BooleanType)
component_ConnectorProfile_sourceString: Property = Property(name="sourceString", type=StringType)
component_ConnectorProfile_targetString: Property = Property(name="targetString", type=StringType)
component_ConnectorProfile_outportBufferLength: Property = Property(name="outportBufferLength", type=StringType)
component_ConnectorProfile_outportBufferFullPolicy: Property = Property(name="outportBufferFullPolicy", type=StringType)
component_ConnectorProfile_outportBufferWriteTimeout: Property = Property(name="outportBufferWriteTimeout", type=StringType)
component_ConnectorProfile_outportBufferEmptyPolicy: Property = Property(name="outportBufferEmptyPolicy", type=StringType)
component_ConnectorProfile_outportBufferReadTimeout: Property = Property(name="outportBufferReadTimeout", type=StringType)
component_ConnectorProfile_inportBufferLength: Property = Property(name="inportBufferLength", type=StringType)
component_ConnectorProfile_inportBufferFullPolicy: Property = Property(name="inportBufferFullPolicy", type=StringType)
component_ConnectorProfile_inportBufferWriteTimeout: Property = Property(name="inportBufferWriteTimeout", type=StringType)
component_ConnectorProfile_inportBufferEmptyPolicy: Property = Property(name="inportBufferEmptyPolicy", type=StringType)
component_ConnectorProfile_inportBufferReadTimeout: Property = Property(name="inportBufferReadTimeout", type=StringType)
component_ConnectorProfile_timestampPolicy: Property = Property(name="timestampPolicy", type=StringType)
component_ConnectorProfile_isReverse: Property = Property(name="isReverse", type=BooleanType)
component_ConnectorProfile_outportSerializerType: Property = Property(name="outportSerializerType", type=StringType)
component_ConnectorProfile_inportSerializerType: Property = Property(name="inportSerializerType", type=StringType)
component_ConnectorProfile.attributes={component_ConnectorProfile_inportBufferLength, component_ConnectorProfile_connectorId, component_ConnectorProfile_outportBufferReadTimeout, component_ConnectorProfile_inportBufferReadTimeout, component_ConnectorProfile_skipCountAvailable, component_ConnectorProfile_name, component_ConnectorProfile_skipCount, component_ConnectorProfile_dataType, component_ConnectorProfile_interfaceType, component_ConnectorProfile_pushRate, component_ConnectorProfile_targetString, component_ConnectorProfile_inportBufferWriteTimeout, component_ConnectorProfile_isReverse, component_ConnectorProfile_outportBufferLength, component_ConnectorProfile_sourceString, component_ConnectorProfile_inportBufferFullPolicy, component_ConnectorProfile_inportSerializerType, component_ConnectorProfile_outportBufferFullPolicy, component_ConnectorProfile_pushPolicy, component_ConnectorProfile_inportBufferEmptyPolicy, component_ConnectorProfile_pushPolicyAvailable, component_ConnectorProfile_subscriptionTypeAvailable, component_ConnectorProfile_pushIntervalAvailable, component_ConnectorProfile_outportBufferEmptyPolicy, component_ConnectorProfile_timestampPolicy, component_ConnectorProfile_outportBufferWriteTimeout, component_ConnectorProfile_subscriptionType, component_ConnectorProfile_outportSerializerType, component_ConnectorProfile_dataflowType}

# Port class attributes and methods

# component_PortConnector class attributes and methods
component_PortConnector_m_createConnectorR: Method = Method(name="createConnectorR", parameters={}, type=BooleanType)
component_PortConnector_m_deleteConnectorR: Method = Method(name="deleteConnectorR", parameters={}, type=BooleanType)
component_PortConnector.methods={component_PortConnector_m_createConnectorR, component_PortConnector_m_deleteConnectorR}

# component_IPropertyMap class attributes and methods
component_IPropertyMap_m_setProperty: Method = Method(name="setProperty", parameters={Parameter(name='key'), Parameter(name='value')})
component_IPropertyMap_m_removeProperty: Method = Method(name="removeProperty", parameters={Parameter(name='key')}, type=StringType)
component_IPropertyMap_m_getPropertyKeys: Method = Method(name="getPropertyKeys", parameters={}, type=StringType)
component_IPropertyMap_m_getPropertyMap: Method = Method(name="getPropertyMap", parameters={}, type=IPropertyMap)
component_IPropertyMap_m_getProperty: Method = Method(name="getProperty", parameters={Parameter(name='key')}, type=StringType)
component_IPropertyMap.methods={component_IPropertyMap_m_getProperty, component_IPropertyMap_m_getPropertyMap, component_IPropertyMap_m_setProperty, component_IPropertyMap_m_getPropertyKeys, component_IPropertyMap_m_removeProperty}

# component_CorbaStatusObserver class attributes and methods
component_CorbaStatusObserver_m_isTimeOut: Method = Method(name="isTimeOut", parameters={}, type=BooleanType)
component_CorbaStatusObserver.methods={component_CorbaStatusObserver_m_isTimeOut}

# component_CorbaLogObserver class attributes and methods

# component_CorbaPortSynchronizer class attributes and methods
component_CorbaPortSynchronizer_rTCPortProfile: Property = Property(name="rTCPortProfile", type=StringType)
component_CorbaPortSynchronizer.attributes={component_CorbaPortSynchronizer_rTCPortProfile}

# PortSynchronizer class attributes and methods

# component_CorbaConnectorProfile class attributes and methods
component_CorbaConnectorProfile_rtcConnectorProfile: Property = Property(name="rtcConnectorProfile", type=StringType)
component_CorbaConnectorProfile.attributes={component_CorbaConnectorProfile_rtcConnectorProfile}

# ConnectorProfile class attributes and methods

# component_CorbaConfigurationSet class attributes and methods
component_CorbaConfigurationSet_sDOConfigurationSet: Property = Property(name="sDOConfigurationSet", type=StringType)
component_CorbaConfigurationSet.attributes={component_CorbaConfigurationSet_sDOConfigurationSet}

# component_CorbaComponent class attributes and methods
component_CorbaComponent_ior: Property = Property(name="ior", type=StringType)
component_CorbaComponent_rTCComponentProfile: Property = Property(name="rTCComponentProfile", type=StringType)
component_CorbaComponent_rTCExecutionContexts: Property = Property(name="rTCExecutionContexts", type=StringType)
component_CorbaComponent_rTCParticipationContexts: Property = Property(name="rTCParticipationContexts", type=StringType)
component_CorbaComponent_sDOConfiguration: Property = Property(name="sDOConfiguration", type=StringType)
component_CorbaComponent_sDOOrganization: Property = Property(name="sDOOrganization", type=StringType)
component_CorbaComponent_rTCRTObjects: Property = Property(name="rTCRTObjects", type=StringType)
component_CorbaComponent_componentState: Property = Property(name="componentState", type=IntegerType)
component_CorbaComponent_m_startR: Method = Method(name="startR", parameters={}, type=IntegerType)
component_CorbaComponent_m_stopR: Method = Method(name="stopR", parameters={}, type=IntegerType)
component_CorbaComponent_m_activateR: Method = Method(name="activateR", parameters={}, type=IntegerType)
component_CorbaComponent_m_deactivateR: Method = Method(name="deactivateR", parameters={}, type=IntegerType)
component_CorbaComponent_m_resetR: Method = Method(name="resetR", parameters={}, type=IntegerType)
component_CorbaComponent_m_finalizeR: Method = Method(name="finalizeR", parameters={}, type=IntegerType)
component_CorbaComponent_m_exitR: Method = Method(name="exitR", parameters={}, type=IntegerType)
component_CorbaComponent_m_getExecutionContextState: Method = Method(name="getExecutionContextState", parameters={}, type=IntegerType)
component_CorbaComponent_m_getExecutionContextState: Method = Method(name="getExecutionContextState", parameters={Parameter(name='ec')}, type=IntegerType)
component_CorbaComponent_m_getExecutionContextStateName: Method = Method(name="getExecutionContextStateName", parameters={}, type=StringType)
component_CorbaComponent_m_getExecutionContextStateName: Method = Method(name="getExecutionContextStateName", parameters={Parameter(name='ec')}, type=StringType)
component_CorbaComponent_m_getComponentStateName: Method = Method(name="getComponentStateName", parameters={}, type=StringType)
component_CorbaComponent_m_getCorbaObjectInterface: Method = Method(name="getCorbaObjectInterface", parameters={}, type=StringType)
component_CorbaComponent_m_supportedCorbaObserver: Method = Method(name="supportedCorbaObserver", parameters={}, type=BooleanType)
component_CorbaComponent_m_activateAll: Method = Method(name="activateAll", parameters={})
component_CorbaComponent_m_deactivateAll: Method = Method(name="deactivateAll", parameters={})
component_CorbaComponent_m_startAll: Method = Method(name="startAll", parameters={})
component_CorbaComponent_m_stopAll: Method = Method(name="stopAll", parameters={})
component_CorbaComponent_m_attachPortEventObserver: Method = Method(name="attachPortEventObserver", parameters={Parameter(name='observer')})
component_CorbaComponent_m_detatchPortEventObserver: Method = Method(name="detatchPortEventObserver", parameters={Parameter(name='observer')})
component_CorbaComponent.attributes={component_CorbaComponent_rTCComponentProfile, component_CorbaComponent_sDOOrganization, component_CorbaComponent_rTCRTObjects, component_CorbaComponent_componentState, component_CorbaComponent_sDOConfiguration, component_CorbaComponent_rTCParticipationContexts, component_CorbaComponent_rTCExecutionContexts, component_CorbaComponent_ior}
component_CorbaComponent.methods={component_CorbaComponent_m_detatchPortEventObserver, component_CorbaComponent_m_stopAll, component_CorbaComponent_m_getExecutionContextState, component_CorbaComponent_m_getComponentStateName, component_CorbaComponent_m_deactivateR, component_CorbaComponent_m_getExecutionContextState, component_CorbaComponent_m_startR, component_CorbaComponent_m_deactivateAll, component_CorbaComponent_m_attachPortEventObserver, component_CorbaComponent_m_activateAll, component_CorbaComponent_m_finalizeR, component_CorbaComponent_m_getExecutionContextStateName, component_CorbaComponent_m_getExecutionContextStateName, component_CorbaComponent_m_getCorbaObjectInterface, component_CorbaComponent_m_stopR, component_CorbaComponent_m_exitR, component_CorbaComponent_m_activateR, component_CorbaComponent_m_startAll, component_CorbaComponent_m_resetR, component_CorbaComponent_m_supportedCorbaObserver}

# CorbaWrapperObject class attributes and methods

# ConfigurationSet class attributes and methods

# component_CorbaExecutionContext class attributes and methods
component_CorbaExecutionContext_rtcExecutionContextProfile: Property = Property(name="rtcExecutionContextProfile", type=StringType)
component_CorbaExecutionContext_m_startR: Method = Method(name="startR", parameters={}, type=IntegerType)
component_CorbaExecutionContext_m_stopR: Method = Method(name="stopR", parameters={}, type=IntegerType)
component_CorbaExecutionContext_m_activateR: Method = Method(name="activateR", parameters={Parameter(name='comp')}, type=IntegerType)
component_CorbaExecutionContext_m_deactivateR: Method = Method(name="deactivateR", parameters={Parameter(name='comp')}, type=IntegerType)
component_CorbaExecutionContext_m_resetR: Method = Method(name="resetR", parameters={Parameter(name='comp')}, type=IntegerType)
component_CorbaExecutionContext_m_getComponentState: Method = Method(name="getComponentState", parameters={Parameter(name='comp')}, type=IntegerType)
component_CorbaExecutionContext_m_getComponentStateName: Method = Method(name="getComponentStateName", parameters={Parameter(name='comp')}, type=StringType)
component_CorbaExecutionContext.attributes={component_CorbaExecutionContext_rtcExecutionContextProfile}
component_CorbaExecutionContext.methods={component_CorbaExecutionContext_m_stopR, component_CorbaExecutionContext_m_deactivateR, component_CorbaExecutionContext_m_resetR, component_CorbaExecutionContext_m_activateR, component_CorbaExecutionContext_m_getComponentState, component_CorbaExecutionContext_m_startR, component_CorbaExecutionContext_m_getComponentStateName}

# ExecutionContext class attributes and methods

# component_CorbaContextHandler class attributes and methods

# ContextHandler class attributes and methods

# component_CorbaObserver class attributes and methods
component_CorbaObserver_serviceProfile: Property = Property(name="serviceProfile", type=StringType)
component_CorbaObserver_servant: Property = Property(name="servant", type=StringType)
component_CorbaObserver_m_activate: Method = Method(name="activate", parameters={})
component_CorbaObserver_m_deactivate: Method = Method(name="deactivate", parameters={})
component_CorbaObserver_m_attachComponent: Method = Method(name="attachComponent", parameters={Parameter(name='component')}, type=BooleanType)
component_CorbaObserver_m_detachComponent: Method = Method(name="detachComponent", parameters={}, type=BooleanType)
component_CorbaObserver_m_finish: Method = Method(name="finish", parameters={}, type=BooleanType)
component_CorbaObserver.attributes={component_CorbaObserver_servant, component_CorbaObserver_serviceProfile}
component_CorbaObserver.methods={component_CorbaObserver_m_finish, component_CorbaObserver_m_detachComponent, component_CorbaObserver_m_attachComponent, component_CorbaObserver_m_activate, component_CorbaObserver_m_deactivate}

# CorbaObserver class attributes and methods

# Relationships
configurationSets7: BinaryAssociation = BinaryAssociation(
    name="configurationSets7",
    ends={
        Property(name="component_ConfigurationSet", type=component_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="component_Component8", type=component_ConfigurationSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activeConfigurationSet9: BinaryAssociation = BinaryAssociation(
    name="activeConfigurationSet9",
    ends={
        Property(name="component_ConfigurationSet11", type=component_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="component_Component10", type=component_ConfigurationSet, multiplicity=Multiplicity(0, 1))
    }
)
ports12: BinaryAssociation = BinaryAssociation(
    name="ports12",
    ends={
        Property(name="component_Port", type=component_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="component_Component13", type=component_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inports14: BinaryAssociation = BinaryAssociation(
    name="inports14",
    ends={
        Property(name="component_InPort", type=component_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="component_Component15", type=component_InPort, multiplicity=Multiplicity(0, 9999))
    }
)
components0: BinaryAssociation = BinaryAssociation(
    name="components0",
    ends={
        Property(name="component_Component", type=component_SystemDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="component_SystemDiagram", type=component_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentSystemDiagram2: BinaryAssociation = BinaryAssociation(
    name="parentSystemDiagram2",
    ends={
        Property(name="component_SystemDiagram3", type=component_SystemDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="component_SystemDiagram1", type=component_SystemDiagram, multiplicity=Multiplicity(0, 1))
    }
)
compositeComponent4: BinaryAssociation = BinaryAssociation(
    name="compositeComponent4",
    ends={
        Property(name="component_Component6", type=component_SystemDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="component_SystemDiagram5", type=component_Component, multiplicity=Multiplicity(0, 1))
    }
)
outports16: BinaryAssociation = BinaryAssociation(
    name="outports16",
    ends={
        Property(name="component_OutPort", type=component_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="component_Component17", type=component_OutPort, multiplicity=Multiplicity(0, 9999))
    }
)
serviceports18: BinaryAssociation = BinaryAssociation(
    name="serviceports18",
    ends={
        Property(name="component_ServicePort", type=component_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="component_Component19", type=component_ServicePort, multiplicity=Multiplicity(0, 9999))
    }
)
components21: BinaryAssociation = BinaryAssociation(
    name="components21",
    ends={
        Property(name="component_Component22", type=component_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="component_Component20", type=component_Component, multiplicity=Multiplicity(0, 9999))
    }
)
primaryExecutionContext23: BinaryAssociation = BinaryAssociation(
    name="primaryExecutionContext23",
    ends={
        Property(name="component_ExecutionContext", type=component_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="component_Component24", type=component_ExecutionContext, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
executionContexts25: BinaryAssociation = BinaryAssociation(
    name="executionContexts25",
    ends={
        Property(name="component_ExecutionContext27", type=component_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="component_Component26", type=component_ExecutionContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
participationContexts28: BinaryAssociation = BinaryAssociation(
    name="participationContexts28",
    ends={
        Property(name="component_ExecutionContext30", type=component_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="component_Component29", type=component_ExecutionContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
executionContextHandler31: BinaryAssociation = BinaryAssociation(
    name="executionContextHandler31",
    ends={
        Property(name="component_ContextHandler", type=component_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="component_Component32", type=component_ContextHandler, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
participationContextHandler33: BinaryAssociation = BinaryAssociation(
    name="participationContextHandler33",
    ends={
        Property(name="component_ContextHandler35", type=component_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="component_Component34", type=component_ContextHandler, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
childSystemDiagram36: BinaryAssociation = BinaryAssociation(
    name="childSystemDiagram36",
    ends={
        Property(name="component_SystemDiagram38", type=component_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="component_Component37", type=component_SystemDiagram, multiplicity=Multiplicity(0, 1))
    }
)
configurationData45: BinaryAssociation = BinaryAssociation(
    name="configurationData45",
    ends={
        Property(name="component_NameValue", type=component_ConfigurationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="component_ConfigurationSet46", type=component_NameValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner39: BinaryAssociation = BinaryAssociation(
    name="owner39",
    ends={
        Property(name="component_Component41", type=component_ExecutionContext, multiplicity=Multiplicity(1, 1)),
        Property(name="component_ExecutionContext40", type=component_Component, multiplicity=Multiplicity(0, 1))
    }
)
participants42: BinaryAssociation = BinaryAssociation(
    name="participants42",
    ends={
        Property(name="component_Component44", type=component_ExecutionContext, multiplicity=Multiplicity(1, 1)),
        Property(name="component_ExecutionContext43", type=component_Component, multiplicity=Multiplicity(0, 9999))
    }
)
connectorProfile51: BinaryAssociation = BinaryAssociation(
    name="connectorProfile51",
    ends={
        Property(name="component_ConnectorProfile52", type=component_PortConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="component_PortConnector", type=component_ConnectorProfile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
routingConstraint53: BinaryAssociation = BinaryAssociation(
    name="routingConstraint53",
    ends={
        Property(name="component_EIntegerObjectToPointMapEntry", type=component_PortConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="component_PortConnector54", type=component_EIntegerObjectToPointMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source55: BinaryAssociation = BinaryAssociation(
    name="source55",
    ends={
        Property(name="component_Port57", type=component_PortConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="component_PortConnector56", type=component_Port, multiplicity=Multiplicity(0, 1))
    }
)
target58: BinaryAssociation = BinaryAssociation(
    name="target58",
    ends={
        Property(name="component_Port60", type=component_PortConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="component_PortConnector59", type=component_Port, multiplicity=Multiplicity(0, 1))
    }
)
synchronizer47: BinaryAssociation = BinaryAssociation(
    name="synchronizer47",
    ends={
        Property(name="component_PortSynchronizer", type=component_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="component_Port48", type=component_PortSynchronizer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connectorProfiles49: BinaryAssociation = BinaryAssociation(
    name="connectorProfiles49",
    ends={
        Property(name="component_ConnectorProfile", type=component_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="component_Port50", type=component_ConnectorProfile, multiplicity=Multiplicity(0, 9999))
    }
)
statusObserver61: BinaryAssociation = BinaryAssociation(
    name="statusObserver61",
    ends={
        Property(name="component_CorbaStatusObserver", type=component_CorbaComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="component_CorbaComponent", type=component_CorbaStatusObserver, multiplicity=Multiplicity(0, 1))
    }
)
logObserver62: BinaryAssociation = BinaryAssociation(
    name="logObserver62",
    ends={
        Property(name="component_CorbaLogObserver", type=component_CorbaComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="component_CorbaComponent63", type=component_CorbaLogObserver, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_component_SystemDiagram_ModelElement = Generalization(general=ModelElement, specific=component_SystemDiagram)
gen_component_SystemDiagram_IPropertyMap = Generalization(general=IPropertyMap, specific=component_SystemDiagram)
gen_component_Component_WrapperObject = Generalization(general=WrapperObject, specific=component_Component)
gen_component_Component_IPropertyMap = Generalization(general=IPropertyMap, specific=component_Component)
gen_component_ComponentSpecification_Component = Generalization(general=Component, specific=component_ComponentSpecification)
gen_component_ExecutionContext_WrapperObject = Generalization(general=WrapperObject, specific=component_ExecutionContext)
gen_component_ExecutionContext_IPropertyMap = Generalization(general=IPropertyMap, specific=component_ExecutionContext)
gen_component_NameValue_WrapperObject = Generalization(general=WrapperObject, specific=component_NameValue)
gen_component_Port_WrapperObject = Generalization(general=WrapperObject, specific=component_Port)
gen_component_ContextHandler_IAdaptable = Generalization(general=IAdaptable, specific=component_ContextHandler)
gen_component_ConfigurationSet_WrapperObject = Generalization(general=WrapperObject, specific=component_ConfigurationSet)
gen_component_InPort_Port = Generalization(general=Port, specific=component_InPort)
gen_component_OutPort_Port = Generalization(general=Port, specific=component_OutPort)
gen_component_ServicePort_Port = Generalization(general=Port, specific=component_ServicePort)
gen_component_PortSynchronizer_IPropertyMap = Generalization(general=IPropertyMap, specific=component_PortSynchronizer)
gen_component_PortConnector_WrapperObject = Generalization(general=WrapperObject, specific=component_PortConnector)
gen_component_ConnectorProfile_WrapperObject = Generalization(general=WrapperObject, specific=component_ConnectorProfile)
gen_component_ConnectorProfile_IPropertyMap = Generalization(general=IPropertyMap, specific=component_ConnectorProfile)
gen_component_IPropertyMap_IAdaptable = Generalization(general=IAdaptable, specific=component_IPropertyMap)
gen_component_CorbaPortSynchronizer_CorbaWrapperObject = Generalization(general=CorbaWrapperObject, specific=component_CorbaPortSynchronizer)
gen_component_CorbaPortSynchronizer_PortSynchronizer = Generalization(general=PortSynchronizer, specific=component_CorbaPortSynchronizer)
gen_component_CorbaConnectorProfile_ConnectorProfile = Generalization(general=ConnectorProfile, specific=component_CorbaConnectorProfile)
gen_component_CorbaComponent_Component = Generalization(general=Component, specific=component_CorbaComponent)
gen_component_CorbaComponent_CorbaWrapperObject = Generalization(general=CorbaWrapperObject, specific=component_CorbaComponent)
gen_component_CorbaConfigurationSet_ConfigurationSet = Generalization(general=ConfigurationSet, specific=component_CorbaConfigurationSet)
gen_component_CorbaExecutionContext_ExecutionContext = Generalization(general=ExecutionContext, specific=component_CorbaExecutionContext)
gen_component_CorbaExecutionContext_CorbaWrapperObject = Generalization(general=CorbaWrapperObject, specific=component_CorbaExecutionContext)
gen_component_CorbaContextHandler_ContextHandler = Generalization(general=ContextHandler, specific=component_CorbaContextHandler)
gen_component_CorbaObserver_IPropertyMap = Generalization(general=IPropertyMap, specific=component_CorbaObserver)
gen_component_CorbaObserver_IAdaptable = Generalization(general=IAdaptable, specific=component_CorbaObserver)
gen_component_CorbaStatusObserver_CorbaObserver = Generalization(general=CorbaObserver, specific=component_CorbaStatusObserver)
gen_component_CorbaLogObserver_CorbaObserver = Generalization(general=CorbaObserver, specific=component_CorbaLogObserver)

# Domain Model
domain_model = DomainModel(
    name="component",
    types={component_SystemDiagram, ModelElement, IPropertyMap, component_ConfigurationSet, component_Port, component_InPort, component_Component, WrapperObject, component_ComponentSpecification, Component, component_OutPort, component_ServicePort, component_ExecutionContext, component_ContextHandler, component_NameValue, IAdaptable, component_EIntegerObjectToPointMapEntry, component_PortSynchronizer, component_ConnectorProfile, Port, component_PortConnector, component_IPropertyMap, component_CorbaStatusObserver, component_CorbaLogObserver, component_CorbaPortSynchronizer, PortSynchronizer, component_CorbaConnectorProfile, ConnectorProfile, component_CorbaConfigurationSet, component_CorbaComponent, CorbaWrapperObject, ConfigurationSet, component_CorbaExecutionContext, ExecutionContext, component_CorbaContextHandler, ContextHandler, component_CorbaObserver, CorbaObserver, SystemDiagramKind},
    associations={configurationSets7, activeConfigurationSet9, ports12, inports14, components0, parentSystemDiagram2, compositeComponent4, outports16, serviceports18, components21, primaryExecutionContext23, executionContexts25, participationContexts28, executionContextHandler31, participationContextHandler33, childSystemDiagram36, configurationData45, owner39, participants42, connectorProfile51, routingConstraint53, source55, target58, synchronizer47, connectorProfiles49, statusObserver61, logObserver62},
    generalizations={gen_component_SystemDiagram_ModelElement, gen_component_SystemDiagram_IPropertyMap, gen_component_Component_WrapperObject, gen_component_Component_IPropertyMap, gen_component_ComponentSpecification_Component, gen_component_ExecutionContext_WrapperObject, gen_component_ExecutionContext_IPropertyMap, gen_component_NameValue_WrapperObject, gen_component_Port_WrapperObject, gen_component_ContextHandler_IAdaptable, gen_component_ConfigurationSet_WrapperObject, gen_component_InPort_Port, gen_component_OutPort_Port, gen_component_ServicePort_Port, gen_component_PortSynchronizer_IPropertyMap, gen_component_PortConnector_WrapperObject, gen_component_ConnectorProfile_WrapperObject, gen_component_ConnectorProfile_IPropertyMap, gen_component_IPropertyMap_IAdaptable, gen_component_CorbaPortSynchronizer_CorbaWrapperObject, gen_component_CorbaPortSynchronizer_PortSynchronizer, gen_component_CorbaConnectorProfile_ConnectorProfile, gen_component_CorbaComponent_Component, gen_component_CorbaComponent_CorbaWrapperObject, gen_component_CorbaConfigurationSet_ConfigurationSet, gen_component_CorbaExecutionContext_ExecutionContext, gen_component_CorbaExecutionContext_CorbaWrapperObject, gen_component_CorbaContextHandler_ContextHandler, gen_component_CorbaObserver_IPropertyMap, gen_component_CorbaObserver_IAdaptable, gen_component_CorbaStatusObserver_CorbaObserver, gen_component_CorbaLogObserver_CorbaObserver},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)