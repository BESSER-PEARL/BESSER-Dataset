import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    out::RootContainer,
    RootOut,
    out::E,
    out::D,
    out::RootOut,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_out::rootcontainer_is_not_abstract():
    assert not inspect.isabstract(out::RootContainer)


def test_out::rootcontainer_constructor_exists():
    assert callable(out::RootContainer.__init__)


def test_out::rootcontainer_constructor_args():
    sig = inspect.signature(out::RootContainer.__init__)
    params = list(sig.parameters.keys())



def test_rootout_is_not_abstract():
    assert not inspect.isabstract(RootOut)


def test_rootout_constructor_exists():
    assert callable(RootOut.__init__)


def test_rootout_constructor_args():
    sig = inspect.signature(RootOut.__init__)
    params = list(sig.parameters.keys())



def test_out::e_is_not_abstract():
    assert not inspect.isabstract(out::E)


def test_out::e_constructor_exists():
    assert callable(out::E.__init__)


def test_out::e_constructor_args():
    sig = inspect.signature(out::E.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_out::e_has_name():
    assert hasattr(out::E, "name")
    descriptor = None
    for klass in out::E.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_out::d_is_not_abstract():
    assert not inspect.isabstract(out::D)


def test_out::d_constructor_exists():
    assert callable(out::D.__init__)


def test_out::d_constructor_args():
    sig = inspect.signature(out::D.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_out::d_has_name():
    assert hasattr(out::D, "name")
    descriptor = None
    for klass in out::D.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_out::rootout_is_not_abstract():
    assert not inspect.isabstract(out::RootOut)


def test_out::rootout_constructor_exists():
    assert callable(out::RootOut.__init__)


def test_out::rootout_constructor_args():
    sig = inspect.signature(out::RootOut.__init__)
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
out::RootContainer_strategy = st.builds(
    out::RootContainer,
)
RootOut_strategy = st.builds(
    RootOut,
)
out::E_strategy = st.builds(
    out::E,
    name=
        safe_text
)
out::D_strategy = st.builds(
    out::D,
    name=
        safe_text
)
out::RootOut_strategy = st.builds(
    out::RootOut,
)

@given(instance=out::RootContainer_strategy)
@settings(max_examples=50)
def test_out::rootcontainer_instantiation(instance):
    assert isinstance(instance, out::RootContainer)

@given(instance=RootOut_strategy)
@settings(max_examples=50)
def test_rootout_instantiation(instance):
    assert isinstance(instance, RootOut)

@given(instance=out::E_strategy)
@settings(max_examples=50)
def test_out::e_instantiation(instance):
    assert isinstance(instance, out::E)

@given(instance=out::E_strategy)
def test_out::e_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=out::E_strategy)
def test_out::e_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=out::D_strategy)
@settings(max_examples=50)
def test_out::d_instantiation(instance):
    assert isinstance(instance, out::D)

@given(instance=out::D_strategy)
def test_out::d_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=out::D_strategy)
def test_out::d_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=out::RootOut_strategy)
@settings(max_examples=50)
def test_out::rootout_instantiation(instance):
    assert isinstance(instance, out::RootOut)
