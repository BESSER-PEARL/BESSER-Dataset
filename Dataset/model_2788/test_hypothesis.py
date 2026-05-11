import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    test1::StringToIntegerMapEntry,
    test1::ConceptA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test1::stringtointegermapentry_is_not_abstract():
    assert not inspect.isabstract(test1::StringToIntegerMapEntry)


def test_test1::stringtointegermapentry_constructor_exists():
    assert callable(test1::StringToIntegerMapEntry.__init__)


def test_test1::stringtointegermapentry_constructor_args():
    sig = inspect.signature(test1::StringToIntegerMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_test1::stringtointegermapentry_has_key():
    assert hasattr(test1::StringToIntegerMapEntry, "key")
    descriptor = None
    for klass in test1::StringToIntegerMapEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_test1::stringtointegermapentry_has_value():
    assert hasattr(test1::StringToIntegerMapEntry, "value")
    descriptor = None
    for klass in test1::StringToIntegerMapEntry.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_test1::concepta_is_not_abstract():
    assert not inspect.isabstract(test1::ConceptA)


def test_test1::concepta_constructor_exists():
    assert callable(test1::ConceptA.__init__)


def test_test1::concepta_constructor_args():
    sig = inspect.signature(test1::ConceptA.__init__)
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
test1::StringToIntegerMapEntry_strategy = st.builds(
    test1::StringToIntegerMapEntry,
    key=
        safe_text,
    value=
        safe_text
)
test1::ConceptA_strategy = st.builds(
    test1::ConceptA,
)

@given(instance=test1::StringToIntegerMapEntry_strategy)
@settings(max_examples=50)
def test_test1::stringtointegermapentry_instantiation(instance):
    assert isinstance(instance, test1::StringToIntegerMapEntry)

@given(instance=test1::StringToIntegerMapEntry_strategy)
def test_test1::stringtointegermapentry_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=test1::StringToIntegerMapEntry_strategy)
def test_test1::stringtointegermapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=test1::StringToIntegerMapEntry_strategy)
def test_test1::stringtointegermapentry_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=test1::StringToIntegerMapEntry_strategy)
def test_test1::stringtointegermapentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=test1::ConceptA_strategy)
@settings(max_examples=50)
def test_test1::concepta_instantiation(instance):
    assert isinstance(instance, test1::ConceptA)
