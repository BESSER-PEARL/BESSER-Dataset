import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BoemTest_NamedElement,
    NamedElement,
    BoemTest_Node,
    BoemTest_A,
    B,
    BoemTest_C,
    BoemTest_BNode,
    A,
    BoemTest_B,
    AnEnumeration,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_boemtest_namedelement_is_not_abstract():
    assert not inspect.isabstract(BoemTest_NamedElement)


def test_boemtest_namedelement_constructor_exists():
    assert callable(BoemTest_NamedElement.__init__)


def test_boemtest_namedelement_constructor_args():
    sig = inspect.signature(BoemTest_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_boemtest_namedelement_has_name():
    assert hasattr(BoemTest_NamedElement, "name")
    descriptor = None
    for klass in BoemTest_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_boemtest_node_is_not_abstract():
    assert not inspect.isabstract(BoemTest_Node)


def test_boemtest_node_constructor_exists():
    assert callable(BoemTest_Node.__init__)


def test_boemtest_node_constructor_args():
    sig = inspect.signature(BoemTest_Node.__init__)
    params = list(sig.parameters.keys())



def test_boemtest_a_is_not_abstract():
    assert not inspect.isabstract(BoemTest_A)


def test_boemtest_a_constructor_exists():
    assert callable(BoemTest_A.__init__)


def test_boemtest_a_constructor_args():
    sig = inspect.signature(BoemTest_A.__init__)
    params = list(sig.parameters.keys())



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_boemtest_c_is_not_abstract():
    assert not inspect.isabstract(BoemTest_C)


def test_boemtest_c_constructor_exists():
    assert callable(BoemTest_C.__init__)


def test_boemtest_c_constructor_args():
    sig = inspect.signature(BoemTest_C.__init__)
    params = list(sig.parameters.keys())



def test_boemtest_bnode_is_not_abstract():
    assert not inspect.isabstract(BoemTest_BNode)


def test_boemtest_bnode_constructor_exists():
    assert callable(BoemTest_BNode.__init__)


def test_boemtest_bnode_constructor_args():
    sig = inspect.signature(BoemTest_BNode.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_boemtest_b_is_not_abstract():
    assert not inspect.isabstract(BoemTest_B)


def test_boemtest_b_constructor_exists():
    assert callable(BoemTest_B.__init__)


def test_boemtest_b_constructor_args():
    sig = inspect.signature(BoemTest_B.__init__)
    params = list(sig.parameters.keys())
    assert "enumAttr" in params, "Missing parameter 'enumAttr'"

def test_boemtest_b_has_enumAttr():
    assert hasattr(BoemTest_B, "enumAttr")
    descriptor = None
    for klass in BoemTest_B.__mro__:
        if "enumAttr" in klass.__dict__:
            descriptor = klass.__dict__["enumAttr"]
            break
    assert isinstance(descriptor, property)

def test_anenumeration_exists():
    # Check that the Enumeration exists
    assert AnEnumeration is not None

def test_anenumeration_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AnEnumeration]
    expected_literals = [
        "LITERAL1",
        "LITERAL2",
        "LITERAL0",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AnEnumeration"


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
BoemTest_NamedElement_strategy = st.builds(
    BoemTest_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
BoemTest_Node_strategy = st.builds(
    BoemTest_Node,
)
BoemTest_A_strategy = st.builds(
    BoemTest_A,
)
B_strategy = st.builds(
    B,
)
BoemTest_C_strategy = st.builds(
    BoemTest_C,
)
BoemTest_BNode_strategy = st.builds(
    BoemTest_BNode,
)
A_strategy = st.builds(
    A,
)
BoemTest_B_strategy = st.builds(
    BoemTest_B,
    enumAttr=
        safe_text
)

@given(instance=BoemTest_NamedElement_strategy)
@settings(max_examples=50)
def test_boemtest_namedelement_instantiation(instance):
    assert isinstance(instance, BoemTest_NamedElement)



@given(instance=BoemTest_NamedElement_strategy)
def test_boemtest_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=BoemTest_Node_strategy)
@settings(max_examples=50)
def test_boemtest_node_instantiation(instance):
    assert isinstance(instance, BoemTest_Node)

@given(instance=BoemTest_A_strategy)
@settings(max_examples=50)
def test_boemtest_a_instantiation(instance):
    assert isinstance(instance, BoemTest_A)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=BoemTest_C_strategy)
@settings(max_examples=50)
def test_boemtest_c_instantiation(instance):
    assert isinstance(instance, BoemTest_C)

@given(instance=BoemTest_BNode_strategy)
@settings(max_examples=50)
def test_boemtest_bnode_instantiation(instance):
    assert isinstance(instance, BoemTest_BNode)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=BoemTest_B_strategy)
@settings(max_examples=50)
def test_boemtest_b_instantiation(instance):
    assert isinstance(instance, BoemTest_B)



@given(instance=BoemTest_B_strategy)
def test_boemtest_b_enumAttr_setter(instance):
    original = instance.enumAttr
    instance.enumAttr = original
    assert instance.enumAttr == original
