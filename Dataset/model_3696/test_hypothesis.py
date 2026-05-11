import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    UML2WithID::Element,
    Association,
    Property,
    Element,
    UML2WithID::CommunicationPath,
    UML2WithID::Association,
    UML2WithID::AssociationClass,
    UML2WithID::ExtensionEnd,
    UML2WithID::Extension,
    UML2WithID::Port,
    UML2WithID::Property,
    AggregationKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uml2withid::element_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Element)


def test_uml2withid::element_constructor_exists():
    assert callable(UML2WithID::Element.__init__)


def test_uml2withid::element_constructor_args():
    sig = inspect.signature(UML2WithID::Element.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"

def test_uml2withid::element_has_ID():
    assert hasattr(UML2WithID::Element, "ID")
    descriptor = None
    for klass in UML2WithID::Element.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::communicationpath_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::CommunicationPath)


def test_uml2withid::communicationpath_constructor_exists():
    assert callable(UML2WithID::CommunicationPath.__init__)


def test_uml2withid::communicationpath_constructor_args():
    sig = inspect.signature(UML2WithID::CommunicationPath.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::association_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Association)


def test_uml2withid::association_constructor_exists():
    assert callable(UML2WithID::Association.__init__)


def test_uml2withid::association_constructor_args():
    sig = inspect.signature(UML2WithID::Association.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::associationclass_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::AssociationClass)


def test_uml2withid::associationclass_constructor_exists():
    assert callable(UML2WithID::AssociationClass.__init__)


def test_uml2withid::associationclass_constructor_args():
    sig = inspect.signature(UML2WithID::AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::extensionend_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::ExtensionEnd)


def test_uml2withid::extensionend_constructor_exists():
    assert callable(UML2WithID::ExtensionEnd.__init__)


def test_uml2withid::extensionend_constructor_args():
    sig = inspect.signature(UML2WithID::ExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::extension_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Extension)


def test_uml2withid::extension_constructor_exists():
    assert callable(UML2WithID::Extension.__init__)


def test_uml2withid::extension_constructor_args():
    sig = inspect.signature(UML2WithID::Extension.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::port_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Port)


def test_uml2withid::port_constructor_exists():
    assert callable(UML2WithID::Port.__init__)


def test_uml2withid::port_constructor_args():
    sig = inspect.signature(UML2WithID::Port.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::property_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Property)


def test_uml2withid::property_constructor_exists():
    assert callable(UML2WithID::Property.__init__)


def test_uml2withid::property_constructor_args():
    sig = inspect.signature(UML2WithID::Property.__init__)
    params = list(sig.parameters.keys())
    assert "aggregation" in params, "Missing parameter 'aggregation'"

def test_uml2withid::property_has_aggregation():
    assert hasattr(UML2WithID::Property, "aggregation")
    descriptor = None
    for klass in UML2WithID::Property.__mro__:
        if "aggregation" in klass.__dict__:
            descriptor = klass.__dict__["aggregation"]
            break
    assert isinstance(descriptor, property)

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
UML2WithID::Element_strategy = st.builds(
    UML2WithID::Element,
    ID=
        safe_text
)
Association_strategy = st.builds(
    Association,
)
Property_strategy = st.builds(
    Property,
)
Element_strategy = st.builds(
    Element,
)
UML2WithID::CommunicationPath_strategy = st.builds(
    UML2WithID::CommunicationPath,
)
UML2WithID::Association_strategy = st.builds(
    UML2WithID::Association,
)
UML2WithID::AssociationClass_strategy = st.builds(
    UML2WithID::AssociationClass,
)
UML2WithID::ExtensionEnd_strategy = st.builds(
    UML2WithID::ExtensionEnd,
)
UML2WithID::Extension_strategy = st.builds(
    UML2WithID::Extension,
)
UML2WithID::Port_strategy = st.builds(
    UML2WithID::Port,
)
UML2WithID::Property_strategy = st.builds(
    UML2WithID::Property,
    aggregation=
        safe_text
)

@given(instance=UML2WithID::Element_strategy)
@settings(max_examples=50)
def test_uml2withid::element_instantiation(instance):
    assert isinstance(instance, UML2WithID::Element)

@given(instance=UML2WithID::Element_strategy)
def test_uml2withid::element_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=UML2WithID::Element_strategy)
def test_uml2withid::element_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=UML2WithID::CommunicationPath_strategy)
@settings(max_examples=50)
def test_uml2withid::communicationpath_instantiation(instance):
    assert isinstance(instance, UML2WithID::CommunicationPath)

@given(instance=UML2WithID::Association_strategy)
@settings(max_examples=50)
def test_uml2withid::association_instantiation(instance):
    assert isinstance(instance, UML2WithID::Association)

@given(instance=UML2WithID::AssociationClass_strategy)
@settings(max_examples=50)
def test_uml2withid::associationclass_instantiation(instance):
    assert isinstance(instance, UML2WithID::AssociationClass)

@given(instance=UML2WithID::ExtensionEnd_strategy)
@settings(max_examples=50)
def test_uml2withid::extensionend_instantiation(instance):
    assert isinstance(instance, UML2WithID::ExtensionEnd)

@given(instance=UML2WithID::Extension_strategy)
@settings(max_examples=50)
def test_uml2withid::extension_instantiation(instance):
    assert isinstance(instance, UML2WithID::Extension)

@given(instance=UML2WithID::Port_strategy)
@settings(max_examples=50)
def test_uml2withid::port_instantiation(instance):
    assert isinstance(instance, UML2WithID::Port)

@given(instance=UML2WithID::Property_strategy)
@settings(max_examples=50)
def test_uml2withid::property_instantiation(instance):
    assert isinstance(instance, UML2WithID::Property)

@given(instance=UML2WithID::Property_strategy)
def test_uml2withid::property_aggregation_type(instance):
    assert isinstance(instance.aggregation, str)


@given(instance=UML2WithID::Property_strategy)
def test_uml2withid::property_aggregation_setter(instance):
    original = instance.aggregation
    instance.aggregation = original
    assert instance.aggregation == original
