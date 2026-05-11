import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Trigger,
    CompleteDSLPckg::AndTrigger,
    CompleteDSLPckg::OrTrigger,
    CompleteDSLPckg::NotTrigger,
    CompleteDSLPckg::NamedElement,
    AbstractState,
    CompleteDSLPckg::State,
    NamedElement,
    CompleteDSLPckg::AbstractState,
    CompleteDSLPckg::Region,
    CompleteDSLPckg::Transition,
    CompleteDSLPckg::StateMachine,
    State,
    CompleteDSLPckg::FinalState,
    Pseudostate,
    CompleteDSLPckg::InitialState,
    CompleteDSLPckg::Pseudostate,
    CompleteDSLPckg::Trigger,
    Statement,
    CompleteDSLPckg::VarDecl,
    CompleteDSLPckg::Loop,
    CompleteDSLPckg::Conditional,
    CompleteDSLPckg::Statement,
    CompleteDSLPckg::Block,
    CompleteDSLPckg::Wait,
    ConsoleOutput,
    CompleteDSLPckg::Print,
    CompleteDSLPckg::Println,
    CompleteDSLPckg::ConsoleOutput,
    CompleteDSLPckg::Assignation,
    Literal,
    CompleteDSLPckg::IntegerLit,
    Expression,
    CompleteDSLPckg::VarRef,
    CompleteDSLPckg::Literal,
    CompleteDSLPckg::Expression,
    CompleteDSLPckg::RelationalExpression,
    CompleteDSLPckg::ArithmeticExpression,
    CompleteDSLPckg::BoolLit,
    CompleteDSLPckg::StringLit,
    RelationalOperator,
    ArithmeticOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trigger_is_not_abstract():
    assert not inspect.isabstract(Trigger)


def test_trigger_constructor_exists():
    assert callable(Trigger.__init__)


def test_trigger_constructor_args():
    sig = inspect.signature(Trigger.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::andtrigger_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::AndTrigger)


def test_completedslpckg::andtrigger_constructor_exists():
    assert callable(CompleteDSLPckg::AndTrigger.__init__)


def test_completedslpckg::andtrigger_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::AndTrigger.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::ortrigger_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::OrTrigger)


def test_completedslpckg::ortrigger_constructor_exists():
    assert callable(CompleteDSLPckg::OrTrigger.__init__)


def test_completedslpckg::ortrigger_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::OrTrigger.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::nottrigger_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::NotTrigger)


def test_completedslpckg::nottrigger_constructor_exists():
    assert callable(CompleteDSLPckg::NotTrigger.__init__)


def test_completedslpckg::nottrigger_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::NotTrigger.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::namedelement_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::NamedElement)


def test_completedslpckg::namedelement_constructor_exists():
    assert callable(CompleteDSLPckg::NamedElement.__init__)


def test_completedslpckg::namedelement_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_completedslpckg::namedelement_has_name():
    assert hasattr(CompleteDSLPckg::NamedElement, "name")
    descriptor = None
    for klass in CompleteDSLPckg::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::state_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::State)


def test_completedslpckg::state_constructor_exists():
    assert callable(CompleteDSLPckg::State.__init__)


def test_completedslpckg::state_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::State.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::abstractstate_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::AbstractState)


def test_completedslpckg::abstractstate_constructor_exists():
    assert callable(CompleteDSLPckg::AbstractState.__init__)


def test_completedslpckg::abstractstate_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::region_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Region)


def test_completedslpckg::region_constructor_exists():
    assert callable(CompleteDSLPckg::Region.__init__)


def test_completedslpckg::region_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Region.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::transition_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Transition)


def test_completedslpckg::transition_constructor_exists():
    assert callable(CompleteDSLPckg::Transition.__init__)


def test_completedslpckg::transition_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Transition.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::statemachine_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::StateMachine)


def test_completedslpckg::statemachine_constructor_exists():
    assert callable(CompleteDSLPckg::StateMachine.__init__)


def test_completedslpckg::statemachine_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::finalstate_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::FinalState)


def test_completedslpckg::finalstate_constructor_exists():
    assert callable(CompleteDSLPckg::FinalState.__init__)


