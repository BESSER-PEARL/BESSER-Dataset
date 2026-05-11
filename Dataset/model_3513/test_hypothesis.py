import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Parent,
    testoperationbody::ChildB,
    testoperationbody::ChildA,
    testoperationbody::Main,
    testoperationbody::Parent,
    testoperationbody::ConceptA,
    EnumA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_parent_is_not_abstract():
    assert not inspect.isabstract(Parent)


def test_parent_constructor_exists():
    assert callable(Parent.__init__)


def test_parent_constructor_args():
    sig = inspect.signature(Parent.__init__)
    params = list(sig.parameters.keys())



def test_testoperationbody::childb_is_not_abstract():
    assert not inspect.isabstract(testoperationbody::ChildB)


def test_testoperationbody::childb_constructor_exists():
    assert callable(testoperationbody::ChildB.__init__)


def test_testoperationbody::childb_constructor_args():
    sig = inspect.signature(testoperationbody::ChildB.__init__)
    params = list(sig.parameters.keys())



def test_testoperationbody::childa_is_not_abstract():
    assert not inspect.isabstract(testoperationbody::ChildA)


def test_testoperationbody::childa_constructor_exists():
    assert callable(testoperationbody::ChildA.__init__)


def test_testoperationbody::childa_constructor_args():
    sig = inspect.signature(testoperationbody::ChildA.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_testoperationbody::childa_has_value():
    assert hasattr(testoperationbody::ChildA, "value")
    descriptor = None
    for klass in testoperationbody::ChildA.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_testoperationbody::main_is_not_abstract():
    assert not inspect.isabstract(testoperationbody::Main)


def test_testoperationbody::main_constructor_exists():
    assert callable(testoperationbody::Main.__init__)


def test_testoperationbody::main_constructor_args():
    sig = inspect.signature(testoperationbody::Main.__init__)
    params = list(sig.parameters.keys())
    assert "listint" in params, "Missing parameter 'listint'"
    assert "singlebool" in params, "Missing parameter 'singlebool'"

def test_testoperationbody::main_has_listint():
    assert hasattr(testoperationbody::Main, "listint")
    descriptor = None
    for klass in testoperationbody::Main.__mro__:
        if "listint" in klass.__dict__:
            descriptor = klass.__dict__["listint"]
            break
    assert isinstance(descriptor, property)

def test_testoperationbody::main_has_singlebool():
    assert hasattr(testoperationbody::Main, "singlebool")
    descriptor = None
    for klass in testoperationbody::Main.__mro__:
        if "singlebool" in klass.__dict__:
            descriptor = klass.__dict__["singlebool"]
            break
    assert isinstance(descriptor, property)



def test_testoperationbody::parent_is_not_abstract():
    assert not inspect.isabstract(testoperationbody::Parent)


def test_testoperationbody::parent_constructor_exists():
    assert callable(testoperationbody::Parent.__init__)


def test_testoperationbody::parent_constructor_args():
    sig = inspect.signature(testoperationbody::Parent.__init__)
    params = list(sig.parameters.keys())



def test_testoperationbody::concepta_is_not_abstract():
    assert not inspect.isabstract(testoperationbody::ConceptA)


def test_testoperationbody::concepta_constructor_exists():
    assert callable(testoperationbody::ConceptA.__init__)


def test_testoperationbody::concepta_constructor_args():
    sig = inspect.signature(testoperationbody::ConceptA.__init__)
    params = list(sig.parameters.keys())

def test_enuma_exists():
    # Check that the Enumeration exists
    assert EnumA is not None

def test_enuma_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EnumA]
    expected_literals = [
        "CASE1",
        "CASE2",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EnumA"


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
Parent_strategy = st.builds(
    Parent,
)
testoperationbody::ChildB_strategy = st.builds(
    testoperationbody::ChildB,
)
testoperationbody::ChildA_strategy = st.builds(
    testoperationbody::ChildA,
    value=
        safe_text
)
testoperationbody::Main_strategy = st.builds(
    testoperationbody::Main,
    listint=
        st.integers(),
    singlebool=
        st.booleans()
)
testoperationbody::Parent_strategy = st.builds(
    testoperationbody::Parent,
)
testoperationbody::ConceptA_strategy = st.builds(
    testoperationbody::ConceptA,
)

@given(instance=Parent_strategy)
@settings(max_examples=50)
def test_parent_instantiation(instance):
    assert isinstance(instance, Parent)

@given(instance=testoperationbody::ChildB_strategy)
@settings(max_examples=50)
def test_testoperationbody::childb_instantiation(instance):
    assert isinstance(instance, testoperationbody::ChildB)

@given(instance=testoperationbody::ChildA_strategy)
@settings(max_examples=50)
def test_testoperationbody::childa_instantiation(instance):
    assert isinstance(instance, testoperationbody::ChildA)

@given(instance=testoperationbody::ChildA_strategy)
def test_testoperationbody::childa_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=testoperationbody::ChildA_strategy)
def test_testoperationbody::childa_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=testoperationbody::Main_strategy)
@settings(max_examples=50)
def test_testoperationbody::main_instantiation(instance):
    assert isinstance(instance, testoperationbody::Main)

@given(instance=testoperationbody::Main_strategy)
def test_testoperationbody::main_listint_type(instance):
    assert isinstance(instance.listint, int)


@given(instance=testoperationbody::Main_strategy)
def test_testoperationbody::main_listint_setter(instance):
    original = instance.listint
    instance.listint = original
    assert instance.listint == original

@given(instance=testoperationbody::Main_strategy)
def test_testoperationbody::main_singlebool_type(instance):
    assert isinstance(instance.singlebool, bool)


@given(instance=testoperationbody::Main_strategy)
def test_testoperationbody::main_singlebool_setter(instance):
    original = instance.singlebool
    instance.singlebool = original
    assert instance.singlebool == original

@given(instance=testoperationbody::Parent_strategy)
@settings(max_examples=50)
def test_testoperationbody::parent_instantiation(instance):
    assert isinstance(instance, testoperationbody::Parent)

@given(instance=testoperationbody::ConceptA_strategy)
@settings(max_examples=50)
def test_testoperationbody::concepta_instantiation(instance):
    assert isinstance(instance, testoperationbody::ConceptA)
