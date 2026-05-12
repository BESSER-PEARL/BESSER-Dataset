import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    UIActionSpecification,
    applauseDsl_UIActionNavigateAction,
    applauseDsl_UIActionSpecification,
    applauseDsl_ReferrableElement,
    applauseDsl_UIComponentMemberConfiguration,
    applauseDsl_RESTMethodCall,
    applauseDsl_ScreenListItemCell,
    applauseDsl_ScreenSectionItems,
    applauseDsl_RESTSpecification,
    UrlFragment,
    applauseDsl_Variable,
    applauseDsl_UrlPathFragment,
    RESTURL,
    applauseDsl_RelativeRESTURL,
    applauseDsl_UrlFragment,
    ReferrableElement,
    applauseDsl_LoopVariable,
    applauseDsl_Parameter,
    applauseDsl_DataSourceBodySpecification,
    applauseDsl_RESTURL,
    applauseDsl_DataSourceAccessMethod,
    applauseDsl_AbsoluteRESTURL,
    PlatformMapping,
    applauseDsl_TypeMapping,
    applauseDsl_PlatformMapping,
    applauseDsl_Attribute,
    UIComponentOrDataType,
    Type,
    applauseDsl_Entity,
    applauseDsl_DataType,
    NamedElement,
    applauseDsl_Platform,
    applauseDsl_DataSource,
    applauseDsl_ListItemCellDeclaration,
    applauseDsl_Screen,
    applauseDsl_Type,
    applauseDsl_NamedElement,
    applauseDsl_Model,
    applauseDsl_AttributeReference,
    applauseDsl_EntityMemberCallTail,
    Expression,
    applauseDsl_StringLiteral,
    applauseDsl_EntityMemberCall,
    applauseDsl_Expression,
    applauseDsl_UIComponentMemberCall,
    applauseDsl_UIComponentOrDataType,
    applauseDsl_UIComponentDeclaration,
    applauseDsl_UIComponentMemberDeclaration,
    applauseDsl_UIActionDeleteAction,
    applauseDsl_UIAction,
    applauseDsl_ScreenSection,
    applauseDsl_DataSourceCall,
    ScreenKind,
    GestureKind,
    ActionVerb,
    RESTVerb,
    UIActionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uiactionspecification_is_not_abstract():
    assert not inspect.isabstract(UIActionSpecification)


def test_uiactionspecification_constructor_exists():
    assert callable(UIActionSpecification.__init__)


def test_uiactionspecification_constructor_args():
    sig = inspect.signature(UIActionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_uiactionnavigateaction_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_UIActionNavigateAction)


def test_applausedsl_uiactionnavigateaction_constructor_exists():
    assert callable(applauseDsl_UIActionNavigateAction.__init__)


def test_applausedsl_uiactionnavigateaction_constructor_args():
    sig = inspect.signature(applauseDsl_UIActionNavigateAction.__init__)
    params = list(sig.parameters.keys())
    assert "actionVerb" in params, "Missing parameter 'actionVerb'"

def test_applausedsl_uiactionnavigateaction_has_actionVerb():
    assert hasattr(applauseDsl_UIActionNavigateAction, "actionVerb")
    descriptor = None
    for klass in applauseDsl_UIActionNavigateAction.__mro__:
        if "actionVerb" in klass.__dict__:
            descriptor = klass.__dict__["actionVerb"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl_uiactionspecification_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_UIActionSpecification)


def test_applausedsl_uiactionspecification_constructor_exists():
    assert callable(applauseDsl_UIActionSpecification.__init__)


def test_applausedsl_uiactionspecification_constructor_args():
    sig = inspect.signature(applauseDsl_UIActionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_referrableelement_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_ReferrableElement)


def test_applausedsl_referrableelement_constructor_exists():
    assert callable(applauseDsl_ReferrableElement.__init__)


def test_applausedsl_referrableelement_constructor_args():
    sig = inspect.signature(applauseDsl_ReferrableElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_applausedsl_referrableelement_has_name():
    assert hasattr(applauseDsl_ReferrableElement, "name")
    descriptor = None
    for klass in applauseDsl_ReferrableElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl_uicomponentmemberconfiguration_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_UIComponentMemberConfiguration)


def test_applausedsl_uicomponentmemberconfiguration_constructor_exists():
    assert callable(applauseDsl_UIComponentMemberConfiguration.__init__)


def test_applausedsl_uicomponentmemberconfiguration_constructor_args():
    sig = inspect.signature(applauseDsl_UIComponentMemberConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_restmethodcall_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_RESTMethodCall)


def test_applausedsl_restmethodcall_constructor_exists():
    assert callable(applauseDsl_RESTMethodCall.__init__)


def test_applausedsl_restmethodcall_constructor_args():
    sig = inspect.signature(applauseDsl_RESTMethodCall.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_screenlistitemcell_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_ScreenListItemCell)


def test_applausedsl_screenlistitemcell_constructor_exists():
    assert callable(applauseDsl_ScreenListItemCell.__init__)


def test_applausedsl_screenlistitemcell_constructor_args():
    sig = inspect.signature(applauseDsl_ScreenListItemCell.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_screensectionitems_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_ScreenSectionItems)


