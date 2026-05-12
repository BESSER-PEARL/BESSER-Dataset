import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    CollectionFunction,
    applauseDsl_StringSplit,
    StringFunction,
    applauseDsl_StringUrlConform,
    applauseDsl_StringReplace,
    applauseDsl_StringConcat,
    applauseDsl_ViewAction,
    ViewAction,
    applauseDsl_ExternalOpen,
    applauseDsl_ActionDelegate,
    applauseDsl_ViewHeader,
    SectionedView,
    applauseDsl_DetailsView,
    applauseDsl_TableView,
    applauseDsl_ViewSection,
    applauseDsl_ViewForAllSections,
    View,
    applauseDsl_CustomView,
    applauseDsl_WebView,
    applauseDsl_SectionedView,
    applauseDsl_SectionCell,
    applauseDsl_ProviderConstruction,
    applauseDsl_Button,
    applauseDsl_ViewCall,
    PredefinedParameter,
    applauseDsl_SectionId,
    applauseDsl_PredefinedParameter,
    applauseDsl_CollectionExpression,
    applauseDsl_Expression,
    CollectionExpression,
    ScalarExpression,
    Expression,
    applauseDsl_CollectionLiteral,
    applauseDsl_StringLiteral,
    applauseDsl_StringFunction,
    applauseDsl_CollectionFunction,
    applauseDsl_ObjectReference,
    VariableDeclaration,
    applauseDsl_Property,
    applauseDsl_CollectionIterator,
    applauseDsl_Constant,
    applauseDsl_Parameter,
    Type,
    applauseDsl_Entity,
    applauseDsl_SimpleType,
    ModelElement,
    applauseDsl_View,
    applauseDsl_ContentProvider,
    applauseDsl_NavigationBarItem,
    applauseDsl_ModelElement,
    applauseDsl_Application,
    applauseDsl_ApplauseModel,
    applauseDsl_Type,
    applauseDsl_TypeDescription,
    applauseDsl_VariableDeclaration,
    applauseDsl_ScalarExpression,
    Position,
    CellType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_collectionfunction_is_not_abstract():
    assert not inspect.isabstract(CollectionFunction)


def test_collectionfunction_constructor_exists():
    assert callable(CollectionFunction.__init__)


def test_collectionfunction_constructor_args():
    sig = inspect.signature(CollectionFunction.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_stringsplit_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_StringSplit)


def test_applausedsl_stringsplit_constructor_exists():
    assert callable(applauseDsl_StringSplit.__init__)


def test_applausedsl_stringsplit_constructor_args():
    sig = inspect.signature(applauseDsl_StringSplit.__init__)
    params = list(sig.parameters.keys())



def test_stringfunction_is_not_abstract():
    assert not inspect.isabstract(StringFunction)


def test_stringfunction_constructor_exists():
    assert callable(StringFunction.__init__)


def test_stringfunction_constructor_args():
    sig = inspect.signature(StringFunction.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_stringurlconform_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_StringUrlConform)


def test_applausedsl_stringurlconform_constructor_exists():
    assert callable(applauseDsl_StringUrlConform.__init__)


def test_applausedsl_stringurlconform_constructor_args():
    sig = inspect.signature(applauseDsl_StringUrlConform.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_stringreplace_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_StringReplace)


def test_applausedsl_stringreplace_constructor_exists():
    assert callable(applauseDsl_StringReplace.__init__)


def test_applausedsl_stringreplace_constructor_args():
    sig = inspect.signature(applauseDsl_StringReplace.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_stringconcat_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_StringConcat)


def test_applausedsl_stringconcat_constructor_exists():
    assert callable(applauseDsl_StringConcat.__init__)


def test_applausedsl_stringconcat_constructor_args():
    sig = inspect.signature(applauseDsl_StringConcat.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_viewaction_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_ViewAction)


def test_applausedsl_viewaction_constructor_exists():
    assert callable(applauseDsl_ViewAction.__init__)


def test_applausedsl_viewaction_constructor_args():
    sig = inspect.signature(applauseDsl_ViewAction.__init__)
    params = list(sig.parameters.keys())



def test_viewaction_is_not_abstract():
    assert not inspect.isabstract(ViewAction)


def test_viewaction_constructor_exists():
    assert callable(ViewAction.__init__)


def test_viewaction_constructor_args():
    sig = inspect.signature(ViewAction.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_externalopen_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_ExternalOpen)


def test_applausedsl_externalopen_constructor_exists():
    assert callable(applauseDsl_ExternalOpen.__init__)


def test_applausedsl_externalopen_constructor_args():
    sig = inspect.signature(applauseDsl_ExternalOpen.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_actiondelegate_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_ActionDelegate)


def test_applausedsl_actiondelegate_constructor_exists():
    assert callable(applauseDsl_ActionDelegate.__init__)


def test_applausedsl_actiondelegate_constructor_args():
    sig = inspect.signature(applauseDsl_ActionDelegate.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_viewheader_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_ViewHeader)


def test_applausedsl_viewheader_constructor_exists():
    assert callable(applauseDsl_ViewHeader.__init__)


