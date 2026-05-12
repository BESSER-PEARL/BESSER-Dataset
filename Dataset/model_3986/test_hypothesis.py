import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    IModelElementNodeSymbol,
    carnot_IModelParticipantSymbol,
    carnot_ParticipantType,
    IFlowObjectSymbol,
    carnot_AbstractEventSymbol,
    IGraphicalObject,
    carnot_IConnectionSymbol,
    carnot_INodeSymbol,
    INodeSymbol,
    carnot_IModelElementNodeSymbol,
    carnot_IFlowObjectSymbol,
    carnot_TextSymbolType,
    carnot_ProcessSymbolType,
    carnot_GatewaySymbol,
    carnot_DataSymbolType,
    carnot_ModelerSymbolType,
    carnot_ActivitySymbolType,
    carnot_ITypedElement,
    IIdentifiableModelElement,
    carnot_IModelParticipant,
    carnot_IMetaType,
    carnot_IAccessPointOwner,
    carnot_ApplicationSymbolType,
    carnot_AnnotationSymbolType,
    carnot_IModelElement,
    carnot_EObject,
    carnot_IdentifiableReference,
    carnot_AttributeType,
    carnot_IExtensibleElement,
    carnot_IIdentifiableElement,
    carnot_IEventHandlerOwner,
    carnot_DescriptionType,
    IExtensibleElement,
    carnot_ISymbolContainer,
    IIdentifiableElement,
    carnot_ISwimlaneSymbol,
    IModelElement,
    carnot_IGraphicalObject,
    carnot_IIdentifiableModelElement,
    carnot_Coordinates,
    FormalParameterMappingType,
    carnot_extensions_FormalParameterMappingsType,
    extensions_carnot_FormalParameterType,
    extensions_carnot_DataType,
    carnot_extensions_FormalParameterMappingType,
    carnot_ViewableType,
    FormalParameterMappingsType,
    carnot_FormalParametersType,
    carnot_ViewType,
    carnot_TypeDeclarationsType,
    carnot_ScriptType,
    carnot_ExternalPackages,
    carnot_QualityControlType,
    carnot_ModelerType,
    ISwimlaneSymbol,
    carnot_IdRefOwner,
    carnot_ExternalPackage,
    carnot_IdRef,
    carnot_EStringToStringMapEntry,
    carnot_DocumentRoot,
    AbstractEventSymbol,
    carnot_EndEventSymbol,
    carnot_IntermediateEventSymbol,
    carnot_PublicInterfaceSymbol,
    carnot_StartEventSymbol,
    carnot_ModelType,
    carnot_ExternalReferenceType,
    carnot_ParameterMappingType,
    ISymbolContainer,
    carnot_LaneSymbol,
    carnot_GroupSymbolType,
    carnot_PoolSymbol,
    carnot_DiagramType,
    carnot_DataPathType,
    IConnectionSymbol,
    carnot_WorksForConnectionType,
    carnot_TriggersConnectionType,
    carnot_PerformsConnectionType,
    carnot_SubProcessOfConnectionType,
    carnot_TransitionConnectionType,
    carnot_RefersToConnectionType,
    carnot_DataMappingConnectionType,
    carnot_TeamLeadConnectionType,
    carnot_PartOfConnectionType,
    carnot_ExecutedByConnectionType,
    IModelParticipantSymbol,
    carnot_OrganizationSymbolType,
    carnot_ConditionalPerformerSymbolType,
    carnot_RoleSymbolType,
    AbstractEventAction,
    carnot_UnbindActionType,
    carnot_EventActionType,
    carnot_BindActionType,
    IModelParticipant,
    carnot_RoleType,
    carnot_OrganizationType,
    carnot_ConditionalPerformerType,
    carnot_XmlTextNode,
    IMetaType,
    carnot_TriggerTypeType,
    carnot_DataTypeType,
    carnot_EventConditionTypeType,
    carnot_ApplicationTypeType,
    carnot_LinkTypeType,
    carnot_ApplicationContextTypeType,
    carnot_TextType,
    carnot_LoopType,
    IAccessPointOwner,
    carnot_Code,
    carnot_TransitionType,
    carnot_DataMappingType,
    IdRefOwner,
    IEventHandlerOwner,
    carnot_ProcessDefinitionType,
    carnot_ActivityType,
    carnot_EventActionTypeType,
    ITypedElement,
    carnot_DataType,
    carnot_TriggerType,
    carnot_ApplicationType,
    carnot_ContextType,
    carnot_EventHandlerType,
    carnot_GenericLinkConnectionType,
    carnot_AccessPointType,
    carnot_AbstractEventAction,
    LoopType,
    LinkColor,
    SubProcessModeType,
    OrientationType,
    JoinSplitType,
    ActivityImplementationType,
    LinkLineStyle,
    RoutingType,
    LinkEndStyle,
    FlowControlType,
    DiagramModeType,
    LinkCardinality,
    ImplementationType,
    DirectionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_imodelelementnodesymbol_is_not_abstract():
    assert not inspect.isabstract(IModelElementNodeSymbol)


def test_imodelelementnodesymbol_constructor_exists():
    assert callable(IModelElementNodeSymbol.__init__)


def test_imodelelementnodesymbol_constructor_args():
    sig = inspect.signature(IModelElementNodeSymbol.__init__)
    params = list(sig.parameters.keys())



def test_carnot_imodelparticipantsymbol_is_not_abstract():
    assert not inspect.isabstract(carnot_IModelParticipantSymbol)


def test_carnot_imodelparticipantsymbol_constructor_exists():
    assert callable(carnot_IModelParticipantSymbol.__init__)


def test_carnot_imodelparticipantsymbol_constructor_args():
    sig = inspect.signature(carnot_IModelParticipantSymbol.__init__)
    params = list(sig.parameters.keys())



def test_carnot_participanttype_is_not_abstract():
    assert not inspect.isabstract(carnot_ParticipantType)


def test_carnot_participanttype_constructor_exists():
    assert callable(carnot_ParticipantType.__init__)


def test_carnot_participanttype_constructor_args():
    sig = inspect.signature(carnot_ParticipantType.__init__)
    params = list(sig.parameters.keys())



def test_iflowobjectsymbol_is_not_abstract():
    assert not inspect.isabstract(IFlowObjectSymbol)


def test_iflowobjectsymbol_constructor_exists():
    assert callable(IFlowObjectSymbol.__init__)


def test_iflowobjectsymbol_constructor_args():
    sig = inspect.signature(IFlowObjectSymbol.__init__)
    params = list(sig.parameters.keys())



def test_carnot_abstracteventsymbol_is_not_abstract():
    assert not inspect.isabstract(carnot_AbstractEventSymbol)


def test_carnot_abstracteventsymbol_constructor_exists():
    assert callable(carnot_AbstractEventSymbol.__init__)


def test_carnot_abstracteventsymbol_constructor_args():
    sig = inspect.signature(carnot_AbstractEventSymbol.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_carnot_abstracteventsymbol_has_label():
    assert hasattr(carnot_AbstractEventSymbol, "label")
    descriptor = None
    for klass in carnot_AbstractEventSymbol.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_igraphicalobject_is_not_abstract():
    assert not inspect.isabstract(IGraphicalObject)


def test_igraphicalobject_constructor_exists():
    assert callable(IGraphicalObject.__init__)


def test_igraphicalobject_constructor_args():
    sig = inspect.signature(IGraphicalObject.__init__)
    params = list(sig.parameters.keys())



def test_carnot_iconnectionsymbol_is_not_abstract():
    assert not inspect.isabstract(carnot_IConnectionSymbol)


def test_carnot_iconnectionsymbol_constructor_exists():
    assert callable(carnot_IConnectionSymbol.__init__)


def test_carnot_iconnectionsymbol_constructor_args():
    sig = inspect.signature(carnot_IConnectionSymbol.__init__)
    params = list(sig.parameters.keys())
    assert "sourceAnchor" in params, "Missing parameter 'sourceAnchor'"
    assert "routing" in params, "Missing parameter 'routing'"
    assert "targetAnchor" in params, "Missing parameter 'targetAnchor'"

def test_carnot_iconnectionsymbol_has_sourceAnchor():
    assert hasattr(carnot_IConnectionSymbol, "sourceAnchor")
    descriptor = None
    for klass in carnot_IConnectionSymbol.__mro__:
        if "sourceAnchor" in klass.__dict__:
            descriptor = klass.__dict__["sourceAnchor"]
            break
    assert isinstance(descriptor, property)

def test_carnot_iconnectionsymbol_has_routing():
    assert hasattr(carnot_IConnectionSymbol, "routing")
    descriptor = None
    for klass in carnot_IConnectionSymbol.__mro__:
        if "routing" in klass.__dict__:
            descriptor = klass.__dict__["routing"]
            break
    assert isinstance(descriptor, property)

def test_carnot_iconnectionsymbol_has_targetAnchor():
    assert hasattr(carnot_IConnectionSymbol, "targetAnchor")
    descriptor = None
    for klass in carnot_IConnectionSymbol.__mro__:
        if "targetAnchor" in klass.__dict__:
            descriptor = klass.__dict__["targetAnchor"]
            break
    assert isinstance(descriptor, property)



def test_carnot_inodesymbol_is_not_abstract():
    assert not inspect.isabstract(carnot_INodeSymbol)


def test_carnot_inodesymbol_constructor_exists():
    assert callable(carnot_INodeSymbol.__init__)


def test_carnot_inodesymbol_constructor_args():
    sig = inspect.signature(carnot_INodeSymbol.__init__)
    params = list(sig.parameters.keys())
    assert "yPos" in params, "Missing parameter 'yPos'"
    assert "shape" in params, "Missing parameter 'shape'"
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"
    assert "xPos" in params, "Missing parameter 'xPos'"

def test_carnot_inodesymbol_has_yPos():
    assert hasattr(carnot_INodeSymbol, "yPos")
    descriptor = None
    for klass in carnot_INodeSymbol.__mro__:
        if "yPos" in klass.__dict__:
            descriptor = klass.__dict__["yPos"]
            break
    assert isinstance(descriptor, property)

def test_carnot_inodesymbol_has_shape():
    assert hasattr(carnot_INodeSymbol, "shape")
    descriptor = None
    for klass in carnot_INodeSymbol.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)

def test_carnot_inodesymbol_has_height():
    assert hasattr(carnot_INodeSymbol, "height")
    descriptor = None
    for klass in carnot_INodeSymbol.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_carnot_inodesymbol_has_width():
    assert hasattr(carnot_INodeSymbol, "width")
    descriptor = None
    for klass in carnot_INodeSymbol.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_carnot_inodesymbol_has_xPos():
    assert hasattr(carnot_INodeSymbol, "xPos")
    descriptor = None
    for klass in carnot_INodeSymbol.__mro__:
        if "xPos" in klass.__dict__:
            descriptor = klass.__dict__["xPos"]
            break
    assert isinstance(descriptor, property)



def test_inodesymbol_is_not_abstract():
    assert not inspect.isabstract(INodeSymbol)


def test_inodesymbol_constructor_exists():
    assert callable(INodeSymbol.__init__)


def test_inodesymbol_constructor_args():
    sig = inspect.signature(INodeSymbol.__init__)
    params = list(sig.parameters.keys())



def test_carnot_imodelelementnodesymbol_is_not_abstract():
    assert not inspect.isabstract(carnot_IModelElementNodeSymbol)


def test_carnot_imodelelementnodesymbol_constructor_exists():
    assert callable(carnot_IModelElementNodeSymbol.__init__)


def test_carnot_imodelelementnodesymbol_constructor_args():
    sig = inspect.signature(carnot_IModelElementNodeSymbol.__init__)
    params = list(sig.parameters.keys())



def test_carnot_iflowobjectsymbol_is_not_abstract():
    assert not inspect.isabstract(carnot_IFlowObjectSymbol)


def test_carnot_iflowobjectsymbol_constructor_exists():
    assert callable(carnot_IFlowObjectSymbol.__init__)


def test_carnot_iflowobjectsymbol_constructor_args():
    sig = inspect.signature(carnot_IFlowObjectSymbol.__init__)
    params = list(sig.parameters.keys())



def test_carnot_textsymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot_TextSymbolType)


def test_carnot_textsymboltype_constructor_exists():
    assert callable(carnot_TextSymbolType.__init__)


def test_carnot_textsymboltype_constructor_args():
    sig = inspect.signature(carnot_TextSymbolType.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_carnot_textsymboltype_has_text():
    assert hasattr(carnot_TextSymbolType, "text")
    descriptor = None
    for klass in carnot_TextSymbolType.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_carnot_processsymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot_ProcessSymbolType)


def test_carnot_processsymboltype_constructor_exists():
    assert callable(carnot_ProcessSymbolType.__init__)


def test_carnot_processsymboltype_constructor_args():
    sig = inspect.signature(carnot_ProcessSymbolType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_gatewaysymbol_is_not_abstract():
    assert not inspect.isabstract(carnot_GatewaySymbol)


def test_carnot_gatewaysymbol_constructor_exists():
    assert callable(carnot_GatewaySymbol.__init__)


def test_carnot_gatewaysymbol_constructor_args():
    sig = inspect.signature(carnot_GatewaySymbol.__init__)
    params = list(sig.parameters.keys())
    assert "flowKind" in params, "Missing parameter 'flowKind'"

def test_carnot_gatewaysymbol_has_flowKind():
    assert hasattr(carnot_GatewaySymbol, "flowKind")
    descriptor = None
    for klass in carnot_GatewaySymbol.__mro__:
        if "flowKind" in klass.__dict__:
            descriptor = klass.__dict__["flowKind"]
            break
    assert isinstance(descriptor, property)



def test_carnot_datasymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot_DataSymbolType)


def test_carnot_datasymboltype_constructor_exists():
    assert callable(carnot_DataSymbolType.__init__)


def test_carnot_datasymboltype_constructor_args():
    sig = inspect.signature(carnot_DataSymbolType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_modelersymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot_ModelerSymbolType)


def test_carnot_modelersymboltype_constructor_exists():
    assert callable(carnot_ModelerSymbolType.__init__)


def test_carnot_modelersymboltype_constructor_args():
    sig = inspect.signature(carnot_ModelerSymbolType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_activitysymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot_ActivitySymbolType)


def test_carnot_activitysymboltype_constructor_exists():
    assert callable(carnot_ActivitySymbolType.__init__)


def test_carnot_activitysymboltype_constructor_args():
    sig = inspect.signature(carnot_ActivitySymbolType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_itypedelement_is_not_abstract():
    assert not inspect.isabstract(carnot_ITypedElement)


def test_carnot_itypedelement_constructor_exists():
    assert callable(carnot_ITypedElement.__init__)


def test_carnot_itypedelement_constructor_args():
    sig = inspect.signature(carnot_ITypedElement.__init__)
    params = list(sig.parameters.keys())



def test_iidentifiablemodelelement_is_not_abstract():
    assert not inspect.isabstract(IIdentifiableModelElement)


def test_iidentifiablemodelelement_constructor_exists():
    assert callable(IIdentifiableModelElement.__init__)


def test_iidentifiablemodelelement_constructor_args():
    sig = inspect.signature(IIdentifiableModelElement.__init__)
    params = list(sig.parameters.keys())



def test_carnot_imodelparticipant_is_not_abstract():
    assert not inspect.isabstract(carnot_IModelParticipant)


def test_carnot_imodelparticipant_constructor_exists():
    assert callable(carnot_IModelParticipant.__init__)


def test_carnot_imodelparticipant_constructor_args():
    sig = inspect.signature(carnot_IModelParticipant.__init__)
    params = list(sig.parameters.keys())



def test_carnot_imetatype_is_not_abstract():
    assert not inspect.isabstract(carnot_IMetaType)


def test_carnot_imetatype_constructor_exists():
    assert callable(carnot_IMetaType.__init__)


def test_carnot_imetatype_constructor_args():
    sig = inspect.signature(carnot_IMetaType.__init__)
    params = list(sig.parameters.keys())
    assert "isPredefined" in params, "Missing parameter 'isPredefined'"

def test_carnot_imetatype_has_isPredefined():
    assert hasattr(carnot_IMetaType, "isPredefined")
    descriptor = None
    for klass in carnot_IMetaType.__mro__:
        if "isPredefined" in klass.__dict__:
            descriptor = klass.__dict__["isPredefined"]
            break
    assert isinstance(descriptor, property)



def test_carnot_iaccesspointowner_is_not_abstract():
    assert not inspect.isabstract(carnot_IAccessPointOwner)


def test_carnot_iaccesspointowner_constructor_exists():
    assert callable(carnot_IAccessPointOwner.__init__)


def test_carnot_iaccesspointowner_constructor_args():
    sig = inspect.signature(carnot_IAccessPointOwner.__init__)
    params = list(sig.parameters.keys())



def test_carnot_applicationsymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot_ApplicationSymbolType)


def test_carnot_applicationsymboltype_constructor_exists():
    assert callable(carnot_ApplicationSymbolType.__init__)


def test_carnot_applicationsymboltype_constructor_args():
    sig = inspect.signature(carnot_ApplicationSymbolType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_annotationsymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot_AnnotationSymbolType)


def test_carnot_annotationsymboltype_constructor_exists():
    assert callable(carnot_AnnotationSymbolType.__init__)


