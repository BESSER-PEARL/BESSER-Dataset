import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    eJSL::PositionParameter,
    eJSL::MethodParameter,
    eJSL::Method,
    eJSL::Package,
    eJSL::Class,
    eJSL::Author,
    eJSL::CssBlock,
    eJSL::Position,
    eJSL::ComponentReference,
    Section,
    eJSL::BackendSection,
    eJSL::PageReference,
    Extension,
    eJSL::Template,
    eJSL::Component,
    eJSL::ExtensionPackage,
    eJSL::Language,
    eJSL::Manifestation,
    eJSL::LinkParameter,
    InternalLink,
    eJSL::ContextLink,
    eJSL::Library,
    eJSL::Plugin,
    eJSL::Module,
    eJSL::FrontendSection,
    eJSL::DetailPageField,
    DynamicPage,
    eJSL::DetailsPage,
    eJSL::IndexPage,
    Link,
    eJSL::InternalLink,
    eJSL::ExternalLink,
    eJSL::Reference,
    eJSL::Attribute,
    Page,
    eJSL::DynamicPage,
    eJSL::CustomPage,
    eJSL::StaticPage,
    eJSL::Link,
    eJSL::HTMLTypes,
    HTMLTypes,
    eJSL::SimpleHTMLTypes,
    eJSL::ComplexHTMLTypes,
    Type,
    eJSL::StandardTypes,
    eJSL::DatatypeReference,
    eJSL::Type,
    eJSL::Section,
    eJSL::Page,
    eJSL::Entity,
    eJSL::Entitypackage,
    eJSL::Extension,
    eJSL::PageAction,
    eJSL::KeyValuePair,
    eJSL::EJSLModel,
    eJSL::coreFeature,
    EJSLPart,
    eJSL::CMSExtension,
    eJSL::CMSCore,
    eJSL::Feature,
    eJSL::ParameterGroup,
    eJSL::Parameter,
    eJSL::Datatype,
    eJSL::EJSLPart,
    PageActionKind,
    StandardTypeKinds,
    PageActionPositionKind,
    DataAccessKinds,
    PageKinds,
    CoreComponent,
    SimpleHTMLTypeKinds,
    PluginKinds,
    ComplexHTMLTypeKinds,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ejsl::positionparameter_is_not_abstract():
    assert not inspect.isabstract(eJSL::PositionParameter)


def test_ejsl::positionparameter_constructor_exists():
    assert callable(eJSL::PositionParameter.__init__)


