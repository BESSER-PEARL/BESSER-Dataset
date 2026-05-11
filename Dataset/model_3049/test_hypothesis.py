import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Feature,
    myDsl::Reference,
    myDsl::Attribute,
    myDsl::Entity,
    myDsl::Model,
    myDsl::Feature,
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



def test_mydsl::reference_is_not_abstract():
    assert not inspect.isabstract(myDsl::Reference)


def test_mydsl::reference_constructor_exists():
    assert callable(myDsl::Reference.__init__)


def test_mydsl::reference_constructor_args():
    sig = inspect.signature(myDsl::Reference.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::attribute_is_not_abstract():
    assert not inspect.isabstract(myDsl::Attribute)


def test_mydsl::attribute_constructor_exists():
    assert callable(myDsl::Attribute.__init__)


def test_mydsl::attribute_constructor_args():
    sig = inspect.signature(myDsl::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_mydsl::attribute_has_type():
    assert hasattr(myDsl::Attribute, "type")
    descriptor = None
    for klass in myDsl::Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::entity_is_not_abstract():
    assert not inspect.isabstract(myDsl::Entity)


def test_mydsl::entity_constructor_exists():
    assert callable(myDsl::Entity.__init__)


def test_mydsl::entity_constructor_args():
    sig = inspect.signature(myDsl::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::entity_has_name():
    assert hasattr(myDsl::Entity, "name")
    descriptor = None
    for klass in myDsl::Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::model_is_not_abstract():
    assert not inspect.isabstract(myDsl::Model)


def test_mydsl::model_constructor_exists():
    assert callable(myDsl::Model.__init__)


def test_mydsl::model_constructor_args():
    sig = inspect.signature(myDsl::Model.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::feature_is_not_abstract():
    assert not inspect.isabstract(myDsl::Feature)


def test_mydsl::feature_constructor_exists():
    assert callable(myDsl::Feature.__init__)


def test_mydsl::feature_constructor_args():
    sig = inspect.signature(myDsl::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::feature_has_name():
    assert hasattr(myDsl::Feature, "name")
    descriptor = None
    for klass in myDsl::Feature.__mro__:
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
        "string",
        "int",
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
myDsl::Reference_strategy = st.builds(
    myDsl::Reference,
)
myDsl::Attribute_strategy = st.builds(
    myDsl::Attribute,
    type=
        safe_text
)
myDsl::Entity_strategy = st.builds(
    myDsl::Entity,
    name=
        safe_text
)
myDsl::Model_strategy = st.builds(
    myDsl::Model,
)
myDsl::Feature_strategy = st.builds(
    myDsl::Feature,
    name=
        safe_text
)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=myDsl::Reference_strategy)
@settings(max_examples=50)
def test_mydsl::reference_instantiation(instance):
    assert isinstance(instance, myDsl::Reference)

@given(instance=myDsl::Attribute_strategy)
@settings(max_examples=50)
def test_mydsl::attribute_instantiation(instance):
    assert isinstance(instance, myDsl::Attribute)

@given(instance=myDsl::Attribute_strategy)
def test_mydsl::attribute_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=myDsl::Attribute_strategy)
def test_mydsl::attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=myDsl::Entity_strategy)
@settings(max_examples=50)
def test_mydsl::entity_instantiation(instance):
    assert isinstance(instance, myDsl::Entity)

@given(instance=myDsl::Entity_strategy)
def test_mydsl::entity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Entity_strategy)
def test_mydsl::entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Model_strategy)
@settings(max_examples=50)
def test_mydsl::model_instantiation(instance):
    assert isinstance(instance, myDsl::Model)

@given(instance=myDsl::Feature_strategy)
@settings(max_examples=50)
def test_mydsl::feature_instantiation(instance):
    assert isinstance(instance, myDsl::Feature)

@given(instance=myDsl::Feature_strategy)
def test_mydsl::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Feature_strategy)
def test_mydsl::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
