import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    applauseDsl::AttributeReference,
    applauseDsl::EntityMemberCallTail,
    Expression,
    applauseDsl::StringLiteral,
    applauseDsl::EntityMemberCall,
    applauseDsl::Expression,
    applauseDsl::UIComponentMemberCall,
    applauseDsl::UIComponentOrDataType,
    applauseDsl::UIComponentMemberDeclaration,
    applauseDsl::UIAction,
    applauseDsl::ScreenSection,
    applauseDsl::DataSourceCall,
    UIActionSpecification,
    applauseDsl::UIActionDeleteAction,
    applauseDsl::UIActionNavigateAction,
    applauseDsl::UIActionSpecification,
    applauseDsl::ReferrableElement,
    applauseDsl::UIComponentMemberConfiguration,
    applauseDsl::RESTMethodCall,
    applauseDsl::ScreenListItemCell,
    applauseDsl::ScreenSectionItems,
    applauseDsl::RESTSpecification,
    UrlFragment,
    applauseDsl::Variable,
    applauseDsl::UrlPathFragment,
    RESTURL,
    applauseDsl::RelativeRESTURL,
    applauseDsl::UrlFragment,
    ReferrableElement,
    applauseDsl::Parameter,
    applauseDsl::LoopVariable,
    applauseDsl::DataSourceBodySpecification,
    applauseDsl::RESTURL,
    applauseDsl::DataSourceAccessMethod,
    applauseDsl::AbsoluteRESTURL,
    PlatformMapping,
    applauseDsl::TypeMapping,
    applauseDsl::PlatformMapping,
    applauseDsl::Attribute,
    UIComponentOrDataType,
    Type,
    applauseDsl::Entity,
    applauseDsl::DataType,
    NamedElement,
    applauseDsl::Screen,
    applauseDsl::DataSource,
    applauseDsl::ListItemCellDeclaration,
    applauseDsl::UIComponentDeclaration,
    applauseDsl::Platform,
    applauseDsl::Type,
    applauseDsl::NamedElement,
    applauseDsl::Model,
    ActionVerb,
    ScreenKind,
    UIActionKind,
    GestureKind,
    RESTVerb,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_applausedsl::attributereference_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::AttributeReference)


def test_applausedsl::attributereference_constructor_exists():
    assert callable(applauseDsl::AttributeReference.__init__)


def test_applausedsl::attributereference_constructor_args():
    sig = inspect.signature(applauseDsl::AttributeReference.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::entitymembercalltail_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::EntityMemberCallTail)


def test_applausedsl::entitymembercalltail_constructor_exists():
    assert callable(applauseDsl::EntityMemberCallTail.__init__)


def test_applausedsl::entitymembercalltail_constructor_args():
    sig = inspect.signature(applauseDsl::EntityMemberCallTail.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::stringliteral_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::StringLiteral)


def test_applausedsl::stringliteral_constructor_exists():
    assert callable(applauseDsl::StringLiteral.__init__)


def test_applausedsl::stringliteral_constructor_args():
    sig = inspect.signature(applauseDsl::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_applausedsl::stringliteral_has_value():
    assert hasattr(applauseDsl::StringLiteral, "value")
    descriptor = None
    for klass in applauseDsl::StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl::entitymembercall_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::EntityMemberCall)


def test_applausedsl::entitymembercall_constructor_exists():
    assert callable(applauseDsl::EntityMemberCall.__init__)


def test_applausedsl::entitymembercall_constructor_args():
    sig = inspect.signature(applauseDsl::EntityMemberCall.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::expression_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::Expression)


def test_applausedsl::expression_constructor_exists():
    assert callable(applauseDsl::Expression.__init__)


def test_applausedsl::expression_constructor_args():
    sig = inspect.signature(applauseDsl::Expression.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::uicomponentmembercall_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::UIComponentMemberCall)


def test_applausedsl::uicomponentmembercall_constructor_exists():
    assert callable(applauseDsl::UIComponentMemberCall.__init__)


def test_applausedsl::uicomponentmembercall_constructor_args():
    sig = inspect.signature(applauseDsl::UIComponentMemberCall.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::uicomponentordatatype_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::UIComponentOrDataType)


def test_applausedsl::uicomponentordatatype_constructor_exists():
    assert callable(applauseDsl::UIComponentOrDataType.__init__)


def test_applausedsl::uicomponentordatatype_constructor_args():
    sig = inspect.signature(applauseDsl::UIComponentOrDataType.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::uicomponentmemberdeclaration_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::UIComponentMemberDeclaration)


def test_applausedsl::uicomponentmemberdeclaration_constructor_exists():
    assert callable(applauseDsl::UIComponentMemberDeclaration.__init__)


def test_applausedsl::uicomponentmemberdeclaration_constructor_args():
    sig = inspect.signature(applauseDsl::UIComponentMemberDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_applausedsl::uicomponentmemberdeclaration_has_name():
    assert hasattr(applauseDsl::UIComponentMemberDeclaration, "name")
    descriptor = None
    for klass in applauseDsl::UIComponentMemberDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl::uiaction_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::UIAction)


def test_applausedsl::uiaction_constructor_exists():
    assert callable(applauseDsl::UIAction.__init__)


def test_applausedsl::uiaction_constructor_args():
    sig = inspect.signature(applauseDsl::UIAction.__init__)
    params = list(sig.parameters.keys())
    assert "order" in params, "Missing parameter 'order'"
    assert "title" in params, "Missing parameter 'title'"
    assert "icon" in params, "Missing parameter 'icon'"
    assert "gesture" in params, "Missing parameter 'gesture'"

