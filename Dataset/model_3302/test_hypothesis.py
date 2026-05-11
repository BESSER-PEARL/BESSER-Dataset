import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    trigger::Decorator,
    trigger::Predicate,
    Decorator,
    trigger::Trigger,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trigger::decorator_is_not_abstract():
    assert not inspect.isabstract(trigger::Decorator)


def test_trigger::decorator_constructor_exists():
    assert callable(trigger::Decorator.__init__)


def test_trigger::decorator_constructor_args():
    sig = inspect.signature(trigger::Decorator.__init__)
    params = list(sig.parameters.keys())



def test_trigger::predicate_is_not_abstract():
    assert not inspect.isabstract(trigger::Predicate)


def test_trigger::predicate_constructor_exists():
    assert callable(trigger::Predicate.__init__)


def test_trigger::predicate_constructor_args():
    sig = inspect.signature(trigger::Predicate.__init__)
    params = list(sig.parameters.keys())



def test_decorator_is_not_abstract():
    assert not inspect.isabstract(Decorator)


def test_decorator_constructor_exists():
    assert callable(Decorator.__init__)


def test_decorator_constructor_args():
    sig = inspect.signature(Decorator.__init__)
    params = list(sig.parameters.keys())



def test_trigger::trigger_is_not_abstract():
    assert not inspect.isabstract(trigger::Trigger)


def test_trigger::trigger_constructor_exists():
    assert callable(trigger::Trigger.__init__)


def test_trigger::trigger_constructor_args():
    sig = inspect.signature(trigger::Trigger.__init__)
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
trigger::Decorator_strategy = st.builds(
    trigger::Decorator,
)
trigger::Predicate_strategy = st.builds(
    trigger::Predicate,
)
Decorator_strategy = st.builds(
    Decorator,
)
trigger::Trigger_strategy = st.builds(
    trigger::Trigger,
)

@given(instance=trigger::Decorator_strategy)
@settings(max_examples=50)
def test_trigger::decorator_instantiation(instance):
    assert isinstance(instance, trigger::Decorator)

@given(instance=trigger::Predicate_strategy)
@settings(max_examples=50)
def test_trigger::predicate_instantiation(instance):
    assert isinstance(instance, trigger::Predicate)

@given(instance=Decorator_strategy)
@settings(max_examples=50)
def test_decorator_instantiation(instance):
    assert isinstance(instance, Decorator)

@given(instance=trigger::Trigger_strategy)
@settings(max_examples=50)
def test_trigger::trigger_instantiation(instance):
    assert isinstance(instance, trigger::Trigger)
