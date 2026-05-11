import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    myDsl::Features,
    Type,
    myDsl::Entity,
    myDsl::DataType,
    myDsl::Type,
    myDsl::DomainModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl::features_is_not_abstract():
    assert not inspect.isabstract(myDsl::Features)


def test_mydsl::features_constructor_exists():
    assert callable(myDsl::Features.__init__)


def test_mydsl::features_constructor_args():
    sig = inspect.signature(myDsl::Features.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::features_has_name():
    assert hasattr(myDsl::Features, "name")
    descriptor = None
    for klass in myDsl::Features.__mro__:
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



def test_mydsl::entity_is_not_abstract():
    assert not inspect.isabstract(myDsl::Entity)


def test_mydsl::entity_constructor_exists():
    assert callable(myDsl::Entity.__init__)


def test_mydsl::entity_constructor_args():
    sig = inspect.signature(myDsl::Entity.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::datatype_is_not_abstract():
    assert not inspect.isabstract(myDsl::DataType)


def test_mydsl::datatype_constructor_exists():
    assert callable(myDsl::DataType.__init__)


def test_mydsl::datatype_constructor_args():
    sig = inspect.signature(myDsl::DataType.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::type_is_not_abstract():
    assert not inspect.isabstract(myDsl::Type)


def test_mydsl::type_constructor_exists():
    assert callable(myDsl::Type.__init__)


def test_mydsl::type_constructor_args():
    sig = inspect.signature(myDsl::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::type_has_name():
    assert hasattr(myDsl::Type, "name")
    descriptor = None
    for klass in myDsl::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::domainmodel_is_not_abstract():
    assert not inspect.isabstract(myDsl::DomainModel)


def test_mydsl::domainmodel_constructor_exists():
    assert callable(myDsl::DomainModel.__init__)


def test_mydsl::domainmodel_constructor_args():
    sig = inspect.signature(myDsl::DomainModel.__init__)
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
myDsl::Features_strategy = st.builds(
    myDsl::Features,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
myDsl::Entity_strategy = st.builds(
    myDsl::Entity,
)
myDsl::DataType_strategy = st.builds(
    myDsl::DataType,
)
myDsl::Type_strategy = st.builds(
    myDsl::Type,
    name=
        safe_text
)
myDsl::DomainModel_strategy = st.builds(
    myDsl::DomainModel,
)

@given(instance=myDsl::Features_strategy)
@settings(max_examples=50)
def test_mydsl::features_instantiation(instance):
    assert isinstance(instance, myDsl::Features)

@given(instance=myDsl::Features_strategy)
def test_mydsl::features_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Features_strategy)
def test_mydsl::features_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=myDsl::Entity_strategy)
@settings(max_examples=50)
def test_mydsl::entity_instantiation(instance):
    assert isinstance(instance, myDsl::Entity)

@given(instance=myDsl::DataType_strategy)
@settings(max_examples=50)
def test_mydsl::datatype_instantiation(instance):
    assert isinstance(instance, myDsl::DataType)

@given(instance=myDsl::Type_strategy)
@settings(max_examples=50)
def test_mydsl::type_instantiation(instance):
    assert isinstance(instance, myDsl::Type)

@given(instance=myDsl::Type_strategy)
def test_mydsl::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Type_strategy)
def test_mydsl::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::DomainModel_strategy)
@settings(max_examples=50)
def test_mydsl::domainmodel_instantiation(instance):
    assert isinstance(instance, myDsl::DomainModel)
