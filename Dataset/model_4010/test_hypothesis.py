import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    class::Attribute,
    class::Association,
    class::Clazz,
    class::ClassDiagram,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_class::attribute_is_not_abstract():
    assert not inspect.isabstract(class::Attribute)


def test_class::attribute_constructor_exists():
    assert callable(class::Attribute.__init__)


def test_class::attribute_constructor_args():
    sig = inspect.signature(class::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_class::attribute_has_id():
    assert hasattr(class::Attribute, "id")
    descriptor = None
    for klass in class::Attribute.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_class::association_is_not_abstract():
    assert not inspect.isabstract(class::Association)


def test_class::association_constructor_exists():
    assert callable(class::Association.__init__)


def test_class::association_constructor_args():
    sig = inspect.signature(class::Association.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_class::association_has_id():
    assert hasattr(class::Association, "id")
    descriptor = None
    for klass in class::Association.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_class::clazz_is_not_abstract():
    assert not inspect.isabstract(class::Clazz)


def test_class::clazz_constructor_exists():
    assert callable(class::Clazz.__init__)


def test_class::clazz_constructor_args():
    sig = inspect.signature(class::Clazz.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_class::clazz_has_id():
    assert hasattr(class::Clazz, "id")
    descriptor = None
    for klass in class::Clazz.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_class::classdiagram_is_not_abstract():
    assert not inspect.isabstract(class::ClassDiagram)


def test_class::classdiagram_constructor_exists():
    assert callable(class::ClassDiagram.__init__)


def test_class::classdiagram_constructor_args():
    sig = inspect.signature(class::ClassDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_class::classdiagram_has_id():
    assert hasattr(class::ClassDiagram, "id")
    descriptor = None
    for klass in class::ClassDiagram.__mro__:
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
class::Attribute_strategy = st.builds(
    class::Attribute,
    id=
        safe_text
)
class::Association_strategy = st.builds(
    class::Association,
    id=
        safe_text
)
class::Clazz_strategy = st.builds(
    class::Clazz,
    id=
        safe_text
)
class::ClassDiagram_strategy = st.builds(
    class::ClassDiagram,
    id=
        safe_text
)

@given(instance=class::Attribute_strategy)
@settings(max_examples=50)
def test_class::attribute_instantiation(instance):
    assert isinstance(instance, class::Attribute)

@given(instance=class::Attribute_strategy)
def test_class::attribute_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=class::Attribute_strategy)
def test_class::attribute_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=class::Association_strategy)
@settings(max_examples=50)
def test_class::association_instantiation(instance):
    assert isinstance(instance, class::Association)

@given(instance=class::Association_strategy)
def test_class::association_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=class::Association_strategy)
def test_class::association_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=class::Clazz_strategy)
@settings(max_examples=50)
def test_class::clazz_instantiation(instance):
    assert isinstance(instance, class::Clazz)

@given(instance=class::Clazz_strategy)
def test_class::clazz_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=class::Clazz_strategy)
def test_class::clazz_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=class::ClassDiagram_strategy)
@settings(max_examples=50)
def test_class::classdiagram_instantiation(instance):
    assert isinstance(instance, class::ClassDiagram)

@given(instance=class::ClassDiagram_strategy)
def test_class::classdiagram_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=class::ClassDiagram_strategy)
def test_class::classdiagram_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
