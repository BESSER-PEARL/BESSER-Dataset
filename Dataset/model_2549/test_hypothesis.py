import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    out_RootContainer,
    RootOut,
    out_E,
    out_D,
    out_RootOut,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_out_rootcontainer_is_not_abstract():
    assert not inspect.isabstract(out_RootContainer)


def test_out_rootcontainer_constructor_exists():
    assert callable(out_RootContainer.__init__)


def test_out_rootcontainer_constructor_args():
    sig = inspect.signature(out_RootContainer.__init__)
    params = list(sig.parameters.keys())



def test_rootout_is_not_abstract():
    assert not inspect.isabstract(RootOut)


def test_rootout_constructor_exists():
    assert callable(RootOut.__init__)


def test_rootout_constructor_args():
    sig = inspect.signature(RootOut.__init__)
    params = list(sig.parameters.keys())



def test_out_e_is_not_abstract():
    assert not inspect.isabstract(out_E)


def test_out_e_constructor_exists():
    assert callable(out_E.__init__)


def test_out_e_constructor_args():
    sig = inspect.signature(out_E.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_out_e_has_name():
    assert hasattr(out_E, "name")
    descriptor = None
    for klass in out_E.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_out_d_is_not_abstract():
    assert not inspect.isabstract(out_D)


def test_out_d_constructor_exists():
    assert callable(out_D.__init__)


def test_out_d_constructor_args():
    sig = inspect.signature(out_D.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_out_d_has_name():
    assert hasattr(out_D, "name")
    descriptor = None
    for klass in out_D.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_out_rootout_is_not_abstract():
    assert not inspect.isabstract(out_RootOut)


def test_out_rootout_constructor_exists():
    assert callable(out_RootOut.__init__)


def test_out_rootout_constructor_args():
    sig = inspect.signature(out_RootOut.__init__)
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
out_RootContainer_strategy = st.builds(
    out_RootContainer,
)
RootOut_strategy = st.builds(
    RootOut,
)
out_E_strategy = st.builds(
    out_E,
    name=
        safe_text
)
out_D_strategy = st.builds(
    out_D,
    name=
        safe_text
)
out_RootOut_strategy = st.builds(
    out_RootOut,
)

@given(instance=out_RootContainer_strategy)
@settings(max_examples=50)
def test_out_rootcontainer_instantiation(instance):
    assert isinstance(instance, out_RootContainer)

@given(instance=RootOut_strategy)
@settings(max_examples=50)
def test_rootout_instantiation(instance):
    assert isinstance(instance, RootOut)

@given(instance=out_E_strategy)
@settings(max_examples=50)
def test_out_e_instantiation(instance):
    assert isinstance(instance, out_E)



@given(instance=out_E_strategy)
def test_out_e_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=out_D_strategy)
@settings(max_examples=50)
def test_out_d_instantiation(instance):
    assert isinstance(instance, out_D)



@given(instance=out_D_strategy)
def test_out_d_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=out_RootOut_strategy)
@settings(max_examples=50)
def test_out_rootout_instantiation(instance):
    assert isinstance(instance, out_RootOut)
