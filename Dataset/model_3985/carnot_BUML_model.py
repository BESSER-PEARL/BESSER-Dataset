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
            EnumerationLiteral(name="IN"),
			EnumerationLiteral(name="OUT"),
			EnumerationLiteral(name="INOUT")
    }
)

FlowControlType: Enumeration = Enumeration(
    name="FlowControlType",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="join"),
			EnumerationLiteral(name="split")
    }
)

ImplementationType: Enumeration = Enumeration(
    name="ImplementationType",
    literals={
            EnumerationLiteral(name="engine"),
			EnumerationLiteral(name="pull"),
			EnumerationLiteral(name="push")
    }
)

JoinSplitType: Enumeration = Enumeration(
    name="JoinSplitType",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="XOR"),
			EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR")
    }
)

LinkCardinality: Enumeration = Enumeration(
    name="LinkCardinality",
    literals={
            EnumerationLiteral(name="Unknown"),
			EnumerationLiteral(name="One"),
			EnumerationLiteral(name="Many")
    }
)

ActivityImplementationType: Enumeration = Enumeration(
    name="ActivityImplementationType",
    literals={
            EnumerationLiteral(name="Manual"),
			EnumerationLiteral(name="Application"),
			EnumerationLiteral(name="Subprocess"),
			EnumerationLiteral(name="Route")
    }
)

SubProcessModeType: Enumeration = Enumeration(
    name="SubProcessModeType",
    literals={
            EnumerationLiteral(name="sync_shared"),
			EnumerationLiteral(name="sync_separate"),
			EnumerationLiteral(name="async_separate")
    }
)

DiagramModeType: Enumeration = Enumeration(
    name="DiagramModeType",
    literals={
            EnumerationLiteral(name="MODE_4_0_0"),
			EnumerationLiteral(name="MODE_4_5_0")
    }
)

LinkColor: Enumeration = Enumeration(
    name="LinkColor",
    literals={
            EnumerationLiteral(name="Unknown"),
			EnumerationLiteral(name="Black"),
			EnumerationLiteral(name="DarkBlue"),
			EnumerationLiteral(name="DarkGray"),
			EnumerationLiteral(name="Blue"),
			EnumerationLiteral(name="LightGray"),
			EnumerationLiteral(name="Red"),
			EnumerationLiteral(name="Yellow")
    }
)

LinkLineStyle: Enumeration = Enumeration(
    name="LinkLineStyle",
    literals={
            EnumerationLiteral(name="Unknown"),
			EnumerationLiteral(name="Normal"),
			EnumerationLiteral(name="ShortStrokes"),
			EnumerationLiteral(name="LongStrokes")
    }
)

LinkEndStyle: Enumeration = Enumeration(
    name="LinkEndStyle",
    literals={
            EnumerationLiteral(name="Unknown"),
			EnumerationLiteral(name="NoArrow"),
			EnumerationLiteral(name="OpenTriangle"),
			EnumerationLiteral(name="EmptyTriangle"),
			EnumerationLiteral(name="FilledTriangle"),
			EnumerationLiteral(name="EmptyRhombus"),
			EnumerationLiteral(name="FilledRhombus")
    }
)

LoopType: Enumeration = Enumeration(
    name="LoopType",
    literals={
            EnumerationLiteral(name="Unknown"),
			EnumerationLiteral(name="None"),
			EnumerationLiteral(name="While"),
			EnumerationLiteral(name="Repeat")
    }
)

OrientationType: Enumeration = Enumeration(
    name="OrientationType",
    literals={
            EnumerationLiteral(name="Vertical"),
			EnumerationLiteral(name="Horizontal")
    }
)

RoutingType: Enumeration = Enumeration(
    name="RoutingType",
    literals={
            EnumerationLiteral(name="Default"),
			EnumerationLiteral(name="ShortestPath"),
			EnumerationLiteral(name="Manhattan"),
			EnumerationLiteral(name="Explicit")
    }
)

# Classes
carnot_Coordinates = Class(name="carnot::Coordinates")
carnot_IIdentifiableElement = Class(name="carnot::IIdentifiableElement", is_abstract=True)
carnot_IExtensibleElement = Class(name="carnot::IExtensibleElement")
carnot_AttributeType = Class(name="carnot::AttributeType")
carnot_IdentifiableReference = Class(name="carnot::IdentifiableReference")
carnot_EObject = Class(name="carnot::EObject")
carnot_IModelElement = Class(name="carnot::IModelElement", is_abstract=True)
carnot_IIdentifiableModelElement = Class(name="carnot::IIdentifiableModelElement", is_abstract=True)
IModelElement = Class(name="IModelElement")
IIdentifiableElement = Class(name="IIdentifiableElement")
IExtensibleElement = Class(name="IExtensibleElement")
carnot_DescriptionType = Class(name="carnot::DescriptionType")
carnot_IEventHandlerOwner = Class(name="carnot::IEventHandlerOwner", is_abstract=True)
carnot_EventHandlerType = Class(name="carnot::EventHandlerType")
carnot_IAccessPointOwner = Class(name="carnot::IAccessPointOwner", is_abstract=True)
carnot_AccessPointType = Class(name="carnot::AccessPointType")
carnot_IMetaType = Class(name="carnot::IMetaType", is_abstract=True)
IIdentifiableModelElement = Class(name="IIdentifiableModelElement")
carnot_ITypedElement = Class(name="carnot::ITypedElement", is_abstract=True)
carnot_ISymbolContainer = Class(name="carnot::ISymbolContainer", is_abstract=True)
carnot_ActivitySymbolType = Class(name="carnot::ActivitySymbolType")
carnot_AnnotationSymbolType = Class(name="carnot::AnnotationSymbolType")
carnot_ApplicationSymbolType = Class(name="carnot::ApplicationSymbolType")
carnot_ConditionalPerformerSymbolType = Class(name="carnot::ConditionalPerformerSymbolType")
carnot_DataSymbolType = Class(name="carnot::DataSymbolType")
carnot_EndEventSymbol = Class(name="carnot::EndEventSymbol")
carnot_GatewaySymbol = Class(name="carnot::GatewaySymbol")
carnot_GroupSymbolType = Class(name="carnot::GroupSymbolType")
carnot_IntermediateEventSymbol = Class(name="carnot::IntermediateEventSymbol")
carnot_ModelerSymbolType = Class(name="carnot::ModelerSymbolType")
carnot_OrganizationSymbolType = Class(name="carnot::OrganizationSymbolType")
carnot_ProcessSymbolType = Class(name="carnot::ProcessSymbolType")
carnot_PublicInterfaceSymbol = Class(name="carnot::PublicInterfaceSymbol")
carnot_RoleSymbolType = Class(name="carnot::RoleSymbolType")
carnot_StartEventSymbol = Class(name="carnot::StartEventSymbol")
carnot_TextSymbolType = Class(name="carnot::TextSymbolType")
carnot_DataMappingConnectionType = Class(name="carnot::DataMappingConnectionType")
carnot_ExecutedByConnectionType = Class(name="carnot::ExecutedByConnectionType")
carnot_GenericLinkConnectionType = Class(name="carnot::GenericLinkConnectionType")
carnot_PartOfConnectionType = Class(name="carnot::PartOfConnectionType")
carnot_PerformsConnectionType = Class(name="carnot::PerformsConnectionType")
carnot_TriggersConnectionType = Class(name="carnot::TriggersConnectionType")
carnot_RefersToConnectionType = Class(name="carnot::RefersToConnectionType")
carnot_SubProcessOfConnectionType = Class(name="carnot::SubProcessOfConnectionType")
carnot_TransitionConnectionType = Class(name="carnot::TransitionConnectionType")
carnot_WorksForConnectionType = Class(name="carnot::WorksForConnectionType")
carnot_TeamLeadConnectionType = Class(name="carnot::TeamLeadConnectionType")
carnot_IGraphicalObject = Class(name="carnot::IGraphicalObject", is_abstract=True)
carnot_INodeSymbol = Class(name="carnot::INodeSymbol", is_abstract=True)
IGraphicalObject = Class(name="IGraphicalObject")
carnot_ISwimlaneSymbol = Class(name="carnot::ISwimlaneSymbol", is_abstract=True)
INodeSymbol = Class(name="INodeSymbol")
carnot_IModelParticipant = Class(name="carnot::IModelParticipant", is_abstract=True)
carnot_LaneSymbol = Class(name="carnot::LaneSymbol")
carnot_IModelElementNodeSymbol = Class(name="carnot::IModelElementNodeSymbol", is_abstract=True)
carnot_IFlowObjectSymbol = Class(name="carnot::IFlowObjectSymbol", is_abstract=True)
carnot_IConnectionSymbol = Class(name="carnot::IConnectionSymbol", is_abstract=True)
carnot_DataTypeType = Class(name="carnot::DataTypeType")
carnot_ActivityType = Class(name="carnot::ActivityType")
carnot_ParticipantType = Class(name="carnot::ParticipantType")
carnot_IModelParticipantSymbol = Class(name="carnot::IModelParticipantSymbol", is_abstract=True)
IModelElementNodeSymbol = Class(name="IModelElementNodeSymbol")
carnot_AbstractEventAction = Class(name="carnot::AbstractEventAction", is_abstract=True)
ITypedElement = Class(name="ITypedElement")
carnot_EventActionTypeType = Class(name="carnot::EventActionTypeType")
carnot_AbstractEventSymbol = Class(name="carnot::AbstractEventSymbol", is_abstract=True)
IFlowObjectSymbol = Class(name="IFlowObjectSymbol")
IEventHandlerOwner = Class(name="IEventHandlerOwner")
IdRefOwner = Class(name="IdRefOwner")
carnot_DataMappingType = Class(name="carnot::DataMappingType")
carnot_ApplicationType = Class(name="carnot::ApplicationType")
carnot_TransitionType = Class(name="carnot::TransitionType")
carnot_Code = Class(name="carnot::Code")
carnot_ProcessDefinitionType = Class(name="carnot::ProcessDefinitionType")
IAccessPointOwner = Class(name="IAccessPointOwner")
carnot_LoopType = Class(name="carnot::LoopType")
carnot_TextType = Class(name="carnot::TextType")
carnot_ApplicationContextTypeType = Class(name="carnot::ApplicationContextTypeType")
IMetaType = Class(name="IMetaType")
carnot_ContextType = Class(name="carnot::ContextType")
carnot_ApplicationTypeType = Class(name="carnot::ApplicationTypeType")
carnot_BindActionType = Class(name="carnot::BindActionType")
AbstractEventAction = Class(name="AbstractEventAction")
carnot_XmlTextNode = Class(name="carnot::XmlTextNode")
IModelParticipantSymbol = Class(name="IModelParticipantSymbol")
carnot_ConditionalPerformerType = Class(name="carnot::ConditionalPerformerType")
IModelParticipant = Class(name="IModelParticipant")
carnot_DataType = Class(name="carnot::DataType")
carnot_DataPathType = Class(name="carnot::DataPathType")
IConnectionSymbol = Class(name="IConnectionSymbol")
carnot_ParameterMappingType = Class(name="carnot::ParameterMappingType")
carnot_PoolSymbol = Class(name="carnot::PoolSymbol")
carnot_ExternalReferenceType = Class(name="carnot::ExternalReferenceType")
carnot_DiagramType = Class(name="carnot::DiagramType")
ISymbolContainer = Class(name="ISymbolContainer")
carnot_DocumentRoot = Class(name="carnot::DocumentRoot")
carnot_EStringToStringMapEntry = Class(name="carnot::EStringToStringMapEntry")
carnot_ModelType = Class(name="carnot::ModelType")
AbstractEventSymbol = Class(name="AbstractEventSymbol")
carnot_EventActionType = Class(name="carnot::EventActionType")
carnot_EventConditionTypeType = Class(name="carnot::EventConditionTypeType")
carnot_UnbindActionType = Class(name="carnot::UnbindActionType")
carnot_IdRef = Class(name="carnot::IdRef")
carnot_ExternalPackage = Class(name="carnot::ExternalPackage")
carnot_IdRefOwner = Class(name="carnot::IdRefOwner", is_abstract=True)
carnot_LinkTypeType = Class(name="carnot::LinkTypeType")
ISwimlaneSymbol = Class(name="ISwimlaneSymbol")
carnot_ModelerType = Class(name="carnot::ModelerType")
carnot_TriggerTypeType = Class(name="carnot::TriggerTypeType")
carnot_ExternalPackages = Class(name="carnot::ExternalPackages")
carnot_ScriptType = Class(name="carnot::ScriptType")
carnot_TypeDeclarationsType = Class(name="carnot::TypeDeclarationsType")
carnot_QualityControlType = Class(name="carnot::QualityControlType")
carnot_RoleType = Class(name="carnot::RoleType")
carnot_OrganizationType = Class(name="carnot::OrganizationType")
carnot_ViewType = Class(name="carnot::ViewType")
carnot_TriggerType = Class(name="carnot::TriggerType")
carnot_FormalParametersType = Class(name="carnot::FormalParametersType")
FormalParameterMappingsType = Class(name="FormalParameterMappingsType")
carnot_ViewableType = Class(name="carnot::ViewableType")
extensions_carnot_FormalParameterType = Class(name="extensions::carnot::FormalParameterType")
carnot_extensions_FormalParameterMappingsType = Class(name="carnot::extensions::FormalParameterMappingsType")
FormalParameterMappingType = Class(name="FormalParameterMappingType")
carnot_extensions_FormalParameterMappingType = Class(name="carnot::extensions::FormalParameterMappingType")
extensions_carnot_DataType = Class(name="extensions::carnot::DataType")

# carnot_Coordinates class attributes and methods
carnot_Coordinates_xPos: Property = Property(name="xPos", type=StringType)
carnot_Coordinates_yPos: Property = Property(name="yPos", type=StringType)
carnot_Coordinates.attributes={carnot_Coordinates_xPos, carnot_Coordinates_yPos}

# carnot_IIdentifiableElement class attributes and methods
carnot_IIdentifiableElement_id: Property = Property(name="id", type=StringType)
carnot_IIdentifiableElement_name: Property = Property(name="name", type=StringType)
carnot_IIdentifiableElement.attributes={carnot_IIdentifiableElement_id, carnot_IIdentifiableElement_name}

# carnot_IExtensibleElement class attributes and methods

# carnot_AttributeType class attributes and methods
carnot_AttributeType_mixed: Property = Property(name="mixed", type=StringType)
carnot_AttributeType_group: Property = Property(name="group", type=StringType)
carnot_AttributeType_any: Property = Property(name="any", type=StringType)
carnot_AttributeType_name: Property = Property(name="name", type=StringType)
carnot_AttributeType_type: Property = Property(name="type", type=StringType)
carnot_AttributeType_value: Property = Property(name="value", type=StringType)
carnot_AttributeType_m_getAttributeValue: Method = Method(name="getAttributeValue", parameters={}, type=StringType)
carnot_AttributeType_m_setAttributeValue: Method = Method(name="setAttributeValue", parameters={Parameter(name='value'), Parameter(name='type')})
carnot_AttributeType.attributes={carnot_AttributeType_value, carnot_AttributeType_any, carnot_AttributeType_group, carnot_AttributeType_mixed, carnot_AttributeType_type, carnot_AttributeType_name}
carnot_AttributeType.methods={carnot_AttributeType_m_setAttributeValue, carnot_AttributeType_m_getAttributeValue}

# carnot_IdentifiableReference class attributes and methods

# carnot_EObject class attributes and methods

# carnot_IModelElement class attributes and methods
carnot_IModelElement_elementOid: Property = Property(name="elementOid", type=StringType)
carnot_IModelElement.attributes={carnot_IModelElement_elementOid}

# carnot_IIdentifiableModelElement class attributes and methods
carnot_IIdentifiableModelElement_m_getSymbols: Method = Method(name="getSymbols", parameters={})
carnot_IIdentifiableModelElement.methods={carnot_IIdentifiableModelElement_m_getSymbols}

# IModelElement class attributes and methods

# IIdentifiableElement class attributes and methods

# IExtensibleElement class attributes and methods