def test_applausedsl_viewheader_constructor_args():
    sig = inspect.signature(applauseDsl_ViewHeader.__init__)
    params = list(sig.parameters.keys())



def test_sectionedview_is_not_abstract():
    assert not inspect.isabstract(SectionedView)


def test_sectionedview_constructor_exists():
    assert callable(SectionedView.__init__)


def test_sectionedview_constructor_args():
    sig = inspect.signature(SectionedView.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_detailsview_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_DetailsView)


def test_applausedsl_detailsview_constructor_exists():
    assert callable(applauseDsl_DetailsView.__init__)


def test_applausedsl_detailsview_constructor_args():
    sig = inspect.signature(applauseDsl_DetailsView.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_tableview_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_TableView)


def test_applausedsl_tableview_constructor_exists():
    assert callable(applauseDsl_TableView.__init__)


def test_applausedsl_tableview_constructor_args():
    sig = inspect.signature(applauseDsl_TableView.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_viewsection_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_ViewSection)


def test_applausedsl_viewsection_constructor_exists():
    assert callable(applauseDsl_ViewSection.__init__)


def test_applausedsl_viewsection_constructor_args():
    sig = inspect.signature(applauseDsl_ViewSection.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_viewforallsections_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_ViewForAllSections)


def test_applausedsl_viewforallsections_constructor_exists():
    assert callable(applauseDsl_ViewForAllSections.__init__)


def test_applausedsl_viewforallsections_constructor_args():
    sig = inspect.signature(applauseDsl_ViewForAllSections.__init__)
    params = list(sig.parameters.keys())



def test_view_is_not_abstract():
    assert not inspect.isabstract(View)


def test_view_constructor_exists():
    assert callable(View.__init__)


def test_view_constructor_args():
    sig = inspect.signature(View.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_customview_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_CustomView)


def test_applausedsl_customview_constructor_exists():
    assert callable(applauseDsl_CustomView.__init__)


def test_applausedsl_customview_constructor_args():
    sig = inspect.signature(applauseDsl_CustomView.__init__)
    params = list(sig.parameters.keys())
    assert "objclass" in params, "Missing parameter 'objclass'"

def test_applausedsl_customview_has_objclass():
    assert hasattr(applauseDsl_CustomView, "objclass")
    descriptor = None
    for klass in applauseDsl_CustomView.__mro__:
        if "objclass" in klass.__dict__:
            descriptor = klass.__dict__["objclass"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl_webview_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_WebView)


def test_applausedsl_webview_constructor_exists():
    assert callable(applauseDsl_WebView.__init__)


def test_applausedsl_webview_constructor_args():
    sig = inspect.signature(applauseDsl_WebView.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_sectionedview_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_SectionedView)


def test_applausedsl_sectionedview_constructor_exists():
    assert callable(applauseDsl_SectionedView.__init__)


def test_applausedsl_sectionedview_constructor_args():
    sig = inspect.signature(applauseDsl_SectionedView.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_sectioncell_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_SectionCell)


def test_applausedsl_sectioncell_constructor_exists():
    assert callable(applauseDsl_SectionCell.__init__)


def test_applausedsl_sectioncell_constructor_args():
    sig = inspect.signature(applauseDsl_SectionCell.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_applausedsl_sectioncell_has_type():
    assert hasattr(applauseDsl_SectionCell, "type")
    descriptor = None
    for klass in applauseDsl_SectionCell.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl_providerconstruction_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_ProviderConstruction)


def test_applausedsl_providerconstruction_constructor_exists():
    assert callable(applauseDsl_ProviderConstruction.__init__)


def test_applausedsl_providerconstruction_constructor_args():
    sig = inspect.signature(applauseDsl_ProviderConstruction.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_button_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_Button)


def test_applausedsl_button_constructor_exists():
    assert callable(applauseDsl_Button.__init__)


def test_applausedsl_button_constructor_args():
    sig = inspect.signature(applauseDsl_Button.__init__)
    params = list(sig.parameters.keys())
    assert "handler" in params, "Missing parameter 'handler'"

def test_applausedsl_button_has_handler():
    assert hasattr(applauseDsl_Button, "handler")
    descriptor = None
    for klass in applauseDsl_Button.__mro__:
        if "handler" in klass.__dict__:
            descriptor = klass.__dict__["handler"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl_viewcall_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_ViewCall)


def test_applausedsl_viewcall_constructor_exists():
    assert callable(applauseDsl_ViewCall.__init__)


def test_applausedsl_viewcall_constructor_args():
    sig = inspect.signature(applauseDsl_ViewCall.__init__)
    params = list(sig.parameters.keys())



def test_predefinedparameter_is_not_abstract():
    assert not inspect.isabstract(PredefinedParameter)


def test_predefinedparameter_constructor_exists():
    assert callable(PredefinedParameter.__init__)


def test_predefinedparameter_constructor_args():
    sig = inspect.signature(PredefinedParameter.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_sectionid_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_SectionId)


def test_applausedsl_sectionid_constructor_exists():
    assert callable(applauseDsl_SectionId.__init__)


