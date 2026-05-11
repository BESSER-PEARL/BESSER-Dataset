import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tests::Named,
    Named,
    tests::Root,
    tests::TypeB,
    tests::TypeA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tests::named_is_not_abstract():
    assert not inspect.isabstract(tests::Named)


def test_tests::named_constructor_exists():
    assert callable(tests::Named.__init__)


def test_tests::named_constructor_args():
    sig = inspect.signature(tests::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tests::named_has_name():
    assert hasattr(tests::Named, "name")
    descriptor = None
    for klass in tests::Named.__mro__:
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



def test_tests::root_is_not_abstract():
    assert not inspect.isabstract(tests::Root)


def test_tests::root_constructor_exists():
    assert callable(tests::Root.__init__)


def test_tests::root_constructor_args():
    sig = inspect.signature(tests::Root.__init__)
    params = list(sig.parameters.keys())



def test_tests::typeb_is_not_abstract():
    assert not inspect.isabstract(tests::TypeB)


def test_tests::typeb_constructor_exists():
    assert callable(tests::TypeB.__init__)


def test_tests::typeb_constructor_args():
    sig = inspect.signature(tests::TypeB.__init__)
    params = list(sig.parameters.keys())



def test_tests::typea_is_not_abstract():
    assert not inspect.isabstract(tests::TypeA)


def test_tests::typea_constructor_exists():
    assert callable(tests::TypeA.__init__)


def test_tests::typea_constructor_args():
    sig = inspect.signature(tests::TypeA.__init__)
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
tests::Named_strategy = st.builds(
    tests::Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
tests::Root_strategy = st.builds(
    tests::Root,
)
tests::TypeB_strategy = st.builds(
    tests::TypeB,
)
tests::TypeA_strategy = st.builds(
    tests::TypeA,
)

@given(instance=tests::Named_strategy)
@settings(max_examples=50)
def test_tests::named_instantiation(instance):
    assert isinstance(instance, tests::Named)

@given(instance=tests::Named_strategy)
def test_tests::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tests::Named_strategy)
def test_tests::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=tests::Root_strategy)
@settings(max_examples=50)
def test_tests::root_instantiation(instance):
    assert isinstance(instance, tests::Root)

@given(instance=tests::TypeB_strategy)
@settings(max_examples=50)
def test_tests::typeb_instantiation(instance):
    assert isinstance(instance, tests::TypeB)

@given(instance=tests::TypeA_strategy)
@settings(max_examples=50)
def test_tests::typea_instantiation(instance):
    assert isinstance(instance, tests::TypeA)
