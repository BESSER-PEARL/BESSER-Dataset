import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    simpleUML_UMLAttribute,
    simpleUML_Generalization,
    simpleUML_SimpleClass,
    simpleUML_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_simpleuml_simpleclass_is_not_abstract():
    assert not inspect.isabstract(simpleUML_SimpleClass)


def test_simpleuml_simpleclass_constructor_exists():
    assert callable(simpleUML_SimpleClass.__init__)


def test_simpleuml_simpleclass_constructor_args():
    sig = inspect.signature(simpleUML_SimpleClass.__init__)
    params = list(sig.parameters.keys())
    assert "simpleName" in params, "Missing parameter 'simpleName'"

def test_simpleuml_simpleclass_has_simpleName():
    assert hasattr(simpleUML_SimpleClass, "simpleName")
    descriptor = None
    for klass in simpleUML_SimpleClass.__mro__:
        if "simpleName" in klass.__dict__:
            descriptor = klass.__dict__["simpleName"]
            break
    assert isinstance(descriptor, property)



def test_simpleuml_model_is_not_abstract():
    assert not inspect.isabstract(simpleUML_Model)


def test_simpleuml_model_constructor_exists():
    assert callable(simpleUML_Model.__init__)


def test_simpleuml_model_constructor_args():
    sig = inspect.signature(simpleUML_Model.__init__)
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
simpleUML_UMLAttribute_strategy = st.builds(
    simpleUML_UMLAttribute,
    umlName=
        safe_text
)
simpleUML_Generalization_strategy = st.builds(
    simpleUML_Generalization,
)
simpleUML_SimpleClass_strategy = st.builds(
    simpleUML_SimpleClass,
    simpleName=
        safe_text
)
simpleUML_Model_strategy = st.builds(
    simpleUML_Model,
)

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

@given(instance=simpleUML_SimpleClass_strategy)
@settings(max_examples=50)
def test_simpleuml_simpleclass_instantiation(instance):
    assert isinstance(instance, simpleUML_SimpleClass)



@given(instance=simpleUML_SimpleClass_strategy)
def test_simpleuml_simpleclass_simpleName_setter(instance):
    original = instance.simpleName
    instance.simpleName = original
    assert instance.simpleName == original

@given(instance=simpleUML_Model_strategy)
@settings(max_examples=50)
def test_simpleuml_model_instantiation(instance):
    assert isinstance(instance, simpleUML_Model)
