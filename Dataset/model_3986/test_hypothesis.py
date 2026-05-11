import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    carnot::XmlTextNode,
    IMetaType,
    carnot::ApplicationTypeType,
    carnot::ApplicationContextTypeType,
    carnot::TextType,
    carnot::LoopType,
    IAccessPointOwner,
    carnot::Code,
    IdRefOwner,
    IEventHandlerOwner,
    carnot::EventActionTypeType,
    ITypedElement,
    IModelElementNodeSymbol,
    carnot::IModelParticipantSymbol,
    carnot::ParticipantType,
    carnot::DataTypeType,
    IFlowObjectSymbol,
    carnot::AbstractEventSymbol,
    IGraphicalObject,
    carnot::IConnectionSymbol,
    carnot::INodeSymbol,
    INodeSymbol,
    carnot::IFlowObjectSymbol,
    carnot::IModelElementNodeSymbol,
    carnot::TextSymbolType,
    carnot::ProcessSymbolType,
    carnot::GatewaySymbol,
    carnot::DataSymbolType,
    carnot::ModelerSymbolType,
    carnot::ActivitySymbolType,
    carnot::ITypedElement,
    IIdentifiableModelElement,
    carnot::AbstractEventAction,
    carnot::TransitionType,
    carnot::ActivityType,
    carnot::IModelParticipant,
    carnot::ProcessDefinitionType,
    carnot::ApplicationType,
    carnot::IMetaType,
    carnot::AccessPointType,
    carnot::IAccessPointOwner,
    carnot::ApplicationSymbolType,
    carnot::AnnotationSymbolType,
    carnot::IModelElement,
    carnot::EObject,
    carnot::IdentifiableReference,
    carnot::AttributeType,
    carnot::IExtensibleElement,
    carnot::IIdentifiableElement,
    carnot::EventHandlerType,
    carnot::IEventHandlerOwner,
    carnot::DescriptionType,
    IExtensibleElement,
    carnot::ISymbolContainer,
    IIdentifiableElement,
    carnot::ISwimlaneSymbol,
    IModelElement,
    carnot::IGraphicalObject,
    carnot::DataMappingType,
    carnot::ContextType,
    carnot::IIdentifiableModelElement,
    carnot::Coordinates,
    FormalParameterMappingType,
    carnot::extensions::FormalParameterMappingsType,
    extensions::carnot::FormalParameterType,
    extensions::carnot::DataType,
    carnot::extensions::FormalParameterMappingType,
    carnot::ViewableType,
    carnot::TriggerType,
    FormalParameterMappingsType,
    carnot::FormalParametersType,
    carnot::ViewType,
    carnot::TypeDeclarationsType,
    carnot::ScriptType,
    carnot::ExternalPackages,
    carnot::TriggerTypeType,
    carnot::QualityControlType,
    carnot::ModelerType,
    ISwimlaneSymbol,
    carnot::LinkTypeType,
    carnot::IdRefOwner,
    carnot::ExternalPackage,
    carnot::IdRef,
    carnot::EventConditionTypeType,
    carnot::EStringToStringMapEntry,
    carnot::DocumentRoot,
    AbstractEventSymbol,
    carnot::PublicInterfaceSymbol,
    carnot::IntermediateEventSymbol,
    carnot::StartEventSymbol,
    carnot::EndEventSymbol,
    carnot::ModelType,
    carnot::ExternalReferenceType,
    carnot::ParameterMappingType,
    ISymbolContainer,
    carnot::PoolSymbol,
    carnot::GroupSymbolType,
    carnot::LaneSymbol,
    carnot::DiagramType,
    carnot::DataPathType,
    IConnectionSymbol,
    carnot::TransitionConnectionType,
    carnot::TeamLeadConnectionType,
    carnot::GenericLinkConnectionType,
    carnot::WorksForConnectionType,
    carnot::SubProcessOfConnectionType,
    carnot::PartOfConnectionType,
    carnot::ExecutedByConnectionType,
    carnot::RefersToConnectionType,
    carnot::TriggersConnectionType,
    carnot::PerformsConnectionType,
    carnot::DataMappingConnectionType,
    IModelParticipantSymbol,
    carnot::RoleSymbolType,
    carnot::OrganizationSymbolType,
    carnot::ConditionalPerformerSymbolType,
    AbstractEventAction,
    carnot::EventActionType,
    carnot::UnbindActionType,
    carnot::BindActionType,
    carnot::DataType,
    IModelParticipant,
    carnot::OrganizationType,
    carnot::ConditionalPerformerType,
    carnot::RoleType,
    LinkCardinality,
    LinkEndStyle,
    LoopType,
    ImplementationType,
    RoutingType,
    SubProcessModeType,
    LinkColor,
    OrientationType,
    DiagramModeType,
    FlowControlType,
    ActivityImplementationType,
    JoinSplitType,
    LinkLineStyle,
    DirectionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_carnot::xmltextnode_is_not_abstract():
    assert not inspect.isabstract(carnot::XmlTextNode)


def test_carnot::xmltextnode_constructor_exists():
    assert callable(carnot::XmlTextNode.__init__)


