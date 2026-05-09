import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ConsoleOutput,
    fsm::Print,
    fsm::Println,
    Literal,
    fsm::StringLit,
    fsm::BoolLit,
    fsm::IntegerLit,
    Expression,
    fsm::VarReference,
    fsm::ArithmeticExpression,
    fsm::RelationalExpression,
    fsm::Literal,
    fsm::Trigger,
    Statement,
    fsm::ConsoleOutput,
    fsm::VarDecl,
    fsm::Loop,
    fsm::Conditional,
    fsm::Wait,
    fsm::Assignation,
    fsm::Expression,
    Constraint,
    fsm::RelationalConstraint,
    State,
    fsm::FinalState,
    fsm::Constraint,
    fsm::Statement,
    fsm::Program,
    AbstractState,
    fsm::Pseudostate,
    fsm::State,
    fsm::Transition,
    fsm::AbstractState,
    fsm::StateMachine,
    ArithmeticOperator,
    PseudostateKind,
    RelationalOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_consoleoutput_is_not_abstract():
    assert not inspect.isabstract(ConsoleOutput)


def test_consoleoutput_constructor_exists():
    assert callable(ConsoleOutput.__init__)


def test_consoleoutput_constructor_args():
    sig = inspect.signature(ConsoleOutput.__init__)
    params = list(sig.parameters.keys())



def test_fsm::print_is_not_abstract():
    assert not inspect.isabstract(fsm::Print)


def test_fsm::print_constructor_exists():
    assert callable(fsm::Print.__init__)


def test_fsm::print_constructor_args():
    sig = inspect.signature(fsm::Print.__init__)
    params = list(sig.parameters.keys())



def test_fsm::println_is_not_abstract():
    assert not inspect.isabstract(fsm::Println)


def test_fsm::println_constructor_exists():
    assert callable(fsm::Println.__init__)


