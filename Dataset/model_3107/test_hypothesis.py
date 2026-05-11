import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    source::ClassDiagram,
    source::PrimitiveDataType,
    source::Association,
    source::Attribute,
    source::Class,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_source::classdiagram_is_not_abstract():
    assert not inspect.isabstract(source::ClassDiagram)


def test_source::classdiagram_constructor_exists():
    assert callable(source::ClassDiagram.__init__)


def test_source::classdiagram_constructor_args():
    sig = inspect.signature(source::ClassDiagram.__init__)
    params = list(sig.parameters.keys())



def test_source::primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(source::PrimitiveDataType)


def test_source::primitivedatatype_constructor_exists():
    assert callable(source::PrimitiveDataType.__init__)


def test_source::primitivedatatype_constructor_args():
    sig = inspect.signature(source::PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_source::primitivedatatype_has_name():
    assert hasattr(source::PrimitiveDataType, "name")
    descriptor = None
    for klass in source::PrimitiveDataType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_source::association_is_not_abstract():
    assert not inspect.isabstract(source::Association)


def test_source::association_constructor_exists():
    assert callable(source::Association.__init__)


def test_source::association_constructor_args():
    sig = inspect.signature(source::Association.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "leftMultiplicity" in params, "Missing parameter 'leftMultiplicity'"

def test_source::association_has_name():
    assert hasattr(source::Association, "name")
    descriptor = None
    for klass in source::Association.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_source::association_has_leftMultiplicity():
    assert hasattr(source::Association, "leftMultiplicity")
    descriptor = None
    for klass in source::Association.__mro__:
        if "leftMultiplicity" in klass.__dict__:
            descriptor = klass.__dict__["leftMultiplicity"]
            break
    assert isinstance(descriptor, property)



def test_source::attribute_is_not_abstract():
    assert not inspect.isabstract(source::Attribute)


def test_source::attribute_constructor_exists():
    assert callable(source::Attribute.__init__)


def test_source::attribute_constructor_args():
    sig = inspect.signature(source::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "is_primary" in params, "Missing parameter 'is_primary'"

def test_source::attribute_has_name():
    assert hasattr(source::Attribute, "name")
    descriptor = None
    for klass in source::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_source::attribute_has_is_primary():
    assert hasattr(source::Attribute, "is_primary")
    descriptor = None
    for klass in source::Attribute.__mro__:
        if "is_primary" in klass.__dict__:
            descriptor = klass.__dict__["is_primary"]
            break
    assert isinstance(descriptor, property)



def test_source::class_is_not_abstract():
    assert not inspect.isabstract(source::Class)


def test_source::class_constructor_exists():
    assert callable(source::Class.__init__)


def test_source::class_constructor_args():
    sig = inspect.signature(source::Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_source::class_has_name():
    assert hasattr(source::Class, "name")
    descriptor = None
    for klass in source::Class.__mro__:
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
source::ClassDiagram_strategy = st.builds(
    source::ClassDiagram,
)
source::PrimitiveDataType_strategy = st.builds(
    source::PrimitiveDataType,
    name=
        safe_text
)
source::Association_strategy = st.builds(
    source::Association,
    name=
        safe_text,
    leftMultiplicity=
        st.integers()
)
source::Attribute_strategy = st.builds(
    source::Attribute,
    name=
        safe_text,
    is_primary=
        st.booleans()
)
source::Class_strategy = st.builds(
    source::Class,
    name=
        safe_text
)

@given(instance=source::ClassDiagram_strategy)
@settings(max_examples=50)
def test_source::classdiagram_instantiation(instance):
    assert isinstance(instance, source::ClassDiagram)

@given(instance=source::PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_source::primitivedatatype_instantiation(instance):
    assert isinstance(instance, source::PrimitiveDataType)

@given(instance=source::PrimitiveDataType_strategy)
def test_source::primitivedatatype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=source::PrimitiveDataType_strategy)
def test_source::primitivedatatype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=source::Association_strategy)
@settings(max_examples=50)
def test_source::association_instantiation(instance):
    assert isinstance(instance, source::Association)

@given(instance=source::Association_strategy)
def test_source::association_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=source::Association_strategy)
def test_source::association_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=source::Association_strategy)
def test_source::association_leftMultiplicity_type(instance):
    assert isinstance(instance.leftMultiplicity, int)


@given(instance=source::Association_strategy)
def test_source::association_leftMultiplicity_setter(instance):
    original = instance.leftMultiplicity
    instance.leftMultiplicity = original
    assert instance.leftMultiplicity == original

@given(instance=source::Attribute_strategy)
@settings(max_examples=50)
def test_source::attribute_instantiation(instance):
    assert isinstance(instance, source::Attribute)

@given(instance=source::Attribute_strategy)
def test_source::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=source::Attribute_strategy)
def test_source::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=source::Attribute_strategy)
def test_source::attribute_is_primary_type(instance):
    assert isinstance(instance.is_primary, bool)


@given(instance=source::Attribute_strategy)
def test_source::attribute_is_primary_setter(instance):
    original = instance.is_primary
    instance.is_primary = original
    assert instance.is_primary == original

@given(instance=source::Class_strategy)
@settings(max_examples=50)
def test_source::class_instantiation(instance):
    assert isinstance(instance, source::Class)

@given(instance=source::Class_strategy)
def test_source::class_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=source::Class_strategy)
def test_source::class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