def test_completedslpckg::finalstate_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_pseudostate_is_not_abstract():
    assert not inspect.isabstract(Pseudostate)


def test_pseudostate_constructor_exists():
    assert callable(Pseudostate.__init__)


def test_pseudostate_constructor_args():
    sig = inspect.signature(Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::initialstate_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::InitialState)


def test_completedslpckg::initialstate_constructor_exists():
    assert callable(CompleteDSLPckg::InitialState.__init__)


def test_completedslpckg::initialstate_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::pseudostate_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Pseudostate)


def test_completedslpckg::pseudostate_constructor_exists():
    assert callable(CompleteDSLPckg::Pseudostate.__init__)


def test_completedslpckg::pseudostate_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::trigger_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Trigger)


def test_completedslpckg::trigger_constructor_exists():
    assert callable(CompleteDSLPckg::Trigger.__init__)


def test_completedslpckg::trigger_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_completedslpckg::trigger_has_expression():
    assert hasattr(CompleteDSLPckg::Trigger, "expression")
    descriptor = None
    for klass in CompleteDSLPckg::Trigger.__mro__:
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



def test_completedslpckg::vardecl_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::VarDecl)


def test_completedslpckg::vardecl_constructor_exists():
    assert callable(CompleteDSLPckg::VarDecl.__init__)


def test_completedslpckg::vardecl_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::VarDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_completedslpckg::vardecl_has_name():
    assert hasattr(CompleteDSLPckg::VarDecl, "name")
    descriptor = None
    for klass in CompleteDSLPckg::VarDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::loop_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Loop)


def test_completedslpckg::loop_constructor_exists():
    assert callable(CompleteDSLPckg::Loop.__init__)


def test_completedslpckg::loop_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Loop.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::conditional_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Conditional)


def test_completedslpckg::conditional_constructor_exists():
    assert callable(CompleteDSLPckg::Conditional.__init__)


def test_completedslpckg::conditional_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Conditional.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::statement_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Statement)


def test_completedslpckg::statement_constructor_exists():
    assert callable(CompleteDSLPckg::Statement.__init__)


def test_completedslpckg::statement_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Statement.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::block_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Block)


def test_completedslpckg::block_constructor_exists():
    assert callable(CompleteDSLPckg::Block.__init__)


def test_completedslpckg::block_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Block.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::wait_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Wait)


def test_completedslpckg::wait_constructor_exists():
    assert callable(CompleteDSLPckg::Wait.__init__)


def test_completedslpckg::wait_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Wait.__init__)
    params = list(sig.parameters.keys())
    assert "miliseconds" in params, "Missing parameter 'miliseconds'"

def test_completedslpckg::wait_has_miliseconds():
    assert hasattr(CompleteDSLPckg::Wait, "miliseconds")
    descriptor = None
    for klass in CompleteDSLPckg::Wait.__mro__:
        if "miliseconds" in klass.__dict__:
            descriptor = klass.__dict__["miliseconds"]
            break
    assert isinstance(descriptor, property)



def test_consoleoutput_is_not_abstract():
    assert not inspect.isabstract(ConsoleOutput)


def test_consoleoutput_constructor_exists():
    assert callable(ConsoleOutput.__init__)


def test_consoleoutput_constructor_args():
    sig = inspect.signature(ConsoleOutput.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::print_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Print)


def test_completedslpckg::print_constructor_exists():
    assert callable(CompleteDSLPckg::Print.__init__)


def test_completedslpckg::print_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Print.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::println_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Println)


def test_completedslpckg::println_constructor_exists():
    assert callable(CompleteDSLPckg::Println.__init__)


def test_completedslpckg::println_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Println.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::consoleoutput_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ConsoleOutput)


def test_completedslpckg::consoleoutput_constructor_exists():
    assert callable(CompleteDSLPckg::ConsoleOutput.__init__)


def test_completedslpckg::consoleoutput_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ConsoleOutput.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"

