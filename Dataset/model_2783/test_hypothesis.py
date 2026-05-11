import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BoemTest::NamedElement,
    NamedElement,
    BoemTest::Node,
    BoemTest::A,
    B,
    BoemTest::C,
    BoemTest::BNode,
    A,
    BoemTest::B,
    AnEnumeration,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_boemtest::namedelement_is_not_abstract():
    assert not inspect.isabstract(BoemTest::NamedElement)


def test_boemtest::namedelement_constructor_exists():
    assert callable(BoemTest::NamedElement.__init__)


def test_boemtest::namedelement_constructor_args():
    sig = inspect.signature(BoemTest::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_boemtest::namedelement_has_name():
    assert hasattr(BoemTest::NamedElement, "name")
    descriptor = None
    for klass in BoemTest::NamedElement.__mro__:
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



def test_boemtest::node_is_not_abstract():
    assert not inspect.isabstract(BoemTest::Node)


def test_boemtest::node_constructor_exists():
    assert callable(BoemTest::Node.__init__)


def test_boemtest::node_constructor_args():
    sig = inspect.signature(BoemTest::Node.__init__)
    params = list(sig.parameters.keys())



def test_boemtest::a_is_not_abstract():
    assert not inspect.isabstract(BoemTest::A)


def test_boemtest::a_constructor_exists():
    assert callable(BoemTest::A.__init__)


def test_boemtest::a_constructor_args():
    sig = inspect.signature(BoemTest::A.__init__)
    params = list(sig.parameters.keys())



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_boemtest::c_is_not_abstract():
    assert not inspect.isabstract(BoemTest::C)


def test_boemtest::c_constructor_exists():
    assert callable(BoemTest::C.__init__)


def test_boemtest::c_constructor_args():
    sig = inspect.signature(BoemTest::C.__init__)
    params = list(sig.parameters.keys())



def test_boemtest::bnode_is_not_abstract():
    assert not inspect.isabstract(BoemTest::BNode)


def test_boemtest::bnode_constructor_exists():
    assert callable(BoemTest::BNode.__init__)


def test_boemtest::bnode_constructor_args():
    sig = inspect.signature(BoemTest::BNode.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_boemtest::b_is_not_abstract():
    assert not inspect.isabstract(BoemTest::B)


def test_boemtest::b_constructor_exists():
    assert callable(BoemTest::B.__init__)


def test_boemtest::b_constructor_args():
    sig = inspect.signature(BoemTest::B.__init__)
    params = list(sig.parameters.keys())
    assert "enumAttr" in params, "Missing parameter 'enumAttr'"

def test_boemtest::b_has_enumAttr():
    assert hasattr(BoemTest::B, "enumAttr")
    descriptor = None
    for klass in BoemTest::B.__mro__:
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
        "LITERAL2",
        "LITERAL1",
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
BoemTest::NamedElement_strategy = st.builds(
    BoemTest::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
BoemTest::Node_strategy = st.builds(
    BoemTest::Node,
)
BoemTest::A_strategy = st.builds(
    BoemTest::A,
)
B_strategy = st.builds(
    B,
)
BoemTest::C_strategy = st.builds(
    BoemTest::C,
)
BoemTest::BNode_strategy = st.builds(
    BoemTest::BNode,
)
A_strategy = st.builds(
    A,
)
BoemTest::B_strategy = st.builds(
    BoemTest::B,
    enumAttr=
        safe_text
)

@given(instance=BoemTest::NamedElement_strategy)
@settings(max_examples=50)
def test_boemtest::namedelement_instantiation(instance):
    assert isinstance(instance, BoemTest::NamedElement)

@given(instance=BoemTest::NamedElement_strategy)
def test_boemtest::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=BoemTest::NamedElement_strategy)
def test_boemtest::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=BoemTest::Node_strategy)
@settings(max_examples=50)
def test_boemtest::node_instantiation(instance):
    assert isinstance(instance, BoemTest::Node)

@given(instance=BoemTest::A_strategy)
@settings(max_examples=50)
def test_boemtest::a_instantiation(instance):
    assert isinstance(instance, BoemTest::A)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=BoemTest::C_strategy)
@settings(max_examples=50)
def test_boemtest::c_instantiation(instance):
    assert isinstance(instance, BoemTest::C)

@given(instance=BoemTest::BNode_strategy)
@settings(max_examples=50)
def test_boemtest::bnode_instantiation(instance):
    assert isinstance(instance, BoemTest::BNode)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=BoemTest::B_strategy)
@settings(max_examples=50)
def test_boemtest::b_instantiation(instance):
    assert isinstance(instance, BoemTest::B)

@given(instance=BoemTest::B_strategy)
def test_boemtest::b_enumAttr_type(instance):
    assert isinstance(instance.enumAttr, str)


@given(instance=BoemTest::B_strategy)
def test_boemtest::b_enumAttr_setter(instance):
    original = instance.enumAttr
    instance.enumAttr = original
    assert instance.enumAttr == original