def test_ejsl::positionparameter_constructor_args():
    sig = inspect.signature(eJSL::PositionParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "divid" in params, "Missing parameter 'divid'"
    assert "type" in params, "Missing parameter 'type'"

def test_ejsl::positionparameter_has_name():
    assert hasattr(eJSL::PositionParameter, "name")
    descriptor = None
    for klass in eJSL::PositionParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::positionparameter_has_divid():
    assert hasattr(eJSL::PositionParameter, "divid")
    descriptor = None
    for klass in eJSL::PositionParameter.__mro__:
        if "divid" in klass.__dict__:
            descriptor = klass.__dict__["divid"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::positionparameter_has_type():
    assert hasattr(eJSL::PositionParameter, "type")
    descriptor = None
    for klass in eJSL::PositionParameter.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_ejsl::methodparameter_is_not_abstract():
    assert not inspect.isabstract(eJSL::MethodParameter)


def test_ejsl::methodparameter_constructor_exists():
    assert callable(eJSL::MethodParameter.__init__)


def test_ejsl::methodparameter_constructor_args():
    sig = inspect.signature(eJSL::MethodParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl::methodparameter_has_name():
    assert hasattr(eJSL::MethodParameter, "name")
    descriptor = None
    for klass in eJSL::MethodParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl::method_is_not_abstract():
    assert not inspect.isabstract(eJSL::Method)


def test_ejsl::method_constructor_exists():
    assert callable(eJSL::Method.__init__)


def test_ejsl::method_constructor_args():
    sig = inspect.signature(eJSL::Method.__init__)
    params = list(sig.parameters.keys())
    assert "returnvalue" in params, "Missing parameter 'returnvalue'"
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl::method_has_returnvalue():
    assert hasattr(eJSL::Method, "returnvalue")
    descriptor = None
    for klass in eJSL::Method.__mro__:
        if "returnvalue" in klass.__dict__:
            descriptor = klass.__dict__["returnvalue"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::method_has_name():
    assert hasattr(eJSL::Method, "name")
    descriptor = None
    for klass in eJSL::Method.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl::package_is_not_abstract():
    assert not inspect.isabstract(eJSL::Package)


def test_ejsl::package_constructor_exists():
    assert callable(eJSL::Package.__init__)


def test_ejsl::package_constructor_args():
    sig = inspect.signature(eJSL::Package.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl::package_has_name():
    assert hasattr(eJSL::Package, "name")
    descriptor = None
    for klass in eJSL::Package.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl::class_is_not_abstract():
    assert not inspect.isabstract(eJSL::Class)


def test_ejsl::class_constructor_exists():
    assert callable(eJSL::Class.__init__)


def test_ejsl::class_constructor_args():
    sig = inspect.signature(eJSL::Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl::class_has_name():
    assert hasattr(eJSL::Class, "name")
    descriptor = None
    for klass in eJSL::Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl::author_is_not_abstract():
    assert not inspect.isabstract(eJSL::Author)


def test_ejsl::author_constructor_exists():
    assert callable(eJSL::Author.__init__)


def test_ejsl::author_constructor_args():
    sig = inspect.signature(eJSL::Author.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "authoremail" in params, "Missing parameter 'authoremail'"
    assert "authorurl" in params, "Missing parameter 'authorurl'"

def test_ejsl::author_has_name():
    assert hasattr(eJSL::Author, "name")
    descriptor = None
    for klass in eJSL::Author.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::author_has_authoremail():
    assert hasattr(eJSL::Author, "authoremail")
    descriptor = None
    for klass in eJSL::Author.__mro__:
        if "authoremail" in klass.__dict__:
            descriptor = klass.__dict__["authoremail"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::author_has_authorurl():
    assert hasattr(eJSL::Author, "authorurl")
    descriptor = None
    for klass in eJSL::Author.__mro__:
        if "authorurl" in klass.__dict__:
            descriptor = klass.__dict__["authorurl"]
            break
    assert isinstance(descriptor, property)



def test_ejsl::cssblock_is_not_abstract():
    assert not inspect.isabstract(eJSL::CssBlock)


def test_ejsl::cssblock_constructor_exists():
    assert callable(eJSL::CssBlock.__init__)


def test_ejsl::cssblock_constructor_args():
    sig = inspect.signature(eJSL::CssBlock.__init__)
    params = list(sig.parameters.keys())
    assert "selector" in params, "Missing parameter 'selector'"

def test_ejsl::cssblock_has_selector():
    assert hasattr(eJSL::CssBlock, "selector")
    descriptor = None
    for klass in eJSL::CssBlock.__mro__:
        if "selector" in klass.__dict__:
            descriptor = klass.__dict__["selector"]
            break
    assert isinstance(descriptor, property)



def test_ejsl::position_is_not_abstract():
    assert not inspect.isabstract(eJSL::Position)


def test_ejsl::position_constructor_exists():
    assert callable(eJSL::Position.__init__)


def test_ejsl::position_constructor_args():
    sig = inspect.signature(eJSL::Position.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl::position_has_name():
    assert hasattr(eJSL::Position, "name")
    descriptor = None
    for klass in eJSL::Position.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl::componentreference_is_not_abstract():
    assert not inspect.isabstract(eJSL::ComponentReference)


def test_ejsl::componentreference_constructor_exists():
    assert callable(eJSL::ComponentReference.__init__)


def test_ejsl::componentreference_constructor_args():
    sig = inspect.signature(eJSL::ComponentReference.__init__)
    params = list(sig.parameters.keys())
    assert "core" in params, "Missing parameter 'core'"

def test_ejsl::componentreference_has_core():
    assert hasattr(eJSL::ComponentReference, "core")
    descriptor = None
    for klass in eJSL::ComponentReference.__mro__:
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



def test_ejsl::backendsection_is_not_abstract():
    assert not inspect.isabstract(eJSL::BackendSection)


def test_ejsl::backendsection_constructor_exists():
    assert callable(eJSL::BackendSection.__init__)


def test_ejsl::backendsection_constructor_args():
    sig = inspect.signature(eJSL::BackendSection.__init__)
    params = list(sig.parameters.keys())



def test_ejsl::pagereference_is_not_abstract():
    assert not inspect.isabstract(eJSL::PageReference)


def test_ejsl::pagereference_constructor_exists():
    assert callable(eJSL::PageReference.__init__)


def test_ejsl::pagereference_constructor_args():
    sig = inspect.signature(eJSL::PageReference.__init__)
    params = list(sig.parameters.keys())
    assert "sect" in params, "Missing parameter 'sect'"

def test_ejsl::pagereference_has_sect():
    assert hasattr(eJSL::PageReference, "sect")
    descriptor = None
    for klass in eJSL::PageReference.__mro__:
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



def test_ejsl::template_is_not_abstract():
    assert not inspect.isabstract(eJSL::Template)


def test_ejsl::template_constructor_exists():
    assert callable(eJSL::Template.__init__)


def test_ejsl::template_constructor_args():
    sig = inspect.signature(eJSL::Template.__init__)
    params = list(sig.parameters.keys())



def test_ejsl::component_is_not_abstract():
    assert not inspect.isabstract(eJSL::Component)


def test_ejsl::component_constructor_exists():
    assert callable(eJSL::Component.__init__)


def test_ejsl::component_constructor_args():
    sig = inspect.signature(eJSL::Component.__init__)
    params = list(sig.parameters.keys())



def test_ejsl::extensionpackage_is_not_abstract():
    assert not inspect.isabstract(eJSL::ExtensionPackage)


def test_ejsl::extensionpackage_constructor_exists():
    assert callable(eJSL::ExtensionPackage.__init__)


def test_ejsl::extensionpackage_constructor_args():
    sig = inspect.signature(eJSL::ExtensionPackage.__init__)
    params = list(sig.parameters.keys())



def test_ejsl::language_is_not_abstract():
    assert not inspect.isabstract(eJSL::Language)


def test_ejsl::language_constructor_exists():
    assert callable(eJSL::Language.__init__)


def test_ejsl::language_constructor_args():
    sig = inspect.signature(eJSL::Language.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "sys" in params, "Missing parameter 'sys'"

def test_ejsl::language_has_name():
    assert hasattr(eJSL::Language, "name")
    descriptor = None
    for klass in eJSL::Language.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::language_has_sys():
    assert hasattr(eJSL::Language, "sys")
    descriptor = None
    for klass in eJSL::Language.__mro__:
        if "sys" in klass.__dict__:
            descriptor = klass.__dict__["sys"]
            break
    assert isinstance(descriptor, property)



def test_ejsl::manifestation_is_not_abstract():
    assert not inspect.isabstract(eJSL::Manifestation)


def test_ejsl::manifestation_constructor_exists():
    assert callable(eJSL::Manifestation.__init__)


def test_ejsl::manifestation_constructor_args():
    sig = inspect.signature(eJSL::Manifestation.__init__)
    params = list(sig.parameters.keys())
    assert "link" in params, "Missing parameter 'link'"
    assert "copyright" in params, "Missing parameter 'copyright'"
    assert "version" in params, "Missing parameter 'version'"
    assert "license" in params, "Missing parameter 'license'"
    assert "creationdate" in params, "Missing parameter 'creationdate'"
    assert "description" in params, "Missing parameter 'description'"

def test_ejsl::manifestation_has_link():
    assert hasattr(eJSL::Manifestation, "link")
    descriptor = None
    for klass in eJSL::Manifestation.__mro__:
        if "link" in klass.__dict__:
            descriptor = klass.__dict__["link"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::manifestation_has_copyright():
    assert hasattr(eJSL::Manifestation, "copyright")
    descriptor = None
    for klass in eJSL::Manifestation.__mro__:
        if "copyright" in klass.__dict__:
            descriptor = klass.__dict__["copyright"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::manifestation_has_version():
    assert hasattr(eJSL::Manifestation, "version")
    descriptor = None
    for klass in eJSL::Manifestation.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::manifestation_has_license():
    assert hasattr(eJSL::Manifestation, "license")
    descriptor = None
    for klass in eJSL::Manifestation.__mro__:
        if "license" in klass.__dict__:
            descriptor = klass.__dict__["license"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::manifestation_has_creationdate():
    assert hasattr(eJSL::Manifestation, "creationdate")
    descriptor = None
    for klass in eJSL::Manifestation.__mro__:
        if "creationdate" in klass.__dict__:
            descriptor = klass.__dict__["creationdate"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::manifestation_has_description():
    assert hasattr(eJSL::Manifestation, "description")
    descriptor = None
    for klass in eJSL::Manifestation.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_ejsl::linkparameter_is_not_abstract():
    assert not inspect.isabstract(eJSL::LinkParameter)


def test_ejsl::linkparameter_constructor_exists():
    assert callable(eJSL::LinkParameter.__init__)


def test_ejsl::linkparameter_constructor_args():
    sig = inspect.signature(eJSL::LinkParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"
    assert "id" in params, "Missing parameter 'id'"

def test_ejsl::linkparameter_has_name():
    assert hasattr(eJSL::LinkParameter, "name")
    descriptor = None
    for klass in eJSL::LinkParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::linkparameter_has_value():
    assert hasattr(eJSL::LinkParameter, "value")
    descriptor = None
    for klass in eJSL::LinkParameter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::linkparameter_has_id():
    assert hasattr(eJSL::LinkParameter, "id")
    descriptor = None
    for klass in eJSL::LinkParameter.__mro__:
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



def test_ejsl::contextlink_is_not_abstract():
    assert not inspect.isabstract(eJSL::ContextLink)


def test_ejsl::contextlink_constructor_exists():
    assert callable(eJSL::ContextLink.__init__)


def test_ejsl::contextlink_constructor_args():
    sig = inspect.signature(eJSL::ContextLink.__init__)
    params = list(sig.parameters.keys())



def test_ejsl::library_is_not_abstract():
    assert not inspect.isabstract(eJSL::Library)


def test_ejsl::library_constructor_exists():
    assert callable(eJSL::Library.__init__)


def test_ejsl::library_constructor_args():
    sig = inspect.signature(eJSL::Library.__init__)
    params = list(sig.parameters.keys())



def test_ejsl::plugin_is_not_abstract():
    assert not inspect.isabstract(eJSL::Plugin)


def test_ejsl::plugin_constructor_exists():
    assert callable(eJSL::Plugin.__init__)


def test_ejsl::plugin_constructor_args():
    sig = inspect.signature(eJSL::Plugin.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_ejsl::plugin_has_type():
    assert hasattr(eJSL::Plugin, "type")
    descriptor = None
    for klass in eJSL::Plugin.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_ejsl::module_is_not_abstract():
    assert not inspect.isabstract(eJSL::Module)


def test_ejsl::module_constructor_exists():
    assert callable(eJSL::Module.__init__)


def test_ejsl::module_constructor_args():
    sig = inspect.signature(eJSL::Module.__init__)
    params = list(sig.parameters.keys())



def test_ejsl::frontendsection_is_not_abstract():
    assert not inspect.isabstract(eJSL::FrontendSection)


def test_ejsl::frontendsection_constructor_exists():
    assert callable(eJSL::FrontendSection.__init__)


def test_ejsl::frontendsection_constructor_args():
    sig = inspect.signature(eJSL::FrontendSection.__init__)
    params = list(sig.parameters.keys())



def test_ejsl::detailpagefield_is_not_abstract():
    assert not inspect.isabstract(eJSL::DetailPageField)


def test_ejsl::detailpagefield_constructor_exists():
    assert callable(eJSL::DetailPageField.__init__)


def test_ejsl::detailpagefield_constructor_args():
    sig = inspect.signature(eJSL::DetailPageField.__init__)
    params = list(sig.parameters.keys())



def test_dynamicpage_is_not_abstract():
    assert not inspect.isabstract(DynamicPage)


def test_dynamicpage_constructor_exists():
    assert callable(DynamicPage.__init__)


def test_dynamicpage_constructor_args():
    sig = inspect.signature(DynamicPage.__init__)
    params = list(sig.parameters.keys())



def test_ejsl::detailspage_is_not_abstract():
    assert not inspect.isabstract(eJSL::DetailsPage)


def test_ejsl::detailspage_constructor_exists():
    assert callable(eJSL::DetailsPage.__init__)


def test_ejsl::detailspage_constructor_args():
    sig = inspect.signature(eJSL::DetailsPage.__init__)
    params = list(sig.parameters.keys())



def test_ejsl::indexpage_is_not_abstract():
    assert not inspect.isabstract(eJSL::IndexPage)


def test_ejsl::indexpage_constructor_exists():
    assert callable(eJSL::IndexPage.__init__)


def test_ejsl::indexpage_constructor_args():
    sig = inspect.signature(eJSL::IndexPage.__init__)
    params = list(sig.parameters.keys())



def test_link_is_not_abstract():
    assert not inspect.isabstract(Link)


def test_link_constructor_exists():
    assert callable(Link.__init__)


def test_link_constructor_args():
    sig = inspect.signature(Link.__init__)
    params = list(sig.parameters.keys())



def test_ejsl::internallink_is_not_abstract():
    assert not inspect.isabstract(eJSL::InternalLink)


def test_ejsl::internallink_constructor_exists():
    assert callable(eJSL::InternalLink.__init__)


def test_ejsl::internallink_constructor_args():
    sig = inspect.signature(eJSL::InternalLink.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl::internallink_has_name():
    assert hasattr(eJSL::InternalLink, "name")
    descriptor = None
    for klass in eJSL::InternalLink.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl::externallink_is_not_abstract():
    assert not inspect.isabstract(eJSL::ExternalLink)


def test_ejsl::externallink_constructor_exists():
    assert callable(eJSL::ExternalLink.__init__)


def test_ejsl::externallink_constructor_args():
    sig = inspect.signature(eJSL::ExternalLink.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "target" in params, "Missing parameter 'target'"

def test_ejsl::externallink_has_label():
    assert hasattr(eJSL::ExternalLink, "label")
    descriptor = None
    for klass in eJSL::ExternalLink.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::externallink_has_target():
    assert hasattr(eJSL::ExternalLink, "target")
    descriptor = None
    for klass in eJSL::ExternalLink.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)



def test_ejsl::reference_is_not_abstract():
    assert not inspect.isabstract(eJSL::Reference)


def test_ejsl::reference_constructor_exists():
    assert callable(eJSL::Reference.__init__)


def test_ejsl::reference_constructor_args():
    sig = inspect.signature(eJSL::Reference.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "id" in params, "Missing parameter 'id'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "preserve" in params, "Missing parameter 'preserve'"

def test_ejsl::reference_has_upper():
    assert hasattr(eJSL::Reference, "upper")
    descriptor = None
    for klass in eJSL::Reference.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::reference_has_id():
    assert hasattr(eJSL::Reference, "id")
    descriptor = None
    for klass in eJSL::Reference.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::reference_has_lower():
    assert hasattr(eJSL::Reference, "lower")
    descriptor = None
    for klass in eJSL::Reference.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::reference_has_preserve():
    assert hasattr(eJSL::Reference, "preserve")
    descriptor = None
    for klass in eJSL::Reference.__mro__:
        if "preserve" in klass.__dict__:
            descriptor = klass.__dict__["preserve"]
            break
    assert isinstance(descriptor, property)



def test_ejsl::attribute_is_not_abstract():
    assert not inspect.isabstract(eJSL::Attribute)


def test_ejsl::attribute_constructor_exists():
    assert callable(eJSL::Attribute.__init__)


def test_ejsl::attribute_constructor_args():
    sig = inspect.signature(eJSL::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "isprimary" in params, "Missing parameter 'isprimary'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isunique" in params, "Missing parameter 'isunique'"
    assert "id" in params, "Missing parameter 'id'"
    assert "preserve" in params, "Missing parameter 'preserve'"

def test_ejsl::attribute_has_isprimary():
    assert hasattr(eJSL::Attribute, "isprimary")
    descriptor = None
    for klass in eJSL::Attribute.__mro__:
        if "isprimary" in klass.__dict__:
            descriptor = klass.__dict__["isprimary"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::attribute_has_name():
    assert hasattr(eJSL::Attribute, "name")
    descriptor = None
    for klass in eJSL::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::attribute_has_isunique():
    assert hasattr(eJSL::Attribute, "isunique")
    descriptor = None
    for klass in eJSL::Attribute.__mro__:
        if "isunique" in klass.__dict__:
            descriptor = klass.__dict__["isunique"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::attribute_has_id():
    assert hasattr(eJSL::Attribute, "id")
    descriptor = None
    for klass in eJSL::Attribute.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::attribute_has_preserve():
    assert hasattr(eJSL::Attribute, "preserve")
    descriptor = None
    for klass in eJSL::Attribute.__mro__:
        if "preserve" in klass.__dict__:
            descriptor = klass.__dict__["preserve"]
            break
    assert isinstance(descriptor, property)



def test_page_is_not_abstract():
    assert not inspect.isabstract(Page)


def test_page_constructor_exists():
    assert callable(Page.__init__)


def test_page_constructor_args():
    sig = inspect.signature(Page.__init__)
    params = list(sig.parameters.keys())



def test_ejsl::dynamicpage_is_not_abstract():
    assert not inspect.isabstract(eJSL::DynamicPage)


def test_ejsl::dynamicpage_constructor_exists():
    assert callable(eJSL::DynamicPage.__init__)


def test_ejsl::dynamicpage_constructor_args():
    sig = inspect.signature(eJSL::DynamicPage.__init__)
    params = list(sig.parameters.keys())
    assert "preserve" in params, "Missing parameter 'preserve'"

def test_ejsl::dynamicpage_has_preserve():
    assert hasattr(eJSL::DynamicPage, "preserve")
    descriptor = None
    for klass in eJSL::DynamicPage.__mro__:
        if "preserve" in klass.__dict__:
            descriptor = klass.__dict__["preserve"]
            break
    assert isinstance(descriptor, property)



def test_ejsl::custompage_is_not_abstract():
    assert not inspect.isabstract(eJSL::CustomPage)


def test_ejsl::custompage_constructor_exists():
    assert callable(eJSL::CustomPage.__init__)


def test_ejsl::custompage_constructor_args():
    sig = inspect.signature(eJSL::CustomPage.__init__)
    params = list(sig.parameters.keys())
    assert "preserve" in params, "Missing parameter 'preserve'"
    assert "pageType" in params, "Missing parameter 'pageType'"

def test_ejsl::custompage_has_preserve():
    assert hasattr(eJSL::CustomPage, "preserve")
    descriptor = None
    for klass in eJSL::CustomPage.__mro__:
        if "preserve" in klass.__dict__:
            descriptor = klass.__dict__["preserve"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::custompage_has_pageType():
    assert hasattr(eJSL::CustomPage, "pageType")
    descriptor = None
    for klass in eJSL::CustomPage.__mro__:
        if "pageType" in klass.__dict__:
            descriptor = klass.__dict__["pageType"]
            break
    assert isinstance(descriptor, property)



def test_ejsl::staticpage_is_not_abstract():
    assert not inspect.isabstract(eJSL::StaticPage)


def test_ejsl::staticpage_constructor_exists():
    assert callable(eJSL::StaticPage.__init__)


def test_ejsl::staticpage_constructor_args():
    sig = inspect.signature(eJSL::StaticPage.__init__)
    params = list(sig.parameters.keys())
    assert "preserve" in params, "Missing parameter 'preserve'"
    assert "HTMLBody" in params, "Missing parameter 'HTMLBody'"

def test_ejsl::staticpage_has_preserve():
    assert hasattr(eJSL::StaticPage, "preserve")
    descriptor = None
    for klass in eJSL::StaticPage.__mro__:
        if "preserve" in klass.__dict__:
            descriptor = klass.__dict__["preserve"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::staticpage_has_HTMLBody():
    assert hasattr(eJSL::StaticPage, "HTMLBody")
    descriptor = None
    for klass in eJSL::StaticPage.__mro__:
        if "HTMLBody" in klass.__dict__:
            descriptor = klass.__dict__["HTMLBody"]
            break
    assert isinstance(descriptor, property)



def test_ejsl::link_is_not_abstract():
    assert not inspect.isabstract(eJSL::Link)


def test_ejsl::link_constructor_exists():
    assert callable(eJSL::Link.__init__)


def test_ejsl::link_constructor_args():
    sig = inspect.signature(eJSL::Link.__init__)
    params = list(sig.parameters.keys())



def test_ejsl::htmltypes_is_not_abstract():
    assert not inspect.isabstract(eJSL::HTMLTypes)


def test_ejsl::htmltypes_constructor_exists():
    assert callable(eJSL::HTMLTypes.__init__)


def test_ejsl::htmltypes_constructor_args():
    sig = inspect.signature(eJSL::HTMLTypes.__init__)
    params = list(sig.parameters.keys())



def test_htmltypes_is_not_abstract():
    assert not inspect.isabstract(HTMLTypes)


def test_htmltypes_constructor_exists():
    assert callable(HTMLTypes.__init__)


def test_htmltypes_constructor_args():
    sig = inspect.signature(HTMLTypes.__init__)
    params = list(sig.parameters.keys())



def test_ejsl::simplehtmltypes_is_not_abstract():
    assert not inspect.isabstract(eJSL::SimpleHTMLTypes)


def test_ejsl::simplehtmltypes_constructor_exists():
    assert callable(eJSL::SimpleHTMLTypes.__init__)


def test_ejsl::simplehtmltypes_constructor_args():
    sig = inspect.signature(eJSL::SimpleHTMLTypes.__init__)
    params = list(sig.parameters.keys())
    assert "htmltype" in params, "Missing parameter 'htmltype'"

def test_ejsl::simplehtmltypes_has_htmltype():
    assert hasattr(eJSL::SimpleHTMLTypes, "htmltype")
    descriptor = None
    for klass in eJSL::SimpleHTMLTypes.__mro__:
        if "htmltype" in klass.__dict__:
            descriptor = klass.__dict__["htmltype"]
            break
    assert isinstance(descriptor, property)



def test_ejsl::complexhtmltypes_is_not_abstract():
    assert not inspect.isabstract(eJSL::ComplexHTMLTypes)


def test_ejsl::complexhtmltypes_constructor_exists():
    assert callable(eJSL::ComplexHTMLTypes.__init__)


def test_ejsl::complexhtmltypes_constructor_args():
    sig = inspect.signature(eJSL::ComplexHTMLTypes.__init__)
    params = list(sig.parameters.keys())
    assert "htmltype" in params, "Missing parameter 'htmltype'"

def test_ejsl::complexhtmltypes_has_htmltype():
    assert hasattr(eJSL::ComplexHTMLTypes, "htmltype")
    descriptor = None
    for klass in eJSL::ComplexHTMLTypes.__mro__:
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



def test_ejsl::standardtypes_is_not_abstract():
    assert not inspect.isabstract(eJSL::StandardTypes)


def test_ejsl::standardtypes_constructor_exists():
    assert callable(eJSL::StandardTypes.__init__)


def test_ejsl::standardtypes_constructor_args():
    sig = inspect.signature(eJSL::StandardTypes.__init__)
    params = list(sig.parameters.keys())
    assert "autoincrement" in params, "Missing parameter 'autoincrement'"
    assert "type" in params, "Missing parameter 'type'"
    assert "notnull" in params, "Missing parameter 'notnull'"
    assert "default" in params, "Missing parameter 'default'"

def test_ejsl::standardtypes_has_autoincrement():
    assert hasattr(eJSL::StandardTypes, "autoincrement")
    descriptor = None
    for klass in eJSL::StandardTypes.__mro__:
        if "autoincrement" in klass.__dict__:
            descriptor = klass.__dict__["autoincrement"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::standardtypes_has_type():
    assert hasattr(eJSL::StandardTypes, "type")
    descriptor = None
    for klass in eJSL::StandardTypes.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::standardtypes_has_notnull():
    assert hasattr(eJSL::StandardTypes, "notnull")
    descriptor = None
    for klass in eJSL::StandardTypes.__mro__:
        if "notnull" in klass.__dict__:
            descriptor = klass.__dict__["notnull"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::standardtypes_has_default():
    assert hasattr(eJSL::StandardTypes, "default")
    descriptor = None
    for klass in eJSL::StandardTypes.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_ejsl::datatypereference_is_not_abstract():
    assert not inspect.isabstract(eJSL::DatatypeReference)


def test_ejsl::datatypereference_constructor_exists():
    assert callable(eJSL::DatatypeReference.__init__)


def test_ejsl::datatypereference_constructor_args():
    sig = inspect.signature(eJSL::DatatypeReference.__init__)
    params = list(sig.parameters.keys())



def test_ejsl::type_is_not_abstract():
    assert not inspect.isabstract(eJSL::Type)


def test_ejsl::type_constructor_exists():
    assert callable(eJSL::Type.__init__)


def test_ejsl::type_constructor_args():
    sig = inspect.signature(eJSL::Type.__init__)
    params = list(sig.parameters.keys())



def test_ejsl::section_is_not_abstract():
    assert not inspect.isabstract(eJSL::Section)


def test_ejsl::section_constructor_exists():
    assert callable(eJSL::Section.__init__)


def test_ejsl::section_constructor_args():
    sig = inspect.signature(eJSL::Section.__init__)
    params = list(sig.parameters.keys())



def test_ejsl::page_is_not_abstract():
    assert not inspect.isabstract(eJSL::Page)


def test_ejsl::page_constructor_exists():
    assert callable(eJSL::Page.__init__)


def test_ejsl::page_constructor_args():
    sig = inspect.signature(eJSL::Page.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl::page_has_name():
    assert hasattr(eJSL::Page, "name")
    descriptor = None
    for klass in eJSL::Page.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl::entity_is_not_abstract():
    assert not inspect.isabstract(eJSL::Entity)


def test_ejsl::entity_constructor_exists():
    assert callable(eJSL::Entity.__init__)


def test_ejsl::entity_constructor_args():
    sig = inspect.signature(eJSL::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "preserve" in params, "Missing parameter 'preserve'"

def test_ejsl::entity_has_name():
    assert hasattr(eJSL::Entity, "name")
    descriptor = None
    for klass in eJSL::Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::entity_has_preserve():
    assert hasattr(eJSL::Entity, "preserve")
    descriptor = None
    for klass in eJSL::Entity.__mro__:
        if "preserve" in klass.__dict__:
            descriptor = klass.__dict__["preserve"]
            break
    assert isinstance(descriptor, property)



def test_ejsl::entitypackage_is_not_abstract():
    assert not inspect.isabstract(eJSL::Entitypackage)


def test_ejsl::entitypackage_constructor_exists():
    assert callable(eJSL::Entitypackage.__init__)


def test_ejsl::entitypackage_constructor_args():
    sig = inspect.signature(eJSL::Entitypackage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl::entitypackage_has_name():
    assert hasattr(eJSL::Entitypackage, "name")
    descriptor = None
    for klass in eJSL::Entitypackage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl::extension_is_not_abstract():
    assert not inspect.isabstract(eJSL::Extension)


def test_ejsl::extension_constructor_exists():
    assert callable(eJSL::Extension.__init__)


def test_ejsl::extension_constructor_args():
    sig = inspect.signature(eJSL::Extension.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl::extension_has_name():
    assert hasattr(eJSL::Extension, "name")
    descriptor = None
    for klass in eJSL::Extension.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl::pageaction_is_not_abstract():
    assert not inspect.isabstract(eJSL::PageAction)


def test_ejsl::pageaction_constructor_exists():
    assert callable(eJSL::PageAction.__init__)


def test_ejsl::pageaction_constructor_args():
    sig = inspect.signature(eJSL::PageAction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "pageActionPosition" in params, "Missing parameter 'pageActionPosition'"
    assert "pageActionType" in params, "Missing parameter 'pageActionType'"

def test_ejsl::pageaction_has_name():
    assert hasattr(eJSL::PageAction, "name")
    descriptor = None
    for klass in eJSL::PageAction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::pageaction_has_pageActionPosition():
    assert hasattr(eJSL::PageAction, "pageActionPosition")
    descriptor = None
    for klass in eJSL::PageAction.__mro__:
        if "pageActionPosition" in klass.__dict__:
            descriptor = klass.__dict__["pageActionPosition"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::pageaction_has_pageActionType():
    assert hasattr(eJSL::PageAction, "pageActionType")
    descriptor = None
    for klass in eJSL::PageAction.__mro__:
        if "pageActionType" in klass.__dict__:
            descriptor = klass.__dict__["pageActionType"]
            break
    assert isinstance(descriptor, property)



def test_ejsl::keyvaluepair_is_not_abstract():
    assert not inspect.isabstract(eJSL::KeyValuePair)


def test_ejsl::keyvaluepair_constructor_exists():
    assert callable(eJSL::KeyValuePair.__init__)


def test_ejsl::keyvaluepair_constructor_args():
    sig = inspect.signature(eJSL::KeyValuePair.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl::keyvaluepair_has_value():
    assert hasattr(eJSL::KeyValuePair, "value")
    descriptor = None
    for klass in eJSL::KeyValuePair.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::keyvaluepair_has_name():
    assert hasattr(eJSL::KeyValuePair, "name")
    descriptor = None
    for klass in eJSL::KeyValuePair.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl::ejslmodel_is_not_abstract():
    assert not inspect.isabstract(eJSL::EJSLModel)


def test_ejsl::ejslmodel_constructor_exists():
    assert callable(eJSL::EJSLModel.__init__)


def test_ejsl::ejslmodel_constructor_args():
    sig = inspect.signature(eJSL::EJSLModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl::ejslmodel_has_name():
    assert hasattr(eJSL::EJSLModel, "name")
    descriptor = None
    for klass in eJSL::EJSLModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl::corefeature_is_not_abstract():
    assert not inspect.isabstract(eJSL::coreFeature)


def test_ejsl::corefeature_constructor_exists():
    assert callable(eJSL::coreFeature.__init__)


def test_ejsl::corefeature_constructor_args():
    sig = inspect.signature(eJSL::coreFeature.__init__)
    params = list(sig.parameters.keys())



def test_ejslpart_is_not_abstract():
    assert not inspect.isabstract(EJSLPart)


def test_ejslpart_constructor_exists():
    assert callable(EJSLPart.__init__)


def test_ejslpart_constructor_args():
    sig = inspect.signature(EJSLPart.__init__)
    params = list(sig.parameters.keys())



def test_ejsl::cmsextension_is_not_abstract():
    assert not inspect.isabstract(eJSL::CMSExtension)


def test_ejsl::cmsextension_constructor_exists():
    assert callable(eJSL::CMSExtension.__init__)


def test_ejsl::cmsextension_constructor_args():
    sig = inspect.signature(eJSL::CMSExtension.__init__)
    params = list(sig.parameters.keys())



def test_ejsl::cmscore_is_not_abstract():
    assert not inspect.isabstract(eJSL::CMSCore)


def test_ejsl::cmscore_constructor_exists():
    assert callable(eJSL::CMSCore.__init__)


def test_ejsl::cmscore_constructor_args():
    sig = inspect.signature(eJSL::CMSCore.__init__)
    params = list(sig.parameters.keys())



def test_ejsl::feature_is_not_abstract():
    assert not inspect.isabstract(eJSL::Feature)


def test_ejsl::feature_constructor_exists():
    assert callable(eJSL::Feature.__init__)


def test_ejsl::feature_constructor_args():
    sig = inspect.signature(eJSL::Feature.__init__)
    params = list(sig.parameters.keys())



def test_ejsl::parametergroup_is_not_abstract():
    assert not inspect.isabstract(eJSL::ParameterGroup)


def test_ejsl::parametergroup_constructor_exists():
    assert callable(eJSL::ParameterGroup.__init__)


def test_ejsl::parametergroup_constructor_args():
    sig = inspect.signature(eJSL::ParameterGroup.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl::parametergroup_has_label():
    assert hasattr(eJSL::ParameterGroup, "label")
    descriptor = None
    for klass in eJSL::ParameterGroup.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::parametergroup_has_name():
    assert hasattr(eJSL::ParameterGroup, "name")
    descriptor = None
    for klass in eJSL::ParameterGroup.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl::parameter_is_not_abstract():
    assert not inspect.isabstract(eJSL::Parameter)


def test_ejsl::parameter_constructor_exists():
    assert callable(eJSL::Parameter.__init__)


def test_ejsl::parameter_constructor_args():
    sig = inspect.signature(eJSL::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "descripton" in params, "Missing parameter 'descripton'"
    assert "defaultvalue" in params, "Missing parameter 'defaultvalue'"
    assert "label" in params, "Missing parameter 'label'"
    assert "name" in params, "Missing parameter 'name'"

def test_ejsl::parameter_has_size():
    assert hasattr(eJSL::Parameter, "size")
    descriptor = None
    for klass in eJSL::Parameter.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::parameter_has_descripton():
    assert hasattr(eJSL::Parameter, "descripton")
    descriptor = None
    for klass in eJSL::Parameter.__mro__:
        if "descripton" in klass.__dict__:
            descriptor = klass.__dict__["descripton"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::parameter_has_defaultvalue():
    assert hasattr(eJSL::Parameter, "defaultvalue")
    descriptor = None
    for klass in eJSL::Parameter.__mro__:
        if "defaultvalue" in klass.__dict__:
            descriptor = klass.__dict__["defaultvalue"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::parameter_has_label():
    assert hasattr(eJSL::Parameter, "label")
    descriptor = None
    for klass in eJSL::Parameter.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::parameter_has_name():
    assert hasattr(eJSL::Parameter, "name")
    descriptor = None
    for klass in eJSL::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ejsl::datatype_is_not_abstract():
    assert not inspect.isabstract(eJSL::Datatype)


def test_ejsl::datatype_constructor_exists():
    assert callable(eJSL::Datatype.__init__)


def test_ejsl::datatype_constructor_args():
    sig = inspect.signature(eJSL::Datatype.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_ejsl::datatype_has_name():
    assert hasattr(eJSL::Datatype, "name")
    descriptor = None
    for klass in eJSL::Datatype.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ejsl::datatype_has_type():
    assert hasattr(eJSL::Datatype, "type")
    descriptor = None
    for klass in eJSL::Datatype.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_ejsl::ejslpart_is_not_abstract():
    assert not inspect.isabstract(eJSL::EJSLPart)


def test_ejsl::ejslpart_constructor_exists():
    assert callable(eJSL::EJSLPart.__init__)


def test_ejsl::ejslpart_constructor_args():
    sig = inspect.signature(eJSL::EJSLPart.__init__)
    params = list(sig.parameters.keys())

def test_pageactionkind_exists():
    # Check that the Enumeration exists
    assert PageActionKind is not None

def test_pageactionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PageActionKind]
    expected_literals = [
        "NEW",
        "PUBLISH",
        "CHECKIN",
        "HIDE",
        "TRASH",
        "SAVE",
        "CLOSE",
        "SAVE_COPY",
        "PWRESET",
        "CANCEL",
        "SAVE_CLOSE",
        "EDIT",
        "UNPUBLISH",
        "INDIVIDUAL",
        "ARCHIVE",
        "LOGIN",
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
        "Text",
        "Image",
        "Time",
        "Integer",
        "Datetime",
        "Label",
        "Boolean",
        "Link",
        "Short_Text",
        "Date",
        "File",
        "Encrypted_Text",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StandardTypeKinds"

def test_pageactionpositionkind_exists():
    # Check that the Enumeration exists
    assert PageActionPositionKind is not None

def test_pageactionpositionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PageActionPositionKind]
    expected_literals = [
        "top",
        "center",
        "bottom",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PageActionPositionKind"

def test_dataaccesskinds_exists():
    # Check that the Enumeration exists
    assert DataAccessKinds is not None

def test_dataaccesskinds_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataAccessKinds]
    expected_literals = [
        "webservice",
        "database",
        "frontendDAO",
        "backendDAO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataAccessKinds"

def test_pagekinds_exists():
    # Check that the Enumeration exists
    assert PageKinds is not None

def test_pagekinds_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PageKinds]
    expected_literals = [
        "custom",
        "list",
        "details",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PageKinds"

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

def test_simplehtmltypekinds_exists():
    # Check that the Enumeration exists
    assert SimpleHTMLTypeKinds is not None

def test_simplehtmltypekinds_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SimpleHTMLTypeKinds]
    expected_literals = [
        "Editor",
        "Text_Field",
        "Filepicker",
        "Link",
        "Integer",
        "Yes_No_Buttons",
        "Textarea",
        "Datepicker",
        "Imagepicker",
        "Text_Field_NE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SimpleHTMLTypeKinds"

def test_pluginkinds_exists():
    # Check that the Enumeration exists
    assert PluginKinds is not None

def test_pluginkinds_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PluginKinds]
    expected_literals = [
        "extensions",
        "contact",
        "authenticate",
        "user",
        "quick_icons",
        "search",
        "xml_rpc",
        "captcha",
        "editors",
        "content",
        "finder",
        "system",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PluginKinds"

def test_complexhtmltypekinds_exists():
    # Check that the Enumeration exists
    assert ComplexHTMLTypeKinds is not None

def test_complexhtmltypekinds_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComplexHTMLTypeKinds]
    expected_literals = [
        "Multiselect",
        "Radiobutton",
        "Checkbox",
        "Select",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComplexHTMLTypeKinds"


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
eJSL::PositionParameter_strategy = st.builds(
    eJSL::PositionParameter,
    name=
        safe_text,
    divid=
        safe_text,
    type=
        safe_text
)
eJSL::MethodParameter_strategy = st.builds(
    eJSL::MethodParameter,
    name=
        safe_text
)
eJSL::Method_strategy = st.builds(
    eJSL::Method,
    returnvalue=
        safe_text,
    name=
        safe_text
)
eJSL::Package_strategy = st.builds(
    eJSL::Package,
    name=
        safe_text
)
eJSL::Class_strategy = st.builds(
    eJSL::Class,
    name=
        safe_text
)
eJSL::Author_strategy = st.builds(
    eJSL::Author,
    name=
        safe_text,
    authoremail=
        safe_text,
    authorurl=
        safe_text
)
eJSL::CssBlock_strategy = st.builds(
    eJSL::CssBlock,
    selector=
        safe_text
)
eJSL::Position_strategy = st.builds(
    eJSL::Position,
    name=
        safe_text
)
eJSL::ComponentReference_strategy = st.builds(
    eJSL::ComponentReference,
    core=
        safe_text
)
Section_strategy = st.builds(
    Section,
)
eJSL::BackendSection_strategy = st.builds(
    eJSL::BackendSection,
)
eJSL::PageReference_strategy = st.builds(
    eJSL::PageReference,
    sect=
        safe_text
)
Extension_strategy = st.builds(
    Extension,
)
eJSL::Template_strategy = st.builds(
    eJSL::Template,
)
eJSL::Component_strategy = st.builds(
    eJSL::Component,
)
eJSL::ExtensionPackage_strategy = st.builds(
    eJSL::ExtensionPackage,
)
eJSL::Language_strategy = st.builds(
    eJSL::Language,
    name=
        safe_text,
    sys=
        st.booleans()
)
eJSL::Manifestation_strategy = st.builds(
    eJSL::Manifestation,
    link=
        safe_text,
    copyright=
        safe_text,
    version=
        safe_text,
    license=
        safe_text,
    creationdate=
        safe_text,
    description=
        safe_text
)
eJSL::LinkParameter_strategy = st.builds(
    eJSL::LinkParameter,
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
eJSL::ContextLink_strategy = st.builds(
    eJSL::ContextLink,
)
eJSL::Library_strategy = st.builds(
    eJSL::Library,
)
eJSL::Plugin_strategy = st.builds(
    eJSL::Plugin,
    type=
        safe_text
)
eJSL::Module_strategy = st.builds(
    eJSL::Module,
)
eJSL::FrontendSection_strategy = st.builds(
    eJSL::FrontendSection,
)
eJSL::DetailPageField_strategy = st.builds(
    eJSL::DetailPageField,
)
DynamicPage_strategy = st.builds(
    DynamicPage,
)
eJSL::DetailsPage_strategy = st.builds(
    eJSL::DetailsPage,
)
eJSL::IndexPage_strategy = st.builds(
    eJSL::IndexPage,
)
Link_strategy = st.builds(
    Link,
)
eJSL::InternalLink_strategy = st.builds(
    eJSL::InternalLink,
    name=
        safe_text
)
eJSL::ExternalLink_strategy = st.builds(
    eJSL::ExternalLink,
    label=
        safe_text,
    target=
        safe_text
)
eJSL::Reference_strategy = st.builds(
    eJSL::Reference,
    upper=
        safe_text,
    id=
        st.booleans(),
    lower=
        safe_text,
    preserve=
        st.booleans()
)
eJSL::Attribute_strategy = st.builds(
    eJSL::Attribute,
    isprimary=
        st.booleans(),
    name=
        safe_text,
    isunique=
        st.booleans(),
    id=
        st.booleans(),
    preserve=
        st.booleans()
)
Page_strategy = st.builds(
    Page,
)
eJSL::DynamicPage_strategy = st.builds(
    eJSL::DynamicPage,
    preserve=
        st.booleans()
)
eJSL::CustomPage_strategy = st.builds(
    eJSL::CustomPage,
    preserve=
        safe_text,
    pageType=
        safe_text
)
eJSL::StaticPage_strategy = st.builds(
    eJSL::StaticPage,
    preserve=
        st.booleans(),
    HTMLBody=
        safe_text
)
eJSL::Link_strategy = st.builds(
    eJSL::Link,
)
eJSL::HTMLTypes_strategy = st.builds(
    eJSL::HTMLTypes,
)
HTMLTypes_strategy = st.builds(
    HTMLTypes,
)
eJSL::SimpleHTMLTypes_strategy = st.builds(
    eJSL::SimpleHTMLTypes,
    htmltype=
        safe_text
)
eJSL::ComplexHTMLTypes_strategy = st.builds(
    eJSL::ComplexHTMLTypes,
    htmltype=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
eJSL::StandardTypes_strategy = st.builds(
    eJSL::StandardTypes,
    autoincrement=
        st.booleans(),
    type=
        safe_text,
    notnull=
        st.booleans(),
    default=
        safe_text
)
eJSL::DatatypeReference_strategy = st.builds(
    eJSL::DatatypeReference,
)
eJSL::Type_strategy = st.builds(
    eJSL::Type,
)
eJSL::Section_strategy = st.builds(
    eJSL::Section,
)
eJSL::Page_strategy = st.builds(
    eJSL::Page,
    name=
        safe_text
)
eJSL::Entity_strategy = st.builds(
    eJSL::Entity,
    name=
        safe_text,
    preserve=
        st.booleans()
)
eJSL::Entitypackage_strategy = st.builds(
    eJSL::Entitypackage,
    name=
        safe_text
)
eJSL::Extension_strategy = st.builds(
    eJSL::Extension,
    name=
        safe_text
)
eJSL::PageAction_strategy = st.builds(
    eJSL::PageAction,
    name=
        safe_text,
    pageActionPosition=
        safe_text,
    pageActionType=
        safe_text
)
eJSL::KeyValuePair_strategy = st.builds(
    eJSL::KeyValuePair,
    value=
        safe_text,
    name=
        safe_text
)
eJSL::EJSLModel_strategy = st.builds(
    eJSL::EJSLModel,
    name=
        safe_text
)
eJSL::coreFeature_strategy = st.builds(
    eJSL::coreFeature,
)
EJSLPart_strategy = st.builds(
    EJSLPart,
)
eJSL::CMSExtension_strategy = st.builds(
    eJSL::CMSExtension,
)
eJSL::CMSCore_strategy = st.builds(
    eJSL::CMSCore,
)
eJSL::Feature_strategy = st.builds(
    eJSL::Feature,
)
eJSL::ParameterGroup_strategy = st.builds(
    eJSL::ParameterGroup,
    label=
        safe_text,
    name=
        safe_text
)
eJSL::Parameter_strategy = st.builds(
    eJSL::Parameter,
    size=
        st.integers(),
    descripton=
        safe_text,
    defaultvalue=
        safe_text,
    label=
        safe_text,
    name=
        safe_text
)
eJSL::Datatype_strategy = st.builds(
    eJSL::Datatype,
    name=
        safe_text,
    type=
        safe_text
)
eJSL::EJSLPart_strategy = st.builds(
    eJSL::EJSLPart,
)

@given(instance=eJSL::PositionParameter_strategy)
@settings(max_examples=50)
def test_ejsl::positionparameter_instantiation(instance):
    assert isinstance(instance, eJSL::PositionParameter)

@given(instance=eJSL::PositionParameter_strategy)
def test_ejsl::positionparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eJSL::PositionParameter_strategy)
def test_ejsl::positionparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL::PositionParameter_strategy)
def test_ejsl::positionparameter_divid_type(instance):
    assert isinstance(instance.divid, str)


@given(instance=eJSL::PositionParameter_strategy)
def test_ejsl::positionparameter_divid_setter(instance):
    original = instance.divid
    instance.divid = original
    assert instance.divid == original

@given(instance=eJSL::PositionParameter_strategy)
def test_ejsl::positionparameter_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=eJSL::PositionParameter_strategy)
def test_ejsl::positionparameter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=eJSL::MethodParameter_strategy)
@settings(max_examples=50)
def test_ejsl::methodparameter_instantiation(instance):
    assert isinstance(instance, eJSL::MethodParameter)

@given(instance=eJSL::MethodParameter_strategy)
def test_ejsl::methodparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eJSL::MethodParameter_strategy)
def test_ejsl::methodparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL::Method_strategy)
@settings(max_examples=50)
def test_ejsl::method_instantiation(instance):
    assert isinstance(instance, eJSL::Method)

@given(instance=eJSL::Method_strategy)
def test_ejsl::method_returnvalue_type(instance):
    assert isinstance(instance.returnvalue, str)


@given(instance=eJSL::Method_strategy)
def test_ejsl::method_returnvalue_setter(instance):
    original = instance.returnvalue
    instance.returnvalue = original
    assert instance.returnvalue == original

@given(instance=eJSL::Method_strategy)
def test_ejsl::method_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eJSL::Method_strategy)
def test_ejsl::method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL::Package_strategy)
@settings(max_examples=50)
def test_ejsl::package_instantiation(instance):
    assert isinstance(instance, eJSL::Package)

@given(instance=eJSL::Package_strategy)
def test_ejsl::package_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eJSL::Package_strategy)
def test_ejsl::package_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL::Class_strategy)
@settings(max_examples=50)
def test_ejsl::class_instantiation(instance):
    assert isinstance(instance, eJSL::Class)

@given(instance=eJSL::Class_strategy)
def test_ejsl::class_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eJSL::Class_strategy)
def test_ejsl::class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL::Author_strategy)
@settings(max_examples=50)
def test_ejsl::author_instantiation(instance):
    assert isinstance(instance, eJSL::Author)

@given(instance=eJSL::Author_strategy)
def test_ejsl::author_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eJSL::Author_strategy)
def test_ejsl::author_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL::Author_strategy)
def test_ejsl::author_authoremail_type(instance):
    assert isinstance(instance.authoremail, str)


@given(instance=eJSL::Author_strategy)
def test_ejsl::author_authoremail_setter(instance):
    original = instance.authoremail
    instance.authoremail = original
    assert instance.authoremail == original

@given(instance=eJSL::Author_strategy)
def test_ejsl::author_authorurl_type(instance):
    assert isinstance(instance.authorurl, str)


@given(instance=eJSL::Author_strategy)
def test_ejsl::author_authorurl_setter(instance):
    original = instance.authorurl
    instance.authorurl = original
    assert instance.authorurl == original

@given(instance=eJSL::CssBlock_strategy)
@settings(max_examples=50)
def test_ejsl::cssblock_instantiation(instance):
    assert isinstance(instance, eJSL::CssBlock)

@given(instance=eJSL::CssBlock_strategy)
def test_ejsl::cssblock_selector_type(instance):
    assert isinstance(instance.selector, str)


@given(instance=eJSL::CssBlock_strategy)
def test_ejsl::cssblock_selector_setter(instance):
    original = instance.selector
    instance.selector = original
    assert instance.selector == original

@given(instance=eJSL::Position_strategy)
@settings(max_examples=50)
def test_ejsl::position_instantiation(instance):
    assert isinstance(instance, eJSL::Position)

@given(instance=eJSL::Position_strategy)
def test_ejsl::position_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eJSL::Position_strategy)
def test_ejsl::position_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL::ComponentReference_strategy)
@settings(max_examples=50)
def test_ejsl::componentreference_instantiation(instance):
    assert isinstance(instance, eJSL::ComponentReference)

@given(instance=eJSL::ComponentReference_strategy)
def test_ejsl::componentreference_core_type(instance):
    assert isinstance(instance.core, str)


@given(instance=eJSL::ComponentReference_strategy)
def test_ejsl::componentreference_core_setter(instance):
    original = instance.core
    instance.core = original
    assert instance.core == original

@given(instance=Section_strategy)
@settings(max_examples=50)
def test_section_instantiation(instance):
    assert isinstance(instance, Section)

@given(instance=eJSL::BackendSection_strategy)
@settings(max_examples=50)
def test_ejsl::backendsection_instantiation(instance):
    assert isinstance(instance, eJSL::BackendSection)

@given(instance=eJSL::PageReference_strategy)
@settings(max_examples=50)
def test_ejsl::pagereference_instantiation(instance):
    assert isinstance(instance, eJSL::PageReference)

@given(instance=eJSL::PageReference_strategy)
def test_ejsl::pagereference_sect_type(instance):
    assert isinstance(instance.sect, str)


@given(instance=eJSL::PageReference_strategy)
def test_ejsl::pagereference_sect_setter(instance):
    original = instance.sect
    instance.sect = original
    assert instance.sect == original

@given(instance=Extension_strategy)
@settings(max_examples=50)
def test_extension_instantiation(instance):
    assert isinstance(instance, Extension)

@given(instance=eJSL::Template_strategy)
@settings(max_examples=50)
def test_ejsl::template_instantiation(instance):
    assert isinstance(instance, eJSL::Template)

@given(instance=eJSL::Component_strategy)
@settings(max_examples=50)
def test_ejsl::component_instantiation(instance):
    assert isinstance(instance, eJSL::Component)

@given(instance=eJSL::ExtensionPackage_strategy)
@settings(max_examples=50)
def test_ejsl::extensionpackage_instantiation(instance):
    assert isinstance(instance, eJSL::ExtensionPackage)

@given(instance=eJSL::Language_strategy)
@settings(max_examples=50)
def test_ejsl::language_instantiation(instance):
    assert isinstance(instance, eJSL::Language)

@given(instance=eJSL::Language_strategy)
def test_ejsl::language_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eJSL::Language_strategy)
def test_ejsl::language_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL::Language_strategy)
def test_ejsl::language_sys_type(instance):
    assert isinstance(instance.sys, bool)


@given(instance=eJSL::Language_strategy)
def test_ejsl::language_sys_setter(instance):
    original = instance.sys
    instance.sys = original
    assert instance.sys == original

@given(instance=eJSL::Manifestation_strategy)
@settings(max_examples=50)
def test_ejsl::manifestation_instantiation(instance):
    assert isinstance(instance, eJSL::Manifestation)

@given(instance=eJSL::Manifestation_strategy)
def test_ejsl::manifestation_link_type(instance):
    assert isinstance(instance.link, str)


@given(instance=eJSL::Manifestation_strategy)
def test_ejsl::manifestation_link_setter(instance):
    original = instance.link
    instance.link = original
    assert instance.link == original

@given(instance=eJSL::Manifestation_strategy)
def test_ejsl::manifestation_copyright_type(instance):
    assert isinstance(instance.copyright, str)


@given(instance=eJSL::Manifestation_strategy)
def test_ejsl::manifestation_copyright_setter(instance):
    original = instance.copyright
    instance.copyright = original
    assert instance.copyright == original

@given(instance=eJSL::Manifestation_strategy)
def test_ejsl::manifestation_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=eJSL::Manifestation_strategy)
def test_ejsl::manifestation_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=eJSL::Manifestation_strategy)
def test_ejsl::manifestation_license_type(instance):
    assert isinstance(instance.license, str)


@given(instance=eJSL::Manifestation_strategy)
def test_ejsl::manifestation_license_setter(instance):
    original = instance.license
    instance.license = original
    assert instance.license == original

@given(instance=eJSL::Manifestation_strategy)
def test_ejsl::manifestation_creationdate_type(instance):
    assert isinstance(instance.creationdate, str)


@given(instance=eJSL::Manifestation_strategy)
def test_ejsl::manifestation_creationdate_setter(instance):
    original = instance.creationdate
    instance.creationdate = original
    assert instance.creationdate == original

@given(instance=eJSL::Manifestation_strategy)
def test_ejsl::manifestation_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=eJSL::Manifestation_strategy)
def test_ejsl::manifestation_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=eJSL::LinkParameter_strategy)
@settings(max_examples=50)
def test_ejsl::linkparameter_instantiation(instance):
    assert isinstance(instance, eJSL::LinkParameter)

@given(instance=eJSL::LinkParameter_strategy)
def test_ejsl::linkparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eJSL::LinkParameter_strategy)
def test_ejsl::linkparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL::LinkParameter_strategy)
def test_ejsl::linkparameter_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=eJSL::LinkParameter_strategy)
def test_ejsl::linkparameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eJSL::LinkParameter_strategy)
def test_ejsl::linkparameter_id_type(instance):
    assert isinstance(instance.id, bool)


@given(instance=eJSL::LinkParameter_strategy)
def test_ejsl::linkparameter_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=InternalLink_strategy)
@settings(max_examples=50)
def test_internallink_instantiation(instance):
    assert isinstance(instance, InternalLink)

@given(instance=eJSL::ContextLink_strategy)
@settings(max_examples=50)
def test_ejsl::contextlink_instantiation(instance):
    assert isinstance(instance, eJSL::ContextLink)

@given(instance=eJSL::Library_strategy)
@settings(max_examples=50)
def test_ejsl::library_instantiation(instance):
    assert isinstance(instance, eJSL::Library)

@given(instance=eJSL::Plugin_strategy)
@settings(max_examples=50)
def test_ejsl::plugin_instantiation(instance):
    assert isinstance(instance, eJSL::Plugin)

@given(instance=eJSL::Plugin_strategy)
def test_ejsl::plugin_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=eJSL::Plugin_strategy)
def test_ejsl::plugin_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=eJSL::Module_strategy)
@settings(max_examples=50)
def test_ejsl::module_instantiation(instance):
    assert isinstance(instance, eJSL::Module)

@given(instance=eJSL::FrontendSection_strategy)
@settings(max_examples=50)
def test_ejsl::frontendsection_instantiation(instance):
    assert isinstance(instance, eJSL::FrontendSection)

@given(instance=eJSL::DetailPageField_strategy)
@settings(max_examples=50)
def test_ejsl::detailpagefield_instantiation(instance):
    assert isinstance(instance, eJSL::DetailPageField)

@given(instance=DynamicPage_strategy)
@settings(max_examples=50)
def test_dynamicpage_instantiation(instance):
    assert isinstance(instance, DynamicPage)

@given(instance=eJSL::DetailsPage_strategy)
@settings(max_examples=50)
def test_ejsl::detailspage_instantiation(instance):
    assert isinstance(instance, eJSL::DetailsPage)

@given(instance=eJSL::IndexPage_strategy)
@settings(max_examples=50)
def test_ejsl::indexpage_instantiation(instance):
    assert isinstance(instance, eJSL::IndexPage)

@given(instance=Link_strategy)
@settings(max_examples=50)
def test_link_instantiation(instance):
    assert isinstance(instance, Link)

@given(instance=eJSL::InternalLink_strategy)
@settings(max_examples=50)
def test_ejsl::internallink_instantiation(instance):
    assert isinstance(instance, eJSL::InternalLink)

@given(instance=eJSL::InternalLink_strategy)
def test_ejsl::internallink_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eJSL::InternalLink_strategy)
def test_ejsl::internallink_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL::ExternalLink_strategy)
@settings(max_examples=50)
def test_ejsl::externallink_instantiation(instance):
    assert isinstance(instance, eJSL::ExternalLink)

@given(instance=eJSL::ExternalLink_strategy)
def test_ejsl::externallink_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=eJSL::ExternalLink_strategy)
def test_ejsl::externallink_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=eJSL::ExternalLink_strategy)
def test_ejsl::externallink_target_type(instance):
    assert isinstance(instance.target, str)


@given(instance=eJSL::ExternalLink_strategy)
def test_ejsl::externallink_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original

@given(instance=eJSL::Reference_strategy)
@settings(max_examples=50)
def test_ejsl::reference_instantiation(instance):
    assert isinstance(instance, eJSL::Reference)

@given(instance=eJSL::Reference_strategy)
def test_ejsl::reference_upper_type(instance):
    assert isinstance(instance.upper, str)


@given(instance=eJSL::Reference_strategy)
def test_ejsl::reference_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=eJSL::Reference_strategy)
def test_ejsl::reference_id_type(instance):
    assert isinstance(instance.id, bool)


@given(instance=eJSL::Reference_strategy)
def test_ejsl::reference_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=eJSL::Reference_strategy)
def test_ejsl::reference_lower_type(instance):
    assert isinstance(instance.lower, str)


@given(instance=eJSL::Reference_strategy)
def test_ejsl::reference_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=eJSL::Reference_strategy)
def test_ejsl::reference_preserve_type(instance):
    assert isinstance(instance.preserve, bool)


@given(instance=eJSL::Reference_strategy)
def test_ejsl::reference_preserve_setter(instance):
    original = instance.preserve
    instance.preserve = original
    assert instance.preserve == original

@given(instance=eJSL::Attribute_strategy)
@settings(max_examples=50)
def test_ejsl::attribute_instantiation(instance):
    assert isinstance(instance, eJSL::Attribute)

@given(instance=eJSL::Attribute_strategy)
def test_ejsl::attribute_isprimary_type(instance):
    assert isinstance(instance.isprimary, bool)


@given(instance=eJSL::Attribute_strategy)
def test_ejsl::attribute_isprimary_setter(instance):
    original = instance.isprimary
    instance.isprimary = original
    assert instance.isprimary == original

@given(instance=eJSL::Attribute_strategy)
def test_ejsl::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eJSL::Attribute_strategy)
def test_ejsl::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL::Attribute_strategy)
def test_ejsl::attribute_isunique_type(instance):
    assert isinstance(instance.isunique, bool)


@given(instance=eJSL::Attribute_strategy)
def test_ejsl::attribute_isunique_setter(instance):
    original = instance.isunique
    instance.isunique = original
    assert instance.isunique == original

@given(instance=eJSL::Attribute_strategy)
def test_ejsl::attribute_id_type(instance):
    assert isinstance(instance.id, bool)


@given(instance=eJSL::Attribute_strategy)
def test_ejsl::attribute_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=eJSL::Attribute_strategy)
def test_ejsl::attribute_preserve_type(instance):
    assert isinstance(instance.preserve, bool)


@given(instance=eJSL::Attribute_strategy)
def test_ejsl::attribute_preserve_setter(instance):
    original = instance.preserve
    instance.preserve = original
    assert instance.preserve == original

@given(instance=Page_strategy)
@settings(max_examples=50)
def test_page_instantiation(instance):
    assert isinstance(instance, Page)

@given(instance=eJSL::DynamicPage_strategy)
@settings(max_examples=50)
def test_ejsl::dynamicpage_instantiation(instance):
    assert isinstance(instance, eJSL::DynamicPage)

@given(instance=eJSL::DynamicPage_strategy)
def test_ejsl::dynamicpage_preserve_type(instance):
    assert isinstance(instance.preserve, bool)


@given(instance=eJSL::DynamicPage_strategy)
def test_ejsl::dynamicpage_preserve_setter(instance):
    original = instance.preserve
    instance.preserve = original
    assert instance.preserve == original

@given(instance=eJSL::CustomPage_strategy)
@settings(max_examples=50)
def test_ejsl::custompage_instantiation(instance):
    assert isinstance(instance, eJSL::CustomPage)

@given(instance=eJSL::CustomPage_strategy)
def test_ejsl::custompage_preserve_type(instance):
    assert isinstance(instance.preserve, str)


@given(instance=eJSL::CustomPage_strategy)
def test_ejsl::custompage_preserve_setter(instance):
    original = instance.preserve
    instance.preserve = original
    assert instance.preserve == original

@given(instance=eJSL::CustomPage_strategy)
def test_ejsl::custompage_pageType_type(instance):
    assert isinstance(instance.pageType, str)


@given(instance=eJSL::CustomPage_strategy)
def test_ejsl::custompage_pageType_setter(instance):
    original = instance.pageType
    instance.pageType = original
    assert instance.pageType == original

@given(instance=eJSL::StaticPage_strategy)
@settings(max_examples=50)
def test_ejsl::staticpage_instantiation(instance):
    assert isinstance(instance, eJSL::StaticPage)

@given(instance=eJSL::StaticPage_strategy)
def test_ejsl::staticpage_preserve_type(instance):
    assert isinstance(instance.preserve, bool)


@given(instance=eJSL::StaticPage_strategy)
def test_ejsl::staticpage_preserve_setter(instance):
    original = instance.preserve
    instance.preserve = original
    assert instance.preserve == original

@given(instance=eJSL::StaticPage_strategy)
def test_ejsl::staticpage_HTMLBody_type(instance):
    assert isinstance(instance.HTMLBody, str)


@given(instance=eJSL::StaticPage_strategy)
def test_ejsl::staticpage_HTMLBody_setter(instance):
    original = instance.HTMLBody
    instance.HTMLBody = original
    assert instance.HTMLBody == original

@given(instance=eJSL::Link_strategy)
@settings(max_examples=50)
def test_ejsl::link_instantiation(instance):
    assert isinstance(instance, eJSL::Link)

@given(instance=eJSL::HTMLTypes_strategy)
@settings(max_examples=50)
def test_ejsl::htmltypes_instantiation(instance):
    assert isinstance(instance, eJSL::HTMLTypes)

@given(instance=HTMLTypes_strategy)
@settings(max_examples=50)
def test_htmltypes_instantiation(instance):
    assert isinstance(instance, HTMLTypes)

@given(instance=eJSL::SimpleHTMLTypes_strategy)
@settings(max_examples=50)
def test_ejsl::simplehtmltypes_instantiation(instance):
    assert isinstance(instance, eJSL::SimpleHTMLTypes)

@given(instance=eJSL::SimpleHTMLTypes_strategy)
def test_ejsl::simplehtmltypes_htmltype_type(instance):
    assert isinstance(instance.htmltype, str)


@given(instance=eJSL::SimpleHTMLTypes_strategy)
def test_ejsl::simplehtmltypes_htmltype_setter(instance):
    original = instance.htmltype
    instance.htmltype = original
    assert instance.htmltype == original

@given(instance=eJSL::ComplexHTMLTypes_strategy)
@settings(max_examples=50)
def test_ejsl::complexhtmltypes_instantiation(instance):
    assert isinstance(instance, eJSL::ComplexHTMLTypes)

@given(instance=eJSL::ComplexHTMLTypes_strategy)
def test_ejsl::complexhtmltypes_htmltype_type(instance):
    assert isinstance(instance.htmltype, str)


@given(instance=eJSL::ComplexHTMLTypes_strategy)
def test_ejsl::complexhtmltypes_htmltype_setter(instance):
    original = instance.htmltype
    instance.htmltype = original
    assert instance.htmltype == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=eJSL::StandardTypes_strategy)
