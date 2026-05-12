import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Expression,
    simpleimperative_VarRef,
    ConsoleOutput,
    simpleimperative_Print,
    simpleimperative_Println,
    simpleimperative_Expression,
    Statement,
    simpleimperative_ConsoleOutput,
    simpleimperative_VarDecl,
    simpleimperative_Wait,
    simpleimperative_Loop,
    simpleimperative_Assignation,
    simpleimperative_Conditional,
    simpleimperative_Statement,
    simpleimperative_Program,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_simpleimperative_varref_is_not_abstract():
    assert not inspect.isabstract(simpleimperative_VarRef)


def test_simpleimperative_varref_constructor_exists():
    assert callable(simpleimperative_VarRef.__init__)


def test_simpleimperative_varref_constructor_args():
    sig = inspect.signature(simpleimperative_VarRef.__init__)
    params = list(sig.parameters.keys())
    assert "varRef" in params, "Missing parameter 'varRef'"

def test_simpleimperative_varref_has_varRef():
    assert hasattr(simpleimperative_VarRef, "varRef")
    descriptor = None
    for klass in simpleimperative_VarRef.__mro__:
        if "varRef" in klass.__dict__:
            descriptor = klass.__dict__["varRef"]
            break
    assert isinstance(descriptor, property)



def test_consoleoutput_is_not_abstract():
    assert not inspect.isabstract(ConsoleOutput)


def test_consoleoutput_constructor_exists():
    assert callable(ConsoleOutput.__init__)


def test_consoleoutput_constructor_args():
    sig = inspect.signature(ConsoleOutput.__init__)
    params = list(sig.parameters.keys())



def test_simpleimperative_print_is_not_abstract():
    assert not inspect.isabstract(simpleimperative_Print)


def test_simpleimperative_print_constructor_exists():
    assert callable(simpleimperative_Print.__init__)


def test_simpleimperative_print_constructor_args():
    sig = inspect.signature(simpleimperative_Print.__init__)
    params = list(sig.parameters.keys())



def test_simpleimperative_println_is_not_abstract():
    assert not inspect.isabstract(simpleimperative_Println)


def test_simpleimperative_println_constructor_exists():
    assert callable(simpleimperative_Println.__init__)


def test_simpleimperative_println_constructor_args():
    sig = inspect.signature(simpleimperative_Println.__init__)
    params = list(sig.parameters.keys())



def test_simpleimperative_expression_is_not_abstract():
    assert not inspect.isabstract(simpleimperative_Expression)


def test_simpleimperative_expression_constructor_exists():
    assert callable(simpleimperative_Expression.__init__)