def test_applausedsl_screensectionitems_constructor_exists():
    assert callable(applauseDsl_ScreenSectionItems.__init__)


def test_applausedsl_screensectionitems_constructor_args():
    sig = inspect.signature(applauseDsl_ScreenSectionItems.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_restspecification_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_RESTSpecification)


def test_applausedsl_restspecification_constructor_exists():
    assert callable(applauseDsl_RESTSpecification.__init__)


def test_applausedsl_restspecification_constructor_args():
    sig = inspect.signature(applauseDsl_RESTSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "verb" in params, "Missing parameter 'verb'"

def test_applausedsl_restspecification_has_verb():
    assert hasattr(applauseDsl_RESTSpecification, "verb")
    descriptor = None
    for klass in applauseDsl_RESTSpecification.__mro__:
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



def test_applausedsl_variable_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_Variable)


def test_applausedsl_variable_constructor_exists():
    assert callable(applauseDsl_Variable.__init__)


def test_applausedsl_variable_constructor_args():
    sig = inspect.signature(applauseDsl_Variable.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_urlpathfragment_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_UrlPathFragment)


def test_applausedsl_urlpathfragment_constructor_exists():
    assert callable(applauseDsl_UrlPathFragment.__init__)


def test_applausedsl_urlpathfragment_constructor_args():
    sig = inspect.signature(applauseDsl_UrlPathFragment.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_applausedsl_urlpathfragment_has_name():
    assert hasattr(applauseDsl_UrlPathFragment, "name")
    descriptor = None
    for klass in applauseDsl_UrlPathFragment.__mro__:
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



def test_applausedsl_relativeresturl_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_RelativeRESTURL)


def test_applausedsl_relativeresturl_constructor_exists():
    assert callable(applauseDsl_RelativeRESTURL.__init__)


def test_applausedsl_relativeresturl_constructor_args():
    sig = inspect.signature(applauseDsl_RelativeRESTURL.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_urlfragment_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_UrlFragment)


def test_applausedsl_urlfragment_constructor_exists():
    assert callable(applauseDsl_UrlFragment.__init__)


def test_applausedsl_urlfragment_constructor_args():
    sig = inspect.signature(applauseDsl_UrlFragment.__init__)
    params = list(sig.parameters.keys())



def test_referrableelement_is_not_abstract():
    assert not inspect.isabstract(ReferrableElement)


def test_referrableelement_constructor_exists():
    assert callable(ReferrableElement.__init__)


def test_referrableelement_constructor_args():
    sig = inspect.signature(ReferrableElement.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_loopvariable_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_LoopVariable)


def test_applausedsl_loopvariable_constructor_exists():
    assert callable(applauseDsl_LoopVariable.__init__)


def test_applausedsl_loopvariable_constructor_args():
    sig = inspect.signature(applauseDsl_LoopVariable.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_parameter_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_Parameter)


def test_applausedsl_parameter_constructor_exists():
    assert callable(applauseDsl_Parameter.__init__)


def test_applausedsl_parameter_constructor_args():
    sig = inspect.signature(applauseDsl_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_datasourcebodyspecification_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_DataSourceBodySpecification)


def test_applausedsl_datasourcebodyspecification_constructor_exists():
    assert callable(applauseDsl_DataSourceBodySpecification.__init__)


def test_applausedsl_datasourcebodyspecification_constructor_args():
    sig = inspect.signature(applauseDsl_DataSourceBodySpecification.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_resturl_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_RESTURL)


def test_applausedsl_resturl_constructor_exists():
    assert callable(applauseDsl_RESTURL.__init__)


def test_applausedsl_resturl_constructor_args():
    sig = inspect.signature(applauseDsl_RESTURL.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_datasourceaccessmethod_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_DataSourceAccessMethod)


def test_applausedsl_datasourceaccessmethod_constructor_exists():
    assert callable(applauseDsl_DataSourceAccessMethod.__init__)


def test_applausedsl_datasourceaccessmethod_constructor_args():
    sig = inspect.signature(applauseDsl_DataSourceAccessMethod.__init__)
    params = list(sig.parameters.keys())
    assert "returnsMany" in params, "Missing parameter 'returnsMany'"
    assert "name" in params, "Missing parameter 'name'"

def test_applausedsl_datasourceaccessmethod_has_returnsMany():
    assert hasattr(applauseDsl_DataSourceAccessMethod, "returnsMany")
    descriptor = None
    for klass in applauseDsl_DataSourceAccessMethod.__mro__:
        if "returnsMany" in klass.__dict__:
            descriptor = klass.__dict__["returnsMany"]
            break
    assert isinstance(descriptor, property)

def test_applausedsl_datasourceaccessmethod_has_name():
    assert hasattr(applauseDsl_DataSourceAccessMethod, "name")
    descriptor = None
    for klass in applauseDsl_DataSourceAccessMethod.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl_absoluteresturl_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_AbsoluteRESTURL)


def test_applausedsl_absoluteresturl_constructor_exists():
    assert callable(applauseDsl_AbsoluteRESTURL.__init__)


