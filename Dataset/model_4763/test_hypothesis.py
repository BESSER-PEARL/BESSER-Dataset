import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Sequence,
    ctrlflow101::Start,
    ctrlflow101::Or,
    ctrlflow101::Final,
    ctrlflow101::Loop,
    ctrlflow101::And,
    ctrlflow101::SequenceNode,
    SequenceNode,
    ctrlflow101::Function,
    ctrlflow101::Token,
    ctrlflow101::Sequence,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sequence_is_not_abstract():
    assert not inspect.isabstract(Sequence)


def test_sequence_constructor_exists():
    assert callable(Sequence.__init__)


def test_sequence_constructor_args():
    sig = inspect.signature(Sequence.__init__)
    params = list(sig.parameters.keys())



def test_ctrlflow101::start_is_not_abstract():
    assert not inspect.isabstract(ctrlflow101::Start)


def test_ctrlflow101::start_constructor_exists():
    assert callable(ctrlflow101::Start.__init__)


def test_ctrlflow101::start_constructor_args():
    sig = inspect.signature(ctrlflow101::Start.__init__)
    params = list(sig.parameters.keys())



def test_ctrlflow101::or_is_not_abstract():
    assert not inspect.isabstract(ctrlflow101::Or)


def test_ctrlflow101::or_constructor_exists():
    assert callable(ctrlflow101::Or.__init__)


def test_ctrlflow101::or_constructor_args():
    sig = inspect.signature(ctrlflow101::Or.__init__)
    params = list(sig.parameters.keys())



def test_ctrlflow101::final_is_not_abstract():
    assert not inspect.isabstract(ctrlflow101::Final)


def test_ctrlflow101::final_constructor_exists():
    assert callable(ctrlflow101::Final.__init__)


def test_ctrlflow101::final_constructor_args():
    sig = inspect.signature(ctrlflow101::Final.__init__)
    params = list(sig.parameters.keys())



def test_ctrlflow101::loop_is_not_abstract():
    assert not inspect.isabstract(ctrlflow101::Loop)


def test_ctrlflow101::loop_constructor_exists():
    assert callable(ctrlflow101::Loop.__init__)


def test_ctrlflow101::loop_constructor_args():
    sig = inspect.signature(ctrlflow101::Loop.__init__)
    params = list(sig.parameters.keys())



def test_ctrlflow101::and_is_not_abstract():
    assert not inspect.isabstract(ctrlflow101::And)


def test_ctrlflow101::and_constructor_exists():
    assert callable(ctrlflow101::And.__init__)


def test_ctrlflow101::and_constructor_args():
    sig = inspect.signature(ctrlflow101::And.__init__)
    params = list(sig.parameters.keys())



def test_ctrlflow101::sequencenode_is_not_abstract():
    assert not inspect.isabstract(ctrlflow101::SequenceNode)


def test_ctrlflow101::sequencenode_constructor_exists():
    assert callable(ctrlflow101::SequenceNode.__init__)


def test_ctrlflow101::sequencenode_constructor_args():
    sig = inspect.signature(ctrlflow101::SequenceNode.__init__)
    params = list(sig.parameters.keys())
    assert "tMax" in params, "Missing parameter 'tMax'"
    assert "name" in params, "Missing parameter 'name'"
    assert "tMin" in params, "Missing parameter 'tMin'"

def test_ctrlflow101::sequencenode_has_tMax():
    assert hasattr(ctrlflow101::SequenceNode, "tMax")
    descriptor = None
    for klass in ctrlflow101::SequenceNode.__mro__:
        if "tMax" in klass.__dict__:
            descriptor = klass.__dict__["tMax"]
            break
    assert isinstance(descriptor, property)

def test_ctrlflow101::sequencenode_has_name():
    assert hasattr(ctrlflow101::SequenceNode, "name")
    descriptor = None
    for klass in ctrlflow101::SequenceNode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ctrlflow101::sequencenode_has_tMin():
    assert hasattr(ctrlflow101::SequenceNode, "tMin")
    descriptor = None
    for klass in ctrlflow101::SequenceNode.__mro__:
        if "tMin" in klass.__dict__:
            descriptor = klass.__dict__["tMin"]
            break
    assert isinstance(descriptor, property)



def test_sequencenode_is_not_abstract():
    assert not inspect.isabstract(SequenceNode)


def test_sequencenode_constructor_exists():
    assert callable(SequenceNode.__init__)


def test_sequencenode_constructor_args():
    sig = inspect.signature(SequenceNode.__init__)
    params = list(sig.parameters.keys())



def test_ctrlflow101::function_is_not_abstract():
    assert not inspect.isabstract(ctrlflow101::Function)


def test_ctrlflow101::function_constructor_exists():
    assert callable(ctrlflow101::Function.__init__)


def test_ctrlflow101::function_constructor_args():
    sig = inspect.signature(ctrlflow101::Function.__init__)
    params = list(sig.parameters.keys())



def test_ctrlflow101::token_is_not_abstract():
    assert not inspect.isabstract(ctrlflow101::Token)


def test_ctrlflow101::token_constructor_exists():
    assert callable(ctrlflow101::Token.__init__)


