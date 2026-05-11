import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Class::Attribute,
    Class::Class,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_class::attribute_is_not_abstract():
    assert not inspect.isabstract(Class::Attribute)


def test_class::attribute_constructor_exists():
    assert callable(Class::Attribute.__init__)


def test_class::attribute_constructor_args():
    sig = inspect.signature(Class::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "multiValued" in params, "Missing parameter 'multiValued'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_class::attribute_has_multiValued():
    assert hasattr(Class::Attribute, "multiValued")
    descriptor = None
    for klass in Class::Attribute.__mro__:
        if "multiValued" in klass.__dict__:
            descriptor = klass.__dict__["multiValued"]
            break
    assert isinstance(descriptor, property)

def test_class::attribute_has_id():
    assert hasattr(Class::Attribute, "id")
    descriptor = None
    for klass in Class::Attribute.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_class::attribute_has_name():
    assert hasattr(Class::Attribute, "name")
    descriptor = None
    for klass in Class::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_class::class_is_not_abstract():
    assert not inspect.isabstract(Class::Class)


def test_class::class_constructor_exists():
    assert callable(Class::Class.__init__)


def test_class::class_constructor_args():
    sig = inspect.signature(Class::Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_class::class_has_name():
    assert hasattr(Class::Class, "name")
    descriptor = None
    for klass in Class::Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_class::class_has_id():
    assert hasattr(Class::Class, "id")
    descriptor = None
    for klass in Class::Class.__mro__:
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
Class::Attribute_strategy = st.builds(
    Class::Attribute,
    multiValued=
        st.booleans(),
    id=
        safe_text,
    name=
        safe_text
)
Class::Class_strategy = st.builds(
    Class::Class,
    name=
        safe_text,
    id=
        safe_text
)

@given(instance=Class::Attribute_strategy)
@settings(max_examples=50)
def test_class::attribute_instantiation(instance):
    assert isinstance(instance, Class::Attribute)

@given(instance=Class::Attribute_strategy)
def test_class::attribute_multiValued_type(instance):
    assert isinstance(instance.multiValued, bool)


@given(instance=Class::Attribute_strategy)
def test_class::attribute_multiValued_setter(instance):
    original = instance.multiValued
    instance.multiValued = original
    assert instance.multiValued == original

@given(instance=Class::Attribute_strategy)
def test_class::attribute_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=Class::Attribute_strategy)
def test_class::attribute_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Class::Attribute_strategy)
def test_class::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Class::Attribute_strategy)
def test_class::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Class::Class_strategy)
@settings(max_examples=50)
def test_class::class_instantiation(instance):
    assert isinstance(instance, Class::Class)

@given(instance=Class::Class_strategy)
def test_class::class_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Class::Class_strategy)
def test_class::class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Class::Class_strategy)
def test_class::class_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=Class::Class_strategy)
def test_class::class_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
