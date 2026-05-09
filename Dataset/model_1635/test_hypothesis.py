import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AbstractTransition,
    ptn::Transition,
    ptn::Token,
    ptn::AbstractNode,
    AbstractNode,
    ptn::AbstractTransition,
    ptn::Place,
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



def test_ptn::transition_is_not_abstract():
    assert not inspect.isabstract(ptn::Transition)


def test_ptn::transition_constructor_exists():
    assert callable(ptn::Transition.__init__)


def test_ptn::transition_constructor_args():
    sig = inspect.signature(ptn::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_ptn::transition_has_weight():
    assert hasattr(ptn::Transition, "weight")
    descriptor = None
    for klass in ptn::Transition.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_ptn::token_is_not_abstract():
    assert not inspect.isabstract(ptn::Token)


def test_ptn::token_constructor_exists():
    assert callable(ptn::Token.__init__)


def test_ptn::token_constructor_args():
    sig = inspect.signature(ptn::Token.__init__)
    params = list(sig.parameters.keys())



def test_ptn::abstractnode_is_not_abstract():
    assert not inspect.isabstract(ptn::AbstractNode)


def test_ptn::abstractnode_constructor_exists():
    assert callable(ptn::AbstractNode.__init__)


def test_ptn::abstractnode_constructor_args():
    sig = inspect.signature(ptn::AbstractNode.__init__)
    params = list(sig.parameters.keys())
    assert "tMax" in params, "Missing parameter 'tMax'"
    assert "tMin" in params, "Missing parameter 'tMin'"
    assert "name" in params, "Missing parameter 'name'"

def test_ptn::abstractnode_has_tMax():
    assert hasattr(ptn::AbstractNode, "tMax")
    descriptor = None
    for klass in ptn::AbstractNode.__mro__:
        if "tMax" in klass.__dict__:
            descriptor = klass.__dict__["tMax"]
            break
    assert isinstance(descriptor, property)

def test_ptn::abstractnode_has_tMin():
    assert hasattr(ptn::AbstractNode, "tMin")
    descriptor = None
    for klass in ptn::AbstractNode.__mro__:
        if "tMin" in klass.__dict__:
            descriptor = klass.__dict__["tMin"]
            break
    assert isinstance(descriptor, property)

def test_ptn::abstractnode_has_name():
    assert hasattr(ptn::AbstractNode, "name")
    descriptor = None
    for klass in ptn::AbstractNode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abstractnode_is_not_abstract():
    assert not inspect.isabstract(AbstractNode)


def test_abstractnode_constructor_exists():
    assert callable(AbstractNode.__init__)


def test_abstractnode_constructor_args():
    sig = inspect.signature(AbstractNode.__init__)
    params = list(sig.parameters.keys())



def test_ptn::abstracttransition_is_not_abstract():
    assert not inspect.isabstract(ptn::AbstractTransition)


def test_ptn::abstracttransition_constructor_exists():
    assert callable(ptn::AbstractTransition.__init__)


def test_ptn::abstracttransition_constructor_args():
    sig = inspect.signature(ptn::AbstractTransition.__init__)
    params = list(sig.parameters.keys())
    assert "guard" in params, "Missing parameter 'guard'"

def test_ptn::abstracttransition_has_guard():
    assert hasattr(ptn::AbstractTransition, "guard")
    descriptor = None
    for klass in ptn::AbstractTransition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)



def test_ptn::place_is_not_abstract():
    assert not inspect.isabstract(ptn::Place)


def test_ptn::place_constructor_exists():
    assert callable(ptn::Place.__init__)


def test_ptn::place_constructor_args():
    sig = inspect.signature(ptn::Place.__init__)
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
ptn::Transition_strategy = st.builds(
    ptn::Transition,
    weight=
        st.integers()
)
ptn::Token_strategy = st.builds(
    ptn::Token,
)
ptn::AbstractNode_strategy = st.builds(
    ptn::AbstractNode,
    tMax=
        st.integers(),
    tMin=
        st.integers(),
    name=
        safe_text
)
AbstractNode_strategy = st.builds(
    AbstractNode,
)
ptn::AbstractTransition_strategy = st.builds(
    ptn::AbstractTransition,
    guard=
        safe_text
)
ptn::Place_strategy = st.builds(
    ptn::Place,
)

@given(instance=AbstractTransition_strategy)
@settings(max_examples=50)
def test_abstracttransition_instantiation(instance):
    assert isinstance(instance, AbstractTransition)

@given(instance=ptn::Transition_strategy)
@settings(max_examples=50)
def test_ptn::transition_instantiation(instance):
    assert isinstance(instance, ptn::Transition)

@given(instance=ptn::Transition_strategy)
def test_ptn::transition_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=ptn::Transition_strategy)
def test_ptn::transition_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=ptn::Token_strategy)
@settings(max_examples=50)
def test_ptn::token_instantiation(instance):
    assert isinstance(instance, ptn::Token)

@given(instance=ptn::AbstractNode_strategy)
@settings(max_examples=50)
def test_ptn::abstractnode_instantiation(instance):
    assert isinstance(instance, ptn::AbstractNode)

@given(instance=ptn::AbstractNode_strategy)
def test_ptn::abstractnode_tMax_type(instance):
    assert isinstance(instance.tMax, int)


@given(instance=ptn::AbstractNode_strategy)
def test_ptn::abstractnode_tMax_setter(instance):
    original = instance.tMax
    instance.tMax = original
    assert instance.tMax == original

@given(instance=ptn::AbstractNode_strategy)
def test_ptn::abstractnode_tMin_type(instance):
    assert isinstance(instance.tMin, int)


@given(instance=ptn::AbstractNode_strategy)
def test_ptn::abstractnode_tMin_setter(instance):
    original = instance.tMin
    instance.tMin = original
    assert instance.tMin == original

@given(instance=ptn::AbstractNode_strategy)
def test_ptn::abstractnode_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ptn::AbstractNode_strategy)
def test_ptn::abstractnode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractNode_strategy)
@settings(max_examples=50)
def test_abstractnode_instantiation(instance):
    assert isinstance(instance, AbstractNode)

@given(instance=ptn::AbstractTransition_strategy)
@settings(max_examples=50)
def test_ptn::abstracttransition_instantiation(instance):
    assert isinstance(instance, ptn::AbstractTransition)

@given(instance=ptn::AbstractTransition_strategy)
def test_ptn::abstracttransition_guard_type(instance):
    assert isinstance(instance.guard, str)


@given(instance=ptn::AbstractTransition_strategy)
def test_ptn::abstracttransition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=ptn::Place_strategy)
@settings(max_examples=50)
def test_ptn::place_instantiation(instance):
    assert isinstance(instance, ptn::Place)
