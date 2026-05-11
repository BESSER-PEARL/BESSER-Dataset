import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    UML2::Property,
    Property,
    UML2::Port,
    UML2::ExtensionEnd,
    AggregationKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uml2::property_is_not_abstract():
    assert not inspect.isabstract(UML2::Property)


def test_uml2::property_constructor_exists():
    assert callable(UML2::Property.__init__)


def test_uml2::property_constructor_args():
    sig = inspect.signature(UML2::Property.__init__)
    params = list(sig.parameters.keys())
    assert "aggregation" in params, "Missing parameter 'aggregation'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"

def test_uml2::property_has_aggregation():
    assert hasattr(UML2::Property, "aggregation")
    descriptor = None
    for klass in UML2::Property.__mro__:
        if "aggregation" in klass.__dict__:
            descriptor = klass.__dict__["aggregation"]
            break
    assert isinstance(descriptor, property)

def test_uml2::property_has_isComposite():
    assert hasattr(UML2::Property, "isComposite")
    descriptor = None
    for klass in UML2::Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_uml2::port_is_not_abstract():
    assert not inspect.isabstract(UML2::Port)


def test_uml2::port_constructor_exists():
    assert callable(UML2::Port.__init__)


def test_uml2::port_constructor_args():
    sig = inspect.signature(UML2::Port.__init__)
    params = list(sig.parameters.keys())



def test_uml2::extensionend_is_not_abstract():
    assert not inspect.isabstract(UML2::ExtensionEnd)


def test_uml2::extensionend_constructor_exists():
    assert callable(UML2::ExtensionEnd.__init__)


def test_uml2::extensionend_constructor_args():
    sig = inspect.signature(UML2::ExtensionEnd.__init__)
    params = list(sig.parameters.keys())

def test_aggregationkind_exists():
    # Check that the Enumeration exists
    assert AggregationKind is not None

def test_aggregationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AggregationKind]
    expected_literals = [
        "none",
        "shared",
        "composite",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AggregationKind"


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
UML2::Property_strategy = st.builds(
    UML2::Property,
    aggregation=
        safe_text,
    isComposite=
        st.booleans()
)
Property_strategy = st.builds(
    Property,
)
UML2::Port_strategy = st.builds(
    UML2::Port,
)
UML2::ExtensionEnd_strategy = st.builds(
    UML2::ExtensionEnd,
)

@given(instance=UML2::Property_strategy)
@settings(max_examples=50)
def test_uml2::property_instantiation(instance):
    assert isinstance(instance, UML2::Property)

@given(instance=UML2::Property_strategy)
def test_uml2::property_aggregation_type(instance):
    assert isinstance(instance.aggregation, str)


@given(instance=UML2::Property_strategy)
def test_uml2::property_aggregation_setter(instance):
    original = instance.aggregation
    instance.aggregation = original
    assert instance.aggregation == original

@given(instance=UML2::Property_strategy)
def test_uml2::property_isComposite_type(instance):
    assert isinstance(instance.isComposite, bool)


@given(instance=UML2::Property_strategy)
def test_uml2::property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=UML2::Port_strategy)
@settings(max_examples=50)
def test_uml2::port_instantiation(instance):
    assert isinstance(instance, UML2::Port)

@given(instance=UML2::ExtensionEnd_strategy)
@settings(max_examples=50)
def test_uml2::extensionend_instantiation(instance):
    assert isinstance(instance, UML2::ExtensionEnd)
