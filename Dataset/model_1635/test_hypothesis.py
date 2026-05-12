import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbstractTransition,
    ptn_Transition,
    ptn_Token,
    ptn_AbstractNode,
    AbstractNode,
    ptn_AbstractTransition,
    ptn_Place,
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



def test_ptn_transition_is_not_abstract():
    assert not inspect.isabstract(ptn_Transition)


def test_ptn_transition_constructor_exists():
    assert callable(ptn_Transition.__init__)


def test_ptn_transition_constructor_args():
    sig = inspect.signature(ptn_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_ptn_transition_has_weight():
    assert hasattr(ptn_Transition, "weight")
    descriptor = None
    for klass in ptn_Transition.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_ptn_token_is_not_abstract():
    assert not inspect.isabstract(ptn_Token)


def test_ptn_token_constructor_exists():
    assert callable(ptn_Token.__init__)


def test_ptn_token_constructor_args():
    sig = inspect.signature(ptn_Token.__init__)
    params = list(sig.parameters.keys())



def test_ptn_abstractnode_is_not_abstract():
    assert not inspect.isabstract(ptn_AbstractNode)


def test_ptn_abstractnode_constructor_exists():
    assert callable(ptn_AbstractNode.__init__)


def test_ptn_abstractnode_constructor_args():
    sig = inspect.signature(ptn_AbstractNode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "tMax" in params, "Missing parameter 'tMax'"
    assert "tMin" in params, "Missing parameter 'tMin'"

def test_ptn_abstractnode_has_name():
    assert hasattr(ptn_AbstractNode, "name")
    descriptor = None
    for klass in ptn_AbstractNode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ptn_abstractnode_has_tMax():
    assert hasattr(ptn_AbstractNode, "tMax")
    descriptor = None
    for klass in ptn_AbstractNode.__mro__:
        if "tMax" in klass.__dict__:
            descriptor = klass.__dict__["tMax"]
            break
    assert isinstance(descriptor, property)

def test_ptn_abstractnode_has_tMin():
    assert hasattr(ptn_AbstractNode, "tMin")
    descriptor = None
    for klass in ptn_AbstractNode.__mro__:
        if "tMin" in klass.__dict__:
            descriptor = klass.__dict__["tMin"]
            break
    assert isinstance(descriptor, property)



def test_abstractnode_is_not_abstract():
    assert not inspect.isabstract(AbstractNode)


def test_abstractnode_constructor_exists():
    assert callable(AbstractNode.__init__)


def test_abstractnode_constructor_args():
    sig = inspect.signature(AbstractNode.__init__)
    params = list(sig.parameters.keys())



def test_ptn_abstracttransition_is_not_abstract():
    assert not inspect.isabstract(ptn_AbstractTransition)


def test_ptn_abstracttransition_constructor_exists():
    assert callable(ptn_AbstractTransition.__init__)


def test_ptn_abstracttransition_constructor_args():
    sig = inspect.signature(ptn_AbstractTransition.__init__)
    params = list(sig.parameters.keys())
    assert "guard" in params, "Missing parameter 'guard'"

def test_ptn_abstracttransition_has_guard():
    assert hasattr(ptn_AbstractTransition, "guard")
    descriptor = None
    for klass in ptn_AbstractTransition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)



def test_ptn_place_is_not_abstract():
    assert not inspect.isabstract(ptn_Place)


def test_ptn_place_constructor_exists():
    assert callable(ptn_Place.__init__)


def test_ptn_place_constructor_args():
    sig = inspect.signature(ptn_Place.__init__)
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
ptn_Transition_strategy = st.builds(
    ptn_Transition,
    weight=
        st.integers()
)
ptn_Token_strategy = st.builds(
    ptn_Token,
)
ptn_AbstractNode_strategy = st.builds(
    ptn_AbstractNode,
    name=
        safe_text,
    tMax=
        st.integers(),
    tMin=
        st.integers()
)
AbstractNode_strategy = st.builds(
    AbstractNode,
)
ptn_AbstractTransition_strategy = st.builds(
    ptn_AbstractTransition,
    guard=
        safe_text
)
ptn_Place_strategy = st.builds(
    ptn_Place,
)

@given(instance=AbstractTransition_strategy)
@settings(max_examples=50)
def test_abstracttransition_instantiation(instance):
    assert isinstance(instance, AbstractTransition)

@given(instance=ptn_Transition_strategy)
@settings(max_examples=50)
def test_ptn_transition_instantiation(instance):
    assert isinstance(instance, ptn_Transition)



@given(instance=ptn_Transition_strategy)
def test_ptn_transition_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=ptn_Token_strategy)
@settings(max_examples=50)
def test_ptn_token_instantiation(instance):
    assert isinstance(instance, ptn_Token)

@given(instance=ptn_AbstractNode_strategy)
@settings(max_examples=50)
def test_ptn_abstractnode_instantiation(instance):
    assert isinstance(instance, ptn_AbstractNode)



@given(instance=ptn_AbstractNode_strategy)
def test_ptn_abstractnode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ptn_AbstractNode_strategy)
def test_ptn_abstractnode_tMax_setter(instance):
    original = instance.tMax
    instance.tMax = original
    assert instance.tMax == original



@given(instance=ptn_AbstractNode_strategy)
def test_ptn_abstractnode_tMin_setter(instance):
    original = instance.tMin
    instance.tMin = original
    assert instance.tMin == original

@given(instance=AbstractNode_strategy)
@settings(max_examples=50)
def test_abstractnode_instantiation(instance):
    assert isinstance(instance, AbstractNode)

@given(instance=ptn_AbstractTransition_strategy)
@settings(max_examples=50)
def test_ptn_abstracttransition_instantiation(instance):
    assert isinstance(instance, ptn_AbstractTransition)



@given(instance=ptn_AbstractTransition_strategy)
def test_ptn_abstracttransition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=ptn_Place_strategy)
@settings(max_examples=50)
def test_ptn_place_instantiation(instance):
    assert isinstance(instance, ptn_Place)
