import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    trigger_Decorator,
    trigger_Predicate,
    Decorator,
    trigger_Trigger,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trigger_decorator_is_not_abstract():
    assert not inspect.isabstract(trigger_Decorator)


def test_trigger_decorator_constructor_exists():
    assert callable(trigger_Decorator.__init__)


def test_trigger_decorator_constructor_args():
    sig = inspect.signature(trigger_Decorator.__init__)
    params = list(sig.parameters.keys())



def test_trigger_predicate_is_not_abstract():
    assert not inspect.isabstract(trigger_Predicate)


def test_trigger_predicate_constructor_exists():
    assert callable(trigger_Predicate.__init__)


def test_trigger_predicate_constructor_args():
    sig = inspect.signature(trigger_Predicate.__init__)
    params = list(sig.parameters.keys())



def test_decorator_is_not_abstract():
    assert not inspect.isabstract(Decorator)


def test_decorator_constructor_exists():
    assert callable(Decorator.__init__)


def test_decorator_constructor_args():
    sig = inspect.signature(Decorator.__init__)
    params = list(sig.parameters.keys())



def test_trigger_trigger_is_not_abstract():
    assert not inspect.isabstract(trigger_Trigger)


def test_trigger_trigger_constructor_exists():
    assert callable(trigger_Trigger.__init__)


def test_trigger_trigger_constructor_args():
    sig = inspect.signature(trigger_Trigger.__init__)
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
trigger_Decorator_strategy = st.builds(
    trigger_Decorator,
)
trigger_Predicate_strategy = st.builds(
    trigger_Predicate,
)
Decorator_strategy = st.builds(
    Decorator,
)
trigger_Trigger_strategy = st.builds(
    trigger_Trigger,
)

@given(instance=trigger_Decorator_strategy)
@settings(max_examples=50)
def test_trigger_decorator_instantiation(instance):
    assert isinstance(instance, trigger_Decorator)

@given(instance=trigger_Predicate_strategy)
@settings(max_examples=50)
def test_trigger_predicate_instantiation(instance):
    assert isinstance(instance, trigger_Predicate)

@given(instance=Decorator_strategy)
@settings(max_examples=50)
def test_decorator_instantiation(instance):
    assert isinstance(instance, Decorator)

@given(instance=trigger_Trigger_strategy)
@settings(max_examples=50)
def test_trigger_trigger_instantiation(instance):
    assert isinstance(instance, trigger_Trigger)
