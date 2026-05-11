import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    testmodel::Val,
    testmodel::Node,
    testmodel::cont,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testmodel::val_is_not_abstract():
    assert not inspect.isabstract(testmodel::Val)


def test_testmodel::val_constructor_exists():
    assert callable(testmodel::Val.__init__)


def test_testmodel::val_constructor_args():
    sig = inspect.signature(testmodel::Val.__init__)
    params = list(sig.parameters.keys())
    assert "intvl" in params, "Missing parameter 'intvl'"
    assert "valname" in params, "Missing parameter 'valname'"
    assert "intlist" in params, "Missing parameter 'intlist'"

def test_testmodel::val_has_intvl():
    assert hasattr(testmodel::Val, "intvl")
    descriptor = None
    for klass in testmodel::Val.__mro__:
        if "intvl" in klass.__dict__:
            descriptor = klass.__dict__["intvl"]
            break
    assert isinstance(descriptor, property)

def test_testmodel::val_has_valname():
    assert hasattr(testmodel::Val, "valname")
    descriptor = None
    for klass in testmodel::Val.__mro__:
        if "valname" in klass.__dict__:
            descriptor = klass.__dict__["valname"]
            break
    assert isinstance(descriptor, property)

def test_testmodel::val_has_intlist():
    assert hasattr(testmodel::Val, "intlist")
    descriptor = None
    for klass in testmodel::Val.__mro__:
        if "intlist" in klass.__dict__:
            descriptor = klass.__dict__["intlist"]
            break
    assert isinstance(descriptor, property)



def test_testmodel::node_is_not_abstract():
    assert not inspect.isabstract(testmodel::Node)


def test_testmodel::node_constructor_exists():
    assert callable(testmodel::Node.__init__)


def test_testmodel::node_constructor_args():
    sig = inspect.signature(testmodel::Node.__init__)
    params = list(sig.parameters.keys())
    assert "nodename" in params, "Missing parameter 'nodename'"

def test_testmodel::node_has_nodename():
    assert hasattr(testmodel::Node, "nodename")
    descriptor = None
    for klass in testmodel::Node.__mro__:
        if "nodename" in klass.__dict__:
            descriptor = klass.__dict__["nodename"]
            break
    assert isinstance(descriptor, property)



def test_testmodel::cont_is_not_abstract():
    assert not inspect.isabstract(testmodel::cont)


def test_testmodel::cont_constructor_exists():
    assert callable(testmodel::cont.__init__)


def test_testmodel::cont_constructor_args():
    sig = inspect.signature(testmodel::cont.__init__)
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
testmodel::Val_strategy = st.builds(
    testmodel::Val,
    intvl=
        st.integers(),
    valname=
        safe_text,
    intlist=
        st.integers()
)
testmodel::Node_strategy = st.builds(
    testmodel::Node,
    nodename=
        safe_text
)
testmodel::cont_strategy = st.builds(
    testmodel::cont,
)

@given(instance=testmodel::Val_strategy)
@settings(max_examples=50)
def test_testmodel::val_instantiation(instance):
    assert isinstance(instance, testmodel::Val)

@given(instance=testmodel::Val_strategy)
def test_testmodel::val_intvl_type(instance):
    assert isinstance(instance.intvl, int)


@given(instance=testmodel::Val_strategy)
def test_testmodel::val_intvl_setter(instance):
    original = instance.intvl
    instance.intvl = original
    assert instance.intvl == original

@given(instance=testmodel::Val_strategy)
def test_testmodel::val_valname_type(instance):
    assert isinstance(instance.valname, str)


@given(instance=testmodel::Val_strategy)
def test_testmodel::val_valname_setter(instance):
    original = instance.valname
    instance.valname = original
    assert instance.valname == original

@given(instance=testmodel::Val_strategy)
def test_testmodel::val_intlist_type(instance):
    assert isinstance(instance.intlist, int)


@given(instance=testmodel::Val_strategy)
def test_testmodel::val_intlist_setter(instance):
    original = instance.intlist
    instance.intlist = original
    assert instance.intlist == original

@given(instance=testmodel::Node_strategy)
@settings(max_examples=50)
def test_testmodel::node_instantiation(instance):
    assert isinstance(instance, testmodel::Node)

@given(instance=testmodel::Node_strategy)
def test_testmodel::node_nodename_type(instance):
    assert isinstance(instance.nodename, str)


@given(instance=testmodel::Node_strategy)
def test_testmodel::node_nodename_setter(instance):
    original = instance.nodename
    instance.nodename = original
    assert instance.nodename == original

@given(instance=testmodel::cont_strategy)
@settings(max_examples=50)
def test_testmodel::cont_instantiation(instance):
    assert isinstance(instance, testmodel::cont)
