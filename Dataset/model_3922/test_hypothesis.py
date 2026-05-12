import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    myDsl_Property,
    Type,
    myDsl_Entity,
    myDsl_SimpleType,
    myDsl_Type,
    myDsl_Import,
    myDsl_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl_property_is_not_abstract():
    assert not inspect.isabstract(myDsl_Property)


def test_mydsl_property_constructor_exists():
    assert callable(myDsl_Property.__init__)


def test_mydsl_property_constructor_args():
    sig = inspect.signature(myDsl_Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "many" in params, "Missing parameter 'many'"

def test_mydsl_property_has_name():
    assert hasattr(myDsl_Property, "name")
    descriptor = None
    for klass in myDsl_Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_property_has_many():
    assert hasattr(myDsl_Property, "many")
    descriptor = None
    for klass in myDsl_Property.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
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



def test_mydsl_simpletype_is_not_abstract():
    assert not inspect.isabstract(myDsl_SimpleType)


def test_mydsl_simpletype_constructor_exists():
    assert callable(myDsl_SimpleType.__init__)


def test_mydsl_simpletype_constructor_args():
    sig = inspect.signature(myDsl_SimpleType.__init__)
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



def test_mydsl_import_is_not_abstract():
    assert not inspect.isabstract(myDsl_Import)


def test_mydsl_import_constructor_exists():
    assert callable(myDsl_Import.__init__)


def test_mydsl_import_constructor_args():
    sig = inspect.signature(myDsl_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_mydsl_import_has_importURI():
    assert hasattr(myDsl_Import, "importURI")
    descriptor = None
    for klass in myDsl_Import.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_model_is_not_abstract():
    assert not inspect.isabstract(myDsl_Model)


def test_mydsl_model_constructor_exists():
    assert callable(myDsl_Model.__init__)


def test_mydsl_model_constructor_args():
    sig = inspect.signature(myDsl_Model.__init__)
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
myDsl_Property_strategy = st.builds(
    myDsl_Property,
    name=
        safe_text,
    many=
        st.booleans()
)
Type_strategy = st.builds(
    Type,
)
myDsl_Entity_strategy = st.builds(
    myDsl_Entity,
)
myDsl_SimpleType_strategy = st.builds(
    myDsl_SimpleType,
)
myDsl_Type_strategy = st.builds(
    myDsl_Type,
    name=
        safe_text
)
myDsl_Import_strategy = st.builds(
    myDsl_Import,
    importURI=
        safe_text
)
myDsl_Model_strategy = st.builds(
    myDsl_Model,
)

@given(instance=myDsl_Property_strategy)
@settings(max_examples=50)
def test_mydsl_property_instantiation(instance):
    assert isinstance(instance, myDsl_Property)



@given(instance=myDsl_Property_strategy)
def test_mydsl_property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=myDsl_Property_strategy)
def test_mydsl_property_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=myDsl_Entity_strategy)
@settings(max_examples=50)
def test_mydsl_entity_instantiation(instance):
    assert isinstance(instance, myDsl_Entity)

@given(instance=myDsl_SimpleType_strategy)
@settings(max_examples=50)
def test_mydsl_simpletype_instantiation(instance):
    assert isinstance(instance, myDsl_SimpleType)

@given(instance=myDsl_Type_strategy)
@settings(max_examples=50)
def test_mydsl_type_instantiation(instance):
    assert isinstance(instance, myDsl_Type)



@given(instance=myDsl_Type_strategy)
def test_mydsl_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Import_strategy)
@settings(max_examples=50)
def test_mydsl_import_instantiation(instance):
    assert isinstance(instance, myDsl_Import)



@given(instance=myDsl_Import_strategy)
def test_mydsl_import_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=myDsl_Model_strategy)
@settings(max_examples=50)
def test_mydsl_model_instantiation(instance):
    assert isinstance(instance, myDsl_Model)
