import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    OpaqueExpression,
    UML2_Expression,
    UML2_Behavior,
    UML2_OpaqueExpression,
    UML2_ParameterSet,
    Behavior,
    UML2_StateMachine,
    UML2_Interaction,
    UML2_Activity,
    UML2_Parameter,
    StateMachine,
    UML2_ProtocolStateMachine,
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



def test_uml2_expression_is_not_abstract():
    assert not inspect.isabstract(UML2_Expression)


def test_uml2_expression_constructor_exists():
    assert callable(UML2_Expression.__init__)


def test_uml2_expression_constructor_args():
    sig = inspect.signature(UML2_Expression.__init__)
    params = list(sig.parameters.keys())



def test_uml2_behavior_is_not_abstract():
    assert not inspect.isabstract(UML2_Behavior)


def test_uml2_behavior_constructor_exists():
    assert callable(UML2_Behavior.__init__)


def test_uml2_behavior_constructor_args():
    sig = inspect.signature(UML2_Behavior.__init__)
    params = list(sig.parameters.keys())



def test_uml2_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(UML2_OpaqueExpression)


def test_uml2_opaqueexpression_constructor_exists():
    assert callable(UML2_OpaqueExpression.__init__)


def test_uml2_opaqueexpression_constructor_args():
    sig = inspect.signature(UML2_OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml2_parameterset_is_not_abstract():
    assert not inspect.isabstract(UML2_ParameterSet)


def test_uml2_parameterset_constructor_exists():
    assert callable(UML2_ParameterSet.__init__)


def test_uml2_parameterset_constructor_args():
    sig = inspect.signature(UML2_ParameterSet.__init__)
    params = list(sig.parameters.keys())



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_uml2_statemachine_is_not_abstract():
    assert not inspect.isabstract(UML2_StateMachine)


def test_uml2_statemachine_constructor_exists():
    assert callable(UML2_StateMachine.__init__)


def test_uml2_statemachine_constructor_args():
    sig = inspect.signature(UML2_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml2_interaction_is_not_abstract():
    assert not inspect.isabstract(UML2_Interaction)


def test_uml2_interaction_constructor_exists():
    assert callable(UML2_Interaction.__init__)


def test_uml2_interaction_constructor_args():
    sig = inspect.signature(UML2_Interaction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_activity_is_not_abstract():
    assert not inspect.isabstract(UML2_Activity)


def test_uml2_activity_constructor_exists():
    assert callable(UML2_Activity.__init__)


def test_uml2_activity_constructor_args():
    sig = inspect.signature(UML2_Activity.__init__)
    params = list(sig.parameters.keys())



def test_uml2_parameter_is_not_abstract():
    assert not inspect.isabstract(UML2_Parameter)


def test_uml2_parameter_constructor_exists():
    assert callable(UML2_Parameter.__init__)


def test_uml2_parameter_constructor_args():
    sig = inspect.signature(UML2_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_uml2_parameter_has_direction():
    assert hasattr(UML2_Parameter, "direction")
    descriptor = None
    for klass in UML2_Parameter.__mro__:
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



def test_uml2_protocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(UML2_ProtocolStateMachine)


def test_uml2_protocolstatemachine_constructor_exists():
    assert callable(UML2_ProtocolStateMachine.__init__)


def test_uml2_protocolstatemachine_constructor_args():
    sig = inspect.signature(UML2_ProtocolStateMachine.__init__)
    params = list(sig.parameters.keys())

def test_parameterdirectionkind_exists():
    # Check that the Enumeration exists
    assert ParameterDirectionKind is not None

def test_parameterdirectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterDirectionKind]
    expected_literals = [
        "out",
        "in_",
        "return_",
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
UML2_Expression_strategy = st.builds(
    UML2_Expression,
)
UML2_Behavior_strategy = st.builds(
    UML2_Behavior,
)
UML2_OpaqueExpression_strategy = st.builds(
    UML2_OpaqueExpression,
)
UML2_ParameterSet_strategy = st.builds(
    UML2_ParameterSet,
)
Behavior_strategy = st.builds(
    Behavior,
)
UML2_StateMachine_strategy = st.builds(
    UML2_StateMachine,
)
UML2_Interaction_strategy = st.builds(
    UML2_Interaction,
)
UML2_Activity_strategy = st.builds(
    UML2_Activity,
)
UML2_Parameter_strategy = st.builds(
    UML2_Parameter,
    direction=
        safe_text
)
StateMachine_strategy = st.builds(
    StateMachine,
)
UML2_ProtocolStateMachine_strategy = st.builds(
    UML2_ProtocolStateMachine,
)

@given(instance=OpaqueExpression_strategy)
@settings(max_examples=50)
def test_opaqueexpression_instantiation(instance):
    assert isinstance(instance, OpaqueExpression)

@given(instance=UML2_Expression_strategy)
@settings(max_examples=50)
def test_uml2_expression_instantiation(instance):
    assert isinstance(instance, UML2_Expression)

@given(instance=UML2_Behavior_strategy)
@settings(max_examples=50)
def test_uml2_behavior_instantiation(instance):
    assert isinstance(instance, UML2_Behavior)

@given(instance=UML2_OpaqueExpression_strategy)
@settings(max_examples=50)
def test_uml2_opaqueexpression_instantiation(instance):
    assert isinstance(instance, UML2_OpaqueExpression)

@given(instance=UML2_ParameterSet_strategy)
@settings(max_examples=50)
def test_uml2_parameterset_instantiation(instance):
    assert isinstance(instance, UML2_ParameterSet)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=UML2_StateMachine_strategy)
@settings(max_examples=50)
def test_uml2_statemachine_instantiation(instance):
    assert isinstance(instance, UML2_StateMachine)

@given(instance=UML2_Interaction_strategy)
@settings(max_examples=50)
def test_uml2_interaction_instantiation(instance):
    assert isinstance(instance, UML2_Interaction)

@given(instance=UML2_Activity_strategy)
@settings(max_examples=50)
def test_uml2_activity_instantiation(instance):
    assert isinstance(instance, UML2_Activity)

@given(instance=UML2_Parameter_strategy)
@settings(max_examples=50)
def test_uml2_parameter_instantiation(instance):
    assert isinstance(instance, UML2_Parameter)



@given(instance=UML2_Parameter_strategy)
def test_uml2_parameter_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=UML2_ProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_uml2_protocolstatemachine_instantiation(instance):
    assert isinstance(instance, UML2_ProtocolStateMachine)