def test_carnot::xmltextnode_constructor_args():
    sig = inspect.signature(carnot::XmlTextNode.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_carnot::xmltextnode_has_mixed():
    assert hasattr(carnot::XmlTextNode, "mixed")
    descriptor = None
    for klass in carnot::XmlTextNode.__mro__:
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



def test_carnot::applicationtypetype_is_not_abstract():
    assert not inspect.isabstract(carnot::ApplicationTypeType)


def test_carnot::applicationtypetype_constructor_exists():
    assert callable(carnot::ApplicationTypeType.__init__)


def test_carnot::applicationtypetype_constructor_args():
    sig = inspect.signature(carnot::ApplicationTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "accessPointProviderClass" in params, "Missing parameter 'accessPointProviderClass'"
    assert "instanceClass" in params, "Missing parameter 'instanceClass'"
    assert "panelClass" in params, "Missing parameter 'panelClass'"
    assert "synchronous" in params, "Missing parameter 'synchronous'"
    assert "validatorClass" in params, "Missing parameter 'validatorClass'"

def test_carnot::applicationtypetype_has_accessPointProviderClass():
    assert hasattr(carnot::ApplicationTypeType, "accessPointProviderClass")
    descriptor = None
    for klass in carnot::ApplicationTypeType.__mro__:
        if "accessPointProviderClass" in klass.__dict__:
            descriptor = klass.__dict__["accessPointProviderClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot::applicationtypetype_has_instanceClass():
    assert hasattr(carnot::ApplicationTypeType, "instanceClass")
    descriptor = None
    for klass in carnot::ApplicationTypeType.__mro__:
        if "instanceClass" in klass.__dict__:
            descriptor = klass.__dict__["instanceClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot::applicationtypetype_has_panelClass():
    assert hasattr(carnot::ApplicationTypeType, "panelClass")
    descriptor = None
    for klass in carnot::ApplicationTypeType.__mro__:
        if "panelClass" in klass.__dict__:
            descriptor = klass.__dict__["panelClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot::applicationtypetype_has_synchronous():
    assert hasattr(carnot::ApplicationTypeType, "synchronous")
    descriptor = None
    for klass in carnot::ApplicationTypeType.__mro__:
        if "synchronous" in klass.__dict__:
            descriptor = klass.__dict__["synchronous"]
            break
    assert isinstance(descriptor, property)

def test_carnot::applicationtypetype_has_validatorClass():
    assert hasattr(carnot::ApplicationTypeType, "validatorClass")
    descriptor = None
    for klass in carnot::ApplicationTypeType.__mro__:
        if "validatorClass" in klass.__dict__:
            descriptor = klass.__dict__["validatorClass"]
            break
    assert isinstance(descriptor, property)



def test_carnot::applicationcontexttypetype_is_not_abstract():
    assert not inspect.isabstract(carnot::ApplicationContextTypeType)


def test_carnot::applicationcontexttypetype_constructor_exists():
    assert callable(carnot::ApplicationContextTypeType.__init__)


def test_carnot::applicationcontexttypetype_constructor_args():
    sig = inspect.signature(carnot::ApplicationContextTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "accessPointProviderClass" in params, "Missing parameter 'accessPointProviderClass'"
    assert "panelClass" in params, "Missing parameter 'panelClass'"
    assert "hasApplicationPath" in params, "Missing parameter 'hasApplicationPath'"
    assert "hasMappingId" in params, "Missing parameter 'hasMappingId'"
    assert "validatorClass" in params, "Missing parameter 'validatorClass'"

def test_carnot::applicationcontexttypetype_has_accessPointProviderClass():
    assert hasattr(carnot::ApplicationContextTypeType, "accessPointProviderClass")
    descriptor = None
    for klass in carnot::ApplicationContextTypeType.__mro__:
        if "accessPointProviderClass" in klass.__dict__:
            descriptor = klass.__dict__["accessPointProviderClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot::applicationcontexttypetype_has_panelClass():
    assert hasattr(carnot::ApplicationContextTypeType, "panelClass")
    descriptor = None
    for klass in carnot::ApplicationContextTypeType.__mro__:
        if "panelClass" in klass.__dict__:
            descriptor = klass.__dict__["panelClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot::applicationcontexttypetype_has_hasApplicationPath():
    assert hasattr(carnot::ApplicationContextTypeType, "hasApplicationPath")
    descriptor = None
    for klass in carnot::ApplicationContextTypeType.__mro__:
        if "hasApplicationPath" in klass.__dict__:
            descriptor = klass.__dict__["hasApplicationPath"]
            break
    assert isinstance(descriptor, property)

def test_carnot::applicationcontexttypetype_has_hasMappingId():
    assert hasattr(carnot::ApplicationContextTypeType, "hasMappingId")
    descriptor = None
    for klass in carnot::ApplicationContextTypeType.__mro__:
        if "hasMappingId" in klass.__dict__:
            descriptor = klass.__dict__["hasMappingId"]
            break
    assert isinstance(descriptor, property)

def test_carnot::applicationcontexttypetype_has_validatorClass():
    assert hasattr(carnot::ApplicationContextTypeType, "validatorClass")
    descriptor = None
    for klass in carnot::ApplicationContextTypeType.__mro__:
        if "validatorClass" in klass.__dict__:
            descriptor = klass.__dict__["validatorClass"]
            break
    assert isinstance(descriptor, property)



def test_carnot::texttype_is_not_abstract():
    assert not inspect.isabstract(carnot::TextType)


def test_carnot::texttype_constructor_exists():
    assert callable(carnot::TextType.__init__)


def test_carnot::texttype_constructor_args():
    sig = inspect.signature(carnot::TextType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_carnot::texttype_has_mixed():
    assert hasattr(carnot::TextType, "mixed")
    descriptor = None
    for klass in carnot::TextType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_carnot::looptype_is_not_abstract():
    assert not inspect.isabstract(carnot::LoopType)


def test_carnot::looptype_constructor_exists():
    assert callable(carnot::LoopType.__init__)


def test_carnot::looptype_constructor_args():
    sig = inspect.signature(carnot::LoopType.__init__)
    params = list(sig.parameters.keys())



def test_iaccesspointowner_is_not_abstract():
    assert not inspect.isabstract(IAccessPointOwner)


def test_iaccesspointowner_constructor_exists():
    assert callable(IAccessPointOwner.__init__)


def test_iaccesspointowner_constructor_args():
    sig = inspect.signature(IAccessPointOwner.__init__)
    params = list(sig.parameters.keys())



def test_carnot::code_is_not_abstract():
    assert not inspect.isabstract(carnot::Code)


def test_carnot::code_constructor_exists():
    assert callable(carnot::Code.__init__)


def test_carnot::code_constructor_args():
    sig = inspect.signature(carnot::Code.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_carnot::code_has_code():
    assert hasattr(carnot::Code, "code")
    descriptor = None
    for klass in carnot::Code.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_carnot::code_has_value():
    assert hasattr(carnot::Code, "value")
    descriptor = None
    for klass in carnot::Code.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_carnot::code_has_name():
    assert hasattr(carnot::Code, "name")
    descriptor = None
    for klass in carnot::Code.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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



def test_carnot::eventactiontypetype_is_not_abstract():
    assert not inspect.isabstract(carnot::EventActionTypeType)


def test_carnot::eventactiontypetype_constructor_exists():
    assert callable(carnot::EventActionTypeType.__init__)


def test_carnot::eventactiontypetype_constructor_args():
    sig = inspect.signature(carnot::EventActionTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "unsupportedContexts" in params, "Missing parameter 'unsupportedContexts'"
    assert "activityAction" in params, "Missing parameter 'activityAction'"
    assert "supportedConditionTypes" in params, "Missing parameter 'supportedConditionTypes'"
    assert "actionClass" in params, "Missing parameter 'actionClass'"
    assert "processAction" in params, "Missing parameter 'processAction'"
    assert "panelClass" in params, "Missing parameter 'panelClass'"

def test_carnot::eventactiontypetype_has_unsupportedContexts():
    assert hasattr(carnot::EventActionTypeType, "unsupportedContexts")
    descriptor = None
    for klass in carnot::EventActionTypeType.__mro__:
        if "unsupportedContexts" in klass.__dict__:
            descriptor = klass.__dict__["unsupportedContexts"]
            break
    assert isinstance(descriptor, property)

def test_carnot::eventactiontypetype_has_activityAction():
    assert hasattr(carnot::EventActionTypeType, "activityAction")
    descriptor = None
    for klass in carnot::EventActionTypeType.__mro__:
        if "activityAction" in klass.__dict__:
            descriptor = klass.__dict__["activityAction"]
            break
    assert isinstance(descriptor, property)

def test_carnot::eventactiontypetype_has_supportedConditionTypes():
    assert hasattr(carnot::EventActionTypeType, "supportedConditionTypes")
    descriptor = None
    for klass in carnot::EventActionTypeType.__mro__:
        if "supportedConditionTypes" in klass.__dict__:
            descriptor = klass.__dict__["supportedConditionTypes"]
            break
    assert isinstance(descriptor, property)

def test_carnot::eventactiontypetype_has_actionClass():
    assert hasattr(carnot::EventActionTypeType, "actionClass")
    descriptor = None
    for klass in carnot::EventActionTypeType.__mro__:
        if "actionClass" in klass.__dict__:
            descriptor = klass.__dict__["actionClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot::eventactiontypetype_has_processAction():
    assert hasattr(carnot::EventActionTypeType, "processAction")
    descriptor = None
    for klass in carnot::EventActionTypeType.__mro__:
        if "processAction" in klass.__dict__:
            descriptor = klass.__dict__["processAction"]
            break
    assert isinstance(descriptor, property)

def test_carnot::eventactiontypetype_has_panelClass():
    assert hasattr(carnot::EventActionTypeType, "panelClass")
    descriptor = None
    for klass in carnot::EventActionTypeType.__mro__:
        if "panelClass" in klass.__dict__:
            descriptor = klass.__dict__["panelClass"]
            break
    assert isinstance(descriptor, property)



def test_itypedelement_is_not_abstract():
    assert not inspect.isabstract(ITypedElement)


def test_itypedelement_constructor_exists():
    assert callable(ITypedElement.__init__)


def test_itypedelement_constructor_args():
    sig = inspect.signature(ITypedElement.__init__)
    params = list(sig.parameters.keys())



def test_imodelelementnodesymbol_is_not_abstract():
    assert not inspect.isabstract(IModelElementNodeSymbol)


def test_imodelelementnodesymbol_constructor_exists():
    assert callable(IModelElementNodeSymbol.__init__)


def test_imodelelementnodesymbol_constructor_args():
    sig = inspect.signature(IModelElementNodeSymbol.__init__)
    params = list(sig.parameters.keys())



def test_carnot::imodelparticipantsymbol_is_not_abstract():
    assert not inspect.isabstract(carnot::IModelParticipantSymbol)


def test_carnot::imodelparticipantsymbol_constructor_exists():
    assert callable(carnot::IModelParticipantSymbol.__init__)


def test_carnot::imodelparticipantsymbol_constructor_args():
    sig = inspect.signature(carnot::IModelParticipantSymbol.__init__)
    params = list(sig.parameters.keys())



def test_carnot::participanttype_is_not_abstract():
    assert not inspect.isabstract(carnot::ParticipantType)


def test_carnot::participanttype_constructor_exists():
    assert callable(carnot::ParticipantType.__init__)


def test_carnot::participanttype_constructor_args():
    sig = inspect.signature(carnot::ParticipantType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::datatypetype_is_not_abstract():
    assert not inspect.isabstract(carnot::DataTypeType)


def test_carnot::datatypetype_constructor_exists():
    assert callable(carnot::DataTypeType.__init__)


def test_carnot::datatypetype_constructor_args():
    sig = inspect.signature(carnot::DataTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "readable" in params, "Missing parameter 'readable'"
    assert "valueCreator" in params, "Missing parameter 'valueCreator'"
    assert "accessPathEditor" in params, "Missing parameter 'accessPathEditor'"
    assert "writable" in params, "Missing parameter 'writable'"
    assert "panelClass" in params, "Missing parameter 'panelClass'"
    assert "storageStrategy" in params, "Missing parameter 'storageStrategy'"
    assert "instanceClass" in params, "Missing parameter 'instanceClass'"
    assert "validatorClass" in params, "Missing parameter 'validatorClass'"
    assert "evaluator" in params, "Missing parameter 'evaluator'"

def test_carnot::datatypetype_has_readable():
    assert hasattr(carnot::DataTypeType, "readable")
    descriptor = None
    for klass in carnot::DataTypeType.__mro__:
        if "readable" in klass.__dict__:
            descriptor = klass.__dict__["readable"]
            break
    assert isinstance(descriptor, property)

def test_carnot::datatypetype_has_valueCreator():
    assert hasattr(carnot::DataTypeType, "valueCreator")
    descriptor = None
    for klass in carnot::DataTypeType.__mro__:
        if "valueCreator" in klass.__dict__:
            descriptor = klass.__dict__["valueCreator"]
            break
    assert isinstance(descriptor, property)

def test_carnot::datatypetype_has_accessPathEditor():
    assert hasattr(carnot::DataTypeType, "accessPathEditor")
    descriptor = None
    for klass in carnot::DataTypeType.__mro__:
        if "accessPathEditor" in klass.__dict__:
            descriptor = klass.__dict__["accessPathEditor"]
            break
    assert isinstance(descriptor, property)

def test_carnot::datatypetype_has_writable():
    assert hasattr(carnot::DataTypeType, "writable")
    descriptor = None
    for klass in carnot::DataTypeType.__mro__:
        if "writable" in klass.__dict__:
            descriptor = klass.__dict__["writable"]
            break
    assert isinstance(descriptor, property)

def test_carnot::datatypetype_has_panelClass():
    assert hasattr(carnot::DataTypeType, "panelClass")
    descriptor = None
    for klass in carnot::DataTypeType.__mro__:
        if "panelClass" in klass.__dict__:
            descriptor = klass.__dict__["panelClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot::datatypetype_has_storageStrategy():
    assert hasattr(carnot::DataTypeType, "storageStrategy")
    descriptor = None
    for klass in carnot::DataTypeType.__mro__:
        if "storageStrategy" in klass.__dict__:
            descriptor = klass.__dict__["storageStrategy"]
            break
    assert isinstance(descriptor, property)

def test_carnot::datatypetype_has_instanceClass():
    assert hasattr(carnot::DataTypeType, "instanceClass")
    descriptor = None
    for klass in carnot::DataTypeType.__mro__:
        if "instanceClass" in klass.__dict__:
            descriptor = klass.__dict__["instanceClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot::datatypetype_has_validatorClass():
    assert hasattr(carnot::DataTypeType, "validatorClass")
    descriptor = None
    for klass in carnot::DataTypeType.__mro__:
        if "validatorClass" in klass.__dict__:
            descriptor = klass.__dict__["validatorClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot::datatypetype_has_evaluator():
    assert hasattr(carnot::DataTypeType, "evaluator")
    descriptor = None
    for klass in carnot::DataTypeType.__mro__:
        if "evaluator" in klass.__dict__:
            descriptor = klass.__dict__["evaluator"]
            break
    assert isinstance(descriptor, property)



def test_iflowobjectsymbol_is_not_abstract():
    assert not inspect.isabstract(IFlowObjectSymbol)


def test_iflowobjectsymbol_constructor_exists():
    assert callable(IFlowObjectSymbol.__init__)


def test_iflowobjectsymbol_constructor_args():
    sig = inspect.signature(IFlowObjectSymbol.__init__)
    params = list(sig.parameters.keys())



def test_carnot::abstracteventsymbol_is_not_abstract():
    assert not inspect.isabstract(carnot::AbstractEventSymbol)


def test_carnot::abstracteventsymbol_constructor_exists():
    assert callable(carnot::AbstractEventSymbol.__init__)


def test_carnot::abstracteventsymbol_constructor_args():
    sig = inspect.signature(carnot::AbstractEventSymbol.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_carnot::abstracteventsymbol_has_label():
    assert hasattr(carnot::AbstractEventSymbol, "label")
    descriptor = None
    for klass in carnot::AbstractEventSymbol.__mro__:
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



def test_carnot::iconnectionsymbol_is_not_abstract():
    assert not inspect.isabstract(carnot::IConnectionSymbol)


def test_carnot::iconnectionsymbol_constructor_exists():
    assert callable(carnot::IConnectionSymbol.__init__)


def test_carnot::iconnectionsymbol_constructor_args():
    sig = inspect.signature(carnot::IConnectionSymbol.__init__)
    params = list(sig.parameters.keys())
    assert "sourceAnchor" in params, "Missing parameter 'sourceAnchor'"
    assert "targetAnchor" in params, "Missing parameter 'targetAnchor'"
    assert "routing" in params, "Missing parameter 'routing'"

def test_carnot::iconnectionsymbol_has_sourceAnchor():
    assert hasattr(carnot::IConnectionSymbol, "sourceAnchor")
    descriptor = None
    for klass in carnot::IConnectionSymbol.__mro__:
        if "sourceAnchor" in klass.__dict__:
            descriptor = klass.__dict__["sourceAnchor"]
            break
    assert isinstance(descriptor, property)

def test_carnot::iconnectionsymbol_has_targetAnchor():
    assert hasattr(carnot::IConnectionSymbol, "targetAnchor")
    descriptor = None
    for klass in carnot::IConnectionSymbol.__mro__:
        if "targetAnchor" in klass.__dict__:
            descriptor = klass.__dict__["targetAnchor"]
            break
    assert isinstance(descriptor, property)

def test_carnot::iconnectionsymbol_has_routing():
    assert hasattr(carnot::IConnectionSymbol, "routing")
    descriptor = None
    for klass in carnot::IConnectionSymbol.__mro__:
        if "routing" in klass.__dict__:
            descriptor = klass.__dict__["routing"]
            break
    assert isinstance(descriptor, property)



def test_carnot::inodesymbol_is_not_abstract():
    assert not inspect.isabstract(carnot::INodeSymbol)


def test_carnot::inodesymbol_constructor_exists():
    assert callable(carnot::INodeSymbol.__init__)


def test_carnot::inodesymbol_constructor_args():
    sig = inspect.signature(carnot::INodeSymbol.__init__)
    params = list(sig.parameters.keys())
    assert "xPos" in params, "Missing parameter 'xPos'"
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"
    assert "yPos" in params, "Missing parameter 'yPos'"
    assert "shape" in params, "Missing parameter 'shape'"

def test_carnot::inodesymbol_has_xPos():
    assert hasattr(carnot::INodeSymbol, "xPos")
    descriptor = None
    for klass in carnot::INodeSymbol.__mro__:
        if "xPos" in klass.__dict__:
            descriptor = klass.__dict__["xPos"]
            break
    assert isinstance(descriptor, property)

def test_carnot::inodesymbol_has_width():
    assert hasattr(carnot::INodeSymbol, "width")
    descriptor = None
    for klass in carnot::INodeSymbol.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_carnot::inodesymbol_has_height():
    assert hasattr(carnot::INodeSymbol, "height")
    descriptor = None
    for klass in carnot::INodeSymbol.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_carnot::inodesymbol_has_yPos():
    assert hasattr(carnot::INodeSymbol, "yPos")
    descriptor = None
    for klass in carnot::INodeSymbol.__mro__:
        if "yPos" in klass.__dict__:
            descriptor = klass.__dict__["yPos"]
            break
    assert isinstance(descriptor, property)

def test_carnot::inodesymbol_has_shape():
    assert hasattr(carnot::INodeSymbol, "shape")
    descriptor = None
    for klass in carnot::INodeSymbol.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_inodesymbol_is_not_abstract():
    assert not inspect.isabstract(INodeSymbol)


def test_inodesymbol_constructor_exists():
    assert callable(INodeSymbol.__init__)


def test_inodesymbol_constructor_args():
    sig = inspect.signature(INodeSymbol.__init__)
    params = list(sig.parameters.keys())



def test_carnot::iflowobjectsymbol_is_not_abstract():
    assert not inspect.isabstract(carnot::IFlowObjectSymbol)


def test_carnot::iflowobjectsymbol_constructor_exists():
    assert callable(carnot::IFlowObjectSymbol.__init__)


def test_carnot::iflowobjectsymbol_constructor_args():
    sig = inspect.signature(carnot::IFlowObjectSymbol.__init__)
    params = list(sig.parameters.keys())



def test_carnot::imodelelementnodesymbol_is_not_abstract():
    assert not inspect.isabstract(carnot::IModelElementNodeSymbol)


def test_carnot::imodelelementnodesymbol_constructor_exists():
    assert callable(carnot::IModelElementNodeSymbol.__init__)


def test_carnot::imodelelementnodesymbol_constructor_args():
    sig = inspect.signature(carnot::IModelElementNodeSymbol.__init__)
    params = list(sig.parameters.keys())



def test_carnot::textsymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot::TextSymbolType)


def test_carnot::textsymboltype_constructor_exists():
    assert callable(carnot::TextSymbolType.__init__)


def test_carnot::textsymboltype_constructor_args():
    sig = inspect.signature(carnot::TextSymbolType.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_carnot::textsymboltype_has_text():
    assert hasattr(carnot::TextSymbolType, "text")
    descriptor = None
    for klass in carnot::TextSymbolType.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_carnot::processsymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot::ProcessSymbolType)


def test_carnot::processsymboltype_constructor_exists():
    assert callable(carnot::ProcessSymbolType.__init__)


def test_carnot::processsymboltype_constructor_args():
    sig = inspect.signature(carnot::ProcessSymbolType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::gatewaysymbol_is_not_abstract():
    assert not inspect.isabstract(carnot::GatewaySymbol)


def test_carnot::gatewaysymbol_constructor_exists():
    assert callable(carnot::GatewaySymbol.__init__)


def test_carnot::gatewaysymbol_constructor_args():
    sig = inspect.signature(carnot::GatewaySymbol.__init__)
    params = list(sig.parameters.keys())
    assert "flowKind" in params, "Missing parameter 'flowKind'"

def test_carnot::gatewaysymbol_has_flowKind():
    assert hasattr(carnot::GatewaySymbol, "flowKind")
    descriptor = None
    for klass in carnot::GatewaySymbol.__mro__:
        if "flowKind" in klass.__dict__:
            descriptor = klass.__dict__["flowKind"]
            break
    assert isinstance(descriptor, property)



def test_carnot::datasymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot::DataSymbolType)


def test_carnot::datasymboltype_constructor_exists():
    assert callable(carnot::DataSymbolType.__init__)


def test_carnot::datasymboltype_constructor_args():
    sig = inspect.signature(carnot::DataSymbolType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::modelersymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot::ModelerSymbolType)


def test_carnot::modelersymboltype_constructor_exists():
    assert callable(carnot::ModelerSymbolType.__init__)


def test_carnot::modelersymboltype_constructor_args():
    sig = inspect.signature(carnot::ModelerSymbolType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::activitysymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot::ActivitySymbolType)


def test_carnot::activitysymboltype_constructor_exists():
    assert callable(carnot::ActivitySymbolType.__init__)


def test_carnot::activitysymboltype_constructor_args():
    sig = inspect.signature(carnot::ActivitySymbolType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::itypedelement_is_not_abstract():
    assert not inspect.isabstract(carnot::ITypedElement)


def test_carnot::itypedelement_constructor_exists():
    assert callable(carnot::ITypedElement.__init__)


def test_carnot::itypedelement_constructor_args():
    sig = inspect.signature(carnot::ITypedElement.__init__)
    params = list(sig.parameters.keys())



def test_iidentifiablemodelelement_is_not_abstract():
    assert not inspect.isabstract(IIdentifiableModelElement)


def test_iidentifiablemodelelement_constructor_exists():
    assert callable(IIdentifiableModelElement.__init__)


def test_iidentifiablemodelelement_constructor_args():
    sig = inspect.signature(IIdentifiableModelElement.__init__)
    params = list(sig.parameters.keys())



def test_carnot::abstracteventaction_is_not_abstract():
    assert not inspect.isabstract(carnot::AbstractEventAction)


def test_carnot::abstracteventaction_constructor_exists():
    assert callable(carnot::AbstractEventAction.__init__)


def test_carnot::abstracteventaction_constructor_args():
    sig = inspect.signature(carnot::AbstractEventAction.__init__)
    params = list(sig.parameters.keys())



def test_carnot::transitiontype_is_not_abstract():
    assert not inspect.isabstract(carnot::TransitionType)


def test_carnot::transitiontype_constructor_exists():
    assert callable(carnot::TransitionType.__init__)


def test_carnot::transitiontype_constructor_args():
    sig = inspect.signature(carnot::TransitionType.__init__)
    params = list(sig.parameters.keys())
    assert "forkOnTraversal" in params, "Missing parameter 'forkOnTraversal'"
    assert "condition" in params, "Missing parameter 'condition'"

def test_carnot::transitiontype_has_forkOnTraversal():
    assert hasattr(carnot::TransitionType, "forkOnTraversal")
    descriptor = None
    for klass in carnot::TransitionType.__mro__:
        if "forkOnTraversal" in klass.__dict__:
            descriptor = klass.__dict__["forkOnTraversal"]
            break
    assert isinstance(descriptor, property)

def test_carnot::transitiontype_has_condition():
    assert hasattr(carnot::TransitionType, "condition")
    descriptor = None
    for klass in carnot::TransitionType.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_carnot::activitytype_is_not_abstract():
    assert not inspect.isabstract(carnot::ActivityType)


def test_carnot::activitytype_constructor_exists():
    assert callable(carnot::ActivityType.__init__)


def test_carnot::activitytype_constructor_args():
    sig = inspect.signature(carnot::ActivityType.__init__)
    params = list(sig.parameters.keys())
    assert "loopCondition" in params, "Missing parameter 'loopCondition'"
    assert "join" in params, "Missing parameter 'join'"
    assert "hibernateOnCreation" in params, "Missing parameter 'hibernateOnCreation'"
    assert "allowsAbortByPerformer" in params, "Missing parameter 'allowsAbortByPerformer'"
    assert "split" in params, "Missing parameter 'split'"
    assert "loopType" in params, "Missing parameter 'loopType'"
    assert "subProcessMode" in params, "Missing parameter 'subProcessMode'"
    assert "implementation" in params, "Missing parameter 'implementation'"

def test_carnot::activitytype_has_loopCondition():
    assert hasattr(carnot::ActivityType, "loopCondition")
    descriptor = None
    for klass in carnot::ActivityType.__mro__:
        if "loopCondition" in klass.__dict__:
            descriptor = klass.__dict__["loopCondition"]
            break
    assert isinstance(descriptor, property)

def test_carnot::activitytype_has_join():
    assert hasattr(carnot::ActivityType, "join")
    descriptor = None
    for klass in carnot::ActivityType.__mro__:
        if "join" in klass.__dict__:
            descriptor = klass.__dict__["join"]
            break
    assert isinstance(descriptor, property)

def test_carnot::activitytype_has_hibernateOnCreation():
    assert hasattr(carnot::ActivityType, "hibernateOnCreation")
    descriptor = None
    for klass in carnot::ActivityType.__mro__:
        if "hibernateOnCreation" in klass.__dict__:
            descriptor = klass.__dict__["hibernateOnCreation"]
            break
    assert isinstance(descriptor, property)

def test_carnot::activitytype_has_allowsAbortByPerformer():
    assert hasattr(carnot::ActivityType, "allowsAbortByPerformer")
    descriptor = None
    for klass in carnot::ActivityType.__mro__:
        if "allowsAbortByPerformer" in klass.__dict__:
            descriptor = klass.__dict__["allowsAbortByPerformer"]
            break
    assert isinstance(descriptor, property)

def test_carnot::activitytype_has_split():
    assert hasattr(carnot::ActivityType, "split")
    descriptor = None
    for klass in carnot::ActivityType.__mro__:
        if "split" in klass.__dict__:
            descriptor = klass.__dict__["split"]
            break
    assert isinstance(descriptor, property)

def test_carnot::activitytype_has_loopType():
    assert hasattr(carnot::ActivityType, "loopType")
    descriptor = None
    for klass in carnot::ActivityType.__mro__:
        if "loopType" in klass.__dict__:
            descriptor = klass.__dict__["loopType"]
            break
    assert isinstance(descriptor, property)

def test_carnot::activitytype_has_subProcessMode():
    assert hasattr(carnot::ActivityType, "subProcessMode")
    descriptor = None
    for klass in carnot::ActivityType.__mro__:
        if "subProcessMode" in klass.__dict__:
            descriptor = klass.__dict__["subProcessMode"]
            break
    assert isinstance(descriptor, property)

def test_carnot::activitytype_has_implementation():
    assert hasattr(carnot::ActivityType, "implementation")
    descriptor = None
    for klass in carnot::ActivityType.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)



def test_carnot::imodelparticipant_is_not_abstract():
    assert not inspect.isabstract(carnot::IModelParticipant)


def test_carnot::imodelparticipant_constructor_exists():
    assert callable(carnot::IModelParticipant.__init__)


def test_carnot::imodelparticipant_constructor_args():
    sig = inspect.signature(carnot::IModelParticipant.__init__)
    params = list(sig.parameters.keys())



def test_carnot::processdefinitiontype_is_not_abstract():
    assert not inspect.isabstract(carnot::ProcessDefinitionType)


def test_carnot::processdefinitiontype_constructor_exists():
    assert callable(carnot::ProcessDefinitionType.__init__)


def test_carnot::processdefinitiontype_constructor_args():
    sig = inspect.signature(carnot::ProcessDefinitionType.__init__)
    params = list(sig.parameters.keys())
    assert "defaultPriority" in params, "Missing parameter 'defaultPriority'"

def test_carnot::processdefinitiontype_has_defaultPriority():
    assert hasattr(carnot::ProcessDefinitionType, "defaultPriority")
    descriptor = None
    for klass in carnot::ProcessDefinitionType.__mro__:
        if "defaultPriority" in klass.__dict__:
            descriptor = klass.__dict__["defaultPriority"]
            break
    assert isinstance(descriptor, property)



def test_carnot::applicationtype_is_not_abstract():
    assert not inspect.isabstract(carnot::ApplicationType)


def test_carnot::applicationtype_constructor_exists():
    assert callable(carnot::ApplicationType.__init__)


def test_carnot::applicationtype_constructor_args():
    sig = inspect.signature(carnot::ApplicationType.__init__)
    params = list(sig.parameters.keys())
    assert "interactive" in params, "Missing parameter 'interactive'"

def test_carnot::applicationtype_has_interactive():
    assert hasattr(carnot::ApplicationType, "interactive")
    descriptor = None
    for klass in carnot::ApplicationType.__mro__:
        if "interactive" in klass.__dict__:
            descriptor = klass.__dict__["interactive"]
            break
    assert isinstance(descriptor, property)



def test_carnot::imetatype_is_not_abstract():
    assert not inspect.isabstract(carnot::IMetaType)


def test_carnot::imetatype_constructor_exists():
    assert callable(carnot::IMetaType.__init__)


def test_carnot::imetatype_constructor_args():
    sig = inspect.signature(carnot::IMetaType.__init__)
    params = list(sig.parameters.keys())
    assert "isPredefined" in params, "Missing parameter 'isPredefined'"

def test_carnot::imetatype_has_isPredefined():
    assert hasattr(carnot::IMetaType, "isPredefined")
    descriptor = None
    for klass in carnot::IMetaType.__mro__:
        if "isPredefined" in klass.__dict__:
            descriptor = klass.__dict__["isPredefined"]
            break
    assert isinstance(descriptor, property)



def test_carnot::accesspointtype_is_not_abstract():
    assert not inspect.isabstract(carnot::AccessPointType)


def test_carnot::accesspointtype_constructor_exists():
    assert callable(carnot::AccessPointType.__init__)


def test_carnot::accesspointtype_constructor_args():
    sig = inspect.signature(carnot::AccessPointType.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_carnot::accesspointtype_has_direction():
    assert hasattr(carnot::AccessPointType, "direction")
    descriptor = None
    for klass in carnot::AccessPointType.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_carnot::iaccesspointowner_is_not_abstract():
    assert not inspect.isabstract(carnot::IAccessPointOwner)


def test_carnot::iaccesspointowner_constructor_exists():
    assert callable(carnot::IAccessPointOwner.__init__)


def test_carnot::iaccesspointowner_constructor_args():
    sig = inspect.signature(carnot::IAccessPointOwner.__init__)
    params = list(sig.parameters.keys())



def test_carnot::applicationsymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot::ApplicationSymbolType)


def test_carnot::applicationsymboltype_constructor_exists():
    assert callable(carnot::ApplicationSymbolType.__init__)


def test_carnot::applicationsymboltype_constructor_args():
    sig = inspect.signature(carnot::ApplicationSymbolType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::annotationsymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot::AnnotationSymbolType)


def test_carnot::annotationsymboltype_constructor_exists():
    assert callable(carnot::AnnotationSymbolType.__init__)


def test_carnot::annotationsymboltype_constructor_args():
    sig = inspect.signature(carnot::AnnotationSymbolType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::imodelelement_is_not_abstract():
    assert not inspect.isabstract(carnot::IModelElement)


def test_carnot::imodelelement_constructor_exists():
    assert callable(carnot::IModelElement.__init__)


def test_carnot::imodelelement_constructor_args():
    sig = inspect.signature(carnot::IModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "elementOid" in params, "Missing parameter 'elementOid'"

def test_carnot::imodelelement_has_elementOid():
    assert hasattr(carnot::IModelElement, "elementOid")
    descriptor = None
    for klass in carnot::IModelElement.__mro__:
        if "elementOid" in klass.__dict__:
            descriptor = klass.__dict__["elementOid"]
            break
    assert isinstance(descriptor, property)



def test_carnot::eobject_is_not_abstract():
    assert not inspect.isabstract(carnot::EObject)


def test_carnot::eobject_constructor_exists():
    assert callable(carnot::EObject.__init__)


def test_carnot::eobject_constructor_args():
    sig = inspect.signature(carnot::EObject.__init__)
    params = list(sig.parameters.keys())



def test_carnot::identifiablereference_is_not_abstract():
    assert not inspect.isabstract(carnot::IdentifiableReference)


def test_carnot::identifiablereference_constructor_exists():
    assert callable(carnot::IdentifiableReference.__init__)


def test_carnot::identifiablereference_constructor_args():
    sig = inspect.signature(carnot::IdentifiableReference.__init__)
    params = list(sig.parameters.keys())



def test_carnot::attributetype_is_not_abstract():
    assert not inspect.isabstract(carnot::AttributeType)


def test_carnot::attributetype_constructor_exists():
    assert callable(carnot::AttributeType.__init__)


def test_carnot::attributetype_constructor_args():
    sig = inspect.signature(carnot::AttributeType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "group" in params, "Missing parameter 'group'"
    assert "any" in params, "Missing parameter 'any'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_carnot::attributetype_has_value():
    assert hasattr(carnot::AttributeType, "value")
    descriptor = None
    for klass in carnot::AttributeType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_carnot::attributetype_has_group():
    assert hasattr(carnot::AttributeType, "group")
    descriptor = None
    for klass in carnot::AttributeType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_carnot::attributetype_has_any():
    assert hasattr(carnot::AttributeType, "any")
    descriptor = None
    for klass in carnot::AttributeType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_carnot::attributetype_has_mixed():
    assert hasattr(carnot::AttributeType, "mixed")
    descriptor = None
    for klass in carnot::AttributeType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_carnot::attributetype_has_name():
    assert hasattr(carnot::AttributeType, "name")
    descriptor = None
    for klass in carnot::AttributeType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_carnot::attributetype_has_type():
    assert hasattr(carnot::AttributeType, "type")
    descriptor = None
    for klass in carnot::AttributeType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_carnot::iextensibleelement_is_not_abstract():
    assert not inspect.isabstract(carnot::IExtensibleElement)


def test_carnot::iextensibleelement_constructor_exists():
    assert callable(carnot::IExtensibleElement.__init__)


def test_carnot::iextensibleelement_constructor_args():
    sig = inspect.signature(carnot::IExtensibleElement.__init__)
    params = list(sig.parameters.keys())



def test_carnot::iidentifiableelement_is_not_abstract():
    assert not inspect.isabstract(carnot::IIdentifiableElement)


def test_carnot::iidentifiableelement_constructor_exists():
    assert callable(carnot::IIdentifiableElement.__init__)


def test_carnot::iidentifiableelement_constructor_args():
    sig = inspect.signature(carnot::IIdentifiableElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_carnot::iidentifiableelement_has_id():
    assert hasattr(carnot::IIdentifiableElement, "id")
    descriptor = None
    for klass in carnot::IIdentifiableElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_carnot::iidentifiableelement_has_name():
    assert hasattr(carnot::IIdentifiableElement, "name")
    descriptor = None
    for klass in carnot::IIdentifiableElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_carnot::eventhandlertype_is_not_abstract():
    assert not inspect.isabstract(carnot::EventHandlerType)


def test_carnot::eventhandlertype_constructor_exists():
    assert callable(carnot::EventHandlerType.__init__)


def test_carnot::eventhandlertype_constructor_args():
    sig = inspect.signature(carnot::EventHandlerType.__init__)
    params = list(sig.parameters.keys())
    assert "autoBind" in params, "Missing parameter 'autoBind'"
    assert "logHandler" in params, "Missing parameter 'logHandler'"
    assert "consumeOnMatch" in params, "Missing parameter 'consumeOnMatch'"
    assert "unbindOnMatch" in params, "Missing parameter 'unbindOnMatch'"

def test_carnot::eventhandlertype_has_autoBind():
    assert hasattr(carnot::EventHandlerType, "autoBind")
    descriptor = None
    for klass in carnot::EventHandlerType.__mro__:
        if "autoBind" in klass.__dict__:
            descriptor = klass.__dict__["autoBind"]
            break
    assert isinstance(descriptor, property)

def test_carnot::eventhandlertype_has_logHandler():
    assert hasattr(carnot::EventHandlerType, "logHandler")
    descriptor = None
    for klass in carnot::EventHandlerType.__mro__:
        if "logHandler" in klass.__dict__:
            descriptor = klass.__dict__["logHandler"]
            break
    assert isinstance(descriptor, property)

def test_carnot::eventhandlertype_has_consumeOnMatch():
    assert hasattr(carnot::EventHandlerType, "consumeOnMatch")
    descriptor = None
    for klass in carnot::EventHandlerType.__mro__:
        if "consumeOnMatch" in klass.__dict__:
            descriptor = klass.__dict__["consumeOnMatch"]
            break
    assert isinstance(descriptor, property)

def test_carnot::eventhandlertype_has_unbindOnMatch():
    assert hasattr(carnot::EventHandlerType, "unbindOnMatch")
    descriptor = None
    for klass in carnot::EventHandlerType.__mro__:
        if "unbindOnMatch" in klass.__dict__:
            descriptor = klass.__dict__["unbindOnMatch"]
            break
    assert isinstance(descriptor, property)



def test_carnot::ieventhandlerowner_is_not_abstract():
    assert not inspect.isabstract(carnot::IEventHandlerOwner)


def test_carnot::ieventhandlerowner_constructor_exists():
    assert callable(carnot::IEventHandlerOwner.__init__)


def test_carnot::ieventhandlerowner_constructor_args():
    sig = inspect.signature(carnot::IEventHandlerOwner.__init__)
    params = list(sig.parameters.keys())



def test_carnot::descriptiontype_is_not_abstract():
    assert not inspect.isabstract(carnot::DescriptionType)


def test_carnot::descriptiontype_constructor_exists():
    assert callable(carnot::DescriptionType.__init__)


def test_carnot::descriptiontype_constructor_args():
    sig = inspect.signature(carnot::DescriptionType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_carnot::descriptiontype_has_mixed():
    assert hasattr(carnot::DescriptionType, "mixed")
    descriptor = None
    for klass in carnot::DescriptionType.__mro__:
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



def test_carnot::isymbolcontainer_is_not_abstract():
    assert not inspect.isabstract(carnot::ISymbolContainer)


def test_carnot::isymbolcontainer_constructor_exists():
    assert callable(carnot::ISymbolContainer.__init__)


def test_carnot::isymbolcontainer_constructor_args():
    sig = inspect.signature(carnot::ISymbolContainer.__init__)
    params = list(sig.parameters.keys())
    assert "connections" in params, "Missing parameter 'connections'"
    assert "nodes" in params, "Missing parameter 'nodes'"

def test_carnot::isymbolcontainer_has_connections():
    assert hasattr(carnot::ISymbolContainer, "connections")
    descriptor = None
    for klass in carnot::ISymbolContainer.__mro__:
        if "connections" in klass.__dict__:
            descriptor = klass.__dict__["connections"]
            break
    assert isinstance(descriptor, property)

def test_carnot::isymbolcontainer_has_nodes():
    assert hasattr(carnot::ISymbolContainer, "nodes")
    descriptor = None
    for klass in carnot::ISymbolContainer.__mro__:
        if "nodes" in klass.__dict__:
            descriptor = klass.__dict__["nodes"]
            break
    assert isinstance(descriptor, property)



def test_iidentifiableelement_is_not_abstract():
    assert not inspect.isabstract(IIdentifiableElement)


def test_iidentifiableelement_constructor_exists():
    assert callable(IIdentifiableElement.__init__)


def test_iidentifiableelement_constructor_args():
    sig = inspect.signature(IIdentifiableElement.__init__)
    params = list(sig.parameters.keys())



def test_carnot::iswimlanesymbol_is_not_abstract():
    assert not inspect.isabstract(carnot::ISwimlaneSymbol)


def test_carnot::iswimlanesymbol_constructor_exists():
    assert callable(carnot::ISwimlaneSymbol.__init__)


def test_carnot::iswimlanesymbol_constructor_args():
    sig = inspect.signature(carnot::ISwimlaneSymbol.__init__)
    params = list(sig.parameters.keys())
    assert "collapsed" in params, "Missing parameter 'collapsed'"
    assert "orientation" in params, "Missing parameter 'orientation'"

def test_carnot::iswimlanesymbol_has_collapsed():
    assert hasattr(carnot::ISwimlaneSymbol, "collapsed")
    descriptor = None
    for klass in carnot::ISwimlaneSymbol.__mro__:
        if "collapsed" in klass.__dict__:
            descriptor = klass.__dict__["collapsed"]
            break
    assert isinstance(descriptor, property)

def test_carnot::iswimlanesymbol_has_orientation():
    assert hasattr(carnot::ISwimlaneSymbol, "orientation")
    descriptor = None
    for klass in carnot::ISwimlaneSymbol.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)



def test_imodelelement_is_not_abstract():
    assert not inspect.isabstract(IModelElement)


def test_imodelelement_constructor_exists():
    assert callable(IModelElement.__init__)


def test_imodelelement_constructor_args():
    sig = inspect.signature(IModelElement.__init__)
    params = list(sig.parameters.keys())



def test_carnot::igraphicalobject_is_not_abstract():
    assert not inspect.isabstract(carnot::IGraphicalObject)


def test_carnot::igraphicalobject_constructor_exists():
    assert callable(carnot::IGraphicalObject.__init__)


def test_carnot::igraphicalobject_constructor_args():
    sig = inspect.signature(carnot::IGraphicalObject.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "fillColor" in params, "Missing parameter 'fillColor'"
    assert "borderColor" in params, "Missing parameter 'borderColor'"

def test_carnot::igraphicalobject_has_style():
    assert hasattr(carnot::IGraphicalObject, "style")
    descriptor = None
    for klass in carnot::IGraphicalObject.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_carnot::igraphicalobject_has_fillColor():
    assert hasattr(carnot::IGraphicalObject, "fillColor")
    descriptor = None
    for klass in carnot::IGraphicalObject.__mro__:
        if "fillColor" in klass.__dict__:
            descriptor = klass.__dict__["fillColor"]
            break
    assert isinstance(descriptor, property)

def test_carnot::igraphicalobject_has_borderColor():
    assert hasattr(carnot::IGraphicalObject, "borderColor")
    descriptor = None
    for klass in carnot::IGraphicalObject.__mro__:
        if "borderColor" in klass.__dict__:
            descriptor = klass.__dict__["borderColor"]
            break
    assert isinstance(descriptor, property)



def test_carnot::datamappingtype_is_not_abstract():
    assert not inspect.isabstract(carnot::DataMappingType)


def test_carnot::datamappingtype_constructor_exists():
    assert callable(carnot::DataMappingType.__init__)


def test_carnot::datamappingtype_constructor_args():
    sig = inspect.signature(carnot::DataMappingType.__init__)
    params = list(sig.parameters.keys())
    assert "applicationAccessPoint" in params, "Missing parameter 'applicationAccessPoint'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "dataPath" in params, "Missing parameter 'dataPath'"
    assert "applicationPath" in params, "Missing parameter 'applicationPath'"
    assert "context" in params, "Missing parameter 'context'"

def test_carnot::datamappingtype_has_applicationAccessPoint():
    assert hasattr(carnot::DataMappingType, "applicationAccessPoint")
    descriptor = None
    for klass in carnot::DataMappingType.__mro__:
        if "applicationAccessPoint" in klass.__dict__:
            descriptor = klass.__dict__["applicationAccessPoint"]
            break
    assert isinstance(descriptor, property)

def test_carnot::datamappingtype_has_direction():
    assert hasattr(carnot::DataMappingType, "direction")
    descriptor = None
    for klass in carnot::DataMappingType.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_carnot::datamappingtype_has_dataPath():
    assert hasattr(carnot::DataMappingType, "dataPath")
    descriptor = None
    for klass in carnot::DataMappingType.__mro__:
        if "dataPath" in klass.__dict__:
            descriptor = klass.__dict__["dataPath"]
            break
    assert isinstance(descriptor, property)

def test_carnot::datamappingtype_has_applicationPath():
    assert hasattr(carnot::DataMappingType, "applicationPath")
    descriptor = None
    for klass in carnot::DataMappingType.__mro__:
        if "applicationPath" in klass.__dict__:
            descriptor = klass.__dict__["applicationPath"]
            break
    assert isinstance(descriptor, property)

def test_carnot::datamappingtype_has_context():
    assert hasattr(carnot::DataMappingType, "context")
    descriptor = None
    for klass in carnot::DataMappingType.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)



def test_carnot::contexttype_is_not_abstract():
    assert not inspect.isabstract(carnot::ContextType)


def test_carnot::contexttype_constructor_exists():
    assert callable(carnot::ContextType.__init__)


def test_carnot::contexttype_constructor_args():
    sig = inspect.signature(carnot::ContextType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::iidentifiablemodelelement_is_not_abstract():
    assert not inspect.isabstract(carnot::IIdentifiableModelElement)


def test_carnot::iidentifiablemodelelement_constructor_exists():
    assert callable(carnot::IIdentifiableModelElement.__init__)


def test_carnot::iidentifiablemodelelement_constructor_args():
    sig = inspect.signature(carnot::IIdentifiableModelElement.__init__)
    params = list(sig.parameters.keys())



def test_carnot::coordinates_is_not_abstract():
    assert not inspect.isabstract(carnot::Coordinates)


def test_carnot::coordinates_constructor_exists():
    assert callable(carnot::Coordinates.__init__)


def test_carnot::coordinates_constructor_args():
    sig = inspect.signature(carnot::Coordinates.__init__)
    params = list(sig.parameters.keys())
    assert "yPos" in params, "Missing parameter 'yPos'"
    assert "xPos" in params, "Missing parameter 'xPos'"

def test_carnot::coordinates_has_yPos():
    assert hasattr(carnot::Coordinates, "yPos")
    descriptor = None
    for klass in carnot::Coordinates.__mro__:
        if "yPos" in klass.__dict__:
            descriptor = klass.__dict__["yPos"]
            break
    assert isinstance(descriptor, property)

def test_carnot::coordinates_has_xPos():
    assert hasattr(carnot::Coordinates, "xPos")
    descriptor = None
    for klass in carnot::Coordinates.__mro__:
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



def test_carnot::extensions::formalparametermappingstype_is_not_abstract():
    assert not inspect.isabstract(carnot::extensions::FormalParameterMappingsType)


def test_carnot::extensions::formalparametermappingstype_constructor_exists():
    assert callable(carnot::extensions::FormalParameterMappingsType.__init__)


def test_carnot::extensions::formalparametermappingstype_constructor_args():
    sig = inspect.signature(carnot::extensions::FormalParameterMappingsType.__init__)
    params = list(sig.parameters.keys())



def test_extensions::carnot::formalparametertype_is_not_abstract():
    assert not inspect.isabstract(extensions::carnot::FormalParameterType)


def test_extensions::carnot::formalparametertype_constructor_exists():
    assert callable(extensions::carnot::FormalParameterType.__init__)


def test_extensions::carnot::formalparametertype_constructor_args():
    sig = inspect.signature(extensions::carnot::FormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_extensions::carnot::datatype_is_not_abstract():
    assert not inspect.isabstract(extensions::carnot::DataType)


def test_extensions::carnot::datatype_constructor_exists():
    assert callable(extensions::carnot::DataType.__init__)


def test_extensions::carnot::datatype_constructor_args():
    sig = inspect.signature(extensions::carnot::DataType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::extensions::formalparametermappingtype_is_not_abstract():
    assert not inspect.isabstract(carnot::extensions::FormalParameterMappingType)


def test_carnot::extensions::formalparametermappingtype_constructor_exists():
    assert callable(carnot::extensions::FormalParameterMappingType.__init__)


def test_carnot::extensions::formalparametermappingtype_constructor_args():
    sig = inspect.signature(carnot::extensions::FormalParameterMappingType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::viewabletype_is_not_abstract():
    assert not inspect.isabstract(carnot::ViewableType)


def test_carnot::viewabletype_constructor_exists():
    assert callable(carnot::ViewableType.__init__)


def test_carnot::viewabletype_constructor_args():
    sig = inspect.signature(carnot::ViewableType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::triggertype_is_not_abstract():
    assert not inspect.isabstract(carnot::TriggerType)


def test_carnot::triggertype_constructor_exists():
    assert callable(carnot::TriggerType.__init__)


def test_carnot::triggertype_constructor_args():
    sig = inspect.signature(carnot::TriggerType.__init__)
    params = list(sig.parameters.keys())



def test_formalparametermappingstype_is_not_abstract():
    assert not inspect.isabstract(FormalParameterMappingsType)


def test_formalparametermappingstype_constructor_exists():
    assert callable(FormalParameterMappingsType.__init__)


def test_formalparametermappingstype_constructor_args():
    sig = inspect.signature(FormalParameterMappingsType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::formalparameterstype_is_not_abstract():
    assert not inspect.isabstract(carnot::FormalParametersType)


def test_carnot::formalparameterstype_constructor_exists():
    assert callable(carnot::FormalParametersType.__init__)


def test_carnot::formalparameterstype_constructor_args():
    sig = inspect.signature(carnot::FormalParametersType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::viewtype_is_not_abstract():
    assert not inspect.isabstract(carnot::ViewType)


def test_carnot::viewtype_constructor_exists():
    assert callable(carnot::ViewType.__init__)


def test_carnot::viewtype_constructor_args():
    sig = inspect.signature(carnot::ViewType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_carnot::viewtype_has_name():
    assert hasattr(carnot::ViewType, "name")
    descriptor = None
    for klass in carnot::ViewType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_carnot::typedeclarationstype_is_not_abstract():
    assert not inspect.isabstract(carnot::TypeDeclarationsType)


def test_carnot::typedeclarationstype_constructor_exists():
    assert callable(carnot::TypeDeclarationsType.__init__)


def test_carnot::typedeclarationstype_constructor_args():
    sig = inspect.signature(carnot::TypeDeclarationsType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::scripttype_is_not_abstract():
    assert not inspect.isabstract(carnot::ScriptType)


def test_carnot::scripttype_constructor_exists():
    assert callable(carnot::ScriptType.__init__)


def test_carnot::scripttype_constructor_args():
    sig = inspect.signature(carnot::ScriptType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::externalpackages_is_not_abstract():
    assert not inspect.isabstract(carnot::ExternalPackages)


def test_carnot::externalpackages_constructor_exists():
    assert callable(carnot::ExternalPackages.__init__)


def test_carnot::externalpackages_constructor_args():
    sig = inspect.signature(carnot::ExternalPackages.__init__)
    params = list(sig.parameters.keys())



def test_carnot::triggertypetype_is_not_abstract():
    assert not inspect.isabstract(carnot::TriggerTypeType)


def test_carnot::triggertypetype_constructor_exists():
    assert callable(carnot::TriggerTypeType.__init__)


def test_carnot::triggertypetype_constructor_args():
    sig = inspect.signature(carnot::TriggerTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "pullTriggerEvaluator" in params, "Missing parameter 'pullTriggerEvaluator'"
    assert "pullTrigger" in params, "Missing parameter 'pullTrigger'"
    assert "panelClass" in params, "Missing parameter 'panelClass'"
    assert "rule" in params, "Missing parameter 'rule'"

def test_carnot::triggertypetype_has_pullTriggerEvaluator():
    assert hasattr(carnot::TriggerTypeType, "pullTriggerEvaluator")
    descriptor = None
    for klass in carnot::TriggerTypeType.__mro__:
        if "pullTriggerEvaluator" in klass.__dict__:
            descriptor = klass.__dict__["pullTriggerEvaluator"]
            break
    assert isinstance(descriptor, property)

def test_carnot::triggertypetype_has_pullTrigger():
    assert hasattr(carnot::TriggerTypeType, "pullTrigger")
    descriptor = None
    for klass in carnot::TriggerTypeType.__mro__:
        if "pullTrigger" in klass.__dict__:
            descriptor = klass.__dict__["pullTrigger"]
            break
    assert isinstance(descriptor, property)

def test_carnot::triggertypetype_has_panelClass():
    assert hasattr(carnot::TriggerTypeType, "panelClass")
    descriptor = None
    for klass in carnot::TriggerTypeType.__mro__:
        if "panelClass" in klass.__dict__:
            descriptor = klass.__dict__["panelClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot::triggertypetype_has_rule():
    assert hasattr(carnot::TriggerTypeType, "rule")
    descriptor = None
    for klass in carnot::TriggerTypeType.__mro__:
        if "rule" in klass.__dict__:
            descriptor = klass.__dict__["rule"]
            break
    assert isinstance(descriptor, property)



def test_carnot::qualitycontroltype_is_not_abstract():
    assert not inspect.isabstract(carnot::QualityControlType)


def test_carnot::qualitycontroltype_constructor_exists():
    assert callable(carnot::QualityControlType.__init__)


def test_carnot::qualitycontroltype_constructor_args():
    sig = inspect.signature(carnot::QualityControlType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::modelertype_is_not_abstract():
    assert not inspect.isabstract(carnot::ModelerType)


def test_carnot::modelertype_constructor_exists():
    assert callable(carnot::ModelerType.__init__)


def test_carnot::modelertype_constructor_args():
    sig = inspect.signature(carnot::ModelerType.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "password" in params, "Missing parameter 'password'"

def test_carnot::modelertype_has_email():
    assert hasattr(carnot::ModelerType, "email")
    descriptor = None
    for klass in carnot::ModelerType.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_carnot::modelertype_has_password():
    assert hasattr(carnot::ModelerType, "password")
    descriptor = None
    for klass in carnot::ModelerType.__mro__:
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



def test_carnot::linktypetype_is_not_abstract():
    assert not inspect.isabstract(carnot::LinkTypeType)


def test_carnot::linktypetype_constructor_exists():
    assert callable(carnot::LinkTypeType.__init__)


def test_carnot::linktypetype_constructor_args():
    sig = inspect.signature(carnot::LinkTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "targetSymbol" in params, "Missing parameter 'targetSymbol'"
    assert "sourceClass" in params, "Missing parameter 'sourceClass'"
    assert "sourceSymbol" in params, "Missing parameter 'sourceSymbol'"
    assert "sourceRole" in params, "Missing parameter 'sourceRole'"
    assert "lineColor" in params, "Missing parameter 'lineColor'"
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"
    assert "targetRole" in params, "Missing parameter 'targetRole'"
    assert "showRoleNames" in params, "Missing parameter 'showRoleNames'"
    assert "showLinkTypeName" in params, "Missing parameter 'showLinkTypeName'"
    assert "targetClass" in params, "Missing parameter 'targetClass'"
    assert "targetCardinality" in params, "Missing parameter 'targetCardinality'"
    assert "sourceCardinality" in params, "Missing parameter 'sourceCardinality'"

def test_carnot::linktypetype_has_targetSymbol():
    assert hasattr(carnot::LinkTypeType, "targetSymbol")
    descriptor = None
    for klass in carnot::LinkTypeType.__mro__:
        if "targetSymbol" in klass.__dict__:
            descriptor = klass.__dict__["targetSymbol"]
            break
    assert isinstance(descriptor, property)

def test_carnot::linktypetype_has_sourceClass():
    assert hasattr(carnot::LinkTypeType, "sourceClass")
    descriptor = None
    for klass in carnot::LinkTypeType.__mro__:
        if "sourceClass" in klass.__dict__:
            descriptor = klass.__dict__["sourceClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot::linktypetype_has_sourceSymbol():
    assert hasattr(carnot::LinkTypeType, "sourceSymbol")
    descriptor = None
    for klass in carnot::LinkTypeType.__mro__:
        if "sourceSymbol" in klass.__dict__:
            descriptor = klass.__dict__["sourceSymbol"]
            break
    assert isinstance(descriptor, property)

def test_carnot::linktypetype_has_sourceRole():
    assert hasattr(carnot::LinkTypeType, "sourceRole")
    descriptor = None
    for klass in carnot::LinkTypeType.__mro__:
        if "sourceRole" in klass.__dict__:
            descriptor = klass.__dict__["sourceRole"]
            break
    assert isinstance(descriptor, property)

def test_carnot::linktypetype_has_lineColor():
    assert hasattr(carnot::LinkTypeType, "lineColor")
    descriptor = None
    for klass in carnot::LinkTypeType.__mro__:
        if "lineColor" in klass.__dict__:
            descriptor = klass.__dict__["lineColor"]
            break
    assert isinstance(descriptor, property)

def test_carnot::linktypetype_has_lineStyle():
    assert hasattr(carnot::LinkTypeType, "lineStyle")
    descriptor = None
    for klass in carnot::LinkTypeType.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)

def test_carnot::linktypetype_has_targetRole():
    assert hasattr(carnot::LinkTypeType, "targetRole")
    descriptor = None
    for klass in carnot::LinkTypeType.__mro__:
        if "targetRole" in klass.__dict__:
            descriptor = klass.__dict__["targetRole"]
            break
    assert isinstance(descriptor, property)

def test_carnot::linktypetype_has_showRoleNames():
    assert hasattr(carnot::LinkTypeType, "showRoleNames")
    descriptor = None
    for klass in carnot::LinkTypeType.__mro__:
        if "showRoleNames" in klass.__dict__:
            descriptor = klass.__dict__["showRoleNames"]
            break
    assert isinstance(descriptor, property)

def test_carnot::linktypetype_has_showLinkTypeName():
    assert hasattr(carnot::LinkTypeType, "showLinkTypeName")
    descriptor = None
    for klass in carnot::LinkTypeType.__mro__:
        if "showLinkTypeName" in klass.__dict__:
            descriptor = klass.__dict__["showLinkTypeName"]
            break
    assert isinstance(descriptor, property)

def test_carnot::linktypetype_has_targetClass():
    assert hasattr(carnot::LinkTypeType, "targetClass")
    descriptor = None
    for klass in carnot::LinkTypeType.__mro__:
        if "targetClass" in klass.__dict__:
            descriptor = klass.__dict__["targetClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot::linktypetype_has_targetCardinality():
    assert hasattr(carnot::LinkTypeType, "targetCardinality")
    descriptor = None
    for klass in carnot::LinkTypeType.__mro__:
        if "targetCardinality" in klass.__dict__:
            descriptor = klass.__dict__["targetCardinality"]
            break
    assert isinstance(descriptor, property)

def test_carnot::linktypetype_has_sourceCardinality():
    assert hasattr(carnot::LinkTypeType, "sourceCardinality")
    descriptor = None
    for klass in carnot::LinkTypeType.__mro__:
        if "sourceCardinality" in klass.__dict__:
            descriptor = klass.__dict__["sourceCardinality"]
            break
    assert isinstance(descriptor, property)



def test_carnot::idrefowner_is_not_abstract():
    assert not inspect.isabstract(carnot::IdRefOwner)


def test_carnot::idrefowner_constructor_exists():
    assert callable(carnot::IdRefOwner.__init__)


def test_carnot::idrefowner_constructor_args():
    sig = inspect.signature(carnot::IdRefOwner.__init__)
    params = list(sig.parameters.keys())



def test_carnot::externalpackage_is_not_abstract():
    assert not inspect.isabstract(carnot::ExternalPackage)


def test_carnot::externalpackage_constructor_exists():
    assert callable(carnot::ExternalPackage.__init__)


def test_carnot::externalpackage_constructor_args():
    sig = inspect.signature(carnot::ExternalPackage.__init__)
    params = list(sig.parameters.keys())



def test_carnot::idref_is_not_abstract():
    assert not inspect.isabstract(carnot::IdRef)


def test_carnot::idref_constructor_exists():
    assert callable(carnot::IdRef.__init__)


def test_carnot::idref_constructor_args():
    sig = inspect.signature(carnot::IdRef.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"

def test_carnot::idref_has_ref():
    assert hasattr(carnot::IdRef, "ref")
    descriptor = None
    for klass in carnot::IdRef.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_carnot::eventconditiontypetype_is_not_abstract():
    assert not inspect.isabstract(carnot::EventConditionTypeType)


def test_carnot::eventconditiontypetype_constructor_exists():
    assert callable(carnot::EventConditionTypeType.__init__)


def test_carnot::eventconditiontypetype_constructor_args():
    sig = inspect.signature(carnot::EventConditionTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "binderClass" in params, "Missing parameter 'binderClass'"
    assert "processCondition" in params, "Missing parameter 'processCondition'"
    assert "implementation" in params, "Missing parameter 'implementation'"
    assert "activityCondition" in params, "Missing parameter 'activityCondition'"
    assert "pullEventEmitterClass" in params, "Missing parameter 'pullEventEmitterClass'"
    assert "panelClass" in params, "Missing parameter 'panelClass'"
    assert "rule" in params, "Missing parameter 'rule'"

def test_carnot::eventconditiontypetype_has_binderClass():
    assert hasattr(carnot::EventConditionTypeType, "binderClass")
    descriptor = None
    for klass in carnot::EventConditionTypeType.__mro__:
        if "binderClass" in klass.__dict__:
            descriptor = klass.__dict__["binderClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot::eventconditiontypetype_has_processCondition():
    assert hasattr(carnot::EventConditionTypeType, "processCondition")
    descriptor = None
    for klass in carnot::EventConditionTypeType.__mro__:
        if "processCondition" in klass.__dict__:
            descriptor = klass.__dict__["processCondition"]
            break
    assert isinstance(descriptor, property)

def test_carnot::eventconditiontypetype_has_implementation():
    assert hasattr(carnot::EventConditionTypeType, "implementation")
    descriptor = None
    for klass in carnot::EventConditionTypeType.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)

def test_carnot::eventconditiontypetype_has_activityCondition():
    assert hasattr(carnot::EventConditionTypeType, "activityCondition")
    descriptor = None
    for klass in carnot::EventConditionTypeType.__mro__:
        if "activityCondition" in klass.__dict__:
            descriptor = klass.__dict__["activityCondition"]
            break
    assert isinstance(descriptor, property)

def test_carnot::eventconditiontypetype_has_pullEventEmitterClass():
    assert hasattr(carnot::EventConditionTypeType, "pullEventEmitterClass")
    descriptor = None
    for klass in carnot::EventConditionTypeType.__mro__:
        if "pullEventEmitterClass" in klass.__dict__:
            descriptor = klass.__dict__["pullEventEmitterClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot::eventconditiontypetype_has_panelClass():
    assert hasattr(carnot::EventConditionTypeType, "panelClass")
    descriptor = None
    for klass in carnot::EventConditionTypeType.__mro__:
        if "panelClass" in klass.__dict__:
            descriptor = klass.__dict__["panelClass"]
            break
    assert isinstance(descriptor, property)

def test_carnot::eventconditiontypetype_has_rule():
    assert hasattr(carnot::EventConditionTypeType, "rule")
    descriptor = None
    for klass in carnot::EventConditionTypeType.__mro__:
        if "rule" in klass.__dict__:
            descriptor = klass.__dict__["rule"]
            break
    assert isinstance(descriptor, property)



def test_carnot::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(carnot::EStringToStringMapEntry)


def test_carnot::estringtostringmapentry_constructor_exists():
    assert callable(carnot::EStringToStringMapEntry.__init__)


def test_carnot::estringtostringmapentry_constructor_args():
    sig = inspect.signature(carnot::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_carnot::documentroot_is_not_abstract():
    assert not inspect.isabstract(carnot::DocumentRoot)


def test_carnot::documentroot_constructor_exists():
    assert callable(carnot::DocumentRoot.__init__)


def test_carnot::documentroot_constructor_args():
    sig = inspect.signature(carnot::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_carnot::documentroot_has_mixed():
    assert hasattr(carnot::DocumentRoot, "mixed")
    descriptor = None
    for klass in carnot::DocumentRoot.__mro__:
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



def test_carnot::publicinterfacesymbol_is_not_abstract():
    assert not inspect.isabstract(carnot::PublicInterfaceSymbol)


def test_carnot::publicinterfacesymbol_constructor_exists():
    assert callable(carnot::PublicInterfaceSymbol.__init__)


def test_carnot::publicinterfacesymbol_constructor_args():
    sig = inspect.signature(carnot::PublicInterfaceSymbol.__init__)
    params = list(sig.parameters.keys())



def test_carnot::intermediateeventsymbol_is_not_abstract():
    assert not inspect.isabstract(carnot::IntermediateEventSymbol)


def test_carnot::intermediateeventsymbol_constructor_exists():
    assert callable(carnot::IntermediateEventSymbol.__init__)


def test_carnot::intermediateeventsymbol_constructor_args():
    sig = inspect.signature(carnot::IntermediateEventSymbol.__init__)
    params = list(sig.parameters.keys())



def test_carnot::starteventsymbol_is_not_abstract():
    assert not inspect.isabstract(carnot::StartEventSymbol)


def test_carnot::starteventsymbol_constructor_exists():
    assert callable(carnot::StartEventSymbol.__init__)


def test_carnot::starteventsymbol_constructor_args():
    sig = inspect.signature(carnot::StartEventSymbol.__init__)
    params = list(sig.parameters.keys())



def test_carnot::endeventsymbol_is_not_abstract():
    assert not inspect.isabstract(carnot::EndEventSymbol)


def test_carnot::endeventsymbol_constructor_exists():
    assert callable(carnot::EndEventSymbol.__init__)


def test_carnot::endeventsymbol_constructor_args():
    sig = inspect.signature(carnot::EndEventSymbol.__init__)
    params = list(sig.parameters.keys())



def test_carnot::modeltype_is_not_abstract():
    assert not inspect.isabstract(carnot::ModelType)


def test_carnot::modeltype_constructor_exists():
    assert callable(carnot::ModelType.__init__)


def test_carnot::modeltype_constructor_args():
    sig = inspect.signature(carnot::ModelType.__init__)
    params = list(sig.parameters.keys())
    assert "vendor" in params, "Missing parameter 'vendor'"
    assert "author" in params, "Missing parameter 'author'"
    assert "carnotVersion" in params, "Missing parameter 'carnotVersion'"
    assert "modelOID" in params, "Missing parameter 'modelOID'"
    assert "created" in params, "Missing parameter 'created'"
    assert "oid" in params, "Missing parameter 'oid'"

def test_carnot::modeltype_has_vendor():
    assert hasattr(carnot::ModelType, "vendor")
    descriptor = None
    for klass in carnot::ModelType.__mro__:
        if "vendor" in klass.__dict__:
            descriptor = klass.__dict__["vendor"]
            break
    assert isinstance(descriptor, property)

def test_carnot::modeltype_has_author():
    assert hasattr(carnot::ModelType, "author")
    descriptor = None
    for klass in carnot::ModelType.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_carnot::modeltype_has_carnotVersion():
    assert hasattr(carnot::ModelType, "carnotVersion")
    descriptor = None
    for klass in carnot::ModelType.__mro__:
        if "carnotVersion" in klass.__dict__:
            descriptor = klass.__dict__["carnotVersion"]
            break
    assert isinstance(descriptor, property)

def test_carnot::modeltype_has_modelOID():
    assert hasattr(carnot::ModelType, "modelOID")
    descriptor = None
    for klass in carnot::ModelType.__mro__:
        if "modelOID" in klass.__dict__:
            descriptor = klass.__dict__["modelOID"]
            break
    assert isinstance(descriptor, property)

def test_carnot::modeltype_has_created():
    assert hasattr(carnot::ModelType, "created")
    descriptor = None
    for klass in carnot::ModelType.__mro__:
        if "created" in klass.__dict__:
            descriptor = klass.__dict__["created"]
            break
    assert isinstance(descriptor, property)

def test_carnot::modeltype_has_oid():
    assert hasattr(carnot::ModelType, "oid")
    descriptor = None
    for klass in carnot::ModelType.__mro__:
        if "oid" in klass.__dict__:
            descriptor = klass.__dict__["oid"]
            break
    assert isinstance(descriptor, property)



def test_carnot::externalreferencetype_is_not_abstract():
    assert not inspect.isabstract(carnot::ExternalReferenceType)


def test_carnot::externalreferencetype_constructor_exists():
    assert callable(carnot::ExternalReferenceType.__init__)


def test_carnot::externalreferencetype_constructor_args():
    sig = inspect.signature(carnot::ExternalReferenceType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::parametermappingtype_is_not_abstract():
    assert not inspect.isabstract(carnot::ParameterMappingType)


def test_carnot::parametermappingtype_constructor_exists():
    assert callable(carnot::ParameterMappingType.__init__)


def test_carnot::parametermappingtype_constructor_args():
    sig = inspect.signature(carnot::ParameterMappingType.__init__)
    params = list(sig.parameters.keys())
    assert "dataPath" in params, "Missing parameter 'dataPath'"
    assert "parameter" in params, "Missing parameter 'parameter'"
    assert "parameterPath" in params, "Missing parameter 'parameterPath'"

def test_carnot::parametermappingtype_has_dataPath():
    assert hasattr(carnot::ParameterMappingType, "dataPath")
    descriptor = None
    for klass in carnot::ParameterMappingType.__mro__:
        if "dataPath" in klass.__dict__:
            descriptor = klass.__dict__["dataPath"]
            break
    assert isinstance(descriptor, property)

def test_carnot::parametermappingtype_has_parameter():
    assert hasattr(carnot::ParameterMappingType, "parameter")
    descriptor = None
    for klass in carnot::ParameterMappingType.__mro__:
        if "parameter" in klass.__dict__:
            descriptor = klass.__dict__["parameter"]
            break
    assert isinstance(descriptor, property)

def test_carnot::parametermappingtype_has_parameterPath():
    assert hasattr(carnot::ParameterMappingType, "parameterPath")
    descriptor = None
    for klass in carnot::ParameterMappingType.__mro__:
        if "parameterPath" in klass.__dict__:
            descriptor = klass.__dict__["parameterPath"]
            break
    assert isinstance(descriptor, property)



def test_isymbolcontainer_is_not_abstract():
    assert not inspect.isabstract(ISymbolContainer)


def test_isymbolcontainer_constructor_exists():
    assert callable(ISymbolContainer.__init__)


def test_isymbolcontainer_constructor_args():
    sig = inspect.signature(ISymbolContainer.__init__)
    params = list(sig.parameters.keys())



def test_carnot::poolsymbol_is_not_abstract():
    assert not inspect.isabstract(carnot::PoolSymbol)


def test_carnot::poolsymbol_constructor_exists():
    assert callable(carnot::PoolSymbol.__init__)


def test_carnot::poolsymbol_constructor_args():
    sig = inspect.signature(carnot::PoolSymbol.__init__)
    params = list(sig.parameters.keys())
    assert "boundaryVisible" in params, "Missing parameter 'boundaryVisible'"

def test_carnot::poolsymbol_has_boundaryVisible():
    assert hasattr(carnot::PoolSymbol, "boundaryVisible")
    descriptor = None
    for klass in carnot::PoolSymbol.__mro__:
        if "boundaryVisible" in klass.__dict__:
            descriptor = klass.__dict__["boundaryVisible"]
            break
    assert isinstance(descriptor, property)



def test_carnot::groupsymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot::GroupSymbolType)


def test_carnot::groupsymboltype_constructor_exists():
    assert callable(carnot::GroupSymbolType.__init__)


def test_carnot::groupsymboltype_constructor_args():
    sig = inspect.signature(carnot::GroupSymbolType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::lanesymbol_is_not_abstract():
    assert not inspect.isabstract(carnot::LaneSymbol)


def test_carnot::lanesymbol_constructor_exists():
    assert callable(carnot::LaneSymbol.__init__)


def test_carnot::lanesymbol_constructor_args():
    sig = inspect.signature(carnot::LaneSymbol.__init__)
    params = list(sig.parameters.keys())



def test_carnot::diagramtype_is_not_abstract():
    assert not inspect.isabstract(carnot::DiagramType)


def test_carnot::diagramtype_constructor_exists():
    assert callable(carnot::DiagramType.__init__)


def test_carnot::diagramtype_constructor_args():
    sig = inspect.signature(carnot::DiagramType.__init__)
    params = list(sig.parameters.keys())
    assert "orientation" in params, "Missing parameter 'orientation'"
    assert "name" in params, "Missing parameter 'name'"
    assert "mode" in params, "Missing parameter 'mode'"

def test_carnot::diagramtype_has_orientation():
    assert hasattr(carnot::DiagramType, "orientation")
    descriptor = None
    for klass in carnot::DiagramType.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)

def test_carnot::diagramtype_has_name():
    assert hasattr(carnot::DiagramType, "name")
    descriptor = None
    for klass in carnot::DiagramType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_carnot::diagramtype_has_mode():
    assert hasattr(carnot::DiagramType, "mode")
    descriptor = None
    for klass in carnot::DiagramType.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_carnot::datapathtype_is_not_abstract():
    assert not inspect.isabstract(carnot::DataPathType)


def test_carnot::datapathtype_constructor_exists():
    assert callable(carnot::DataPathType.__init__)


def test_carnot::datapathtype_constructor_args():
    sig = inspect.signature(carnot::DataPathType.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "dataPath" in params, "Missing parameter 'dataPath'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "descriptor" in params, "Missing parameter 'descriptor'"

def test_carnot::datapathtype_has_key():
    assert hasattr(carnot::DataPathType, "key")
    descriptor = None
    for klass in carnot::DataPathType.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_carnot::datapathtype_has_dataPath():
    assert hasattr(carnot::DataPathType, "dataPath")
    descriptor = None
    for klass in carnot::DataPathType.__mro__:
        if "dataPath" in klass.__dict__:
            descriptor = klass.__dict__["dataPath"]
            break
    assert isinstance(descriptor, property)

def test_carnot::datapathtype_has_direction():
    assert hasattr(carnot::DataPathType, "direction")
    descriptor = None
    for klass in carnot::DataPathType.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_carnot::datapathtype_has_descriptor():
    assert hasattr(carnot::DataPathType, "descriptor")
    descriptor = None
    for klass in carnot::DataPathType.__mro__:
        if "descriptor" in klass.__dict__:
            descriptor = klass.__dict__["descriptor"]
            break
    assert isinstance(descriptor, property)



def test_iconnectionsymbol_is_not_abstract():
    assert not inspect.isabstract(IConnectionSymbol)


def test_iconnectionsymbol_constructor_exists():
    assert callable(IConnectionSymbol.__init__)


def test_iconnectionsymbol_constructor_args():
    sig = inspect.signature(IConnectionSymbol.__init__)
    params = list(sig.parameters.keys())



def test_carnot::transitionconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot::TransitionConnectionType)


def test_carnot::transitionconnectiontype_constructor_exists():
    assert callable(carnot::TransitionConnectionType.__init__)


def test_carnot::transitionconnectiontype_constructor_args():
    sig = inspect.signature(carnot::TransitionConnectionType.__init__)
    params = list(sig.parameters.keys())
    assert "points" in params, "Missing parameter 'points'"

def test_carnot::transitionconnectiontype_has_points():
    assert hasattr(carnot::TransitionConnectionType, "points")
    descriptor = None
    for klass in carnot::TransitionConnectionType.__mro__:
        if "points" in klass.__dict__:
            descriptor = klass.__dict__["points"]
            break
    assert isinstance(descriptor, property)



def test_carnot::teamleadconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot::TeamLeadConnectionType)


def test_carnot::teamleadconnectiontype_constructor_exists():
    assert callable(carnot::TeamLeadConnectionType.__init__)


def test_carnot::teamleadconnectiontype_constructor_args():
    sig = inspect.signature(carnot::TeamLeadConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::genericlinkconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot::GenericLinkConnectionType)


def test_carnot::genericlinkconnectiontype_constructor_exists():
    assert callable(carnot::GenericLinkConnectionType.__init__)


def test_carnot::genericlinkconnectiontype_constructor_args():
    sig = inspect.signature(carnot::GenericLinkConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::worksforconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot::WorksForConnectionType)


def test_carnot::worksforconnectiontype_constructor_exists():
    assert callable(carnot::WorksForConnectionType.__init__)


def test_carnot::worksforconnectiontype_constructor_args():
    sig = inspect.signature(carnot::WorksForConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::subprocessofconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot::SubProcessOfConnectionType)


def test_carnot::subprocessofconnectiontype_constructor_exists():
    assert callable(carnot::SubProcessOfConnectionType.__init__)


def test_carnot::subprocessofconnectiontype_constructor_args():
    sig = inspect.signature(carnot::SubProcessOfConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::partofconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot::PartOfConnectionType)


def test_carnot::partofconnectiontype_constructor_exists():
    assert callable(carnot::PartOfConnectionType.__init__)


def test_carnot::partofconnectiontype_constructor_args():
    sig = inspect.signature(carnot::PartOfConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::executedbyconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot::ExecutedByConnectionType)


def test_carnot::executedbyconnectiontype_constructor_exists():
    assert callable(carnot::ExecutedByConnectionType.__init__)


def test_carnot::executedbyconnectiontype_constructor_args():
    sig = inspect.signature(carnot::ExecutedByConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::referstoconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot::RefersToConnectionType)


def test_carnot::referstoconnectiontype_constructor_exists():
    assert callable(carnot::RefersToConnectionType.__init__)


def test_carnot::referstoconnectiontype_constructor_args():
    sig = inspect.signature(carnot::RefersToConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::triggersconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot::TriggersConnectionType)


def test_carnot::triggersconnectiontype_constructor_exists():
    assert callable(carnot::TriggersConnectionType.__init__)


def test_carnot::triggersconnectiontype_constructor_args():
    sig = inspect.signature(carnot::TriggersConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::performsconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot::PerformsConnectionType)


def test_carnot::performsconnectiontype_constructor_exists():
    assert callable(carnot::PerformsConnectionType.__init__)


def test_carnot::performsconnectiontype_constructor_args():
    sig = inspect.signature(carnot::PerformsConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::datamappingconnectiontype_is_not_abstract():
    assert not inspect.isabstract(carnot::DataMappingConnectionType)


def test_carnot::datamappingconnectiontype_constructor_exists():
    assert callable(carnot::DataMappingConnectionType.__init__)


def test_carnot::datamappingconnectiontype_constructor_args():
    sig = inspect.signature(carnot::DataMappingConnectionType.__init__)
    params = list(sig.parameters.keys())



def test_imodelparticipantsymbol_is_not_abstract():
    assert not inspect.isabstract(IModelParticipantSymbol)


def test_imodelparticipantsymbol_constructor_exists():
    assert callable(IModelParticipantSymbol.__init__)


def test_imodelparticipantsymbol_constructor_args():
    sig = inspect.signature(IModelParticipantSymbol.__init__)
    params = list(sig.parameters.keys())



def test_carnot::rolesymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot::RoleSymbolType)


def test_carnot::rolesymboltype_constructor_exists():
    assert callable(carnot::RoleSymbolType.__init__)


def test_carnot::rolesymboltype_constructor_args():
    sig = inspect.signature(carnot::RoleSymbolType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::organizationsymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot::OrganizationSymbolType)


def test_carnot::organizationsymboltype_constructor_exists():
    assert callable(carnot::OrganizationSymbolType.__init__)


def test_carnot::organizationsymboltype_constructor_args():
    sig = inspect.signature(carnot::OrganizationSymbolType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::conditionalperformersymboltype_is_not_abstract():
    assert not inspect.isabstract(carnot::ConditionalPerformerSymbolType)


def test_carnot::conditionalperformersymboltype_constructor_exists():
    assert callable(carnot::ConditionalPerformerSymbolType.__init__)


def test_carnot::conditionalperformersymboltype_constructor_args():
    sig = inspect.signature(carnot::ConditionalPerformerSymbolType.__init__)
    params = list(sig.parameters.keys())



def test_abstracteventaction_is_not_abstract():
    assert not inspect.isabstract(AbstractEventAction)


def test_abstracteventaction_constructor_exists():
    assert callable(AbstractEventAction.__init__)


def test_abstracteventaction_constructor_args():
    sig = inspect.signature(AbstractEventAction.__init__)
    params = list(sig.parameters.keys())



def test_carnot::eventactiontype_is_not_abstract():
    assert not inspect.isabstract(carnot::EventActionType)


def test_carnot::eventactiontype_constructor_exists():
    assert callable(carnot::EventActionType.__init__)


def test_carnot::eventactiontype_constructor_args():
    sig = inspect.signature(carnot::EventActionType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::unbindactiontype_is_not_abstract():
    assert not inspect.isabstract(carnot::UnbindActionType)


def test_carnot::unbindactiontype_constructor_exists():
    assert callable(carnot::UnbindActionType.__init__)


def test_carnot::unbindactiontype_constructor_args():
    sig = inspect.signature(carnot::UnbindActionType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::bindactiontype_is_not_abstract():
    assert not inspect.isabstract(carnot::BindActionType)


def test_carnot::bindactiontype_constructor_exists():
    assert callable(carnot::BindActionType.__init__)


def test_carnot::bindactiontype_constructor_args():
    sig = inspect.signature(carnot::BindActionType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::datatype_is_not_abstract():
    assert not inspect.isabstract(carnot::DataType)


def test_carnot::datatype_constructor_exists():
    assert callable(carnot::DataType.__init__)


def test_carnot::datatype_constructor_args():
    sig = inspect.signature(carnot::DataType.__init__)
    params = list(sig.parameters.keys())
    assert "predefined" in params, "Missing parameter 'predefined'"

def test_carnot::datatype_has_predefined():
    assert hasattr(carnot::DataType, "predefined")
    descriptor = None
    for klass in carnot::DataType.__mro__:
        if "predefined" in klass.__dict__:
            descriptor = klass.__dict__["predefined"]
            break
    assert isinstance(descriptor, property)



def test_imodelparticipant_is_not_abstract():
    assert not inspect.isabstract(IModelParticipant)


def test_imodelparticipant_constructor_exists():
    assert callable(IModelParticipant.__init__)


def test_imodelparticipant_constructor_args():
    sig = inspect.signature(IModelParticipant.__init__)
    params = list(sig.parameters.keys())



def test_carnot::organizationtype_is_not_abstract():
    assert not inspect.isabstract(carnot::OrganizationType)


def test_carnot::organizationtype_constructor_exists():
    assert callable(carnot::OrganizationType.__init__)


def test_carnot::organizationtype_constructor_args():
    sig = inspect.signature(carnot::OrganizationType.__init__)
    params = list(sig.parameters.keys())



def test_carnot::conditionalperformertype_is_not_abstract():
    assert not inspect.isabstract(carnot::ConditionalPerformerType)


def test_carnot::conditionalperformertype_constructor_exists():
    assert callable(carnot::ConditionalPerformerType.__init__)


def test_carnot::conditionalperformertype_constructor_args():
    sig = inspect.signature(carnot::ConditionalPerformerType.__init__)
    params = list(sig.parameters.keys())
    assert "dataPath" in params, "Missing parameter 'dataPath'"
    assert "isUser" in params, "Missing parameter 'isUser'"

def test_carnot::conditionalperformertype_has_dataPath():
    assert hasattr(carnot::ConditionalPerformerType, "dataPath")
    descriptor = None
    for klass in carnot::ConditionalPerformerType.__mro__:
        if "dataPath" in klass.__dict__:
            descriptor = klass.__dict__["dataPath"]
            break
    assert isinstance(descriptor, property)

def test_carnot::conditionalperformertype_has_isUser():
    assert hasattr(carnot::ConditionalPerformerType, "isUser")
    descriptor = None
    for klass in carnot::ConditionalPerformerType.__mro__:
        if "isUser" in klass.__dict__:
            descriptor = klass.__dict__["isUser"]
            break
    assert isinstance(descriptor, property)



def test_carnot::roletype_is_not_abstract():
    assert not inspect.isabstract(carnot::RoleType)


def test_carnot::roletype_constructor_exists():
    assert callable(carnot::RoleType.__init__)


def test_carnot::roletype_constructor_args():
    sig = inspect.signature(carnot::RoleType.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_carnot::roletype_has_cardinality():
    assert hasattr(carnot::RoleType, "cardinality")
    descriptor = None
    for klass in carnot::RoleType.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)

def test_linkcardinality_exists():
    # Check that the Enumeration exists
    assert LinkCardinality is not None

def test_linkcardinality_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LinkCardinality]
    expected_literals = [
        "One",
        "Unknown",
        "Many",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LinkCardinality"

def test_linkendstyle_exists():
    # Check that the Enumeration exists
    assert LinkEndStyle is not None

def test_linkendstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LinkEndStyle]
    expected_literals = [
        "FilledRhombus",
        "FilledTriangle",
        "Unknown",
        "EmptyRhombus",
        "OpenTriangle",
        "EmptyTriangle",
        "NoArrow",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LinkEndStyle"

def test_looptype_exists():
    # Check that the Enumeration exists
    assert LoopType is not None

def test_looptype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LoopType]
    expected_literals = [
        "Repeat",
        "While",
        "None_",
        "Unknown",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LoopType"

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

def test_routingtype_exists():
    # Check that the Enumeration exists
    assert RoutingType is not None

def test_routingtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RoutingType]
    expected_literals = [
        "Default",
        "ShortestPath",
        "Manhattan",
        "Explicit",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RoutingType"

def test_subprocessmodetype_exists():
    # Check that the Enumeration exists
    assert SubProcessModeType is not None

def test_subprocessmodetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SubProcessModeType]
    expected_literals = [
        "sync_shared",
        "async_separate",
        "sync_separate",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SubProcessModeType"

def test_linkcolor_exists():
    # Check that the Enumeration exists
    assert LinkColor is not None

def test_linkcolor_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LinkColor]
    expected_literals = [
        "Black",
        "Red",
        "DarkBlue",
        "Yellow",
        "LightGray",
        "Unknown",
        "Blue",
        "DarkGray",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LinkColor"

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

def test_diagrammodetype_exists():
    # Check that the Enumeration exists
    assert DiagramModeType is not None

def test_diagrammodetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DiagramModeType]
    expected_literals = [
        "MODE_4_0_0",
        "MODE_4_5_0",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DiagramModeType"

def test_flowcontroltype_exists():
    # Check that the Enumeration exists
    assert FlowControlType is not None

def test_flowcontroltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FlowControlType]
    expected_literals = [
        "split",
        "none",
        "join",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FlowControlType"

def test_activityimplementationtype_exists():
    # Check that the Enumeration exists
    assert ActivityImplementationType is not None

def test_activityimplementationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActivityImplementationType]
    expected_literals = [
        "Subprocess",
        "Manual",
        "Application",
        "Route",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActivityImplementationType"

def test_joinsplittype_exists():
    # Check that the Enumeration exists
    assert JoinSplitType is not None

def test_joinsplittype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JoinSplitType]
    expected_literals = [
        "XOR",
        "None_",
        "AND",
        "OR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JoinSplitType"

def test_linklinestyle_exists():
    # Check that the Enumeration exists
    assert LinkLineStyle is not None

def test_linklinestyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LinkLineStyle]
    expected_literals = [
        "LongStrokes",
        "ShortStrokes",
        "Unknown",
        "Normal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LinkLineStyle"

def test_directiontype_exists():
    # Check that the Enumeration exists
    assert DirectionType is not None

def test_directiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DirectionType]
    expected_literals = [
        "IN",
        "INOUT",
        "OUT",
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
carnot::XmlTextNode_strategy = st.builds(
    carnot::XmlTextNode,
    mixed=
        safe_text
)
IMetaType_strategy = st.builds(
    IMetaType,
)
carnot::ApplicationTypeType_strategy = st.builds(
    carnot::ApplicationTypeType,
    accessPointProviderClass=
        safe_text,
    instanceClass=
        safe_text,
    panelClass=
        safe_text,
    synchronous=
        safe_text,
    validatorClass=
        safe_text
)
carnot::ApplicationContextTypeType_strategy = st.builds(
    carnot::ApplicationContextTypeType,
    accessPointProviderClass=
        safe_text,
    panelClass=
        safe_text,
    hasApplicationPath=
        safe_text,
    hasMappingId=
        safe_text,
    validatorClass=
        safe_text
)
carnot::TextType_strategy = st.builds(
    carnot::TextType,
    mixed=
        safe_text
)
carnot::LoopType_strategy = st.builds(
    carnot::LoopType,
)
IAccessPointOwner_strategy = st.builds(
    IAccessPointOwner,
)
carnot::Code_strategy = st.builds(
    carnot::Code,
    code=
        safe_text,
    value=
        safe_text,
    name=
        safe_text
)
IdRefOwner_strategy = st.builds(
    IdRefOwner,
)
IEventHandlerOwner_strategy = st.builds(
    IEventHandlerOwner,
)
carnot::EventActionTypeType_strategy = st.builds(
    carnot::EventActionTypeType,
    unsupportedContexts=
        safe_text,
    activityAction=
        safe_text,
    supportedConditionTypes=
        safe_text,
    actionClass=
        safe_text,
    processAction=
        safe_text,
    panelClass=
        safe_text
)
ITypedElement_strategy = st.builds(
    ITypedElement,
)
IModelElementNodeSymbol_strategy = st.builds(
    IModelElementNodeSymbol,
)
carnot::IModelParticipantSymbol_strategy = st.builds(
    carnot::IModelParticipantSymbol,
)
carnot::ParticipantType_strategy = st.builds(
    carnot::ParticipantType,
)
carnot::DataTypeType_strategy = st.builds(
    carnot::DataTypeType,
    readable=
        safe_text,
    valueCreator=
        safe_text,
    accessPathEditor=
        safe_text,
    writable=
        safe_text,
    panelClass=
        safe_text,
    storageStrategy=
        safe_text,
    instanceClass=
        safe_text,
    validatorClass=
        safe_text,
    evaluator=
        safe_text
)
IFlowObjectSymbol_strategy = st.builds(
    IFlowObjectSymbol,
)
carnot::AbstractEventSymbol_strategy = st.builds(
    carnot::AbstractEventSymbol,
    label=
        safe_text
)
IGraphicalObject_strategy = st.builds(
    IGraphicalObject,
)
carnot::IConnectionSymbol_strategy = st.builds(
    carnot::IConnectionSymbol,
    sourceAnchor=
        safe_text,
    targetAnchor=
        safe_text,
    routing=
        safe_text
)
carnot::INodeSymbol_strategy = st.builds(
    carnot::INodeSymbol,
    xPos=
        safe_text,
    width=
        safe_text,
    height=
        safe_text,
    yPos=
        safe_text,
    shape=
        safe_text
)
INodeSymbol_strategy = st.builds(
    INodeSymbol,
)
carnot::IFlowObjectSymbol_strategy = st.builds(
    carnot::IFlowObjectSymbol,
)
carnot::IModelElementNodeSymbol_strategy = st.builds(
    carnot::IModelElementNodeSymbol,
)
carnot::TextSymbolType_strategy = st.builds(
    carnot::TextSymbolType,
    text=
        safe_text
)
carnot::ProcessSymbolType_strategy = st.builds(
    carnot::ProcessSymbolType,
)
carnot::GatewaySymbol_strategy = st.builds(
    carnot::GatewaySymbol,
    flowKind=
        safe_text
)
carnot::DataSymbolType_strategy = st.builds(
    carnot::DataSymbolType,
)
carnot::ModelerSymbolType_strategy = st.builds(
    carnot::ModelerSymbolType,
)
carnot::ActivitySymbolType_strategy = st.builds(
    carnot::ActivitySymbolType,
)
carnot::ITypedElement_strategy = st.builds(
    carnot::ITypedElement,
)
IIdentifiableModelElement_strategy = st.builds(
    IIdentifiableModelElement,
)
carnot::AbstractEventAction_strategy = st.builds(
    carnot::AbstractEventAction,
)
carnot::TransitionType_strategy = st.builds(
    carnot::TransitionType,
    forkOnTraversal=
        safe_text,
    condition=
        safe_text
)
carnot::ActivityType_strategy = st.builds(
    carnot::ActivityType,
    loopCondition=
        safe_text,
    join=
        safe_text,
    hibernateOnCreation=
        safe_text,
    allowsAbortByPerformer=
        safe_text,
    split=
        safe_text,
    loopType=
        safe_text,
    subProcessMode=
        safe_text,
    implementation=
        safe_text
)
carnot::IModelParticipant_strategy = st.builds(
    carnot::IModelParticipant,
)
carnot::ProcessDefinitionType_strategy = st.builds(
    carnot::ProcessDefinitionType,
    defaultPriority=
        safe_text
)
carnot::ApplicationType_strategy = st.builds(
    carnot::ApplicationType,
    interactive=
        safe_text
)
carnot::IMetaType_strategy = st.builds(
    carnot::IMetaType,
    isPredefined=
        safe_text
)
carnot::AccessPointType_strategy = st.builds(
    carnot::AccessPointType,
    direction=
        safe_text
)
carnot::IAccessPointOwner_strategy = st.builds(
    carnot::IAccessPointOwner,
)
carnot::ApplicationSymbolType_strategy = st.builds(
    carnot::ApplicationSymbolType,
)
carnot::AnnotationSymbolType_strategy = st.builds(
    carnot::AnnotationSymbolType,
)
carnot::IModelElement_strategy = st.builds(
    carnot::IModelElement,
    elementOid=
        safe_text
)
carnot::EObject_strategy = st.builds(
    carnot::EObject,
)
carnot::IdentifiableReference_strategy = st.builds(
    carnot::IdentifiableReference,
)
carnot::AttributeType_strategy = st.builds(
    carnot::AttributeType,
    value=
        safe_text,
    group=
        safe_text,
    any=
        safe_text,
    mixed=
        safe_text,
    name=
        safe_text,
    type=
        safe_text
)
carnot::IExtensibleElement_strategy = st.builds(
    carnot::IExtensibleElement,
)
carnot::IIdentifiableElement_strategy = st.builds(
    carnot::IIdentifiableElement,
    id=
        safe_text,
    name=
        safe_text
)
carnot::EventHandlerType_strategy = st.builds(
    carnot::EventHandlerType,
    autoBind=
        safe_text,
    logHandler=
        safe_text,
    consumeOnMatch=
        safe_text,
    unbindOnMatch=
        safe_text
)
carnot::IEventHandlerOwner_strategy = st.builds(
    carnot::IEventHandlerOwner,
)
carnot::DescriptionType_strategy = st.builds(
    carnot::DescriptionType,
    mixed=
        safe_text
)
IExtensibleElement_strategy = st.builds(
    IExtensibleElement,
)
carnot::ISymbolContainer_strategy = st.builds(
    carnot::ISymbolContainer,
    connections=
        safe_text,
    nodes=
        safe_text
)
IIdentifiableElement_strategy = st.builds(
    IIdentifiableElement,
)
carnot::ISwimlaneSymbol_strategy = st.builds(
    carnot::ISwimlaneSymbol,
    collapsed=
        safe_text,
    orientation=
        safe_text
)
IModelElement_strategy = st.builds(
    IModelElement,
)
carnot::IGraphicalObject_strategy = st.builds(
    carnot::IGraphicalObject,
    style=
        safe_text,
    fillColor=
        safe_text,
    borderColor=
        safe_text
)
carnot::DataMappingType_strategy = st.builds(
    carnot::DataMappingType,
    applicationAccessPoint=
        safe_text,
    direction=
        safe_text,
    dataPath=
        safe_text,
    applicationPath=
        safe_text,
    context=
        safe_text
)
carnot::ContextType_strategy = st.builds(
    carnot::ContextType,
)
carnot::IIdentifiableModelElement_strategy = st.builds(
    carnot::IIdentifiableModelElement,
)
carnot::Coordinates_strategy = st.builds(
    carnot::Coordinates,
    yPos=
        safe_text,
    xPos=
        safe_text
)
FormalParameterMappingType_strategy = st.builds(
    FormalParameterMappingType,
)
carnot::extensions::FormalParameterMappingsType_strategy = st.builds(
    carnot::extensions::FormalParameterMappingsType,
)
extensions::carnot::FormalParameterType_strategy = st.builds(
    extensions::carnot::FormalParameterType,
)
extensions::carnot::DataType_strategy = st.builds(
    extensions::carnot::DataType,
)
carnot::extensions::FormalParameterMappingType_strategy = st.builds(
    carnot::extensions::FormalParameterMappingType,
)
carnot::ViewableType_strategy = st.builds(
    carnot::ViewableType,
)
carnot::TriggerType_strategy = st.builds(
    carnot::TriggerType,
)
FormalParameterMappingsType_strategy = st.builds(
    FormalParameterMappingsType,
)
carnot::FormalParametersType_strategy = st.builds(
    carnot::FormalParametersType,
)
carnot::ViewType_strategy = st.builds(
    carnot::ViewType,
    name=
        safe_text
)
carnot::TypeDeclarationsType_strategy = st.builds(
    carnot::TypeDeclarationsType,
)
carnot::ScriptType_strategy = st.builds(
    carnot::ScriptType,
)
carnot::ExternalPackages_strategy = st.builds(
    carnot::ExternalPackages,
)
carnot::TriggerTypeType_strategy = st.builds(
    carnot::TriggerTypeType,
    pullTriggerEvaluator=
        safe_text,
    pullTrigger=
        safe_text,
    panelClass=
        safe_text,
    rule=
        safe_text
)
carnot::QualityControlType_strategy = st.builds(
    carnot::QualityControlType,
)
carnot::ModelerType_strategy = st.builds(
    carnot::ModelerType,
    email=
        safe_text,
    password=
        safe_text
)
ISwimlaneSymbol_strategy = st.builds(
    ISwimlaneSymbol,
)
carnot::LinkTypeType_strategy = st.builds(
    carnot::LinkTypeType,
    targetSymbol=
        safe_text,
    sourceClass=
        safe_text,
    sourceSymbol=
        safe_text,
    sourceRole=
        safe_text,
    lineColor=
        safe_text,
    lineStyle=
        safe_text,
    targetRole=
        safe_text,
    showRoleNames=
        safe_text,
    showLinkTypeName=
        safe_text,
    targetClass=
        safe_text,
    targetCardinality=
        safe_text,
    sourceCardinality=
        safe_text
)
carnot::IdRefOwner_strategy = st.builds(
    carnot::IdRefOwner,
)
carnot::ExternalPackage_strategy = st.builds(
    carnot::ExternalPackage,
)
carnot::IdRef_strategy = st.builds(
    carnot::IdRef,
    ref=
        safe_text
)
carnot::EventConditionTypeType_strategy = st.builds(
    carnot::EventConditionTypeType,
    binderClass=
        safe_text,
    processCondition=
        safe_text,
    implementation=
        safe_text,
    activityCondition=
        safe_text,
    pullEventEmitterClass=
        safe_text,
    panelClass=
        safe_text,
    rule=
        safe_text
)
carnot::EStringToStringMapEntry_strategy = st.builds(
    carnot::EStringToStringMapEntry,
)
carnot::DocumentRoot_strategy = st.builds(
    carnot::DocumentRoot,
    mixed=
        safe_text
)
AbstractEventSymbol_strategy = st.builds(
    AbstractEventSymbol,
)
carnot::PublicInterfaceSymbol_strategy = st.builds(
    carnot::PublicInterfaceSymbol,
)
carnot::IntermediateEventSymbol_strategy = st.builds(
    carnot::IntermediateEventSymbol,
)
carnot::StartEventSymbol_strategy = st.builds(
    carnot::StartEventSymbol,
)
carnot::EndEventSymbol_strategy = st.builds(
    carnot::EndEventSymbol,
)
carnot::ModelType_strategy = st.builds(
    carnot::ModelType,
    vendor=
        safe_text,
    author=
        safe_text,
    carnotVersion=
        safe_text,
    modelOID=
        safe_text,
    created=
        safe_text,
    oid=
        safe_text
)
carnot::ExternalReferenceType_strategy = st.builds(
    carnot::ExternalReferenceType,
)
carnot::ParameterMappingType_strategy = st.builds(
    carnot::ParameterMappingType,
    dataPath=
        safe_text,
    parameter=
        safe_text,
    parameterPath=
        safe_text
)
ISymbolContainer_strategy = st.builds(
    ISymbolContainer,
)
carnot::PoolSymbol_strategy = st.builds(
    carnot::PoolSymbol,
    boundaryVisible=
        safe_text
)
carnot::GroupSymbolType_strategy = st.builds(
    carnot::GroupSymbolType,
)
carnot::LaneSymbol_strategy = st.builds(
    carnot::LaneSymbol,
)
carnot::DiagramType_strategy = st.builds(
    carnot::DiagramType,
    orientation=
        safe_text,
    name=
        safe_text,
    mode=
        safe_text
)
carnot::DataPathType_strategy = st.builds(
    carnot::DataPathType,
    key=
        safe_text,
    dataPath=
        safe_text,
    direction=
        safe_text,
    descriptor=
        safe_text
)
IConnectionSymbol_strategy = st.builds(
    IConnectionSymbol,
)
carnot::TransitionConnectionType_strategy = st.builds(
    carnot::TransitionConnectionType,
    points=
        safe_text
)
carnot::TeamLeadConnectionType_strategy = st.builds(
    carnot::TeamLeadConnectionType,
)
carnot::GenericLinkConnectionType_strategy = st.builds(
    carnot::GenericLinkConnectionType,
)
carnot::WorksForConnectionType_strategy = st.builds(
    carnot::WorksForConnectionType,
)
carnot::SubProcessOfConnectionType_strategy = st.builds(
    carnot::SubProcessOfConnectionType,
)
carnot::PartOfConnectionType_strategy = st.builds(
    carnot::PartOfConnectionType,
)
carnot::ExecutedByConnectionType_strategy = st.builds(
    carnot::ExecutedByConnectionType,
)
carnot::RefersToConnectionType_strategy = st.builds(
    carnot::RefersToConnectionType,
)
carnot::TriggersConnectionType_strategy = st.builds(
    carnot::TriggersConnectionType,
)
carnot::PerformsConnectionType_strategy = st.builds(
    carnot::PerformsConnectionType,
)
carnot::DataMappingConnectionType_strategy = st.builds(
    carnot::DataMappingConnectionType,
)
IModelParticipantSymbol_strategy = st.builds(
    IModelParticipantSymbol,
)
carnot::RoleSymbolType_strategy = st.builds(
    carnot::RoleSymbolType,
)
carnot::OrganizationSymbolType_strategy = st.builds(
    carnot::OrganizationSymbolType,
)
carnot::ConditionalPerformerSymbolType_strategy = st.builds(
    carnot::ConditionalPerformerSymbolType,
)
AbstractEventAction_strategy = st.builds(
    AbstractEventAction,
)
carnot::EventActionType_strategy = st.builds(
    carnot::EventActionType,
)
carnot::UnbindActionType_strategy = st.builds(
    carnot::UnbindActionType,
)
carnot::BindActionType_strategy = st.builds(
    carnot::BindActionType,
)
carnot::DataType_strategy = st.builds(
    carnot::DataType,
    predefined=
        safe_text
)
IModelParticipant_strategy = st.builds(
    IModelParticipant,
)
carnot::OrganizationType_strategy = st.builds(
    carnot::OrganizationType,
)
carnot::ConditionalPerformerType_strategy = st.builds(
    carnot::ConditionalPerformerType,
    dataPath=
        safe_text,
    isUser=
        safe_text
)
carnot::RoleType_strategy = st.builds(
    carnot::RoleType,
    cardinality=
        st.integers()
)

@given(instance=carnot::XmlTextNode_strategy)
@settings(max_examples=50)
def test_carnot::xmltextnode_instantiation(instance):
    assert isinstance(instance, carnot::XmlTextNode)

@given(instance=carnot::XmlTextNode_strategy)
def test_carnot::xmltextnode_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=carnot::XmlTextNode_strategy)
def test_carnot::xmltextnode_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=IMetaType_strategy)
@settings(max_examples=50)
def test_imetatype_instantiation(instance):
    assert isinstance(instance, IMetaType)

@given(instance=carnot::ApplicationTypeType_strategy)
@settings(max_examples=50)
def test_carnot::applicationtypetype_instantiation(instance):
    assert isinstance(instance, carnot::ApplicationTypeType)

@given(instance=carnot::ApplicationTypeType_strategy)
def test_carnot::applicationtypetype_accessPointProviderClass_type(instance):
    assert isinstance(instance.accessPointProviderClass, str)


@given(instance=carnot::ApplicationTypeType_strategy)
def test_carnot::applicationtypetype_accessPointProviderClass_setter(instance):
    original = instance.accessPointProviderClass
    instance.accessPointProviderClass = original
    assert instance.accessPointProviderClass == original

@given(instance=carnot::ApplicationTypeType_strategy)
def test_carnot::applicationtypetype_instanceClass_type(instance):
    assert isinstance(instance.instanceClass, str)


@given(instance=carnot::ApplicationTypeType_strategy)
def test_carnot::applicationtypetype_instanceClass_setter(instance):
    original = instance.instanceClass
    instance.instanceClass = original
    assert instance.instanceClass == original

@given(instance=carnot::ApplicationTypeType_strategy)
def test_carnot::applicationtypetype_panelClass_type(instance):
    assert isinstance(instance.panelClass, str)


@given(instance=carnot::ApplicationTypeType_strategy)
def test_carnot::applicationtypetype_panelClass_setter(instance):
    original = instance.panelClass
    instance.panelClass = original
    assert instance.panelClass == original

@given(instance=carnot::ApplicationTypeType_strategy)
def test_carnot::applicationtypetype_synchronous_type(instance):
    assert isinstance(instance.synchronous, str)


@given(instance=carnot::ApplicationTypeType_strategy)
def test_carnot::applicationtypetype_synchronous_setter(instance):
    original = instance.synchronous
    instance.synchronous = original
    assert instance.synchronous == original

@given(instance=carnot::ApplicationTypeType_strategy)
def test_carnot::applicationtypetype_validatorClass_type(instance):
    assert isinstance(instance.validatorClass, str)


@given(instance=carnot::ApplicationTypeType_strategy)
def test_carnot::applicationtypetype_validatorClass_setter(instance):
    original = instance.validatorClass
    instance.validatorClass = original
    assert instance.validatorClass == original

@given(instance=carnot::ApplicationContextTypeType_strategy)
@settings(max_examples=50)
def test_carnot::applicationcontexttypetype_instantiation(instance):
    assert isinstance(instance, carnot::ApplicationContextTypeType)

@given(instance=carnot::ApplicationContextTypeType_strategy)
def test_carnot::applicationcontexttypetype_accessPointProviderClass_type(instance):
    assert isinstance(instance.accessPointProviderClass, str)


@given(instance=carnot::ApplicationContextTypeType_strategy)
def test_carnot::applicationcontexttypetype_accessPointProviderClass_setter(instance):
    original = instance.accessPointProviderClass
    instance.accessPointProviderClass = original
    assert instance.accessPointProviderClass == original

@given(instance=carnot::ApplicationContextTypeType_strategy)
def test_carnot::applicationcontexttypetype_panelClass_type(instance):
    assert isinstance(instance.panelClass, str)


@given(instance=carnot::ApplicationContextTypeType_strategy)
def test_carnot::applicationcontexttypetype_panelClass_setter(instance):
    original = instance.panelClass
    instance.panelClass = original
    assert instance.panelClass == original

@given(instance=carnot::ApplicationContextTypeType_strategy)
def test_carnot::applicationcontexttypetype_hasApplicationPath_type(instance):
    assert isinstance(instance.hasApplicationPath, str)


@given(instance=carnot::ApplicationContextTypeType_strategy)
def test_carnot::applicationcontexttypetype_hasApplicationPath_setter(instance):
    original = instance.hasApplicationPath
    instance.hasApplicationPath = original
    assert instance.hasApplicationPath == original

@given(instance=carnot::ApplicationContextTypeType_strategy)
def test_carnot::applicationcontexttypetype_hasMappingId_type(instance):
    assert isinstance(instance.hasMappingId, str)


@given(instance=carnot::ApplicationContextTypeType_strategy)
def test_carnot::applicationcontexttypetype_hasMappingId_setter(instance):
    original = instance.hasMappingId
    instance.hasMappingId = original
    assert instance.hasMappingId == original

@given(instance=carnot::ApplicationContextTypeType_strategy)
def test_carnot::applicationcontexttypetype_validatorClass_type(instance):
    assert isinstance(instance.validatorClass, str)


@given(instance=carnot::ApplicationContextTypeType_strategy)
def test_carnot::applicationcontexttypetype_validatorClass_setter(instance):
    original = instance.validatorClass
    instance.validatorClass = original
    assert instance.validatorClass == original

@given(instance=carnot::TextType_strategy)
@settings(max_examples=50)
def test_carnot::texttype_instantiation(instance):
    assert isinstance(instance, carnot::TextType)

@given(instance=carnot::TextType_strategy)
def test_carnot::texttype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=carnot::TextType_strategy)
def test_carnot::texttype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=carnot::LoopType_strategy)
@settings(max_examples=50)
def test_carnot::looptype_instantiation(instance):
    assert isinstance(instance, carnot::LoopType)

@given(instance=IAccessPointOwner_strategy)
@settings(max_examples=50)
def test_iaccesspointowner_instantiation(instance):
    assert isinstance(instance, IAccessPointOwner)

@given(instance=carnot::Code_strategy)
@settings(max_examples=50)
def test_carnot::code_instantiation(instance):
    assert isinstance(instance, carnot::Code)

@given(instance=carnot::Code_strategy)
def test_carnot::code_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=carnot::Code_strategy)
def test_carnot::code_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=carnot::Code_strategy)
def test_carnot::code_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=carnot::Code_strategy)
def test_carnot::code_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=carnot::Code_strategy)
def test_carnot::code_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=carnot::Code_strategy)
def test_carnot::code_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=IdRefOwner_strategy)
@settings(max_examples=50)
def test_idrefowner_instantiation(instance):
    assert isinstance(instance, IdRefOwner)

@given(instance=IEventHandlerOwner_strategy)
@settings(max_examples=50)
def test_ieventhandlerowner_instantiation(instance):
    assert isinstance(instance, IEventHandlerOwner)

@given(instance=carnot::EventActionTypeType_strategy)
@settings(max_examples=50)
def test_carnot::eventactiontypetype_instantiation(instance):
    assert isinstance(instance, carnot::EventActionTypeType)

@given(instance=carnot::EventActionTypeType_strategy)
def test_carnot::eventactiontypetype_unsupportedContexts_type(instance):
    assert isinstance(instance.unsupportedContexts, str)


@given(instance=carnot::EventActionTypeType_strategy)
def test_carnot::eventactiontypetype_unsupportedContexts_setter(instance):
    original = instance.unsupportedContexts
    instance.unsupportedContexts = original
    assert instance.unsupportedContexts == original

@given(instance=carnot::EventActionTypeType_strategy)
def test_carnot::eventactiontypetype_activityAction_type(instance):
    assert isinstance(instance.activityAction, str)


@given(instance=carnot::EventActionTypeType_strategy)
def test_carnot::eventactiontypetype_activityAction_setter(instance):
    original = instance.activityAction
    instance.activityAction = original
    assert instance.activityAction == original

@given(instance=carnot::EventActionTypeType_strategy)
def test_carnot::eventactiontypetype_supportedConditionTypes_type(instance):
    assert isinstance(instance.supportedConditionTypes, str)


@given(instance=carnot::EventActionTypeType_strategy)
def test_carnot::eventactiontypetype_supportedConditionTypes_setter(instance):
    original = instance.supportedConditionTypes
    instance.supportedConditionTypes = original
    assert instance.supportedConditionTypes == original

@given(instance=carnot::EventActionTypeType_strategy)
def test_carnot::eventactiontypetype_actionClass_type(instance):
    assert isinstance(instance.actionClass, str)


@given(instance=carnot::EventActionTypeType_strategy)
def test_carnot::eventactiontypetype_actionClass_setter(instance):
    original = instance.actionClass
    instance.actionClass = original
    assert instance.actionClass == original

@given(instance=carnot::EventActionTypeType_strategy)
def test_carnot::eventactiontypetype_processAction_type(instance):
    assert isinstance(instance.processAction, str)


@given(instance=carnot::EventActionTypeType_strategy)
def test_carnot::eventactiontypetype_processAction_setter(instance):
    original = instance.processAction
    instance.processAction = original
    assert instance.processAction == original

@given(instance=carnot::EventActionTypeType_strategy)
def test_carnot::eventactiontypetype_panelClass_type(instance):
    assert isinstance(instance.panelClass, str)


@given(instance=carnot::EventActionTypeType_strategy)
def test_carnot::eventactiontypetype_panelClass_setter(instance):
    original = instance.panelClass
    instance.panelClass = original
    assert instance.panelClass == original

@given(instance=ITypedElement_strategy)
@settings(max_examples=50)
def test_itypedelement_instantiation(instance):
    assert isinstance(instance, ITypedElement)

@given(instance=IModelElementNodeSymbol_strategy)
@settings(max_examples=50)
def test_imodelelementnodesymbol_instantiation(instance):
    assert isinstance(instance, IModelElementNodeSymbol)

@given(instance=carnot::IModelParticipantSymbol_strategy)
@settings(max_examples=50)
def test_carnot::imodelparticipantsymbol_instantiation(instance):
    assert isinstance(instance, carnot::IModelParticipantSymbol)

@given(instance=carnot::ParticipantType_strategy)
@settings(max_examples=50)
def test_carnot::participanttype_instantiation(instance):
    assert isinstance(instance, carnot::ParticipantType)

@given(instance=carnot::DataTypeType_strategy)
@settings(max_examples=50)
def test_carnot::datatypetype_instantiation(instance):
    assert isinstance(instance, carnot::DataTypeType)

@given(instance=carnot::DataTypeType_strategy)
def test_carnot::datatypetype_readable_type(instance):
    assert isinstance(instance.readable, str)


@given(instance=carnot::DataTypeType_strategy)
def test_carnot::datatypetype_readable_setter(instance):
    original = instance.readable
    instance.readable = original
    assert instance.readable == original

@given(instance=carnot::DataTypeType_strategy)
def test_carnot::datatypetype_valueCreator_type(instance):
    assert isinstance(instance.valueCreator, str)


@given(instance=carnot::DataTypeType_strategy)
def test_carnot::datatypetype_valueCreator_setter(instance):
    original = instance.valueCreator
    instance.valueCreator = original
    assert instance.valueCreator == original

@given(instance=carnot::DataTypeType_strategy)
def test_carnot::datatypetype_accessPathEditor_type(instance):
    assert isinstance(instance.accessPathEditor, str)


@given(instance=carnot::DataTypeType_strategy)
def test_carnot::datatypetype_accessPathEditor_setter(instance):
    original = instance.accessPathEditor
    instance.accessPathEditor = original
    assert instance.accessPathEditor == original

@given(instance=carnot::DataTypeType_strategy)
def test_carnot::datatypetype_writable_type(instance):
    assert isinstance(instance.writable, str)


@given(instance=carnot::DataTypeType_strategy)
def test_carnot::datatypetype_writable_setter(instance):
    original = instance.writable
    instance.writable = original
    assert instance.writable == original

@given(instance=carnot::DataTypeType_strategy)
def test_carnot::datatypetype_panelClass_type(instance):
    assert isinstance(instance.panelClass, str)


@given(instance=carnot::DataTypeType_strategy)
def test_carnot::datatypetype_panelClass_setter(instance):
    original = instance.panelClass
    instance.panelClass = original
    assert instance.panelClass == original

@given(instance=carnot::DataTypeType_strategy)
def test_carnot::datatypetype_storageStrategy_type(instance):
    assert isinstance(instance.storageStrategy, str)


@given(instance=carnot::DataTypeType_strategy)
def test_carnot::datatypetype_storageStrategy_setter(instance):
    original = instance.storageStrategy
    instance.storageStrategy = original
    assert instance.storageStrategy == original

@given(instance=carnot::DataTypeType_strategy)
def test_carnot::datatypetype_instanceClass_type(instance):
    assert isinstance(instance.instanceClass, str)


@given(instance=carnot::DataTypeType_strategy)
def test_carnot::datatypetype_instanceClass_setter(instance):
    original = instance.instanceClass
    instance.instanceClass = original
    assert instance.instanceClass == original

@given(instance=carnot::DataTypeType_strategy)
def test_carnot::datatypetype_validatorClass_type(instance):
    assert isinstance(instance.validatorClass, str)


@given(instance=carnot::DataTypeType_strategy)
def test_carnot::datatypetype_validatorClass_setter(instance):
    original = instance.validatorClass
    instance.validatorClass = original
    assert instance.validatorClass == original

@given(instance=carnot::DataTypeType_strategy)
def test_carnot::datatypetype_evaluator_type(instance):
    assert isinstance(instance.evaluator, str)


@given(instance=carnot::DataTypeType_strategy)
def test_carnot::datatypetype_evaluator_setter(instance):
    original = instance.evaluator
    instance.evaluator = original
    assert instance.evaluator == original

@given(instance=IFlowObjectSymbol_strategy)
@settings(max_examples=50)
def test_iflowobjectsymbol_instantiation(instance):
    assert isinstance(instance, IFlowObjectSymbol)

@given(instance=carnot::AbstractEventSymbol_strategy)
@settings(max_examples=50)
def test_carnot::abstracteventsymbol_instantiation(instance):
    assert isinstance(instance, carnot::AbstractEventSymbol)

@given(instance=carnot::AbstractEventSymbol_strategy)
def test_carnot::abstracteventsymbol_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=carnot::AbstractEventSymbol_strategy)
def test_carnot::abstracteventsymbol_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=IGraphicalObject_strategy)
@settings(max_examples=50)
def test_igraphicalobject_instantiation(instance):
    assert isinstance(instance, IGraphicalObject)

@given(instance=carnot::IConnectionSymbol_strategy)
@settings(max_examples=50)
def test_carnot::iconnectionsymbol_instantiation(instance):
    assert isinstance(instance, carnot::IConnectionSymbol)

@given(instance=carnot::IConnectionSymbol_strategy)
def test_carnot::iconnectionsymbol_sourceAnchor_type(instance):
    assert isinstance(instance.sourceAnchor, str)


@given(instance=carnot::IConnectionSymbol_strategy)
def test_carnot::iconnectionsymbol_sourceAnchor_setter(instance):
    original = instance.sourceAnchor
    instance.sourceAnchor = original
    assert instance.sourceAnchor == original

@given(instance=carnot::IConnectionSymbol_strategy)
def test_carnot::iconnectionsymbol_targetAnchor_type(instance):
    assert isinstance(instance.targetAnchor, str)


@given(instance=carnot::IConnectionSymbol_strategy)
def test_carnot::iconnectionsymbol_targetAnchor_setter(instance):
    original = instance.targetAnchor
    instance.targetAnchor = original
    assert instance.targetAnchor == original

@given(instance=carnot::IConnectionSymbol_strategy)
def test_carnot::iconnectionsymbol_routing_type(instance):
    assert isinstance(instance.routing, str)


@given(instance=carnot::IConnectionSymbol_strategy)
def test_carnot::iconnectionsymbol_routing_setter(instance):
    original = instance.routing
    instance.routing = original
    assert instance.routing == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=carnot::IConnectionSymbol_strategy)
@settings(max_examples=30)
def test_carnot::iconnectionsymbol_setsourcenode_changes_state(instance):
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
        assert has_statements, f"Function 'setSourceNode' in carnot::IConnectionSymbol is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setSourceNode' in carnot::IConnectionSymbol did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setSourceNode' in carnot::IConnectionSymbol is not implemented or raised an error")

@given(instance=carnot::INodeSymbol_strategy)
@settings(max_examples=50)
def test_carnot::inodesymbol_instantiation(instance):
    assert isinstance(instance, carnot::INodeSymbol)

@given(instance=carnot::INodeSymbol_strategy)
def test_carnot::inodesymbol_xPos_type(instance):
    assert isinstance(instance.xPos, str)


@given(instance=carnot::INodeSymbol_strategy)
def test_carnot::inodesymbol_xPos_setter(instance):
    original = instance.xPos
    instance.xPos = original
    assert instance.xPos == original

@given(instance=carnot::INodeSymbol_strategy)
def test_carnot::inodesymbol_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=carnot::INodeSymbol_strategy)
def test_carnot::inodesymbol_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=carnot::INodeSymbol_strategy)
def test_carnot::inodesymbol_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=carnot::INodeSymbol_strategy)
def test_carnot::inodesymbol_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=carnot::INodeSymbol_strategy)
def test_carnot::inodesymbol_yPos_type(instance):
    assert isinstance(instance.yPos, str)


@given(instance=carnot::INodeSymbol_strategy)
def test_carnot::inodesymbol_yPos_setter(instance):
    original = instance.yPos
    instance.yPos = original
    assert instance.yPos == original

@given(instance=carnot::INodeSymbol_strategy)
def test_carnot::inodesymbol_shape_type(instance):
    assert isinstance(instance.shape, str)


@given(instance=carnot::INodeSymbol_strategy)
def test_carnot::inodesymbol_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=INodeSymbol_strategy)
@settings(max_examples=50)
def test_inodesymbol_instantiation(instance):
    assert isinstance(instance, INodeSymbol)

@given(instance=carnot::IFlowObjectSymbol_strategy)
@settings(max_examples=50)
def test_carnot::iflowobjectsymbol_instantiation(instance):
    assert isinstance(instance, carnot::IFlowObjectSymbol)

@given(instance=carnot::IModelElementNodeSymbol_strategy)
@settings(max_examples=50)
def test_carnot::imodelelementnodesymbol_instantiation(instance):
    assert isinstance(instance, carnot::IModelElementNodeSymbol)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=carnot::IModelElementNodeSymbol_strategy)
@settings(max_examples=30)
def test_carnot::imodelelementnodesymbol_setmodelelement_changes_state(instance):
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
        assert has_statements, f"Function 'setModelElement' in carnot::IModelElementNodeSymbol is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setModelElement' in carnot::IModelElementNodeSymbol did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setModelElement' in carnot::IModelElementNodeSymbol is not implemented or raised an error")

@given(instance=carnot::TextSymbolType_strategy)
@settings(max_examples=50)
def test_carnot::textsymboltype_instantiation(instance):
    assert isinstance(instance, carnot::TextSymbolType)

@given(instance=carnot::TextSymbolType_strategy)
def test_carnot::textsymboltype_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=carnot::TextSymbolType_strategy)
def test_carnot::textsymboltype_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=carnot::ProcessSymbolType_strategy)
@settings(max_examples=50)
def test_carnot::processsymboltype_instantiation(instance):
    assert isinstance(instance, carnot::ProcessSymbolType)

@given(instance=carnot::GatewaySymbol_strategy)
@settings(max_examples=50)
def test_carnot::gatewaysymbol_instantiation(instance):
    assert isinstance(instance, carnot::GatewaySymbol)

@given(instance=carnot::GatewaySymbol_strategy)
def test_carnot::gatewaysymbol_flowKind_type(instance):
    assert isinstance(instance.flowKind, str)


@given(instance=carnot::GatewaySymbol_strategy)
def test_carnot::gatewaysymbol_flowKind_setter(instance):
    original = instance.flowKind
    instance.flowKind = original
    assert instance.flowKind == original

@given(instance=carnot::DataSymbolType_strategy)
@settings(max_examples=50)
def test_carnot::datasymboltype_instantiation(instance):
    assert isinstance(instance, carnot::DataSymbolType)

@given(instance=carnot::ModelerSymbolType_strategy)
@settings(max_examples=50)
def test_carnot::modelersymboltype_instantiation(instance):
    assert isinstance(instance, carnot::ModelerSymbolType)

@given(instance=carnot::ActivitySymbolType_strategy)
@settings(max_examples=50)
def test_carnot::activitysymboltype_instantiation(instance):
    assert isinstance(instance, carnot::ActivitySymbolType)

@given(instance=carnot::ITypedElement_strategy)
@settings(max_examples=50)
def test_carnot::itypedelement_instantiation(instance):
    assert isinstance(instance, carnot::ITypedElement)

@given(instance=IIdentifiableModelElement_strategy)
@settings(max_examples=50)
def test_iidentifiablemodelelement_instantiation(instance):
    assert isinstance(instance, IIdentifiableModelElement)

@given(instance=carnot::AbstractEventAction_strategy)
@settings(max_examples=50)
def test_carnot::abstracteventaction_instantiation(instance):
    assert isinstance(instance, carnot::AbstractEventAction)

@given(instance=carnot::TransitionType_strategy)
@settings(max_examples=50)
def test_carnot::transitiontype_instantiation(instance):
    assert isinstance(instance, carnot::TransitionType)

@given(instance=carnot::TransitionType_strategy)
def test_carnot::transitiontype_forkOnTraversal_type(instance):
    assert isinstance(instance.forkOnTraversal, str)


@given(instance=carnot::TransitionType_strategy)
def test_carnot::transitiontype_forkOnTraversal_setter(instance):
    original = instance.forkOnTraversal
    instance.forkOnTraversal = original
    assert instance.forkOnTraversal == original

@given(instance=carnot::TransitionType_strategy)
def test_carnot::transitiontype_condition_type(instance):
    assert isinstance(instance.condition, str)


@given(instance=carnot::TransitionType_strategy)
def test_carnot::transitiontype_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=carnot::ActivityType_strategy)
@settings(max_examples=50)
def test_carnot::activitytype_instantiation(instance):
    assert isinstance(instance, carnot::ActivityType)

@given(instance=carnot::ActivityType_strategy)
def test_carnot::activitytype_loopCondition_type(instance):
    assert isinstance(instance.loopCondition, str)


@given(instance=carnot::ActivityType_strategy)
def test_carnot::activitytype_loopCondition_setter(instance):
    original = instance.loopCondition
    instance.loopCondition = original
    assert instance.loopCondition == original

@given(instance=carnot::ActivityType_strategy)
def test_carnot::activitytype_join_type(instance):
    assert isinstance(instance.join, str)


@given(instance=carnot::ActivityType_strategy)
def test_carnot::activitytype_join_setter(instance):
    original = instance.join
    instance.join = original
    assert instance.join == original

@given(instance=carnot::ActivityType_strategy)
def test_carnot::activitytype_hibernateOnCreation_type(instance):
    assert isinstance(instance.hibernateOnCreation, str)


@given(instance=carnot::ActivityType_strategy)
def test_carnot::activitytype_hibernateOnCreation_setter(instance):
    original = instance.hibernateOnCreation
    instance.hibernateOnCreation = original
    assert instance.hibernateOnCreation == original

@given(instance=carnot::ActivityType_strategy)
def test_carnot::activitytype_allowsAbortByPerformer_type(instance):
    assert isinstance(instance.allowsAbortByPerformer, str)


@given(instance=carnot::ActivityType_strategy)
def test_carnot::activitytype_allowsAbortByPerformer_setter(instance):
    original = instance.allowsAbortByPerformer
    instance.allowsAbortByPerformer = original
    assert instance.allowsAbortByPerformer == original

@given(instance=carnot::ActivityType_strategy)
def test_carnot::activitytype_split_type(instance):
    assert isinstance(instance.split, str)


@given(instance=carnot::ActivityType_strategy)
def test_carnot::activitytype_split_setter(instance):
    original = instance.split
    instance.split = original
    assert instance.split == original

@given(instance=carnot::ActivityType_strategy)
def test_carnot::activitytype_loopType_type(instance):
    assert isinstance(instance.loopType, str)


@given(instance=carnot::ActivityType_strategy)
def test_carnot::activitytype_loopType_setter(instance):
    original = instance.loopType
    instance.loopType = original
    assert instance.loopType == original

@given(instance=carnot::ActivityType_strategy)
def test_carnot::activitytype_subProcessMode_type(instance):
    assert isinstance(instance.subProcessMode, str)


@given(instance=carnot::ActivityType_strategy)
def test_carnot::activitytype_subProcessMode_setter(instance):
    original = instance.subProcessMode
    instance.subProcessMode = original
    assert instance.subProcessMode == original

@given(instance=carnot::ActivityType_strategy)
def test_carnot::activitytype_implementation_type(instance):
    assert isinstance(instance.implementation, str)


@given(instance=carnot::ActivityType_strategy)
def test_carnot::activitytype_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=carnot::IModelParticipant_strategy)
@settings(max_examples=50)
def test_carnot::imodelparticipant_instantiation(instance):
    assert isinstance(instance, carnot::IModelParticipant)

@given(instance=carnot::ProcessDefinitionType_strategy)
@settings(max_examples=50)
def test_carnot::processdefinitiontype_instantiation(instance):
    assert isinstance(instance, carnot::ProcessDefinitionType)

@given(instance=carnot::ProcessDefinitionType_strategy)
def test_carnot::processdefinitiontype_defaultPriority_type(instance):
    assert isinstance(instance.defaultPriority, str)


@given(instance=carnot::ProcessDefinitionType_strategy)
def test_carnot::processdefinitiontype_defaultPriority_setter(instance):
    original = instance.defaultPriority
    instance.defaultPriority = original
    assert instance.defaultPriority == original

@given(instance=carnot::ApplicationType_strategy)
@settings(max_examples=50)
def test_carnot::applicationtype_instantiation(instance):
    assert isinstance(instance, carnot::ApplicationType)

@given(instance=carnot::ApplicationType_strategy)
def test_carnot::applicationtype_interactive_type(instance):
    assert isinstance(instance.interactive, str)


@given(instance=carnot::ApplicationType_strategy)
def test_carnot::applicationtype_interactive_setter(instance):
    original = instance.interactive
    instance.interactive = original
    assert instance.interactive == original

@given(instance=carnot::IMetaType_strategy)
@settings(max_examples=50)
def test_carnot::imetatype_instantiation(instance):
    assert isinstance(instance, carnot::IMetaType)

@given(instance=carnot::IMetaType_strategy)
def test_carnot::imetatype_isPredefined_type(instance):
    assert isinstance(instance.isPredefined, str)


@given(instance=carnot::IMetaType_strategy)
def test_carnot::imetatype_isPredefined_setter(instance):
    original = instance.isPredefined
    instance.isPredefined = original
    assert instance.isPredefined == original

@given(instance=carnot::AccessPointType_strategy)
@settings(max_examples=50)
def test_carnot::accesspointtype_instantiation(instance):
    assert isinstance(instance, carnot::AccessPointType)

@given(instance=carnot::AccessPointType_strategy)
def test_carnot::accesspointtype_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=carnot::AccessPointType_strategy)
def test_carnot::accesspointtype_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=carnot::IAccessPointOwner_strategy)
@settings(max_examples=50)
def test_carnot::iaccesspointowner_instantiation(instance):
    assert isinstance(instance, carnot::IAccessPointOwner)

@given(instance=carnot::ApplicationSymbolType_strategy)
@settings(max_examples=50)
def test_carnot::applicationsymboltype_instantiation(instance):
    assert isinstance(instance, carnot::ApplicationSymbolType)

@given(instance=carnot::AnnotationSymbolType_strategy)
@settings(max_examples=50)
def test_carnot::annotationsymboltype_instantiation(instance):
    assert isinstance(instance, carnot::AnnotationSymbolType)

@given(instance=carnot::IModelElement_strategy)
@settings(max_examples=50)
def test_carnot::imodelelement_instantiation(instance):
    assert isinstance(instance, carnot::IModelElement)

@given(instance=carnot::IModelElement_strategy)
def test_carnot::imodelelement_elementOid_type(instance):
    assert isinstance(instance.elementOid, str)


@given(instance=carnot::IModelElement_strategy)
def test_carnot::imodelelement_elementOid_setter(instance):
    original = instance.elementOid
    instance.elementOid = original
    assert instance.elementOid == original

@given(instance=carnot::EObject_strategy)
@settings(max_examples=50)
def test_carnot::eobject_instantiation(instance):
    assert isinstance(instance, carnot::EObject)

@given(instance=carnot::IdentifiableReference_strategy)
@settings(max_examples=50)
def test_carnot::identifiablereference_instantiation(instance):
    assert isinstance(instance, carnot::IdentifiableReference)

@given(instance=carnot::AttributeType_strategy)
@settings(max_examples=50)
def test_carnot::attributetype_instantiation(instance):
    assert isinstance(instance, carnot::AttributeType)

@given(instance=carnot::AttributeType_strategy)
def test_carnot::attributetype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=carnot::AttributeType_strategy)
def test_carnot::attributetype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=carnot::AttributeType_strategy)
def test_carnot::attributetype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=carnot::AttributeType_strategy)
def test_carnot::attributetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=carnot::AttributeType_strategy)
def test_carnot::attributetype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=carnot::AttributeType_strategy)
def test_carnot::attributetype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=carnot::AttributeType_strategy)
def test_carnot::attributetype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=carnot::AttributeType_strategy)
def test_carnot::attributetype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=carnot::AttributeType_strategy)
def test_carnot::attributetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=carnot::AttributeType_strategy)
def test_carnot::attributetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=carnot::AttributeType_strategy)
def test_carnot::attributetype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=carnot::AttributeType_strategy)
def test_carnot::attributetype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=carnot::AttributeType_strategy)
@settings(max_examples=30)
def test_carnot::attributetype_setattributevalue_changes_state(instance):
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
        assert has_statements, f"Function 'setAttributeValue' in carnot::AttributeType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setAttributeValue' in carnot::AttributeType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setAttributeValue' in carnot::AttributeType is not implemented or raised an error")

@given(instance=carnot::IExtensibleElement_strategy)
@settings(max_examples=50)
def test_carnot::iextensibleelement_instantiation(instance):
    assert isinstance(instance, carnot::IExtensibleElement)

@given(instance=carnot::IIdentifiableElement_strategy)
@settings(max_examples=50)
def test_carnot::iidentifiableelement_instantiation(instance):
    assert isinstance(instance, carnot::IIdentifiableElement)

@given(instance=carnot::IIdentifiableElement_strategy)
def test_carnot::iidentifiableelement_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=carnot::IIdentifiableElement_strategy)
def test_carnot::iidentifiableelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=carnot::IIdentifiableElement_strategy)
def test_carnot::iidentifiableelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=carnot::IIdentifiableElement_strategy)
def test_carnot::iidentifiableelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=carnot::EventHandlerType_strategy)
@settings(max_examples=50)
def test_carnot::eventhandlertype_instantiation(instance):
    assert isinstance(instance, carnot::EventHandlerType)

@given(instance=carnot::EventHandlerType_strategy)
def test_carnot::eventhandlertype_autoBind_type(instance):
    assert isinstance(instance.autoBind, str)


@given(instance=carnot::EventHandlerType_strategy)
def test_carnot::eventhandlertype_autoBind_setter(instance):
    original = instance.autoBind
    instance.autoBind = original
    assert instance.autoBind == original

@given(instance=carnot::EventHandlerType_strategy)
def test_carnot::eventhandlertype_logHandler_type(instance):
    assert isinstance(instance.logHandler, str)


@given(instance=carnot::EventHandlerType_strategy)
def test_carnot::eventhandlertype_logHandler_setter(instance):
    original = instance.logHandler
    instance.logHandler = original
    assert instance.logHandler == original

@given(instance=carnot::EventHandlerType_strategy)
def test_carnot::eventhandlertype_consumeOnMatch_type(instance):
    assert isinstance(instance.consumeOnMatch, str)


@given(instance=carnot::EventHandlerType_strategy)
def test_carnot::eventhandlertype_consumeOnMatch_setter(instance):
    original = instance.consumeOnMatch
    instance.consumeOnMatch = original
    assert instance.consumeOnMatch == original

@given(instance=carnot::EventHandlerType_strategy)
def test_carnot::eventhandlertype_unbindOnMatch_type(instance):
    assert isinstance(instance.unbindOnMatch, str)


@given(instance=carnot::EventHandlerType_strategy)
def test_carnot::eventhandlertype_unbindOnMatch_setter(instance):
    original = instance.unbindOnMatch
    instance.unbindOnMatch = original
    assert instance.unbindOnMatch == original

@given(instance=carnot::IEventHandlerOwner_strategy)
@settings(max_examples=50)
def test_carnot::ieventhandlerowner_instantiation(instance):
    assert isinstance(instance, carnot::IEventHandlerOwner)

@given(instance=carnot::DescriptionType_strategy)
@settings(max_examples=50)
def test_carnot::descriptiontype_instantiation(instance):
    assert isinstance(instance, carnot::DescriptionType)

@given(instance=carnot::DescriptionType_strategy)
def test_carnot::descriptiontype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=carnot::DescriptionType_strategy)
def test_carnot::descriptiontype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=IExtensibleElement_strategy)
@settings(max_examples=50)
def test_iextensibleelement_instantiation(instance):
    assert isinstance(instance, IExtensibleElement)

