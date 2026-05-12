import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    testup_G,
    G,
    E,
    testup_F,
    AUp,
    testup_E,
    testup_D,
    testup_B,
    testup_AUp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testup_g_is_not_abstract():
    assert not inspect.isabstract(testup_G)


def test_testup_g_constructor_exists():
    assert callable(testup_G.__init__)


def test_testup_g_constructor_args():
    sig = inspect.signature(testup_G.__init__)
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



def test_testup_f_is_not_abstract():
    assert not inspect.isabstract(testup_F)


def test_testup_f_constructor_exists():
    assert callable(testup_F.__init__)


def test_testup_f_constructor_args():
    sig = inspect.signature(testup_F.__init__)
    params = list(sig.parameters.keys())



def test_aup_is_not_abstract():
    assert not inspect.isabstract(AUp)


def test_aup_constructor_exists():
    assert callable(AUp.__init__)


def test_aup_constructor_args():
    sig = inspect.signature(AUp.__init__)
    params = list(sig.parameters.keys())



def test_testup_e_is_not_abstract():
    assert not inspect.isabstract(testup_E)


def test_testup_e_constructor_exists():
    assert callable(testup_E.__init__)


def test_testup_e_constructor_args():
    sig = inspect.signature(testup_E.__init__)
    params = list(sig.parameters.keys())
    assert "newAttribute" in params, "Missing parameter 'newAttribute'"

def test_testup_e_has_newAttribute():
    assert hasattr(testup_E, "newAttribute")
    descriptor = None
    for klass in testup_E.__mro__:
        if "newAttribute" in klass.__dict__:
            descriptor = klass.__dict__["newAttribute"]
            break
    assert isinstance(descriptor, property)



def test_testup_d_is_not_abstract():
    assert not inspect.isabstract(testup_D)


def test_testup_d_constructor_exists():
    assert callable(testup_D.__init__)


def test_testup_d_constructor_args():
    sig = inspect.signature(testup_D.__init__)
    params = list(sig.parameters.keys())
    assert "newAttribute" in params, "Missing parameter 'newAttribute'"

def test_testup_d_has_newAttribute():
    assert hasattr(testup_D, "newAttribute")
    descriptor = None
    for klass in testup_D.__mro__:
        if "newAttribute" in klass.__dict__:
            descriptor = klass.__dict__["newAttribute"]
            break
    assert isinstance(descriptor, property)



def test_testup_b_is_not_abstract():
    assert not inspect.isabstract(testup_B)


def test_testup_b_constructor_exists():
    assert callable(testup_B.__init__)


def test_testup_b_constructor_args():
    sig = inspect.signature(testup_B.__init__)
    params = list(sig.parameters.keys())
    assert "newAttribute" in params, "Missing parameter 'newAttribute'"

def test_testup_b_has_newAttribute():
    assert hasattr(testup_B, "newAttribute")
    descriptor = None
    for klass in testup_B.__mro__:
        if "newAttribute" in klass.__dict__:
            descriptor = klass.__dict__["newAttribute"]
            break
    assert isinstance(descriptor, property)



def test_testup_aup_is_not_abstract():
    assert not inspect.isabstract(testup_AUp)


def test_testup_aup_constructor_exists():
    assert callable(testup_AUp.__init__)


def test_testup_aup_constructor_args():
    sig = inspect.signature(testup_AUp.__init__)
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
testup_G_strategy = st.builds(
    testup_G,
)
G_strategy = st.builds(
    G,
)
E_strategy = st.builds(
    E,
)
testup_F_strategy = st.builds(
    testup_F,
)
AUp_strategy = st.builds(
    AUp,
)
testup_E_strategy = st.builds(
    testup_E,
    newAttribute=
        safe_text
)
testup_D_strategy = st.builds(
    testup_D,
    newAttribute=
        safe_text
)
testup_B_strategy = st.builds(
    testup_B,
    newAttribute=
        safe_text
)
testup_AUp_strategy = st.builds(
    testup_AUp,
)

@given(instance=testup_G_strategy)
@settings(max_examples=50)
def test_testup_g_instantiation(instance):
    assert isinstance(instance, testup_G)

@given(instance=G_strategy)
@settings(max_examples=50)
def test_g_instantiation(instance):
    assert isinstance(instance, G)

@given(instance=E_strategy)
@settings(max_examples=50)
def test_e_instantiation(instance):
    assert isinstance(instance, E)

@given(instance=testup_F_strategy)
@settings(max_examples=50)
def test_testup_f_instantiation(instance):
    assert isinstance(instance, testup_F)

@given(instance=AUp_strategy)
@settings(max_examples=50)
def test_aup_instantiation(instance):
    assert isinstance(instance, AUp)

@given(instance=testup_E_strategy)
@settings(max_examples=50)
def test_testup_e_instantiation(instance):
    assert isinstance(instance, testup_E)



@given(instance=testup_E_strategy)
def test_testup_e_newAttribute_setter(instance):
    original = instance.newAttribute
    instance.newAttribute = original
    assert instance.newAttribute == original

@given(instance=testup_D_strategy)
@settings(max_examples=50)
def test_testup_d_instantiation(instance):
    assert isinstance(instance, testup_D)



@given(instance=testup_D_strategy)
def test_testup_d_newAttribute_setter(instance):
    original = instance.newAttribute
    instance.newAttribute = original
    assert instance.newAttribute == original

@given(instance=testup_B_strategy)
@settings(max_examples=50)
def test_testup_b_instantiation(instance):
    assert isinstance(instance, testup_B)



@given(instance=testup_B_strategy)
def test_testup_b_newAttribute_setter(instance):
    original = instance.newAttribute
    instance.newAttribute = original
    assert instance.newAttribute == original

@given(instance=testup_AUp_strategy)
@settings(max_examples=50)
def test_testup_aup_instantiation(instance):
    assert isinstance(instance, testup_AUp)
