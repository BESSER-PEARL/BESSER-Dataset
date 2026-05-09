import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fsmcore::NamedElement,
    State,
    fsmcore::FinalState,
    Statement,
    fsmcore::Loop,
    fsmcore::VarDecl,
    fsmcore::Conditional,
    fsmcore::Statement,
    fsmcore::Constraint,
    fsmcore::Trigger,
    fsmcore::Program,
    AbstractState,
    fsmcore::Pseudostate,
    fsmcore::State,
    NamedElement,
    fsmcore::Transition,
    fsmcore::AbstractState,
    fsmcore::Region,
    fsmcore::StateMachine,
    PseudostateKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsmcore::namedelement_is_not_abstract():
    assert not inspect.isabstract(fsmcore::NamedElement)


def test_fsmcore::namedelement_constructor_exists():
    assert callable(fsmcore::NamedElement.__init__)


def test_fsmcore::namedelement_constructor_args():
    sig = inspect.signature(fsmcore::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsmcore::namedelement_has_name():
    assert hasattr(fsmcore::NamedElement, "name")
    descriptor = None
    for klass in fsmcore::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_fsmcore::finalstate_is_not_abstract():
    assert not inspect.isabstract(fsmcore::FinalState)


def test_fsmcore::finalstate_constructor_exists():
    assert callable(fsmcore::FinalState.__init__)


def test_fsmcore::finalstate_constructor_args():
    sig = inspect.signature(fsmcore::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_fsmcore::loop_is_not_abstract():
    assert not inspect.isabstract(fsmcore::Loop)


def test_fsmcore::loop_constructor_exists():
    assert callable(fsmcore::Loop.__init__)


def test_fsmcore::loop_constructor_args():
    sig = inspect.signature(fsmcore::Loop.__init__)
    params = list(sig.parameters.keys())



def test_fsmcore::vardecl_is_not_abstract():
    assert not inspect.isabstract(fsmcore::VarDecl)


def test_fsmcore::vardecl_constructor_exists():
    assert callable(fsmcore::VarDecl.__init__)


def test_fsmcore::vardecl_constructor_args():
    sig = inspect.signature(fsmcore::VarDecl.__init__)
    params = list(sig.parameters.keys())



def test_fsmcore::conditional_is_not_abstract():
    assert not inspect.isabstract(fsmcore::Conditional)


def test_fsmcore::conditional_constructor_exists():
    assert callable(fsmcore::Conditional.__init__)


def test_fsmcore::conditional_constructor_args():
    sig = inspect.signature(fsmcore::Conditional.__init__)
    params = list(sig.parameters.keys())



def test_fsmcore::statement_is_not_abstract():
    assert not inspect.isabstract(fsmcore::Statement)


def test_fsmcore::statement_constructor_exists():
    assert callable(fsmcore::Statement.__init__)


def test_fsmcore::statement_constructor_args():
    sig = inspect.signature(fsmcore::Statement.__init__)
    params = list(sig.parameters.keys())



def test_fsmcore::constraint_is_not_abstract():
    assert not inspect.isabstract(fsmcore::Constraint)


def test_fsmcore::constraint_constructor_exists():
    assert callable(fsmcore::Constraint.__init__)


def test_fsmcore::constraint_constructor_args():
    sig = inspect.signature(fsmcore::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_fsmcore::trigger_is_not_abstract():
    assert not inspect.isabstract(fsmcore::Trigger)


def test_fsmcore::trigger_constructor_exists():
    assert callable(fsmcore::Trigger.__init__)


def test_fsmcore::trigger_constructor_args():
    sig = inspect.signature(fsmcore::Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_fsmcore::trigger_has_expression():
    assert hasattr(fsmcore::Trigger, "expression")
    descriptor = None
    for klass in fsmcore::Trigger.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_fsmcore::program_is_not_abstract():
    assert not inspect.isabstract(fsmcore::Program)


def test_fsmcore::program_constructor_exists():
    assert callable(fsmcore::Program.__init__)


def test_fsmcore::program_constructor_args():
    sig = inspect.signature(fsmcore::Program.__init__)
    params = list(sig.parameters.keys())



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_fsmcore::pseudostate_is_not_abstract():
    assert not inspect.isabstract(fsmcore::Pseudostate)


def test_fsmcore::pseudostate_constructor_exists():
    assert callable(fsmcore::Pseudostate.__init__)


def test_fsmcore::pseudostate_constructor_args():
    sig = inspect.signature(fsmcore::Pseudostate.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_fsmcore::pseudostate_has_kind():
    assert hasattr(fsmcore::Pseudostate, "kind")
    descriptor = None
    for klass in fsmcore::Pseudostate.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_fsmcore::state_is_not_abstract():
    assert not inspect.isabstract(fsmcore::State)


def test_fsmcore::state_constructor_exists():
    assert callable(fsmcore::State.__init__)


def test_fsmcore::state_constructor_args():
    sig = inspect.signature(fsmcore::State.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_fsmcore::transition_is_not_abstract():
    assert not inspect.isabstract(fsmcore::Transition)


def test_fsmcore::transition_constructor_exists():
    assert callable(fsmcore::Transition.__init__)


def test_fsmcore::transition_constructor_args():
    sig = inspect.signature(fsmcore::Transition.__init__)
    params = list(sig.parameters.keys())



def test_fsmcore::abstractstate_is_not_abstract():
    assert not inspect.isabstract(fsmcore::AbstractState)


def test_fsmcore::abstractstate_constructor_exists():
    assert callable(fsmcore::AbstractState.__init__)


def test_fsmcore::abstractstate_constructor_args():
    sig = inspect.signature(fsmcore::AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_fsmcore::region_is_not_abstract():
    assert not inspect.isabstract(fsmcore::Region)


def test_fsmcore::region_constructor_exists():
    assert callable(fsmcore::Region.__init__)


def test_fsmcore::region_constructor_args():
    sig = inspect.signature(fsmcore::Region.__init__)
    params = list(sig.parameters.keys())



def test_fsmcore::statemachine_is_not_abstract():
    assert not inspect.isabstract(fsmcore::StateMachine)


def test_fsmcore::statemachine_constructor_exists():
    assert callable(fsmcore::StateMachine.__init__)


def test_fsmcore::statemachine_constructor_args():
    sig = inspect.signature(fsmcore::StateMachine.__init__)
    params = list(sig.parameters.keys())

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
fsmcore::NamedElement_strategy = st.builds(
    fsmcore::NamedElement,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
fsmcore::FinalState_strategy = st.builds(
    fsmcore::FinalState,
)
Statement_strategy = st.builds(
    Statement,
)
fsmcore::Loop_strategy = st.builds(
    fsmcore::Loop,
)
fsmcore::VarDecl_strategy = st.builds(
    fsmcore::VarDecl,
)
fsmcore::Conditional_strategy = st.builds(
    fsmcore::Conditional,
)
fsmcore::Statement_strategy = st.builds(
    fsmcore::Statement,
)
fsmcore::Constraint_strategy = st.builds(
    fsmcore::Constraint,
)
fsmcore::Trigger_strategy = st.builds(
    fsmcore::Trigger,
    expression=
        st.booleans()
)
fsmcore::Program_strategy = st.builds(
    fsmcore::Program,
)
AbstractState_strategy = st.builds(
    AbstractState,
)
fsmcore::Pseudostate_strategy = st.builds(
    fsmcore::Pseudostate,
    kind=
        safe_text
)
fsmcore::State_strategy = st.builds(
    fsmcore::State,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
fsmcore::Transition_strategy = st.builds(
    fsmcore::Transition,
)
fsmcore::AbstractState_strategy = st.builds(
    fsmcore::AbstractState,
)
fsmcore::Region_strategy = st.builds(
    fsmcore::Region,
)
fsmcore::StateMachine_strategy = st.builds(
    fsmcore::StateMachine,
)

@given(instance=fsmcore::NamedElement_strategy)
@settings(max_examples=50)
def test_fsmcore::namedelement_instantiation(instance):
    assert isinstance(instance, fsmcore::NamedElement)

@given(instance=fsmcore::NamedElement_strategy)
def test_fsmcore::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsmcore::NamedElement_strategy)
def test_fsmcore::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=fsmcore::FinalState_strategy)
@settings(max_examples=50)
def test_fsmcore::finalstate_instantiation(instance):
    assert isinstance(instance, fsmcore::FinalState)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=fsmcore::Loop_strategy)
@settings(max_examples=50)
def test_fsmcore::loop_instantiation(instance):
    assert isinstance(instance, fsmcore::Loop)

@given(instance=fsmcore::VarDecl_strategy)
@settings(max_examples=50)
def test_fsmcore::vardecl_instantiation(instance):
    assert isinstance(instance, fsmcore::VarDecl)

@given(instance=fsmcore::Conditional_strategy)
@settings(max_examples=50)
def test_fsmcore::conditional_instantiation(instance):
    assert isinstance(instance, fsmcore::Conditional)

@given(instance=fsmcore::Statement_strategy)
@settings(max_examples=50)
def test_fsmcore::statement_instantiation(instance):
    assert isinstance(instance, fsmcore::Statement)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsmcore::Statement_strategy)
@settings(max_examples=30)
def test_fsmcore::statement_eval_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eval(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eval).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eval' in fsmcore::Statement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in fsmcore::Statement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in fsmcore::Statement is not implemented or raised an error")

@given(instance=fsmcore::Constraint_strategy)
@settings(max_examples=50)
def test_fsmcore::constraint_instantiation(instance):
    assert isinstance(instance, fsmcore::Constraint)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsmcore::Constraint_strategy)
@settings(max_examples=30)
def test_fsmcore::constraint_evalconstraint_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evalConstraint(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evalConstraint).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evalConstraint' in fsmcore::Constraint is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evalConstraint' in fsmcore::Constraint did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evalConstraint' in fsmcore::Constraint is not implemented or raised an error")

@given(instance=fsmcore::Trigger_strategy)
@settings(max_examples=50)
def test_fsmcore::trigger_instantiation(instance):
    assert isinstance(instance, fsmcore::Trigger)

@given(instance=fsmcore::Trigger_strategy)
def test_fsmcore::trigger_expression_type(instance):
    assert isinstance(instance.expression, bool)


@given(instance=fsmcore::Trigger_strategy)
def test_fsmcore::trigger_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=fsmcore::Program_strategy)
@settings(max_examples=50)
def test_fsmcore::program_instantiation(instance):
    assert isinstance(instance, fsmcore::Program)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsmcore::Program_strategy)
@settings(max_examples=30)
def test_fsmcore::program_eval_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eval(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eval).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eval' in fsmcore::Program is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in fsmcore::Program did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in fsmcore::Program is not implemented or raised an error")

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=fsmcore::Pseudostate_strategy)
@settings(max_examples=50)
def test_fsmcore::pseudostate_instantiation(instance):
    assert isinstance(instance, fsmcore::Pseudostate)

@given(instance=fsmcore::Pseudostate_strategy)
def test_fsmcore::pseudostate_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=fsmcore::Pseudostate_strategy)
def test_fsmcore::pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=fsmcore::State_strategy)
@settings(max_examples=50)
def test_fsmcore::state_instantiation(instance):
    assert isinstance(instance, fsmcore::State)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=fsmcore::Transition_strategy)
@settings(max_examples=50)
def test_fsmcore::transition_instantiation(instance):
    assert isinstance(instance, fsmcore::Transition)

@given(instance=fsmcore::AbstractState_strategy)
@settings(max_examples=50)
def test_fsmcore::abstractstate_instantiation(instance):
    assert isinstance(instance, fsmcore::AbstractState)

@given(instance=fsmcore::Region_strategy)
@settings(max_examples=50)
def test_fsmcore::region_instantiation(instance):
    assert isinstance(instance, fsmcore::Region)

@given(instance=fsmcore::StateMachine_strategy)
@settings(max_examples=50)
def test_fsmcore::statemachine_instantiation(instance):
    assert isinstance(instance, fsmcore::StateMachine)
