import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    root::Test,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_root::test_is_not_abstract():
    assert not inspect.isabstract(root::Test)


def test_root::test_constructor_exists():
    assert callable(root::Test.__init__)


def test_root::test_constructor_args():
    sig = inspect.signature(root::Test.__init__)
    params = list(sig.parameters.keys())
    assert "att2" in params, "Missing parameter 'att2'"
    assert "name" in params, "Missing parameter 'name'"
    assert "att1" in params, "Missing parameter 'att1'"

def test_root::test_has_att2():
    assert hasattr(root::Test, "att2")
    descriptor = None
    for klass in root::Test.__mro__:
        if "att2" in klass.__dict__:
            descriptor = klass.__dict__["att2"]
            break
    assert isinstance(descriptor, property)

def test_root::test_has_name():
    assert hasattr(root::Test, "name")
    descriptor = None
    for klass in root::Test.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_root::test_has_att1():
    assert hasattr(root::Test, "att1")
    descriptor = None
    for klass in root::Test.__mro__:
        if "att1" in klass.__dict__:
            descriptor = klass.__dict__["att1"]
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
root::Test_strategy = st.builds(
    root::Test,
    att2=
        st.integers(),
    name=
        safe_text,
    att1=
        st.integers()
)

@given(instance=root::Test_strategy)
@settings(max_examples=50)
def test_root::test_instantiation(instance):
    assert isinstance(instance, root::Test)

@given(instance=root::Test_strategy)
def test_root::test_att2_type(instance):
    assert isinstance(instance.att2, int)


@given(instance=root::Test_strategy)
def test_root::test_att2_setter(instance):
    original = instance.att2
    instance.att2 = original
    assert instance.att2 == original

@given(instance=root::Test_strategy)
def test_root::test_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=root::Test_strategy)
def test_root::test_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=root::Test_strategy)
def test_root::test_att1_type(instance):
    assert isinstance(instance.att1, int)


@given(instance=root::Test_strategy)
def test_root::test_att1_setter(instance):
    original = instance.att1
    instance.att1 = original
    assert instance.att1 == original
