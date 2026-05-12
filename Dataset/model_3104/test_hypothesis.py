import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    source_ClassDiagram,
    source_PrimitiveDataType,
    source_Association,
    source_Attribute,
    source_Class,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_source_classdiagram_is_not_abstract():
    assert not inspect.isabstract(source_ClassDiagram)


def test_source_classdiagram_constructor_exists():
    assert callable(source_ClassDiagram.__init__)


def test_source_classdiagram_constructor_args():
    sig = inspect.signature(source_ClassDiagram.__init__)
    params = list(sig.parameters.keys())



def test_source_primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(source_PrimitiveDataType)


def test_source_primitivedatatype_constructor_exists():
    assert callable(source_PrimitiveDataType.__init__)


def test_source_primitivedatatype_constructor_args():
    sig = inspect.signature(source_PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_source_primitivedatatype_has_name():
    assert hasattr(source_PrimitiveDataType, "name")
    descriptor = None
    for klass in source_PrimitiveDataType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_source_association_is_not_abstract():
    assert not inspect.isabstract(source_Association)


def test_source_association_constructor_exists():
    assert callable(source_Association.__init__)


def test_source_association_constructor_args():
    sig = inspect.signature(source_Association.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_source_association_has_name():
    assert hasattr(source_Association, "name")
    descriptor = None
    for klass in source_Association.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_source_attribute_is_not_abstract():
    assert not inspect.isabstract(source_Attribute)


def test_source_attribute_constructor_exists():
    assert callable(source_Attribute.__init__)


def test_source_attribute_constructor_args():
    sig = inspect.signature(source_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "is_primary" in params, "Missing parameter 'is_primary'"
    assert "name" in params, "Missing parameter 'name'"

def test_source_attribute_has_is_primary():
    assert hasattr(source_Attribute, "is_primary")
    descriptor = None
    for klass in source_Attribute.__mro__:
        if "is_primary" in klass.__dict__:
            descriptor = klass.__dict__["is_primary"]
            break
    assert isinstance(descriptor, property)

def test_source_attribute_has_name():
    assert hasattr(source_Attribute, "name")
    descriptor = None
    for klass in source_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_source_class_is_not_abstract():
    assert not inspect.isabstract(source_Class)


def test_source_class_constructor_exists():
    assert callable(source_Class.__init__)


def test_source_class_constructor_args():
    sig = inspect.signature(source_Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_source_class_has_name():
    assert hasattr(source_Class, "name")
    descriptor = None
    for klass in source_Class.__mro__:
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
source_ClassDiagram_strategy = st.builds(
    source_ClassDiagram,
)
source_PrimitiveDataType_strategy = st.builds(
    source_PrimitiveDataType,
    name=
        safe_text
)
source_Association_strategy = st.builds(
    source_Association,
    name=
        safe_text
)
source_Attribute_strategy = st.builds(
    source_Attribute,
    is_primary=
        st.booleans(),
    name=
        safe_text
)
source_Class_strategy = st.builds(
    source_Class,
    name=
        safe_text
)

@given(instance=source_ClassDiagram_strategy)
@settings(max_examples=50)
def test_source_classdiagram_instantiation(instance):
    assert isinstance(instance, source_ClassDiagram)

@given(instance=source_PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_source_primitivedatatype_instantiation(instance):
    assert isinstance(instance, source_PrimitiveDataType)



@given(instance=source_PrimitiveDataType_strategy)
def test_source_primitivedatatype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=source_Association_strategy)
@settings(max_examples=50)
def test_source_association_instantiation(instance):
    assert isinstance(instance, source_Association)



@given(instance=source_Association_strategy)
def test_source_association_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=source_Attribute_strategy)
@settings(max_examples=50)
def test_source_attribute_instantiation(instance):
    assert isinstance(instance, source_Attribute)



@given(instance=source_Attribute_strategy)
def test_source_attribute_is_primary_setter(instance):
    original = instance.is_primary
    instance.is_primary = original
    assert instance.is_primary == original



@given(instance=source_Attribute_strategy)
def test_source_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=source_Class_strategy)
@settings(max_examples=50)
def test_source_class_instantiation(instance):
    assert isinstance(instance, source_Class)



@given(instance=source_Class_strategy)
def test_source_class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
