import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    entity_Feature,
    Type,
    entity_Entity,
    entity_Datatype,
    entity_Type,
    entity_Domain,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_entity_feature_is_not_abstract():
    assert not inspect.isabstract(entity_Feature)


def test_entity_feature_constructor_exists():
    assert callable(entity_Feature.__init__)


def test_entity_feature_constructor_args():
    sig = inspect.signature(entity_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entity_feature_has_name():
    assert hasattr(entity_Feature, "name")
    descriptor = None
    for klass in entity_Feature.__mro__:
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



def test_entity_entity_is_not_abstract():
    assert not inspect.isabstract(entity_Entity)


def test_entity_entity_constructor_exists():
    assert callable(entity_Entity.__init__)


def test_entity_entity_constructor_args():
    sig = inspect.signature(entity_Entity.__init__)
    params = list(sig.parameters.keys())



def test_entity_datatype_is_not_abstract():
    assert not inspect.isabstract(entity_Datatype)


def test_entity_datatype_constructor_exists():
    assert callable(entity_Datatype.__init__)


def test_entity_datatype_constructor_args():
    sig = inspect.signature(entity_Datatype.__init__)
    params = list(sig.parameters.keys())



def test_entity_type_is_not_abstract():
    assert not inspect.isabstract(entity_Type)


def test_entity_type_constructor_exists():
    assert callable(entity_Type.__init__)


def test_entity_type_constructor_args():
    sig = inspect.signature(entity_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entity_type_has_name():
    assert hasattr(entity_Type, "name")
    descriptor = None
    for klass in entity_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entity_domain_is_not_abstract():
    assert not inspect.isabstract(entity_Domain)


def test_entity_domain_constructor_exists():
    assert callable(entity_Domain.__init__)


def test_entity_domain_constructor_args():
    sig = inspect.signature(entity_Domain.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_entity_domain_has_name():
    assert hasattr(entity_Domain, "name")
    descriptor = None
    for klass in entity_Domain.__mro__:
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
entity_Feature_strategy = st.builds(
    entity_Feature,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
entity_Entity_strategy = st.builds(
    entity_Entity,
)
entity_Datatype_strategy = st.builds(
    entity_Datatype,
)
entity_Type_strategy = st.builds(
    entity_Type,
    name=
        safe_text
)
entity_Domain_strategy = st.builds(
    entity_Domain,
    name=
        safe_text
)

@given(instance=entity_Feature_strategy)
@settings(max_examples=50)
def test_entity_feature_instantiation(instance):
    assert isinstance(instance, entity_Feature)



@given(instance=entity_Feature_strategy)
def test_entity_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=entity_Entity_strategy)
@settings(max_examples=50)
def test_entity_entity_instantiation(instance):
    assert isinstance(instance, entity_Entity)

@given(instance=entity_Datatype_strategy)
@settings(max_examples=50)
def test_entity_datatype_instantiation(instance):
    assert isinstance(instance, entity_Datatype)

@given(instance=entity_Type_strategy)
@settings(max_examples=50)
def test_entity_type_instantiation(instance):
    assert isinstance(instance, entity_Type)



@given(instance=entity_Type_strategy)
def test_entity_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=entity_Domain_strategy)
@settings(max_examples=50)
def test_entity_domain_instantiation(instance):
    assert isinstance(instance, entity_Domain)



@given(instance=entity_Domain_strategy)
def test_entity_domain_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
