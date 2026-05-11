import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    simpleUML::UMLAttribute,
    simpleUML::Generalization,
    simpleUML::SimpleClass,
    simpleUML::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_simpleuml::simpleclass_is_not_abstract():
    assert not inspect.isabstract(simpleUML::SimpleClass)


def test_simpleuml::simpleclass_constructor_exists():
    assert callable(simpleUML::SimpleClass.__init__)


def test_simpleuml::simpleclass_constructor_args():
    sig = inspect.signature(simpleUML::SimpleClass.__init__)
    params = list(sig.parameters.keys())
    assert "simpleName" in params, "Missing parameter 'simpleName'"

def test_simpleuml::simpleclass_has_simpleName():
    assert hasattr(simpleUML::SimpleClass, "simpleName")
    descriptor = None
    for klass in simpleUML::SimpleClass.__mro__:
        if "simpleName" in klass.__dict__:
            descriptor = klass.__dict__["simpleName"]
            break
    assert isinstance(descriptor, property)



def test_simpleuml::model_is_not_abstract():
    assert not inspect.isabstract(simpleUML::Model)


def test_simpleuml::model_constructor_exists():
    assert callable(simpleUML::Model.__init__)


def test_simpleuml::model_constructor_args():
    sig = inspect.signature(simpleUML::Model.__init__)
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
simpleUML::UMLAttribute_strategy = st.builds(
    simpleUML::UMLAttribute,
    umlName=
        safe_text
)
simpleUML::Generalization_strategy = st.builds(
    simpleUML::Generalization,
)
simpleUML::SimpleClass_strategy = st.builds(
    simpleUML::SimpleClass,
    simpleName=
        safe_text
)
simpleUML::Model_strategy = st.builds(
    simpleUML::Model,
)

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

@given(instance=simpleUML::SimpleClass_strategy)
@settings(max_examples=50)
def test_simpleuml::simpleclass_instantiation(instance):
    assert isinstance(instance, simpleUML::SimpleClass)

@given(instance=simpleUML::SimpleClass_strategy)
def test_simpleuml::simpleclass_simpleName_type(instance):
    assert isinstance(instance.simpleName, str)


@given(instance=simpleUML::SimpleClass_strategy)
def test_simpleuml::simpleclass_simpleName_setter(instance):
    original = instance.simpleName
    instance.simpleName = original
    assert instance.simpleName == original

@given(instance=simpleUML::Model_strategy)
@settings(max_examples=50)
def test_simpleuml::model_instantiation(instance):
    assert isinstance(instance, simpleUML::Model)
