import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    myDsl_Features,
    Type,
    myDsl_Entity,
    myDsl_DataType,
    myDsl_Type,
    myDsl_DomainModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl_features_is_not_abstract():
    assert not inspect.isabstract(myDsl_Features)


def test_mydsl_features_constructor_exists():
    assert callable(myDsl_Features.__init__)


def test_mydsl_features_constructor_args():
    sig = inspect.signature(myDsl_Features.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_features_has_name():
    assert hasattr(myDsl_Features, "name")
    descriptor = None
    for klass in myDsl_Features.__mro__:
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



def test_mydsl_entity_is_not_abstract():
    assert not inspect.isabstract(myDsl_Entity)


def test_mydsl_entity_constructor_exists():
    assert callable(myDsl_Entity.__init__)


def test_mydsl_entity_constructor_args():
    sig = inspect.signature(myDsl_Entity.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_datatype_is_not_abstract():
    assert not inspect.isabstract(myDsl_DataType)


def test_mydsl_datatype_constructor_exists():
    assert callable(myDsl_DataType.__init__)


def test_mydsl_datatype_constructor_args():
    sig = inspect.signature(myDsl_DataType.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_type_is_not_abstract():
    assert not inspect.isabstract(myDsl_Type)


def test_mydsl_type_constructor_exists():
    assert callable(myDsl_Type.__init__)


def test_mydsl_type_constructor_args():
    sig = inspect.signature(myDsl_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_type_has_name():
    assert hasattr(myDsl_Type, "name")
    descriptor = None
    for klass in myDsl_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_domainmodel_is_not_abstract():
    assert not inspect.isabstract(myDsl_DomainModel)


def test_mydsl_domainmodel_constructor_exists():
    assert callable(myDsl_DomainModel.__init__)


def test_mydsl_domainmodel_constructor_args():
    sig = inspect.signature(myDsl_DomainModel.__init__)
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
myDsl_Features_strategy = st.builds(
    myDsl_Features,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
myDsl_Entity_strategy = st.builds(
    myDsl_Entity,
)
myDsl_DataType_strategy = st.builds(
    myDsl_DataType,
)
myDsl_Type_strategy = st.builds(
    myDsl_Type,
    name=
        safe_text
)
myDsl_DomainModel_strategy = st.builds(
    myDsl_DomainModel,
)

@given(instance=myDsl_Features_strategy)
@settings(max_examples=50)
def test_mydsl_features_instantiation(instance):
    assert isinstance(instance, myDsl_Features)



@given(instance=myDsl_Features_strategy)
def test_mydsl_features_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=myDsl_Entity_strategy)
@settings(max_examples=50)
def test_mydsl_entity_instantiation(instance):
    assert isinstance(instance, myDsl_Entity)

@given(instance=myDsl_DataType_strategy)
@settings(max_examples=50)
def test_mydsl_datatype_instantiation(instance):
    assert isinstance(instance, myDsl_DataType)

@given(instance=myDsl_Type_strategy)
@settings(max_examples=50)
def test_mydsl_type_instantiation(instance):
    assert isinstance(instance, myDsl_Type)



@given(instance=myDsl_Type_strategy)
def test_mydsl_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_DomainModel_strategy)
@settings(max_examples=50)
def test_mydsl_domainmodel_instantiation(instance):
    assert isinstance(instance, myDsl_DomainModel)
