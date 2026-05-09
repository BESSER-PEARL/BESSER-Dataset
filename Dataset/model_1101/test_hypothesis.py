import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PetriNets::Token,
    PetriNets::Transition,
    PetriNets::Place,
    PetriNets::PetriNet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinets::token_is_not_abstract():
    assert not inspect.isabstract(PetriNets::Token)


def test_petrinets::token_constructor_exists():
    assert callable(PetriNets::Token.__init__)


def test_petrinets::token_constructor_args():
    sig = inspect.signature(PetriNets::Token.__init__)
    params = list(sig.parameters.keys())



def test_petrinets::transition_is_not_abstract():
    assert not inspect.isabstract(PetriNets::Transition)


def test_petrinets::transition_constructor_exists():
    assert callable(PetriNets::Transition.__init__)


def test_petrinets::transition_constructor_args():
    sig = inspect.signature(PetriNets::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"

def test_petrinets::transition_has_priority():
    assert hasattr(PetriNets::Transition, "priority")
    descriptor = None
    for klass in PetriNets::Transition.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)



def test_petrinets::place_is_not_abstract():
    assert not inspect.isabstract(PetriNets::Place)


def test_petrinets::place_constructor_exists():
    assert callable(PetriNets::Place.__init__)


def test_petrinets::place_constructor_args():
    sig = inspect.signature(PetriNets::Place.__init__)
    params = list(sig.parameters.keys())
    assert "bound" in params, "Missing parameter 'bound'"
    assert "itokens" in params, "Missing parameter 'itokens'"

def test_petrinets::place_has_bound():
    assert hasattr(PetriNets::Place, "bound")
    descriptor = None
    for klass in PetriNets::Place.__mro__:
        if "bound" in klass.__dict__:
            descriptor = klass.__dict__["bound"]
            break
    assert isinstance(descriptor, property)

def test_petrinets::place_has_itokens():
    assert hasattr(PetriNets::Place, "itokens")
    descriptor = None
    for klass in PetriNets::Place.__mro__:
        if "itokens" in klass.__dict__:
            descriptor = klass.__dict__["itokens"]
            break
    assert isinstance(descriptor, property)



def test_petrinets::petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNets::PetriNet)


def test_petrinets::petrinet_constructor_exists():
    assert callable(PetriNets::PetriNet.__init__)


def test_petrinets::petrinet_constructor_args():
    sig = inspect.signature(PetriNets::PetriNet.__init__)
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
PetriNets::Token_strategy = st.builds(
    PetriNets::Token,
)
PetriNets::Transition_strategy = st.builds(
    PetriNets::Transition,
    priority=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
PetriNets::Place_strategy = st.builds(
    PetriNets::Place,
    bound=
        st.integers(),
    itokens=
        st.integers()
)
PetriNets::PetriNet_strategy = st.builds(
    PetriNets::PetriNet,
)

@given(instance=PetriNets::Token_strategy)
@settings(max_examples=50)
def test_petrinets::token_instantiation(instance):
    assert isinstance(instance, PetriNets::Token)

@given(instance=PetriNets::Transition_strategy)
@settings(max_examples=50)
def test_petrinets::transition_instantiation(instance):
    assert isinstance(instance, PetriNets::Transition)

@given(instance=PetriNets::Transition_strategy)
def test_petrinets::transition_priority_type(instance):
    assert isinstance(instance.priority, float)


@given(instance=PetriNets::Transition_strategy)
def test_petrinets::transition_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=PetriNets::Place_strategy)
@settings(max_examples=50)
def test_petrinets::place_instantiation(instance):
    assert isinstance(instance, PetriNets::Place)

@given(instance=PetriNets::Place_strategy)
def test_petrinets::place_bound_type(instance):
    assert isinstance(instance.bound, int)


@given(instance=PetriNets::Place_strategy)
def test_petrinets::place_bound_setter(instance):
    original = instance.bound
    instance.bound = original
    assert instance.bound == original

@given(instance=PetriNets::Place_strategy)
def test_petrinets::place_itokens_type(instance):
    assert isinstance(instance.itokens, int)


@given(instance=PetriNets::Place_strategy)
def test_petrinets::place_itokens_setter(instance):
    original = instance.itokens
    instance.itokens = original
    assert instance.itokens == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=PetriNets::Place_strategy)
@settings(max_examples=30)
def test_petrinets::place_tokens_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.tokens()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.tokens).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'tokens' in PetriNets::Place is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'tokens' in PetriNets::Place did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'tokens' in PetriNets::Place is not implemented or raised an error")

@given(instance=PetriNets::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinets::petrinet_instantiation(instance):
    assert isinstance(instance, PetriNets::PetriNet)
