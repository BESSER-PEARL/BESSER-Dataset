import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    UML2::MultiplicityElement,
    StructuralFeature,
    UML2::Property,
    InputPin,
    UML2::ValuePin,
    Property,
    UML2::Port,
    UML2::ExtensionEnd,
    MultiplicityElement,
    UML2::StructuralFeature,
    UML2::ConnectorEnd,
    UML2::Pin,
    UML2::Variable,
    UML2::Operation,
    Pin,
    UML2::OutputPin,
    UML2::InputPin,
    UML2::Parameter,
    ParameterDirectionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uml2::multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(UML2::MultiplicityElement)


def test_uml2::multiplicityelement_constructor_exists():
    assert callable(UML2::MultiplicityElement.__init__)


def test_uml2::multiplicityelement_constructor_args():
    sig = inspect.signature(UML2::MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"

def test_uml2::multiplicityelement_has_upper():
    assert hasattr(UML2::MultiplicityElement, "upper")
    descriptor = None
    for klass in UML2::MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
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



def test_inputpin_is_not_abstract():
    assert not inspect.isabstract(InputPin)


def test_inputpin_constructor_exists():
    assert callable(InputPin.__init__)


def test_inputpin_constructor_args():
    sig = inspect.signature(InputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml2::valuepin_is_not_abstract():
    assert not inspect.isabstract(UML2::ValuePin)


def test_uml2::valuepin_constructor_exists():
    assert callable(UML2::ValuePin.__init__)


def test_uml2::valuepin_constructor_args():
    sig = inspect.signature(UML2::ValuePin.__init__)
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



def test_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(MultiplicityElement)


def test_multiplicityelement_constructor_exists():
    assert callable(MultiplicityElement.__init__)


def test_multiplicityelement_constructor_args():
    sig = inspect.signature(MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2::structuralfeature_is_not_abstract():
    assert not inspect.isabstract(UML2::StructuralFeature)


def test_uml2::structuralfeature_constructor_exists():
    assert callable(UML2::StructuralFeature.__init__)


def test_uml2::structuralfeature_constructor_args():
    sig = inspect.signature(UML2::StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml2::connectorend_is_not_abstract():
    assert not inspect.isabstract(UML2::ConnectorEnd)


def test_uml2::connectorend_constructor_exists():
    assert callable(UML2::ConnectorEnd.__init__)


def test_uml2::connectorend_constructor_args():
    sig = inspect.signature(UML2::ConnectorEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml2::pin_is_not_abstract():
    assert not inspect.isabstract(UML2::Pin)


def test_uml2::pin_constructor_exists():
    assert callable(UML2::Pin.__init__)


def test_uml2::pin_constructor_args():
    sig = inspect.signature(UML2::Pin.__init__)
    params = list(sig.parameters.keys())



def test_uml2::variable_is_not_abstract():
    assert not inspect.isabstract(UML2::Variable)


def test_uml2::variable_constructor_exists():
    assert callable(UML2::Variable.__init__)


def test_uml2::variable_constructor_args():
    sig = inspect.signature(UML2::Variable.__init__)
    params = list(sig.parameters.keys())



def test_uml2::operation_is_not_abstract():
    assert not inspect.isabstract(UML2::Operation)


def test_uml2::operation_constructor_exists():
    assert callable(UML2::Operation.__init__)


def test_uml2::operation_constructor_args():
    sig = inspect.signature(UML2::Operation.__init__)
    params = list(sig.parameters.keys())



def test_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_uml2::outputpin_is_not_abstract():
    assert not inspect.isabstract(UML2::OutputPin)


def test_uml2::outputpin_constructor_exists():
    assert callable(UML2::OutputPin.__init__)


def test_uml2::outputpin_constructor_args():
    sig = inspect.signature(UML2::OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml2::inputpin_is_not_abstract():
    assert not inspect.isabstract(UML2::InputPin)


def test_uml2::inputpin_constructor_exists():
    assert callable(UML2::InputPin.__init__)


def test_uml2::inputpin_constructor_args():
    sig = inspect.signature(UML2::InputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml2::parameter_is_not_abstract():
    assert not inspect.isabstract(UML2::Parameter)


def test_uml2::parameter_constructor_exists():
    assert callable(UML2::Parameter.__init__)


def test_uml2::parameter_constructor_args():
    sig = inspect.signature(UML2::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_uml2::parameter_has_direction():
    assert hasattr(UML2::Parameter, "direction")
    descriptor = None
    for klass in UML2::Parameter.__mro__:
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
        "return_",
        "in_",
        "out",
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
UML2::MultiplicityElement_strategy = st.builds(
    UML2::MultiplicityElement,
    upper=
        safe_text
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
UML2::Property_strategy = st.builds(
    UML2::Property,
)
InputPin_strategy = st.builds(
    InputPin,
)
UML2::ValuePin_strategy = st.builds(
    UML2::ValuePin,
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
MultiplicityElement_strategy = st.builds(
    MultiplicityElement,
)
UML2::StructuralFeature_strategy = st.builds(
    UML2::StructuralFeature,
)
UML2::ConnectorEnd_strategy = st.builds(
    UML2::ConnectorEnd,
)
UML2::Pin_strategy = st.builds(
    UML2::Pin,
)
UML2::Variable_strategy = st.builds(
    UML2::Variable,
)
UML2::Operation_strategy = st.builds(
    UML2::Operation,
)
Pin_strategy = st.builds(
    Pin,
)
UML2::OutputPin_strategy = st.builds(
    UML2::OutputPin,
)
UML2::InputPin_strategy = st.builds(
    UML2::InputPin,
)
UML2::Parameter_strategy = st.builds(
    UML2::Parameter,
    direction=
        safe_text
)

@given(instance=UML2::MultiplicityElement_strategy)
@settings(max_examples=50)
def test_uml2::multiplicityelement_instantiation(instance):
    assert isinstance(instance, UML2::MultiplicityElement)

@given(instance=UML2::MultiplicityElement_strategy)
def test_uml2::multiplicityelement_upper_type(instance):
    assert isinstance(instance.upper, str)


@given(instance=UML2::MultiplicityElement_strategy)
def test_uml2::multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=UML2::Property_strategy)
@settings(max_examples=50)
def test_uml2::property_instantiation(instance):
    assert isinstance(instance, UML2::Property)

@given(instance=InputPin_strategy)
@settings(max_examples=50)
def test_inputpin_instantiation(instance):
    assert isinstance(instance, InputPin)

@given(instance=UML2::ValuePin_strategy)
@settings(max_examples=50)
def test_uml2::valuepin_instantiation(instance):
    assert isinstance(instance, UML2::ValuePin)

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

@given(instance=MultiplicityElement_strategy)
@settings(max_examples=50)
def test_multiplicityelement_instantiation(instance):
    assert isinstance(instance, MultiplicityElement)

@given(instance=UML2::StructuralFeature_strategy)
@settings(max_examples=50)
def test_uml2::structuralfeature_instantiation(instance):
    assert isinstance(instance, UML2::StructuralFeature)

@given(instance=UML2::ConnectorEnd_strategy)
@settings(max_examples=50)
def test_uml2::connectorend_instantiation(instance):
    assert isinstance(instance, UML2::ConnectorEnd)

@given(instance=UML2::Pin_strategy)
@settings(max_examples=50)
def test_uml2::pin_instantiation(instance):
    assert isinstance(instance, UML2::Pin)

@given(instance=UML2::Variable_strategy)
@settings(max_examples=50)
def test_uml2::variable_instantiation(instance):
    assert isinstance(instance, UML2::Variable)

@given(instance=UML2::Operation_strategy)
@settings(max_examples=50)
def test_uml2::operation_instantiation(instance):
    assert isinstance(instance, UML2::Operation)

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=UML2::OutputPin_strategy)
@settings(max_examples=50)
def test_uml2::outputpin_instantiation(instance):
    assert isinstance(instance, UML2::OutputPin)

@given(instance=UML2::InputPin_strategy)
@settings(max_examples=50)
def test_uml2::inputpin_instantiation(instance):
    assert isinstance(instance, UML2::InputPin)

@given(instance=UML2::Parameter_strategy)
@settings(max_examples=50)
def test_uml2::parameter_instantiation(instance):
    assert isinstance(instance, UML2::Parameter)

@given(instance=UML2::Parameter_strategy)
def test_uml2::parameter_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=UML2::Parameter_strategy)
def test_uml2::parameter_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original
