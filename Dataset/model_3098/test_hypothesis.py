import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SimpleClass::Association,
    SimpleClass::Attribute,
    Classifier,
    SimpleClass::PrimitiveDataType,
    SimpleClass::Class,
    SimpleClass::Classifier,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpleclass::association_is_not_abstract():
    assert not inspect.isabstract(SimpleClass::Association)


def test_simpleclass::association_constructor_exists():
    assert callable(SimpleClass::Association.__init__)


def test_simpleclass::association_constructor_args():
    sig = inspect.signature(SimpleClass::Association.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleclass::association_has_name():
    assert hasattr(SimpleClass::Association, "name")
    descriptor = None
    for klass in SimpleClass::Association.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleclass::attribute_is_not_abstract():
    assert not inspect.isabstract(SimpleClass::Attribute)


def test_simpleclass::attribute_constructor_exists():
    assert callable(SimpleClass::Attribute.__init__)


def test_simpleclass::attribute_constructor_args():
    sig = inspect.signature(SimpleClass::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "is_primary" in params, "Missing parameter 'is_primary'"

def test_simpleclass::attribute_has_name():
    assert hasattr(SimpleClass::Attribute, "name")
    descriptor = None
    for klass in SimpleClass::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simpleclass::attribute_has_is_primary():
    assert hasattr(SimpleClass::Attribute, "is_primary")
    descriptor = None
    for klass in SimpleClass::Attribute.__mro__:
        if "is_primary" in klass.__dict__:
            descriptor = klass.__dict__["is_primary"]
            break
    assert isinstance(descriptor, property)



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_simpleclass::primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(SimpleClass::PrimitiveDataType)


def test_simpleclass::primitivedatatype_constructor_exists():
    assert callable(SimpleClass::PrimitiveDataType.__init__)


def test_simpleclass::primitivedatatype_constructor_args():
    sig = inspect.signature(SimpleClass::PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())



def test_simpleclass::class_is_not_abstract():
    assert not inspect.isabstract(SimpleClass::Class)


def test_simpleclass::class_constructor_exists():
    assert callable(SimpleClass::Class.__init__)


def test_simpleclass::class_constructor_args():
    sig = inspect.signature(SimpleClass::Class.__init__)
    params = list(sig.parameters.keys())
    assert "is_persistent" in params, "Missing parameter 'is_persistent'"

def test_simpleclass::class_has_is_persistent():
    assert hasattr(SimpleClass::Class, "is_persistent")
    descriptor = None
    for klass in SimpleClass::Class.__mro__:
        if "is_persistent" in klass.__dict__:
            descriptor = klass.__dict__["is_persistent"]
            break
    assert isinstance(descriptor, property)



def test_simpleclass::classifier_is_not_abstract():
    assert not inspect.isabstract(SimpleClass::Classifier)


def test_simpleclass::classifier_constructor_exists():
    assert callable(SimpleClass::Classifier.__init__)


def test_simpleclass::classifier_constructor_args():
    sig = inspect.signature(SimpleClass::Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleclass::classifier_has_name():
    assert hasattr(SimpleClass::Classifier, "name")
    descriptor = None
    for klass in SimpleClass::Classifier.__mro__:
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
SimpleClass::Association_strategy = st.builds(
    SimpleClass::Association,
    name=
        safe_text
)
SimpleClass::Attribute_strategy = st.builds(
    SimpleClass::Attribute,
    name=
        safe_text,
    is_primary=
        st.booleans()
)
Classifier_strategy = st.builds(
    Classifier,
)
SimpleClass::PrimitiveDataType_strategy = st.builds(
    SimpleClass::PrimitiveDataType,
)
SimpleClass::Class_strategy = st.builds(
    SimpleClass::Class,
    is_persistent=
        st.booleans()
)
SimpleClass::Classifier_strategy = st.builds(
    SimpleClass::Classifier,
    name=
        safe_text
)

@given(instance=SimpleClass::Association_strategy)
@settings(max_examples=50)
def test_simpleclass::association_instantiation(instance):
    assert isinstance(instance, SimpleClass::Association)

@given(instance=SimpleClass::Association_strategy)
def test_simpleclass::association_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SimpleClass::Association_strategy)
def test_simpleclass::association_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimpleClass::Attribute_strategy)
@settings(max_examples=50)
def test_simpleclass::attribute_instantiation(instance):
    assert isinstance(instance, SimpleClass::Attribute)

@given(instance=SimpleClass::Attribute_strategy)
def test_simpleclass::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SimpleClass::Attribute_strategy)
def test_simpleclass::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimpleClass::Attribute_strategy)
def test_simpleclass::attribute_is_primary_type(instance):
    assert isinstance(instance.is_primary, bool)


@given(instance=SimpleClass::Attribute_strategy)
def test_simpleclass::attribute_is_primary_setter(instance):
    original = instance.is_primary
    instance.is_primary = original
    assert instance.is_primary == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=SimpleClass::PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_simpleclass::primitivedatatype_instantiation(instance):
    assert isinstance(instance, SimpleClass::PrimitiveDataType)

@given(instance=SimpleClass::Class_strategy)
@settings(max_examples=50)
def test_simpleclass::class_instantiation(instance):
    assert isinstance(instance, SimpleClass::Class)

@given(instance=SimpleClass::Class_strategy)
def test_simpleclass::class_is_persistent_type(instance):
    assert isinstance(instance.is_persistent, bool)


@given(instance=SimpleClass::Class_strategy)
def test_simpleclass::class_is_persistent_setter(instance):
    original = instance.is_persistent
    instance.is_persistent = original
    assert instance.is_persistent == original

@given(instance=SimpleClass::Classifier_strategy)
@settings(max_examples=50)
def test_simpleclass::classifier_instantiation(instance):
    assert isinstance(instance, SimpleClass::Classifier)

@given(instance=SimpleClass::Classifier_strategy)
def test_simpleclass::classifier_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SimpleClass::Classifier_strategy)
def test_simpleclass::classifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