@given(instance=carnot::ISymbolContainer_strategy)
@settings(max_examples=50)
def test_carnot::isymbolcontainer_instantiation(instance):
    assert isinstance(instance, carnot::ISymbolContainer)

@given(instance=carnot::ISymbolContainer_strategy)
def test_carnot::isymbolcontainer_connections_type(instance):
    assert isinstance(instance.connections, str)


@given(instance=carnot::ISymbolContainer_strategy)
def test_carnot::isymbolcontainer_connections_setter(instance):
    original = instance.connections
    instance.connections = original
    assert instance.connections == original

@given(instance=carnot::ISymbolContainer_strategy)
def test_carnot::isymbolcontainer_nodes_type(instance):
    assert isinstance(instance.nodes, str)


@given(instance=carnot::ISymbolContainer_strategy)
def test_carnot::isymbolcontainer_nodes_setter(instance):
    original = instance.nodes
    instance.nodes = original
    assert instance.nodes == original

@given(instance=IIdentifiableElement_strategy)
@settings(max_examples=50)
def test_iidentifiableelement_instantiation(instance):
    assert isinstance(instance, IIdentifiableElement)

@given(instance=carnot::ISwimlaneSymbol_strategy)
@settings(max_examples=50)
def test_carnot::iswimlanesymbol_instantiation(instance):
    assert isinstance(instance, carnot::ISwimlaneSymbol)