def test_applausedsl_sectionid_constructor_args():
    sig = inspect.signature(applauseDsl_SectionId.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_predefinedparameter_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_PredefinedParameter)


def test_applausedsl_predefinedparameter_constructor_exists():
    assert callable(applauseDsl_PredefinedParameter.__init__)


def test_applausedsl_predefinedparameter_constructor_args():
    sig = inspect.signature(applauseDsl_PredefinedParameter.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_collectionexpression_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_CollectionExpression)


def test_applausedsl_collectionexpression_constructor_exists():
    assert callable(applauseDsl_CollectionExpression.__init__)


def test_applausedsl_collectionexpression_constructor_args():
    sig = inspect.signature(applauseDsl_CollectionExpression.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_expression_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_Expression)


def test_applausedsl_expression_constructor_exists():
    assert callable(applauseDsl_Expression.__init__)


def test_applausedsl_expression_constructor_args():
    sig = inspect.signature(applauseDsl_Expression.__init__)
    params = list(sig.parameters.keys())



def test_collectionexpression_is_not_abstract():
    assert not inspect.isabstract(CollectionExpression)


def test_collectionexpression_constructor_exists():
    assert callable(CollectionExpression.__init__)


def test_collectionexpression_constructor_args():
    sig = inspect.signature(CollectionExpression.__init__)
    params = list(sig.parameters.keys())



def test_scalarexpression_is_not_abstract():
    assert not inspect.isabstract(ScalarExpression)


def test_scalarexpression_constructor_exists():
    assert callable(ScalarExpression.__init__)


def test_scalarexpression_constructor_args():
    sig = inspect.signature(ScalarExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_collectionliteral_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_CollectionLiteral)


def test_applausedsl_collectionliteral_constructor_exists():
    assert callable(applauseDsl_CollectionLiteral.__init__)


def test_applausedsl_collectionliteral_constructor_args():
    sig = inspect.signature(applauseDsl_CollectionLiteral.__init__)
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



def test_applausedsl_stringfunction_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_StringFunction)


def test_applausedsl_stringfunction_constructor_exists():
    assert callable(applauseDsl_StringFunction.__init__)


def test_applausedsl_stringfunction_constructor_args():
    sig = inspect.signature(applauseDsl_StringFunction.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_collectionfunction_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_CollectionFunction)


def test_applausedsl_collectionfunction_constructor_exists():
    assert callable(applauseDsl_CollectionFunction.__init__)


def test_applausedsl_collectionfunction_constructor_args():
    sig = inspect.signature(applauseDsl_CollectionFunction.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_objectreference_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_ObjectReference)


def test_applausedsl_objectreference_constructor_exists():
    assert callable(applauseDsl_ObjectReference.__init__)


def test_applausedsl_objectreference_constructor_args():
    sig = inspect.signature(applauseDsl_ObjectReference.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_property_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_Property)


def test_applausedsl_property_constructor_exists():
    assert callable(applauseDsl_Property.__init__)


def test_applausedsl_property_constructor_args():
    sig = inspect.signature(applauseDsl_Property.__init__)
    params = list(sig.parameters.keys())
    assert "derived" in params, "Missing parameter 'derived'"

def test_applausedsl_property_has_derived():
    assert hasattr(applauseDsl_Property, "derived")
    descriptor = None
    for klass in applauseDsl_Property.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl_collectioniterator_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_CollectionIterator)


def test_applausedsl_collectioniterator_constructor_exists():
    assert callable(applauseDsl_CollectionIterator.__init__)


def test_applausedsl_collectioniterator_constructor_args():
    sig = inspect.signature(applauseDsl_CollectionIterator.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_constant_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_Constant)


def test_applausedsl_constant_constructor_exists():
    assert callable(applauseDsl_Constant.__init__)


def test_applausedsl_constant_constructor_args():
    sig = inspect.signature(applauseDsl_Constant.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"

def test_applausedsl_constant_has_language():
    assert hasattr(applauseDsl_Constant, "language")
    descriptor = None
    for klass in applauseDsl_Constant.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl_parameter_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_Parameter)


def test_applausedsl_parameter_constructor_exists():
    assert callable(applauseDsl_Parameter.__init__)


def test_applausedsl_parameter_constructor_args():
    sig = inspect.signature(applauseDsl_Parameter.__init__)
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



def test_applausedsl_simpletype_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_SimpleType)


def test_applausedsl_simpletype_constructor_exists():
    assert callable(applauseDsl_SimpleType.__init__)


def test_applausedsl_simpletype_constructor_args():
    sig = inspect.signature(applauseDsl_SimpleType.__init__)
    params = list(sig.parameters.keys())
    assert "platformType" in params, "Missing parameter 'platformType'"

def test_applausedsl_simpletype_has_platformType():
    assert hasattr(applauseDsl_SimpleType, "platformType")
    descriptor = None
    for klass in applauseDsl_SimpleType.__mro__:
        if "platformType" in klass.__dict__:
            descriptor = klass.__dict__["platformType"]
            break
    assert isinstance(descriptor, property)



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_view_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_View)


