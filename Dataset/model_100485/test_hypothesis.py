import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    State,
    model::state::StateAutomaton,
    StateAutomaton,
    Var,
    model::state::Action,
    Action,
    model::state::TransitionSegmentSpecification,
    TransitionSegmentSpecification,
    TransitionSegment,
    IExpressionTerm,
    model::expression::BoolConst,
    model::expression::Var,
    model::expression::IExpressionTerm,
    model::INamedElement,
    Port,
    model::component::OutputPort,
    model::component::InputPort,
    INamedElement,
    model::state::State,
    model::state::TransitionSegment,
    model::state::DataStateVariable,
    model::component::Port,
    model::component::Component,
    model::expression::Operation,
    model::expression::IntConst,
    EType,
    EOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_model::state::stateautomaton_is_not_abstract():
    assert not inspect.isabstract(model::state::StateAutomaton)


def test_model::state::stateautomaton_constructor_exists():
    assert callable(model::state::StateAutomaton.__init__)


def test_model::state::stateautomaton_constructor_args():
    sig = inspect.signature(model::state::StateAutomaton.__init__)
    params = list(sig.parameters.keys())



def test_stateautomaton_is_not_abstract():
    assert not inspect.isabstract(StateAutomaton)


def test_stateautomaton_constructor_exists():
    assert callable(StateAutomaton.__init__)


def test_stateautomaton_constructor_args():
    sig = inspect.signature(StateAutomaton.__init__)
    params = list(sig.parameters.keys())



def test_var_is_not_abstract():
    assert not inspect.isabstract(Var)


def test_var_constructor_exists():
    assert callable(Var.__init__)


def test_var_constructor_args():
    sig = inspect.signature(Var.__init__)
    params = list(sig.parameters.keys())



def test_model::state::action_is_not_abstract():
    assert not inspect.isabstract(model::state::Action)


def test_model::state::action_constructor_exists():
    assert callable(model::state::Action.__init__)


