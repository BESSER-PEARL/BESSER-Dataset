import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fsm::Expression,
    Statement,
    fsm::Loop,
    fsm::Context,
    State,
    fsm::FinalState,
    Literal,
    fsm::String,
    fsm::VarRef,
    fsm::Real,
    fsm::Boolean,
    fsm::Integer,
    Expression,
    fsm::ArithmeticExpression,
    fsm::Literal,
    fsm::RelationalExpression,
    fsm::Assignation,
    fsm::VarDecl,
    fsm::Conditional,
    fsm::Trigger,
    fsm::Block,
    AbstractState,
    Pseudostate,
    fsm::ShallowHistory,
    fsm::Junction,
    fsm::Condition,
    fsm::Fork,
    fsm::DeepHistory,
    fsm::Join,
    fsm::InitialState,
    fsm::Pseudostate,
    Trigger,
    fsm::AndTrigger,
    fsm::OrTrigger,
    fsm::NotTrigger,
    fsm::Constraint,
    fsm::Statement,
    fsm::State,
    fsm::Transition,
    fsm::AbstractState,
    fsm::Region,
    fsm::StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm::expression_is_not_abstract():
    assert not inspect.isabstract(fsm::Expression)


def test_fsm::expression_constructor_exists():
    assert callable(fsm::Expression.__init__)