def test_applausedsl_absoluteresturl_constructor_args():
    sig = inspect.signature(applauseDsl_AbsoluteRESTURL.__init__)
    params = list(sig.parameters.keys())
    assert "port" in params, "Missing parameter 'port'"

def test_applausedsl_absoluteresturl_has_port():
    assert hasattr(applauseDsl_AbsoluteRESTURL, "port")
    descriptor = None
    for klass in applauseDsl_AbsoluteRESTURL.__mro__:
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



def test_applausedsl_typemapping_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_TypeMapping)


def test_applausedsl_typemapping_constructor_exists():
    assert callable(applauseDsl_TypeMapping.__init__)


def test_applausedsl_typemapping_constructor_args():
    sig = inspect.signature(applauseDsl_TypeMapping.__init__)
    params = list(sig.parameters.keys())
    assert "simpleName" in params, "Missing parameter 'simpleName'"

def test_applausedsl_typemapping_has_simpleName():
    assert hasattr(applauseDsl_TypeMapping, "simpleName")
    descriptor = None
    for klass in applauseDsl_TypeMapping.__mro__:
        if "simpleName" in klass.__dict__:
            descriptor = klass.__dict__["simpleName"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl_platformmapping_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_PlatformMapping)


def test_applausedsl_platformmapping_constructor_exists():
    assert callable(applauseDsl_PlatformMapping.__init__)


def test_applausedsl_platformmapping_constructor_args():
    sig = inspect.signature(applauseDsl_PlatformMapping.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_attribute_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_Attribute)


def test_applausedsl_attribute_constructor_exists():
    assert callable(applauseDsl_Attribute.__init__)


def test_applausedsl_attribute_constructor_args():
    sig = inspect.signature(applauseDsl_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"
    assert "name" in params, "Missing parameter 'name'"

def test_applausedsl_attribute_has_many():
    assert hasattr(applauseDsl_Attribute, "many")
    descriptor = None
    for klass in applauseDsl_Attribute.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_applausedsl_attribute_has_name():
    assert hasattr(applauseDsl_Attribute, "name")
    descriptor = None
    for klass in applauseDsl_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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



def test_applausedsl_entity_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_Entity)


def test_applausedsl_entity_constructor_exists():
    assert callable(applauseDsl_Entity.__init__)


def test_applausedsl_entity_constructor_args():
    sig = inspect.signature(applauseDsl_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_applausedsl_entity_has_abstract():
    assert hasattr(applauseDsl_Entity, "abstract")
    descriptor = None
    for klass in applauseDsl_Entity.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl_datatype_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_DataType)


def test_applausedsl_datatype_constructor_exists():
    assert callable(applauseDsl_DataType.__init__)


def test_applausedsl_datatype_constructor_args():
    sig = inspect.signature(applauseDsl_DataType.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_platform_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_Platform)


def test_applausedsl_platform_constructor_exists():
    assert callable(applauseDsl_Platform.__init__)


def test_applausedsl_platform_constructor_args():
    sig = inspect.signature(applauseDsl_Platform.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_datasource_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_DataSource)


def test_applausedsl_datasource_constructor_exists():
    assert callable(applauseDsl_DataSource.__init__)


def test_applausedsl_datasource_constructor_args():
    sig = inspect.signature(applauseDsl_DataSource.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_listitemcelldeclaration_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_ListItemCellDeclaration)


def test_applausedsl_listitemcelldeclaration_constructor_exists():
    assert callable(applauseDsl_ListItemCellDeclaration.__init__)


def test_applausedsl_listitemcelldeclaration_constructor_args():
    sig = inspect.signature(applauseDsl_ListItemCellDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_screen_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_Screen)


def test_applausedsl_screen_constructor_exists():
    assert callable(applauseDsl_Screen.__init__)


def test_applausedsl_screen_constructor_args():
    sig = inspect.signature(applauseDsl_Screen.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "title" in params, "Missing parameter 'title'"

def test_applausedsl_screen_has_kind():
    assert hasattr(applauseDsl_Screen, "kind")
    descriptor = None
    for klass in applauseDsl_Screen.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_applausedsl_screen_has_title():
    assert hasattr(applauseDsl_Screen, "title")
    descriptor = None
    for klass in applauseDsl_Screen.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl_type_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_Type)


def test_applausedsl_type_constructor_exists():
    assert callable(applauseDsl_Type.__init__)


def test_applausedsl_type_constructor_args():
    sig = inspect.signature(applauseDsl_Type.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_namedelement_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_NamedElement)


def test_applausedsl_namedelement_constructor_exists():
    assert callable(applauseDsl_NamedElement.__init__)


def test_applausedsl_namedelement_constructor_args():
    sig = inspect.signature(applauseDsl_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_applausedsl_namedelement_has_name():
    assert hasattr(applauseDsl_NamedElement, "name")
    descriptor = None
    for klass in applauseDsl_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl_model_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_Model)


def test_applausedsl_model_constructor_exists():
    assert callable(applauseDsl_Model.__init__)


def test_applausedsl_model_constructor_args():
    sig = inspect.signature(applauseDsl_Model.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_attributereference_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_AttributeReference)


def test_applausedsl_attributereference_constructor_exists():
    assert callable(applauseDsl_AttributeReference.__init__)