def test_fsm::println_constructor_args():
    sig = inspect.signature(fsm::Println.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_fsm::stringlit_is_not_abstract():
    assert not inspect.isabstract(fsm::StringLit)


def test_fsm::stringlit_constructor_exists():
    assert callable(fsm::StringLit.__init__)


def test_fsm::stringlit_constructor_args():
    sig = inspect.signature(fsm::StringLit.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fsm::stringlit_has_value():
    assert hasattr(fsm::StringLit, "value")
    descriptor = None
    for klass in fsm::StringLit.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fsm::boollit_is_not_abstract():
    assert not inspect.isabstract(fsm::BoolLit)


def test_fsm::boollit_constructor_exists():
    assert callable(fsm::BoolLit.__init__)


def test_fsm::boollit_constructor_args():
    sig = inspect.signature(fsm::BoolLit.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fsm::boollit_has_value():
    assert hasattr(fsm::BoolLit, "value")
    descriptor = None
    for klass in fsm::BoolLit.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fsm::integerlit_is_not_abstract():
    assert not inspect.isabstract(fsm::IntegerLit)


def test_fsm::integerlit_constructor_exists():
    assert callable(fsm::IntegerLit.__init__)


def test_fsm::integerlit_constructor_args():
    sig = inspect.signature(fsm::IntegerLit.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fsm::integerlit_has_value():
    assert hasattr(fsm::IntegerLit, "value")
    descriptor = None
    for klass in fsm::IntegerLit.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_fsm::varreference_is_not_abstract():
    assert not inspect.isabstract(fsm::VarReference)


def test_fsm::varreference_constructor_exists():
    assert callable(fsm::VarReference.__init__)


def test_fsm::varreference_constructor_args():
    sig = inspect.signature(fsm::VarReference.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_fsm::varreference_has_key():
    assert hasattr(fsm::VarReference, "key")
    descriptor = None
    for klass in fsm::VarReference.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_fsm::arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(fsm::ArithmeticExpression)


def test_fsm::arithmeticexpression_constructor_exists():
    assert callable(fsm::ArithmeticExpression.__init__)


def test_fsm::arithmeticexpression_constructor_args():
    sig = inspect.signature(fsm::ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_fsm::arithmeticexpression_has_operator():
    assert hasattr(fsm::ArithmeticExpression, "operator")
    descriptor = None
    for klass in fsm::ArithmeticExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_fsm::relationalexpression_is_not_abstract():
    assert not inspect.isabstract(fsm::RelationalExpression)


def test_fsm::relationalexpression_constructor_exists():
    assert callable(fsm::RelationalExpression.__init__)


def test_fsm::relationalexpression_constructor_args():
    sig = inspect.signature(fsm::RelationalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_fsm::relationalexpression_has_operator():
    assert hasattr(fsm::RelationalExpression, "operator")
    descriptor = None
    for klass in fsm::RelationalExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_fsm::literal_is_not_abstract():
    assert not inspect.isabstract(fsm::Literal)


def test_fsm::literal_constructor_exists():
    assert callable(fsm::Literal.__init__)


def test_fsm::literal_constructor_args():
    sig = inspect.signature(fsm::Literal.__init__)
    params = list(sig.parameters.keys())



def test_fsm::trigger_is_not_abstract():
    assert not inspect.isabstract(fsm::Trigger)


def test_fsm::trigger_constructor_exists():
    assert callable(fsm::Trigger.__init__)


def test_fsm::trigger_constructor_args():
    sig = inspect.signature(fsm::Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_fsm::trigger_has_expression():
    assert hasattr(fsm::Trigger, "expression")
    descriptor = None
    for klass in fsm::Trigger.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_fsm::consoleoutput_is_not_abstract():
    assert not inspect.isabstract(fsm::ConsoleOutput)


def test_fsm::consoleoutput_constructor_exists():
    assert callable(fsm::ConsoleOutput.__init__)


def test_fsm::consoleoutput_constructor_args():
    sig = inspect.signature(fsm::ConsoleOutput.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"

def test_fsm::consoleoutput_has_input():
    assert hasattr(fsm::ConsoleOutput, "input")
    descriptor = None
    for klass in fsm::ConsoleOutput.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)



def test_fsm::vardecl_is_not_abstract():
    assert not inspect.isabstract(fsm::VarDecl)


def test_fsm::vardecl_constructor_exists():
    assert callable(fsm::VarDecl.__init__)


def test_fsm::vardecl_constructor_args():
    sig = inspect.signature(fsm::VarDecl.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_fsm::vardecl_has_key():
    assert hasattr(fsm::VarDecl, "key")
    descriptor = None
    for klass in fsm::VarDecl.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_fsm::loop_is_not_abstract():
    assert not inspect.isabstract(fsm::Loop)


def test_fsm::loop_constructor_exists():
    assert callable(fsm::Loop.__init__)


def test_fsm::loop_constructor_args():
    sig = inspect.signature(fsm::Loop.__init__)
    params = list(sig.parameters.keys())



def test_fsm::conditional_is_not_abstract():
    assert not inspect.isabstract(fsm::Conditional)


def test_fsm::conditional_constructor_exists():
    assert callable(fsm::Conditional.__init__)


def test_fsm::conditional_constructor_args():
    sig = inspect.signature(fsm::Conditional.__init__)
    params = list(sig.parameters.keys())



def test_fsm::wait_is_not_abstract():
    assert not inspect.isabstract(fsm::Wait)


def test_fsm::wait_constructor_exists():
    assert callable(fsm::Wait.__init__)


def test_fsm::wait_constructor_args():
    sig = inspect.signature(fsm::Wait.__init__)
    params = list(sig.parameters.keys())
    assert "miliseconds" in params, "Missing parameter 'miliseconds'"

def test_fsm::wait_has_miliseconds():
    assert hasattr(fsm::Wait, "miliseconds")
    descriptor = None
    for klass in fsm::Wait.__mro__:
        if "miliseconds" in klass.__dict__:
            descriptor = klass.__dict__["miliseconds"]
            break
    assert isinstance(descriptor, property)



def test_fsm::assignation_is_not_abstract():
    assert not inspect.isabstract(fsm::Assignation)


def test_fsm::assignation_constructor_exists():
    assert callable(fsm::Assignation.__init__)


def test_fsm::assignation_constructor_args():
    sig = inspect.signature(fsm::Assignation.__init__)
    params = list(sig.parameters.keys())



def test_fsm::expression_is_not_abstract():
    assert not inspect.isabstract(fsm::Expression)


def test_fsm::expression_constructor_exists():
    assert callable(fsm::Expression.__init__)


def test_fsm::expression_constructor_args():
    sig = inspect.signature(fsm::Expression.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_fsm::relationalconstraint_is_not_abstract():
    assert not inspect.isabstract(fsm::RelationalConstraint)


def test_fsm::relationalconstraint_constructor_exists():
    assert callable(fsm::RelationalConstraint.__init__)


def test_fsm::relationalconstraint_constructor_args():
    sig = inspect.signature(fsm::RelationalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_fsm::finalstate_is_not_abstract():
    assert not inspect.isabstract(fsm::FinalState)


def test_fsm::finalstate_constructor_exists():
    assert callable(fsm::FinalState.__init__)


def test_fsm::finalstate_constructor_args():
    sig = inspect.signature(fsm::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_fsm::constraint_is_not_abstract():
    assert not inspect.isabstract(fsm::Constraint)


def test_fsm::constraint_constructor_exists():
    assert callable(fsm::Constraint.__init__)


def test_fsm::constraint_constructor_args():
    sig = inspect.signature(fsm::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_fsm::statement_is_not_abstract():
    assert not inspect.isabstract(fsm::Statement)


def test_fsm::statement_constructor_exists():
    assert callable(fsm::Statement.__init__)


def test_fsm::statement_constructor_args():
    sig = inspect.signature(fsm::Statement.__init__)
    params = list(sig.parameters.keys())



def test_fsm::program_is_not_abstract():
    assert not inspect.isabstract(fsm::Program)


def test_fsm::program_constructor_exists():
    assert callable(fsm::Program.__init__)


def test_fsm::program_constructor_args():
    sig = inspect.signature(fsm::Program.__init__)
    params = list(sig.parameters.keys())



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_fsm::pseudostate_is_not_abstract():
    assert not inspect.isabstract(fsm::Pseudostate)


def test_fsm::pseudostate_constructor_exists():
    assert callable(fsm::Pseudostate.__init__)


def test_fsm::pseudostate_constructor_args():
    sig = inspect.signature(fsm::Pseudostate.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_fsm::pseudostate_has_kind():
    assert hasattr(fsm::Pseudostate, "kind")
    descriptor = None
    for klass in fsm::Pseudostate.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_fsm::state_is_not_abstract():
    assert not inspect.isabstract(fsm::State)


def test_fsm::state_constructor_exists():
    assert callable(fsm::State.__init__)


def test_fsm::state_constructor_args():
    sig = inspect.signature(fsm::State.__init__)
    params = list(sig.parameters.keys())



def test_fsm::transition_is_not_abstract():
    assert not inspect.isabstract(fsm::Transition)


def test_fsm::transition_constructor_exists():
    assert callable(fsm::Transition.__init__)


def test_fsm::transition_constructor_args():
    sig = inspect.signature(fsm::Transition.__init__)
    params = list(sig.parameters.keys())



def test_fsm::abstractstate_is_not_abstract():
    assert not inspect.isabstract(fsm::AbstractState)


def test_fsm::abstractstate_constructor_exists():
    assert callable(fsm::AbstractState.__init__)


def test_fsm::abstractstate_constructor_args():
    sig = inspect.signature(fsm::AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::abstractstate_has_name():
    assert hasattr(fsm::AbstractState, "name")
    descriptor = None
    for klass in fsm::AbstractState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm::statemachine_is_not_abstract():
    assert not inspect.isabstract(fsm::StateMachine)


def test_fsm::statemachine_constructor_exists():
    assert callable(fsm::StateMachine.__init__)


def test_fsm::statemachine_constructor_args():
    sig = inspect.signature(fsm::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::statemachine_has_name():
    assert hasattr(fsm::StateMachine, "name")
    descriptor = None
    for klass in fsm::StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_arithmeticoperator_exists():
    # Check that the Enumeration exists
    assert ArithmeticOperator is not None

def test_arithmeticoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArithmeticOperator]
    expected_literals = [
        "mult",
        "minus",
        "div",
        "plus",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArithmeticOperator"

def test_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudostateKind is not None

def test_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudostateKind]
    expected_literals = [
        "initial",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PseudostateKind"

def test_relationaloperator_exists():
    # Check that the Enumeration exists
    assert RelationalOperator is not None

def test_relationaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOperator]
    expected_literals = [
        "notEqual",
        "greaterThan",
        "equals",
        "lessThan",
        "lessThanOrEqualTo",
        "greaterThanOrEqualTo",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOperator"


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
ConsoleOutput_strategy = st.builds(
    ConsoleOutput,
)
fsm::Print_strategy = st.builds(
    fsm::Print,
)
fsm::Println_strategy = st.builds(
    fsm::Println,
)
Literal_strategy = st.builds(
    Literal,
)
fsm::StringLit_strategy = st.builds(
    fsm::StringLit,
    value=
        safe_text
)
fsm::BoolLit_strategy = st.builds(
    fsm::BoolLit,
    value=
        st.booleans()
)
fsm::IntegerLit_strategy = st.builds(
    fsm::IntegerLit,
    value=
        st.integers()
)
Expression_strategy = st.builds(
    Expression,
)
fsm::VarReference_strategy = st.builds(
    fsm::VarReference,
    key=
        safe_text
)
fsm::ArithmeticExpression_strategy = st.builds(
    fsm::ArithmeticExpression,
    operator=
        safe_text
)
fsm::RelationalExpression_strategy = st.builds(
    fsm::RelationalExpression,
    operator=
        safe_text
)
fsm::Literal_strategy = st.builds(
    fsm::Literal,
)
fsm::Trigger_strategy = st.builds(
    fsm::Trigger,
    expression=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
fsm::ConsoleOutput_strategy = st.builds(
    fsm::ConsoleOutput,
    input=
        safe_text
)
fsm::VarDecl_strategy = st.builds(
    fsm::VarDecl,
    key=
        safe_text
)
fsm::Loop_strategy = st.builds(
    fsm::Loop,
)
fsm::Conditional_strategy = st.builds(
    fsm::Conditional,
)
fsm::Wait_strategy = st.builds(
    fsm::Wait,
    miliseconds=
        safe_text
)
fsm::Assignation_strategy = st.builds(
    fsm::Assignation,
)
fsm::Expression_strategy = st.builds(
    fsm::Expression,
)
Constraint_strategy = st.builds(
    Constraint,
)
fsm::RelationalConstraint_strategy = st.builds(
    fsm::RelationalConstraint,
)
State_strategy = st.builds(
    State,
)
fsm::FinalState_strategy = st.builds(
    fsm::FinalState,
)
fsm::Constraint_strategy = st.builds(
    fsm::Constraint,
)
fsm::Statement_strategy = st.builds(
    fsm::Statement,
)
fsm::Program_strategy = st.builds(
    fsm::Program,
)
AbstractState_strategy = st.builds(
    AbstractState,
)
fsm::Pseudostate_strategy = st.builds(
    fsm::Pseudostate,
    kind=
        safe_text
)
fsm::State_strategy = st.builds(
    fsm::State,
)
fsm::Transition_strategy = st.builds(
    fsm::Transition,
)
fsm::AbstractState_strategy = st.builds(
    fsm::AbstractState,
    name=
        safe_text
)
fsm::StateMachine_strategy = st.builds(
    fsm::StateMachine,
    name=
        safe_text
)

@given(instance=ConsoleOutput_strategy)
@settings(max_examples=50)
def test_consoleoutput_instantiation(instance):
    assert isinstance(instance, ConsoleOutput)

@given(instance=fsm::Print_strategy)
@settings(max_examples=50)
def test_fsm::print_instantiation(instance):
    assert isinstance(instance, fsm::Print)

@given(instance=fsm::Println_strategy)
@settings(max_examples=50)
def test_fsm::println_instantiation(instance):
    assert isinstance(instance, fsm::Println)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=fsm::StringLit_strategy)
@settings(max_examples=50)
def test_fsm::stringlit_instantiation(instance):
    assert isinstance(instance, fsm::StringLit)

@given(instance=fsm::StringLit_strategy)
def test_fsm::stringlit_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=fsm::StringLit_strategy)
def test_fsm::stringlit_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fsm::BoolLit_strategy)
@settings(max_examples=50)
def test_fsm::boollit_instantiation(instance):
    assert isinstance(instance, fsm::BoolLit)

@given(instance=fsm::BoolLit_strategy)
def test_fsm::boollit_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=fsm::BoolLit_strategy)
def test_fsm::boollit_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fsm::IntegerLit_strategy)
@settings(max_examples=50)
def test_fsm::integerlit_instantiation(instance):
    assert isinstance(instance, fsm::IntegerLit)

@given(instance=fsm::IntegerLit_strategy)
def test_fsm::integerlit_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fsm::IntegerLit_strategy)
def test_fsm::integerlit_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=fsm::VarReference_strategy)
@settings(max_examples=50)
def test_fsm::varreference_instantiation(instance):
    assert isinstance(instance, fsm::VarReference)

@given(instance=fsm::VarReference_strategy)
def test_fsm::varreference_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=fsm::VarReference_strategy)
def test_fsm::varreference_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=fsm::ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_fsm::arithmeticexpression_instantiation(instance):
    assert isinstance(instance, fsm::ArithmeticExpression)

@given(instance=fsm::ArithmeticExpression_strategy)
def test_fsm::arithmeticexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=fsm::ArithmeticExpression_strategy)
def test_fsm::arithmeticexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=fsm::RelationalExpression_strategy)
@settings(max_examples=50)
def test_fsm::relationalexpression_instantiation(instance):
    assert isinstance(instance, fsm::RelationalExpression)

@given(instance=fsm::RelationalExpression_strategy)
def test_fsm::relationalexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=fsm::RelationalExpression_strategy)
def test_fsm::relationalexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=fsm::Literal_strategy)
@settings(max_examples=50)
def test_fsm::literal_instantiation(instance):
    assert isinstance(instance, fsm::Literal)

@given(instance=fsm::Trigger_strategy)
@settings(max_examples=50)
def test_fsm::trigger_instantiation(instance):
    assert isinstance(instance, fsm::Trigger)

@given(instance=fsm::Trigger_strategy)
def test_fsm::trigger_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=fsm::Trigger_strategy)
def test_fsm::trigger_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=fsm::ConsoleOutput_strategy)
@settings(max_examples=50)
def test_fsm::consoleoutput_instantiation(instance):
    assert isinstance(instance, fsm::ConsoleOutput)

@given(instance=fsm::ConsoleOutput_strategy)
def test_fsm::consoleoutput_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=fsm::ConsoleOutput_strategy)
def test_fsm::consoleoutput_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=fsm::VarDecl_strategy)
@settings(max_examples=50)
def test_fsm::vardecl_instantiation(instance):
    assert isinstance(instance, fsm::VarDecl)

@given(instance=fsm::VarDecl_strategy)
def test_fsm::vardecl_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=fsm::VarDecl_strategy)
def test_fsm::vardecl_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=fsm::Loop_strategy)
@settings(max_examples=50)
def test_fsm::loop_instantiation(instance):
    assert isinstance(instance, fsm::Loop)