# carnot_DescriptionType class attributes and methods
carnot_DescriptionType_mixed: Property = Property(name="mixed", type=StringType)
carnot_DescriptionType.attributes={carnot_DescriptionType_mixed}

# carnot_IEventHandlerOwner class attributes and methods

# carnot_EventHandlerType class attributes and methods
carnot_EventHandlerType_autoBind: Property = Property(name="autoBind", type=StringType)
carnot_EventHandlerType_consumeOnMatch: Property = Property(name="consumeOnMatch", type=StringType)
carnot_EventHandlerType_logHandler: Property = Property(name="logHandler", type=StringType)
carnot_EventHandlerType_unbindOnMatch: Property = Property(name="unbindOnMatch", type=StringType)
carnot_EventHandlerType.attributes={carnot_EventHandlerType_unbindOnMatch, carnot_EventHandlerType_logHandler, carnot_EventHandlerType_consumeOnMatch, carnot_EventHandlerType_autoBind}

# carnot_IAccessPointOwner class attributes and methods

# carnot_AccessPointType class attributes and methods
carnot_AccessPointType_direction: Property = Property(name="direction", type=StringType)
carnot_AccessPointType.attributes={carnot_AccessPointType_direction}

# carnot_IMetaType class attributes and methods
carnot_IMetaType_isPredefined: Property = Property(name="isPredefined", type=StringType)
carnot_IMetaType_m_getExtensionPointId: Method = Method(name="getExtensionPointId", parameters={}, type=StringType)
carnot_IMetaType_m_getTypedElements: Method = Method(name="getTypedElements", parameters={})
carnot_IMetaType.attributes={carnot_IMetaType_isPredefined}
carnot_IMetaType.methods={carnot_IMetaType_m_getExtensionPointId, carnot_IMetaType_m_getTypedElements}

# IIdentifiableModelElement class attributes and methods

# carnot_ITypedElement class attributes and methods
carnot_ITypedElement_m_getMetaType: Method = Method(name="getMetaType", parameters={}, type=StringType)
carnot_ITypedElement.methods={carnot_ITypedElement_m_getMetaType}

# carnot_ISymbolContainer class attributes and methods
carnot_ISymbolContainer_nodes: Property = Property(name="nodes", type=StringType)
carnot_ISymbolContainer_connections: Property = Property(name="connections", type=StringType)
carnot_ISymbolContainer_m_getNodeContainingFeatures: Method = Method(name="getNodeContainingFeatures", parameters={}, type=StringType)
carnot_ISymbolContainer_m_getConnectionContainingFeatures: Method = Method(name="getConnectionContainingFeatures", parameters={}, type=StringType)
carnot_ISymbolContainer.attributes={carnot_ISymbolContainer_nodes, carnot_ISymbolContainer_connections}
carnot_ISymbolContainer.methods={carnot_ISymbolContainer_m_getNodeContainingFeatures, carnot_ISymbolContainer_m_getConnectionContainingFeatures}

# carnot_ActivitySymbolType class attributes and methods

# carnot_AnnotationSymbolType class attributes and methods

# carnot_ApplicationSymbolType class attributes and methods

# carnot_ConditionalPerformerSymbolType class attributes and methods

# carnot_DataSymbolType class attributes and methods

# carnot_EndEventSymbol class attributes and methods

# carnot_GatewaySymbol class attributes and methods
carnot_GatewaySymbol_flowKind: Property = Property(name="flowKind", type=StringType)
carnot_GatewaySymbol.attributes={carnot_GatewaySymbol_flowKind}

# carnot_GroupSymbolType class attributes and methods

# carnot_IntermediateEventSymbol class attributes and methods

# carnot_ModelerSymbolType class attributes and methods

# carnot_OrganizationSymbolType class attributes and methods

# carnot_ProcessSymbolType class attributes and methods

# carnot_PublicInterfaceSymbol class attributes and methods

# carnot_RoleSymbolType class attributes and methods

# carnot_StartEventSymbol class attributes and methods

# carnot_TextSymbolType class attributes and methods
carnot_TextSymbolType_text: Property = Property(name="text", type=StringType)
carnot_TextSymbolType.attributes={carnot_TextSymbolType_text}

# carnot_DataMappingConnectionType class attributes and methods

# carnot_ExecutedByConnectionType class attributes and methods

# carnot_GenericLinkConnectionType class attributes and methods

# carnot_PartOfConnectionType class attributes and methods

# carnot_PerformsConnectionType class attributes and methods

# carnot_TriggersConnectionType class attributes and methods

# carnot_RefersToConnectionType class attributes and methods

# carnot_SubProcessOfConnectionType class attributes and methods

# carnot_TransitionConnectionType class attributes and methods
carnot_TransitionConnectionType_points: Property = Property(name="points", type=StringType)
carnot_TransitionConnectionType.attributes={carnot_TransitionConnectionType_points}

# carnot_WorksForConnectionType class attributes and methods

# carnot_TeamLeadConnectionType class attributes and methods

# carnot_IGraphicalObject class attributes and methods
carnot_IGraphicalObject_borderColor: Property = Property(name="borderColor", type=StringType)
carnot_IGraphicalObject_fillColor: Property = Property(name="fillColor", type=StringType)
carnot_IGraphicalObject_style: Property = Property(name="style", type=StringType)
carnot_IGraphicalObject.attributes={carnot_IGraphicalObject_borderColor, carnot_IGraphicalObject_fillColor, carnot_IGraphicalObject_style}

# carnot_INodeSymbol class attributes and methods
carnot_INodeSymbol_xPos: Property = Property(name="xPos", type=StringType)
carnot_INodeSymbol_yPos: Property = Property(name="yPos", type=StringType)
carnot_INodeSymbol_width: Property = Property(name="width", type=StringType)
carnot_INodeSymbol_height: Property = Property(name="height", type=StringType)
carnot_INodeSymbol_shape: Property = Property(name="shape", type=StringType)
carnot_INodeSymbol_m_getInConnectionFeatures: Method = Method(name="getInConnectionFeatures", parameters={}, type=StringType)
carnot_INodeSymbol_m_getOutConnectionFeatures: Method = Method(name="getOutConnectionFeatures", parameters={}, type=StringType)
carnot_INodeSymbol.attributes={carnot_INodeSymbol_shape, carnot_INodeSymbol_height, carnot_INodeSymbol_xPos, carnot_INodeSymbol_yPos, carnot_INodeSymbol_width}
carnot_INodeSymbol.methods={carnot_INodeSymbol_m_getInConnectionFeatures, carnot_INodeSymbol_m_getOutConnectionFeatures}

# IGraphicalObject class attributes and methods

# carnot_ISwimlaneSymbol class attributes and methods
carnot_ISwimlaneSymbol_orientation: Property = Property(name="orientation", type=StringType)
carnot_ISwimlaneSymbol_collapsed: Property = Property(name="collapsed", type=StringType)
carnot_ISwimlaneSymbol.attributes={carnot_ISwimlaneSymbol_collapsed, carnot_ISwimlaneSymbol_orientation}

# INodeSymbol class attributes and methods

# carnot_IModelParticipant class attributes and methods

# carnot_LaneSymbol class attributes and methods

# carnot_IModelElementNodeSymbol class attributes and methods
carnot_IModelElementNodeSymbol_m_getModelElement: Method = Method(name="getModelElement", parameters={}, type=IIdentifiableModelElement)
carnot_IModelElementNodeSymbol_m_setModelElement: Method = Method(name="setModelElement", parameters={Parameter(name='element')})
carnot_IModelElementNodeSymbol.methods={carnot_IModelElementNodeSymbol_m_setModelElement, carnot_IModelElementNodeSymbol_m_getModelElement}

# carnot_IFlowObjectSymbol class attributes and methods

# carnot_IConnectionSymbol class attributes and methods
carnot_IConnectionSymbol_sourceAnchor: Property = Property(name="sourceAnchor", type=StringType)
carnot_IConnectionSymbol_targetAnchor: Property = Property(name="targetAnchor", type=StringType)
carnot_IConnectionSymbol_routing: Property = Property(name="routing", type=StringType)
carnot_IConnectionSymbol_m_setTargetNode: Method = Method(name="setTargetNode", parameters={Parameter(name='nodeSymbol')})
carnot_IConnectionSymbol_m_getSourceNode: Method = Method(name="getSourceNode", parameters={}, type=INodeSymbol)
carnot_IConnectionSymbol_m_setSourceNode: Method = Method(name="setSourceNode", parameters={Parameter(name='nodeSymbol')})
carnot_IConnectionSymbol_m_getTargetNode: Method = Method(name="getTargetNode", parameters={}, type=INodeSymbol)
carnot_IConnectionSymbol.attributes={carnot_IConnectionSymbol_sourceAnchor, carnot_IConnectionSymbol_routing, carnot_IConnectionSymbol_targetAnchor}
carnot_IConnectionSymbol.methods={carnot_IConnectionSymbol_m_setSourceNode, carnot_IConnectionSymbol_m_setTargetNode, carnot_IConnectionSymbol_m_getTargetNode, carnot_IConnectionSymbol_m_getSourceNode}

# carnot_DataTypeType class attributes and methods
carnot_DataTypeType_accessPathEditor: Property = Property(name="accessPathEditor", type=StringType)
carnot_DataTypeType_evaluator: Property = Property(name="evaluator", type=StringType)
carnot_DataTypeType_instanceClass: Property = Property(name="instanceClass", type=StringType)
carnot_DataTypeType_panelClass: Property = Property(name="panelClass", type=StringType)
carnot_DataTypeType_readable: Property = Property(name="readable", type=StringType)
carnot_DataTypeType_storageStrategy: Property = Property(name="storageStrategy", type=StringType)
carnot_DataTypeType_validatorClass: Property = Property(name="validatorClass", type=StringType)
carnot_DataTypeType_valueCreator: Property = Property(name="valueCreator", type=StringType)
carnot_DataTypeType_writable: Property = Property(name="writable", type=StringType)
carnot_DataTypeType.attributes={carnot_DataTypeType_readable, carnot_DataTypeType_evaluator, carnot_DataTypeType_panelClass, carnot_DataTypeType_instanceClass, carnot_DataTypeType_validatorClass, carnot_DataTypeType_writable, carnot_DataTypeType_accessPathEditor, carnot_DataTypeType_storageStrategy, carnot_DataTypeType_valueCreator}

# carnot_ActivityType class attributes and methods
carnot_ActivityType_hibernateOnCreation: Property = Property(name="hibernateOnCreation", type=StringType)
carnot_ActivityType_implementation: Property = Property(name="implementation", type=StringType)
carnot_ActivityType_allowsAbortByPerformer: Property = Property(name="allowsAbortByPerformer", type=StringType)
carnot_ActivityType_join: Property = Property(name="join", type=StringType)
carnot_ActivityType_loopCondition: Property = Property(name="loopCondition", type=StringType)
carnot_ActivityType_loopType: Property = Property(name="loopType", type=StringType)
carnot_ActivityType_split: Property = Property(name="split", type=StringType)
carnot_ActivityType_subProcessMode: Property = Property(name="subProcessMode", type=StringType)
carnot_ActivityType.attributes={carnot_ActivityType_loopCondition, carnot_ActivityType_allowsAbortByPerformer, carnot_ActivityType_loopType, carnot_ActivityType_hibernateOnCreation, carnot_ActivityType_split, carnot_ActivityType_subProcessMode, carnot_ActivityType_implementation, carnot_ActivityType_join}

# carnot_ParticipantType class attributes and methods

# carnot_IModelParticipantSymbol class attributes and methods

# IModelElementNodeSymbol class attributes and methods

# carnot_AbstractEventAction class attributes and methods

# ITypedElement class attributes and methods

# carnot_EventActionTypeType class attributes and methods
carnot_EventActionTypeType_actionClass: Property = Property(name="actionClass", type=StringType)
carnot_EventActionTypeType_activityAction: Property = Property(name="activityAction", type=StringType)
carnot_EventActionTypeType_panelClass: Property = Property(name="panelClass", type=StringType)
carnot_EventActionTypeType_processAction: Property = Property(name="processAction", type=StringType)
carnot_EventActionTypeType_supportedConditionTypes: Property = Property(name="supportedConditionTypes", type=StringType)
carnot_EventActionTypeType_unsupportedContexts: Property = Property(name="unsupportedContexts", type=StringType)
carnot_EventActionTypeType.attributes={carnot_EventActionTypeType_unsupportedContexts, carnot_EventActionTypeType_activityAction, carnot_EventActionTypeType_panelClass, carnot_EventActionTypeType_actionClass, carnot_EventActionTypeType_processAction, carnot_EventActionTypeType_supportedConditionTypes}

# carnot_AbstractEventSymbol class attributes and methods
carnot_AbstractEventSymbol_label: Property = Property(name="label", type=StringType)
carnot_AbstractEventSymbol.attributes={carnot_AbstractEventSymbol_label}

# IFlowObjectSymbol class attributes and methods

# IEventHandlerOwner class attributes and methods

# IdRefOwner class attributes and methods

# carnot_DataMappingType class attributes and methods
carnot_DataMappingType_applicationAccessPoint: Property = Property(name="applicationAccessPoint", type=StringType)
carnot_DataMappingType_applicationPath: Property = Property(name="applicationPath", type=StringType)
carnot_DataMappingType_context: Property = Property(name="context", type=StringType)
carnot_DataMappingType_dataPath: Property = Property(name="dataPath", type=StringType)
carnot_DataMappingType_direction: Property = Property(name="direction", type=StringType)
carnot_DataMappingType.attributes={carnot_DataMappingType_dataPath, carnot_DataMappingType_applicationAccessPoint, carnot_DataMappingType_context, carnot_DataMappingType_applicationPath, carnot_DataMappingType_direction}

# carnot_ApplicationType class attributes and methods
carnot_ApplicationType_interactive: Property = Property(name="interactive", type=StringType)
carnot_ApplicationType.attributes={carnot_ApplicationType_interactive}

# carnot_TransitionType class attributes and methods
carnot_TransitionType_condition: Property = Property(name="condition", type=StringType)
carnot_TransitionType_forkOnTraversal: Property = Property(name="forkOnTraversal", type=StringType)
carnot_TransitionType.attributes={carnot_TransitionType_forkOnTraversal, carnot_TransitionType_condition}

# carnot_Code class attributes and methods
carnot_Code_code: Property = Property(name="code", type=StringType)
carnot_Code_value: Property = Property(name="value", type=StringType)
carnot_Code_name: Property = Property(name="name", type=StringType)
carnot_Code.attributes={carnot_Code_value, carnot_Code_code, carnot_Code_name}

# carnot_ProcessDefinitionType class attributes and methods
carnot_ProcessDefinitionType_defaultPriority: Property = Property(name="defaultPriority", type=StringType)
carnot_ProcessDefinitionType.attributes={carnot_ProcessDefinitionType_defaultPriority}

# IAccessPointOwner class attributes and methods

# carnot_LoopType class attributes and methods

# carnot_TextType class attributes and methods
carnot_TextType_mixed: Property = Property(name="mixed", type=StringType)
carnot_TextType.attributes={carnot_TextType_mixed}

# carnot_ApplicationContextTypeType class attributes and methods
carnot_ApplicationContextTypeType_accessPointProviderClass: Property = Property(name="accessPointProviderClass", type=StringType)
carnot_ApplicationContextTypeType_hasApplicationPath: Property = Property(name="hasApplicationPath", type=StringType)
carnot_ApplicationContextTypeType_hasMappingId: Property = Property(name="hasMappingId", type=StringType)
carnot_ApplicationContextTypeType_panelClass: Property = Property(name="panelClass", type=StringType)
carnot_ApplicationContextTypeType_validatorClass: Property = Property(name="validatorClass", type=StringType)
carnot_ApplicationContextTypeType.attributes={carnot_ApplicationContextTypeType_validatorClass, carnot_ApplicationContextTypeType_hasApplicationPath, carnot_ApplicationContextTypeType_accessPointProviderClass, carnot_ApplicationContextTypeType_panelClass, carnot_ApplicationContextTypeType_hasMappingId}

# IMetaType class attributes and methods

# carnot_ContextType class attributes and methods

