import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    uml_NamedElement,
    NamedElement,
    uml_Class,
    uml_UMLSpecification,
    uml_Attribute,
    uml_Association,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uml_namedelement_is_not_abstract():
    assert not inspect.isabstract(uml_NamedElement)


def test_uml_namedelement_constructor_exists():
    assert callable(uml_NamedElement.__init__)


def test_uml_namedelement_constructor_args():
    sig = inspect.signature(uml_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uml_namedelement_has_name():
    assert hasattr(uml_NamedElement, "name")
    descriptor = None
    for klass in uml_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml_class_is_not_abstract():
    assert not inspect.isabstract(uml_Class)


def test_uml_class_constructor_exists():
    assert callable(uml_Class.__init__)


def test_uml_class_constructor_args():
    sig = inspect.signature(uml_Class.__init__)
    params = list(sig.parameters.keys())



def test_uml_umlspecification_is_not_abstract():
    assert not inspect.isabstract(uml_UMLSpecification)


def test_uml_umlspecification_constructor_exists():
    assert callable(uml_UMLSpecification.__init__)


def test_uml_umlspecification_constructor_args():
    sig = inspect.signature(uml_UMLSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_attribute_is_not_abstract():
    assert not inspect.isabstract(uml_Attribute)


def test_uml_attribute_constructor_exists():
    assert callable(uml_Attribute.__init__)


def test_uml_attribute_constructor_args():
    sig = inspect.signature(uml_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_uml_association_is_not_abstract():
    assert not inspect.isabstract(uml_Association)


def test_uml_association_constructor_exists():
    assert callable(uml_Association.__init__)


def test_uml_association_constructor_args():
    sig = inspect.signature(uml_Association.__init__)
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
uml_NamedElement_strategy = st.builds(
    uml_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
uml_Class_strategy = st.builds(
    uml_Class,
)
uml_UMLSpecification_strategy = st.builds(
    uml_UMLSpecification,
)
uml_Attribute_strategy = st.builds(
    uml_Attribute,
)
uml_Association_strategy = st.builds(
    uml_Association,
)

@given(instance=uml_NamedElement_strategy)
@settings(max_examples=50)
def test_uml_namedelement_instantiation(instance):
    assert isinstance(instance, uml_NamedElement)



@given(instance=uml_NamedElement_strategy)
def test_uml_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=uml_Class_strategy)
@settings(max_examples=50)
def test_uml_class_instantiation(instance):
    assert isinstance(instance, uml_Class)

@given(instance=uml_UMLSpecification_strategy)
@settings(max_examples=50)
def test_uml_umlspecification_instantiation(instance):
    assert isinstance(instance, uml_UMLSpecification)

@given(instance=uml_Attribute_strategy)
@settings(max_examples=50)
def test_uml_attribute_instantiation(instance):
    assert isinstance(instance, uml_Attribute)

@given(instance=uml_Association_strategy)
@settings(max_examples=50)
def test_uml_association_instantiation(instance):
    assert isinstance(instance, uml_Association)
