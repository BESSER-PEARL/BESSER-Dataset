import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    euml::Relations,
    NamedElement,
    euml::Attribute,
    euml::Operation,
    euml::Class,
    euml::Package,
    euml::NamedElement,
    Relations,
    euml::Realization,
    euml::Dependecy,
    euml::Generalization,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_euml::relations_is_not_abstract():
    assert not inspect.isabstract(euml::Relations)


def test_euml::relations_constructor_exists():
    assert callable(euml::Relations.__init__)


def test_euml::relations_constructor_args():
    sig = inspect.signature(euml::Relations.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_euml::attribute_is_not_abstract():
    assert not inspect.isabstract(euml::Attribute)


def test_euml::attribute_constructor_exists():
    assert callable(euml::Attribute.__init__)


def test_euml::attribute_constructor_args():
    sig = inspect.signature(euml::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_euml::operation_is_not_abstract():
    assert not inspect.isabstract(euml::Operation)


def test_euml::operation_constructor_exists():
    assert callable(euml::Operation.__init__)


def test_euml::operation_constructor_args():
    sig = inspect.signature(euml::Operation.__init__)
    params = list(sig.parameters.keys())



def test_euml::class_is_not_abstract():
    assert not inspect.isabstract(euml::Class)


def test_euml::class_constructor_exists():
    assert callable(euml::Class.__init__)


def test_euml::class_constructor_args():
    sig = inspect.signature(euml::Class.__init__)
    params = list(sig.parameters.keys())



def test_euml::package_is_not_abstract():
    assert not inspect.isabstract(euml::Package)


def test_euml::package_constructor_exists():
    assert callable(euml::Package.__init__)


def test_euml::package_constructor_args():
    sig = inspect.signature(euml::Package.__init__)
    params = list(sig.parameters.keys())



def test_euml::namedelement_is_not_abstract():
    assert not inspect.isabstract(euml::NamedElement)


def test_euml::namedelement_constructor_exists():
    assert callable(euml::NamedElement.__init__)


def test_euml::namedelement_constructor_args():
    sig = inspect.signature(euml::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_euml::namedelement_has_name():
    assert hasattr(euml::NamedElement, "name")
    descriptor = None
    for klass in euml::NamedElement.__mro__:
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



def test_euml::realization_is_not_abstract():
    assert not inspect.isabstract(euml::Realization)


def test_euml::realization_constructor_exists():
    assert callable(euml::Realization.__init__)


def test_euml::realization_constructor_args():
    sig = inspect.signature(euml::Realization.__init__)
    params = list(sig.parameters.keys())



def test_euml::dependecy_is_not_abstract():
    assert not inspect.isabstract(euml::Dependecy)


def test_euml::dependecy_constructor_exists():
    assert callable(euml::Dependecy.__init__)


def test_euml::dependecy_constructor_args():
    sig = inspect.signature(euml::Dependecy.__init__)
    params = list(sig.parameters.keys())



def test_euml::generalization_is_not_abstract():
    assert not inspect.isabstract(euml::Generalization)


def test_euml::generalization_constructor_exists():
    assert callable(euml::Generalization.__init__)


def test_euml::generalization_constructor_args():
    sig = inspect.signature(euml::Generalization.__init__)
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
euml::Relations_strategy = st.builds(
    euml::Relations,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
euml::Attribute_strategy = st.builds(
    euml::Attribute,
)
euml::Operation_strategy = st.builds(
    euml::Operation,
)
euml::Class_strategy = st.builds(
    euml::Class,
)
euml::Package_strategy = st.builds(
    euml::Package,
)
euml::NamedElement_strategy = st.builds(
    euml::NamedElement,
    name=
        safe_text
)
Relations_strategy = st.builds(
    Relations,
)
euml::Realization_strategy = st.builds(
    euml::Realization,
)
euml::Dependecy_strategy = st.builds(
    euml::Dependecy,
)
euml::Generalization_strategy = st.builds(
    euml::Generalization,
)

@given(instance=euml::Relations_strategy)
@settings(max_examples=50)
def test_euml::relations_instantiation(instance):
    assert isinstance(instance, euml::Relations)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=euml::Attribute_strategy)
@settings(max_examples=50)
def test_euml::attribute_instantiation(instance):
    assert isinstance(instance, euml::Attribute)

@given(instance=euml::Operation_strategy)
@settings(max_examples=50)
def test_euml::operation_instantiation(instance):
    assert isinstance(instance, euml::Operation)

@given(instance=euml::Class_strategy)
@settings(max_examples=50)
def test_euml::class_instantiation(instance):
    assert isinstance(instance, euml::Class)

@given(instance=euml::Package_strategy)
@settings(max_examples=50)
def test_euml::package_instantiation(instance):
    assert isinstance(instance, euml::Package)

@given(instance=euml::NamedElement_strategy)
@settings(max_examples=50)
def test_euml::namedelement_instantiation(instance):
    assert isinstance(instance, euml::NamedElement)

@given(instance=euml::NamedElement_strategy)
def test_euml::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=euml::NamedElement_strategy)
def test_euml::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Relations_strategy)
@settings(max_examples=50)
def test_relations_instantiation(instance):
    assert isinstance(instance, Relations)

@given(instance=euml::Realization_strategy)
@settings(max_examples=50)
def test_euml::realization_instantiation(instance):
    assert isinstance(instance, euml::Realization)

@given(instance=euml::Dependecy_strategy)
@settings(max_examples=50)
def test_euml::dependecy_instantiation(instance):
    assert isinstance(instance, euml::Dependecy)

@given(instance=euml::Generalization_strategy)
@settings(max_examples=50)
def test_euml::generalization_instantiation(instance):
    assert isinstance(instance, euml::Generalization)