def test_applausedsl::uiaction_has_order():
    assert hasattr(applauseDsl::UIAction, "order")
    descriptor = None
    for klass in applauseDsl::UIAction.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)

def test_applausedsl::uiaction_has_title():
    assert hasattr(applauseDsl::UIAction, "title")
    descriptor = None
    for klass in applauseDsl::UIAction.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_applausedsl::uiaction_has_icon():
    assert hasattr(applauseDsl::UIAction, "icon")
    descriptor = None
    for klass in applauseDsl::UIAction.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)

def test_applausedsl::uiaction_has_gesture():
    assert hasattr(applauseDsl::UIAction, "gesture")
    descriptor = None
    for klass in applauseDsl::UIAction.__mro__:
        if "gesture" in klass.__dict__:
            descriptor = klass.__dict__["gesture"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl::screensection_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::ScreenSection)


def test_applausedsl::screensection_constructor_exists():
    assert callable(applauseDsl::ScreenSection.__init__)


def test_applausedsl::screensection_constructor_args():
    sig = inspect.signature(applauseDsl::ScreenSection.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_applausedsl::screensection_has_title():
    assert hasattr(applauseDsl::ScreenSection, "title")
    descriptor = None
    for klass in applauseDsl::ScreenSection.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl::datasourcecall_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::DataSourceCall)


def test_applausedsl::datasourcecall_constructor_exists():
    assert callable(applauseDsl::DataSourceCall.__init__)


