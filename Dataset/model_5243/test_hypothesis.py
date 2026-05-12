import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sbase_EObject,
    sbase_SElement,
    SElement,
    sbase_SRoot,
    sbase_Y,
    sbase_X,
    sbase_Z,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sbase_eobject_is_not_abstract():
    assert not inspect.isabstract(sbase_EObject)


def test_sbase_eobject_constructor_exists():
    assert callable(sbase_EObject.__init__)


def test_sbase_eobject_constructor_args():
    sig = inspect.signature(sbase_EObject.__init__)
    params = list(sig.parameters.keys())



def test_sbase_selement_is_not_abstract():
    assert not inspect.isabstract(sbase_SElement)


def test_sbase_selement_constructor_exists():
    assert callable(sbase_SElement.__init__)


def test_sbase_selement_constructor_args():
    sig = inspect.signature(sbase_SElement.__init__)
    params = list(sig.parameters.keys())



def test_selement_is_not_abstract():
    assert not inspect.isabstract(SElement)


def test_selement_constructor_exists():
    assert callable(SElement.__init__)


def test_selement_constructor_args():
    sig = inspect.signature(SElement.__init__)
    params = list(sig.parameters.keys())



def test_sbase_sroot_is_not_abstract():
    assert not inspect.isabstract(sbase_SRoot)


def test_sbase_sroot_constructor_exists():
    assert callable(sbase_SRoot.__init__)


def test_sbase_sroot_constructor_args():
    sig = inspect.signature(sbase_SRoot.__init__)
    params = list(sig.parameters.keys())



def test_sbase_y_is_not_abstract():
    assert not inspect.isabstract(sbase_Y)


def test_sbase_y_constructor_exists():
    assert callable(sbase_Y.__init__)


def test_sbase_y_constructor_args():
    sig = inspect.signature(sbase_Y.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sbase_y_has_name():
    assert hasattr(sbase_Y, "name")
    descriptor = None
    for klass in sbase_Y.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sbase_x_is_not_abstract():
    assert not inspect.isabstract(sbase_X)


def test_sbase_x_constructor_exists():
    assert callable(sbase_X.__init__)


def test_sbase_x_constructor_args():
    sig = inspect.signature(sbase_X.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sbase_x_has_name():
    assert hasattr(sbase_X, "name")
    descriptor = None
    for klass in sbase_X.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sbase_z_is_not_abstract():
    assert not inspect.isabstract(sbase_Z)


def test_sbase_z_constructor_exists():
    assert callable(sbase_Z.__init__)


def test_sbase_z_constructor_args():
    sig = inspect.signature(sbase_Z.__init__)
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
sbase_EObject_strategy = st.builds(
    sbase_EObject,
)
sbase_SElement_strategy = st.builds(
    sbase_SElement,
)
SElement_strategy = st.builds(
    SElement,
)
sbase_SRoot_strategy = st.builds(
    sbase_SRoot,
)
sbase_Y_strategy = st.builds(
    sbase_Y,
    name=
        safe_text
)
sbase_X_strategy = st.builds(
    sbase_X,
    name=
        safe_text
)
sbase_Z_strategy = st.builds(
    sbase_Z,
)

@given(instance=sbase_EObject_strategy)
@settings(max_examples=50)
def test_sbase_eobject_instantiation(instance):
    assert isinstance(instance, sbase_EObject)

@given(instance=sbase_SElement_strategy)
@settings(max_examples=50)
def test_sbase_selement_instantiation(instance):
    assert isinstance(instance, sbase_SElement)

@given(instance=SElement_strategy)
@settings(max_examples=50)
def test_selement_instantiation(instance):
    assert isinstance(instance, SElement)

@given(instance=sbase_SRoot_strategy)
@settings(max_examples=50)
def test_sbase_sroot_instantiation(instance):
    assert isinstance(instance, sbase_SRoot)

@given(instance=sbase_Y_strategy)
@settings(max_examples=50)
def test_sbase_y_instantiation(instance):
    assert isinstance(instance, sbase_Y)



@given(instance=sbase_Y_strategy)
def test_sbase_y_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sbase_X_strategy)
@settings(max_examples=50)
def test_sbase_x_instantiation(instance):
    assert isinstance(instance, sbase_X)



@given(instance=sbase_X_strategy)
def test_sbase_x_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sbase_Z_strategy)
@settings(max_examples=50)
def test_sbase_z_instantiation(instance):
    assert isinstance(instance, sbase_Z)
