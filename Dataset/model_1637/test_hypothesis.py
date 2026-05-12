import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbstractTransition,
    ptn104_And,
    ptn104_Or,
    ptn104_Token,
    ptn104_AbstractNode,
    AbstractNode,
    ptn104_AbstractTransition,
    ptn104_Place,
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



def test_ptn104_and_is_not_abstract():
    assert not inspect.isabstract(ptn104_And)


def test_ptn104_and_constructor_exists():
    assert callable(ptn104_And.__init__)


def test_ptn104_and_constructor_args():
    sig = inspect.signature(ptn104_And.__init__)
    params = list(sig.parameters.keys())



def test_ptn104_or_is_not_abstract():
    assert not inspect.isabstract(ptn104_Or)


def test_ptn104_or_constructor_exists():
    assert callable(ptn104_Or.__init__)


def test_ptn104_or_constructor_args():
    sig = inspect.signature(ptn104_Or.__init__)
    params = list(sig.parameters.keys())



def test_ptn104_token_is_not_abstract():
    assert not inspect.isabstract(ptn104_Token)


def test_ptn104_token_constructor_exists():
    assert callable(ptn104_Token.__init__)


def test_ptn104_token_constructor_args():
    sig = inspect.signature(ptn104_Token.__init__)
    params = list(sig.parameters.keys())



def test_ptn104_abstractnode_is_not_abstract():
    assert not inspect.isabstract(ptn104_AbstractNode)


def test_ptn104_abstractnode_constructor_exists():
    assert callable(ptn104_AbstractNode.__init__)


def test_ptn104_abstractnode_constructor_args():
    sig = inspect.signature(ptn104_AbstractNode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ptn104_abstractnode_has_name():
    assert hasattr(ptn104_AbstractNode, "name")
    descriptor = None
    for klass in ptn104_AbstractNode.__mro__:
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



def test_ptn104_abstracttransition_is_not_abstract():
    assert not inspect.isabstract(ptn104_AbstractTransition)


def test_ptn104_abstracttransition_constructor_exists():
    assert callable(ptn104_AbstractTransition.__init__)


def test_ptn104_abstracttransition_constructor_args():
    sig = inspect.signature(ptn104_AbstractTransition.__init__)
    params = list(sig.parameters.keys())
    assert "guard" in params, "Missing parameter 'guard'"

def test_ptn104_abstracttransition_has_guard():
    assert hasattr(ptn104_AbstractTransition, "guard")
    descriptor = None
    for klass in ptn104_AbstractTransition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)



def test_ptn104_place_is_not_abstract():
    assert not inspect.isabstract(ptn104_Place)


def test_ptn104_place_constructor_exists():
    assert callable(ptn104_Place.__init__)


def test_ptn104_place_constructor_args():
    sig = inspect.signature(ptn104_Place.__init__)
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
ptn104_And_strategy = st.builds(
    ptn104_And,
)
ptn104_Or_strategy = st.builds(
    ptn104_Or,
)
ptn104_Token_strategy = st.builds(
    ptn104_Token,
)
ptn104_AbstractNode_strategy = st.builds(
    ptn104_AbstractNode,
    name=
        safe_text
)
AbstractNode_strategy = st.builds(
    AbstractNode,
)
ptn104_AbstractTransition_strategy = st.builds(
    ptn104_AbstractTransition,
    guard=
        safe_text
)
ptn104_Place_strategy = st.builds(
    ptn104_Place,
)

@given(instance=AbstractTransition_strategy)
@settings(max_examples=50)
def test_abstracttransition_instantiation(instance):
    assert isinstance(instance, AbstractTransition)

@given(instance=ptn104_And_strategy)
@settings(max_examples=50)
def test_ptn104_and_instantiation(instance):
    assert isinstance(instance, ptn104_And)

@given(instance=ptn104_Or_strategy)
@settings(max_examples=50)
def test_ptn104_or_instantiation(instance):
    assert isinstance(instance, ptn104_Or)

@given(instance=ptn104_Token_strategy)
@settings(max_examples=50)
def test_ptn104_token_instantiation(instance):
    assert isinstance(instance, ptn104_Token)

@given(instance=ptn104_AbstractNode_strategy)
@settings(max_examples=50)
def test_ptn104_abstractnode_instantiation(instance):
    assert isinstance(instance, ptn104_AbstractNode)



@given(instance=ptn104_AbstractNode_strategy)
def test_ptn104_abstractnode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractNode_strategy)
@settings(max_examples=50)
def test_abstractnode_instantiation(instance):
    assert isinstance(instance, AbstractNode)

@given(instance=ptn104_AbstractTransition_strategy)
@settings(max_examples=50)
def test_ptn104_abstracttransition_instantiation(instance):
    assert isinstance(instance, ptn104_AbstractTransition)



@given(instance=ptn104_AbstractTransition_strategy)
def test_ptn104_abstracttransition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=ptn104_Place_strategy)
@settings(max_examples=50)
def test_ptn104_place_instantiation(instance):
    assert isinstance(instance, ptn104_Place)