def test_applausedsl::datasourcecall_constructor_args():
    sig = inspect.signature(applauseDsl::DataSourceCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_applausedsl::datasourcecall_has_name():
    assert hasattr(applauseDsl::DataSourceCall, "name")
    descriptor = None
    for klass in applauseDsl::DataSourceCall.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uiactionspecification_is_not_abstract():
    assert not inspect.isabstract(UIActionSpecification)


def test_uiactionspecification_constructor_exists():
    assert callable(UIActionSpecification.__init__)


def test_uiactionspecification_constructor_args():
    sig = inspect.signature(UIActionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::uiactiondeleteaction_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::UIActionDeleteAction)


def test_applausedsl::uiactiondeleteaction_constructor_exists():
    assert callable(applauseDsl::UIActionDeleteAction.__init__)


def test_applausedsl::uiactiondeleteaction_constructor_args():
    sig = inspect.signature(applauseDsl::UIActionDeleteAction.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::uiactionnavigateaction_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::UIActionNavigateAction)


def test_applausedsl::uiactionnavigateaction_constructor_exists():
    assert callable(applauseDsl::UIActionNavigateAction.__init__)


def test_applausedsl::uiactionnavigateaction_constructor_args():
    sig = inspect.signature(applauseDsl::UIActionNavigateAction.__init__)
    params = list(sig.parameters.keys())
    assert "actionVerb" in params, "Missing parameter 'actionVerb'"

def test_applausedsl::uiactionnavigateaction_has_actionVerb():
    assert hasattr(applauseDsl::UIActionNavigateAction, "actionVerb")
    descriptor = None
    for klass in applauseDsl::UIActionNavigateAction.__mro__:
        if "actionVerb" in klass.__dict__:
            descriptor = klass.__dict__["actionVerb"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl::uiactionspecification_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::UIActionSpecification)


def test_applausedsl::uiactionspecification_constructor_exists():
    assert callable(applauseDsl::UIActionSpecification.__init__)


def test_applausedsl::uiactionspecification_constructor_args():
    sig = inspect.signature(applauseDsl::UIActionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::referrableelement_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::ReferrableElement)


def test_applausedsl::referrableelement_constructor_exists():
    assert callable(applauseDsl::ReferrableElement.__init__)


def test_applausedsl::referrableelement_constructor_args():
    sig = inspect.signature(applauseDsl::ReferrableElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_applausedsl::referrableelement_has_name():
    assert hasattr(applauseDsl::ReferrableElement, "name")
    descriptor = None
    for klass in applauseDsl::ReferrableElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl::uicomponentmemberconfiguration_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::UIComponentMemberConfiguration)


def test_applausedsl::uicomponentmemberconfiguration_constructor_exists():
    assert callable(applauseDsl::UIComponentMemberConfiguration.__init__)


def test_applausedsl::uicomponentmemberconfiguration_constructor_args():
    sig = inspect.signature(applauseDsl::UIComponentMemberConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::restmethodcall_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::RESTMethodCall)


def test_applausedsl::restmethodcall_constructor_exists():
    assert callable(applauseDsl::RESTMethodCall.__init__)


def test_applausedsl::restmethodcall_constructor_args():
    sig = inspect.signature(applauseDsl::RESTMethodCall.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::screenlistitemcell_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::ScreenListItemCell)


def test_applausedsl::screenlistitemcell_constructor_exists():
    assert callable(applauseDsl::ScreenListItemCell.__init__)


def test_applausedsl::screenlistitemcell_constructor_args():
    sig = inspect.signature(applauseDsl::ScreenListItemCell.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::screensectionitems_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::ScreenSectionItems)


def test_applausedsl::screensectionitems_constructor_exists():
    assert callable(applauseDsl::ScreenSectionItems.__init__)


def test_applausedsl::screensectionitems_constructor_args():
    sig = inspect.signature(applauseDsl::ScreenSectionItems.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::restspecification_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::RESTSpecification)


def test_applausedsl::restspecification_constructor_exists():
    assert callable(applauseDsl::RESTSpecification.__init__)


def test_applausedsl::restspecification_constructor_args():
    sig = inspect.signature(applauseDsl::RESTSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "verb" in params, "Missing parameter 'verb'"

def test_applausedsl::restspecification_has_verb():
    assert hasattr(applauseDsl::RESTSpecification, "verb")
    descriptor = None
    for klass in applauseDsl::RESTSpecification.__mro__:
        if "verb" in klass.__dict__:
            descriptor = klass.__dict__["verb"]
            break
    assert isinstance(descriptor, property)



def test_urlfragment_is_not_abstract():
    assert not inspect.isabstract(UrlFragment)


def test_urlfragment_constructor_exists():
    assert callable(UrlFragment.__init__)


def test_urlfragment_constructor_args():
    sig = inspect.signature(UrlFragment.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::variable_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::Variable)


def test_applausedsl::variable_constructor_exists():
    assert callable(applauseDsl::Variable.__init__)


def test_applausedsl::variable_constructor_args():
    sig = inspect.signature(applauseDsl::Variable.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::urlpathfragment_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::UrlPathFragment)


def test_applausedsl::urlpathfragment_constructor_exists():
    assert callable(applauseDsl::UrlPathFragment.__init__)


def test_applausedsl::urlpathfragment_constructor_args():
    sig = inspect.signature(applauseDsl::UrlPathFragment.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_applausedsl::urlpathfragment_has_name():
    assert hasattr(applauseDsl::UrlPathFragment, "name")
    descriptor = None
    for klass in applauseDsl::UrlPathFragment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_resturl_is_not_abstract():
    assert not inspect.isabstract(RESTURL)


def test_resturl_constructor_exists():
    assert callable(RESTURL.__init__)


def test_resturl_constructor_args():
    sig = inspect.signature(RESTURL.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::relativeresturl_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::RelativeRESTURL)


def test_applausedsl::relativeresturl_constructor_exists():
    assert callable(applauseDsl::RelativeRESTURL.__init__)


def test_applausedsl::relativeresturl_constructor_args():
    sig = inspect.signature(applauseDsl::RelativeRESTURL.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::urlfragment_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::UrlFragment)


def test_applausedsl::urlfragment_constructor_exists():
    assert callable(applauseDsl::UrlFragment.__init__)


def test_applausedsl::urlfragment_constructor_args():
    sig = inspect.signature(applauseDsl::UrlFragment.__init__)
    params = list(sig.parameters.keys())



def test_referrableelement_is_not_abstract():
    assert not inspect.isabstract(ReferrableElement)


def test_referrableelement_constructor_exists():
    assert callable(ReferrableElement.__init__)


def test_referrableelement_constructor_args():
    sig = inspect.signature(ReferrableElement.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::parameter_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::Parameter)


def test_applausedsl::parameter_constructor_exists():
    assert callable(applauseDsl::Parameter.__init__)


def test_applausedsl::parameter_constructor_args():
    sig = inspect.signature(applauseDsl::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::loopvariable_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::LoopVariable)


def test_applausedsl::loopvariable_constructor_exists():
    assert callable(applauseDsl::LoopVariable.__init__)


def test_applausedsl::loopvariable_constructor_args():
    sig = inspect.signature(applauseDsl::LoopVariable.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::datasourcebodyspecification_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::DataSourceBodySpecification)


def test_applausedsl::datasourcebodyspecification_constructor_exists():
    assert callable(applauseDsl::DataSourceBodySpecification.__init__)


def test_applausedsl::datasourcebodyspecification_constructor_args():
    sig = inspect.signature(applauseDsl::DataSourceBodySpecification.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::resturl_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::RESTURL)


def test_applausedsl::resturl_constructor_exists():
    assert callable(applauseDsl::RESTURL.__init__)


def test_applausedsl::resturl_constructor_args():
    sig = inspect.signature(applauseDsl::RESTURL.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::datasourceaccessmethod_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::DataSourceAccessMethod)


def test_applausedsl::datasourceaccessmethod_constructor_exists():
    assert callable(applauseDsl::DataSourceAccessMethod.__init__)


def test_applausedsl::datasourceaccessmethod_constructor_args():
    sig = inspect.signature(applauseDsl::DataSourceAccessMethod.__init__)
    params = list(sig.parameters.keys())
    assert "returnsMany" in params, "Missing parameter 'returnsMany'"
    assert "name" in params, "Missing parameter 'name'"

def test_applausedsl::datasourceaccessmethod_has_returnsMany():
    assert hasattr(applauseDsl::DataSourceAccessMethod, "returnsMany")
    descriptor = None
    for klass in applauseDsl::DataSourceAccessMethod.__mro__:
        if "returnsMany" in klass.__dict__:
            descriptor = klass.__dict__["returnsMany"]
            break
    assert isinstance(descriptor, property)

def test_applausedsl::datasourceaccessmethod_has_name():
    assert hasattr(applauseDsl::DataSourceAccessMethod, "name")
    descriptor = None
    for klass in applauseDsl::DataSourceAccessMethod.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl::absoluteresturl_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::AbsoluteRESTURL)


def test_applausedsl::absoluteresturl_constructor_exists():
    assert callable(applauseDsl::AbsoluteRESTURL.__init__)


def test_applausedsl::absoluteresturl_constructor_args():
    sig = inspect.signature(applauseDsl::AbsoluteRESTURL.__init__)
    params = list(sig.parameters.keys())
    assert "port" in params, "Missing parameter 'port'"

def test_applausedsl::absoluteresturl_has_port():
    assert hasattr(applauseDsl::AbsoluteRESTURL, "port")
    descriptor = None
    for klass in applauseDsl::AbsoluteRESTURL.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)



def test_platformmapping_is_not_abstract():
    assert not inspect.isabstract(PlatformMapping)


def test_platformmapping_constructor_exists():
    assert callable(PlatformMapping.__init__)


def test_platformmapping_constructor_args():
    sig = inspect.signature(PlatformMapping.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::typemapping_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::TypeMapping)


def test_applausedsl::typemapping_constructor_exists():
    assert callable(applauseDsl::TypeMapping.__init__)


def test_applausedsl::typemapping_constructor_args():
    sig = inspect.signature(applauseDsl::TypeMapping.__init__)
    params = list(sig.parameters.keys())
    assert "simpleName" in params, "Missing parameter 'simpleName'"

def test_applausedsl::typemapping_has_simpleName():
    assert hasattr(applauseDsl::TypeMapping, "simpleName")
    descriptor = None
    for klass in applauseDsl::TypeMapping.__mro__:
        if "simpleName" in klass.__dict__:
            descriptor = klass.__dict__["simpleName"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl::platformmapping_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::PlatformMapping)


def test_applausedsl::platformmapping_constructor_exists():
    assert callable(applauseDsl::PlatformMapping.__init__)


def test_applausedsl::platformmapping_constructor_args():
    sig = inspect.signature(applauseDsl::PlatformMapping.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::attribute_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::Attribute)


def test_applausedsl::attribute_constructor_exists():
    assert callable(applauseDsl::Attribute.__init__)


def test_applausedsl::attribute_constructor_args():
    sig = inspect.signature(applauseDsl::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "many" in params, "Missing parameter 'many'"

def test_applausedsl::attribute_has_name():
    assert hasattr(applauseDsl::Attribute, "name")
    descriptor = None
    for klass in applauseDsl::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_applausedsl::attribute_has_many():
    assert hasattr(applauseDsl::Attribute, "many")
    descriptor = None
    for klass in applauseDsl::Attribute.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)



def test_uicomponentordatatype_is_not_abstract():
    assert not inspect.isabstract(UIComponentOrDataType)


def test_uicomponentordatatype_constructor_exists():
    assert callable(UIComponentOrDataType.__init__)


def test_uicomponentordatatype_constructor_args():
    sig = inspect.signature(UIComponentOrDataType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::entity_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::Entity)


def test_applausedsl::entity_constructor_exists():
    assert callable(applauseDsl::Entity.__init__)


def test_applausedsl::entity_constructor_args():
    sig = inspect.signature(applauseDsl::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_applausedsl::entity_has_abstract():
    assert hasattr(applauseDsl::Entity, "abstract")
    descriptor = None
    for klass in applauseDsl::Entity.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl::datatype_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::DataType)


def test_applausedsl::datatype_constructor_exists():
    assert callable(applauseDsl::DataType.__init__)


def test_applausedsl::datatype_constructor_args():
    sig = inspect.signature(applauseDsl::DataType.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::screen_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::Screen)


def test_applausedsl::screen_constructor_exists():
    assert callable(applauseDsl::Screen.__init__)


def test_applausedsl::screen_constructor_args():
    sig = inspect.signature(applauseDsl::Screen.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "title" in params, "Missing parameter 'title'"

def test_applausedsl::screen_has_kind():
    assert hasattr(applauseDsl::Screen, "kind")
    descriptor = None
    for klass in applauseDsl::Screen.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_applausedsl::screen_has_title():
    assert hasattr(applauseDsl::Screen, "title")
    descriptor = None
    for klass in applauseDsl::Screen.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl::datasource_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::DataSource)


def test_applausedsl::datasource_constructor_exists():
    assert callable(applauseDsl::DataSource.__init__)


def test_applausedsl::datasource_constructor_args():
    sig = inspect.signature(applauseDsl::DataSource.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::listitemcelldeclaration_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::ListItemCellDeclaration)


def test_applausedsl::listitemcelldeclaration_constructor_exists():
    assert callable(applauseDsl::ListItemCellDeclaration.__init__)


def test_applausedsl::listitemcelldeclaration_constructor_args():
    sig = inspect.signature(applauseDsl::ListItemCellDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::uicomponentdeclaration_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::UIComponentDeclaration)


def test_applausedsl::uicomponentdeclaration_constructor_exists():
    assert callable(applauseDsl::UIComponentDeclaration.__init__)


def test_applausedsl::uicomponentdeclaration_constructor_args():
    sig = inspect.signature(applauseDsl::UIComponentDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::platform_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::Platform)


def test_applausedsl::platform_constructor_exists():
    assert callable(applauseDsl::Platform.__init__)


def test_applausedsl::platform_constructor_args():
    sig = inspect.signature(applauseDsl::Platform.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::type_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::Type)


def test_applausedsl::type_constructor_exists():
    assert callable(applauseDsl::Type.__init__)


def test_applausedsl::type_constructor_args():
    sig = inspect.signature(applauseDsl::Type.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl::namedelement_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::NamedElement)


def test_applausedsl::namedelement_constructor_exists():
    assert callable(applauseDsl::NamedElement.__init__)


def test_applausedsl::namedelement_constructor_args():
    sig = inspect.signature(applauseDsl::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_applausedsl::namedelement_has_name():
    assert hasattr(applauseDsl::NamedElement, "name")
    descriptor = None
    for klass in applauseDsl::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl::model_is_not_abstract():
    assert not inspect.isabstract(applauseDsl::Model)


def test_applausedsl::model_constructor_exists():
    assert callable(applauseDsl::Model.__init__)


def test_applausedsl::model_constructor_args():
    sig = inspect.signature(applauseDsl::Model.__init__)
    params = list(sig.parameters.keys())

def test_actionverb_exists():
    # Check that the Enumeration exists
    assert ActionVerb is not None

def test_actionverb_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActionVerb]
    expected_literals = [
        "edit",
        "add",
        "display",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActionVerb"

def test_screenkind_exists():
    # Check that the Enumeration exists
    assert ScreenKind is not None

def test_screenkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ScreenKind]
    expected_literals = [
        "DefaultDetails",
        "DefaultList",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ScreenKind"

def test_uiactionkind_exists():
    # Check that the Enumeration exists
    assert UIActionKind is not None

def test_uiactionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UIActionKind]
    expected_literals = [
        "performaction",
        "delete",
        "navigate",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UIActionKind"

def test_gesturekind_exists():
    # Check that the Enumeration exists
    assert GestureKind is not None

def test_gesturekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GestureKind]
    expected_literals = [
        "longpress",
        "swipe",
        "tap",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GestureKind"

def test_restverb_exists():
    # Check that the Enumeration exists
    assert RESTVerb is not None

def test_restverb_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RESTVerb]
    expected_literals = [
        "GET",
        "DELETE",
        "POST",
        "PUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RESTVerb"


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
applauseDsl::AttributeReference_strategy = st.builds(
    applauseDsl::AttributeReference,
)
applauseDsl::EntityMemberCallTail_strategy = st.builds(
    applauseDsl::EntityMemberCallTail,
)
Expression_strategy = st.builds(
    Expression,
)
applauseDsl::StringLiteral_strategy = st.builds(
    applauseDsl::StringLiteral,
    value=
        safe_text
)
applauseDsl::EntityMemberCall_strategy = st.builds(
    applauseDsl::EntityMemberCall,
)
applauseDsl::Expression_strategy = st.builds(
    applauseDsl::Expression,
)
applauseDsl::UIComponentMemberCall_strategy = st.builds(
    applauseDsl::UIComponentMemberCall,
)
applauseDsl::UIComponentOrDataType_strategy = st.builds(
    applauseDsl::UIComponentOrDataType,
)
applauseDsl::UIComponentMemberDeclaration_strategy = st.builds(
    applauseDsl::UIComponentMemberDeclaration,
    name=
        safe_text
)
applauseDsl::UIAction_strategy = st.builds(
    applauseDsl::UIAction,
    order=
        st.integers(),
    title=
        safe_text,
    icon=
        safe_text,
    gesture=
        safe_text
)
applauseDsl::ScreenSection_strategy = st.builds(
    applauseDsl::ScreenSection,
    title=
        safe_text
)
applauseDsl::DataSourceCall_strategy = st.builds(
    applauseDsl::DataSourceCall,
    name=
        safe_text
)
UIActionSpecification_strategy = st.builds(
    UIActionSpecification,
)
applauseDsl::UIActionDeleteAction_strategy = st.builds(
    applauseDsl::UIActionDeleteAction,
)
applauseDsl::UIActionNavigateAction_strategy = st.builds(
    applauseDsl::UIActionNavigateAction,
    actionVerb=
        safe_text
)
applauseDsl::UIActionSpecification_strategy = st.builds(
    applauseDsl::UIActionSpecification,
)
applauseDsl::ReferrableElement_strategy = st.builds(
    applauseDsl::ReferrableElement,
    name=
        safe_text
)
applauseDsl::UIComponentMemberConfiguration_strategy = st.builds(
    applauseDsl::UIComponentMemberConfiguration,
)
applauseDsl::RESTMethodCall_strategy = st.builds(
    applauseDsl::RESTMethodCall,
)
applauseDsl::ScreenListItemCell_strategy = st.builds(
    applauseDsl::ScreenListItemCell,
)
applauseDsl::ScreenSectionItems_strategy = st.builds(
    applauseDsl::ScreenSectionItems,
)
applauseDsl::RESTSpecification_strategy = st.builds(
    applauseDsl::RESTSpecification,
    verb=
        safe_text
)
UrlFragment_strategy = st.builds(
    UrlFragment,
)
applauseDsl::Variable_strategy = st.builds(
    applauseDsl::Variable,
)
applauseDsl::UrlPathFragment_strategy = st.builds(
    applauseDsl::UrlPathFragment,
    name=
        safe_text
)
RESTURL_strategy = st.builds(
    RESTURL,
)
applauseDsl::RelativeRESTURL_strategy = st.builds(
    applauseDsl::RelativeRESTURL,
)
applauseDsl::UrlFragment_strategy = st.builds(
    applauseDsl::UrlFragment,
)
ReferrableElement_strategy = st.builds(
    ReferrableElement,
)
applauseDsl::Parameter_strategy = st.builds(
    applauseDsl::Parameter,
)
applauseDsl::LoopVariable_strategy = st.builds(
    applauseDsl::LoopVariable,
)
applauseDsl::DataSourceBodySpecification_strategy = st.builds(
    applauseDsl::DataSourceBodySpecification,
)
applauseDsl::RESTURL_strategy = st.builds(
    applauseDsl::RESTURL,
)
applauseDsl::DataSourceAccessMethod_strategy = st.builds(
    applauseDsl::DataSourceAccessMethod,
    returnsMany=
        st.booleans(),
    name=
        safe_text
)
applauseDsl::AbsoluteRESTURL_strategy = st.builds(
    applauseDsl::AbsoluteRESTURL,
    port=
        st.integers()
)
PlatformMapping_strategy = st.builds(
    PlatformMapping,
)
applauseDsl::TypeMapping_strategy = st.builds(
    applauseDsl::TypeMapping,
    simpleName=
        safe_text
)
applauseDsl::PlatformMapping_strategy = st.builds(
    applauseDsl::PlatformMapping,
)
applauseDsl::Attribute_strategy = st.builds(
    applauseDsl::Attribute,
    name=
        safe_text,
    many=
        st.booleans()
)
UIComponentOrDataType_strategy = st.builds(
    UIComponentOrDataType,
)
Type_strategy = st.builds(
    Type,
)
applauseDsl::Entity_strategy = st.builds(
    applauseDsl::Entity,
    abstract=
        st.booleans()
)
applauseDsl::DataType_strategy = st.builds(
    applauseDsl::DataType,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
applauseDsl::Screen_strategy = st.builds(
    applauseDsl::Screen,
    kind=
        safe_text,
    title=
        safe_text
)
applauseDsl::DataSource_strategy = st.builds(
    applauseDsl::DataSource,
)
applauseDsl::ListItemCellDeclaration_strategy = st.builds(
    applauseDsl::ListItemCellDeclaration,
)
applauseDsl::UIComponentDeclaration_strategy = st.builds(
    applauseDsl::UIComponentDeclaration,
)
applauseDsl::Platform_strategy = st.builds(
    applauseDsl::Platform,
)
applauseDsl::Type_strategy = st.builds(
    applauseDsl::Type,
)
applauseDsl::NamedElement_strategy = st.builds(
    applauseDsl::NamedElement,
    name=
        safe_text
)
applauseDsl::Model_strategy = st.builds(
    applauseDsl::Model,
)

@given(instance=applauseDsl::AttributeReference_strategy)
@settings(max_examples=50)
def test_applausedsl::attributereference_instantiation(instance):
    assert isinstance(instance, applauseDsl::AttributeReference)

@given(instance=applauseDsl::EntityMemberCallTail_strategy)
@settings(max_examples=50)
def test_applausedsl::entitymembercalltail_instantiation(instance):
    assert isinstance(instance, applauseDsl::EntityMemberCallTail)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=applauseDsl::StringLiteral_strategy)
@settings(max_examples=50)
def test_applausedsl::stringliteral_instantiation(instance):
    assert isinstance(instance, applauseDsl::StringLiteral)

@given(instance=applauseDsl::StringLiteral_strategy)
def test_applausedsl::stringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=applauseDsl::StringLiteral_strategy)
def test_applausedsl::stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=applauseDsl::EntityMemberCall_strategy)
@settings(max_examples=50)
def test_applausedsl::entitymembercall_instantiation(instance):
    assert isinstance(instance, applauseDsl::EntityMemberCall)

