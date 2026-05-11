import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    atomic::XAnnotable,
    atomic::ATargetEdge,
    XAnnotable,
    atomic::ANode,
    ANode,
    atomic::AEdge,
    atomic::AStructured,
    atomic::AToken,
    atomic::AGraph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_atomic::xannotable_is_not_abstract():
    assert not inspect.isabstract(atomic::XAnnotable)


def test_atomic::xannotable_constructor_exists():
    assert callable(atomic::XAnnotable.__init__)


def test_atomic::xannotable_constructor_args():
    sig = inspect.signature(atomic::XAnnotable.__init__)
    params = list(sig.parameters.keys())



def test_atomic::atargetedge_is_not_abstract():
    assert not inspect.isabstract(atomic::ATargetEdge)


def test_atomic::atargetedge_constructor_exists():
    assert callable(atomic::ATargetEdge.__init__)


def test_atomic::atargetedge_constructor_args():
    sig = inspect.signature(atomic::ATargetEdge.__init__)
    params = list(sig.parameters.keys())



def test_xannotable_is_not_abstract():
    assert not inspect.isabstract(XAnnotable)


def test_xannotable_constructor_exists():
    assert callable(XAnnotable.__init__)


def test_xannotable_constructor_args():
    sig = inspect.signature(XAnnotable.__init__)
    params = list(sig.parameters.keys())



def test_atomic::anode_is_not_abstract():
    assert not inspect.isabstract(atomic::ANode)


def test_atomic::anode_constructor_exists():
    assert callable(atomic::ANode.__init__)


def test_atomic::anode_constructor_args():
    sig = inspect.signature(atomic::ANode.__init__)
    params = list(sig.parameters.keys())



def test_anode_is_not_abstract():
    assert not inspect.isabstract(ANode)


def test_anode_constructor_exists():
    assert callable(ANode.__init__)


def test_anode_constructor_args():
    sig = inspect.signature(ANode.__init__)
    params = list(sig.parameters.keys())



def test_atomic::aedge_is_not_abstract():
    assert not inspect.isabstract(atomic::AEdge)


def test_atomic::aedge_constructor_exists():
    assert callable(atomic::AEdge.__init__)


def test_atomic::aedge_constructor_args():
    sig = inspect.signature(atomic::AEdge.__init__)
    params = list(sig.parameters.keys())



def test_atomic::astructured_is_not_abstract():
    assert not inspect.isabstract(atomic::AStructured)


def test_atomic::astructured_constructor_exists():
    assert callable(atomic::AStructured.__init__)


def test_atomic::astructured_constructor_args():
    sig = inspect.signature(atomic::AStructured.__init__)
    params = list(sig.parameters.keys())



def test_atomic::atoken_is_not_abstract():
    assert not inspect.isabstract(atomic::AToken)


def test_atomic::atoken_constructor_exists():
    assert callable(atomic::AToken.__init__)


def test_atomic::atoken_constructor_args():
    sig = inspect.signature(atomic::AToken.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_atomic::atoken_has_text():
    assert hasattr(atomic::AToken, "text")
    descriptor = None
    for klass in atomic::AToken.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_atomic::agraph_is_not_abstract():
    assert not inspect.isabstract(atomic::AGraph)


def test_atomic::agraph_constructor_exists():
    assert callable(atomic::AGraph.__init__)


def test_atomic::agraph_constructor_args():
    sig = inspect.signature(atomic::AGraph.__init__)
    params = list(sig.parameters.keys())
    assert "corpus" in params, "Missing parameter 'corpus'"

def test_atomic::agraph_has_corpus():
    assert hasattr(atomic::AGraph, "corpus")
    descriptor = None
    for klass in atomic::AGraph.__mro__:
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
atomic::XAnnotable_strategy = st.builds(
    atomic::XAnnotable,
)
atomic::ATargetEdge_strategy = st.builds(
    atomic::ATargetEdge,
)
XAnnotable_strategy = st.builds(
    XAnnotable,
)
atomic::ANode_strategy = st.builds(
    atomic::ANode,
)
ANode_strategy = st.builds(
    ANode,
)
atomic::AEdge_strategy = st.builds(
    atomic::AEdge,
)
atomic::AStructured_strategy = st.builds(
    atomic::AStructured,
)
atomic::AToken_strategy = st.builds(
    atomic::AToken,
    text=
        safe_text
)
atomic::AGraph_strategy = st.builds(
    atomic::AGraph,
    corpus=
        safe_text
)

@given(instance=atomic::XAnnotable_strategy)
@settings(max_examples=50)
def test_atomic::xannotable_instantiation(instance):
    assert isinstance(instance, atomic::XAnnotable)

@given(instance=atomic::ATargetEdge_strategy)
@settings(max_examples=50)
def test_atomic::atargetedge_instantiation(instance):
    assert isinstance(instance, atomic::ATargetEdge)

@given(instance=XAnnotable_strategy)
@settings(max_examples=50)
def test_xannotable_instantiation(instance):
    assert isinstance(instance, XAnnotable)

@given(instance=atomic::ANode_strategy)
@settings(max_examples=50)
def test_atomic::anode_instantiation(instance):
    assert isinstance(instance, atomic::ANode)

@given(instance=ANode_strategy)
@settings(max_examples=50)
def test_anode_instantiation(instance):
    assert isinstance(instance, ANode)

@given(instance=atomic::AEdge_strategy)
@settings(max_examples=50)
def test_atomic::aedge_instantiation(instance):
    assert isinstance(instance, atomic::AEdge)

@given(instance=atomic::AStructured_strategy)
@settings(max_examples=50)
def test_atomic::astructured_instantiation(instance):
    assert isinstance(instance, atomic::AStructured)

@given(instance=atomic::AToken_strategy)
@settings(max_examples=50)
def test_atomic::atoken_instantiation(instance):
    assert isinstance(instance, atomic::AToken)

@given(instance=atomic::AToken_strategy)
def test_atomic::atoken_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=atomic::AToken_strategy)
def test_atomic::atoken_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=atomic::AGraph_strategy)
@settings(max_examples=50)
def test_atomic::agraph_instantiation(instance):
    assert isinstance(instance, atomic::AGraph)

@given(instance=atomic::AGraph_strategy)
def test_atomic::agraph_corpus_type(instance):
    assert isinstance(instance.corpus, str)


@given(instance=atomic::AGraph_strategy)
def test_atomic::agraph_corpus_setter(instance):
    original = instance.corpus
    instance.corpus = original
    assert instance.corpus == original
