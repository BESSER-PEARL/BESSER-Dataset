import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Type,
    smalluml::Integer,
    smalluml::Bool,
    smalluml::Real,
    smalluml::UnlimitedNatural,
    smalluml::String,
    smalluml::Type,
    NamedElement,
    smalluml::Parameter,
    smalluml::Relation,
    smalluml::Attribute,
    smalluml::Method,
    smalluml::Class,
    smalluml::NamedElement,
    smalluml::Package,
    Relation,
    smalluml::Reference,
    smalluml::Composition,
    smalluml::Enumeration,
    smalluml::Role,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::integer_is_not_abstract():
    assert not inspect.isabstract(smalluml::Integer)


def test_smalluml::integer_constructor_exists():
    assert callable(smalluml::Integer.__init__)


def test_smalluml::integer_constructor_args():
    sig = inspect.signature(smalluml::Integer.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::bool_is_not_abstract():
    assert not inspect.isabstract(smalluml::Bool)


def test_smalluml::bool_constructor_exists():
    assert callable(smalluml::Bool.__init__)


def test_smalluml::bool_constructor_args():
    sig = inspect.signature(smalluml::Bool.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::real_is_not_abstract():
    assert not inspect.isabstract(smalluml::Real)


def test_smalluml::real_constructor_exists():
    assert callable(smalluml::Real.__init__)


def test_smalluml::real_constructor_args():
    sig = inspect.signature(smalluml::Real.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::unlimitednatural_is_not_abstract():
    assert not inspect.isabstract(smalluml::UnlimitedNatural)


def test_smalluml::unlimitednatural_constructor_exists():
    assert callable(smalluml::UnlimitedNatural.__init__)


def test_smalluml::unlimitednatural_constructor_args():
    sig = inspect.signature(smalluml::UnlimitedNatural.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::string_is_not_abstract():
    assert not inspect.isabstract(smalluml::String)


def test_smalluml::string_constructor_exists():
    assert callable(smalluml::String.__init__)


def test_smalluml::string_constructor_args():
    sig = inspect.signature(smalluml::String.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::type_is_not_abstract():
    assert not inspect.isabstract(smalluml::Type)


def test_smalluml::type_constructor_exists():
    assert callable(smalluml::Type.__init__)


def test_smalluml::type_constructor_args():
    sig = inspect.signature(smalluml::Type.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::parameter_is_not_abstract():
    assert not inspect.isabstract(smalluml::Parameter)


def test_smalluml::parameter_constructor_exists():
    assert callable(smalluml::Parameter.__init__)


def test_smalluml::parameter_constructor_args():
    sig = inspect.signature(smalluml::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::relation_is_not_abstract():
    assert not inspect.isabstract(smalluml::Relation)


def test_smalluml::relation_constructor_exists():
    assert callable(smalluml::Relation.__init__)


def test_smalluml::relation_constructor_args():
    sig = inspect.signature(smalluml::Relation.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::attribute_is_not_abstract():
    assert not inspect.isabstract(smalluml::Attribute)


def test_smalluml::attribute_constructor_exists():
    assert callable(smalluml::Attribute.__init__)


def test_smalluml::attribute_constructor_args():
    sig = inspect.signature(smalluml::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::method_is_not_abstract():
    assert not inspect.isabstract(smalluml::Method)


def test_smalluml::method_constructor_exists():
    assert callable(smalluml::Method.__init__)


def test_smalluml::method_constructor_args():
    sig = inspect.signature(smalluml::Method.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::class_is_not_abstract():
    assert not inspect.isabstract(smalluml::Class)


def test_smalluml::class_constructor_exists():
    assert callable(smalluml::Class.__init__)


def test_smalluml::class_constructor_args():
    sig = inspect.signature(smalluml::Class.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::namedelement_is_not_abstract():
    assert not inspect.isabstract(smalluml::NamedElement)


def test_smalluml::namedelement_constructor_exists():
    assert callable(smalluml::NamedElement.__init__)


def test_smalluml::namedelement_constructor_args():
    sig = inspect.signature(smalluml::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smalluml::namedelement_has_name():
    assert hasattr(smalluml::NamedElement, "name")
    descriptor = None
    for klass in smalluml::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smalluml::package_is_not_abstract():
    assert not inspect.isabstract(smalluml::Package)


def test_smalluml::package_constructor_exists():
    assert callable(smalluml::Package.__init__)


def test_smalluml::package_constructor_args():
    sig = inspect.signature(smalluml::Package.__init__)
    params = list(sig.parameters.keys())



def test_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::reference_is_not_abstract():
    assert not inspect.isabstract(smalluml::Reference)


def test_smalluml::reference_constructor_exists():
    assert callable(smalluml::Reference.__init__)


def test_smalluml::reference_constructor_args():
    sig = inspect.signature(smalluml::Reference.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::composition_is_not_abstract():
    assert not inspect.isabstract(smalluml::Composition)


def test_smalluml::composition_constructor_exists():
    assert callable(smalluml::Composition.__init__)


def test_smalluml::composition_constructor_args():
    sig = inspect.signature(smalluml::Composition.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::enumeration_is_not_abstract():
    assert not inspect.isabstract(smalluml::Enumeration)


def test_smalluml::enumeration_constructor_exists():
    assert callable(smalluml::Enumeration.__init__)


def test_smalluml::enumeration_constructor_args():
    sig = inspect.signature(smalluml::Enumeration.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_smalluml::enumeration_has_values():
    assert hasattr(smalluml::Enumeration, "values")
    descriptor = None
    for klass in smalluml::Enumeration.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_smalluml::role_is_not_abstract():
    assert not inspect.isabstract(smalluml::Role)


def test_smalluml::role_constructor_exists():
    assert callable(smalluml::Role.__init__)


def test_smalluml::role_constructor_args():
    sig = inspect.signature(smalluml::Role.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_smalluml::role_has_lowerBound():
    assert hasattr(smalluml::Role, "lowerBound")
    descriptor = None
    for klass in smalluml::Role.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_smalluml::role_has_upperBound():
    assert hasattr(smalluml::Role, "upperBound")
    descriptor = None
    for klass in smalluml::Role.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)


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
Type_strategy = st.builds(
    Type,
)
smalluml::Integer_strategy = st.builds(
    smalluml::Integer,
)
smalluml::Bool_strategy = st.builds(
    smalluml::Bool,
)
smalluml::Real_strategy = st.builds(
    smalluml::Real,
)
smalluml::UnlimitedNatural_strategy = st.builds(
    smalluml::UnlimitedNatural,
)
smalluml::String_strategy = st.builds(
    smalluml::String,
)
smalluml::Type_strategy = st.builds(
    smalluml::Type,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
smalluml::Parameter_strategy = st.builds(
    smalluml::Parameter,
)
smalluml::Relation_strategy = st.builds(
    smalluml::Relation,
)
smalluml::Attribute_strategy = st.builds(
    smalluml::Attribute,
)
smalluml::Method_strategy = st.builds(
    smalluml::Method,
)
smalluml::Class_strategy = st.builds(
    smalluml::Class,
)
smalluml::NamedElement_strategy = st.builds(
    smalluml::NamedElement,
    name=
        safe_text
)
smalluml::Package_strategy = st.builds(
    smalluml::Package,
)
Relation_strategy = st.builds(
    Relation,
)
smalluml::Reference_strategy = st.builds(
    smalluml::Reference,
)
smalluml::Composition_strategy = st.builds(
    smalluml::Composition,
)
smalluml::Enumeration_strategy = st.builds(
    smalluml::Enumeration,
    values=
        safe_text
)
smalluml::Role_strategy = st.builds(
    smalluml::Role,
    lowerBound=
        st.integers(),
    upperBound=
        st.integers()
)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=smalluml::Integer_strategy)
@settings(max_examples=50)
def test_smalluml::integer_instantiation(instance):
    assert isinstance(instance, smalluml::Integer)

@given(instance=smalluml::Bool_strategy)
@settings(max_examples=50)
def test_smalluml::bool_instantiation(instance):
    assert isinstance(instance, smalluml::Bool)

@given(instance=smalluml::Real_strategy)
@settings(max_examples=50)
def test_smalluml::real_instantiation(instance):
    assert isinstance(instance, smalluml::Real)

@given(instance=smalluml::UnlimitedNatural_strategy)
@settings(max_examples=50)
def test_smalluml::unlimitednatural_instantiation(instance):
    assert isinstance(instance, smalluml::UnlimitedNatural)

@given(instance=smalluml::String_strategy)
@settings(max_examples=50)
def test_smalluml::string_instantiation(instance):
    assert isinstance(instance, smalluml::String)

@given(instance=smalluml::Type_strategy)
@settings(max_examples=50)
def test_smalluml::type_instantiation(instance):
    assert isinstance(instance, smalluml::Type)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=smalluml::Parameter_strategy)
@settings(max_examples=50)
def test_smalluml::parameter_instantiation(instance):
    assert isinstance(instance, smalluml::Parameter)

@given(instance=smalluml::Relation_strategy)
@settings(max_examples=50)
def test_smalluml::relation_instantiation(instance):
    assert isinstance(instance, smalluml::Relation)

@given(instance=smalluml::Attribute_strategy)
@settings(max_examples=50)
def test_smalluml::attribute_instantiation(instance):
    assert isinstance(instance, smalluml::Attribute)

@given(instance=smalluml::Method_strategy)
@settings(max_examples=50)
def test_smalluml::method_instantiation(instance):
    assert isinstance(instance, smalluml::Method)

@given(instance=smalluml::Class_strategy)
@settings(max_examples=50)
def test_smalluml::class_instantiation(instance):
    assert isinstance(instance, smalluml::Class)

@given(instance=smalluml::NamedElement_strategy)
@settings(max_examples=50)
def test_smalluml::namedelement_instantiation(instance):
    assert isinstance(instance, smalluml::NamedElement)

@given(instance=smalluml::NamedElement_strategy)
def test_smalluml::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smalluml::NamedElement_strategy)
def test_smalluml::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smalluml::Package_strategy)
@settings(max_examples=50)
def test_smalluml::package_instantiation(instance):
    assert isinstance(instance, smalluml::Package)

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=smalluml::Reference_strategy)
@settings(max_examples=50)
def test_smalluml::reference_instantiation(instance):
    assert isinstance(instance, smalluml::Reference)

@given(instance=smalluml::Composition_strategy)
@settings(max_examples=50)
def test_smalluml::composition_instantiation(instance):
    assert isinstance(instance, smalluml::Composition)

@given(instance=smalluml::Enumeration_strategy)
@settings(max_examples=50)
def test_smalluml::enumeration_instantiation(instance):
    assert isinstance(instance, smalluml::Enumeration)

@given(instance=smalluml::Enumeration_strategy)
def test_smalluml::enumeration_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=smalluml::Enumeration_strategy)
def test_smalluml::enumeration_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=smalluml::Role_strategy)
@settings(max_examples=50)
def test_smalluml::role_instantiation(instance):
    assert isinstance(instance, smalluml::Role)

@given(instance=smalluml::Role_strategy)
def test_smalluml::role_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=smalluml::Role_strategy)
def test_smalluml::role_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=smalluml::Role_strategy)
def test_smalluml::role_upperBound_type(instance):
    assert isinstance(instance.upperBound, int)


@given(instance=smalluml::Role_strategy)
def test_smalluml::role_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original