@given(instance=fsm::Conditional_strategy)
@settings(max_examples=50)
def test_fsm::conditional_instantiation(instance):
    assert isinstance(instance, fsm::Conditional)

@given(instance=fsm::Wait_strategy)
@settings(max_examples=50)
def test_fsm::wait_instantiation(instance):
    assert isinstance(instance, fsm::Wait)

@given(instance=fsm::Wait_strategy)
def test_fsm::wait_miliseconds_type(instance):
    assert isinstance(instance.miliseconds, str)


@given(instance=fsm::Wait_strategy)
def test_fsm::wait_miliseconds_setter(instance):
    original = instance.miliseconds
    instance.miliseconds = original
    assert instance.miliseconds == original

@given(instance=fsm::Assignation_strategy)
@settings(max_examples=50)
def test_fsm::assignation_instantiation(instance):
    assert isinstance(instance, fsm::Assignation)

@given(instance=fsm::Expression_strategy)
@settings(max_examples=50)
def test_fsm::expression_instantiation(instance):
    assert isinstance(instance, fsm::Expression)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=fsm::RelationalConstraint_strategy)
@settings(max_examples=50)
def test_fsm::relationalconstraint_instantiation(instance):
    assert isinstance(instance, fsm::RelationalConstraint)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=fsm::FinalState_strategy)
