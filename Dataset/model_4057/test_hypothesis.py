import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NamedElement,
    classdiagram_Method,
    classdiagram_Attribute,
    classdiagram_Class,
    classdiagram_NamedElement,
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



def test_classdiagram_method_is_not_abstract():
    assert not inspect.isabstract(classdiagram_Method)


def test_classdiagram_method_constructor_exists():
    assert callable(classdiagram_Method.__init__)


def test_classdiagram_method_constructor_args():
    sig = inspect.signature(classdiagram_Method.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram_attribute_is_not_abstract():
    assert not inspect.isabstract(classdiagram_Attribute)


def test_classdiagram_attribute_constructor_exists():
    assert callable(classdiagram_Attribute.__init__)


def test_classdiagram_attribute_constructor_args():
    sig = inspect.signature(classdiagram_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram_class_is_not_abstract():
    assert not inspect.isabstract(classdiagram_Class)


def test_classdiagram_class_constructor_exists():
    assert callable(classdiagram_Class.__init__)


def test_classdiagram_class_constructor_args():
    sig = inspect.signature(classdiagram_Class.__init__)
    params = list(sig.parameters.keys())



def test_classdiagram_namedelement_is_not_abstract():
    assert not inspect.isabstract(classdiagram_NamedElement)


def test_classdiagram_namedelement_constructor_exists():
    assert callable(classdiagram_NamedElement.__init__)


def test_classdiagram_namedelement_constructor_args():
    sig = inspect.signature(classdiagram_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classdiagram_namedelement_has_name():
    assert hasattr(classdiagram_NamedElement, "name")
    descriptor = None
    for klass in classdiagram_NamedElement.__mro__:
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
classdiagram_Method_strategy = st.builds(
    classdiagram_Method,
)
classdiagram_Attribute_strategy = st.builds(
    classdiagram_Attribute,
)
classdiagram_Class_strategy = st.builds(
    classdiagram_Class,
)
classdiagram_NamedElement_strategy = st.builds(
    classdiagram_NamedElement,
    name=
        safe_text
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=classdiagram_Method_strategy)
@settings(max_examples=50)
def test_classdiagram_method_instantiation(instance):
    assert isinstance(instance, classdiagram_Method)

@given(instance=classdiagram_Attribute_strategy)
@settings(max_examples=50)
def test_classdiagram_attribute_instantiation(instance):
    assert isinstance(instance, classdiagram_Attribute)

@given(instance=classdiagram_Class_strategy)
@settings(max_examples=50)
def test_classdiagram_class_instantiation(instance):
    assert isinstance(instance, classdiagram_Class)

@given(instance=classdiagram_NamedElement_strategy)
@settings(max_examples=50)
def test_classdiagram_namedelement_instantiation(instance):
    assert isinstance(instance, classdiagram_NamedElement)



@given(instance=classdiagram_NamedElement_strategy)
def test_classdiagram_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
