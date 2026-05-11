import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SuperA,
    testmerge::A,
    B,
    testmerge::SubB,
    testmerge::SuperA,
    AA,
    testmerge::AAA,
    A,
    testmerge::AA,
    testmerge::C,
    testmerge::B,
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



def test_testmerge::a_is_not_abstract():
    assert not inspect.isabstract(testmerge::A)


def test_testmerge::a_constructor_exists():
    assert callable(testmerge::A.__init__)


def test_testmerge::a_constructor_args():
    sig = inspect.signature(testmerge::A.__init__)
    params = list(sig.parameters.keys())



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_testmerge::subb_is_not_abstract():
    assert not inspect.isabstract(testmerge::SubB)


def test_testmerge::subb_constructor_exists():
    assert callable(testmerge::SubB.__init__)


def test_testmerge::subb_constructor_args():
    sig = inspect.signature(testmerge::SubB.__init__)
    params = list(sig.parameters.keys())



def test_testmerge::supera_is_not_abstract():
    assert not inspect.isabstract(testmerge::SuperA)


def test_testmerge::supera_constructor_exists():
    assert callable(testmerge::SuperA.__init__)


def test_testmerge::supera_constructor_args():
    sig = inspect.signature(testmerge::SuperA.__init__)
    params = list(sig.parameters.keys())



def test_aa_is_not_abstract():
    assert not inspect.isabstract(AA)


def test_aa_constructor_exists():
    assert callable(AA.__init__)


def test_aa_constructor_args():
    sig = inspect.signature(AA.__init__)
    params = list(sig.parameters.keys())



def test_testmerge::aaa_is_not_abstract():
    assert not inspect.isabstract(testmerge::AAA)


def test_testmerge::aaa_constructor_exists():
    assert callable(testmerge::AAA.__init__)


def test_testmerge::aaa_constructor_args():
    sig = inspect.signature(testmerge::AAA.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_testmerge::aa_is_not_abstract():
    assert not inspect.isabstract(testmerge::AA)


def test_testmerge::aa_constructor_exists():
    assert callable(testmerge::AA.__init__)


def test_testmerge::aa_constructor_args():
    sig = inspect.signature(testmerge::AA.__init__)
    params = list(sig.parameters.keys())



def test_testmerge::c_is_not_abstract():
    assert not inspect.isabstract(testmerge::C)


def test_testmerge::c_constructor_exists():
    assert callable(testmerge::C.__init__)


def test_testmerge::c_constructor_args():
    sig = inspect.signature(testmerge::C.__init__)
    params = list(sig.parameters.keys())



def test_testmerge::b_is_not_abstract():
    assert not inspect.isabstract(testmerge::B)


def test_testmerge::b_constructor_exists():
    assert callable(testmerge::B.__init__)


def test_testmerge::b_constructor_args():
    sig = inspect.signature(testmerge::B.__init__)
    params = list(sig.parameters.keys())
    assert "anAttribute" in params, "Missing parameter 'anAttribute'"

def test_testmerge::b_has_anAttribute():
    assert hasattr(testmerge::B, "anAttribute")
    descriptor = None
    for klass in testmerge::B.__mro__:
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
testmerge::A_strategy = st.builds(
    testmerge::A,
)
B_strategy = st.builds(
    B,
)
testmerge::SubB_strategy = st.builds(
    testmerge::SubB,
)
testmerge::SuperA_strategy = st.builds(
    testmerge::SuperA,
)
AA_strategy = st.builds(
    AA,
)
testmerge::AAA_strategy = st.builds(
    testmerge::AAA,
)
A_strategy = st.builds(
    A,
)
testmerge::AA_strategy = st.builds(
    testmerge::AA,
)
testmerge::C_strategy = st.builds(
    testmerge::C,
)
testmerge::B_strategy = st.builds(
    testmerge::B,
    anAttribute=
        safe_text
)

@given(instance=SuperA_strategy)
@settings(max_examples=50)
def test_supera_instantiation(instance):
    assert isinstance(instance, SuperA)

@given(instance=testmerge::A_strategy)
@settings(max_examples=50)
def test_testmerge::a_instantiation(instance):
    assert isinstance(instance, testmerge::A)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=testmerge::SubB_strategy)
@settings(max_examples=50)
def test_testmerge::subb_instantiation(instance):
    assert isinstance(instance, testmerge::SubB)

@given(instance=testmerge::SuperA_strategy)
@settings(max_examples=50)
def test_testmerge::supera_instantiation(instance):
    assert isinstance(instance, testmerge::SuperA)

@given(instance=AA_strategy)
@settings(max_examples=50)
def test_aa_instantiation(instance):
    assert isinstance(instance, AA)

@given(instance=testmerge::AAA_strategy)
@settings(max_examples=50)
def test_testmerge::aaa_instantiation(instance):
    assert isinstance(instance, testmerge::AAA)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=testmerge::AA_strategy)
@settings(max_examples=50)
def test_testmerge::aa_instantiation(instance):
    assert isinstance(instance, testmerge::AA)

@given(instance=testmerge::C_strategy)
@settings(max_examples=50)
def test_testmerge::c_instantiation(instance):
    assert isinstance(instance, testmerge::C)

@given(instance=testmerge::B_strategy)
@settings(max_examples=50)
def test_testmerge::b_instantiation(instance):
    assert isinstance(instance, testmerge::B)

@given(instance=testmerge::B_strategy)
def test_testmerge::b_anAttribute_type(instance):
    assert isinstance(instance.anAttribute, str)


@given(instance=testmerge::B_strategy)
def test_testmerge::b_anAttribute_setter(instance):
    original = instance.anAttribute
    instance.anAttribute = original
    assert instance.anAttribute == original
