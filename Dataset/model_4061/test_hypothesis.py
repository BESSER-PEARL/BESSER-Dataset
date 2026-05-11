import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    simpleUML::NamedElement,
    NamedElement,
    simpleUML::Classifier,
    simpleUML::Attribute,
    Classifier,
    simpleUML::Package,
    simpleUML::DataType,
    simpleUML::Association,
    simpleUML::Class,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpleuml::namedelement_is_not_abstract():
    assert not inspect.isabstract(simpleUML::NamedElement)


def test_simpleuml::namedelement_constructor_exists():
    assert callable(simpleUML::NamedElement.__init__)


def test_simpleuml::namedelement_constructor_args():
    sig = inspect.signature(simpleUML::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleuml::namedelement_has_name():
    assert hasattr(simpleUML::NamedElement, "name")
    descriptor = None
    for klass in simpleUML::NamedElement.__mro__:
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



def test_simpleuml::classifier_is_not_abstract():
    assert not inspect.isabstract(simpleUML::Classifier)


def test_simpleuml::classifier_constructor_exists():
    assert callable(simpleUML::Classifier.__init__)


def test_simpleuml::classifier_constructor_args():
    sig = inspect.signature(simpleUML::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::attribute_is_not_abstract():
    assert not inspect.isabstract(simpleUML::Attribute)


def test_simpleuml::attribute_constructor_exists():
    assert callable(simpleUML::Attribute.__init__)


def test_simpleuml::attribute_constructor_args():
    sig = inspect.signature(simpleUML::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::package_is_not_abstract():
    assert not inspect.isabstract(simpleUML::Package)


def test_simpleuml::package_constructor_exists():
    assert callable(simpleUML::Package.__init__)


def test_simpleuml::package_constructor_args():
    sig = inspect.signature(simpleUML::Package.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::datatype_is_not_abstract():
    assert not inspect.isabstract(simpleUML::DataType)


def test_simpleuml::datatype_constructor_exists():
    assert callable(simpleUML::DataType.__init__)


def test_simpleuml::datatype_constructor_args():
    sig = inspect.signature(simpleUML::DataType.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::association_is_not_abstract():
    assert not inspect.isabstract(simpleUML::Association)


def test_simpleuml::association_constructor_exists():
    assert callable(simpleUML::Association.__init__)


def test_simpleuml::association_constructor_args():
    sig = inspect.signature(simpleUML::Association.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::class_is_not_abstract():
    assert not inspect.isabstract(simpleUML::Class)


def test_simpleuml::class_constructor_exists():
    assert callable(simpleUML::Class.__init__)


def test_simpleuml::class_constructor_args():
    sig = inspect.signature(simpleUML::Class.__init__)
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
simpleUML::NamedElement_strategy = st.builds(
    simpleUML::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
simpleUML::Classifier_strategy = st.builds(
    simpleUML::Classifier,
)
simpleUML::Attribute_strategy = st.builds(
    simpleUML::Attribute,
)
Classifier_strategy = st.builds(
    Classifier,
)
simpleUML::Package_strategy = st.builds(
    simpleUML::Package,
)
simpleUML::DataType_strategy = st.builds(
    simpleUML::DataType,
)
simpleUML::Association_strategy = st.builds(
    simpleUML::Association,
)
simpleUML::Class_strategy = st.builds(
    simpleUML::Class,
)

@given(instance=simpleUML::NamedElement_strategy)
@settings(max_examples=50)
def test_simpleuml::namedelement_instantiation(instance):
    assert isinstance(instance, simpleUML::NamedElement)

@given(instance=simpleUML::NamedElement_strategy)
def test_simpleuml::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleUML::NamedElement_strategy)
def test_simpleuml::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=simpleUML::Classifier_strategy)
@settings(max_examples=50)
def test_simpleuml::classifier_instantiation(instance):
    assert isinstance(instance, simpleUML::Classifier)

@given(instance=simpleUML::Attribute_strategy)
@settings(max_examples=50)
def test_simpleuml::attribute_instantiation(instance):
    assert isinstance(instance, simpleUML::Attribute)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=simpleUML::Package_strategy)
@settings(max_examples=50)
def test_simpleuml::package_instantiation(instance):
    assert isinstance(instance, simpleUML::Package)

@given(instance=simpleUML::DataType_strategy)
@settings(max_examples=50)
def test_simpleuml::datatype_instantiation(instance):
    assert isinstance(instance, simpleUML::DataType)

@given(instance=simpleUML::Association_strategy)
@settings(max_examples=50)
def test_simpleuml::association_instantiation(instance):
    assert isinstance(instance, simpleUML::Association)

@given(instance=simpleUML::Class_strategy)
@settings(max_examples=50)
def test_simpleuml::class_instantiation(instance):
    assert isinstance(instance, simpleUML::Class)