@settings(max_examples=50)
def test_ejsl::standardtypes_instantiation(instance):
    assert isinstance(instance, eJSL::StandardTypes)

@given(instance=eJSL::StandardTypes_strategy)
def test_ejsl::standardtypes_autoincrement_type(instance):
    assert isinstance(instance.autoincrement, bool)


@given(instance=eJSL::StandardTypes_strategy)
def test_ejsl::standardtypes_autoincrement_setter(instance):
    original = instance.autoincrement
    instance.autoincrement = original
    assert instance.autoincrement == original

@given(instance=eJSL::StandardTypes_strategy)
def test_ejsl::standardtypes_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=eJSL::StandardTypes_strategy)
def test_ejsl::standardtypes_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=eJSL::StandardTypes_strategy)
def test_ejsl::standardtypes_notnull_type(instance):
    assert isinstance(instance.notnull, bool)


@given(instance=eJSL::StandardTypes_strategy)
def test_ejsl::standardtypes_notnull_setter(instance):
    original = instance.notnull
    instance.notnull = original
    assert instance.notnull == original

@given(instance=eJSL::StandardTypes_strategy)
def test_ejsl::standardtypes_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=eJSL::StandardTypes_strategy)
def test_ejsl::standardtypes_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=eJSL::DatatypeReference_strategy)
@settings(max_examples=50)
def test_ejsl::datatypereference_instantiation(instance):
    assert isinstance(instance, eJSL::DatatypeReference)

