import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Class_Attribute,
    Class_Class,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_class_attribute_is_not_abstract():
    assert not inspect.isabstract(Class_Attribute)


def test_class_attribute_constructor_exists():
    assert callable(Class_Attribute.__init__)


def test_class_attribute_constructor_args():
    sig = inspect.signature(Class_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "derive" in params, "Missing parameter 'derive'"
    assert "id" in params, "Missing parameter 'id'"

def test_class_attribute_has_name():
    assert hasattr(Class_Attribute, "name")
    descriptor = None
    for klass in Class_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_class_attribute_has_derive():
    assert hasattr(Class_Attribute, "derive")
    descriptor = None
    for klass in Class_Attribute.__mro__:
        if "derive" in klass.__dict__:
            descriptor = klass.__dict__["derive"]
            break
    assert isinstance(descriptor, property)

def test_class_attribute_has_id():
    assert hasattr(Class_Attribute, "id")
    descriptor = None
    for klass in Class_Attribute.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_class_class_is_not_abstract():
    assert not inspect.isabstract(Class_Class)


def test_class_class_constructor_exists():
    assert callable(Class_Class.__init__)


def test_class_class_constructor_args():
    sig = inspect.signature(Class_Class.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_class_class_has_id():
    assert hasattr(Class_Class, "id")
    descriptor = None
    for klass in Class_Class.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_class_class_has_name():
    assert hasattr(Class_Class, "name")
    descriptor = None
    for klass in Class_Class.__mro__:
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
Class_Attribute_strategy = st.builds(
    Class_Attribute,
    name=
        safe_text,
    derive=
        st.booleans(),
    id=
        safe_text
)
Class_Class_strategy = st.builds(
    Class_Class,
    id=
        safe_text,
    name=
        safe_text
)

@given(instance=Class_Attribute_strategy)
@settings(max_examples=50)
def test_class_attribute_instantiation(instance):
    assert isinstance(instance, Class_Attribute)



@given(instance=Class_Attribute_strategy)
def test_class_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Class_Attribute_strategy)
def test_class_attribute_derive_setter(instance):
    original = instance.derive
    instance.derive = original
    assert instance.derive == original



@given(instance=Class_Attribute_strategy)
def test_class_attribute_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Class_Class_strategy)
@settings(max_examples=50)
def test_class_class_instantiation(instance):
    assert isinstance(instance, Class_Class)



@given(instance=Class_Class_strategy)
def test_class_class_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Class_Class_strategy)
def test_class_class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