def test_applausedsl_view_constructor_exists():
    assert callable(applauseDsl_View.__init__)


def test_applausedsl_view_constructor_args():
    sig = inspect.signature(applauseDsl_View.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_applausedsl_view_has_name():
    assert hasattr(applauseDsl_View, "name")
    descriptor = None
    for klass in applauseDsl_View.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl_contentprovider_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_ContentProvider)


def test_applausedsl_contentprovider_constructor_exists():
    assert callable(applauseDsl_ContentProvider.__init__)


def test_applausedsl_contentprovider_constructor_args():
    sig = inspect.signature(applauseDsl_ContentProvider.__init__)
    params = list(sig.parameters.keys())
    assert "xml" in params, "Missing parameter 'xml'"
    assert "html" in params, "Missing parameter 'html'"
    assert "many" in params, "Missing parameter 'many'"
    assert "resolver" in params, "Missing parameter 'resolver'"
    assert "name" in params, "Missing parameter 'name'"

def test_applausedsl_contentprovider_has_xml():
    assert hasattr(applauseDsl_ContentProvider, "xml")
    descriptor = None
    for klass in applauseDsl_ContentProvider.__mro__:
        if "xml" in klass.__dict__:
            descriptor = klass.__dict__["xml"]
            break
    assert isinstance(descriptor, property)

def test_applausedsl_contentprovider_has_html():
    assert hasattr(applauseDsl_ContentProvider, "html")
    descriptor = None
    for klass in applauseDsl_ContentProvider.__mro__:
        if "html" in klass.__dict__:
            descriptor = klass.__dict__["html"]
            break
    assert isinstance(descriptor, property)

def test_applausedsl_contentprovider_has_many():
    assert hasattr(applauseDsl_ContentProvider, "many")
    descriptor = None
    for klass in applauseDsl_ContentProvider.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_applausedsl_contentprovider_has_resolver():
    assert hasattr(applauseDsl_ContentProvider, "resolver")
    descriptor = None
    for klass in applauseDsl_ContentProvider.__mro__:
        if "resolver" in klass.__dict__:
            descriptor = klass.__dict__["resolver"]
            break
    assert isinstance(descriptor, property)

def test_applausedsl_contentprovider_has_name():
    assert hasattr(applauseDsl_ContentProvider, "name")
    descriptor = None
    for klass in applauseDsl_ContentProvider.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl_navigationbaritem_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_NavigationBarItem)


def test_applausedsl_navigationbaritem_constructor_exists():
    assert callable(applauseDsl_NavigationBarItem.__init__)


def test_applausedsl_navigationbaritem_constructor_args():
    sig = inspect.signature(applauseDsl_NavigationBarItem.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_applausedsl_navigationbaritem_has_position():
    assert hasattr(applauseDsl_NavigationBarItem, "position")
    descriptor = None
    for klass in applauseDsl_NavigationBarItem.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl_modelelement_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_ModelElement)


def test_applausedsl_modelelement_constructor_exists():
    assert callable(applauseDsl_ModelElement.__init__)


def test_applausedsl_modelelement_constructor_args():
    sig = inspect.signature(applauseDsl_ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_application_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_Application)


def test_applausedsl_application_constructor_exists():
    assert callable(applauseDsl_Application.__init__)


def test_applausedsl_application_constructor_args():
    sig = inspect.signature(applauseDsl_Application.__init__)
    params = list(sig.parameters.keys())
    assert "tabbarApplication" in params, "Missing parameter 'tabbarApplication'"
    assert "name" in params, "Missing parameter 'name'"

def test_applausedsl_application_has_tabbarApplication():
    assert hasattr(applauseDsl_Application, "tabbarApplication")
    descriptor = None
    for klass in applauseDsl_Application.__mro__:
        if "tabbarApplication" in klass.__dict__:
            descriptor = klass.__dict__["tabbarApplication"]
            break
    assert isinstance(descriptor, property)

def test_applausedsl_application_has_name():
    assert hasattr(applauseDsl_Application, "name")
    descriptor = None
    for klass in applauseDsl_Application.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl_applausemodel_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_ApplauseModel)


def test_applausedsl_applausemodel_constructor_exists():
    assert callable(applauseDsl_ApplauseModel.__init__)


def test_applausedsl_applausemodel_constructor_args():
    sig = inspect.signature(applauseDsl_ApplauseModel.__init__)
    params = list(sig.parameters.keys())



def test_applausedsl_type_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_Type)


def test_applausedsl_type_constructor_exists():
    assert callable(applauseDsl_Type.__init__)


def test_applausedsl_type_constructor_args():
    sig = inspect.signature(applauseDsl_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_applausedsl_type_has_name():
    assert hasattr(applauseDsl_Type, "name")
    descriptor = None
    for klass in applauseDsl_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl_typedescription_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_TypeDescription)


def test_applausedsl_typedescription_constructor_exists():
    assert callable(applauseDsl_TypeDescription.__init__)


