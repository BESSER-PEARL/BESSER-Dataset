import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    test_F,
    test_E,
    test_D,
    test_C,
    test_B,
    E,
    test_Adown,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test_f_is_not_abstract():
    assert not inspect.isabstract(test_F)


def test_test_f_constructor_exists():
    assert callable(test_F.__init__)


def test_test_f_constructor_args():
    sig = inspect.signature(test_F.__init__)
    params = list(sig.parameters.keys())



def test_test_e_is_not_abstract():
    assert not inspect.isabstract(test_E)


def test_test_e_constructor_exists():
    assert callable(test_E.__init__)


def test_test_e_constructor_args():
    sig = inspect.signature(test_E.__init__)
    params = list(sig.parameters.keys())
    assert "newAttribute2" in params, "Missing parameter 'newAttribute2'"

def test_test_e_has_newAttribute2():
    assert hasattr(test_E, "newAttribute2")
    descriptor = None
    for klass in test_E.__mro__:
        if "newAttribute2" in klass.__dict__:
            descriptor = klass.__dict__["newAttribute2"]
            break
    assert isinstance(descriptor, property)



def test_test_d_is_not_abstract():
    assert not inspect.isabstract(test_D)


def test_test_d_constructor_exists():
    assert callable(test_D.__init__)


def test_test_d_constructor_args():
    sig = inspect.signature(test_D.__init__)
    params = list(sig.parameters.keys())
    assert "newAttribute" in params, "Missing parameter 'newAttribute'"

def test_test_d_has_newAttribute():
    assert hasattr(test_D, "newAttribute")
    descriptor = None
    for klass in test_D.__mro__:
        if "newAttribute" in klass.__dict__:
            descriptor = klass.__dict__["newAttribute"]
            break
    assert isinstance(descriptor, property)



def test_test_c_is_not_abstract():
    assert not inspect.isabstract(test_C)


def test_test_c_constructor_exists():
    assert callable(test_C.__init__)


def test_test_c_constructor_args():
    sig = inspect.signature(test_C.__init__)
    params = list(sig.parameters.keys())
    assert "newAttribute" in params, "Missing parameter 'newAttribute'"

def test_test_c_has_newAttribute():
    assert hasattr(test_C, "newAttribute")
    descriptor = None
    for klass in test_C.__mro__:
        if "newAttribute" in klass.__dict__:
            descriptor = klass.__dict__["newAttribute"]
            break
    assert isinstance(descriptor, property)



def test_test_b_is_not_abstract():
    assert not inspect.isabstract(test_B)


def test_test_b_constructor_exists():
    assert callable(test_B.__init__)


def test_test_b_constructor_args():
    sig = inspect.signature(test_B.__init__)
    params = list(sig.parameters.keys())
    assert "newAttribute" in params, "Missing parameter 'newAttribute'"

def test_test_b_has_newAttribute():
    assert hasattr(test_B, "newAttribute")
    descriptor = None
    for klass in test_B.__mro__:
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



def test_test_adown_is_not_abstract():
    assert not inspect.isabstract(test_Adown)


def test_test_adown_constructor_exists():
    assert callable(test_Adown.__init__)


def test_test_adown_constructor_args():
    sig = inspect.signature(test_Adown.__init__)
    params = list(sig.parameters.keys())
    assert "newAttribute" in params, "Missing parameter 'newAttribute'"

def test_test_adown_has_newAttribute():
    assert hasattr(test_Adown, "newAttribute")
    descriptor = None
    for klass in test_Adown.__mro__:
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
test_F_strategy = st.builds(
    test_F,
)
test_E_strategy = st.builds(
    test_E,
    newAttribute2=
        safe_text
)
test_D_strategy = st.builds(
    test_D,
    newAttribute=
        safe_text
)
test_C_strategy = st.builds(
    test_C,
    newAttribute=
        safe_text
)
test_B_strategy = st.builds(
    test_B,
    newAttribute=
        safe_text
)
E_strategy = st.builds(
    E,
)
test_Adown_strategy = st.builds(
    test_Adown,
    newAttribute=
        safe_text
)

@given(instance=test_F_strategy)
@settings(max_examples=50)
def test_test_f_instantiation(instance):
    assert isinstance(instance, test_F)

@given(instance=test_E_strategy)
@settings(max_examples=50)
def test_test_e_instantiation(instance):
    assert isinstance(instance, test_E)



@given(instance=test_E_strategy)
def test_test_e_newAttribute2_setter(instance):
    original = instance.newAttribute2
    instance.newAttribute2 = original
    assert instance.newAttribute2 == original

@given(instance=test_D_strategy)
@settings(max_examples=50)
def test_test_d_instantiation(instance):
    assert isinstance(instance, test_D)



@given(instance=test_D_strategy)
def test_test_d_newAttribute_setter(instance):
    original = instance.newAttribute
    instance.newAttribute = original
    assert instance.newAttribute == original

@given(instance=test_C_strategy)
@settings(max_examples=50)
def test_test_c_instantiation(instance):
    assert isinstance(instance, test_C)



@given(instance=test_C_strategy)
def test_test_c_newAttribute_setter(instance):
    original = instance.newAttribute
    instance.newAttribute = original
    assert instance.newAttribute == original

@given(instance=test_B_strategy)
@settings(max_examples=50)
def test_test_b_instantiation(instance):
    assert isinstance(instance, test_B)



@given(instance=test_B_strategy)
def test_test_b_newAttribute_setter(instance):
    original = instance.newAttribute
    instance.newAttribute = original
    assert instance.newAttribute == original

@given(instance=E_strategy)
@settings(max_examples=50)
def test_e_instantiation(instance):
    assert isinstance(instance, E)

@given(instance=test_Adown_strategy)
@settings(max_examples=50)
def test_test_adown_instantiation(instance):
    assert isinstance(instance, test_Adown)



@given(instance=test_Adown_strategy)
def test_test_adown_newAttribute_setter(instance):
    original = instance.newAttribute
    instance.newAttribute = original
    assert instance.newAttribute == original