@given(instance=applauseDsl::Expression_strategy)
@settings(max_examples=50)
def test_applausedsl::expression_instantiation(instance):
    assert isinstance(instance, applauseDsl::Expression)

@given(instance=applauseDsl::UIComponentMemberCall_strategy)
@settings(max_examples=50)
def test_applausedsl::uicomponentmembercall_instantiation(instance):
    assert isinstance(instance, applauseDsl::UIComponentMemberCall)

@given(instance=applauseDsl::UIComponentOrDataType_strategy)
@settings(max_examples=50)
def test_applausedsl::uicomponentordatatype_instantiation(instance):
    assert isinstance(instance, applauseDsl::UIComponentOrDataType)

@given(instance=applauseDsl::UIComponentMemberDeclaration_strategy)
@settings(max_examples=50)
def test_applausedsl::uicomponentmemberdeclaration_instantiation(instance):
    assert isinstance(instance, applauseDsl::UIComponentMemberDeclaration)

@given(instance=applauseDsl::UIComponentMemberDeclaration_strategy)
def test_applausedsl::uicomponentmemberdeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=applauseDsl::UIComponentMemberDeclaration_strategy)
def test_applausedsl::uicomponentmemberdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=applauseDsl::UIAction_strategy)
@settings(max_examples=50)
def test_applausedsl::uiaction_instantiation(instance):
    assert isinstance(instance, applauseDsl::UIAction)

