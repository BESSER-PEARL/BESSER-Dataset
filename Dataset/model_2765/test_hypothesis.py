import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    tests_Named,
    Named,
    tests_Root,
    tests_TypeB,
    tests_TypeA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tests_named_is_not_abstract():
    assert not inspect.isabstract(tests_Named)


def test_tests_named_constructor_exists():
    assert callable(tests_Named.__init__)


def test_tests_named_constructor_args():
    sig = inspect.signature(tests_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tests_named_has_name():
    assert hasattr(tests_Named, "name")
    descriptor = None
    for klass in tests_Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_tests_root_is_not_abstract():
    assert not inspect.isabstract(tests_Root)


def test_tests_root_constructor_exists():
    assert callable(tests_Root.__init__)


def test_tests_root_constructor_args():
    sig = inspect.signature(tests_Root.__init__)
    params = list(sig.parameters.keys())



def test_tests_typeb_is_not_abstract():
    assert not inspect.isabstract(tests_TypeB)


def test_tests_typeb_constructor_exists():
    assert callable(tests_TypeB.__init__)


def test_tests_typeb_constructor_args():
    sig = inspect.signature(tests_TypeB.__init__)
    params = list(sig.parameters.keys())



def test_tests_typea_is_not_abstract():
    assert not inspect.isabstract(tests_TypeA)


def test_tests_typea_constructor_exists():
    assert callable(tests_TypeA.__init__)


def test_tests_typea_constructor_args():
    sig = inspect.signature(tests_TypeA.__init__)
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
tests_Named_strategy = st.builds(
    tests_Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
tests_Root_strategy = st.builds(
    tests_Root,
)
tests_TypeB_strategy = st.builds(
    tests_TypeB,
)
tests_TypeA_strategy = st.builds(
    tests_TypeA,
)

@given(instance=tests_Named_strategy)
@settings(max_examples=50)
def test_tests_named_instantiation(instance):
    assert isinstance(instance, tests_Named)



@given(instance=tests_Named_strategy)
def test_tests_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=tests_Root_strategy)
@settings(max_examples=50)
def test_tests_root_instantiation(instance):
    assert isinstance(instance, tests_Root)

@given(instance=tests_TypeB_strategy)
@settings(max_examples=50)
def test_tests_typeb_instantiation(instance):
    assert isinstance(instance, tests_TypeB)

@given(instance=tests_TypeA_strategy)
@settings(max_examples=50)
def test_tests_typea_instantiation(instance):
    assert isinstance(instance, tests_TypeA)
