import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Ref,
    myDot::EntityRef,
    myDot::DotExpression,
    Feature,
    myDot::Reference,
    myDot::Attribute,
    myDot::Feature,
    myDot::Usage,
    myDot::Entity,
    myDot::Model,
    myDot::Ref,
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



def test_mydot::entityref_is_not_abstract():
    assert not inspect.isabstract(myDot::EntityRef)


def test_mydot::entityref_constructor_exists():
    assert callable(myDot::EntityRef.__init__)


def test_mydot::entityref_constructor_args():
    sig = inspect.signature(myDot::EntityRef.__init__)
    params = list(sig.parameters.keys())



def test_mydot::dotexpression_is_not_abstract():
    assert not inspect.isabstract(myDot::DotExpression)


def test_mydot::dotexpression_constructor_exists():
    assert callable(myDot::DotExpression.__init__)


def test_mydot::dotexpression_constructor_args():
    sig = inspect.signature(myDot::DotExpression.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_mydot::reference_is_not_abstract():
    assert not inspect.isabstract(myDot::Reference)


def test_mydot::reference_constructor_exists():
    assert callable(myDot::Reference.__init__)


def test_mydot::reference_constructor_args():
    sig = inspect.signature(myDot::Reference.__init__)
    params = list(sig.parameters.keys())



def test_mydot::attribute_is_not_abstract():
    assert not inspect.isabstract(myDot::Attribute)


def test_mydot::attribute_constructor_exists():
    assert callable(myDot::Attribute.__init__)


def test_mydot::attribute_constructor_args():
    sig = inspect.signature(myDot::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_mydot::attribute_has_type():
    assert hasattr(myDot::Attribute, "type")
    descriptor = None
    for klass in myDot::Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mydot::feature_is_not_abstract():
    assert not inspect.isabstract(myDot::Feature)


def test_mydot::feature_constructor_exists():
    assert callable(myDot::Feature.__init__)


def test_mydot::feature_constructor_args():
    sig = inspect.signature(myDot::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydot::feature_has_name():
    assert hasattr(myDot::Feature, "name")
    descriptor = None
    for klass in myDot::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydot::usage_is_not_abstract():
    assert not inspect.isabstract(myDot::Usage)


def test_mydot::usage_constructor_exists():
    assert callable(myDot::Usage.__init__)


def test_mydot::usage_constructor_args():
    sig = inspect.signature(myDot::Usage.__init__)
    params = list(sig.parameters.keys())



def test_mydot::entity_is_not_abstract():
    assert not inspect.isabstract(myDot::Entity)


def test_mydot::entity_constructor_exists():
    assert callable(myDot::Entity.__init__)


def test_mydot::entity_constructor_args():
    sig = inspect.signature(myDot::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydot::entity_has_name():
    assert hasattr(myDot::Entity, "name")
    descriptor = None
    for klass in myDot::Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydot::model_is_not_abstract():
    assert not inspect.isabstract(myDot::Model)


def test_mydot::model_constructor_exists():
    assert callable(myDot::Model.__init__)


def test_mydot::model_constructor_args():
    sig = inspect.signature(myDot::Model.__init__)
    params = list(sig.parameters.keys())



def test_mydot::ref_is_not_abstract():
    assert not inspect.isabstract(myDot::Ref)


def test_mydot::ref_constructor_exists():
    assert callable(myDot::Ref.__init__)


def test_mydot::ref_constructor_args():
    sig = inspect.signature(myDot::Ref.__init__)
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
myDot::EntityRef_strategy = st.builds(
    myDot::EntityRef,
)
myDot::DotExpression_strategy = st.builds(
    myDot::DotExpression,
)
Feature_strategy = st.builds(
    Feature,
)
myDot::Reference_strategy = st.builds(
    myDot::Reference,
)
myDot::Attribute_strategy = st.builds(
    myDot::Attribute,
    type=
        safe_text
)
myDot::Feature_strategy = st.builds(
    myDot::Feature,
    name=
        safe_text
)
myDot::Usage_strategy = st.builds(
    myDot::Usage,
)
myDot::Entity_strategy = st.builds(
    myDot::Entity,
    name=
        safe_text
)
myDot::Model_strategy = st.builds(
    myDot::Model,
)
myDot::Ref_strategy = st.builds(
    myDot::Ref,
)

@given(instance=Ref_strategy)
@settings(max_examples=50)
def test_ref_instantiation(instance):
    assert isinstance(instance, Ref)

@given(instance=myDot::EntityRef_strategy)
@settings(max_examples=50)
def test_mydot::entityref_instantiation(instance):
    assert isinstance(instance, myDot::EntityRef)

@given(instance=myDot::DotExpression_strategy)
@settings(max_examples=50)
def test_mydot::dotexpression_instantiation(instance):
    assert isinstance(instance, myDot::DotExpression)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=myDot::Reference_strategy)
@settings(max_examples=50)
def test_mydot::reference_instantiation(instance):
    assert isinstance(instance, myDot::Reference)

@given(instance=myDot::Attribute_strategy)
@settings(max_examples=50)
def test_mydot::attribute_instantiation(instance):
    assert isinstance(instance, myDot::Attribute)

@given(instance=myDot::Attribute_strategy)
def test_mydot::attribute_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=myDot::Attribute_strategy)
def test_mydot::attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=myDot::Feature_strategy)
@settings(max_examples=50)
def test_mydot::feature_instantiation(instance):
    assert isinstance(instance, myDot::Feature)

@given(instance=myDot::Feature_strategy)
def test_mydot::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDot::Feature_strategy)
def test_mydot::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDot::Usage_strategy)
@settings(max_examples=50)
def test_mydot::usage_instantiation(instance):
    assert isinstance(instance, myDot::Usage)

@given(instance=myDot::Entity_strategy)
@settings(max_examples=50)
def test_mydot::entity_instantiation(instance):
    assert isinstance(instance, myDot::Entity)

@given(instance=myDot::Entity_strategy)
def test_mydot::entity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDot::Entity_strategy)
def test_mydot::entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDot::Model_strategy)
@settings(max_examples=50)
def test_mydot::model_instantiation(instance):
    assert isinstance(instance, myDot::Model)

@given(instance=myDot::Ref_strategy)
@settings(max_examples=50)
def test_mydot::ref_instantiation(instance):
    assert isinstance(instance, myDot::Ref)
