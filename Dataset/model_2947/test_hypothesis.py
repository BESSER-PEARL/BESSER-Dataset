import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    slolpBPM::Feature,
    Type,
    slolpBPM::Entity,
    slolpBPM::Datatype,
    slolpBPM::Type,
    slolpBPM::DomainModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_slolpbpm::feature_is_not_abstract():
    assert not inspect.isabstract(slolpBPM::Feature)


def test_slolpbpm::feature_constructor_exists():
    assert callable(slolpBPM::Feature.__init__)


def test_slolpbpm::feature_constructor_args():
    sig = inspect.signature(slolpBPM::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"
    assert "name" in params, "Missing parameter 'name'"

def test_slolpbpm::feature_has_many():
    assert hasattr(slolpBPM::Feature, "many")
    descriptor = None
    for klass in slolpBPM::Feature.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_slolpbpm::feature_has_name():
    assert hasattr(slolpBPM::Feature, "name")
    descriptor = None
    for klass in slolpBPM::Feature.__mro__:
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



def test_slolpbpm::entity_is_not_abstract():
    assert not inspect.isabstract(slolpBPM::Entity)


def test_slolpbpm::entity_constructor_exists():
    assert callable(slolpBPM::Entity.__init__)


def test_slolpbpm::entity_constructor_args():
    sig = inspect.signature(slolpBPM::Entity.__init__)
    params = list(sig.parameters.keys())



def test_slolpbpm::datatype_is_not_abstract():
    assert not inspect.isabstract(slolpBPM::Datatype)


def test_slolpbpm::datatype_constructor_exists():
    assert callable(slolpBPM::Datatype.__init__)


def test_slolpbpm::datatype_constructor_args():
    sig = inspect.signature(slolpBPM::Datatype.__init__)
    params = list(sig.parameters.keys())



def test_slolpbpm::type_is_not_abstract():
    assert not inspect.isabstract(slolpBPM::Type)


def test_slolpbpm::type_constructor_exists():
    assert callable(slolpBPM::Type.__init__)


def test_slolpbpm::type_constructor_args():
    sig = inspect.signature(slolpBPM::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_slolpbpm::type_has_name():
    assert hasattr(slolpBPM::Type, "name")
    descriptor = None
    for klass in slolpBPM::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_slolpbpm::domainmodel_is_not_abstract():
    assert not inspect.isabstract(slolpBPM::DomainModel)


def test_slolpbpm::domainmodel_constructor_exists():
    assert callable(slolpBPM::DomainModel.__init__)


def test_slolpbpm::domainmodel_constructor_args():
    sig = inspect.signature(slolpBPM::DomainModel.__init__)
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
slolpBPM::Feature_strategy = st.builds(
    slolpBPM::Feature,
    many=
        st.booleans(),
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
slolpBPM::Entity_strategy = st.builds(
    slolpBPM::Entity,
)
slolpBPM::Datatype_strategy = st.builds(
    slolpBPM::Datatype,
)
slolpBPM::Type_strategy = st.builds(
    slolpBPM::Type,
    name=
        safe_text
)
slolpBPM::DomainModel_strategy = st.builds(
    slolpBPM::DomainModel,
)

@given(instance=slolpBPM::Feature_strategy)
@settings(max_examples=50)
def test_slolpbpm::feature_instantiation(instance):
    assert isinstance(instance, slolpBPM::Feature)

@given(instance=slolpBPM::Feature_strategy)
def test_slolpbpm::feature_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=slolpBPM::Feature_strategy)
def test_slolpbpm::feature_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=slolpBPM::Feature_strategy)
def test_slolpbpm::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=slolpBPM::Feature_strategy)
def test_slolpbpm::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=slolpBPM::Entity_strategy)
@settings(max_examples=50)
def test_slolpbpm::entity_instantiation(instance):
    assert isinstance(instance, slolpBPM::Entity)

@given(instance=slolpBPM::Datatype_strategy)
@settings(max_examples=50)
def test_slolpbpm::datatype_instantiation(instance):
    assert isinstance(instance, slolpBPM::Datatype)

@given(instance=slolpBPM::Type_strategy)
@settings(max_examples=50)
def test_slolpbpm::type_instantiation(instance):
    assert isinstance(instance, slolpBPM::Type)

@given(instance=slolpBPM::Type_strategy)
def test_slolpbpm::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=slolpBPM::Type_strategy)
def test_slolpbpm::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=slolpBPM::DomainModel_strategy)
@settings(max_examples=50)
def test_slolpbpm::domainmodel_instantiation(instance):
    assert isinstance(instance, slolpBPM::DomainModel)