@given(instance=carnot::ISwimlaneSymbol_strategy)
def test_carnot::iswimlanesymbol_collapsed_type(instance):
    assert isinstance(instance.collapsed, str)


@given(instance=carnot::ISwimlaneSymbol_strategy)
def test_carnot::iswimlanesymbol_collapsed_setter(instance):
    original = instance.collapsed
    instance.collapsed = original
    assert instance.collapsed == original

@given(instance=carnot::ISwimlaneSymbol_strategy)
def test_carnot::iswimlanesymbol_orientation_type(instance):
    assert isinstance(instance.orientation, str)


@given(instance=carnot::ISwimlaneSymbol_strategy)
def test_carnot::iswimlanesymbol_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original

@given(instance=IModelElement_strategy)
@settings(max_examples=50)
def test_imodelelement_instantiation(instance):
    assert isinstance(instance, IModelElement)

@given(instance=carnot::IGraphicalObject_strategy)
@settings(max_examples=50)
def test_carnot::igraphicalobject_instantiation(instance):
    assert isinstance(instance, carnot::IGraphicalObject)

@given(instance=carnot::IGraphicalObject_strategy)
def test_carnot::igraphicalobject_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=carnot::IGraphicalObject_strategy)
def test_carnot::igraphicalobject_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=carnot::IGraphicalObject_strategy)
def test_carnot::igraphicalobject_fillColor_type(instance):
    assert isinstance(instance.fillColor, str)


