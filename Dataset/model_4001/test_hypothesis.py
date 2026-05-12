import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    classes_Reference,
    classes_Attribute,
    classes_Class,
    classes_ClassDiagram,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classes_reference_is_not_abstract():
    assert not inspect.isabstract(classes_Reference)


def test_classes_reference_constructor_exists():
    assert callable(classes_Reference.__init__)


def test_classes_reference_constructor_args():
    sig = inspect.signature(classes_Reference.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classes_reference_has_name():
    assert hasattr(classes_Reference, "name")
    descriptor = None
    for klass in classes_Reference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classes_attribute_is_not_abstract():
    assert not inspect.isabstract(classes_Attribute)


def test_classes_attribute_constructor_exists():
    assert callable(classes_Attribute.__init__)


def test_classes_attribute_constructor_args():
    sig = inspect.signature(classes_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_classes_attribute_has_type():
    assert hasattr(classes_Attribute, "type")
    descriptor = None
    for klass in classes_Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_classes_attribute_has_name():
    assert hasattr(classes_Attribute, "name")
    descriptor = None
    for klass in classes_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classes_class_is_not_abstract():
    assert not inspect.isabstract(classes_Class)


def test_classes_class_constructor_exists():
    assert callable(classes_Class.__init__)


def test_classes_class_constructor_args():
    sig = inspect.signature(classes_Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classes_class_has_name():
    assert hasattr(classes_Class, "name")
    descriptor = None
    for klass in classes_Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classes_classdiagram_is_not_abstract():
    assert not inspect.isabstract(classes_ClassDiagram)


def test_classes_classdiagram_constructor_exists():
    assert callable(classes_ClassDiagram.__init__)


def test_classes_classdiagram_constructor_args():
    sig = inspect.signature(classes_ClassDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classes_classdiagram_has_name():
    assert hasattr(classes_ClassDiagram, "name")
    descriptor = None
    for klass in classes_ClassDiagram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "datetime",
        "string",
        "integer",
        "bool",
        "float",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"


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
classes_Reference_strategy = st.builds(
    classes_Reference,
    name=
        safe_text
)
classes_Attribute_strategy = st.builds(
    classes_Attribute,
    type=
        safe_text,
    name=
        safe_text
)
classes_Class_strategy = st.builds(
    classes_Class,
    name=
        safe_text
)
classes_ClassDiagram_strategy = st.builds(
    classes_ClassDiagram,
    name=
        safe_text
)

@given(instance=classes_Reference_strategy)
@settings(max_examples=50)
def test_classes_reference_instantiation(instance):
    assert isinstance(instance, classes_Reference)



@given(instance=classes_Reference_strategy)
def test_classes_reference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classes_Attribute_strategy)
@settings(max_examples=50)
def test_classes_attribute_instantiation(instance):
    assert isinstance(instance, classes_Attribute)



@given(instance=classes_Attribute_strategy)
def test_classes_attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=classes_Attribute_strategy)
def test_classes_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classes_Class_strategy)
@settings(max_examples=50)
def test_classes_class_instantiation(instance):
    assert isinstance(instance, classes_Class)



@given(instance=classes_Class_strategy)
def test_classes_class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classes_ClassDiagram_strategy)
@settings(max_examples=50)
def test_classes_classdiagram_instantiation(instance):
    assert isinstance(instance, classes_ClassDiagram)



@given(instance=classes_ClassDiagram_strategy)
def test_classes_classdiagram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