def test_model::state::action_constructor_args():
    sig = inspect.signature(model::state::Action.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_model::state::transitionsegmentspecification_is_not_abstract():
    assert not inspect.isabstract(model::state::TransitionSegmentSpecification)


def test_model::state::transitionsegmentspecification_constructor_exists():
    assert callable(model::state::TransitionSegmentSpecification.__init__)


def test_model::state::transitionsegmentspecification_constructor_args():
    sig = inspect.signature(model::state::TransitionSegmentSpecification.__init__)
    params = list(sig.parameters.keys())



def test_transitionsegmentspecification_is_not_abstract():
    assert not inspect.isabstract(TransitionSegmentSpecification)


def test_transitionsegmentspecification_constructor_exists():
    assert callable(TransitionSegmentSpecification.__init__)


def test_transitionsegmentspecification_constructor_args():
    sig = inspect.signature(TransitionSegmentSpecification.__init__)
    params = list(sig.parameters.keys())



def test_transitionsegment_is_not_abstract():
    assert not inspect.isabstract(TransitionSegment)


def test_transitionsegment_constructor_exists():
    assert callable(TransitionSegment.__init__)


def test_transitionsegment_constructor_args():
    sig = inspect.signature(TransitionSegment.__init__)
    params = list(sig.parameters.keys())



def test_iexpressionterm_is_not_abstract():
    assert not inspect.isabstract(IExpressionTerm)


def test_iexpressionterm_constructor_exists():
    assert callable(IExpressionTerm.__init__)


def test_iexpressionterm_constructor_args():
    sig = inspect.signature(IExpressionTerm.__init__)
    params = list(sig.parameters.keys())



def test_model::expression::boolconst_is_not_abstract():
    assert not inspect.isabstract(model::expression::BoolConst)


def test_model::expression::boolconst_constructor_exists():
    assert callable(model::expression::BoolConst.__init__)


def test_model::expression::boolconst_constructor_args():
    sig = inspect.signature(model::expression::BoolConst.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_model::expression::boolconst_has_value():
    assert hasattr(model::expression::BoolConst, "value")
    descriptor = None
    for klass in model::expression::BoolConst.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_model::expression::var_is_not_abstract():
    assert not inspect.isabstract(model::expression::Var)


def test_model::expression::var_constructor_exists():
    assert callable(model::expression::Var.__init__)


def test_model::expression::var_constructor_args():
    sig = inspect.signature(model::expression::Var.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_model::expression::var_has_identifier():
    assert hasattr(model::expression::Var, "identifier")
    descriptor = None
    for klass in model::expression::Var.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_model::expression::iexpressionterm_is_not_abstract():
    assert not inspect.isabstract(model::expression::IExpressionTerm)


def test_model::expression::iexpressionterm_constructor_exists():
    assert callable(model::expression::IExpressionTerm.__init__)


def test_model::expression::iexpressionterm_constructor_args():
    sig = inspect.signature(model::expression::IExpressionTerm.__init__)
    params = list(sig.parameters.keys())



def test_model::inamedelement_is_not_abstract():
    assert not inspect.isabstract(model::INamedElement)


def test_model::inamedelement_constructor_exists():
    assert callable(model::INamedElement.__init__)


def test_model::inamedelement_constructor_args():
    sig = inspect.signature(model::INamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::inamedelement_has_name():
    assert hasattr(model::INamedElement, "name")
    descriptor = None
    for klass in model::INamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_port_constructor_exists():
    assert callable(Port.__init__)


def test_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_model::component::outputport_is_not_abstract():
    assert not inspect.isabstract(model::component::OutputPort)


def test_model::component::outputport_constructor_exists():
    assert callable(model::component::OutputPort.__init__)


def test_model::component::outputport_constructor_args():
    sig = inspect.signature(model::component::OutputPort.__init__)
    params = list(sig.parameters.keys())



def test_model::component::inputport_is_not_abstract():
    assert not inspect.isabstract(model::component::InputPort)


def test_model::component::inputport_constructor_exists():
    assert callable(model::component::InputPort.__init__)


def test_model::component::inputport_constructor_args():
    sig = inspect.signature(model::component::InputPort.__init__)
    params = list(sig.parameters.keys())



def test_inamedelement_is_not_abstract():
    assert not inspect.isabstract(INamedElement)


def test_inamedelement_constructor_exists():
    assert callable(INamedElement.__init__)


def test_inamedelement_constructor_args():
    sig = inspect.signature(INamedElement.__init__)
    params = list(sig.parameters.keys())



def test_model::state::state_is_not_abstract():
    assert not inspect.isabstract(model::state::State)


def test_model::state::state_constructor_exists():
    assert callable(model::state::State.__init__)


def test_model::state::state_constructor_args():
    sig = inspect.signature(model::state::State.__init__)
    params = list(sig.parameters.keys())
    assert "isInitial" in params, "Missing parameter 'isInitial'"

def test_model::state::state_has_isInitial():
    assert hasattr(model::state::State, "isInitial")
    descriptor = None
    for klass in model::state::State.__mro__:
        if "isInitial" in klass.__dict__:
            descriptor = klass.__dict__["isInitial"]
            break
    assert isinstance(descriptor, property)



def test_model::state::transitionsegment_is_not_abstract():
    assert not inspect.isabstract(model::state::TransitionSegment)


def test_model::state::transitionsegment_constructor_exists():
    assert callable(model::state::TransitionSegment.__init__)


def test_model::state::transitionsegment_constructor_args():
    sig = inspect.signature(model::state::TransitionSegment.__init__)
    params = list(sig.parameters.keys())



def test_model::state::datastatevariable_is_not_abstract():
    assert not inspect.isabstract(model::state::DataStateVariable)


def test_model::state::datastatevariable_constructor_exists():
    assert callable(model::state::DataStateVariable.__init__)


def test_model::state::datastatevariable_constructor_args():
    sig = inspect.signature(model::state::DataStateVariable.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_model::state::datastatevariable_has_type():
    assert hasattr(model::state::DataStateVariable, "type")
    descriptor = None
    for klass in model::state::DataStateVariable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_model::component::port_is_not_abstract():
    assert not inspect.isabstract(model::component::Port)


def test_model::component::port_constructor_exists():
    assert callable(model::component::Port.__init__)


def test_model::component::port_constructor_args():
    sig = inspect.signature(model::component::Port.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_model::component::port_has_type():
    assert hasattr(model::component::Port, "type")
    descriptor = None
    for klass in model::component::Port.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_model::component::component_is_not_abstract():
    assert not inspect.isabstract(model::component::Component)


def test_model::component::component_constructor_exists():
    assert callable(model::component::Component.__init__)


def test_model::component::component_constructor_args():
    sig = inspect.signature(model::component::Component.__init__)
    params = list(sig.parameters.keys())



def test_model::expression::operation_is_not_abstract():
    assert not inspect.isabstract(model::expression::Operation)


def test_model::expression::operation_constructor_exists():
    assert callable(model::expression::Operation.__init__)


def test_model::expression::operation_constructor_args():
    sig = inspect.signature(model::expression::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_model::expression::operation_has_operator():
    assert hasattr(model::expression::Operation, "operator")
    descriptor = None
    for klass in model::expression::Operation.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_model::expression::intconst_is_not_abstract():
    assert not inspect.isabstract(model::expression::IntConst)


def test_model::expression::intconst_constructor_exists():
    assert callable(model::expression::IntConst.__init__)


def test_model::expression::intconst_constructor_args():
    sig = inspect.signature(model::expression::IntConst.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_model::expression::intconst_has_value():
    assert hasattr(model::expression::IntConst, "value")
    descriptor = None
    for klass in model::expression::IntConst.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_etype_exists():
    # Check that the Enumeration exists
    assert EType is not None

def test_etype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EType]
    expected_literals = [
        "TBool",
        "TInt",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EType"

def test_eoperator_exists():
    # Check that the Enumeration exists
    assert EOperator is not None

def test_eoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EOperator]
    expected_literals = [
        "And",
        "Divide",
        "Negate",
        "Or",
        "LowerThan",
        "LowerEqual",
        "GreaterThan",
        "GreaterEqual",
        "Add",
        "Equal",
        "NotEqual",
        "Multiply",
        "Not",
        "Subtract",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EOperator"


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
State_strategy = st.builds(
    State,
)
model::state::StateAutomaton_strategy = st.builds(
    model::state::StateAutomaton,
)
StateAutomaton_strategy = st.builds(
    StateAutomaton,
)
Var_strategy = st.builds(
    Var,
)
model::state::Action_strategy = st.builds(
    model::state::Action,
)
Action_strategy = st.builds(
    Action,
)
model::state::TransitionSegmentSpecification_strategy = st.builds(
    model::state::TransitionSegmentSpecification,
)
TransitionSegmentSpecification_strategy = st.builds(
    TransitionSegmentSpecification,
)
TransitionSegment_strategy = st.builds(
    TransitionSegment,
)
IExpressionTerm_strategy = st.builds(
    IExpressionTerm,
)
model::expression::BoolConst_strategy = st.builds(
    model::expression::BoolConst,
    value=
        st.booleans()
)
model::expression::Var_strategy = st.builds(
    model::expression::Var,
    identifier=
        safe_text
)
model::expression::IExpressionTerm_strategy = st.builds(
    model::expression::IExpressionTerm,
)
model::INamedElement_strategy = st.builds(
    model::INamedElement,
    name=
        safe_text
)
Port_strategy = st.builds(
    Port,
)
model::component::OutputPort_strategy = st.builds(
    model::component::OutputPort,
)
model::component::InputPort_strategy = st.builds(
    model::component::InputPort,
)
INamedElement_strategy = st.builds(
    INamedElement,
)
model::state::State_strategy = st.builds(
    model::state::State,
    isInitial=
        st.booleans()
)
model::state::TransitionSegment_strategy = st.builds(
    model::state::TransitionSegment,
)
model::state::DataStateVariable_strategy = st.builds(
    model::state::DataStateVariable,
    type=
        safe_text
)
model::component::Port_strategy = st.builds(
    model::component::Port,
    type=
        safe_text
)
model::component::Component_strategy = st.builds(
    model::component::Component,
)
model::expression::Operation_strategy = st.builds(
    model::expression::Operation,
    operator=
        safe_text
)
model::expression::IntConst_strategy = st.builds(
    model::expression::IntConst,
    value=
        st.integers()
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=model::state::StateAutomaton_strategy)
@settings(max_examples=50)
def test_model::state::stateautomaton_instantiation(instance):
    assert isinstance(instance, model::state::StateAutomaton)

@given(instance=StateAutomaton_strategy)
@settings(max_examples=50)
def test_stateautomaton_instantiation(instance):
    assert isinstance(instance, StateAutomaton)

@given(instance=Var_strategy)
@settings(max_examples=50)
def test_var_instantiation(instance):
    assert isinstance(instance, Var)

@given(instance=model::state::Action_strategy)
@settings(max_examples=50)
def test_model::state::action_instantiation(instance):
    assert isinstance(instance, model::state::Action)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=model::state::TransitionSegmentSpecification_strategy)
@settings(max_examples=50)
def test_model::state::transitionsegmentspecification_instantiation(instance):
    assert isinstance(instance, model::state::TransitionSegmentSpecification)

@given(instance=TransitionSegmentSpecification_strategy)
@settings(max_examples=50)
def test_transitionsegmentspecification_instantiation(instance):
    assert isinstance(instance, TransitionSegmentSpecification)

@given(instance=TransitionSegment_strategy)
@settings(max_examples=50)
def test_transitionsegment_instantiation(instance):
    assert isinstance(instance, TransitionSegment)

@given(instance=IExpressionTerm_strategy)
@settings(max_examples=50)
def test_iexpressionterm_instantiation(instance):
    assert isinstance(instance, IExpressionTerm)

@given(instance=model::expression::BoolConst_strategy)
@settings(max_examples=50)
def test_model::expression::boolconst_instantiation(instance):
    assert isinstance(instance, model::expression::BoolConst)

@given(instance=model::expression::BoolConst_strategy)
def test_model::expression::boolconst_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=model::expression::BoolConst_strategy)
def test_model::expression::boolconst_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model::expression::Var_strategy)
@settings(max_examples=50)
def test_model::expression::var_instantiation(instance):
    assert isinstance(instance, model::expression::Var)

@given(instance=model::expression::Var_strategy)
def test_model::expression::var_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=model::expression::Var_strategy)
def test_model::expression::var_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=model::expression::IExpressionTerm_strategy)
@settings(max_examples=50)
def test_model::expression::iexpressionterm_instantiation(instance):
    assert isinstance(instance, model::expression::IExpressionTerm)

@given(instance=model::INamedElement_strategy)
@settings(max_examples=50)
def test_model::inamedelement_instantiation(instance):
    assert isinstance(instance, model::INamedElement)

@given(instance=model::INamedElement_strategy)
def test_model::inamedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::INamedElement_strategy)
def test_model::inamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=model::component::OutputPort_strategy)
@settings(max_examples=50)
def test_model::component::outputport_instantiation(instance):
    assert isinstance(instance, model::component::OutputPort)

@given(instance=model::component::InputPort_strategy)
@settings(max_examples=50)
def test_model::component::inputport_instantiation(instance):
    assert isinstance(instance, model::component::InputPort)

@given(instance=INamedElement_strategy)
@settings(max_examples=50)
def test_inamedelement_instantiation(instance):
    assert isinstance(instance, INamedElement)

@given(instance=model::state::State_strategy)
@settings(max_examples=50)
def test_model::state::state_instantiation(instance):
    assert isinstance(instance, model::state::State)

@given(instance=model::state::State_strategy)
def test_model::state::state_isInitial_type(instance):
    assert isinstance(instance.isInitial, bool)


@given(instance=model::state::State_strategy)
def test_model::state::state_isInitial_setter(instance):
    original = instance.isInitial
    instance.isInitial = original
    assert instance.isInitial == original

@given(instance=model::state::TransitionSegment_strategy)
@settings(max_examples=50)
def test_model::state::transitionsegment_instantiation(instance):
    assert isinstance(instance, model::state::TransitionSegment)

@given(instance=model::state::DataStateVariable_strategy)
@settings(max_examples=50)
def test_model::state::datastatevariable_instantiation(instance):
    assert isinstance(instance, model::state::DataStateVariable)

@given(instance=model::state::DataStateVariable_strategy)
def test_model::state::datastatevariable_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=model::state::DataStateVariable_strategy)
def test_model::state::datastatevariable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=model::component::Port_strategy)
@settings(max_examples=50)
def test_model::component::port_instantiation(instance):
    assert isinstance(instance, model::component::Port)

@given(instance=model::component::Port_strategy)
def test_model::component::port_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=model::component::Port_strategy)
def test_model::component::port_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=model::component::Component_strategy)
@settings(max_examples=50)
def test_model::component::component_instantiation(instance):
    assert isinstance(instance, model::component::Component)

@given(instance=model::expression::Operation_strategy)
@settings(max_examples=50)
def test_model::expression::operation_instantiation(instance):
    assert isinstance(instance, model::expression::Operation)

@given(instance=model::expression::Operation_strategy)
def test_model::expression::operation_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=model::expression::Operation_strategy)
def test_model::expression::operation_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=model::expression::IntConst_strategy)
@settings(max_examples=50)
def test_model::expression::intconst_instantiation(instance):
    assert isinstance(instance, model::expression::IntConst)

@given(instance=model::expression::IntConst_strategy)
def test_model::expression::intconst_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=model::expression::IntConst_strategy)
def test_model::expression::intconst_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
