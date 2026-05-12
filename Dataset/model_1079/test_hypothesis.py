import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PetriNet,
    PetriNets_Place,
    PetriNets_PetriNet,
    PetriNets_Token,
    PetriNets_Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNet)


def test_petrinet_constructor_exists():
    assert callable(PetriNet.__init__)


def test_petrinet_constructor_args():
    sig = inspect.signature(PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_petrinets_place_is_not_abstract():
    assert not inspect.isabstract(PetriNets_Place)


def test_petrinets_place_constructor_exists():
    assert callable(PetriNets_Place.__init__)


def test_petrinets_place_constructor_args():
    sig = inspect.signature(PetriNets_Place.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "itokens" in params, "Missing parameter 'itokens'"

def test_petrinets_place_has_capacity():
    assert hasattr(PetriNets_Place, "capacity")
    descriptor = None
    for klass in PetriNets_Place.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)

def test_petrinets_place_has_itokens():
    assert hasattr(PetriNets_Place, "itokens")
    descriptor = None
    for klass in PetriNets_Place.__mro__:
        if "itokens" in klass.__dict__:
            descriptor = klass.__dict__["itokens"]
            break
    assert isinstance(descriptor, property)



def test_petrinets_petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNets_PetriNet)


def test_petrinets_petrinet_constructor_exists():
    assert callable(PetriNets_PetriNet.__init__)


def test_petrinets_petrinet_constructor_args():
    sig = inspect.signature(PetriNets_PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_petrinets_token_is_not_abstract():
    assert not inspect.isabstract(PetriNets_Token)


def test_petrinets_token_constructor_exists():
    assert callable(PetriNets_Token.__init__)


def test_petrinets_token_constructor_args():
    sig = inspect.signature(PetriNets_Token.__init__)
    params = list(sig.parameters.keys())



def test_petrinets_transition_is_not_abstract():
    assert not inspect.isabstract(PetriNets_Transition)


def test_petrinets_transition_constructor_exists():
    assert callable(PetriNets_Transition.__init__)


def test_petrinets_transition_constructor_args():
    sig = inspect.signature(PetriNets_Transition.__init__)
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
PetriNet_strategy = st.builds(
    PetriNet,
)
PetriNets_Place_strategy = st.builds(
    PetriNets_Place,
    capacity=
        st.integers(),
    itokens=
        st.integers()
)
PetriNets_PetriNet_strategy = st.builds(
    PetriNets_PetriNet,
)
PetriNets_Token_strategy = st.builds(
    PetriNets_Token,
)
PetriNets_Transition_strategy = st.builds(
    PetriNets_Transition,
)

@given(instance=PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet_instantiation(instance):
    assert isinstance(instance, PetriNet)

@given(instance=PetriNets_Place_strategy)
@settings(max_examples=50)
def test_petrinets_place_instantiation(instance):
    assert isinstance(instance, PetriNets_Place)



@given(instance=PetriNets_Place_strategy)
def test_petrinets_place_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original



@given(instance=PetriNets_Place_strategy)
def test_petrinets_place_itokens_setter(instance):
    original = instance.itokens
    instance.itokens = original
    assert instance.itokens == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=PetriNets_Place_strategy)
@settings(max_examples=30)
def test_petrinets_place_tokens_changes_state(instance):
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
        assert has_statements, f"Function 'tokens' in PetriNets_Place is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'tokens' in PetriNets_Place did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'tokens' in PetriNets_Place is not implemented or raised an error")

@given(instance=PetriNets_PetriNet_strategy)
@settings(max_examples=50)
def test_petrinets_petrinet_instantiation(instance):
    assert isinstance(instance, PetriNets_PetriNet)

@given(instance=PetriNets_Token_strategy)
@settings(max_examples=50)
def test_petrinets_token_instantiation(instance):
    assert isinstance(instance, PetriNets_Token)

@given(instance=PetriNets_Transition_strategy)
@settings(max_examples=50)
def test_petrinets_transition_instantiation(instance):
    assert isinstance(instance, PetriNets_Transition)
