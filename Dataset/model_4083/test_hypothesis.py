import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    simpleUML_Model,
    simpleUML_UMLAttribute,
    simpleUML_Generalization,
    simpleUML_UMLClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpleuml_model_is_not_abstract():
    assert not inspect.isabstract(simpleUML_Model)


def test_simpleuml_model_constructor_exists():
    assert callable(simpleUML_Model.__init__)


def test_simpleuml_model_constructor_args():
    sig = inspect.signature(simpleUML_Model.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml_umlattribute_is_not_abstract():
    assert not inspect.isabstract(simpleUML_UMLAttribute)


def test_simpleuml_umlattribute_constructor_exists():
    assert callable(simpleUML_UMLAttribute.__init__)


def test_simpleuml_umlattribute_constructor_args():
    sig = inspect.signature(simpleUML_UMLAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "umlName" in params, "Missing parameter 'umlName'"

def test_simpleuml_umlattribute_has_umlName():
    assert hasattr(simpleUML_UMLAttribute, "umlName")
    descriptor = None
    for klass in simpleUML_UMLAttribute.__mro__:
        if "umlName" in klass.__dict__:
            descriptor = klass.__dict__["umlName"]
            break
    assert isinstance(descriptor, property)



def test_simpleuml_generalization_is_not_abstract():
    assert not inspect.isabstract(simpleUML_Generalization)


def test_simpleuml_generalization_constructor_exists():
    assert callable(simpleUML_Generalization.__init__)


def test_simpleuml_generalization_constructor_args():
    sig = inspect.signature(simpleUML_Generalization.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml_umlclass_is_not_abstract():
    assert not inspect.isabstract(simpleUML_UMLClass)


def test_simpleuml_umlclass_constructor_exists():
    assert callable(simpleUML_UMLClass.__init__)


def test_simpleuml_umlclass_constructor_args():
    sig = inspect.signature(simpleUML_UMLClass.__init__)
    params = list(sig.parameters.keys())
    assert "umlName" in params, "Missing parameter 'umlName'"

def test_simpleuml_umlclass_has_umlName():
    assert hasattr(simpleUML_UMLClass, "umlName")
    descriptor = None
    for klass in simpleUML_UMLClass.__mro__:
        if "umlName" in klass.__dict__:
            descriptor = klass.__dict__["umlName"]
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
simpleUML_Model_strategy = st.builds(
    simpleUML_Model,
)
simpleUML_UMLAttribute_strategy = st.builds(
    simpleUML_UMLAttribute,
    umlName=
        safe_text
)
simpleUML_Generalization_strategy = st.builds(
    simpleUML_Generalization,
)
simpleUML_UMLClass_strategy = st.builds(
    simpleUML_UMLClass,
    umlName=
        safe_text
)

@given(instance=simpleUML_Model_strategy)
@settings(max_examples=50)
def test_simpleuml_model_instantiation(instance):
    assert isinstance(instance, simpleUML_Model)

@given(instance=simpleUML_UMLAttribute_strategy)
@settings(max_examples=50)
def test_simpleuml_umlattribute_instantiation(instance):
    assert isinstance(instance, simpleUML_UMLAttribute)



@given(instance=simpleUML_UMLAttribute_strategy)
def test_simpleuml_umlattribute_umlName_setter(instance):
    original = instance.umlName
    instance.umlName = original
    assert instance.umlName == original

@given(instance=simpleUML_Generalization_strategy)
@settings(max_examples=50)
def test_simpleuml_generalization_instantiation(instance):
    assert isinstance(instance, simpleUML_Generalization)

@given(instance=simpleUML_UMLClass_strategy)
@settings(max_examples=50)
def test_simpleuml_umlclass_instantiation(instance):
    assert isinstance(instance, simpleUML_UMLClass)



@given(instance=simpleUML_UMLClass_strategy)
def test_simpleuml_umlclass_umlName_setter(instance):
    original = instance.umlName
    instance.umlName = original
    assert instance.umlName == original