@given(instance=eJSL::Type_strategy)
@settings(max_examples=50)
def test_ejsl::type_instantiation(instance):
    assert isinstance(instance, eJSL::Type)

@given(instance=eJSL::Section_strategy)
@settings(max_examples=50)
def test_ejsl::section_instantiation(instance):
    assert isinstance(instance, eJSL::Section)

@given(instance=eJSL::Page_strategy)
@settings(max_examples=50)
def test_ejsl::page_instantiation(instance):
    assert isinstance(instance, eJSL::Page)

@given(instance=eJSL::Page_strategy)
def test_ejsl::page_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eJSL::Page_strategy)
def test_ejsl::page_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL::Entity_strategy)
@settings(max_examples=50)
def test_ejsl::entity_instantiation(instance):
    assert isinstance(instance, eJSL::Entity)

@given(instance=eJSL::Entity_strategy)
def test_ejsl::entity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eJSL::Entity_strategy)
def test_ejsl::entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL::Entity_strategy)
def test_ejsl::entity_preserve_type(instance):
    assert isinstance(instance.preserve, bool)


@given(instance=eJSL::Entity_strategy)
def test_ejsl::entity_preserve_setter(instance):
    original = instance.preserve
    instance.preserve = original
    assert instance.preserve == original

@given(instance=eJSL::Entitypackage_strategy)
@settings(max_examples=50)
def test_ejsl::entitypackage_instantiation(instance):
    assert isinstance(instance, eJSL::Entitypackage)

