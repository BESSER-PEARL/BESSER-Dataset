import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    domainmodel::Feature,
    Type,
    domainmodel::Entity,
    domainmodel::DataType,
    domainmodel::Type,
    domainmodel::Domainmodel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_domainmodel::feature_is_not_abstract():
    assert not inspect.isabstract(domainmodel::Feature)


def test_domainmodel::feature_constructor_exists():
    assert callable(domainmodel::Feature.__init__)


def test_domainmodel::feature_constructor_args():
    sig = inspect.signature(domainmodel::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "not_" in params, "Missing parameter 'not_'"
    assert "key" in params, "Missing parameter 'key'"

def test_domainmodel::feature_has_name():
    assert hasattr(domainmodel::Feature, "name")
    descriptor = None
    for klass in domainmodel::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domainmodel::feature_has_not_():
    assert hasattr(domainmodel::Feature, "not_")
    descriptor = None
    for klass in domainmodel::Feature.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)

def test_domainmodel::feature_has_key():
    assert hasattr(domainmodel::Feature, "key")
    descriptor = None
    for klass in domainmodel::Feature.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel::entity_is_not_abstract():
    assert not inspect.isabstract(domainmodel::Entity)


def test_domainmodel::entity_constructor_exists():
    assert callable(domainmodel::Entity.__init__)


def test_domainmodel::entity_constructor_args():
    sig = inspect.signature(domainmodel::Entity.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel::datatype_is_not_abstract():
    assert not inspect.isabstract(domainmodel::DataType)


def test_domainmodel::datatype_constructor_exists():
    assert callable(domainmodel::DataType.__init__)


def test_domainmodel::datatype_constructor_args():
    sig = inspect.signature(domainmodel::DataType.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel::type_is_not_abstract():
    assert not inspect.isabstract(domainmodel::Type)


def test_domainmodel::type_constructor_exists():
    assert callable(domainmodel::Type.__init__)


def test_domainmodel::type_constructor_args():
    sig = inspect.signature(domainmodel::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_domainmodel::type_has_name():
    assert hasattr(domainmodel::Type, "name")
    descriptor = None
    for klass in domainmodel::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel::domainmodel_is_not_abstract():
    assert not inspect.isabstract(domainmodel::Domainmodel)


def test_domainmodel::domainmodel_constructor_exists():
    assert callable(domainmodel::Domainmodel.__init__)


def test_domainmodel::domainmodel_constructor_args():
    sig = inspect.signature(domainmodel::Domainmodel.__init__)
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
domainmodel::Feature_strategy = st.builds(
    domainmodel::Feature,
    name=
        safe_text,
    not_=
        safe_text,
    key=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
domainmodel::Entity_strategy = st.builds(
    domainmodel::Entity,
)
domainmodel::DataType_strategy = st.builds(
    domainmodel::DataType,
)
domainmodel::Type_strategy = st.builds(
    domainmodel::Type,
    name=
        safe_text
)
domainmodel::Domainmodel_strategy = st.builds(
    domainmodel::Domainmodel,
)

@given(instance=domainmodel::Feature_strategy)
@settings(max_examples=50)
def test_domainmodel::feature_instantiation(instance):
    assert isinstance(instance, domainmodel::Feature)

@given(instance=domainmodel::Feature_strategy)
def test_domainmodel::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domainmodel::Feature_strategy)
def test_domainmodel::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domainmodel::Feature_strategy)
def test_domainmodel::feature_not__type(instance):
    assert isinstance(instance.not_, str)


@given(instance=domainmodel::Feature_strategy)
def test_domainmodel::feature_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=domainmodel::Feature_strategy)
def test_domainmodel::feature_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=domainmodel::Feature_strategy)
def test_domainmodel::feature_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=domainmodel::Entity_strategy)
@settings(max_examples=50)
def test_domainmodel::entity_instantiation(instance):
    assert isinstance(instance, domainmodel::Entity)

@given(instance=domainmodel::DataType_strategy)
@settings(max_examples=50)
def test_domainmodel::datatype_instantiation(instance):
    assert isinstance(instance, domainmodel::DataType)

@given(instance=domainmodel::Type_strategy)
@settings(max_examples=50)
def test_domainmodel::type_instantiation(instance):
    assert isinstance(instance, domainmodel::Type)

@given(instance=domainmodel::Type_strategy)
def test_domainmodel::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=domainmodel::Type_strategy)
def test_domainmodel::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domainmodel::Domainmodel_strategy)
@settings(max_examples=50)
def test_domainmodel::domainmodel_instantiation(instance):
    assert isinstance(instance, domainmodel::Domainmodel)
