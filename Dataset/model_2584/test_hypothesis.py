import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    atomic_XAnnotable,
    atomic_ATargetEdge,
    XAnnotable,
    atomic_ANode,
    ANode,
    atomic_AEdge,
    atomic_AStructured,
    atomic_AToken,
    atomic_AGraph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_atomic_xannotable_is_not_abstract():
    assert not inspect.isabstract(atomic_XAnnotable)


def test_atomic_xannotable_constructor_exists():
    assert callable(atomic_XAnnotable.__init__)


def test_atomic_xannotable_constructor_args():
    sig = inspect.signature(atomic_XAnnotable.__init__)
    params = list(sig.parameters.keys())



def test_atomic_atargetedge_is_not_abstract():
    assert not inspect.isabstract(atomic_ATargetEdge)


def test_atomic_atargetedge_constructor_exists():
    assert callable(atomic_ATargetEdge.__init__)


def test_atomic_atargetedge_constructor_args():
    sig = inspect.signature(atomic_ATargetEdge.__init__)
    params = list(sig.parameters.keys())



def test_xannotable_is_not_abstract():
    assert not inspect.isabstract(XAnnotable)


def test_xannotable_constructor_exists():
    assert callable(XAnnotable.__init__)


def test_xannotable_constructor_args():
    sig = inspect.signature(XAnnotable.__init__)
    params = list(sig.parameters.keys())



def test_atomic_anode_is_not_abstract():
    assert not inspect.isabstract(atomic_ANode)


def test_atomic_anode_constructor_exists():
    assert callable(atomic_ANode.__init__)


def test_atomic_anode_constructor_args():
    sig = inspect.signature(atomic_ANode.__init__)
    params = list(sig.parameters.keys())



def test_anode_is_not_abstract():
    assert not inspect.isabstract(ANode)


def test_anode_constructor_exists():
    assert callable(ANode.__init__)


def test_anode_constructor_args():
    sig = inspect.signature(ANode.__init__)
    params = list(sig.parameters.keys())



def test_atomic_aedge_is_not_abstract():
    assert not inspect.isabstract(atomic_AEdge)


def test_atomic_aedge_constructor_exists():
    assert callable(atomic_AEdge.__init__)


def test_atomic_aedge_constructor_args():
    sig = inspect.signature(atomic_AEdge.__init__)
    params = list(sig.parameters.keys())



def test_atomic_astructured_is_not_abstract():
    assert not inspect.isabstract(atomic_AStructured)


def test_atomic_astructured_constructor_exists():
    assert callable(atomic_AStructured.__init__)


def test_atomic_astructured_constructor_args():
    sig = inspect.signature(atomic_AStructured.__init__)
    params = list(sig.parameters.keys())



def test_atomic_atoken_is_not_abstract():
    assert not inspect.isabstract(atomic_AToken)


def test_atomic_atoken_constructor_exists():
    assert callable(atomic_AToken.__init__)


def test_atomic_atoken_constructor_args():
    sig = inspect.signature(atomic_AToken.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_atomic_atoken_has_text():
    assert hasattr(atomic_AToken, "text")
    descriptor = None
    for klass in atomic_AToken.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_atomic_agraph_is_not_abstract():
    assert not inspect.isabstract(atomic_AGraph)


def test_atomic_agraph_constructor_exists():
    assert callable(atomic_AGraph.__init__)


def test_atomic_agraph_constructor_args():
    sig = inspect.signature(atomic_AGraph.__init__)
    params = list(sig.parameters.keys())
    assert "corpus" in params, "Missing parameter 'corpus'"

def test_atomic_agraph_has_corpus():
    assert hasattr(atomic_AGraph, "corpus")
    descriptor = None
    for klass in atomic_AGraph.__mro__:
        if "corpus" in klass.__dict__:
            descriptor = klass.__dict__["corpus"]
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
atomic_XAnnotable_strategy = st.builds(
    atomic_XAnnotable,
)
atomic_ATargetEdge_strategy = st.builds(
    atomic_ATargetEdge,
)
XAnnotable_strategy = st.builds(
    XAnnotable,
)
atomic_ANode_strategy = st.builds(
    atomic_ANode,
)
ANode_strategy = st.builds(
    ANode,
)
atomic_AEdge_strategy = st.builds(
    atomic_AEdge,
)
atomic_AStructured_strategy = st.builds(
    atomic_AStructured,
)
atomic_AToken_strategy = st.builds(
    atomic_AToken,
    text=
        safe_text
)
atomic_AGraph_strategy = st.builds(
    atomic_AGraph,
    corpus=
        safe_text
)

@given(instance=atomic_XAnnotable_strategy)
@settings(max_examples=50)
def test_atomic_xannotable_instantiation(instance):
    assert isinstance(instance, atomic_XAnnotable)

@given(instance=atomic_ATargetEdge_strategy)
@settings(max_examples=50)
def test_atomic_atargetedge_instantiation(instance):
    assert isinstance(instance, atomic_ATargetEdge)

@given(instance=XAnnotable_strategy)
@settings(max_examples=50)
def test_xannotable_instantiation(instance):
    assert isinstance(instance, XAnnotable)

@given(instance=atomic_ANode_strategy)
@settings(max_examples=50)
def test_atomic_anode_instantiation(instance):
    assert isinstance(instance, atomic_ANode)

@given(instance=ANode_strategy)
@settings(max_examples=50)
def test_anode_instantiation(instance):
    assert isinstance(instance, ANode)

@given(instance=atomic_AEdge_strategy)
@settings(max_examples=50)
def test_atomic_aedge_instantiation(instance):
    assert isinstance(instance, atomic_AEdge)

@given(instance=atomic_AStructured_strategy)
@settings(max_examples=50)
def test_atomic_astructured_instantiation(instance):
    assert isinstance(instance, atomic_AStructured)

@given(instance=atomic_AToken_strategy)
@settings(max_examples=50)
def test_atomic_atoken_instantiation(instance):
    assert isinstance(instance, atomic_AToken)



@given(instance=atomic_AToken_strategy)
def test_atomic_atoken_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=atomic_AGraph_strategy)
@settings(max_examples=50)
def test_atomic_agraph_instantiation(instance):
    assert isinstance(instance, atomic_AGraph)



@given(instance=atomic_AGraph_strategy)
def test_atomic_agraph_corpus_setter(instance):
    original = instance.corpus
    instance.corpus = original
    assert instance.corpus == original
