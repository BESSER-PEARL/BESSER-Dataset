import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Test_Foo,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test_foo_is_not_abstract():
    assert not inspect.isabstract(Test_Foo)


def test_test_foo_constructor_exists():
    assert callable(Test_Foo.__init__)


def test_test_foo_constructor_args():
    sig = inspect.signature(Test_Foo.__init__)
    params = list(sig.parameters.keys())
    assert "bar" in params, "Missing parameter 'bar'"

def test_test_foo_has_bar():
    assert hasattr(Test_Foo, "bar")
    descriptor = None
    for klass in Test_Foo.__mro__:
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
Test_Foo_strategy = st.builds(
    Test_Foo,
    bar=
        safe_text
)

@given(instance=Test_Foo_strategy)
@settings(max_examples=50)
def test_test_foo_instantiation(instance):
    assert isinstance(instance, Test_Foo)



@given(instance=Test_Foo_strategy)
def test_test_foo_bar_setter(instance):
    original = instance.bar
    instance.bar = original
    assert instance.bar == original
