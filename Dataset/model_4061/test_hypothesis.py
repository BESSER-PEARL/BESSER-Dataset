import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    simpleUML_NamedElement,
    NamedElement,
    simpleUML_Classifier,
    simpleUML_Attribute,
    Classifier,
    simpleUML_DataType,
    simpleUML_Association,
    simpleUML_Package,
    simpleUML_Class,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpleuml_namedelement_is_not_abstract():
    assert not inspect.isabstract(simpleUML_NamedElement)


def test_simpleuml_namedelement_constructor_exists():
    assert callable(simpleUML_NamedElement.__init__)


def test_simpleuml_namedelement_constructor_args():
    sig = inspect.signature(simpleUML_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleuml_namedelement_has_name():
    assert hasattr(simpleUML_NamedElement, "name")
    descriptor = None
    for klass in simpleUML_NamedElement.__mro__:
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



def test_simpleuml_classifier_is_not_abstract():
    assert not inspect.isabstract(simpleUML_Classifier)


def test_simpleuml_classifier_constructor_exists():
    assert callable(simpleUML_Classifier.__init__)


def test_simpleuml_classifier_constructor_args():
    sig = inspect.signature(simpleUML_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml_attribute_is_not_abstract():
    assert not inspect.isabstract(simpleUML_Attribute)


def test_simpleuml_attribute_constructor_exists():
    assert callable(simpleUML_Attribute.__init__)


def test_simpleuml_attribute_constructor_args():
    sig = inspect.signature(simpleUML_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml_datatype_is_not_abstract():
    assert not inspect.isabstract(simpleUML_DataType)


def test_simpleuml_datatype_constructor_exists():
    assert callable(simpleUML_DataType.__init__)


def test_simpleuml_datatype_constructor_args():
    sig = inspect.signature(simpleUML_DataType.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml_association_is_not_abstract():
    assert not inspect.isabstract(simpleUML_Association)


def test_simpleuml_association_constructor_exists():
    assert callable(simpleUML_Association.__init__)


def test_simpleuml_association_constructor_args():
    sig = inspect.signature(simpleUML_Association.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml_package_is_not_abstract():
    assert not inspect.isabstract(simpleUML_Package)


def test_simpleuml_package_constructor_exists():
    assert callable(simpleUML_Package.__init__)


def test_simpleuml_package_constructor_args():
    sig = inspect.signature(simpleUML_Package.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml_class_is_not_abstract():
    assert not inspect.isabstract(simpleUML_Class)


def test_simpleuml_class_constructor_exists():
    assert callable(simpleUML_Class.__init__)


def test_simpleuml_class_constructor_args():
    sig = inspect.signature(simpleUML_Class.__init__)
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
simpleUML_NamedElement_strategy = st.builds(
    simpleUML_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
simpleUML_Classifier_strategy = st.builds(
    simpleUML_Classifier,
)
simpleUML_Attribute_strategy = st.builds(
    simpleUML_Attribute,
)
Classifier_strategy = st.builds(
    Classifier,
)
simpleUML_DataType_strategy = st.builds(
    simpleUML_DataType,
)
simpleUML_Association_strategy = st.builds(
    simpleUML_Association,
)
simpleUML_Package_strategy = st.builds(
    simpleUML_Package,
)
simpleUML_Class_strategy = st.builds(
    simpleUML_Class,
)

@given(instance=simpleUML_NamedElement_strategy)
@settings(max_examples=50)
def test_simpleuml_namedelement_instantiation(instance):
    assert isinstance(instance, simpleUML_NamedElement)



@given(instance=simpleUML_NamedElement_strategy)
def test_simpleuml_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=simpleUML_Classifier_strategy)
@settings(max_examples=50)
def test_simpleuml_classifier_instantiation(instance):
    assert isinstance(instance, simpleUML_Classifier)

@given(instance=simpleUML_Attribute_strategy)
@settings(max_examples=50)
def test_simpleuml_attribute_instantiation(instance):
    assert isinstance(instance, simpleUML_Attribute)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=simpleUML_DataType_strategy)
@settings(max_examples=50)
def test_simpleuml_datatype_instantiation(instance):
    assert isinstance(instance, simpleUML_DataType)

@given(instance=simpleUML_Association_strategy)
@settings(max_examples=50)
def test_simpleuml_association_instantiation(instance):
    assert isinstance(instance, simpleUML_Association)

@given(instance=simpleUML_Package_strategy)
@settings(max_examples=50)
def test_simpleuml_package_instantiation(instance):
    assert isinstance(instance, simpleUML_Package)

@given(instance=simpleUML_Class_strategy)
@settings(max_examples=50)
def test_simpleuml_class_instantiation(instance):
    assert isinstance(instance, simpleUML_Class)