@given(instance=carnot::IGraphicalObject_strategy)
def test_carnot::igraphicalobject_fillColor_setter(instance):
    original = instance.fillColor
    instance.fillColor = original
    assert instance.fillColor == original

@given(instance=carnot::IGraphicalObject_strategy)
def test_carnot::igraphicalobject_borderColor_type(instance):
    assert isinstance(instance.borderColor, str)


@given(instance=carnot::IGraphicalObject_strategy)
def test_carnot::igraphicalobject_borderColor_setter(instance):
    original = instance.borderColor
    instance.borderColor = original
    assert instance.borderColor == original

@given(instance=carnot::DataMappingType_strategy)
@settings(max_examples=50)
def test_carnot::datamappingtype_instantiation(instance):
    assert isinstance(instance, carnot::DataMappingType)

@given(instance=carnot::DataMappingType_strategy)
def test_carnot::datamappingtype_applicationAccessPoint_type(instance):
    assert isinstance(instance.applicationAccessPoint, str)


@given(instance=carnot::DataMappingType_strategy)
def test_carnot::datamappingtype_applicationAccessPoint_setter(instance):
    original = instance.applicationAccessPoint
    instance.applicationAccessPoint = original
    assert instance.applicationAccessPoint == original

@given(instance=carnot::DataMappingType_strategy)
def test_carnot::datamappingtype_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=carnot::DataMappingType_strategy)
def test_carnot::datamappingtype_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=carnot::DataMappingType_strategy)
def test_carnot::datamappingtype_dataPath_type(instance):
    assert isinstance(instance.dataPath, str)


