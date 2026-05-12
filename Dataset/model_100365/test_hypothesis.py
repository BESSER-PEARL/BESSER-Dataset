import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ConsoleOutput,
    fsm_Print,
    fsm_Println,
    Literal,
    fsm_StringLit,
    fsm_BoolLit,
    fsm_IntegerLit,
    Expression,
    fsm_VarReference,
    fsm_ArithmeticExpression,
    fsm_Literal,
    fsm_RelationalExpression,
    fsm_Expression,
    Constraint,
    fsm_RelationalConstraint,
    State,
    fsm_FinalState,
    Statement,
    fsm_Wait,
    fsm_ConsoleOutput,
    fsm_VarDecl,
    fsm_Loop,
    fsm_Conditional,
    fsm_Assignation,
    fsm_Trigger,
    fsm_Constraint,
    fsm_Statement,
    fsm_Transition,
    fsm_Program,
    AbstractState,
    fsm_Pseudostate,
    fsm_State,
    fsm_AbstractState,
    fsm_StateMachine,
    PseudostateKind,
    RelationalOperator,
    ArithmeticOperator,
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



def test_fsm_print_is_not_abstract():
    assert not inspect.isabstract(fsm_Print)


def test_fsm_print_constructor_exists():
    assert callable(fsm_Print.__init__)


def test_fsm_print_constructor_args():
    sig = inspect.signature(fsm_Print.__init__)
    params = list(sig.parameters.keys())



def test_fsm_println_is_not_abstract():
    assert not inspect.isabstract(fsm_Println)


def test_fsm_println_constructor_exists():
    assert callable(fsm_Println.__init__)