@given(instance=applauseDsl::UIAction_strategy)
def test_applausedsl::uiaction_order_type(instance):
    assert isinstance(instance.order, int)


@given(instance=applauseDsl::UIAction_strategy)
def test_applausedsl::uiaction_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original

@given(instance=applauseDsl::UIAction_strategy)
def test_applausedsl::uiaction_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=applauseDsl::UIAction_strategy)
def test_applausedsl::uiaction_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=applauseDsl::UIAction_strategy)
def test_applausedsl::uiaction_icon_type(instance):
    assert isinstance(instance.icon, str)


@given(instance=applauseDsl::UIAction_strategy)
def test_applausedsl::uiaction_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original

@given(instance=applauseDsl::UIAction_strategy)
def test_applausedsl::uiaction_gesture_type(instance):
    assert isinstance(instance.gesture, str)


@given(instance=applauseDsl::UIAction_strategy)
def test_applausedsl::uiaction_gesture_setter(instance):
    original = instance.gesture
    instance.gesture = original
    assert instance.gesture == original

@given(instance=applauseDsl::ScreenSection_strategy)
@settings(max_examples=50)
def test_applausedsl::screensection_instantiation(instance):
    assert isinstance(instance, applauseDsl::ScreenSection)

@given(instance=applauseDsl::ScreenSection_strategy)
def test_applausedsl::screensection_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=applauseDsl::ScreenSection_strategy)
def test_applausedsl::screensection_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=applauseDsl::DataSourceCall_strategy)
@settings(max_examples=50)
def test_applausedsl::datasourcecall_instantiation(instance):
    assert isinstance(instance, applauseDsl::DataSourceCall)

