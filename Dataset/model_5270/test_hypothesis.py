import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    testup::G,
    G,
    E,
    testup::F,
    AUp,
    testup::E,
    testup::D,
    testup::B,
    testup::AUp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testup::g_is_not_abstract():
    assert not inspect.isabstract(testup::G)


def test_testup::g_constructor_exists():
    assert callable(testup::G.__init__)


def test_testup::g_constructor_args():
    sig = inspect.signature(testup::G.__init__)
    params = list(sig.parameters.keys())



def test_g_is_not_abstract():
    assert not inspect.isabstract(G)


def test_g_constructor_exists():
    assert callable(G.__init__)


def test_g_constructor_args():
    sig = inspect.signature(G.__init__)
    params = list(sig.parameters.keys())



def test_e_is_not_abstract():
    assert not inspect.isabstract(E)


def test_e_constructor_exists():
    assert callable(E.__init__)


def test_e_constructor_args():
    sig = inspect.signature(E.__init__)
    params = list(sig.parameters.keys())



def test_testup::f_is_not_abstract():
    assert not inspect.isabstract(testup::F)


def test_testup::f_constructor_exists():
    assert callable(testup::F.__init__)


def test_testup::f_constructor_args():
    sig = inspect.signature(testup::F.__init__)
    params = list(sig.parameters.keys())



def test_aup_is_not_abstract():
    assert not inspect.isabstract(AUp)


def test_aup_constructor_exists():
    assert callable(AUp.__init__)


def test_aup_constructor_args():
    sig = inspect.signature(AUp.__init__)
    params = list(sig.parameters.keys())



def test_testup::e_is_not_abstract():
    assert not inspect.isabstract(testup::E)


def test_testup::e_constructor_exists():
    assert callable(testup::E.__init__)


def test_testup::e_constructor_args():
    sig = inspect.signature(testup::E.__init__)
    params = list(sig.parameters.keys())
    assert "newAttribute" in params, "Missing parameter 'newAttribute'"

def test_testup::e_has_newAttribute():
    assert hasattr(testup::E, "newAttribute")
    descriptor = None
    for klass in testup::E.__mro__:
        if "newAttribute" in klass.__dict__:
            descriptor = klass.__dict__["newAttribute"]
            break
    assert isinstance(descriptor, property)



def test_testup::d_is_not_abstract():
    assert not inspect.isabstract(testup::D)


def test_testup::d_constructor_exists():
    assert callable(testup::D.__init__)


def test_testup::d_constructor_args():
    sig = inspect.signature(testup::D.__init__)
    params = list(sig.parameters.keys())
    assert "newAttribute" in params, "Missing parameter 'newAttribute'"

def test_testup::d_has_newAttribute():
    assert hasattr(testup::D, "newAttribute")
    descriptor = None
    for klass in testup::D.__mro__:
        if "newAttribute" in klass.__dict__:
            descriptor = klass.__dict__["newAttribute"]
            break
    assert isinstance(descriptor, property)



def test_testup::b_is_not_abstract():
    assert not inspect.isabstract(testup::B)


def test_testup::b_constructor_exists():
    assert callable(testup::B.__init__)


def test_testup::b_constructor_args():
    sig = inspect.signature(testup::B.__init__)
    params = list(sig.parameters.keys())
    assert "newAttribute" in params, "Missing parameter 'newAttribute'"

def test_testup::b_has_newAttribute():
    assert hasattr(testup::B, "newAttribute")
    descriptor = None
    for klass in testup::B.__mro__:
        if "newAttribute" in klass.__dict__:
            descriptor = klass.__dict__["newAttribute"]
            break
    assert isinstance(descriptor, property)



def test_testup::aup_is_not_abstract():
    assert not inspect.isabstract(testup::AUp)


def test_testup::aup_constructor_exists():
    assert callable(testup::AUp.__init__)


def test_testup::aup_constructor_args():
    sig = inspect.signature(testup::AUp.__init__)
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
testup::G_strategy = st.builds(
    testup::G,
)
G_strategy = st.builds(
    G,
)
E_strategy = st.builds(
    E,
)
testup::F_strategy = st.builds(
    testup::F,
)
AUp_strategy = st.builds(
    AUp,
)
testup::E_strategy = st.builds(
    testup::E,
    newAttribute=
        safe_text
)
testup::D_strategy = st.builds(
    testup::D,
    newAttribute=
        safe_text
)
testup::B_strategy = st.builds(
    testup::B,
    newAttribute=
        safe_text
)
testup::AUp_strategy = st.builds(
    testup::AUp,
)

@given(instance=testup::G_strategy)
@settings(max_examples=50)
def test_testup::g_instantiation(instance):
    assert isinstance(instance, testup::G)

@given(instance=G_strategy)
@settings(max_examples=50)
def test_g_instantiation(instance):
    assert isinstance(instance, G)

@given(instance=E_strategy)
@settings(max_examples=50)
def test_e_instantiation(instance):
    assert isinstance(instance, E)

@given(instance=testup::F_strategy)
@settings(max_examples=50)
def test_testup::f_instantiation(instance):
    assert isinstance(instance, testup::F)

@given(instance=AUp_strategy)
@settings(max_examples=50)
def test_aup_instantiation(instance):
    assert isinstance(instance, AUp)

@given(instance=testup::E_strategy)
@settings(max_examples=50)
def test_testup::e_instantiation(instance):
    assert isinstance(instance, testup::E)

@given(instance=testup::E_strategy)
def test_testup::e_newAttribute_type(instance):
    assert isinstance(instance.newAttribute, str)


@given(instance=testup::E_strategy)
def test_testup::e_newAttribute_setter(instance):
    original = instance.newAttribute
    instance.newAttribute = original
    assert instance.newAttribute == original

@given(instance=testup::D_strategy)
@settings(max_examples=50)
def test_testup::d_instantiation(instance):
    assert isinstance(instance, testup::D)

@given(instance=testup::D_strategy)
def test_testup::d_newAttribute_type(instance):
    assert isinstance(instance.newAttribute, str)


@given(instance=testup::D_strategy)
def test_testup::d_newAttribute_setter(instance):
    original = instance.newAttribute
    instance.newAttribute = original
    assert instance.newAttribute == original

@given(instance=testup::B_strategy)
@settings(max_examples=50)
def test_testup::b_instantiation(instance):
    assert isinstance(instance, testup::B)

@given(instance=testup::B_strategy)
def test_testup::b_newAttribute_type(instance):
    assert isinstance(instance.newAttribute, str)


@given(instance=testup::B_strategy)
def test_testup::b_newAttribute_setter(instance):
    original = instance.newAttribute
    instance.newAttribute = original
    assert instance.newAttribute == original

@given(instance=testup::AUp_strategy)
@settings(max_examples=50)
def test_testup::aup_instantiation(instance):
    assert isinstance(instance, testup::AUp)
