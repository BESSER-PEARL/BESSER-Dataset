import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AbstractTransition,
    ptntim101::Transition,
    AbstractNode,
    ptntim101::Token,
    ptntim101::AbstractTransition,
    ptntim101::AbstractNode,
    ptntim101::Place,
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



def test_ptntim101::transition_is_not_abstract():
    assert not inspect.isabstract(ptntim101::Transition)


def test_ptntim101::transition_constructor_exists():
    assert callable(ptntim101::Transition.__init__)


def test_ptntim101::transition_constructor_args():
    sig = inspect.signature(ptntim101::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_ptntim101::transition_has_weight():
    assert hasattr(ptntim101::Transition, "weight")
    descriptor = None
    for klass in ptntim101::Transition.__mro__:
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



def test_ptntim101::token_is_not_abstract():
    assert not inspect.isabstract(ptntim101::Token)


def test_ptntim101::token_constructor_exists():
    assert callable(ptntim101::Token.__init__)


def test_ptntim101::token_constructor_args():
    sig = inspect.signature(ptntim101::Token.__init__)
    params = list(sig.parameters.keys())



def test_ptntim101::abstracttransition_is_not_abstract():
    assert not inspect.isabstract(ptntim101::AbstractTransition)


def test_ptntim101::abstracttransition_constructor_exists():
    assert callable(ptntim101::AbstractTransition.__init__)


def test_ptntim101::abstracttransition_constructor_args():
    sig = inspect.signature(ptntim101::AbstractTransition.__init__)
    params = list(sig.parameters.keys())
    assert "guard" in params, "Missing parameter 'guard'"

def test_ptntim101::abstracttransition_has_guard():
    assert hasattr(ptntim101::AbstractTransition, "guard")
    descriptor = None
    for klass in ptntim101::AbstractTransition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)



def test_ptntim101::abstractnode_is_not_abstract():
    assert not inspect.isabstract(ptntim101::AbstractNode)


def test_ptntim101::abstractnode_constructor_exists():
    assert callable(ptntim101::AbstractNode.__init__)


def test_ptntim101::abstractnode_constructor_args():
    sig = inspect.signature(ptntim101::AbstractNode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "tMax" in params, "Missing parameter 'tMax'"
    assert "tMin" in params, "Missing parameter 'tMin'"

def test_ptntim101::abstractnode_has_name():
    assert hasattr(ptntim101::AbstractNode, "name")
    descriptor = None
    for klass in ptntim101::AbstractNode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ptntim101::abstractnode_has_tMax():
    assert hasattr(ptntim101::AbstractNode, "tMax")
    descriptor = None
    for klass in ptntim101::AbstractNode.__mro__:
        if "tMax" in klass.__dict__:
            descriptor = klass.__dict__["tMax"]
            break
    assert isinstance(descriptor, property)

def test_ptntim101::abstractnode_has_tMin():
    assert hasattr(ptntim101::AbstractNode, "tMin")
    descriptor = None
    for klass in ptntim101::AbstractNode.__mro__:
        if "tMin" in klass.__dict__:
            descriptor = klass.__dict__["tMin"]
            break
    assert isinstance(descriptor, property)



def test_ptntim101::place_is_not_abstract():
    assert not inspect.isabstract(ptntim101::Place)


def test_ptntim101::place_constructor_exists():
    assert callable(ptntim101::Place.__init__)


def test_ptntim101::place_constructor_args():
    sig = inspect.signature(ptntim101::Place.__init__)
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
ptntim101::Transition_strategy = st.builds(
    ptntim101::Transition,
    weight=
        st.integers()
)
AbstractNode_strategy = st.builds(
    AbstractNode,
)
ptntim101::Token_strategy = st.builds(
    ptntim101::Token,
)
ptntim101::AbstractTransition_strategy = st.builds(
    ptntim101::AbstractTransition,
    guard=
        safe_text
)
ptntim101::AbstractNode_strategy = st.builds(
    ptntim101::AbstractNode,
    name=
        safe_text,
    tMax=
        st.integers(),
    tMin=
        st.integers()
)
ptntim101::Place_strategy = st.builds(
    ptntim101::Place,
)

@given(instance=AbstractTransition_strategy)
@settings(max_examples=50)
def test_abstracttransition_instantiation(instance):
    assert isinstance(instance, AbstractTransition)

@given(instance=ptntim101::Transition_strategy)
@settings(max_examples=50)
def test_ptntim101::transition_instantiation(instance):
    assert isinstance(instance, ptntim101::Transition)

@given(instance=ptntim101::Transition_strategy)
def test_ptntim101::transition_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=ptntim101::Transition_strategy)
def test_ptntim101::transition_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=AbstractNode_strategy)
@settings(max_examples=50)
def test_abstractnode_instantiation(instance):
    assert isinstance(instance, AbstractNode)

@given(instance=ptntim101::Token_strategy)
@settings(max_examples=50)
def test_ptntim101::token_instantiation(instance):
    assert isinstance(instance, ptntim101::Token)

@given(instance=ptntim101::AbstractTransition_strategy)
@settings(max_examples=50)
def test_ptntim101::abstracttransition_instantiation(instance):
    assert isinstance(instance, ptntim101::AbstractTransition)

@given(instance=ptntim101::AbstractTransition_strategy)
def test_ptntim101::abstracttransition_guard_type(instance):
    assert isinstance(instance.guard, str)


@given(instance=ptntim101::AbstractTransition_strategy)
def test_ptntim101::abstracttransition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=ptntim101::AbstractNode_strategy)
@settings(max_examples=50)
def test_ptntim101::abstractnode_instantiation(instance):
    assert isinstance(instance, ptntim101::AbstractNode)

@given(instance=ptntim101::AbstractNode_strategy)
def test_ptntim101::abstractnode_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ptntim101::AbstractNode_strategy)
def test_ptntim101::abstractnode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ptntim101::AbstractNode_strategy)
def test_ptntim101::abstractnode_tMax_type(instance):
    assert isinstance(instance.tMax, int)


@given(instance=ptntim101::AbstractNode_strategy)
def test_ptntim101::abstractnode_tMax_setter(instance):
    original = instance.tMax
    instance.tMax = original
    assert instance.tMax == original

@given(instance=ptntim101::AbstractNode_strategy)
def test_ptntim101::abstractnode_tMin_type(instance):
    assert isinstance(instance.tMin, int)


@given(instance=ptntim101::AbstractNode_strategy)
def test_ptntim101::abstractnode_tMin_setter(instance):
    original = instance.tMin
    instance.tMin = original
    assert instance.tMin == original

@given(instance=ptntim101::Place_strategy)
@settings(max_examples=50)
def test_ptntim101::place_instantiation(instance):
    assert isinstance(instance, ptntim101::Place)