@given(instance=applauseDsl::DataSourceCall_strategy)
def test_applausedsl::datasourcecall_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=applauseDsl::DataSourceCall_strategy)
def test_applausedsl::datasourcecall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UIActionSpecification_strategy)
@settings(max_examples=50)
def test_uiactionspecification_instantiation(instance):
    assert isinstance(instance, UIActionSpecification)

@given(instance=applauseDsl::UIActionDeleteAction_strategy)
@settings(max_examples=50)
def test_applausedsl::uiactiondeleteaction_instantiation(instance):
    assert isinstance(instance, applauseDsl::UIActionDeleteAction)

@given(instance=applauseDsl::UIActionNavigateAction_strategy)
@settings(max_examples=50)
def test_applausedsl::uiactionnavigateaction_instantiation(instance):
    assert isinstance(instance, applauseDsl::UIActionNavigateAction)

@given(instance=applauseDsl::UIActionNavigateAction_strategy)
def test_applausedsl::uiactionnavigateaction_actionVerb_type(instance):
    assert isinstance(instance.actionVerb, str)


@given(instance=applauseDsl::UIActionNavigateAction_strategy)
def test_applausedsl::uiactionnavigateaction_actionVerb_setter(instance):
    original = instance.actionVerb
    instance.actionVerb = original
    assert instance.actionVerb == original