def test_completedslpckg::consoleoutput_has_input():
    assert hasattr(CompleteDSLPckg::ConsoleOutput, "input")
    descriptor = None
    for klass in CompleteDSLPckg::ConsoleOutput.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::assignation_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Assignation)


def test_completedslpckg::assignation_constructor_exists():
    assert callable(CompleteDSLPckg::Assignation.__init__)


def test_completedslpckg::assignation_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Assignation.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::integerlit_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::IntegerLit)


def test_completedslpckg::integerlit_constructor_exists():
    assert callable(CompleteDSLPckg::IntegerLit.__init__)


def test_completedslpckg::integerlit_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::IntegerLit.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_completedslpckg::integerlit_has_value():
    assert hasattr(CompleteDSLPckg::IntegerLit, "value")
    descriptor = None
    for klass in CompleteDSLPckg::IntegerLit.__mro__:
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



def test_completedslpckg::varref_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::VarRef)


def test_completedslpckg::varref_constructor_exists():
    assert callable(CompleteDSLPckg::VarRef.__init__)


def test_completedslpckg::varref_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::VarRef.__init__)
    params = list(sig.parameters.keys())
    assert "ref" in params, "Missing parameter 'ref'"

def test_completedslpckg::varref_has_ref():
    assert hasattr(CompleteDSLPckg::VarRef, "ref")
    descriptor = None
    for klass in CompleteDSLPckg::VarRef.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::literal_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Literal)


def test_completedslpckg::literal_constructor_exists():
    assert callable(CompleteDSLPckg::Literal.__init__)


def test_completedslpckg::literal_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Literal.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::expression_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::Expression)


def test_completedslpckg::expression_constructor_exists():
    assert callable(CompleteDSLPckg::Expression.__init__)


def test_completedslpckg::expression_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::Expression.__init__)
    params = list(sig.parameters.keys())



def test_completedslpckg::relationalexpression_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::RelationalExpression)


def test_completedslpckg::relationalexpression_constructor_exists():
    assert callable(CompleteDSLPckg::RelationalExpression.__init__)


def test_completedslpckg::relationalexpression_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::RelationalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_completedslpckg::relationalexpression_has_operator():
    assert hasattr(CompleteDSLPckg::RelationalExpression, "operator")
    descriptor = None
    for klass in CompleteDSLPckg::RelationalExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::ArithmeticExpression)


def test_completedslpckg::arithmeticexpression_constructor_exists():
    assert callable(CompleteDSLPckg::ArithmeticExpression.__init__)


def test_completedslpckg::arithmeticexpression_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_completedslpckg::arithmeticexpression_has_operator():
    assert hasattr(CompleteDSLPckg::ArithmeticExpression, "operator")
    descriptor = None
    for klass in CompleteDSLPckg::ArithmeticExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::boollit_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::BoolLit)


def test_completedslpckg::boollit_constructor_exists():
    assert callable(CompleteDSLPckg::BoolLit.__init__)


def test_completedslpckg::boollit_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::BoolLit.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_completedslpckg::boollit_has_value():
    assert hasattr(CompleteDSLPckg::BoolLit, "value")
    descriptor = None
    for klass in CompleteDSLPckg::BoolLit.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_completedslpckg::stringlit_is_not_abstract():
    assert not inspect.isabstract(CompleteDSLPckg::StringLit)


def test_completedslpckg::stringlit_constructor_exists():
    assert callable(CompleteDSLPckg::StringLit.__init__)


