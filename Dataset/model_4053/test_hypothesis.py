import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Type,
    smalluml::Infinity,
    smalluml::String,
    smalluml::Integer,
    smalluml::Boolean,
    smalluml::Real,
    NamedElement,
    smalluml::Package,
    smalluml::Generalisation,
    smalluml::Enumeration,
    smalluml::Type,
    smalluml::NamedElement,
    smalluml::Cardinality,
    smalluml::Relation,
    smalluml::Method,
    smalluml::Attribute,
    smalluml::Class,
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



def test_smalluml::infinity_is_not_abstract():
    assert not inspect.isabstract(smalluml::Infinity)


def test_smalluml::infinity_constructor_exists():
    assert callable(smalluml::Infinity.__init__)


def test_smalluml::infinity_constructor_args():
    sig = inspect.signature(smalluml::Infinity.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::string_is_not_abstract():
    assert not inspect.isabstract(smalluml::String)


def test_smalluml::string_constructor_exists():
    assert callable(smalluml::String.__init__)


def test_smalluml::string_constructor_args():
    sig = inspect.signature(smalluml::String.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::integer_is_not_abstract():
    assert not inspect.isabstract(smalluml::Integer)


def test_smalluml::integer_constructor_exists():
    assert callable(smalluml::Integer.__init__)


def test_smalluml::integer_constructor_args():
    sig = inspect.signature(smalluml::Integer.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::boolean_is_not_abstract():
    assert not inspect.isabstract(smalluml::Boolean)


def test_smalluml::boolean_constructor_exists():
    assert callable(smalluml::Boolean.__init__)


def test_smalluml::boolean_constructor_args():
    sig = inspect.signature(smalluml::Boolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smalluml::boolean_has_value():
    assert hasattr(smalluml::Boolean, "value")
    descriptor = None
    for klass in smalluml::Boolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smalluml::real_is_not_abstract():
    assert not inspect.isabstract(smalluml::Real)


def test_smalluml::real_constructor_exists():
    assert callable(smalluml::Real.__init__)


def test_smalluml::real_constructor_args():
    sig = inspect.signature(smalluml::Real.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::package_is_not_abstract():
    assert not inspect.isabstract(smalluml::Package)


def test_smalluml::package_constructor_exists():
    assert callable(smalluml::Package.__init__)


def test_smalluml::package_constructor_args():
    sig = inspect.signature(smalluml::Package.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::generalisation_is_not_abstract():
    assert not inspect.isabstract(smalluml::Generalisation)


def test_smalluml::generalisation_constructor_exists():
    assert callable(smalluml::Generalisation.__init__)


def test_smalluml::generalisation_constructor_args():
    sig = inspect.signature(smalluml::Generalisation.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::enumeration_is_not_abstract():
    assert not inspect.isabstract(smalluml::Enumeration)


def test_smalluml::enumeration_constructor_exists():
    assert callable(smalluml::Enumeration.__init__)


def test_smalluml::enumeration_constructor_args():
    sig = inspect.signature(smalluml::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::type_is_not_abstract():
    assert not inspect.isabstract(smalluml::Type)


def test_smalluml::type_constructor_exists():
    assert callable(smalluml::Type.__init__)


def test_smalluml::type_constructor_args():
    sig = inspect.signature(smalluml::Type.__init__)
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



def test_smalluml::cardinality_is_not_abstract():
    assert not inspect.isabstract(smalluml::Cardinality)


def test_smalluml::cardinality_constructor_exists():
    assert callable(smalluml::Cardinality.__init__)


def test_smalluml::cardinality_constructor_args():
    sig = inspect.signature(smalluml::Cardinality.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_smalluml::cardinality_has_lowerBound():
    assert hasattr(smalluml::Cardinality, "lowerBound")
    descriptor = None
    for klass in smalluml::Cardinality.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_smalluml::cardinality_has_upperBound():
    assert hasattr(smalluml::Cardinality, "upperBound")
    descriptor = None
    for klass in smalluml::Cardinality.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_smalluml::relation_is_not_abstract():
    assert not inspect.isabstract(smalluml::Relation)


def test_smalluml::relation_constructor_exists():
    assert callable(smalluml::Relation.__init__)


def test_smalluml::relation_constructor_args():
    sig = inspect.signature(smalluml::Relation.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::method_is_not_abstract():
    assert not inspect.isabstract(smalluml::Method)


def test_smalluml::method_constructor_exists():
    assert callable(smalluml::Method.__init__)


def test_smalluml::method_constructor_args():
    sig = inspect.signature(smalluml::Method.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::attribute_is_not_abstract():
    assert not inspect.isabstract(smalluml::Attribute)


def test_smalluml::attribute_constructor_exists():
    assert callable(smalluml::Attribute.__init__)


def test_smalluml::attribute_constructor_args():
    sig = inspect.signature(smalluml::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::class_is_not_abstract():
    assert not inspect.isabstract(smalluml::Class)


def test_smalluml::class_constructor_exists():
    assert callable(smalluml::Class.__init__)


def test_smalluml::class_constructor_args():
    sig = inspect.signature(smalluml::Class.__init__)
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
Type_strategy = st.builds(
    Type,
)
smalluml::Infinity_strategy = st.builds(
    smalluml::Infinity,
)
smalluml::String_strategy = st.builds(
    smalluml::String,
)
smalluml::Integer_strategy = st.builds(
    smalluml::Integer,
)
smalluml::Boolean_strategy = st.builds(
    smalluml::Boolean,
    value=
        st.booleans()
)
smalluml::Real_strategy = st.builds(
    smalluml::Real,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
smalluml::Package_strategy = st.builds(
    smalluml::Package,
)
smalluml::Generalisation_strategy = st.builds(
    smalluml::Generalisation,
)
smalluml::Enumeration_strategy = st.builds(
    smalluml::Enumeration,
)
smalluml::Type_strategy = st.builds(
    smalluml::Type,
)
smalluml::NamedElement_strategy = st.builds(
    smalluml::NamedElement,
    name=
        safe_text
)
smalluml::Cardinality_strategy = st.builds(
    smalluml::Cardinality,
    lowerBound=
        st.integers(),
    upperBound=
        st.integers()
)
smalluml::Relation_strategy = st.builds(
    smalluml::Relation,
)
smalluml::Method_strategy = st.builds(
    smalluml::Method,
)
smalluml::Attribute_strategy = st.builds(
    smalluml::Attribute,
)
smalluml::Class_strategy = st.builds(
    smalluml::Class,
)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=smalluml::Infinity_strategy)
@settings(max_examples=50)
def test_smalluml::infinity_instantiation(instance):
    assert isinstance(instance, smalluml::Infinity)

@given(instance=smalluml::String_strategy)
@settings(max_examples=50)
def test_smalluml::string_instantiation(instance):
    assert isinstance(instance, smalluml::String)

@given(instance=smalluml::Integer_strategy)
@settings(max_examples=50)
def test_smalluml::integer_instantiation(instance):
    assert isinstance(instance, smalluml::Integer)

@given(instance=smalluml::Boolean_strategy)
@settings(max_examples=50)
def test_smalluml::boolean_instantiation(instance):
    assert isinstance(instance, smalluml::Boolean)

@given(instance=smalluml::Boolean_strategy)
def test_smalluml::boolean_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=smalluml::Boolean_strategy)
def test_smalluml::boolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smalluml::Real_strategy)
@settings(max_examples=50)
def test_smalluml::real_instantiation(instance):
    assert isinstance(instance, smalluml::Real)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=smalluml::Package_strategy)
@settings(max_examples=50)
def test_smalluml::package_instantiation(instance):
    assert isinstance(instance, smalluml::Package)

@given(instance=smalluml::Generalisation_strategy)
@settings(max_examples=50)
def test_smalluml::generalisation_instantiation(instance):
    assert isinstance(instance, smalluml::Generalisation)

@given(instance=smalluml::Enumeration_strategy)
@settings(max_examples=50)
def test_smalluml::enumeration_instantiation(instance):
    assert isinstance(instance, smalluml::Enumeration)

@given(instance=smalluml::Type_strategy)
@settings(max_examples=50)
def test_smalluml::type_instantiation(instance):
    assert isinstance(instance, smalluml::Type)

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

@given(instance=smalluml::Cardinality_strategy)
@settings(max_examples=50)
def test_smalluml::cardinality_instantiation(instance):
    assert isinstance(instance, smalluml::Cardinality)

@given(instance=smalluml::Cardinality_strategy)
def test_smalluml::cardinality_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=smalluml::Cardinality_strategy)
def test_smalluml::cardinality_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=smalluml::Cardinality_strategy)
def test_smalluml::cardinality_upperBound_type(instance):
    assert isinstance(instance.upperBound, int)


@given(instance=smalluml::Cardinality_strategy)
def test_smalluml::cardinality_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=smalluml::Relation_strategy)
@settings(max_examples=50)
def test_smalluml::relation_instantiation(instance):
    assert isinstance(instance, smalluml::Relation)

@given(instance=smalluml::Method_strategy)
@settings(max_examples=50)
def test_smalluml::method_instantiation(instance):
    assert isinstance(instance, smalluml::Method)

@given(instance=smalluml::Attribute_strategy)
@settings(max_examples=50)
def test_smalluml::attribute_instantiation(instance):
    assert isinstance(instance, smalluml::Attribute)

@given(instance=smalluml::Class_strategy)
@settings(max_examples=50)
def test_smalluml::class_instantiation(instance):
    assert isinstance(instance, smalluml::Class)