@given(instance=applauseDsl::UIActionSpecification_strategy)
@settings(max_examples=50)
def test_applausedsl::uiactionspecification_instantiation(instance):
    assert isinstance(instance, applauseDsl::UIActionSpecification)

@given(instance=applauseDsl::ReferrableElement_strategy)
@settings(max_examples=50)
def test_applausedsl::referrableelement_instantiation(instance):
    assert isinstance(instance, applauseDsl::ReferrableElement)

@given(instance=applauseDsl::ReferrableElement_strategy)
def test_applausedsl::referrableelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=applauseDsl::ReferrableElement_strategy)
def test_applausedsl::referrableelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=applauseDsl::UIComponentMemberConfiguration_strategy)
@settings(max_examples=50)
def test_applausedsl::uicomponentmemberconfiguration_instantiation(instance):
    assert isinstance(instance, applauseDsl::UIComponentMemberConfiguration)

@given(instance=applauseDsl::RESTMethodCall_strategy)
@settings(max_examples=50)
def test_applausedsl::restmethodcall_instantiation(instance):
    assert isinstance(instance, applauseDsl::RESTMethodCall)

@given(instance=applauseDsl::ScreenListItemCell_strategy)
@settings(max_examples=50)
def test_applausedsl::screenlistitemcell_instantiation(instance):
    assert isinstance(instance, applauseDsl::ScreenListItemCell)

@given(instance=applauseDsl::ScreenSectionItems_strategy)
@settings(max_examples=50)
def test_applausedsl::screensectionitems_instantiation(instance):
    assert isinstance(instance, applauseDsl::ScreenSectionItems)

@given(instance=applauseDsl::RESTSpecification_strategy)
@settings(max_examples=50)
def test_applausedsl::restspecification_instantiation(instance):
    assert isinstance(instance, applauseDsl::RESTSpecification)

@given(instance=applauseDsl::RESTSpecification_strategy)
def test_applausedsl::restspecification_verb_type(instance):
    assert isinstance(instance.verb, str)


@given(instance=applauseDsl::RESTSpecification_strategy)
def test_applausedsl::restspecification_verb_setter(instance):
    original = instance.verb
    instance.verb = original
    assert instance.verb == original

@given(instance=UrlFragment_strategy)
@settings(max_examples=50)
def test_urlfragment_instantiation(instance):
    assert isinstance(instance, UrlFragment)

@given(instance=applauseDsl::Variable_strategy)
@settings(max_examples=50)
def test_applausedsl::variable_instantiation(instance):
    assert isinstance(instance, applauseDsl::Variable)

@given(instance=applauseDsl::UrlPathFragment_strategy)
@settings(max_examples=50)
def test_applausedsl::urlpathfragment_instantiation(instance):
    assert isinstance(instance, applauseDsl::UrlPathFragment)

@given(instance=applauseDsl::UrlPathFragment_strategy)
def test_applausedsl::urlpathfragment_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=applauseDsl::UrlPathFragment_strategy)
def test_applausedsl::urlpathfragment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RESTURL_strategy)
@settings(max_examples=50)
def test_resturl_instantiation(instance):
    assert isinstance(instance, RESTURL)

@given(instance=applauseDsl::RelativeRESTURL_strategy)
@settings(max_examples=50)
def test_applausedsl::relativeresturl_instantiation(instance):
    assert isinstance(instance, applauseDsl::RelativeRESTURL)

@given(instance=applauseDsl::UrlFragment_strategy)
@settings(max_examples=50)
def test_applausedsl::urlfragment_instantiation(instance):
    assert isinstance(instance, applauseDsl::UrlFragment)

@given(instance=ReferrableElement_strategy)
@settings(max_examples=50)
def test_referrableelement_instantiation(instance):
    assert isinstance(instance, ReferrableElement)

@given(instance=applauseDsl::Parameter_strategy)
@settings(max_examples=50)
def test_applausedsl::parameter_instantiation(instance):
    assert isinstance(instance, applauseDsl::Parameter)

@given(instance=applauseDsl::LoopVariable_strategy)
@settings(max_examples=50)
def test_applausedsl::loopvariable_instantiation(instance):
    assert isinstance(instance, applauseDsl::LoopVariable)

@given(instance=applauseDsl::DataSourceBodySpecification_strategy)
@settings(max_examples=50)
def test_applausedsl::datasourcebodyspecification_instantiation(instance):
    assert isinstance(instance, applauseDsl::DataSourceBodySpecification)

@given(instance=applauseDsl::RESTURL_strategy)
@settings(max_examples=50)
def test_applausedsl::resturl_instantiation(instance):
    assert isinstance(instance, applauseDsl::RESTURL)

@given(instance=applauseDsl::DataSourceAccessMethod_strategy)
@settings(max_examples=50)
def test_applausedsl::datasourceaccessmethod_instantiation(instance):
    assert isinstance(instance, applauseDsl::DataSourceAccessMethod)