def test_completedslpckg::stringlit_constructor_args():
    sig = inspect.signature(CompleteDSLPckg::StringLit.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_completedslpckg::stringlit_has_value():
    assert hasattr(CompleteDSLPckg::StringLit, "value")
    descriptor = None
    for klass in CompleteDSLPckg::StringLit.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_relationaloperator_exists():
    # Check that the Enumeration exists
    assert RelationalOperator is not None

def test_relationaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOperator]
    expected_literals = [
        "greaterThan",
        "greaterThanOrEqualTo",
        "notEqual",
        "lessThanOrEqualTo",
        "lessThan",
        "equals",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOperator"

def test_arithmeticoperator_exists():
    # Check that the Enumeration exists
    assert ArithmeticOperator is not None

def test_arithmeticoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArithmeticOperator]
    expected_literals = [
        "mult",
        "plus",
        "minus",
        "div",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArithmeticOperator"


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
Trigger_strategy = st.builds(
    Trigger,
)
CompleteDSLPckg::AndTrigger_strategy = st.builds(
    CompleteDSLPckg::AndTrigger,
)
CompleteDSLPckg::OrTrigger_strategy = st.builds(
    CompleteDSLPckg::OrTrigger,
)
CompleteDSLPckg::NotTrigger_strategy = st.builds(
    CompleteDSLPckg::NotTrigger,
)
CompleteDSLPckg::NamedElement_strategy = st.builds(
    CompleteDSLPckg::NamedElement,
    name=
        safe_text
)
AbstractState_strategy = st.builds(
    AbstractState,
)
CompleteDSLPckg::State_strategy = st.builds(
    CompleteDSLPckg::State,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
CompleteDSLPckg::AbstractState_strategy = st.builds(
    CompleteDSLPckg::AbstractState,
)
CompleteDSLPckg::Region_strategy = st.builds(
    CompleteDSLPckg::Region,
)
CompleteDSLPckg::Transition_strategy = st.builds(
    CompleteDSLPckg::Transition,
)
CompleteDSLPckg::StateMachine_strategy = st.builds(
    CompleteDSLPckg::StateMachine,
)
State_strategy = st.builds(
    State,
)
CompleteDSLPckg::FinalState_strategy = st.builds(
    CompleteDSLPckg::FinalState,
)
Pseudostate_strategy = st.builds(
    Pseudostate,
)
CompleteDSLPckg::InitialState_strategy = st.builds(
    CompleteDSLPckg::InitialState,
)
CompleteDSLPckg::Pseudostate_strategy = st.builds(
    CompleteDSLPckg::Pseudostate,
)
CompleteDSLPckg::Trigger_strategy = st.builds(
    CompleteDSLPckg::Trigger,
    expression=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
CompleteDSLPckg::VarDecl_strategy = st.builds(
    CompleteDSLPckg::VarDecl,
    name=
        safe_text
)
CompleteDSLPckg::Loop_strategy = st.builds(
    CompleteDSLPckg::Loop,
)
CompleteDSLPckg::Conditional_strategy = st.builds(
    CompleteDSLPckg::Conditional,
)
CompleteDSLPckg::Statement_strategy = st.builds(
    CompleteDSLPckg::Statement,
)
CompleteDSLPckg::Block_strategy = st.builds(
    CompleteDSLPckg::Block,
)
CompleteDSLPckg::Wait_strategy = st.builds(
    CompleteDSLPckg::Wait,
    miliseconds=
        safe_text
)
ConsoleOutput_strategy = st.builds(
    ConsoleOutput,
)
CompleteDSLPckg::Print_strategy = st.builds(
    CompleteDSLPckg::Print,
)
CompleteDSLPckg::Println_strategy = st.builds(
    CompleteDSLPckg::Println,
)
CompleteDSLPckg::ConsoleOutput_strategy = st.builds(
    CompleteDSLPckg::ConsoleOutput,
    input=
        safe_text
)
CompleteDSLPckg::Assignation_strategy = st.builds(
    CompleteDSLPckg::Assignation,
)
Literal_strategy = st.builds(
    Literal,
)
CompleteDSLPckg::IntegerLit_strategy = st.builds(
    CompleteDSLPckg::IntegerLit,
    value=
        st.integers()
)
Expression_strategy = st.builds(
    Expression,
)
CompleteDSLPckg::VarRef_strategy = st.builds(
    CompleteDSLPckg::VarRef,
    ref=
        safe_text
)
CompleteDSLPckg::Literal_strategy = st.builds(
    CompleteDSLPckg::Literal,
)
CompleteDSLPckg::Expression_strategy = st.builds(
    CompleteDSLPckg::Expression,
)
CompleteDSLPckg::RelationalExpression_strategy = st.builds(
    CompleteDSLPckg::RelationalExpression,
    operator=
        safe_text
)
CompleteDSLPckg::ArithmeticExpression_strategy = st.builds(
    CompleteDSLPckg::ArithmeticExpression,
    operator=
        safe_text
)
CompleteDSLPckg::BoolLit_strategy = st.builds(
    CompleteDSLPckg::BoolLit,
    value=
        st.booleans()
)
CompleteDSLPckg::StringLit_strategy = st.builds(
    CompleteDSLPckg::StringLit,
    value=
        safe_text
)

@given(instance=Trigger_strategy)
@settings(max_examples=50)
def test_trigger_instantiation(instance):
    assert isinstance(instance, Trigger)

@given(instance=CompleteDSLPckg::AndTrigger_strategy)
@settings(max_examples=50)
def test_completedslpckg::andtrigger_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::AndTrigger)

@given(instance=CompleteDSLPckg::OrTrigger_strategy)
@settings(max_examples=50)
def test_completedslpckg::ortrigger_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::OrTrigger)

@given(instance=CompleteDSLPckg::NotTrigger_strategy)
@settings(max_examples=50)
def test_completedslpckg::nottrigger_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::NotTrigger)

