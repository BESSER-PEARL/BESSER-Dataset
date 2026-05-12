import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Statement,
    sourcecode_Decision,
    sourcecode_Assignment,
    sourcecode_Program,
    sourcecode_While,
    sourcecode_Statement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_sourcecode_decision_is_not_abstract():
    assert not inspect.isabstract(sourcecode_Decision)


def test_sourcecode_decision_constructor_exists():
    assert callable(sourcecode_Decision.__init__)


def test_sourcecode_decision_constructor_args():
    sig = inspect.signature(sourcecode_Decision.__init__)
    params = list(sig.parameters.keys())



def test_sourcecode_assignment_is_not_abstract():
    assert not inspect.isabstract(sourcecode_Assignment)


def test_sourcecode_assignment_constructor_exists():
    assert callable(sourcecode_Assignment.__init__)


def test_sourcecode_assignment_constructor_args():
    sig = inspect.signature(sourcecode_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_sourcecode_program_is_not_abstract():
    assert not inspect.isabstract(sourcecode_Program)


def test_sourcecode_program_constructor_exists():
    assert callable(sourcecode_Program.__init__)


def test_sourcecode_program_constructor_args():
    sig = inspect.signature(sourcecode_Program.__init__)
    params = list(sig.parameters.keys())



def test_sourcecode_while_is_not_abstract():
    assert not inspect.isabstract(sourcecode_While)


def test_sourcecode_while_constructor_exists():
    assert callable(sourcecode_While.__init__)


def test_sourcecode_while_constructor_args():
    sig = inspect.signature(sourcecode_While.__init__)
    params = list(sig.parameters.keys())



def test_sourcecode_statement_is_not_abstract():
    assert not inspect.isabstract(sourcecode_Statement)


def test_sourcecode_statement_constructor_exists():
    assert callable(sourcecode_Statement.__init__)


def test_sourcecode_statement_constructor_args():
    sig = inspect.signature(sourcecode_Statement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_sourcecode_statement_has_id():
    assert hasattr(sourcecode_Statement, "id")
    descriptor = None
    for klass in sourcecode_Statement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)


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
Statement_strategy = st.builds(
    Statement,
)
sourcecode_Decision_strategy = st.builds(
    sourcecode_Decision,
)
sourcecode_Assignment_strategy = st.builds(
    sourcecode_Assignment,
)
sourcecode_Program_strategy = st.builds(
    sourcecode_Program,
)
sourcecode_While_strategy = st.builds(
    sourcecode_While,
)
sourcecode_Statement_strategy = st.builds(
    sourcecode_Statement,
    id=
        safe_text
)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=sourcecode_Decision_strategy)
@settings(max_examples=50)
def test_sourcecode_decision_instantiation(instance):
    assert isinstance(instance, sourcecode_Decision)

@given(instance=sourcecode_Assignment_strategy)
@settings(max_examples=50)
def test_sourcecode_assignment_instantiation(instance):
    assert isinstance(instance, sourcecode_Assignment)

@given(instance=sourcecode_Program_strategy)
@settings(max_examples=50)
def test_sourcecode_program_instantiation(instance):
    assert isinstance(instance, sourcecode_Program)

@given(instance=sourcecode_While_strategy)
@settings(max_examples=50)
def test_sourcecode_while_instantiation(instance):
    assert isinstance(instance, sourcecode_While)

@given(instance=sourcecode_Statement_strategy)
@settings(max_examples=50)
def test_sourcecode_statement_instantiation(instance):
    assert isinstance(instance, sourcecode_Statement)



@given(instance=sourcecode_Statement_strategy)
def test_sourcecode_statement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