@given(instance=eJSL::Entitypackage_strategy)
def test_ejsl::entitypackage_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eJSL::Entitypackage_strategy)
def test_ejsl::entitypackage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL::Extension_strategy)
@settings(max_examples=50)
def test_ejsl::extension_instantiation(instance):
    assert isinstance(instance, eJSL::Extension)

@given(instance=eJSL::Extension_strategy)
def test_ejsl::extension_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eJSL::Extension_strategy)
def test_ejsl::extension_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL::PageAction_strategy)
@settings(max_examples=50)
def test_ejsl::pageaction_instantiation(instance):
    assert isinstance(instance, eJSL::PageAction)

@given(instance=eJSL::PageAction_strategy)
def test_ejsl::pageaction_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eJSL::PageAction_strategy)
def test_ejsl::pageaction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL::PageAction_strategy)
def test_ejsl::pageaction_pageActionPosition_type(instance):
    assert isinstance(instance.pageActionPosition, str)


@given(instance=eJSL::PageAction_strategy)
def test_ejsl::pageaction_pageActionPosition_setter(instance):
    original = instance.pageActionPosition
    instance.pageActionPosition = original
    assert instance.pageActionPosition == original

@given(instance=eJSL::PageAction_strategy)
def test_ejsl::pageaction_pageActionType_type(instance):
    assert isinstance(instance.pageActionType, str)