@given(instance=CompleteDSLPckg::NamedElement_strategy)
@settings(max_examples=50)
def test_completedslpckg::namedelement_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::NamedElement)

@given(instance=CompleteDSLPckg::NamedElement_strategy)
def test_completedslpckg::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=CompleteDSLPckg::NamedElement_strategy)
def test_completedslpckg::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=CompleteDSLPckg::State_strategy)
@settings(max_examples=50)
def test_completedslpckg::state_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::State)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=CompleteDSLPckg::AbstractState_strategy)
@settings(max_examples=50)
def test_completedslpckg::abstractstate_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::AbstractState)

@given(instance=CompleteDSLPckg::Region_strategy)
@settings(max_examples=50)
def test_completedslpckg::region_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Region)

@given(instance=CompleteDSLPckg::Transition_strategy)
@settings(max_examples=50)
def test_completedslpckg::transition_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Transition)

@given(instance=CompleteDSLPckg::StateMachine_strategy)
@settings(max_examples=50)
def test_completedslpckg::statemachine_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::StateMachine)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=CompleteDSLPckg::FinalState_strategy)
@settings(max_examples=50)
def test_completedslpckg::finalstate_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::FinalState)

@given(instance=Pseudostate_strategy)
@settings(max_examples=50)
def test_pseudostate_instantiation(instance):
    assert isinstance(instance, Pseudostate)

@given(instance=CompleteDSLPckg::InitialState_strategy)
@settings(max_examples=50)
def test_completedslpckg::initialstate_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::InitialState)

@given(instance=CompleteDSLPckg::Pseudostate_strategy)
@settings(max_examples=50)
def test_completedslpckg::pseudostate_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Pseudostate)

@given(instance=CompleteDSLPckg::Trigger_strategy)
@settings(max_examples=50)
def test_completedslpckg::trigger_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Trigger)

@given(instance=CompleteDSLPckg::Trigger_strategy)
def test_completedslpckg::trigger_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=CompleteDSLPckg::Trigger_strategy)
def test_completedslpckg::trigger_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=CompleteDSLPckg::VarDecl_strategy)
@settings(max_examples=50)
def test_completedslpckg::vardecl_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::VarDecl)

@given(instance=CompleteDSLPckg::VarDecl_strategy)
def test_completedslpckg::vardecl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=CompleteDSLPckg::VarDecl_strategy)
def test_completedslpckg::vardecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CompleteDSLPckg::Loop_strategy)
@settings(max_examples=50)
def test_completedslpckg::loop_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Loop)

@given(instance=CompleteDSLPckg::Conditional_strategy)
@settings(max_examples=50)
def test_completedslpckg::conditional_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Conditional)

@given(instance=CompleteDSLPckg::Statement_strategy)
@settings(max_examples=50)
def test_completedslpckg::statement_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Statement)

@given(instance=CompleteDSLPckg::Block_strategy)
@settings(max_examples=50)
def test_completedslpckg::block_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Block)

