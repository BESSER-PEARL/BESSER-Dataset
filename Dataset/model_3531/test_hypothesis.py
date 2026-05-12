import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    testoperationbody_Parent,
    Parent,
    testoperationbody_ChildB,
    testoperationbody_ChildA,
    testoperationbody_ConceptA,
    testoperationbody_Main,
    EnumA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testoperationbody_parent_is_not_abstract():
    assert not inspect.isabstract(testoperationbody_Parent)


def test_testoperationbody_parent_constructor_exists():
    assert callable(testoperationbody_Parent.__init__)


def test_testoperationbody_parent_constructor_args():
    sig = inspect.signature(testoperationbody_Parent.__init__)
    params = list(sig.parameters.keys())



def test_parent_is_not_abstract():
    assert not inspect.isabstract(Parent)


def test_parent_constructor_exists():
    assert callable(Parent.__init__)


def test_parent_constructor_args():
    sig = inspect.signature(Parent.__init__)
    params = list(sig.parameters.keys())



def test_testoperationbody_childb_is_not_abstract():
    assert not inspect.isabstract(testoperationbody_ChildB)


def test_testoperationbody_childb_constructor_exists():
    assert callable(testoperationbody_ChildB.__init__)


def test_testoperationbody_childb_constructor_args():
    sig = inspect.signature(testoperationbody_ChildB.__init__)
    params = list(sig.parameters.keys())



def test_testoperationbody_childa_is_not_abstract():
    assert not inspect.isabstract(testoperationbody_ChildA)


def test_testoperationbody_childa_constructor_exists():
    assert callable(testoperationbody_ChildA.__init__)


def test_testoperationbody_childa_constructor_args():
    sig = inspect.signature(testoperationbody_ChildA.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_testoperationbody_childa_has_value():
    assert hasattr(testoperationbody_ChildA, "value")
    descriptor = None
    for klass in testoperationbody_ChildA.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_testoperationbody_concepta_is_not_abstract():
    assert not inspect.isabstract(testoperationbody_ConceptA)


def test_testoperationbody_concepta_constructor_exists():
    assert callable(testoperationbody_ConceptA.__init__)


def test_testoperationbody_concepta_constructor_args():
    sig = inspect.signature(testoperationbody_ConceptA.__init__)
    params = list(sig.parameters.keys())



def test_testoperationbody_main_is_not_abstract():
    assert not inspect.isabstract(testoperationbody_Main)


def test_testoperationbody_main_constructor_exists():
    assert callable(testoperationbody_Main.__init__)


def test_testoperationbody_main_constructor_args():
    sig = inspect.signature(testoperationbody_Main.__init__)
    params = list(sig.parameters.keys())
    assert "listint" in params, "Missing parameter 'listint'"
    assert "singlebool" in params, "Missing parameter 'singlebool'"

def test_testoperationbody_main_has_listint():
    assert hasattr(testoperationbody_Main, "listint")
    descriptor = None
    for klass in testoperationbody_Main.__mro__:
        if "listint" in klass.__dict__:
            descriptor = klass.__dict__["listint"]
            break
    assert isinstance(descriptor, property)

def test_testoperationbody_main_has_singlebool():
    assert hasattr(testoperationbody_Main, "singlebool")
    descriptor = None
    for klass in testoperationbody_Main.__mro__:
        if "singlebool" in klass.__dict__:
            descriptor = klass.__dict__["singlebool"]
            break
    assert isinstance(descriptor, property)

def test_enuma_exists():
    # Check that the Enumeration exists
    assert EnumA is not None

def test_enuma_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EnumA]
    expected_literals = [
        "CASE2",
        "CASE1",
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
testoperationbody_Parent_strategy = st.builds(
    testoperationbody_Parent,
)
Parent_strategy = st.builds(
    Parent,
)
testoperationbody_ChildB_strategy = st.builds(
    testoperationbody_ChildB,
)
testoperationbody_ChildA_strategy = st.builds(
    testoperationbody_ChildA,
    value=
        safe_text
)
testoperationbody_ConceptA_strategy = st.builds(
    testoperationbody_ConceptA,
)
testoperationbody_Main_strategy = st.builds(
    testoperationbody_Main,
    listint=
        st.integers(),
    singlebool=
        st.booleans()
)

@given(instance=testoperationbody_Parent_strategy)
@settings(max_examples=50)
def test_testoperationbody_parent_instantiation(instance):
    assert isinstance(instance, testoperationbody_Parent)

@given(instance=Parent_strategy)
@settings(max_examples=50)
def test_parent_instantiation(instance):
    assert isinstance(instance, Parent)

@given(instance=testoperationbody_ChildB_strategy)
@settings(max_examples=50)
def test_testoperationbody_childb_instantiation(instance):
    assert isinstance(instance, testoperationbody_ChildB)

@given(instance=testoperationbody_ChildA_strategy)
@settings(max_examples=50)
def test_testoperationbody_childa_instantiation(instance):
    assert isinstance(instance, testoperationbody_ChildA)



@given(instance=testoperationbody_ChildA_strategy)
def test_testoperationbody_childa_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=testoperationbody_ConceptA_strategy)
@settings(max_examples=50)
def test_testoperationbody_concepta_instantiation(instance):
    assert isinstance(instance, testoperationbody_ConceptA)

@given(instance=testoperationbody_Main_strategy)
@settings(max_examples=50)
def test_testoperationbody_main_instantiation(instance):
    assert isinstance(instance, testoperationbody_Main)



@given(instance=testoperationbody_Main_strategy)
def test_testoperationbody_main_listint_setter(instance):
    original = instance.listint
    instance.listint = original
    assert instance.listint == original



@given(instance=testoperationbody_Main_strategy)
def test_testoperationbody_main_singlebool_setter(instance):
    original = instance.singlebool
    instance.singlebool = original
    assert instance.singlebool == original
