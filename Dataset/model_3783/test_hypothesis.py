import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    test::NamedElement,
    NamedElement,
    test::TestElementWrapper,
    test::TestPolicy,
    test::TestClassDelegate,
    test::TestElement,
    test::Root,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test::namedelement_is_not_abstract():
    assert not inspect.isabstract(test::NamedElement)


def test_test::namedelement_constructor_exists():
    assert callable(test::NamedElement.__init__)


def test_test::namedelement_constructor_args():
    sig = inspect.signature(test::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_test::namedelement_has_Name():
    assert hasattr(test::NamedElement, "Name")
    descriptor = None
    for klass in test::NamedElement.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_test::testelementwrapper_is_not_abstract():
    assert not inspect.isabstract(test::TestElementWrapper)


def test_test::testelementwrapper_constructor_exists():
    assert callable(test::TestElementWrapper.__init__)


def test_test::testelementwrapper_constructor_args():
    sig = inspect.signature(test::TestElementWrapper.__init__)
    params = list(sig.parameters.keys())



def test_test::testpolicy_is_not_abstract():
    assert not inspect.isabstract(test::TestPolicy)


def test_test::testpolicy_constructor_exists():
    assert callable(test::TestPolicy.__init__)


def test_test::testpolicy_constructor_args():
    sig = inspect.signature(test::TestPolicy.__init__)
    params = list(sig.parameters.keys())



def test_test::testclassdelegate_is_not_abstract():
    assert not inspect.isabstract(test::TestClassDelegate)


def test_test::testclassdelegate_constructor_exists():
    assert callable(test::TestClassDelegate.__init__)


def test_test::testclassdelegate_constructor_args():
    sig = inspect.signature(test::TestClassDelegate.__init__)
    params = list(sig.parameters.keys())



def test_test::testelement_is_not_abstract():
    assert not inspect.isabstract(test::TestElement)


def test_test::testelement_constructor_exists():
    assert callable(test::TestElement.__init__)


def test_test::testelement_constructor_args():
    sig = inspect.signature(test::TestElement.__init__)
    params = list(sig.parameters.keys())



def test_test::root_is_not_abstract():
    assert not inspect.isabstract(test::Root)


def test_test::root_constructor_exists():
    assert callable(test::Root.__init__)


def test_test::root_constructor_args():
    sig = inspect.signature(test::Root.__init__)
    params = list(sig.parameters.keys())
    assert "ttt" in params, "Missing parameter 'ttt'"

def test_test::root_has_ttt():
    assert hasattr(test::Root, "ttt")
    descriptor = None
    for klass in test::Root.__mro__:
        if "ttt" in klass.__dict__:
            descriptor = klass.__dict__["ttt"]
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
test::NamedElement_strategy = st.builds(
    test::NamedElement,
    Name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
test::TestElementWrapper_strategy = st.builds(
    test::TestElementWrapper,
)
test::TestPolicy_strategy = st.builds(
    test::TestPolicy,
)
test::TestClassDelegate_strategy = st.builds(
    test::TestClassDelegate,
)
test::TestElement_strategy = st.builds(
    test::TestElement,
)
test::Root_strategy = st.builds(
    test::Root,
    ttt=
        safe_text
)

@given(instance=test::NamedElement_strategy)
@settings(max_examples=50)
def test_test::namedelement_instantiation(instance):
    assert isinstance(instance, test::NamedElement)

@given(instance=test::NamedElement_strategy)
def test_test::namedelement_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=test::NamedElement_strategy)
def test_test::namedelement_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=test::TestElementWrapper_strategy)
@settings(max_examples=50)
def test_test::testelementwrapper_instantiation(instance):
    assert isinstance(instance, test::TestElementWrapper)

@given(instance=test::TestPolicy_strategy)
@settings(max_examples=50)
def test_test::testpolicy_instantiation(instance):
    assert isinstance(instance, test::TestPolicy)

@given(instance=test::TestClassDelegate_strategy)
@settings(max_examples=50)
def test_test::testclassdelegate_instantiation(instance):
    assert isinstance(instance, test::TestClassDelegate)

@given(instance=test::TestElement_strategy)
@settings(max_examples=50)
def test_test::testelement_instantiation(instance):
    assert isinstance(instance, test::TestElement)

@given(instance=test::Root_strategy)
@settings(max_examples=50)
def test_test::root_instantiation(instance):
    assert isinstance(instance, test::Root)

@given(instance=test::Root_strategy)
def test_test::root_ttt_type(instance):
    assert isinstance(instance.ttt, str)


@given(instance=test::Root_strategy)
def test_test::root_ttt_setter(instance):
    original = instance.ttt
    instance.ttt = original
    assert instance.ttt == original