def test_ctrlflow101::token_constructor_args():
    sig = inspect.signature(ctrlflow101::Token.__init__)
    params = list(sig.parameters.keys())



def test_ctrlflow101::sequence_is_not_abstract():
    assert not inspect.isabstract(ctrlflow101::Sequence)


def test_ctrlflow101::sequence_constructor_exists():
    assert callable(ctrlflow101::Sequence.__init__)


def test_ctrlflow101::sequence_constructor_args():
    sig = inspect.signature(ctrlflow101::Sequence.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_ctrlflow101::sequence_has_weight():
    assert hasattr(ctrlflow101::Sequence, "weight")
    descriptor = None
    for klass in ctrlflow101::Sequence.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
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
Sequence_strategy = st.builds(
    Sequence,
)
ctrlflow101::Start_strategy = st.builds(
    ctrlflow101::Start,
)
ctrlflow101::Or_strategy = st.builds(
    ctrlflow101::Or,
)
ctrlflow101::Final_strategy = st.builds(
    ctrlflow101::Final,
)
ctrlflow101::Loop_strategy = st.builds(
    ctrlflow101::Loop,
)
ctrlflow101::And_strategy = st.builds(
    ctrlflow101::And,
)
ctrlflow101::SequenceNode_strategy = st.builds(
    ctrlflow101::SequenceNode,
    tMax=
        st.integers(),
    name=
        safe_text,
    tMin=
        st.integers()
)
SequenceNode_strategy = st.builds(
    SequenceNode,
)
ctrlflow101::Function_strategy = st.builds(
    ctrlflow101::Function,
)
ctrlflow101::Token_strategy = st.builds(
    ctrlflow101::Token,
)
ctrlflow101::Sequence_strategy = st.builds(
    ctrlflow101::Sequence,
    weight=
        st.integers()
)

@given(instance=Sequence_strategy)
@settings(max_examples=50)
def test_sequence_instantiation(instance):
    assert isinstance(instance, Sequence)

@given(instance=ctrlflow101::Start_strategy)
@settings(max_examples=50)
def test_ctrlflow101::start_instantiation(instance):
    assert isinstance(instance, ctrlflow101::Start)

@given(instance=ctrlflow101::Or_strategy)
@settings(max_examples=50)
def test_ctrlflow101::or_instantiation(instance):
    assert isinstance(instance, ctrlflow101::Or)

@given(instance=ctrlflow101::Final_strategy)
@settings(max_examples=50)
def test_ctrlflow101::final_instantiation(instance):
    assert isinstance(instance, ctrlflow101::Final)

@given(instance=ctrlflow101::Loop_strategy)
@settings(max_examples=50)
def test_ctrlflow101::loop_instantiation(instance):
    assert isinstance(instance, ctrlflow101::Loop)

@given(instance=ctrlflow101::And_strategy)
@settings(max_examples=50)
def test_ctrlflow101::and_instantiation(instance):
    assert isinstance(instance, ctrlflow101::And)

@given(instance=ctrlflow101::SequenceNode_strategy)
@settings(max_examples=50)
def test_ctrlflow101::sequencenode_instantiation(instance):
    assert isinstance(instance, ctrlflow101::SequenceNode)

@given(instance=ctrlflow101::SequenceNode_strategy)
def test_ctrlflow101::sequencenode_tMax_type(instance):
    assert isinstance(instance.tMax, int)


@given(instance=ctrlflow101::SequenceNode_strategy)
def test_ctrlflow101::sequencenode_tMax_setter(instance):
    original = instance.tMax
    instance.tMax = original
    assert instance.tMax == original

@given(instance=ctrlflow101::SequenceNode_strategy)
def test_ctrlflow101::sequencenode_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ctrlflow101::SequenceNode_strategy)
def test_ctrlflow101::sequencenode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ctrlflow101::SequenceNode_strategy)
def test_ctrlflow101::sequencenode_tMin_type(instance):
    assert isinstance(instance.tMin, int)


@given(instance=ctrlflow101::SequenceNode_strategy)
def test_ctrlflow101::sequencenode_tMin_setter(instance):
    original = instance.tMin
    instance.tMin = original
    assert instance.tMin == original

@given(instance=SequenceNode_strategy)
@settings(max_examples=50)
def test_sequencenode_instantiation(instance):
    assert isinstance(instance, SequenceNode)

@given(instance=ctrlflow101::Function_strategy)
@settings(max_examples=50)
def test_ctrlflow101::function_instantiation(instance):
    assert isinstance(instance, ctrlflow101::Function)

@given(instance=ctrlflow101::Token_strategy)
@settings(max_examples=50)
def test_ctrlflow101::token_instantiation(instance):
    assert isinstance(instance, ctrlflow101::Token)

@given(instance=ctrlflow101::Sequence_strategy)
@settings(max_examples=50)
def test_ctrlflow101::sequence_instantiation(instance):
    assert isinstance(instance, ctrlflow101::Sequence)

@given(instance=ctrlflow101::Sequence_strategy)
def test_ctrlflow101::sequence_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=ctrlflow101::Sequence_strategy)
def test_ctrlflow101::sequence_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original