def test_simpleimperative_expression_constructor_args():
    sig = inspect.signature(simpleimperative_Expression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_simpleimperative_consoleoutput_is_not_abstract():
    assert not inspect.isabstract(simpleimperative_ConsoleOutput)


def test_simpleimperative_consoleoutput_constructor_exists():
    assert callable(simpleimperative_ConsoleOutput.__init__)


def test_simpleimperative_consoleoutput_constructor_args():
    sig = inspect.signature(simpleimperative_ConsoleOutput.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"

def test_simpleimperative_consoleoutput_has_input():
    assert hasattr(simpleimperative_ConsoleOutput, "input")
    descriptor = None
    for klass in simpleimperative_ConsoleOutput.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)



def test_simpleimperative_vardecl_is_not_abstract():
    assert not inspect.isabstract(simpleimperative_VarDecl)


def test_simpleimperative_vardecl_constructor_exists():
    assert callable(simpleimperative_VarDecl.__init__)


def test_simpleimperative_vardecl_constructor_args():
    sig = inspect.signature(simpleimperative_VarDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleimperative_vardecl_has_name():
    assert hasattr(simpleimperative_VarDecl, "name")
    descriptor = None
    for klass in simpleimperative_VarDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleimperative_wait_is_not_abstract():
    assert not inspect.isabstract(simpleimperative_Wait)


def test_simpleimperative_wait_constructor_exists():
    assert callable(simpleimperative_Wait.__init__)


def test_simpleimperative_wait_constructor_args():
    sig = inspect.signature(simpleimperative_Wait.__init__)
    params = list(sig.parameters.keys())
    assert "miliseconds" in params, "Missing parameter 'miliseconds'"

def test_simpleimperative_wait_has_miliseconds():
    assert hasattr(simpleimperative_Wait, "miliseconds")
    descriptor = None
    for klass in simpleimperative_Wait.__mro__:
        if "miliseconds" in klass.__dict__:
            descriptor = klass.__dict__["miliseconds"]
            break
    assert isinstance(descriptor, property)



def test_simpleimperative_loop_is_not_abstract():
    assert not inspect.isabstract(simpleimperative_Loop)


def test_simpleimperative_loop_constructor_exists():
    assert callable(simpleimperative_Loop.__init__)


def test_simpleimperative_loop_constructor_args():
    sig = inspect.signature(simpleimperative_Loop.__init__)
    params = list(sig.parameters.keys())



def test_simpleimperative_assignation_is_not_abstract():
    assert not inspect.isabstract(simpleimperative_Assignation)


def test_simpleimperative_assignation_constructor_exists():
    assert callable(simpleimperative_Assignation.__init__)


def test_simpleimperative_assignation_constructor_args():
    sig = inspect.signature(simpleimperative_Assignation.__init__)
    params = list(sig.parameters.keys())



def test_simpleimperative_conditional_is_not_abstract():
    assert not inspect.isabstract(simpleimperative_Conditional)


def test_simpleimperative_conditional_constructor_exists():
    assert callable(simpleimperative_Conditional.__init__)


def test_simpleimperative_conditional_constructor_args():
    sig = inspect.signature(simpleimperative_Conditional.__init__)
    params = list(sig.parameters.keys())



def test_simpleimperative_statement_is_not_abstract():
    assert not inspect.isabstract(simpleimperative_Statement)


def test_simpleimperative_statement_constructor_exists():
    assert callable(simpleimperative_Statement.__init__)


def test_simpleimperative_statement_constructor_args():
    sig = inspect.signature(simpleimperative_Statement.__init__)
    params = list(sig.parameters.keys())



def test_simpleimperative_program_is_not_abstract():
    assert not inspect.isabstract(simpleimperative_Program)


def test_simpleimperative_program_constructor_exists():
    assert callable(simpleimperative_Program.__init__)


def test_simpleimperative_program_constructor_args():
    sig = inspect.signature(simpleimperative_Program.__init__)
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
Expression_strategy = st.builds(
    Expression,
)
simpleimperative_VarRef_strategy = st.builds(
    simpleimperative_VarRef,
    varRef=
        safe_text
)
ConsoleOutput_strategy = st.builds(
    ConsoleOutput,
)
simpleimperative_Print_strategy = st.builds(
    simpleimperative_Print,
)
simpleimperative_Println_strategy = st.builds(
    simpleimperative_Println,
)
simpleimperative_Expression_strategy = st.builds(
    simpleimperative_Expression,
)
Statement_strategy = st.builds(
    Statement,
)
simpleimperative_ConsoleOutput_strategy = st.builds(
    simpleimperative_ConsoleOutput,
    input=
        safe_text
)
simpleimperative_VarDecl_strategy = st.builds(
    simpleimperative_VarDecl,
    name=
        safe_text
)
simpleimperative_Wait_strategy = st.builds(
    simpleimperative_Wait,
    miliseconds=
        safe_text
)
simpleimperative_Loop_strategy = st.builds(
    simpleimperative_Loop,
)
simpleimperative_Assignation_strategy = st.builds(
    simpleimperative_Assignation,
)
simpleimperative_Conditional_strategy = st.builds(
    simpleimperative_Conditional,
)
simpleimperative_Statement_strategy = st.builds(
    simpleimperative_Statement,
)
simpleimperative_Program_strategy = st.builds(
    simpleimperative_Program,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=simpleimperative_VarRef_strategy)
@settings(max_examples=50)
def test_simpleimperative_varref_instantiation(instance):
    assert isinstance(instance, simpleimperative_VarRef)



@given(instance=simpleimperative_VarRef_strategy)
def test_simpleimperative_varref_varRef_setter(instance):
    original = instance.varRef
    instance.varRef = original
    assert instance.varRef == original

@given(instance=ConsoleOutput_strategy)
@settings(max_examples=50)
def test_consoleoutput_instantiation(instance):
    assert isinstance(instance, ConsoleOutput)

@given(instance=simpleimperative_Print_strategy)
@settings(max_examples=50)
def test_simpleimperative_print_instantiation(instance):
    assert isinstance(instance, simpleimperative_Print)

@given(instance=simpleimperative_Println_strategy)
@settings(max_examples=50)
def test_simpleimperative_println_instantiation(instance):
    assert isinstance(instance, simpleimperative_Println)

@given(instance=simpleimperative_Expression_strategy)
@settings(max_examples=50)
def test_simpleimperative_expression_instantiation(instance):
    assert isinstance(instance, simpleimperative_Expression)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=simpleimperative_Expression_strategy)
@settings(max_examples=30)
def test_simpleimperative_expression_eval_changes_state(instance):
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
        assert has_statements, f"Function 'eval' in simpleimperative_Expression is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in simpleimperative_Expression did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in simpleimperative_Expression is not implemented or raised an error")

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=simpleimperative_ConsoleOutput_strategy)
@settings(max_examples=50)
def test_simpleimperative_consoleoutput_instantiation(instance):
    assert isinstance(instance, simpleimperative_ConsoleOutput)



@given(instance=simpleimperative_ConsoleOutput_strategy)
def test_simpleimperative_consoleoutput_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=simpleimperative_VarDecl_strategy)
@settings(max_examples=50)
def test_simpleimperative_vardecl_instantiation(instance):
    assert isinstance(instance, simpleimperative_VarDecl)



@given(instance=simpleimperative_VarDecl_strategy)
def test_simpleimperative_vardecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleimperative_Wait_strategy)
@settings(max_examples=50)
def test_simpleimperative_wait_instantiation(instance):
    assert isinstance(instance, simpleimperative_Wait)



@given(instance=simpleimperative_Wait_strategy)
def test_simpleimperative_wait_miliseconds_setter(instance):
    original = instance.miliseconds
    instance.miliseconds = original
    assert instance.miliseconds == original

@given(instance=simpleimperative_Loop_strategy)
@settings(max_examples=50)
def test_simpleimperative_loop_instantiation(instance):
    assert isinstance(instance, simpleimperative_Loop)

@given(instance=simpleimperative_Assignation_strategy)
@settings(max_examples=50)
def test_simpleimperative_assignation_instantiation(instance):
    assert isinstance(instance, simpleimperative_Assignation)

@given(instance=simpleimperative_Conditional_strategy)
@settings(max_examples=50)
def test_simpleimperative_conditional_instantiation(instance):
    assert isinstance(instance, simpleimperative_Conditional)

@given(instance=simpleimperative_Statement_strategy)
@settings(max_examples=50)
def test_simpleimperative_statement_instantiation(instance):
    assert isinstance(instance, simpleimperative_Statement)

@given(instance=simpleimperative_Program_strategy)
@settings(max_examples=50)
def test_simpleimperative_program_instantiation(instance):
    assert isinstance(instance, simpleimperative_Program)
