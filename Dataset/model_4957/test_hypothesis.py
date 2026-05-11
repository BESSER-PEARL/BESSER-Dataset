import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NamedElement,
    extmetadata::Attribute,
    extmetadata::Class,
    extmetadata::NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_extmetadata::attribute_is_not_abstract():
    assert not inspect.isabstract(extmetadata::Attribute)


def test_extmetadata::attribute_constructor_exists():
    assert callable(extmetadata::Attribute.__init__)


def test_extmetadata::attribute_constructor_args():
    sig = inspect.signature(extmetadata::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_extmetadata::class_is_not_abstract():
    assert not inspect.isabstract(extmetadata::Class)


def test_extmetadata::class_constructor_exists():
    assert callable(extmetadata::Class.__init__)


def test_extmetadata::class_constructor_args():
    sig = inspect.signature(extmetadata::Class.__init__)
    params = list(sig.parameters.keys())



def test_extmetadata::namedelement_is_not_abstract():
    assert not inspect.isabstract(extmetadata::NamedElement)


def test_extmetadata::namedelement_constructor_exists():
    assert callable(extmetadata::NamedElement.__init__)


def test_extmetadata::namedelement_constructor_args():
    sig = inspect.signature(extmetadata::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_extmetadata::namedelement_has_name():
    assert hasattr(extmetadata::NamedElement, "name")
    descriptor = None
    for klass in extmetadata::NamedElement.__mro__:
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
NamedElement_strategy = st.builds(
    NamedElement,
)
extmetadata::Attribute_strategy = st.builds(
    extmetadata::Attribute,
)
extmetadata::Class_strategy = st.builds(
    extmetadata::Class,
)
extmetadata::NamedElement_strategy = st.builds(
    extmetadata::NamedElement,
    name=
        safe_text
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=extmetadata::Attribute_strategy)
@settings(max_examples=50)
def test_extmetadata::attribute_instantiation(instance):
    assert isinstance(instance, extmetadata::Attribute)

@given(instance=extmetadata::Class_strategy)
@settings(max_examples=50)
def test_extmetadata::class_instantiation(instance):
    assert isinstance(instance, extmetadata::Class)

@given(instance=extmetadata::NamedElement_strategy)
@settings(max_examples=50)
def test_extmetadata::namedelement_instantiation(instance):
    assert isinstance(instance, extmetadata::NamedElement)

@given(instance=extmetadata::NamedElement_strategy)
def test_extmetadata::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=extmetadata::NamedElement_strategy)
def test_extmetadata::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
