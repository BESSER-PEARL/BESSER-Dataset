import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    UML2WithID_Element,
    Property,
    Element,
    UML2WithID_Association,
    UML2WithID_Port,
    UML2WithID_ExtensionEnd,
    UML2WithID_Property,
    Association,
    UML2WithID_Extension,
    UML2WithID_AssociationClass,
    UML2WithID_CommunicationPath,
    AggregationKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uml2withid_element_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Element)


def test_uml2withid_element_constructor_exists():
    assert callable(UML2WithID_Element.__init__)


def test_uml2withid_element_constructor_args():
    sig = inspect.signature(UML2WithID_Element.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"

def test_uml2withid_element_has_ID():
    assert hasattr(UML2WithID_Element, "ID")
    descriptor = None
    for klass in UML2WithID_Element.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



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



def test_uml2withid_association_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Association)


def test_uml2withid_association_constructor_exists():
    assert callable(UML2WithID_Association.__init__)


def test_uml2withid_association_constructor_args():
    sig = inspect.signature(UML2WithID_Association.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_port_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Port)


def test_uml2withid_port_constructor_exists():
    assert callable(UML2WithID_Port.__init__)


def test_uml2withid_port_constructor_args():
    sig = inspect.signature(UML2WithID_Port.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_extensionend_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ExtensionEnd)


def test_uml2withid_extensionend_constructor_exists():
    assert callable(UML2WithID_ExtensionEnd.__init__)


def test_uml2withid_extensionend_constructor_args():
    sig = inspect.signature(UML2WithID_ExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_property_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Property)


def test_uml2withid_property_constructor_exists():
    assert callable(UML2WithID_Property.__init__)


def test_uml2withid_property_constructor_args():
    sig = inspect.signature(UML2WithID_Property.__init__)
    params = list(sig.parameters.keys())
    assert "aggregation" in params, "Missing parameter 'aggregation'"

def test_uml2withid_property_has_aggregation():
    assert hasattr(UML2WithID_Property, "aggregation")
    descriptor = None
    for klass in UML2WithID_Property.__mro__:
        if "aggregation" in klass.__dict__:
            descriptor = klass.__dict__["aggregation"]
            break
    assert isinstance(descriptor, property)



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_extension_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Extension)


def test_uml2withid_extension_constructor_exists():
    assert callable(UML2WithID_Extension.__init__)


def test_uml2withid_extension_constructor_args():
    sig = inspect.signature(UML2WithID_Extension.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_associationclass_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_AssociationClass)


def test_uml2withid_associationclass_constructor_exists():
    assert callable(UML2WithID_AssociationClass.__init__)


def test_uml2withid_associationclass_constructor_args():
    sig = inspect.signature(UML2WithID_AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_communicationpath_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_CommunicationPath)


def test_uml2withid_communicationpath_constructor_exists():
    assert callable(UML2WithID_CommunicationPath.__init__)


def test_uml2withid_communicationpath_constructor_args():
    sig = inspect.signature(UML2WithID_CommunicationPath.__init__)
    params = list(sig.parameters.keys())

def test_aggregationkind_exists():
    # Check that the Enumeration exists
    assert AggregationKind is not None

def test_aggregationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AggregationKind]
    expected_literals = [
        "composite",
        "shared",
        "none",
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
UML2WithID_Element_strategy = st.builds(
    UML2WithID_Element,
    ID=
        safe_text
)
Property_strategy = st.builds(
    Property,
)
Element_strategy = st.builds(
    Element,
)
UML2WithID_Association_strategy = st.builds(
    UML2WithID_Association,
)
UML2WithID_Port_strategy = st.builds(
    UML2WithID_Port,
)
UML2WithID_ExtensionEnd_strategy = st.builds(
    UML2WithID_ExtensionEnd,
)
UML2WithID_Property_strategy = st.builds(
    UML2WithID_Property,
    aggregation=
        safe_text
)
Association_strategy = st.builds(
    Association,
)
UML2WithID_Extension_strategy = st.builds(
    UML2WithID_Extension,
)
UML2WithID_AssociationClass_strategy = st.builds(
    UML2WithID_AssociationClass,
)
UML2WithID_CommunicationPath_strategy = st.builds(
    UML2WithID_CommunicationPath,
)

@given(instance=UML2WithID_Element_strategy)
@settings(max_examples=50)
def test_uml2withid_element_instantiation(instance):
    assert isinstance(instance, UML2WithID_Element)



@given(instance=UML2WithID_Element_strategy)
def test_uml2withid_element_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=UML2WithID_Association_strategy)
@settings(max_examples=50)
def test_uml2withid_association_instantiation(instance):
    assert isinstance(instance, UML2WithID_Association)

@given(instance=UML2WithID_Port_strategy)
@settings(max_examples=50)
def test_uml2withid_port_instantiation(instance):
    assert isinstance(instance, UML2WithID_Port)

@given(instance=UML2WithID_ExtensionEnd_strategy)
@settings(max_examples=50)
def test_uml2withid_extensionend_instantiation(instance):
    assert isinstance(instance, UML2WithID_ExtensionEnd)

@given(instance=UML2WithID_Property_strategy)
@settings(max_examples=50)
def test_uml2withid_property_instantiation(instance):
    assert isinstance(instance, UML2WithID_Property)



@given(instance=UML2WithID_Property_strategy)
def test_uml2withid_property_aggregation_setter(instance):
    original = instance.aggregation
    instance.aggregation = original
    assert instance.aggregation == original

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=UML2WithID_Extension_strategy)
@settings(max_examples=50)
def test_uml2withid_extension_instantiation(instance):
    assert isinstance(instance, UML2WithID_Extension)

@given(instance=UML2WithID_AssociationClass_strategy)
@settings(max_examples=50)
def test_uml2withid_associationclass_instantiation(instance):
    assert isinstance(instance, UML2WithID_AssociationClass)

@given(instance=UML2WithID_CommunicationPath_strategy)
@settings(max_examples=50)
def test_uml2withid_communicationpath_instantiation(instance):
    assert isinstance(instance, UML2WithID_CommunicationPath)
