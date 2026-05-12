import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    slolpBPM_Feature,
    Type,
    slolpBPM_Entity,
    slolpBPM_Datatype,
    slolpBPM_Type,
    slolpBPM_DomainModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_slolpbpm_feature_is_not_abstract():
    assert not inspect.isabstract(slolpBPM_Feature)


def test_slolpbpm_feature_constructor_exists():
    assert callable(slolpBPM_Feature.__init__)


def test_slolpbpm_feature_constructor_args():
    sig = inspect.signature(slolpBPM_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"
    assert "name" in params, "Missing parameter 'name'"

def test_slolpbpm_feature_has_many():
    assert hasattr(slolpBPM_Feature, "many")
    descriptor = None
    for klass in slolpBPM_Feature.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_slolpbpm_feature_has_name():
    assert hasattr(slolpBPM_Feature, "name")
    descriptor = None
    for klass in slolpBPM_Feature.__mro__:
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



def test_slolpbpm_entity_is_not_abstract():
    assert not inspect.isabstract(slolpBPM_Entity)


def test_slolpbpm_entity_constructor_exists():
    assert callable(slolpBPM_Entity.__init__)


def test_slolpbpm_entity_constructor_args():
    sig = inspect.signature(slolpBPM_Entity.__init__)
    params = list(sig.parameters.keys())



def test_slolpbpm_datatype_is_not_abstract():
    assert not inspect.isabstract(slolpBPM_Datatype)


def test_slolpbpm_datatype_constructor_exists():
    assert callable(slolpBPM_Datatype.__init__)


def test_slolpbpm_datatype_constructor_args():
    sig = inspect.signature(slolpBPM_Datatype.__init__)
    params = list(sig.parameters.keys())



def test_slolpbpm_type_is_not_abstract():
    assert not inspect.isabstract(slolpBPM_Type)


def test_slolpbpm_type_constructor_exists():
    assert callable(slolpBPM_Type.__init__)


def test_slolpbpm_type_constructor_args():
    sig = inspect.signature(slolpBPM_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_slolpbpm_type_has_name():
    assert hasattr(slolpBPM_Type, "name")
    descriptor = None
    for klass in slolpBPM_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_slolpbpm_domainmodel_is_not_abstract():
    assert not inspect.isabstract(slolpBPM_DomainModel)


def test_slolpbpm_domainmodel_constructor_exists():
    assert callable(slolpBPM_DomainModel.__init__)


def test_slolpbpm_domainmodel_constructor_args():
    sig = inspect.signature(slolpBPM_DomainModel.__init__)
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
slolpBPM_Feature_strategy = st.builds(
    slolpBPM_Feature,
    many=
        st.booleans(),
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
slolpBPM_Entity_strategy = st.builds(
    slolpBPM_Entity,
)
slolpBPM_Datatype_strategy = st.builds(
    slolpBPM_Datatype,
)
slolpBPM_Type_strategy = st.builds(
    slolpBPM_Type,
    name=
        safe_text
)
slolpBPM_DomainModel_strategy = st.builds(
    slolpBPM_DomainModel,
)

@given(instance=slolpBPM_Feature_strategy)
@settings(max_examples=50)
def test_slolpbpm_feature_instantiation(instance):
    assert isinstance(instance, slolpBPM_Feature)



@given(instance=slolpBPM_Feature_strategy)
def test_slolpbpm_feature_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original



@given(instance=slolpBPM_Feature_strategy)
def test_slolpbpm_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=slolpBPM_Entity_strategy)
@settings(max_examples=50)
def test_slolpbpm_entity_instantiation(instance):
    assert isinstance(instance, slolpBPM_Entity)

@given(instance=slolpBPM_Datatype_strategy)
@settings(max_examples=50)
def test_slolpbpm_datatype_instantiation(instance):
    assert isinstance(instance, slolpBPM_Datatype)

@given(instance=slolpBPM_Type_strategy)
@settings(max_examples=50)
def test_slolpbpm_type_instantiation(instance):
    assert isinstance(instance, slolpBPM_Type)



@given(instance=slolpBPM_Type_strategy)
def test_slolpbpm_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=slolpBPM_DomainModel_strategy)
@settings(max_examples=50)
def test_slolpbpm_domainmodel_instantiation(instance):
    assert isinstance(instance, slolpBPM_DomainModel)