def test_applausedsl_attributereference_constructor_args():
    sig = inspect.signature(applauseDsl_AttributeReference.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_entitymembercalltail_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_EntityMemberCallTail)


def test_applausedsl_entitymembercalltail_constructor_exists():
    assert callable(applauseDsl_EntityMemberCallTail.__init__)


def test_applausedsl_entitymembercalltail_constructor_args():
    sig = inspect.signature(applauseDsl_EntityMemberCallTail.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_stringliteral_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_StringLiteral)


def test_applausedsl_stringliteral_constructor_exists():
    assert callable(applauseDsl_StringLiteral.__init__)


def test_applausedsl_stringliteral_constructor_args():
    sig = inspect.signature(applauseDsl_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_applausedsl_stringliteral_has_value():
    assert hasattr(applauseDsl_StringLiteral, "value")
    descriptor = None
    for klass in applauseDsl_StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl_entitymembercall_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_EntityMemberCall)


def test_applausedsl_entitymembercall_constructor_exists():
    assert callable(applauseDsl_EntityMemberCall.__init__)


def test_applausedsl_entitymembercall_constructor_args():
    sig = inspect.signature(applauseDsl_EntityMemberCall.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_expression_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_Expression)


def test_applausedsl_expression_constructor_exists():
    assert callable(applauseDsl_Expression.__init__)


def test_applausedsl_expression_constructor_args():
    sig = inspect.signature(applauseDsl_Expression.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_uicomponentmembercall_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_UIComponentMemberCall)


def test_applausedsl_uicomponentmembercall_constructor_exists():
    assert callable(applauseDsl_UIComponentMemberCall.__init__)


def test_applausedsl_uicomponentmembercall_constructor_args():
    sig = inspect.signature(applauseDsl_UIComponentMemberCall.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_uicomponentordatatype_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_UIComponentOrDataType)


def test_applausedsl_uicomponentordatatype_constructor_exists():
    assert callable(applauseDsl_UIComponentOrDataType.__init__)


def test_applausedsl_uicomponentordatatype_constructor_args():
    sig = inspect.signature(applauseDsl_UIComponentOrDataType.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_uicomponentdeclaration_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_UIComponentDeclaration)


def test_applausedsl_uicomponentdeclaration_constructor_exists():
    assert callable(applauseDsl_UIComponentDeclaration.__init__)


def test_applausedsl_uicomponentdeclaration_constructor_args():
    sig = inspect.signature(applauseDsl_UIComponentDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_uicomponentmemberdeclaration_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_UIComponentMemberDeclaration)


def test_applausedsl_uicomponentmemberdeclaration_constructor_exists():
    assert callable(applauseDsl_UIComponentMemberDeclaration.__init__)


def test_applausedsl_uicomponentmemberdeclaration_constructor_args():
    sig = inspect.signature(applauseDsl_UIComponentMemberDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_applausedsl_uicomponentmemberdeclaration_has_name():
    assert hasattr(applauseDsl_UIComponentMemberDeclaration, "name")
    descriptor = None
    for klass in applauseDsl_UIComponentMemberDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl_uiactiondeleteaction_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_UIActionDeleteAction)


def test_applausedsl_uiactiondeleteaction_constructor_exists():
    assert callable(applauseDsl_UIActionDeleteAction.__init__)


def test_applausedsl_uiactiondeleteaction_constructor_args():
    sig = inspect.signature(applauseDsl_UIActionDeleteAction.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_uiaction_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_UIAction)


def test_applausedsl_uiaction_constructor_exists():
    assert callable(applauseDsl_UIAction.__init__)


def test_applausedsl_uiaction_constructor_args():
    sig = inspect.signature(applauseDsl_UIAction.__init__)
    params = list(sig.parameters.keys())
    assert "icon" in params, "Missing parameter 'icon'"
    assert "order" in params, "Missing parameter 'order'"
    assert "title" in params, "Missing parameter 'title'"
    assert "gesture" in params, "Missing parameter 'gesture'"

def test_applausedsl_uiaction_has_icon():
    assert hasattr(applauseDsl_UIAction, "icon")
    descriptor = None
    for klass in applauseDsl_UIAction.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)

def test_applausedsl_uiaction_has_order():
    assert hasattr(applauseDsl_UIAction, "order")
    descriptor = None
    for klass in applauseDsl_UIAction.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)

def test_applausedsl_uiaction_has_title():
    assert hasattr(applauseDsl_UIAction, "title")
    descriptor = None
    for klass in applauseDsl_UIAction.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_applausedsl_uiaction_has_gesture():
    assert hasattr(applauseDsl_UIAction, "gesture")
    descriptor = None
    for klass in applauseDsl_UIAction.__mro__:
        if "gesture" in klass.__dict__:
            descriptor = klass.__dict__["gesture"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl_screensection_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_ScreenSection)


def test_applausedsl_screensection_constructor_exists():
    assert callable(applauseDsl_ScreenSection.__init__)


def test_applausedsl_screensection_constructor_args():
    sig = inspect.signature(applauseDsl_ScreenSection.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_applausedsl_screensection_has_title():
    assert hasattr(applauseDsl_ScreenSection, "title")
    descriptor = None
    for klass in applauseDsl_ScreenSection.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl_datasourcecall_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_DataSourceCall)


