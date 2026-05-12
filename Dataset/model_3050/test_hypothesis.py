import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Ref,
    myDot_EntityRef,
    myDot_DotExpression,
    Feature,
    myDot_Reference,
    myDot_Attribute,
    myDot_Feature,
    myDot_Usage,
    myDot_Entity,
    myDot_Model,
    myDot_Ref,
    DataType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ref_is_not_abstract():
    assert not inspect.isabstract(Ref)


def test_ref_constructor_exists():
    assert callable(Ref.__init__)


def test_ref_constructor_args():
    sig = inspect.signature(Ref.__init__)
    params = list(sig.parameters.keys())



def test_mydot_entityref_is_not_abstract():
    assert not inspect.isabstract(myDot_EntityRef)


def test_mydot_entityref_constructor_exists():
    assert callable(myDot_EntityRef.__init__)


def test_mydot_entityref_constructor_args():
    sig = inspect.signature(myDot_EntityRef.__init__)
    params = list(sig.parameters.keys())



def test_mydot_dotexpression_is_not_abstract():
    assert not inspect.isabstract(myDot_DotExpression)


def test_mydot_dotexpression_constructor_exists():
    assert callable(myDot_DotExpression.__init__)


def test_mydot_dotexpression_constructor_args():
    sig = inspect.signature(myDot_DotExpression.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_mydot_reference_is_not_abstract():
    assert not inspect.isabstract(myDot_Reference)


def test_mydot_reference_constructor_exists():
    assert callable(myDot_Reference.__init__)


def test_mydot_reference_constructor_args():
    sig = inspect.signature(myDot_Reference.__init__)
    params = list(sig.parameters.keys())



def test_mydot_attribute_is_not_abstract():
    assert not inspect.isabstract(myDot_Attribute)


def test_mydot_attribute_constructor_exists():
    assert callable(myDot_Attribute.__init__)


def test_mydot_attribute_constructor_args():
    sig = inspect.signature(myDot_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_mydot_attribute_has_type():
    assert hasattr(myDot_Attribute, "type")
    descriptor = None
    for klass in myDot_Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mydot_feature_is_not_abstract():
    assert not inspect.isabstract(myDot_Feature)


def test_mydot_feature_constructor_exists():
    assert callable(myDot_Feature.__init__)


def test_mydot_feature_constructor_args():
    sig = inspect.signature(myDot_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydot_feature_has_name():
    assert hasattr(myDot_Feature, "name")
    descriptor = None
    for klass in myDot_Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydot_usage_is_not_abstract():
    assert not inspect.isabstract(myDot_Usage)


def test_mydot_usage_constructor_exists():
    assert callable(myDot_Usage.__init__)


def test_mydot_usage_constructor_args():
    sig = inspect.signature(myDot_Usage.__init__)
    params = list(sig.parameters.keys())



def test_mydot_entity_is_not_abstract():
    assert not inspect.isabstract(myDot_Entity)


def test_mydot_entity_constructor_exists():
    assert callable(myDot_Entity.__init__)


def test_mydot_entity_constructor_args():
    sig = inspect.signature(myDot_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydot_entity_has_name():
    assert hasattr(myDot_Entity, "name")
    descriptor = None
    for klass in myDot_Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydot_model_is_not_abstract():
    assert not inspect.isabstract(myDot_Model)


def test_mydot_model_constructor_exists():
    assert callable(myDot_Model.__init__)


def test_mydot_model_constructor_args():
    sig = inspect.signature(myDot_Model.__init__)
    params = list(sig.parameters.keys())



def test_mydot_ref_is_not_abstract():
    assert not inspect.isabstract(myDot_Ref)


def test_mydot_ref_constructor_exists():
    assert callable(myDot_Ref.__init__)


def test_mydot_ref_constructor_args():
    sig = inspect.signature(myDot_Ref.__init__)
    params = list(sig.parameters.keys())

def test_datatype_exists():
    # Check that the Enumeration exists
    assert DataType is not None

def test_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataType]
    expected_literals = [
        "int",
        "string",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataType"


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
Ref_strategy = st.builds(
    Ref,
)
myDot_EntityRef_strategy = st.builds(
    myDot_EntityRef,
)
myDot_DotExpression_strategy = st.builds(
    myDot_DotExpression,
)
Feature_strategy = st.builds(
    Feature,
)
myDot_Reference_strategy = st.builds(
    myDot_Reference,
)
myDot_Attribute_strategy = st.builds(
    myDot_Attribute,
    type=
        safe_text
)
myDot_Feature_strategy = st.builds(
    myDot_Feature,
    name=
        safe_text
)
myDot_Usage_strategy = st.builds(
    myDot_Usage,
)
myDot_Entity_strategy = st.builds(
    myDot_Entity,
    name=
        safe_text
)
myDot_Model_strategy = st.builds(
    myDot_Model,
)
myDot_Ref_strategy = st.builds(
    myDot_Ref,
)

@given(instance=Ref_strategy)
@settings(max_examples=50)
def test_ref_instantiation(instance):
    assert isinstance(instance, Ref)

@given(instance=myDot_EntityRef_strategy)
@settings(max_examples=50)
def test_mydot_entityref_instantiation(instance):
    assert isinstance(instance, myDot_EntityRef)

@given(instance=myDot_DotExpression_strategy)
@settings(max_examples=50)
def test_mydot_dotexpression_instantiation(instance):
    assert isinstance(instance, myDot_DotExpression)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=myDot_Reference_strategy)
@settings(max_examples=50)
def test_mydot_reference_instantiation(instance):
    assert isinstance(instance, myDot_Reference)

@given(instance=myDot_Attribute_strategy)
@settings(max_examples=50)
def test_mydot_attribute_instantiation(instance):
    assert isinstance(instance, myDot_Attribute)



@given(instance=myDot_Attribute_strategy)
def test_mydot_attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=myDot_Feature_strategy)
@settings(max_examples=50)
def test_mydot_feature_instantiation(instance):
    assert isinstance(instance, myDot_Feature)



@given(instance=myDot_Feature_strategy)
def test_mydot_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDot_Usage_strategy)
@settings(max_examples=50)
def test_mydot_usage_instantiation(instance):
    assert isinstance(instance, myDot_Usage)

@given(instance=myDot_Entity_strategy)
@settings(max_examples=50)
def test_mydot_entity_instantiation(instance):
    assert isinstance(instance, myDot_Entity)



@given(instance=myDot_Entity_strategy)
def test_mydot_entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDot_Model_strategy)
@settings(max_examples=50)
def test_mydot_model_instantiation(instance):
    assert isinstance(instance, myDot_Model)

@given(instance=myDot_Ref_strategy)
@settings(max_examples=50)
def test_mydot_ref_instantiation(instance):
    assert isinstance(instance, myDot_Ref)
