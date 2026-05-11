import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    simpleClass::Model,
    simpleClass::Attribute,
    simpleClass::Class,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpleclass::model_is_not_abstract():
    assert not inspect.isabstract(simpleClass::Model)


def test_simpleclass::model_constructor_exists():
    assert callable(simpleClass::Model.__init__)


def test_simpleclass::model_constructor_args():
    sig = inspect.signature(simpleClass::Model.__init__)
    params = list(sig.parameters.keys())



def test_simpleclass::attribute_is_not_abstract():
    assert not inspect.isabstract(simpleClass::Attribute)


def test_simpleclass::attribute_constructor_exists():
    assert callable(simpleClass::Attribute.__init__)


def test_simpleclass::attribute_constructor_args():
    sig = inspect.signature(simpleClass::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isPublic" in params, "Missing parameter 'isPublic'"

def test_simpleclass::attribute_has_name():
    assert hasattr(simpleClass::Attribute, "name")
    descriptor = None
    for klass in simpleClass::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simpleclass::attribute_has_isPublic():
    assert hasattr(simpleClass::Attribute, "isPublic")
    descriptor = None
    for klass in simpleClass::Attribute.__mro__:
        if "isPublic" in klass.__dict__:
            descriptor = klass.__dict__["isPublic"]
            break
    assert isinstance(descriptor, property)



def test_simpleclass::class_is_not_abstract():
    assert not inspect.isabstract(simpleClass::Class)


def test_simpleclass::class_constructor_exists():
    assert callable(simpleClass::Class.__init__)


def test_simpleclass::class_constructor_args():
    sig = inspect.signature(simpleClass::Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleclass::class_has_name():
    assert hasattr(simpleClass::Class, "name")
    descriptor = None
    for klass in simpleClass::Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
simpleClass::Model_strategy = st.builds(
    simpleClass::Model,
)
simpleClass::Attribute_strategy = st.builds(
    simpleClass::Attribute,
    name=
        safe_text,
    isPublic=
        st.booleans()
)
simpleClass::Class_strategy = st.builds(
    simpleClass::Class,
    name=
        safe_text
)

@given(instance=simpleClass::Model_strategy)
@settings(max_examples=50)
def test_simpleclass::model_instantiation(instance):
    assert isinstance(instance, simpleClass::Model)

@given(instance=simpleClass::Attribute_strategy)
@settings(max_examples=50)
def test_simpleclass::attribute_instantiation(instance):
    assert isinstance(instance, simpleClass::Attribute)

@given(instance=simpleClass::Attribute_strategy)
def test_simpleclass::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleClass::Attribute_strategy)
def test_simpleclass::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleClass::Attribute_strategy)
def test_simpleclass::attribute_isPublic_type(instance):
    assert isinstance(instance.isPublic, bool)


@given(instance=simpleClass::Attribute_strategy)
def test_simpleclass::attribute_isPublic_setter(instance):
    original = instance.isPublic
    instance.isPublic = original
    assert instance.isPublic == original

@given(instance=simpleClass::Class_strategy)
@settings(max_examples=50)
def test_simpleclass::class_instantiation(instance):
    assert isinstance(instance, simpleClass::Class)

@given(instance=simpleClass::Class_strategy)
def test_simpleclass::class_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleClass::Class_strategy)
def test_simpleclass::class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