@given(instance=eJSL::PageAction_strategy)
def test_ejsl::pageaction_pageActionType_setter(instance):
    original = instance.pageActionType
    instance.pageActionType = original
    assert instance.pageActionType == original

@given(instance=eJSL::KeyValuePair_strategy)
@settings(max_examples=50)
def test_ejsl::keyvaluepair_instantiation(instance):
    assert isinstance(instance, eJSL::KeyValuePair)

@given(instance=eJSL::KeyValuePair_strategy)
def test_ejsl::keyvaluepair_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=eJSL::KeyValuePair_strategy)
def test_ejsl::keyvaluepair_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=eJSL::KeyValuePair_strategy)
def test_ejsl::keyvaluepair_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eJSL::KeyValuePair_strategy)
def test_ejsl::keyvaluepair_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL::EJSLModel_strategy)
@settings(max_examples=50)
def test_ejsl::ejslmodel_instantiation(instance):
    assert isinstance(instance, eJSL::EJSLModel)

@given(instance=eJSL::EJSLModel_strategy)
def test_ejsl::ejslmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eJSL::EJSLModel_strategy)
def test_ejsl::ejslmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL::coreFeature_strategy)
@settings(max_examples=50)
def test_ejsl::corefeature_instantiation(instance):
    assert isinstance(instance, eJSL::coreFeature)

