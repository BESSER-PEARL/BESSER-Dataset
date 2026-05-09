import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Extent,
    emof::URIExtent,
    Package,
    Parameter,
    MultiplicityElement,
    TypedElement,
    emof::Parameter,
    emof::Property,
    emof::Operation,
    emof::Object,
    EnumerationLiteral,
    DataType,
    emof::PrimitiveType,
    emof::Enumeration,
    Tag,
    Comment,
    Object,
    emof::Element,
    NamedElement,
    emof::Package,
    emof::TypedElement,
    emof::Type,
    emof::EnumerationLiteral,
    Element,
    emof::Tag,
    emof::NamedElement,
    emof::Comment,
    Class,
    Operation,
    Property,
    Type,
    emof::DataType,
    emof::Class,
    emof::MultiplicityElement,
    emof::Extent,
    Enumeration,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_extent_is_not_abstract():
    assert not inspect.isabstract(Extent)


def test_extent_constructor_exists():
    assert callable(Extent.__init__)


def test_extent_constructor_args():
    sig = inspect.signature(Extent.__init__)
    params = list(sig.parameters.keys())



def test_emof::uriextent_is_not_abstract():
    assert not inspect.isabstract(emof::URIExtent)


def test_emof::uriextent_constructor_exists():
    assert callable(emof::URIExtent.__init__)


