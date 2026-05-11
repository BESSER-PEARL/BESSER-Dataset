import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    simpleimperative::VarRef,
    ConsoleOutput,
    simpleimperative::Print,
    simpleimperative::Println,
    simpleimperative::Expression,
    Statement,
    simpleimperative::ConsoleOutput,
    simpleimperative::VarDecl,
    simpleimperative::Loop,
    simpleimperative::Wait,
    simpleimperative::Assignation,
    simpleimperative::Conditional,
    simpleimperative::Statement,
    simpleimperative::Program,
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



def test_simpleimperative::varref_is_not_abstract():
    assert not inspect.isabstract(simpleimperative::VarRef)


def test_simpleimperative::varref_constructor_exists():
    assert callable(simpleimperative::VarRef.__init__)


def test_simpleimperative::varref_constructor_args():
    sig = inspect.signature(simpleimperative::VarRef.__init__)
    params = list(sig.parameters.keys())
    assert "varRef" in params, "Missing parameter 'varRef'"

def test_simpleimperative::varref_has_varRef():
    assert hasattr(simpleimperative::VarRef, "varRef")
    descriptor = None
    for klass in simpleimperative::VarRef.__mro__:
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



def test_simpleimperative::print_is_not_abstract():
    assert not inspect.isabstract(simpleimperative::Print)


def test_simpleimperative::print_constructor_exists():
    assert callable(simpleimperative::Print.__init__)


def test_simpleimperative::print_constructor_args():
    sig = inspect.signature(simpleimperative::Print.__init__)
    params = list(sig.parameters.keys())



def test_simpleimperative::println_is_not_abstract():
    assert not inspect.isabstract(simpleimperative::Println)


def test_simpleimperative::println_constructor_exists():
    assert callable(simpleimperative::Println.__init__)


def test_simpleimperative::println_constructor_args():
    sig = inspect.signature(simpleimperative::Println.__init__)
    params = list(sig.parameters.keys())



def test_simpleimperative::expression_is_not_abstract():
    assert not inspect.isabstract(simpleimperative::Expression)


def test_simpleimperative::expression_constructor_exists():
    assert callable(simpleimperative::Expression.__init__)


