import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    root_Test,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_root_test_is_not_abstract():
    assert not inspect.isabstract(root_Test)


def test_root_test_constructor_exists():
    assert callable(root_Test.__init__)


def test_root_test_constructor_args():
    sig = inspect.signature(root_Test.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "att1" in params, "Missing parameter 'att1'"
    assert "att2" in params, "Missing parameter 'att2'"

def test_root_test_has_name():
    assert hasattr(root_Test, "name")
    descriptor = None
    for klass in root_Test.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_root_test_has_att1():
    assert hasattr(root_Test, "att1")
    descriptor = None
    for klass in root_Test.__mro__:
        if "att1" in klass.__dict__:
            descriptor = klass.__dict__["att1"]
            break
    assert isinstance(descriptor, property)

def test_root_test_has_att2():
    assert hasattr(root_Test, "att2")
    descriptor = None
    for klass in root_Test.__mro__:
        if "att2" in klass.__dict__:
            descriptor = klass.__dict__["att2"]
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
root_Test_strategy = st.builds(
    root_Test,
    name=
        safe_text,
    att1=
        st.integers(),
    att2=
        st.integers()
)

@given(instance=root_Test_strategy)
@settings(max_examples=50)
def test_root_test_instantiation(instance):
    assert isinstance(instance, root_Test)



@given(instance=root_Test_strategy)
def test_root_test_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=root_Test_strategy)
def test_root_test_att1_setter(instance):
    original = instance.att1
    instance.att1 = original
    assert instance.att1 == original



@given(instance=root_Test_strategy)
def test_root_test_att2_setter(instance):
    original = instance.att2
    instance.att2 = original
    assert instance.att2 == original