def test_applausedsl_datasourcecall_constructor_exists():
    assert callable(applauseDsl_DataSourceCall.__init__)


def test_applausedsl_datasourcecall_constructor_args():
    sig = inspect.signature(applauseDsl_DataSourceCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_applausedsl_datasourcecall_has_name():
    assert hasattr(applauseDsl_DataSourceCall, "name")
    descriptor = None
    for klass in applauseDsl_DataSourceCall.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_screenkind_exists():
    # Check that the Enumeration exists
    assert ScreenKind is not None

def test_screenkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ScreenKind]
    expected_literals = [
        "DefaultList",
        "DefaultDetails",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ScreenKind"

def test_gesturekind_exists():
    # Check that the Enumeration exists
    assert GestureKind is not None

def test_gesturekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GestureKind]
    expected_literals = [
        "swipe",
        "longpress",
        "tap",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GestureKind"

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

def test_restverb_exists():
    # Check that the Enumeration exists
    assert RESTVerb is not None

def test_restverb_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RESTVerb]
    expected_literals = [
        "POST",
        "PUT",
        "GET",
        "DELETE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RESTVerb"

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
UIActionSpecification_strategy = st.builds(
    UIActionSpecification,
)
applauseDsl_UIActionNavigateAction_strategy = st.builds(
    applauseDsl_UIActionNavigateAction,
    actionVerb=
        safe_text
)
applauseDsl_UIActionSpecification_strategy = st.builds(
    applauseDsl_UIActionSpecification,
)
applauseDsl_ReferrableElement_strategy = st.builds(
    applauseDsl_ReferrableElement,
    name=
        safe_text
)
applauseDsl_UIComponentMemberConfiguration_strategy = st.builds(
    applauseDsl_UIComponentMemberConfiguration,
)
applauseDsl_RESTMethodCall_strategy = st.builds(
    applauseDsl_RESTMethodCall,
)
applauseDsl_ScreenListItemCell_strategy = st.builds(
    applauseDsl_ScreenListItemCell,
)
applauseDsl_ScreenSectionItems_strategy = st.builds(
    applauseDsl_ScreenSectionItems,
)
applauseDsl_RESTSpecification_strategy = st.builds(
    applauseDsl_RESTSpecification,
    verb=
        safe_text
)
UrlFragment_strategy = st.builds(
    UrlFragment,
)
applauseDsl_Variable_strategy = st.builds(
    applauseDsl_Variable,
)
applauseDsl_UrlPathFragment_strategy = st.builds(
    applauseDsl_UrlPathFragment,
    name=
        safe_text
)
RESTURL_strategy = st.builds(
    RESTURL,
)
applauseDsl_RelativeRESTURL_strategy = st.builds(
    applauseDsl_RelativeRESTURL,
)
applauseDsl_UrlFragment_strategy = st.builds(
    applauseDsl_UrlFragment,
)
ReferrableElement_strategy = st.builds(
    ReferrableElement,
)
applauseDsl_LoopVariable_strategy = st.builds(
    applauseDsl_LoopVariable,
)
applauseDsl_Parameter_strategy = st.builds(
    applauseDsl_Parameter,
)
applauseDsl_DataSourceBodySpecification_strategy = st.builds(
    applauseDsl_DataSourceBodySpecification,
)
applauseDsl_RESTURL_strategy = st.builds(
    applauseDsl_RESTURL,
)
applauseDsl_DataSourceAccessMethod_strategy = st.builds(
    applauseDsl_DataSourceAccessMethod,
    returnsMany=
        st.booleans(),
    name=
        safe_text
)
applauseDsl_AbsoluteRESTURL_strategy = st.builds(
    applauseDsl_AbsoluteRESTURL,
    port=
        st.integers()
)
PlatformMapping_strategy = st.builds(
    PlatformMapping,
)
applauseDsl_TypeMapping_strategy = st.builds(
    applauseDsl_TypeMapping,
    simpleName=
        safe_text
)
applauseDsl_PlatformMapping_strategy = st.builds(
    applauseDsl_PlatformMapping,
)
applauseDsl_Attribute_strategy = st.builds(
    applauseDsl_Attribute,
    many=
        st.booleans(),
    name=
        safe_text
)
UIComponentOrDataType_strategy = st.builds(
    UIComponentOrDataType,
)
Type_strategy = st.builds(
    Type,
)
applauseDsl_Entity_strategy = st.builds(
    applauseDsl_Entity,
    abstract=
        st.booleans()
)
applauseDsl_DataType_strategy = st.builds(
    applauseDsl_DataType,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
applauseDsl_Platform_strategy = st.builds(
    applauseDsl_Platform,
)
applauseDsl_DataSource_strategy = st.builds(
    applauseDsl_DataSource,
)
applauseDsl_ListItemCellDeclaration_strategy = st.builds(
    applauseDsl_ListItemCellDeclaration,
)
applauseDsl_Screen_strategy = st.builds(
    applauseDsl_Screen,
    kind=
        safe_text,
    title=
        safe_text
)
applauseDsl_Type_strategy = st.builds(
    applauseDsl_Type,
)
applauseDsl_NamedElement_strategy = st.builds(
    applauseDsl_NamedElement,
    name=
        safe_text
)
applauseDsl_Model_strategy = st.builds(
    applauseDsl_Model,
)
applauseDsl_AttributeReference_strategy = st.builds(
    applauseDsl_AttributeReference,
)
applauseDsl_EntityMemberCallTail_strategy = st.builds(
    applauseDsl_EntityMemberCallTail,
)
Expression_strategy = st.builds(
    Expression,
)
applauseDsl_StringLiteral_strategy = st.builds(
    applauseDsl_StringLiteral,
    value=
        safe_text
)
applauseDsl_EntityMemberCall_strategy = st.builds(
    applauseDsl_EntityMemberCall,
)
applauseDsl_Expression_strategy = st.builds(
    applauseDsl_Expression,
)
applauseDsl_UIComponentMemberCall_strategy = st.builds(
    applauseDsl_UIComponentMemberCall,
)
applauseDsl_UIComponentOrDataType_strategy = st.builds(
    applauseDsl_UIComponentOrDataType,
)
applauseDsl_UIComponentDeclaration_strategy = st.builds(
    applauseDsl_UIComponentDeclaration,
)
applauseDsl_UIComponentMemberDeclaration_strategy = st.builds(
    applauseDsl_UIComponentMemberDeclaration,
    name=
        safe_text
)
applauseDsl_UIActionDeleteAction_strategy = st.builds(
    applauseDsl_UIActionDeleteAction,
)
applauseDsl_UIAction_strategy = st.builds(
    applauseDsl_UIAction,
    icon=
        safe_text,
    order=
        st.integers(),
    title=
        safe_text,
    gesture=
        safe_text
)
applauseDsl_ScreenSection_strategy = st.builds(
    applauseDsl_ScreenSection,
    title=
        safe_text
)
applauseDsl_DataSourceCall_strategy = st.builds(
    applauseDsl_DataSourceCall,
    name=
        safe_text
)

@given(instance=UIActionSpecification_strategy)
@settings(max_examples=50)
def test_uiactionspecification_instantiation(instance):
    assert isinstance(instance, UIActionSpecification)

@given(instance=applauseDsl_UIActionNavigateAction_strategy)
@settings(max_examples=50)
def test_applausedsl_uiactionnavigateaction_instantiation(instance):
    assert isinstance(instance, applauseDsl_UIActionNavigateAction)



@given(instance=applauseDsl_UIActionNavigateAction_strategy)
def test_applausedsl_uiactionnavigateaction_actionVerb_setter(instance):
    original = instance.actionVerb
    instance.actionVerb = original
    assert instance.actionVerb == original

@given(instance=applauseDsl_UIActionSpecification_strategy)
@settings(max_examples=50)
def test_applausedsl_uiactionspecification_instantiation(instance):
    assert isinstance(instance, applauseDsl_UIActionSpecification)

@given(instance=applauseDsl_ReferrableElement_strategy)
@settings(max_examples=50)
def test_applausedsl_referrableelement_instantiation(instance):
    assert isinstance(instance, applauseDsl_ReferrableElement)



@given(instance=applauseDsl_ReferrableElement_strategy)
def test_applausedsl_referrableelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=applauseDsl_UIComponentMemberConfiguration_strategy)
@settings(max_examples=50)
def test_applausedsl_uicomponentmemberconfiguration_instantiation(instance):
    assert isinstance(instance, applauseDsl_UIComponentMemberConfiguration)

@given(instance=applauseDsl_RESTMethodCall_strategy)
@settings(max_examples=50)
def test_applausedsl_restmethodcall_instantiation(instance):
    assert isinstance(instance, applauseDsl_RESTMethodCall)

@given(instance=applauseDsl_ScreenListItemCell_strategy)
@settings(max_examples=50)
def test_applausedsl_screenlistitemcell_instantiation(instance):
    assert isinstance(instance, applauseDsl_ScreenListItemCell)

@given(instance=applauseDsl_ScreenSectionItems_strategy)
@settings(max_examples=50)
def test_applausedsl_screensectionitems_instantiation(instance):
    assert isinstance(instance, applauseDsl_ScreenSectionItems)

@given(instance=applauseDsl_RESTSpecification_strategy)
@settings(max_examples=50)
def test_applausedsl_restspecification_instantiation(instance):
    assert isinstance(instance, applauseDsl_RESTSpecification)



@given(instance=applauseDsl_RESTSpecification_strategy)
def test_applausedsl_restspecification_verb_setter(instance):
    original = instance.verb
    instance.verb = original
    assert instance.verb == original

@given(instance=UrlFragment_strategy)
@settings(max_examples=50)
def test_urlfragment_instantiation(instance):
    assert isinstance(instance, UrlFragment)

@given(instance=applauseDsl_Variable_strategy)
@settings(max_examples=50)
def test_applausedsl_variable_instantiation(instance):
    assert isinstance(instance, applauseDsl_Variable)

@given(instance=applauseDsl_UrlPathFragment_strategy)
@settings(max_examples=50)
def test_applausedsl_urlpathfragment_instantiation(instance):
    assert isinstance(instance, applauseDsl_UrlPathFragment)



@given(instance=applauseDsl_UrlPathFragment_strategy)
def test_applausedsl_urlpathfragment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RESTURL_strategy)
@settings(max_examples=50)
def test_resturl_instantiation(instance):
    assert isinstance(instance, RESTURL)