def test_emof::uriextent_constructor_args():
    sig = inspect.signature(emof::URIExtent.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(MultiplicityElement)


def test_multiplicityelement_constructor_exists():
    assert callable(MultiplicityElement.__init__)


def test_multiplicityelement_constructor_args():
    sig = inspect.signature(MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_emof::parameter_is_not_abstract():
    assert not inspect.isabstract(emof::Parameter)


def test_emof::parameter_constructor_exists():
    assert callable(emof::Parameter.__init__)


def test_emof::parameter_constructor_args():
    sig = inspect.signature(emof::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_emof::property_is_not_abstract():
    assert not inspect.isabstract(emof::Property)


def test_emof::property_constructor_exists():
    assert callable(emof::Property.__init__)


def test_emof::property_constructor_args():
    sig = inspect.signature(emof::Property.__init__)
    params = list(sig.parameters.keys())
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "default" in params, "Missing parameter 'default'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isId" in params, "Missing parameter 'isId'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"

def test_emof::property_has_isDerived():
    assert hasattr(emof::Property, "isDerived")
    descriptor = None
    for klass in emof::Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)

def test_emof::property_has_default():
    assert hasattr(emof::Property, "default")
    descriptor = None
    for klass in emof::Property.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_emof::property_has_isComposite():
    assert hasattr(emof::Property, "isComposite")
    descriptor = None
    for klass in emof::Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_emof::property_has_isId():
    assert hasattr(emof::Property, "isId")
    descriptor = None
    for klass in emof::Property.__mro__:
        if "isId" in klass.__dict__:
            descriptor = klass.__dict__["isId"]
            break
    assert isinstance(descriptor, property)

def test_emof::property_has_isReadOnly():
    assert hasattr(emof::Property, "isReadOnly")
    descriptor = None
    for klass in emof::Property.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)



def test_emof::operation_is_not_abstract():
    assert not inspect.isabstract(emof::Operation)


def test_emof::operation_constructor_exists():
    assert callable(emof::Operation.__init__)


def test_emof::operation_constructor_args():
    sig = inspect.signature(emof::Operation.__init__)
    params = list(sig.parameters.keys())



def test_emof::object_is_not_abstract():
    assert not inspect.isabstract(emof::Object)


def test_emof::object_constructor_exists():
    assert callable(emof::Object.__init__)


def test_emof::object_constructor_args():
    sig = inspect.signature(emof::Object.__init__)
    params = list(sig.parameters.keys())



def test_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(EnumerationLiteral)


def test_enumerationliteral_constructor_exists():
    assert callable(EnumerationLiteral.__init__)


def test_enumerationliteral_constructor_args():
    sig = inspect.signature(EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_emof::primitivetype_is_not_abstract():
    assert not inspect.isabstract(emof::PrimitiveType)


def test_emof::primitivetype_constructor_exists():
    assert callable(emof::PrimitiveType.__init__)


def test_emof::primitivetype_constructor_args():
    sig = inspect.signature(emof::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_emof::enumeration_is_not_abstract():
    assert not inspect.isabstract(emof::Enumeration)


def test_emof::enumeration_constructor_exists():
    assert callable(emof::Enumeration.__init__)


def test_emof::enumeration_constructor_args():
    sig = inspect.signature(emof::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_tag_is_not_abstract():
    assert not inspect.isabstract(Tag)


def test_tag_constructor_exists():
    assert callable(Tag.__init__)


def test_tag_constructor_args():
    sig = inspect.signature(Tag.__init__)
    params = list(sig.parameters.keys())



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_object_is_not_abstract():
    assert not inspect.isabstract(Object)


def test_object_constructor_exists():
    assert callable(Object.__init__)


def test_object_constructor_args():
    sig = inspect.signature(Object.__init__)
    params = list(sig.parameters.keys())



def test_emof::element_is_not_abstract():
    assert not inspect.isabstract(emof::Element)


def test_emof::element_constructor_exists():
    assert callable(emof::Element.__init__)


def test_emof::element_constructor_args():
    sig = inspect.signature(emof::Element.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_emof::package_is_not_abstract():
    assert not inspect.isabstract(emof::Package)


def test_emof::package_constructor_exists():
    assert callable(emof::Package.__init__)


def test_emof::package_constructor_args():
    sig = inspect.signature(emof::Package.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_emof::package_has_uri():
    assert hasattr(emof::Package, "uri")
    descriptor = None
    for klass in emof::Package.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_emof::typedelement_is_not_abstract():
    assert not inspect.isabstract(emof::TypedElement)


def test_emof::typedelement_constructor_exists():
    assert callable(emof::TypedElement.__init__)


def test_emof::typedelement_constructor_args():
    sig = inspect.signature(emof::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_emof::type_is_not_abstract():
    assert not inspect.isabstract(emof::Type)


def test_emof::type_constructor_exists():
    assert callable(emof::Type.__init__)


def test_emof::type_constructor_args():
    sig = inspect.signature(emof::Type.__init__)
    params = list(sig.parameters.keys())



def test_emof::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(emof::EnumerationLiteral)


def test_emof::enumerationliteral_constructor_exists():
    assert callable(emof::EnumerationLiteral.__init__)


def test_emof::enumerationliteral_constructor_args():
    sig = inspect.signature(emof::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_emof::tag_is_not_abstract():
    assert not inspect.isabstract(emof::Tag)


def test_emof::tag_constructor_exists():
    assert callable(emof::Tag.__init__)


def test_emof::tag_constructor_args():
    sig = inspect.signature(emof::Tag.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_emof::tag_has_value():
    assert hasattr(emof::Tag, "value")
    descriptor = None
    for klass in emof::Tag.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_emof::tag_has_name():
    assert hasattr(emof::Tag, "name")
    descriptor = None
    for klass in emof::Tag.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emof::namedelement_is_not_abstract():
    assert not inspect.isabstract(emof::NamedElement)


def test_emof::namedelement_constructor_exists():
    assert callable(emof::NamedElement.__init__)


def test_emof::namedelement_constructor_args():
    sig = inspect.signature(emof::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emof::namedelement_has_name():
    assert hasattr(emof::NamedElement, "name")
    descriptor = None
    for klass in emof::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_emof::comment_is_not_abstract():
    assert not inspect.isabstract(emof::Comment)


def test_emof::comment_constructor_exists():
    assert callable(emof::Comment.__init__)


def test_emof::comment_constructor_args():
    sig = inspect.signature(emof::Comment.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_emof::datatype_is_not_abstract():
    assert not inspect.isabstract(emof::DataType)


def test_emof::datatype_constructor_exists():
    assert callable(emof::DataType.__init__)


def test_emof::datatype_constructor_args():
    sig = inspect.signature(emof::DataType.__init__)
    params = list(sig.parameters.keys())



def test_emof::class_is_not_abstract():
    assert not inspect.isabstract(emof::Class)


def test_emof::class_constructor_exists():
    assert callable(emof::Class.__init__)


def test_emof::class_constructor_args():
    sig = inspect.signature(emof::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_emof::class_has_isAbstract():
    assert hasattr(emof::Class, "isAbstract")
    descriptor = None
    for klass in emof::Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_emof::multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(emof::MultiplicityElement)


def test_emof::multiplicityelement_constructor_exists():
    assert callable(emof::MultiplicityElement.__init__)


def test_emof::multiplicityelement_constructor_args():
    sig = inspect.signature(emof::MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "lower" in params, "Missing parameter 'lower'"

def test_emof::multiplicityelement_has_isOrdered():
    assert hasattr(emof::MultiplicityElement, "isOrdered")
    descriptor = None
    for klass in emof::MultiplicityElement.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_emof::multiplicityelement_has_isUnique():
    assert hasattr(emof::MultiplicityElement, "isUnique")
    descriptor = None
    for klass in emof::MultiplicityElement.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_emof::multiplicityelement_has_upper():
    assert hasattr(emof::MultiplicityElement, "upper")
    descriptor = None
    for klass in emof::MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_emof::multiplicityelement_has_lower():
    assert hasattr(emof::MultiplicityElement, "lower")
    descriptor = None
    for klass in emof::MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)



def test_emof::extent_is_not_abstract():
    assert not inspect.isabstract(emof::Extent)


def test_emof::extent_constructor_exists():
    assert callable(emof::Extent.__init__)


def test_emof::extent_constructor_args():
    sig = inspect.signature(emof::Extent.__init__)
    params = list(sig.parameters.keys())



def test_enumeration_is_not_abstract():
    assert not inspect.isabstract(Enumeration)


def test_enumeration_constructor_exists():
    assert callable(Enumeration.__init__)


def test_enumeration_constructor_args():
    sig = inspect.signature(Enumeration.__init__)
    params = list(sig.parameters.keys())


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
Extent_strategy = st.builds(
    Extent,
)
emof::URIExtent_strategy = st.builds(
    emof::URIExtent,
)
Package_strategy = st.builds(
    Package,
)
Parameter_strategy = st.builds(
    Parameter,
)
MultiplicityElement_strategy = st.builds(
    MultiplicityElement,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
emof::Parameter_strategy = st.builds(
    emof::Parameter,
)
emof::Property_strategy = st.builds(
    emof::Property,
    isDerived=
        safe_text,
    default=
        safe_text,
    isComposite=
        safe_text,
    isId=
        safe_text,
    isReadOnly=
        safe_text
)
emof::Operation_strategy = st.builds(
    emof::Operation,
)
emof::Object_strategy = st.builds(
    emof::Object,
)
EnumerationLiteral_strategy = st.builds(
    EnumerationLiteral,
)
DataType_strategy = st.builds(
    DataType,
)
emof::PrimitiveType_strategy = st.builds(
    emof::PrimitiveType,
)
emof::Enumeration_strategy = st.builds(
    emof::Enumeration,
)
Tag_strategy = st.builds(
    Tag,
)
Comment_strategy = st.builds(
    Comment,
)
Object_strategy = st.builds(
    Object,
)
emof::Element_strategy = st.builds(
    emof::Element,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
emof::Package_strategy = st.builds(
    emof::Package,
    uri=
        safe_text
)
emof::TypedElement_strategy = st.builds(
    emof::TypedElement,
)
emof::Type_strategy = st.builds(
    emof::Type,
)
emof::EnumerationLiteral_strategy = st.builds(
    emof::EnumerationLiteral,
)
Element_strategy = st.builds(
    Element,
)
emof::Tag_strategy = st.builds(
    emof::Tag,
    value=
        safe_text,
    name=
        safe_text
)
emof::NamedElement_strategy = st.builds(
    emof::NamedElement,
    name=
        safe_text
)
emof::Comment_strategy = st.builds(
    emof::Comment,
)
Class_strategy = st.builds(
    Class,
)
Operation_strategy = st.builds(
    Operation,
)
Property_strategy = st.builds(
    Property,
)
Type_strategy = st.builds(
    Type,
)
emof::DataType_strategy = st.builds(
    emof::DataType,
)
emof::Class_strategy = st.builds(
    emof::Class,
    isAbstract=
        safe_text
)
emof::MultiplicityElement_strategy = st.builds(
    emof::MultiplicityElement,
    isOrdered=
        safe_text,
    isUnique=
        safe_text,
    upper=
        safe_text,
    lower=
        safe_text
)
emof::Extent_strategy = st.builds(
    emof::Extent,
)
Enumeration_strategy = st.builds(
    Enumeration,
)

@given(instance=Extent_strategy)
@settings(max_examples=50)
def test_extent_instantiation(instance):
    assert isinstance(instance, Extent)

@given(instance=emof::URIExtent_strategy)
@settings(max_examples=50)
def test_emof::uriextent_instantiation(instance):
    assert isinstance(instance, emof::URIExtent)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=MultiplicityElement_strategy)
@settings(max_examples=50)
def test_multiplicityelement_instantiation(instance):
    assert isinstance(instance, MultiplicityElement)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=emof::Parameter_strategy)
@settings(max_examples=50)
def test_emof::parameter_instantiation(instance):
    assert isinstance(instance, emof::Parameter)

@given(instance=emof::Property_strategy)
@settings(max_examples=50)
def test_emof::property_instantiation(instance):
    assert isinstance(instance, emof::Property)

@given(instance=emof::Property_strategy)
def test_emof::property_isDerived_type(instance):
    assert isinstance(instance.isDerived, str)


@given(instance=emof::Property_strategy)
def test_emof::property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=emof::Property_strategy)
def test_emof::property_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=emof::Property_strategy)
def test_emof::property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=emof::Property_strategy)
def test_emof::property_isComposite_type(instance):
    assert isinstance(instance.isComposite, str)


@given(instance=emof::Property_strategy)
def test_emof::property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=emof::Property_strategy)
def test_emof::property_isId_type(instance):
    assert isinstance(instance.isId, str)


@given(instance=emof::Property_strategy)
def test_emof::property_isId_setter(instance):
    original = instance.isId
    instance.isId = original
    assert instance.isId == original

@given(instance=emof::Property_strategy)
def test_emof::property_isReadOnly_type(instance):
    assert isinstance(instance.isReadOnly, str)


@given(instance=emof::Property_strategy)
def test_emof::property_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=emof::Operation_strategy)
@settings(max_examples=50)
def test_emof::operation_instantiation(instance):
    assert isinstance(instance, emof::Operation)

@given(instance=emof::Object_strategy)
@settings(max_examples=50)
def test_emof::object_instantiation(instance):
    assert isinstance(instance, emof::Object)

@given(instance=EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_enumerationliteral_instantiation(instance):
    assert isinstance(instance, EnumerationLiteral)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=emof::PrimitiveType_strategy)
@settings(max_examples=50)
def test_emof::primitivetype_instantiation(instance):
    assert isinstance(instance, emof::PrimitiveType)

@given(instance=emof::Enumeration_strategy)
@settings(max_examples=50)
def test_emof::enumeration_instantiation(instance):
    assert isinstance(instance, emof::Enumeration)

@given(instance=Tag_strategy)
@settings(max_examples=50)
def test_tag_instantiation(instance):
    assert isinstance(instance, Tag)

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=Object_strategy)
@settings(max_examples=50)
def test_object_instantiation(instance):
    assert isinstance(instance, Object)

@given(instance=emof::Element_strategy)
@settings(max_examples=50)
def test_emof::element_instantiation(instance):
    assert isinstance(instance, emof::Element)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=emof::Package_strategy)
@settings(max_examples=50)
def test_emof::package_instantiation(instance):
    assert isinstance(instance, emof::Package)

@given(instance=emof::Package_strategy)
def test_emof::package_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=emof::Package_strategy)
def test_emof::package_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=emof::TypedElement_strategy)
@settings(max_examples=50)
def test_emof::typedelement_instantiation(instance):
    assert isinstance(instance, emof::TypedElement)

@given(instance=emof::Type_strategy)
@settings(max_examples=50)
def test_emof::type_instantiation(instance):
    assert isinstance(instance, emof::Type)

@given(instance=emof::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_emof::enumerationliteral_instantiation(instance):
    assert isinstance(instance, emof::EnumerationLiteral)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=emof::Tag_strategy)
@settings(max_examples=50)
def test_emof::tag_instantiation(instance):
    assert isinstance(instance, emof::Tag)

@given(instance=emof::Tag_strategy)
def test_emof::tag_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=emof::Tag_strategy)
def test_emof::tag_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=emof::Tag_strategy)
def test_emof::tag_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=emof::Tag_strategy)
def test_emof::tag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=emof::NamedElement_strategy)
@settings(max_examples=50)
def test_emof::namedelement_instantiation(instance):
    assert isinstance(instance, emof::NamedElement)

