import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    simpleClass_Model,
    simpleClass_Attribute,
    simpleClass_Class,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpleclass_model_is_not_abstract():
    assert not inspect.isabstract(simpleClass_Model)


def test_simpleclass_model_constructor_exists():
    assert callable(simpleClass_Model.__init__)


def test_simpleclass_model_constructor_args():
    sig = inspect.signature(simpleClass_Model.__init__)
    params = list(sig.parameters.keys())



def test_simpleclass_attribute_is_not_abstract():
    assert not inspect.isabstract(simpleClass_Attribute)


def test_simpleclass_attribute_constructor_exists():
    assert callable(simpleClass_Attribute.__init__)


def test_simpleclass_attribute_constructor_args():
    sig = inspect.signature(simpleClass_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "isPublic" in params, "Missing parameter 'isPublic'"
    assert "name" in params, "Missing parameter 'name'"

def test_simpleclass_attribute_has_isPublic():
    assert hasattr(simpleClass_Attribute, "isPublic")
    descriptor = None
    for klass in simpleClass_Attribute.__mro__:
        if "isPublic" in klass.__dict__:
            descriptor = klass.__dict__["isPublic"]
            break
    assert isinstance(descriptor, property)

def test_simpleclass_attribute_has_name():
    assert hasattr(simpleClass_Attribute, "name")
    descriptor = None
    for klass in simpleClass_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleclass_class_is_not_abstract():
    assert not inspect.isabstract(simpleClass_Class)


def test_simpleclass_class_constructor_exists():
    assert callable(simpleClass_Class.__init__)


def test_simpleclass_class_constructor_args():
    sig = inspect.signature(simpleClass_Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleclass_class_has_name():
    assert hasattr(simpleClass_Class, "name")
    descriptor = None
    for klass in simpleClass_Class.__mro__:
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
simpleClass_Model_strategy = st.builds(
    simpleClass_Model,
)
simpleClass_Attribute_strategy = st.builds(
    simpleClass_Attribute,
    isPublic=
        st.booleans(),
    name=
        safe_text
)
simpleClass_Class_strategy = st.builds(
    simpleClass_Class,
    name=
        safe_text
)

@given(instance=simpleClass_Model_strategy)
@settings(max_examples=50)
def test_simpleclass_model_instantiation(instance):
    assert isinstance(instance, simpleClass_Model)

@given(instance=simpleClass_Attribute_strategy)
@settings(max_examples=50)
def test_simpleclass_attribute_instantiation(instance):
    assert isinstance(instance, simpleClass_Attribute)



@given(instance=simpleClass_Attribute_strategy)
def test_simpleclass_attribute_isPublic_setter(instance):
    original = instance.isPublic
    instance.isPublic = original
    assert instance.isPublic == original



@given(instance=simpleClass_Attribute_strategy)
def test_simpleclass_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleClass_Class_strategy)
@settings(max_examples=50)
def test_simpleclass_class_instantiation(instance):
    assert isinstance(instance, simpleClass_Class)



@given(instance=simpleClass_Class_strategy)
def test_simpleclass_class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