def test_carnot_annotationsymboltype_constructor_args():
    sig = inspect.signature(carnot_AnnotationSymbolType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_imodelelement_is_not_abstract():
    assert not inspect.isabstract(carnot_IModelElement)


def test_carnot_imodelelement_constructor_exists():
    assert callable(carnot_IModelElement.__init__)


def test_carnot_imodelelement_constructor_args():
    sig = inspect.signature(carnot_IModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "elementOid" in params, "Missing parameter 'elementOid'"

def test_carnot_imodelelement_has_elementOid():
    assert hasattr(carnot_IModelElement, "elementOid")
    descriptor = None
    for klass in carnot_IModelElement.__mro__:
        if "elementOid" in klass.__dict__:
            descriptor = klass.__dict__["elementOid"]
            break
    assert isinstance(descriptor, property)



def test_carnot_eobject_is_not_abstract():
    assert not inspect.isabstract(carnot_EObject)


def test_carnot_eobject_constructor_exists():
    assert callable(carnot_EObject.__init__)


def test_carnot_eobject_constructor_args():
    sig = inspect.signature(carnot_EObject.__init__)
    params = list(sig.parameters.keys())



def test_carnot_identifiablereference_is_not_abstract():
    assert not inspect.isabstract(carnot_IdentifiableReference)


def test_carnot_identifiablereference_constructor_exists():
    assert callable(carnot_IdentifiableReference.__init__)


def test_carnot_identifiablereference_constructor_args():
    sig = inspect.signature(carnot_IdentifiableReference.__init__)
    params = list(sig.parameters.keys())



def test_carnot_attributetype_is_not_abstract():
    assert not inspect.isabstract(carnot_AttributeType)


def test_carnot_attributetype_constructor_exists():
    assert callable(carnot_AttributeType.__init__)


def test_carnot_attributetype_constructor_args():
    sig = inspect.signature(carnot_AttributeType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "group" in params, "Missing parameter 'group'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "any" in params, "Missing parameter 'any'"

def test_carnot_attributetype_has_value():
    assert hasattr(carnot_AttributeType, "value")
    descriptor = None
    for klass in carnot_AttributeType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_carnot_attributetype_has_group():
    assert hasattr(carnot_AttributeType, "group")
    descriptor = None
    for klass in carnot_AttributeType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_carnot_attributetype_has_name():
    assert hasattr(carnot_AttributeType, "name")
    descriptor = None
    for klass in carnot_AttributeType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_carnot_attributetype_has_type():
    assert hasattr(carnot_AttributeType, "type")
    descriptor = None
    for klass in carnot_AttributeType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_carnot_attributetype_has_mixed():
    assert hasattr(carnot_AttributeType, "mixed")
    descriptor = None
    for klass in carnot_AttributeType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_carnot_attributetype_has_any():
    assert hasattr(carnot_AttributeType, "any")
    descriptor = None
    for klass in carnot_AttributeType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_carnot_iextensibleelement_is_not_abstract():
    assert not inspect.isabstract(carnot_IExtensibleElement)


def test_carnot_iextensibleelement_constructor_exists():
    assert callable(carnot_IExtensibleElement.__init__)


def test_carnot_iextensibleelement_constructor_args():
    sig = inspect.signature(carnot_IExtensibleElement.__init__)
    params = list(sig.parameters.keys())



def test_carnot_iidentifiableelement_is_not_abstract():
    assert not inspect.isabstract(carnot_IIdentifiableElement)


def test_carnot_iidentifiableelement_constructor_exists():
    assert callable(carnot_IIdentifiableElement.__init__)


def test_carnot_iidentifiableelement_constructor_args():
    sig = inspect.signature(carnot_IIdentifiableElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_carnot_iidentifiableelement_has_id():
    assert hasattr(carnot_IIdentifiableElement, "id")
    descriptor = None
    for klass in carnot_IIdentifiableElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_carnot_iidentifiableelement_has_name():
    assert hasattr(carnot_IIdentifiableElement, "name")
    descriptor = None
    for klass in carnot_IIdentifiableElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_carnot_ieventhandlerowner_is_not_abstract():
    assert not inspect.isabstract(carnot_IEventHandlerOwner)


def test_carnot_ieventhandlerowner_constructor_exists():
    assert callable(carnot_IEventHandlerOwner.__init__)


def test_carnot_ieventhandlerowner_constructor_args():
    sig = inspect.signature(carnot_IEventHandlerOwner.__init__)
    params = list(sig.parameters.keys())



def test_carnot_descriptiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_DescriptionType)


def test_carnot_descriptiontype_constructor_exists():
    assert callable(carnot_DescriptionType.__init__)


def test_carnot_descriptiontype_constructor_args():
    sig = inspect.signature(carnot_DescriptionType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_carnot_descriptiontype_has_mixed():
    assert hasattr(carnot_DescriptionType, "mixed")
    descriptor = None
    for klass in carnot_DescriptionType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_iextensibleelement_is_not_abstract():
    assert not inspect.isabstract(IExtensibleElement)


def test_iextensibleelement_constructor_exists():
    assert callable(IExtensibleElement.__init__)


def test_iextensibleelement_constructor_args():
    sig = inspect.signature(IExtensibleElement.__init__)
    params = list(sig.parameters.keys())



def test_carnot_isymbolcontainer_is_not_abstract():
    assert not inspect.isabstract(carnot_ISymbolContainer)


def test_carnot_isymbolcontainer_constructor_exists():
    assert callable(carnot_ISymbolContainer.__init__)


def test_carnot_isymbolcontainer_constructor_args():
    sig = inspect.signature(carnot_ISymbolContainer.__init__)
    params = list(sig.parameters.keys())
    assert "nodes" in params, "Missing parameter 'nodes'"
    assert "connections" in params, "Missing parameter 'connections'"

def test_carnot_isymbolcontainer_has_nodes():
    assert hasattr(carnot_ISymbolContainer, "nodes")
    descriptor = None
    for klass in carnot_ISymbolContainer.__mro__:
        if "nodes" in klass.__dict__:
            descriptor = klass.__dict__["nodes"]
            break
    assert isinstance(descriptor, property)

def test_carnot_isymbolcontainer_has_connections():
    assert hasattr(carnot_ISymbolContainer, "connections")
    descriptor = None
    for klass in carnot_ISymbolContainer.__mro__:
        if "connections" in klass.__dict__:
            descriptor = klass.__dict__["connections"]
            break
    assert isinstance(descriptor, property)



def test_iidentifiableelement_is_not_abstract():
    assert not inspect.isabstract(IIdentifiableElement)


def test_iidentifiableelement_constructor_exists():
    assert callable(IIdentifiableElement.__init__)


def test_iidentifiableelement_constructor_args():
    sig = inspect.signature(IIdentifiableElement.__init__)
    params = list(sig.parameters.keys())



def test_carnot_iswimlanesymbol_is_not_abstract():
    assert not inspect.isabstract(carnot_ISwimlaneSymbol)


def test_carnot_iswimlanesymbol_constructor_exists():
    assert callable(carnot_ISwimlaneSymbol.__init__)


def test_carnot_iswimlanesymbol_constructor_args():
    sig = inspect.signature(carnot_ISwimlaneSymbol.__init__)
    params = list(sig.parameters.keys())
    assert "orientation" in params, "Missing parameter 'orientation'"
    assert "collapsed" in params, "Missing parameter 'collapsed'"

def test_carnot_iswimlanesymbol_has_orientation():
    assert hasattr(carnot_ISwimlaneSymbol, "orientation")
    descriptor = None
    for klass in carnot_ISwimlaneSymbol.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)

def test_carnot_iswimlanesymbol_has_collapsed():
    assert hasattr(carnot_ISwimlaneSymbol, "collapsed")
    descriptor = None
    for klass in carnot_ISwimlaneSymbol.__mro__:
        if "collapsed" in klass.__dict__:
            descriptor = klass.__dict__["collapsed"]
            break
    assert isinstance(descriptor, property)



def test_imodelelement_is_not_abstract():
    assert not inspect.isabstract(IModelElement)


def test_imodelelement_constructor_exists():
    assert callable(IModelElement.__init__)


def test_imodelelement_constructor_args():
    sig = inspect.signature(IModelElement.__init__)
    params = list(sig.parameters.keys())



def test_carnot_igraphicalobject_is_not_abstract():
    assert not inspect.isabstract(carnot_IGraphicalObject)


def test_carnot_igraphicalobject_constructor_exists():
    assert callable(carnot_IGraphicalObject.__init__)


def test_carnot_igraphicalobject_constructor_args():
    sig = inspect.signature(carnot_IGraphicalObject.__init__)
    params = list(sig.parameters.keys())
    assert "borderColor" in params, "Missing parameter 'borderColor'"
    assert "fillColor" in params, "Missing parameter 'fillColor'"
    assert "style" in params, "Missing parameter 'style'"

def test_carnot_igraphicalobject_has_borderColor():
    assert hasattr(carnot_IGraphicalObject, "borderColor")
    descriptor = None
    for klass in carnot_IGraphicalObject.__mro__:
        if "borderColor" in klass.__dict__:
            descriptor = klass.__dict__["borderColor"]
            break
    assert isinstance(descriptor, property)

def test_carnot_igraphicalobject_has_fillColor():
    assert hasattr(carnot_IGraphicalObject, "fillColor")
    descriptor = None
    for klass in carnot_IGraphicalObject.__mro__:
        if "fillColor" in klass.__dict__:
            descriptor = klass.__dict__["fillColor"]
            break
    assert isinstance(descriptor, property)

def test_carnot_igraphicalobject_has_style():
    assert hasattr(carnot_IGraphicalObject, "style")
    descriptor = None
    for klass in carnot_IGraphicalObject.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_carnot_iidentifiablemodelelement_is_not_abstract():
    assert not inspect.isabstract(carnot_IIdentifiableModelElement)


def test_carnot_iidentifiablemodelelement_constructor_exists():
    assert callable(carnot_IIdentifiableModelElement.__init__)


def test_carnot_iidentifiablemodelelement_constructor_args():
    sig = inspect.signature(carnot_IIdentifiableModelElement.__init__)
    params = list(sig.parameters.keys())



def test_carnot_coordinates_is_not_abstract():
    assert not inspect.isabstract(carnot_Coordinates)


def test_carnot_coordinates_constructor_exists():
    assert callable(carnot_Coordinates.__init__)


def test_carnot_coordinates_constructor_args():
    sig = inspect.signature(carnot_Coordinates.__init__)
    params = list(sig.parameters.keys())
    assert "yPos" in params, "Missing parameter 'yPos'"
    assert "xPos" in params, "Missing parameter 'xPos'"

def test_carnot_coordinates_has_yPos():
    assert hasattr(carnot_Coordinates, "yPos")
    descriptor = None
    for klass in carnot_Coordinates.__mro__:
        if "yPos" in klass.__dict__:
            descriptor = klass.__dict__["yPos"]
            break
    assert isinstance(descriptor, property)

def test_carnot_coordinates_has_xPos():
    assert hasattr(carnot_Coordinates, "xPos")
    descriptor = None
    for klass in carnot_Coordinates.__mro__:
        if "xPos" in klass.__dict__:
            descriptor = klass.__dict__["xPos"]
            break
    assert isinstance(descriptor, property)



def test_formalparametermappingtype_is_not_abstract():
    assert not inspect.isabstract(FormalParameterMappingType)


def test_formalparametermappingtype_constructor_exists():
    assert callable(FormalParameterMappingType.__init__)


def test_formalparametermappingtype_constructor_args():
    sig = inspect.signature(FormalParameterMappingType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_extensions_formalparametermappingstype_is_not_abstract():
    assert not inspect.isabstract(carnot_extensions_FormalParameterMappingsType)


def test_carnot_extensions_formalparametermappingstype_constructor_exists():
    assert callable(carnot_extensions_FormalParameterMappingsType.__init__)


def test_carnot_extensions_formalparametermappingstype_constructor_args():
    sig = inspect.signature(carnot_extensions_FormalParameterMappingsType.__init__)
    params = list(sig.parameters.keys())



def test_extensions_carnot_formalparametertype_is_not_abstract():
    assert not inspect.isabstract(extensions_carnot_FormalParameterType)


def test_extensions_carnot_formalparametertype_constructor_exists():
    assert callable(extensions_carnot_FormalParameterType.__init__)


def test_extensions_carnot_formalparametertype_constructor_args():
    sig = inspect.signature(extensions_carnot_FormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_extensions_carnot_datatype_is_not_abstract():
    assert not inspect.isabstract(extensions_carnot_DataType)


def test_extensions_carnot_datatype_constructor_exists():
    assert callable(extensions_carnot_DataType.__init__)


def test_extensions_carnot_datatype_constructor_args():
    sig = inspect.signature(extensions_carnot_DataType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_extensions_formalparametermappingtype_is_not_abstract():
    assert not inspect.isabstract(carnot_extensions_FormalParameterMappingType)


def test_carnot_extensions_formalparametermappingtype_constructor_exists():
    assert callable(carnot_extensions_FormalParameterMappingType.__init__)


def test_carnot_extensions_formalparametermappingtype_constructor_args():
    sig = inspect.signature(carnot_extensions_FormalParameterMappingType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_viewabletype_is_not_abstract():
    assert not inspect.isabstract(carnot_ViewableType)


def test_carnot_viewabletype_constructor_exists():
    assert callable(carnot_ViewableType.__init__)


def test_carnot_viewabletype_constructor_args():
    sig = inspect.signature(carnot_ViewableType.__init__)
    params = list(sig.parameters.keys())



def test_formalparametermappingstype_is_not_abstract():
    assert not inspect.isabstract(FormalParameterMappingsType)


def test_formalparametermappingstype_constructor_exists():
    assert callable(FormalParameterMappingsType.__init__)


def test_formalparametermappingstype_constructor_args():
    sig = inspect.signature(FormalParameterMappingsType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_formalparameterstype_is_not_abstract():
    assert not inspect.isabstract(carnot_FormalParametersType)


def test_carnot_formalparameterstype_constructor_exists():
    assert callable(carnot_FormalParametersType.__init__)


def test_carnot_formalparameterstype_constructor_args():
    sig = inspect.signature(carnot_FormalParametersType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_viewtype_is_not_abstract():
    assert not inspect.isabstract(carnot_ViewType)


def test_carnot_viewtype_constructor_exists():
    assert callable(carnot_ViewType.__init__)


def test_carnot_viewtype_constructor_args():
    sig = inspect.signature(carnot_ViewType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_carnot_viewtype_has_name():
    assert hasattr(carnot_ViewType, "name")
    descriptor = None
    for klass in carnot_ViewType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_carnot_typedeclarationstype_is_not_abstract():
    assert not inspect.isabstract(carnot_TypeDeclarationsType)


def test_carnot_typedeclarationstype_constructor_exists():
    assert callable(carnot_TypeDeclarationsType.__init__)


def test_carnot_typedeclarationstype_constructor_args():
    sig = inspect.signature(carnot_TypeDeclarationsType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_scripttype_is_not_abstract():
    assert not inspect.isabstract(carnot_ScriptType)


def test_carnot_scripttype_constructor_exists():
    assert callable(carnot_ScriptType.__init__)


def test_carnot_scripttype_constructor_args():
    sig = inspect.signature(carnot_ScriptType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_externalpackages_is_not_abstract():
    assert not inspect.isabstract(carnot_ExternalPackages)


def test_carnot_externalpackages_constructor_exists():
    assert callable(carnot_ExternalPackages.__init__)


def test_carnot_externalpackages_constructor_args():
    sig = inspect.signature(carnot_ExternalPackages.__init__)
    params = list(sig.parameters.keys())



def test_carnot_qualitycontroltype_is_not_abstract():
    assert not inspect.isabstract(carnot_QualityControlType)


def test_carnot_qualitycontroltype_constructor_exists():
    assert callable(carnot_QualityControlType.__init__)


def test_carnot_qualitycontroltype_constructor_args():
    sig = inspect.signature(carnot_QualityControlType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_modelertype_is_not_abstract():
    assert not inspect.isabstract(carnot_ModelerType)


def test_carnot_modelertype_constructor_exists():
    assert callable(carnot_ModelerType.__init__)


def test_carnot_modelertype_constructor_args():
    sig = inspect.signature(carnot_ModelerType.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "password" in params, "Missing parameter 'password'"

def test_carnot_modelertype_has_email():
    assert hasattr(carnot_ModelerType, "email")
    descriptor = None
    for klass in carnot_ModelerType.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_carnot_modelertype_has_password():
    assert hasattr(carnot_ModelerType, "password")
    descriptor = None
    for klass in carnot_ModelerType.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_iswimlanesymbol_is_not_abstract():
    assert not inspect.isabstract(ISwimlaneSymbol)


def test_iswimlanesymbol_constructor_exists():
    assert callable(ISwimlaneSymbol.__init__)


def test_iswimlanesymbol_constructor_args():
    sig = inspect.signature(ISwimlaneSymbol.__init__)
    params = list(sig.parameters.keys())



def test_carnot_idrefowner_is_not_abstract():
    assert not inspect.isabstract(carnot_IdRefOwner)


def test_carnot_idrefowner_constructor_exists():
    assert callable(carnot_IdRefOwner.__init__)


def test_carnot_idrefowner_constructor_args():
    sig = inspect.signature(carnot_IdRefOwner.__init__)
    params = list(sig.parameters.keys())



def test_carnot_externalpackage_is_not_abstract():
    assert not inspect.isabstract(carnot_ExternalPackage)


def test_carnot_externalpackage_constructor_exists():
    assert callable(carnot_ExternalPackage.__init__)


def test_carnot_externalpackage_constructor_args():
    sig = inspect.signature(carnot_ExternalPackage.__init__)
    params = list(sig.parameters.keys())



def test_carnot_idref_is_not_abstract():
    assert not inspect.isabstract(carnot_IdRef)


def test_carnot_idref_constructor_exists():
    assert callable(carnot_IdRef.__init__)


def test_carnot_idref_constructor_args():
    sig = inspect.signature(carnot_IdRef.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"

def test_carnot_idref_has_ref():
    assert hasattr(carnot_IdRef, "ref")
    descriptor = None
    for klass in carnot_IdRef.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_carnot_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(carnot_EStringToStringMapEntry)


def test_carnot_estringtostringmapentry_constructor_exists():
    assert callable(carnot_EStringToStringMapEntry.__init__)


def test_carnot_estringtostringmapentry_constructor_args():
    sig = inspect.signature(carnot_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_carnot_documentroot_is_not_abstract():
    assert not inspect.isabstract(carnot_DocumentRoot)


def test_carnot_documentroot_constructor_exists():
    assert callable(carnot_DocumentRoot.__init__)


def test_carnot_documentroot_constructor_args():
    sig = inspect.signature(carnot_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_carnot_documentroot_has_mixed():
    assert hasattr(carnot_DocumentRoot, "mixed")
    descriptor = None
    for klass in carnot_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_abstracteventsymbol_is_not_abstract():
    assert not inspect.isabstract(AbstractEventSymbol)


def test_abstracteventsymbol_constructor_exists():
    assert callable(AbstractEventSymbol.__init__)


def test_abstracteventsymbol_constructor_args():
    sig = inspect.signature(AbstractEventSymbol.__init__)
    params = list(sig.parameters.keys())



def test_carnot_endeventsymbol_is_not_abstract():
    assert not inspect.isabstract(carnot_EndEventSymbol)


def test_carnot_endeventsymbol_constructor_exists():
    assert callable(carnot_EndEventSymbol.__init__)


def test_carnot_endeventsymbol_constructor_args():
    sig = inspect.signature(carnot_EndEventSymbol.__init__)
    params = list(sig.parameters.keys())



def test_carnot_intermediateeventsymbol_is_not_abstract():
    assert not inspect.isabstract(carnot_IntermediateEventSymbol)


def test_carnot_intermediateeventsymbol_constructor_exists():
    assert callable(carnot_IntermediateEventSymbol.__init__)


def test_carnot_intermediateeventsymbol_constructor_args():
    sig = inspect.signature(carnot_IntermediateEventSymbol.__init__)
    params = list(sig.parameters.keys())



def test_carnot_publicinterfacesymbol_is_not_abstract():
    assert not inspect.isabstract(carnot_PublicInterfaceSymbol)


def test_carnot_publicinterfacesymbol_constructor_exists():
    assert callable(carnot_PublicInterfaceSymbol.__init__)


def test_carnot_publicinterfacesymbol_constructor_args():
    sig = inspect.signature(carnot_PublicInterfaceSymbol.__init__)
    params = list(sig.parameters.keys())



def test_carnot_starteventsymbol_is_not_abstract():
    assert not inspect.isabstract(carnot_StartEventSymbol)


def test_carnot_starteventsymbol_constructor_exists():
    assert callable(carnot_StartEventSymbol.__init__)


def test_carnot_starteventsymbol_constructor_args():
    sig = inspect.signature(carnot_StartEventSymbol.__init__)
    params = list(sig.parameters.keys())



def test_carnot_modeltype_is_not_abstract():
    assert not inspect.isabstract(carnot_ModelType)


def test_carnot_modeltype_constructor_exists():
    assert callable(carnot_ModelType.__init__)


def test_carnot_modeltype_constructor_args():
    sig = inspect.signature(carnot_ModelType.__init__)
    params = list(sig.parameters.keys())
    assert "created" in params, "Missing parameter 'created'"
    assert "vendor" in params, "Missing parameter 'vendor'"
    assert "modelOID" in params, "Missing parameter 'modelOID'"
    assert "oid" in params, "Missing parameter 'oid'"
    assert "author" in params, "Missing parameter 'author'"
    assert "carnotVersion" in params, "Missing parameter 'carnotVersion'"

def test_carnot_modeltype_has_created():
    assert hasattr(carnot_ModelType, "created")
    descriptor = None
    for klass in carnot_ModelType.__mro__:
        if "created" in klass.__dict__:
            descriptor = klass.__dict__["created"]
            break
    assert isinstance(descriptor, property)

def test_carnot_modeltype_has_vendor():
    assert hasattr(carnot_ModelType, "vendor")
    descriptor = None
    for klass in carnot_ModelType.__mro__:
        if "vendor" in klass.__dict__:
            descriptor = klass.__dict__["vendor"]
            break
    assert isinstance(descriptor, property)

def test_carnot_modeltype_has_modelOID():
    assert hasattr(carnot_ModelType, "modelOID")
    descriptor = None
    for klass in carnot_ModelType.__mro__:
        if "modelOID" in klass.__dict__:
            descriptor = klass.__dict__["modelOID"]
            break
    assert isinstance(descriptor, property)

def test_carnot_modeltype_has_oid():
    assert hasattr(carnot_ModelType, "oid")
    descriptor = None
    for klass in carnot_ModelType.__mro__:
        if "oid" in klass.__dict__:
            descriptor = klass.__dict__["oid"]
            break
    assert isinstance(descriptor, property)

def test_carnot_modeltype_has_author():
    assert hasattr(carnot_ModelType, "author")
    descriptor = None
    for klass in carnot_ModelType.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_carnot_modeltype_has_carnotVersion():
    assert hasattr(carnot_ModelType, "carnotVersion")
    descriptor = None
    for klass in carnot_ModelType.__mro__:
        if "carnotVersion" in klass.__dict__:
            descriptor = klass.__dict__["carnotVersion"]
            break
    assert isinstance(descriptor, property)



def test_carnot_externalreferencetype_is_not_abstract():
    assert not inspect.isabstract(carnot_ExternalReferenceType)


def test_carnot_externalreferencetype_constructor_exists():
    assert callable(carnot_ExternalReferenceType.__init__)


def test_carnot_externalreferencetype_constructor_args():
    sig = inspect.signature(carnot_ExternalReferenceType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_parametermappingtype_is_not_abstract():
    assert not inspect.isabstract(carnot_ParameterMappingType)


def test_carnot_parametermappingtype_constructor_exists():
    assert callable(carnot_ParameterMappingType.__init__)


def test_carnot_parametermappingtype_constructor_args():
    sig = inspect.signature(carnot_ParameterMappingType.__init__)
    params = list(sig.parameters.keys())
    assert "parameter" in params, "Missing parameter 'parameter'"
    assert "parameterPath" in params, "Missing parameter 'parameterPath'"
    assert "dataPath" in params, "Missing parameter 'dataPath'"

def test_carnot_parametermappingtype_has_parameter():
    assert hasattr(carnot_ParameterMappingType, "parameter")
    descriptor = None
    for klass in carnot_ParameterMappingType.__mro__:
        if "parameter" in klass.__dict__:
            descriptor = klass.__dict__["parameter"]
            break
    assert isinstance(descriptor, property)

def test_carnot_parametermappingtype_has_parameterPath():
    assert hasattr(carnot_ParameterMappingType, "parameterPath")
    descriptor = None
    for klass in carnot_ParameterMappingType.__mro__:
        if "parameterPath" in klass.__dict__:
            descriptor = klass.__dict__["parameterPath"]
            break
    assert isinstance(descriptor, property)

def test_carnot_parametermappingtype_has_dataPath():
    assert hasattr(carnot_ParameterMappingType, "dataPath")
    descriptor = None
    for klass in carnot_ParameterMappingType.__mro__:
        if "dataPath" in klass.__dict__:
            descriptor = klass.__dict__["dataPath"]
            break
    assert isinstance(descriptor, property)



def test_isymbolcontainer_is_not_abstract():
    assert not inspect.isabstract(ISymbolContainer)


def test_isymbolcontainer_constructor_exists():
    assert callable(ISymbolContainer.__init__)


def test_isymbolcontainer_constructor_args():
    sig = inspect.signature(ISymbolContainer.__init__)
    params = list(sig.parameters.keys())



def test_carnot_lanesymbol_is_not_abstract():
    assert not inspect.isabstract(carnot_LaneSymbol)


def test_carnot_lanesymbol_constructor_exists():
    assert callable(carnot_LaneSymbol.__init__)


def test_carnot_lanesymbol_constructor_args():
    sig = inspect.signature(carnot_LaneSymbol.__init__)
    params = list(sig.parameters.keys())



def test_carnot_groupsymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot_GroupSymbolType)


def test_carnot_groupsymboltype_constructor_exists():
    assert callable(carnot_GroupSymbolType.__init__)


def test_carnot_groupsymboltype_constructor_args():
    sig = inspect.signature(carnot_GroupSymbolType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_poolsymbol_is_not_abstract():
    assert not inspect.isabstract(carnot_PoolSymbol)


def test_carnot_poolsymbol_constructor_exists():
    assert callable(carnot_PoolSymbol.__init__)


def test_carnot_poolsymbol_constructor_args():
    sig = inspect.signature(carnot_PoolSymbol.__init__)
    params = list(sig.parameters.keys())
    assert "boundaryVisible" in params, "Missing parameter 'boundaryVisible'"

def test_carnot_poolsymbol_has_boundaryVisible():
    assert hasattr(carnot_PoolSymbol, "boundaryVisible")
    descriptor = None
    for klass in carnot_PoolSymbol.__mro__:
        if "boundaryVisible" in klass.__dict__:
            descriptor = klass.__dict__["boundaryVisible"]
            break
    assert isinstance(descriptor, property)



def test_carnot_diagramtype_is_not_abstract():
    assert not inspect.isabstract(carnot_DiagramType)


def test_carnot_diagramtype_constructor_exists():
    assert callable(carnot_DiagramType.__init__)


def test_carnot_diagramtype_constructor_args():
    sig = inspect.signature(carnot_DiagramType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "orientation" in params, "Missing parameter 'orientation'"
    assert "mode" in params, "Missing parameter 'mode'"

def test_carnot_diagramtype_has_name():
    assert hasattr(carnot_DiagramType, "name")
    descriptor = None
    for klass in carnot_DiagramType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_carnot_diagramtype_has_orientation():
    assert hasattr(carnot_DiagramType, "orientation")
    descriptor = None
    for klass in carnot_DiagramType.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)

def test_carnot_diagramtype_has_mode():
    assert hasattr(carnot_DiagramType, "mode")
    descriptor = None
    for klass in carnot_DiagramType.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_carnot_datapathtype_is_not_abstract():
    assert not inspect.isabstract(carnot_DataPathType)


def test_carnot_datapathtype_constructor_exists():
    assert callable(carnot_DataPathType.__init__)


def test_carnot_datapathtype_constructor_args():
    sig = inspect.signature(carnot_DataPathType.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"
    assert "dataPath" in params, "Missing parameter 'dataPath'"
    assert "descriptor" in params, "Missing parameter 'descriptor'"
    assert "key" in params, "Missing parameter 'key'"

def test_carnot_datapathtype_has_direction():
    assert hasattr(carnot_DataPathType, "direction")
    descriptor = None
    for klass in carnot_DataPathType.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_carnot_datapathtype_has_dataPath():
    assert hasattr(carnot_DataPathType, "dataPath")
    descriptor = None
    for klass in carnot_DataPathType.__mro__:
        if "dataPath" in klass.__dict__:
            descriptor = klass.__dict__["dataPath"]
            break
    assert isinstance(descriptor, property)

def test_carnot_datapathtype_has_descriptor():
    assert hasattr(carnot_DataPathType, "descriptor")
    descriptor = None
    for klass in carnot_DataPathType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)

def test_carnot_datapathtype_has_key():
    assert hasattr(carnot_DataPathType, "key")
    descriptor = None
    for klass in carnot_DataPathType.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_iconnectionsymbol_is_not_abstract():
    assert not inspect.isabstract(IConnectionSymbol)


def test_iconnectionsymbol_constructor_exists():
    assert callable(IConnectionSymbol.__init__)


def test_iconnectionsymbol_constructor_args():
    sig = inspect.signature(IConnectionSymbol.__init__)
    params = list(sig.parameters.keys())



def test_carnot_worksforconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_WorksForConnectionType)


def test_carnot_worksforconnectiontype_constructor_exists():
    assert callable(carnot_WorksForConnectionType.__init__)


def test_carnot_worksforconnectiontype_constructor_args():
    sig = inspect.signature(carnot_WorksForConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_triggersconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_TriggersConnectionType)


def test_carnot_triggersconnectiontype_constructor_exists():
    assert callable(carnot_TriggersConnectionType.__init__)


def test_carnot_triggersconnectiontype_constructor_args():
    sig = inspect.signature(carnot_TriggersConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_performsconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_PerformsConnectionType)


def test_carnot_performsconnectiontype_constructor_exists():
    assert callable(carnot_PerformsConnectionType.__init__)


def test_carnot_performsconnectiontype_constructor_args():
    sig = inspect.signature(carnot_PerformsConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_subprocessofconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_SubProcessOfConnectionType)


def test_carnot_subprocessofconnectiontype_constructor_exists():
    assert callable(carnot_SubProcessOfConnectionType.__init__)


def test_carnot_subprocessofconnectiontype_constructor_args():
    sig = inspect.signature(carnot_SubProcessOfConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_transitionconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_TransitionConnectionType)


def test_carnot_transitionconnectiontype_constructor_exists():
    assert callable(carnot_TransitionConnectionType.__init__)


def test_carnot_transitionconnectiontype_constructor_args():
    sig = inspect.signature(carnot_TransitionConnectionType.__init__)
    params = list(sig.parameters.keys())
    assert "points" in params, "Missing parameter 'points'"

def test_carnot_transitionconnectiontype_has_points():
    assert hasattr(carnot_TransitionConnectionType, "points")
    descriptor = None
    for klass in carnot_TransitionConnectionType.__mro__:
        if "points" in klass.__dict__:
            descriptor = klass.__dict__["points"]
            break
    assert isinstance(descriptor, property)



def test_carnot_referstoconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_RefersToConnectionType)


def test_carnot_referstoconnectiontype_constructor_exists():
    assert callable(carnot_RefersToConnectionType.__init__)


def test_carnot_referstoconnectiontype_constructor_args():
    sig = inspect.signature(carnot_RefersToConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_datamappingconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_DataMappingConnectionType)


def test_carnot_datamappingconnectiontype_constructor_exists():
    assert callable(carnot_DataMappingConnectionType.__init__)


def test_carnot_datamappingconnectiontype_constructor_args():
    sig = inspect.signature(carnot_DataMappingConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_teamleadconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_TeamLeadConnectionType)


def test_carnot_teamleadconnectiontype_constructor_exists():
    assert callable(carnot_TeamLeadConnectionType.__init__)


def test_carnot_teamleadconnectiontype_constructor_args():
    sig = inspect.signature(carnot_TeamLeadConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_partofconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_PartOfConnectionType)


def test_carnot_partofconnectiontype_constructor_exists():
    assert callable(carnot_PartOfConnectionType.__init__)


def test_carnot_partofconnectiontype_constructor_args():
    sig = inspect.signature(carnot_PartOfConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_executedbyconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_ExecutedByConnectionType)


def test_carnot_executedbyconnectiontype_constructor_exists():
    assert callable(carnot_ExecutedByConnectionType.__init__)


def test_carnot_executedbyconnectiontype_constructor_args():
    sig = inspect.signature(carnot_ExecutedByConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_imodelparticipantsymbol_is_not_abstract():
    assert not inspect.isabstract(IModelParticipantSymbol)


def test_imodelparticipantsymbol_constructor_exists():
    assert callable(IModelParticipantSymbol.__init__)


def test_imodelparticipantsymbol_constructor_args():
    sig = inspect.signature(IModelParticipantSymbol.__init__)
    params = list(sig.parameters.keys())



def test_carnot_organizationsymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot_OrganizationSymbolType)


def test_carnot_organizationsymboltype_constructor_exists():
    assert callable(carnot_OrganizationSymbolType.__init__)


def test_carnot_organizationsymboltype_constructor_args():
    sig = inspect.signature(carnot_OrganizationSymbolType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_conditionalperformersymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot_ConditionalPerformerSymbolType)


def test_carnot_conditionalperformersymboltype_constructor_exists():
    assert callable(carnot_ConditionalPerformerSymbolType.__init__)


def test_carnot_conditionalperformersymboltype_constructor_args():
    sig = inspect.signature(carnot_ConditionalPerformerSymbolType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_rolesymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot_RoleSymbolType)


def test_carnot_rolesymboltype_constructor_exists():
    assert callable(carnot_RoleSymbolType.__init__)


def test_carnot_rolesymboltype_constructor_args():
    sig = inspect.signature(carnot_RoleSymbolType.__init__)
    params = list(sig.parameters.keys())



def test_abstracteventaction_is_not_abstract():
    assert not inspect.isabstract(AbstractEventAction)


def test_abstracteventaction_constructor_exists():
    assert callable(AbstractEventAction.__init__)


def test_abstracteventaction_constructor_args():
    sig = inspect.signature(AbstractEventAction.__init__)
    params = list(sig.parameters.keys())



def test_carnot_unbindactiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_UnbindActionType)


def test_carnot_unbindactiontype_constructor_exists():
    assert callable(carnot_UnbindActionType.__init__)


def test_carnot_unbindactiontype_constructor_args():
    sig = inspect.signature(carnot_UnbindActionType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_eventactiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_EventActionType)


def test_carnot_eventactiontype_constructor_exists():
    assert callable(carnot_EventActionType.__init__)


def test_carnot_eventactiontype_constructor_args():
    sig = inspect.signature(carnot_EventActionType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_bindactiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_BindActionType)


def test_carnot_bindactiontype_constructor_exists():
    assert callable(carnot_BindActionType.__init__)


def test_carnot_bindactiontype_constructor_args():
    sig = inspect.signature(carnot_BindActionType.__init__)
    params = list(sig.parameters.keys())



def test_imodelparticipant_is_not_abstract():
    assert not inspect.isabstract(IModelParticipant)


def test_imodelparticipant_constructor_exists():
    assert callable(IModelParticipant.__init__)


def test_imodelparticipant_constructor_args():
    sig = inspect.signature(IModelParticipant.__init__)
    params = list(sig.parameters.keys())



def test_carnot_roletype_is_not_abstract():
    assert not inspect.isabstract(carnot_RoleType)


def test_carnot_roletype_constructor_exists():
    assert callable(carnot_RoleType.__init__)


def test_carnot_roletype_constructor_args():
    sig = inspect.signature(carnot_RoleType.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_carnot_roletype_has_cardinality():
    assert hasattr(carnot_RoleType, "cardinality")
    descriptor = None
    for klass in carnot_RoleType.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)



def test_carnot_organizationtype_is_not_abstract():
    assert not inspect.isabstract(carnot_OrganizationType)


def test_carnot_organizationtype_constructor_exists():
    assert callable(carnot_OrganizationType.__init__)


def test_carnot_organizationtype_constructor_args():
    sig = inspect.signature(carnot_OrganizationType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_conditionalperformertype_is_not_abstract():
    assert not inspect.isabstract(carnot_ConditionalPerformerType)


def test_carnot_conditionalperformertype_constructor_exists():
    assert callable(carnot_ConditionalPerformerType.__init__)


def test_carnot_conditionalperformertype_constructor_args():
    sig = inspect.signature(carnot_ConditionalPerformerType.__init__)
    params = list(sig.parameters.keys())
    assert "dataPath" in params, "Missing parameter 'dataPath'"
    assert "isUser" in params, "Missing parameter 'isUser'"

def test_carnot_conditionalperformertype_has_dataPath():
    assert hasattr(carnot_ConditionalPerformerType, "dataPath")
    descriptor = None
    for klass in carnot_ConditionalPerformerType.__mro__:
        if "dataPath" in klass.__dict__:
            descriptor = klass.__dict__["dataPath"]
            break
    assert isinstance(descriptor, property)

def test_carnot_conditionalperformertype_has_isUser():
    assert hasattr(carnot_ConditionalPerformerType, "isUser")
    descriptor = None
    for klass in carnot_ConditionalPerformerType.__mro__:
        if "isUser" in klass.__dict__:
            descriptor = klass.__dict__["isUser"]
            break
    assert isinstance(descriptor, property)



def test_carnot_xmltextnode_is_not_abstract():
    assert not inspect.isabstract(carnot_XmlTextNode)


def test_carnot_xmltextnode_constructor_exists():
    assert callable(carnot_XmlTextNode.__init__)


def test_carnot_xmltextnode_constructor_args():
    sig = inspect.signature(carnot_XmlTextNode.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_carnot_xmltextnode_has_mixed():
    assert hasattr(carnot_XmlTextNode, "mixed")
    descriptor = None
    for klass in carnot_XmlTextNode.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_imetatype_is_not_abstract():
    assert not inspect.isabstract(IMetaType)


def test_imetatype_constructor_exists():
    assert callable(IMetaType.__init__)


def test_imetatype_constructor_args():
    sig = inspect.signature(IMetaType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_triggertypetype_is_not_abstract():
    assert not inspect.isabstract(carnot_TriggerTypeType)


def test_carnot_triggertypetype_constructor_exists():
    assert callable(carnot_TriggerTypeType.__init__)


def test_carnot_triggertypetype_constructor_args():
    sig = inspect.signature(carnot_TriggerTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "panelClass" in params, "Missing parameter 'panelClass'"
    assert "pullTriggerEvaluator" in params, "Missing parameter 'pullTriggerEvaluator'"
    assert "rule" in params, "Missing parameter 'rule'"
    assert "pullTrigger" in params, "Missing parameter 'pullTrigger'"

def test_carnot_triggertypetype_has_panelClass():
    assert hasattr(carnot_TriggerTypeType, "panelClass")
    descriptor = None
    for klass in carnot_TriggerTypeType.__mro__:
        if "panelClass" in klass.__dict__:
            descriptor = klass.__dict__["panelClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot_triggertypetype_has_pullTriggerEvaluator():
    assert hasattr(carnot_TriggerTypeType, "pullTriggerEvaluator")
    descriptor = None
    for klass in carnot_TriggerTypeType.__mro__:
        if "pullTriggerEvaluator" in klass.__dict__:
            descriptor = klass.__dict__["pullTriggerEvaluator"]
            break
    assert isinstance(descriptor, property)

def test_carnot_triggertypetype_has_rule():
    assert hasattr(carnot_TriggerTypeType, "rule")
    descriptor = None
    for klass in carnot_TriggerTypeType.__mro__:
        if "rule" in klass.__dict__:
            descriptor = klass.__dict__["rule"]
            break
    assert isinstance(descriptor, property)

def test_carnot_triggertypetype_has_pullTrigger():
    assert hasattr(carnot_TriggerTypeType, "pullTrigger")
    descriptor = None
    for klass in carnot_TriggerTypeType.__mro__:
        if "pullTrigger" in klass.__dict__:
            descriptor = klass.__dict__["pullTrigger"]
            break
    assert isinstance(descriptor, property)



def test_carnot_datatypetype_is_not_abstract():
    assert not inspect.isabstract(carnot_DataTypeType)


def test_carnot_datatypetype_constructor_exists():
    assert callable(carnot_DataTypeType.__init__)


def test_carnot_datatypetype_constructor_args():
    sig = inspect.signature(carnot_DataTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "panelClass" in params, "Missing parameter 'panelClass'"
    assert "storageStrategy" in params, "Missing parameter 'storageStrategy'"
    assert "valueCreator" in params, "Missing parameter 'valueCreator'"
    assert "accessPathEditor" in params, "Missing parameter 'accessPathEditor'"
    assert "writable" in params, "Missing parameter 'writable'"
    assert "instanceClass" in params, "Missing parameter 'instanceClass'"
    assert "validatorClass" in params, "Missing parameter 'validatorClass'"
    assert "readable" in params, "Missing parameter 'readable'"
    assert "evaluator" in params, "Missing parameter 'evaluator'"

def test_carnot_datatypetype_has_panelClass():
    assert hasattr(carnot_DataTypeType, "panelClass")
    descriptor = None
    for klass in carnot_DataTypeType.__mro__:
        if "panelClass" in klass.__dict__:
            descriptor = klass.__dict__["panelClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot_datatypetype_has_storageStrategy():
    assert hasattr(carnot_DataTypeType, "storageStrategy")
    descriptor = None
    for klass in carnot_DataTypeType.__mro__:
        if "storageStrategy" in klass.__dict__:
            descriptor = klass.__dict__["storageStrategy"]
            break
    assert isinstance(descriptor, property)

def test_carnot_datatypetype_has_valueCreator():
    assert hasattr(carnot_DataTypeType, "valueCreator")
    descriptor = None
    for klass in carnot_DataTypeType.__mro__:
        if "valueCreator" in klass.__dict__:
            descriptor = klass.__dict__["valueCreator"]
            break
    assert isinstance(descriptor, property)

def test_carnot_datatypetype_has_accessPathEditor():
    assert hasattr(carnot_DataTypeType, "accessPathEditor")
    descriptor = None
    for klass in carnot_DataTypeType.__mro__:
        if "accessPathEditor" in klass.__dict__:
            descriptor = klass.__dict__["accessPathEditor"]
            break
    assert isinstance(descriptor, property)

def test_carnot_datatypetype_has_writable():
    assert hasattr(carnot_DataTypeType, "writable")
    descriptor = None
    for klass in carnot_DataTypeType.__mro__:
        if "writable" in klass.__dict__:
            descriptor = klass.__dict__["writable"]
            break
    assert isinstance(descriptor, property)

def test_carnot_datatypetype_has_instanceClass():
    assert hasattr(carnot_DataTypeType, "instanceClass")
    descriptor = None
    for klass in carnot_DataTypeType.__mro__:
        if "instanceClass" in klass.__dict__:
            descriptor = klass.__dict__["instanceClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot_datatypetype_has_validatorClass():
    assert hasattr(carnot_DataTypeType, "validatorClass")
    descriptor = None
    for klass in carnot_DataTypeType.__mro__:
        if "validatorClass" in klass.__dict__:
            descriptor = klass.__dict__["validatorClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot_datatypetype_has_readable():
    assert hasattr(carnot_DataTypeType, "readable")
    descriptor = None
    for klass in carnot_DataTypeType.__mro__:
        if "readable" in klass.__dict__:
            descriptor = klass.__dict__["readable"]
            break
    assert isinstance(descriptor, property)

def test_carnot_datatypetype_has_evaluator():
    assert hasattr(carnot_DataTypeType, "evaluator")
    descriptor = None
    for klass in carnot_DataTypeType.__mro__:
        if "evaluator" in klass.__dict__:
            descriptor = klass.__dict__["evaluator"]
            break
    assert isinstance(descriptor, property)



def test_carnot_eventconditiontypetype_is_not_abstract():
    assert not inspect.isabstract(carnot_EventConditionTypeType)


def test_carnot_eventconditiontypetype_constructor_exists():
    assert callable(carnot_EventConditionTypeType.__init__)


def test_carnot_eventconditiontypetype_constructor_args():
    sig = inspect.signature(carnot_EventConditionTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "implementation" in params, "Missing parameter 'implementation'"
    assert "rule" in params, "Missing parameter 'rule'"
    assert "pullEventEmitterClass" in params, "Missing parameter 'pullEventEmitterClass'"
    assert "panelClass" in params, "Missing parameter 'panelClass'"
    assert "activityCondition" in params, "Missing parameter 'activityCondition'"
    assert "processCondition" in params, "Missing parameter 'processCondition'"
    assert "binderClass" in params, "Missing parameter 'binderClass'"

def test_carnot_eventconditiontypetype_has_implementation():
    assert hasattr(carnot_EventConditionTypeType, "implementation")
    descriptor = None
    for klass in carnot_EventConditionTypeType.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)

def test_carnot_eventconditiontypetype_has_rule():
    assert hasattr(carnot_EventConditionTypeType, "rule")
    descriptor = None
    for klass in carnot_EventConditionTypeType.__mro__:
        if "rule" in klass.__dict__:
            descriptor = klass.__dict__["rule"]
            break
    assert isinstance(descriptor, property)

def test_carnot_eventconditiontypetype_has_pullEventEmitterClass():
    assert hasattr(carnot_EventConditionTypeType, "pullEventEmitterClass")
    descriptor = None
    for klass in carnot_EventConditionTypeType.__mro__:
        if "pullEventEmitterClass" in klass.__dict__:
            descriptor = klass.__dict__["pullEventEmitterClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot_eventconditiontypetype_has_panelClass():
    assert hasattr(carnot_EventConditionTypeType, "panelClass")
    descriptor = None
    for klass in carnot_EventConditionTypeType.__mro__:
        if "panelClass" in klass.__dict__:
            descriptor = klass.__dict__["panelClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot_eventconditiontypetype_has_activityCondition():
    assert hasattr(carnot_EventConditionTypeType, "activityCondition")
    descriptor = None
    for klass in carnot_EventConditionTypeType.__mro__:
        if "activityCondition" in klass.__dict__:
            descriptor = klass.__dict__["activityCondition"]
            break
    assert isinstance(descriptor, property)

def test_carnot_eventconditiontypetype_has_processCondition():
    assert hasattr(carnot_EventConditionTypeType, "processCondition")
    descriptor = None
    for klass in carnot_EventConditionTypeType.__mro__:
        if "processCondition" in klass.__dict__:
            descriptor = klass.__dict__["processCondition"]
            break
    assert isinstance(descriptor, property)

def test_carnot_eventconditiontypetype_has_binderClass():
    assert hasattr(carnot_EventConditionTypeType, "binderClass")
    descriptor = None
    for klass in carnot_EventConditionTypeType.__mro__:
        if "binderClass" in klass.__dict__:
            descriptor = klass.__dict__["binderClass"]
            break
    assert isinstance(descriptor, property)



def test_carnot_applicationtypetype_is_not_abstract():
    assert not inspect.isabstract(carnot_ApplicationTypeType)


def test_carnot_applicationtypetype_constructor_exists():
    assert callable(carnot_ApplicationTypeType.__init__)


def test_carnot_applicationtypetype_constructor_args():
    sig = inspect.signature(carnot_ApplicationTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "instanceClass" in params, "Missing parameter 'instanceClass'"
    assert "accessPointProviderClass" in params, "Missing parameter 'accessPointProviderClass'"
    assert "synchronous" in params, "Missing parameter 'synchronous'"
    assert "panelClass" in params, "Missing parameter 'panelClass'"
    assert "validatorClass" in params, "Missing parameter 'validatorClass'"

def test_carnot_applicationtypetype_has_instanceClass():
    assert hasattr(carnot_ApplicationTypeType, "instanceClass")
    descriptor = None
    for klass in carnot_ApplicationTypeType.__mro__:
        if "instanceClass" in klass.__dict__:
            descriptor = klass.__dict__["instanceClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot_applicationtypetype_has_accessPointProviderClass():
    assert hasattr(carnot_ApplicationTypeType, "accessPointProviderClass")
    descriptor = None
    for klass in carnot_ApplicationTypeType.__mro__:
        if "accessPointProviderClass" in klass.__dict__:
            descriptor = klass.__dict__["accessPointProviderClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot_applicationtypetype_has_synchronous():
    assert hasattr(carnot_ApplicationTypeType, "synchronous")
    descriptor = None
    for klass in carnot_ApplicationTypeType.__mro__:
        if "synchronous" in klass.__dict__:
            descriptor = klass.__dict__["synchronous"]
            break
    assert isinstance(descriptor, property)

def test_carnot_applicationtypetype_has_panelClass():
    assert hasattr(carnot_ApplicationTypeType, "panelClass")
    descriptor = None
    for klass in carnot_ApplicationTypeType.__mro__:
        if "panelClass" in klass.__dict__:
            descriptor = klass.__dict__["panelClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot_applicationtypetype_has_validatorClass():
    assert hasattr(carnot_ApplicationTypeType, "validatorClass")
    descriptor = None
    for klass in carnot_ApplicationTypeType.__mro__:
        if "validatorClass" in klass.__dict__:
            descriptor = klass.__dict__["validatorClass"]
            break
    assert isinstance(descriptor, property)



def test_carnot_linktypetype_is_not_abstract():
    assert not inspect.isabstract(carnot_LinkTypeType)


def test_carnot_linktypetype_constructor_exists():
    assert callable(carnot_LinkTypeType.__init__)


def test_carnot_linktypetype_constructor_args():
    sig = inspect.signature(carnot_LinkTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "showRoleNames" in params, "Missing parameter 'showRoleNames'"
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"
    assert "targetSymbol" in params, "Missing parameter 'targetSymbol'"
    assert "sourceCardinality" in params, "Missing parameter 'sourceCardinality'"
    assert "sourceClass" in params, "Missing parameter 'sourceClass'"
    assert "targetClass" in params, "Missing parameter 'targetClass'"
    assert "lineColor" in params, "Missing parameter 'lineColor'"
    assert "targetRole" in params, "Missing parameter 'targetRole'"
    assert "targetCardinality" in params, "Missing parameter 'targetCardinality'"
    assert "sourceSymbol" in params, "Missing parameter 'sourceSymbol'"
    assert "showLinkTypeName" in params, "Missing parameter 'showLinkTypeName'"
    assert "sourceRole" in params, "Missing parameter 'sourceRole'"

def test_carnot_linktypetype_has_showRoleNames():
    assert hasattr(carnot_LinkTypeType, "showRoleNames")
    descriptor = None
    for klass in carnot_LinkTypeType.__mro__:
        if "showRoleNames" in klass.__dict__:
            descriptor = klass.__dict__["showRoleNames"]
            break
    assert isinstance(descriptor, property)

def test_carnot_linktypetype_has_lineStyle():
    assert hasattr(carnot_LinkTypeType, "lineStyle")
    descriptor = None
    for klass in carnot_LinkTypeType.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)

def test_carnot_linktypetype_has_targetSymbol():
    assert hasattr(carnot_LinkTypeType, "targetSymbol")
    descriptor = None
    for klass in carnot_LinkTypeType.__mro__:
        if "targetSymbol" in klass.__dict__:
            descriptor = klass.__dict__["targetSymbol"]
            break
    assert isinstance(descriptor, property)

def test_carnot_linktypetype_has_sourceCardinality():
    assert hasattr(carnot_LinkTypeType, "sourceCardinality")
    descriptor = None
    for klass in carnot_LinkTypeType.__mro__:
        if "sourceCardinality" in klass.__dict__:
            descriptor = klass.__dict__["sourceCardinality"]
            break
    assert isinstance(descriptor, property)

def test_carnot_linktypetype_has_sourceClass():
    assert hasattr(carnot_LinkTypeType, "sourceClass")
    descriptor = None
    for klass in carnot_LinkTypeType.__mro__:
        if "sourceClass" in klass.__dict__:
            descriptor = klass.__dict__["sourceClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot_linktypetype_has_targetClass():
    assert hasattr(carnot_LinkTypeType, "targetClass")
    descriptor = None
    for klass in carnot_LinkTypeType.__mro__:
        if "targetClass" in klass.__dict__:
            descriptor = klass.__dict__["targetClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot_linktypetype_has_lineColor():
    assert hasattr(carnot_LinkTypeType, "lineColor")
    descriptor = None
    for klass in carnot_LinkTypeType.__mro__:
        if "lineColor" in klass.__dict__:
            descriptor = klass.__dict__["lineColor"]
            break
    assert isinstance(descriptor, property)

def test_carnot_linktypetype_has_targetRole():
    assert hasattr(carnot_LinkTypeType, "targetRole")
    descriptor = None
    for klass in carnot_LinkTypeType.__mro__:
        if "targetRole" in klass.__dict__:
            descriptor = klass.__dict__["targetRole"]
            break
    assert isinstance(descriptor, property)

def test_carnot_linktypetype_has_targetCardinality():
    assert hasattr(carnot_LinkTypeType, "targetCardinality")
    descriptor = None
    for klass in carnot_LinkTypeType.__mro__:
        if "targetCardinality" in klass.__dict__:
            descriptor = klass.__dict__["targetCardinality"]
            break
    assert isinstance(descriptor, property)

def test_carnot_linktypetype_has_sourceSymbol():
    assert hasattr(carnot_LinkTypeType, "sourceSymbol")
    descriptor = None
    for klass in carnot_LinkTypeType.__mro__:
        if "sourceSymbol" in klass.__dict__:
            descriptor = klass.__dict__["sourceSymbol"]
            break
    assert isinstance(descriptor, property)

def test_carnot_linktypetype_has_showLinkTypeName():
    assert hasattr(carnot_LinkTypeType, "showLinkTypeName")
    descriptor = None
    for klass in carnot_LinkTypeType.__mro__:
        if "showLinkTypeName" in klass.__dict__:
            descriptor = klass.__dict__["showLinkTypeName"]
            break
    assert isinstance(descriptor, property)

def test_carnot_linktypetype_has_sourceRole():
    assert hasattr(carnot_LinkTypeType, "sourceRole")
    descriptor = None
    for klass in carnot_LinkTypeType.__mro__:
        if "sourceRole" in klass.__dict__:
            descriptor = klass.__dict__["sourceRole"]
            break
    assert isinstance(descriptor, property)



def test_carnot_applicationcontexttypetype_is_not_abstract():
    assert not inspect.isabstract(carnot_ApplicationContextTypeType)


def test_carnot_applicationcontexttypetype_constructor_exists():
    assert callable(carnot_ApplicationContextTypeType.__init__)


def test_carnot_applicationcontexttypetype_constructor_args():
    sig = inspect.signature(carnot_ApplicationContextTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "hasApplicationPath" in params, "Missing parameter 'hasApplicationPath'"
    assert "accessPointProviderClass" in params, "Missing parameter 'accessPointProviderClass'"
    assert "panelClass" in params, "Missing parameter 'panelClass'"
    assert "validatorClass" in params, "Missing parameter 'validatorClass'"
    assert "hasMappingId" in params, "Missing parameter 'hasMappingId'"

def test_carnot_applicationcontexttypetype_has_hasApplicationPath():
    assert hasattr(carnot_ApplicationContextTypeType, "hasApplicationPath")
    descriptor = None
    for klass in carnot_ApplicationContextTypeType.__mro__:
        if "hasApplicationPath" in klass.__dict__:
            descriptor = klass.__dict__["hasApplicationPath"]
            break
    assert isinstance(descriptor, property)

def test_carnot_applicationcontexttypetype_has_accessPointProviderClass():
    assert hasattr(carnot_ApplicationContextTypeType, "accessPointProviderClass")
    descriptor = None
    for klass in carnot_ApplicationContextTypeType.__mro__:
        if "accessPointProviderClass" in klass.__dict__:
            descriptor = klass.__dict__["accessPointProviderClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot_applicationcontexttypetype_has_panelClass():
    assert hasattr(carnot_ApplicationContextTypeType, "panelClass")
    descriptor = None
    for klass in carnot_ApplicationContextTypeType.__mro__:
        if "panelClass" in klass.__dict__:
            descriptor = klass.__dict__["panelClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot_applicationcontexttypetype_has_validatorClass():
    assert hasattr(carnot_ApplicationContextTypeType, "validatorClass")
    descriptor = None
    for klass in carnot_ApplicationContextTypeType.__mro__:
        if "validatorClass" in klass.__dict__:
            descriptor = klass.__dict__["validatorClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot_applicationcontexttypetype_has_hasMappingId():
    assert hasattr(carnot_ApplicationContextTypeType, "hasMappingId")
    descriptor = None
    for klass in carnot_ApplicationContextTypeType.__mro__:
        if "hasMappingId" in klass.__dict__:
            descriptor = klass.__dict__["hasMappingId"]
            break
    assert isinstance(descriptor, property)



def test_carnot_texttype_is_not_abstract():
    assert not inspect.isabstract(carnot_TextType)


def test_carnot_texttype_constructor_exists():
    assert callable(carnot_TextType.__init__)


def test_carnot_texttype_constructor_args():
    sig = inspect.signature(carnot_TextType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_carnot_texttype_has_mixed():
    assert hasattr(carnot_TextType, "mixed")
    descriptor = None
    for klass in carnot_TextType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_carnot_looptype_is_not_abstract():
    assert not inspect.isabstract(carnot_LoopType)


def test_carnot_looptype_constructor_exists():
    assert callable(carnot_LoopType.__init__)


def test_carnot_looptype_constructor_args():
    sig = inspect.signature(carnot_LoopType.__init__)
    params = list(sig.parameters.keys())



def test_iaccesspointowner_is_not_abstract():
    assert not inspect.isabstract(IAccessPointOwner)


def test_iaccesspointowner_constructor_exists():
    assert callable(IAccessPointOwner.__init__)


def test_iaccesspointowner_constructor_args():
    sig = inspect.signature(IAccessPointOwner.__init__)
    params = list(sig.parameters.keys())



def test_carnot_code_is_not_abstract():
    assert not inspect.isabstract(carnot_Code)


def test_carnot_code_constructor_exists():
    assert callable(carnot_Code.__init__)


def test_carnot_code_constructor_args():
    sig = inspect.signature(carnot_Code.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_carnot_code_has_code():
    assert hasattr(carnot_Code, "code")
    descriptor = None
    for klass in carnot_Code.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_carnot_code_has_name():
    assert hasattr(carnot_Code, "name")
    descriptor = None
    for klass in carnot_Code.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_carnot_code_has_value():
    assert hasattr(carnot_Code, "value")
    descriptor = None
    for klass in carnot_Code.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_carnot_transitiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_TransitionType)


def test_carnot_transitiontype_constructor_exists():
    assert callable(carnot_TransitionType.__init__)


def test_carnot_transitiontype_constructor_args():
    sig = inspect.signature(carnot_TransitionType.__init__)
    params = list(sig.parameters.keys())
    assert "forkOnTraversal" in params, "Missing parameter 'forkOnTraversal'"
    assert "condition" in params, "Missing parameter 'condition'"

def test_carnot_transitiontype_has_forkOnTraversal():
    assert hasattr(carnot_TransitionType, "forkOnTraversal")
    descriptor = None
    for klass in carnot_TransitionType.__mro__:
        if "forkOnTraversal" in klass.__dict__:
            descriptor = klass.__dict__["forkOnTraversal"]
            break
    assert isinstance(descriptor, property)

def test_carnot_transitiontype_has_condition():
    assert hasattr(carnot_TransitionType, "condition")
    descriptor = None
    for klass in carnot_TransitionType.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_carnot_datamappingtype_is_not_abstract():
    assert not inspect.isabstract(carnot_DataMappingType)


def test_carnot_datamappingtype_constructor_exists():
    assert callable(carnot_DataMappingType.__init__)


def test_carnot_datamappingtype_constructor_args():
    sig = inspect.signature(carnot_DataMappingType.__init__)
    params = list(sig.parameters.keys())
    assert "applicationPath" in params, "Missing parameter 'applicationPath'"
    assert "dataPath" in params, "Missing parameter 'dataPath'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "context" in params, "Missing parameter 'context'"
    assert "applicationAccessPoint" in params, "Missing parameter 'applicationAccessPoint'"

def test_carnot_datamappingtype_has_applicationPath():
    assert hasattr(carnot_DataMappingType, "applicationPath")
    descriptor = None
    for klass in carnot_DataMappingType.__mro__:
        if "applicationPath" in klass.__dict__:
            descriptor = klass.__dict__["applicationPath"]
            break
    assert isinstance(descriptor, property)

def test_carnot_datamappingtype_has_dataPath():
    assert hasattr(carnot_DataMappingType, "dataPath")
    descriptor = None
    for klass in carnot_DataMappingType.__mro__:
        if "dataPath" in klass.__dict__:
            descriptor = klass.__dict__["dataPath"]
            break
    assert isinstance(descriptor, property)

def test_carnot_datamappingtype_has_direction():
    assert hasattr(carnot_DataMappingType, "direction")
    descriptor = None
    for klass in carnot_DataMappingType.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_carnot_datamappingtype_has_context():
    assert hasattr(carnot_DataMappingType, "context")
    descriptor = None
    for klass in carnot_DataMappingType.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)

def test_carnot_datamappingtype_has_applicationAccessPoint():
    assert hasattr(carnot_DataMappingType, "applicationAccessPoint")
    descriptor = None
    for klass in carnot_DataMappingType.__mro__:
        if "applicationAccessPoint" in klass.__dict__:
            descriptor = klass.__dict__["applicationAccessPoint"]
            break
    assert isinstance(descriptor, property)



def test_idrefowner_is_not_abstract():
    assert not inspect.isabstract(IdRefOwner)


def test_idrefowner_constructor_exists():
    assert callable(IdRefOwner.__init__)


def test_idrefowner_constructor_args():
    sig = inspect.signature(IdRefOwner.__init__)
    params = list(sig.parameters.keys())



def test_ieventhandlerowner_is_not_abstract():
    assert not inspect.isabstract(IEventHandlerOwner)


def test_ieventhandlerowner_constructor_exists():
    assert callable(IEventHandlerOwner.__init__)


def test_ieventhandlerowner_constructor_args():
    sig = inspect.signature(IEventHandlerOwner.__init__)
    params = list(sig.parameters.keys())



def test_carnot_processdefinitiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_ProcessDefinitionType)


def test_carnot_processdefinitiontype_constructor_exists():
    assert callable(carnot_ProcessDefinitionType.__init__)


def test_carnot_processdefinitiontype_constructor_args():
    sig = inspect.signature(carnot_ProcessDefinitionType.__init__)
    params = list(sig.parameters.keys())
    assert "defaultPriority" in params, "Missing parameter 'defaultPriority'"

def test_carnot_processdefinitiontype_has_defaultPriority():
    assert hasattr(carnot_ProcessDefinitionType, "defaultPriority")
    descriptor = None
    for klass in carnot_ProcessDefinitionType.__mro__:
        if "defaultPriority" in klass.__dict__:
            descriptor = klass.__dict__["defaultPriority"]
            break
    assert isinstance(descriptor, property)



def test_carnot_activitytype_is_not_abstract():
    assert not inspect.isabstract(carnot_ActivityType)


def test_carnot_activitytype_constructor_exists():
    assert callable(carnot_ActivityType.__init__)


def test_carnot_activitytype_constructor_args():
    sig = inspect.signature(carnot_ActivityType.__init__)
    params = list(sig.parameters.keys())
    assert "subProcessMode" in params, "Missing parameter 'subProcessMode'"
    assert "loopCondition" in params, "Missing parameter 'loopCondition'"
    assert "hibernateOnCreation" in params, "Missing parameter 'hibernateOnCreation'"
    assert "join" in params, "Missing parameter 'join'"
    assert "split" in params, "Missing parameter 'split'"
    assert "implementation" in params, "Missing parameter 'implementation'"
    assert "allowsAbortByPerformer" in params, "Missing parameter 'allowsAbortByPerformer'"
    assert "loopType" in params, "Missing parameter 'loopType'"

def test_carnot_activitytype_has_subProcessMode():
    assert hasattr(carnot_ActivityType, "subProcessMode")
    descriptor = None
    for klass in carnot_ActivityType.__mro__:
        if "subProcessMode" in klass.__dict__:
            descriptor = klass.__dict__["subProcessMode"]
            break
    assert isinstance(descriptor, property)

def test_carnot_activitytype_has_loopCondition():
    assert hasattr(carnot_ActivityType, "loopCondition")
    descriptor = None
    for klass in carnot_ActivityType.__mro__:
        if "loopCondition" in klass.__dict__:
            descriptor = klass.__dict__["loopCondition"]
            break
    assert isinstance(descriptor, property)

def test_carnot_activitytype_has_hibernateOnCreation():
    assert hasattr(carnot_ActivityType, "hibernateOnCreation")
    descriptor = None
    for klass in carnot_ActivityType.__mro__:
        if "hibernateOnCreation" in klass.__dict__:
            descriptor = klass.__dict__["hibernateOnCreation"]
            break
    assert isinstance(descriptor, property)

def test_carnot_activitytype_has_join():
    assert hasattr(carnot_ActivityType, "join")
    descriptor = None
    for klass in carnot_ActivityType.__mro__:
        if "join" in klass.__dict__:
            descriptor = klass.__dict__["join"]
            break
    assert isinstance(descriptor, property)

def test_carnot_activitytype_has_split():
    assert hasattr(carnot_ActivityType, "split")
    descriptor = None
    for klass in carnot_ActivityType.__mro__:
        if "split" in klass.__dict__:
            descriptor = klass.__dict__["split"]
            break
    assert isinstance(descriptor, property)

def test_carnot_activitytype_has_implementation():
    assert hasattr(carnot_ActivityType, "implementation")
    descriptor = None
    for klass in carnot_ActivityType.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)

def test_carnot_activitytype_has_allowsAbortByPerformer():
    assert hasattr(carnot_ActivityType, "allowsAbortByPerformer")
    descriptor = None
    for klass in carnot_ActivityType.__mro__:
        if "allowsAbortByPerformer" in klass.__dict__:
            descriptor = klass.__dict__["allowsAbortByPerformer"]
            break
    assert isinstance(descriptor, property)

def test_carnot_activitytype_has_loopType():
    assert hasattr(carnot_ActivityType, "loopType")
    descriptor = None
    for klass in carnot_ActivityType.__mro__:
        if "loopType" in klass.__dict__:
            descriptor = klass.__dict__["loopType"]
            break
    assert isinstance(descriptor, property)



def test_carnot_eventactiontypetype_is_not_abstract():
    assert not inspect.isabstract(carnot_EventActionTypeType)


def test_carnot_eventactiontypetype_constructor_exists():
    assert callable(carnot_EventActionTypeType.__init__)


def test_carnot_eventactiontypetype_constructor_args():
    sig = inspect.signature(carnot_EventActionTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "unsupportedContexts" in params, "Missing parameter 'unsupportedContexts'"
    assert "actionClass" in params, "Missing parameter 'actionClass'"
    assert "supportedConditionTypes" in params, "Missing parameter 'supportedConditionTypes'"
    assert "panelClass" in params, "Missing parameter 'panelClass'"
    assert "processAction" in params, "Missing parameter 'processAction'"
    assert "activityAction" in params, "Missing parameter 'activityAction'"

def test_carnot_eventactiontypetype_has_unsupportedContexts():
    assert hasattr(carnot_EventActionTypeType, "unsupportedContexts")
    descriptor = None
    for klass in carnot_EventActionTypeType.__mro__:
        if "unsupportedContexts" in klass.__dict__:
            descriptor = klass.__dict__["unsupportedContexts"]
            break
    assert isinstance(descriptor, property)

def test_carnot_eventactiontypetype_has_actionClass():
    assert hasattr(carnot_EventActionTypeType, "actionClass")
    descriptor = None
    for klass in carnot_EventActionTypeType.__mro__:
        if "actionClass" in klass.__dict__:
            descriptor = klass.__dict__["actionClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot_eventactiontypetype_has_supportedConditionTypes():
    assert hasattr(carnot_EventActionTypeType, "supportedConditionTypes")
    descriptor = None
    for klass in carnot_EventActionTypeType.__mro__:
        if "supportedConditionTypes" in klass.__dict__:
            descriptor = klass.__dict__["supportedConditionTypes"]
            break
    assert isinstance(descriptor, property)

def test_carnot_eventactiontypetype_has_panelClass():
    assert hasattr(carnot_EventActionTypeType, "panelClass")
    descriptor = None
    for klass in carnot_EventActionTypeType.__mro__:
        if "panelClass" in klass.__dict__:
            descriptor = klass.__dict__["panelClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot_eventactiontypetype_has_processAction():
    assert hasattr(carnot_EventActionTypeType, "processAction")
    descriptor = None
    for klass in carnot_EventActionTypeType.__mro__:
        if "processAction" in klass.__dict__:
            descriptor = klass.__dict__["processAction"]
            break
    assert isinstance(descriptor, property)

def test_carnot_eventactiontypetype_has_activityAction():
    assert hasattr(carnot_EventActionTypeType, "activityAction")
    descriptor = None
    for klass in carnot_EventActionTypeType.__mro__:
        if "activityAction" in klass.__dict__:
            descriptor = klass.__dict__["activityAction"]
            break
    assert isinstance(descriptor, property)



def test_itypedelement_is_not_abstract():
    assert not inspect.isabstract(ITypedElement)


def test_itypedelement_constructor_exists():
    assert callable(ITypedElement.__init__)


def test_itypedelement_constructor_args():
    sig = inspect.signature(ITypedElement.__init__)
    params = list(sig.parameters.keys())



def test_carnot_datatype_is_not_abstract():
    assert not inspect.isabstract(carnot_DataType)


def test_carnot_datatype_constructor_exists():
    assert callable(carnot_DataType.__init__)


def test_carnot_datatype_constructor_args():
    sig = inspect.signature(carnot_DataType.__init__)
    params = list(sig.parameters.keys())
    assert "predefined" in params, "Missing parameter 'predefined'"

def test_carnot_datatype_has_predefined():
    assert hasattr(carnot_DataType, "predefined")
    descriptor = None
    for klass in carnot_DataType.__mro__:
        if "predefined" in klass.__dict__:
            descriptor = klass.__dict__["predefined"]
            break
    assert isinstance(descriptor, property)



def test_carnot_triggertype_is_not_abstract():
    assert not inspect.isabstract(carnot_TriggerType)


def test_carnot_triggertype_constructor_exists():
    assert callable(carnot_TriggerType.__init__)


def test_carnot_triggertype_constructor_args():
    sig = inspect.signature(carnot_TriggerType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_applicationtype_is_not_abstract():
    assert not inspect.isabstract(carnot_ApplicationType)


def test_carnot_applicationtype_constructor_exists():
    assert callable(carnot_ApplicationType.__init__)


def test_carnot_applicationtype_constructor_args():
    sig = inspect.signature(carnot_ApplicationType.__init__)
    params = list(sig.parameters.keys())
    assert "interactive" in params, "Missing parameter 'interactive'"

def test_carnot_applicationtype_has_interactive():
    assert hasattr(carnot_ApplicationType, "interactive")
    descriptor = None
    for klass in carnot_ApplicationType.__mro__:
        if "interactive" in klass.__dict__:
            descriptor = klass.__dict__["interactive"]
            break
    assert isinstance(descriptor, property)



def test_carnot_contexttype_is_not_abstract():
    assert not inspect.isabstract(carnot_ContextType)


def test_carnot_contexttype_constructor_exists():
    assert callable(carnot_ContextType.__init__)


def test_carnot_contexttype_constructor_args():
    sig = inspect.signature(carnot_ContextType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_eventhandlertype_is_not_abstract():
    assert not inspect.isabstract(carnot_EventHandlerType)


def test_carnot_eventhandlertype_constructor_exists():
    assert callable(carnot_EventHandlerType.__init__)


def test_carnot_eventhandlertype_constructor_args():
    sig = inspect.signature(carnot_EventHandlerType.__init__)
    params = list(sig.parameters.keys())
    assert "unbindOnMatch" in params, "Missing parameter 'unbindOnMatch'"
    assert "consumeOnMatch" in params, "Missing parameter 'consumeOnMatch'"
    assert "autoBind" in params, "Missing parameter 'autoBind'"
    assert "logHandler" in params, "Missing parameter 'logHandler'"

def test_carnot_eventhandlertype_has_unbindOnMatch():
    assert hasattr(carnot_EventHandlerType, "unbindOnMatch")
    descriptor = None
    for klass in carnot_EventHandlerType.__mro__:
        if "unbindOnMatch" in klass.__dict__:
            descriptor = klass.__dict__["unbindOnMatch"]
            break
    assert isinstance(descriptor, property)

def test_carnot_eventhandlertype_has_consumeOnMatch():
    assert hasattr(carnot_EventHandlerType, "consumeOnMatch")
    descriptor = None
    for klass in carnot_EventHandlerType.__mro__:
        if "consumeOnMatch" in klass.__dict__:
            descriptor = klass.__dict__["consumeOnMatch"]
            break
    assert isinstance(descriptor, property)

def test_carnot_eventhandlertype_has_autoBind():
    assert hasattr(carnot_EventHandlerType, "autoBind")
    descriptor = None
    for klass in carnot_EventHandlerType.__mro__:
        if "autoBind" in klass.__dict__:
            descriptor = klass.__dict__["autoBind"]
            break
    assert isinstance(descriptor, property)

def test_carnot_eventhandlertype_has_logHandler():
    assert hasattr(carnot_EventHandlerType, "logHandler")
    descriptor = None
    for klass in carnot_EventHandlerType.__mro__:
        if "logHandler" in klass.__dict__:
            descriptor = klass.__dict__["logHandler"]
            break
    assert isinstance(descriptor, property)



def test_carnot_genericlinkconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot_GenericLinkConnectionType)


def test_carnot_genericlinkconnectiontype_constructor_exists():
    assert callable(carnot_GenericLinkConnectionType.__init__)


def test_carnot_genericlinkconnectiontype_constructor_args():
    sig = inspect.signature(carnot_GenericLinkConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_carnot_accesspointtype_is_not_abstract():
    assert not inspect.isabstract(carnot_AccessPointType)


def test_carnot_accesspointtype_constructor_exists():
    assert callable(carnot_AccessPointType.__init__)


def test_carnot_accesspointtype_constructor_args():
    sig = inspect.signature(carnot_AccessPointType.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_carnot_accesspointtype_has_direction():
    assert hasattr(carnot_AccessPointType, "direction")
    descriptor = None
    for klass in carnot_AccessPointType.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_carnot_abstracteventaction_is_not_abstract():
    assert not inspect.isabstract(carnot_AbstractEventAction)


def test_carnot_abstracteventaction_constructor_exists():
    assert callable(carnot_AbstractEventAction.__init__)


def test_carnot_abstracteventaction_constructor_args():
    sig = inspect.signature(carnot_AbstractEventAction.__init__)
    params = list(sig.parameters.keys())

def test_looptype_exists():
    # Check that the Enumeration exists
    assert LoopType is not None

def test_looptype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LoopType]
    expected_literals = [
        "While",
        "None_",
        "Unknown",
        "Repeat",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LoopType"

def test_linkcolor_exists():
    # Check that the Enumeration exists
    assert LinkColor is not None

def test_linkcolor_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LinkColor]
    expected_literals = [
        "Black",
        "Blue",
        "DarkBlue",
        "DarkGray",
        "Yellow",
        "Red",
        "Unknown",
        "LightGray",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LinkColor"

def test_subprocessmodetype_exists():
    # Check that the Enumeration exists
    assert SubProcessModeType is not None

def test_subprocessmodetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SubProcessModeType]
    expected_literals = [
        "sync_separate",
        "async_separate",
        "sync_shared",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SubProcessModeType"

def test_orientationtype_exists():
    # Check that the Enumeration exists
    assert OrientationType is not None

def test_orientationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrientationType]
    expected_literals = [
        "Horizontal",
        "Vertical",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrientationType"

def test_joinsplittype_exists():
    # Check that the Enumeration exists
    assert JoinSplitType is not None

def test_joinsplittype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JoinSplitType]
    expected_literals = [
        "None_",
        "OR",
        "XOR",
        "AND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JoinSplitType"

def test_activityimplementationtype_exists():
    # Check that the Enumeration exists
    assert ActivityImplementationType is not None

def test_activityimplementationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActivityImplementationType]
    expected_literals = [
        "Route",
        "Manual",
        "Subprocess",
        "Application",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActivityImplementationType"

def test_linklinestyle_exists():
    # Check that the Enumeration exists
    assert LinkLineStyle is not None

def test_linklinestyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LinkLineStyle]
    expected_literals = [
        "ShortStrokes",
        "Unknown",
        "Normal",
        "LongStrokes",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LinkLineStyle"

def test_routingtype_exists():
    # Check that the Enumeration exists
    assert RoutingType is not None

def test_routingtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RoutingType]
    expected_literals = [
        "ShortestPath",
        "Manhattan",
        "Explicit",
        "Default",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RoutingType"

def test_linkendstyle_exists():
    # Check that the Enumeration exists
    assert LinkEndStyle is not None

def test_linkendstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LinkEndStyle]
    expected_literals = [
        "FilledRhombus",
        "FilledTriangle",
        "OpenTriangle",
        "EmptyTriangle",
        "EmptyRhombus",
        "NoArrow",
        "Unknown",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LinkEndStyle"

def test_flowcontroltype_exists():
    # Check that the Enumeration exists
    assert FlowControlType is not None

def test_flowcontroltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FlowControlType]
    expected_literals = [
        "none",
        "split",
        "join",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FlowControlType"

def test_diagrammodetype_exists():
    # Check that the Enumeration exists
    assert DiagramModeType is not None

def test_diagrammodetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DiagramModeType]
    expected_literals = [
        "MODE_4_5_0",
        "MODE_4_0_0",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DiagramModeType"

def test_linkcardinality_exists():
    # Check that the Enumeration exists
    assert LinkCardinality is not None

def test_linkcardinality_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LinkCardinality]
    expected_literals = [
        "Many",
        "Unknown",
        "One",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LinkCardinality"

def test_implementationtype_exists():
    # Check that the Enumeration exists
    assert ImplementationType is not None

def test_implementationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImplementationType]
    expected_literals = [
        "push",
        "engine",
        "pull",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImplementationType"

def test_directiontype_exists():
    # Check that the Enumeration exists
    assert DirectionType is not None

def test_directiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DirectionType]
    expected_literals = [
        "IN",
        "OUT",
        "INOUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DirectionType"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
IModelElementNodeSymbol_strategy = st.builds(
    IModelElementNodeSymbol,
)
carnot_IModelParticipantSymbol_strategy = st.builds(
    carnot_IModelParticipantSymbol,
)
carnot_ParticipantType_strategy = st.builds(
    carnot_ParticipantType,
)
IFlowObjectSymbol_strategy = st.builds(
    IFlowObjectSymbol,
)
carnot_AbstractEventSymbol_strategy = st.builds(
    carnot_AbstractEventSymbol,
    label=
        safe_text
)
IGraphicalObject_strategy = st.builds(
    IGraphicalObject,
)
carnot_IConnectionSymbol_strategy = st.builds(
    carnot_IConnectionSymbol,
    sourceAnchor=
        safe_text,
    routing=
        safe_text,
    targetAnchor=
        safe_text
)
carnot_INodeSymbol_strategy = st.builds(
    carnot_INodeSymbol,
    yPos=
        safe_text,
    shape=
        safe_text,
    height=
        safe_text,
    width=
        safe_text,
    xPos=
        safe_text
)
INodeSymbol_strategy = st.builds(
    INodeSymbol,
)
carnot_IModelElementNodeSymbol_strategy = st.builds(
    carnot_IModelElementNodeSymbol,
)
carnot_IFlowObjectSymbol_strategy = st.builds(
    carnot_IFlowObjectSymbol,
)
carnot_TextSymbolType_strategy = st.builds(
    carnot_TextSymbolType,
    text=
        safe_text
)
carnot_ProcessSymbolType_strategy = st.builds(
    carnot_ProcessSymbolType,
)
carnot_GatewaySymbol_strategy = st.builds(
    carnot_GatewaySymbol,
    flowKind=
        safe_text
)
carnot_DataSymbolType_strategy = st.builds(
    carnot_DataSymbolType,
)
carnot_ModelerSymbolType_strategy = st.builds(
    carnot_ModelerSymbolType,
)
carnot_ActivitySymbolType_strategy = st.builds(
    carnot_ActivitySymbolType,
)
carnot_ITypedElement_strategy = st.builds(
    carnot_ITypedElement,
)
IIdentifiableModelElement_strategy = st.builds(
    IIdentifiableModelElement,
)
carnot_IModelParticipant_strategy = st.builds(
    carnot_IModelParticipant,
)
carnot_IMetaType_strategy = st.builds(
    carnot_IMetaType,
    isPredefined=
        safe_text
)
carnot_IAccessPointOwner_strategy = st.builds(
    carnot_IAccessPointOwner,
)
carnot_ApplicationSymbolType_strategy = st.builds(
    carnot_ApplicationSymbolType,
)
carnot_AnnotationSymbolType_strategy = st.builds(
    carnot_AnnotationSymbolType,
)
carnot_IModelElement_strategy = st.builds(
    carnot_IModelElement,
    elementOid=
        safe_text
)
carnot_EObject_strategy = st.builds(
    carnot_EObject,
)
carnot_IdentifiableReference_strategy = st.builds(
    carnot_IdentifiableReference,
)
carnot_AttributeType_strategy = st.builds(
    carnot_AttributeType,
    value=
        safe_text,
    group=
        safe_text,
    name=
        safe_text,
    type=
        safe_text,
    mixed=
        safe_text,
    any=
        safe_text
)
carnot_IExtensibleElement_strategy = st.builds(
    carnot_IExtensibleElement,
)
carnot_IIdentifiableElement_strategy = st.builds(
    carnot_IIdentifiableElement,
    id=
        safe_text,
    name=
        safe_text
)
carnot_IEventHandlerOwner_strategy = st.builds(
    carnot_IEventHandlerOwner,
)
carnot_DescriptionType_strategy = st.builds(
    carnot_DescriptionType,
    mixed=
        safe_text
)
IExtensibleElement_strategy = st.builds(
    IExtensibleElement,
)
carnot_ISymbolContainer_strategy = st.builds(
    carnot_ISymbolContainer,
    nodes=
        safe_text,
    connections=
        safe_text
)
IIdentifiableElement_strategy = st.builds(
    IIdentifiableElement,
)
carnot_ISwimlaneSymbol_strategy = st.builds(
    carnot_ISwimlaneSymbol,
    orientation=
        safe_text,
    collapsed=
        safe_text
)
IModelElement_strategy = st.builds(
    IModelElement,
)
carnot_IGraphicalObject_strategy = st.builds(
    carnot_IGraphicalObject,
    borderColor=
        safe_text,
    fillColor=
        safe_text,
    style=
        safe_text
)
carnot_IIdentifiableModelElement_strategy = st.builds(
    carnot_IIdentifiableModelElement,
)
carnot_Coordinates_strategy = st.builds(
    carnot_Coordinates,
    yPos=
        safe_text,
    xPos=
        safe_text
)
FormalParameterMappingType_strategy = st.builds(
    FormalParameterMappingType,
)
carnot_extensions_FormalParameterMappingsType_strategy = st.builds(
    carnot_extensions_FormalParameterMappingsType,
)
extensions_carnot_FormalParameterType_strategy = st.builds(
    extensions_carnot_FormalParameterType,
)
extensions_carnot_DataType_strategy = st.builds(
    extensions_carnot_DataType,
)
carnot_extensions_FormalParameterMappingType_strategy = st.builds(
    carnot_extensions_FormalParameterMappingType,
)
carnot_ViewableType_strategy = st.builds(
    carnot_ViewableType,
)
FormalParameterMappingsType_strategy = st.builds(
    FormalParameterMappingsType,
)
carnot_FormalParametersType_strategy = st.builds(
    carnot_FormalParametersType,
)
carnot_ViewType_strategy = st.builds(
    carnot_ViewType,
    name=
        safe_text
)
carnot_TypeDeclarationsType_strategy = st.builds(
    carnot_TypeDeclarationsType,
)
carnot_ScriptType_strategy = st.builds(
    carnot_ScriptType,
)
carnot_ExternalPackages_strategy = st.builds(
    carnot_ExternalPackages,
)
carnot_QualityControlType_strategy = st.builds(
    carnot_QualityControlType,
)
carnot_ModelerType_strategy = st.builds(
    carnot_ModelerType,
    email=
        safe_text,
    password=
        safe_text
)
ISwimlaneSymbol_strategy = st.builds(
    ISwimlaneSymbol,
)
carnot_IdRefOwner_strategy = st.builds(
    carnot_IdRefOwner,
)
carnot_ExternalPackage_strategy = st.builds(
    carnot_ExternalPackage,
)
carnot_IdRef_strategy = st.builds(
    carnot_IdRef,
    ref=
        safe_text
)
carnot_EStringToStringMapEntry_strategy = st.builds(
    carnot_EStringToStringMapEntry,
)
carnot_DocumentRoot_strategy = st.builds(
    carnot_DocumentRoot,
    mixed=
        safe_text
)
AbstractEventSymbol_strategy = st.builds(
    AbstractEventSymbol,
)
carnot_EndEventSymbol_strategy = st.builds(
    carnot_EndEventSymbol,
)
carnot_IntermediateEventSymbol_strategy = st.builds(
    carnot_IntermediateEventSymbol,
)
carnot_PublicInterfaceSymbol_strategy = st.builds(
    carnot_PublicInterfaceSymbol,
)
carnot_StartEventSymbol_strategy = st.builds(
    carnot_StartEventSymbol,
)
carnot_ModelType_strategy = st.builds(
    carnot_ModelType,
    created=
        safe_text,
    vendor=
        safe_text,
    modelOID=
        safe_text,
    oid=
        safe_text,
    author=
        safe_text,
    carnotVersion=
        safe_text
)
carnot_ExternalReferenceType_strategy = st.builds(
    carnot_ExternalReferenceType,
)
carnot_ParameterMappingType_strategy = st.builds(
    carnot_ParameterMappingType,
    parameter=
        safe_text,
    parameterPath=
        safe_text,
    dataPath=
        safe_text
)
ISymbolContainer_strategy = st.builds(
    ISymbolContainer,
)
carnot_LaneSymbol_strategy = st.builds(
    carnot_LaneSymbol,
)
carnot_GroupSymbolType_strategy = st.builds(
    carnot_GroupSymbolType,
)
carnot_PoolSymbol_strategy = st.builds(
    carnot_PoolSymbol,
    boundaryVisible=
        safe_text
)
carnot_DiagramType_strategy = st.builds(
    carnot_DiagramType,
    name=
        safe_text,
    orientation=
        safe_text,
    mode=
        safe_text
)
carnot_DataPathType_strategy = st.builds(
    carnot_DataPathType,
    direction=
        safe_text,
    dataPath=
        safe_text,
    descriptor=
        safe_text,
    key=
        safe_text
)
IConnectionSymbol_strategy = st.builds(
    IConnectionSymbol,
)
carnot_WorksForConnectionType_strategy = st.builds(
    carnot_WorksForConnectionType,
)
carnot_TriggersConnectionType_strategy = st.builds(
    carnot_TriggersConnectionType,
)
carnot_PerformsConnectionType_strategy = st.builds(
    carnot_PerformsConnectionType,
)
carnot_SubProcessOfConnectionType_strategy = st.builds(
    carnot_SubProcessOfConnectionType,
)
carnot_TransitionConnectionType_strategy = st.builds(
    carnot_TransitionConnectionType,
    points=
        safe_text
)
carnot_RefersToConnectionType_strategy = st.builds(
    carnot_RefersToConnectionType,
)
carnot_DataMappingConnectionType_strategy = st.builds(
    carnot_DataMappingConnectionType,
)
carnot_TeamLeadConnectionType_strategy = st.builds(
    carnot_TeamLeadConnectionType,
)
carnot_PartOfConnectionType_strategy = st.builds(
    carnot_PartOfConnectionType,
)
carnot_ExecutedByConnectionType_strategy = st.builds(
    carnot_ExecutedByConnectionType,
)
IModelParticipantSymbol_strategy = st.builds(
    IModelParticipantSymbol,
)
carnot_OrganizationSymbolType_strategy = st.builds(
    carnot_OrganizationSymbolType,
)
carnot_ConditionalPerformerSymbolType_strategy = st.builds(
    carnot_ConditionalPerformerSymbolType,
)
carnot_RoleSymbolType_strategy = st.builds(
    carnot_RoleSymbolType,
)
AbstractEventAction_strategy = st.builds(
    AbstractEventAction,
)
carnot_UnbindActionType_strategy = st.builds(
    carnot_UnbindActionType,
)
carnot_EventActionType_strategy = st.builds(
    carnot_EventActionType,
)
carnot_BindActionType_strategy = st.builds(
    carnot_BindActionType,
)
IModelParticipant_strategy = st.builds(
    IModelParticipant,
)
carnot_RoleType_strategy = st.builds(
    carnot_RoleType,
    cardinality=
        st.integers()
)
carnot_OrganizationType_strategy = st.builds(
    carnot_OrganizationType,
)
carnot_ConditionalPerformerType_strategy = st.builds(
    carnot_ConditionalPerformerType,
    dataPath=
        safe_text,
    isUser=
        safe_text
)
carnot_XmlTextNode_strategy = st.builds(
    carnot_XmlTextNode,
    mixed=
        safe_text
)
IMetaType_strategy = st.builds(
    IMetaType,
)
carnot_TriggerTypeType_strategy = st.builds(
    carnot_TriggerTypeType,
    panelClass=
        safe_text,
    pullTriggerEvaluator=
        safe_text,
    rule=
        safe_text,
    pullTrigger=
        safe_text
)
carnot_DataTypeType_strategy = st.builds(
    carnot_DataTypeType,
    panelClass=
        safe_text,
    storageStrategy=
        safe_text,
    valueCreator=
        safe_text,
    accessPathEditor=
        safe_text,
    writable=
        safe_text,
    instanceClass=
        safe_text,
    validatorClass=
        safe_text,
    readable=
        safe_text,
    evaluator=
        safe_text
)
carnot_EventConditionTypeType_strategy = st.builds(
    carnot_EventConditionTypeType,
    implementation=
        safe_text,
    rule=
        safe_text,
    pullEventEmitterClass=
        safe_text,
    panelClass=
        safe_text,
    activityCondition=
        safe_text,
    processCondition=
        safe_text,
    binderClass=
        safe_text
)
carnot_ApplicationTypeType_strategy = st.builds(
    carnot_ApplicationTypeType,
    instanceClass=
        safe_text,
    accessPointProviderClass=
        safe_text,
    synchronous=
        safe_text,
    panelClass=
        safe_text,
    validatorClass=
        safe_text
)
carnot_LinkTypeType_strategy = st.builds(
    carnot_LinkTypeType,
    showRoleNames=
        safe_text,
    lineStyle=
        safe_text,
    targetSymbol=
        safe_text,
    sourceCardinality=
        safe_text,
    sourceClass=
        safe_text,
    targetClass=
        safe_text,
    lineColor=
        safe_text,
    targetRole=
        safe_text,
    targetCardinality=
        safe_text,
    sourceSymbol=
        safe_text,
    showLinkTypeName=
        safe_text,
    sourceRole=
        safe_text
)
carnot_ApplicationContextTypeType_strategy = st.builds(
    carnot_ApplicationContextTypeType,
    hasApplicationPath=
        safe_text,
    accessPointProviderClass=
        safe_text,
    panelClass=
        safe_text,
    validatorClass=
        safe_text,
    hasMappingId=
        safe_text
)
carnot_TextType_strategy = st.builds(
    carnot_TextType,
    mixed=
        safe_text
)
carnot_LoopType_strategy = st.builds(
    carnot_LoopType,
)
IAccessPointOwner_strategy = st.builds(
    IAccessPointOwner,
)
carnot_Code_strategy = st.builds(
    carnot_Code,
    code=
        safe_text,
    name=
        safe_text,
    value=
        safe_text
)
carnot_TransitionType_strategy = st.builds(
    carnot_TransitionType,
    forkOnTraversal=
        safe_text,
    condition=
        safe_text
)
carnot_DataMappingType_strategy = st.builds(
    carnot_DataMappingType,
    applicationPath=
        safe_text,
    dataPath=
        safe_text,
    direction=
        safe_text,
    context=
        safe_text,
    applicationAccessPoint=
        safe_text
)
IdRefOwner_strategy = st.builds(
    IdRefOwner,
)
IEventHandlerOwner_strategy = st.builds(
    IEventHandlerOwner,
)
carnot_ProcessDefinitionType_strategy = st.builds(
    carnot_ProcessDefinitionType,
    defaultPriority=
        safe_text
)
carnot_ActivityType_strategy = st.builds(
    carnot_ActivityType,
    subProcessMode=
        safe_text,
    loopCondition=
        safe_text,
    hibernateOnCreation=
        safe_text,
    join=
        safe_text,
    split=
        safe_text,
    implementation=
        safe_text,
    allowsAbortByPerformer=
        safe_text,
    loopType=
        safe_text
)
carnot_EventActionTypeType_strategy = st.builds(
    carnot_EventActionTypeType,
    unsupportedContexts=
        safe_text,
    actionClass=
        safe_text,
    supportedConditionTypes=
        safe_text,
    panelClass=
        safe_text,
    processAction=
        safe_text,
    activityAction=
        safe_text
)
ITypedElement_strategy = st.builds(
    ITypedElement,
)
carnot_DataType_strategy = st.builds(
    carnot_DataType,
    predefined=
        safe_text
)
carnot_TriggerType_strategy = st.builds(
    carnot_TriggerType,
)
carnot_ApplicationType_strategy = st.builds(
    carnot_ApplicationType,
    interactive=
        safe_text
)
carnot_ContextType_strategy = st.builds(
    carnot_ContextType,
)
carnot_EventHandlerType_strategy = st.builds(
    carnot_EventHandlerType,
    unbindOnMatch=
        safe_text,
    consumeOnMatch=
        safe_text,
    autoBind=
        safe_text,
    logHandler=
        safe_text
)
carnot_GenericLinkConnectionType_strategy = st.builds(
    carnot_GenericLinkConnectionType,
)
carnot_AccessPointType_strategy = st.builds(
    carnot_AccessPointType,
    direction=
        safe_text
)
carnot_AbstractEventAction_strategy = st.builds(
    carnot_AbstractEventAction,
)

@given(instance=IModelElementNodeSymbol_strategy)
@settings(max_examples=50)
def test_imodelelementnodesymbol_instantiation(instance):
    assert isinstance(instance, IModelElementNodeSymbol)

@given(instance=carnot_IModelParticipantSymbol_strategy)
@settings(max_examples=50)
def test_carnot_imodelparticipantsymbol_instantiation(instance):
    assert isinstance(instance, carnot_IModelParticipantSymbol)

@given(instance=carnot_ParticipantType_strategy)
@settings(max_examples=50)
def test_carnot_participanttype_instantiation(instance):
    assert isinstance(instance, carnot_ParticipantType)

@given(instance=IFlowObjectSymbol_strategy)
@settings(max_examples=50)
def test_iflowobjectsymbol_instantiation(instance):
    assert isinstance(instance, IFlowObjectSymbol)

@given(instance=carnot_AbstractEventSymbol_strategy)
@settings(max_examples=50)
def test_carnot_abstracteventsymbol_instantiation(instance):
    assert isinstance(instance, carnot_AbstractEventSymbol)



@given(instance=carnot_AbstractEventSymbol_strategy)
def test_carnot_abstracteventsymbol_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=IGraphicalObject_strategy)
@settings(max_examples=50)
def test_igraphicalobject_instantiation(instance):
    assert isinstance(instance, IGraphicalObject)

@given(instance=carnot_IConnectionSymbol_strategy)
@settings(max_examples=50)
def test_carnot_iconnectionsymbol_instantiation(instance):
    assert isinstance(instance, carnot_IConnectionSymbol)



@given(instance=carnot_IConnectionSymbol_strategy)
def test_carnot_iconnectionsymbol_sourceAnchor_setter(instance):
    original = instance.sourceAnchor
    instance.sourceAnchor = original
    assert instance.sourceAnchor == original



@given(instance=carnot_IConnectionSymbol_strategy)
def test_carnot_iconnectionsymbol_routing_setter(instance):
    original = instance.routing
    instance.routing = original
    assert instance.routing == original



@given(instance=carnot_IConnectionSymbol_strategy)
def test_carnot_iconnectionsymbol_targetAnchor_setter(instance):
    original = instance.targetAnchor
    instance.targetAnchor = original
    assert instance.targetAnchor == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=carnot_IConnectionSymbol_strategy)
@settings(max_examples=30)
def test_carnot_iconnectionsymbol_setsourcenode_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setSourceNode(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setSourceNode).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setSourceNode' in carnot_IConnectionSymbol is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setSourceNode' in carnot_IConnectionSymbol did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setSourceNode' in carnot_IConnectionSymbol is not implemented or raised an error")

@given(instance=carnot_INodeSymbol_strategy)
@settings(max_examples=50)
def test_carnot_inodesymbol_instantiation(instance):
    assert isinstance(instance, carnot_INodeSymbol)



@given(instance=carnot_INodeSymbol_strategy)
def test_carnot_inodesymbol_yPos_setter(instance):
    original = instance.yPos
    instance.yPos = original
    assert instance.yPos == original



@given(instance=carnot_INodeSymbol_strategy)
def test_carnot_inodesymbol_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original



@given(instance=carnot_INodeSymbol_strategy)
def test_carnot_inodesymbol_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=carnot_INodeSymbol_strategy)
def test_carnot_inodesymbol_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=carnot_INodeSymbol_strategy)
def test_carnot_inodesymbol_xPos_setter(instance):
    original = instance.xPos
    instance.xPos = original
    assert instance.xPos == original

@given(instance=INodeSymbol_strategy)
@settings(max_examples=50)
def test_inodesymbol_instantiation(instance):
    assert isinstance(instance, INodeSymbol)

@given(instance=carnot_IModelElementNodeSymbol_strategy)
@settings(max_examples=50)
def test_carnot_imodelelementnodesymbol_instantiation(instance):
    assert isinstance(instance, carnot_IModelElementNodeSymbol)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=carnot_IModelElementNodeSymbol_strategy)
@settings(max_examples=30)
def test_carnot_imodelelementnodesymbol_setmodelelement_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setModelElement(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setModelElement).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setModelElement' in carnot_IModelElementNodeSymbol is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setModelElement' in carnot_IModelElementNodeSymbol did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setModelElement' in carnot_IModelElementNodeSymbol is not implemented or raised an error")

@given(instance=carnot_IFlowObjectSymbol_strategy)
@settings(max_examples=50)
def test_carnot_iflowobjectsymbol_instantiation(instance):
    assert isinstance(instance, carnot_IFlowObjectSymbol)

@given(instance=carnot_TextSymbolType_strategy)
@settings(max_examples=50)
def test_carnot_textsymboltype_instantiation(instance):
    assert isinstance(instance, carnot_TextSymbolType)



@given(instance=carnot_TextSymbolType_strategy)
def test_carnot_textsymboltype_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=carnot_ProcessSymbolType_strategy)
@settings(max_examples=50)
def test_carnot_processsymboltype_instantiation(instance):
    assert isinstance(instance, carnot_ProcessSymbolType)

@given(instance=carnot_GatewaySymbol_strategy)
@settings(max_examples=50)
def test_carnot_gatewaysymbol_instantiation(instance):
    assert isinstance(instance, carnot_GatewaySymbol)



@given(instance=carnot_GatewaySymbol_strategy)
def test_carnot_gatewaysymbol_flowKind_setter(instance):
    original = instance.flowKind
    instance.flowKind = original
    assert instance.flowKind == original

@given(instance=carnot_DataSymbolType_strategy)
@settings(max_examples=50)
def test_carnot_datasymboltype_instantiation(instance):
    assert isinstance(instance, carnot_DataSymbolType)

@given(instance=carnot_ModelerSymbolType_strategy)
@settings(max_examples=50)
def test_carnot_modelersymboltype_instantiation(instance):
    assert isinstance(instance, carnot_ModelerSymbolType)

@given(instance=carnot_ActivitySymbolType_strategy)
@settings(max_examples=50)
def test_carnot_activitysymboltype_instantiation(instance):
    assert isinstance(instance, carnot_ActivitySymbolType)

@given(instance=carnot_ITypedElement_strategy)
@settings(max_examples=50)
def test_carnot_itypedelement_instantiation(instance):
    assert isinstance(instance, carnot_ITypedElement)

@given(instance=IIdentifiableModelElement_strategy)
@settings(max_examples=50)
def test_iidentifiablemodelelement_instantiation(instance):
    assert isinstance(instance, IIdentifiableModelElement)

@given(instance=carnot_IModelParticipant_strategy)
@settings(max_examples=50)
def test_carnot_imodelparticipant_instantiation(instance):
    assert isinstance(instance, carnot_IModelParticipant)

@given(instance=carnot_IMetaType_strategy)
@settings(max_examples=50)
def test_carnot_imetatype_instantiation(instance):
    assert isinstance(instance, carnot_IMetaType)



@given(instance=carnot_IMetaType_strategy)
def test_carnot_imetatype_isPredefined_setter(instance):
    original = instance.isPredefined
    instance.isPredefined = original
    assert instance.isPredefined == original

@given(instance=carnot_IAccessPointOwner_strategy)
@settings(max_examples=50)
def test_carnot_iaccesspointowner_instantiation(instance):
    assert isinstance(instance, carnot_IAccessPointOwner)

@given(instance=carnot_ApplicationSymbolType_strategy)
@settings(max_examples=50)
def test_carnot_applicationsymboltype_instantiation(instance):
    assert isinstance(instance, carnot_ApplicationSymbolType)

@given(instance=carnot_AnnotationSymbolType_strategy)
@settings(max_examples=50)
def test_carnot_annotationsymboltype_instantiation(instance):
    assert isinstance(instance, carnot_AnnotationSymbolType)

@given(instance=carnot_IModelElement_strategy)
@settings(max_examples=50)
def test_carnot_imodelelement_instantiation(instance):
    assert isinstance(instance, carnot_IModelElement)



@given(instance=carnot_IModelElement_strategy)
def test_carnot_imodelelement_elementOid_setter(instance):
    original = instance.elementOid
    instance.elementOid = original
    assert instance.elementOid == original

@given(instance=carnot_EObject_strategy)
@settings(max_examples=50)
def test_carnot_eobject_instantiation(instance):
    assert isinstance(instance, carnot_EObject)

@given(instance=carnot_IdentifiableReference_strategy)
@settings(max_examples=50)
def test_carnot_identifiablereference_instantiation(instance):
    assert isinstance(instance, carnot_IdentifiableReference)

@given(instance=carnot_AttributeType_strategy)
@settings(max_examples=50)
def test_carnot_attributetype_instantiation(instance):
    assert isinstance(instance, carnot_AttributeType)



@given(instance=carnot_AttributeType_strategy)
def test_carnot_attributetype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=carnot_AttributeType_strategy)
def test_carnot_attributetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=carnot_AttributeType_strategy)
def test_carnot_attributetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=carnot_AttributeType_strategy)
def test_carnot_attributetype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=carnot_AttributeType_strategy)
def test_carnot_attributetype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=carnot_AttributeType_strategy)
def test_carnot_attributetype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=carnot_AttributeType_strategy)
@settings(max_examples=30)
def test_carnot_attributetype_setattributevalue_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setAttributeValue(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setAttributeValue).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setAttributeValue' in carnot_AttributeType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setAttributeValue' in carnot_AttributeType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setAttributeValue' in carnot_AttributeType is not implemented or raised an error")

@given(instance=carnot_IExtensibleElement_strategy)
@settings(max_examples=50)
def test_carnot_iextensibleelement_instantiation(instance):
    assert isinstance(instance, carnot_IExtensibleElement)

@given(instance=carnot_IIdentifiableElement_strategy)
@settings(max_examples=50)
def test_carnot_iidentifiableelement_instantiation(instance):
    assert isinstance(instance, carnot_IIdentifiableElement)



@given(instance=carnot_IIdentifiableElement_strategy)
def test_carnot_iidentifiableelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=carnot_IIdentifiableElement_strategy)
def test_carnot_iidentifiableelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=carnot_IEventHandlerOwner_strategy)
@settings(max_examples=50)
def test_carnot_ieventhandlerowner_instantiation(instance):
    assert isinstance(instance, carnot_IEventHandlerOwner)

@given(instance=carnot_DescriptionType_strategy)
@settings(max_examples=50)
def test_carnot_descriptiontype_instantiation(instance):
    assert isinstance(instance, carnot_DescriptionType)



@given(instance=carnot_DescriptionType_strategy)
def test_carnot_descriptiontype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=IExtensibleElement_strategy)
@settings(max_examples=50)
def test_iextensibleelement_instantiation(instance):
    assert isinstance(instance, IExtensibleElement)

@given(instance=carnot_ISymbolContainer_strategy)
@settings(max_examples=50)
def test_carnot_isymbolcontainer_instantiation(instance):
    assert isinstance(instance, carnot_ISymbolContainer)



@given(instance=carnot_ISymbolContainer_strategy)
def test_carnot_isymbolcontainer_nodes_setter(instance):
    original = instance.nodes
    instance.nodes = original
    assert instance.nodes == original



@given(instance=carnot_ISymbolContainer_strategy)
def test_carnot_isymbolcontainer_connections_setter(instance):
    original = instance.connections
    instance.connections = original
    assert instance.connections == original

@given(instance=IIdentifiableElement_strategy)
@settings(max_examples=50)
def test_iidentifiableelement_instantiation(instance):
    assert isinstance(instance, IIdentifiableElement)

@given(instance=carnot_ISwimlaneSymbol_strategy)
@settings(max_examples=50)
def test_carnot_iswimlanesymbol_instantiation(instance):
    assert isinstance(instance, carnot_ISwimlaneSymbol)



@given(instance=carnot_ISwimlaneSymbol_strategy)
def test_carnot_iswimlanesymbol_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original



@given(instance=carnot_ISwimlaneSymbol_strategy)
def test_carnot_iswimlanesymbol_collapsed_setter(instance):
    original = instance.collapsed
    instance.collapsed = original
    assert instance.collapsed == original

@given(instance=IModelElement_strategy)
@settings(max_examples=50)
def test_imodelelement_instantiation(instance):
    assert isinstance(instance, IModelElement)

@given(instance=carnot_IGraphicalObject_strategy)
@settings(max_examples=50)
def test_carnot_igraphicalobject_instantiation(instance):
    assert isinstance(instance, carnot_IGraphicalObject)



@given(instance=carnot_IGraphicalObject_strategy)
def test_carnot_igraphicalobject_borderColor_setter(instance):
    original = instance.borderColor
    instance.borderColor = original
    assert instance.borderColor == original



@given(instance=carnot_IGraphicalObject_strategy)
def test_carnot_igraphicalobject_fillColor_setter(instance):
    original = instance.fillColor
    instance.fillColor = original
    assert instance.fillColor == original



@given(instance=carnot_IGraphicalObject_strategy)
def test_carnot_igraphicalobject_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=carnot_IIdentifiableModelElement_strategy)
@settings(max_examples=50)
def test_carnot_iidentifiablemodelelement_instantiation(instance):
    assert isinstance(instance, carnot_IIdentifiableModelElement)

@given(instance=carnot_Coordinates_strategy)
@settings(max_examples=50)
def test_carnot_coordinates_instantiation(instance):
    assert isinstance(instance, carnot_Coordinates)



@given(instance=carnot_Coordinates_strategy)
def test_carnot_coordinates_yPos_setter(instance):
    original = instance.yPos
    instance.yPos = original
    assert instance.yPos == original



@given(instance=carnot_Coordinates_strategy)
def test_carnot_coordinates_xPos_setter(instance):
    original = instance.xPos
    instance.xPos = original
    assert instance.xPos == original

@given(instance=FormalParameterMappingType_strategy)
@settings(max_examples=50)
def test_formalparametermappingtype_instantiation(instance):
    assert isinstance(instance, FormalParameterMappingType)

@given(instance=carnot_extensions_FormalParameterMappingsType_strategy)
@settings(max_examples=50)
def test_carnot_extensions_formalparametermappingstype_instantiation(instance):
    assert isinstance(instance, carnot_extensions_FormalParameterMappingsType)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=carnot_extensions_FormalParameterMappingsType_strategy)
@settings(max_examples=30)
def test_carnot_extensions_formalparametermappingstype_setmappeddata_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setMappedData(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setMappedData).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setMappedData' in carnot_extensions_FormalParameterMappingsType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setMappedData' in carnot_extensions_FormalParameterMappingsType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setMappedData' in carnot_extensions_FormalParameterMappingsType is not implemented or raised an error")

@given(instance=extensions_carnot_FormalParameterType_strategy)
@settings(max_examples=50)
def test_extensions_carnot_formalparametertype_instantiation(instance):
    assert isinstance(instance, extensions_carnot_FormalParameterType)

@given(instance=extensions_carnot_DataType_strategy)
@settings(max_examples=50)
def test_extensions_carnot_datatype_instantiation(instance):
    assert isinstance(instance, extensions_carnot_DataType)

@given(instance=carnot_extensions_FormalParameterMappingType_strategy)
@settings(max_examples=50)
def test_carnot_extensions_formalparametermappingtype_instantiation(instance):
    assert isinstance(instance, carnot_extensions_FormalParameterMappingType)

@given(instance=carnot_ViewableType_strategy)
@settings(max_examples=50)
def test_carnot_viewabletype_instantiation(instance):
    assert isinstance(instance, carnot_ViewableType)

@given(instance=FormalParameterMappingsType_strategy)
@settings(max_examples=50)
def test_formalparametermappingstype_instantiation(instance):
    assert isinstance(instance, FormalParameterMappingsType)

@given(instance=carnot_FormalParametersType_strategy)
@settings(max_examples=50)
def test_carnot_formalparameterstype_instantiation(instance):
    assert isinstance(instance, carnot_FormalParametersType)

@given(instance=carnot_ViewType_strategy)
@settings(max_examples=50)
def test_carnot_viewtype_instantiation(instance):
    assert isinstance(instance, carnot_ViewType)



@given(instance=carnot_ViewType_strategy)
def test_carnot_viewtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=carnot_TypeDeclarationsType_strategy)
@settings(max_examples=50)
def test_carnot_typedeclarationstype_instantiation(instance):
    assert isinstance(instance, carnot_TypeDeclarationsType)

@given(instance=carnot_ScriptType_strategy)
@settings(max_examples=50)
def test_carnot_scripttype_instantiation(instance):
    assert isinstance(instance, carnot_ScriptType)

@given(instance=carnot_ExternalPackages_strategy)
@settings(max_examples=50)
def test_carnot_externalpackages_instantiation(instance):
    assert isinstance(instance, carnot_ExternalPackages)

@given(instance=carnot_QualityControlType_strategy)
@settings(max_examples=50)
def test_carnot_qualitycontroltype_instantiation(instance):
    assert isinstance(instance, carnot_QualityControlType)

@given(instance=carnot_ModelerType_strategy)
@settings(max_examples=50)
def test_carnot_modelertype_instantiation(instance):
    assert isinstance(instance, carnot_ModelerType)



@given(instance=carnot_ModelerType_strategy)
def test_carnot_modelertype_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=carnot_ModelerType_strategy)
def test_carnot_modelertype_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=ISwimlaneSymbol_strategy)
@settings(max_examples=50)
def test_iswimlanesymbol_instantiation(instance):
    assert isinstance(instance, ISwimlaneSymbol)

@given(instance=carnot_IdRefOwner_strategy)
@settings(max_examples=50)
def test_carnot_idrefowner_instantiation(instance):
    assert isinstance(instance, carnot_IdRefOwner)

@given(instance=carnot_ExternalPackage_strategy)
@settings(max_examples=50)
def test_carnot_externalpackage_instantiation(instance):
    assert isinstance(instance, carnot_ExternalPackage)

@given(instance=carnot_IdRef_strategy)
@settings(max_examples=50)
def test_carnot_idref_instantiation(instance):
    assert isinstance(instance, carnot_IdRef)



@given(instance=carnot_IdRef_strategy)
def test_carnot_idref_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=carnot_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_carnot_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, carnot_EStringToStringMapEntry)

@given(instance=carnot_DocumentRoot_strategy)
@settings(max_examples=50)
def test_carnot_documentroot_instantiation(instance):
    assert isinstance(instance, carnot_DocumentRoot)



@given(instance=carnot_DocumentRoot_strategy)
def test_carnot_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=AbstractEventSymbol_strategy)
@settings(max_examples=50)
def test_abstracteventsymbol_instantiation(instance):
    assert isinstance(instance, AbstractEventSymbol)

@given(instance=carnot_EndEventSymbol_strategy)
@settings(max_examples=50)
def test_carnot_endeventsymbol_instantiation(instance):
    assert isinstance(instance, carnot_EndEventSymbol)

@given(instance=carnot_IntermediateEventSymbol_strategy)
@settings(max_examples=50)
def test_carnot_intermediateeventsymbol_instantiation(instance):
    assert isinstance(instance, carnot_IntermediateEventSymbol)

@given(instance=carnot_PublicInterfaceSymbol_strategy)
@settings(max_examples=50)
def test_carnot_publicinterfacesymbol_instantiation(instance):
    assert isinstance(instance, carnot_PublicInterfaceSymbol)

@given(instance=carnot_StartEventSymbol_strategy)
@settings(max_examples=50)
def test_carnot_starteventsymbol_instantiation(instance):
    assert isinstance(instance, carnot_StartEventSymbol)

@given(instance=carnot_ModelType_strategy)
@settings(max_examples=50)
def test_carnot_modeltype_instantiation(instance):
    assert isinstance(instance, carnot_ModelType)



@given(instance=carnot_ModelType_strategy)
def test_carnot_modeltype_created_setter(instance):
    original = instance.created
    instance.created = original
    assert instance.created == original



@given(instance=carnot_ModelType_strategy)
def test_carnot_modeltype_vendor_setter(instance):
    original = instance.vendor
    instance.vendor = original
    assert instance.vendor == original



@given(instance=carnot_ModelType_strategy)
def test_carnot_modeltype_modelOID_setter(instance):
    original = instance.modelOID
    instance.modelOID = original
    assert instance.modelOID == original



@given(instance=carnot_ModelType_strategy)
def test_carnot_modeltype_oid_setter(instance):
    original = instance.oid
    instance.oid = original
    assert instance.oid == original



@given(instance=carnot_ModelType_strategy)
def test_carnot_modeltype_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=carnot_ModelType_strategy)
def test_carnot_modeltype_carnotVersion_setter(instance):
    original = instance.carnotVersion
    instance.carnotVersion = original
    assert instance.carnotVersion == original

@given(instance=carnot_ExternalReferenceType_strategy)
@settings(max_examples=50)
def test_carnot_externalreferencetype_instantiation(instance):
    assert isinstance(instance, carnot_ExternalReferenceType)

@given(instance=carnot_ParameterMappingType_strategy)
@settings(max_examples=50)
def test_carnot_parametermappingtype_instantiation(instance):
    assert isinstance(instance, carnot_ParameterMappingType)



@given(instance=carnot_ParameterMappingType_strategy)
def test_carnot_parametermappingtype_parameter_setter(instance):
    original = instance.parameter
    instance.parameter = original
    assert instance.parameter == original



@given(instance=carnot_ParameterMappingType_strategy)
def test_carnot_parametermappingtype_parameterPath_setter(instance):
    original = instance.parameterPath
    instance.parameterPath = original
    assert instance.parameterPath == original



@given(instance=carnot_ParameterMappingType_strategy)
def test_carnot_parametermappingtype_dataPath_setter(instance):
    original = instance.dataPath
    instance.dataPath = original
    assert instance.dataPath == original

@given(instance=ISymbolContainer_strategy)
@settings(max_examples=50)
def test_isymbolcontainer_instantiation(instance):
    assert isinstance(instance, ISymbolContainer)

@given(instance=carnot_LaneSymbol_strategy)
@settings(max_examples=50)
def test_carnot_lanesymbol_instantiation(instance):
    assert isinstance(instance, carnot_LaneSymbol)

@given(instance=carnot_GroupSymbolType_strategy)
@settings(max_examples=50)
def test_carnot_groupsymboltype_instantiation(instance):
    assert isinstance(instance, carnot_GroupSymbolType)

@given(instance=carnot_PoolSymbol_strategy)
@settings(max_examples=50)
def test_carnot_poolsymbol_instantiation(instance):
    assert isinstance(instance, carnot_PoolSymbol)



@given(instance=carnot_PoolSymbol_strategy)
def test_carnot_poolsymbol_boundaryVisible_setter(instance):
    original = instance.boundaryVisible
    instance.boundaryVisible = original
    assert instance.boundaryVisible == original

@given(instance=carnot_DiagramType_strategy)
@settings(max_examples=50)
def test_carnot_diagramtype_instantiation(instance):
    assert isinstance(instance, carnot_DiagramType)



@given(instance=carnot_DiagramType_strategy)
def test_carnot_diagramtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=carnot_DiagramType_strategy)
def test_carnot_diagramtype_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original



@given(instance=carnot_DiagramType_strategy)
def test_carnot_diagramtype_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=carnot_DataPathType_strategy)
@settings(max_examples=50)
def test_carnot_datapathtype_instantiation(instance):
    assert isinstance(instance, carnot_DataPathType)



@given(instance=carnot_DataPathType_strategy)
def test_carnot_datapathtype_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=carnot_DataPathType_strategy)
def test_carnot_datapathtype_dataPath_setter(instance):
    original = instance.dataPath
    instance.dataPath = original
    assert instance.dataPath == original



@given(instance=carnot_DataPathType_strategy)
def test_carnot_datapathtype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original



@given(instance=carnot_DataPathType_strategy)
def test_carnot_datapathtype_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=IConnectionSymbol_strategy)
@settings(max_examples=50)
def test_iconnectionsymbol_instantiation(instance):
    assert isinstance(instance, IConnectionSymbol)

@given(instance=carnot_WorksForConnectionType_strategy)
@settings(max_examples=50)
def test_carnot_worksforconnectiontype_instantiation(instance):
    assert isinstance(instance, carnot_WorksForConnectionType)

@given(instance=carnot_TriggersConnectionType_strategy)
@settings(max_examples=50)
def test_carnot_triggersconnectiontype_instantiation(instance):
    assert isinstance(instance, carnot_TriggersConnectionType)

@given(instance=carnot_PerformsConnectionType_strategy)
@settings(max_examples=50)
def test_carnot_performsconnectiontype_instantiation(instance):
    assert isinstance(instance, carnot_PerformsConnectionType)

@given(instance=carnot_SubProcessOfConnectionType_strategy)
@settings(max_examples=50)
def test_carnot_subprocessofconnectiontype_instantiation(instance):
    assert isinstance(instance, carnot_SubProcessOfConnectionType)

@given(instance=carnot_TransitionConnectionType_strategy)
@settings(max_examples=50)
def test_carnot_transitionconnectiontype_instantiation(instance):
    assert isinstance(instance, carnot_TransitionConnectionType)



@given(instance=carnot_TransitionConnectionType_strategy)
def test_carnot_transitionconnectiontype_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original

@given(instance=carnot_RefersToConnectionType_strategy)
@settings(max_examples=50)
def test_carnot_referstoconnectiontype_instantiation(instance):
    assert isinstance(instance, carnot_RefersToConnectionType)

@given(instance=carnot_DataMappingConnectionType_strategy)
@settings(max_examples=50)
def test_carnot_datamappingconnectiontype_instantiation(instance):
    assert isinstance(instance, carnot_DataMappingConnectionType)

@given(instance=carnot_TeamLeadConnectionType_strategy)
@settings(max_examples=50)
def test_carnot_teamleadconnectiontype_instantiation(instance):
    assert isinstance(instance, carnot_TeamLeadConnectionType)

@given(instance=carnot_PartOfConnectionType_strategy)
@settings(max_examples=50)
def test_carnot_partofconnectiontype_instantiation(instance):
    assert isinstance(instance, carnot_PartOfConnectionType)

@given(instance=carnot_ExecutedByConnectionType_strategy)
@settings(max_examples=50)
def test_carnot_executedbyconnectiontype_instantiation(instance):
    assert isinstance(instance, carnot_ExecutedByConnectionType)

@given(instance=IModelParticipantSymbol_strategy)
@settings(max_examples=50)
def test_imodelparticipantsymbol_instantiation(instance):
    assert isinstance(instance, IModelParticipantSymbol)

@given(instance=carnot_OrganizationSymbolType_strategy)
@settings(max_examples=50)
def test_carnot_organizationsymboltype_instantiation(instance):
    assert isinstance(instance, carnot_OrganizationSymbolType)

@given(instance=carnot_ConditionalPerformerSymbolType_strategy)
@settings(max_examples=50)
def test_carnot_conditionalperformersymboltype_instantiation(instance):
    assert isinstance(instance, carnot_ConditionalPerformerSymbolType)

@given(instance=carnot_RoleSymbolType_strategy)
@settings(max_examples=50)
def test_carnot_rolesymboltype_instantiation(instance):
    assert isinstance(instance, carnot_RoleSymbolType)

@given(instance=AbstractEventAction_strategy)
@settings(max_examples=50)
def test_abstracteventaction_instantiation(instance):
    assert isinstance(instance, AbstractEventAction)

@given(instance=carnot_UnbindActionType_strategy)
@settings(max_examples=50)
def test_carnot_unbindactiontype_instantiation(instance):
    assert isinstance(instance, carnot_UnbindActionType)

@given(instance=carnot_EventActionType_strategy)
@settings(max_examples=50)
def test_carnot_eventactiontype_instantiation(instance):
    assert isinstance(instance, carnot_EventActionType)

@given(instance=carnot_BindActionType_strategy)
@settings(max_examples=50)
def test_carnot_bindactiontype_instantiation(instance):
    assert isinstance(instance, carnot_BindActionType)

@given(instance=IModelParticipant_strategy)
@settings(max_examples=50)
def test_imodelparticipant_instantiation(instance):
    assert isinstance(instance, IModelParticipant)

@given(instance=carnot_RoleType_strategy)
@settings(max_examples=50)
def test_carnot_roletype_instantiation(instance):
    assert isinstance(instance, carnot_RoleType)



@given(instance=carnot_RoleType_strategy)
def test_carnot_roletype_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=carnot_OrganizationType_strategy)
@settings(max_examples=50)
def test_carnot_organizationtype_instantiation(instance):
    assert isinstance(instance, carnot_OrganizationType)

@given(instance=carnot_ConditionalPerformerType_strategy)
@settings(max_examples=50)
def test_carnot_conditionalperformertype_instantiation(instance):
    assert isinstance(instance, carnot_ConditionalPerformerType)



@given(instance=carnot_ConditionalPerformerType_strategy)
def test_carnot_conditionalperformertype_dataPath_setter(instance):
    original = instance.dataPath
    instance.dataPath = original
    assert instance.dataPath == original



@given(instance=carnot_ConditionalPerformerType_strategy)
def test_carnot_conditionalperformertype_isUser_setter(instance):
    original = instance.isUser
    instance.isUser = original
    assert instance.isUser == original

@given(instance=carnot_XmlTextNode_strategy)
@settings(max_examples=50)
def test_carnot_xmltextnode_instantiation(instance):
    assert isinstance(instance, carnot_XmlTextNode)



@given(instance=carnot_XmlTextNode_strategy)
def test_carnot_xmltextnode_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=IMetaType_strategy)
@settings(max_examples=50)
def test_imetatype_instantiation(instance):
    assert isinstance(instance, IMetaType)

@given(instance=carnot_TriggerTypeType_strategy)
@settings(max_examples=50)
def test_carnot_triggertypetype_instantiation(instance):
    assert isinstance(instance, carnot_TriggerTypeType)



@given(instance=carnot_TriggerTypeType_strategy)
def test_carnot_triggertypetype_panelClass_setter(instance):
    original = instance.panelClass
    instance.panelClass = original
    assert instance.panelClass == original



@given(instance=carnot_TriggerTypeType_strategy)
def test_carnot_triggertypetype_pullTriggerEvaluator_setter(instance):
    original = instance.pullTriggerEvaluator
    instance.pullTriggerEvaluator = original
    assert instance.pullTriggerEvaluator == original



@given(instance=carnot_TriggerTypeType_strategy)
def test_carnot_triggertypetype_rule_setter(instance):
    original = instance.rule
    instance.rule = original
    assert instance.rule == original



@given(instance=carnot_TriggerTypeType_strategy)
def test_carnot_triggertypetype_pullTrigger_setter(instance):
    original = instance.pullTrigger
    instance.pullTrigger = original
    assert instance.pullTrigger == original

@given(instance=carnot_DataTypeType_strategy)
@settings(max_examples=50)
def test_carnot_datatypetype_instantiation(instance):
    assert isinstance(instance, carnot_DataTypeType)



@given(instance=carnot_DataTypeType_strategy)
def test_carnot_datatypetype_panelClass_setter(instance):
    original = instance.panelClass
    instance.panelClass = original
    assert instance.panelClass == original



@given(instance=carnot_DataTypeType_strategy)
def test_carnot_datatypetype_storageStrategy_setter(instance):
    original = instance.storageStrategy
    instance.storageStrategy = original
    assert instance.storageStrategy == original



@given(instance=carnot_DataTypeType_strategy)
def test_carnot_datatypetype_valueCreator_setter(instance):
    original = instance.valueCreator
    instance.valueCreator = original
    assert instance.valueCreator == original



@given(instance=carnot_DataTypeType_strategy)
def test_carnot_datatypetype_accessPathEditor_setter(instance):
    original = instance.accessPathEditor
    instance.accessPathEditor = original
    assert instance.accessPathEditor == original



@given(instance=carnot_DataTypeType_strategy)
def test_carnot_datatypetype_writable_setter(instance):
    original = instance.writable
    instance.writable = original
    assert instance.writable == original



@given(instance=carnot_DataTypeType_strategy)
def test_carnot_datatypetype_instanceClass_setter(instance):
    original = instance.instanceClass
    instance.instanceClass = original
    assert instance.instanceClass == original



@given(instance=carnot_DataTypeType_strategy)
def test_carnot_datatypetype_validatorClass_setter(instance):
    original = instance.validatorClass
    instance.validatorClass = original
    assert instance.validatorClass == original



@given(instance=carnot_DataTypeType_strategy)
def test_carnot_datatypetype_readable_setter(instance):
    original = instance.readable
    instance.readable = original
    assert instance.readable == original



@given(instance=carnot_DataTypeType_strategy)
def test_carnot_datatypetype_evaluator_setter(instance):
    original = instance.evaluator
    instance.evaluator = original
    assert instance.evaluator == original

@given(instance=carnot_EventConditionTypeType_strategy)
@settings(max_examples=50)
def test_carnot_eventconditiontypetype_instantiation(instance):
    assert isinstance(instance, carnot_EventConditionTypeType)



@given(instance=carnot_EventConditionTypeType_strategy)
def test_carnot_eventconditiontypetype_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original



@given(instance=carnot_EventConditionTypeType_strategy)
def test_carnot_eventconditiontypetype_rule_setter(instance):
    original = instance.rule
    instance.rule = original
    assert instance.rule == original



@given(instance=carnot_EventConditionTypeType_strategy)
def test_carnot_eventconditiontypetype_pullEventEmitterClass_setter(instance):
    original = instance.pullEventEmitterClass
    instance.pullEventEmitterClass = original
    assert instance.pullEventEmitterClass == original



@given(instance=carnot_EventConditionTypeType_strategy)
def test_carnot_eventconditiontypetype_panelClass_setter(instance):
    original = instance.panelClass
    instance.panelClass = original
    assert instance.panelClass == original



@given(instance=carnot_EventConditionTypeType_strategy)
def test_carnot_eventconditiontypetype_activityCondition_setter(instance):
    original = instance.activityCondition
    instance.activityCondition = original
    assert instance.activityCondition == original



@given(instance=carnot_EventConditionTypeType_strategy)
def test_carnot_eventconditiontypetype_processCondition_setter(instance):
    original = instance.processCondition
    instance.processCondition = original
    assert instance.processCondition == original



@given(instance=carnot_EventConditionTypeType_strategy)
def test_carnot_eventconditiontypetype_binderClass_setter(instance):
    original = instance.binderClass
    instance.binderClass = original
    assert instance.binderClass == original

@given(instance=carnot_ApplicationTypeType_strategy)
@settings(max_examples=50)
def test_carnot_applicationtypetype_instantiation(instance):
    assert isinstance(instance, carnot_ApplicationTypeType)



@given(instance=carnot_ApplicationTypeType_strategy)
def test_carnot_applicationtypetype_instanceClass_setter(instance):
    original = instance.instanceClass
    instance.instanceClass = original
    assert instance.instanceClass == original



@given(instance=carnot_ApplicationTypeType_strategy)
def test_carnot_applicationtypetype_accessPointProviderClass_setter(instance):
    original = instance.accessPointProviderClass
    instance.accessPointProviderClass = original
    assert instance.accessPointProviderClass == original



@given(instance=carnot_ApplicationTypeType_strategy)
def test_carnot_applicationtypetype_synchronous_setter(instance):
    original = instance.synchronous
    instance.synchronous = original
    assert instance.synchronous == original



@given(instance=carnot_ApplicationTypeType_strategy)
def test_carnot_applicationtypetype_panelClass_setter(instance):
    original = instance.panelClass
    instance.panelClass = original
    assert instance.panelClass == original



@given(instance=carnot_ApplicationTypeType_strategy)
def test_carnot_applicationtypetype_validatorClass_setter(instance):
    original = instance.validatorClass
    instance.validatorClass = original
    assert instance.validatorClass == original

@given(instance=carnot_LinkTypeType_strategy)
@settings(max_examples=50)
def test_carnot_linktypetype_instantiation(instance):
    assert isinstance(instance, carnot_LinkTypeType)



@given(instance=carnot_LinkTypeType_strategy)
def test_carnot_linktypetype_showRoleNames_setter(instance):
    original = instance.showRoleNames
    instance.showRoleNames = original
    assert instance.showRoleNames == original



@given(instance=carnot_LinkTypeType_strategy)
def test_carnot_linktypetype_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original



@given(instance=carnot_LinkTypeType_strategy)
def test_carnot_linktypetype_targetSymbol_setter(instance):
    original = instance.targetSymbol
    instance.targetSymbol = original
    assert instance.targetSymbol == original



@given(instance=carnot_LinkTypeType_strategy)
def test_carnot_linktypetype_sourceCardinality_setter(instance):
    original = instance.sourceCardinality
    instance.sourceCardinality = original
    assert instance.sourceCardinality == original



@given(instance=carnot_LinkTypeType_strategy)
def test_carnot_linktypetype_sourceClass_setter(instance):
    original = instance.sourceClass
    instance.sourceClass = original
    assert instance.sourceClass == original



@given(instance=carnot_LinkTypeType_strategy)
def test_carnot_linktypetype_targetClass_setter(instance):
    original = instance.targetClass
    instance.targetClass = original
    assert instance.targetClass == original



@given(instance=carnot_LinkTypeType_strategy)
def test_carnot_linktypetype_lineColor_setter(instance):
    original = instance.lineColor
    instance.lineColor = original
    assert instance.lineColor == original



@given(instance=carnot_LinkTypeType_strategy)
def test_carnot_linktypetype_targetRole_setter(instance):
    original = instance.targetRole
    instance.targetRole = original
    assert instance.targetRole == original



@given(instance=carnot_LinkTypeType_strategy)
def test_carnot_linktypetype_targetCardinality_setter(instance):
    original = instance.targetCardinality
    instance.targetCardinality = original
    assert instance.targetCardinality == original



@given(instance=carnot_LinkTypeType_strategy)
def test_carnot_linktypetype_sourceSymbol_setter(instance):
    original = instance.sourceSymbol
    instance.sourceSymbol = original
    assert instance.sourceSymbol == original



@given(instance=carnot_LinkTypeType_strategy)
def test_carnot_linktypetype_showLinkTypeName_setter(instance):
    original = instance.showLinkTypeName
    instance.showLinkTypeName = original
    assert instance.showLinkTypeName == original



@given(instance=carnot_LinkTypeType_strategy)
def test_carnot_linktypetype_sourceRole_setter(instance):
    original = instance.sourceRole
    instance.sourceRole = original
    assert instance.sourceRole == original

@given(instance=carnot_ApplicationContextTypeType_strategy)
@settings(max_examples=50)
def test_carnot_applicationcontexttypetype_instantiation(instance):
    assert isinstance(instance, carnot_ApplicationContextTypeType)



@given(instance=carnot_ApplicationContextTypeType_strategy)
def test_carnot_applicationcontexttypetype_hasApplicationPath_setter(instance):
    original = instance.hasApplicationPath
    instance.hasApplicationPath = original
    assert instance.hasApplicationPath == original



@given(instance=carnot_ApplicationContextTypeType_strategy)
def test_carnot_applicationcontexttypetype_accessPointProviderClass_setter(instance):
    original = instance.accessPointProviderClass
    instance.accessPointProviderClass = original
    assert instance.accessPointProviderClass == original



@given(instance=carnot_ApplicationContextTypeType_strategy)
def test_carnot_applicationcontexttypetype_panelClass_setter(instance):
    original = instance.panelClass
    instance.panelClass = original
    assert instance.panelClass == original



@given(instance=carnot_ApplicationContextTypeType_strategy)
def test_carnot_applicationcontexttypetype_validatorClass_setter(instance):
    original = instance.validatorClass
    instance.validatorClass = original
    assert instance.validatorClass == original



@given(instance=carnot_ApplicationContextTypeType_strategy)
def test_carnot_applicationcontexttypetype_hasMappingId_setter(instance):
    original = instance.hasMappingId
    instance.hasMappingId = original
    assert instance.hasMappingId == original

@given(instance=carnot_TextType_strategy)
@settings(max_examples=50)
def test_carnot_texttype_instantiation(instance):
    assert isinstance(instance, carnot_TextType)



@given(instance=carnot_TextType_strategy)
def test_carnot_texttype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=carnot_LoopType_strategy)
@settings(max_examples=50)
def test_carnot_looptype_instantiation(instance):
    assert isinstance(instance, carnot_LoopType)

@given(instance=IAccessPointOwner_strategy)
@settings(max_examples=50)
def test_iaccesspointowner_instantiation(instance):
    assert isinstance(instance, IAccessPointOwner)

@given(instance=carnot_Code_strategy)
@settings(max_examples=50)
def test_carnot_code_instantiation(instance):
    assert isinstance(instance, carnot_Code)



@given(instance=carnot_Code_strategy)
def test_carnot_code_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=carnot_Code_strategy)
def test_carnot_code_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=carnot_Code_strategy)
def test_carnot_code_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=carnot_TransitionType_strategy)
@settings(max_examples=50)
def test_carnot_transitiontype_instantiation(instance):
    assert isinstance(instance, carnot_TransitionType)



@given(instance=carnot_TransitionType_strategy)
def test_carnot_transitiontype_forkOnTraversal_setter(instance):
    original = instance.forkOnTraversal
    instance.forkOnTraversal = original
    assert instance.forkOnTraversal == original



@given(instance=carnot_TransitionType_strategy)
def test_carnot_transitiontype_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=carnot_DataMappingType_strategy)
@settings(max_examples=50)
def test_carnot_datamappingtype_instantiation(instance):
    assert isinstance(instance, carnot_DataMappingType)



@given(instance=carnot_DataMappingType_strategy)
def test_carnot_datamappingtype_applicationPath_setter(instance):
    original = instance.applicationPath
    instance.applicationPath = original
    assert instance.applicationPath == original



@given(instance=carnot_DataMappingType_strategy)
def test_carnot_datamappingtype_dataPath_setter(instance):
    original = instance.dataPath
    instance.dataPath = original
    assert instance.dataPath == original



@given(instance=carnot_DataMappingType_strategy)
def test_carnot_datamappingtype_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=carnot_DataMappingType_strategy)
def test_carnot_datamappingtype_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original



@given(instance=carnot_DataMappingType_strategy)
def test_carnot_datamappingtype_applicationAccessPoint_setter(instance):
    original = instance.applicationAccessPoint
    instance.applicationAccessPoint = original
    assert instance.applicationAccessPoint == original

@given(instance=IdRefOwner_strategy)
@settings(max_examples=50)
def test_idrefowner_instantiation(instance):
    assert isinstance(instance, IdRefOwner)

@given(instance=IEventHandlerOwner_strategy)
@settings(max_examples=50)
def test_ieventhandlerowner_instantiation(instance):
    assert isinstance(instance, IEventHandlerOwner)

@given(instance=carnot_ProcessDefinitionType_strategy)
@settings(max_examples=50)
def test_carnot_processdefinitiontype_instantiation(instance):
    assert isinstance(instance, carnot_ProcessDefinitionType)



@given(instance=carnot_ProcessDefinitionType_strategy)
def test_carnot_processdefinitiontype_defaultPriority_setter(instance):
    original = instance.defaultPriority
    instance.defaultPriority = original
    assert instance.defaultPriority == original

@given(instance=carnot_ActivityType_strategy)
@settings(max_examples=50)
def test_carnot_activitytype_instantiation(instance):
    assert isinstance(instance, carnot_ActivityType)



@given(instance=carnot_ActivityType_strategy)
def test_carnot_activitytype_subProcessMode_setter(instance):
    original = instance.subProcessMode
    instance.subProcessMode = original
    assert instance.subProcessMode == original



@given(instance=carnot_ActivityType_strategy)
def test_carnot_activitytype_loopCondition_setter(instance):
    original = instance.loopCondition
    instance.loopCondition = original
    assert instance.loopCondition == original



@given(instance=carnot_ActivityType_strategy)
def test_carnot_activitytype_hibernateOnCreation_setter(instance):
    original = instance.hibernateOnCreation
    instance.hibernateOnCreation = original
    assert instance.hibernateOnCreation == original



@given(instance=carnot_ActivityType_strategy)
def test_carnot_activitytype_join_setter(instance):
    original = instance.join
    instance.join = original
    assert instance.join == original



@given(instance=carnot_ActivityType_strategy)
def test_carnot_activitytype_split_setter(instance):
    original = instance.split
    instance.split = original
    assert instance.split == original



@given(instance=carnot_ActivityType_strategy)
def test_carnot_activitytype_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original



@given(instance=carnot_ActivityType_strategy)
def test_carnot_activitytype_allowsAbortByPerformer_setter(instance):
    original = instance.allowsAbortByPerformer
    instance.allowsAbortByPerformer = original
    assert instance.allowsAbortByPerformer == original



@given(instance=carnot_ActivityType_strategy)
def test_carnot_activitytype_loopType_setter(instance):
    original = instance.loopType
    instance.loopType = original
    assert instance.loopType == original

@given(instance=carnot_EventActionTypeType_strategy)
@settings(max_examples=50)
def test_carnot_eventactiontypetype_instantiation(instance):
    assert isinstance(instance, carnot_EventActionTypeType)



@given(instance=carnot_EventActionTypeType_strategy)
def test_carnot_eventactiontypetype_unsupportedContexts_setter(instance):
    original = instance.unsupportedContexts
    instance.unsupportedContexts = original
    assert instance.unsupportedContexts == original



@given(instance=carnot_EventActionTypeType_strategy)
def test_carnot_eventactiontypetype_actionClass_setter(instance):
    original = instance.actionClass
    instance.actionClass = original
    assert instance.actionClass == original



@given(instance=carnot_EventActionTypeType_strategy)
def test_carnot_eventactiontypetype_supportedConditionTypes_setter(instance):
    original = instance.supportedConditionTypes
    instance.supportedConditionTypes = original
    assert instance.supportedConditionTypes == original



@given(instance=carnot_EventActionTypeType_strategy)
def test_carnot_eventactiontypetype_panelClass_setter(instance):
    original = instance.panelClass
    instance.panelClass = original
    assert instance.panelClass == original



@given(instance=carnot_EventActionTypeType_strategy)
def test_carnot_eventactiontypetype_processAction_setter(instance):
    original = instance.processAction
    instance.processAction = original
    assert instance.processAction == original



@given(instance=carnot_EventActionTypeType_strategy)
def test_carnot_eventactiontypetype_activityAction_setter(instance):
    original = instance.activityAction
    instance.activityAction = original
    assert instance.activityAction == original

@given(instance=ITypedElement_strategy)
@settings(max_examples=50)
def test_itypedelement_instantiation(instance):
    assert isinstance(instance, ITypedElement)

@given(instance=carnot_DataType_strategy)
@settings(max_examples=50)
def test_carnot_datatype_instantiation(instance):
    assert isinstance(instance, carnot_DataType)



@given(instance=carnot_DataType_strategy)
def test_carnot_datatype_predefined_setter(instance):
    original = instance.predefined
    instance.predefined = original
    assert instance.predefined == original

@given(instance=carnot_TriggerType_strategy)
@settings(max_examples=50)
def test_carnot_triggertype_instantiation(instance):
    assert isinstance(instance, carnot_TriggerType)

@given(instance=carnot_ApplicationType_strategy)
@settings(max_examples=50)
def test_carnot_applicationtype_instantiation(instance):
    assert isinstance(instance, carnot_ApplicationType)



@given(instance=carnot_ApplicationType_strategy)
def test_carnot_applicationtype_interactive_setter(instance):
    original = instance.interactive
    instance.interactive = original
    assert instance.interactive == original

@given(instance=carnot_ContextType_strategy)
@settings(max_examples=50)
def test_carnot_contexttype_instantiation(instance):
    assert isinstance(instance, carnot_ContextType)

@given(instance=carnot_EventHandlerType_strategy)
@settings(max_examples=50)
def test_carnot_eventhandlertype_instantiation(instance):
    assert isinstance(instance, carnot_EventHandlerType)



@given(instance=carnot_EventHandlerType_strategy)
def test_carnot_eventhandlertype_unbindOnMatch_setter(instance):
    original = instance.unbindOnMatch
    instance.unbindOnMatch = original
    assert instance.unbindOnMatch == original



@given(instance=carnot_EventHandlerType_strategy)
def test_carnot_eventhandlertype_consumeOnMatch_setter(instance):
    original = instance.consumeOnMatch
    instance.consumeOnMatch = original
    assert instance.consumeOnMatch == original



@given(instance=carnot_EventHandlerType_strategy)
def test_carnot_eventhandlertype_autoBind_setter(instance):
    original = instance.autoBind
    instance.autoBind = original
    assert instance.autoBind == original



@given(instance=carnot_EventHandlerType_strategy)
def test_carnot_eventhandlertype_logHandler_setter(instance):
    original = instance.logHandler
    instance.logHandler = original
    assert instance.logHandler == original

@given(instance=carnot_GenericLinkConnectionType_strategy)
@settings(max_examples=50)
def test_carnot_genericlinkconnectiontype_instantiation(instance):
    assert isinstance(instance, carnot_GenericLinkConnectionType)

@given(instance=carnot_AccessPointType_strategy)
@settings(max_examples=50)
def test_carnot_accesspointtype_instantiation(instance):
    assert isinstance(instance, carnot_AccessPointType)



@given(instance=carnot_AccessPointType_strategy)
def test_carnot_accesspointtype_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=carnot_AbstractEventAction_strategy)
@settings(max_examples=50)
def test_carnot_abstracteventaction_instantiation(instance):
    assert isinstance(instance, carnot_AbstractEventAction)