@settings(max_examples=50)
def test_fsm::finalstate_instantiation(instance):
    assert isinstance(instance, fsm::FinalState)

@given(instance=fsm::Constraint_strategy)
@settings(max_examples=50)
def test_fsm::constraint_instantiation(instance):
    assert isinstance(instance, fsm::Constraint)

@given(instance=fsm::Statement_strategy)
@settings(max_examples=50)
def test_fsm::statement_instantiation(instance):
    assert isinstance(instance, fsm::Statement)

@given(instance=fsm::Program_strategy)
@settings(max_examples=50)
def test_fsm::program_instantiation(instance):
    assert isinstance(instance, fsm::Program)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=fsm::Pseudostate_strategy)
@settings(max_examples=50)
def test_fsm::pseudostate_instantiation(instance):
    assert isinstance(instance, fsm::Pseudostate)

@given(instance=fsm::Pseudostate_strategy)
def test_fsm::pseudostate_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=fsm::Pseudostate_strategy)
def test_fsm::pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=fsm::State_strategy)
@settings(max_examples=50)
def test_fsm::state_instantiation(instance):
    assert isinstance(instance, fsm::State)

@given(instance=fsm::Transition_strategy)
@settings(max_examples=50)
def test_fsm::transition_instantiation(instance):
    assert isinstance(instance, fsm::Transition)

@given(instance=fsm::AbstractState_strategy)
@settings(max_examples=50)
def test_fsm::abstractstate_instantiation(instance):
    assert isinstance(instance, fsm::AbstractState)

@given(instance=fsm::AbstractState_strategy)
def test_fsm::abstractstate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::AbstractState_strategy)
def test_fsm::abstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm::StateMachine_strategy)
@settings(max_examples=50)
def test_fsm::statemachine_instantiation(instance):
    assert isinstance(instance, fsm::StateMachine)

@given(instance=fsm::StateMachine_strategy)
def test_fsm::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::StateMachine_strategy)
def test_fsm::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