@given(instance=EJSLPart_strategy)
@settings(max_examples=50)
def test_ejslpart_instantiation(instance):
    assert isinstance(instance, EJSLPart)

@given(instance=eJSL::CMSExtension_strategy)
@settings(max_examples=50)
def test_ejsl::cmsextension_instantiation(instance):
    assert isinstance(instance, eJSL::CMSExtension)

@given(instance=eJSL::CMSCore_strategy)
@settings(max_examples=50)
def test_ejsl::cmscore_instantiation(instance):
    assert isinstance(instance, eJSL::CMSCore)

@given(instance=eJSL::Feature_strategy)
@settings(max_examples=50)
def test_ejsl::feature_instantiation(instance):
    assert isinstance(instance, eJSL::Feature)

@given(instance=eJSL::ParameterGroup_strategy)
@settings(max_examples=50)
def test_ejsl::parametergroup_instantiation(instance):
    assert isinstance(instance, eJSL::ParameterGroup)

@given(instance=eJSL::ParameterGroup_strategy)
def test_ejsl::parametergroup_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=eJSL::ParameterGroup_strategy)
def test_ejsl::parametergroup_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=eJSL::ParameterGroup_strategy)
def test_ejsl::parametergroup_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eJSL::ParameterGroup_strategy)
def test_ejsl::parametergroup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL::Parameter_strategy)
@settings(max_examples=50)
def test_ejsl::parameter_instantiation(instance):
    assert isinstance(instance, eJSL::Parameter)