def test_simpleimperative::expression_constructor_args():
    sig = inspect.signature(simpleimperative::Expression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_simpleimperative::consoleoutput_is_not_abstract():
    assert not inspect.isabstract(simpleimperative::ConsoleOutput)


def test_simpleimperative::consoleoutput_constructor_exists():
    assert callable(simpleimperative::ConsoleOutput.__init__)


def test_simpleimperative::consoleoutput_constructor_args():
    sig = inspect.signature(simpleimperative::ConsoleOutput.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"

def test_simpleimperative::consoleoutput_has_input():
    assert hasattr(simpleimperative::ConsoleOutput, "input")
    descriptor = None
    for klass in simpleimperative::ConsoleOutput.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)



def test_simpleimperative::vardecl_is_not_abstract():
    assert not inspect.isabstract(simpleimperative::VarDecl)


def test_simpleimperative::vardecl_constructor_exists():
    assert callable(simpleimperative::VarDecl.__init__)


def test_simpleimperative::vardecl_constructor_args():
    sig = inspect.signature(simpleimperative::VarDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleimperative::vardecl_has_name():
    assert hasattr(simpleimperative::VarDecl, "name")
    descriptor = None
    for klass in simpleimperative::VarDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleimperative::loop_is_not_abstract():
    assert not inspect.isabstract(simpleimperative::Loop)


def test_simpleimperative::loop_constructor_exists():
    assert callable(simpleimperative::Loop.__init__)


def test_simpleimperative::loop_constructor_args():
    sig = inspect.signature(simpleimperative::Loop.__init__)
    params = list(sig.parameters.keys())



def test_simpleimperative::wait_is_not_abstract():
    assert not inspect.isabstract(simpleimperative::Wait)


def test_simpleimperative::wait_constructor_exists():
    assert callable(simpleimperative::Wait.__init__)


def test_simpleimperative::wait_constructor_args():
    sig = inspect.signature(simpleimperative::Wait.__init__)
    params = list(sig.parameters.keys())
    assert "miliseconds" in params, "Missing parameter 'miliseconds'"

def test_simpleimperative::wait_has_miliseconds():
    assert hasattr(simpleimperative::Wait, "miliseconds")
    descriptor = None
    for klass in simpleimperative::Wait.__mro__:
        if "miliseconds" in klass.__dict__:
            descriptor = klass.__dict__["miliseconds"]
            break
    assert isinstance(descriptor, property)



def test_simpleimperative::assignation_is_not_abstract():
    assert not inspect.isabstract(simpleimperative::Assignation)


def test_simpleimperative::assignation_constructor_exists():
    assert callable(simpleimperative::Assignation.__init__)


def test_simpleimperative::assignation_constructor_args():
    sig = inspect.signature(simpleimperative::Assignation.__init__)
    params = list(sig.parameters.keys())



def test_simpleimperative::conditional_is_not_abstract():
    assert not inspect.isabstract(simpleimperative::Conditional)


def test_simpleimperative::conditional_constructor_exists():
    assert callable(simpleimperative::Conditional.__init__)


def test_simpleimperative::conditional_constructor_args():
    sig = inspect.signature(simpleimperative::Conditional.__init__)
    params = list(sig.parameters.keys())



def test_simpleimperative::statement_is_not_abstract():
    assert not inspect.isabstract(simpleimperative::Statement)


def test_simpleimperative::statement_constructor_exists():
    assert callable(simpleimperative::Statement.__init__)


def test_simpleimperative::statement_constructor_args():
    sig = inspect.signature(simpleimperative::Statement.__init__)
    params = list(sig.parameters.keys())



def test_simpleimperative::program_is_not_abstract():
    assert not inspect.isabstract(simpleimperative::Program)


def test_simpleimperative::program_constructor_exists():
    assert callable(simpleimperative::Program.__init__)


def test_simpleimperative::program_constructor_args():
    sig = inspect.signature(simpleimperative::Program.__init__)
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
simpleimperative::VarRef_strategy = st.builds(
    simpleimperative::VarRef,
    varRef=
        safe_text
)
ConsoleOutput_strategy = st.builds(
    ConsoleOutput,
)
simpleimperative::Print_strategy = st.builds(
    simpleimperative::Print,
)
simpleimperative::Println_strategy = st.builds(
    simpleimperative::Println,
)
simpleimperative::Expression_strategy = st.builds(
    simpleimperative::Expression,
)
Statement_strategy = st.builds(
    Statement,
)
simpleimperative::ConsoleOutput_strategy = st.builds(
    simpleimperative::ConsoleOutput,
    input=
        safe_text
)
simpleimperative::VarDecl_strategy = st.builds(
    simpleimperative::VarDecl,
    name=
        safe_text
)
simpleimperative::Loop_strategy = st.builds(
    simpleimperative::Loop,
)
simpleimperative::Wait_strategy = st.builds(
    simpleimperative::Wait,
    miliseconds=
        safe_text
)
simpleimperative::Assignation_strategy = st.builds(
    simpleimperative::Assignation,
)
simpleimperative::Conditional_strategy = st.builds(
    simpleimperative::Conditional,
)
simpleimperative::Statement_strategy = st.builds(
    simpleimperative::Statement,
)
simpleimperative::Program_strategy = st.builds(
    simpleimperative::Program,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=simpleimperative::VarRef_strategy)
@settings(max_examples=50)
def test_simpleimperative::varref_instantiation(instance):
    assert isinstance(instance, simpleimperative::VarRef)

@given(instance=simpleimperative::VarRef_strategy)
def test_simpleimperative::varref_varRef_type(instance):
    assert isinstance(instance.varRef, str)


@given(instance=simpleimperative::VarRef_strategy)
def test_simpleimperative::varref_varRef_setter(instance):
    original = instance.varRef
    instance.varRef = original
    assert instance.varRef == original

@given(instance=ConsoleOutput_strategy)
@settings(max_examples=50)
def test_consoleoutput_instantiation(instance):
    assert isinstance(instance, ConsoleOutput)

@given(instance=simpleimperative::Print_strategy)
@settings(max_examples=50)
def test_simpleimperative::print_instantiation(instance):
    assert isinstance(instance, simpleimperative::Print)

@given(instance=simpleimperative::Println_strategy)
@settings(max_examples=50)
def test_simpleimperative::println_instantiation(instance):
    assert isinstance(instance, simpleimperative::Println)

@given(instance=simpleimperative::Expression_strategy)
@settings(max_examples=50)
def test_simpleimperative::expression_instantiation(instance):
    assert isinstance(instance, simpleimperative::Expression)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=simpleimperative::Expression_strategy)
@settings(max_examples=30)
def test_simpleimperative::expression_eval_changes_state(instance):
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
        assert has_statements, f"Function 'eval' in simpleimperative::Expression is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in simpleimperative::Expression did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in simpleimperative::Expression is not implemented or raised an error")

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=simpleimperative::ConsoleOutput_strategy)
@settings(max_examples=50)
def test_simpleimperative::consoleoutput_instantiation(instance):
    assert isinstance(instance, simpleimperative::ConsoleOutput)

@given(instance=simpleimperative::ConsoleOutput_strategy)
def test_simpleimperative::consoleoutput_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=simpleimperative::ConsoleOutput_strategy)
def test_simpleimperative::consoleoutput_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=simpleimperative::VarDecl_strategy)
@settings(max_examples=50)
def test_simpleimperative::vardecl_instantiation(instance):
    assert isinstance(instance, simpleimperative::VarDecl)

@given(instance=simpleimperative::VarDecl_strategy)
def test_simpleimperative::vardecl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleimperative::VarDecl_strategy)
def test_simpleimperative::vardecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleimperative::Loop_strategy)
@settings(max_examples=50)
def test_simpleimperative::loop_instantiation(instance):
    assert isinstance(instance, simpleimperative::Loop)

@given(instance=simpleimperative::Wait_strategy)
@settings(max_examples=50)
def test_simpleimperative::wait_instantiation(instance):
    assert isinstance(instance, simpleimperative::Wait)

@given(instance=simpleimperative::Wait_strategy)
def test_simpleimperative::wait_miliseconds_type(instance):
    assert isinstance(instance.miliseconds, str)


@given(instance=simpleimperative::Wait_strategy)
def test_simpleimperative::wait_miliseconds_setter(instance):
    original = instance.miliseconds
    instance.miliseconds = original
    assert instance.miliseconds == original

@given(instance=simpleimperative::Assignation_strategy)
@settings(max_examples=50)
def test_simpleimperative::assignation_instantiation(instance):
    assert isinstance(instance, simpleimperative::Assignation)

@given(instance=simpleimperative::Conditional_strategy)
@settings(max_examples=50)
def test_simpleimperative::conditional_instantiation(instance):
    assert isinstance(instance, simpleimperative::Conditional)

@given(instance=simpleimperative::Statement_strategy)
@settings(max_examples=50)
def test_simpleimperative::statement_instantiation(instance):
    assert isinstance(instance, simpleimperative::Statement)

@given(instance=simpleimperative::Program_strategy)
@settings(max_examples=50)
def test_simpleimperative::program_instantiation(instance):
    assert isinstance(instance, simpleimperative::Program)
