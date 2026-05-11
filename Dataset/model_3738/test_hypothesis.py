import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    LinkEndData,
    UML2::LinkEndCreationData,
    Property,
    UML2::Port,
    UML2::ExtensionEnd,
    UML2::QualifierValue,
    UML2::Property,
    UML2::LinkEndData,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_linkenddata_is_not_abstract():
    assert not inspect.isabstract(LinkEndData)


def test_linkenddata_constructor_exists():
    assert callable(LinkEndData.__init__)


def test_linkenddata_constructor_args():
    sig = inspect.signature(LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_uml2::linkendcreationdata_is_not_abstract():
    assert not inspect.isabstract(UML2::LinkEndCreationData)


def test_uml2::linkendcreationdata_constructor_exists():
    assert callable(UML2::LinkEndCreationData.__init__)


def test_uml2::linkendcreationdata_constructor_args():
    sig = inspect.signature(UML2::LinkEndCreationData.__init__)
    params = list(sig.parameters.keys())



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



def test_uml2::qualifiervalue_is_not_abstract():
    assert not inspect.isabstract(UML2::QualifierValue)


def test_uml2::qualifiervalue_constructor_exists():
    assert callable(UML2::QualifierValue.__init__)


def test_uml2::qualifiervalue_constructor_args():
    sig = inspect.signature(UML2::QualifierValue.__init__)
    params = list(sig.parameters.keys())



def test_uml2::property_is_not_abstract():
    assert not inspect.isabstract(UML2::Property)


def test_uml2::property_constructor_exists():
    assert callable(UML2::Property.__init__)


def test_uml2::property_constructor_args():
    sig = inspect.signature(UML2::Property.__init__)
    params = list(sig.parameters.keys())



def test_uml2::linkenddata_is_not_abstract():
    assert not inspect.isabstract(UML2::LinkEndData)


def test_uml2::linkenddata_constructor_exists():
    assert callable(UML2::LinkEndData.__init__)


def test_uml2::linkenddata_constructor_args():
    sig = inspect.signature(UML2::LinkEndData.__init__)
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
LinkEndData_strategy = st.builds(
    LinkEndData,
)
UML2::LinkEndCreationData_strategy = st.builds(
    UML2::LinkEndCreationData,
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
UML2::QualifierValue_strategy = st.builds(
    UML2::QualifierValue,
)
UML2::Property_strategy = st.builds(
    UML2::Property,
)
UML2::LinkEndData_strategy = st.builds(
    UML2::LinkEndData,
)

@given(instance=LinkEndData_strategy)
@settings(max_examples=50)
def test_linkenddata_instantiation(instance):
    assert isinstance(instance, LinkEndData)

@given(instance=UML2::LinkEndCreationData_strategy)
@settings(max_examples=50)
def test_uml2::linkendcreationdata_instantiation(instance):
    assert isinstance(instance, UML2::LinkEndCreationData)

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

@given(instance=UML2::QualifierValue_strategy)
@settings(max_examples=50)
def test_uml2::qualifiervalue_instantiation(instance):
    assert isinstance(instance, UML2::QualifierValue)

@given(instance=UML2::Property_strategy)
@settings(max_examples=50)
def test_uml2::property_instantiation(instance):
    assert isinstance(instance, UML2::Property)

@given(instance=UML2::LinkEndData_strategy)
@settings(max_examples=50)
def test_uml2::linkenddata_instantiation(instance):
    assert isinstance(instance, UML2::LinkEndData)
