import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    class_Attribute,
    class_Association,
    class_Clazz,
    class_ClassDiagram,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_class_attribute_is_not_abstract():
    assert not inspect.isabstract(class_Attribute)


def test_class_attribute_constructor_exists():
    assert callable(class_Attribute.__init__)


def test_class_attribute_constructor_args():
    sig = inspect.signature(class_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_class_attribute_has_id():
    assert hasattr(class_Attribute, "id")
    descriptor = None
    for klass in class_Attribute.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_class_association_is_not_abstract():
    assert not inspect.isabstract(class_Association)


def test_class_association_constructor_exists():
    assert callable(class_Association.__init__)


def test_class_association_constructor_args():
    sig = inspect.signature(class_Association.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_class_association_has_id():
    assert hasattr(class_Association, "id")
    descriptor = None
    for klass in class_Association.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_class_clazz_is_not_abstract():
    assert not inspect.isabstract(class_Clazz)


def test_class_clazz_constructor_exists():
    assert callable(class_Clazz.__init__)


def test_class_clazz_constructor_args():
    sig = inspect.signature(class_Clazz.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_class_clazz_has_id():
    assert hasattr(class_Clazz, "id")
    descriptor = None
    for klass in class_Clazz.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_class_classdiagram_is_not_abstract():
    assert not inspect.isabstract(class_ClassDiagram)


def test_class_classdiagram_constructor_exists():
    assert callable(class_ClassDiagram.__init__)


def test_class_classdiagram_constructor_args():
    sig = inspect.signature(class_ClassDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_class_classdiagram_has_id():
    assert hasattr(class_ClassDiagram, "id")
    descriptor = None
    for klass in class_ClassDiagram.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
class_Attribute_strategy = st.builds(
    class_Attribute,
    id=
        safe_text
)
class_Association_strategy = st.builds(
    class_Association,
    id=
        safe_text
)
class_Clazz_strategy = st.builds(
    class_Clazz,
    id=
        safe_text
)
class_ClassDiagram_strategy = st.builds(
    class_ClassDiagram,
    id=
        safe_text
)

@given(instance=class_Attribute_strategy)
@settings(max_examples=50)
def test_class_attribute_instantiation(instance):
    assert isinstance(instance, class_Attribute)



@given(instance=class_Attribute_strategy)
def test_class_attribute_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=class_Association_strategy)
@settings(max_examples=50)
def test_class_association_instantiation(instance):
    assert isinstance(instance, class_Association)



@given(instance=class_Association_strategy)
def test_class_association_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=class_Clazz_strategy)
@settings(max_examples=50)
def test_class_clazz_instantiation(instance):
    assert isinstance(instance, class_Clazz)



@given(instance=class_Clazz_strategy)
def test_class_clazz_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=class_ClassDiagram_strategy)
@settings(max_examples=50)
def test_class_classdiagram_instantiation(instance):
    assert isinstance(instance, class_ClassDiagram)



@given(instance=class_ClassDiagram_strategy)
def test_class_classdiagram_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
