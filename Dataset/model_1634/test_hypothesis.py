import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AbstractTransition,
    ptn103::Transition,
    AbstractNode,
    ptn103::Place,
    ptn103::Token,
    ptn103::AbstractTransition,
    ptn103::AbstractNode,
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



def test_ptn103::transition_is_not_abstract():
    assert not inspect.isabstract(ptn103::Transition)


def test_ptn103::transition_constructor_exists():
    assert callable(ptn103::Transition.__init__)


def test_ptn103::transition_constructor_args():
    sig = inspect.signature(ptn103::Transition.__init__)
    params = list(sig.parameters.keys())



def test_abstractnode_is_not_abstract():
    assert not inspect.isabstract(AbstractNode)


def test_abstractnode_constructor_exists():
    assert callable(AbstractNode.__init__)


def test_abstractnode_constructor_args():
    sig = inspect.signature(AbstractNode.__init__)
    params = list(sig.parameters.keys())



def test_ptn103::place_is_not_abstract():
    assert not inspect.isabstract(ptn103::Place)


def test_ptn103::place_constructor_exists():
    assert callable(ptn103::Place.__init__)


def test_ptn103::place_constructor_args():
    sig = inspect.signature(ptn103::Place.__init__)
    params = list(sig.parameters.keys())



def test_ptn103::token_is_not_abstract():
    assert not inspect.isabstract(ptn103::Token)


def test_ptn103::token_constructor_exists():
    assert callable(ptn103::Token.__init__)


def test_ptn103::token_constructor_args():
    sig = inspect.signature(ptn103::Token.__init__)
    params = list(sig.parameters.keys())



def test_ptn103::abstracttransition_is_not_abstract():
    assert not inspect.isabstract(ptn103::AbstractTransition)


def test_ptn103::abstracttransition_constructor_exists():
    assert callable(ptn103::AbstractTransition.__init__)


def test_ptn103::abstracttransition_constructor_args():
    sig = inspect.signature(ptn103::AbstractTransition.__init__)
    params = list(sig.parameters.keys())
    assert "guard" in params, "Missing parameter 'guard'"

def test_ptn103::abstracttransition_has_guard():
    assert hasattr(ptn103::AbstractTransition, "guard")
    descriptor = None
    for klass in ptn103::AbstractTransition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)



def test_ptn103::abstractnode_is_not_abstract():
    assert not inspect.isabstract(ptn103::AbstractNode)


def test_ptn103::abstractnode_constructor_exists():
    assert callable(ptn103::AbstractNode.__init__)


def test_ptn103::abstractnode_constructor_args():
    sig = inspect.signature(ptn103::AbstractNode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ptn103::abstractnode_has_name():
    assert hasattr(ptn103::AbstractNode, "name")
    descriptor = None
    for klass in ptn103::AbstractNode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
AbstractTransition_strategy = st.builds(
    AbstractTransition,
)
ptn103::Transition_strategy = st.builds(
    ptn103::Transition,
)
AbstractNode_strategy = st.builds(
    AbstractNode,
)
ptn103::Place_strategy = st.builds(
    ptn103::Place,
)
ptn103::Token_strategy = st.builds(
    ptn103::Token,
)
ptn103::AbstractTransition_strategy = st.builds(
    ptn103::AbstractTransition,
    guard=
        safe_text
)
ptn103::AbstractNode_strategy = st.builds(
    ptn103::AbstractNode,
    name=
        safe_text
)

@given(instance=AbstractTransition_strategy)
@settings(max_examples=50)
def test_abstracttransition_instantiation(instance):
    assert isinstance(instance, AbstractTransition)

@given(instance=ptn103::Transition_strategy)
@settings(max_examples=50)
def test_ptn103::transition_instantiation(instance):
    assert isinstance(instance, ptn103::Transition)

@given(instance=AbstractNode_strategy)
@settings(max_examples=50)
def test_abstractnode_instantiation(instance):
    assert isinstance(instance, AbstractNode)

@given(instance=ptn103::Place_strategy)
@settings(max_examples=50)
def test_ptn103::place_instantiation(instance):
    assert isinstance(instance, ptn103::Place)

@given(instance=ptn103::Token_strategy)
@settings(max_examples=50)
def test_ptn103::token_instantiation(instance):
    assert isinstance(instance, ptn103::Token)

@given(instance=ptn103::AbstractTransition_strategy)
@settings(max_examples=50)
def test_ptn103::abstracttransition_instantiation(instance):
    assert isinstance(instance, ptn103::AbstractTransition)

@given(instance=ptn103::AbstractTransition_strategy)
def test_ptn103::abstracttransition_guard_type(instance):
    assert isinstance(instance.guard, str)


@given(instance=ptn103::AbstractTransition_strategy)
def test_ptn103::abstracttransition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=ptn103::AbstractNode_strategy)
@settings(max_examples=50)
def test_ptn103::abstractnode_instantiation(instance):
    assert isinstance(instance, ptn103::AbstractNode)

@given(instance=ptn103::AbstractNode_strategy)
def test_ptn103::abstractnode_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ptn103::AbstractNode_strategy)
def test_ptn103::abstractnode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
