import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    test::F,
    test::E,
    test::D,
    test::C,
    test::B,
    E,
    test::Adown,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test::f_is_not_abstract():
    assert not inspect.isabstract(test::F)


def test_test::f_constructor_exists():
    assert callable(test::F.__init__)


def test_test::f_constructor_args():
    sig = inspect.signature(test::F.__init__)
    params = list(sig.parameters.keys())



def test_test::e_is_not_abstract():
    assert not inspect.isabstract(test::E)


def test_test::e_constructor_exists():
    assert callable(test::E.__init__)


def test_test::e_constructor_args():
    sig = inspect.signature(test::E.__init__)
    params = list(sig.parameters.keys())
    assert "newAttribute2" in params, "Missing parameter 'newAttribute2'"

def test_test::e_has_newAttribute2():
    assert hasattr(test::E, "newAttribute2")
    descriptor = None
    for klass in test::E.__mro__:
        if "newAttribute2" in klass.__dict__:
            descriptor = klass.__dict__["newAttribute2"]
            break
    assert isinstance(descriptor, property)



def test_test::d_is_not_abstract():
    assert not inspect.isabstract(test::D)


def test_test::d_constructor_exists():
    assert callable(test::D.__init__)


def test_test::d_constructor_args():
    sig = inspect.signature(test::D.__init__)
    params = list(sig.parameters.keys())
    assert "newAttribute" in params, "Missing parameter 'newAttribute'"

def test_test::d_has_newAttribute():
    assert hasattr(test::D, "newAttribute")
    descriptor = None
    for klass in test::D.__mro__:
        if "newAttribute" in klass.__dict__:
            descriptor = klass.__dict__["newAttribute"]
            break
    assert isinstance(descriptor, property)



def test_test::c_is_not_abstract():
    assert not inspect.isabstract(test::C)


def test_test::c_constructor_exists():
    assert callable(test::C.__init__)


def test_test::c_constructor_args():
    sig = inspect.signature(test::C.__init__)
    params = list(sig.parameters.keys())
    assert "newAttribute" in params, "Missing parameter 'newAttribute'"

def test_test::c_has_newAttribute():
    assert hasattr(test::C, "newAttribute")
    descriptor = None
    for klass in test::C.__mro__:
        if "newAttribute" in klass.__dict__:
            descriptor = klass.__dict__["newAttribute"]
            break
    assert isinstance(descriptor, property)



def test_test::b_is_not_abstract():
    assert not inspect.isabstract(test::B)


def test_test::b_constructor_exists():
    assert callable(test::B.__init__)


def test_test::b_constructor_args():
    sig = inspect.signature(test::B.__init__)
    params = list(sig.parameters.keys())
    assert "newAttribute" in params, "Missing parameter 'newAttribute'"

def test_test::b_has_newAttribute():
    assert hasattr(test::B, "newAttribute")
    descriptor = None
    for klass in test::B.__mro__:
        if "newAttribute" in klass.__dict__:
            descriptor = klass.__dict__["newAttribute"]
            break
    assert isinstance(descriptor, property)



def test_e_is_not_abstract():
    assert not inspect.isabstract(E)


def test_e_constructor_exists():
    assert callable(E.__init__)


def test_e_constructor_args():
    sig = inspect.signature(E.__init__)
    params = list(sig.parameters.keys())



def test_test::adown_is_not_abstract():
    assert not inspect.isabstract(test::Adown)


def test_test::adown_constructor_exists():
    assert callable(test::Adown.__init__)


def test_test::adown_constructor_args():
    sig = inspect.signature(test::Adown.__init__)
    params = list(sig.parameters.keys())
    assert "newAttribute" in params, "Missing parameter 'newAttribute'"

def test_test::adown_has_newAttribute():
    assert hasattr(test::Adown, "newAttribute")
    descriptor = None
    for klass in test::Adown.__mro__:
        if "newAttribute" in klass.__dict__:
            descriptor = klass.__dict__["newAttribute"]
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
test::F_strategy = st.builds(
    test::F,
)
test::E_strategy = st.builds(
    test::E,
    newAttribute2=
        safe_text
)
test::D_strategy = st.builds(
    test::D,
    newAttribute=
        safe_text
)
test::C_strategy = st.builds(
    test::C,
    newAttribute=
        safe_text
)
test::B_strategy = st.builds(
    test::B,
    newAttribute=
        safe_text
)
E_strategy = st.builds(
    E,
)
test::Adown_strategy = st.builds(
    test::Adown,
    newAttribute=
        safe_text
)

@given(instance=test::F_strategy)
@settings(max_examples=50)
def test_test::f_instantiation(instance):
    assert isinstance(instance, test::F)

@given(instance=test::E_strategy)
@settings(max_examples=50)
def test_test::e_instantiation(instance):
    assert isinstance(instance, test::E)

@given(instance=test::E_strategy)
def test_test::e_newAttribute2_type(instance):
    assert isinstance(instance.newAttribute2, str)


@given(instance=test::E_strategy)
def test_test::e_newAttribute2_setter(instance):
    original = instance.newAttribute2
    instance.newAttribute2 = original
    assert instance.newAttribute2 == original

@given(instance=test::D_strategy)
@settings(max_examples=50)
def test_test::d_instantiation(instance):
    assert isinstance(instance, test::D)

@given(instance=test::D_strategy)
def test_test::d_newAttribute_type(instance):
    assert isinstance(instance.newAttribute, str)


@given(instance=test::D_strategy)
def test_test::d_newAttribute_setter(instance):
    original = instance.newAttribute
    instance.newAttribute = original
    assert instance.newAttribute == original

@given(instance=test::C_strategy)
@settings(max_examples=50)
def test_test::c_instantiation(instance):
    assert isinstance(instance, test::C)

@given(instance=test::C_strategy)
def test_test::c_newAttribute_type(instance):
    assert isinstance(instance.newAttribute, str)


@given(instance=test::C_strategy)
def test_test::c_newAttribute_setter(instance):
    original = instance.newAttribute
    instance.newAttribute = original
    assert instance.newAttribute == original

@given(instance=test::B_strategy)
@settings(max_examples=50)
def test_test::b_instantiation(instance):
    assert isinstance(instance, test::B)

@given(instance=test::B_strategy)
def test_test::b_newAttribute_type(instance):
    assert isinstance(instance.newAttribute, str)


@given(instance=test::B_strategy)
def test_test::b_newAttribute_setter(instance):
    original = instance.newAttribute
    instance.newAttribute = original
    assert instance.newAttribute == original

@given(instance=E_strategy)
@settings(max_examples=50)
def test_e_instantiation(instance):
    assert isinstance(instance, E)

@given(instance=test::Adown_strategy)
@settings(max_examples=50)
def test_test::adown_instantiation(instance):
    assert isinstance(instance, test::Adown)

@given(instance=test::Adown_strategy)
def test_test::adown_newAttribute_type(instance):
    assert isinstance(instance.newAttribute, str)


@given(instance=test::Adown_strategy)
def test_test::adown_newAttribute_setter(instance):
    original = instance.newAttribute
    instance.newAttribute = original
    assert instance.newAttribute == original
