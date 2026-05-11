import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    UML2WithID::Element,
    Element,
    UML2WithID::Operation,
    UML2WithID::Parameter,
    ParameterDirectionKind,
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



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::operation_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Operation)


def test_uml2withid::operation_constructor_exists():
    assert callable(UML2WithID::Operation.__init__)


def test_uml2withid::operation_constructor_args():
    sig = inspect.signature(UML2WithID::Operation.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid::parameter_is_not_abstract():
    assert not inspect.isabstract(UML2WithID::Parameter)


def test_uml2withid::parameter_constructor_exists():
    assert callable(UML2WithID::Parameter.__init__)


def test_uml2withid::parameter_constructor_args():
    sig = inspect.signature(UML2WithID::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_uml2withid::parameter_has_direction():
    assert hasattr(UML2WithID::Parameter, "direction")
    descriptor = None
    for klass in UML2WithID::Parameter.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_parameterdirectionkind_exists():
    # Check that the Enumeration exists
    assert ParameterDirectionKind is not None

def test_parameterdirectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterDirectionKind]
    expected_literals = [
        "in_",
        "return_",
        "inout",
        "out",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterDirectionKind"


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
Element_strategy = st.builds(
    Element,
)
UML2WithID::Operation_strategy = st.builds(
    UML2WithID::Operation,
)
UML2WithID::Parameter_strategy = st.builds(
    UML2WithID::Parameter,
    direction=
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

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=UML2WithID::Operation_strategy)
@settings(max_examples=50)
def test_uml2withid::operation_instantiation(instance):
    assert isinstance(instance, UML2WithID::Operation)

@given(instance=UML2WithID::Parameter_strategy)
@settings(max_examples=50)
def test_uml2withid::parameter_instantiation(instance):
    assert isinstance(instance, UML2WithID::Parameter)

@given(instance=UML2WithID::Parameter_strategy)
def test_uml2withid::parameter_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=UML2WithID::Parameter_strategy)
def test_uml2withid::parameter_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original
