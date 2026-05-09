import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AbstractTransition,
    ptn104::And,
    ptn104::Or,
    ptn104::Token,
    ptn104::AbstractNode,
    AbstractNode,
    ptn104::AbstractTransition,
    ptn104::Place,
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



def test_ptn104::and_is_not_abstract():
    assert not inspect.isabstract(ptn104::And)


def test_ptn104::and_constructor_exists():
    assert callable(ptn104::And.__init__)


def test_ptn104::and_constructor_args():
    sig = inspect.signature(ptn104::And.__init__)
    params = list(sig.parameters.keys())



def test_ptn104::or_is_not_abstract():
    assert not inspect.isabstract(ptn104::Or)


def test_ptn104::or_constructor_exists():
    assert callable(ptn104::Or.__init__)


def test_ptn104::or_constructor_args():
    sig = inspect.signature(ptn104::Or.__init__)
    params = list(sig.parameters.keys())



def test_ptn104::token_is_not_abstract():
    assert not inspect.isabstract(ptn104::Token)


def test_ptn104::token_constructor_exists():
    assert callable(ptn104::Token.__init__)


def test_ptn104::token_constructor_args():
    sig = inspect.signature(ptn104::Token.__init__)
    params = list(sig.parameters.keys())



def test_ptn104::abstractnode_is_not_abstract():
    assert not inspect.isabstract(ptn104::AbstractNode)


def test_ptn104::abstractnode_constructor_exists():
    assert callable(ptn104::AbstractNode.__init__)


def test_ptn104::abstractnode_constructor_args():
    sig = inspect.signature(ptn104::AbstractNode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ptn104::abstractnode_has_name():
    assert hasattr(ptn104::AbstractNode, "name")
    descriptor = None
    for klass in ptn104::AbstractNode.__mro__:
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



def test_ptn104::abstracttransition_is_not_abstract():
    assert not inspect.isabstract(ptn104::AbstractTransition)


def test_ptn104::abstracttransition_constructor_exists():
    assert callable(ptn104::AbstractTransition.__init__)


def test_ptn104::abstracttransition_constructor_args():
    sig = inspect.signature(ptn104::AbstractTransition.__init__)
    params = list(sig.parameters.keys())
    assert "guard" in params, "Missing parameter 'guard'"

def test_ptn104::abstracttransition_has_guard():
    assert hasattr(ptn104::AbstractTransition, "guard")
    descriptor = None
    for klass in ptn104::AbstractTransition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)



def test_ptn104::place_is_not_abstract():
    assert not inspect.isabstract(ptn104::Place)


def test_ptn104::place_constructor_exists():
    assert callable(ptn104::Place.__init__)


def test_ptn104::place_constructor_args():
    sig = inspect.signature(ptn104::Place.__init__)
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
ptn104::And_strategy = st.builds(
    ptn104::And,
)
ptn104::Or_strategy = st.builds(
    ptn104::Or,
)
ptn104::Token_strategy = st.builds(
    ptn104::Token,
)
ptn104::AbstractNode_strategy = st.builds(
    ptn104::AbstractNode,
    name=
        safe_text
)
AbstractNode_strategy = st.builds(
    AbstractNode,
)
ptn104::AbstractTransition_strategy = st.builds(
    ptn104::AbstractTransition,
    guard=
        safe_text
)
ptn104::Place_strategy = st.builds(
    ptn104::Place,
)

@given(instance=AbstractTransition_strategy)
@settings(max_examples=50)
def test_abstracttransition_instantiation(instance):
    assert isinstance(instance, AbstractTransition)

@given(instance=ptn104::And_strategy)
@settings(max_examples=50)
def test_ptn104::and_instantiation(instance):
    assert isinstance(instance, ptn104::And)

@given(instance=ptn104::Or_strategy)
@settings(max_examples=50)
def test_ptn104::or_instantiation(instance):
    assert isinstance(instance, ptn104::Or)

@given(instance=ptn104::Token_strategy)
@settings(max_examples=50)
def test_ptn104::token_instantiation(instance):
    assert isinstance(instance, ptn104::Token)

@given(instance=ptn104::AbstractNode_strategy)
@settings(max_examples=50)
def test_ptn104::abstractnode_instantiation(instance):
    assert isinstance(instance, ptn104::AbstractNode)

@given(instance=ptn104::AbstractNode_strategy)
def test_ptn104::abstractnode_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ptn104::AbstractNode_strategy)
def test_ptn104::abstractnode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractNode_strategy)
@settings(max_examples=50)
def test_abstractnode_instantiation(instance):
    assert isinstance(instance, AbstractNode)

@given(instance=ptn104::AbstractTransition_strategy)
@settings(max_examples=50)
def test_ptn104::abstracttransition_instantiation(instance):
    assert isinstance(instance, ptn104::AbstractTransition)

@given(instance=ptn104::AbstractTransition_strategy)
def test_ptn104::abstracttransition_guard_type(instance):
    assert isinstance(instance.guard, str)


@given(instance=ptn104::AbstractTransition_strategy)
def test_ptn104::abstracttransition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=ptn104::Place_strategy)
@settings(max_examples=50)
def test_ptn104::place_instantiation(instance):
    assert isinstance(instance, ptn104::Place)