@given(instance=carnot::DataMappingType_strategy)
def test_carnot::datamappingtype_dataPath_setter(instance):
    original = instance.dataPath
    instance.dataPath = original
    assert instance.dataPath == original

@given(instance=carnot::DataMappingType_strategy)
def test_carnot::datamappingtype_applicationPath_type(instance):
    assert isinstance(instance.applicationPath, str)


@given(instance=carnot::DataMappingType_strategy)
def test_carnot::datamappingtype_applicationPath_setter(instance):
    original = instance.applicationPath
    instance.applicationPath = original
    assert instance.applicationPath == original

@given(instance=carnot::DataMappingType_strategy)
def test_carnot::datamappingtype_context_type(instance):
    assert isinstance(instance.context, str)


@given(instance=carnot::DataMappingType_strategy)
def test_carnot::datamappingtype_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original

@given(instance=carnot::ContextType_strategy)
@settings(max_examples=50)
def test_carnot::contexttype_instantiation(instance):
    assert isinstance(instance, carnot::ContextType)

@given(instance=carnot::IIdentifiableModelElement_strategy)
@settings(max_examples=50)
def test_carnot::iidentifiablemodelelement_instantiation(instance):
    assert isinstance(instance, carnot::IIdentifiableModelElement)

@given(instance=carnot::Coordinates_strategy)
@settings(max_examples=50)
def test_carnot::coordinates_instantiation(instance):
    assert isinstance(instance, carnot::Coordinates)