def test_applausedsl_typedescription_constructor_args():
    sig = inspect.signature(applauseDsl_TypeDescription.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"

def test_applausedsl_typedescription_has_many():
    assert hasattr(applauseDsl_TypeDescription, "many")
    descriptor = None
    for klass in applauseDsl_TypeDescription.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_VariableDeclaration)


def test_applausedsl_variabledeclaration_constructor_exists():
    assert callable(applauseDsl_VariableDeclaration.__init__)


def test_applausedsl_variabledeclaration_constructor_args():
    sig = inspect.signature(applauseDsl_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_applausedsl_variabledeclaration_has_name():
    assert hasattr(applauseDsl_VariableDeclaration, "name")
    descriptor = None
    for klass in applauseDsl_VariableDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_applausedsl_scalarexpression_is_not_abstract():
    assert not inspect.isabstract(applauseDsl_ScalarExpression)


def test_applausedsl_scalarexpression_constructor_exists():
    assert callable(applauseDsl_ScalarExpression.__init__)


def test_applausedsl_scalarexpression_constructor_args():
    sig = inspect.signature(applauseDsl_ScalarExpression.__init__)
    params = list(sig.parameters.keys())

def test_position_exists():
    # Check that the Enumeration exists
    assert Position is not None

def test_position_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Position]
    expected_literals = [
        "center",
        "right",
        "default",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Position"

def test_celltype_exists():
    # Check that the Enumeration exists
    assert CellType is not None

def test_celltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CellType]
    expected_literals = [
        "defaultWithDisclosure",
        "value2",
        "double",
        "subtitle",
        "default",
        "maps",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CellType"


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
CollectionFunction_strategy = st.builds(
    CollectionFunction,
)
applauseDsl_StringSplit_strategy = st.builds(
    applauseDsl_StringSplit,
)
StringFunction_strategy = st.builds(
    StringFunction,
)
applauseDsl_StringUrlConform_strategy = st.builds(
    applauseDsl_StringUrlConform,
)
applauseDsl_StringReplace_strategy = st.builds(
    applauseDsl_StringReplace,
)
applauseDsl_StringConcat_strategy = st.builds(
    applauseDsl_StringConcat,
)
applauseDsl_ViewAction_strategy = st.builds(
    applauseDsl_ViewAction,
)
ViewAction_strategy = st.builds(
    ViewAction,
)
applauseDsl_ExternalOpen_strategy = st.builds(
    applauseDsl_ExternalOpen,
)
applauseDsl_ActionDelegate_strategy = st.builds(
    applauseDsl_ActionDelegate,
)
applauseDsl_ViewHeader_strategy = st.builds(
    applauseDsl_ViewHeader,
)
SectionedView_strategy = st.builds(
    SectionedView,
)
applauseDsl_DetailsView_strategy = st.builds(
    applauseDsl_DetailsView,
)
applauseDsl_TableView_strategy = st.builds(
    applauseDsl_TableView,
)
applauseDsl_ViewSection_strategy = st.builds(
    applauseDsl_ViewSection,
)
applauseDsl_ViewForAllSections_strategy = st.builds(
    applauseDsl_ViewForAllSections,
)
View_strategy = st.builds(
    View,
)
applauseDsl_CustomView_strategy = st.builds(
    applauseDsl_CustomView,
    objclass=
        safe_text
)
applauseDsl_WebView_strategy = st.builds(
    applauseDsl_WebView,
)
applauseDsl_SectionedView_strategy = st.builds(
    applauseDsl_SectionedView,
)
applauseDsl_SectionCell_strategy = st.builds(
    applauseDsl_SectionCell,
    type=
        safe_text
)
applauseDsl_ProviderConstruction_strategy = st.builds(
    applauseDsl_ProviderConstruction,
)
applauseDsl_Button_strategy = st.builds(
    applauseDsl_Button,
    handler=
        safe_text
)
applauseDsl_ViewCall_strategy = st.builds(
    applauseDsl_ViewCall,
)
PredefinedParameter_strategy = st.builds(
    PredefinedParameter,
)
applauseDsl_SectionId_strategy = st.builds(
    applauseDsl_SectionId,
)
applauseDsl_PredefinedParameter_strategy = st.builds(
    applauseDsl_PredefinedParameter,
)
applauseDsl_CollectionExpression_strategy = st.builds(
    applauseDsl_CollectionExpression,
)
applauseDsl_Expression_strategy = st.builds(
    applauseDsl_Expression,
)
CollectionExpression_strategy = st.builds(
    CollectionExpression,
)
ScalarExpression_strategy = st.builds(
    ScalarExpression,
)
Expression_strategy = st.builds(
    Expression,
)
applauseDsl_CollectionLiteral_strategy = st.builds(
    applauseDsl_CollectionLiteral,
)
applauseDsl_StringLiteral_strategy = st.builds(
    applauseDsl_StringLiteral,
    value=
        safe_text
)
applauseDsl_StringFunction_strategy = st.builds(
    applauseDsl_StringFunction,
)
applauseDsl_CollectionFunction_strategy = st.builds(
    applauseDsl_CollectionFunction,
)
applauseDsl_ObjectReference_strategy = st.builds(
    applauseDsl_ObjectReference,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
applauseDsl_Property_strategy = st.builds(
    applauseDsl_Property,
    derived=
        st.booleans()
)
applauseDsl_CollectionIterator_strategy = st.builds(
    applauseDsl_CollectionIterator,
)
applauseDsl_Constant_strategy = st.builds(
    applauseDsl_Constant,
    language=
        safe_text
)
applauseDsl_Parameter_strategy = st.builds(
    applauseDsl_Parameter,
)
Type_strategy = st.builds(
    Type,
)
applauseDsl_Entity_strategy = st.builds(
    applauseDsl_Entity,
)
applauseDsl_SimpleType_strategy = st.builds(
    applauseDsl_SimpleType,
    platformType=
        safe_text
)
ModelElement_strategy = st.builds(
    ModelElement,
)
applauseDsl_View_strategy = st.builds(
    applauseDsl_View,
    name=
        safe_text
)
applauseDsl_ContentProvider_strategy = st.builds(
    applauseDsl_ContentProvider,
    xml=
        st.booleans(),
    html=
        st.booleans(),
    many=
        st.booleans(),
    resolver=
        st.booleans(),
    name=
        safe_text
)
applauseDsl_NavigationBarItem_strategy = st.builds(
    applauseDsl_NavigationBarItem,
    position=
        safe_text
)
applauseDsl_ModelElement_strategy = st.builds(
    applauseDsl_ModelElement,
)
applauseDsl_Application_strategy = st.builds(
    applauseDsl_Application,
    tabbarApplication=
        st.booleans(),
    name=
        safe_text
)
applauseDsl_ApplauseModel_strategy = st.builds(
    applauseDsl_ApplauseModel,
)
applauseDsl_Type_strategy = st.builds(
    applauseDsl_Type,
    name=
        safe_text
)
applauseDsl_TypeDescription_strategy = st.builds(
    applauseDsl_TypeDescription,
    many=
        st.booleans()
)
applauseDsl_VariableDeclaration_strategy = st.builds(
    applauseDsl_VariableDeclaration,
    name=
        safe_text
)
applauseDsl_ScalarExpression_strategy = st.builds(
    applauseDsl_ScalarExpression,
)

@given(instance=CollectionFunction_strategy)
@settings(max_examples=50)
def test_collectionfunction_instantiation(instance):
    assert isinstance(instance, CollectionFunction)

@given(instance=applauseDsl_StringSplit_strategy)
@settings(max_examples=50)
def test_applausedsl_stringsplit_instantiation(instance):
    assert isinstance(instance, applauseDsl_StringSplit)

@given(instance=StringFunction_strategy)
@settings(max_examples=50)
def test_stringfunction_instantiation(instance):
    assert isinstance(instance, StringFunction)

@given(instance=applauseDsl_StringUrlConform_strategy)
@settings(max_examples=50)
def test_applausedsl_stringurlconform_instantiation(instance):
    assert isinstance(instance, applauseDsl_StringUrlConform)

@given(instance=applauseDsl_StringReplace_strategy)
@settings(max_examples=50)
def test_applausedsl_stringreplace_instantiation(instance):
    assert isinstance(instance, applauseDsl_StringReplace)

@given(instance=applauseDsl_StringConcat_strategy)
@settings(max_examples=50)
def test_applausedsl_stringconcat_instantiation(instance):
    assert isinstance(instance, applauseDsl_StringConcat)

@given(instance=applauseDsl_ViewAction_strategy)
@settings(max_examples=50)
def test_applausedsl_viewaction_instantiation(instance):
    assert isinstance(instance, applauseDsl_ViewAction)

@given(instance=ViewAction_strategy)
@settings(max_examples=50)
def test_viewaction_instantiation(instance):
    assert isinstance(instance, ViewAction)

@given(instance=applauseDsl_ExternalOpen_strategy)
@settings(max_examples=50)
def test_applausedsl_externalopen_instantiation(instance):
    assert isinstance(instance, applauseDsl_ExternalOpen)

@given(instance=applauseDsl_ActionDelegate_strategy)
@settings(max_examples=50)
def test_applausedsl_actiondelegate_instantiation(instance):
    assert isinstance(instance, applauseDsl_ActionDelegate)

@given(instance=applauseDsl_ViewHeader_strategy)
@settings(max_examples=50)
def test_applausedsl_viewheader_instantiation(instance):
    assert isinstance(instance, applauseDsl_ViewHeader)

@given(instance=SectionedView_strategy)
@settings(max_examples=50)
def test_sectionedview_instantiation(instance):
    assert isinstance(instance, SectionedView)

@given(instance=applauseDsl_DetailsView_strategy)
@settings(max_examples=50)
def test_applausedsl_detailsview_instantiation(instance):
    assert isinstance(instance, applauseDsl_DetailsView)

@given(instance=applauseDsl_TableView_strategy)
@settings(max_examples=50)
def test_applausedsl_tableview_instantiation(instance):
    assert isinstance(instance, applauseDsl_TableView)

@given(instance=applauseDsl_ViewSection_strategy)
@settings(max_examples=50)
def test_applausedsl_viewsection_instantiation(instance):
    assert isinstance(instance, applauseDsl_ViewSection)

@given(instance=applauseDsl_ViewForAllSections_strategy)
@settings(max_examples=50)
def test_applausedsl_viewforallsections_instantiation(instance):
    assert isinstance(instance, applauseDsl_ViewForAllSections)

@given(instance=View_strategy)
@settings(max_examples=50)
def test_view_instantiation(instance):
    assert isinstance(instance, View)

@given(instance=applauseDsl_CustomView_strategy)
@settings(max_examples=50)
def test_applausedsl_customview_instantiation(instance):
    assert isinstance(instance, applauseDsl_CustomView)



@given(instance=applauseDsl_CustomView_strategy)
def test_applausedsl_customview_objclass_setter(instance):
    original = instance.objclass
    instance.objclass = original
    assert instance.objclass == original

@given(instance=applauseDsl_WebView_strategy)
@settings(max_examples=50)
def test_applausedsl_webview_instantiation(instance):
    assert isinstance(instance, applauseDsl_WebView)

@given(instance=applauseDsl_SectionedView_strategy)
@settings(max_examples=50)
def test_applausedsl_sectionedview_instantiation(instance):
    assert isinstance(instance, applauseDsl_SectionedView)

@given(instance=applauseDsl_SectionCell_strategy)
@settings(max_examples=50)
def test_applausedsl_sectioncell_instantiation(instance):
    assert isinstance(instance, applauseDsl_SectionCell)



@given(instance=applauseDsl_SectionCell_strategy)
def test_applausedsl_sectioncell_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=applauseDsl_ProviderConstruction_strategy)
@settings(max_examples=50)
def test_applausedsl_providerconstruction_instantiation(instance):
    assert isinstance(instance, applauseDsl_ProviderConstruction)

@given(instance=applauseDsl_Button_strategy)
@settings(max_examples=50)
def test_applausedsl_button_instantiation(instance):
    assert isinstance(instance, applauseDsl_Button)



@given(instance=applauseDsl_Button_strategy)
def test_applausedsl_button_handler_setter(instance):
    original = instance.handler
    instance.handler = original
    assert instance.handler == original

@given(instance=applauseDsl_ViewCall_strategy)
@settings(max_examples=50)
def test_applausedsl_viewcall_instantiation(instance):
    assert isinstance(instance, applauseDsl_ViewCall)

@given(instance=PredefinedParameter_strategy)
@settings(max_examples=50)
def test_predefinedparameter_instantiation(instance):
    assert isinstance(instance, PredefinedParameter)

@given(instance=applauseDsl_SectionId_strategy)
@settings(max_examples=50)
def test_applausedsl_sectionid_instantiation(instance):
    assert isinstance(instance, applauseDsl_SectionId)

@given(instance=applauseDsl_PredefinedParameter_strategy)
@settings(max_examples=50)
def test_applausedsl_predefinedparameter_instantiation(instance):
    assert isinstance(instance, applauseDsl_PredefinedParameter)

@given(instance=applauseDsl_CollectionExpression_strategy)
@settings(max_examples=50)
def test_applausedsl_collectionexpression_instantiation(instance):
    assert isinstance(instance, applauseDsl_CollectionExpression)

@given(instance=applauseDsl_Expression_strategy)
@settings(max_examples=50)
def test_applausedsl_expression_instantiation(instance):
    assert isinstance(instance, applauseDsl_Expression)

@given(instance=CollectionExpression_strategy)
@settings(max_examples=50)
def test_collectionexpression_instantiation(instance):
    assert isinstance(instance, CollectionExpression)

@given(instance=ScalarExpression_strategy)
@settings(max_examples=50)
def test_scalarexpression_instantiation(instance):
    assert isinstance(instance, ScalarExpression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=applauseDsl_CollectionLiteral_strategy)
@settings(max_examples=50)
def test_applausedsl_collectionliteral_instantiation(instance):
    assert isinstance(instance, applauseDsl_CollectionLiteral)

@given(instance=applauseDsl_StringLiteral_strategy)
@settings(max_examples=50)
def test_applausedsl_stringliteral_instantiation(instance):
    assert isinstance(instance, applauseDsl_StringLiteral)



@given(instance=applauseDsl_StringLiteral_strategy)
def test_applausedsl_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=applauseDsl_StringFunction_strategy)
@settings(max_examples=50)
def test_applausedsl_stringfunction_instantiation(instance):
    assert isinstance(instance, applauseDsl_StringFunction)

