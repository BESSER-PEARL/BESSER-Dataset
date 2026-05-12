import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SuperA,
    testmerge_A,
    B,
    testmerge_SubB,
    testmerge_SuperA,
    AA,
    testmerge_AAA,
    A,
    testmerge_AA,
    testmerge_C,
    testmerge_B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_supera_is_not_abstract():
    assert not inspect.isabstract(SuperA)


def test_supera_constructor_exists():
    assert callable(SuperA.__init__)


def test_supera_constructor_args():
    sig = inspect.signature(SuperA.__init__)
    params = list(sig.parameters.keys())



def test_testmerge_a_is_not_abstract():
    assert not inspect.isabstract(testmerge_A)


def test_testmerge_a_constructor_exists():
    assert callable(testmerge_A.__init__)


def test_testmerge_a_constructor_args():
    sig = inspect.signature(testmerge_A.__init__)
    params = list(sig.parameters.keys())



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_testmerge_subb_is_not_abstract():
    assert not inspect.isabstract(testmerge_SubB)


def test_testmerge_subb_constructor_exists():
    assert callable(testmerge_SubB.__init__)


def test_testmerge_subb_constructor_args():
    sig = inspect.signature(testmerge_SubB.__init__)
    params = list(sig.parameters.keys())



def test_testmerge_supera_is_not_abstract():
    assert not inspect.isabstract(testmerge_SuperA)


def test_testmerge_supera_constructor_exists():
    assert callable(testmerge_SuperA.__init__)


def test_testmerge_supera_constructor_args():
    sig = inspect.signature(testmerge_SuperA.__init__)
    params = list(sig.parameters.keys())



def test_aa_is_not_abstract():
    assert not inspect.isabstract(AA)


def test_aa_constructor_exists():
    assert callable(AA.__init__)


def test_aa_constructor_args():
    sig = inspect.signature(AA.__init__)
    params = list(sig.parameters.keys())



def test_testmerge_aaa_is_not_abstract():
    assert not inspect.isabstract(testmerge_AAA)


def test_testmerge_aaa_constructor_exists():
    assert callable(testmerge_AAA.__init__)


def test_testmerge_aaa_constructor_args():
    sig = inspect.signature(testmerge_AAA.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_testmerge_aa_is_not_abstract():
    assert not inspect.isabstract(testmerge_AA)


def test_testmerge_aa_constructor_exists():
    assert callable(testmerge_AA.__init__)


def test_testmerge_aa_constructor_args():
    sig = inspect.signature(testmerge_AA.__init__)
    params = list(sig.parameters.keys())



def test_testmerge_c_is_not_abstract():
    assert not inspect.isabstract(testmerge_C)


def test_testmerge_c_constructor_exists():
    assert callable(testmerge_C.__init__)


def test_testmerge_c_constructor_args():
    sig = inspect.signature(testmerge_C.__init__)
    params = list(sig.parameters.keys())



def test_testmerge_b_is_not_abstract():
    assert not inspect.isabstract(testmerge_B)


def test_testmerge_b_constructor_exists():
    assert callable(testmerge_B.__init__)


def test_testmerge_b_constructor_args():
    sig = inspect.signature(testmerge_B.__init__)
    params = list(sig.parameters.keys())
    assert "anAttribute" in params, "Missing parameter 'anAttribute'"

def test_testmerge_b_has_anAttribute():
    assert hasattr(testmerge_B, "anAttribute")
    descriptor = None
    for klass in testmerge_B.__mro__:
        if "anAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anAttribute"]
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
SuperA_strategy = st.builds(
    SuperA,
)
testmerge_A_strategy = st.builds(
    testmerge_A,
)
B_strategy = st.builds(
    B,
)
testmerge_SubB_strategy = st.builds(
    testmerge_SubB,
)
testmerge_SuperA_strategy = st.builds(
    testmerge_SuperA,
)
AA_strategy = st.builds(
    AA,
)
testmerge_AAA_strategy = st.builds(
    testmerge_AAA,
)
A_strategy = st.builds(
    A,
)
testmerge_AA_strategy = st.builds(
    testmerge_AA,
)
testmerge_C_strategy = st.builds(
    testmerge_C,
)
testmerge_B_strategy = st.builds(
    testmerge_B,
    anAttribute=
        safe_text
)

@given(instance=SuperA_strategy)
@settings(max_examples=50)
def test_supera_instantiation(instance):
    assert isinstance(instance, SuperA)

@given(instance=testmerge_A_strategy)
@settings(max_examples=50)
def test_testmerge_a_instantiation(instance):
    assert isinstance(instance, testmerge_A)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=testmerge_SubB_strategy)
@settings(max_examples=50)
def test_testmerge_subb_instantiation(instance):
    assert isinstance(instance, testmerge_SubB)

@given(instance=testmerge_SuperA_strategy)
@settings(max_examples=50)
def test_testmerge_supera_instantiation(instance):
    assert isinstance(instance, testmerge_SuperA)

@given(instance=AA_strategy)
@settings(max_examples=50)
def test_aa_instantiation(instance):
    assert isinstance(instance, AA)

@given(instance=testmerge_AAA_strategy)
@settings(max_examples=50)
def test_testmerge_aaa_instantiation(instance):
    assert isinstance(instance, testmerge_AAA)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=testmerge_AA_strategy)
@settings(max_examples=50)
def test_testmerge_aa_instantiation(instance):
    assert isinstance(instance, testmerge_AA)

@given(instance=testmerge_C_strategy)
@settings(max_examples=50)
def test_testmerge_c_instantiation(instance):
    assert isinstance(instance, testmerge_C)

@given(instance=testmerge_B_strategy)
@settings(max_examples=50)
def test_testmerge_b_instantiation(instance):
    assert isinstance(instance, testmerge_B)



@given(instance=testmerge_B_strategy)
def test_testmerge_b_anAttribute_setter(instance):
    original = instance.anAttribute
    instance.anAttribute = original
    assert instance.anAttribute == original
