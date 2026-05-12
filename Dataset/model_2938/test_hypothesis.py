import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    eJSL_PositionParameter,
    eJSL_MethodParameter,
    eJSL_Method,
    eJSL_Package,
    eJSL_Class,
    eJSL_Author,
    eJSL_CssBlock,
    eJSL_Position,
    eJSL_ComponentReference,
    Section,
    eJSL_BackendSection,
    eJSL_PageReference,
    Extension,
    eJSL_Component,
    eJSL_Template,
    eJSL_ExtensionPackage,
    eJSL_Language,
    eJSL_Manifestation,
    eJSL_LinkParameter,
    InternalLink,
    eJSL_ContextLink,
    eJSL_Library,
    eJSL_Plugin,
    eJSL_Module,
    eJSL_FrontendSection,
    eJSL_DetailPageField,
    DynamicPage,
    eJSL_DetailsPage,
    eJSL_IndexPage,
    Link,
    eJSL_InternalLink,
    eJSL_ExternalLink,
    eJSL_Reference,
    eJSL_Attribute,
    Page,
    eJSL_DynamicPage,
    eJSL_CustomPage,
    eJSL_StaticPage,
    eJSL_Link,
    eJSL_HTMLTypes,
    HTMLTypes,
    eJSL_SimpleHTMLTypes,
    eJSL_ComplexHTMLTypes,
    Type,
    eJSL_StandardTypes,
    eJSL_DatatypeReference,
    eJSL_Type,
    eJSL_Section,
    eJSL_Page,
    eJSL_Entity,
    eJSL_Entitypackage,
    eJSL_Extension,
    eJSL_PageAction,
    eJSL_KeyValuePair,
    eJSL_EJSLModel,
    eJSL_coreFeature,
    EJSLPart,
    eJSL_CMSExtension,
    eJSL_CMSCore,
    eJSL_Feature,
    eJSL_ParameterGroup,
    eJSL_Parameter,
    eJSL_Datatype,
    eJSL_EJSLPart,
    ComplexHTMLTypeKinds,
    PluginKinds,
    SimpleHTMLTypeKinds,
    CoreComponent,
    DataAccessKinds,
    PageActionPositionKind,
    PageActionKind,
    StandardTypeKinds,
    PageKinds,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ejsl_positionparameter_is_not_abstract():
    assert not inspect.isabstract(eJSL_PositionParameter)


def test_ejsl_positionparameter_constructor_exists():
    assert callable(eJSL_PositionParameter.__init__)


