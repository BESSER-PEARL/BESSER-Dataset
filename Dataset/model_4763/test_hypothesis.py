import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Sequence,
    ctrlflow101_Loop,
    ctrlflow101_Or,
    ctrlflow101_Start,
    ctrlflow101_Final,
    ctrlflow101_And,
    ctrlflow101_SequenceNode,
    SequenceNode,
    ctrlflow101_Function,
    ctrlflow101_Token,
    ctrlflow101_Sequence,
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



def test_ctrlflow101_loop_is_not_abstract():
    assert not inspect.isabstract(ctrlflow101_Loop)


def test_ctrlflow101_loop_constructor_exists():
    assert callable(ctrlflow101_Loop.__init__)


def test_ctrlflow101_loop_constructor_args():
    sig = inspect.signature(ctrlflow101_Loop.__init__)
    params = list(sig.parameters.keys())



def test_ctrlflow101_or_is_not_abstract():
    assert not inspect.isabstract(ctrlflow101_Or)


def test_ctrlflow101_or_constructor_exists():
    assert callable(ctrlflow101_Or.__init__)


def test_ctrlflow101_or_constructor_args():
    sig = inspect.signature(ctrlflow101_Or.__init__)
    params = list(sig.parameters.keys())



def test_ctrlflow101_start_is_not_abstract():
    assert not inspect.isabstract(ctrlflow101_Start)


def test_ctrlflow101_start_constructor_exists():
    assert callable(ctrlflow101_Start.__init__)


def test_ctrlflow101_start_constructor_args():
    sig = inspect.signature(ctrlflow101_Start.__init__)
    params = list(sig.parameters.keys())



def test_ctrlflow101_final_is_not_abstract():
    assert not inspect.isabstract(ctrlflow101_Final)


def test_ctrlflow101_final_constructor_exists():
    assert callable(ctrlflow101_Final.__init__)


def test_ctrlflow101_final_constructor_args():
    sig = inspect.signature(ctrlflow101_Final.__init__)
    params = list(sig.parameters.keys())



def test_ctrlflow101_and_is_not_abstract():
    assert not inspect.isabstract(ctrlflow101_And)


def test_ctrlflow101_and_constructor_exists():
    assert callable(ctrlflow101_And.__init__)


def test_ctrlflow101_and_constructor_args():
    sig = inspect.signature(ctrlflow101_And.__init__)
    params = list(sig.parameters.keys())



def test_ctrlflow101_sequencenode_is_not_abstract():
    assert not inspect.isabstract(ctrlflow101_SequenceNode)


def test_ctrlflow101_sequencenode_constructor_exists():
    assert callable(ctrlflow101_SequenceNode.__init__)


def test_ctrlflow101_sequencenode_constructor_args():
    sig = inspect.signature(ctrlflow101_SequenceNode.__init__)
    params = list(sig.parameters.keys())
    assert "tMax" in params, "Missing parameter 'tMax'"
    assert "tMin" in params, "Missing parameter 'tMin'"
    assert "name" in params, "Missing parameter 'name'"

def test_ctrlflow101_sequencenode_has_tMax():
    assert hasattr(ctrlflow101_SequenceNode, "tMax")
    descriptor = None
    for klass in ctrlflow101_SequenceNode.__mro__:
        if "tMax" in klass.__dict__:
            descriptor = klass.__dict__["tMax"]
            break
    assert isinstance(descriptor, property)

def test_ctrlflow101_sequencenode_has_tMin():
    assert hasattr(ctrlflow101_SequenceNode, "tMin")
    descriptor = None
    for klass in ctrlflow101_SequenceNode.__mro__:
        if "tMin" in klass.__dict__:
            descriptor = klass.__dict__["tMin"]
            break
    assert isinstance(descriptor, property)

def test_ctrlflow101_sequencenode_has_name():
    assert hasattr(ctrlflow101_SequenceNode, "name")
    descriptor = None
    for klass in ctrlflow101_SequenceNode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sequencenode_is_not_abstract():
    assert not inspect.isabstract(SequenceNode)


def test_sequencenode_constructor_exists():
    assert callable(SequenceNode.__init__)


def test_sequencenode_constructor_args():
    sig = inspect.signature(SequenceNode.__init__)
    params = list(sig.parameters.keys())



def test_ctrlflow101_function_is_not_abstract():
    assert not inspect.isabstract(ctrlflow101_Function)


def test_ctrlflow101_function_constructor_exists():
    assert callable(ctrlflow101_Function.__init__)


def test_ctrlflow101_function_constructor_args():
    sig = inspect.signature(ctrlflow101_Function.__init__)
    params = list(sig.parameters.keys())



def test_ctrlflow101_token_is_not_abstract():
    assert not inspect.isabstract(ctrlflow101_Token)


