import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    p_ThisClassWasLast,
    p_ThisClassWasMiddle,
    p_ThisClassWasFirst,
    p_append,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_p_thisclasswaslast_is_not_abstract():
    assert not inspect.isabstract(p_ThisClassWasLast)


def test_p_thisclasswaslast_constructor_exists():
    assert callable(p_ThisClassWasLast.__init__)


def test_p_thisclasswaslast_constructor_args():
    sig = inspect.signature(p_ThisClassWasLast.__init__)
    params = list(sig.parameters.keys())



def test_p_thisclasswasmiddle_is_not_abstract():
    assert not inspect.isabstract(p_ThisClassWasMiddle)


def test_p_thisclasswasmiddle_constructor_exists():
    assert callable(p_ThisClassWasMiddle.__init__)


def test_p_thisclasswasmiddle_constructor_args():
    sig = inspect.signature(p_ThisClassWasMiddle.__init__)
    params = list(sig.parameters.keys())



def test_p_thisclasswasfirst_is_not_abstract():
    assert not inspect.isabstract(p_ThisClassWasFirst)


def test_p_thisclasswasfirst_constructor_exists():
    assert callable(p_ThisClassWasFirst.__init__)


def test_p_thisclasswasfirst_constructor_args():
    sig = inspect.signature(p_ThisClassWasFirst.__init__)
    params = list(sig.parameters.keys())



def test_p_append_is_not_abstract():
    assert not inspect.isabstract(p_append)


def test_p_append_constructor_exists():
    assert callable(p_append.__init__)


def test_p_append_constructor_args():
    sig = inspect.signature(p_append.__init__)
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
p_ThisClassWasLast_strategy = st.builds(
    p_ThisClassWasLast,
)
p_ThisClassWasMiddle_strategy = st.builds(
    p_ThisClassWasMiddle,
)
p_ThisClassWasFirst_strategy = st.builds(
    p_ThisClassWasFirst,
)
p_append_strategy = st.builds(
    p_append,
)

@given(instance=p_ThisClassWasLast_strategy)
@settings(max_examples=50)
def test_p_thisclasswaslast_instantiation(instance):
    assert isinstance(instance, p_ThisClassWasLast)

@given(instance=p_ThisClassWasMiddle_strategy)
@settings(max_examples=50)
def test_p_thisclasswasmiddle_instantiation(instance):
    assert isinstance(instance, p_ThisClassWasMiddle)

@given(instance=p_ThisClassWasFirst_strategy)
@settings(max_examples=50)
def test_p_thisclasswasfirst_instantiation(instance):
    assert isinstance(instance, p_ThisClassWasFirst)

@given(instance=p_append_strategy)
@settings(max_examples=50)
def test_p_append_instantiation(instance):
    assert isinstance(instance, p_append)
