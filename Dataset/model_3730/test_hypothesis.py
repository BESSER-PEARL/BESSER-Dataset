import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    UML2_Property,
    Property,
    UML2_Port,
    UML2_ExtensionEnd,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uml2_property_is_not_abstract():
    assert not inspect.isabstract(UML2_Property)


def test_uml2_property_constructor_exists():
    assert callable(UML2_Property.__init__)


def test_uml2_property_constructor_args():
    sig = inspect.signature(UML2_Property.__init__)
    params = list(sig.parameters.keys())
    assert "isDerivedUnion" in params, "Missing parameter 'isDerivedUnion'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"

def test_uml2_property_has_isDerivedUnion():
    assert hasattr(UML2_Property, "isDerivedUnion")
    descriptor = None
    for klass in UML2_Property.__mro__:
        if "isDerivedUnion" in klass.__dict__:
            descriptor = klass.__dict__["isDerivedUnion"]
            break
    assert isinstance(descriptor, property)

def test_uml2_property_has_isDerived():
    assert hasattr(UML2_Property, "isDerived")
    descriptor = None
    for klass in UML2_Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_uml2_port_is_not_abstract():
    assert not inspect.isabstract(UML2_Port)


def test_uml2_port_constructor_exists():
    assert callable(UML2_Port.__init__)


def test_uml2_port_constructor_args():
    sig = inspect.signature(UML2_Port.__init__)
    params = list(sig.parameters.keys())



def test_uml2_extensionend_is_not_abstract():
    assert not inspect.isabstract(UML2_ExtensionEnd)


def test_uml2_extensionend_constructor_exists():
    assert callable(UML2_ExtensionEnd.__init__)


def test_uml2_extensionend_constructor_args():
    sig = inspect.signature(UML2_ExtensionEnd.__init__)
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
UML2_Property_strategy = st.builds(
    UML2_Property,
    isDerivedUnion=
        st.booleans(),
    isDerived=
        st.booleans()
)
Property_strategy = st.builds(
    Property,
)
UML2_Port_strategy = st.builds(
    UML2_Port,
)
UML2_ExtensionEnd_strategy = st.builds(
    UML2_ExtensionEnd,
)

@given(instance=UML2_Property_strategy)
@settings(max_examples=50)
def test_uml2_property_instantiation(instance):
    assert isinstance(instance, UML2_Property)



@given(instance=UML2_Property_strategy)
def test_uml2_property_isDerivedUnion_setter(instance):
    original = instance.isDerivedUnion
    instance.isDerivedUnion = original
    assert instance.isDerivedUnion == original



@given(instance=UML2_Property_strategy)
def test_uml2_property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=UML2_Port_strategy)
@settings(max_examples=50)
def test_uml2_port_instantiation(instance):
    assert isinstance(instance, UML2_Port)

@given(instance=UML2_ExtensionEnd_strategy)
@settings(max_examples=50)
def test_uml2_extensionend_instantiation(instance):
    assert isinstance(instance, UML2_ExtensionEnd)