# carnot_ApplicationTypeType class attributes and methods
carnot_ApplicationTypeType_panelClass: Property = Property(name="panelClass", type=StringType)
carnot_ApplicationTypeType_synchronous: Property = Property(name="synchronous", type=StringType)
carnot_ApplicationTypeType_validatorClass: Property = Property(name="validatorClass", type=StringType)
carnot_ApplicationTypeType_accessPointProviderClass: Property = Property(name="accessPointProviderClass", type=StringType)
carnot_ApplicationTypeType_instanceClass: Property = Property(name="instanceClass", type=StringType)
carnot_ApplicationTypeType.attributes={carnot_ApplicationTypeType_instanceClass, carnot_ApplicationTypeType_accessPointProviderClass, carnot_ApplicationTypeType_panelClass, carnot_ApplicationTypeType_synchronous, carnot_ApplicationTypeType_validatorClass}

# carnot_BindActionType class attributes and methods

# AbstractEventAction class attributes and methods

# carnot_XmlTextNode class attributes and methods
carnot_XmlTextNode_mixed: Property = Property(name="mixed", type=StringType)
carnot_XmlTextNode.attributes={carnot_XmlTextNode_mixed}

# IModelParticipantSymbol class attributes and methods

# carnot_ConditionalPerformerType class attributes and methods
carnot_ConditionalPerformerType_dataPath: Property = Property(name="dataPath", type=StringType)
carnot_ConditionalPerformerType_isUser: Property = Property(name="isUser", type=StringType)
carnot_ConditionalPerformerType.attributes={carnot_ConditionalPerformerType_isUser, carnot_ConditionalPerformerType_dataPath}

# IModelParticipant class attributes and methods

# carnot_DataType class attributes and methods
carnot_DataType_predefined: Property = Property(name="predefined", type=StringType)
carnot_DataType.attributes={carnot_DataType_predefined}

# carnot_DataPathType class attributes and methods
carnot_DataPathType_dataPath: Property = Property(name="dataPath", type=StringType)
carnot_DataPathType_descriptor: Property = Property(name="descriptor", type=StringType)
carnot_DataPathType_key: Property = Property(name="key", type=StringType)
carnot_DataPathType_direction: Property = Property(name="direction", type=StringType)
carnot_DataPathType.attributes={carnot_DataPathType_key, carnot_DataPathType_direction, carnot_DataPathType_descriptor, carnot_DataPathType_dataPath}

# IConnectionSymbol class attributes and methods

# carnot_ParameterMappingType class attributes and methods
carnot_ParameterMappingType_dataPath: Property = Property(name="dataPath", type=StringType)
carnot_ParameterMappingType_parameter: Property = Property(name="parameter", type=StringType)
carnot_ParameterMappingType_parameterPath: Property = Property(name="parameterPath", type=StringType)
carnot_ParameterMappingType.attributes={carnot_ParameterMappingType_dataPath, carnot_ParameterMappingType_parameter, carnot_ParameterMappingType_parameterPath}

# carnot_PoolSymbol class attributes and methods
carnot_PoolSymbol_boundaryVisible: Property = Property(name="boundaryVisible", type=StringType)
carnot_PoolSymbol.attributes={carnot_PoolSymbol_boundaryVisible}

# carnot_ExternalReferenceType class attributes and methods

# carnot_DiagramType class attributes and methods
carnot_DiagramType_name: Property = Property(name="name", type=StringType)
carnot_DiagramType_orientation: Property = Property(name="orientation", type=StringType)
carnot_DiagramType_mode: Property = Property(name="mode", type=StringType)
carnot_DiagramType.attributes={carnot_DiagramType_orientation, carnot_DiagramType_mode, carnot_DiagramType_name}

# ISymbolContainer class attributes and methods

# carnot_DocumentRoot class attributes and methods
carnot_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
carnot_DocumentRoot.attributes={carnot_DocumentRoot_mixed}

# carnot_EStringToStringMapEntry class attributes and methods

# carnot_ModelType class attributes and methods
carnot_ModelType_modelOID: Property = Property(name="modelOID", type=StringType)
carnot_ModelType_oid: Property = Property(name="oid", type=StringType)
carnot_ModelType_vendor: Property = Property(name="vendor", type=StringType)
carnot_ModelType_author: Property = Property(name="author", type=StringType)
carnot_ModelType_carnotVersion: Property = Property(name="carnotVersion", type=StringType)
carnot_ModelType_created: Property = Property(name="created", type=StringType)
carnot_ModelType.attributes={carnot_ModelType_created, carnot_ModelType_carnotVersion, carnot_ModelType_modelOID, carnot_ModelType_oid, carnot_ModelType_author, carnot_ModelType_vendor}

# AbstractEventSymbol class attributes and methods

# carnot_EventActionType class attributes and methods

# carnot_EventConditionTypeType class attributes and methods
carnot_EventConditionTypeType_activityCondition: Property = Property(name="activityCondition", type=StringType)
carnot_EventConditionTypeType_binderClass: Property = Property(name="binderClass", type=StringType)
carnot_EventConditionTypeType_implementation: Property = Property(name="implementation", type=StringType)
carnot_EventConditionTypeType_panelClass: Property = Property(name="panelClass", type=StringType)
carnot_EventConditionTypeType_processCondition: Property = Property(name="processCondition", type=StringType)
carnot_EventConditionTypeType_pullEventEmitterClass: Property = Property(name="pullEventEmitterClass", type=StringType)
carnot_EventConditionTypeType_rule: Property = Property(name="rule", type=StringType)
carnot_EventConditionTypeType.attributes={carnot_EventConditionTypeType_pullEventEmitterClass, carnot_EventConditionTypeType_rule, carnot_EventConditionTypeType_panelClass, carnot_EventConditionTypeType_implementation, carnot_EventConditionTypeType_processCondition, carnot_EventConditionTypeType_binderClass, carnot_EventConditionTypeType_activityCondition}

# carnot_UnbindActionType class attributes and methods

# carnot_IdRef class attributes and methods
carnot_IdRef_ref: Property = Property(name="ref", type=StringType)
carnot_IdRef.attributes={carnot_IdRef_ref}

# carnot_ExternalPackage class attributes and methods

# carnot_IdRefOwner class attributes and methods

# carnot_LinkTypeType class attributes and methods
carnot_LinkTypeType_sourceClass: Property = Property(name="sourceClass", type=StringType)
carnot_LinkTypeType_sourceCardinality: Property = Property(name="sourceCardinality", type=StringType)
carnot_LinkTypeType_sourceRole: Property = Property(name="sourceRole", type=StringType)
carnot_LinkTypeType_targetCardinality: Property = Property(name="targetCardinality", type=StringType)
carnot_LinkTypeType_lineStyle: Property = Property(name="lineStyle", type=StringType)
carnot_LinkTypeType_lineColor: Property = Property(name="lineColor", type=StringType)
carnot_LinkTypeType_targetRole: Property = Property(name="targetRole", type=StringType)
carnot_LinkTypeType_targetClass: Property = Property(name="targetClass", type=StringType)
carnot_LinkTypeType_sourceSymbol: Property = Property(name="sourceSymbol", type=StringType)
carnot_LinkTypeType_targetSymbol: Property = Property(name="targetSymbol", type=StringType)
carnot_LinkTypeType_showRoleNames: Property = Property(name="showRoleNames", type=StringType)
carnot_LinkTypeType_showLinkTypeName: Property = Property(name="showLinkTypeName", type=StringType)
carnot_LinkTypeType.attributes={carnot_LinkTypeType_targetCardinality, carnot_LinkTypeType_showLinkTypeName, carnot_LinkTypeType_sourceCardinality, carnot_LinkTypeType_targetClass, carnot_LinkTypeType_targetSymbol, carnot_LinkTypeType_sourceRole, carnot_LinkTypeType_sourceSymbol, carnot_LinkTypeType_showRoleNames, carnot_LinkTypeType_lineStyle, carnot_LinkTypeType_lineColor, carnot_LinkTypeType_sourceClass, carnot_LinkTypeType_targetRole}

# ISwimlaneSymbol class attributes and methods

# carnot_ModelerType class attributes and methods
carnot_ModelerType_email: Property = Property(name="email", type=StringType)
carnot_ModelerType_password: Property = Property(name="password", type=StringType)
carnot_ModelerType.attributes={carnot_ModelerType_email, carnot_ModelerType_password}

# carnot_TriggerTypeType class attributes and methods
carnot_TriggerTypeType_panelClass: Property = Property(name="panelClass", type=StringType)
carnot_TriggerTypeType_pullTrigger: Property = Property(name="pullTrigger", type=StringType)
carnot_TriggerTypeType_pullTriggerEvaluator: Property = Property(name="pullTriggerEvaluator", type=StringType)
carnot_TriggerTypeType_rule: Property = Property(name="rule", type=StringType)
carnot_TriggerTypeType.attributes={carnot_TriggerTypeType_rule, carnot_TriggerTypeType_panelClass, carnot_TriggerTypeType_pullTrigger, carnot_TriggerTypeType_pullTriggerEvaluator}

# carnot_ExternalPackages class attributes and methods

# carnot_ScriptType class attributes and methods

# carnot_TypeDeclarationsType class attributes and methods

# carnot_QualityControlType class attributes and methods

# carnot_RoleType class attributes and methods
carnot_RoleType_cardinality: Property = Property(name="cardinality", type=IntegerType)
carnot_RoleType.attributes={carnot_RoleType_cardinality}

# carnot_OrganizationType class attributes and methods

# carnot_ViewType class attributes and methods
carnot_ViewType_name: Property = Property(name="name", type=StringType)
carnot_ViewType.attributes={carnot_ViewType_name}

# carnot_TriggerType class attributes and methods

# carnot_FormalParametersType class attributes and methods

# FormalParameterMappingsType class attributes and methods

# carnot_ViewableType class attributes and methods

# extensions_carnot_FormalParameterType class attributes and methods

# carnot_extensions_FormalParameterMappingsType class attributes and methods
carnot_extensions_FormalParameterMappingsType_m_getMappedData: Method = Method(name="getMappedData", parameters={Parameter(name='formalParameter')}, type=StringType)
carnot_extensions_FormalParameterMappingsType_m_setMappedData: Method = Method(name="setMappedData", parameters={Parameter(name='data'), Parameter(name='formalParameter')})
carnot_extensions_FormalParameterMappingsType.methods={carnot_extensions_FormalParameterMappingsType_m_getMappedData, carnot_extensions_FormalParameterMappingsType_m_setMappedData}

# FormalParameterMappingType class attributes and methods

# carnot_extensions_FormalParameterMappingType class attributes and methods

# extensions_carnot_DataType class attributes and methods