@given(instance=applauseDsl_CollectionFunction_strategy)
@settings(max_examples=50)
def test_applausedsl_collectionfunction_instantiation(instance):
    assert isinstance(instance, applauseDsl_CollectionFunction)

@given(instance=applauseDsl_ObjectReference_strategy)
@settings(max_examples=50)
def test_applausedsl_objectreference_instantiation(instance):
    assert isinstance(instance, applauseDsl_ObjectReference)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=applauseDsl_Property_strategy)
@settings(max_examples=50)
def test_applausedsl_property_instantiation(instance):
    assert isinstance(instance, applauseDsl_Property)



@given(instance=applauseDsl_Property_strategy)
def test_applausedsl_property_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original

@given(instance=applauseDsl_CollectionIterator_strategy)
@settings(max_examples=50)
def test_applausedsl_collectioniterator_instantiation(instance):
    assert isinstance(instance, applauseDsl_CollectionIterator)

@given(instance=applauseDsl_Constant_strategy)
@settings(max_examples=50)
def test_applausedsl_constant_instantiation(instance):
    assert isinstance(instance, applauseDsl_Constant)



@given(instance=applauseDsl_Constant_strategy)
def test_applausedsl_constant_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=applauseDsl_Parameter_strategy)
@settings(max_examples=50)
def test_applausedsl_parameter_instantiation(instance):
    assert isinstance(instance, applauseDsl_Parameter)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=applauseDsl_Entity_strategy)
