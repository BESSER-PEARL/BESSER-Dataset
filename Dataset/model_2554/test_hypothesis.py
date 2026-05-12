import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    testmodel_Val,
    testmodel_Node,
    testmodel_cont,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testmodel_val_is_not_abstract():
    assert not inspect.isabstract(testmodel_Val)


def test_testmodel_val_constructor_exists():
    assert callable(testmodel_Val.__init__)


def test_testmodel_val_constructor_args():
    sig = inspect.signature(testmodel_Val.__init__)
    params = list(sig.parameters.keys())
    assert "valname" in params, "Missing parameter 'valname'"
    assert "intlist" in params, "Missing parameter 'intlist'"
    assert "intvl" in params, "Missing parameter 'intvl'"

def test_testmodel_val_has_valname():
    assert hasattr(testmodel_Val, "valname")
    descriptor = None
    for klass in testmodel_Val.__mro__:
        if "valname" in klass.__dict__:
            descriptor = klass.__dict__["valname"]
            break
    assert isinstance(descriptor, property)

def test_testmodel_val_has_intlist():
    assert hasattr(testmodel_Val, "intlist")
    descriptor = None
    for klass in testmodel_Val.__mro__:
        if "intlist" in klass.__dict__:
            descriptor = klass.__dict__["intlist"]
            break
    assert isinstance(descriptor, property)

def test_testmodel_val_has_intvl():
    assert hasattr(testmodel_Val, "intvl")
    descriptor = None
    for klass in testmodel_Val.__mro__:
        if "intvl" in klass.__dict__:
            descriptor = klass.__dict__["intvl"]
            break
    assert isinstance(descriptor, property)



def test_testmodel_node_is_not_abstract():
    assert not inspect.isabstract(testmodel_Node)


def test_testmodel_node_constructor_exists():
    assert callable(testmodel_Node.__init__)


def test_testmodel_node_constructor_args():
    sig = inspect.signature(testmodel_Node.__init__)
    params = list(sig.parameters.keys())
    assert "nodename" in params, "Missing parameter 'nodename'"

def test_testmodel_node_has_nodename():
    assert hasattr(testmodel_Node, "nodename")
    descriptor = None
    for klass in testmodel_Node.__mro__:
        if "nodename" in klass.__dict__:
            descriptor = klass.__dict__["nodename"]
            break
    assert isinstance(descriptor, property)



def test_testmodel_cont_is_not_abstract():
    assert not inspect.isabstract(testmodel_cont)


def test_testmodel_cont_constructor_exists():
    assert callable(testmodel_cont.__init__)


def test_testmodel_cont_constructor_args():
    sig = inspect.signature(testmodel_cont.__init__)
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
testmodel_Val_strategy = st.builds(
    testmodel_Val,
    valname=
        safe_text,
    intlist=
        st.integers(),
    intvl=
        st.integers()
)
testmodel_Node_strategy = st.builds(
    testmodel_Node,
    nodename=
        safe_text
)
testmodel_cont_strategy = st.builds(
    testmodel_cont,
)

@given(instance=testmodel_Val_strategy)
@settings(max_examples=50)
def test_testmodel_val_instantiation(instance):
    assert isinstance(instance, testmodel_Val)



@given(instance=testmodel_Val_strategy)
def test_testmodel_val_valname_setter(instance):
    original = instance.valname
    instance.valname = original
    assert instance.valname == original



@given(instance=testmodel_Val_strategy)
def test_testmodel_val_intlist_setter(instance):
    original = instance.intlist
    instance.intlist = original
    assert instance.intlist == original



@given(instance=testmodel_Val_strategy)
def test_testmodel_val_intvl_setter(instance):
    original = instance.intvl
    instance.intvl = original
    assert instance.intvl == original

@given(instance=testmodel_Node_strategy)
@settings(max_examples=50)
def test_testmodel_node_instantiation(instance):
    assert isinstance(instance, testmodel_Node)



@given(instance=testmodel_Node_strategy)
def test_testmodel_node_nodename_setter(instance):
    original = instance.nodename
    instance.nodename = original
    assert instance.nodename == original

@given(instance=testmodel_cont_strategy)
@settings(max_examples=50)
def test_testmodel_cont_instantiation(instance):
    assert isinstance(instance, testmodel_cont)
