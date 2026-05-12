import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    UML2WithID_Element,
    Element,
    UML2WithID_Operation,
    UML2WithID_Parameter,
    ParameterDirectionKind,
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



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_operation_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Operation)


def test_uml2withid_operation_constructor_exists():
    assert callable(UML2WithID_Operation.__init__)


def test_uml2withid_operation_constructor_args():
    sig = inspect.signature(UML2WithID_Operation.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_parameter_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Parameter)


def test_uml2withid_parameter_constructor_exists():
    assert callable(UML2WithID_Parameter.__init__)


def test_uml2withid_parameter_constructor_args():
    sig = inspect.signature(UML2WithID_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_uml2withid_parameter_has_direction():
    assert hasattr(UML2WithID_Parameter, "direction")
    descriptor = None
    for klass in UML2WithID_Parameter.__mro__:
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
        "out",
        "return_",
        "in_",
        "inout",
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
UML2WithID_Element_strategy = st.builds(
    UML2WithID_Element,
    ID=
        safe_text
)
Element_strategy = st.builds(
    Element,
)
UML2WithID_Operation_strategy = st.builds(
    UML2WithID_Operation,
)
UML2WithID_Parameter_strategy = st.builds(
    UML2WithID_Parameter,
    direction=
        safe_text
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

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=UML2WithID_Operation_strategy)
@settings(max_examples=50)
def test_uml2withid_operation_instantiation(instance):
    assert isinstance(instance, UML2WithID_Operation)

@given(instance=UML2WithID_Parameter_strategy)
@settings(max_examples=50)
def test_uml2withid_parameter_instantiation(instance):
    assert isinstance(instance, UML2WithID_Parameter)



@given(instance=UML2WithID_Parameter_strategy)
def test_uml2withid_parameter_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original