@settings(max_examples=50)
def test_applausedsl_entity_instantiation(instance):
    assert isinstance(instance, applauseDsl_Entity)

@given(instance=applauseDsl_SimpleType_strategy)
@settings(max_examples=50)
def test_applausedsl_simpletype_instantiation(instance):
    assert isinstance(instance, applauseDsl_SimpleType)



@given(instance=applauseDsl_SimpleType_strategy)
def test_applausedsl_simpletype_platformType_setter(instance):
    original = instance.platformType
    instance.platformType = original
    assert instance.platformType == original

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=applauseDsl_View_strategy)
@settings(max_examples=50)
def test_applausedsl_view_instantiation(instance):
    assert isinstance(instance, applauseDsl_View)



@given(instance=applauseDsl_View_strategy)
def test_applausedsl_view_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=applauseDsl_ContentProvider_strategy)
@settings(max_examples=50)
def test_applausedsl_contentprovider_instantiation(instance):
    assert isinstance(instance, applauseDsl_ContentProvider)



@given(instance=applauseDsl_ContentProvider_strategy)
def test_applausedsl_contentprovider_xml_setter(instance):
    original = instance.xml
    instance.xml = original
    assert instance.xml == original



@given(instance=applauseDsl_ContentProvider_strategy)
def test_applausedsl_contentprovider_html_setter(instance):
    original = instance.html
    instance.html = original
    assert instance.html == original