@given(instance=eJSL::Parameter_strategy)
def test_ejsl::parameter_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=eJSL::Parameter_strategy)
def test_ejsl::parameter_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=eJSL::Parameter_strategy)
def test_ejsl::parameter_descripton_type(instance):
    assert isinstance(instance.descripton, str)


@given(instance=eJSL::Parameter_strategy)
def test_ejsl::parameter_descripton_setter(instance):
    original = instance.descripton
    instance.descripton = original
    assert instance.descripton == original

@given(instance=eJSL::Parameter_strategy)
def test_ejsl::parameter_defaultvalue_type(instance):
    assert isinstance(instance.defaultvalue, str)


@given(instance=eJSL::Parameter_strategy)
def test_ejsl::parameter_defaultvalue_setter(instance):
    original = instance.defaultvalue
    instance.defaultvalue = original
    assert instance.defaultvalue == original

@given(instance=eJSL::Parameter_strategy)
def test_ejsl::parameter_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=eJSL::Parameter_strategy)
def test_ejsl::parameter_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=eJSL::Parameter_strategy)
def test_ejsl::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eJSL::Parameter_strategy)
def test_ejsl::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL::Datatype_strategy)
@settings(max_examples=50)
def test_ejsl::datatype_instantiation(instance):
    assert isinstance(instance, eJSL::Datatype)

@given(instance=eJSL::Datatype_strategy)
def test_ejsl::datatype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=eJSL::Datatype_strategy)
def test_ejsl::datatype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=eJSL::Datatype_strategy)
def test_ejsl::datatype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=eJSL::Datatype_strategy)
def test_ejsl::datatype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=eJSL::EJSLPart_strategy)
@settings(max_examples=50)
def test_ejsl::ejslpart_instantiation(instance):
    assert isinstance(instance, eJSL::EJSLPart)