@given(instance=applauseDsl_RelativeRESTURL_strategy)
@settings(max_examples=50)
def test_applausedsl_relativeresturl_instantiation(instance):
    assert isinstance(instance, applauseDsl_RelativeRESTURL)

@given(instance=applauseDsl_UrlFragment_strategy)
@settings(max_examples=50)
def test_applausedsl_urlfragment_instantiation(instance):
    assert isinstance(instance, applauseDsl_UrlFragment)

@given(instance=ReferrableElement_strategy)
@settings(max_examples=50)
def test_referrableelement_instantiation(instance):
    assert isinstance(instance, ReferrableElement)

@given(instance=applauseDsl_LoopVariable_strategy)
@settings(max_examples=50)
def test_applausedsl_loopvariable_instantiation(instance):
    assert isinstance(instance, applauseDsl_LoopVariable)

@given(instance=applauseDsl_Parameter_strategy)
@settings(max_examples=50)
def test_applausedsl_parameter_instantiation(instance):
    assert isinstance(instance, applauseDsl_Parameter)

@given(instance=applauseDsl_DataSourceBodySpecification_strategy)
@settings(max_examples=50)
def test_applausedsl_datasourcebodyspecification_instantiation(instance):
    assert isinstance(instance, applauseDsl_DataSourceBodySpecification)