@given(instance=applauseDsl_ContentProvider_strategy)
def test_applausedsl_contentprovider_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original



@given(instance=applauseDsl_ContentProvider_strategy)
def test_applausedsl_contentprovider_resolver_setter(instance):
    original = instance.resolver
    instance.resolver = original
    assert instance.resolver == original



@given(instance=applauseDsl_ContentProvider_strategy)
def test_applausedsl_contentprovider_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=applauseDsl_NavigationBarItem_strategy)
@settings(max_examples=50)
def test_applausedsl_navigationbaritem_instantiation(instance):
    assert isinstance(instance, applauseDsl_NavigationBarItem)



@given(instance=applauseDsl_NavigationBarItem_strategy)
def test_applausedsl_navigationbaritem_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=applauseDsl_ModelElement_strategy)
@settings(max_examples=50)
def test_applausedsl_modelelement_instantiation(instance):
    assert isinstance(instance, applauseDsl_ModelElement)

@given(instance=applauseDsl_Application_strategy)
@settings(max_examples=50)
def test_applausedsl_application_instantiation(instance):
    assert isinstance(instance, applauseDsl_Application)



@given(instance=applauseDsl_Application_strategy)
def test_applausedsl_application_tabbarApplication_setter(instance):
    original = instance.tabbarApplication
    instance.tabbarApplication = original
    assert instance.tabbarApplication == original



@given(instance=applauseDsl_Application_strategy)
def test_applausedsl_application_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=applauseDsl_ApplauseModel_strategy)
@settings(max_examples=50)
def test_applausedsl_applausemodel_instantiation(instance):
    assert isinstance(instance, applauseDsl_ApplauseModel)

@given(instance=applauseDsl_Type_strategy)
@settings(max_examples=50)
def test_applausedsl_type_instantiation(instance):
    assert isinstance(instance, applauseDsl_Type)



@given(instance=applauseDsl_Type_strategy)
def test_applausedsl_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=applauseDsl_TypeDescription_strategy)
@settings(max_examples=50)
def test_applausedsl_typedescription_instantiation(instance):
    assert isinstance(instance, applauseDsl_TypeDescription)



@given(instance=applauseDsl_TypeDescription_strategy)
def test_applausedsl_typedescription_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=applauseDsl_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_applausedsl_variabledeclaration_instantiation(instance):
    assert isinstance(instance, applauseDsl_VariableDeclaration)



@given(instance=applauseDsl_VariableDeclaration_strategy)
def test_applausedsl_variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=applauseDsl_ScalarExpression_strategy)
@settings(max_examples=50)
def test_applausedsl_scalarexpression_instantiation(instance):
    assert isinstance(instance, applauseDsl_ScalarExpression)