@given(instance=applauseDsl::DataSourceAccessMethod_strategy)
def test_applausedsl::datasourceaccessmethod_returnsMany_type(instance):
    assert isinstance(instance.returnsMany, bool)


@given(instance=applauseDsl::DataSourceAccessMethod_strategy)
def test_applausedsl::datasourceaccessmethod_returnsMany_setter(instance):
    original = instance.returnsMany
    instance.returnsMany = original
    assert instance.returnsMany == original

@given(instance=applauseDsl::DataSourceAccessMethod_strategy)
def test_applausedsl::datasourceaccessmethod_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=applauseDsl::DataSourceAccessMethod_strategy)
def test_applausedsl::datasourceaccessmethod_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=applauseDsl::AbsoluteRESTURL_strategy)
@settings(max_examples=50)
def test_applausedsl::absoluteresturl_instantiation(instance):
    assert isinstance(instance, applauseDsl::AbsoluteRESTURL)

@given(instance=applauseDsl::AbsoluteRESTURL_strategy)
def test_applausedsl::absoluteresturl_port_type(instance):
    assert isinstance(instance.port, int)


@given(instance=applauseDsl::AbsoluteRESTURL_strategy)
def test_applausedsl::absoluteresturl_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original

@given(instance=PlatformMapping_strategy)
@settings(max_examples=50)
def test_platformmapping_instantiation(instance):
    assert isinstance(instance, PlatformMapping)

@given(instance=applauseDsl::TypeMapping_strategy)
@settings(max_examples=50)
def test_applausedsl::typemapping_instantiation(instance):
    assert isinstance(instance, applauseDsl::TypeMapping)

@given(instance=applauseDsl::TypeMapping_strategy)
def test_applausedsl::typemapping_simpleName_type(instance):
    assert isinstance(instance.simpleName, str)


@given(instance=applauseDsl::TypeMapping_strategy)
def test_applausedsl::typemapping_simpleName_setter(instance):
    original = instance.simpleName
    instance.simpleName = original
    assert instance.simpleName == original

@given(instance=applauseDsl::PlatformMapping_strategy)
@settings(max_examples=50)
def test_applausedsl::platformmapping_instantiation(instance):
    assert isinstance(instance, applauseDsl::PlatformMapping)

@given(instance=applauseDsl::Attribute_strategy)
@settings(max_examples=50)
def test_applausedsl::attribute_instantiation(instance):
    assert isinstance(instance, applauseDsl::Attribute)

@given(instance=applauseDsl::Attribute_strategy)
def test_applausedsl::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=applauseDsl::Attribute_strategy)
def test_applausedsl::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=applauseDsl::Attribute_strategy)
def test_applausedsl::attribute_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=applauseDsl::Attribute_strategy)
def test_applausedsl::attribute_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=UIComponentOrDataType_strategy)
@settings(max_examples=50)
def test_uicomponentordatatype_instantiation(instance):
    assert isinstance(instance, UIComponentOrDataType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=applauseDsl::Entity_strategy)
@settings(max_examples=50)
def test_applausedsl::entity_instantiation(instance):
    assert isinstance(instance, applauseDsl::Entity)

@given(instance=applauseDsl::Entity_strategy)
def test_applausedsl::entity_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=applauseDsl::Entity_strategy)
def test_applausedsl::entity_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=applauseDsl::DataType_strategy)
@settings(max_examples=50)
def test_applausedsl::datatype_instantiation(instance):
    assert isinstance(instance, applauseDsl::DataType)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=applauseDsl::Screen_strategy)
@settings(max_examples=50)
def test_applausedsl::screen_instantiation(instance):
    assert isinstance(instance, applauseDsl::Screen)

@given(instance=applauseDsl::Screen_strategy)
def test_applausedsl::screen_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=applauseDsl::Screen_strategy)
def test_applausedsl::screen_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=applauseDsl::Screen_strategy)
def test_applausedsl::screen_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=applauseDsl::Screen_strategy)
def test_applausedsl::screen_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=applauseDsl::DataSource_strategy)
@settings(max_examples=50)
def test_applausedsl::datasource_instantiation(instance):
    assert isinstance(instance, applauseDsl::DataSource)

@given(instance=applauseDsl::ListItemCellDeclaration_strategy)
@settings(max_examples=50)
def test_applausedsl::listitemcelldeclaration_instantiation(instance):
    assert isinstance(instance, applauseDsl::ListItemCellDeclaration)

@given(instance=applauseDsl::UIComponentDeclaration_strategy)
@settings(max_examples=50)
def test_applausedsl::uicomponentdeclaration_instantiation(instance):
    assert isinstance(instance, applauseDsl::UIComponentDeclaration)

@given(instance=applauseDsl::Platform_strategy)
@settings(max_examples=50)
def test_applausedsl::platform_instantiation(instance):
    assert isinstance(instance, applauseDsl::Platform)

@given(instance=applauseDsl::Type_strategy)
@settings(max_examples=50)
def test_applausedsl::type_instantiation(instance):
    assert isinstance(instance, applauseDsl::Type)

@given(instance=applauseDsl::NamedElement_strategy)
@settings(max_examples=50)
def test_applausedsl::namedelement_instantiation(instance):
    assert isinstance(instance, applauseDsl::NamedElement)

@given(instance=applauseDsl::NamedElement_strategy)
def test_applausedsl::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=applauseDsl::NamedElement_strategy)
def test_applausedsl::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=applauseDsl::Model_strategy)
@settings(max_examples=50)
def test_applausedsl::model_instantiation(instance):
    assert isinstance(instance, applauseDsl::Model)
