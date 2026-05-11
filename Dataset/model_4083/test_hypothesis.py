import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    simpleUML::Model,
    simpleUML::UMLAttribute,
    simpleUML::Generalization,
    simpleUML::UMLClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpleuml::model_is_not_abstract():
    assert not inspect.isabstract(simpleUML::Model)


def test_simpleuml::model_constructor_exists():
    assert callable(simpleUML::Model.__init__)


def test_simpleuml::model_constructor_args():
    sig = inspect.signature(simpleUML::Model.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::umlattribute_is_not_abstract():
    assert not inspect.isabstract(simpleUML::UMLAttribute)


def test_simpleuml::umlattribute_constructor_exists():
    assert callable(simpleUML::UMLAttribute.__init__)


def test_simpleuml::umlattribute_constructor_args():
    sig = inspect.signature(simpleUML::UMLAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "umlName" in params, "Missing parameter 'umlName'"

def test_simpleuml::umlattribute_has_umlName():
    assert hasattr(simpleUML::UMLAttribute, "umlName")
    descriptor = None
    for klass in simpleUML::UMLAttribute.__mro__:
        if "umlName" in klass.__dict__:
            descriptor = klass.__dict__["umlName"]
            break
    assert isinstance(descriptor, property)



def test_simpleuml::generalization_is_not_abstract():
    assert not inspect.isabstract(simpleUML::Generalization)


def test_simpleuml::generalization_constructor_exists():
    assert callable(simpleUML::Generalization.__init__)


def test_simpleuml::generalization_constructor_args():
    sig = inspect.signature(simpleUML::Generalization.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::umlclass_is_not_abstract():
    assert not inspect.isabstract(simpleUML::UMLClass)


def test_simpleuml::umlclass_constructor_exists():
    assert callable(simpleUML::UMLClass.__init__)


def test_simpleuml::umlclass_constructor_args():
    sig = inspect.signature(simpleUML::UMLClass.__init__)
    params = list(sig.parameters.keys())
    assert "umlName" in params, "Missing parameter 'umlName'"

def test_simpleuml::umlclass_has_umlName():
    assert hasattr(simpleUML::UMLClass, "umlName")
    descriptor = None
    for klass in simpleUML::UMLClass.__mro__:
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
simpleUML::Model_strategy = st.builds(
    simpleUML::Model,
)
simpleUML::UMLAttribute_strategy = st.builds(
    simpleUML::UMLAttribute,
    umlName=
        safe_text
)
simpleUML::Generalization_strategy = st.builds(
    simpleUML::Generalization,
)
simpleUML::UMLClass_strategy = st.builds(
    simpleUML::UMLClass,
    umlName=
        safe_text
)

@given(instance=simpleUML::Model_strategy)
@settings(max_examples=50)
def test_simpleuml::model_instantiation(instance):
    assert isinstance(instance, simpleUML::Model)

@given(instance=simpleUML::UMLAttribute_strategy)
@settings(max_examples=50)
def test_simpleuml::umlattribute_instantiation(instance):
    assert isinstance(instance, simpleUML::UMLAttribute)

@given(instance=simpleUML::UMLAttribute_strategy)
def test_simpleuml::umlattribute_umlName_type(instance):
    assert isinstance(instance.umlName, str)


@given(instance=simpleUML::UMLAttribute_strategy)
def test_simpleuml::umlattribute_umlName_setter(instance):
    original = instance.umlName
    instance.umlName = original
    assert instance.umlName == original

@given(instance=simpleUML::Generalization_strategy)
@settings(max_examples=50)
def test_simpleuml::generalization_instantiation(instance):
    assert isinstance(instance, simpleUML::Generalization)

@given(instance=simpleUML::UMLClass_strategy)
@settings(max_examples=50)
def test_simpleuml::umlclass_instantiation(instance):
    assert isinstance(instance, simpleUML::UMLClass)

@given(instance=simpleUML::UMLClass_strategy)
def test_simpleuml::umlclass_umlName_type(instance):
    assert isinstance(instance.umlName, str)


@given(instance=simpleUML::UMLClass_strategy)
def test_simpleuml::umlclass_umlName_setter(instance):
    original = instance.umlName
    instance.umlName = original
    assert instance.umlName == original