def test_fsm::expression_constructor_args():
    sig = inspect.signature(fsm::Expression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_fsm::loop_is_not_abstract():
    assert not inspect.isabstract(fsm::Loop)


def test_fsm::loop_constructor_exists():
    assert callable(fsm::Loop.__init__)


def test_fsm::loop_constructor_args():
    sig = inspect.signature(fsm::Loop.__init__)
    params = list(sig.parameters.keys())



def test_fsm::context_is_not_abstract():
    assert not inspect.isabstract(fsm::Context)


def test_fsm::context_constructor_exists():
    assert callable(fsm::Context.__init__)


def test_fsm::context_constructor_args():
    sig = inspect.signature(fsm::Context.__init__)
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



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_fsm::string_is_not_abstract():
    assert not inspect.isabstract(fsm::String)


def test_fsm::string_constructor_exists():
    assert callable(fsm::String.__init__)


def test_fsm::string_constructor_args():
    sig = inspect.signature(fsm::String.__init__)
    params = list(sig.parameters.keys())



def test_fsm::varref_is_not_abstract():
    assert not inspect.isabstract(fsm::VarRef)


def test_fsm::varref_constructor_exists():
    assert callable(fsm::VarRef.__init__)


def test_fsm::varref_constructor_args():
    sig = inspect.signature(fsm::VarRef.__init__)
    params = list(sig.parameters.keys())
    assert "varId" in params, "Missing parameter 'varId'"

def test_fsm::varref_has_varId():
    assert hasattr(fsm::VarRef, "varId")
    descriptor = None
    for klass in fsm::VarRef.__mro__:
        if "varId" in klass.__dict__:
            descriptor = klass.__dict__["varId"]
            break
    assert isinstance(descriptor, property)



def test_fsm::real_is_not_abstract():
    assert not inspect.isabstract(fsm::Real)


def test_fsm::real_constructor_exists():
    assert callable(fsm::Real.__init__)


def test_fsm::real_constructor_args():
    sig = inspect.signature(fsm::Real.__init__)
    params = list(sig.parameters.keys())



def test_fsm::boolean_is_not_abstract():
    assert not inspect.isabstract(fsm::Boolean)


def test_fsm::boolean_constructor_exists():
    assert callable(fsm::Boolean.__init__)


def test_fsm::boolean_constructor_args():
    sig = inspect.signature(fsm::Boolean.__init__)
    params = list(sig.parameters.keys())



def test_fsm::integer_is_not_abstract():
    assert not inspect.isabstract(fsm::Integer)


def test_fsm::integer_constructor_exists():
    assert callable(fsm::Integer.__init__)


def test_fsm::integer_constructor_args():
    sig = inspect.signature(fsm::Integer.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_fsm::arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(fsm::ArithmeticExpression)


def test_fsm::arithmeticexpression_constructor_exists():
    assert callable(fsm::ArithmeticExpression.__init__)


def test_fsm::arithmeticexpression_constructor_args():
    sig = inspect.signature(fsm::ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_fsm::literal_is_not_abstract():
    assert not inspect.isabstract(fsm::Literal)


def test_fsm::literal_constructor_exists():
    assert callable(fsm::Literal.__init__)


def test_fsm::literal_constructor_args():
    sig = inspect.signature(fsm::Literal.__init__)
    params = list(sig.parameters.keys())



def test_fsm::relationalexpression_is_not_abstract():
    assert not inspect.isabstract(fsm::RelationalExpression)


def test_fsm::relationalexpression_constructor_exists():
    assert callable(fsm::RelationalExpression.__init__)


def test_fsm::relationalexpression_constructor_args():
    sig = inspect.signature(fsm::RelationalExpression.__init__)
    params = list(sig.parameters.keys())



def test_fsm::assignation_is_not_abstract():
    assert not inspect.isabstract(fsm::Assignation)


def test_fsm::assignation_constructor_exists():
    assert callable(fsm::Assignation.__init__)


def test_fsm::assignation_constructor_args():
    sig = inspect.signature(fsm::Assignation.__init__)
    params = list(sig.parameters.keys())



def test_fsm::vardecl_is_not_abstract():
    assert not inspect.isabstract(fsm::VarDecl)


def test_fsm::vardecl_constructor_exists():
    assert callable(fsm::VarDecl.__init__)


def test_fsm::vardecl_constructor_args():
    sig = inspect.signature(fsm::VarDecl.__init__)
    params = list(sig.parameters.keys())



def test_fsm::conditional_is_not_abstract():
    assert not inspect.isabstract(fsm::Conditional)


def test_fsm::conditional_constructor_exists():
    assert callable(fsm::Conditional.__init__)


def test_fsm::conditional_constructor_args():
    sig = inspect.signature(fsm::Conditional.__init__)
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



def test_fsm::block_is_not_abstract():
    assert not inspect.isabstract(fsm::Block)


def test_fsm::block_constructor_exists():
    assert callable(fsm::Block.__init__)


def test_fsm::block_constructor_args():
    sig = inspect.signature(fsm::Block.__init__)
    params = list(sig.parameters.keys())



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_pseudostate_is_not_abstract():
    assert not inspect.isabstract(Pseudostate)


def test_pseudostate_constructor_exists():
    assert callable(Pseudostate.__init__)


def test_pseudostate_constructor_args():
    sig = inspect.signature(Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_fsm::shallowhistory_is_not_abstract():
    assert not inspect.isabstract(fsm::ShallowHistory)


def test_fsm::shallowhistory_constructor_exists():
    assert callable(fsm::ShallowHistory.__init__)


def test_fsm::shallowhistory_constructor_args():
    sig = inspect.signature(fsm::ShallowHistory.__init__)
    params = list(sig.parameters.keys())



def test_fsm::junction_is_not_abstract():
    assert not inspect.isabstract(fsm::Junction)


def test_fsm::junction_constructor_exists():
    assert callable(fsm::Junction.__init__)


def test_fsm::junction_constructor_args():
    sig = inspect.signature(fsm::Junction.__init__)
    params = list(sig.parameters.keys())



def test_fsm::condition_is_not_abstract():
    assert not inspect.isabstract(fsm::Condition)


def test_fsm::condition_constructor_exists():
    assert callable(fsm::Condition.__init__)


def test_fsm::condition_constructor_args():
    sig = inspect.signature(fsm::Condition.__init__)
    params = list(sig.parameters.keys())



def test_fsm::fork_is_not_abstract():
    assert not inspect.isabstract(fsm::Fork)


def test_fsm::fork_constructor_exists():
    assert callable(fsm::Fork.__init__)


def test_fsm::fork_constructor_args():
    sig = inspect.signature(fsm::Fork.__init__)
    params = list(sig.parameters.keys())



def test_fsm::deephistory_is_not_abstract():
    assert not inspect.isabstract(fsm::DeepHistory)


def test_fsm::deephistory_constructor_exists():
    assert callable(fsm::DeepHistory.__init__)


def test_fsm::deephistory_constructor_args():
    sig = inspect.signature(fsm::DeepHistory.__init__)
    params = list(sig.parameters.keys())



def test_fsm::join_is_not_abstract():
    assert not inspect.isabstract(fsm::Join)


def test_fsm::join_constructor_exists():
    assert callable(fsm::Join.__init__)


def test_fsm::join_constructor_args():
    sig = inspect.signature(fsm::Join.__init__)
    params = list(sig.parameters.keys())



def test_fsm::initialstate_is_not_abstract():
    assert not inspect.isabstract(fsm::InitialState)


def test_fsm::initialstate_constructor_exists():
    assert callable(fsm::InitialState.__init__)


def test_fsm::initialstate_constructor_args():
    sig = inspect.signature(fsm::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_fsm::pseudostate_is_not_abstract():
    assert not inspect.isabstract(fsm::Pseudostate)


def test_fsm::pseudostate_constructor_exists():
    assert callable(fsm::Pseudostate.__init__)


def test_fsm::pseudostate_constructor_args():
    sig = inspect.signature(fsm::Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_trigger_is_not_abstract():
    assert not inspect.isabstract(Trigger)


def test_trigger_constructor_exists():
    assert callable(Trigger.__init__)


def test_trigger_constructor_args():
    sig = inspect.signature(Trigger.__init__)
    params = list(sig.parameters.keys())



def test_fsm::andtrigger_is_not_abstract():
    assert not inspect.isabstract(fsm::AndTrigger)


def test_fsm::andtrigger_constructor_exists():
    assert callable(fsm::AndTrigger.__init__)


def test_fsm::andtrigger_constructor_args():
    sig = inspect.signature(fsm::AndTrigger.__init__)
    params = list(sig.parameters.keys())



def test_fsm::ortrigger_is_not_abstract():
    assert not inspect.isabstract(fsm::OrTrigger)


def test_fsm::ortrigger_constructor_exists():
    assert callable(fsm::OrTrigger.__init__)


def test_fsm::ortrigger_constructor_args():
    sig = inspect.signature(fsm::OrTrigger.__init__)
    params = list(sig.parameters.keys())



def test_fsm::nottrigger_is_not_abstract():
    assert not inspect.isabstract(fsm::NotTrigger)


def test_fsm::nottrigger_constructor_exists():
    assert callable(fsm::NotTrigger.__init__)


def test_fsm::nottrigger_constructor_args():
    sig = inspect.signature(fsm::NotTrigger.__init__)
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



def test_fsm::region_is_not_abstract():
    assert not inspect.isabstract(fsm::Region)


def test_fsm::region_constructor_exists():
    assert callable(fsm::Region.__init__)


def test_fsm::region_constructor_args():
    sig = inspect.signature(fsm::Region.__init__)
    params = list(sig.parameters.keys())



def test_fsm::statemachine_is_not_abstract():
    assert not inspect.isabstract(fsm::StateMachine)


def test_fsm::statemachine_constructor_exists():
    assert callable(fsm::StateMachine.__init__)


def test_fsm::statemachine_constructor_args():
    sig = inspect.signature(fsm::StateMachine.__init__)
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
fsm::Expression_strategy = st.builds(
    fsm::Expression,
)
Statement_strategy = st.builds(
    Statement,
)
fsm::Loop_strategy = st.builds(
    fsm::Loop,
)
fsm::Context_strategy = st.builds(
    fsm::Context,
)
State_strategy = st.builds(
    State,
)
fsm::FinalState_strategy = st.builds(
    fsm::FinalState,
)
Literal_strategy = st.builds(
    Literal,
)
fsm::String_strategy = st.builds(
    fsm::String,
)
fsm::VarRef_strategy = st.builds(
    fsm::VarRef,
    varId=
        safe_text
)
fsm::Real_strategy = st.builds(
    fsm::Real,
)
fsm::Boolean_strategy = st.builds(
    fsm::Boolean,
)
fsm::Integer_strategy = st.builds(
    fsm::Integer,
)
Expression_strategy = st.builds(
    Expression,
)
fsm::ArithmeticExpression_strategy = st.builds(
    fsm::ArithmeticExpression,
)
fsm::Literal_strategy = st.builds(
    fsm::Literal,
)
fsm::RelationalExpression_strategy = st.builds(
    fsm::RelationalExpression,
)
fsm::Assignation_strategy = st.builds(
    fsm::Assignation,
)
fsm::VarDecl_strategy = st.builds(
    fsm::VarDecl,
)
fsm::Conditional_strategy = st.builds(
    fsm::Conditional,
)
fsm::Trigger_strategy = st.builds(
    fsm::Trigger,
    expression=
        safe_text
)
fsm::Block_strategy = st.builds(
    fsm::Block,
)
AbstractState_strategy = st.builds(
    AbstractState,
)
Pseudostate_strategy = st.builds(
    Pseudostate,
)
fsm::ShallowHistory_strategy = st.builds(
    fsm::ShallowHistory,
)
fsm::Junction_strategy = st.builds(
    fsm::Junction,
)
fsm::Condition_strategy = st.builds(
    fsm::Condition,
)
fsm::Fork_strategy = st.builds(
    fsm::Fork,
)
fsm::DeepHistory_strategy = st.builds(
    fsm::DeepHistory,
)
fsm::Join_strategy = st.builds(
    fsm::Join,
)
fsm::InitialState_strategy = st.builds(
    fsm::InitialState,
)
fsm::Pseudostate_strategy = st.builds(
    fsm::Pseudostate,
)
Trigger_strategy = st.builds(
    Trigger,
)
fsm::AndTrigger_strategy = st.builds(
    fsm::AndTrigger,
)
fsm::OrTrigger_strategy = st.builds(
    fsm::OrTrigger,
)
fsm::NotTrigger_strategy = st.builds(
    fsm::NotTrigger,
)
fsm::Constraint_strategy = st.builds(
    fsm::Constraint,
)
fsm::Statement_strategy = st.builds(
    fsm::Statement,
)
fsm::State_strategy = st.builds(
    fsm::State,
)
fsm::Transition_strategy = st.builds(
    fsm::Transition,
)
fsm::AbstractState_strategy = st.builds(
    fsm::AbstractState,
)
fsm::Region_strategy = st.builds(
    fsm::Region,
)
fsm::StateMachine_strategy = st.builds(
    fsm::StateMachine,
)

@given(instance=fsm::Expression_strategy)
@settings(max_examples=50)
def test_fsm::expression_instantiation(instance):
    assert isinstance(instance, fsm::Expression)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=fsm::Loop_strategy)
@settings(max_examples=50)
def test_fsm::loop_instantiation(instance):
    assert isinstance(instance, fsm::Loop)

@given(instance=fsm::Context_strategy)
@settings(max_examples=50)
def test_fsm::context_instantiation(instance):
    assert isinstance(instance, fsm::Context)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=fsm::FinalState_strategy)
@settings(max_examples=50)
def test_fsm::finalstate_instantiation(instance):
    assert isinstance(instance, fsm::FinalState)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=fsm::String_strategy)
@settings(max_examples=50)
def test_fsm::string_instantiation(instance):
    assert isinstance(instance, fsm::String)

@given(instance=fsm::VarRef_strategy)
@settings(max_examples=50)
def test_fsm::varref_instantiation(instance):
    assert isinstance(instance, fsm::VarRef)

@given(instance=fsm::VarRef_strategy)
def test_fsm::varref_varId_type(instance):
    assert isinstance(instance.varId, str)


@given(instance=fsm::VarRef_strategy)
def test_fsm::varref_varId_setter(instance):
    original = instance.varId
    instance.varId = original
    assert instance.varId == original

@given(instance=fsm::Real_strategy)
@settings(max_examples=50)
def test_fsm::real_instantiation(instance):
    assert isinstance(instance, fsm::Real)

@given(instance=fsm::Boolean_strategy)
@settings(max_examples=50)
def test_fsm::boolean_instantiation(instance):
    assert isinstance(instance, fsm::Boolean)

@given(instance=fsm::Integer_strategy)
@settings(max_examples=50)
def test_fsm::integer_instantiation(instance):
    assert isinstance(instance, fsm::Integer)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=fsm::ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_fsm::arithmeticexpression_instantiation(instance):
    assert isinstance(instance, fsm::ArithmeticExpression)

@given(instance=fsm::Literal_strategy)
@settings(max_examples=50)
def test_fsm::literal_instantiation(instance):
    assert isinstance(instance, fsm::Literal)

@given(instance=fsm::RelationalExpression_strategy)
@settings(max_examples=50)
def test_fsm::relationalexpression_instantiation(instance):
    assert isinstance(instance, fsm::RelationalExpression)

@given(instance=fsm::Assignation_strategy)
@settings(max_examples=50)
def test_fsm::assignation_instantiation(instance):
    assert isinstance(instance, fsm::Assignation)

@given(instance=fsm::VarDecl_strategy)
@settings(max_examples=50)
def test_fsm::vardecl_instantiation(instance):
    assert isinstance(instance, fsm::VarDecl)

@given(instance=fsm::Conditional_strategy)
@settings(max_examples=50)
def test_fsm::conditional_instantiation(instance):
    assert isinstance(instance, fsm::Conditional)

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

@given(instance=fsm::Block_strategy)
@settings(max_examples=50)
def test_fsm::block_instantiation(instance):
    assert isinstance(instance, fsm::Block)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=Pseudostate_strategy)
@settings(max_examples=50)
def test_pseudostate_instantiation(instance):
    assert isinstance(instance, Pseudostate)

@given(instance=fsm::ShallowHistory_strategy)
@settings(max_examples=50)
def test_fsm::shallowhistory_instantiation(instance):
    assert isinstance(instance, fsm::ShallowHistory)

@given(instance=fsm::Junction_strategy)
@settings(max_examples=50)
def test_fsm::junction_instantiation(instance):
    assert isinstance(instance, fsm::Junction)

@given(instance=fsm::Condition_strategy)
@settings(max_examples=50)
def test_fsm::condition_instantiation(instance):
    assert isinstance(instance, fsm::Condition)

@given(instance=fsm::Fork_strategy)
@settings(max_examples=50)
def test_fsm::fork_instantiation(instance):
    assert isinstance(instance, fsm::Fork)

@given(instance=fsm::DeepHistory_strategy)
@settings(max_examples=50)
def test_fsm::deephistory_instantiation(instance):
    assert isinstance(instance, fsm::DeepHistory)

@given(instance=fsm::Join_strategy)
@settings(max_examples=50)
def test_fsm::join_instantiation(instance):
    assert isinstance(instance, fsm::Join)

@given(instance=fsm::InitialState_strategy)
@settings(max_examples=50)
def test_fsm::initialstate_instantiation(instance):
    assert isinstance(instance, fsm::InitialState)

@given(instance=fsm::Pseudostate_strategy)
@settings(max_examples=50)
def test_fsm::pseudostate_instantiation(instance):
    assert isinstance(instance, fsm::Pseudostate)

@given(instance=Trigger_strategy)
@settings(max_examples=50)
def test_trigger_instantiation(instance):
    assert isinstance(instance, Trigger)

@given(instance=fsm::AndTrigger_strategy)
@settings(max_examples=50)
def test_fsm::andtrigger_instantiation(instance):
    assert isinstance(instance, fsm::AndTrigger)

@given(instance=fsm::OrTrigger_strategy)
@settings(max_examples=50)
def test_fsm::ortrigger_instantiation(instance):
    assert isinstance(instance, fsm::OrTrigger)

@given(instance=fsm::NotTrigger_strategy)
@settings(max_examples=50)
def test_fsm::nottrigger_instantiation(instance):
    assert isinstance(instance, fsm::NotTrigger)

@given(instance=fsm::Constraint_strategy)
@settings(max_examples=50)
def test_fsm::constraint_instantiation(instance):
    assert isinstance(instance, fsm::Constraint)

@given(instance=fsm::Statement_strategy)
@settings(max_examples=50)
def test_fsm::statement_instantiation(instance):
    assert isinstance(instance, fsm::Statement)

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

@given(instance=fsm::Region_strategy)
@settings(max_examples=50)
def test_fsm::region_instantiation(instance):
    assert isinstance(instance, fsm::Region)

@given(instance=fsm::StateMachine_strategy)
@settings(max_examples=50)
def test_fsm::statemachine_instantiation(instance):
    assert isinstance(instance, fsm::StateMachine)