@given(instance=applauseDsl_RESTURL_strategy)
@settings(max_examples=50)
def test_applausedsl_resturl_instantiation(instance):
    assert isinstance(instance, applauseDsl_RESTURL)

@given(instance=applauseDsl_DataSourceAccessMethod_strategy)
@settings(max_examples=50)
def test_applausedsl_datasourceaccessmethod_instantiation(instance):
    assert isinstance(instance, applauseDsl_DataSourceAccessMethod)



@given(instance=applauseDsl_DataSourceAccessMethod_strategy)
def test_applausedsl_datasourceaccessmethod_returnsMany_setter(instance):
    original = instance.returnsMany
    instance.returnsMany = original
    assert instance.returnsMany == original



@given(instance=applauseDsl_DataSourceAccessMethod_strategy)
def test_applausedsl_datasourceaccessmethod_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=applauseDsl_AbsoluteRESTURL_strategy)
@settings(max_examples=50)
def test_applausedsl_absoluteresturl_instantiation(instance):
    assert isinstance(instance, applauseDsl_AbsoluteRESTURL)



@given(instance=applauseDsl_AbsoluteRESTURL_strategy)
def test_applausedsl_absoluteresturl_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original

@given(instance=PlatformMapping_strategy)
@settings(max_examples=50)
def test_platformmapping_instantiation(instance):
    assert isinstance(instance, PlatformMapping)

@given(instance=applauseDsl_TypeMapping_strategy)
@settings(max_examples=50)
def test_applausedsl_typemapping_instantiation(instance):
    assert isinstance(instance, applauseDsl_TypeMapping)



@given(instance=applauseDsl_TypeMapping_strategy)
def test_applausedsl_typemapping_simpleName_setter(instance):
    original = instance.simpleName
    instance.simpleName = original
    assert instance.simpleName == original

@given(instance=applauseDsl_PlatformMapping_strategy)
@settings(max_examples=50)
def test_applausedsl_platformmapping_instantiation(instance):
    assert isinstance(instance, applauseDsl_PlatformMapping)

@given(instance=applauseDsl_Attribute_strategy)
@settings(max_examples=50)
def test_applausedsl_attribute_instantiation(instance):
    assert isinstance(instance, applauseDsl_Attribute)



@given(instance=applauseDsl_Attribute_strategy)
def test_applausedsl_attribute_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original



@given(instance=applauseDsl_Attribute_strategy)
def test_applausedsl_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UIComponentOrDataType_strategy)
@settings(max_examples=50)
def test_uicomponentordatatype_instantiation(instance):
    assert isinstance(instance, UIComponentOrDataType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=applauseDsl_Entity_strategy)
@settings(max_examples=50)
def test_applausedsl_entity_instantiation(instance):
    assert isinstance(instance, applauseDsl_Entity)



@given(instance=applauseDsl_Entity_strategy)
def test_applausedsl_entity_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=applauseDsl_DataType_strategy)
@settings(max_examples=50)
def test_applausedsl_datatype_instantiation(instance):
    assert isinstance(instance, applauseDsl_DataType)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=applauseDsl_Platform_strategy)
@settings(max_examples=50)
def test_applausedsl_platform_instantiation(instance):
    assert isinstance(instance, applauseDsl_Platform)

@given(instance=applauseDsl_DataSource_strategy)
@settings(max_examples=50)
def test_applausedsl_datasource_instantiation(instance):
    assert isinstance(instance, applauseDsl_DataSource)

