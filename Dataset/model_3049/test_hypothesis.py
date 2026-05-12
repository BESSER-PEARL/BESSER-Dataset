import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Feature,
    myDsl_Reference,
    myDsl_Attribute,
    myDsl_Entity,
    myDsl_Model,
    myDsl_Feature,
    Type,
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



def test_mydsl_reference_is_not_abstract():
    assert not inspect.isabstract(myDsl_Reference)


def test_mydsl_reference_constructor_exists():
    assert callable(myDsl_Reference.__init__)


def test_mydsl_reference_constructor_args():
    sig = inspect.signature(myDsl_Reference.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_attribute_is_not_abstract():
    assert not inspect.isabstract(myDsl_Attribute)


def test_mydsl_attribute_constructor_exists():
    assert callable(myDsl_Attribute.__init__)


def test_mydsl_attribute_constructor_args():
    sig = inspect.signature(myDsl_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_mydsl_attribute_has_type():
    assert hasattr(myDsl_Attribute, "type")
    descriptor = None
    for klass in myDsl_Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_entity_is_not_abstract():
    assert not inspect.isabstract(myDsl_Entity)


def test_mydsl_entity_constructor_exists():
    assert callable(myDsl_Entity.__init__)


def test_mydsl_entity_constructor_args():
    sig = inspect.signature(myDsl_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_entity_has_name():
    assert hasattr(myDsl_Entity, "name")
    descriptor = None
    for klass in myDsl_Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_model_is_not_abstract():
    assert not inspect.isabstract(myDsl_Model)


def test_mydsl_model_constructor_exists():
    assert callable(myDsl_Model.__init__)


def test_mydsl_model_constructor_args():
    sig = inspect.signature(myDsl_Model.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_feature_is_not_abstract():
    assert not inspect.isabstract(myDsl_Feature)


def test_mydsl_feature_constructor_exists():
    assert callable(myDsl_Feature.__init__)


def test_mydsl_feature_constructor_args():
    sig = inspect.signature(myDsl_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_feature_has_name():
    assert hasattr(myDsl_Feature, "name")
    descriptor = None
    for klass in myDsl_Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "int",
        "string",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"


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
myDsl_Reference_strategy = st.builds(
    myDsl_Reference,
)
myDsl_Attribute_strategy = st.builds(
    myDsl_Attribute,
    type=
        safe_text
)
myDsl_Entity_strategy = st.builds(
    myDsl_Entity,
    name=
        safe_text
)
myDsl_Model_strategy = st.builds(
    myDsl_Model,
)
myDsl_Feature_strategy = st.builds(
    myDsl_Feature,
    name=
        safe_text
)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=myDsl_Reference_strategy)
@settings(max_examples=50)
def test_mydsl_reference_instantiation(instance):
    assert isinstance(instance, myDsl_Reference)

@given(instance=myDsl_Attribute_strategy)
@settings(max_examples=50)
def test_mydsl_attribute_instantiation(instance):
    assert isinstance(instance, myDsl_Attribute)



@given(instance=myDsl_Attribute_strategy)
def test_mydsl_attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=myDsl_Entity_strategy)
@settings(max_examples=50)
def test_mydsl_entity_instantiation(instance):
    assert isinstance(instance, myDsl_Entity)



@given(instance=myDsl_Entity_strategy)
def test_mydsl_entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Model_strategy)
@settings(max_examples=50)
def test_mydsl_model_instantiation(instance):
    assert isinstance(instance, myDsl_Model)

@given(instance=myDsl_Feature_strategy)
@settings(max_examples=50)
def test_mydsl_feature_instantiation(instance):
    assert isinstance(instance, myDsl_Feature)



@given(instance=myDsl_Feature_strategy)
def test_mydsl_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
