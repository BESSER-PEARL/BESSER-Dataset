import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    p::ThisClassWasLast,
    p::ThisClassWasMiddle,
    p::ThisClassWasFirst,
    p::append,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_p::thisclasswaslast_is_not_abstract():
    assert not inspect.isabstract(p::ThisClassWasLast)


def test_p::thisclasswaslast_constructor_exists():
    assert callable(p::ThisClassWasLast.__init__)


def test_p::thisclasswaslast_constructor_args():
    sig = inspect.signature(p::ThisClassWasLast.__init__)
    params = list(sig.parameters.keys())



def test_p::thisclasswasmiddle_is_not_abstract():
    assert not inspect.isabstract(p::ThisClassWasMiddle)


def test_p::thisclasswasmiddle_constructor_exists():
    assert callable(p::ThisClassWasMiddle.__init__)


def test_p::thisclasswasmiddle_constructor_args():
    sig = inspect.signature(p::ThisClassWasMiddle.__init__)
    params = list(sig.parameters.keys())



def test_p::thisclasswasfirst_is_not_abstract():
    assert not inspect.isabstract(p::ThisClassWasFirst)


def test_p::thisclasswasfirst_constructor_exists():
    assert callable(p::ThisClassWasFirst.__init__)


def test_p::thisclasswasfirst_constructor_args():
    sig = inspect.signature(p::ThisClassWasFirst.__init__)
    params = list(sig.parameters.keys())



def test_p::append_is_not_abstract():
    assert not inspect.isabstract(p::append)


def test_p::append_constructor_exists():
    assert callable(p::append.__init__)


def test_p::append_constructor_args():
    sig = inspect.signature(p::append.__init__)
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
p::ThisClassWasLast_strategy = st.builds(
    p::ThisClassWasLast,
)
p::ThisClassWasMiddle_strategy = st.builds(
    p::ThisClassWasMiddle,
)
p::ThisClassWasFirst_strategy = st.builds(
    p::ThisClassWasFirst,
)
p::append_strategy = st.builds(
    p::append,
)

@given(instance=p::ThisClassWasLast_strategy)
@settings(max_examples=50)
def test_p::thisclasswaslast_instantiation(instance):
    assert isinstance(instance, p::ThisClassWasLast)

@given(instance=p::ThisClassWasMiddle_strategy)
@settings(max_examples=50)
def test_p::thisclasswasmiddle_instantiation(instance):
    assert isinstance(instance, p::ThisClassWasMiddle)

@given(instance=p::ThisClassWasFirst_strategy)
@settings(max_examples=50)
def test_p::thisclasswasfirst_instantiation(instance):
    assert isinstance(instance, p::ThisClassWasFirst)

@given(instance=p::append_strategy)
@settings(max_examples=50)
def test_p::append_instantiation(instance):
    assert isinstance(instance, p::append)
