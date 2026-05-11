import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NamedElement,
    simpleClass::Association,
    simpleClass::Class,
    simpleClass::Attribute,
    simpleClass::Package,
    simpleClass::ClassModel,
    simpleClass::NamedElement,
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



def test_simpleclass::association_is_not_abstract():
    assert not inspect.isabstract(simpleClass::Association)


def test_simpleclass::association_constructor_exists():
    assert callable(simpleClass::Association.__init__)


def test_simpleclass::association_constructor_args():
    sig = inspect.signature(simpleClass::Association.__init__)
    params = list(sig.parameters.keys())



def test_simpleclass::class_is_not_abstract():
    assert not inspect.isabstract(simpleClass::Class)


def test_simpleclass::class_constructor_exists():
    assert callable(simpleClass::Class.__init__)


def test_simpleclass::class_constructor_args():
    sig = inspect.signature(simpleClass::Class.__init__)
    params = list(sig.parameters.keys())
    assert "persistent" in params, "Missing parameter 'persistent'"

def test_simpleclass::class_has_persistent():
    assert hasattr(simpleClass::Class, "persistent")
    descriptor = None
    for klass in simpleClass::Class.__mro__:
        if "persistent" in klass.__dict__:
            descriptor = klass.__dict__["persistent"]
            break
    assert isinstance(descriptor, property)



def test_simpleclass::attribute_is_not_abstract():
    assert not inspect.isabstract(simpleClass::Attribute)


def test_simpleclass::attribute_constructor_exists():
    assert callable(simpleClass::Attribute.__init__)


def test_simpleclass::attribute_constructor_args():
    sig = inspect.signature(simpleClass::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_simpleclass::package_is_not_abstract():
    assert not inspect.isabstract(simpleClass::Package)


def test_simpleclass::package_constructor_exists():
    assert callable(simpleClass::Package.__init__)


def test_simpleclass::package_constructor_args():
    sig = inspect.signature(simpleClass::Package.__init__)
    params = list(sig.parameters.keys())



def test_simpleclass::classmodel_is_not_abstract():
    assert not inspect.isabstract(simpleClass::ClassModel)


def test_simpleclass::classmodel_constructor_exists():
    assert callable(simpleClass::ClassModel.__init__)


def test_simpleclass::classmodel_constructor_args():
    sig = inspect.signature(simpleClass::ClassModel.__init__)
    params = list(sig.parameters.keys())



def test_simpleclass::namedelement_is_not_abstract():
    assert not inspect.isabstract(simpleClass::NamedElement)


def test_simpleclass::namedelement_constructor_exists():
    assert callable(simpleClass::NamedElement.__init__)


def test_simpleclass::namedelement_constructor_args():
    sig = inspect.signature(simpleClass::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleclass::namedelement_has_name():
    assert hasattr(simpleClass::NamedElement, "name")
    descriptor = None
    for klass in simpleClass::NamedElement.__mro__:
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
simpleClass::Association_strategy = st.builds(
    simpleClass::Association,
)
simpleClass::Class_strategy = st.builds(
    simpleClass::Class,
    persistent=
        st.booleans()
)
simpleClass::Attribute_strategy = st.builds(
    simpleClass::Attribute,
)
simpleClass::Package_strategy = st.builds(
    simpleClass::Package,
)
simpleClass::ClassModel_strategy = st.builds(
    simpleClass::ClassModel,
)
simpleClass::NamedElement_strategy = st.builds(
    simpleClass::NamedElement,
    name=
        safe_text
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=simpleClass::Association_strategy)
@settings(max_examples=50)
def test_simpleclass::association_instantiation(instance):
    assert isinstance(instance, simpleClass::Association)

@given(instance=simpleClass::Class_strategy)
@settings(max_examples=50)
def test_simpleclass::class_instantiation(instance):
    assert isinstance(instance, simpleClass::Class)

@given(instance=simpleClass::Class_strategy)
def test_simpleclass::class_persistent_type(instance):
    assert isinstance(instance.persistent, bool)


@given(instance=simpleClass::Class_strategy)
def test_simpleclass::class_persistent_setter(instance):
    original = instance.persistent
    instance.persistent = original
    assert instance.persistent == original

@given(instance=simpleClass::Attribute_strategy)
@settings(max_examples=50)
def test_simpleclass::attribute_instantiation(instance):
    assert isinstance(instance, simpleClass::Attribute)

@given(instance=simpleClass::Package_strategy)
@settings(max_examples=50)
def test_simpleclass::package_instantiation(instance):
    assert isinstance(instance, simpleClass::Package)

@given(instance=simpleClass::ClassModel_strategy)
@settings(max_examples=50)
def test_simpleclass::classmodel_instantiation(instance):
    assert isinstance(instance, simpleClass::ClassModel)

@given(instance=simpleClass::NamedElement_strategy)
@settings(max_examples=50)
def test_simpleclass::namedelement_instantiation(instance):
    assert isinstance(instance, simpleClass::NamedElement)

@given(instance=simpleClass::NamedElement_strategy)
def test_simpleclass::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleClass::NamedElement_strategy)
def test_simpleclass::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