@given(instance=carnot::Coordinates_strategy)
def test_carnot::coordinates_yPos_type(instance):
    assert isinstance(instance.yPos, str)


@given(instance=carnot::Coordinates_strategy)
def test_carnot::coordinates_yPos_setter(instance):
    original = instance.yPos
    instance.yPos = original
    assert instance.yPos == original

@given(instance=carnot::Coordinates_strategy)
def test_carnot::coordinates_xPos_type(instance):
    assert isinstance(instance.xPos, str)


@given(instance=carnot::Coordinates_strategy)
def test_carnot::coordinates_xPos_setter(instance):
    original = instance.xPos
    instance.xPos = original
    assert instance.xPos == original

@given(instance=FormalParameterMappingType_strategy)
@settings(max_examples=50)
def test_formalparametermappingtype_instantiation(instance):
    assert isinstance(instance, FormalParameterMappingType)

@given(instance=carnot::extensions::FormalParameterMappingsType_strategy)
@settings(max_examples=50)
def test_carnot::extensions::formalparametermappingstype_instantiation(instance):
    assert isinstance(instance, carnot::extensions::FormalParameterMappingsType)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=carnot::extensions::FormalParameterMappingsType_strategy)
@settings(max_examples=30)
def test_carnot::extensions::formalparametermappingstype_setmappeddata_changes_state(instance):
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
        assert has_statements, f"Function 'setMappedData' in carnot::extensions::FormalParameterMappingsType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setMappedData' in carnot::extensions::FormalParameterMappingsType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setMappedData' in carnot::extensions::FormalParameterMappingsType is not implemented or raised an error")

@given(instance=extensions::carnot::FormalParameterType_strategy)
@settings(max_examples=50)
def test_extensions::carnot::formalparametertype_instantiation(instance):
    assert isinstance(instance, extensions::carnot::FormalParameterType)

@given(instance=extensions::carnot::DataType_strategy)
@settings(max_examples=50)
def test_extensions::carnot::datatype_instantiation(instance):
    assert isinstance(instance, extensions::carnot::DataType)

@given(instance=carnot::extensions::FormalParameterMappingType_strategy)
@settings(max_examples=50)
def test_carnot::extensions::formalparametermappingtype_instantiation(instance):
    assert isinstance(instance, carnot::extensions::FormalParameterMappingType)

@given(instance=carnot::ViewableType_strategy)
@settings(max_examples=50)
def test_carnot::viewabletype_instantiation(instance):
    assert isinstance(instance, carnot::ViewableType)

@given(instance=carnot::TriggerType_strategy)
@settings(max_examples=50)
def test_carnot::triggertype_instantiation(instance):
    assert isinstance(instance, carnot::TriggerType)

@given(instance=FormalParameterMappingsType_strategy)
@settings(max_examples=50)
def test_formalparametermappingstype_instantiation(instance):
    assert isinstance(instance, FormalParameterMappingsType)

@given(instance=carnot::FormalParametersType_strategy)
@settings(max_examples=50)
def test_carnot::formalparameterstype_instantiation(instance):
    assert isinstance(instance, carnot::FormalParametersType)

@given(instance=carnot::ViewType_strategy)
@settings(max_examples=50)
def test_carnot::viewtype_instantiation(instance):
    assert isinstance(instance, carnot::ViewType)

@given(instance=carnot::ViewType_strategy)
def test_carnot::viewtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=carnot::ViewType_strategy)
def test_carnot::viewtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=carnot::TypeDeclarationsType_strategy)
@settings(max_examples=50)
def test_carnot::typedeclarationstype_instantiation(instance):
    assert isinstance(instance, carnot::TypeDeclarationsType)

@given(instance=carnot::ScriptType_strategy)
@settings(max_examples=50)
def test_carnot::scripttype_instantiation(instance):
    assert isinstance(instance, carnot::ScriptType)

@given(instance=carnot::ExternalPackages_strategy)
@settings(max_examples=50)
def test_carnot::externalpackages_instantiation(instance):
    assert isinstance(instance, carnot::ExternalPackages)

@given(instance=carnot::TriggerTypeType_strategy)
@settings(max_examples=50)
def test_carnot::triggertypetype_instantiation(instance):
    assert isinstance(instance, carnot::TriggerTypeType)

@given(instance=carnot::TriggerTypeType_strategy)
def test_carnot::triggertypetype_pullTriggerEvaluator_type(instance):
    assert isinstance(instance.pullTriggerEvaluator, str)


@given(instance=carnot::TriggerTypeType_strategy)
def test_carnot::triggertypetype_pullTriggerEvaluator_setter(instance):
    original = instance.pullTriggerEvaluator
    instance.pullTriggerEvaluator = original
    assert instance.pullTriggerEvaluator == original

@given(instance=carnot::TriggerTypeType_strategy)
def test_carnot::triggertypetype_pullTrigger_type(instance):
    assert isinstance(instance.pullTrigger, str)


@given(instance=carnot::TriggerTypeType_strategy)
def test_carnot::triggertypetype_pullTrigger_setter(instance):
    original = instance.pullTrigger
    instance.pullTrigger = original
    assert instance.pullTrigger == original

@given(instance=carnot::TriggerTypeType_strategy)
def test_carnot::triggertypetype_panelClass_type(instance):
    assert isinstance(instance.panelClass, str)


@given(instance=carnot::TriggerTypeType_strategy)
def test_carnot::triggertypetype_panelClass_setter(instance):
    original = instance.panelClass
    instance.panelClass = original
    assert instance.panelClass == original

@given(instance=carnot::TriggerTypeType_strategy)
def test_carnot::triggertypetype_rule_type(instance):
    assert isinstance(instance.rule, str)


@given(instance=carnot::TriggerTypeType_strategy)
def test_carnot::triggertypetype_rule_setter(instance):
    original = instance.rule
    instance.rule = original
    assert instance.rule == original

@given(instance=carnot::QualityControlType_strategy)
@settings(max_examples=50)
def test_carnot::qualitycontroltype_instantiation(instance):
    assert isinstance(instance, carnot::QualityControlType)

@given(instance=carnot::ModelerType_strategy)
@settings(max_examples=50)
def test_carnot::modelertype_instantiation(instance):
    assert isinstance(instance, carnot::ModelerType)

@given(instance=carnot::ModelerType_strategy)
def test_carnot::modelertype_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=carnot::ModelerType_strategy)
def test_carnot::modelertype_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=carnot::ModelerType_strategy)
def test_carnot::modelertype_password_type(instance):
    assert isinstance(instance.password, str)


@given(instance=carnot::ModelerType_strategy)
def test_carnot::modelertype_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=ISwimlaneSymbol_strategy)
@settings(max_examples=50)
def test_iswimlanesymbol_instantiation(instance):
    assert isinstance(instance, ISwimlaneSymbol)

@given(instance=carnot::LinkTypeType_strategy)
@settings(max_examples=50)
def test_carnot::linktypetype_instantiation(instance):
    assert isinstance(instance, carnot::LinkTypeType)

@given(instance=carnot::LinkTypeType_strategy)
def test_carnot::linktypetype_targetSymbol_type(instance):
    assert isinstance(instance.targetSymbol, str)


@given(instance=carnot::LinkTypeType_strategy)
def test_carnot::linktypetype_targetSymbol_setter(instance):
    original = instance.targetSymbol
    instance.targetSymbol = original
    assert instance.targetSymbol == original

@given(instance=carnot::LinkTypeType_strategy)
def test_carnot::linktypetype_sourceClass_type(instance):
    assert isinstance(instance.sourceClass, str)


@given(instance=carnot::LinkTypeType_strategy)
def test_carnot::linktypetype_sourceClass_setter(instance):
    original = instance.sourceClass
    instance.sourceClass = original
    assert instance.sourceClass == original

