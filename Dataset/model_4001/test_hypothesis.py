import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    classes::Reference,
    classes::Attribute,
    classes::Class,
    classes::ClassDiagram,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classes::reference_is_not_abstract():
    assert not inspect.isabstract(classes::Reference)


def test_classes::reference_constructor_exists():
    assert callable(classes::Reference.__init__)


def test_classes::reference_constructor_args():
    sig = inspect.signature(classes::Reference.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classes::reference_has_name():
    assert hasattr(classes::Reference, "name")
    descriptor = None
    for klass in classes::Reference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classes::attribute_is_not_abstract():
    assert not inspect.isabstract(classes::Attribute)


def test_classes::attribute_constructor_exists():
    assert callable(classes::Attribute.__init__)


def test_classes::attribute_constructor_args():
    sig = inspect.signature(classes::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_classes::attribute_has_type():
    assert hasattr(classes::Attribute, "type")
    descriptor = None
    for klass in classes::Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_classes::attribute_has_name():
    assert hasattr(classes::Attribute, "name")
    descriptor = None
    for klass in classes::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classes::class_is_not_abstract():
    assert not inspect.isabstract(classes::Class)


def test_classes::class_constructor_exists():
    assert callable(classes::Class.__init__)


def test_classes::class_constructor_args():
    sig = inspect.signature(classes::Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classes::class_has_name():
    assert hasattr(classes::Class, "name")
    descriptor = None
    for klass in classes::Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classes::classdiagram_is_not_abstract():
    assert not inspect.isabstract(classes::ClassDiagram)


def test_classes::classdiagram_constructor_exists():
    assert callable(classes::ClassDiagram.__init__)


def test_classes::classdiagram_constructor_args():
    sig = inspect.signature(classes::ClassDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classes::classdiagram_has_name():
    assert hasattr(classes::ClassDiagram, "name")
    descriptor = None
    for klass in classes::ClassDiagram.__mro__:
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
        "string",
        "integer",
        "datetime",
        "float",
        "bool",
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
classes::Reference_strategy = st.builds(
    classes::Reference,
    name=
        safe_text
)
classes::Attribute_strategy = st.builds(
    classes::Attribute,
    type=
        safe_text,
    name=
        safe_text
)
classes::Class_strategy = st.builds(
    classes::Class,
    name=
        safe_text
)
classes::ClassDiagram_strategy = st.builds(
    classes::ClassDiagram,
    name=
        safe_text
)

@given(instance=classes::Reference_strategy)
@settings(max_examples=50)
def test_classes::reference_instantiation(instance):
    assert isinstance(instance, classes::Reference)

@given(instance=classes::Reference_strategy)
def test_classes::reference_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classes::Reference_strategy)
def test_classes::reference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classes::Attribute_strategy)
@settings(max_examples=50)
def test_classes::attribute_instantiation(instance):
    assert isinstance(instance, classes::Attribute)

@given(instance=classes::Attribute_strategy)
def test_classes::attribute_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=classes::Attribute_strategy)
def test_classes::attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=classes::Attribute_strategy)
def test_classes::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classes::Attribute_strategy)
def test_classes::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classes::Class_strategy)
@settings(max_examples=50)
def test_classes::class_instantiation(instance):
    assert isinstance(instance, classes::Class)

@given(instance=classes::Class_strategy)
def test_classes::class_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classes::Class_strategy)
def test_classes::class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classes::ClassDiagram_strategy)
@settings(max_examples=50)
def test_classes::classdiagram_instantiation(instance):
    assert isinstance(instance, classes::ClassDiagram)

@given(instance=classes::ClassDiagram_strategy)
def test_classes::classdiagram_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classes::ClassDiagram_strategy)
def test_classes::classdiagram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