def test_fsm_println_constructor_args():
    sig = inspect.signature(fsm_Println.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_fsm_stringlit_is_not_abstract():
    assert not inspect.isabstract(fsm_StringLit)


def test_fsm_stringlit_constructor_exists():
    assert callable(fsm_StringLit.__init__)


def test_fsm_stringlit_constructor_args():
    sig = inspect.signature(fsm_StringLit.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fsm_stringlit_has_value():
    assert hasattr(fsm_StringLit, "value")
    descriptor = None
    for klass in fsm_StringLit.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fsm_boollit_is_not_abstract():
    assert not inspect.isabstract(fsm_BoolLit)


def test_fsm_boollit_constructor_exists():
    assert callable(fsm_BoolLit.__init__)


def test_fsm_boollit_constructor_args():
    sig = inspect.signature(fsm_BoolLit.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fsm_boollit_has_value():
    assert hasattr(fsm_BoolLit, "value")
    descriptor = None
    for klass in fsm_BoolLit.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fsm_integerlit_is_not_abstract():
    assert not inspect.isabstract(fsm_IntegerLit)


def test_fsm_integerlit_constructor_exists():
    assert callable(fsm_IntegerLit.__init__)


def test_fsm_integerlit_constructor_args():
    sig = inspect.signature(fsm_IntegerLit.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fsm_integerlit_has_value():
    assert hasattr(fsm_IntegerLit, "value")
    descriptor = None
    for klass in fsm_IntegerLit.__mro__:
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



def test_fsm_varreference_is_not_abstract():
    assert not inspect.isabstract(fsm_VarReference)


def test_fsm_varreference_constructor_exists():
    assert callable(fsm_VarReference.__init__)


def test_fsm_varreference_constructor_args():
    sig = inspect.signature(fsm_VarReference.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_fsm_varreference_has_key():
    assert hasattr(fsm_VarReference, "key")
    descriptor = None
    for klass in fsm_VarReference.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_fsm_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(fsm_ArithmeticExpression)


def test_fsm_arithmeticexpression_constructor_exists():
    assert callable(fsm_ArithmeticExpression.__init__)


def test_fsm_arithmeticexpression_constructor_args():
    sig = inspect.signature(fsm_ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_fsm_arithmeticexpression_has_operator():
    assert hasattr(fsm_ArithmeticExpression, "operator")
    descriptor = None
    for klass in fsm_ArithmeticExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_fsm_literal_is_not_abstract():
    assert not inspect.isabstract(fsm_Literal)


def test_fsm_literal_constructor_exists():
    assert callable(fsm_Literal.__init__)


def test_fsm_literal_constructor_args():
    sig = inspect.signature(fsm_Literal.__init__)
    params = list(sig.parameters.keys())



def test_fsm_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(fsm_RelationalExpression)


def test_fsm_relationalexpression_constructor_exists():
    assert callable(fsm_RelationalExpression.__init__)


def test_fsm_relationalexpression_constructor_args():
    sig = inspect.signature(fsm_RelationalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_fsm_relationalexpression_has_operator():
    assert hasattr(fsm_RelationalExpression, "operator")
    descriptor = None
    for klass in fsm_RelationalExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_fsm_expression_is_not_abstract():
    assert not inspect.isabstract(fsm_Expression)


def test_fsm_expression_constructor_exists():
    assert callable(fsm_Expression.__init__)


def test_fsm_expression_constructor_args():
    sig = inspect.signature(fsm_Expression.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_fsm_relationalconstraint_is_not_abstract():
    assert not inspect.isabstract(fsm_RelationalConstraint)


def test_fsm_relationalconstraint_constructor_exists():
    assert callable(fsm_RelationalConstraint.__init__)


def test_fsm_relationalconstraint_constructor_args():
    sig = inspect.signature(fsm_RelationalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_fsm_finalstate_is_not_abstract():
    assert not inspect.isabstract(fsm_FinalState)


def test_fsm_finalstate_constructor_exists():
    assert callable(fsm_FinalState.__init__)


def test_fsm_finalstate_constructor_args():
    sig = inspect.signature(fsm_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_fsm_wait_is_not_abstract():
    assert not inspect.isabstract(fsm_Wait)


def test_fsm_wait_constructor_exists():
    assert callable(fsm_Wait.__init__)


def test_fsm_wait_constructor_args():
    sig = inspect.signature(fsm_Wait.__init__)
    params = list(sig.parameters.keys())
    assert "miliseconds" in params, "Missing parameter 'miliseconds'"

def test_fsm_wait_has_miliseconds():
    assert hasattr(fsm_Wait, "miliseconds")
    descriptor = None
    for klass in fsm_Wait.__mro__:
        if "miliseconds" in klass.__dict__:
            descriptor = klass.__dict__["miliseconds"]
            break
    assert isinstance(descriptor, property)



def test_fsm_consoleoutput_is_not_abstract():
    assert not inspect.isabstract(fsm_ConsoleOutput)


def test_fsm_consoleoutput_constructor_exists():
    assert callable(fsm_ConsoleOutput.__init__)


def test_fsm_consoleoutput_constructor_args():
    sig = inspect.signature(fsm_ConsoleOutput.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"

def test_fsm_consoleoutput_has_input():
    assert hasattr(fsm_ConsoleOutput, "input")
    descriptor = None
    for klass in fsm_ConsoleOutput.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)



def test_fsm_vardecl_is_not_abstract():
    assert not inspect.isabstract(fsm_VarDecl)


def test_fsm_vardecl_constructor_exists():
    assert callable(fsm_VarDecl.__init__)


def test_fsm_vardecl_constructor_args():
    sig = inspect.signature(fsm_VarDecl.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_fsm_vardecl_has_key():
    assert hasattr(fsm_VarDecl, "key")
    descriptor = None
    for klass in fsm_VarDecl.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_fsm_loop_is_not_abstract():
    assert not inspect.isabstract(fsm_Loop)


def test_fsm_loop_constructor_exists():
    assert callable(fsm_Loop.__init__)


def test_fsm_loop_constructor_args():
    sig = inspect.signature(fsm_Loop.__init__)
    params = list(sig.parameters.keys())



def test_fsm_conditional_is_not_abstract():
    assert not inspect.isabstract(fsm_Conditional)


def test_fsm_conditional_constructor_exists():
    assert callable(fsm_Conditional.__init__)


def test_fsm_conditional_constructor_args():
    sig = inspect.signature(fsm_Conditional.__init__)
    params = list(sig.parameters.keys())



def test_fsm_assignation_is_not_abstract():
    assert not inspect.isabstract(fsm_Assignation)


def test_fsm_assignation_constructor_exists():
    assert callable(fsm_Assignation.__init__)


def test_fsm_assignation_constructor_args():
    sig = inspect.signature(fsm_Assignation.__init__)
    params = list(sig.parameters.keys())



def test_fsm_trigger_is_not_abstract():
    assert not inspect.isabstract(fsm_Trigger)


def test_fsm_trigger_constructor_exists():
    assert callable(fsm_Trigger.__init__)


def test_fsm_trigger_constructor_args():
    sig = inspect.signature(fsm_Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_fsm_trigger_has_expression():
    assert hasattr(fsm_Trigger, "expression")
    descriptor = None
    for klass in fsm_Trigger.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_fsm_constraint_is_not_abstract():
    assert not inspect.isabstract(fsm_Constraint)


def test_fsm_constraint_constructor_exists():
    assert callable(fsm_Constraint.__init__)


def test_fsm_constraint_constructor_args():
    sig = inspect.signature(fsm_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_fsm_statement_is_not_abstract():
    assert not inspect.isabstract(fsm_Statement)


def test_fsm_statement_constructor_exists():
    assert callable(fsm_Statement.__init__)


def test_fsm_statement_constructor_args():
    sig = inspect.signature(fsm_Statement.__init__)
    params = list(sig.parameters.keys())



def test_fsm_transition_is_not_abstract():
    assert not inspect.isabstract(fsm_Transition)


def test_fsm_transition_constructor_exists():
    assert callable(fsm_Transition.__init__)


def test_fsm_transition_constructor_args():
    sig = inspect.signature(fsm_Transition.__init__)
    params = list(sig.parameters.keys())



def test_fsm_program_is_not_abstract():
    assert not inspect.isabstract(fsm_Program)


def test_fsm_program_constructor_exists():
    assert callable(fsm_Program.__init__)


def test_fsm_program_constructor_args():
    sig = inspect.signature(fsm_Program.__init__)
    params = list(sig.parameters.keys())



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_fsm_pseudostate_is_not_abstract():
    assert not inspect.isabstract(fsm_Pseudostate)


def test_fsm_pseudostate_constructor_exists():
    assert callable(fsm_Pseudostate.__init__)


def test_fsm_pseudostate_constructor_args():
    sig = inspect.signature(fsm_Pseudostate.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_fsm_pseudostate_has_kind():
    assert hasattr(fsm_Pseudostate, "kind")
    descriptor = None
    for klass in fsm_Pseudostate.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_fsm_state_is_not_abstract():
    assert not inspect.isabstract(fsm_State)


def test_fsm_state_constructor_exists():
    assert callable(fsm_State.__init__)


def test_fsm_state_constructor_args():
    sig = inspect.signature(fsm_State.__init__)
    params = list(sig.parameters.keys())



def test_fsm_abstractstate_is_not_abstract():
    assert not inspect.isabstract(fsm_AbstractState)


def test_fsm_abstractstate_constructor_exists():
    assert callable(fsm_AbstractState.__init__)


def test_fsm_abstractstate_constructor_args():
    sig = inspect.signature(fsm_AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_abstractstate_has_name():
    assert hasattr(fsm_AbstractState, "name")
    descriptor = None
    for klass in fsm_AbstractState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm_statemachine_is_not_abstract():
    assert not inspect.isabstract(fsm_StateMachine)


def test_fsm_statemachine_constructor_exists():
    assert callable(fsm_StateMachine.__init__)


def test_fsm_statemachine_constructor_args():
    sig = inspect.signature(fsm_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_statemachine_has_name():
    assert hasattr(fsm_StateMachine, "name")
    descriptor = None
    for klass in fsm_StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

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
        "greaterThan",
        "lessThan",
        "notEqual",
        "equals",
        "greaterThanOrEqualTo",
        "lessThanOrEqualTo",
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
        "minus",
        "div",
        "plus",
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
ConsoleOutput_strategy = st.builds(
    ConsoleOutput,
)
fsm_Print_strategy = st.builds(
    fsm_Print,
)
fsm_Println_strategy = st.builds(
    fsm_Println,
)
Literal_strategy = st.builds(
    Literal,
)
fsm_StringLit_strategy = st.builds(
    fsm_StringLit,
    value=
        safe_text
)
fsm_BoolLit_strategy = st.builds(
    fsm_BoolLit,
    value=
        st.booleans()
)
fsm_IntegerLit_strategy = st.builds(
    fsm_IntegerLit,
    value=
        st.integers()
)
Expression_strategy = st.builds(
    Expression,
)
fsm_VarReference_strategy = st.builds(
    fsm_VarReference,
    key=
        safe_text
)
fsm_ArithmeticExpression_strategy = st.builds(
    fsm_ArithmeticExpression,
    operator=
        safe_text
)
fsm_Literal_strategy = st.builds(
    fsm_Literal,
)
fsm_RelationalExpression_strategy = st.builds(
    fsm_RelationalExpression,
    operator=
        safe_text
)
fsm_Expression_strategy = st.builds(
    fsm_Expression,
)
Constraint_strategy = st.builds(
    Constraint,
)
fsm_RelationalConstraint_strategy = st.builds(
    fsm_RelationalConstraint,
)
State_strategy = st.builds(
    State,
)
fsm_FinalState_strategy = st.builds(
    fsm_FinalState,
)
Statement_strategy = st.builds(
    Statement,
)
fsm_Wait_strategy = st.builds(
    fsm_Wait,
    miliseconds=
        safe_text
)
fsm_ConsoleOutput_strategy = st.builds(
    fsm_ConsoleOutput,
    input=
        safe_text
)
fsm_VarDecl_strategy = st.builds(
    fsm_VarDecl,
    key=
        safe_text
)
fsm_Loop_strategy = st.builds(
    fsm_Loop,
)
fsm_Conditional_strategy = st.builds(
    fsm_Conditional,
)
fsm_Assignation_strategy = st.builds(
    fsm_Assignation,
)
fsm_Trigger_strategy = st.builds(
    fsm_Trigger,
    expression=
        safe_text
)
fsm_Constraint_strategy = st.builds(
    fsm_Constraint,
)
fsm_Statement_strategy = st.builds(
    fsm_Statement,
)
fsm_Transition_strategy = st.builds(
    fsm_Transition,
)
fsm_Program_strategy = st.builds(
    fsm_Program,
)
AbstractState_strategy = st.builds(
    AbstractState,
)
fsm_Pseudostate_strategy = st.builds(
    fsm_Pseudostate,
    kind=
        safe_text
)
fsm_State_strategy = st.builds(
    fsm_State,
)
fsm_AbstractState_strategy = st.builds(
    fsm_AbstractState,
    name=
        safe_text
)
fsm_StateMachine_strategy = st.builds(
    fsm_StateMachine,
    name=
        safe_text
)

@given(instance=ConsoleOutput_strategy)
@settings(max_examples=50)
def test_consoleoutput_instantiation(instance):
    assert isinstance(instance, ConsoleOutput)

@given(instance=fsm_Print_strategy)
@settings(max_examples=50)
def test_fsm_print_instantiation(instance):
    assert isinstance(instance, fsm_Print)

@given(instance=fsm_Println_strategy)
@settings(max_examples=50)
def test_fsm_println_instantiation(instance):
    assert isinstance(instance, fsm_Println)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=fsm_StringLit_strategy)
@settings(max_examples=50)
def test_fsm_stringlit_instantiation(instance):
    assert isinstance(instance, fsm_StringLit)



@given(instance=fsm_StringLit_strategy)
def test_fsm_stringlit_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fsm_BoolLit_strategy)
@settings(max_examples=50)
def test_fsm_boollit_instantiation(instance):
    assert isinstance(instance, fsm_BoolLit)



@given(instance=fsm_BoolLit_strategy)
def test_fsm_boollit_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fsm_IntegerLit_strategy)
@settings(max_examples=50)
def test_fsm_integerlit_instantiation(instance):
    assert isinstance(instance, fsm_IntegerLit)



@given(instance=fsm_IntegerLit_strategy)
def test_fsm_integerlit_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=fsm_VarReference_strategy)
@settings(max_examples=50)
def test_fsm_varreference_instantiation(instance):
    assert isinstance(instance, fsm_VarReference)



@given(instance=fsm_VarReference_strategy)
def test_fsm_varreference_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=fsm_ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_fsm_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, fsm_ArithmeticExpression)



@given(instance=fsm_ArithmeticExpression_strategy)
def test_fsm_arithmeticexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=fsm_Literal_strategy)
@settings(max_examples=50)
def test_fsm_literal_instantiation(instance):
    assert isinstance(instance, fsm_Literal)

@given(instance=fsm_RelationalExpression_strategy)
@settings(max_examples=50)
def test_fsm_relationalexpression_instantiation(instance):
    assert isinstance(instance, fsm_RelationalExpression)



@given(instance=fsm_RelationalExpression_strategy)
def test_fsm_relationalexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=fsm_Expression_strategy)
@settings(max_examples=50)
def test_fsm_expression_instantiation(instance):
    assert isinstance(instance, fsm_Expression)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=fsm_RelationalConstraint_strategy)
@settings(max_examples=50)
def test_fsm_relationalconstraint_instantiation(instance):
    assert isinstance(instance, fsm_RelationalConstraint)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=fsm_FinalState_strategy)
@settings(max_examples=50)
def test_fsm_finalstate_instantiation(instance):
    assert isinstance(instance, fsm_FinalState)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=fsm_Wait_strategy)
@settings(max_examples=50)
def test_fsm_wait_instantiation(instance):
    assert isinstance(instance, fsm_Wait)



@given(instance=fsm_Wait_strategy)
def test_fsm_wait_miliseconds_setter(instance):
    original = instance.miliseconds
    instance.miliseconds = original
    assert instance.miliseconds == original

@given(instance=fsm_ConsoleOutput_strategy)
@settings(max_examples=50)
def test_fsm_consoleoutput_instantiation(instance):
    assert isinstance(instance, fsm_ConsoleOutput)



@given(instance=fsm_ConsoleOutput_strategy)
def test_fsm_consoleoutput_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=fsm_VarDecl_strategy)
@settings(max_examples=50)
def test_fsm_vardecl_instantiation(instance):
    assert isinstance(instance, fsm_VarDecl)



@given(instance=fsm_VarDecl_strategy)
def test_fsm_vardecl_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=fsm_Loop_strategy)
@settings(max_examples=50)
def test_fsm_loop_instantiation(instance):
    assert isinstance(instance, fsm_Loop)

@given(instance=fsm_Conditional_strategy)
@settings(max_examples=50)
def test_fsm_conditional_instantiation(instance):
    assert isinstance(instance, fsm_Conditional)

@given(instance=fsm_Assignation_strategy)
@settings(max_examples=50)
def test_fsm_assignation_instantiation(instance):
    assert isinstance(instance, fsm_Assignation)

@given(instance=fsm_Trigger_strategy)
@settings(max_examples=50)
def test_fsm_trigger_instantiation(instance):
    assert isinstance(instance, fsm_Trigger)



@given(instance=fsm_Trigger_strategy)
def test_fsm_trigger_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=fsm_Constraint_strategy)
@settings(max_examples=50)
def test_fsm_constraint_instantiation(instance):
    assert isinstance(instance, fsm_Constraint)

@given(instance=fsm_Statement_strategy)
@settings(max_examples=50)
def test_fsm_statement_instantiation(instance):
    assert isinstance(instance, fsm_Statement)

@given(instance=fsm_Transition_strategy)
@settings(max_examples=50)
def test_fsm_transition_instantiation(instance):
    assert isinstance(instance, fsm_Transition)

@given(instance=fsm_Program_strategy)
@settings(max_examples=50)
def test_fsm_program_instantiation(instance):
    assert isinstance(instance, fsm_Program)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=fsm_Pseudostate_strategy)
@settings(max_examples=50)
def test_fsm_pseudostate_instantiation(instance):
    assert isinstance(instance, fsm_Pseudostate)



@given(instance=fsm_Pseudostate_strategy)
def test_fsm_pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=fsm_State_strategy)
@settings(max_examples=50)
def test_fsm_state_instantiation(instance):
    assert isinstance(instance, fsm_State)

@given(instance=fsm_AbstractState_strategy)
@settings(max_examples=50)
def test_fsm_abstractstate_instantiation(instance):
    assert isinstance(instance, fsm_AbstractState)



@given(instance=fsm_AbstractState_strategy)
def test_fsm_abstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm_StateMachine_strategy)
@settings(max_examples=50)
def test_fsm_statemachine_instantiation(instance):
    assert isinstance(instance, fsm_StateMachine)



@given(instance=fsm_StateMachine_strategy)
def test_fsm_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