@given(instance=carnot::LinkTypeType_strategy)
def test_carnot::linktypetype_sourceSymbol_type(instance):
    assert isinstance(instance.sourceSymbol, str)


@given(instance=carnot::LinkTypeType_strategy)
def test_carnot::linktypetype_sourceSymbol_setter(instance):
    original = instance.sourceSymbol
    instance.sourceSymbol = original
    assert instance.sourceSymbol == original

@given(instance=carnot::LinkTypeType_strategy)
def test_carnot::linktypetype_sourceRole_type(instance):
    assert isinstance(instance.sourceRole, str)


@given(instance=carnot::LinkTypeType_strategy)
def test_carnot::linktypetype_sourceRole_setter(instance):
    original = instance.sourceRole
    instance.sourceRole = original
    assert instance.sourceRole == original

@given(instance=carnot::LinkTypeType_strategy)
def test_carnot::linktypetype_lineColor_type(instance):
    assert isinstance(instance.lineColor, str)


@given(instance=carnot::LinkTypeType_strategy)
def test_carnot::linktypetype_lineColor_setter(instance):
    original = instance.lineColor
    instance.lineColor = original
    assert instance.lineColor == original

@given(instance=carnot::LinkTypeType_strategy)
def test_carnot::linktypetype_lineStyle_type(instance):
    assert isinstance(instance.lineStyle, str)


@given(instance=carnot::LinkTypeType_strategy)
def test_carnot::linktypetype_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original

@given(instance=carnot::LinkTypeType_strategy)
def test_carnot::linktypetype_targetRole_type(instance):
    assert isinstance(instance.targetRole, str)


@given(instance=carnot::LinkTypeType_strategy)
def test_carnot::linktypetype_targetRole_setter(instance):
    original = instance.targetRole
    instance.targetRole = original
    assert instance.targetRole == original

@given(instance=carnot::LinkTypeType_strategy)
def test_carnot::linktypetype_showRoleNames_type(instance):
    assert isinstance(instance.showRoleNames, str)


@given(instance=carnot::LinkTypeType_strategy)
def test_carnot::linktypetype_showRoleNames_setter(instance):
    original = instance.showRoleNames
    instance.showRoleNames = original
    assert instance.showRoleNames == original

@given(instance=carnot::LinkTypeType_strategy)
def test_carnot::linktypetype_showLinkTypeName_type(instance):
    assert isinstance(instance.showLinkTypeName, str)


@given(instance=carnot::LinkTypeType_strategy)
def test_carnot::linktypetype_showLinkTypeName_setter(instance):
    original = instance.showLinkTypeName
    instance.showLinkTypeName = original
    assert instance.showLinkTypeName == original

@given(instance=carnot::LinkTypeType_strategy)
def test_carnot::linktypetype_targetClass_type(instance):
    assert isinstance(instance.targetClass, str)


@given(instance=carnot::LinkTypeType_strategy)
def test_carnot::linktypetype_targetClass_setter(instance):
    original = instance.targetClass
    instance.targetClass = original
    assert instance.targetClass == original

@given(instance=carnot::LinkTypeType_strategy)
def test_carnot::linktypetype_targetCardinality_type(instance):
    assert isinstance(instance.targetCardinality, str)


@given(instance=carnot::LinkTypeType_strategy)
def test_carnot::linktypetype_targetCardinality_setter(instance):
    original = instance.targetCardinality
    instance.targetCardinality = original
    assert instance.targetCardinality == original

@given(instance=carnot::LinkTypeType_strategy)
def test_carnot::linktypetype_sourceCardinality_type(instance):
    assert isinstance(instance.sourceCardinality, str)


@given(instance=carnot::LinkTypeType_strategy)
def test_carnot::linktypetype_sourceCardinality_setter(instance):
    original = instance.sourceCardinality
    instance.sourceCardinality = original
    assert instance.sourceCardinality == original

@given(instance=carnot::IdRefOwner_strategy)
@settings(max_examples=50)
def test_carnot::idrefowner_instantiation(instance):
    assert isinstance(instance, carnot::IdRefOwner)

@given(instance=carnot::ExternalPackage_strategy)
@settings(max_examples=50)
def test_carnot::externalpackage_instantiation(instance):
    assert isinstance(instance, carnot::ExternalPackage)

@given(instance=carnot::IdRef_strategy)
@settings(max_examples=50)
def test_carnot::idref_instantiation(instance):
    assert isinstance(instance, carnot::IdRef)

@given(instance=carnot::IdRef_strategy)
def test_carnot::idref_ref_type(instance):
    assert isinstance(instance.ref, str)


@given(instance=carnot::IdRef_strategy)
def test_carnot::idref_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=carnot::EventConditionTypeType_strategy)
@settings(max_examples=50)
def test_carnot::eventconditiontypetype_instantiation(instance):
    assert isinstance(instance, carnot::EventConditionTypeType)

@given(instance=carnot::EventConditionTypeType_strategy)
def test_carnot::eventconditiontypetype_binderClass_type(instance):
    assert isinstance(instance.binderClass, str)


@given(instance=carnot::EventConditionTypeType_strategy)
def test_carnot::eventconditiontypetype_binderClass_setter(instance):
    original = instance.binderClass
    instance.binderClass = original
    assert instance.binderClass == original

@given(instance=carnot::EventConditionTypeType_strategy)
def test_carnot::eventconditiontypetype_processCondition_type(instance):
    assert isinstance(instance.processCondition, str)


@given(instance=carnot::EventConditionTypeType_strategy)
def test_carnot::eventconditiontypetype_processCondition_setter(instance):
    original = instance.processCondition
    instance.processCondition = original
    assert instance.processCondition == original

@given(instance=carnot::EventConditionTypeType_strategy)
def test_carnot::eventconditiontypetype_implementation_type(instance):
    assert isinstance(instance.implementation, str)


@given(instance=carnot::EventConditionTypeType_strategy)
def test_carnot::eventconditiontypetype_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=carnot::EventConditionTypeType_strategy)
def test_carnot::eventconditiontypetype_activityCondition_type(instance):
    assert isinstance(instance.activityCondition, str)


@given(instance=carnot::EventConditionTypeType_strategy)
def test_carnot::eventconditiontypetype_activityCondition_setter(instance):
    original = instance.activityCondition
    instance.activityCondition = original
    assert instance.activityCondition == original

@given(instance=carnot::EventConditionTypeType_strategy)
def test_carnot::eventconditiontypetype_pullEventEmitterClass_type(instance):
    assert isinstance(instance.pullEventEmitterClass, str)


@given(instance=carnot::EventConditionTypeType_strategy)
def test_carnot::eventconditiontypetype_pullEventEmitterClass_setter(instance):
    original = instance.pullEventEmitterClass
    instance.pullEventEmitterClass = original
    assert instance.pullEventEmitterClass == original

@given(instance=carnot::EventConditionTypeType_strategy)
def test_carnot::eventconditiontypetype_panelClass_type(instance):
    assert isinstance(instance.panelClass, str)


@given(instance=carnot::EventConditionTypeType_strategy)
def test_carnot::eventconditiontypetype_panelClass_setter(instance):
    original = instance.panelClass
    instance.panelClass = original
    assert instance.panelClass == original

@given(instance=carnot::EventConditionTypeType_strategy)
def test_carnot::eventconditiontypetype_rule_type(instance):
    assert isinstance(instance.rule, str)


@given(instance=carnot::EventConditionTypeType_strategy)
def test_carnot::eventconditiontypetype_rule_setter(instance):
    original = instance.rule
    instance.rule = original
    assert instance.rule == original

@given(instance=carnot::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_carnot::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, carnot::EStringToStringMapEntry)

@given(instance=carnot::DocumentRoot_strategy)
@settings(max_examples=50)
def test_carnot::documentroot_instantiation(instance):
    assert isinstance(instance, carnot::DocumentRoot)

@given(instance=carnot::DocumentRoot_strategy)
def test_carnot::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=carnot::DocumentRoot_strategy)
def test_carnot::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=AbstractEventSymbol_strategy)
@settings(max_examples=50)
def test_abstracteventsymbol_instantiation(instance):
    assert isinstance(instance, AbstractEventSymbol)

@given(instance=carnot::PublicInterfaceSymbol_strategy)
@settings(max_examples=50)
def test_carnot::publicinterfacesymbol_instantiation(instance):
    assert isinstance(instance, carnot::PublicInterfaceSymbol)

@given(instance=carnot::IntermediateEventSymbol_strategy)
@settings(max_examples=50)
def test_carnot::intermediateeventsymbol_instantiation(instance):
    assert isinstance(instance, carnot::IntermediateEventSymbol)

@given(instance=carnot::StartEventSymbol_strategy)
@settings(max_examples=50)
def test_carnot::starteventsymbol_instantiation(instance):
    assert isinstance(instance, carnot::StartEventSymbol)

@given(instance=carnot::EndEventSymbol_strategy)
@settings(max_examples=50)
def test_carnot::endeventsymbol_instantiation(instance):
    assert isinstance(instance, carnot::EndEventSymbol)

@given(instance=carnot::ModelType_strategy)
@settings(max_examples=50)
def test_carnot::modeltype_instantiation(instance):
    assert isinstance(instance, carnot::ModelType)

@given(instance=carnot::ModelType_strategy)
def test_carnot::modeltype_vendor_type(instance):
    assert isinstance(instance.vendor, str)


@given(instance=carnot::ModelType_strategy)
def test_carnot::modeltype_vendor_setter(instance):
    original = instance.vendor
    instance.vendor = original
    assert instance.vendor == original

@given(instance=carnot::ModelType_strategy)
def test_carnot::modeltype_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=carnot::ModelType_strategy)
def test_carnot::modeltype_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=carnot::ModelType_strategy)
def test_carnot::modeltype_carnotVersion_type(instance):
    assert isinstance(instance.carnotVersion, str)


@given(instance=carnot::ModelType_strategy)
def test_carnot::modeltype_carnotVersion_setter(instance):
    original = instance.carnotVersion
    instance.carnotVersion = original
    assert instance.carnotVersion == original

@given(instance=carnot::ModelType_strategy)
def test_carnot::modeltype_modelOID_type(instance):
    assert isinstance(instance.modelOID, str)


@given(instance=carnot::ModelType_strategy)
def test_carnot::modeltype_modelOID_setter(instance):
    original = instance.modelOID
    instance.modelOID = original
    assert instance.modelOID == original

@given(instance=carnot::ModelType_strategy)
def test_carnot::modeltype_created_type(instance):
    assert isinstance(instance.created, str)


@given(instance=carnot::ModelType_strategy)
def test_carnot::modeltype_created_setter(instance):
    original = instance.created
    instance.created = original
    assert instance.created == original

@given(instance=carnot::ModelType_strategy)
def test_carnot::modeltype_oid_type(instance):
    assert isinstance(instance.oid, str)


@given(instance=carnot::ModelType_strategy)
def test_carnot::modeltype_oid_setter(instance):
    original = instance.oid
    instance.oid = original
    assert instance.oid == original

@given(instance=carnot::ExternalReferenceType_strategy)
@settings(max_examples=50)
def test_carnot::externalreferencetype_instantiation(instance):
    assert isinstance(instance, carnot::ExternalReferenceType)

@given(instance=carnot::ParameterMappingType_strategy)
@settings(max_examples=50)
def test_carnot::parametermappingtype_instantiation(instance):
    assert isinstance(instance, carnot::ParameterMappingType)

@given(instance=carnot::ParameterMappingType_strategy)
def test_carnot::parametermappingtype_dataPath_type(instance):
    assert isinstance(instance.dataPath, str)


@given(instance=carnot::ParameterMappingType_strategy)
def test_carnot::parametermappingtype_dataPath_setter(instance):
    original = instance.dataPath
    instance.dataPath = original
    assert instance.dataPath == original

@given(instance=carnot::ParameterMappingType_strategy)
def test_carnot::parametermappingtype_parameter_type(instance):
    assert isinstance(instance.parameter, str)


@given(instance=carnot::ParameterMappingType_strategy)
def test_carnot::parametermappingtype_parameter_setter(instance):
    original = instance.parameter
    instance.parameter = original
    assert instance.parameter == original

@given(instance=carnot::ParameterMappingType_strategy)
def test_carnot::parametermappingtype_parameterPath_type(instance):
    assert isinstance(instance.parameterPath, str)


@given(instance=carnot::ParameterMappingType_strategy)
def test_carnot::parametermappingtype_parameterPath_setter(instance):
    original = instance.parameterPath
    instance.parameterPath = original
    assert instance.parameterPath == original

@given(instance=ISymbolContainer_strategy)
@settings(max_examples=50)
def test_isymbolcontainer_instantiation(instance):
    assert isinstance(instance, ISymbolContainer)

@given(instance=carnot::PoolSymbol_strategy)
@settings(max_examples=50)
def test_carnot::poolsymbol_instantiation(instance):
    assert isinstance(instance, carnot::PoolSymbol)

@given(instance=carnot::PoolSymbol_strategy)
def test_carnot::poolsymbol_boundaryVisible_type(instance):
    assert isinstance(instance.boundaryVisible, str)


@given(instance=carnot::PoolSymbol_strategy)
def test_carnot::poolsymbol_boundaryVisible_setter(instance):
    original = instance.boundaryVisible
    instance.boundaryVisible = original
    assert instance.boundaryVisible == original

@given(instance=carnot::GroupSymbolType_strategy)
@settings(max_examples=50)
def test_carnot::groupsymboltype_instantiation(instance):
    assert isinstance(instance, carnot::GroupSymbolType)

@given(instance=carnot::LaneSymbol_strategy)
@settings(max_examples=50)
def test_carnot::lanesymbol_instantiation(instance):
    assert isinstance(instance, carnot::LaneSymbol)

@given(instance=carnot::DiagramType_strategy)
@settings(max_examples=50)
def test_carnot::diagramtype_instantiation(instance):
    assert isinstance(instance, carnot::DiagramType)

@given(instance=carnot::DiagramType_strategy)
def test_carnot::diagramtype_orientation_type(instance):
    assert isinstance(instance.orientation, str)


@given(instance=carnot::DiagramType_strategy)
def test_carnot::diagramtype_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original

@given(instance=carnot::DiagramType_strategy)
def test_carnot::diagramtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=carnot::DiagramType_strategy)
def test_carnot::diagramtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=carnot::DiagramType_strategy)
def test_carnot::diagramtype_mode_type(instance):
    assert isinstance(instance.mode, str)


@given(instance=carnot::DiagramType_strategy)
def test_carnot::diagramtype_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=carnot::DataPathType_strategy)
@settings(max_examples=50)
def test_carnot::datapathtype_instantiation(instance):
    assert isinstance(instance, carnot::DataPathType)

@given(instance=carnot::DataPathType_strategy)
def test_carnot::datapathtype_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=carnot::DataPathType_strategy)
def test_carnot::datapathtype_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=carnot::DataPathType_strategy)
def test_carnot::datapathtype_dataPath_type(instance):
    assert isinstance(instance.dataPath, str)


@given(instance=carnot::DataPathType_strategy)
def test_carnot::datapathtype_dataPath_setter(instance):
    original = instance.dataPath
    instance.dataPath = original
    assert instance.dataPath == original

@given(instance=carnot::DataPathType_strategy)
def test_carnot::datapathtype_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=carnot::DataPathType_strategy)
def test_carnot::datapathtype_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=carnot::DataPathType_strategy)
def test_carnot::datapathtype_descriptor_type(instance):
    assert isinstance(instance.descriptor, str)


@given(instance=carnot::DataPathType_strategy)
def test_carnot::datapathtype_descriptor_setter(instance):
    original = instance.descriptor
    instance.descriptor = original
    assert instance.descriptor == original

@given(instance=IConnectionSymbol_strategy)
@settings(max_examples=50)
def test_iconnectionsymbol_instantiation(instance):
    assert isinstance(instance, IConnectionSymbol)

@given(instance=carnot::TransitionConnectionType_strategy)
@settings(max_examples=50)
def test_carnot::transitionconnectiontype_instantiation(instance):
    assert isinstance(instance, carnot::TransitionConnectionType)

@given(instance=carnot::TransitionConnectionType_strategy)
def test_carnot::transitionconnectiontype_points_type(instance):
    assert isinstance(instance.points, str)


@given(instance=carnot::TransitionConnectionType_strategy)
def test_carnot::transitionconnectiontype_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original

@given(instance=carnot::TeamLeadConnectionType_strategy)
@settings(max_examples=50)
def test_carnot::teamleadconnectiontype_instantiation(instance):
    assert isinstance(instance, carnot::TeamLeadConnectionType)

@given(instance=carnot::GenericLinkConnectionType_strategy)
@settings(max_examples=50)
def test_carnot::genericlinkconnectiontype_instantiation(instance):
    assert isinstance(instance, carnot::GenericLinkConnectionType)

@given(instance=carnot::WorksForConnectionType_strategy)
@settings(max_examples=50)
def test_carnot::worksforconnectiontype_instantiation(instance):
    assert isinstance(instance, carnot::WorksForConnectionType)

@given(instance=carnot::SubProcessOfConnectionType_strategy)
@settings(max_examples=50)
def test_carnot::subprocessofconnectiontype_instantiation(instance):
    assert isinstance(instance, carnot::SubProcessOfConnectionType)

@given(instance=carnot::PartOfConnectionType_strategy)
@settings(max_examples=50)
def test_carnot::partofconnectiontype_instantiation(instance):
    assert isinstance(instance, carnot::PartOfConnectionType)

@given(instance=carnot::ExecutedByConnectionType_strategy)
@settings(max_examples=50)
def test_carnot::executedbyconnectiontype_instantiation(instance):
    assert isinstance(instance, carnot::ExecutedByConnectionType)

@given(instance=carnot::RefersToConnectionType_strategy)
@settings(max_examples=50)
def test_carnot::referstoconnectiontype_instantiation(instance):
    assert isinstance(instance, carnot::RefersToConnectionType)

@given(instance=carnot::TriggersConnectionType_strategy)
@settings(max_examples=50)
def test_carnot::triggersconnectiontype_instantiation(instance):
    assert isinstance(instance, carnot::TriggersConnectionType)

@given(instance=carnot::PerformsConnectionType_strategy)
@settings(max_examples=50)
def test_carnot::performsconnectiontype_instantiation(instance):
    assert isinstance(instance, carnot::PerformsConnectionType)

@given(instance=carnot::DataMappingConnectionType_strategy)
@settings(max_examples=50)
def test_carnot::datamappingconnectiontype_instantiation(instance):
    assert isinstance(instance, carnot::DataMappingConnectionType)

@given(instance=IModelParticipantSymbol_strategy)
@settings(max_examples=50)
def test_imodelparticipantsymbol_instantiation(instance):
    assert isinstance(instance, IModelParticipantSymbol)

@given(instance=carnot::RoleSymbolType_strategy)
@settings(max_examples=50)
def test_carnot::rolesymboltype_instantiation(instance):
    assert isinstance(instance, carnot::RoleSymbolType)

@given(instance=carnot::OrganizationSymbolType_strategy)
@settings(max_examples=50)
def test_carnot::organizationsymboltype_instantiation(instance):
    assert isinstance(instance, carnot::OrganizationSymbolType)

@given(instance=carnot::ConditionalPerformerSymbolType_strategy)
@settings(max_examples=50)
def test_carnot::conditionalperformersymboltype_instantiation(instance):
    assert isinstance(instance, carnot::ConditionalPerformerSymbolType)

@given(instance=AbstractEventAction_strategy)
@settings(max_examples=50)
def test_abstracteventaction_instantiation(instance):
    assert isinstance(instance, AbstractEventAction)

@given(instance=carnot::EventActionType_strategy)
@settings(max_examples=50)
def test_carnot::eventactiontype_instantiation(instance):
    assert isinstance(instance, carnot::EventActionType)

@given(instance=carnot::UnbindActionType_strategy)
@settings(max_examples=50)
def test_carnot::unbindactiontype_instantiation(instance):
    assert isinstance(instance, carnot::UnbindActionType)

@given(instance=carnot::BindActionType_strategy)
@settings(max_examples=50)
def test_carnot::bindactiontype_instantiation(instance):
    assert isinstance(instance, carnot::BindActionType)

@given(instance=carnot::DataType_strategy)
@settings(max_examples=50)
def test_carnot::datatype_instantiation(instance):
    assert isinstance(instance, carnot::DataType)

@given(instance=carnot::DataType_strategy)
def test_carnot::datatype_predefined_type(instance):
    assert isinstance(instance.predefined, str)


@given(instance=carnot::DataType_strategy)
def test_carnot::datatype_predefined_setter(instance):
    original = instance.predefined
    instance.predefined = original
    assert instance.predefined == original

@given(instance=IModelParticipant_strategy)
@settings(max_examples=50)
def test_imodelparticipant_instantiation(instance):
    assert isinstance(instance, IModelParticipant)

@given(instance=carnot::OrganizationType_strategy)
@settings(max_examples=50)
def test_carnot::organizationtype_instantiation(instance):
    assert isinstance(instance, carnot::OrganizationType)

@given(instance=carnot::ConditionalPerformerType_strategy)
@settings(max_examples=50)
def test_carnot::conditionalperformertype_instantiation(instance):
    assert isinstance(instance, carnot::ConditionalPerformerType)

@given(instance=carnot::ConditionalPerformerType_strategy)
def test_carnot::conditionalperformertype_dataPath_type(instance):
    assert isinstance(instance.dataPath, str)


@given(instance=carnot::ConditionalPerformerType_strategy)
def test_carnot::conditionalperformertype_dataPath_setter(instance):
    original = instance.dataPath
    instance.dataPath = original
    assert instance.dataPath == original

@given(instance=carnot::ConditionalPerformerType_strategy)
def test_carnot::conditionalperformertype_isUser_type(instance):
    assert isinstance(instance.isUser, str)


@given(instance=carnot::ConditionalPerformerType_strategy)
def test_carnot::conditionalperformertype_isUser_setter(instance):
    original = instance.isUser
    instance.isUser = original
    assert instance.isUser == original

@given(instance=carnot::RoleType_strategy)
@settings(max_examples=50)
def test_carnot::roletype_instantiation(instance):
    assert isinstance(instance, carnot::RoleType)

@given(instance=carnot::RoleType_strategy)
def test_carnot::roletype_cardinality_type(instance):
    assert isinstance(instance.cardinality, int)


@given(instance=carnot::RoleType_strategy)
def test_carnot::roletype_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original
