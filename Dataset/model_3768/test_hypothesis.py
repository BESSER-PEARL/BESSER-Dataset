import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fsm_Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm_transition_is_not_abstract():
    assert not inspect.isabstract(fsm_Transition)


def test_fsm_transition_constructor_exists():
    assert callable(fsm_Transition.__init__)


def test_fsm_transition_constructor_args():
    sig = inspect.signature(fsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "als" in params, "Missing parameter 'als'"
    assert "ls" in params, "Missing parameter 'ls'"

def test_fsm_transition_has_als():
    assert hasattr(fsm_Transition, "als")
    descriptor = None
    for klass in fsm_Transition.__mro__:
        if "als" in klass.__dict__:
            descriptor = klass.__dict__["als"]
            break
    assert isinstance(descriptor, property)

def test_fsm_transition_has_ls():
    assert hasattr(fsm_Transition, "ls")
    descriptor = None
    for klass in fsm_Transition.__mro__:
        if "ls" in klass.__dict__:
            descriptor = klass.__dict__["ls"]
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
fsm_Transition_strategy = st.builds(
    fsm_Transition,
    als=
        safe_text,
    ls=
        safe_text
)

@given(instance=fsm_Transition_strategy)
@settings(max_examples=50)
def test_fsm_transition_instantiation(instance):
    assert isinstance(instance, fsm_Transition)



@given(instance=fsm_Transition_strategy)
def test_fsm_transition_als_setter(instance):
    original = instance.als
    instance.als = original
    assert instance.als == original



@given(instance=fsm_Transition_strategy)
def test_fsm_transition_ls_setter(instance):
    original = instance.ls
    instance.ls = original
    assert instance.ls == original
