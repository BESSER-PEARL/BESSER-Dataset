import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    euml_Relations,
    NamedElement,
    euml_Operation,
    euml_Class,
    euml_Attribute,
    euml_Package,
    euml_NamedElement,
    Relations,
    euml_Realization,
    euml_Dependecy,
    euml_Generalization,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_euml_relations_is_not_abstract():
    assert not inspect.isabstract(euml_Relations)


def test_euml_relations_constructor_exists():
    assert callable(euml_Relations.__init__)


def test_euml_relations_constructor_args():
    sig = inspect.signature(euml_Relations.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_euml_operation_is_not_abstract():
    assert not inspect.isabstract(euml_Operation)


def test_euml_operation_constructor_exists():
    assert callable(euml_Operation.__init__)


def test_euml_operation_constructor_args():
    sig = inspect.signature(euml_Operation.__init__)
    params = list(sig.parameters.keys())



def test_euml_class_is_not_abstract():
    assert not inspect.isabstract(euml_Class)


def test_euml_class_constructor_exists():
    assert callable(euml_Class.__init__)


def test_euml_class_constructor_args():
    sig = inspect.signature(euml_Class.__init__)
    params = list(sig.parameters.keys())



def test_euml_attribute_is_not_abstract():
    assert not inspect.isabstract(euml_Attribute)


def test_euml_attribute_constructor_exists():
    assert callable(euml_Attribute.__init__)


def test_euml_attribute_constructor_args():
    sig = inspect.signature(euml_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_euml_package_is_not_abstract():
    assert not inspect.isabstract(euml_Package)


def test_euml_package_constructor_exists():
    assert callable(euml_Package.__init__)


def test_euml_package_constructor_args():
    sig = inspect.signature(euml_Package.__init__)
    params = list(sig.parameters.keys())



def test_euml_namedelement_is_not_abstract():
    assert not inspect.isabstract(euml_NamedElement)


def test_euml_namedelement_constructor_exists():
    assert callable(euml_NamedElement.__init__)


def test_euml_namedelement_constructor_args():
    sig = inspect.signature(euml_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_euml_namedelement_has_name():
    assert hasattr(euml_NamedElement, "name")
    descriptor = None
    for klass in euml_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relations_is_not_abstract():
    assert not inspect.isabstract(Relations)


def test_relations_constructor_exists():
    assert callable(Relations.__init__)


def test_relations_constructor_args():
    sig = inspect.signature(Relations.__init__)
    params = list(sig.parameters.keys())



def test_euml_realization_is_not_abstract():
    assert not inspect.isabstract(euml_Realization)


def test_euml_realization_constructor_exists():
    assert callable(euml_Realization.__init__)


def test_euml_realization_constructor_args():
    sig = inspect.signature(euml_Realization.__init__)
    params = list(sig.parameters.keys())



def test_euml_dependecy_is_not_abstract():
    assert not inspect.isabstract(euml_Dependecy)


def test_euml_dependecy_constructor_exists():
    assert callable(euml_Dependecy.__init__)


def test_euml_dependecy_constructor_args():
    sig = inspect.signature(euml_Dependecy.__init__)
    params = list(sig.parameters.keys())



def test_euml_generalization_is_not_abstract():
    assert not inspect.isabstract(euml_Generalization)


def test_euml_generalization_constructor_exists():
    assert callable(euml_Generalization.__init__)


def test_euml_generalization_constructor_args():
    sig = inspect.signature(euml_Generalization.__init__)
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
euml_Relations_strategy = st.builds(
    euml_Relations,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
euml_Operation_strategy = st.builds(
    euml_Operation,
)
euml_Class_strategy = st.builds(
    euml_Class,
)
euml_Attribute_strategy = st.builds(
    euml_Attribute,
)
euml_Package_strategy = st.builds(
    euml_Package,
)
euml_NamedElement_strategy = st.builds(
    euml_NamedElement,
    name=
        safe_text
)
Relations_strategy = st.builds(
    Relations,
)
euml_Realization_strategy = st.builds(
    euml_Realization,
)
euml_Dependecy_strategy = st.builds(
    euml_Dependecy,
)
euml_Generalization_strategy = st.builds(
    euml_Generalization,
)

@given(instance=euml_Relations_strategy)
@settings(max_examples=50)
def test_euml_relations_instantiation(instance):
    assert isinstance(instance, euml_Relations)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=euml_Operation_strategy)
@settings(max_examples=50)
def test_euml_operation_instantiation(instance):
    assert isinstance(instance, euml_Operation)

@given(instance=euml_Class_strategy)
@settings(max_examples=50)
def test_euml_class_instantiation(instance):
    assert isinstance(instance, euml_Class)

@given(instance=euml_Attribute_strategy)
@settings(max_examples=50)
def test_euml_attribute_instantiation(instance):
    assert isinstance(instance, euml_Attribute)

@given(instance=euml_Package_strategy)
@settings(max_examples=50)
def test_euml_package_instantiation(instance):
    assert isinstance(instance, euml_Package)

@given(instance=euml_NamedElement_strategy)
@settings(max_examples=50)
def test_euml_namedelement_instantiation(instance):
    assert isinstance(instance, euml_NamedElement)



@given(instance=euml_NamedElement_strategy)
def test_euml_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Relations_strategy)
@settings(max_examples=50)
def test_relations_instantiation(instance):
    assert isinstance(instance, Relations)

@given(instance=euml_Realization_strategy)
@settings(max_examples=50)
def test_euml_realization_instantiation(instance):
    assert isinstance(instance, euml_Realization)

@given(instance=euml_Dependecy_strategy)
@settings(max_examples=50)
def test_euml_dependecy_instantiation(instance):
    assert isinstance(instance, euml_Dependecy)

@given(instance=euml_Generalization_strategy)
@settings(max_examples=50)
def test_euml_generalization_instantiation(instance):
    assert isinstance(instance, euml_Generalization)