def test_ejsl_positionparameter_constructor_args():
    sig = inspect.signature(eJSL_PositionParameter.__init__)
    params = list(sig.parameters.keys())
    assert "divid" in params, "Missing parameter 'divid'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl_positionparameter_has_divid():
    assert hasattr(eJSL_PositionParameter, "divid")
    descriptor = None
    for klass in eJSL_PositionParameter.__mro__:
        if "divid" in klass.__dict__:
            descriptor = klass.__dict__["divid"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_positionparameter_has_type():
    assert hasattr(eJSL_PositionParameter, "type")
    descriptor = None
    for klass in eJSL_PositionParameter.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_positionparameter_has_name():
    assert hasattr(eJSL_PositionParameter, "name")
    descriptor = None
    for klass in eJSL_PositionParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl_methodparameter_is_not_abstract():
    assert not inspect.isabstract(eJSL_MethodParameter)


def test_ejsl_methodparameter_constructor_exists():
    assert callable(eJSL_MethodParameter.__init__)


def test_ejsl_methodparameter_constructor_args():
    sig = inspect.signature(eJSL_MethodParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl_methodparameter_has_name():
    assert hasattr(eJSL_MethodParameter, "name")
    descriptor = None
    for klass in eJSL_MethodParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl_method_is_not_abstract():
    assert not inspect.isabstract(eJSL_Method)


def test_ejsl_method_constructor_exists():
    assert callable(eJSL_Method.__init__)


def test_ejsl_method_constructor_args():
    sig = inspect.signature(eJSL_Method.__init__)
    params = list(sig.parameters.keys())
    assert "returnvalue" in params, "Missing parameter 'returnvalue'"
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl_method_has_returnvalue():
    assert hasattr(eJSL_Method, "returnvalue")
    descriptor = None
    for klass in eJSL_Method.__mro__:
        if "returnvalue" in klass.__dict__:
            descriptor = klass.__dict__["returnvalue"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_method_has_name():
    assert hasattr(eJSL_Method, "name")
    descriptor = None
    for klass in eJSL_Method.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl_package_is_not_abstract():
    assert not inspect.isabstract(eJSL_Package)


def test_ejsl_package_constructor_exists():
    assert callable(eJSL_Package.__init__)


def test_ejsl_package_constructor_args():
    sig = inspect.signature(eJSL_Package.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl_package_has_name():
    assert hasattr(eJSL_Package, "name")
    descriptor = None
    for klass in eJSL_Package.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl_class_is_not_abstract():
    assert not inspect.isabstract(eJSL_Class)


def test_ejsl_class_constructor_exists():
    assert callable(eJSL_Class.__init__)


def test_ejsl_class_constructor_args():
    sig = inspect.signature(eJSL_Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl_class_has_name():
    assert hasattr(eJSL_Class, "name")
    descriptor = None
    for klass in eJSL_Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl_author_is_not_abstract():
    assert not inspect.isabstract(eJSL_Author)


def test_ejsl_author_constructor_exists():
    assert callable(eJSL_Author.__init__)


def test_ejsl_author_constructor_args():
    sig = inspect.signature(eJSL_Author.__init__)
    params = list(sig.parameters.keys())
    assert "authorurl" in params, "Missing parameter 'authorurl'"
    assert "name" in params, "Missing parameter 'name'"
    assert "authoremail" in params, "Missing parameter 'authoremail'"

def test_ejsl_author_has_authorurl():
    assert hasattr(eJSL_Author, "authorurl")
    descriptor = None
    for klass in eJSL_Author.__mro__:
        if "authorurl" in klass.__dict__:
            descriptor = klass.__dict__["authorurl"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_author_has_name():
    assert hasattr(eJSL_Author, "name")
    descriptor = None
    for klass in eJSL_Author.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_author_has_authoremail():
    assert hasattr(eJSL_Author, "authoremail")
    descriptor = None
    for klass in eJSL_Author.__mro__:
        if "authoremail" in klass.__dict__:
            descriptor = klass.__dict__["authoremail"]
            break
    assert isinstance(descriptor, property)



def test_ejsl_cssblock_is_not_abstract():
    assert not inspect.isabstract(eJSL_CssBlock)


def test_ejsl_cssblock_constructor_exists():
    assert callable(eJSL_CssBlock.__init__)


def test_ejsl_cssblock_constructor_args():
    sig = inspect.signature(eJSL_CssBlock.__init__)
    params = list(sig.parameters.keys())
    assert "selector" in params, "Missing parameter 'selector'"

def test_ejsl_cssblock_has_selector():
    assert hasattr(eJSL_CssBlock, "selector")
    descriptor = None
    for klass in eJSL_CssBlock.__mro__:
        if "selector" in klass.__dict__:
            descriptor = klass.__dict__["selector"]
            break
    assert isinstance(descriptor, property)



def test_ejsl_position_is_not_abstract():
    assert not inspect.isabstract(eJSL_Position)


def test_ejsl_position_constructor_exists():
    assert callable(eJSL_Position.__init__)


def test_ejsl_position_constructor_args():
    sig = inspect.signature(eJSL_Position.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl_position_has_name():
    assert hasattr(eJSL_Position, "name")
    descriptor = None
    for klass in eJSL_Position.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl_componentreference_is_not_abstract():
    assert not inspect.isabstract(eJSL_ComponentReference)


def test_ejsl_componentreference_constructor_exists():
    assert callable(eJSL_ComponentReference.__init__)


def test_ejsl_componentreference_constructor_args():
    sig = inspect.signature(eJSL_ComponentReference.__init__)
    params = list(sig.parameters.keys())
    assert "core" in params, "Missing parameter 'core'"

def test_ejsl_componentreference_has_core():
    assert hasattr(eJSL_ComponentReference, "core")
    descriptor = None
    for klass in eJSL_ComponentReference.__mro__:
        if "core" in klass.__dict__:
            descriptor = klass.__dict__["core"]
            break
    assert isinstance(descriptor, property)



def test_section_is_not_abstract():
    assert not inspect.isabstract(Section)


def test_section_constructor_exists():
    assert callable(Section.__init__)


def test_section_constructor_args():
    sig = inspect.signature(Section.__init__)
    params = list(sig.parameters.keys())



def test_ejsl_backendsection_is_not_abstract():
    assert not inspect.isabstract(eJSL_BackendSection)


def test_ejsl_backendsection_constructor_exists():
    assert callable(eJSL_BackendSection.__init__)


def test_ejsl_backendsection_constructor_args():
    sig = inspect.signature(eJSL_BackendSection.__init__)
    params = list(sig.parameters.keys())



def test_ejsl_pagereference_is_not_abstract():
    assert not inspect.isabstract(eJSL_PageReference)


def test_ejsl_pagereference_constructor_exists():
    assert callable(eJSL_PageReference.__init__)


def test_ejsl_pagereference_constructor_args():
    sig = inspect.signature(eJSL_PageReference.__init__)
    params = list(sig.parameters.keys())
    assert "sect" in params, "Missing parameter 'sect'"

def test_ejsl_pagereference_has_sect():
    assert hasattr(eJSL_PageReference, "sect")
    descriptor = None
    for klass in eJSL_PageReference.__mro__:
        if "sect" in klass.__dict__:
            descriptor = klass.__dict__["sect"]
            break
    assert isinstance(descriptor, property)



def test_extension_is_not_abstract():
    assert not inspect.isabstract(Extension)


def test_extension_constructor_exists():
    assert callable(Extension.__init__)


def test_extension_constructor_args():
    sig = inspect.signature(Extension.__init__)
    params = list(sig.parameters.keys())



def test_ejsl_component_is_not_abstract():
    assert not inspect.isabstract(eJSL_Component)


def test_ejsl_component_constructor_exists():
    assert callable(eJSL_Component.__init__)


def test_ejsl_component_constructor_args():
    sig = inspect.signature(eJSL_Component.__init__)
    params = list(sig.parameters.keys())



def test_ejsl_template_is_not_abstract():
    assert not inspect.isabstract(eJSL_Template)


def test_ejsl_template_constructor_exists():
    assert callable(eJSL_Template.__init__)


def test_ejsl_template_constructor_args():
    sig = inspect.signature(eJSL_Template.__init__)
    params = list(sig.parameters.keys())



def test_ejsl_extensionpackage_is_not_abstract():
    assert not inspect.isabstract(eJSL_ExtensionPackage)


def test_ejsl_extensionpackage_constructor_exists():
    assert callable(eJSL_ExtensionPackage.__init__)


def test_ejsl_extensionpackage_constructor_args():
    sig = inspect.signature(eJSL_ExtensionPackage.__init__)
    params = list(sig.parameters.keys())



def test_ejsl_language_is_not_abstract():
    assert not inspect.isabstract(eJSL_Language)


def test_ejsl_language_constructor_exists():
    assert callable(eJSL_Language.__init__)


def test_ejsl_language_constructor_args():
    sig = inspect.signature(eJSL_Language.__init__)
    params = list(sig.parameters.keys())
    assert "sys" in params, "Missing parameter 'sys'"
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl_language_has_sys():
    assert hasattr(eJSL_Language, "sys")
    descriptor = None
    for klass in eJSL_Language.__mro__:
        if "sys" in klass.__dict__:
            descriptor = klass.__dict__["sys"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_language_has_name():
    assert hasattr(eJSL_Language, "name")
    descriptor = None
    for klass in eJSL_Language.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl_manifestation_is_not_abstract():
    assert not inspect.isabstract(eJSL_Manifestation)


def test_ejsl_manifestation_constructor_exists():
    assert callable(eJSL_Manifestation.__init__)


def test_ejsl_manifestation_constructor_args():
    sig = inspect.signature(eJSL_Manifestation.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "license" in params, "Missing parameter 'license'"
    assert "copyright" in params, "Missing parameter 'copyright'"
    assert "link" in params, "Missing parameter 'link'"
    assert "creationdate" in params, "Missing parameter 'creationdate'"
    assert "version" in params, "Missing parameter 'version'"

def test_ejsl_manifestation_has_description():
    assert hasattr(eJSL_Manifestation, "description")
    descriptor = None
    for klass in eJSL_Manifestation.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_manifestation_has_license():
    assert hasattr(eJSL_Manifestation, "license")
    descriptor = None
    for klass in eJSL_Manifestation.__mro__:
        if "license" in klass.__dict__:
            descriptor = klass.__dict__["license"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_manifestation_has_copyright():
    assert hasattr(eJSL_Manifestation, "copyright")
    descriptor = None
    for klass in eJSL_Manifestation.__mro__:
        if "copyright" in klass.__dict__:
            descriptor = klass.__dict__["copyright"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_manifestation_has_link():
    assert hasattr(eJSL_Manifestation, "link")
    descriptor = None
    for klass in eJSL_Manifestation.__mro__:
        if "link" in klass.__dict__:
            descriptor = klass.__dict__["link"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_manifestation_has_creationdate():
    assert hasattr(eJSL_Manifestation, "creationdate")
    descriptor = None
    for klass in eJSL_Manifestation.__mro__:
        if "creationdate" in klass.__dict__:
            descriptor = klass.__dict__["creationdate"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_manifestation_has_version():
    assert hasattr(eJSL_Manifestation, "version")
    descriptor = None
    for klass in eJSL_Manifestation.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_ejsl_linkparameter_is_not_abstract():
    assert not inspect.isabstract(eJSL_LinkParameter)


def test_ejsl_linkparameter_constructor_exists():
    assert callable(eJSL_LinkParameter.__init__)


def test_ejsl_linkparameter_constructor_args():
    sig = inspect.signature(eJSL_LinkParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"
    assert "id" in params, "Missing parameter 'id'"

def test_ejsl_linkparameter_has_name():
    assert hasattr(eJSL_LinkParameter, "name")
    descriptor = None
    for klass in eJSL_LinkParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_linkparameter_has_value():
    assert hasattr(eJSL_LinkParameter, "value")
    descriptor = None
    for klass in eJSL_LinkParameter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_linkparameter_has_id():
    assert hasattr(eJSL_LinkParameter, "id")
    descriptor = None
    for klass in eJSL_LinkParameter.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_internallink_is_not_abstract():
    assert not inspect.isabstract(InternalLink)


def test_internallink_constructor_exists():
    assert callable(InternalLink.__init__)


def test_internallink_constructor_args():
    sig = inspect.signature(InternalLink.__init__)
    params = list(sig.parameters.keys())



def test_ejsl_contextlink_is_not_abstract():
    assert not inspect.isabstract(eJSL_ContextLink)


def test_ejsl_contextlink_constructor_exists():
    assert callable(eJSL_ContextLink.__init__)


def test_ejsl_contextlink_constructor_args():
    sig = inspect.signature(eJSL_ContextLink.__init__)
    params = list(sig.parameters.keys())



def test_ejsl_library_is_not_abstract():
    assert not inspect.isabstract(eJSL_Library)


def test_ejsl_library_constructor_exists():
    assert callable(eJSL_Library.__init__)


def test_ejsl_library_constructor_args():
    sig = inspect.signature(eJSL_Library.__init__)
    params = list(sig.parameters.keys())



def test_ejsl_plugin_is_not_abstract():
    assert not inspect.isabstract(eJSL_Plugin)


def test_ejsl_plugin_constructor_exists():
    assert callable(eJSL_Plugin.__init__)


def test_ejsl_plugin_constructor_args():
    sig = inspect.signature(eJSL_Plugin.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_ejsl_plugin_has_type():
    assert hasattr(eJSL_Plugin, "type")
    descriptor = None
    for klass in eJSL_Plugin.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_ejsl_module_is_not_abstract():
    assert not inspect.isabstract(eJSL_Module)


def test_ejsl_module_constructor_exists():
    assert callable(eJSL_Module.__init__)


def test_ejsl_module_constructor_args():
    sig = inspect.signature(eJSL_Module.__init__)
    params = list(sig.parameters.keys())



def test_ejsl_frontendsection_is_not_abstract():
    assert not inspect.isabstract(eJSL_FrontendSection)


def test_ejsl_frontendsection_constructor_exists():
    assert callable(eJSL_FrontendSection.__init__)


def test_ejsl_frontendsection_constructor_args():
    sig = inspect.signature(eJSL_FrontendSection.__init__)
    params = list(sig.parameters.keys())



def test_ejsl_detailpagefield_is_not_abstract():
    assert not inspect.isabstract(eJSL_DetailPageField)


def test_ejsl_detailpagefield_constructor_exists():
    assert callable(eJSL_DetailPageField.__init__)


def test_ejsl_detailpagefield_constructor_args():
    sig = inspect.signature(eJSL_DetailPageField.__init__)
    params = list(sig.parameters.keys())



def test_dynamicpage_is_not_abstract():
    assert not inspect.isabstract(DynamicPage)


def test_dynamicpage_constructor_exists():
    assert callable(DynamicPage.__init__)


def test_dynamicpage_constructor_args():
    sig = inspect.signature(DynamicPage.__init__)
    params = list(sig.parameters.keys())



def test_ejsl_detailspage_is_not_abstract():
    assert not inspect.isabstract(eJSL_DetailsPage)


def test_ejsl_detailspage_constructor_exists():
    assert callable(eJSL_DetailsPage.__init__)


def test_ejsl_detailspage_constructor_args():
    sig = inspect.signature(eJSL_DetailsPage.__init__)
    params = list(sig.parameters.keys())



def test_ejsl_indexpage_is_not_abstract():
    assert not inspect.isabstract(eJSL_IndexPage)


def test_ejsl_indexpage_constructor_exists():
    assert callable(eJSL_IndexPage.__init__)


def test_ejsl_indexpage_constructor_args():
    sig = inspect.signature(eJSL_IndexPage.__init__)
    params = list(sig.parameters.keys())



def test_link_is_not_abstract():
    assert not inspect.isabstract(Link)


def test_link_constructor_exists():
    assert callable(Link.__init__)


def test_link_constructor_args():
    sig = inspect.signature(Link.__init__)
    params = list(sig.parameters.keys())



def test_ejsl_internallink_is_not_abstract():
    assert not inspect.isabstract(eJSL_InternalLink)


def test_ejsl_internallink_constructor_exists():
    assert callable(eJSL_InternalLink.__init__)


def test_ejsl_internallink_constructor_args():
    sig = inspect.signature(eJSL_InternalLink.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl_internallink_has_name():
    assert hasattr(eJSL_InternalLink, "name")
    descriptor = None
    for klass in eJSL_InternalLink.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl_externallink_is_not_abstract():
    assert not inspect.isabstract(eJSL_ExternalLink)


def test_ejsl_externallink_constructor_exists():
    assert callable(eJSL_ExternalLink.__init__)


def test_ejsl_externallink_constructor_args():
    sig = inspect.signature(eJSL_ExternalLink.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "target" in params, "Missing parameter 'target'"

def test_ejsl_externallink_has_label():
    assert hasattr(eJSL_ExternalLink, "label")
    descriptor = None
    for klass in eJSL_ExternalLink.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_externallink_has_target():
    assert hasattr(eJSL_ExternalLink, "target")
    descriptor = None
    for klass in eJSL_ExternalLink.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)



def test_ejsl_reference_is_not_abstract():
    assert not inspect.isabstract(eJSL_Reference)


def test_ejsl_reference_constructor_exists():
    assert callable(eJSL_Reference.__init__)


def test_ejsl_reference_constructor_args():
    sig = inspect.signature(eJSL_Reference.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "preserve" in params, "Missing parameter 'preserve'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "id" in params, "Missing parameter 'id'"

def test_ejsl_reference_has_lower():
    assert hasattr(eJSL_Reference, "lower")
    descriptor = None
    for klass in eJSL_Reference.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_reference_has_preserve():
    assert hasattr(eJSL_Reference, "preserve")
    descriptor = None
    for klass in eJSL_Reference.__mro__:
        if "preserve" in klass.__dict__:
            descriptor = klass.__dict__["preserve"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_reference_has_upper():
    assert hasattr(eJSL_Reference, "upper")
    descriptor = None
    for klass in eJSL_Reference.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_reference_has_id():
    assert hasattr(eJSL_Reference, "id")
    descriptor = None
    for klass in eJSL_Reference.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_ejsl_attribute_is_not_abstract():
    assert not inspect.isabstract(eJSL_Attribute)


def test_ejsl_attribute_constructor_exists():
    assert callable(eJSL_Attribute.__init__)


def test_ejsl_attribute_constructor_args():
    sig = inspect.signature(eJSL_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "preserve" in params, "Missing parameter 'preserve'"
    assert "isunique" in params, "Missing parameter 'isunique'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isprimary" in params, "Missing parameter 'isprimary'"
    assert "id" in params, "Missing parameter 'id'"

def test_ejsl_attribute_has_preserve():
    assert hasattr(eJSL_Attribute, "preserve")
    descriptor = None
    for klass in eJSL_Attribute.__mro__:
        if "preserve" in klass.__dict__:
            descriptor = klass.__dict__["preserve"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_attribute_has_isunique():
    assert hasattr(eJSL_Attribute, "isunique")
    descriptor = None
    for klass in eJSL_Attribute.__mro__:
        if "isunique" in klass.__dict__:
            descriptor = klass.__dict__["isunique"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_attribute_has_name():
    assert hasattr(eJSL_Attribute, "name")
    descriptor = None
    for klass in eJSL_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_attribute_has_isprimary():
    assert hasattr(eJSL_Attribute, "isprimary")
    descriptor = None
    for klass in eJSL_Attribute.__mro__:
        if "isprimary" in klass.__dict__:
            descriptor = klass.__dict__["isprimary"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_attribute_has_id():
    assert hasattr(eJSL_Attribute, "id")
    descriptor = None
    for klass in eJSL_Attribute.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_page_is_not_abstract():
    assert not inspect.isabstract(Page)


def test_page_constructor_exists():
    assert callable(Page.__init__)


def test_page_constructor_args():
    sig = inspect.signature(Page.__init__)
    params = list(sig.parameters.keys())



def test_ejsl_dynamicpage_is_not_abstract():
    assert not inspect.isabstract(eJSL_DynamicPage)


def test_ejsl_dynamicpage_constructor_exists():
    assert callable(eJSL_DynamicPage.__init__)


def test_ejsl_dynamicpage_constructor_args():
    sig = inspect.signature(eJSL_DynamicPage.__init__)
    params = list(sig.parameters.keys())
    assert "preserve" in params, "Missing parameter 'preserve'"

def test_ejsl_dynamicpage_has_preserve():
    assert hasattr(eJSL_DynamicPage, "preserve")
    descriptor = None
    for klass in eJSL_DynamicPage.__mro__:
        if "preserve" in klass.__dict__:
            descriptor = klass.__dict__["preserve"]
            break
    assert isinstance(descriptor, property)



def test_ejsl_custompage_is_not_abstract():
    assert not inspect.isabstract(eJSL_CustomPage)


def test_ejsl_custompage_constructor_exists():
    assert callable(eJSL_CustomPage.__init__)


def test_ejsl_custompage_constructor_args():
    sig = inspect.signature(eJSL_CustomPage.__init__)
    params = list(sig.parameters.keys())
    assert "pageType" in params, "Missing parameter 'pageType'"
    assert "preserve" in params, "Missing parameter 'preserve'"

def test_ejsl_custompage_has_pageType():
    assert hasattr(eJSL_CustomPage, "pageType")
    descriptor = None
    for klass in eJSL_CustomPage.__mro__:
        if "pageType" in klass.__dict__:
            descriptor = klass.__dict__["pageType"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_custompage_has_preserve():
    assert hasattr(eJSL_CustomPage, "preserve")
    descriptor = None
    for klass in eJSL_CustomPage.__mro__:
        if "preserve" in klass.__dict__:
            descriptor = klass.__dict__["preserve"]
            break
    assert isinstance(descriptor, property)



def test_ejsl_staticpage_is_not_abstract():
    assert not inspect.isabstract(eJSL_StaticPage)


def test_ejsl_staticpage_constructor_exists():
    assert callable(eJSL_StaticPage.__init__)


def test_ejsl_staticpage_constructor_args():
    sig = inspect.signature(eJSL_StaticPage.__init__)
    params = list(sig.parameters.keys())
    assert "HTMLBody" in params, "Missing parameter 'HTMLBody'"
    assert "preserve" in params, "Missing parameter 'preserve'"

def test_ejsl_staticpage_has_HTMLBody():
    assert hasattr(eJSL_StaticPage, "HTMLBody")
    descriptor = None
    for klass in eJSL_StaticPage.__mro__:
        if "HTMLBody" in klass.__dict__:
            descriptor = klass.__dict__["HTMLBody"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_staticpage_has_preserve():
    assert hasattr(eJSL_StaticPage, "preserve")
    descriptor = None
    for klass in eJSL_StaticPage.__mro__:
        if "preserve" in klass.__dict__:
            descriptor = klass.__dict__["preserve"]
            break
    assert isinstance(descriptor, property)



def test_ejsl_link_is_not_abstract():
    assert not inspect.isabstract(eJSL_Link)


def test_ejsl_link_constructor_exists():
    assert callable(eJSL_Link.__init__)


def test_ejsl_link_constructor_args():
    sig = inspect.signature(eJSL_Link.__init__)
    params = list(sig.parameters.keys())



def test_ejsl_htmltypes_is_not_abstract():
    assert not inspect.isabstract(eJSL_HTMLTypes)


def test_ejsl_htmltypes_constructor_exists():
    assert callable(eJSL_HTMLTypes.__init__)


def test_ejsl_htmltypes_constructor_args():
    sig = inspect.signature(eJSL_HTMLTypes.__init__)
    params = list(sig.parameters.keys())



def test_htmltypes_is_not_abstract():
    assert not inspect.isabstract(HTMLTypes)


def test_htmltypes_constructor_exists():
    assert callable(HTMLTypes.__init__)


def test_htmltypes_constructor_args():
    sig = inspect.signature(HTMLTypes.__init__)
    params = list(sig.parameters.keys())



def test_ejsl_simplehtmltypes_is_not_abstract():
    assert not inspect.isabstract(eJSL_SimpleHTMLTypes)


def test_ejsl_simplehtmltypes_constructor_exists():
    assert callable(eJSL_SimpleHTMLTypes.__init__)


def test_ejsl_simplehtmltypes_constructor_args():
    sig = inspect.signature(eJSL_SimpleHTMLTypes.__init__)
    params = list(sig.parameters.keys())
    assert "htmltype" in params, "Missing parameter 'htmltype'"

def test_ejsl_simplehtmltypes_has_htmltype():
    assert hasattr(eJSL_SimpleHTMLTypes, "htmltype")
    descriptor = None
    for klass in eJSL_SimpleHTMLTypes.__mro__:
        if "htmltype" in klass.__dict__:
            descriptor = klass.__dict__["htmltype"]
            break
    assert isinstance(descriptor, property)



def test_ejsl_complexhtmltypes_is_not_abstract():
    assert not inspect.isabstract(eJSL_ComplexHTMLTypes)


def test_ejsl_complexhtmltypes_constructor_exists():
    assert callable(eJSL_ComplexHTMLTypes.__init__)


def test_ejsl_complexhtmltypes_constructor_args():
    sig = inspect.signature(eJSL_ComplexHTMLTypes.__init__)
    params = list(sig.parameters.keys())
    assert "htmltype" in params, "Missing parameter 'htmltype'"

def test_ejsl_complexhtmltypes_has_htmltype():
    assert hasattr(eJSL_ComplexHTMLTypes, "htmltype")
    descriptor = None
    for klass in eJSL_ComplexHTMLTypes.__mro__:
        if "htmltype" in klass.__dict__:
            descriptor = klass.__dict__["htmltype"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_ejsl_standardtypes_is_not_abstract():
    assert not inspect.isabstract(eJSL_StandardTypes)


def test_ejsl_standardtypes_constructor_exists():
    assert callable(eJSL_StandardTypes.__init__)


def test_ejsl_standardtypes_constructor_args():
    sig = inspect.signature(eJSL_StandardTypes.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "autoincrement" in params, "Missing parameter 'autoincrement'"
    assert "notnull" in params, "Missing parameter 'notnull'"
    assert "default" in params, "Missing parameter 'default'"

def test_ejsl_standardtypes_has_type():
    assert hasattr(eJSL_StandardTypes, "type")
    descriptor = None
    for klass in eJSL_StandardTypes.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_standardtypes_has_autoincrement():
    assert hasattr(eJSL_StandardTypes, "autoincrement")
    descriptor = None
    for klass in eJSL_StandardTypes.__mro__:
        if "autoincrement" in klass.__dict__:
            descriptor = klass.__dict__["autoincrement"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_standardtypes_has_notnull():
    assert hasattr(eJSL_StandardTypes, "notnull")
    descriptor = None
    for klass in eJSL_StandardTypes.__mro__:
        if "notnull" in klass.__dict__:
            descriptor = klass.__dict__["notnull"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_standardtypes_has_default():
    assert hasattr(eJSL_StandardTypes, "default")
    descriptor = None
    for klass in eJSL_StandardTypes.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_ejsl_datatypereference_is_not_abstract():
    assert not inspect.isabstract(eJSL_DatatypeReference)


def test_ejsl_datatypereference_constructor_exists():
    assert callable(eJSL_DatatypeReference.__init__)


def test_ejsl_datatypereference_constructor_args():
    sig = inspect.signature(eJSL_DatatypeReference.__init__)
    params = list(sig.parameters.keys())



def test_ejsl_type_is_not_abstract():
    assert not inspect.isabstract(eJSL_Type)


def test_ejsl_type_constructor_exists():
    assert callable(eJSL_Type.__init__)


def test_ejsl_type_constructor_args():
    sig = inspect.signature(eJSL_Type.__init__)
    params = list(sig.parameters.keys())



def test_ejsl_section_is_not_abstract():
    assert not inspect.isabstract(eJSL_Section)


def test_ejsl_section_constructor_exists():
    assert callable(eJSL_Section.__init__)


def test_ejsl_section_constructor_args():
    sig = inspect.signature(eJSL_Section.__init__)
    params = list(sig.parameters.keys())



def test_ejsl_page_is_not_abstract():
    assert not inspect.isabstract(eJSL_Page)


def test_ejsl_page_constructor_exists():
    assert callable(eJSL_Page.__init__)


def test_ejsl_page_constructor_args():
    sig = inspect.signature(eJSL_Page.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl_page_has_name():
    assert hasattr(eJSL_Page, "name")
    descriptor = None
    for klass in eJSL_Page.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl_entity_is_not_abstract():
    assert not inspect.isabstract(eJSL_Entity)


def test_ejsl_entity_constructor_exists():
    assert callable(eJSL_Entity.__init__)


def test_ejsl_entity_constructor_args():
    sig = inspect.signature(eJSL_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "preserve" in params, "Missing parameter 'preserve'"
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl_entity_has_preserve():
    assert hasattr(eJSL_Entity, "preserve")
    descriptor = None
    for klass in eJSL_Entity.__mro__:
        if "preserve" in klass.__dict__:
            descriptor = klass.__dict__["preserve"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_entity_has_name():
    assert hasattr(eJSL_Entity, "name")
    descriptor = None
    for klass in eJSL_Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl_entitypackage_is_not_abstract():
    assert not inspect.isabstract(eJSL_Entitypackage)


def test_ejsl_entitypackage_constructor_exists():
    assert callable(eJSL_Entitypackage.__init__)


def test_ejsl_entitypackage_constructor_args():
    sig = inspect.signature(eJSL_Entitypackage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl_entitypackage_has_name():
    assert hasattr(eJSL_Entitypackage, "name")
    descriptor = None
    for klass in eJSL_Entitypackage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl_extension_is_not_abstract():
    assert not inspect.isabstract(eJSL_Extension)


def test_ejsl_extension_constructor_exists():
    assert callable(eJSL_Extension.__init__)


def test_ejsl_extension_constructor_args():
    sig = inspect.signature(eJSL_Extension.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl_extension_has_name():
    assert hasattr(eJSL_Extension, "name")
    descriptor = None
    for klass in eJSL_Extension.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl_pageaction_is_not_abstract():
    assert not inspect.isabstract(eJSL_PageAction)


def test_ejsl_pageaction_constructor_exists():
    assert callable(eJSL_PageAction.__init__)


def test_ejsl_pageaction_constructor_args():
    sig = inspect.signature(eJSL_PageAction.__init__)
    params = list(sig.parameters.keys())
    assert "pageActionType" in params, "Missing parameter 'pageActionType'"
    assert "pageActionPosition" in params, "Missing parameter 'pageActionPosition'"
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl_pageaction_has_pageActionType():
    assert hasattr(eJSL_PageAction, "pageActionType")
    descriptor = None
    for klass in eJSL_PageAction.__mro__:
        if "pageActionType" in klass.__dict__:
            descriptor = klass.__dict__["pageActionType"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_pageaction_has_pageActionPosition():
    assert hasattr(eJSL_PageAction, "pageActionPosition")
    descriptor = None
    for klass in eJSL_PageAction.__mro__:
        if "pageActionPosition" in klass.__dict__:
            descriptor = klass.__dict__["pageActionPosition"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_pageaction_has_name():
    assert hasattr(eJSL_PageAction, "name")
    descriptor = None
    for klass in eJSL_PageAction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl_keyvaluepair_is_not_abstract():
    assert not inspect.isabstract(eJSL_KeyValuePair)


def test_ejsl_keyvaluepair_constructor_exists():
    assert callable(eJSL_KeyValuePair.__init__)


def test_ejsl_keyvaluepair_constructor_args():
    sig = inspect.signature(eJSL_KeyValuePair.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl_keyvaluepair_has_value():
    assert hasattr(eJSL_KeyValuePair, "value")
    descriptor = None
    for klass in eJSL_KeyValuePair.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_keyvaluepair_has_name():
    assert hasattr(eJSL_KeyValuePair, "name")
    descriptor = None
    for klass in eJSL_KeyValuePair.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl_ejslmodel_is_not_abstract():
    assert not inspect.isabstract(eJSL_EJSLModel)


def test_ejsl_ejslmodel_constructor_exists():
    assert callable(eJSL_EJSLModel.__init__)


def test_ejsl_ejslmodel_constructor_args():
    sig = inspect.signature(eJSL_EJSLModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl_ejslmodel_has_name():
    assert hasattr(eJSL_EJSLModel, "name")
    descriptor = None
    for klass in eJSL_EJSLModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl_corefeature_is_not_abstract():
    assert not inspect.isabstract(eJSL_coreFeature)


def test_ejsl_corefeature_constructor_exists():
    assert callable(eJSL_coreFeature.__init__)


def test_ejsl_corefeature_constructor_args():
    sig = inspect.signature(eJSL_coreFeature.__init__)
    params = list(sig.parameters.keys())



def test_ejslpart_is_not_abstract():
    assert not inspect.isabstract(EJSLPart)


def test_ejslpart_constructor_exists():
    assert callable(EJSLPart.__init__)


def test_ejslpart_constructor_args():
    sig = inspect.signature(EJSLPart.__init__)
    params = list(sig.parameters.keys())



def test_ejsl_cmsextension_is_not_abstract():
    assert not inspect.isabstract(eJSL_CMSExtension)


def test_ejsl_cmsextension_constructor_exists():
    assert callable(eJSL_CMSExtension.__init__)


def test_ejsl_cmsextension_constructor_args():
    sig = inspect.signature(eJSL_CMSExtension.__init__)
    params = list(sig.parameters.keys())



def test_ejsl_cmscore_is_not_abstract():
    assert not inspect.isabstract(eJSL_CMSCore)


def test_ejsl_cmscore_constructor_exists():
    assert callable(eJSL_CMSCore.__init__)


def test_ejsl_cmscore_constructor_args():
    sig = inspect.signature(eJSL_CMSCore.__init__)
    params = list(sig.parameters.keys())



def test_ejsl_feature_is_not_abstract():
    assert not inspect.isabstract(eJSL_Feature)


def test_ejsl_feature_constructor_exists():
    assert callable(eJSL_Feature.__init__)


def test_ejsl_feature_constructor_args():
    sig = inspect.signature(eJSL_Feature.__init__)
    params = list(sig.parameters.keys())



def test_ejsl_parametergroup_is_not_abstract():
    assert not inspect.isabstract(eJSL_ParameterGroup)


def test_ejsl_parametergroup_constructor_exists():
    assert callable(eJSL_ParameterGroup.__init__)


def test_ejsl_parametergroup_constructor_args():
    sig = inspect.signature(eJSL_ParameterGroup.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl_parametergroup_has_label():
    assert hasattr(eJSL_ParameterGroup, "label")
    descriptor = None
    for klass in eJSL_ParameterGroup.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_parametergroup_has_name():
    assert hasattr(eJSL_ParameterGroup, "name")
    descriptor = None
    for klass in eJSL_ParameterGroup.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl_parameter_is_not_abstract():
    assert not inspect.isabstract(eJSL_Parameter)


def test_ejsl_parameter_constructor_exists():
    assert callable(eJSL_Parameter.__init__)


def test_ejsl_parameter_constructor_args():
    sig = inspect.signature(eJSL_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "defaultvalue" in params, "Missing parameter 'defaultvalue'"
    assert "descripton" in params, "Missing parameter 'descripton'"
    assert "name" in params, "Missing parameter 'name'"
    assert "size" in params, "Missing parameter 'size'"

def test_ejsl_parameter_has_label():
    assert hasattr(eJSL_Parameter, "label")
    descriptor = None
    for klass in eJSL_Parameter.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_parameter_has_defaultvalue():
    assert hasattr(eJSL_Parameter, "defaultvalue")
    descriptor = None
    for klass in eJSL_Parameter.__mro__:
        if "defaultvalue" in klass.__dict__:
            descriptor = klass.__dict__["defaultvalue"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_parameter_has_descripton():
    assert hasattr(eJSL_Parameter, "descripton")
    descriptor = None
    for klass in eJSL_Parameter.__mro__:
        if "descripton" in klass.__dict__:
            descriptor = klass.__dict__["descripton"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_parameter_has_name():
    assert hasattr(eJSL_Parameter, "name")
    descriptor = None
    for klass in eJSL_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_parameter_has_size():
    assert hasattr(eJSL_Parameter, "size")
    descriptor = None
    for klass in eJSL_Parameter.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_ejsl_datatype_is_not_abstract():
    assert not inspect.isabstract(eJSL_Datatype)


def test_ejsl_datatype_constructor_exists():
    assert callable(eJSL_Datatype.__init__)


def test_ejsl_datatype_constructor_args():
    sig = inspect.signature(eJSL_Datatype.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl_datatype_has_type():
    assert hasattr(eJSL_Datatype, "type")
    descriptor = None
    for klass in eJSL_Datatype.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_ejsl_datatype_has_name():
    assert hasattr(eJSL_Datatype, "name")
    descriptor = None
    for klass in eJSL_Datatype.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl_ejslpart_is_not_abstract():
    assert not inspect.isabstract(eJSL_EJSLPart)


def test_ejsl_ejslpart_constructor_exists():
    assert callable(eJSL_EJSLPart.__init__)


def test_ejsl_ejslpart_constructor_args():
    sig = inspect.signature(eJSL_EJSLPart.__init__)
    params = list(sig.parameters.keys())

def test_complexhtmltypekinds_exists():
    # Check that the Enumeration exists
    assert ComplexHTMLTypeKinds is not None

def test_complexhtmltypekinds_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComplexHTMLTypeKinds]
    expected_literals = [
        "Select",
        "Radiobutton",
        "Multiselect",
        "Checkbox",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComplexHTMLTypeKinds"

def test_pluginkinds_exists():
    # Check that the Enumeration exists
    assert PluginKinds is not None

def test_pluginkinds_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PluginKinds]
    expected_literals = [
        "authenticate",
        "content",
        "contact",
        "quick_icons",
        "search",
        "user",
        "editors",
        "extensions",
        "captcha",
        "xml_rpc",
        "system",
        "finder",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PluginKinds"

def test_simplehtmltypekinds_exists():
    # Check that the Enumeration exists
    assert SimpleHTMLTypeKinds is not None

def test_simplehtmltypekinds_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SimpleHTMLTypeKinds]
    expected_literals = [
        "Link",
        "Yes_No_Buttons",
        "Editor",
        "Text_Field_NE",
        "Textarea",
        "Filepicker",
        "Datepicker",
        "Integer",
        "Imagepicker",
        "Text_Field",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SimpleHTMLTypeKinds"

def test_corecomponent_exists():
    # Check that the Enumeration exists
    assert CoreComponent is not None

def test_corecomponent_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CoreComponent]
    expected_literals = [
        "User",
        "Content",
        "Menu",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CoreComponent"

def test_dataaccesskinds_exists():
    # Check that the Enumeration exists
    assert DataAccessKinds is not None

def test_dataaccesskinds_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataAccessKinds]
    expected_literals = [
        "database",
        "webservice",
        "frontendDAO",
        "backendDAO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataAccessKinds"

def test_pageactionpositionkind_exists():
    # Check that the Enumeration exists
    assert PageActionPositionKind is not None

def test_pageactionpositionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PageActionPositionKind]
    expected_literals = [
        "center",
        "top",
        "bottom",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PageActionPositionKind"

def test_pageactionkind_exists():
    # Check that the Enumeration exists
    assert PageActionKind is not None

def test_pageactionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PageActionKind]
    expected_literals = [
        "SAVE",
        "PUBLISH",
        "PWRESET",
        "HIDE",
        "CHECKIN",
        "NEW",
        "EDIT",
        "TRASH",
        "LOGIN",
        "SAVE_COPY",
        "CANCEL",
        "CLOSE",
        "UNPUBLISH",
        "INDIVIDUAL",
        "SAVE_CLOSE",
        "ARCHIVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PageActionKind"

def test_standardtypekinds_exists():
    # Check that the Enumeration exists
    assert StandardTypeKinds is not None

def test_standardtypekinds_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StandardTypeKinds]
    expected_literals = [
        "File",
        "Link",
        "Time",
        "Encrypted_Text",
        "Text",
        "Date",
        "Integer",
        "Datetime",
        "Image",
        "Boolean",
        "Label",
        "Short_Text",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StandardTypeKinds"

def test_pagekinds_exists():
    # Check that the Enumeration exists
    assert PageKinds is not None

def test_pagekinds_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PageKinds]
    expected_literals = [
        "list",
        "details",
        "custom",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PageKinds"


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
eJSL_PositionParameter_strategy = st.builds(
    eJSL_PositionParameter,
    divid=
        safe_text,
    type=
        safe_text,
    name=
        safe_text
)
eJSL_MethodParameter_strategy = st.builds(
    eJSL_MethodParameter,
    name=
        safe_text
)
eJSL_Method_strategy = st.builds(
    eJSL_Method,
    returnvalue=
        safe_text,
    name=
        safe_text
)
eJSL_Package_strategy = st.builds(
    eJSL_Package,
    name=
        safe_text
)
eJSL_Class_strategy = st.builds(
    eJSL_Class,
    name=
        safe_text
)
eJSL_Author_strategy = st.builds(
    eJSL_Author,
    authorurl=
        safe_text,
    name=
        safe_text,
    authoremail=
        safe_text
)
eJSL_CssBlock_strategy = st.builds(
    eJSL_CssBlock,
    selector=
        safe_text
)
eJSL_Position_strategy = st.builds(
    eJSL_Position,
    name=
        safe_text
)
eJSL_ComponentReference_strategy = st.builds(
    eJSL_ComponentReference,
    core=
        safe_text
)
Section_strategy = st.builds(
    Section,
)
eJSL_BackendSection_strategy = st.builds(
    eJSL_BackendSection,
)
eJSL_PageReference_strategy = st.builds(
    eJSL_PageReference,
    sect=
        safe_text
)
Extension_strategy = st.builds(
    Extension,
)
eJSL_Component_strategy = st.builds(
    eJSL_Component,
)
eJSL_Template_strategy = st.builds(
    eJSL_Template,
)
eJSL_ExtensionPackage_strategy = st.builds(
    eJSL_ExtensionPackage,
)
eJSL_Language_strategy = st.builds(
    eJSL_Language,
    sys=
        st.booleans(),
    name=
        safe_text
)
eJSL_Manifestation_strategy = st.builds(
    eJSL_Manifestation,
    description=
        safe_text,
    license=
        safe_text,
    copyright=
        safe_text,
    link=
        safe_text,
    creationdate=
        safe_text,
    version=
        safe_text
)
eJSL_LinkParameter_strategy = st.builds(
    eJSL_LinkParameter,
    name=
        safe_text,
    value=
        safe_text,
    id=
        st.booleans()
)
InternalLink_strategy = st.builds(
    InternalLink,
)
eJSL_ContextLink_strategy = st.builds(
    eJSL_ContextLink,
)
eJSL_Library_strategy = st.builds(
    eJSL_Library,
)
eJSL_Plugin_strategy = st.builds(
    eJSL_Plugin,
    type=
        safe_text
)
eJSL_Module_strategy = st.builds(
    eJSL_Module,
)
eJSL_FrontendSection_strategy = st.builds(
    eJSL_FrontendSection,
)
eJSL_DetailPageField_strategy = st.builds(
    eJSL_DetailPageField,
)
DynamicPage_strategy = st.builds(
    DynamicPage,
)
eJSL_DetailsPage_strategy = st.builds(
    eJSL_DetailsPage,
)
eJSL_IndexPage_strategy = st.builds(
    eJSL_IndexPage,
)
Link_strategy = st.builds(
    Link,
)
eJSL_InternalLink_strategy = st.builds(
    eJSL_InternalLink,
    name=
        safe_text
)
eJSL_ExternalLink_strategy = st.builds(
    eJSL_ExternalLink,
    label=
        safe_text,
    target=
        safe_text
)
eJSL_Reference_strategy = st.builds(
    eJSL_Reference,
    lower=
        safe_text,
    preserve=
        st.booleans(),
    upper=
        safe_text,
    id=
        st.booleans()
)
eJSL_Attribute_strategy = st.builds(
    eJSL_Attribute,
    preserve=
        st.booleans(),
    isunique=
        st.booleans(),
    name=
        safe_text,
    isprimary=
        st.booleans(),
    id=
        st.booleans()
)
Page_strategy = st.builds(
    Page,
)
eJSL_DynamicPage_strategy = st.builds(
    eJSL_DynamicPage,
    preserve=
        st.booleans()
)
eJSL_CustomPage_strategy = st.builds(
    eJSL_CustomPage,
    pageType=
        safe_text,
    preserve=
        safe_text
)
eJSL_StaticPage_strategy = st.builds(
    eJSL_StaticPage,
    HTMLBody=
        safe_text,
    preserve=
        st.booleans()
)
eJSL_Link_strategy = st.builds(
    eJSL_Link,
)
eJSL_HTMLTypes_strategy = st.builds(
    eJSL_HTMLTypes,
)
HTMLTypes_strategy = st.builds(
    HTMLTypes,
)
eJSL_SimpleHTMLTypes_strategy = st.builds(
    eJSL_SimpleHTMLTypes,
    htmltype=
        safe_text
)
eJSL_ComplexHTMLTypes_strategy = st.builds(
    eJSL_ComplexHTMLTypes,
    htmltype=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
eJSL_StandardTypes_strategy = st.builds(
    eJSL_StandardTypes,
    type=
        safe_text,
    autoincrement=
        st.booleans(),
    notnull=
        st.booleans(),
    default=
        safe_text
)
eJSL_DatatypeReference_strategy = st.builds(
    eJSL_DatatypeReference,
)
eJSL_Type_strategy = st.builds(
    eJSL_Type,
)
eJSL_Section_strategy = st.builds(
    eJSL_Section,
)
eJSL_Page_strategy = st.builds(
    eJSL_Page,
    name=
        safe_text
)
eJSL_Entity_strategy = st.builds(
    eJSL_Entity,
    preserve=
        st.booleans(),
    name=
        safe_text
)
eJSL_Entitypackage_strategy = st.builds(
    eJSL_Entitypackage,
    name=
        safe_text
)
eJSL_Extension_strategy = st.builds(
    eJSL_Extension,
    name=
        safe_text
)
eJSL_PageAction_strategy = st.builds(
    eJSL_PageAction,
    pageActionType=
        safe_text,
    pageActionPosition=
        safe_text,
    name=
        safe_text
)
eJSL_KeyValuePair_strategy = st.builds(
    eJSL_KeyValuePair,
    value=
        safe_text,
    name=
        safe_text
)
eJSL_EJSLModel_strategy = st.builds(
    eJSL_EJSLModel,
    name=
        safe_text
)
eJSL_coreFeature_strategy = st.builds(
    eJSL_coreFeature,
)
EJSLPart_strategy = st.builds(
    EJSLPart,
)
eJSL_CMSExtension_strategy = st.builds(
    eJSL_CMSExtension,
)
eJSL_CMSCore_strategy = st.builds(
    eJSL_CMSCore,
)
eJSL_Feature_strategy = st.builds(
    eJSL_Feature,
)
eJSL_ParameterGroup_strategy = st.builds(
    eJSL_ParameterGroup,
    label=
        safe_text,
    name=
        safe_text
)
eJSL_Parameter_strategy = st.builds(
    eJSL_Parameter,
    label=
        safe_text,
    defaultvalue=
        safe_text,
    descripton=
        safe_text,
    name=
        safe_text,
    size=
        st.integers()
)
eJSL_Datatype_strategy = st.builds(
    eJSL_Datatype,
    type=
        safe_text,
    name=
        safe_text
)
eJSL_EJSLPart_strategy = st.builds(
    eJSL_EJSLPart,
)

@given(instance=eJSL_PositionParameter_strategy)
@settings(max_examples=50)
def test_ejsl_positionparameter_instantiation(instance):
    assert isinstance(instance, eJSL_PositionParameter)



@given(instance=eJSL_PositionParameter_strategy)
def test_ejsl_positionparameter_divid_setter(instance):
    original = instance.divid
    instance.divid = original
    assert instance.divid == original



@given(instance=eJSL_PositionParameter_strategy)
def test_ejsl_positionparameter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=eJSL_PositionParameter_strategy)
def test_ejsl_positionparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL_MethodParameter_strategy)
@settings(max_examples=50)
def test_ejsl_methodparameter_instantiation(instance):
    assert isinstance(instance, eJSL_MethodParameter)



@given(instance=eJSL_MethodParameter_strategy)
def test_ejsl_methodparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL_Method_strategy)
@settings(max_examples=50)
def test_ejsl_method_instantiation(instance):
    assert isinstance(instance, eJSL_Method)



@given(instance=eJSL_Method_strategy)
def test_ejsl_method_returnvalue_setter(instance):
    original = instance.returnvalue
    instance.returnvalue = original
    assert instance.returnvalue == original



@given(instance=eJSL_Method_strategy)
def test_ejsl_method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL_Package_strategy)
@settings(max_examples=50)
def test_ejsl_package_instantiation(instance):
    assert isinstance(instance, eJSL_Package)



@given(instance=eJSL_Package_strategy)
def test_ejsl_package_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL_Class_strategy)
@settings(max_examples=50)
def test_ejsl_class_instantiation(instance):
    assert isinstance(instance, eJSL_Class)



@given(instance=eJSL_Class_strategy)
def test_ejsl_class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL_Author_strategy)
@settings(max_examples=50)
def test_ejsl_author_instantiation(instance):
    assert isinstance(instance, eJSL_Author)



@given(instance=eJSL_Author_strategy)
def test_ejsl_author_authorurl_setter(instance):
    original = instance.authorurl
    instance.authorurl = original
    assert instance.authorurl == original



@given(instance=eJSL_Author_strategy)
def test_ejsl_author_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=eJSL_Author_strategy)
def test_ejsl_author_authoremail_setter(instance):
    original = instance.authoremail
    instance.authoremail = original
    assert instance.authoremail == original

@given(instance=eJSL_CssBlock_strategy)
@settings(max_examples=50)
def test_ejsl_cssblock_instantiation(instance):
    assert isinstance(instance, eJSL_CssBlock)



@given(instance=eJSL_CssBlock_strategy)
def test_ejsl_cssblock_selector_setter(instance):
    original = instance.selector
    instance.selector = original
    assert instance.selector == original

@given(instance=eJSL_Position_strategy)
@settings(max_examples=50)
def test_ejsl_position_instantiation(instance):
    assert isinstance(instance, eJSL_Position)



@given(instance=eJSL_Position_strategy)
def test_ejsl_position_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL_ComponentReference_strategy)
@settings(max_examples=50)
def test_ejsl_componentreference_instantiation(instance):
    assert isinstance(instance, eJSL_ComponentReference)



@given(instance=eJSL_ComponentReference_strategy)
def test_ejsl_componentreference_core_setter(instance):
    original = instance.core
    instance.core = original
    assert instance.core == original

@given(instance=Section_strategy)
@settings(max_examples=50)
def test_section_instantiation(instance):
    assert isinstance(instance, Section)

@given(instance=eJSL_BackendSection_strategy)
@settings(max_examples=50)
def test_ejsl_backendsection_instantiation(instance):
    assert isinstance(instance, eJSL_BackendSection)

@given(instance=eJSL_PageReference_strategy)
@settings(max_examples=50)
def test_ejsl_pagereference_instantiation(instance):
    assert isinstance(instance, eJSL_PageReference)



@given(instance=eJSL_PageReference_strategy)
def test_ejsl_pagereference_sect_setter(instance):
    original = instance.sect
    instance.sect = original
    assert instance.sect == original

@given(instance=Extension_strategy)
@settings(max_examples=50)
def test_extension_instantiation(instance):
    assert isinstance(instance, Extension)

@given(instance=eJSL_Component_strategy)
@settings(max_examples=50)
def test_ejsl_component_instantiation(instance):
    assert isinstance(instance, eJSL_Component)

@given(instance=eJSL_Template_strategy)
@settings(max_examples=50)
def test_ejsl_template_instantiation(instance):
    assert isinstance(instance, eJSL_Template)

@given(instance=eJSL_ExtensionPackage_strategy)
@settings(max_examples=50)
def test_ejsl_extensionpackage_instantiation(instance):
    assert isinstance(instance, eJSL_ExtensionPackage)

@given(instance=eJSL_Language_strategy)
@settings(max_examples=50)
def test_ejsl_language_instantiation(instance):
    assert isinstance(instance, eJSL_Language)



@given(instance=eJSL_Language_strategy)
def test_ejsl_language_sys_setter(instance):
    original = instance.sys
    instance.sys = original
    assert instance.sys == original



@given(instance=eJSL_Language_strategy)
def test_ejsl_language_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL_Manifestation_strategy)
@settings(max_examples=50)
def test_ejsl_manifestation_instantiation(instance):
    assert isinstance(instance, eJSL_Manifestation)



@given(instance=eJSL_Manifestation_strategy)
def test_ejsl_manifestation_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=eJSL_Manifestation_strategy)
def test_ejsl_manifestation_license_setter(instance):
    original = instance.license
    instance.license = original
    assert instance.license == original



@given(instance=eJSL_Manifestation_strategy)
def test_ejsl_manifestation_copyright_setter(instance):
    original = instance.copyright
    instance.copyright = original
    assert instance.copyright == original



@given(instance=eJSL_Manifestation_strategy)
def test_ejsl_manifestation_link_setter(instance):
    original = instance.link
    instance.link = original
    assert instance.link == original



@given(instance=eJSL_Manifestation_strategy)
def test_ejsl_manifestation_creationdate_setter(instance):
    original = instance.creationdate
    instance.creationdate = original
    assert instance.creationdate == original



@given(instance=eJSL_Manifestation_strategy)
def test_ejsl_manifestation_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=eJSL_LinkParameter_strategy)
@settings(max_examples=50)
def test_ejsl_linkparameter_instantiation(instance):
    assert isinstance(instance, eJSL_LinkParameter)



@given(instance=eJSL_LinkParameter_strategy)
def test_ejsl_linkparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=eJSL_LinkParameter_strategy)
def test_ejsl_linkparameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=eJSL_LinkParameter_strategy)
def test_ejsl_linkparameter_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=InternalLink_strategy)
@settings(max_examples=50)
def test_internallink_instantiation(instance):
    assert isinstance(instance, InternalLink)

@given(instance=eJSL_ContextLink_strategy)
@settings(max_examples=50)
def test_ejsl_contextlink_instantiation(instance):
    assert isinstance(instance, eJSL_ContextLink)

@given(instance=eJSL_Library_strategy)
@settings(max_examples=50)
def test_ejsl_library_instantiation(instance):
    assert isinstance(instance, eJSL_Library)

@given(instance=eJSL_Plugin_strategy)
@settings(max_examples=50)
def test_ejsl_plugin_instantiation(instance):
    assert isinstance(instance, eJSL_Plugin)



@given(instance=eJSL_Plugin_strategy)
def test_ejsl_plugin_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=eJSL_Module_strategy)
@settings(max_examples=50)
def test_ejsl_module_instantiation(instance):
    assert isinstance(instance, eJSL_Module)

@given(instance=eJSL_FrontendSection_strategy)
@settings(max_examples=50)
def test_ejsl_frontendsection_instantiation(instance):
    assert isinstance(instance, eJSL_FrontendSection)

@given(instance=eJSL_DetailPageField_strategy)
@settings(max_examples=50)
def test_ejsl_detailpagefield_instantiation(instance):
    assert isinstance(instance, eJSL_DetailPageField)

@given(instance=DynamicPage_strategy)
@settings(max_examples=50)
def test_dynamicpage_instantiation(instance):
    assert isinstance(instance, DynamicPage)

@given(instance=eJSL_DetailsPage_strategy)
@settings(max_examples=50)
def test_ejsl_detailspage_instantiation(instance):
    assert isinstance(instance, eJSL_DetailsPage)

@given(instance=eJSL_IndexPage_strategy)
@settings(max_examples=50)
def test_ejsl_indexpage_instantiation(instance):
    assert isinstance(instance, eJSL_IndexPage)

@given(instance=Link_strategy)
@settings(max_examples=50)
def test_link_instantiation(instance):
    assert isinstance(instance, Link)

@given(instance=eJSL_InternalLink_strategy)
@settings(max_examples=50)
def test_ejsl_internallink_instantiation(instance):
    assert isinstance(instance, eJSL_InternalLink)



@given(instance=eJSL_InternalLink_strategy)
def test_ejsl_internallink_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL_ExternalLink_strategy)
@settings(max_examples=50)
def test_ejsl_externallink_instantiation(instance):
    assert isinstance(instance, eJSL_ExternalLink)



@given(instance=eJSL_ExternalLink_strategy)
def test_ejsl_externallink_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=eJSL_ExternalLink_strategy)
def test_ejsl_externallink_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original

@given(instance=eJSL_Reference_strategy)
@settings(max_examples=50)
def test_ejsl_reference_instantiation(instance):
    assert isinstance(instance, eJSL_Reference)



@given(instance=eJSL_Reference_strategy)
def test_ejsl_reference_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=eJSL_Reference_strategy)
def test_ejsl_reference_preserve_setter(instance):
    original = instance.preserve
    instance.preserve = original
    assert instance.preserve == original



@given(instance=eJSL_Reference_strategy)
def test_ejsl_reference_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=eJSL_Reference_strategy)
def test_ejsl_reference_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=eJSL_Attribute_strategy)
@settings(max_examples=50)
def test_ejsl_attribute_instantiation(instance):
    assert isinstance(instance, eJSL_Attribute)



@given(instance=eJSL_Attribute_strategy)
def test_ejsl_attribute_preserve_setter(instance):
    original = instance.preserve
    instance.preserve = original
    assert instance.preserve == original



@given(instance=eJSL_Attribute_strategy)
def test_ejsl_attribute_isunique_setter(instance):
    original = instance.isunique
    instance.isunique = original
    assert instance.isunique == original



@given(instance=eJSL_Attribute_strategy)
def test_ejsl_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=eJSL_Attribute_strategy)
def test_ejsl_attribute_isprimary_setter(instance):
    original = instance.isprimary
    instance.isprimary = original
    assert instance.isprimary == original



@given(instance=eJSL_Attribute_strategy)
def test_ejsl_attribute_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Page_strategy)
@settings(max_examples=50)
def test_page_instantiation(instance):
    assert isinstance(instance, Page)

@given(instance=eJSL_DynamicPage_strategy)
@settings(max_examples=50)
def test_ejsl_dynamicpage_instantiation(instance):
    assert isinstance(instance, eJSL_DynamicPage)



@given(instance=eJSL_DynamicPage_strategy)
def test_ejsl_dynamicpage_preserve_setter(instance):
    original = instance.preserve
    instance.preserve = original
    assert instance.preserve == original

@given(instance=eJSL_CustomPage_strategy)
@settings(max_examples=50)
def test_ejsl_custompage_instantiation(instance):
    assert isinstance(instance, eJSL_CustomPage)



@given(instance=eJSL_CustomPage_strategy)
def test_ejsl_custompage_pageType_setter(instance):
    original = instance.pageType
    instance.pageType = original
    assert instance.pageType == original



@given(instance=eJSL_CustomPage_strategy)
def test_ejsl_custompage_preserve_setter(instance):
    original = instance.preserve
    instance.preserve = original
    assert instance.preserve == original

@given(instance=eJSL_StaticPage_strategy)
@settings(max_examples=50)
def test_ejsl_staticpage_instantiation(instance):
    assert isinstance(instance, eJSL_StaticPage)



@given(instance=eJSL_StaticPage_strategy)
def test_ejsl_staticpage_HTMLBody_setter(instance):
    original = instance.HTMLBody
    instance.HTMLBody = original
    assert instance.HTMLBody == original



@given(instance=eJSL_StaticPage_strategy)
def test_ejsl_staticpage_preserve_setter(instance):
    original = instance.preserve
    instance.preserve = original
    assert instance.preserve == original

@given(instance=eJSL_Link_strategy)
@settings(max_examples=50)
def test_ejsl_link_instantiation(instance):
    assert isinstance(instance, eJSL_Link)

@given(instance=eJSL_HTMLTypes_strategy)
@settings(max_examples=50)
def test_ejsl_htmltypes_instantiation(instance):
    assert isinstance(instance, eJSL_HTMLTypes)

@given(instance=HTMLTypes_strategy)
@settings(max_examples=50)
def test_htmltypes_instantiation(instance):
    assert isinstance(instance, HTMLTypes)

@given(instance=eJSL_SimpleHTMLTypes_strategy)
@settings(max_examples=50)
def test_ejsl_simplehtmltypes_instantiation(instance):
    assert isinstance(instance, eJSL_SimpleHTMLTypes)



@given(instance=eJSL_SimpleHTMLTypes_strategy)
def test_ejsl_simplehtmltypes_htmltype_setter(instance):
    original = instance.htmltype
    instance.htmltype = original
    assert instance.htmltype == original

@given(instance=eJSL_ComplexHTMLTypes_strategy)
@settings(max_examples=50)
def test_ejsl_complexhtmltypes_instantiation(instance):
    assert isinstance(instance, eJSL_ComplexHTMLTypes)



@given(instance=eJSL_ComplexHTMLTypes_strategy)
def test_ejsl_complexhtmltypes_htmltype_setter(instance):
    original = instance.htmltype
    instance.htmltype = original
    assert instance.htmltype == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=eJSL_StandardTypes_strategy)
@settings(max_examples=50)
def test_ejsl_standardtypes_instantiation(instance):
    assert isinstance(instance, eJSL_StandardTypes)



@given(instance=eJSL_StandardTypes_strategy)
def test_ejsl_standardtypes_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=eJSL_StandardTypes_strategy)
def test_ejsl_standardtypes_autoincrement_setter(instance):
    original = instance.autoincrement
    instance.autoincrement = original
    assert instance.autoincrement == original



@given(instance=eJSL_StandardTypes_strategy)
def test_ejsl_standardtypes_notnull_setter(instance):
    original = instance.notnull
    instance.notnull = original
    assert instance.notnull == original



@given(instance=eJSL_StandardTypes_strategy)
def test_ejsl_standardtypes_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=eJSL_DatatypeReference_strategy)
@settings(max_examples=50)
def test_ejsl_datatypereference_instantiation(instance):
    assert isinstance(instance, eJSL_DatatypeReference)

@given(instance=eJSL_Type_strategy)
@settings(max_examples=50)
def test_ejsl_type_instantiation(instance):
    assert isinstance(instance, eJSL_Type)

@given(instance=eJSL_Section_strategy)
@settings(max_examples=50)
def test_ejsl_section_instantiation(instance):
    assert isinstance(instance, eJSL_Section)

@given(instance=eJSL_Page_strategy)
@settings(max_examples=50)
def test_ejsl_page_instantiation(instance):
    assert isinstance(instance, eJSL_Page)



@given(instance=eJSL_Page_strategy)
def test_ejsl_page_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL_Entity_strategy)
@settings(max_examples=50)
def test_ejsl_entity_instantiation(instance):
    assert isinstance(instance, eJSL_Entity)



@given(instance=eJSL_Entity_strategy)
def test_ejsl_entity_preserve_setter(instance):
    original = instance.preserve
    instance.preserve = original
    assert instance.preserve == original



@given(instance=eJSL_Entity_strategy)
def test_ejsl_entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL_Entitypackage_strategy)
@settings(max_examples=50)
def test_ejsl_entitypackage_instantiation(instance):
    assert isinstance(instance, eJSL_Entitypackage)



@given(instance=eJSL_Entitypackage_strategy)
def test_ejsl_entitypackage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL_Extension_strategy)
@settings(max_examples=50)
def test_ejsl_extension_instantiation(instance):
    assert isinstance(instance, eJSL_Extension)



@given(instance=eJSL_Extension_strategy)
def test_ejsl_extension_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL_PageAction_strategy)
@settings(max_examples=50)
def test_ejsl_pageaction_instantiation(instance):
    assert isinstance(instance, eJSL_PageAction)



@given(instance=eJSL_PageAction_strategy)
def test_ejsl_pageaction_pageActionType_setter(instance):
    original = instance.pageActionType
    instance.pageActionType = original
    assert instance.pageActionType == original



@given(instance=eJSL_PageAction_strategy)
def test_ejsl_pageaction_pageActionPosition_setter(instance):
    original = instance.pageActionPosition
    instance.pageActionPosition = original
    assert instance.pageActionPosition == original



@given(instance=eJSL_PageAction_strategy)
def test_ejsl_pageaction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL_KeyValuePair_strategy)
@settings(max_examples=50)
def test_ejsl_keyvaluepair_instantiation(instance):
    assert isinstance(instance, eJSL_KeyValuePair)



@given(instance=eJSL_KeyValuePair_strategy)
def test_ejsl_keyvaluepair_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=eJSL_KeyValuePair_strategy)
def test_ejsl_keyvaluepair_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL_EJSLModel_strategy)
@settings(max_examples=50)
def test_ejsl_ejslmodel_instantiation(instance):
    assert isinstance(instance, eJSL_EJSLModel)



@given(instance=eJSL_EJSLModel_strategy)
def test_ejsl_ejslmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL_coreFeature_strategy)
@settings(max_examples=50)
def test_ejsl_corefeature_instantiation(instance):
    assert isinstance(instance, eJSL_coreFeature)

@given(instance=EJSLPart_strategy)
@settings(max_examples=50)
def test_ejslpart_instantiation(instance):
    assert isinstance(instance, EJSLPart)

@given(instance=eJSL_CMSExtension_strategy)
@settings(max_examples=50)
def test_ejsl_cmsextension_instantiation(instance):
    assert isinstance(instance, eJSL_CMSExtension)

@given(instance=eJSL_CMSCore_strategy)
@settings(max_examples=50)
def test_ejsl_cmscore_instantiation(instance):
    assert isinstance(instance, eJSL_CMSCore)

@given(instance=eJSL_Feature_strategy)
@settings(max_examples=50)
def test_ejsl_feature_instantiation(instance):
    assert isinstance(instance, eJSL_Feature)

@given(instance=eJSL_ParameterGroup_strategy)
@settings(max_examples=50)
def test_ejsl_parametergroup_instantiation(instance):
    assert isinstance(instance, eJSL_ParameterGroup)



@given(instance=eJSL_ParameterGroup_strategy)
def test_ejsl_parametergroup_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=eJSL_ParameterGroup_strategy)
def test_ejsl_parametergroup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL_Parameter_strategy)
@settings(max_examples=50)
def test_ejsl_parameter_instantiation(instance):
    assert isinstance(instance, eJSL_Parameter)



@given(instance=eJSL_Parameter_strategy)
def test_ejsl_parameter_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=eJSL_Parameter_strategy)
def test_ejsl_parameter_defaultvalue_setter(instance):
    original = instance.defaultvalue
    instance.defaultvalue = original
    assert instance.defaultvalue == original



@given(instance=eJSL_Parameter_strategy)
def test_ejsl_parameter_descripton_setter(instance):
    original = instance.descripton
    instance.descripton = original
    assert instance.descripton == original



@given(instance=eJSL_Parameter_strategy)
def test_ejsl_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=eJSL_Parameter_strategy)
def test_ejsl_parameter_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=eJSL_Datatype_strategy)
@settings(max_examples=50)
def test_ejsl_datatype_instantiation(instance):
    assert isinstance(instance, eJSL_Datatype)



@given(instance=eJSL_Datatype_strategy)
def test_ejsl_datatype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=eJSL_Datatype_strategy)
def test_ejsl_datatype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL_EJSLPart_strategy)
@settings(max_examples=50)
def test_ejsl_ejslpart_instantiation(instance):
    assert isinstance(instance, eJSL_EJSLPart)
