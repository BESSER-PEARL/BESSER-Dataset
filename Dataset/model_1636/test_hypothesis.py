import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbstractTransition,
    ptntim101_Transition,
    AbstractNode,
    ptntim101_Token,
    ptntim101_AbstractTransition,
    ptntim101_AbstractNode,
    ptntim101_Place,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstracttransition_is_not_abstract():
    assert not inspect.isabstract(AbstractTransition)


def test_abstracttransition_constructor_exists():
    assert callable(AbstractTransition.__init__)


def test_abstracttransition_constructor_args():
    sig = inspect.signature(AbstractTransition.__init__)
    params = list(sig.parameters.keys())



def test_ptntim101_transition_is_not_abstract():
    assert not inspect.isabstract(ptntim101_Transition)


def test_ptntim101_transition_constructor_exists():
    assert callable(ptntim101_Transition.__init__)


def test_ptntim101_transition_constructor_args():
    sig = inspect.signature(ptntim101_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_ptntim101_transition_has_weight():
    assert hasattr(ptntim101_Transition, "weight")
    descriptor = None
    for klass in ptntim101_Transition.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_abstractnode_is_not_abstract():
    assert not inspect.isabstract(AbstractNode)


def test_abstractnode_constructor_exists():
    assert callable(AbstractNode.__init__)


def test_abstractnode_constructor_args():
    sig = inspect.signature(AbstractNode.__init__)
    params = list(sig.parameters.keys())



def test_ptntim101_token_is_not_abstract():
    assert not inspect.isabstract(ptntim101_Token)


def test_ptntim101_token_constructor_exists():
    assert callable(ptntim101_Token.__init__)


def test_ptntim101_token_constructor_args():
    sig = inspect.signature(ptntim101_Token.__init__)
    params = list(sig.parameters.keys())



def test_ptntim101_abstracttransition_is_not_abstract():
    assert not inspect.isabstract(ptntim101_AbstractTransition)


def test_ptntim101_abstracttransition_constructor_exists():
    assert callable(ptntim101_AbstractTransition.__init__)


def test_ptntim101_abstracttransition_constructor_args():
    sig = inspect.signature(ptntim101_AbstractTransition.__init__)
    params = list(sig.parameters.keys())
    assert "guard" in params, "Missing parameter 'guard'"

def test_ptntim101_abstracttransition_has_guard():
    assert hasattr(ptntim101_AbstractTransition, "guard")
    descriptor = None
    for klass in ptntim101_AbstractTransition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)



def test_ptntim101_abstractnode_is_not_abstract():
    assert not inspect.isabstract(ptntim101_AbstractNode)


def test_ptntim101_abstractnode_constructor_exists():
    assert callable(ptntim101_AbstractNode.__init__)


def test_ptntim101_abstractnode_constructor_args():
    sig = inspect.signature(ptntim101_AbstractNode.__init__)
    params = list(sig.parameters.keys())
    assert "tMin" in params, "Missing parameter 'tMin'"
    assert "tMax" in params, "Missing parameter 'tMax'"
    assert "name" in params, "Missing parameter 'name'"

def test_ptntim101_abstractnode_has_tMin():
    assert hasattr(ptntim101_AbstractNode, "tMin")
    descriptor = None
    for klass in ptntim101_AbstractNode.__mro__:
        if "tMin" in klass.__dict__:
            descriptor = klass.__dict__["tMin"]
            break
    assert isinstance(descriptor, property)

def test_ptntim101_abstractnode_has_tMax():
    assert hasattr(ptntim101_AbstractNode, "tMax")
    descriptor = None
    for klass in ptntim101_AbstractNode.__mro__:
        if "tMax" in klass.__dict__:
            descriptor = klass.__dict__["tMax"]
            break
    assert isinstance(descriptor, property)

def test_ptntim101_abstractnode_has_name():
    assert hasattr(ptntim101_AbstractNode, "name")
    descriptor = None
    for klass in ptntim101_AbstractNode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ptntim101_place_is_not_abstract():
    assert not inspect.isabstract(ptntim101_Place)


def test_ptntim101_place_constructor_exists():
    assert callable(ptntim101_Place.__init__)


def test_ptntim101_place_constructor_args():
    sig = inspect.signature(ptntim101_Place.__init__)
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
AbstractTransition_strategy = st.builds(
    AbstractTransition,
)
ptntim101_Transition_strategy = st.builds(
    ptntim101_Transition,
    weight=
        st.integers()
)
AbstractNode_strategy = st.builds(
    AbstractNode,
)
ptntim101_Token_strategy = st.builds(
    ptntim101_Token,
)
ptntim101_AbstractTransition_strategy = st.builds(
    ptntim101_AbstractTransition,
    guard=
        safe_text
)
ptntim101_AbstractNode_strategy = st.builds(
    ptntim101_AbstractNode,
    tMin=
        st.integers(),
    tMax=
        st.integers(),
    name=
        safe_text
)
ptntim101_Place_strategy = st.builds(
    ptntim101_Place,
)

@given(instance=AbstractTransition_strategy)
@settings(max_examples=50)
def test_abstracttransition_instantiation(instance):
    assert isinstance(instance, AbstractTransition)

@given(instance=ptntim101_Transition_strategy)
@settings(max_examples=50)
def test_ptntim101_transition_instantiation(instance):
    assert isinstance(instance, ptntim101_Transition)



@given(instance=ptntim101_Transition_strategy)
def test_ptntim101_transition_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=AbstractNode_strategy)
@settings(max_examples=50)
def test_abstractnode_instantiation(instance):
    assert isinstance(instance, AbstractNode)

@given(instance=ptntim101_Token_strategy)
@settings(max_examples=50)
def test_ptntim101_token_instantiation(instance):
    assert isinstance(instance, ptntim101_Token)

@given(instance=ptntim101_AbstractTransition_strategy)
@settings(max_examples=50)
def test_ptntim101_abstracttransition_instantiation(instance):
    assert isinstance(instance, ptntim101_AbstractTransition)



@given(instance=ptntim101_AbstractTransition_strategy)
def test_ptntim101_abstracttransition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=ptntim101_AbstractNode_strategy)
@settings(max_examples=50)
def test_ptntim101_abstractnode_instantiation(instance):
    assert isinstance(instance, ptntim101_AbstractNode)



@given(instance=ptntim101_AbstractNode_strategy)
def test_ptntim101_abstractnode_tMin_setter(instance):
    original = instance.tMin
    instance.tMin = original
    assert instance.tMin == original



@given(instance=ptntim101_AbstractNode_strategy)
def test_ptntim101_abstractnode_tMax_setter(instance):
    original = instance.tMax
    instance.tMax = original
    assert instance.tMax == original



@given(instance=ptntim101_AbstractNode_strategy)
def test_ptntim101_abstractnode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ptntim101_Place_strategy)
@settings(max_examples=50)
def test_ptntim101_place_instantiation(instance):
    assert isinstance(instance, ptntim101_Place)
