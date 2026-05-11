import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    OpaqueExpression,
    UML2::Expression,
    UML2::Behavior,
    UML2::OpaqueExpression,
    UML2::ParameterSet,
    Behavior,
    UML2::StateMachine,
    UML2::Interaction,
    UML2::Activity,
    UML2::Parameter,
    StateMachine,
    UML2::ProtocolStateMachine,
    ParameterDirectionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(OpaqueExpression)


def test_opaqueexpression_constructor_exists():
    assert callable(OpaqueExpression.__init__)


def test_opaqueexpression_constructor_args():
    sig = inspect.signature(OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml2::expression_is_not_abstract():
    assert not inspect.isabstract(UML2::Expression)


def test_uml2::expression_constructor_exists():
    assert callable(UML2::Expression.__init__)


def test_uml2::expression_constructor_args():
    sig = inspect.signature(UML2::Expression.__init__)
    params = list(sig.parameters.keys())



def test_uml2::behavior_is_not_abstract():
    assert not inspect.isabstract(UML2::Behavior)


def test_uml2::behavior_constructor_exists():
    assert callable(UML2::Behavior.__init__)


def test_uml2::behavior_constructor_args():
    sig = inspect.signature(UML2::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_uml2::opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(UML2::OpaqueExpression)


def test_uml2::opaqueexpression_constructor_exists():
    assert callable(UML2::OpaqueExpression.__init__)


def test_uml2::opaqueexpression_constructor_args():
    sig = inspect.signature(UML2::OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml2::parameterset_is_not_abstract():
    assert not inspect.isabstract(UML2::ParameterSet)


def test_uml2::parameterset_constructor_exists():
    assert callable(UML2::ParameterSet.__init__)


def test_uml2::parameterset_constructor_args():
    sig = inspect.signature(UML2::ParameterSet.__init__)
    params = list(sig.parameters.keys())



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_uml2::statemachine_is_not_abstract():
    assert not inspect.isabstract(UML2::StateMachine)


def test_uml2::statemachine_constructor_exists():
    assert callable(UML2::StateMachine.__init__)


def test_uml2::statemachine_constructor_args():
    sig = inspect.signature(UML2::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml2::interaction_is_not_abstract():
    assert not inspect.isabstract(UML2::Interaction)


def test_uml2::interaction_constructor_exists():
    assert callable(UML2::Interaction.__init__)


def test_uml2::interaction_constructor_args():
    sig = inspect.signature(UML2::Interaction.__init__)
    params = list(sig.parameters.keys())



def test_uml2::activity_is_not_abstract():
    assert not inspect.isabstract(UML2::Activity)


def test_uml2::activity_constructor_exists():
    assert callable(UML2::Activity.__init__)


def test_uml2::activity_constructor_args():
    sig = inspect.signature(UML2::Activity.__init__)
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



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml2::protocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(UML2::ProtocolStateMachine)


def test_uml2::protocolstatemachine_constructor_exists():
    assert callable(UML2::ProtocolStateMachine.__init__)


def test_uml2::protocolstatemachine_constructor_args():
    sig = inspect.signature(UML2::ProtocolStateMachine.__init__)
    params = list(sig.parameters.keys())

def test_parameterdirectionkind_exists():
    # Check that the Enumeration exists
    assert ParameterDirectionKind is not None

def test_parameterdirectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterDirectionKind]
    expected_literals = [
        "in_",
        "return_",
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
OpaqueExpression_strategy = st.builds(
    OpaqueExpression,
)
UML2::Expression_strategy = st.builds(
    UML2::Expression,
)
UML2::Behavior_strategy = st.builds(
    UML2::Behavior,
)
UML2::OpaqueExpression_strategy = st.builds(
    UML2::OpaqueExpression,
)
UML2::ParameterSet_strategy = st.builds(
    UML2::ParameterSet,
)
Behavior_strategy = st.builds(
    Behavior,
)
UML2::StateMachine_strategy = st.builds(
    UML2::StateMachine,
)
UML2::Interaction_strategy = st.builds(
    UML2::Interaction,
)
UML2::Activity_strategy = st.builds(
    UML2::Activity,
)
UML2::Parameter_strategy = st.builds(
    UML2::Parameter,
    direction=
        safe_text
)
StateMachine_strategy = st.builds(
    StateMachine,
)
UML2::ProtocolStateMachine_strategy = st.builds(
    UML2::ProtocolStateMachine,
)

@given(instance=OpaqueExpression_strategy)
@settings(max_examples=50)
def test_opaqueexpression_instantiation(instance):
    assert isinstance(instance, OpaqueExpression)

@given(instance=UML2::Expression_strategy)
@settings(max_examples=50)
def test_uml2::expression_instantiation(instance):
    assert isinstance(instance, UML2::Expression)

@given(instance=UML2::Behavior_strategy)
@settings(max_examples=50)
def test_uml2::behavior_instantiation(instance):
    assert isinstance(instance, UML2::Behavior)

@given(instance=UML2::OpaqueExpression_strategy)
@settings(max_examples=50)
def test_uml2::opaqueexpression_instantiation(instance):
    assert isinstance(instance, UML2::OpaqueExpression)

@given(instance=UML2::ParameterSet_strategy)
@settings(max_examples=50)
def test_uml2::parameterset_instantiation(instance):
    assert isinstance(instance, UML2::ParameterSet)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=UML2::StateMachine_strategy)
@settings(max_examples=50)
def test_uml2::statemachine_instantiation(instance):
    assert isinstance(instance, UML2::StateMachine)

@given(instance=UML2::Interaction_strategy)
@settings(max_examples=50)
def test_uml2::interaction_instantiation(instance):
    assert isinstance(instance, UML2::Interaction)

@given(instance=UML2::Activity_strategy)
@settings(max_examples=50)
def test_uml2::activity_instantiation(instance):
    assert isinstance(instance, UML2::Activity)

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

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=UML2::ProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_uml2::protocolstatemachine_instantiation(instance):
    assert isinstance(instance, UML2::ProtocolStateMachine)
