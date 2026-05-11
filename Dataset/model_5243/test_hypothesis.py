import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sbase::EObject,
    sbase::SElement,
    SElement,
    sbase::Y,
    sbase::SRoot,
    sbase::X,
    sbase::Z,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sbase::eobject_is_not_abstract():
    assert not inspect.isabstract(sbase::EObject)


def test_sbase::eobject_constructor_exists():
    assert callable(sbase::EObject.__init__)


def test_sbase::eobject_constructor_args():
    sig = inspect.signature(sbase::EObject.__init__)
    params = list(sig.parameters.keys())



def test_sbase::selement_is_not_abstract():
    assert not inspect.isabstract(sbase::SElement)


def test_sbase::selement_constructor_exists():
    assert callable(sbase::SElement.__init__)


def test_sbase::selement_constructor_args():
    sig = inspect.signature(sbase::SElement.__init__)
    params = list(sig.parameters.keys())



def test_selement_is_not_abstract():
    assert not inspect.isabstract(SElement)


def test_selement_constructor_exists():
    assert callable(SElement.__init__)


def test_selement_constructor_args():
    sig = inspect.signature(SElement.__init__)
    params = list(sig.parameters.keys())



def test_sbase::y_is_not_abstract():
    assert not inspect.isabstract(sbase::Y)


def test_sbase::y_constructor_exists():
    assert callable(sbase::Y.__init__)


def test_sbase::y_constructor_args():
    sig = inspect.signature(sbase::Y.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sbase::y_has_name():
    assert hasattr(sbase::Y, "name")
    descriptor = None
    for klass in sbase::Y.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sbase::sroot_is_not_abstract():
    assert not inspect.isabstract(sbase::SRoot)


def test_sbase::sroot_constructor_exists():
    assert callable(sbase::SRoot.__init__)


def test_sbase::sroot_constructor_args():
    sig = inspect.signature(sbase::SRoot.__init__)
    params = list(sig.parameters.keys())



def test_sbase::x_is_not_abstract():
    assert not inspect.isabstract(sbase::X)


def test_sbase::x_constructor_exists():
    assert callable(sbase::X.__init__)


def test_sbase::x_constructor_args():
    sig = inspect.signature(sbase::X.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sbase::x_has_name():
    assert hasattr(sbase::X, "name")
    descriptor = None
    for klass in sbase::X.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sbase::z_is_not_abstract():
    assert not inspect.isabstract(sbase::Z)


def test_sbase::z_constructor_exists():
    assert callable(sbase::Z.__init__)


def test_sbase::z_constructor_args():
    sig = inspect.signature(sbase::Z.__init__)
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
sbase::EObject_strategy = st.builds(
    sbase::EObject,
)
sbase::SElement_strategy = st.builds(
    sbase::SElement,
)
SElement_strategy = st.builds(
    SElement,
)
sbase::Y_strategy = st.builds(
    sbase::Y,
    name=
        safe_text
)
sbase::SRoot_strategy = st.builds(
    sbase::SRoot,
)
sbase::X_strategy = st.builds(
    sbase::X,
    name=
        safe_text
)
sbase::Z_strategy = st.builds(
    sbase::Z,
)

@given(instance=sbase::EObject_strategy)
@settings(max_examples=50)
def test_sbase::eobject_instantiation(instance):
    assert isinstance(instance, sbase::EObject)

@given(instance=sbase::SElement_strategy)
@settings(max_examples=50)
def test_sbase::selement_instantiation(instance):
    assert isinstance(instance, sbase::SElement)

@given(instance=SElement_strategy)
@settings(max_examples=50)
def test_selement_instantiation(instance):
    assert isinstance(instance, SElement)

@given(instance=sbase::Y_strategy)
@settings(max_examples=50)
def test_sbase::y_instantiation(instance):
    assert isinstance(instance, sbase::Y)

@given(instance=sbase::Y_strategy)
def test_sbase::y_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sbase::Y_strategy)
def test_sbase::y_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sbase::SRoot_strategy)
@settings(max_examples=50)
def test_sbase::sroot_instantiation(instance):
    assert isinstance(instance, sbase::SRoot)

@given(instance=sbase::X_strategy)
@settings(max_examples=50)
def test_sbase::x_instantiation(instance):
    assert isinstance(instance, sbase::X)

@given(instance=sbase::X_strategy)
def test_sbase::x_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sbase::X_strategy)
def test_sbase::x_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sbase::Z_strategy)
@settings(max_examples=50)
def test_sbase::z_instantiation(instance):
    assert isinstance(instance, sbase::Z)
