import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    UML2_Association,
    Property,
    UML2_ExtensionEnd,
    UML2_Property,
    Association,
    UML2_AssociationClass,
    UML2_CommunicationPath,
    UML2_Port,
    UML2_Extension,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uml2_association_is_not_abstract():
    assert not inspect.isabstract(UML2_Association)


def test_uml2_association_constructor_exists():
    assert callable(UML2_Association.__init__)


def test_uml2_association_constructor_args():
    sig = inspect.signature(UML2_Association.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_uml2_extensionend_is_not_abstract():
    assert not inspect.isabstract(UML2_ExtensionEnd)


def test_uml2_extensionend_constructor_exists():
    assert callable(UML2_ExtensionEnd.__init__)


def test_uml2_extensionend_constructor_args():
    sig = inspect.signature(UML2_ExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml2_property_is_not_abstract():
    assert not inspect.isabstract(UML2_Property)


def test_uml2_property_constructor_exists():
    assert callable(UML2_Property.__init__)


def test_uml2_property_constructor_args():
    sig = inspect.signature(UML2_Property.__init__)
    params = list(sig.parameters.keys())



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_uml2_associationclass_is_not_abstract():
    assert not inspect.isabstract(UML2_AssociationClass)


def test_uml2_associationclass_constructor_exists():
    assert callable(UML2_AssociationClass.__init__)


def test_uml2_associationclass_constructor_args():
    sig = inspect.signature(UML2_AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_uml2_communicationpath_is_not_abstract():
    assert not inspect.isabstract(UML2_CommunicationPath)


def test_uml2_communicationpath_constructor_exists():
    assert callable(UML2_CommunicationPath.__init__)


def test_uml2_communicationpath_constructor_args():
    sig = inspect.signature(UML2_CommunicationPath.__init__)
    params = list(sig.parameters.keys())



def test_uml2_port_is_not_abstract():
    assert not inspect.isabstract(UML2_Port)


def test_uml2_port_constructor_exists():
    assert callable(UML2_Port.__init__)


def test_uml2_port_constructor_args():
    sig = inspect.signature(UML2_Port.__init__)
    params = list(sig.parameters.keys())



def test_uml2_extension_is_not_abstract():
    assert not inspect.isabstract(UML2_Extension)


def test_uml2_extension_constructor_exists():
    assert callable(UML2_Extension.__init__)


def test_uml2_extension_constructor_args():
    sig = inspect.signature(UML2_Extension.__init__)
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
UML2_Association_strategy = st.builds(
    UML2_Association,
)
Property_strategy = st.builds(
    Property,
)
UML2_ExtensionEnd_strategy = st.builds(
    UML2_ExtensionEnd,
)
UML2_Property_strategy = st.builds(
    UML2_Property,
)
Association_strategy = st.builds(
    Association,
)
UML2_AssociationClass_strategy = st.builds(
    UML2_AssociationClass,
)
UML2_CommunicationPath_strategy = st.builds(
    UML2_CommunicationPath,
)
UML2_Port_strategy = st.builds(
    UML2_Port,
)
UML2_Extension_strategy = st.builds(
    UML2_Extension,
)

@given(instance=UML2_Association_strategy)
@settings(max_examples=50)
def test_uml2_association_instantiation(instance):
    assert isinstance(instance, UML2_Association)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=UML2_ExtensionEnd_strategy)
@settings(max_examples=50)
def test_uml2_extensionend_instantiation(instance):
    assert isinstance(instance, UML2_ExtensionEnd)

@given(instance=UML2_Property_strategy)
@settings(max_examples=50)
def test_uml2_property_instantiation(instance):
    assert isinstance(instance, UML2_Property)

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=UML2_AssociationClass_strategy)
@settings(max_examples=50)
def test_uml2_associationclass_instantiation(instance):
    assert isinstance(instance, UML2_AssociationClass)

@given(instance=UML2_CommunicationPath_strategy)
@settings(max_examples=50)
def test_uml2_communicationpath_instantiation(instance):
    assert isinstance(instance, UML2_CommunicationPath)

@given(instance=UML2_Port_strategy)
@settings(max_examples=50)
def test_uml2_port_instantiation(instance):
    assert isinstance(instance, UML2_Port)

@given(instance=UML2_Extension_strategy)
@settings(max_examples=50)
def test_uml2_extension_instantiation(instance):
    assert isinstance(instance, UML2_Extension)
