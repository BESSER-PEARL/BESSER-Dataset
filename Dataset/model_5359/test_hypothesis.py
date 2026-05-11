import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Test::Foo,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test::foo_is_not_abstract():
    assert not inspect.isabstract(Test::Foo)


def test_test::foo_constructor_exists():
    assert callable(Test::Foo.__init__)


def test_test::foo_constructor_args():
    sig = inspect.signature(Test::Foo.__init__)
    params = list(sig.parameters.keys())
    assert "bar" in params, "Missing parameter 'bar'"

def test_test::foo_has_bar():
    assert hasattr(Test::Foo, "bar")
    descriptor = None
    for klass in Test::Foo.__mro__:
        if "bar" in klass.__dict__:
            descriptor = klass.__dict__["bar"]
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
Test::Foo_strategy = st.builds(
    Test::Foo,
    bar=
        safe_text
)

@given(instance=Test::Foo_strategy)
@settings(max_examples=50)
def test_test::foo_instantiation(instance):
    assert isinstance(instance, Test::Foo)

@given(instance=Test::Foo_strategy)
def test_test::foo_bar_type(instance):
    assert isinstance(instance.bar, str)


@given(instance=Test::Foo_strategy)
def test_test::foo_bar_setter(instance):
    original = instance.bar
    instance.bar = original
    assert instance.bar == original
