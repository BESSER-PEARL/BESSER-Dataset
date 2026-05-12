import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NamedElement,
    extmetadata_Attribute,
    extmetadata_Class,
    extmetadata_NamedElement,
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



def test_extmetadata_attribute_is_not_abstract():
    assert not inspect.isabstract(extmetadata_Attribute)


def test_extmetadata_attribute_constructor_exists():
    assert callable(extmetadata_Attribute.__init__)


def test_extmetadata_attribute_constructor_args():
    sig = inspect.signature(extmetadata_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_extmetadata_class_is_not_abstract():
    assert not inspect.isabstract(extmetadata_Class)


def test_extmetadata_class_constructor_exists():
    assert callable(extmetadata_Class.__init__)


def test_extmetadata_class_constructor_args():
    sig = inspect.signature(extmetadata_Class.__init__)
    params = list(sig.parameters.keys())



def test_extmetadata_namedelement_is_not_abstract():
    assert not inspect.isabstract(extmetadata_NamedElement)


def test_extmetadata_namedelement_constructor_exists():
    assert callable(extmetadata_NamedElement.__init__)


def test_extmetadata_namedelement_constructor_args():
    sig = inspect.signature(extmetadata_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_extmetadata_namedelement_has_name():
    assert hasattr(extmetadata_NamedElement, "name")
    descriptor = None
    for klass in extmetadata_NamedElement.__mro__:
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
extmetadata_Attribute_strategy = st.builds(
    extmetadata_Attribute,
)
extmetadata_Class_strategy = st.builds(
    extmetadata_Class,
)
extmetadata_NamedElement_strategy = st.builds(
    extmetadata_NamedElement,
    name=
        safe_text
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=extmetadata_Attribute_strategy)
@settings(max_examples=50)
def test_extmetadata_attribute_instantiation(instance):
    assert isinstance(instance, extmetadata_Attribute)

@given(instance=extmetadata_Class_strategy)
@settings(max_examples=50)
def test_extmetadata_class_instantiation(instance):
    assert isinstance(instance, extmetadata_Class)

@given(instance=extmetadata_NamedElement_strategy)
@settings(max_examples=50)
def test_extmetadata_namedelement_instantiation(instance):
    assert isinstance(instance, extmetadata_NamedElement)



@given(instance=extmetadata_NamedElement_strategy)
def test_extmetadata_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