# Relationships
attribute0: BinaryAssociation = BinaryAssociation(
    name="attribute0",
    ends={
        Property(name="carnot_AttributeType", type=carnot_IExtensibleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_IExtensibleElement", type=carnot_AttributeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute1: BinaryAssociation = BinaryAssociation(
    name="attribute1",
    ends={
        Property(name="AttributeType", type=carnot_IdentifiableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="reference", type=carnot_AttributeType, multiplicity=Multiplicity(0, 1))
    }
)
identifiable2: BinaryAssociation = BinaryAssociation(
    name="identifiable2",
    ends={
        Property(name="carnot_EObject", type=carnot_IdentifiableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_IdentifiableReference", type=carnot_EObject, multiplicity=Multiplicity(0, 1))
    }
)
description3: BinaryAssociation = BinaryAssociation(
    name="description3",
    ends={
        Property(name="carnot_DescriptionType", type=carnot_IIdentifiableModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_IIdentifiableModelElement", type=carnot_DescriptionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventHandler4: BinaryAssociation = BinaryAssociation(
    name="eventHandler4",
    ends={
        Property(name="carnot_EventHandlerType", type=carnot_IEventHandlerOwner, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_IEventHandlerOwner", type=carnot_EventHandlerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accessPoint5: BinaryAssociation = BinaryAssociation(
    name="accessPoint5",
    ends={
        Property(name="carnot_AccessPointType", type=carnot_IAccessPointOwner, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_IAccessPointOwner", type=carnot_AccessPointType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitySymbol6: BinaryAssociation = BinaryAssociation(
    name="activitySymbol6",
    ends={
        Property(name="carnot_ActivitySymbolType", type=carnot_ISymbolContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ISymbolContainer", type=carnot_ActivitySymbolType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotationSymbol7: BinaryAssociation = BinaryAssociation(
    name="annotationSymbol7",
    ends={
        Property(name="carnot_AnnotationSymbolType", type=carnot_ISymbolContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ISymbolContainer8", type=carnot_AnnotationSymbolType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
applicationSymbol9: BinaryAssociation = BinaryAssociation(
    name="applicationSymbol9",
    ends={
        Property(name="carnot_ApplicationSymbolType", type=carnot_ISymbolContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ISymbolContainer10", type=carnot_ApplicationSymbolType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conditionalPerformerSymbol11: BinaryAssociation = BinaryAssociation(
    name="conditionalPerformerSymbol11",
    ends={
        Property(name="carnot_ConditionalPerformerSymbolType", type=carnot_ISymbolContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ISymbolContainer12", type=carnot_ConditionalPerformerSymbolType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataSymbol13: BinaryAssociation = BinaryAssociation(
    name="dataSymbol13",
    ends={
        Property(name="carnot_DataSymbolType", type=carnot_ISymbolContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ISymbolContainer14", type=carnot_DataSymbolType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endEventSymbols15: BinaryAssociation = BinaryAssociation(
    name="endEventSymbols15",
    ends={
        Property(name="carnot_EndEventSymbol", type=carnot_ISymbolContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ISymbolContainer16", type=carnot_EndEventSymbol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gatewaySymbol17: BinaryAssociation = BinaryAssociation(
    name="gatewaySymbol17",
    ends={
        Property(name="carnot_GatewaySymbol", type=carnot_ISymbolContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ISymbolContainer18", type=carnot_GatewaySymbol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groupSymbol19: BinaryAssociation = BinaryAssociation(
    name="groupSymbol19",
    ends={
        Property(name="carnot_GroupSymbolType", type=carnot_ISymbolContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ISymbolContainer20", type=carnot_GroupSymbolType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateEventSymbols21: BinaryAssociation = BinaryAssociation(
    name="intermediateEventSymbols21",
    ends={
        Property(name="carnot_IntermediateEventSymbol", type=carnot_ISymbolContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ISymbolContainer22", type=carnot_IntermediateEventSymbol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelerSymbol23: BinaryAssociation = BinaryAssociation(
    name="modelerSymbol23",
    ends={
        Property(name="carnot_ModelerSymbolType", type=carnot_ISymbolContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ISymbolContainer24", type=carnot_ModelerSymbolType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
organizationSymbol25: BinaryAssociation = BinaryAssociation(
    name="organizationSymbol25",
    ends={
        Property(name="carnot_OrganizationSymbolType", type=carnot_ISymbolContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ISymbolContainer26", type=carnot_OrganizationSymbolType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processSymbol27: BinaryAssociation = BinaryAssociation(
    name="processSymbol27",
    ends={
        Property(name="carnot_ProcessSymbolType", type=carnot_ISymbolContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ISymbolContainer28", type=carnot_ProcessSymbolType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processInterfaceSymbols29: BinaryAssociation = BinaryAssociation(
    name="processInterfaceSymbols29",
    ends={
        Property(name="carnot_PublicInterfaceSymbol", type=carnot_ISymbolContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ISymbolContainer30", type=carnot_PublicInterfaceSymbol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
roleSymbol31: BinaryAssociation = BinaryAssociation(
    name="roleSymbol31",
    ends={
        Property(name="carnot_RoleSymbolType", type=carnot_ISymbolContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ISymbolContainer32", type=carnot_RoleSymbolType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
startEventSymbols33: BinaryAssociation = BinaryAssociation(
    name="startEventSymbols33",
    ends={
        Property(name="carnot_StartEventSymbol", type=carnot_ISymbolContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ISymbolContainer34", type=carnot_StartEventSymbol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
textSymbol35: BinaryAssociation = BinaryAssociation(
    name="textSymbol35",
    ends={
        Property(name="carnot_TextSymbolType", type=carnot_ISymbolContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ISymbolContainer36", type=carnot_TextSymbolType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataMappingConnection37: BinaryAssociation = BinaryAssociation(
    name="dataMappingConnection37",
    ends={
        Property(name="carnot_DataMappingConnectionType", type=carnot_ISymbolContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ISymbolContainer38", type=carnot_DataMappingConnectionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
executedByConnection39: BinaryAssociation = BinaryAssociation(
    name="executedByConnection39",
    ends={
        Property(name="carnot_ExecutedByConnectionType", type=carnot_ISymbolContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ISymbolContainer40", type=carnot_ExecutedByConnectionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
genericLinkConnection41: BinaryAssociation = BinaryAssociation(
    name="genericLinkConnection41",
    ends={
        Property(name="carnot_GenericLinkConnectionType", type=carnot_ISymbolContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ISymbolContainer42", type=carnot_GenericLinkConnectionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
partOfConnection43: BinaryAssociation = BinaryAssociation(
    name="partOfConnection43",
    ends={
        Property(name="carnot_PartOfConnectionType", type=carnot_ISymbolContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ISymbolContainer44", type=carnot_PartOfConnectionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
performsConnection45: BinaryAssociation = BinaryAssociation(
    name="performsConnection45",
    ends={
        Property(name="carnot_PerformsConnectionType", type=carnot_ISymbolContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ISymbolContainer46", type=carnot_PerformsConnectionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triggersConnection47: BinaryAssociation = BinaryAssociation(
    name="triggersConnection47",
    ends={
        Property(name="carnot_TriggersConnectionType", type=carnot_ISymbolContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ISymbolContainer48", type=carnot_TriggersConnectionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refersToConnection49: BinaryAssociation = BinaryAssociation(
    name="refersToConnection49",
    ends={
        Property(name="carnot_RefersToConnectionType", type=carnot_ISymbolContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ISymbolContainer50", type=carnot_RefersToConnectionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subProcessOfConnection51: BinaryAssociation = BinaryAssociation(
    name="subProcessOfConnection51",
    ends={
        Property(name="carnot_SubProcessOfConnectionType", type=carnot_ISymbolContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ISymbolContainer52", type=carnot_SubProcessOfConnectionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitionConnection53: BinaryAssociation = BinaryAssociation(
    name="transitionConnection53",
    ends={
        Property(name="carnot_TransitionConnectionType", type=carnot_ISymbolContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ISymbolContainer54", type=carnot_TransitionConnectionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
worksForConnection55: BinaryAssociation = BinaryAssociation(
    name="worksForConnection55",
    ends={
        Property(name="carnot_WorksForConnectionType", type=carnot_ISymbolContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ISymbolContainer56", type=carnot_WorksForConnectionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
teamLeadConnection57: BinaryAssociation = BinaryAssociation(
    name="teamLeadConnection57",
    ends={
        Property(name="carnot_TeamLeadConnectionType", type=carnot_ISymbolContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ISymbolContainer58", type=carnot_TeamLeadConnectionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referingToConnections59: BinaryAssociation = BinaryAssociation(
    name="referingToConnections59",
    ends={
        Property(name="RefersToConnectionType", type=carnot_IGraphicalObject, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=carnot_RefersToConnectionType, multiplicity=Multiplicity(0, 9999))
    }
)
referingFromConnections60: BinaryAssociation = BinaryAssociation(
    name="referingFromConnections60",
    ends={
        Property(name="RefersToConnectionType61", type=carnot_IGraphicalObject, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=carnot_RefersToConnectionType, multiplicity=Multiplicity(0, 9999))
    }
)
inLinks62: BinaryAssociation = BinaryAssociation(
    name="inLinks62",
    ends={
        Property(name="GenericLinkConnectionType", type=carnot_INodeSymbol, multiplicity=Multiplicity(1, 1)),
        Property(name="targetSymbol", type=carnot_GenericLinkConnectionType, multiplicity=Multiplicity(0, 9999))
    }
)
outLinks63: BinaryAssociation = BinaryAssociation(
    name="outLinks63",
    ends={
        Property(name="GenericLinkConnectionType64", type=carnot_INodeSymbol, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceSymbol", type=carnot_GenericLinkConnectionType, multiplicity=Multiplicity(0, 9999))
    }
)
participant65: BinaryAssociation = BinaryAssociation(
    name="participant65",
    ends={
        Property(name="IModelParticipant", type=carnot_ISwimlaneSymbol, multiplicity=Multiplicity(1, 1)),
        Property(name="performedSwimlanes", type=carnot_IModelParticipant, multiplicity=Multiplicity(0, 1))
    }
)
childLanes66: BinaryAssociation = BinaryAssociation(
    name="childLanes66",
    ends={
        Property(name="LaneSymbol", type=carnot_ISwimlaneSymbol, multiplicity=Multiplicity(1, 1)),
        Property(name="parentLane", type=carnot_LaneSymbol, multiplicity=Multiplicity(0, 9999))
    }
)
participantReference67: BinaryAssociation = BinaryAssociation(
    name="participantReference67",
    ends={
        Property(name="carnot_IModelParticipant", type=carnot_ISwimlaneSymbol, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ISwimlaneSymbol", type=carnot_IModelParticipant, multiplicity=Multiplicity(0, 1))
    }
)
inTransitions68: BinaryAssociation = BinaryAssociation(
    name="inTransitions68",
    ends={
        Property(name="TransitionConnectionType", type=carnot_IFlowObjectSymbol, multiplicity=Multiplicity(1, 1)),
        Property(name="targetActivitySymbol", type=carnot_TransitionConnectionType, multiplicity=Multiplicity(0, 9999))
    }
)
outTransitions69: BinaryAssociation = BinaryAssociation(
    name="outTransitions69",
    ends={
        Property(name="TransitionConnectionType70", type=carnot_IFlowObjectSymbol, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceActivitySymbol", type=carnot_TransitionConnectionType, multiplicity=Multiplicity(0, 9999))
    }
)
type80: BinaryAssociation = BinaryAssociation(
    name="type80",
    ends={
        Property(name="carnot_DataTypeType", type=carnot_AccessPointType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_AccessPointType81", type=carnot_DataTypeType, multiplicity=Multiplicity(0, 1))
    }
)
coordinates71: BinaryAssociation = BinaryAssociation(
    name="coordinates71",
    ends={
        Property(name="carnot_Coordinates", type=carnot_IConnectionSymbol, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_IConnectionSymbol", type=carnot_Coordinates, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
performedActivities72: BinaryAssociation = BinaryAssociation(
    name="performedActivities72",
    ends={
        Property(name="ActivityType", type=carnot_IModelParticipant, multiplicity=Multiplicity(1, 1)),
        Property(name="performer", type=carnot_ActivityType, multiplicity=Multiplicity(0, 9999))
    }
)
performedSwimlanes73: BinaryAssociation = BinaryAssociation(
    name="performedSwimlanes73",
    ends={
        Property(name="ISwimlaneSymbol", type=carnot_IModelParticipant, multiplicity=Multiplicity(1, 1)),
        Property(name="participant", type=carnot_ISwimlaneSymbol, multiplicity=Multiplicity(0, 9999))
    }
)
participantAssociations74: BinaryAssociation = BinaryAssociation(
    name="participantAssociations74",
    ends={
        Property(name="ParticipantType", type=carnot_IModelParticipant, multiplicity=Multiplicity(1, 1)),
        Property(name="participant75", type=carnot_ParticipantType, multiplicity=Multiplicity(0, 9999))
    }
)
performedActivities76: BinaryAssociation = BinaryAssociation(
    name="performedActivities76",
    ends={
        Property(name="PerformsConnectionType", type=carnot_IModelParticipantSymbol, multiplicity=Multiplicity(1, 1)),
        Property(name="participantSymbol", type=carnot_PerformsConnectionType, multiplicity=Multiplicity(0, 9999))
    }
)
triggeredEvents77: BinaryAssociation = BinaryAssociation(
    name="triggeredEvents77",
    ends={
        Property(name="TriggersConnectionType", type=carnot_IModelParticipantSymbol, multiplicity=Multiplicity(1, 1)),
        Property(name="participantSymbol78", type=carnot_TriggersConnectionType, multiplicity=Multiplicity(0, 9999))
    }
)
type79: BinaryAssociation = BinaryAssociation(
    name="type79",
    ends={
        Property(name="EventActionTypeType", type=carnot_AbstractEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="actionInstances", type=carnot_EventActionTypeType, multiplicity=Multiplicity(0, 1))
    }
)
activity82: BinaryAssociation = BinaryAssociation(
    name="activity82",
    ends={
        Property(name="ActivityType83", type=carnot_ActivitySymbolType, multiplicity=Multiplicity(1, 1)),
        Property(name="activitySymbols", type=carnot_ActivityType, multiplicity=Multiplicity(1, 1))
    }
)
performsConnections84: BinaryAssociation = BinaryAssociation(
    name="performsConnections84",
    ends={
        Property(name="PerformsConnectionType85", type=carnot_ActivitySymbolType, multiplicity=Multiplicity(1, 1)),
        Property(name="activitySymbol", type=carnot_PerformsConnectionType, multiplicity=Multiplicity(0, 9999))
    }
)
executedByConnections86: BinaryAssociation = BinaryAssociation(
    name="executedByConnections86",
    ends={
        Property(name="ExecutedByConnectionType", type=carnot_ActivitySymbolType, multiplicity=Multiplicity(1, 1)),
        Property(name="activitySymbol87", type=carnot_ExecutedByConnectionType, multiplicity=Multiplicity(0, 9999))
    }
)
dataMappings88: BinaryAssociation = BinaryAssociation(
    name="dataMappings88",
    ends={
        Property(name="DataMappingConnectionType", type=carnot_ActivitySymbolType, multiplicity=Multiplicity(1, 1)),
        Property(name="activitySymbol89", type=carnot_DataMappingConnectionType, multiplicity=Multiplicity(0, 9999))
    }
)
gatewaySymbols90: BinaryAssociation = BinaryAssociation(
    name="gatewaySymbols90",
    ends={
        Property(name="GatewaySymbol", type=carnot_ActivitySymbolType, multiplicity=Multiplicity(1, 1)),
        Property(name="activitySymbol91", type=carnot_GatewaySymbol, multiplicity=Multiplicity(0, 9999))
    }
)
dataMapping92: BinaryAssociation = BinaryAssociation(
    name="dataMapping92",
    ends={
        Property(name="carnot_DataMappingType", type=carnot_ActivityType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ActivityType", type=carnot_DataMappingType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
application93: BinaryAssociation = BinaryAssociation(
    name="application93",
    ends={
        Property(name="ApplicationType", type=carnot_ActivityType, multiplicity=Multiplicity(1, 1)),
        Property(name="executedActivities", type=carnot_ApplicationType, multiplicity=Multiplicity(0, 1))
    }
)
startingEventSymbols101: BinaryAssociation = BinaryAssociation(
    name="startingEventSymbols101",
    ends={
        Property(name="StartEventSymbol", type=carnot_ActivityType, multiplicity=Multiplicity(1, 1)),
        Property(name="startActivity", type=carnot_StartEventSymbol, multiplicity=Multiplicity(0, 9999))
    }
)
inTransitions102: BinaryAssociation = BinaryAssociation(
    name="inTransitions102",
    ends={
        Property(name="TransitionType", type=carnot_ActivityType, multiplicity=Multiplicity(1, 1)),
        Property(name="to103", type=carnot_TransitionType, multiplicity=Multiplicity(0, 9999))
    }
)
outTransitions104: BinaryAssociation = BinaryAssociation(
    name="outTransitions104",
    ends={
        Property(name="TransitionType106", type=carnot_ActivityType, multiplicity=Multiplicity(1, 1)),
        Property(name="from105", type=carnot_TransitionType, multiplicity=Multiplicity(0, 9999))
    }
)
validQualityCodes107: BinaryAssociation = BinaryAssociation(
    name="validQualityCodes107",
    ends={
        Property(name="carnot_Code", type=carnot_ActivityType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ActivityType108", type=carnot_Code, multiplicity=Multiplicity(0, 9999))
    }
)
implementationProcess94: BinaryAssociation = BinaryAssociation(
    name="implementationProcess94",
    ends={
        Property(name="ProcessDefinitionType", type=carnot_ActivityType, multiplicity=Multiplicity(1, 1)),
        Property(name="executingActivities", type=carnot_ProcessDefinitionType, multiplicity=Multiplicity(0, 1))
    }
)
performer95: BinaryAssociation = BinaryAssociation(
    name="performer95",
    ends={
        Property(name="IModelParticipant96", type=carnot_ActivityType, multiplicity=Multiplicity(1, 1)),
        Property(name="performedActivities", type=carnot_IModelParticipant, multiplicity=Multiplicity(0, 1))
    }
)
qualityControlPerformer97: BinaryAssociation = BinaryAssociation(
    name="qualityControlPerformer97",
    ends={
        Property(name="carnot_IModelParticipant99", type=carnot_ActivityType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ActivityType98", type=carnot_IModelParticipant, multiplicity=Multiplicity(0, 1))
    }
)
activitySymbols100: BinaryAssociation = BinaryAssociation(
    name="activitySymbols100",
    ends={
        Property(name="ActivitySymbolType", type=carnot_ActivityType, multiplicity=Multiplicity(1, 1)),
        Property(name="activity", type=carnot_ActivitySymbolType, multiplicity=Multiplicity(0, 9999))
    }
)
application116: BinaryAssociation = BinaryAssociation(
    name="application116",
    ends={
        Property(name="ApplicationType117", type=carnot_ApplicationSymbolType, multiplicity=Multiplicity(1, 1)),
        Property(name="applicationSymbols", type=carnot_ApplicationType, multiplicity=Multiplicity(1, 1))
    }
)
context118: BinaryAssociation = BinaryAssociation(
    name="context118",
    ends={
        Property(name="carnot_ContextType", type=carnot_ApplicationType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ApplicationType", type=carnot_ContextType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loop109: BinaryAssociation = BinaryAssociation(
    name="loop109",
    ends={
        Property(name="carnot_LoopType", type=carnot_ActivityType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ActivityType110", type=carnot_LoopType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
text111: BinaryAssociation = BinaryAssociation(
    name="text111",
    ends={
        Property(name="carnot_TextType", type=carnot_AnnotationSymbolType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_AnnotationSymbolType112", type=carnot_TextType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contexts113: BinaryAssociation = BinaryAssociation(
    name="contexts113",
    ends={
        Property(name="ContextType", type=carnot_ApplicationContextTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=carnot_ContextType, multiplicity=Multiplicity(0, 9999))
    }
)
executingActivities114: BinaryAssociation = BinaryAssociation(
    name="executingActivities114",
    ends={
        Property(name="ExecutedByConnectionType115", type=carnot_ApplicationSymbolType, multiplicity=Multiplicity(1, 1)),
        Property(name="applicationSymbol", type=carnot_ExecutedByConnectionType, multiplicity=Multiplicity(0, 9999))
    }
)
type119: BinaryAssociation = BinaryAssociation(
    name="type119",
    ends={
        Property(name="ApplicationTypeType", type=carnot_ApplicationType, multiplicity=Multiplicity(1, 1)),
        Property(name="applications", type=carnot_ApplicationTypeType, multiplicity=Multiplicity(0, 1))
    }
)
executedActivities120: BinaryAssociation = BinaryAssociation(
    name="executedActivities120",
    ends={
        Property(name="ActivityType121", type=carnot_ApplicationType, multiplicity=Multiplicity(1, 1)),
        Property(name="application", type=carnot_ActivityType, multiplicity=Multiplicity(0, 9999))
    }
)
applicationSymbols122: BinaryAssociation = BinaryAssociation(
    name="applicationSymbols122",
    ends={
        Property(name="ApplicationSymbolType", type=carnot_ApplicationType, multiplicity=Multiplicity(1, 1)),
        Property(name="application123", type=carnot_ApplicationSymbolType, multiplicity=Multiplicity(0, 9999))
    }
)
reference129: BinaryAssociation = BinaryAssociation(
    name="reference129",
    ends={
        Property(name="IdentifiableReference", type=carnot_AttributeType, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=carnot_IdentifiableReference, multiplicity=Multiplicity(0, 1))
    }
)
applications124: BinaryAssociation = BinaryAssociation(
    name="applications124",
    ends={
        Property(name="ApplicationType126", type=carnot_ApplicationTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="type125", type=carnot_ApplicationType, multiplicity=Multiplicity(0, 9999))
    }
)
valueNode127: BinaryAssociation = BinaryAssociation(
    name="valueNode127",
    ends={
        Property(name="carnot_XmlTextNode", type=carnot_AttributeType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_AttributeType128", type=carnot_XmlTextNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
description134: BinaryAssociation = BinaryAssociation(
    name="description134",
    ends={
        Property(name="carnot_DescriptionType136", type=carnot_ContextType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ContextType135", type=carnot_DescriptionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type137: BinaryAssociation = BinaryAssociation(
    name="type137",
    ends={
        Property(name="ApplicationContextTypeType", type=carnot_ContextType, multiplicity=Multiplicity(1, 1)),
        Property(name="contexts", type=carnot_ApplicationContextTypeType, multiplicity=Multiplicity(0, 1))
    }
)
participant130: BinaryAssociation = BinaryAssociation(
    name="participant130",
    ends={
        Property(name="ConditionalPerformerType", type=carnot_ConditionalPerformerSymbolType, multiplicity=Multiplicity(1, 1)),
        Property(name="conditionalPerformerSymbols", type=carnot_ConditionalPerformerType, multiplicity=Multiplicity(1, 1))
    }
)
data131: BinaryAssociation = BinaryAssociation(
    name="data131",
    ends={
        Property(name="DataType", type=carnot_ConditionalPerformerType, multiplicity=Multiplicity(1, 1)),
        Property(name="conditionalPerformers", type=carnot_DataType, multiplicity=Multiplicity(1, 1))
    }
)
conditionalPerformerSymbols132: BinaryAssociation = BinaryAssociation(
    name="conditionalPerformerSymbols132",
    ends={
        Property(name="ConditionalPerformerSymbolType", type=carnot_ConditionalPerformerType, multiplicity=Multiplicity(1, 1)),
        Property(name="participant133", type=carnot_ConditionalPerformerSymbolType, multiplicity=Multiplicity(0, 9999))
    }
)
data145: BinaryAssociation = BinaryAssociation(
    name="data145",
    ends={
        Property(name="DataType146", type=carnot_DataPathType, multiplicity=Multiplicity(1, 1)),
        Property(name="dataPaths", type=carnot_DataType, multiplicity=Multiplicity(1, 1))
    }
)
activitySymbol138: BinaryAssociation = BinaryAssociation(
    name="activitySymbol138",
    ends={
        Property(name="ActivitySymbolType139", type=carnot_DataMappingConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="dataMappings", type=carnot_ActivitySymbolType, multiplicity=Multiplicity(1, 1))
    }
)
dataSymbol140: BinaryAssociation = BinaryAssociation(
    name="dataSymbol140",
    ends={
        Property(name="DataSymbolType", type=carnot_DataMappingConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="dataMappings141", type=carnot_DataSymbolType, multiplicity=Multiplicity(1, 1))
    }
)
data142: BinaryAssociation = BinaryAssociation(
    name="data142",
    ends={
        Property(name="DataType144", type=carnot_DataMappingType, multiplicity=Multiplicity(1, 1)),
        Property(name="dataMappings143", type=carnot_DataType, multiplicity=Multiplicity(1, 1))
    }
)
dataSymbols154: BinaryAssociation = BinaryAssociation(
    name="dataSymbols154",
    ends={
        Property(name="DataSymbolType156", type=carnot_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="data155", type=carnot_DataSymbolType, multiplicity=Multiplicity(0, 9999))
    }
)
conditionalPerformers157: BinaryAssociation = BinaryAssociation(
    name="conditionalPerformers157",
    ends={
        Property(name="ConditionalPerformerType159", type=carnot_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="data158", type=carnot_ConditionalPerformerType, multiplicity=Multiplicity(0, 9999))
    }
)
dataPaths160: BinaryAssociation = BinaryAssociation(
    name="dataPaths160",
    ends={
        Property(name="DataPathType", type=carnot_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="data161", type=carnot_DataPathType, multiplicity=Multiplicity(0, 9999))
    }
)
parameterMappings162: BinaryAssociation = BinaryAssociation(
    name="parameterMappings162",
    ends={
        Property(name="ParameterMappingType", type=carnot_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="data163", type=carnot_ParameterMappingType, multiplicity=Multiplicity(0, 9999))
    }
)
data147: BinaryAssociation = BinaryAssociation(
    name="data147",
    ends={
        Property(name="DataType148", type=carnot_DataSymbolType, multiplicity=Multiplicity(1, 1)),
        Property(name="dataSymbols", type=carnot_DataType, multiplicity=Multiplicity(1, 1))
    }
)
dataMappings149: BinaryAssociation = BinaryAssociation(
    name="dataMappings149",
    ends={
        Property(name="DataMappingConnectionType150", type=carnot_DataSymbolType, multiplicity=Multiplicity(1, 1)),
        Property(name="dataSymbol", type=carnot_DataMappingConnectionType, multiplicity=Multiplicity(0, 9999))
    }
)
dataMappings151: BinaryAssociation = BinaryAssociation(
    name="dataMappings151",
    ends={
        Property(name="DataMappingType", type=carnot_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="data", type=carnot_DataMappingType, multiplicity=Multiplicity(0, 9999))
    }
)
type152: BinaryAssociation = BinaryAssociation(
    name="type152",
    ends={
        Property(name="DataTypeType", type=carnot_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="data153", type=carnot_DataTypeType, multiplicity=Multiplicity(0, 1))
    }
)
poolSymbols168: BinaryAssociation = BinaryAssociation(
    name="poolSymbols168",
    ends={
        Property(name="PoolSymbol", type=carnot_DiagramType, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram", type=carnot_PoolSymbol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalReference164: BinaryAssociation = BinaryAssociation(
    name="externalReference164",
    ends={
        Property(name="carnot_ExternalReferenceType", type=carnot_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_DataType", type=carnot_ExternalReferenceType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
data165: BinaryAssociation = BinaryAssociation(
    name="data165",
    ends={
        Property(name="DataType167", type=carnot_DataTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="type166", type=carnot_DataType, multiplicity=Multiplicity(0, 9999))
    }
)
xMLNSPrefixMap169: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap169",
    ends={
        Property(name="carnot_EStringToStringMapEntry", type=carnot_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_DocumentRoot", type=carnot_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation170: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation170",
    ends={
        Property(name="carnot_EStringToStringMapEntry172", type=carnot_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_DocumentRoot171", type=carnot_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model173: BinaryAssociation = BinaryAssociation(
    name="model173",
    ends={
        Property(name="carnot_ModelType", type=carnot_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_DocumentRoot174", type=carnot_ModelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventHandlers177: BinaryAssociation = BinaryAssociation(
    name="eventHandlers177",
    ends={
        Property(name="EventHandlerType", type=carnot_EventConditionTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="type178", type=carnot_EventHandlerType, multiplicity=Multiplicity(0, 9999))
    }
)
bindAction179: BinaryAssociation = BinaryAssociation(
    name="bindAction179",
    ends={
        Property(name="carnot_BindActionType", type=carnot_EventHandlerType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_EventHandlerType180", type=carnot_BindActionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionInstances175: BinaryAssociation = BinaryAssociation(
    name="actionInstances175",
    ends={
        Property(name="AbstractEventAction", type=carnot_EventActionTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="type176", type=carnot_AbstractEventAction, multiplicity=Multiplicity(0, 9999))
    }
)
activitySymbol186: BinaryAssociation = BinaryAssociation(
    name="activitySymbol186",
    ends={
        Property(name="ActivitySymbolType187", type=carnot_ExecutedByConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="executedByConnections", type=carnot_ActivitySymbolType, multiplicity=Multiplicity(1, 1))
    }
)
applicationSymbol188: BinaryAssociation = BinaryAssociation(
    name="applicationSymbol188",
    ends={
        Property(name="ApplicationSymbolType190", type=carnot_ExecutedByConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="executingActivities189", type=carnot_ApplicationSymbolType, multiplicity=Multiplicity(1, 1))
    }
)
eventAction181: BinaryAssociation = BinaryAssociation(
    name="eventAction181",
    ends={
        Property(name="carnot_EventActionType", type=carnot_EventHandlerType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_EventHandlerType182", type=carnot_EventActionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unbindAction183: BinaryAssociation = BinaryAssociation(
    name="unbindAction183",
    ends={
        Property(name="carnot_UnbindActionType", type=carnot_EventHandlerType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_EventHandlerType184", type=carnot_UnbindActionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type185: BinaryAssociation = BinaryAssociation(
    name="type185",
    ends={
        Property(name="EventConditionTypeType", type=carnot_EventHandlerType, multiplicity=Multiplicity(1, 1)),
        Property(name="eventHandlers", type=carnot_EventConditionTypeType, multiplicity=Multiplicity(0, 1))
    }
)
sourceSymbol197: BinaryAssociation = BinaryAssociation(
    name="sourceSymbol197",
    ends={
        Property(name="INodeSymbol", type=carnot_GenericLinkConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="outLinks", type=carnot_INodeSymbol, multiplicity=Multiplicity(1, 1))
    }
)
targetSymbol198: BinaryAssociation = BinaryAssociation(
    name="targetSymbol198",
    ends={
        Property(name="INodeSymbol199", type=carnot_GenericLinkConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="inLinks", type=carnot_INodeSymbol, multiplicity=Multiplicity(1, 1))
    }
)
packageRef191: BinaryAssociation = BinaryAssociation(
    name="packageRef191",
    ends={
        Property(name="carnot_ExternalPackage", type=carnot_IdRef, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_IdRef", type=carnot_ExternalPackage, multiplicity=Multiplicity(0, 1))
    }
)
externalRef192: BinaryAssociation = BinaryAssociation(
    name="externalRef192",
    ends={
        Property(name="carnot_IdRef193", type=carnot_IdRefOwner, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_IdRefOwner", type=carnot_IdRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
activitySymbol194: BinaryAssociation = BinaryAssociation(
    name="activitySymbol194",
    ends={
        Property(name="ActivitySymbolType195", type=carnot_GatewaySymbol, multiplicity=Multiplicity(1, 1)),
        Property(name="gatewaySymbols", type=carnot_ActivitySymbolType, multiplicity=Multiplicity(1, 1))
    }
)
linkType196: BinaryAssociation = BinaryAssociation(
    name="linkType196",
    ends={
        Property(name="LinkTypeType", type=carnot_GenericLinkConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="linkInstances", type=carnot_LinkTypeType, multiplicity=Multiplicity(0, 1))
    }
)
parentPool200: BinaryAssociation = BinaryAssociation(
    name="parentPool200",
    ends={
        Property(name="PoolSymbol201", type=carnot_LaneSymbol, multiplicity=Multiplicity(1, 1)),
        Property(name="lanes", type=carnot_PoolSymbol, multiplicity=Multiplicity(1, 1))
    }
)
parentLane202: BinaryAssociation = BinaryAssociation(
    name="parentLane202",
    ends={
        Property(name="ISwimlaneSymbol203", type=carnot_LaneSymbol, multiplicity=Multiplicity(1, 1)),
        Property(name="childLanes", type=carnot_ISwimlaneSymbol, multiplicity=Multiplicity(0, 1))
    }
)
modelerSymbols207: BinaryAssociation = BinaryAssociation(
    name="modelerSymbols207",
    ends={
        Property(name="ModelerSymbolType", type=carnot_ModelerType, multiplicity=Multiplicity(1, 1)),
        Property(name="modeler", type=carnot_ModelerSymbolType, multiplicity=Multiplicity(0, 9999))
    }
)
linkInstances204: BinaryAssociation = BinaryAssociation(
    name="linkInstances204",
    ends={
        Property(name="GenericLinkConnectionType205", type=carnot_LinkTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="linkType", type=carnot_GenericLinkConnectionType, multiplicity=Multiplicity(0, 9999))
    }
)
modeler206: BinaryAssociation = BinaryAssociation(
    name="modeler206",
    ends={
        Property(name="ModelerType", type=carnot_ModelerSymbolType, multiplicity=Multiplicity(1, 1)),
        Property(name="modelerSymbols", type=carnot_ModelerType, multiplicity=Multiplicity(1, 1))
    }
)
eventActionType222: BinaryAssociation = BinaryAssociation(
    name="eventActionType222",
    ends={
        Property(name="carnot_EventActionTypeType", type=carnot_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ModelType223", type=carnot_EventActionTypeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
data224: BinaryAssociation = BinaryAssociation(
    name="data224",
    ends={
        Property(name="carnot_DataType226", type=carnot_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ModelType225", type=carnot_DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
application227: BinaryAssociation = BinaryAssociation(
    name="application227",
    ends={
        Property(name="carnot_ApplicationType229", type=carnot_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ModelType228", type=carnot_ApplicationType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
description208: BinaryAssociation = BinaryAssociation(
    name="description208",
    ends={
        Property(name="carnot_DescriptionType210", type=carnot_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ModelType209", type=carnot_DescriptionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dataType211: BinaryAssociation = BinaryAssociation(
    name="dataType211",
    ends={
        Property(name="carnot_DataTypeType213", type=carnot_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ModelType212", type=carnot_DataTypeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
applicationType214: BinaryAssociation = BinaryAssociation(
    name="applicationType214",
    ends={
        Property(name="carnot_ApplicationTypeType", type=carnot_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ModelType215", type=carnot_ApplicationTypeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
applicationContextType216: BinaryAssociation = BinaryAssociation(
    name="applicationContextType216",
    ends={
        Property(name="carnot_ApplicationContextTypeType", type=carnot_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ModelType217", type=carnot_ApplicationContextTypeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triggerType218: BinaryAssociation = BinaryAssociation(
    name="triggerType218",
    ends={
        Property(name="carnot_TriggerTypeType", type=carnot_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ModelType219", type=carnot_TriggerTypeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventConditionType220: BinaryAssociation = BinaryAssociation(
    name="eventConditionType220",
    ends={
        Property(name="carnot_EventConditionTypeType", type=carnot_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ModelType221", type=carnot_EventConditionTypeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalPackages242: BinaryAssociation = BinaryAssociation(
    name="externalPackages242",
    ends={
        Property(name="carnot_ExternalPackages", type=carnot_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ModelType243", type=carnot_ExternalPackages, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
script244: BinaryAssociation = BinaryAssociation(
    name="script244",
    ends={
        Property(name="carnot_ScriptType", type=carnot_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ModelType245", type=carnot_ScriptType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeDeclarations246: BinaryAssociation = BinaryAssociation(
    name="typeDeclarations246",
    ends={
        Property(name="carnot_TypeDeclarationsType", type=carnot_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ModelType247", type=carnot_TypeDeclarationsType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modeler230: BinaryAssociation = BinaryAssociation(
    name="modeler230",
    ends={
        Property(name="carnot_ModelerType", type=carnot_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ModelType231", type=carnot_ModelerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualityControl232: BinaryAssociation = BinaryAssociation(
    name="qualityControl232",
    ends={
        Property(name="carnot_QualityControlType", type=carnot_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ModelType233", type=carnot_QualityControlType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
role234: BinaryAssociation = BinaryAssociation(
    name="role234",
    ends={
        Property(name="carnot_RoleType", type=carnot_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ModelType235", type=carnot_RoleType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
organization236: BinaryAssociation = BinaryAssociation(
    name="organization236",
    ends={
        Property(name="carnot_OrganizationType", type=carnot_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ModelType237", type=carnot_OrganizationType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conditionalPerformer238: BinaryAssociation = BinaryAssociation(
    name="conditionalPerformer238",
    ends={
        Property(name="carnot_ConditionalPerformerType", type=carnot_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ModelType239", type=carnot_ConditionalPerformerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processDefinition240: BinaryAssociation = BinaryAssociation(
    name="processDefinition240",
    ends={
        Property(name="carnot_ProcessDefinitionType", type=carnot_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ModelType241", type=carnot_ProcessDefinitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
organization254: BinaryAssociation = BinaryAssociation(
    name="organization254",
    ends={
        Property(name="OrganizationType", type=carnot_OrganizationSymbolType, multiplicity=Multiplicity(1, 1)),
        Property(name="organizationSymbols", type=carnot_OrganizationType, multiplicity=Multiplicity(1, 1))
    }
)
diagram248: BinaryAssociation = BinaryAssociation(
    name="diagram248",
    ends={
        Property(name="carnot_DiagramType", type=carnot_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ModelType249", type=carnot_DiagramType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linkType250: BinaryAssociation = BinaryAssociation(
    name="linkType250",
    ends={
        Property(name="carnot_LinkTypeType", type=carnot_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ModelType251", type=carnot_LinkTypeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
view252: BinaryAssociation = BinaryAssociation(
    name="view252",
    ends={
        Property(name="carnot_ViewType", type=carnot_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ModelType253", type=carnot_ViewType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
data265: BinaryAssociation = BinaryAssociation(
    name="data265",
    ends={
        Property(name="DataType266", type=carnot_ParameterMappingType, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterMappings", type=carnot_DataType, multiplicity=Multiplicity(1, 1))
    }
)
superOrganizations255: BinaryAssociation = BinaryAssociation(
    name="superOrganizations255",
    ends={
        Property(name="PartOfConnectionType", type=carnot_OrganizationSymbolType, multiplicity=Multiplicity(1, 1)),
        Property(name="suborganizationSymbol", type=carnot_PartOfConnectionType, multiplicity=Multiplicity(0, 9999))
    }
)
subOrganizations256: BinaryAssociation = BinaryAssociation(
    name="subOrganizations256",
    ends={
        Property(name="PartOfConnectionType257", type=carnot_OrganizationSymbolType, multiplicity=Multiplicity(1, 1)),
        Property(name="organizationSymbol", type=carnot_PartOfConnectionType, multiplicity=Multiplicity(0, 9999))
    }
)
memberRoles258: BinaryAssociation = BinaryAssociation(
    name="memberRoles258",
    ends={
        Property(name="WorksForConnectionType", type=carnot_OrganizationSymbolType, multiplicity=Multiplicity(1, 1)),
        Property(name="organizationSymbol259", type=carnot_WorksForConnectionType, multiplicity=Multiplicity(0, 9999))
    }
)
teamLead260: BinaryAssociation = BinaryAssociation(
    name="teamLead260",
    ends={
        Property(name="TeamLeadConnectionType", type=carnot_OrganizationSymbolType, multiplicity=Multiplicity(1, 1)),
        Property(name="teamSymbol", type=carnot_TeamLeadConnectionType, multiplicity=Multiplicity(0, 9999))
    }
)
participant261: BinaryAssociation = BinaryAssociation(
    name="participant261",
    ends={
        Property(name="carnot_ParticipantType", type=carnot_OrganizationType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_OrganizationType262", type=carnot_ParticipantType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
organizationSymbols263: BinaryAssociation = BinaryAssociation(
    name="organizationSymbols263",
    ends={
        Property(name="OrganizationSymbolType", type=carnot_OrganizationType, multiplicity=Multiplicity(1, 1)),
        Property(name="organization", type=carnot_OrganizationSymbolType, multiplicity=Multiplicity(0, 9999))
    }
)
teamLead264: BinaryAssociation = BinaryAssociation(
    name="teamLead264",
    ends={
        Property(name="RoleType", type=carnot_OrganizationType, multiplicity=Multiplicity(1, 1)),
        Property(name="teams", type=carnot_RoleType, multiplicity=Multiplicity(0, 1))
    }
)
activitySymbol273: BinaryAssociation = BinaryAssociation(
    name="activitySymbol273",
    ends={
        Property(name="ActivitySymbolType274", type=carnot_PerformsConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="performsConnections", type=carnot_ActivitySymbolType, multiplicity=Multiplicity(1, 1))
    }
)
participantSymbol275: BinaryAssociation = BinaryAssociation(
    name="participantSymbol275",
    ends={
        Property(name="IModelParticipantSymbol", type=carnot_PerformsConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="performedActivities276", type=carnot_IModelParticipantSymbol, multiplicity=Multiplicity(1, 1))
    }
)
diagram277: BinaryAssociation = BinaryAssociation(
    name="diagram277",
    ends={
        Property(name="DiagramType", type=carnot_PoolSymbol, multiplicity=Multiplicity(1, 1)),
        Property(name="poolSymbols", type=carnot_DiagramType, multiplicity=Multiplicity(1, 1))
    }
)
participant267: BinaryAssociation = BinaryAssociation(
    name="participant267",
    ends={
        Property(name="IModelParticipant268", type=carnot_ParticipantType, multiplicity=Multiplicity(1, 1)),
        Property(name="participantAssociations", type=carnot_IModelParticipant, multiplicity=Multiplicity(1, 1))
    }
)
organizationSymbol269: BinaryAssociation = BinaryAssociation(
    name="organizationSymbol269",
    ends={
        Property(name="OrganizationSymbolType270", type=carnot_PartOfConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="subOrganizations", type=carnot_OrganizationSymbolType, multiplicity=Multiplicity(1, 1))
    }
)
suborganizationSymbol271: BinaryAssociation = BinaryAssociation(
    name="suborganizationSymbol271",
    ends={
        Property(name="OrganizationSymbolType272", type=carnot_PartOfConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="superOrganizations", type=carnot_OrganizationSymbolType, multiplicity=Multiplicity(1, 1))
    }
)
trigger287: BinaryAssociation = BinaryAssociation(
    name="trigger287",
    ends={
        Property(name="carnot_TriggerType", type=carnot_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ProcessDefinitionType288", type=carnot_TriggerType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataPath289: BinaryAssociation = BinaryAssociation(
    name="dataPath289",
    ends={
        Property(name="carnot_DataPathType", type=carnot_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ProcessDefinitionType290", type=carnot_DataPathType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diagram291: BinaryAssociation = BinaryAssociation(
    name="diagram291",
    ends={
        Property(name="carnot_DiagramType293", type=carnot_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ProcessDefinitionType292", type=carnot_DiagramType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
process278: BinaryAssociation = BinaryAssociation(
    name="process278",
    ends={
        Property(name="carnot_ProcessDefinitionType279", type=carnot_PoolSymbol, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_PoolSymbol", type=carnot_ProcessDefinitionType, multiplicity=Multiplicity(0, 1))
    }
)
lanes280: BinaryAssociation = BinaryAssociation(
    name="lanes280",
    ends={
        Property(name="LaneSymbol281", type=carnot_PoolSymbol, multiplicity=Multiplicity(1, 1)),
        Property(name="parentPool", type=carnot_LaneSymbol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activity282: BinaryAssociation = BinaryAssociation(
    name="activity282",
    ends={
        Property(name="carnot_ActivityType284", type=carnot_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ProcessDefinitionType283", type=carnot_ActivityType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition285: BinaryAssociation = BinaryAssociation(
    name="transition285",
    ends={
        Property(name="carnot_TransitionType", type=carnot_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ProcessDefinitionType286", type=carnot_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subProcesses303: BinaryAssociation = BinaryAssociation(
    name="subProcesses303",
    ends={
        Property(name="SubProcessOfConnectionType", type=carnot_ProcessSymbolType, multiplicity=Multiplicity(1, 1)),
        Property(name="processSymbol", type=carnot_SubProcessOfConnectionType, multiplicity=Multiplicity(0, 9999))
    }
)
parentProcesses304: BinaryAssociation = BinaryAssociation(
    name="parentProcesses304",
    ends={
        Property(name="SubProcessOfConnectionType305", type=carnot_ProcessSymbolType, multiplicity=Multiplicity(1, 1)),
        Property(name="subprocessSymbol", type=carnot_SubProcessOfConnectionType, multiplicity=Multiplicity(0, 9999))
    }
)
Code306: BinaryAssociation = BinaryAssociation(
    name="Code306",
    ends={
        Property(name="carnot_Code308", type=carnot_QualityControlType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_QualityControlType307", type=carnot_Code, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
executingActivities294: BinaryAssociation = BinaryAssociation(
    name="executingActivities294",
    ends={
        Property(name="ActivityType295", type=carnot_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="implementationProcess", type=carnot_ActivityType, multiplicity=Multiplicity(0, 9999))
    }
)
processSymbols296: BinaryAssociation = BinaryAssociation(
    name="processSymbols296",
    ends={
        Property(name="ProcessSymbolType", type=carnot_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="process", type=carnot_ProcessSymbolType, multiplicity=Multiplicity(0, 9999))
    }
)
formalParameters297: BinaryAssociation = BinaryAssociation(
    name="formalParameters297",
    ends={
        Property(name="carnot_FormalParametersType", type=carnot_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ProcessDefinitionType298", type=carnot_FormalParametersType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameterMappings299: BinaryAssociation = BinaryAssociation(
    name="formalParameterMappings299",
    ends={
        Property(name="FormalParameterMappingsType", type=carnot_ProcessDefinitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ProcessDefinitionType300", type=FormalParameterMappingsType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
process301: BinaryAssociation = BinaryAssociation(
    name="process301",
    ends={
        Property(name="ProcessDefinitionType302", type=carnot_ProcessSymbolType, multiplicity=Multiplicity(1, 1)),
        Property(name="processSymbols", type=carnot_ProcessDefinitionType, multiplicity=Multiplicity(1, 1))
    }
)
teams319: BinaryAssociation = BinaryAssociation(
    name="teams319",
    ends={
        Property(name="OrganizationType320", type=carnot_RoleType, multiplicity=Multiplicity(1, 1)),
        Property(name="teamLead", type=carnot_OrganizationType, multiplicity=Multiplicity(0, 9999))
    }
)
roleSymbols321: BinaryAssociation = BinaryAssociation(
    name="roleSymbols321",
    ends={
        Property(name="RoleSymbolType", type=carnot_RoleType, multiplicity=Multiplicity(1, 1)),
        Property(name="role", type=carnot_RoleSymbolType, multiplicity=Multiplicity(0, 9999))
    }
)
trigger322: BinaryAssociation = BinaryAssociation(
    name="trigger322",
    ends={
        Property(name="TriggerType", type=carnot_StartEventSymbol, multiplicity=Multiplicity(1, 1)),
        Property(name="startingEventSymbols", type=carnot_TriggerType, multiplicity=Multiplicity(1, 1))
    }
)
from309: BinaryAssociation = BinaryAssociation(
    name="from309",
    ends={
        Property(name="IGraphicalObject", type=carnot_RefersToConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="referingFromConnections", type=carnot_IGraphicalObject, multiplicity=Multiplicity(1, 1))
    }
)
to310: BinaryAssociation = BinaryAssociation(
    name="to310",
    ends={
        Property(name="IGraphicalObject311", type=carnot_RefersToConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="referingToConnections", type=carnot_IGraphicalObject, multiplicity=Multiplicity(1, 1))
    }
)
role312: BinaryAssociation = BinaryAssociation(
    name="role312",
    ends={
        Property(name="RoleType313", type=carnot_RoleSymbolType, multiplicity=Multiplicity(1, 1)),
        Property(name="roleSymbols", type=carnot_RoleType, multiplicity=Multiplicity(1, 1))
    }
)
organizationMemberships314: BinaryAssociation = BinaryAssociation(
    name="organizationMemberships314",
    ends={
        Property(name="WorksForConnectionType316", type=carnot_RoleSymbolType, multiplicity=Multiplicity(1, 1)),
        Property(name="participantSymbol315", type=carnot_WorksForConnectionType, multiplicity=Multiplicity(0, 9999))
    }
)
teams317: BinaryAssociation = BinaryAssociation(
    name="teams317",
    ends={
        Property(name="TeamLeadConnectionType318", type=carnot_RoleSymbolType, multiplicity=Multiplicity(1, 1)),
        Property(name="teamLeadSymbol", type=carnot_TeamLeadConnectionType, multiplicity=Multiplicity(0, 9999))
    }
)
teamSymbol332: BinaryAssociation = BinaryAssociation(
    name="teamSymbol332",
    ends={
        Property(name="teamLead333", type=carnot_OrganizationSymbolType, multiplicity=Multiplicity(1, 1)),
        Property(name="OrganizationSymbolType334", type=carnot_TeamLeadConnectionType, multiplicity=Multiplicity(1, 1))
    }
)
teamLeadSymbol335: BinaryAssociation = BinaryAssociation(
    name="teamLeadSymbol335",
    ends={
        Property(name="RoleSymbolType337", type=carnot_TeamLeadConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="teams336", type=carnot_RoleSymbolType, multiplicity=Multiplicity(1, 1))
    }
)
triggersConnections323: BinaryAssociation = BinaryAssociation(
    name="triggersConnections323",
    ends={
        Property(name="TriggersConnectionType324", type=carnot_StartEventSymbol, multiplicity=Multiplicity(1, 1)),
        Property(name="startEventSymbol", type=carnot_TriggersConnectionType, multiplicity=Multiplicity(0, 9999))
    }
)
startActivity325: BinaryAssociation = BinaryAssociation(
    name="startActivity325",
    ends={
        Property(name="ActivityType327", type=carnot_StartEventSymbol, multiplicity=Multiplicity(1, 1)),
        Property(name="startingEventSymbols326", type=carnot_ActivityType, multiplicity=Multiplicity(0, 1))
    }
)
processSymbol328: BinaryAssociation = BinaryAssociation(
    name="processSymbol328",
    ends={
        Property(name="ProcessSymbolType329", type=carnot_SubProcessOfConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="subProcesses", type=carnot_ProcessSymbolType, multiplicity=Multiplicity(1, 1))
    }
)
subprocessSymbol330: BinaryAssociation = BinaryAssociation(
    name="subprocessSymbol330",
    ends={
        Property(name="ProcessSymbolType331", type=carnot_SubProcessOfConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="parentProcesses", type=carnot_ProcessSymbolType, multiplicity=Multiplicity(1, 1))
    }
)
expression343: BinaryAssociation = BinaryAssociation(
    name="expression343",
    ends={
        Property(name="carnot_XmlTextNode345", type=carnot_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_TransitionType344", type=carnot_XmlTextNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
from346: BinaryAssociation = BinaryAssociation(
    name="from346",
    ends={
        Property(name="ActivityType348", type=carnot_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="outTransitions347", type=carnot_ActivityType, multiplicity=Multiplicity(0, 1))
    }
)
sourceActivitySymbol338: BinaryAssociation = BinaryAssociation(
    name="sourceActivitySymbol338",
    ends={
        Property(name="IFlowObjectSymbol", type=carnot_TransitionConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="outTransitions", type=carnot_IFlowObjectSymbol, multiplicity=Multiplicity(1, 1))
    }
)
targetActivitySymbol339: BinaryAssociation = BinaryAssociation(
    name="targetActivitySymbol339",
    ends={
        Property(name="IFlowObjectSymbol340", type=carnot_TransitionConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="inTransitions", type=carnot_IFlowObjectSymbol, multiplicity=Multiplicity(1, 1))
    }
)
transition341: BinaryAssociation = BinaryAssociation(
    name="transition341",
    ends={
        Property(name="TransitionType342", type=carnot_TransitionConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="transitionConnections", type=carnot_TransitionType, multiplicity=Multiplicity(1, 1))
    }
)
type360: BinaryAssociation = BinaryAssociation(
    name="type360",
    ends={
        Property(name="TriggerTypeType", type=carnot_TriggerType, multiplicity=Multiplicity(1, 1)),
        Property(name="triggers", type=carnot_TriggerTypeType, multiplicity=Multiplicity(0, 1))
    }
)
startingEventSymbols361: BinaryAssociation = BinaryAssociation(
    name="startingEventSymbols361",
    ends={
        Property(name="StartEventSymbol362", type=carnot_TriggerType, multiplicity=Multiplicity(1, 1)),
        Property(name="trigger", type=carnot_StartEventSymbol, multiplicity=Multiplicity(0, 9999))
    }
)
to349: BinaryAssociation = BinaryAssociation(
    name="to349",
    ends={
        Property(name="ActivityType351", type=carnot_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="inTransitions350", type=carnot_ActivityType, multiplicity=Multiplicity(0, 1))
    }
)
transitionConnections352: BinaryAssociation = BinaryAssociation(
    name="transitionConnections352",
    ends={
        Property(name="TransitionConnectionType353", type=carnot_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=carnot_TransitionConnectionType, multiplicity=Multiplicity(0, 9999))
    }
)
startEventSymbol354: BinaryAssociation = BinaryAssociation(
    name="startEventSymbol354",
    ends={
        Property(name="StartEventSymbol355", type=carnot_TriggersConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="triggersConnections", type=carnot_StartEventSymbol, multiplicity=Multiplicity(1, 1))
    }
)
participantSymbol356: BinaryAssociation = BinaryAssociation(
    name="participantSymbol356",
    ends={
        Property(name="IModelParticipantSymbol357", type=carnot_TriggersConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="triggeredEvents", type=carnot_IModelParticipantSymbol, multiplicity=Multiplicity(1, 1))
    }
)
parameterMapping358: BinaryAssociation = BinaryAssociation(
    name="parameterMapping358",
    ends={
        Property(name="carnot_ParameterMappingType", type=carnot_TriggerType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_TriggerType359", type=carnot_ParameterMappingType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
view371: BinaryAssociation = BinaryAssociation(
    name="view371",
    ends={
        Property(name="carnot_ViewType372", type=carnot_ViewType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ViewType370", type=carnot_ViewType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
viewable373: BinaryAssociation = BinaryAssociation(
    name="viewable373",
    ends={
        Property(name="carnot_ViewableType375", type=carnot_ViewType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ViewType374", type=carnot_ViewableType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triggers363: BinaryAssociation = BinaryAssociation(
    name="triggers363",
    ends={
        Property(name="TriggerType365", type=carnot_TriggerTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="type364", type=carnot_TriggerType, multiplicity=Multiplicity(0, 9999))
    }
)
viewable366: BinaryAssociation = BinaryAssociation(
    name="viewable366",
    ends={
        Property(name="carnot_IModelElement", type=carnot_ViewableType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ViewableType", type=carnot_IModelElement, multiplicity=Multiplicity(1, 1))
    }
)
description367: BinaryAssociation = BinaryAssociation(
    name="description367",
    ends={
        Property(name="carnot_DescriptionType369", type=carnot_ViewType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_ViewType368", type=carnot_DescriptionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
organizationSymbol376: BinaryAssociation = BinaryAssociation(
    name="organizationSymbol376",
    ends={
        Property(name="OrganizationSymbolType377", type=carnot_WorksForConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="memberRoles", type=carnot_OrganizationSymbolType, multiplicity=Multiplicity(1, 1))
    }
)
participantSymbol378: BinaryAssociation = BinaryAssociation(
    name="participantSymbol378",
    ends={
        Property(name="RoleSymbolType379", type=carnot_WorksForConnectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="organizationMemberships", type=carnot_RoleSymbolType, multiplicity=Multiplicity(1, 1))
    }
)
parameter381: BinaryAssociation = BinaryAssociation(
    name="parameter381",
    ends={
        Property(name="extensions_carnot_FormalParameterType", type=carnot_extensions_FormalParameterMappingType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_extensions_FormalParameterMappingType382", type=extensions_carnot_FormalParameterType, multiplicity=Multiplicity(1, 1))
    }
)
mapping383: BinaryAssociation = BinaryAssociation(
    name="mapping383",
    ends={
        Property(name="FormalParameterMappingType", type=carnot_extensions_FormalParameterMappingsType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_extensions_FormalParameterMappingsType", type=FormalParameterMappingType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
data380: BinaryAssociation = BinaryAssociation(
    name="data380",
    ends={
        Property(name="extensions_carnot_DataType", type=carnot_extensions_FormalParameterMappingType, multiplicity=Multiplicity(1, 1)),
        Property(name="carnot_extensions_FormalParameterMappingType", type=extensions_carnot_DataType, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_carnot_IIdentifiableModelElement_IModelElement = Generalization(general=IModelElement, specific=carnot_IIdentifiableModelElement)
gen_carnot_IIdentifiableModelElement_IIdentifiableElement = Generalization(general=IIdentifiableElement, specific=carnot_IIdentifiableModelElement)
gen_carnot_IIdentifiableModelElement_IExtensibleElement = Generalization(general=IExtensibleElement, specific=carnot_IIdentifiableModelElement)
gen_carnot_IMetaType_IIdentifiableModelElement = Generalization(general=IIdentifiableModelElement, specific=carnot_IMetaType)
gen_carnot_ISymbolContainer_IExtensibleElement = Generalization(general=IExtensibleElement, specific=carnot_ISymbolContainer)
gen_carnot_IGraphicalObject_IModelElement = Generalization(general=IModelElement, specific=carnot_IGraphicalObject)
gen_carnot_INodeSymbol_IGraphicalObject = Generalization(general=IGraphicalObject, specific=carnot_INodeSymbol)
gen_carnot_ISwimlaneSymbol_INodeSymbol = Generalization(general=INodeSymbol, specific=carnot_ISwimlaneSymbol)
gen_carnot_ISwimlaneSymbol_IIdentifiableElement = Generalization(general=IIdentifiableElement, specific=carnot_ISwimlaneSymbol)
gen_carnot_IModelElementNodeSymbol_INodeSymbol = Generalization(general=INodeSymbol, specific=carnot_IModelElementNodeSymbol)
gen_carnot_IFlowObjectSymbol_INodeSymbol = Generalization(general=INodeSymbol, specific=carnot_IFlowObjectSymbol)
gen_carnot_IConnectionSymbol_IGraphicalObject = Generalization(general=IGraphicalObject, specific=carnot_IConnectionSymbol)
gen_carnot_AccessPointType_IIdentifiableModelElement = Generalization(general=IIdentifiableModelElement, specific=carnot_AccessPointType)
gen_carnot_AccessPointType_ITypedElement = Generalization(general=ITypedElement, specific=carnot_AccessPointType)
gen_carnot_IModelParticipant_IIdentifiableModelElement = Generalization(general=IIdentifiableModelElement, specific=carnot_IModelParticipant)
gen_carnot_IModelParticipantSymbol_IModelElementNodeSymbol = Generalization(general=IModelElementNodeSymbol, specific=carnot_IModelParticipantSymbol)
gen_carnot_AbstractEventAction_IIdentifiableModelElement = Generalization(general=IIdentifiableModelElement, specific=carnot_AbstractEventAction)
gen_carnot_AbstractEventAction_ITypedElement = Generalization(general=ITypedElement, specific=carnot_AbstractEventAction)
gen_carnot_AbstractEventSymbol_IFlowObjectSymbol = Generalization(general=IFlowObjectSymbol, specific=carnot_AbstractEventSymbol)
gen_carnot_AbstractEventSymbol_IModelElementNodeSymbol = Generalization(general=IModelElementNodeSymbol, specific=carnot_AbstractEventSymbol)
gen_carnot_ActivitySymbolType_IFlowObjectSymbol = Generalization(general=IFlowObjectSymbol, specific=carnot_ActivitySymbolType)
gen_carnot_ActivitySymbolType_IModelElementNodeSymbol = Generalization(general=IModelElementNodeSymbol, specific=carnot_ActivitySymbolType)
gen_carnot_ActivityType_IIdentifiableModelElement = Generalization(general=IIdentifiableModelElement, specific=carnot_ActivityType)
gen_carnot_ActivityType_IEventHandlerOwner = Generalization(general=IEventHandlerOwner, specific=carnot_ActivityType)
gen_carnot_ActivityType_IdRefOwner = Generalization(general=IdRefOwner, specific=carnot_ActivityType)
gen_carnot_ApplicationType_IIdentifiableModelElement = Generalization(general=IIdentifiableModelElement, specific=carnot_ApplicationType)
gen_carnot_ApplicationType_ITypedElement = Generalization(general=ITypedElement, specific=carnot_ApplicationType)
gen_carnot_ApplicationType_IAccessPointOwner = Generalization(general=IAccessPointOwner, specific=carnot_ApplicationType)
gen_carnot_AnnotationSymbolType_INodeSymbol = Generalization(general=INodeSymbol, specific=carnot_AnnotationSymbolType)
gen_carnot_ApplicationContextTypeType_IMetaType = Generalization(general=IMetaType, specific=carnot_ApplicationContextTypeType)
gen_carnot_ApplicationSymbolType_IModelElementNodeSymbol = Generalization(general=IModelElementNodeSymbol, specific=carnot_ApplicationSymbolType)
gen_carnot_ApplicationTypeType_IMetaType = Generalization(general=IMetaType, specific=carnot_ApplicationTypeType)
gen_carnot_BindActionType_AbstractEventAction = Generalization(general=AbstractEventAction, specific=carnot_BindActionType)
gen_carnot_ConditionalPerformerSymbolType_IModelParticipantSymbol = Generalization(general=IModelParticipantSymbol, specific=carnot_ConditionalPerformerSymbolType)
gen_carnot_ConditionalPerformerType_IModelParticipant = Generalization(general=IModelParticipant, specific=carnot_ConditionalPerformerType)
gen_carnot_ContextType_IModelElement = Generalization(general=IModelElement, specific=carnot_ContextType)
gen_carnot_ContextType_IExtensibleElement = Generalization(general=IExtensibleElement, specific=carnot_ContextType)
gen_carnot_ContextType_ITypedElement = Generalization(general=ITypedElement, specific=carnot_ContextType)
gen_carnot_ContextType_IAccessPointOwner = Generalization(general=IAccessPointOwner, specific=carnot_ContextType)
gen_carnot_DataPathType_IIdentifiableModelElement = Generalization(general=IIdentifiableModelElement, specific=carnot_DataPathType)
gen_carnot_DataMappingConnectionType_IConnectionSymbol = Generalization(general=IConnectionSymbol, specific=carnot_DataMappingConnectionType)
gen_carnot_DataMappingType_IModelElement = Generalization(general=IModelElement, specific=carnot_DataMappingType)
gen_carnot_DataMappingType_IIdentifiableElement = Generalization(general=IIdentifiableElement, specific=carnot_DataMappingType)
gen_carnot_DataMappingType_IExtensibleElement = Generalization(general=IExtensibleElement, specific=carnot_DataMappingType)
gen_carnot_DataSymbolType_IModelElementNodeSymbol = Generalization(general=IModelElementNodeSymbol, specific=carnot_DataSymbolType)
gen_carnot_DataType_IIdentifiableModelElement = Generalization(general=IIdentifiableModelElement, specific=carnot_DataType)
gen_carnot_DataType_ITypedElement = Generalization(general=ITypedElement, specific=carnot_DataType)
gen_carnot_DiagramType_IModelElement = Generalization(general=IModelElement, specific=carnot_DiagramType)
gen_carnot_DiagramType_IExtensibleElement = Generalization(general=IExtensibleElement, specific=carnot_DiagramType)
gen_carnot_DataTypeType_IMetaType = Generalization(general=IMetaType, specific=carnot_DataTypeType)
gen_carnot_DiagramType_ISymbolContainer = Generalization(general=ISymbolContainer, specific=carnot_DiagramType)
gen_carnot_EventActionTypeType_IMetaType = Generalization(general=IMetaType, specific=carnot_EventActionTypeType)
gen_carnot_EndEventSymbol_AbstractEventSymbol = Generalization(general=AbstractEventSymbol, specific=carnot_EndEventSymbol)
gen_carnot_EventActionType_AbstractEventAction = Generalization(general=AbstractEventAction, specific=carnot_EventActionType)
gen_carnot_EventHandlerType_IIdentifiableModelElement = Generalization(general=IIdentifiableModelElement, specific=carnot_EventHandlerType)
gen_carnot_EventHandlerType_ITypedElement = Generalization(general=ITypedElement, specific=carnot_EventHandlerType)
gen_carnot_EventHandlerType_IAccessPointOwner = Generalization(general=IAccessPointOwner, specific=carnot_EventHandlerType)
gen_carnot_EventConditionTypeType_IMetaType = Generalization(general=IMetaType, specific=carnot_EventConditionTypeType)
gen_carnot_ExecutedByConnectionType_IConnectionSymbol = Generalization(general=IConnectionSymbol, specific=carnot_ExecutedByConnectionType)
gen_carnot_GatewaySymbol_IFlowObjectSymbol = Generalization(general=IFlowObjectSymbol, specific=carnot_GatewaySymbol)
gen_carnot_GenericLinkConnectionType_IConnectionSymbol = Generalization(general=IConnectionSymbol, specific=carnot_GenericLinkConnectionType)
gen_carnot_GenericLinkConnectionType_ITypedElement = Generalization(general=ITypedElement, specific=carnot_GenericLinkConnectionType)
gen_carnot_GroupSymbolType_ISymbolContainer = Generalization(general=ISymbolContainer, specific=carnot_GroupSymbolType)
gen_carnot_GroupSymbolType_INodeSymbol = Generalization(general=INodeSymbol, specific=carnot_GroupSymbolType)
gen_carnot_IntermediateEventSymbol_AbstractEventSymbol = Generalization(general=AbstractEventSymbol, specific=carnot_IntermediateEventSymbol)
gen_carnot_LaneSymbol_ISymbolContainer = Generalization(general=ISymbolContainer, specific=carnot_LaneSymbol)
gen_carnot_LaneSymbol_ISwimlaneSymbol = Generalization(general=ISwimlaneSymbol, specific=carnot_LaneSymbol)
gen_carnot_LinkTypeType_IMetaType = Generalization(general=IMetaType, specific=carnot_LinkTypeType)
gen_carnot_LinkTypeType_IExtensibleElement = Generalization(general=IExtensibleElement, specific=carnot_LinkTypeType)
gen_carnot_ModelerType_IIdentifiableModelElement = Generalization(general=IIdentifiableModelElement, specific=carnot_ModelerType)
gen_carnot_ModelType_IIdentifiableElement = Generalization(general=IIdentifiableElement, specific=carnot_ModelType)
gen_carnot_ModelType_IExtensibleElement = Generalization(general=IExtensibleElement, specific=carnot_ModelType)
gen_carnot_ModelerSymbolType_IModelElementNodeSymbol = Generalization(general=IModelElementNodeSymbol, specific=carnot_ModelerSymbolType)
gen_carnot_OrganizationSymbolType_IModelParticipantSymbol = Generalization(general=IModelParticipantSymbol, specific=carnot_OrganizationSymbolType)
gen_carnot_ParameterMappingType_IModelElement = Generalization(general=IModelElement, specific=carnot_ParameterMappingType)
gen_carnot_OrganizationType_IModelParticipant = Generalization(general=IModelParticipant, specific=carnot_OrganizationType)
gen_carnot_PoolSymbol_ISymbolContainer = Generalization(general=ISymbolContainer, specific=carnot_PoolSymbol)
gen_carnot_PoolSymbol_ISwimlaneSymbol = Generalization(general=ISwimlaneSymbol, specific=carnot_PoolSymbol)
gen_carnot_PartOfConnectionType_IConnectionSymbol = Generalization(general=IConnectionSymbol, specific=carnot_PartOfConnectionType)
gen_carnot_PerformsConnectionType_IConnectionSymbol = Generalization(general=IConnectionSymbol, specific=carnot_PerformsConnectionType)
gen_carnot_ProcessDefinitionType_IIdentifiableModelElement = Generalization(general=IIdentifiableModelElement, specific=carnot_ProcessDefinitionType)
gen_carnot_ProcessDefinitionType_IEventHandlerOwner = Generalization(general=IEventHandlerOwner, specific=carnot_ProcessDefinitionType)
gen_carnot_ProcessDefinitionType_IdRefOwner = Generalization(general=IdRefOwner, specific=carnot_ProcessDefinitionType)
gen_carnot_PublicInterfaceSymbol_AbstractEventSymbol = Generalization(general=AbstractEventSymbol, specific=carnot_PublicInterfaceSymbol)
gen_carnot_RefersToConnectionType_IConnectionSymbol = Generalization(general=IConnectionSymbol, specific=carnot_RefersToConnectionType)
gen_carnot_ProcessSymbolType_IModelElementNodeSymbol = Generalization(general=IModelElementNodeSymbol, specific=carnot_ProcessSymbolType)
gen_carnot_StartEventSymbol_AbstractEventSymbol = Generalization(general=AbstractEventSymbol, specific=carnot_StartEventSymbol)
gen_carnot_RoleSymbolType_IModelParticipantSymbol = Generalization(general=IModelParticipantSymbol, specific=carnot_RoleSymbolType)
gen_carnot_RoleType_IModelParticipant = Generalization(general=IModelParticipant, specific=carnot_RoleType)
gen_carnot_TextSymbolType_INodeSymbol = Generalization(general=INodeSymbol, specific=carnot_TextSymbolType)
gen_carnot_SubProcessOfConnectionType_IConnectionSymbol = Generalization(general=IConnectionSymbol, specific=carnot_SubProcessOfConnectionType)
gen_carnot_TeamLeadConnectionType_IConnectionSymbol = Generalization(general=IConnectionSymbol, specific=carnot_TeamLeadConnectionType)
gen_carnot_TransitionConnectionType_IConnectionSymbol = Generalization(general=IConnectionSymbol, specific=carnot_TransitionConnectionType)
gen_carnot_TransitionType_IIdentifiableModelElement = Generalization(general=IIdentifiableModelElement, specific=carnot_TransitionType)
gen_carnot_TriggerTypeType_IMetaType = Generalization(general=IMetaType, specific=carnot_TriggerTypeType)
gen_carnot_TriggersConnectionType_IConnectionSymbol = Generalization(general=IConnectionSymbol, specific=carnot_TriggersConnectionType)
gen_carnot_TriggerType_IIdentifiableModelElement = Generalization(general=IIdentifiableModelElement, specific=carnot_TriggerType)
gen_carnot_TriggerType_ITypedElement = Generalization(general=ITypedElement, specific=carnot_TriggerType)
gen_carnot_TriggerType_IAccessPointOwner = Generalization(general=IAccessPointOwner, specific=carnot_TriggerType)
gen_carnot_WorksForConnectionType_IConnectionSymbol = Generalization(general=IConnectionSymbol, specific=carnot_WorksForConnectionType)
gen_carnot_UnbindActionType_AbstractEventAction = Generalization(general=AbstractEventAction, specific=carnot_UnbindActionType)
gen_carnot_ViewType_IModelElement = Generalization(general=IModelElement, specific=carnot_ViewType)
gen_carnot_ViewType_IExtensibleElement = Generalization(general=IExtensibleElement, specific=carnot_ViewType)

# Domain Model
domain_model = DomainModel(
    name="carnot",
    types={carnot_Coordinates, carnot_IIdentifiableElement, carnot_IExtensibleElement, carnot_AttributeType, carnot_IdentifiableReference, carnot_EObject, carnot_IModelElement, carnot_IIdentifiableModelElement, IModelElement, IIdentifiableElement, IExtensibleElement, carnot_DescriptionType, carnot_IEventHandlerOwner, carnot_EventHandlerType, carnot_IAccessPointOwner, carnot_AccessPointType, carnot_IMetaType, IIdentifiableModelElement, carnot_ITypedElement, carnot_ISymbolContainer, carnot_ActivitySymbolType, carnot_AnnotationSymbolType, carnot_ApplicationSymbolType, carnot_ConditionalPerformerSymbolType, carnot_DataSymbolType, carnot_EndEventSymbol, carnot_GatewaySymbol, carnot_GroupSymbolType, carnot_IntermediateEventSymbol, carnot_ModelerSymbolType, carnot_OrganizationSymbolType, carnot_ProcessSymbolType, carnot_PublicInterfaceSymbol, carnot_RoleSymbolType, carnot_StartEventSymbol, carnot_TextSymbolType, carnot_DataMappingConnectionType, carnot_ExecutedByConnectionType, carnot_GenericLinkConnectionType, carnot_PartOfConnectionType, carnot_PerformsConnectionType, carnot_TriggersConnectionType, carnot_RefersToConnectionType, carnot_SubProcessOfConnectionType, carnot_TransitionConnectionType, carnot_WorksForConnectionType, carnot_TeamLeadConnectionType, carnot_IGraphicalObject, carnot_INodeSymbol, IGraphicalObject, carnot_ISwimlaneSymbol, INodeSymbol, carnot_IModelParticipant, carnot_LaneSymbol, carnot_IModelElementNodeSymbol, carnot_IFlowObjectSymbol, carnot_IConnectionSymbol, carnot_DataTypeType, carnot_ActivityType, carnot_ParticipantType, carnot_IModelParticipantSymbol, IModelElementNodeSymbol, carnot_AbstractEventAction, ITypedElement, carnot_EventActionTypeType, carnot_AbstractEventSymbol, IFlowObjectSymbol, IEventHandlerOwner, IdRefOwner, carnot_DataMappingType, carnot_ApplicationType, carnot_TransitionType, carnot_Code, carnot_ProcessDefinitionType, IAccessPointOwner, carnot_LoopType, carnot_TextType, carnot_ApplicationContextTypeType, IMetaType, carnot_ContextType, carnot_ApplicationTypeType, carnot_BindActionType, AbstractEventAction, carnot_XmlTextNode, IModelParticipantSymbol, carnot_ConditionalPerformerType, IModelParticipant, carnot_DataType, carnot_DataPathType, IConnectionSymbol, carnot_ParameterMappingType, carnot_PoolSymbol, carnot_ExternalReferenceType, carnot_DiagramType, ISymbolContainer, carnot_DocumentRoot, carnot_EStringToStringMapEntry, carnot_ModelType, AbstractEventSymbol, carnot_EventActionType, carnot_EventConditionTypeType, carnot_UnbindActionType, carnot_IdRef, carnot_ExternalPackage, carnot_IdRefOwner, carnot_LinkTypeType, ISwimlaneSymbol, carnot_ModelerType, carnot_TriggerTypeType, carnot_ExternalPackages, carnot_ScriptType, carnot_TypeDeclarationsType, carnot_QualityControlType, carnot_RoleType, carnot_OrganizationType, carnot_ViewType, carnot_TriggerType, carnot_FormalParametersType, FormalParameterMappingsType, carnot_ViewableType, extensions_carnot_FormalParameterType, carnot_extensions_FormalParameterMappingsType, FormalParameterMappingType, carnot_extensions_FormalParameterMappingType, extensions_carnot_DataType, DirectionType, FlowControlType, ImplementationType, JoinSplitType, LinkCardinality, ActivityImplementationType, SubProcessModeType, DiagramModeType, LinkColor, LinkLineStyle, LinkEndStyle, LoopType, OrientationType, RoutingType},
    associations={attribute0, attribute1, identifiable2, description3, eventHandler4, accessPoint5, activitySymbol6, annotationSymbol7, applicationSymbol9, conditionalPerformerSymbol11, dataSymbol13, endEventSymbols15, gatewaySymbol17, groupSymbol19, intermediateEventSymbols21, modelerSymbol23, organizationSymbol25, processSymbol27, processInterfaceSymbols29, roleSymbol31, startEventSymbols33, textSymbol35, dataMappingConnection37, executedByConnection39, genericLinkConnection41, partOfConnection43, performsConnection45, triggersConnection47, refersToConnection49, subProcessOfConnection51, transitionConnection53, worksForConnection55, teamLeadConnection57, referingToConnections59, referingFromConnections60, inLinks62, outLinks63, participant65, childLanes66, participantReference67, inTransitions68, outTransitions69, type80, coordinates71, performedActivities72, performedSwimlanes73, participantAssociations74, performedActivities76, triggeredEvents77, type79, activity82, performsConnections84, executedByConnections86, dataMappings88, gatewaySymbols90, dataMapping92, application93, startingEventSymbols101, inTransitions102, outTransitions104, validQualityCodes107, implementationProcess94, performer95, qualityControlPerformer97, activitySymbols100, application116, context118, loop109, text111, contexts113, executingActivities114, type119, executedActivities120, applicationSymbols122, reference129, applications124, valueNode127, description134, type137, participant130, data131, conditionalPerformerSymbols132, data145, activitySymbol138, dataSymbol140, data142, dataSymbols154, conditionalPerformers157, dataPaths160, parameterMappings162, data147, dataMappings149, dataMappings151, type152, poolSymbols168, externalReference164, data165, xMLNSPrefixMap169, xSISchemaLocation170, model173, eventHandlers177, bindAction179, actionInstances175, activitySymbol186, applicationSymbol188, eventAction181, unbindAction183, type185, sourceSymbol197, targetSymbol198, packageRef191, externalRef192, activitySymbol194, linkType196, parentPool200, parentLane202, modelerSymbols207, linkInstances204, modeler206, eventActionType222, data224, application227, description208, dataType211, applicationType214, applicationContextType216, triggerType218, eventConditionType220, externalPackages242, script244, typeDeclarations246, modeler230, qualityControl232, role234, organization236, conditionalPerformer238, processDefinition240, organization254, diagram248, linkType250, view252, data265, superOrganizations255, subOrganizations256, memberRoles258, teamLead260, participant261, organizationSymbols263, teamLead264, activitySymbol273, participantSymbol275, diagram277, participant267, organizationSymbol269, suborganizationSymbol271, trigger287, dataPath289, diagram291, process278, lanes280, activity282, transition285, subProcesses303, parentProcesses304, Code306, executingActivities294, processSymbols296, formalParameters297, formalParameterMappings299, process301, teams319, roleSymbols321, trigger322, from309, to310, role312, organizationMemberships314, teams317, teamSymbol332, teamLeadSymbol335, triggersConnections323, startActivity325, processSymbol328, subprocessSymbol330, expression343, from346, sourceActivitySymbol338, targetActivitySymbol339, transition341, type360, startingEventSymbols361, to349, transitionConnections352, startEventSymbol354, participantSymbol356, parameterMapping358, view371, viewable373, triggers363, viewable366, description367, organizationSymbol376, participantSymbol378, parameter381, mapping383, data380},
    generalizations={gen_carnot_IIdentifiableModelElement_IModelElement, gen_carnot_IIdentifiableModelElement_IIdentifiableElement, gen_carnot_IIdentifiableModelElement_IExtensibleElement, gen_carnot_IMetaType_IIdentifiableModelElement, gen_carnot_ISymbolContainer_IExtensibleElement, gen_carnot_IGraphicalObject_IModelElement, gen_carnot_INodeSymbol_IGraphicalObject, gen_carnot_ISwimlaneSymbol_INodeSymbol, gen_carnot_ISwimlaneSymbol_IIdentifiableElement, gen_carnot_IModelElementNodeSymbol_INodeSymbol, gen_carnot_IFlowObjectSymbol_INodeSymbol, gen_carnot_IConnectionSymbol_IGraphicalObject, gen_carnot_AccessPointType_IIdentifiableModelElement, gen_carnot_AccessPointType_ITypedElement, gen_carnot_IModelParticipant_IIdentifiableModelElement, gen_carnot_IModelParticipantSymbol_IModelElementNodeSymbol, gen_carnot_AbstractEventAction_IIdentifiableModelElement, gen_carnot_AbstractEventAction_ITypedElement, gen_carnot_AbstractEventSymbol_IFlowObjectSymbol, gen_carnot_AbstractEventSymbol_IModelElementNodeSymbol, gen_carnot_ActivitySymbolType_IFlowObjectSymbol, gen_carnot_ActivitySymbolType_IModelElementNodeSymbol, gen_carnot_ActivityType_IIdentifiableModelElement, gen_carnot_ActivityType_IEventHandlerOwner, gen_carnot_ActivityType_IdRefOwner, gen_carnot_ApplicationType_IIdentifiableModelElement, gen_carnot_ApplicationType_ITypedElement, gen_carnot_ApplicationType_IAccessPointOwner, gen_carnot_AnnotationSymbolType_INodeSymbol, gen_carnot_ApplicationContextTypeType_IMetaType, gen_carnot_ApplicationSymbolType_IModelElementNodeSymbol, gen_carnot_ApplicationTypeType_IMetaType, gen_carnot_BindActionType_AbstractEventAction, gen_carnot_ConditionalPerformerSymbolType_IModelParticipantSymbol, gen_carnot_ConditionalPerformerType_IModelParticipant, gen_carnot_ContextType_IModelElement, gen_carnot_ContextType_IExtensibleElement, gen_carnot_ContextType_ITypedElement, gen_carnot_ContextType_IAccessPointOwner, gen_carnot_DataPathType_IIdentifiableModelElement, gen_carnot_DataMappingConnectionType_IConnectionSymbol, gen_carnot_DataMappingType_IModelElement, gen_carnot_DataMappingType_IIdentifiableElement, gen_carnot_DataMappingType_IExtensibleElement, gen_carnot_DataSymbolType_IModelElementNodeSymbol, gen_carnot_DataType_IIdentifiableModelElement, gen_carnot_DataType_ITypedElement, gen_carnot_DiagramType_IModelElement, gen_carnot_DiagramType_IExtensibleElement, gen_carnot_DataTypeType_IMetaType, gen_carnot_DiagramType_ISymbolContainer, gen_carnot_EventActionTypeType_IMetaType, gen_carnot_EndEventSymbol_AbstractEventSymbol, gen_carnot_EventActionType_AbstractEventAction, gen_carnot_EventHandlerType_IIdentifiableModelElement, gen_carnot_EventHandlerType_ITypedElement, gen_carnot_EventHandlerType_IAccessPointOwner, gen_carnot_EventConditionTypeType_IMetaType, gen_carnot_ExecutedByConnectionType_IConnectionSymbol, gen_carnot_GatewaySymbol_IFlowObjectSymbol, gen_carnot_GenericLinkConnectionType_IConnectionSymbol, gen_carnot_GenericLinkConnectionType_ITypedElement, gen_carnot_GroupSymbolType_ISymbolContainer, gen_carnot_GroupSymbolType_INodeSymbol, gen_carnot_IntermediateEventSymbol_AbstractEventSymbol, gen_carnot_LaneSymbol_ISymbolContainer, gen_carnot_LaneSymbol_ISwimlaneSymbol, gen_carnot_LinkTypeType_IMetaType, gen_carnot_LinkTypeType_IExtensibleElement, gen_carnot_ModelerType_IIdentifiableModelElement, gen_carnot_ModelType_IIdentifiableElement, gen_carnot_ModelType_IExtensibleElement, gen_carnot_ModelerSymbolType_IModelElementNodeSymbol, gen_carnot_OrganizationSymbolType_IModelParticipantSymbol, gen_carnot_ParameterMappingType_IModelElement, gen_carnot_OrganizationType_IModelParticipant, gen_carnot_PoolSymbol_ISymbolContainer, gen_carnot_PoolSymbol_ISwimlaneSymbol, gen_carnot_PartOfConnectionType_IConnectionSymbol, gen_carnot_PerformsConnectionType_IConnectionSymbol, gen_carnot_ProcessDefinitionType_IIdentifiableModelElement, gen_carnot_ProcessDefinitionType_IEventHandlerOwner, gen_carnot_ProcessDefinitionType_IdRefOwner, gen_carnot_PublicInterfaceSymbol_AbstractEventSymbol, gen_carnot_RefersToConnectionType_IConnectionSymbol, gen_carnot_ProcessSymbolType_IModelElementNodeSymbol, gen_carnot_StartEventSymbol_AbstractEventSymbol, gen_carnot_RoleSymbolType_IModelParticipantSymbol, gen_carnot_RoleType_IModelParticipant, gen_carnot_TextSymbolType_INodeSymbol, gen_carnot_SubProcessOfConnectionType_IConnectionSymbol, gen_carnot_TeamLeadConnectionType_IConnectionSymbol, gen_carnot_TransitionConnectionType_IConnectionSymbol, gen_carnot_TransitionType_IIdentifiableModelElement, gen_carnot_TriggerTypeType_IMetaType, gen_carnot_TriggersConnectionType_IConnectionSymbol, gen_carnot_TriggerType_IIdentifiableModelElement, gen_carnot_TriggerType_ITypedElement, gen_carnot_TriggerType_IAccessPointOwner, gen_carnot_WorksForConnectionType_IConnectionSymbol, gen_carnot_UnbindActionType_AbstractEventAction, gen_carnot_ViewType_IModelElement, gen_carnot_ViewType_IExtensibleElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)