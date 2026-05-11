import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Feature,
    types::Property,
    types::Operation,
    TypedElement,
    NamedElement,
    types::Feature,
    types::Parameter,
    types::Event,
    types::TypedElement,
    types::Type,
    types::Library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_types::property_is_not_abstract():
    assert not inspect.isabstract(types::Property)


def test_types::property_constructor_exists():
    assert callable(types::Property.__init__)


def test_types::property_constructor_args():
    sig = inspect.signature(types::Property.__init__)
    params = list(sig.parameters.keys())



def test_types::operation_is_not_abstract():
    assert not inspect.isabstract(types::Operation)


def test_types::operation_constructor_exists():
    assert callable(types::Operation.__init__)


def test_types::operation_constructor_args():
    sig = inspect.signature(types::Operation.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_types::feature_is_not_abstract():
    assert not inspect.isabstract(types::Feature)


def test_types::feature_constructor_exists():
    assert callable(types::Feature.__init__)


def test_types::feature_constructor_args():
    sig = inspect.signature(types::Feature.__init__)
    params = list(sig.parameters.keys())



def test_types::parameter_is_not_abstract():
    assert not inspect.isabstract(types::Parameter)


def test_types::parameter_constructor_exists():
    assert callable(types::Parameter.__init__)


def test_types::parameter_constructor_args():
    sig = inspect.signature(types::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_types::event_is_not_abstract():
    assert not inspect.isabstract(types::Event)


def test_types::event_constructor_exists():
    assert callable(types::Event.__init__)


def test_types::event_constructor_args():
    sig = inspect.signature(types::Event.__init__)
    params = list(sig.parameters.keys())



def test_types::typedelement_is_not_abstract():
    assert not inspect.isabstract(types::TypedElement)


def test_types::typedelement_constructor_exists():
    assert callable(types::TypedElement.__init__)


def test_types::typedelement_constructor_args():
    sig = inspect.signature(types::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_types::type_is_not_abstract():
    assert not inspect.isabstract(types::Type)


def test_types::type_constructor_exists():
    assert callable(types::Type.__init__)


def test_types::type_constructor_args():
    sig = inspect.signature(types::Type.__init__)
    params = list(sig.parameters.keys())



def test_types::library_is_not_abstract():
    assert not inspect.isabstract(types::Library)


def test_types::library_constructor_exists():
    assert callable(types::Library.__init__)


def test_types::library_constructor_args():
    sig = inspect.signature(types::Library.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_types::library_has_id():
    assert hasattr(types::Library, "id")
    descriptor = None
    for klass in types::Library.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
Feature_strategy = st.builds(
    Feature,
)
types::Property_strategy = st.builds(
    types::Property,
)
types::Operation_strategy = st.builds(
    types::Operation,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
types::Feature_strategy = st.builds(
    types::Feature,
)
types::Parameter_strategy = st.builds(
    types::Parameter,
)
types::Event_strategy = st.builds(
    types::Event,
)
types::TypedElement_strategy = st.builds(
    types::TypedElement,
)
types::Type_strategy = st.builds(
    types::Type,
)
types::Library_strategy = st.builds(
    types::Library,
    id=
        safe_text
)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=types::Property_strategy)
@settings(max_examples=50)
def test_types::property_instantiation(instance):
    assert isinstance(instance, types::Property)

@given(instance=types::Operation_strategy)
@settings(max_examples=50)
def test_types::operation_instantiation(instance):
    assert isinstance(instance, types::Operation)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=types::Feature_strategy)
@settings(max_examples=50)
def test_types::feature_instantiation(instance):
    assert isinstance(instance, types::Feature)

@given(instance=types::Parameter_strategy)
@settings(max_examples=50)
def test_types::parameter_instantiation(instance):
    assert isinstance(instance, types::Parameter)

@given(instance=types::Event_strategy)
@settings(max_examples=50)
def test_types::event_instantiation(instance):
    assert isinstance(instance, types::Event)

@given(instance=types::TypedElement_strategy)
@settings(max_examples=50)
def test_types::typedelement_instantiation(instance):
    assert isinstance(instance, types::TypedElement)

@given(instance=types::Type_strategy)
@settings(max_examples=50)
def test_types::type_instantiation(instance):
    assert isinstance(instance, types::Type)

@given(instance=types::Library_strategy)
@settings(max_examples=50)
def test_types::library_instantiation(instance):
    assert isinstance(instance, types::Library)

@given(instance=types::Library_strategy)
def test_types::library_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=types::Library_strategy)
def test_types::library_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
