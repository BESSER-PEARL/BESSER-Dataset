import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Statement,
    sourcecode::Decision,
    sourcecode::Assignment,
    sourcecode::Program,
    sourcecode::While,
    sourcecode::Statement,
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



def test_sourcecode::decision_is_not_abstract():
    assert not inspect.isabstract(sourcecode::Decision)


def test_sourcecode::decision_constructor_exists():
    assert callable(sourcecode::Decision.__init__)


def test_sourcecode::decision_constructor_args():
    sig = inspect.signature(sourcecode::Decision.__init__)
    params = list(sig.parameters.keys())



def test_sourcecode::assignment_is_not_abstract():
    assert not inspect.isabstract(sourcecode::Assignment)


def test_sourcecode::assignment_constructor_exists():
    assert callable(sourcecode::Assignment.__init__)


def test_sourcecode::assignment_constructor_args():
    sig = inspect.signature(sourcecode::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_sourcecode::program_is_not_abstract():
    assert not inspect.isabstract(sourcecode::Program)


def test_sourcecode::program_constructor_exists():
    assert callable(sourcecode::Program.__init__)


def test_sourcecode::program_constructor_args():
    sig = inspect.signature(sourcecode::Program.__init__)
    params = list(sig.parameters.keys())



def test_sourcecode::while_is_not_abstract():
    assert not inspect.isabstract(sourcecode::While)


def test_sourcecode::while_constructor_exists():
    assert callable(sourcecode::While.__init__)


def test_sourcecode::while_constructor_args():
    sig = inspect.signature(sourcecode::While.__init__)
    params = list(sig.parameters.keys())



def test_sourcecode::statement_is_not_abstract():
    assert not inspect.isabstract(sourcecode::Statement)


def test_sourcecode::statement_constructor_exists():
    assert callable(sourcecode::Statement.__init__)


def test_sourcecode::statement_constructor_args():
    sig = inspect.signature(sourcecode::Statement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_sourcecode::statement_has_id():
    assert hasattr(sourcecode::Statement, "id")
    descriptor = None
    for klass in sourcecode::Statement.__mro__:
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
sourcecode::Decision_strategy = st.builds(
    sourcecode::Decision,
)
sourcecode::Assignment_strategy = st.builds(
    sourcecode::Assignment,
)
sourcecode::Program_strategy = st.builds(
    sourcecode::Program,
)
sourcecode::While_strategy = st.builds(
    sourcecode::While,
)
sourcecode::Statement_strategy = st.builds(
    sourcecode::Statement,
    id=
        safe_text
)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=sourcecode::Decision_strategy)
@settings(max_examples=50)
def test_sourcecode::decision_instantiation(instance):
    assert isinstance(instance, sourcecode::Decision)

@given(instance=sourcecode::Assignment_strategy)
@settings(max_examples=50)
def test_sourcecode::assignment_instantiation(instance):
    assert isinstance(instance, sourcecode::Assignment)

@given(instance=sourcecode::Program_strategy)
@settings(max_examples=50)
def test_sourcecode::program_instantiation(instance):
    assert isinstance(instance, sourcecode::Program)

@given(instance=sourcecode::While_strategy)
@settings(max_examples=50)
def test_sourcecode::while_instantiation(instance):
    assert isinstance(instance, sourcecode::While)

@given(instance=sourcecode::Statement_strategy)
@settings(max_examples=50)
def test_sourcecode::statement_instantiation(instance):
    assert isinstance(instance, sourcecode::Statement)

@given(instance=sourcecode::Statement_strategy)
def test_sourcecode::statement_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=sourcecode::Statement_strategy)
def test_sourcecode::statement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
