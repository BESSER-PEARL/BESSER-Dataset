import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Property,
    UML2::ExtensionEnd,
    UML2::Port,
    UML2::StructuralFeature,
    StructuralFeature,
    UML2::Property,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_uml2::extensionend_is_not_abstract():
    assert not inspect.isabstract(UML2::ExtensionEnd)


def test_uml2::extensionend_constructor_exists():
    assert callable(UML2::ExtensionEnd.__init__)


def test_uml2::extensionend_constructor_args():
    sig = inspect.signature(UML2::ExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml2::port_is_not_abstract():
    assert not inspect.isabstract(UML2::Port)


def test_uml2::port_constructor_exists():
    assert callable(UML2::Port.__init__)


def test_uml2::port_constructor_args():
    sig = inspect.signature(UML2::Port.__init__)
    params = list(sig.parameters.keys())



def test_uml2::structuralfeature_is_not_abstract():
    assert not inspect.isabstract(UML2::StructuralFeature)


def test_uml2::structuralfeature_constructor_exists():
    assert callable(UML2::StructuralFeature.__init__)


def test_uml2::structuralfeature_constructor_args():
    sig = inspect.signature(UML2::StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"

def test_uml2::structuralfeature_has_isReadOnly():
    assert hasattr(UML2::StructuralFeature, "isReadOnly")
    descriptor = None
    for klass in UML2::StructuralFeature.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml2::property_is_not_abstract():
    assert not inspect.isabstract(UML2::Property)


def test_uml2::property_constructor_exists():
    assert callable(UML2::Property.__init__)


def test_uml2::property_constructor_args():
    sig = inspect.signature(UML2::Property.__init__)
    params = list(sig.parameters.keys())
    assert "isDerivedUnion" in params, "Missing parameter 'isDerivedUnion'"

def test_uml2::property_has_isDerivedUnion():
    assert hasattr(UML2::Property, "isDerivedUnion")
    descriptor = None
    for klass in UML2::Property.__mro__:
        if "isDerivedUnion" in klass.__dict__:
            descriptor = klass.__dict__["isDerivedUnion"]
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
Property_strategy = st.builds(
    Property,
)
UML2::ExtensionEnd_strategy = st.builds(
    UML2::ExtensionEnd,
)
UML2::Port_strategy = st.builds(
    UML2::Port,
)
UML2::StructuralFeature_strategy = st.builds(
    UML2::StructuralFeature,
    isReadOnly=
        st.booleans()
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
UML2::Property_strategy = st.builds(
    UML2::Property,
    isDerivedUnion=
        st.booleans()
)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=UML2::ExtensionEnd_strategy)
@settings(max_examples=50)
def test_uml2::extensionend_instantiation(instance):
    assert isinstance(instance, UML2::ExtensionEnd)

@given(instance=UML2::Port_strategy)
@settings(max_examples=50)
def test_uml2::port_instantiation(instance):
    assert isinstance(instance, UML2::Port)

@given(instance=UML2::StructuralFeature_strategy)
@settings(max_examples=50)
def test_uml2::structuralfeature_instantiation(instance):
    assert isinstance(instance, UML2::StructuralFeature)

@given(instance=UML2::StructuralFeature_strategy)
def test_uml2::structuralfeature_isReadOnly_type(instance):
    assert isinstance(instance.isReadOnly, bool)


@given(instance=UML2::StructuralFeature_strategy)
def test_uml2::structuralfeature_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=UML2::Property_strategy)
@settings(max_examples=50)
def test_uml2::property_instantiation(instance):
    assert isinstance(instance, UML2::Property)

@given(instance=UML2::Property_strategy)
def test_uml2::property_isDerivedUnion_type(instance):
    assert isinstance(instance.isDerivedUnion, bool)


@given(instance=UML2::Property_strategy)
def test_uml2::property_isDerivedUnion_setter(instance):
    original = instance.isDerivedUnion
    instance.isDerivedUnion = original
    assert instance.isDerivedUnion == original