@given(instance=applauseDsl_ListItemCellDeclaration_strategy)
@settings(max_examples=50)
def test_applausedsl_listitemcelldeclaration_instantiation(instance):
    assert isinstance(instance, applauseDsl_ListItemCellDeclaration)

@given(instance=applauseDsl_Screen_strategy)
@settings(max_examples=50)
def test_applausedsl_screen_instantiation(instance):
    assert isinstance(instance, applauseDsl_Screen)



@given(instance=applauseDsl_Screen_strategy)
def test_applausedsl_screen_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=applauseDsl_Screen_strategy)
def test_applausedsl_screen_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=applauseDsl_Type_strategy)
@settings(max_examples=50)
def test_applausedsl_type_instantiation(instance):
    assert isinstance(instance, applauseDsl_Type)

@given(instance=applauseDsl_NamedElement_strategy)
@settings(max_examples=50)
def test_applausedsl_namedelement_instantiation(instance):
    assert isinstance(instance, applauseDsl_NamedElement)



@given(instance=applauseDsl_NamedElement_strategy)
def test_applausedsl_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=applauseDsl_Model_strategy)
@settings(max_examples=50)
def test_applausedsl_model_instantiation(instance):
    assert isinstance(instance, applauseDsl_Model)

@given(instance=applauseDsl_AttributeReference_strategy)
@settings(max_examples=50)
def test_applausedsl_attributereference_instantiation(instance):
    assert isinstance(instance, applauseDsl_AttributeReference)

@given(instance=applauseDsl_EntityMemberCallTail_strategy)
@settings(max_examples=50)
def test_applausedsl_entitymembercalltail_instantiation(instance):
    assert isinstance(instance, applauseDsl_EntityMemberCallTail)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=applauseDsl_StringLiteral_strategy)
@settings(max_examples=50)
def test_applausedsl_stringliteral_instantiation(instance):
    assert isinstance(instance, applauseDsl_StringLiteral)



@given(instance=applauseDsl_StringLiteral_strategy)
def test_applausedsl_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=applauseDsl_EntityMemberCall_strategy)
@settings(max_examples=50)
def test_applausedsl_entitymembercall_instantiation(instance):
    assert isinstance(instance, applauseDsl_EntityMemberCall)

@given(instance=applauseDsl_Expression_strategy)
@settings(max_examples=50)
def test_applausedsl_expression_instantiation(instance):
    assert isinstance(instance, applauseDsl_Expression)

@given(instance=applauseDsl_UIComponentMemberCall_strategy)
@settings(max_examples=50)
def test_applausedsl_uicomponentmembercall_instantiation(instance):
    assert isinstance(instance, applauseDsl_UIComponentMemberCall)

@given(instance=applauseDsl_UIComponentOrDataType_strategy)
@settings(max_examples=50)
def test_applausedsl_uicomponentordatatype_instantiation(instance):
    assert isinstance(instance, applauseDsl_UIComponentOrDataType)

@given(instance=applauseDsl_UIComponentDeclaration_strategy)
@settings(max_examples=50)
def test_applausedsl_uicomponentdeclaration_instantiation(instance):
    assert isinstance(instance, applauseDsl_UIComponentDeclaration)

@given(instance=applauseDsl_UIComponentMemberDeclaration_strategy)
@settings(max_examples=50)
def test_applausedsl_uicomponentmemberdeclaration_instantiation(instance):
    assert isinstance(instance, applauseDsl_UIComponentMemberDeclaration)



@given(instance=applauseDsl_UIComponentMemberDeclaration_strategy)
def test_applausedsl_uicomponentmemberdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=applauseDsl_UIActionDeleteAction_strategy)
@settings(max_examples=50)
def test_applausedsl_uiactiondeleteaction_instantiation(instance):
    assert isinstance(instance, applauseDsl_UIActionDeleteAction)

@given(instance=applauseDsl_UIAction_strategy)
@settings(max_examples=50)
def test_applausedsl_uiaction_instantiation(instance):
    assert isinstance(instance, applauseDsl_UIAction)



@given(instance=applauseDsl_UIAction_strategy)
def test_applausedsl_uiaction_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original



@given(instance=applauseDsl_UIAction_strategy)
def test_applausedsl_uiaction_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original



@given(instance=applauseDsl_UIAction_strategy)
def test_applausedsl_uiaction_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=applauseDsl_UIAction_strategy)
def test_applausedsl_uiaction_gesture_setter(instance):
    original = instance.gesture
    instance.gesture = original
    assert instance.gesture == original

@given(instance=applauseDsl_ScreenSection_strategy)
@settings(max_examples=50)
def test_applausedsl_screensection_instantiation(instance):
    assert isinstance(instance, applauseDsl_ScreenSection)



@given(instance=applauseDsl_ScreenSection_strategy)
def test_applausedsl_screensection_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=applauseDsl_DataSourceCall_strategy)
@settings(max_examples=50)
def test_applausedsl_datasourcecall_instantiation(instance):
    assert isinstance(instance, applauseDsl_DataSourceCall)



@given(instance=applauseDsl_DataSourceCall_strategy)
def test_applausedsl_datasourcecall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
