import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    classdiagram_Attribute,
    classdiagram_Class,
    classdiagram_ClassDiagram,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classdiagram_attribute_is_not_abstract():
    assert not inspect.isabstract(classdiagram_Attribute)


def test_classdiagram_attribute_constructor_exists():
    assert callable(classdiagram_Attribute.__init__)


def test_classdiagram_attribute_constructor_args():
    sig = inspect.signature(classdiagram_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classdiagram_attribute_has_name():
    assert hasattr(classdiagram_Attribute, "name")
    descriptor = None
    for klass in classdiagram_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classdiagram_class_is_not_abstract():
    assert not inspect.isabstract(classdiagram_Class)


def test_classdiagram_class_constructor_exists():
    assert callable(classdiagram_Class.__init__)


def test_classdiagram_class_constructor_args():
    sig = inspect.signature(classdiagram_Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classdiagram_class_has_name():
    assert hasattr(classdiagram_Class, "name")
    descriptor = None
    for klass in classdiagram_Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classdiagram_classdiagram_is_not_abstract():
    assert not inspect.isabstract(classdiagram_ClassDiagram)


def test_classdiagram_classdiagram_constructor_exists():
    assert callable(classdiagram_ClassDiagram.__init__)


def test_classdiagram_classdiagram_constructor_args():
    sig = inspect.signature(classdiagram_ClassDiagram.__init__)
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
classdiagram_Attribute_strategy = st.builds(
    classdiagram_Attribute,
    name=
        safe_text
)
classdiagram_Class_strategy = st.builds(
    classdiagram_Class,
    name=
        safe_text
)
classdiagram_ClassDiagram_strategy = st.builds(
    classdiagram_ClassDiagram,
)

@given(instance=classdiagram_Attribute_strategy)
@settings(max_examples=50)
def test_classdiagram_attribute_instantiation(instance):
    assert isinstance(instance, classdiagram_Attribute)



@given(instance=classdiagram_Attribute_strategy)
def test_classdiagram_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classdiagram_Class_strategy)
@settings(max_examples=50)
def test_classdiagram_class_instantiation(instance):
    assert isinstance(instance, classdiagram_Class)



@given(instance=classdiagram_Class_strategy)
def test_classdiagram_class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classdiagram_ClassDiagram_strategy)
@settings(max_examples=50)
def test_classdiagram_classdiagram_instantiation(instance):
    assert isinstance(instance, classdiagram_ClassDiagram)
