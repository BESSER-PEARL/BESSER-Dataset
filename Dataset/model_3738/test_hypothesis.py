import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    LinkEndData,
    UML2_LinkEndCreationData,
    Property,
    UML2_Port,
    UML2_ExtensionEnd,
    UML2_QualifierValue,
    UML2_Property,
    UML2_LinkEndData,
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



def test_uml2_linkendcreationdata_is_not_abstract():
    assert not inspect.isabstract(UML2_LinkEndCreationData)


def test_uml2_linkendcreationdata_constructor_exists():
    assert callable(UML2_LinkEndCreationData.__init__)


def test_uml2_linkendcreationdata_constructor_args():
    sig = inspect.signature(UML2_LinkEndCreationData.__init__)
    params = list(sig.parameters.keys())



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



def test_uml2_qualifiervalue_is_not_abstract():
    assert not inspect.isabstract(UML2_QualifierValue)


def test_uml2_qualifiervalue_constructor_exists():
    assert callable(UML2_QualifierValue.__init__)


def test_uml2_qualifiervalue_constructor_args():
    sig = inspect.signature(UML2_QualifierValue.__init__)
    params = list(sig.parameters.keys())



def test_uml2_property_is_not_abstract():
    assert not inspect.isabstract(UML2_Property)


def test_uml2_property_constructor_exists():
    assert callable(UML2_Property.__init__)


def test_uml2_property_constructor_args():
    sig = inspect.signature(UML2_Property.__init__)
    params = list(sig.parameters.keys())



def test_uml2_linkenddata_is_not_abstract():
    assert not inspect.isabstract(UML2_LinkEndData)


def test_uml2_linkenddata_constructor_exists():
    assert callable(UML2_LinkEndData.__init__)


def test_uml2_linkenddata_constructor_args():
    sig = inspect.signature(UML2_LinkEndData.__init__)
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
UML2_LinkEndCreationData_strategy = st.builds(
    UML2_LinkEndCreationData,
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
UML2_QualifierValue_strategy = st.builds(
    UML2_QualifierValue,
)
UML2_Property_strategy = st.builds(
    UML2_Property,
)
UML2_LinkEndData_strategy = st.builds(
    UML2_LinkEndData,
)

@given(instance=LinkEndData_strategy)
@settings(max_examples=50)
def test_linkenddata_instantiation(instance):
    assert isinstance(instance, LinkEndData)

@given(instance=UML2_LinkEndCreationData_strategy)
@settings(max_examples=50)
def test_uml2_linkendcreationdata_instantiation(instance):
    assert isinstance(instance, UML2_LinkEndCreationData)

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

@given(instance=UML2_QualifierValue_strategy)
@settings(max_examples=50)
def test_uml2_qualifiervalue_instantiation(instance):
    assert isinstance(instance, UML2_QualifierValue)

@given(instance=UML2_Property_strategy)
@settings(max_examples=50)
def test_uml2_property_instantiation(instance):
    assert isinstance(instance, UML2_Property)

@given(instance=UML2_LinkEndData_strategy)
@settings(max_examples=50)
def test_uml2_linkenddata_instantiation(instance):
    assert isinstance(instance, UML2_LinkEndData)
