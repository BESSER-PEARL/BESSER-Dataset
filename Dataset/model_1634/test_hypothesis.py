import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbstractTransition,
    ptn103_Transition,
    AbstractNode,
    ptn103_Place,
    ptn103_Token,
    ptn103_AbstractTransition,
    ptn103_AbstractNode,
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



def test_ptn103_transition_is_not_abstract():
    assert not inspect.isabstract(ptn103_Transition)


def test_ptn103_transition_constructor_exists():
    assert callable(ptn103_Transition.__init__)


def test_ptn103_transition_constructor_args():
    sig = inspect.signature(ptn103_Transition.__init__)
    params = list(sig.parameters.keys())



def test_abstractnode_is_not_abstract():
    assert not inspect.isabstract(AbstractNode)


def test_abstractnode_constructor_exists():
    assert callable(AbstractNode.__init__)


def test_abstractnode_constructor_args():
    sig = inspect.signature(AbstractNode.__init__)
    params = list(sig.parameters.keys())



def test_ptn103_place_is_not_abstract():
    assert not inspect.isabstract(ptn103_Place)


def test_ptn103_place_constructor_exists():
    assert callable(ptn103_Place.__init__)


def test_ptn103_place_constructor_args():
    sig = inspect.signature(ptn103_Place.__init__)
    params = list(sig.parameters.keys())



def test_ptn103_token_is_not_abstract():
    assert not inspect.isabstract(ptn103_Token)


def test_ptn103_token_constructor_exists():
    assert callable(ptn103_Token.__init__)


def test_ptn103_token_constructor_args():
    sig = inspect.signature(ptn103_Token.__init__)
    params = list(sig.parameters.keys())



def test_ptn103_abstracttransition_is_not_abstract():
    assert not inspect.isabstract(ptn103_AbstractTransition)


def test_ptn103_abstracttransition_constructor_exists():
    assert callable(ptn103_AbstractTransition.__init__)


def test_ptn103_abstracttransition_constructor_args():
    sig = inspect.signature(ptn103_AbstractTransition.__init__)
    params = list(sig.parameters.keys())
    assert "guard" in params, "Missing parameter 'guard'"

def test_ptn103_abstracttransition_has_guard():
    assert hasattr(ptn103_AbstractTransition, "guard")
    descriptor = None
    for klass in ptn103_AbstractTransition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)



def test_ptn103_abstractnode_is_not_abstract():
    assert not inspect.isabstract(ptn103_AbstractNode)


def test_ptn103_abstractnode_constructor_exists():
    assert callable(ptn103_AbstractNode.__init__)


def test_ptn103_abstractnode_constructor_args():
    sig = inspect.signature(ptn103_AbstractNode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ptn103_abstractnode_has_name():
    assert hasattr(ptn103_AbstractNode, "name")
    descriptor = None
    for klass in ptn103_AbstractNode.__mro__:
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
ptn103_Transition_strategy = st.builds(
    ptn103_Transition,
)
AbstractNode_strategy = st.builds(
    AbstractNode,
)
ptn103_Place_strategy = st.builds(
    ptn103_Place,
)
ptn103_Token_strategy = st.builds(
    ptn103_Token,
)
ptn103_AbstractTransition_strategy = st.builds(
    ptn103_AbstractTransition,
    guard=
        safe_text
)
ptn103_AbstractNode_strategy = st.builds(
    ptn103_AbstractNode,
    name=
        safe_text
)

@given(instance=AbstractTransition_strategy)
@settings(max_examples=50)
def test_abstracttransition_instantiation(instance):
    assert isinstance(instance, AbstractTransition)

@given(instance=ptn103_Transition_strategy)
@settings(max_examples=50)
def test_ptn103_transition_instantiation(instance):
    assert isinstance(instance, ptn103_Transition)

@given(instance=AbstractNode_strategy)
@settings(max_examples=50)
def test_abstractnode_instantiation(instance):
    assert isinstance(instance, AbstractNode)

@given(instance=ptn103_Place_strategy)
@settings(max_examples=50)
def test_ptn103_place_instantiation(instance):
    assert isinstance(instance, ptn103_Place)

@given(instance=ptn103_Token_strategy)
@settings(max_examples=50)
def test_ptn103_token_instantiation(instance):
    assert isinstance(instance, ptn103_Token)

@given(instance=ptn103_AbstractTransition_strategy)
@settings(max_examples=50)
def test_ptn103_abstracttransition_instantiation(instance):
    assert isinstance(instance, ptn103_AbstractTransition)



@given(instance=ptn103_AbstractTransition_strategy)
def test_ptn103_abstracttransition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=ptn103_AbstractNode_strategy)
@settings(max_examples=50)
def test_ptn103_abstractnode_instantiation(instance):
    assert isinstance(instance, ptn103_AbstractNode)



@given(instance=ptn103_AbstractNode_strategy)
def test_ptn103_abstractnode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
