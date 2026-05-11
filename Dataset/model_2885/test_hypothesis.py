import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    metamodel::Feature,
    Type,
    metamodel::Entity,
    metamodel::Datatype,
    metamodel::Type,
    metamodel::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metamodel::feature_is_not_abstract():
    assert not inspect.isabstract(metamodel::Feature)


def test_metamodel::feature_constructor_exists():
    assert callable(metamodel::Feature.__init__)


def test_metamodel::feature_constructor_args():
    sig = inspect.signature(metamodel::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metamodel::feature_has_name():
    assert hasattr(metamodel::Feature, "name")
    descriptor = None
    for klass in metamodel::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::entity_is_not_abstract():
    assert not inspect.isabstract(metamodel::Entity)


def test_metamodel::entity_constructor_exists():
    assert callable(metamodel::Entity.__init__)


def test_metamodel::entity_constructor_args():
    sig = inspect.signature(metamodel::Entity.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::datatype_is_not_abstract():
    assert not inspect.isabstract(metamodel::Datatype)


def test_metamodel::datatype_constructor_exists():
    assert callable(metamodel::Datatype.__init__)


def test_metamodel::datatype_constructor_args():
    sig = inspect.signature(metamodel::Datatype.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::type_is_not_abstract():
    assert not inspect.isabstract(metamodel::Type)


def test_metamodel::type_constructor_exists():
    assert callable(metamodel::Type.__init__)


def test_metamodel::type_constructor_args():
    sig = inspect.signature(metamodel::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metamodel::type_has_name():
    assert hasattr(metamodel::Type, "name")
    descriptor = None
    for klass in metamodel::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metamodel::model_is_not_abstract():
    assert not inspect.isabstract(metamodel::Model)


def test_metamodel::model_constructor_exists():
    assert callable(metamodel::Model.__init__)


def test_metamodel::model_constructor_args():
    sig = inspect.signature(metamodel::Model.__init__)
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
metamodel::Feature_strategy = st.builds(
    metamodel::Feature,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
metamodel::Entity_strategy = st.builds(
    metamodel::Entity,
)
metamodel::Datatype_strategy = st.builds(
    metamodel::Datatype,
)
metamodel::Type_strategy = st.builds(
    metamodel::Type,
    name=
        safe_text
)
metamodel::Model_strategy = st.builds(
    metamodel::Model,
)

@given(instance=metamodel::Feature_strategy)
@settings(max_examples=50)
def test_metamodel::feature_instantiation(instance):
    assert isinstance(instance, metamodel::Feature)

@given(instance=metamodel::Feature_strategy)
def test_metamodel::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metamodel::Feature_strategy)
def test_metamodel::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=metamodel::Entity_strategy)
@settings(max_examples=50)
def test_metamodel::entity_instantiation(instance):
    assert isinstance(instance, metamodel::Entity)

@given(instance=metamodel::Datatype_strategy)
@settings(max_examples=50)
def test_metamodel::datatype_instantiation(instance):
    assert isinstance(instance, metamodel::Datatype)

@given(instance=metamodel::Type_strategy)
@settings(max_examples=50)
def test_metamodel::type_instantiation(instance):
    assert isinstance(instance, metamodel::Type)

@given(instance=metamodel::Type_strategy)
def test_metamodel::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metamodel::Type_strategy)
def test_metamodel::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metamodel::Model_strategy)
@settings(max_examples=50)
def test_metamodel::model_instantiation(instance):
    assert isinstance(instance, metamodel::Model)