@given(instance=CompleteDSLPckg::Wait_strategy)
@settings(max_examples=50)
def test_completedslpckg::wait_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Wait)

@given(instance=CompleteDSLPckg::Wait_strategy)
def test_completedslpckg::wait_miliseconds_type(instance):
    assert isinstance(instance.miliseconds, str)


@given(instance=CompleteDSLPckg::Wait_strategy)
def test_completedslpckg::wait_miliseconds_setter(instance):
    original = instance.miliseconds
    instance.miliseconds = original
    assert instance.miliseconds == original

@given(instance=ConsoleOutput_strategy)
@settings(max_examples=50)
def test_consoleoutput_instantiation(instance):
    assert isinstance(instance, ConsoleOutput)

@given(instance=CompleteDSLPckg::Print_strategy)
@settings(max_examples=50)
def test_completedslpckg::print_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Print)

@given(instance=CompleteDSLPckg::Println_strategy)
@settings(max_examples=50)
def test_completedslpckg::println_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Println)

@given(instance=CompleteDSLPckg::ConsoleOutput_strategy)
@settings(max_examples=50)
def test_completedslpckg::consoleoutput_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ConsoleOutput)

@given(instance=CompleteDSLPckg::ConsoleOutput_strategy)
def test_completedslpckg::consoleoutput_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=CompleteDSLPckg::ConsoleOutput_strategy)
def test_completedslpckg::consoleoutput_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=CompleteDSLPckg::Assignation_strategy)
@settings(max_examples=50)
def test_completedslpckg::assignation_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Assignation)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=CompleteDSLPckg::IntegerLit_strategy)
@settings(max_examples=50)
def test_completedslpckg::integerlit_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::IntegerLit)

@given(instance=CompleteDSLPckg::IntegerLit_strategy)
def test_completedslpckg::integerlit_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=CompleteDSLPckg::IntegerLit_strategy)
def test_completedslpckg::integerlit_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=CompleteDSLPckg::VarRef_strategy)
@settings(max_examples=50)
def test_completedslpckg::varref_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::VarRef)

@given(instance=CompleteDSLPckg::VarRef_strategy)
def test_completedslpckg::varref_ref_type(instance):
    assert isinstance(instance.ref, str)


@given(instance=CompleteDSLPckg::VarRef_strategy)
def test_completedslpckg::varref_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=CompleteDSLPckg::Literal_strategy)
@settings(max_examples=50)
def test_completedslpckg::literal_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Literal)

@given(instance=CompleteDSLPckg::Expression_strategy)
@settings(max_examples=50)
def test_completedslpckg::expression_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::Expression)

@given(instance=CompleteDSLPckg::RelationalExpression_strategy)
@settings(max_examples=50)
def test_completedslpckg::relationalexpression_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::RelationalExpression)

@given(instance=CompleteDSLPckg::RelationalExpression_strategy)
def test_completedslpckg::relationalexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=CompleteDSLPckg::RelationalExpression_strategy)
def test_completedslpckg::relationalexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=CompleteDSLPckg::ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_completedslpckg::arithmeticexpression_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::ArithmeticExpression)

@given(instance=CompleteDSLPckg::ArithmeticExpression_strategy)
def test_completedslpckg::arithmeticexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=CompleteDSLPckg::ArithmeticExpression_strategy)
def test_completedslpckg::arithmeticexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=CompleteDSLPckg::BoolLit_strategy)
@settings(max_examples=50)
def test_completedslpckg::boollit_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::BoolLit)

@given(instance=CompleteDSLPckg::BoolLit_strategy)
def test_completedslpckg::boollit_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=CompleteDSLPckg::BoolLit_strategy)
def test_completedslpckg::boollit_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=CompleteDSLPckg::StringLit_strategy)
@settings(max_examples=50)
def test_completedslpckg::stringlit_instantiation(instance):
    assert isinstance(instance, CompleteDSLPckg::StringLit)

@given(instance=CompleteDSLPckg::StringLit_strategy)
def test_completedslpckg::stringlit_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=CompleteDSLPckg::StringLit_strategy)
def test_completedslpckg::stringlit_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