@given(instance=emof::NamedElement_strategy)
def test_emof::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=emof::NamedElement_strategy)
def test_emof::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=emof::Comment_strategy)
@settings(max_examples=50)
def test_emof::comment_instantiation(instance):
    assert isinstance(instance, emof::Comment)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=emof::DataType_strategy)
@settings(max_examples=50)
def test_emof::datatype_instantiation(instance):
    assert isinstance(instance, emof::DataType)

@given(instance=emof::Class_strategy)
@settings(max_examples=50)
def test_emof::class_instantiation(instance):
    assert isinstance(instance, emof::Class)

@given(instance=emof::Class_strategy)
def test_emof::class_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=emof::Class_strategy)
def test_emof::class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=emof::MultiplicityElement_strategy)
@settings(max_examples=50)
def test_emof::multiplicityelement_instantiation(instance):
    assert isinstance(instance, emof::MultiplicityElement)

@given(instance=emof::MultiplicityElement_strategy)
def test_emof::multiplicityelement_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, str)


@given(instance=emof::MultiplicityElement_strategy)
def test_emof::multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=emof::MultiplicityElement_strategy)
def test_emof::multiplicityelement_isUnique_type(instance):
    assert isinstance(instance.isUnique, str)


@given(instance=emof::MultiplicityElement_strategy)
def test_emof::multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=emof::MultiplicityElement_strategy)
def test_emof::multiplicityelement_upper_type(instance):
    assert isinstance(instance.upper, str)


@given(instance=emof::MultiplicityElement_strategy)
def test_emof::multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=emof::MultiplicityElement_strategy)
def test_emof::multiplicityelement_lower_type(instance):
    assert isinstance(instance.lower, str)


@given(instance=emof::MultiplicityElement_strategy)
def test_emof::multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=emof::Extent_strategy)
@settings(max_examples=50)
def test_emof::extent_instantiation(instance):
    assert isinstance(instance, emof::Extent)

@given(instance=Enumeration_strategy)
@settings(max_examples=50)
def test_enumeration_instantiation(instance):
    assert isinstance(instance, Enumeration)