def test_ctrlflow101_token_constructor_exists():
    assert callable(ctrlflow101_Token.__init__)


def test_ctrlflow101_token_constructor_args():
    sig = inspect.signature(ctrlflow101_Token.__init__)
    params = list(sig.parameters.keys())



def test_ctrlflow101_sequence_is_not_abstract():
    assert not inspect.isabstract(ctrlflow101_Sequence)


def test_ctrlflow101_sequence_constructor_exists():
    assert callable(ctrlflow101_Sequence.__init__)


def test_ctrlflow101_sequence_constructor_args():
    sig = inspect.signature(ctrlflow101_Sequence.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_ctrlflow101_sequence_has_weight():
    assert hasattr(ctrlflow101_Sequence, "weight")
    descriptor = None
    for klass in ctrlflow101_Sequence.__mro__:
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
ctrlflow101_Loop_strategy = st.builds(
    ctrlflow101_Loop,
)
ctrlflow101_Or_strategy = st.builds(
    ctrlflow101_Or,
)
ctrlflow101_Start_strategy = st.builds(
    ctrlflow101_Start,
)
ctrlflow101_Final_strategy = st.builds(
    ctrlflow101_Final,
)
ctrlflow101_And_strategy = st.builds(
    ctrlflow101_And,
)
ctrlflow101_SequenceNode_strategy = st.builds(
    ctrlflow101_SequenceNode,
    tMax=
        st.integers(),
    tMin=
        st.integers(),
    name=
        safe_text
)
SequenceNode_strategy = st.builds(
    SequenceNode,
)
ctrlflow101_Function_strategy = st.builds(
    ctrlflow101_Function,
)
ctrlflow101_Token_strategy = st.builds(
    ctrlflow101_Token,
)
ctrlflow101_Sequence_strategy = st.builds(
    ctrlflow101_Sequence,
    weight=
        st.integers()
)

@given(instance=Sequence_strategy)
@settings(max_examples=50)
def test_sequence_instantiation(instance):
    assert isinstance(instance, Sequence)

@given(instance=ctrlflow101_Loop_strategy)
@settings(max_examples=50)
def test_ctrlflow101_loop_instantiation(instance):
    assert isinstance(instance, ctrlflow101_Loop)

@given(instance=ctrlflow101_Or_strategy)
@settings(max_examples=50)
def test_ctrlflow101_or_instantiation(instance):
    assert isinstance(instance, ctrlflow101_Or)

@given(instance=ctrlflow101_Start_strategy)
@settings(max_examples=50)
def test_ctrlflow101_start_instantiation(instance):
    assert isinstance(instance, ctrlflow101_Start)

@given(instance=ctrlflow101_Final_strategy)
@settings(max_examples=50)
def test_ctrlflow101_final_instantiation(instance):
    assert isinstance(instance, ctrlflow101_Final)

@given(instance=ctrlflow101_And_strategy)
@settings(max_examples=50)
def test_ctrlflow101_and_instantiation(instance):
    assert isinstance(instance, ctrlflow101_And)

@given(instance=ctrlflow101_SequenceNode_strategy)
@settings(max_examples=50)
def test_ctrlflow101_sequencenode_instantiation(instance):
    assert isinstance(instance, ctrlflow101_SequenceNode)



@given(instance=ctrlflow101_SequenceNode_strategy)
def test_ctrlflow101_sequencenode_tMax_setter(instance):
    original = instance.tMax
    instance.tMax = original
    assert instance.tMax == original



@given(instance=ctrlflow101_SequenceNode_strategy)
def test_ctrlflow101_sequencenode_tMin_setter(instance):
    original = instance.tMin
    instance.tMin = original
    assert instance.tMin == original



@given(instance=ctrlflow101_SequenceNode_strategy)
def test_ctrlflow101_sequencenode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SequenceNode_strategy)
@settings(max_examples=50)
def test_sequencenode_instantiation(instance):
    assert isinstance(instance, SequenceNode)

@given(instance=ctrlflow101_Function_strategy)
@settings(max_examples=50)
def test_ctrlflow101_function_instantiation(instance):
    assert isinstance(instance, ctrlflow101_Function)

@given(instance=ctrlflow101_Token_strategy)
@settings(max_examples=50)
def test_ctrlflow101_token_instantiation(instance):
    assert isinstance(instance, ctrlflow101_Token)

@given(instance=ctrlflow101_Sequence_strategy)
@settings(max_examples=50)
def test_ctrlflow101_sequence_instantiation(instance):
    assert isinstance(instance, ctrlflow101_Sequence)



@given(instance=ctrlflow101_Sequence_strategy)
def test_ctrlflow101_sequence_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original
